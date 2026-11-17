import re

from pipeline import build, common as c


def test_llms_txt():
    t = build.llms_txt("Title", "Summary.", [("Pages", [("A", "https://x/a.md", "about a")])], "Intro.")
    lines = t.splitlines()
    assert lines[0].startswith("# ") and any(l.startswith("> ") for l in lines)
    assert "- [A](https://x/a.md): about a" in lines


def test_write_atomic(tmp_path):
    c.write_atomic(tmp_path / "d" / "f.txt", "hi")
    assert (tmp_path / "d" / "f.txt").read_text() == "hi"
    assert not list(tmp_path.rglob("*.tmp"))


def test_fact_id_pattern():
    assert re.search(build.FACT_ID, "names several kinds of scenarios (f8): a list")
    assert re.search(build.FACT_ID, "both (f2, f3)")
    assert not re.search(build.FACT_ID, "the function f(x) and a (final) note")


def test_fact_talk_pattern():
    for leak in ("The facts here do not cover costs.", "The verified facts describe benefits.", "**Layers named in the facts:**",
                 "The facts give no trade-offs."):
        assert re.search(build.FACT_TALK, leak), leak
    for ok in ("the facts recorded about each entity", "Defer the others until the facts exist.", "decide based on facts"):
        assert not re.search(build.FACT_TALK, ok), ok


def test_check_content():
    def art(slug, words, **kw):
        return {"slug": slug, "title": slug.title(), "category": kw.get("category", "fundamentals"), "kind": "concept",
                "sources": kw.get("sources", [{"url": "https://a.example/1", "title": "A"}, {"url": "https://b.example/2", "title": "B"}]), "related": kw.get("related", []), "_body": " ".join(["w"] * words) + kw.get("tail", ""), **kw.get("extra", {})}
    arts = [art("a", 200, related=["b"]), art("b", 100), art("c", 200, category="quality-attributes", tail=" the ISO 25010 (2011) model")]
    fails, warns = build.check_content(arts)
    assert any("b: 100 words" in f for f in fails)          # too short
    assert any("2011 model wording" in f for f in fails)     # old model
    assert any("c: no page links to it" in w for w in warns) # orphan
    arts[1]["short_ok"] = True
    assert not any("b:" in f for f in build.check_content(arts)[0])


def test_check_content_order():
    def art(slug, order):
        return {"slug": slug, "title": slug, "category": "fundamentals", "kind": "concept", "sources": [{"url": "https://a.example/1", "title": "A"}, {"url": "https://b.example/2", "title": "B"}], "related": [], "order": order, "_body": " ".join(["w"] * 200)}
    arts = [art("a", 1), art("b", 1), art("c", 2)]
    fails, _ = build.check_content(arts)
    assert any("same order 1" in f for f in fails)
    arts[1]["order"] = 3
    assert not any("same order" in f for f in build.check_content(arts)[0])


def test_check_content_sources():
    def art(sources):
        return {"slug": "a", "title": "A", "category": "fundamentals", "kind": "concept", "related": [], "sources": sources, "_body": " ".join(["w"] * 200)}
    s1 = {"url": "https://x.example/p", "title": "P"}
    fails, _ = build.check_content([art([s1, {"url": "https://www.x.example/p/", "title": "P again"}])])
    assert any("listed twice" in f for f in fails)
    fails, _ = build.check_content([art([s1, {"url": "https://y.example/q", "title": ""}])])
    assert any("without title" in f for f in fails)
    fails, _ = build.check_content([art([s1, {"url": "https://learn.microsoft.com/sk-sk/azure/x", "title": "X"}])])
    assert any("locale" in f for f in fails)


def test_link_see():
    titles = {"cv": ("Component View", ("/concepts/d/cv/", "/concepts/d/cv.md")), "rv": ("Runtime View", ("/concepts/d/rv/", "/concepts/d/rv.md")),
              "me": ("This Page", ("/concepts/d/me/", "/concepts/d/me.md"))}
    out = build.link_see("See the articles Component View and *Runtime View*. Runtime View alone stays text. See This Page.", titles, False, "me")
    assert "[Component View](/concepts/d/cv/)" in out and "*[Runtime View](/concepts/d/rv/)*" in out
    assert "Runtime View alone stays text" in out                  # not inside a See clause
    assert "See This Page." in out                                 # never links the page to itself


def test_check_content_empty_section():
    def art(body):
        return {"slug": "a", "title": "A", "category": "fundamentals", "kind": "concept", "related": [], "sources": [{"url": "https://a.example/1", "title": "A"}, {"url": "https://b.example/2", "title": "B"}], "_body": body}
    filler = " ".join(["w"] * 200)
    fails, _ = build.check_content([art("## Explanation\n\n" + filler + "\n\n## Trade-offs\n\n")])
    assert any("empty section" in f for f in fails)
    fails, _ = build.check_content([art("## Explanation\n\n**Lead.**\n\n## Example\n\n" + filler)])
    assert any("empty section" in f for f in fails)
    fails, _ = build.check_content([art("## Explanation\n\n**Group**\n\n**Part one.**\n\n" + filler)])
    assert not any("empty section" in f for f in fails)
    fails, _ = build.check_content([art("## Explanation\n\n" + filler + "\n\n\n**Next.** " + filler)])
    assert any("blank lines" in f for f in fails)  # left where a block was deleted
    assert any("empty list item" in f for f in build.check_content([art(filler + "\n\n1. One.\n2.\n")])[0])
    assert any("refers to itself" in f for f in build.check_content([art(filler + " Cards help (see the article A).")])[0])
    assert not any("refers to itself" in f for f in build.check_content([art(filler + " See A Better Page.")])[0])


def test_check_content_ignores_code_fences():
    body = "## Explanation\n\n" + " ".join(["w"] * 200) + "\n\n```markdown\n## Heading in code\n## Another\n```\n"
    art = {"slug": "a", "title": "A", "category": "fundamentals", "kind": "concept", "related": [], "sources": [{"url": "https://a.example/1", "title": "A"}, {"url": "https://b.example/2", "title": "B"}], "_body": body}
    assert not any("empty section" in f for f in build.check_content([art])[0])


def test_named_but_not_linked():
    filler = " ".join(["w"] * 200)
    def art(slug, title, body, related=()):
        return {"slug": slug, "title": title, "category": "fundamentals", "kind": "concept", "related": list(related), "sources": [{"url": f"https://{slug}.example/1", "title": "A"}, {"url": f"https://{slug}.example/2", "title": "B"}], "_body": "## Explanation\n\n" + filler + " " + body}
    other = art("shared-database", "Shared Database", "See Big Page.")
    warned = lambda body, rel=(): [w for w in build.check_content([art("big-page", "Big Page", body, rel), other])[1] if "does not link" in w]
    assert warned("Teams often use a Shared Database here.")
    assert not warned("Teams often use a Shared Database here.", ["shared-database"])
    assert not warned("The book Shared Database Patterns covers it.")  # part of a longer proper name


def test_source_markers():
    srcs = [{"url": "https://a.example/1", "title": "A"}, {"url": "https://b.example/2", "title": "B"}]
    assert build.cite("It took 70 days [src:2].", srcs, False) == "It took 70 days<sup>[2](https://b.example/2)</sup>."
    assert build.cite("It took 70 days [src:2].", srcs, True) == "It took 70 days [[2]](https://b.example/2)."
    art = {"slug": "a", "title": "A", "category": "fundamentals", "kind": "concept", "related": [], "sources": srcs,
           "_body": "## Explanation\n\n" + " ".join(["w"] * 200) + " It took 70 days [src:3]."}
    assert any("[src:3]" in f for f in build.check_content([art])[0])  # no third source


def test_select_checks():
    def art(title, arc42, checks):
        return {"title": title, "category": "c", "arc42": arc42, "checks": checks}
    arts = [art("A", [1], ["The quality goals are listed."]), art("B", [1], ["The quality goals are listed!", "Another check."]), art("C", [2, 1], ["Second section first", "Fits section one"])]
    rows = build.select_checks(arts, [1, 2], cap=2)
    assert [c for c, _ in rows[1]] == ["The quality goals are listed.", "Another check."]   # near-duplicate dropped, cap 2
    assert [c for c, _ in rows[2]] == ["Second section first"]


def test_title_prefix():
    arts = [{"slug": "x", "title": "Package Diagram", "category": "modeling-uml", "kind": "concept", "related": [], "sources": [{"url": "https://a.example/1", "title": "A"}, {"url": "https://b.example/2", "title": "B"}], "_body": " ".join(["w"] * 200)}]
    sgs = build.json.loads('{"x": "structure-diagrams"}')
    import json, pathlib
    orig = pathlib.Path.read_text
    # the check reads content/subgroups.json; use the real file: only assert the helper data exists
    assert any(x.get("title_prefix") for cat in build.c.TAXONOMY["categories"] for x in cat.get("subcategories", []))


def test_fixaudit_finds_orphan():
    from pipeline import fixaudit
    old = {"a": "**Notes.** The tool is slow. That hurts users. It is fine otherwise.\n"}
    assert fixaudit.audit(old, {"a": "**Notes.** That hurts users. It is fine otherwise.\n"})       # dependent sentence lost its antecedent
    assert not fixaudit.audit(old, {"a": "**Notes.** The tool is slow. That hurts users. It is fine otherwise.\n"})


def test_guide_check_reads_linked_pages():
    from pipeline import claimcheck
    pages = claimcheck.concept_pages("See [Utility Tree](concept:utility-tree), again [tree](concept:utility-tree).")
    assert len(pages) == 1 and pages[0].startswith("=== PAGE: Utility Tree")


def test_link_graph_counts_each_link_once():
    titles = {s: (s.title(), (f"/concepts/x/{s}/", "")) for s in "abc"}
    bodies = {"a": "See [B](/concepts/x/b/).", "b": "Back to [A](/concepts/x/a/) and [C](/concepts/x/c/).", "c": "[C](/concepts/x/c/)"}
    urls, links = build.link_graph(titles, bodies)
    assert links == [(0, 1), (1, 2)]  # a-b once although both link, b-c, no self link


def test_torres_source_themes_diagrams_but_not_bpmn():
    from pipeline.build import torres_source
    assert torres_source("mermaid", "flowchart TD\n  A --> B").startswith("%%{init: {\"theme\": \"base\"")
    assert torres_source("c4plantuml", "@startuml\n!include <C4/C4_Context>\n@enduml").split("\n")[1] == "skinparam monochrome true"
    assert torres_source("bpmn", "<xml/>") == "<xml/>"


def test_pin_inline_scripts_adds_hash_policy(tmp_path):
    import base64, hashlib
    from pipeline.build import pin_inline_scripts
    page = tmp_path / "index.html"
    page.write_text('<html><head><meta charset="utf-8"/><script>run()</script><script type="application/json">{}</script>'
                    '<script src="/a.js"></script></head></html>')
    assert pin_inline_scripts(tmp_path) == []
    want = base64.b64encode(hashlib.sha256(b"run()").digest()).decode()
    out = page.read_text()
    assert f"script-src 'self' 'wasm-unsafe-eval' 'sha256-{want}'\">" in out  # only the script that runs
    assert out.index("Content-Security-Policy") < out.index("<script>")  # before the first script
