# -*- coding: utf-8 -*-
import re

html = open('index.html', encoding='utf-8').read()

# ========== 1. 提取游戏 HTML（排行榜 → 投篮挑战结束） ==========
start_marker = '    <div class="game-box" style="border: 2px solid #ffd700;">'
end_marker = '    <section id="contact">'
si = html.find(start_marker)
ei = html.find(end_marker)
game_html = html[si:ei].rstrip() + '\n'

# ========== 2. 提取完整 CSS ==========
css_start = html.find('<style>') + len('<style>')
css_end = html.find('</style>')
css = html[css_start:css_end].strip()

# ========== 3. 提取游戏 JS ==========
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

def extract_func(src, name):
    m = re.search(r'function\s+' + re.escape(name) + r'\s*\(', src)
    if not m:
        return ''
    brace = src.find('{', m.end())
    depth = 0
    for i in range(brace, len(src)):
        if src[i] == '{':
            depth += 1
        elif src[i] == '}':
            depth -= 1
            if depth == 0:
                return src[m.start():i + 1]
    return ''

# 提取函数
parts = []
for fn in FUNCS:
    f = extract_func(js, fn)
    if f:
        parts.append(f)
    else:
        print('WARN 函数未找到:', fn)

# 提取变量声明行
var_lines = []
for v in VARS:
    for m in re.finditer(r'^(?:\s*)(let|const)\s+' + re.escape(v) + r'\s*=[^;]*;', js, re.M):
        var_lines.append(m.group(0).strip())
        break

# 提取 quiz 数组（多行）
qm = re.search(r'const quiz = \[.*?\];', js, re.S)
quiz_block = qm.group(0) if qm else ''

# 顶层调用
calls = ["memStart();", "dgStart();", "dgLoop();", "showQuiz();", "shuffleQuiz(quiz);"]

game_js = '\n'.join(var_lines) + '\n\n' + quiz_block + '\n\n' + '\n'.join(parts) + '\n\n' + '\n'.join(calls)

# ========== 4. 生成 games.html ==========
games_html = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>热血篮球 · 游戏厅</title>
    <link rel="icon" href="images/basketball.jpg" type="image/jpeg">
    <style>
''' + css + '''
    </style>
</head>
<body style="text-align: center;">
    <div style="padding: 15px 10px;">
        <h1>🎮 热血篮球游戏厅</h1>
        <p>全部游戏都在这里，玩个痛快！</p>
        <a href="index.html" class="portal">🏠 返回主页</a>
    </div>
''' + game_html + '''
</body>
</html>
'''

# 把 JS 插入 </body> 前
games_html = games_html.replace('</body>', '<script>\n' + game_js + '\n</script>\n</body>')
open('games.html', 'w', encoding='utf-8').write(games_html)
print('games.html 已生成:', len(games_html), '字符')
print('函数提取:', sum(1 for fn in FUNCS if extract_func(js, fn)), '/', len(FUNCS))
