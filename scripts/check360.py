# -*- coding: utf-8 -*-
import re, json, urllib.request, urllib.parse

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

def show(items, label, kw_list):
    print("=====", label, "total:", len(items))
    for i, it in enumerate(items):
        title = it.get("title", "")
        if any(k in title for k in kw_list):
            img = it.get("img", "") or it.get("thumb", "")
            print(i, "|", title[:50], "|", img[:120])

def download(url, out):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=30).read()
        open(out, "wb").write(data)
        print("downloaded", out, len(data), "bytes <-", url[:100])
        return True
    except Exception as e:
        print("dl err", out, e)
        return False

# KAI2 图片（360）
items2 = parse360("so360_2.html")
show(items2, "KAI2 candidates", ["KAI2", "KAI 2", "kai2", "kai 2", "二代"])

# KAI3 图片（360）
items3 = parse360("so360_3.html")
show(items3, "KAI3 candidates", ["KAI3", "KAI 3", "kai3", "kai 3", "三代"])
