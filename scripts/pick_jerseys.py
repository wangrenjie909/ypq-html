# -*- coding: utf-8 -*-
import re, json

def parse360(html_file):
    html = open(html_file, encoding="utf-8", errors="ignore").read()
    m = re.search(r'<script type="text/data" id="initData">(.*?)</script>', html, re.S)
    if not m:
        return []
    try:
        obj = json.loads(m.group(1))
        return obj.get("list", [])
    except Exception as e:
        return []

picks = [
    ("j_cavs.html", 1),
    ("j_cavs.html", 12),
    ("j_celtics.html", 15),
    ("j_nets.html", 2),
    ("j_nets.html", 7),
    ("j_mavs.html", 8),
    ("j_mavs.html", 10),
]
for f, idx in picks:
    items = parse360(f)
    if idx < len(items):
        it = items[idx]
        print(f, "idx", idx, "|", it.get("title", "")[:45])
        print("   img:", (it.get("img") or "")[:200])
        print("   link:", (it.get("link") or "")[:120])
