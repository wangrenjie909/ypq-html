# -*- coding: utf-8 -*-
import re, json, urllib.parse, datetime

def extract(html_file):
    html = open(html_file, encoding="utf-8", errors="ignore").read()
    m = re.search(r'__INITIAL_STATE__=(\{.*?\});', html, re.S)
    if not m:
        print(html_file, "no state")
        return
    try:
        obj = json.loads(m.group(1))
        items = obj.get("searchList", {}).get("searchList", [])
    except Exception as e:
        print(html_file, "json err", e)
        return
    print("=====", html_file, "items:", len(items))
    for it in items:
        ts = it.get("publish_time") or "0"
        try:
            year = datetime.datetime.fromtimestamp(int(ts)).year
        except Exception:
            year = 0
        if year >= 2025:
            title = it.get("title", "")
            u = it.get("oriPicUrl") or it.get("picUrl") or ""
            print(year, "|", title[:50], "|", urllib.parse.unquote(u)[:110])

extract("sogou2b.html")
extract("sogou3b.html")
extract("sogou2.html")
extract("sogou3.html")
