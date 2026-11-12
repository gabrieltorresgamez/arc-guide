"""Build the site: diagrams, Starlight pages, .md versions, llms.txt files, checks."""
import html
import json
import os
import re
from pathlib import Path
import shutil
import subprocess
import sys

import yaml

from pipeline import common as c

SITE = c.ROOT / "site"
DOCS = SITE / "src" / "content" / "docs"
PUB = SITE / "public"
FENCE = {"plantuml": "plantuml", "c4plantuml": "plantuml", "mermaid": "mermaid", "bpmn": "xml"}

REVIEW_LLMS = """# Architecture review checklist (arc42)

> Instructions and checks for reviewing a software architecture document that follows the arc42 template. Read this file first. Fetch linked pages only when you need more detail.

## How to review

1. Read the user's architecture document completely.
2. Fetch the checklist page of each arc42 section (links below). Each page lists the checks for one section.
3. If the document does not follow arc42, first map its content to the arc42 sections and say so.
4. For each arc42 section, apply every check. Result per check: OK, ISSUE, MISSING (information is absent), or N/A (give a reason).
5. Fetch a linked concept page only when a result is ISSUE or unclear, or the user asks why.
6. Report per section: check, result, evidence (quote or location in the user's document), suggested fix, and the concept link for each ISSUE.
7. End with the three most important improvements, in priority order.
8. Do not invent requirements that are not in the checklist or in the linked pages.

## Pages

SECTION_LINKS- [Guides](SITE_URL/guides/llms.txt): step-by-step help to create missing parts
"""


def llms_txt(h1, summary, sections, intro=""):
    """sections = [(heading, [(title, url, text)])] -> llms.txt text."""
    out = [f"# {h1}", "", f"> {summary}", ""]
    if intro:
        out += [intro, ""]
    for head, items in sections:
        out += [f"## {head}", ""] + [f"- [{t}]({u}): {d}" for t, u, d in items] + [""]
    return "\n".join(out).rstrip() + "\n"


def page_head(md_url, llms_url):
    return [{"tag": "link", "attrs": {"rel": "alternate", "type": "text/markdown", "href": md_url}},
            {"tag": "link", "attrs": {"rel": "describedby", "href": llms_url}}]


def write_page(url_path, title, desc, body, md_body, llms_url, order=None):
    """url_path like 'concepts/cat/slug' (no slashes at the ends). Writes the Starlight page and the .md version."""
    fm = {"title": title, "description": desc, "head": page_head(f"/{url_path}.md", llms_url)}
    if not re.search(r"^## ", body, re.M):  # no sections: the "On this page" box would only say "Overview"
        fm["tableOfContents"] = False
    if order is not None:
        fm["sidebar"] = {"order": order}
    c.write_atomic(DOCS / f"{url_path}.md", "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000) + "---\n\n" + body + "\n")
    c.write_atomic(PUB / f"{url_path}.md", md_body.rstrip() + "\n")


def load_articles():
    arts = []
    for f in sorted((c.CONTENT / "concepts").glob("*/*/index.md")):
        fm, body = c.split_front(f.read_text())
        fm["_dir"], fm["_body"] = f.parent, body
        arts.append(fm)
    return arts


def render_diagrams():
    """Render every diagram file in content/ with Kroki; copy the source next to the SVG. Returns count and failures."""
    ok, bad = 0, []
    for f in sorted(c.CONTENT.rglob("*")):
        if f.is_file() and f.suffix not in (".md", ".json"):
            rel = f.relative_to(c.CONTENT)
            try:
                svg = c.kroki_render(c.kroki_lang(f.name), f.read_text())
            except (c.KrokiError, ValueError, OSError) as e:
                bad.append(f"{rel}: {str(e)[:200]}")
                continue
            c.write_atomic(PUB / "diagrams" / f"{rel}.svg", svg)
            c.write_atomic(PUB / "diagrams" / rel, f.read_bytes())
            ok += 1
    return ok, bad


def art_urls(a):
    base = f"concepts/{a['category']}/{a['slug']}"
    return f"/{base}/", f"/{base}.md"


def diagram_img(rel, caption):
    """<img> with the size of the rendered SVG, so the page does not shift when the image loads."""
    svg = PUB / "diagrams" / f"{rel}.svg"
    m = re.search(rb'<svg[^>]*?\swidth="([\d.]+)(?:px)?"[^>]*?\sheight="([\d.]+)(?:px)?"', svg.read_bytes()) if svg.exists() else None
    size = f' width="{round(float(m[1]))}" height="{round(float(m[2]))}"' if m else ""
    return f'<img src="/diagrams/{rel}.svg" alt="{html.escape(caption)}"{size} loading="lazy" decoding="async">'


def diagram_blocks(a, md):
    out = []
    for d in a.get("diagrams", []):
        f = a["_dir"] / d["file"]
        rel = f.relative_to(c.CONTENT).as_posix()
        lang = c.kroki_lang(d["file"])
        src = f.read_text().rstrip()
        if md:
            if lang == "bpmn":
                out.append(f"BPMN diagram: [{d['caption']}]({c.SITE_URL}/diagrams/{rel})")
            else:
                out.append(f"{d['caption']}\n\n```{FENCE[lang]}\n{src}\n```")
        else:
            out.append(f"{diagram_img(rel, d['caption'])}\n\n<details><summary>Diagram source</summary>\n\n```{FENCE[lang]}\n{src}\n```\n\n</details>")
    return "\n\n".join(out)


def build_article(a, titles, cats):
    url, md_url = art_urls(a)
    related = [s for s in a.get("related", []) if s in titles]
    checks = a.get("checks", [])
    srcs = a.get("sources", [])
    def tail(md):
        parts = []
        if checks:
            parts.append("## Checks\n\n" + "\n".join(f"- {x}" for x in checks))
        if related:
            link = (lambda s: f"[{titles[s][0]}]({c.SITE_URL}{titles[s][1][1]})") if md else (lambda s: f"[{titles[s][0]}]({titles[s][1][0]})")
            parts.append("## Related\n\n" + "\n".join(f"- {link(s)}" for s in related))
        parts.append("## Sources\n\n" + "\n".join(f"- [{s['title']}]({s['url']}) — {s['site']}, accessed {s['accessed']}" for s in srcs))
        return "\n\n".join(parts)
    html_body = f":::note[In short]\n{a['summary']}\n:::\n\n{a['_body'].strip()}\n\n{diagram_blocks(a, False)}\n\n{tail(False)}"
    md_body = f"# {a['title']}\n\n**In short:** {a['summary']}\n\n{a['_body'].strip()}\n\n{diagram_blocks(a, True)}\n\n{tail(True)}"
    write_page(f"concepts/{a['category']}/{a['slug']}", a["title"], a["summary"], html_body, md_body, f"/concepts/{a['category']}/llms.txt")


def rewrite_links(text, titles, md):
    def sub(m):
        s = m.group(2)
        if s not in titles:
            raise SystemExit(f"guide links to unknown concept '{s}'")
        return f"[{m.group(1)}]({c.SITE_URL + titles[s][1][1] if md else titles[s][1][0]})"
    return re.sub(r"\[([^\]]+)\]\(concept:([^)]+)\)", sub, text)


def main(argv=None):
    for d in (DOCS, PUB / "diagrams", PUB / "concepts", PUB / "guides", PUB / "review"):  # generated files only
        shutil.rmtree(d, ignore_errors=True)
    for f in (PUB / "llms.txt", PUB / "glossary.md", PUB / "index.md", PUB / "privacy.md", PUB / "robots.txt"):
        f.unlink(missing_ok=True)
    n_diag, bad_diag = render_diagrams()
    cats = {x["id"]: x for x in c.TAXONOMY["categories"]}
    arts = load_articles()
    titles = {a["slug"]: (a["title"], art_urls(a)) for a in arts}
    for a in arts:
        build_article(a, titles, cats)
    # category llms.txt
    by_cat = {}
    for a in arts:
        by_cat.setdefault(a["category"], []).append(a)
    subs = json.loads((c.CONTENT / "subgroups.json").read_text()) if (c.CONTENT / "subgroups.json").exists() else {}

    def groups(cat):
        """[(title, [articles])] by subgroup of taxonomy.yaml, in its order; one group 'Concepts' if the category has none."""
        items = sorted(by_cat[cat], key=lambda a: a["title"].lower())
        sg = cats[cat].get("subcategories")
        if not sg:
            return [("Concepts", items)]
        out = [(x["title"], [a for a in items if subs.get(a["slug"]) == x["id"]]) for x in sg]
        rest = [a for a in items if subs.get(a["slug"]) not in {x["id"] for x in sg}]
        return [g for g in out + [("More concepts", rest)] if g[1]]

    for cat in by_cat:
        txt = llms_txt(cats[cat]["title"], cats[cat]["scope"], [(t, [(a["title"], c.SITE_URL + art_urls(a)[1], a["summary"]) for a in items]) for t, items in groups(cat)])
        c.write_atomic(PUB / "concepts" / cat / "llms.txt", txt)
    # guides
    gl = []
    for i, g in enumerate(c.TAXONOMY["guides"]):
        f = c.CONTENT / "guides" / g["id"] / "index.md"
        if not f.exists():
            continue
        fm, body = c.split_front(f.read_text())
        write_page(f"guides/{g['id']}", g["title"], g["goal"],
                   rewrite_links(body, titles, False), f"# {g['title']}\n\n" + rewrite_links(body, titles, True), "/guides/llms.txt", i)
        gl.append((g["title"], f"{c.SITE_URL}/guides/{g['id']}.md", g["goal"]))
    if gl:
        c.write_atomic(PUB / "guides" / "llms.txt", llms_txt("Guides", "Step-by-step guides for starting a software architecture.", [("Guides", gl)]))
    # arc42 review pages: one page per section, at most MAX_CHECKS checks per article (the
    # full list had 5463 checks). Check j of an article goes to section arc42[j % len(arc42)] so no check repeats.
    MAX_CHECKS = 3  # ponytail: the first three checks, not the most important ones; rank them if reviews miss things
    rows = {s["n"]: [] for s in c.TAXONOMY["arc42"]}
    for a in sorted(arts, key=lambda a: (a["category"], a["title"])):
        secs = [n for n in a.get("arc42", []) if n in rows]
        for j, ch in enumerate(a.get("checks", [])[:MAX_CHECKS] if secs else []):
            if ch not in {x[0] for x in rows[secs[j % len(secs)]]}:
                rows[secs[j % len(secs)]].append((ch, a))
    def review(s, md):
        link = (lambda a: f"[{a['title']}]({c.SITE_URL}{art_urls(a)[1]})") if md else (lambda a: f"[{a['title']}]({art_urls(a)[0]})")
        return "\n".join([f"{s['scope']}\n"] + ([f"- {ch} → {link(a)}" for ch, a in rows[s["n"]]] or ["_No checks yet._"]))
    index = []
    for s in c.TAXONOMY["arc42"]:
        name = f"arc42-{s['n']:02d}"
        title = f"arc42 section {s['n']}: {s['title']}"
        desc = f"Checks for section {s['n']} ({s['title']}) of an arc42 document."
        write_page(f"review/{name}", title, desc, review(s, False), f"# {title}\n\n{desc}\n\n" + review(s, True), "/review/llms.txt")
        index.append((s, name))
    idx_html = "\n".join(f"- [{s['n']}. {s['title']}](/review/{n}/)" for s, n in index)
    idx_md = "\n".join(f"- [{s['n']}. {s['title']}]({c.SITE_URL}/review/{n}.md)" for s, n in index)
    desc = "Checks for reviewing an architecture document, one page per arc42 section."
    write_page("review/arc42", "arc42 checklist", desc, idx_html, "# arc42 checklist\n\n" + desc + "\n\n" + idx_md, "/review/llms.txt")
    c.write_atomic(PUB / "review" / "llms.txt", REVIEW_LLMS.replace("SECTION_LINKS", "".join(
        f"- [{s['n']}. {s['title']}](SITE_URL/review/arc42-{s['n']:02d}.md): {s['scope']}\n" for s in c.TAXONOMY["arc42"])).replace("SITE_URL", c.SITE_URL))
    # glossary
    gloss = sorted(arts, key=lambda a: a["title"].lower())
    write_page("glossary", "Glossary", "All concepts of this knowledge base, A to Z.",
               "\n".join(f"- [{a['title']}]({art_urls(a)[0]}): {a['summary']}" for a in gloss),
               "# Glossary\n\n" + "\n".join(f"- [{a['title']}]({c.SITE_URL}{art_urls(a)[1]}): {a['summary']}" for a in gloss), "/llms.txt")
    # home (hand-written content/index.md)
    home = (c.CONTENT / "index.md").read_text() if (c.CONTENT / "index.md").exists() else "# Software Architecture Guide\n"
    hfm, hbody = c.split_front(home)
    hbody = re.sub(r"^# .*\n+", "", hbody)
    c.write_atomic(DOCS / "index.md", "---\n" + yaml.safe_dump({"title": hfm.get("title", "Software Architecture Guide"), "description": hfm.get("description", "Software architecture explained for non-architects."),
                   "head": page_head("/index.md", "/llms.txt"), "tableOfContents": False}, sort_keys=False, width=1000) + "---\n\n" + hbody)
    md_home = re.sub(r"\]\((/[^)#]*?)/?\)", lambda m: f"]({c.SITE_URL}{m.group(1)}{'' if m.group(1).endswith(('.txt', '.md')) else '.md'})", hbody)
    c.write_atomic(PUB / "index.md", "# Software Architecture Guide\n\n" + md_home)
    # privacy notice (hand-written content/privacy.md, linked from the footer) and robots.txt
    pfm, pbody = c.split_front((c.CONTENT / "privacy.md").read_text())
    write_page("privacy", pfm["title"], pfm["description"], pbody.strip(), f"# {pfm['title']}\n\n{pbody.strip()}", "/llms.txt")
    c.write_atomic(PUB / "robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {c.SITE_URL}/sitemap-index.xml\n")
    # root llms.txt
    summary = "Software architecture explained in plain language: concept articles, guides for beginners, and an arc42 review checklist. Every page is written from public sources listed on the page."
    root = [("Start here", [("Guides", f"{c.SITE_URL}/guides/llms.txt", "How to start the architecture of a project, step by step")] if gl else []),
            ("Review", [("arc42 review checklist", f"{c.SITE_URL}/review/llms.txt", "How to review an arc42 document with the checks of this site")]),
            ("Concepts", [(cats[k]["title"], f"{c.SITE_URL}/concepts/{k}/llms.txt", cats[k]["scope"]) for k in cats if k in by_cat]),
            ("Glossary", [("Glossary", f"{c.SITE_URL}/glossary.md", "All concepts A to Z with a one-sentence summary")])]
    c.write_atomic(PUB / "llms.txt", llms_txt("Software Architecture Guide", summary, [s for s in root if s[1]],
                                              "Read this file, then fetch only the linked llms.txt files and .md pages you need."))
    # sidebar (read by site/astro.config.mjs)
    sb = []
    if gl:
        sb.append({"label": "Start here", "items": [{"autogenerate": {"directory": "guides"}}]})
    def cat_items(k):
        if not cats[k].get("subcategories"):
            return [{"autogenerate": {"directory": f"concepts/{k}"}}]
        return [{"label": t, "collapsed": True, "items": [{"slug": f"concepts/{k}/{a['slug']}"} for a in items]} for t, items in groups(k)]
    sb.append({"label": "Concepts", "items": [{"label": cats[k]["title"], "collapsed": True, "items": cat_items(k)} for k in cats if k in by_cat]})
    sb += [{"label": "Review", "slug": "review/arc42"}, {"label": "Glossary", "slug": "glossary"}]
    c.write_json(SITE / "sidebar.json", sb)
    rep = [f"articles: {len(arts)}; guides: {len(gl)}; diagrams rendered: {n_diag}; failed: {len(bad_diag)}"] + [f"- FAIL diagram {b}" for b in bad_diag]
    fails = [f"diagram {b}" for b in bad_diag]
    r = subprocess.run(["npm", "run", "build"], cwd=SITE, capture_output=True, text=True, env=os.environ)
    if r.returncode:
        fails.append("npm run build failed:\n" + (r.stdout + r.stderr)[-2000:])
    else:
        fails += check_dist(arts)
    rep += [f"- FAIL {f}" for f in fails] or ["- all checks passed"]
    c.write_report("build", rep)
    print("\n".join(rep))
    if fails:
        sys.exit(1)


def check_dist(arts):
    dist = SITE / "dist"
    fails = []
    for h in dist.rglob("*.html"):
        if h.name == "404.html":
            continue
        tags = re.findall(r"<link\b[^>]*>", h.read_text(errors="replace"))
        if not any('rel="alternate"' in t and "text/markdown" in t for t in tags):
            fails.append(f"{h.relative_to(dist)}: missing rel=alternate text/markdown")
        if not any('rel="describedby"' in t for t in tags):
            fails.append(f"{h.relative_to(dist)}: missing rel=describedby")
    def exists(u):
        u = u.split("#")[0].split("?")[0]
        if u.startswith(c.SITE_URL):
            u = u[len(c.SITE_URL):] or "/"
        elif not u.startswith("/"):
            return True  # external link
        p = dist / u.lstrip("/")
        return p.is_file() or (p / "index.html").is_file()
    for f in list(dist.rglob("llms.txt")) + [p for p in dist.rglob("*.md")]:
        for _, u in re.findall(r"\[([^\]]*)\]\(([^)\s]+)\)", f.read_text()):
            if not exists(u):
                fails.append(f"{f.relative_to(dist)}: broken link {u}")
    for f in dist.rglob("*.md"):
        t = f.read_text(errors="replace")
        if re.search(FACT_ID, t):  # fact ids like (f8) must never reach the text
            fails.append(f"fact id in {f.relative_to(dist)}")
        if m := re.search(FACT_TALK, t):  # the writer talking about its input
            fails.append(f"meta-text '{m[0]}' in {f.relative_to(dist)}")
    return fails


FACT_ID = r"\(f\d+(?:[,;] ?f\d+)*\)"
FACT_TALK = (r"(?i)\b(?:verified|supplied|supporting|available) facts\b|\bthese facts\b|\b(?:in|from) the facts\b"
             r"|\bthe facts (?:here|available|given|above|for|do|don't|say|describe|cover|give|show|support|also|only|accept|favor)\b")


if __name__ == "__main__":
    main()
