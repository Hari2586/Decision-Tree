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
PHONE = "74000 60800"
WA_NUMBER = "917400060800"

SIZES = {"front": (1500, 400, "front-15x4"), "side": (400, 400, "side-4x4"), "back": (1200, 400, "backdrop-12x4")}

# Compliance text stays in English on the Hindi banners too (only the creative copy is translated).
LEGAL = dict(
    amfi="AMFI Registered Mutual Fund Distributor | ARN NO-60930",
    warn="Mutual Fund investments are subject to market risks, read all scheme related documents carefully.",
    since="Since 2008",
    products=["Mutual Funds", "Fixed Deposits", "Debentures", "Gov. Bonds", "Capital Gain Bonds", "SIF", "GIFT City"])
SCAN = {"en": "Scan &amp; say hi", "hi": "स्कैन करें, बात करें"}

PHONE_SVG = ('<svg viewBox="0 0 24 24" class="ico" aria-hidden="true"><path fill="currentColor" d="M6.6 10.8a15.1 '
             '15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 '
             '17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>')

BASE_CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
:root { --navy:#16205B; --orange:#FF4A00; --cream:#F4EFE9; --warm:#FDFBF7; --ink:#0D1440;
  --muted:color-mix(in srgb, #16205B 72%, #ffffff); --lmuted:#B0B8C5; --line:#E0D8CE; }
body.en { --display:'Lora', serif; --sans:'DM Sans', sans-serif; --hand:'Caveat', cursive; --dw:700; --lt:1.06; }
body.hi { --display:'Mukta', sans-serif; --sans:'Mukta', sans-serif; --hand:'Kalam', cursive; --dw:800; --lt:1.2; }
html, body { background:#8a8a8a; }
body { padding:24px; font-family:var(--sans); }
@media print { html, body { background:none; padding:0; } .banner { margin:0 !important; } }
.banner { position:relative; overflow:hidden; margin:0 auto; display:flex; flex-direction:column; color:var(--navy); }
.stage { position:relative; flex:1; min-height:0; overflow:hidden; }
.d { font-family:var(--display); font-weight:var(--dw); line-height:var(--lt); }
.stage div { text-wrap-style:pretty; }
.stage .d, .stage .hl, .stage .h1 { text-wrap-style:balance; }
.stage .cal div { text-wrap-style:auto; }
.s { font-family:var(--sans); }
.h { font-family:var(--hand); font-weight:700; }
.o { color:var(--orange); }
body.hi *:not(.lat) { letter-spacing:0 !important; }
.w { color:#fff; }
.n { color:var(--navy); }
.call { display:inline-flex; align-items:center; gap:.28em; font-family:'DM Sans', sans-serif; font-weight:800;
  white-space:nowrap; letter-spacing:-.01em; line-height:1; }
.call .ico { width:.78em; height:.78em; color:var(--orange); flex:none; }
.call.onorange .ico { color:#fff; }
.logo img { display:block; height:100%; width:auto; }
.logo.chip { background:#fff; border-radius:8px; padding:5px 10px; }
.qrb { display:flex; flex-direction:column; align-items:center; }
.qrb .qr { background:#fff; padding:10px; border-radius:8px; }
.qrb .qr svg { display:block; }
.qrb .qrl { font-weight:700; margin-top:5px; white-space:nowrap; }
.pband { flex:none; height:42px; display:flex; align-items:center; gap:22px; padding:0 40px 0 0; background:var(--navy);
  color:#fff; border-top:3px solid var(--orange); font-family:var(--sans); }
.pband .since { height:100%; display:flex; align-items:center; background:var(--orange); padding:0 22px 0 40px;
  font-weight:800; font-size:19px; white-space:nowrap; clip-path:polygon(0 0,100% 0,calc(100% - 16px) 100%,0 100%); padding-right:34px; }
.pband .prods { flex:1; display:flex; justify-content:space-between; align-items:center; font-weight:700; font-size:19px; white-space:nowrap; }
.pband .sep { color:var(--orange); }
.lockup { display:inline-flex; align-items:center; gap:calc(var(--lh) * .34); }
.lockup img { display:block; height:var(--lh); width:auto; }
.lockup .since { font-family:'DM Sans', sans-serif; font-weight:700; font-size:calc(var(--lh) * .44); color:var(--navy);
  line-height:1; white-space:nowrap; padding-left:calc(var(--lh) * .34); border-left:2px solid var(--orange); }
.lockup.chip { background:#fff; border-radius:8px; padding:6px 12px; }
.scta { position:absolute; display:flex; align-items:center; gap:14px; }
.scta .qr { flex:none; background:#fff; padding:8px; border-radius:8px; box-shadow:0 0 0 1.5px var(--line); }
.scta .qr svg { display:block; }
.scta .call .ico { color:var(--ico); }
.scta .sl { font-weight:700; opacity:.85; margin-bottom:6px; white-space:nowrap; }
.cz { flex:none; background:#fff; text-align:center; font-family:'DM Sans', sans-serif; border-top:3px solid var(--orange); }
.cz-w { color:#000; font-weight:700; line-height:1.22; text-wrap-style:balance; }
.cz-m { color:var(--navy); display:flex; flex-wrap:wrap; justify-content:center; column-gap:1.4em; row-gap:.2em; line-height:1.3; }
.cz-m b { font-weight:700; }
.cz-m .fn { color:var(--muted); text-wrap-style:balance; }
.cz-front { border-top:0; padding:8px 40px 8px; } .cz-front .cz-w { font-size:21px; } .cz-front .cz-m { font-size:10.5px; margin-top:5px; }
.cz-back { padding:8px 36px 8px; } .cz-back .cz-w { font-size:18.5px; } .cz-back .cz-m { font-size:9.6px; margin-top:4px; }
.cz-side { padding:7px 14px 7px; } .cz-side .cz-w { font-size:12.6px; } .cz-side .cz-m { font-size:7.8px; margin-top:4px; }
"""


def qr_svg(message, color="#16205B"):
    url = f"https://wa.me/{WA_NUMBER}?text={urllib.parse.quote(message, safe='!,.:?')}"
    q = segno.make(url, error="m")
    n = q.symbol_size(border=0)[0]
    svg = q.svg_inline(dark=color, light=None, border=0)
    return re.sub(r'width="\d+" height="\d+"',
                  f'viewBox="0 0 {n} {n}" width="100%" height="100%" shape-rendering="crispEdges"', svg, count=1)


def call(size, cls=""):
    return f'<div class="call {cls}" style="font-size:{size}px">{PHONE_SVG}<span>{PHONE}</span></div>'


def logo(height, chip=False, style=""):
    return (f'<div class="logo{" chip" if chip else ""}" style="height:{height + (12 if chip else 0)}px;{style}">'
            f'<img src="{ASSETS}/logo.svg" alt="MoneyHoney"></div>')


def lockup(height, chip=False, style=""):
    """Logo with the 'Since 2008' tag beside it."""
    return (f'<div class="lockup{" chip" if chip else ""}" style="--lh:{height}px;{style}">'
            f'<img src="{ASSETS}/logo.svg" alt="MoneyHoney"><span class="since lat">{LEGAL["since"]}</span></div>')


def qr_block(lang, message, size, label_size=13, color="#16205B", label_color="inherit"):
    return (f'<div class="qrb"><div class="qr" style="width:{size}px;height:{size}px">{qr_svg(message, color)}</div>'
            f'<div class="qrl" style="font-size:{label_size}px;color:{label_color}">{SCAN[lang]}</div></div>')


def side_cta(lang, message, pos="left:24px; bottom:14px;", qr=86, num=30, color="inherit", icon="var(--orange)"):
    """QR + 'scan' label + phone number, the call-to-action block of every side panel."""
    return (f'<div class="scta" style="{pos} color:{color}; --ico:{icon}"><div class="qr" style="width:{qr}px;height:{qr}px">'
            f'{qr_svg(message)}</div><div><div class="sl" style="font-size:{max(12, num * .45):.0f}px">{SCAN[lang]}</div>'
            f'{call(num)}</div></div>')


def footer(panel, note=""):
    """Compliance zone: the standard warning (black on white, bold) and the AMFI/ARN line with any footnote."""
    meta = f'<b>{LEGAL["amfi"]}</b>' + (f'<span class="fn">{note}</span>' if note else "")
    return f'<div class="cz cz-{panel}"><div class="cz-w">{LEGAL["warn"]}</div><div class="cz-m">{meta}</div></div>'


def products_band():
    items = '<span class="sep">|</span>'.join(f"<span>{p}</span>" for p in LEGAL["products"])
    return f'<div class="pband"><div class="since">&#9733; {LEGAL["since"]}</div><div class="prods">{items}</div></div>'


def page(lang, panel, title, w, h, css, stage, legal_html, bg, band=""):
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
<body class="{lang} p-{panel}" data-w="{w}" data-h="{h}">
<div class="banner">
<div class="stage">
{stage}
</div>
{band}
{legal_html}
</div>
</body>
</html>
"""
