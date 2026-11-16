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
                "sources": kw.get("sources", [1, 2]), "related": kw.get("related", []), "_body": " ".join(["w"] * words) + kw.get("tail", ""), **kw.get("extra", {})}
    arts = [art("a", 200, related=["b"]), art("b", 100), art("c", 200, category="quality-attributes", tail=" the ISO 25010 (2011) model")]
    fails, warns = build.check_content(arts)
    assert any("b: 100 words" in f for f in fails)          # too short
    assert any("2011 model wording" in f for f in fails)     # old model
    assert any("c: no page links to it" in w for w in warns) # orphan
    arts[1]["short_ok"] = True
    assert not any("b:" in f for f in build.check_content(arts)[0])


def test_check_content_order():
    def art(slug, order):
        return {"slug": slug, "title": slug, "category": "fundamentals", "kind": "concept", "sources": [1, 2], "related": [], "order": order, "_body": " ".join(["w"] * 200)}
    arts = [art("a", 1), art("b", 1), art("c", 2)]
    fails, _ = build.check_content(arts)
    assert any("same order 1" in f for f in fails)
    arts[1]["order"] = 3
    assert not any("same order" in f for f in build.check_content(arts)[0])
