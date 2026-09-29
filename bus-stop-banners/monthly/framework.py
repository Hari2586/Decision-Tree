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
LEGAL_EN = dict(
    amfi="AMFI Registered Mutual Fund Distributor | ARN NO-60930",
    warn="Mutual Fund investments are subject to market risks, read all scheme related documents carefully.",
    full="This is an investor education and awareness initiative. All Mutual Fund investors have to go through "
         "a one-time KYC (Know Your Customer) process. Investors should deal only with Registered Mutual Fund "
         "Distributors (MFD).",
    nonmf="Fixed Deposits, Debentures, Gov. Bonds, Capital Gain Bonds and GIFT City products are not Mutual Fund products.",
    since="Since 2008",
    products=["Mutual Funds", "Fixed Deposits", "Debentures", "Gov. Bonds", "Capital Gain Bonds", "SIF", "GIFT City"])
TEXT = {"en": dict(LEGAL_EN, scan="Scan &amp; say hi"),
        "hi": dict(LEGAL_EN, scan="स्कैन करें, बात करें")}

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
.band { flex:none; height:40px; display:flex; align-items:center; gap:22px; padding:0 40px 0 0; background:var(--navy);
  color:#fff; border-top:3px solid var(--orange); font-family:var(--sans); }
.band .since { height:100%; display:flex; align-items:center; background:var(--orange); padding:0 22px 0 40px;
  font-weight:800; font-size:19px; white-space:nowrap; clip-path:polygon(0 0,100% 0,calc(100% - 16px) 100%,0 100%); padding-right:34px; }
.band .prods { flex:1; display:flex; justify-content:space-between; align-items:center; font-weight:700; font-size:19px; white-space:nowrap; }
.band .sep { color:var(--orange); }
.warn { flex:none; height:44px; display:flex; align-items:center; justify-content:center; text-align:center;
  background:#fff; color:#0C1632; font-family:'DM Sans', sans-serif; font-weight:800; line-height:1.15; padding:0 14px;
  border-top:3px solid var(--orange); }
.legal { flex:none; text-align:center; line-height:1.3; padding:3px 14px 4px; font-family:var(--sans); }
.legal b { font-weight:700; }
.legal .fn { opacity:.85; }
.legal.dark { background:var(--ink); color:rgba(255,255,255,.88); }
.legal.navy { background:var(--navy); color:rgba(255,255,255,.88); }
.legal.light { background:#fff; color:var(--muted); border-top:1px solid #E0D8CE; }
.legal.cream { background:var(--cream); color:var(--muted); border-top:1px solid #E0D8CE; }
.legal.orange { background:var(--orange); color:#fff; }
"""

LEGAL_SIZE = {"front": 8.6, "back": 7.6, "side": 6.8}
WARN_SIZE = {"front": 21, "back": 17.5, "side": 13}

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
    """Standard warning in its own band (at least 10% of the panel height, large legible type),
    then the AMFI/ARN line, investor-education text and any footnote."""
    t = TEXT[lang]
    small = [f'<b>{t["since"]} &middot; {t["amfi"]}</b>']
    if panel in ("front", "back"):
        small.append(t["full"])
    if panel == "front":
        small.append(t["nonmf"])
    lines = f'<div>{" &middot; ".join(small)}</div>' + (f'<div class="fn">{note}</div>' if note else "")
    return (f'<div class="warn" style="font-size:{WARN_SIZE[panel]}px">{t["warn"]}</div>'
            f'<div class="legal {theme}" style="font-size:{LEGAL_SIZE[panel]}px">{lines}</div>')


def products_band(lang):
    t = TEXT[lang]
    items = '<span class="sep">|</span>'.join(f"<span>{p}</span>" for p in t["products"])
    return f'<div class="band"><div class="since">&#9733; {t["since"]}</div><div class="prods">{items}</div></div>'


def page(lang, title, w, h, css, stage, legal_html, bg, band=""):
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
{band}
{legal_html}
</div>
</body>
</html>
"""
