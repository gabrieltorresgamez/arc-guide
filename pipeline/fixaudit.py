"""Fix audit: finds text damage left by edits that only deleted sentences. Compares the working tree with a git ref.

Usage: uv run python -m pipeline.fixaudit [REF]      (default HEAD)
Reports, per page, every line where a sentence was cut and (a) the next sentence depends on it (starts with
That/It/They/This/So...), or (b) the line is now only a label or a fragment. Fix by rewriting the whole block, not by
deleting a sentence. Exit code 1 if anything is found."""
import difflib
import re
import subprocess
import sys

from pipeline import common as c

DEP = re.compile(r"^(That|They|It|This|These|Those|Its|Their|Such|Both|Then|So|There|Which|Doing so|Otherwise|Because|Also|However|But|Instead)\b")
LEAD = re.compile(r"^(?:- |\d+\. )?(?:\*\*[^*\n]+\*\*|\*[^*\n]+\*)[:.]?\s*")
norm = lambda s: re.sub(r"\s+", " ", s)
sentences = lambda line: [x for x in re.split(r"(?<=[.!?])\s+(?=[A-Z(*\"`])", line.strip()) if x]


def old_pages(ref):
    names = subprocess.run(["git", "ls-tree", "-r", "--name-only", ref, "content/concepts"], capture_output=True, text=True, cwd=c.ROOT).stdout.split()
    return {p: subprocess.run(["git", "show", f"{ref}:{p}"], capture_output=True, text=True, cwd=c.ROOT).stdout.split("---", 2)[-1] for p in names if p.endswith("index.md")}


def audit(old, new):
    """Findings (slug, was, now) for pages in `new` {name: body}, compared with the best matching page in `old` (pages may be renamed)."""
    sets = {k: {norm(s) for l in b.split("\n") for s in sentences(l)} for k, b in old.items()}
    out = []
    for name, body in new.items():
        cur = {norm(s) for l in body.split("\n") for s in sentences(l)}
        best = max(sets, key=lambda k: len(cur & sets[k]), default=None)
        if best is None or not cur & sets[best]:
            continue
        text = norm(body)
        for line in old[best].split("\n"):
            ss = sentences(line)
            gone = [i for i, s in enumerate(ss) if len(s) >= 12 and norm(s) not in text
                    and not any(difflib.SequenceMatcher(None, norm(s), x).ratio() > 0.8 for x in cur if abs(len(x) - len(s)) < len(s) * 0.5)]
            if not gone or len(gone) == len(ss):
                continue
            kept = [s for i, s in enumerate(ss) if i not in gone and norm(s) in text]
            dep = any(i + 1 < len(ss) and i + 1 not in gone and norm(ss[i + 1]) in text and DEP.match(LEAD.sub("", ss[i + 1])) and not LEAD.match(ss[i + 1]) for i in gone)
            stub = bool(kept) and len(" ".join(kept)) < 40 and 0 in gone
            if dep or stub:
                out.append((name, line.strip()[:300], " ".join(kept)[:200]))
    return out


def main(ref="HEAD"):
    new = {str(p.parent.name): p.read_text().split("---", 2)[-1] for p in (c.CONTENT / "concepts").glob("*/*/index.md")}
    found = audit(old_pages(ref), new)
    for name, was, now in found:
        print(f"[{name}]\n  WAS: {was}\n  NOW: {now}\n")
    print(f"{len(found)} damaged edits")
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main(*sys.argv[1:2])
