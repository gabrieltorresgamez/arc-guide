"""Shared helpers for the site build: paths, YAML, atomic writes, Kroki, front matter."""
import hashlib
import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"  # Kroki cache and build report only; safe to delete
CONTENT = ROOT / "content"
REPORTS = BUILD / "reports"


def _load_env():
    f = ROOT / ".env"
    if f.exists():
        for line in f.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


_load_env()
KROKI_URL = os.environ.get("KROKI_URL", "http://localhost:8000").rstrip("/")
SITE_URL = os.environ.get("SITE_URL", "http://localhost:4321").rstrip("/")


def load_yaml(name):
    return yaml.safe_load((ROOT / name).read_text(encoding="utf-8"))


TAXONOMY = load_yaml("taxonomy.yaml")


def write_atomic(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    if isinstance(data, str):
        tmp.write_text(data, encoding="utf-8")
    else:
        tmp.write_bytes(data)
    os.replace(tmp, path)


def write_json(path, obj):
    write_atomic(path, json.dumps(obj, ensure_ascii=False, indent=1))


def write_report(stage, lines):
    write_atomic(REPORTS / f"{stage}.md", f"# {stage}\n\n" + "\n".join(lines) + "\n")


KROKI_LANG = {".c4.puml": "c4plantuml", ".puml": "plantuml", ".bpmn": "bpmn", ".mmd": "mermaid",
              ".d2": "d2", ".dot": "graphviz", ".dbml": "dbml"}


def kroki_lang(filename):
    for ext, lang in KROKI_LANG.items():  # ".c4.puml" is listed before ".puml"
        if str(filename).endswith(ext):
            return lang
    raise ValueError(f"no Kroki language for {filename}")


class KrokiError(Exception):
    pass


def kroki_render(lang, source, fmt="svg"):
    cache = BUILD / "kroki" / f"{hashlib.sha256((lang + source).encode()).hexdigest()}.{fmt}"
    if cache.exists():
        return cache.read_bytes()
    req = urllib.request.Request(f"{KROKI_URL}/{lang}/{fmt}", data=source.encode(),
                                 headers={"Content-Type": "text/plain"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
    except urllib.error.HTTPError as e:
        raise KrokiError(e.read().decode(errors="replace")) from e
    write_atomic(cache, data)
    return data


def split_front(text):
    """Markdown with YAML front matter -> (dict, body)."""
    m = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.S)
    return (yaml.safe_load(m.group(1)) or {}, m.group(2).lstrip("\n")) if m else ({}, text)
