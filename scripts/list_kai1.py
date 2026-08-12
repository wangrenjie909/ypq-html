# -*- coding: utf-8 -*-
import re, json, urllib.parse

html = open("sogou.html", encoding="utf-8", errors="ignore").read()
m = re.search(r'__INITIAL_STATE__=(\{.*?\});', html, re.S)
obj = json.loads(m.group(1))
items = obj.get("searchList", {}).get("searchList", [])
print("total:", len(items))
for i, it in enumerate(items):
    title = it.get("title", "")
    u = it.get("oriPicUrl") or it.get("picUrl") or ""
    if "nimg.ws.126.net" in u:
        print(i, "|", title[:45], "|", urllib.parse.unquote(u)[:120])
