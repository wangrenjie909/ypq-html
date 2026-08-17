# -*- coding: utf-8 -*-
import re

html = open('index.html', encoding='utf-8').read()
i = html.find('const quiz = [')
j = html.find('];', i)
quiz_block = html[i:j+2]
lines = quiz_block.split('\n')
print('quiz 总行数:', len(lines))
bad = 0
for idx, line in enumerate(lines):
    s = line.strip()
    if not s or s.startswith('const quiz'):
        continue
    # 检查引号配对（去掉转义）
    if s.count('"') % 2 != 0:
        print('引号不成对 行', idx, ':', s[:80])
        bad += 1
        continue
    # 检查结构 { q: "...", opts: [...], ans: N },
    if not re.match(r'\{ q: ".*", opts: \[.*\], ans: \d+ \},?$', s):
        print('格式异常 行', idx, ':', s[:100])
        bad += 1
print('异常行数:', bad)
