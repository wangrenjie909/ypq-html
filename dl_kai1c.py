# -*- coding: utf-8 -*-
import urllib.request

urls = [
    ("kai1.jpg", "http://static.shihuocdn.cn/goods/locrevise/20240302/461e90ac-d86d-11ee-bd98-56efd8cfecc7_841x841.jpeg?imageView2/0/w/700/h/700/interlace/1"),
]

for out, url in urls:
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0",
            "Referer": "https://www.shihuo.cn/",
        })
        data = urllib.request.urlopen(req, timeout=30).read()
        open(out, "wb").write(data)
        print(out, "downloaded", len(data), "bytes")
    except Exception as e:
        print(out, "dl err", e)
