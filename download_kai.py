# -*- coding: utf-8 -*-
import re, json, urllib.parse, urllib.request

files = {"sogou.html": "kai1.jpg", "sogou2.html": "kai2.jpg", "sogou3.html": "kai3.jpg"}

for html_file, out_name in files.items():
    try:
        html = open(html_file, encoding="utf-8", errors="ignore").read()
    except Exception as e:
        print(out_name, "read err", e)
        continue
    m = re.search(r'__INITIAL_STATE__=(\{.*?\});', html, re.S)
    if not m:
        print(out_name, "no state found")
        continue
    try:
        obj = json.loads(m.group(1))
        items = obj.get("searchList", {}).get("searchList", [])
    except Exception as e:
        print(out_name, "json err", e)
        continue
    if not items:
        print(out_name, "no items")
        continue
    chosen = None
    for it in items:
        u = it.get("oriPicUrl") or it.get("picUrl")
        if u and "nimg.ws.126.net" in u:
            chosen = urllib.parse.unquote(u)
            break
    if not chosen:
        for it in items:
            u = it.get("oriPicUrl") or it.get("picUrl")
            if u:
                chosen = urllib.parse.unquote(u)
                break
    if not chosen:
        print(out_name, "no url")
        continue
    print(out_name, "URL:", chosen[:150])
    try:
        req = urllib.request.Request(chosen, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=30).read()
        open(out_name, "wb").write(data)
        print(out_name, "downloaded", len(data), "bytes")
    except Exception as e:
        print(out_name, "dl err", e)
