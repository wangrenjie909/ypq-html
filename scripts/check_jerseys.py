# -*- coding: utf-8 -*-
import re, json

def parse360(html_file):
    html = open(html_file, encoding="utf-8", errors="ignore").read()
    m = re.search(r'<script type="text/data" id="initData">(.*?)</script>', html, re.S)
    if not m:
        print(html_file, "no initData")
        return []
    try:
        obj = json.loads(m.group(1))
        return obj.get("list", [])
    except Exception as e:
        print(html_file, "json err", e)
        return []

for f, label, kw in [
    ("j_cavs.html", "骑士", ["骑士", "球衣", "Cavs", "cavs"]),
    ("j_celtics.html", "凯尔特人", ["凯尔特人", "球衣", "Celtics", "celtics"]),
    ("j_nets.html", "篮网", ["篮网", "球衣", "Nets", "nets"]),
    ("j_mavs.html", "独行侠", ["独行侠", "球衣", "Mavericks", "mavericks"]),
]:
    items = parse360(f)
    print("=====", label, "total:", len(items))
    n = 0
    for i, it in enumerate(items):
        title = it.get("title", "")
        if any(k in title for k in ["球衣", label, kw[3]]):
            img = it.get("img", "") or it.get("thumb", "")
            print(i, "|", title[:50], "|", img[:110])
            n += 1
            if n >= 10:
                break
