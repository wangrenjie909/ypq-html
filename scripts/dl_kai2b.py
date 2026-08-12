# -*- coding: utf-8 -*-
import urllib.request

candidates = [
    ("kai2.jpg", "https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2024%2F1215%2Fd21111a6j00soiq7f0050d200u0012qg00it00o9.jpg&thumbnail=660x2147483647&quality=80&type=jpg",
     "欧文脚上惊现 安踏KAI2实拍曝光 20241215"),
    ("kai2.jpg", "https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2025%2F0308%2F03cbafe4j00sssesn00azd200u000iug00it00bt.jpg&thumbnail=660x2147483647&quality=80&type=jpg",
     "欧文安踏KAI 2突袭 20250308"),
    ("kai2.jpg", "https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2025%2F0316%2Ffa2f57e2j00st78ad0039d200u000l0g00u000l0.jpg&thumbnail=660x2147483647&quality=80&type=jpg",
     "欧文KAI 2生日限定曝光 20250316"),
]

for out, url, label in candidates:
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0",
            "Referer": "https://www.163.com/",
        })
        data = urllib.request.urlopen(req, timeout=30).read()
        open(out, "wb").write(data)
        print("OK", label, len(data), "bytes")
        break
    except Exception as e:
        print("ERR", label, e)
