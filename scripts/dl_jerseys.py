# -*- coding: utf-8 -*-
import urllib.request

jobs = [
    ("cavs_jersey.jpg", "http://shihuoproxy.hupucdn.com/aHR0cDovL25iYS5mcmdpbWFnZXMuY29tL0ZGSW1hZ2UvdGh1bWIuYXNweD9pPS9wcm9kdWN0aW1hZ2VzL18yNTA1MDAwL2FsdGltYWdlcy9mZl8yNTA1MzMwYWx0MV9mdWxsLmpwZyZ3PTYwMA?imageView2/0/w/400/", "https://www.shihuo.cn/"),
    ("celtics_jersey.jpg", "https://static.shihuocdn.cn/ucditor/20181101/800x800_c7c7cdaba77c0515dc5f0de58ed8fccc.jpeg", "https://www.shihuo.cn/"),
    ("nets_jersey.jpg", "http://www.usbashop.com/images//20210629/7dae4ef527f46a72.jpg", "http://www.usbashop.com/"),
    ("mavs_jersey.jpg", "https://img0.baidu.com/it/u=2109038877,3043723510&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=667", "https://www.baidu.com/"),
]

backups = {
    "cavs_jersey.jpg": ("https://cbu01.alicdn.com/img/ibank/2018/512/968/8780869215_1861772048.jpg", "https://www.1688.com/"),
    "nets_jersey.jpg": ("https://k.sinaimg.cn/n/sinacn20123/233/w833h1000/20190928/d33c-ifffqup7565224.jpg/w700d1q75cms.jpg?by=cms_fixed_width", "https://www.sina.com.cn/"),
    "mavs_jersey.jpg": ("https://gips1.baidu.com/it/u=4082998627,1518365463&fm=3074&app=3074&f=JPEG", "https://www.baidu.com/"),
}

for out, url, ref in jobs:
    ok = False
    for attempt, (u, r) in enumerate([(url, ref)] + ([backups[out]] if out in backups else [])):
        try:
            req = urllib.request.Request(u, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0",
                "Referer": r,
            })
            data = urllib.request.urlopen(req, timeout=30).read()
            if len(data) > 3000:
                open(out, "wb").write(data)
                print(out, "OK", len(data), "bytes (attempt", attempt, ")")
                ok = True
                break
            else:
                print(out, "too small", len(data))
        except Exception as e:
            print(out, "err attempt", attempt, e)
    if not ok:
        print(out, "FAILED all attempts")
