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
