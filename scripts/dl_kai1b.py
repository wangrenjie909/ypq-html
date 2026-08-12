# -*- coding: utf-8 -*-
import urllib.request

urls = [
    ("kai1.jpg", "https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2024%2F0227%2F88e3dd83j00s9hpkp00g4d001kw01jkg.jpg&thumbnail=660x2147483647&quality=80&type=jpg"),
]

for out, url in urls:
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0",
            "Referer": "https://www.163.com/",
        })
        data = urllib.request.urlopen(req, timeout=30).read()
        open(out, "wb").write(data)
        print(out, "downloaded", len(data), "bytes")
    except Exception as e:
        print(out, "dl err", e)
