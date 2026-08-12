# -*- coding: utf-8 -*-
import urllib.request

jobs = [
    ("kai2.jpg", "http://static.shihuocdn.cn/goods/locrevise/20251130/07c09e86-cdf8-11f0-a902-82ec82919c2b_1947x1947.jpeg?imageView2/0/w/700/h/700/interlace/1", "https://www.shihuo.cn/"),
    ("kai3.jpg", "https://a.zdmimg.com/202602/18/6995485cf6bb1827.jpg_e1080.jpg", "https://www.smzdm.com/"),
]

for out, url, ref in jobs:
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0",
            "Referer": ref,
        })
        data = urllib.request.urlopen(req, timeout=30).read()
        open(out, "wb").write(data)
        print(out, "downloaded", len(data), "bytes")
    except Exception as e:
        print(out, "dl err", e)
