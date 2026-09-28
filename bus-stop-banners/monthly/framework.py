"""Shared building blocks for the monthly bus stop campaigns.

Each page lives at monthly/<lang>/<NN-mon>/<panel>.html and links assets from monthly/assets/.
Scale: 100px = 1 foot.
"""
import pathlib
import re
import urllib.parse

import segno

ROOT = pathlib.Path(__file__).parent
ASSETS = "../../assets"
PHONE = "77380 32704"
WA_NUMBER = "917738032704"

SIZES = {"front": (1500, 400, "front-15x4"), "left": (400, 400, "side-left-4x4"),
         "right": (400, 400, "side-right-4x4"), "back": (1200, 400, "backdrop-12x4")}

TEXT = {
    "en": dict(
        amfi="AMFI Registered Mutual Fund Distributor | ARN NO-60930",
        warn="Mutual Fund investments are subject to market risks, read all scheme related documents carefully.",
        full="This is an investor education and awareness initiative. All Mutual Fund investors have to go through "
             "a one-time KYC (Know Your Customer) process. Investors should deal only with Registered Mutual Fund "
             "Distributors (MFD).",
        since="Trusted Since 2008", scan="Scan &amp; say hi"),
    "hi": dict(
        amfi="AMFI पंजीकृत म्यूचुअल फंड वितरक | ARN NO-60930",
        warn="म्यूचुअल फंड निवेश बाज़ार जोखिमों के अधीन हैं, योजना संबंधी सभी दस्तावेज़ ध्यान से पढ़ें।",
        full="यह निवेशक शिक्षा एवं जागरूकता पहल है। सभी म्यूचुअल फंड निवेशकों को एक बार KYC (अपने ग्राहक को "
             "जानिए) प्रक्रिया पूरी करनी होती है। निवेशकों को केवल पंजीकृत म्यूचुअल फंड वितरक (MFD) से ही "
             "लेन-देन करना चाहिए।",
        since="2008 से भरोसेमंद", scan="स्कैन करें, बात करें"),
}

PHONE_SVG = ('<svg viewBox="0 0 24 24" class="ico" aria-hidden="true"><path fill="currentColor" d="M6.6 10.8a15.1 '
             '15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 '
             '17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>')

BASE_CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
:root { --navy:#1B2666; --orange:#E8511A; --cream:#F4EFE9; --ink:#0C1632; --muted:#5B6478; --gold:#F6B53D; }
body.en { --display:'Lora', serif; --sans:'DM Sans', sans-serif; --hand:'Caveat', cursive; --dw:700; --lt:1.04; }
body.hi { --display:'Mukta', sans-serif; --sans:'Mukta', sans-serif; --hand:'Kalam', cursive; --dw:800; --lt:1.16; }
html, body { background:#8a8a8a; }
body { padding:24px; font-family:var(--sans); }
@media print { html, body { background:none; padding:0; } .banner { margin:0 !important; } }
.banner { position:relative; overflow:hidden; margin:0 auto; display:flex; flex-direction:column; color:var(--navy); }
.stage { position:relative; flex:1; min-height:0; overflow:hidden; }
.d { font-family:var(--display); font-weight:var(--dw); line-height:var(--lt); }
.s { font-family:var(--sans); }
.h { font-family:var(--hand); font-weight:700; }
.o { color:var(--orange); }
body.hi * { letter-spacing:0 !important; }
.g { color:var(--gold); }
.w { color:#fff; }
.n { color:var(--navy); }
.call { display:inline-flex; align-items:center; gap:.28em; font-family:'DM Sans', sans-serif; font-weight:800;
  white-space:nowrap; letter-spacing:-.01em; line-height:1; }
.call .ico { width:.78em; height:.78em; color:var(--orange); flex:none; }
.call.onorange .ico { color:#fff; }
.logo img { display:block; height:100%; width:auto; }
.logo.chip { background:#fff; border-radius:8px; padding:5px 10px; }
.qrb { display:flex; flex-direction:column; align-items:center; }
.qrb .qr { background:#fff; padding:7px; border-radius:8px; }
.qrb .qr svg { display:block; }
.qrb .qrl { font-weight:700; margin-top:5px; white-space:nowrap; }
.legal { flex:none; text-align:center; line-height:1.3; padding:3px 14px 4px; font-family:var(--sans); }
.legal b { font-weight:700; }
.legal .fn { opacity:.85; }
.legal.dark { background:var(--ink); color:rgba(255,255,255,.88); }
.legal.navy { background:var(--navy); color:rgba(255,255,255,.88); }
.legal.light { background:#fff; color:var(--muted); border-top:1px solid #E0D8CE; }
.legal.cream { background:var(--cream); color:var(--muted); border-top:1px solid #E0D8CE; }
.legal.orange { background:var(--orange); color:#fff; }
"""

LEGAL_SIZE = {"front": 8.6, "back": 7.6, "left": 6.6, "right": 6.6}


def qr_svg(message, color="#1B2666"):
    url = f"https://wa.me/{WA_NUMBER}?text={urllib.parse.quote(message)}"
    q = segno.make(url, error="m")
    n = q.symbol_size(border=0)[0]
    svg = q.svg_inline(dark=color, light=None, border=0)
    return re.sub(r'width="\d+" height="\d+"',
                  f'viewBox="0 0 {n} {n}" width="100%" height="100%" shape-rendering="crispEdges"', svg, count=1)


def call(size, cls=""):
    return f'<div class="call {cls}" style="font-size:{size}px">{PHONE_SVG}<span>{PHONE}</span></div>'


def logo(height, chip=False, style=""):
    return (f'<div class="logo{" chip" if chip else ""}" style="height:{height + (12 if chip else 0)}px;{style}">'
            f'<img src="{ASSETS}/logo.png" alt="MoneyHoney"></div>')


def qr_block(lang, message, size, label_size=13, color="#1B2666", label_color="inherit"):
    return (f'<div class="qrb"><div class="qr" style="width:{size}px;height:{size}px">{qr_svg(message, color)}</div>'
            f'<div class="qrl" style="font-size:{label_size}px;color:{label_color}">{TEXT[lang]["scan"]}</div></div>')


def legal(lang, panel, theme, note=""):
    t = TEXT[lang]
    parts = [f'<div><b>{t["amfi"]}</b> &middot; {t["warn"]}</div>']
    if panel in ("front", "back"):
        parts.append(f'<div>{t["full"]}</div>')
    if note:
        parts.append(f'<div class="fn">{note}</div>')
    return f'<div class="legal {theme}" style="font-size:{LEGAL_SIZE[panel]}px">{"".join(parts)}</div>'


def page(lang, title, w, h, css, stage, legal_html, bg):
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{ASSETS}/fonts.css">
<style>
{BASE_CSS}
.banner {{ width:{w}px; height:{h}px; background:{bg}; }}
{css}
</style>
</head>
<body class="{lang}" data-w="{w}" data-h="{h}">
<div class="banner">
<div class="stage">
{stage}
</div>
{legal_html}
</div>
</body>
</html>
"""
