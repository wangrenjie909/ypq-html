# -*- coding: utf-8 -*-
import re, json

html = open("j_celtics.html", encoding="utf-8", errors="ignore").read()
m = re.search(r'<script type="text/data" id="initData">(.*?)</script>', html, re.S)
if not m:
    print("no initData")
    raise SystemExit
obj = json.loads(m.group(1))
items = obj.get("list", [])
print("total:", len(items))
for i, it in enumerate(items):
    title = it.get("title", "")
    img = it.get("img", "") or ""
    if any(k in title for k in ["凯尔特人", "绿", "球衣", "11"]):
        print(i, "|", title[:50], "|", img[:120])
