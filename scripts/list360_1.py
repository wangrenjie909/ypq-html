# -*- coding: utf-8 -*-
import re, json

html = open("so360_1.html", encoding="utf-8", errors="ignore").read()
m = re.search(r'<script type="text/data" id="initData">(.*?)</script>', html, re.S)
if not m:
    print("no initData")
    raise SystemExit
obj = json.loads(m.group(1))
items = obj.get("list", [])
print("total:", len(items))
for i, it in enumerate(items):
    title = it.get("title", "")
    img = it.get("img", "") or it.get("thumb", "")
    if any(k in title for k in ["KAI1", "KAI 1", "kai1", "kai 1", "一代", "欧文1"]):
        print(i, "|", title[:55], "|", img[:120])
