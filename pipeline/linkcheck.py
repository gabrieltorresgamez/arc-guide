"""Check that every URL in the articles' `sources:` lists is reachable and is not a captcha or login page.

Usage: uv run python -m pipeline.linkcheck [SLUG ...]     Report: build/reports/linkcheck.md
Slow (about one request per second per site), so it is not part of the build. Run it before a release or each quarter.
"""
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import date

from pipeline import common as c

BAD = re.compile(r"(?i)are you a robot|verify you are human|checking your browser|enable javascript and cookies|access denied|just a moment")


def blocked(raw):
    """Captcha or block page: judged on the visible text only, because normal pages mention captcha in scripts."""
    text = re.sub(r"(?is)<(script|style)\b.*?</\1\s*>|<[^>]*>", " ", raw)
    return bool(BAD.search(text)) or (len(text.split()) < 400 and "captcha" in text.lower())


def probe(url):
    req = urllib.request.Request(urllib.parse.quote(url, safe=":/?#[]@!$&'()*+,;=%~"), headers={"User-Agent": "arc-guide-linkcheck/1.0 (non-commercial)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            if r.status != 200:
                return f"HTTP {r.status}"
            if "text/html" in r.headers.get("Content-Type", "") and blocked(r.read(200000).decode("utf-8", errors="replace")):
                return "captcha or block page"
    except urllib.error.HTTPError as e:
        return f"HTTP {e.code}"
    except urllib.error.URLError as e:
        if isinstance(e.reason, ssl.SSLCertVerificationError):  # incomplete chain that curl accepts, see common.fetch_public
            try:
                return "captcha or block page" if blocked(c.fetch_public(url)) else None
            except Exception as e2:
                return type(e2).__name__
        return type(e).__name__
    except Exception as e:
        return type(e).__name__
    return None


def main(slugs):
    pages = defaultdict(list)  # url -> slugs
    for f in sorted((c.CONTENT / "concepts").glob("*/*/index.md")):
        meta, _ = c.split_front(f.read_text())
        if slugs and f.parent.name not in slugs:
            continue
        for s in meta.get("sources", []):
            pages[s["url"]].append(f.parent.name)
    last, bad = defaultdict(float), []
    for i, (u, who) in enumerate(sorted(pages.items()), 1):
        host = urllib.parse.urlparse(u).hostname or ""
        time.sleep(max(0, last[host] + 1.0 - time.time()))
        last[host] = time.time()
        if err := probe(u):
            bad.append(f"- {err}: {u} (in {', '.join(who[:3])}{'...' if len(who) > 3 else ''})")
        if i % 100 == 0:
            print(f"{i}/{len(pages)} checked, {len(bad)} problems")
    c.write_report("linkcheck", [f"{date.today()}: {len(pages)} URLs, {len(bad)} problems", ""] + bad)
    print(f"{len(pages)} URLs, {len(bad)} problems, see build/reports/linkcheck.md")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
