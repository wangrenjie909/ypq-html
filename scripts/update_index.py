# -*- coding: utf-8 -*-
import re

html = open('index.html', encoding='utf-8').read()

# ========== 1. 游戏 HTML → 入口卡片 ==========
start_marker = '    <div class="game-box" style="border: 2px solid #ffd700;">'
end_marker = '    <section id="contact">'
si = html.find(start_marker)
ei = html.find(end_marker)
if si == -1 or ei == -1:
    print('游戏区标记未找到!', si, ei)
else:
    entry = '''    <div class="game-box" style="border: 3px solid #ffd700; max-width: 460px;">
        <p style="font-size: 40px; margin: 4px 0;">🎮</p>
        <h3>游戏厅</h3>
        <p style="font-size: 16px;">斗地主、带球过人、猜数字、翻牌、石头剪刀布、投篮、1000题问答……全部游戏都在这里！</p>
        <p style="margin-top: 12px;"><a href="games.html" class="portal game-btn" style="text-decoration: none;">🕹️ 点我进入游戏厅</a></p>
    </div>
'''
    html = html[:si] + entry + html[ei:]

# ========== 2. 删除游戏 JS ==========
js_start = html.find('<script>') + len('<script>')
js_end = html.find('</script>')
js = html[js_start:js_end]

FUNCS = ["loadBest", "celebrate", "shuffleQuiz", "play", "shoot", "memStart", "memRender", "memClick",
         "guessNum", "numReset", "ddzStart", "ddzInfo", "ddzRender", "ddzPlay", "ddzPass", "ddzCompTurn",
         "dgMsg", "dgGen", "dgStart", "dgNext", "dgRetry", "dgBtn", "dgLoop", "dgDraw",
         "showQuiz", "answerQuiz", "nextQuiz"]

VARS = ["bestRps", "bestShot", "bestQuiz", "rpsStreak", "wins", "losses", "draws", "rpsNames",
        "score", "shots", "memCards", "memFlip", "memMatched", "memPairs", "memMoves", "memLock",
        "numTarget", "numCount", "DDZ_POINT", "ddzPlayer", "ddzComputer", "ddzLast",
        "dgP", "dgDef", "dgKeys", "dgLevel", "dgRun", "dgState", "qi", "qscore"]

def remove_func(src, name):
    m = re.search(r'function\s+' + re.escape(name) + r'\s*\(', src)
    if not m:
        return src
    brace = src.find('{', m.end())
    depth = 0
    for i in range(brace, len(src)):
        if src[i] == '{':
            depth += 1
        elif src[i] == '}':
            depth -= 1
            if depth == 0:
                return src[:m.start()] + src[i + 1:]
    return src

# 删函数
for fn in FUNCS:
    js = remove_func(js, fn)

# 删变量行
for v in VARS:
    js = re.sub(r'^(?:\s*)(let|const)\s+' + re.escape(v) + r'\s*=[^;]*;\s*$', '', js, count=1, flags=re.M)

# 删 quiz 数组
js = re.sub(r'const quiz = \[.*?\];', '', js, count=1, flags=re.S)

# 删顶层调用
for call in ["memStart();", "dgStart();", "dgLoop();", "showQuiz();", "shuffleQuiz(quiz);", "shuffleQuiz(quiz);\nshowQuiz();"]:
    js = js.replace(call, '')

# 清理多余空行
js = re.sub(r'\n{3,}', '\n\n', js)

html = html[:js_start] + js + html[js_end:]
open('index.html', 'w', encoding='utf-8').write(html)
print('index.html 已更新')
