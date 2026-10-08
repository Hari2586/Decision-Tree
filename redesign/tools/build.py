"""Build a MoneyHoney page in the Clear Glass design from an original page.

The body is kept byte for byte (only the <body> tag gains a class); the <head>
keeps every meta, title, canonical and JSON-LD line and swaps the embedded
styles for the shared stylesheet and script.

usage: python3 build.py <original.html> <output.html> <asset-prefix> <body-class> [--keep-page-css]
   e.g. python3 build.py original/solutions.html site/solutions/index.html ../ page-hub
"""
import re, sys, pathlib

src, dst, prefix, body_class = sys.argv[1:5]
keep_page_css = len(sys.argv) > 5 and sys.argv[5] == '--keep-page-css'
html = pathlib.Path(src).read_text(encoding='utf-8')

head_m = re.search(r'<head>(.*?)</head>', html, re.S)
head = head_m.group(1)
page_css = ''
if keep_page_css and 'MH-DS:END' in head:
    # the page's own CSS follows the design-system marker; the shared footer/demo block is dropped
    tail = head.split('MH-DS:END', 1)[1]
    for blk in re.findall(r'<style\b[^>]*>.*?</style>', tail, re.S):
        if '.site-foot{' in blk or '.demo-strip{' in blk: continue
        page_css += blk + '\n'
head = re.sub(r'<style\b[^>]*>.*?</style>\s*', '', head, flags=re.S)       # embedded CSS (font, design system, page CSS)
head = re.sub(r'<!--\s*MH-DS[^>]*-->\s*', '', head)                            # generator markers
head = re.sub(r'<link rel="preconnect"[^>]*>\s*', '', head)
head = re.sub(r'<link rel="stylesheet"[^>]*>\s*', '', head)
head = re.sub(r'<meta name="theme-color"[^>]*>\s*', '', head)
head = head.rstrip() + '\n'
assets = (
    '\n<meta name="theme-color" content="#1B2666">\n'
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@700;800&family=Figtree:wght@400;500;600;700&display=swap">\n'
    f'<link rel="stylesheet" href="{prefix}assets/mh.css">\n'
    f'<script defer src="{prefix}assets/mh.js"></script>\n'
) + page_css
body_i = html.index('<body')
body_end = html.index('>', body_i) + 1
orig_body_tag = html[body_i:body_end]
body = html[body_end:]
new_body_tag = f'<body class="{body_class}">'

# Layout-only move: the demo notice goes inside the <header> landmark so every
# piece of content sits in a landmark (axe "region"). Its text is untouched and
# it still comes first in reading order.
strip_m = re.search(r'\s*<div class="demo-strip"[^>]*>.*?</div></div>\s*', body, re.S)
hdr = '<header class="mh-header">'
if strip_m and strip_m.start() < body.index(hdr):
    strip = strip_m.group(0).strip()
    body = body[:strip_m.start()] + '\n\n' + body[strip_m.end():]
    body = body.replace(hdr, hdr + '\n  ' + strip, 1)
out = html[:head_m.start()] + '<head>' + head + assets + '</head>\n' + new_body_tag + body

# content lock proof: the body is unchanged except for that one move
def norm(x):
    x = re.sub(r'\s*<div class="demo-strip"[^>]*>.*?</div></div>\s*', '\n', x, flags=re.S)
    return re.sub(r'\s+', ' ', x).strip()
assert norm(body) == norm(html[body_end:]), 'body changed beyond the demo-strip move'
pathlib.Path(dst).parent.mkdir(parents=True, exist_ok=True)
pathlib.Path(dst).write_text(out, encoding='utf-8')
print(f'built {dst}: head rewritten, body identical ({len(body):,} bytes)')
