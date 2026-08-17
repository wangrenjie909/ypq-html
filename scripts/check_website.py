# -*- coding: utf-8 -*-
import re

html = open('index.html', encoding='utf-8').read()
checks = {
    '导航栏': 'navbar' in html,
    'Hero打字机': 'typewriter' in html,
    '技能徽章': 'badge' in html,
    '欧文荣誉榜': 'honors' in html,
    '效力时间线': '2011-2017' in html,
    '球星名言': 'star-quote' in html,
    '石头剪刀布': 'play(' in html,
    '投篮游戏': 'shoot' in html,
    '千题问答': 'quiz.length' in html and len(re.findall(r'q: "', html)) >= 500,
    '排行榜': 'bestRps' in html,
    '主题切换': 'toggleTheme' in html,
    '访客计数': 'visitor' in html,
    '表单验证': 'formError' in html,
    '字数统计': 'countWords' in html,
    '返回顶部': 'backTop' in html,
    'SEO': 'meta name="description"' in html,
    '音乐': 'bgm.mp3' in html,
    '证书': '网页创作者证书' in html,
}
all_ok = True
for name, ok in checks.items():
    print(('OK' if ok else 'MISS') + ' ' + name)
    if not ok:
        all_ok = False
print()
print('ALL PASS' if all_ok else 'SOME MISSING')
