"""Claim check: compare an article with the public pages in its `sources:` list. Reports only; never edits content/.

Usage: uv run python -m pipeline.claimcheck [SLUG | guides/ID ...]     (needs `claude` logged in; uses your subscription)
Without slugs it checks the pages and guides changed since HEAD. A guide has no sources: it is checked against the
concept pages and web pages it links (the concept pages are claim-checked against their own sources). Exit code 1 if any finding is `unsupported` or `contradicted`;
`stretched` findings are only reported.
Report: build/reports/claimcheck.md
"""
import hashlib
import html
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

from pipeline import common as c
from pipeline.linkcheck import blocked

MODEL = os.environ.get("CLAIMCHECK_MODEL", "sonnet")
PAGE_CHARS = int(os.environ.get("CLAIMCHECK_PAGE_CHARS", 7000))  # minimum share per source; the total budget is split evenly, so few sources are read in full
TOTAL_CHARS = int(os.environ.get("CLAIMCHECK_TOTAL_CHARS", 520000))  # ponytail: sources past this budget are skipped and listed in the report
SCHEMA = {"type": "object", "required": ["problems"], "properties": {"problems": {"type": "array", "items": {
    "type": "object", "required": ["quote", "kind", "note"], "properties": {
        "quote": {"type": "string"}, "kind": {"type": "string", "enum": ["unsupported", "contradicted", "stretched"]},
        "note": {"type": "string"}}}}}}


def page_text(url):
    """Plain text of a public page, cached in build/web. Returns None if it cannot be read."""
    cache = c.BUILD / "web" / f"{hashlib.sha256(url.encode()).hexdigest()}.txt"
    if cache.exists():
        return cache.read_text()
    try:
        raw = c.fetch_public(url, ua="arc-guide-claimcheck/1.0 (non-commercial)")
    except Exception:
        return None
    if blocked(raw):  # a captcha page would be cached and read as the source forever
        return None
    raw = re.sub(r"(?is)<(script|style)\b.*?</\1\s*>", " ", raw)
    text = re.sub(r"\s+", " ", html.unescape(re.sub(r"(?s)<[^>]*>", " ", raw))).strip()
    c.write_atomic(cache, text)
    return text


def ask(prompt):
    """One `claude -p` call with no tools; returns the structured output dict."""
    env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}  # use the subscription, not an API key
    cmd = ["claude", "-p", "--model", MODEL, "--tools", "", "--output-format", "json",
           "--json-schema", json.dumps(SCHEMA, separators=(",", ":")), "--no-session-persistence",
           "--strict-mcp-config", "--setting-sources", "project", "--disable-slash-commands"]
    res = json.loads(subprocess.run(cmd, input=prompt, env=env, capture_output=True, text=True, timeout=900, cwd="/tmp").stdout)
    if res.get("is_error") or not isinstance(res.get("structured_output"), dict):
        raise RuntimeError(str(res.get("result", "no structured_output"))[:300])
    return res["structured_output"]


def concept_pages(body):
    """Text of the concept pages a guide links, in link order."""
    files = {f.parent.name: f for f in (c.CONTENT / "concepts").glob("*/*/index.md")}
    out = []
    for slug in dict.fromkeys(re.findall(r"\(concept:([^)#]+)\)", body)):
        if slug in files:
            meta, text = c.split_front(files[slug].read_text())
            out.append(f"=== PAGE: {meta['title']} ===\n{meta.get('summary', '')}\n{text}")
    return out


def check(path):
    meta, body = c.split_front(path.read_text())
    pages, skipped, used = [], [], 0
    srcs = meta.get("sources", [])
    if path.parent.parent.name == "guides":  # a guide's sources are the pages it links
        pages = concept_pages(body)
        used = sum(map(len, pages))
        srcs = [{"url": u} for u in dict.fromkeys(re.findall(r"\]\((https?://[^)\s]+)\)", body))]
    per = max(PAGE_CHARS, (TOTAL_CHARS - used) // max(1, len(srcs)))  # a fixed 20k cut made claims from later in long sources look unsupported
    for s in srcs:
        text = page_text(s["url"])
        if text is None or used + min(len(text), per) > TOTAL_CHARS:
            skipped.append(s["url"])
            continue
        used += min(len(text), per)
        if len(text) > per:
            skipped.append(f"{s['url']} (only the first {per} of {len(text)} characters)")
        pages.append(f"=== URL: {s['url']} ===\n{text[:per]}")
    prompt = (c.ROOT / "prompts" / "claimcheck.md").read_text().replace("{pages}", "\n\n".join(pages)).replace("{article}", body)
    return ask(prompt)["problems"], skipped


def changed_slugs():
    out = subprocess.run(["git", "diff", "--name-only", "HEAD", "--", "content/concepts", "content/guides"], capture_output=True, text=True, cwd=c.ROOT).stdout
    return sorted({("guides/" if p.startswith("content/guides/") else "") + Path(p).parent.name
                   for p in out.splitlines() if p.endswith("index.md") and (c.ROOT / p).exists()})


def main(slugs):
    files = {f.parent.name: f for f in (c.CONTENT / "concepts").glob("*/*/index.md")}
    files |= {f"guides/{f.parent.name}": f for f in (c.CONTENT / "guides").glob("*/index.md")}
    slugs = slugs or changed_slugs()
    rep, blocking = [], 0
    for slug in slugs:
        if slug not in files:
            sys.exit(f"unknown slug: {slug}")
        try:
            probs, skipped = check(files[slug])
        except Exception as e:  # an outage or usage limit should not lose the rest of the batch
            print(f"[{slugs.index(slug) + 1}/{len(slugs)}] {slug}: NOT CHECKED ({str(e)[:120]})", flush=True)
            rep += [f"### `{slug}`", f"- **not checked**: {str(e)[:200]}", ""]
            blocking += 1
            continue
        blocking += sum(p["kind"] in ("unsupported", "contradicted") for p in probs)
        note = f", {len(skipped)} sources NOT READ in full (findings may be false; raise CLAIMCHECK_TOTAL_CHARS or check the page on its own)" if skipped else ""
        print(f"[{slugs.index(slug) + 1}/{len(slugs)}] {slug}: {len(probs)} problems{note}", flush=True)
        rep += [f"### `{slug}`"] + [f"- **{p['kind']}**: “{p['quote']}” — {p['note']}" for p in probs]
        rep += [f"- _not read in full (unreadable, over budget or cut):_ {u}" for u in skipped] + [""]
    c.write_report(os.environ.get("CLAIMCHECK_STAGE", "claimcheck"), rep)  # CLAIMCHECK_STAGE lets parallel runs write separate reports
    if blocking:
        sys.exit(f"{blocking} unsupported, contradicted or unchecked, see build/reports/claimcheck.md")


if __name__ == "__main__":
    main(sys.argv[1:])
