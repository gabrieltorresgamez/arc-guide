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
6. Report per section: check, result, severity (for ISSUE and MISSING), evidence (quote or location in the user's document), suggested fix, and the concept link for each ISSUE.
7. End with the three most important improvements, highest severity first.

Severity of an ISSUE or MISSING result:
- HIGH: the gap concerns a top quality goal, a fixed constraint, or an architecturally significant decision (one that is costly or risky to change).
- MEDIUM: a stakeholder cannot use the section for its purpose, for example a diagram without a legend or a decision without a reason.
- LOW: form and completeness details that do not block any reader.
8. Do not invent requirements that are not in the checklist or in the linked pages.

## Example of a worked review

Document: a short architecture description of an online shop. Section 1 (Introduction and goals).

- Check: "Section 1.2 lists the top three quality goals, at most five, ordered by priority." Result: ISSUE. Severity: HIGH. Evidence: "Quality goals: fast, secure, cheap, scalable, usable, reliable, maintainable". Seven goals are listed, with no priority. Fix: rank them and keep the top three, at most five. Concept: Quality Attribute Prioritization.
- Check: "Stakeholders are listed with their expectations." Result: MISSING. Severity: MEDIUM. Evidence: the document has no stakeholder list. Fix: add a table of roles and what each expects.
- Check: "The business goals are stated." Result: OK. Evidence: "The shop must double its online revenue within a year."
- Check: "Regulatory goals are described." Result: N/A. Reason: the document states that the shop sells no regulated goods.

Top three improvements, in priority order: 1. rank the quality goals, 2. add the stakeholder table, 3. add a measure to each quality goal.

## Pages

SECTION_LINKS- [Guides](SITE_URL/guides/llms.txt): step-by-step help to create missing parts
"""


MAX_CHECKS, MAX_PER_SECTION = 3, 30


def select_checks(arts, sections, cap=MAX_PER_SECTION):
    """{section: [(check, article)]}: at most `cap` checks per section. Articles whose first arc42 section is this one come
    first, then first checks before later ones. A check that shares 80% of its words with a kept one is dropped."""
    cand = {n: [] for n in sections}
    for a in arts:
        secs = [n for n in a.get("arc42", []) if n in cand]
        for j, ch in enumerate(a.get("checks", [])[:MAX_CHECKS] if secs else []):
            n = secs[j % len(secs)]
            cand[n].append(((n != secs[0], j, a["category"], a["title"]), ch, a))
    words = lambda t: set(re.findall(r"[a-z0-9]+", t.lower()))
    out = {}
    for n, items in cand.items():
        kept = []
        for _, ch, a in sorted(items, key=lambda x: x[0]):
            w = words(ch)
            if any(len(w & words(k)) / max(1, len(w | words(k))) > 0.8 for k, _ in kept):
                continue
            kept.append((ch, a))
            if len(kept) >= cap:
                break
        out[n] = kept
    return out


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


def link_see(text, titles, md, me):
    """Turn the page titles named after "See ..." into links, so 'See the article Component View' is a link.
    Only exact titles inside a "See" clause (up to the end of the sentence or a closing parenthesis) are linked."""
    by_title = {t: s for s, (t, _) in titles.items() if s != me}
    if not by_title:
        return text
    names = "|".join(re.escape(t) for t in sorted(by_title, key=len, reverse=True))
    name_re = re.compile(r"(?<![\w\[])(\*{0,2})(\"?)(" + names + r")(\"?)(\*{0,2})(?![\w\]])")
    def clause(m):
        head, rest = m.group(1), m.group(2)
        if "](" in rest:
            return m.group(0)
        def one(n):
            slug = by_title[n.group(3)]
            href = (c.SITE_URL + titles[slug][1][1]) if md else titles[slug][1][0]
            return f"{n.group(1)}{n.group(2)}[{n.group(3)}]({href}){n.group(4)}{n.group(5)}"
        return head + name_re.sub(one, rest)
    out, fence = [], False
    for line in text.split("\n"):
        if line.startswith("```"):
            fence = not fence
        out.append(line if fence else re.sub(r"(\b[Ss]ee(?: also)?(?: the)?(?: articles?)?(?: on)? )((?:[^.\n)\"]|\.(?=\d)|\"[^\"\n]*\")*)", clause, line))
    return "\n".join(out)


def cite(text, srcs, md):
    """[src:N] in an article becomes a small link to its Nth source, numbered like the Sources list."""
    return re.sub(r"\s?\[src:(\d+)\]", lambda m: f" [[{m[1]}]]({srcs[int(m[1]) - 1]['url']})" if md else f"<sup>[{m[1]}]({srcs[int(m[1]) - 1]['url']})</sup>", text)


def build_article(a, titles, cats):
    url, md_url = art_urls(a)
    related = [s for s in a.get("related", []) if s in titles]
    checks = a.get("checks", [])
    srcs = a.get("sources", [])
    def tail(md):
        parts = []
        if checks:
            parts.append("## Checks\n\n" + "\n".join(f"- {x}" for x in checks))
        if a["slug"] in SECTION_OF:
            sec = next(x for x in c.TAXONOMY["arc42"] if x["n"] == SECTION_OF[a["slug"]])
            parts.append(f"## Review checklist\n\nTo check your own document, use the [{review_title(sec)}]({c.SITE_URL + '/review/' + review_slug(sec) + '.md' if md else '/review/' + review_slug(sec) + '/'}).")
        if related:
            link = (lambda s: f"[{titles[s][0]}]({c.SITE_URL}{titles[s][1][1]})") if md else (lambda s: f"[{titles[s][0]}]({titles[s][1][0]})")
            parts.append("## Related\n\n" + "\n".join(f"- {link(s)}" for s in related))
        parts.append("## Sources\n\n" + "\n".join(f"{i}. [{s['title']}]({s['url']}) — {s['site']}, accessed {s['accessed']}" for i, s in enumerate(srcs or [], 1)))
        return "\n\n".join(parts)
    html_body = f":::note[In short]\n{a['summary']}\n:::\n\n{link_see(cite(a['_body'].strip(), srcs, False), titles, False, a['slug'])}\n\n{diagram_blocks(a, False)}\n\n{tail(False)}"
    md_body = f"# {a['title']}\n\n**In short:** {a['summary']}\n\n{link_see(cite(a['_body'].strip(), srcs, True), titles, True, a['slug'])}\n\n{diagram_blocks(a, True)}\n\n{tail(True)}"
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
        items = sorted(by_cat[cat], key=lambda a: (a.get("order", 10**6), a["title"].lower()))  # `order:` in the front matter, then A to Z
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
    # arc42 review pages: one page per section. Check j of an article goes to section arc42[j % len(arc42)]; each section
    # keeps at most MAX_PER_SECTION checks, primary-section articles first, near-duplicates removed.
    rows = select_checks(arts, [x["n"] for x in c.TAXONOMY["arc42"]])
    def review(s, md):
        ex = titles[ARC42_PAGE[s["n"]]]
        intro = f"Explanation of this section: [{ex[0]}]({c.SITE_URL + ex[1][1] if md else ex[1][0]}).\n\n"
        link = (lambda a: f"[{a['title']}]({c.SITE_URL}{art_urls(a)[1]})") if md else (lambda a: f"[{a['title']}]({art_urls(a)[0]})")
        return intro + "\n".join([f"{s['scope']}\n"] + ([f"- {ch} → {link(a)}" for ch, a in rows[s["n"]]] or ["_No checks yet._"]))
    index = []
    for s in c.TAXONOMY["arc42"]:
        name = review_slug(s)
        title = review_title(s)
        desc = f"Checks for section {s['n']} ({s['title']}) of an arc42 document. This is a checklist, not an explanation."
        write_page(f"review/{name}", title, desc, review(s, False), f"# {title}\n\n{desc}\n\n" + review(s, True), "/review/llms.txt")
        index.append((s, name))
    idx_html = "\n".join(f"- [{s['n']}. {s['title']}](/review/{n}/)" for s, n in index)
    idx_md = "\n".join(f"- [{s['n']}. {s['title']}]({c.SITE_URL}/review/{n}.md)" for s, n in index)
    desc = "Checks for reviewing an architecture document, one page per arc42 section."
    write_page("review/checklists", "arc42 review checklists", desc, idx_html, "# arc42 review checklists\n\n" + desc + "\n\n" + idx_md, "/review/llms.txt")
    c.write_atomic(PUB / "review" / "llms.txt", REVIEW_LLMS.replace("SECTION_LINKS", "".join(
        f"- [{s['n']}. {s['title']}](SITE_URL/review/{review_slug(s)}.md): {s['scope']}\n" for s in c.TAXONOMY["arc42"])).replace("SITE_URL", c.SITE_URL))
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
            return [{"slug": f"concepts/{k}/{a['slug']}"} for a in groups(k)[0][1]]  # explicit list, so `order:` is respected
        return [{"label": t, "collapsed": True, "items": [{"slug": f"concepts/{k}/{a['slug']}"} for a in items]} for t, items in groups(k)]
    sb.append({"label": "Concepts", "items": [{"label": cats[k]["title"], "collapsed": True, "items": cat_items(k)} for k in cats if k in by_cat]})
    sb += [{"label": "Review", "slug": "review/checklists"}, {"label": "Glossary", "slug": "glossary"}]
    c.write_json(SITE / "sidebar.json", sb)
    rep = [f"articles: {len(arts)}; guides: {len(gl)}; diagrams rendered: {n_diag}; failed: {len(bad_diag)}"] + [f"- FAIL diagram {b}" for b in bad_diag]
    fails = [f"diagram {b}" for b in bad_diag]
    cf, cw = check_content(arts)
    fails += cf
    rep += [f"- WARN {w}" for w in cw]
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


# --- content rules (see CLAUDE.md). FAIL blocks the build, WARN is only reported.
MIN_WORDS, MAX_WORDS = 150, 650
OLD_MODEL = (r"(?i)ISO(?:/IEC)? ?25010 ?\(2011\)|\b2011 (?:edition|version|standard)\b|\bUI aesthetics\b|user interface aesthetics"
             r"|\bsub-?characteristic called maturity\b")
ARC42_PAGE = {1: "arc42-introduction-and-goals", 2: "arc42-constraints", 3: "arc42-context-and-scope", 4: "arc42-solution-strategy", 5: "arc42-building-block-view", 6: "arc42-runtime-view",
              7: "arc42-deployment-view", 8: "arc42-crosscutting-concepts", 9: "arc42-architecture-decisions", 10: "arc42-quality-requirements", 11: "arc42-risks-and-technical-debt", 12: "arc42-glossary"}
SECTION_OF = {v: k for k, v in ARC42_PAGE.items()}


def review_slug(s):
    """Review checklist page of an arc42 section: named so it is not confused with the explainer page of the section."""
    return f"section-{s['n']:02d}-" + re.sub(r"[^a-z0-9]+", "-", s["title"].lower()).strip("-")


def review_title(s):
    return f"Review checklist: arc42 section {s['n']}, {s['title']}"


TACTIC_SLUGS = {f"{k}-tactic" for k in ("reliability", "maintainability", "performance-efficiency", "interaction-capability", "security", "safety")}


def check_content(arts):
    """Source-level checks on content/. Returns (fails, warns)."""
    fails, warns = [], []
    slugs = {a["slug"] for a in arts}
    titles = {a["title"].lower() for a in arts}
    titles |= {re.sub(r"\s*\([^)]*\)\s*$", "", x) for x in titles} | {m for x in titles for m in re.findall(r"\(([^)]+)\)\s*$", x)}  # "Title (ACRONYM)": both parts
    inbound = {s: 0 for s in slugs}
    texts = [(a["slug"], a.get("related") or [], a["_body"]) for a in arts]
    for g in sorted((c.CONTENT / "guides").glob("*/index.md")):
        _, body = c.split_front(g.read_text())
        texts.append((None, [], body))
        by_target = {}
        for txt, tgt in re.findall(r"\[([^\]]+)\]\(concept:([^)]+)\)", body):
            by_target.setdefault(tgt, set()).add(txt.lower())
        for tgt, txts in by_target.items():
            if len(txts) >= 3:
                warns.append(f"guide {g.parent.name}: {len(txts)} different link texts for one target '{tgt}'")
    for me, rel, body in texts:
        for s in set(rel) | set(re.findall(r"\(concept:([^)]+)\)", body)):
            if s in inbound and s != me:
                inbound[s] += 1
            elif s not in slugs:
                fails.append(f"{me or 'guide'}: reference to unknown concept '{s}'")
    sgs = json.loads((c.CONTENT / "subgroups.json").read_text()) if (c.CONTENT / "subgroups.json").exists() else {}
    prefix = {x["id"]: x["title_prefix"] for cat in c.TAXONOMY["categories"] for x in cat.get("subcategories", []) if x.get("title_prefix")}
    for a in arts:  # a group with a title_prefix in taxonomy.yaml names all its pages the same way
        want = prefix.get(sgs.get(a["slug"]))
        if want and not a["title"].startswith(want):
            fails.append(f"{a['slug']}: title '{a['title']}' must start with '{want}' (title_prefix of its group)")
    seen = {}
    for a in arts:
        if "order" in a:
            key = (a["category"], sgs.get(a["slug"], "-"), a["order"])
            if key in seen:
                fails.append(f"{a['slug']}: same order {a['order']} as {seen[key]} in its group")
            seen[key] = a["slug"]
    for a in arts:
        s, body = a["slug"], a["_body"]
        n = len(body.split())
        if n < MIN_WORDS and not a.get("short_ok"):
            fails.append(f"{s}: {n} words, under {MIN_WORDS} (cut, merge, or set short_ok: true with a reason in the review)")
        if n > MAX_WORDS and not a.get("long_ok"):
            warns.append(f"{s}: {n} words, over {MAX_WORDS}")
        if not a.get("sources"):
            fails.append(f"{s}: no sources (every page needs at least one public source)")
        elif len(a["sources"]) < 2:
            warns.append(f"{s}: fewer than 2 sources")
        for k in re.findall(r"\[src:(\d+)\]", body):
            if not 1 <= int(k) <= len(a.get("sources") or []):
                fails.append(f"{s}: [src:{k}] but the page has {len(a.get('sources') or [])} sources")
        if not inbound[s]:
            warns.append(f"{s}: no page links to it")
        norm_urls = [re.sub(r"^https?://(www\.)?", "", x["url"]).split("#")[0].rstrip("/").lower() for x in (a.get("sources") or [])]
        for u in {u for u in norm_urls if norm_urls.count(u) > 1}:
            fails.append(f"{s}: source listed twice: {u}")
        for x in a.get("sources") or []:
            if not str(x.get("title", "")).strip():
                fails.append(f"{s}: source without title: {x['url']}")
            if re.search(r"learn\.microsoft\.com/(?!en-us)[a-z]{2}-[a-z]{2}/", x["url"]):
                fails.append(f"{s}: non-English locale in source URL: {x['url']}")
        if re.search(r"\b[Tt]radeoffs?\b(?! Analysis)", re.sub(r"Architecture Tradeoff Analysis Method|Tradeoff Analysis", "", body)):
            warns.append(f"{s}: write 'trade-off', not 'tradeoff'")
        by_target = {}
        for txt, tgt in re.findall(r"\[([^\]]+)\]\(concept:([^)]+)\)", body):
            by_target.setdefault(tgt, set()).add(txt.lower())
        for tgt, txts in by_target.items():
            if len(txts) >= 3:
                warns.append(f"{s}: {len(txts)} different link texts for one target '{tgt}'")
        if a.get("category") in ("quality-attributes", "tactics") and (m := re.search(OLD_MODEL, body)):
            fails.append(f"{s}: 2011 model wording '{m[0]}' (use ISO/IEC 25010:2023 only)")
        lines, fence = [], False  # lines inside code fences count as text, not as headings
        for l in body.split("\n"):
            if l.startswith("```"):
                fence = not fence
                lines.append("code")
            else:
                lines.append("code" if fence else l)
        if m := re.search(r"(?:[Tt]he article|\b[Ss]ee(?: the article)?) \"?" + re.escape(a["title"]) + r"\"?(?=[.,)]| and\b| for\b| covers\b| explains\b| has\b)", body):
            fails.append(f"{s}: refers to itself ('{m[0]}'), usually left by a merge; drop the reference")
        for i, l in enumerate(lines):  # a list item with no text, or only a bold label and nothing nested under it
            if re.fullmatch(r"[ \t]*(?:[-*]|\d+\.)(?:[ \t]+\*\*[^*\n]+\*\*:?)?[ \t]*", l):
                nxt = next((x for x in lines[i + 1:] if x.strip()), "")
                if "**" not in l or not nxt.startswith((" ", "\t")):
                    fails.append(f"{s}: empty list item '{l.strip()}' (its text was deleted; rewrite the list)")
                    break
        if re.search(r"\S\n[ \t]*\n[ \t]*\n", "\n".join(lines)):  # two blank lines in a row are left where a block was deleted
            fails.append(f"{s}: two blank lines in a row (a deleted block? rewrite the paragraph around it)")
        lead = re.compile(r"^\*\*[^*\n]+\*\*\s*[:.]?\s*$")
        h2 =[i for i, l in enumerate(lines) if l.startswith("## ")]
        for k, i in enumerate(h2):  # a "## " section needs text that is not just bold labels
            end = h2[k + 1] if k + 1 < len(h2) else len(lines)
            if not any(lines[j].strip() and not lead.match(lines[j]) for j in range(i + 1, end)):
                fails.append(f"{s}: empty section '{lines[i].strip()[:40]}'")
        heads = [i for i, l in enumerate(lines) if l.startswith("## ") or lead.match(l)]
        for k, i in enumerate(heads):  # a bold label needs text before the next "## " heading or the end
            if lead.match(lines[i]):
                end = heads[k + 1] if k + 1 < len(heads) else len(lines)
                if not any(lines[j].strip() for j in range(i + 1, end)) and (end >= len(lines) or lines[end].startswith("## ")):
                    fails.append(f"{s}: empty section under '{lines[i].strip()[:40]}'")
        if a.get("category") == "tactics" and a.get("kind") == "tactic" and s not in TACTIC_SLUGS | {"architectural-tactic"}:
            fails.append(f"{s}: tactic pages are one per ISO characteristic ({', '.join(sorted(TACTIC_SLUGS))})")
        for m in re.finditer(r"\b[Ss]ee (?:the )?articles? (?:on )?([^\n]+)", body):
            seg = re.split(r"(?<=[A-Za-z0-9)*\"”])\.(?:\s|$)", m[1])[0].strip(" \"“”*")
            seg = re.sub(r"\s+for\b.*$", "", seg)
            quoted = re.findall(r"[\"“]([^\"”]+)[\"”]", m[1])
            if quoted and all(any(q.lower().startswith(x) for x in titles) for q in quoted):
                continue  # quoted titles, which may contain "and"
            if seg.lower() in titles or sum(x in seg.lower() for x in titles if len(x) > 8) >= 1 and "(" in seg:
                continue  # a known title inside a parenthesized or quoted list
            for part in re.split(r",\s*(?:and\s+)?|\s+and\s+", seg):
                part = re.sub(r"^the\s+", "", part.strip(" \"“”*()"), flags=re.I)
                if part and part[0].isupper() and part.count(")") <= part.count("(") and not any(part.lower().startswith(x) or x.startswith(part.lower()) for x in titles):  # a known title at the start (or a prefix of one) is enough; lowercase starts are sentence fragments
                    warns.append(f"{s}: 'See the article {part}' matches no page title")
    by_title = {a["title"]: a["slug"] for a in arts if " " in a["title"]}  # one-word titles are mostly ordinary words
    for a in arts:  # a page that names another page's title in its text should link it somewhere
        plain = re.sub(r"(?s)```.*?```|\[[^\]]*\]\([^)]*\)|\b[Ss]ee (?:the )?(?:articles? )?[^.\n]*", " ", a["_body"])
        linked = set(re.findall(r"\(concept:([^)]+)\)", a["_body"])) | set(a.get("related") or []) | {a["slug"]}
        for t, slug in by_title.items():
            for m in [] if slug in linked else re.finditer(r"(?<![\w-])" + re.escape(t) + r"(?![\w-])", plain):
                prev = plain[:m.start()].split()[-1:]
                if re.match(r" [A-Z(]", plain[m.end():m.end() + 2]) or prev and (prev[0][0].isupper() or prev[0][0].isdigit()) and prev[0][-1] not in ".:!?":
                    continue  # part of a longer proper name, such as "Software Architecture in Practice"
                warns.append(f"{a['slug']}: names '{t}' but does not link it (add 'See {t}.' or put {slug} in related)")
                break
    return fails, warns


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
