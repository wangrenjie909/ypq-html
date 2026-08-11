# -*- coding: utf-8 -*-
import re, json, urllib.request

# 1) 重试 shihuoproxy 的 NBA 官方骑士球衣图（DNS 失败可能是临时的）
urls = [
    ("cavs_jersey.jpg", "http://shihuoproxy.hupucdn.com/aHR0cDovL25iYS5mcmdpbWFnZXMuY29tL0ZGSW1hZ2UvdGh1bWIuYXNweD9pPS9wcm9kdWN0aW1hZ2VzL18yNTA1MDAwL2FsdGltYWdlcy9mZl8yNTA1MzMwYWx0MV9mdWxsLmpwZyZ3PTYwMA?imageView2/0/w/400/", "https://www.shihuo.cn/"),
]

for out, url, ref in urls:
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0",
            "Referer": ref,
        })
        data = urllib.request.urlopen(req, timeout=30).read()
        open(out, "wb").write(data)
        print(out, "OK", len(data), "bytes")
    except Exception as e:
        print(out, "err", e)

# 2) 列出 j_cavs.html 所有候选，找标题含"球衣"或"11"的
html = open("j_cavs.html", encoding="utf-8", errors="ignore").read()
m = re.search(r'<script type="text/data" id="initData">(.*?)</script>', html, re.S)
if m:
    try:
        obj = json.loads(m.group(1))
        items = obj.get("list", [])
        print("---- all cavs candidates ----")
        for i, it in enumerate(items):
            title = it.get("title", "")
            img = it.get("img", "") or ""
            if "球衣" in title or "11" in title or "jersey" in title.lower():
                print(i, "|", title[:50], "|", img[:110])
    except Exception as e:
        print("json err", e)
