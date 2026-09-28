"""Builds the MoneyHoney bus stop banner set as standalone HTML files.

Scale: 100px = 1 foot. render.js exports each file to a true-size PDF.
"""
import base64
import pathlib
import re

import segno

HERE = pathlib.Path(__file__).parent
PHONE_DISPLAY = "+91 77380 32704"
PHONE_TEL = "+917738032704"

FONTS = (HERE / "fonts" / "fonts.css").read_text()
LOGO = base64.b64encode((HERE / "moneyhoney-logo.png").read_bytes()).decode()


def qr_svg():
    q = segno.make(f"tel:{PHONE_TEL}", error="h")
    svg = q.svg_inline(dark="#1B2666", light=None, border=0)
    size = q.symbol_size(border=0)[0]
    # Make it scale with its container
    svg = re.sub(r'width="\d+" height="\d+"',
                 f'viewBox="0 0 {size} {size}" width="100%" height="100%" shape-rendering="crispEdges"',
                 svg, count=1)
    return svg


QR = qr_svg()

PHONE_ICON = """<svg viewBox="0 0 24 24" class="ico" aria-hidden="true"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>"""

SERVICES = ["Mutual Funds", "Fixed Deposits", "Debentures", "Gov. Bonds",
            "Capital Gain Bonds", "SIF", "GIFT City"]

DISCLAIMER = ("This is an investor education and awareness initiative. All Mutual Fund investors have to go "
              "through a one-time KYC (Know Your Customer) process. Investors should deal only with Registered "
              "Mutual Fund Distributors (MFD). <b>Mutual Fund investments are subject to market risks, read all "
              "scheme related documents carefully.</b>")

BASE_CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
:root { --navy:#1B2666; --orange:#E8511A; --cream:#F4EFE9; --white:#FFFFFF; --dark:#0C1632; --muted:#5B6478; }
html, body { background:#8a8a8a; }
body { padding:24px; }
.banner { margin:0 auto; }
@media print { html, body { background:none; padding:0; } .banner { margin:0; } }
.banner { position:relative; overflow:hidden; font-family:'DM Sans', sans-serif; color:var(--navy);
  background:var(--white); flex:none; }
.serif { font-family:'Lora', serif; }
.o { color:var(--orange); }
.logo { display:block; }
.tagline { font-weight:700; letter-spacing:.18em; color:var(--orange); text-transform:uppercase; white-space:nowrap; }
.trusted { font-weight:700; color:var(--navy); white-space:nowrap; }
.ico { width:1em; height:1em; vertical-align:-0.12em; }
.qr { background:#fff; }
.qr svg { display:block; }
.services { display:flex; justify-content:center; align-items:center; flex-wrap:nowrap; white-space:nowrap; }
.services span.sep { color:var(--orange); opacity:.9; }
.disc { line-height:1.3; }
.disc b { font-weight:700; }
"""


def page(title, w, h, css, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
{FONTS}
{BASE_CSS}
.banner {{ width:{w}px; height:{h}px; }}
{css}
</style>
</head>
<body data-w="{w}" data-h="{h}">
<div class="banner">
{body}
</div>
</body>
</html>
"""


def services_html(sep=" | "):
    parts = []
    for i, s in enumerate(SERVICES):
        if i:
            parts.append('<span class="sep">|</span>')
        parts.append(f"<span>{s}</span>")
    return "".join(parts)


def logo_block(cls="brand"):
    return f"""<div class="{cls}">
  <img class="logo" src="data:image/png;base64,{LOGO}" alt="MoneyHoney">
  <div class="tagline">Think Big &bull; Act Fast</div>
  <div class="trusted">(Trusted Since 2007)</div>
</div>"""


# ---------------------------------------------------------------- FRONT 15x4
FRONT_CSS = """
.banner { display:grid; grid-template-columns: 540px 1fr 440px; grid-template-rows: 1fr 58px; }
.hook { grid-column:1; grid-row:1; padding:34px 0 0 44px; }
.hook .pre { font-size:23px; font-weight:700; letter-spacing:.16em; color:var(--muted); text-transform:uppercase; }
.hook h1 { font-family:'Lora',serif; font-weight:700; font-size:66px; line-height:1.02; margin-top:12px; }
.hook h1 .line { display:block; }
.hook .arrow { display:flex; align-items:center; margin-top:18px; gap:14px; font-size:22px; font-weight:700; }
.hook .arrow i { display:block; height:6px; width:150px; background:var(--orange); position:relative; }
.hook .arrow i::after { content:''; position:absolute; right:-4px; top:-9px; border-left:22px solid var(--orange);
  border-top:12px solid transparent; border-bottom:12px solid transparent; }
.mid { grid-column:2; grid-row:1; display:flex; align-items:center; justify-content:center;
  border-left:5px solid var(--orange); margin:44px 0 30px; }
.brand { text-align:center; }
.brand .logo { height:92px; margin:0 auto; }
.brand .tagline { font-size:22px; margin-top:10px; }
.brand .trusted { font-size:22px; margin-top:4px; }
.cta { grid-column:3; grid-row:1; background:var(--navy); color:#fff; display:flex; flex-direction:column;
  justify-content:center; padding:0 30px; position:relative; }
.cta .ask { font-size:20px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--orange); }
.cta .num { font-size:46px; font-weight:800; line-height:1.05; margin-top:6px; white-space:nowrap; letter-spacing:-.01em; }
.cta .num .ico { color:var(--orange); }
.cta .row { display:flex; align-items:center; gap:18px; margin-top:18px; }
.cta .qr { width:112px; height:112px; padding:8px; border-radius:8px; flex:none; }
.cta .row p { font-size:19px; line-height:1.3; }
.cta .row p b { color:var(--orange); }
.strip { grid-column:1 / 4; grid-row:2; background:var(--orange); color:#fff; display:flex; flex-direction:column;
  justify-content:center; }
.strip .services { font-size:26px; font-weight:700; gap:22px; }
.strip .services .sep { color:rgba(255,255,255,.7); }
.foot { position:absolute; left:44px; right:420px; bottom:66px; display:flex; justify-content:space-between;
  align-items:flex-end; font-size:14px; }
.foot .amfi { font-weight:500; }
.foot .amfi b { font-weight:800; }
.disc { position:absolute; left:0; right:0; bottom:3px; text-align:center; font-size:8.6px; color:rgba(255,255,255,.95); }
"""

FRONT_BODY = f"""
<div class="hook">
  <div class="pre">Waiting for your bus?</div>
  <h1><span class="line">Your money</span><span class="line">shouldn&rsquo;t <span class="o">wait.</span></span></h1>
  <div class="arrow"><span>NEXT STOP: <span class="o">WEALTH CREATION</span></span><i></i></div>
</div>
<div class="mid">{logo_block()}</div>
<div class="cta">
  <div class="ask">One call.<br>Free portfolio review.</div>
  <div class="num">{PHONE_ICON} {PHONE_DISPLAY[4:]}</div>
  <div class="row">
    <div class="qr">{QR}</div>
    <p><b>Scan to call</b><br>or dial +91 77380 32704<br>Mon&ndash;Sat</p>
  </div>
</div>
<div class="foot"><div class="amfi">AMFI Registered Mutual Fund Distributor &nbsp;<span class="o">|</span>&nbsp; <b>ARN NO-60930</b></div></div>
<div class="strip">
  <div class="services">{services_html()}</div>
</div>
<div class="disc">{DISCLAIMER}</div>
"""

# ---------------------------------------------------------------- SIDE 4x4 (shared layout)
SIDE_CSS = """
.banner { display:flex; flex-direction:column; }
.top { height:70px; display:flex; align-items:center; justify-content:center; background:#fff;
  border-bottom:5px solid var(--orange); }
.top .logo { height:48px; }
.body { flex:1; min-height:0; background:var(--navy); color:#fff; padding:18px 28px 0; display:flex; flex-direction:column; }
.pre { font-size:15px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:var(--orange); }
h1 { font-family:'Lora',serif; font-weight:700; font-size:31px; line-height:1.12; margin-top:6px; }
.sub { font-size:15px; line-height:1.35; margin-top:8px; color:rgba(255,255,255,.85); }
.callrow { display:flex; align-items:center; gap:16px; margin-top:auto; margin-bottom:12px; }
.qr { width:88px; height:88px; padding:7px; border-radius:7px; flex:none; }
.call .lbl { font-size:14px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--orange); }
.call .num { font-size:30px; font-weight:800; line-height:1.05; white-space:nowrap; }
.call .num .ico { color:var(--orange); }
.call .scan { font-size:13px; color:rgba(255,255,255,.75); margin-top:3px; }
.foot { background:var(--orange); color:#fff; padding:5px 12px 6px; text-align:center; }
.foot .amfi { font-size:12px; font-weight:700; }
.foot .disc { font-size:7.4px; margin-top:2px; }
"""


def side_body(pre, h1, sub):
    return f"""
<div class="top"><img class="logo" src="data:image/png;base64,{LOGO}" alt="MoneyHoney"></div>
<div class="body">
  <div class="pre">{pre}</div>
  <h1>{h1}</h1>
  <div class="sub">{sub}</div>
  <div class="callrow">
    <div class="qr">{QR}</div>
    <div class="call">
      <div class="lbl">Call now</div>
      <div class="num">{PHONE_ICON} {PHONE_DISPLAY[4:]}</div>
      <div class="scan">Scan the code to call &bull; +91</div>
    </div>
  </div>
</div>
<div class="foot">
  <div class="amfi">AMFI Registered Mutual Fund Distributor | ARN NO-60930 | Trusted Since 2007</div>
  <div class="disc">Mutual Fund investments are subject to market risks, read all scheme related documents carefully.</div>
</div>
"""


LEFT_BODY = side_body(
    "Waiting for the bus?",
    'Your savings are<br>waiting too.<br><span class="o">Put them to work.</span>',
    "Funds, FDs, bonds: one advisor for all of it.")

RIGHT_BODY = side_body(
    "Sold a property?",
    'Save tax on your<br><span class="o">capital gains.</span>',
    "Ask us about <b>54EC Capital Gain Bonds</b>.<br>Invest within 6 months of the sale.")

# ---------------------------------------------------------------- BACKDROP 12x4
BACK_CSS = """
.banner { background:var(--cream); display:grid; grid-template-columns: 1fr 380px; grid-template-rows: 1fr 62px; }
.main { grid-column:1; grid-row:1; padding:26px 36px 0 40px; display:flex; flex-direction:column; }
.head { display:flex; align-items:center; justify-content:space-between; }
.head .logo { height:56px; }
.head .tagline { font-size:16px; text-align:right; }
.head .trusted { font-size:16px; text-align:right; }
h1 { font-family:'Lora',serif; font-weight:700; font-size:40px; line-height:1.1; margin-top:14px; }
.reasons { display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin-top:16px; }
.r { background:#fff; border-left:5px solid var(--orange); border-radius:10px; padding:12px 14px;
  box-shadow:0 2px 8px rgba(27,38,102,.06); display:flex; gap:10px; }
.r .n { font-family:'Lora',serif; font-weight:700; font-size:28px; color:var(--orange); line-height:1; }
.r .t { font-size:18px; font-weight:700; line-height:1.15; }
.r .s { font-size:13px; color:var(--muted); margin-top:3px; line-height:1.3; }
.side { grid-column:2; grid-row:1; background:var(--navy); color:#fff; padding:28px 30px 0; display:flex;
  flex-direction:column; align-items:center; text-align:center; }
.side .snap { font-size:15px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--orange); }
.side .num { font-size:40px; font-weight:800; margin-top:8px; white-space:nowrap; }
.side .num .ico { color:var(--orange); }
.side .qr { width:124px; height:124px; padding:9px; border-radius:8px; margin-top:14px; }
.side .scan { font-size:15px; margin-top:8px; }
.side .hrs { font-size:15px; margin-top:auto; margin-bottom:14px; color:rgba(255,255,255,.75); }
.side .scan b { color:var(--orange); }
.strip { grid-column:1 / 3; grid-row:2; background:var(--orange); color:#fff; display:flex; flex-direction:column;
  justify-content:center; }
.strip .services { font-size:21px; font-weight:700; gap:16px; }
.strip .services .sep { color:rgba(255,255,255,.7); }
.disc { font-size:7.6px; text-align:center; margin-top:2px; padding:0 20px; }
.amfi { font-size:13px; margin-top:auto; margin-bottom:10px; }
.amfi b { font-weight:800; }
"""

BACK_BODY = f"""
<div class="main">
  <div class="head">
    <img class="logo" src="data:image/png;base64,{LOGO}" alt="MoneyHoney">
    <div><div class="tagline">Think Big &bull; Act Fast</div><div class="trusted">(Trusted Since 2007)</div></div>
  </div>
  <h1>You have a few minutes.<br><span class="o">Let&rsquo;s talk about your next 20 years.</span></h1>
  <div class="reasons">
    <div class="r"><div class="n">01</div><div><div class="t">Trusted since 2007</div><div class="s">Families have relied on us for years.</div></div></div>
    <div class="r"><div class="n">02</div><div><div class="t">One advisor, every option</div><div class="s">MFs, FDs, bonds, SIF &amp; GIFT City in one place.</div></div></div>
    <div class="r"><div class="n">03</div><div><div class="t">Free portfolio review</div><div class="s">Share your goal, get a clear plan. No charge.</div></div></div>
  </div>
  <div class="amfi">AMFI Registered Mutual Fund Distributor &nbsp;<span class="o">|</span>&nbsp; <b>ARN NO-60930</b></div>
</div>
<div class="side">
  <div class="snap">Take a photo of this number</div>
  <div class="num">{PHONE_ICON} {PHONE_DISPLAY[4:]}</div>
  <div class="qr">{QR}</div>
  <div class="scan"><b>Scan to call</b> &bull; +91 77380 32704</div>
  <div class="hrs">Call Mon&ndash;Sat &bull; Free portfolio review</div>
</div>
<div class="strip">
  <div class="services">{services_html()}</div>
  <div class="disc">{DISCLAIMER}</div>
</div>
"""

FILES = {
    "front-15x4.html": ("MoneyHoney Bus Stop Front", 1500, 400, FRONT_CSS, FRONT_BODY),
    "side-left-4x4.html": ("MoneyHoney Bus Stop Left", 400, 400, SIDE_CSS, LEFT_BODY),
    "side-right-4x4.html": ("MoneyHoney Bus Stop Right", 400, 400, SIDE_CSS, RIGHT_BODY),
    "backdrop-12x4.html": ("MoneyHoney Bus Stop Backdrop", 1200, 400, BACK_CSS, BACK_BODY),
}

if __name__ == "__main__":
    for name, (title, w, h, css, body) in FILES.items():
        (HERE / name).write_text(page(title, w, h, css, body))
        print("wrote", name)
