# -*- coding: utf-8 -*-
import re

html = open('index.html', encoding='utf-8').read()
checks = {
    '带球过人100关': 'dgCanvas' in html and 'dgLevel < 100' in html,
    '猜数字': 'guessNum' in html,
    '翻牌找数字': 'memStart' in html,
    '斗地主': 'ddzStart' in html,
    '石头剪刀布': 'play(' in html,
    '投篮挑战': 'function shoot' in html,
    '千题问答': len(re.findall(r'q: "', html)) >= 500,
    '排行榜': 'bestRps' in html,
    '表情选择器': 'addEmoji' in html,
    'DJ音乐': 'bgm.mp3' in html,
    '主题切换': 'toggleTheme' in html,
    '访客计数': 'visitor' in html,
    '篮球雨彩蛋': 'basketballRain' in html,
    '动态标题': 'visibilitychange' in html,
    '懒加载': 'loading = "lazy"' in html or 'img.loading' in html,
    '表单验证': 'formError' in html,
    '字数统计': 'countWords' in html,
    '证书': '网页创作者证书' in html,
}
all_ok = True
for name, ok in checks.items():
    print(('OK' if ok else 'MISS') + ' ' + name)
    if not ok:
        all_ok = False
print()
print('ALL PASS' if all_ok else 'SOME MISSING')
