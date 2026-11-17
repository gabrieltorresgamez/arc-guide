"""Check that every URL in the articles' `sources:` lists is reachable and is not a captcha or login page.

Usage: uv run python -m pipeline.linkcheck [SLUG ...]     Report: build/reports/linkcheck.md
Slow (about one request per second per site), so it is not part of the build. Run it before a release or each quarter.
"""
import re
import ssl
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import date

from pipeline import common as c

BAD = re.compile(r"(?i)are you a robot|verify you are human|checking your browser|enable javascript and cookies|access denied|just a moment")


def blocked(raw):
    """Captcha or block page: judged on the visible text only, because normal pages mention captcha in scripts."""
    text = re.sub(r"(?is)<(script|style)\b.*?</\1\s*>|<[^>]*>", " ", raw)
    return bool(BAD.search(text)) or (len(text.split()) < 400 and "captcha" in text.lower())


def probe(url):
    if "pmc.ncbi.nlm.nih.gov/articles/" in url:  # PMC shows scripts a browser check; fetch_public reads it via Europe PMC
        try:
            return "captcha or block page" if blocked(c.fetch_public(url)) else None
        except Exception as e:
            return type(e).__name__
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
    by_host = defaultdict(list)  # one request per second per host, different hosts in parallel
    for u, who in sorted(pages.items()):
        by_host[urllib.parse.urlparse(u).hostname or ""].append((u, who))
    bad, done = [], [0]
    lock = threading.Lock()

    def run_host(items):
        for u, who in items:
            started = time.time()
            err = probe(u)
            with lock:
                done[0] += 1
                if err:
                    bad.append((u, who))
                if done[0] % 25 == 0:
                    print(f"[{done[0]}/{len(pages)}] checked, {len(bad)} problems", flush=True)
            time.sleep(max(0, 1.0 - (time.time() - started)))

    with ThreadPoolExecutor(max_workers=16) as pool:  # ponytail: 16 hosts at once; lower it if a firewall objects
        list(pool.map(run_host, by_host.values()))
    if bad:  # timeouts, 429 and 503 are often transient: check each failure once more after a pause
        print(f"rechecking {len(bad)} failures in 30 seconds", flush=True)
        time.sleep(30)
        bad = [f"- {err}: {u} (in {', '.join(who[:3])}{'...' if len(who) > 3 else ''})" for u, who in sorted(bad) if (err := probe(u))]
    c.write_report("linkcheck", [f"{date.today()}: {len(pages)} URLs, {len(bad)} problems", ""] + bad)
    print(f"{len(pages)} URLs, {len(bad)} problems, see build/reports/linkcheck.md")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
