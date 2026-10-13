"""Build three home page versions from one locked content set.
usage: python3 versions.py <scratch-dir-with-home-head/header/footer> <out-dir>
Every string below is the home page's exact text; only layout, colour and imagery differ."""
import re, sys, pathlib, html as H
SP, OUT = sys.argv[1], sys.argv[2]
head = pathlib.Path(SP+'/home-head.html').read_text()
header = pathlib.Path(SP+'/home-header.html').read_text()
footer = pathlib.Path(SP+'/home-footer.html').read_text()
mhjs = pathlib.Path('redesign/site/assets/mh.js').read_text()
mhcss = pathlib.Path('redesign/site/assets/mh.css').read_text()
# icon rules reused from the live stylesheet (CSS only, no text)
prod_icons = '\n'.join(l.replace('.ledger a.card', 'a.card') for l in mhcss.splitlines() if l.startswith('.ledger a.card{--icon') or l.startswith('.ledger a.card['))
sol_icons = '\n'.join(l for l in mhcss.splitlines() if l.startswith('[href$=') and '--sicon' in l)
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@700;800&family=Figtree:wght@400;500;600;700&display=swap">'
head = re.sub(r'<link rel="preconnect"[^>]*>\s*|<link rel="stylesheet"[^>]*fonts.googleapis[^>]*>\s*', '', head).strip() + '\n' + FONTS

H1 = 'Mutual Funds, SIFs, Screens and Calculators'
LEDE = 'Facts on every open mutual fund scheme in India, organised by fund house, SEBI category, theme and index, with Specialised Investment Fund (SIF) strategies, calculators and rule-based fund screens. MoneyHoney is an AMFI-registered mutual fund and SIF distributor; nothing here is a recommendation.'
FACTS = [('Mutual Fund Schemes','1,774'),('Fund Houses','48'),('SEBI Categories','39'),('Data As On','31 Aug 2026')]
SOL_INTRO = 'Start from the problem you want to solve.'
SOL_CTA = ('See All Solutions','solutions/index.html')
SOLS = [('SIP','solutions/sip/index.html'),('Retirement','solutions/retirement/index.html'),('Child Education','solutions/child-education/index.html'),('Women and Money','solutions/women/index.html'),('NRI Investing','solutions/nri/index.html'),('Trusts','solutions/trusts/index.html'),('Building Wealth','solutions/wealth/index.html'),('Vacation Planning','solutions/vacation/index.html'),('Marriage Planning','solutions/marriage/index.html'),('EMI Management','solutions/emi-management/index.html'),('Emergency Fund','solutions/emergency-fund/index.html')]
START = [('Mutual Funds','1,774 schemes by category and fund house','mutual-funds/index.html'),('Explore Funds','Filter every scheme by category, cost and risk','mutual-funds/explore/index.html'),('Fund Screens','Rule-based lists such as index funds under 0.50% cost','mutual-funds/screens/index.html'),('Calculators','SIP, lumpsum, SWP, goal and tax calculators','calculators/index.html'),('New Fund Offers','Open, upcoming and recently closed NFOs','mutual-funds/nfo/index.html'),('Dividend History (IDCW)','Past IDCW record dates and amounts per unit, scheme by scheme','mutual-funds/dividend-history/index.html'),('Specialised Investment Funds','SIF strategies for investments of ₹10,00,000 or more','sif/index.html'),('NCD IPOs','Sample NCD public issues: series, ratings and how to apply','bonds/ncd/index.html'),('Capital Gain Bonds','Save tax on a property gain: REC, PFC and IRFC series','bonds/capital-gain-bonds/index.html'),('RBI Bonds','Government of India bonds, interest every six months','bonds/rbi-bonds/index.html'),('Fixed Deposits','Company and bank FDs we offer, with rates and terms for your investor type.','fixed-deposits/index.html')]
ASSET = [('Equity Funds','11 categories, 614 schemes','mutual-funds/asset/equity/index.html',614),('Debt Funds','16 categories, 434 schemes','mutual-funds/asset/debt/index.html',434),('Hybrid Funds','6 categories, 179 schemes','mutual-funds/asset/hybrid/index.html',179),('Index Funds and Other Schemes','4 categories, 506 schemes','mutual-funds/asset/index-and-other/index.html',506),('Solution Oriented Funds','2 categories, 41 schemes','mutual-funds/asset/solution-oriented/index.html',41)]
THEMES = [('Sector and Theme Funds','Sector and Theme Funds: Active and Index','mutual-funds/theme/index.html'),('Factor Funds','Factor Funds: Momentum, Quality and Value','mutual-funds/theme/factor/index.html'),('Index Funds and ETFs','Equity Index Funds and ETFs by Index','mutual-funds/index-funds/index.html'),('Target Maturity Funds','Target Maturity Funds by Maturity Year','mutual-funds/target-maturity/index.html'),('Open-Ended Debt Index Funds','Open-Ended Debt Index Funds and ETFs','mutual-funds/debt-index/index.html'),('International Funds','International Funds by Region','mutual-funds/international/index.html'),('Gold and Silver','Gold and Silver ETFs and FoFs by Metal','mutual-funds/gold-silver/index.html'),('Funds of Funds','Funds of Funds by Type','mutual-funds/fund-of-funds/index.html')]
CHEV = '<svg class="card__icon" aria-hidden="true" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M7 4l6 6-6 6"/></svg>'
e = H.escape
def card(t, m, h, extra=''): return f'<li><a class="card" href="{h}"{extra}><span class="card__title">{e(t)}</span><span class="card__meta">{e(m)}</span>{CHEV}</a></li>'
def facts(): return ''.join(f'<div class="stat"><dt class="stat__label">{l}</dt><dd class="stat__value">{v}</dd></div>' for l,v in FACTS)
def sols(): return ''.join(f'<li><a href="{h}">{e(t)}</a></li>' for t,h in SOLS)
def cards(items, cls='ledger'): return f'<ul class="{cls}">' + ''.join(card(t,m,h) for t,m,h,*_ in items) + '</ul>'
SPARK = '<svg class="spark" aria-hidden="true" viewBox="0 0 320 120" preserveAspectRatio="none"><defs><linearGradient id="g1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--spark)" stop-opacity=".35"/><stop offset="1" stop-color="var(--spark)" stop-opacity="0"/></linearGradient></defs><path d="M0 104 C40 100 60 92 90 84 S150 60 180 54 S240 34 270 24 S305 10 320 6 V120 H0 Z" fill="url(#g1)"/><path d="M0 104 C40 100 60 92 90 84 S150 60 180 54 S240 34 270 24 S305 10 320 6" fill="none" stroke="var(--spark)" stroke-width="2.5" stroke-linecap="round"/></svg>'

def page(title_class, css, body):
    return f'<!doctype html>\n<html lang="en-IN">\n<head>\n{head}\n<style>\n{css}\n{prod_icons}\n{sol_icons}\n</style>\n</head>\n<body class="page-home {title_class}">\n{header}\n{body}\n{footer}\n<script>\n{mhjs}\n</script>\n</body>\n</html>\n'

BASE = r'''
:root{--navy:#1B2666;--navy-2:#2A3A8F;--ink:#0F163F;--orange:#E8511A;--orange-ink:#C4410E;--orange-deep:#B03A0B;--orange-soft:#FFB28F;--honey:#FDEDE5;--wash:#F1F3FC;--band:#F5F6FC;--fill:#EEF0FA;--paper:#fff;--rule:#E1E4F0;--rule-2:#C9CFEA;--text:#141A3B;--meta:#5D637C;--on-navy-soft:#C9CFEA;--warn-bg:#FFFAEB;--warn-text:#B54708;--warn-rule:#FEDF89;
--display:"Manrope",system-ui,sans-serif;--sans:"Figtree",system-ui,sans-serif;--s1:4px;--s2:8px;--s3:12px;--s4:16px;--s5:20px;--s6:24px;--s8:32px;--s10:40px;--s12:48px;--s16:64px;--gutter:16px;--max:1120px;--r-btn:4px;--r-sm:6px;--r-md:8px;--r-lg:10px;--shadow:0 1px 2px rgba(20,26,59,.04),0 4px 14px -8px rgba(20,26,59,.10);--shadow-lift:0 10px 24px -12px rgba(27,38,102,.28);--ease:cubic-bezier(.22,1,.36,1);--d-fast:160ms;--d-med:320ms;--d-slow:640ms;--focus:0 0 0 3px var(--paper),0 0 0 5px var(--orange)}
@media (min-width:600px){:root{--gutter:24px}}@media (min-width:960px){:root{--gutter:32px}}
*,*::before,*::after{box-sizing:border-box}html{scroll-behavior:smooth}@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation:none!important;transition:none!important}}
body{margin:0;background:var(--paper);color:var(--text);font:400 16px/1.55 var(--sans);-webkit-font-smoothing:antialiased}
.container{width:100%;max-width:var(--max);margin-inline:auto;padding-inline:var(--gutter)}
a{color:var(--navy);text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px;text-decoration-color:var(--rule-2)}a:hover{text-decoration-color:currentColor}
:focus{outline:none}:focus-visible{box-shadow:var(--focus);border-radius:var(--r-btn)}
h1,h2{margin:0;font-family:var(--display);font-weight:800;color:var(--navy);text-wrap:balance;letter-spacing:-.02em}h1{font-size:clamp(30px,3.4vw + 17px,48px);line-height:1.06}h2{font-size:clamp(22px,1.2vw + 17px,28px);line-height:1.2;letter-spacing:-.015em}p{margin:0}
.demo-strip{background:var(--warn-bg);color:var(--warn-text);border-bottom:1px solid var(--warn-rule);font-size:14px;line-height:1.5;padding-block:var(--s2)}.demo-strip b{font-weight:700}
.mh-header{background:var(--paper);border-bottom:1px solid var(--rule)}.mh-header__inner{display:flex;flex-wrap:wrap;align-items:center;gap:0 var(--s6);min-height:60px}
.mh-logo{display:inline-flex;align-items:center;min-height:44px;padding-block:var(--s2);text-decoration:none;border-radius:var(--r-sm)}.mh-logo svg{display:block;height:22px;width:auto}
.mh-header__nav{order:3;width:100%;display:flex;gap:var(--s2);overflow-x:auto;scrollbar-width:none;margin-inline:calc(-1 * var(--gutter));padding:var(--s1) var(--gutter) var(--s3);mask-image:linear-gradient(90deg,transparent,#000 var(--gutter),#000 calc(100% - 32px),transparent);-webkit-mask-image:linear-gradient(90deg,transparent,#000 var(--gutter),#000 calc(100% - 32px),transparent)}
.mh-header__nav::-webkit-scrollbar{display:none}
.mh-header__nav a{flex:0 0 auto;display:inline-flex;align-items:center;min-height:44px;padding:0 var(--s4);border-radius:var(--r-sm);background:var(--fill);color:var(--navy);font-size:14px;font-weight:600;text-decoration:none;white-space:nowrap;transition:background var(--d-fast),color var(--d-fast)}.mh-header__nav a:hover{background:var(--navy);color:#fff}
@media (min-width:960px){.mh-header__inner{min-height:64px}.mh-header__nav{margin-inline:0;padding:0 0 var(--s3);mask-image:none;-webkit-mask-image:none;overflow:visible;flex-wrap:wrap;gap:var(--s1)}.mh-header__nav a{background:transparent;padding:0 var(--s3)}.mh-header__nav a:hover{background:var(--fill);color:var(--navy)}}
.btn-a{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 var(--s6);background:var(--orange-ink);color:#fff;font-size:16px;font-weight:600;text-decoration:none;border-radius:var(--r-btn);transition:background var(--d-fast)}.btn-a:hover{background:var(--orange-deep)}
.sol-intro p span{display:block;margin-bottom:var(--s3);font-size:17px}
.card__icon{width:20px;height:20px;color:var(--meta);flex:none}
.site-foot{margin-top:var(--s12);background:var(--paper);border-top:1px solid var(--rule);padding-block:var(--s8) var(--s10)}.site-foot__links{display:flex;flex-wrap:wrap;gap:var(--s1) var(--s2);margin-bottom:var(--s6)}.site-foot__links a{display:inline-flex;align-items:center;min-height:44px;padding:0 var(--s3);border-radius:var(--r-btn);color:var(--navy);font-weight:600;font-size:14px;text-decoration:none}.site-foot__links a:hover{background:var(--fill)}
.site-foot__id{font-size:14px;line-height:1.6;color:var(--navy);font-weight:600;max-width:80ch;margin-bottom:var(--s5)}.site-foot__warn{font-size:16px;line-height:1.55;color:var(--text);max-width:66ch;padding:var(--s3) var(--s4);background:var(--band);border:1px solid var(--rule);border-left:3px solid var(--orange);border-radius:var(--r-sm)}.site-foot__warn+.site-foot__warn{margin-top:var(--s3)}
.mh-progress{position:fixed;top:0;left:0;height:3px;width:100%;transform-origin:0 50%;transform:scaleX(var(--p,0));background:var(--orange);z-index:50;pointer-events:none}
.mh-anim .reveal{opacity:0;transform:translateY(16px);transition:opacity var(--d-slow) var(--ease),transform var(--d-slow) var(--ease);transition-delay:calc(var(--i,0) * 60ms)}.mh-anim .reveal.is-in{opacity:1;transform:none}
.spark{display:block;width:100%;height:auto}
'''

# ---------------------------------------------------------------- V1 Night Desk
V1_CSS = BASE + r'''
/* V1 · Night Desk. Dark navy opening and closing, light middle. The glow and glass tiles come from the current Dribbble fintech look; buttons stay flat and square. */
.mh-header{background:var(--ink);border-bottom:1px solid rgba(255,255,255,.1)}.mh-logo svg{background:#fff;padding:4px 6px;border-radius:3px;height:30px}
.mh-header__nav a{background:rgba(255,255,255,.08);color:#fff}.mh-header__nav a:hover{background:#fff;color:var(--navy)}
@media (min-width:960px){.mh-header__nav a{background:transparent;color:var(--on-navy-soft)}.mh-header__nav a:hover{background:rgba(255,255,255,.1);color:#fff}}
.hero{position:relative;overflow:hidden;background:radial-gradient(900px 500px at 85% -10%,rgba(232,81,26,.45),transparent 60%),radial-gradient(700px 400px at -10% 110%,rgba(42,58,143,.8),transparent 60%),linear-gradient(160deg,var(--ink),var(--navy));color:#fff;padding-block:var(--s12) var(--s10)}
.hero::after{content:"";position:absolute;inset:auto -10% -40% -10%;height:60%;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 20' preserveAspectRatio='none'%3E%3Cpath d='M0 20 L100 0' stroke='rgba(255,255,255,.06)' stroke-width='.3'/%3E%3C/svg%3E");pointer-events:none}
.hero h1{color:#fff;max-width:18ch;font-size:clamp(34px,4.2vw + 16px,60px)}
.hero .lede{margin-top:var(--s5);font-size:17px;line-height:1.6;max-width:62ch;color:#E8EAF4}
.hero-grid{display:grid;gap:var(--s8);align-items:end}
@media (min-width:960px){.hero-grid{grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr)}.hero{padding-block:var(--s16) var(--s12)}}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:var(--s3);margin:0;position:relative}
.facts::before{content:"";position:absolute;inset:-20px;background:radial-gradient(closest-side,rgba(255,178,143,.18),transparent);pointer-events:none}
.facts .stat{display:flex;flex-direction:column;gap:var(--s1);padding:var(--s4);background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.16);border-radius:var(--r-md);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);position:relative;transition:background var(--d-fast),transform var(--d-med) var(--ease)}
.facts .stat:hover{background:rgba(255,255,255,.12);transform:translateY(-2px)}
.facts .stat__label{font-size:12.5px;color:var(--on-navy-soft);font-weight:500}.facts .stat__value{font:800 28px/1.1 var(--display);color:#fff;letter-spacing:-.02em;margin-top:auto;white-space:nowrap}
.facts .stat:first-child .stat__value{color:var(--orange-soft)}
@media (min-width:600px){.facts .stat__value{font-size:32px}}
.sol{background:var(--ink);color:#fff;padding-block:var(--s8) var(--s10);border-top:1px solid rgba(255,255,255,.08)}
.sol h2{color:#fff}.sol .sol-intro{display:flex;flex-wrap:wrap;gap:var(--s3) var(--s6);align-items:flex-end;margin:var(--s3) 0 var(--s5)}
.sol .sol-intro p{color:var(--on-navy-soft)}.sol .sol-intro p span{color:#E8EAF4}
.sol-links{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:var(--s2)}
.sol-links a{display:inline-flex;align-items:center;gap:var(--s2);min-height:44px;padding:0 var(--s4) 0 var(--s3);border:1px solid rgba(255,255,255,.18);border-radius:var(--r-sm);color:#fff;font-weight:600;font-size:15px;text-decoration:none;background:rgba(255,255,255,.05);transition:background var(--d-fast),border-color var(--d-fast),transform var(--d-fast)}
.sol-links a::before{content:"";width:18px;height:18px;background:var(--sicon) center/18px no-repeat;flex:none}
.sol-links a:hover{background:#fff;color:var(--navy);border-color:#fff;transform:translateY(-1px)}
.section{padding-block:var(--s10)}.section:nth-of-type(odd){background:var(--band)}@media (min-width:960px){.section{padding-block:var(--s16)}}
.section h2{margin-bottom:var(--s5)}
.ledger{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr;gap:var(--s3)}@media (min-width:600px){.ledger{grid-template-columns:repeat(2,1fr);gap:var(--s4)}}@media (min-width:960px){.ledger{grid-template-columns:repeat(3,1fr)}.ledger--dense{grid-template-columns:repeat(4,1fr)}}
a.card{position:relative;display:grid;grid-template-columns:44px 1fr 20px;grid-template-areas:"icon title chev" "icon meta chev";column-gap:var(--s3);row-gap:2px;align-items:start;height:100%;padding:var(--s4);background:var(--paper);border:1px solid var(--rule);border-radius:var(--r-md);text-decoration:none;color:var(--text);box-shadow:var(--shadow);transition:border-color var(--d-fast),transform var(--d-med) var(--ease),box-shadow var(--d-med) var(--ease)}
a.card:hover{border-color:var(--navy);transform:translateY(-3px);box-shadow:var(--shadow-lift)}
a.card::before{content:"";grid-area:icon;width:44px;height:44px;border-radius:var(--r-sm);background:var(--navy)}
a.card::after{content:"";position:absolute;left:calc(var(--s4) + 11px);top:calc(var(--s4) + 11px);width:22px;height:22px;background:var(--orange-soft);-webkit-mask:var(--icon) center/contain no-repeat;mask:var(--icon) center/contain no-repeat}
.card__title{grid-area:title;font:700 16px/1.3 var(--display);color:var(--navy);letter-spacing:-.01em;padding-top:2px}.card__meta{grid-area:meta;font-size:14px;line-height:1.45;color:var(--meta)}.card__icon{grid-area:chev;justify-self:end;margin-top:3px}
.site-foot{background:var(--ink);border-top:0;color:#fff;margin-top:0}.site-foot__links a{color:#fff}.site-foot__links a:hover{background:rgba(255,255,255,.1)}.site-foot__id{color:var(--on-navy-soft)}.site-foot__warn{background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.14);border-left-color:var(--orange);color:#fff}
'''
V1_BODY = f'''
<main id="main">
  <section class="hero" aria-labelledby="page-title"><div class="container hero-grid">
    <div><h1 id="page-title">{H1}</h1><p class="lede">{LEDE}</p></div>
    <dl class="facts">{facts()}</dl>
  </div></section>
  <section class="sol" aria-labelledby="h-solutions"><div class="container">
    <h2 id="h-solutions">Find a Solution</h2>
    <div class="sol-intro"><p><span>{SOL_INTRO}</span> <a class="btn-a" href="{SOL_CTA[1]}">{SOL_CTA[0]}</a></p></div>
    <ul class="sol-links">{sols()}</ul>
  </div></section>
  <section class="section" aria-labelledby="h-start"><div class="container"><h2 id="h-start">Start Here</h2>{cards(START)}</div></section>
  <section class="section" aria-labelledby="h-asset"><div class="container"><h2 id="h-asset">Mutual Funds by Asset Class</h2>{cards(ASSET)}</div></section>
  <section class="section" aria-labelledby="h-themes"><div class="container"><h2 id="h-themes">Themes, Indices and More</h2>{cards(THEMES,'ledger ledger--dense')}</div></section>
</main>'''

# ---------------------------------------------------------------- V2 Bento Board
V2_CSS = BASE + r'''
/* V2 · Bento Board. Everything lives in an asymmetric tile grid on white: the headline tile, four fact tiles, a tall solutions tile, and a product bento where the first card is the hero of its group. */
.bento{display:grid;gap:var(--s3);grid-template-columns:repeat(2,minmax(0,1fr));padding-block:var(--s6) 0}
@media (min-width:760px){.bento{grid-template-columns:repeat(4,minmax(0,1fr));gap:var(--s4)}}
.tile{background:var(--paper);border:1px solid var(--rule);border-radius:var(--r-lg);padding:var(--s5);min-width:0;box-shadow:var(--shadow)}
.tile--head{grid-column:1/-1;background:linear-gradient(135deg,var(--wash),#fff 60%);padding:var(--s8) var(--s6)}
@media (min-width:760px){.tile--head{grid-column:span 4}}
.tile--head h1{max-width:16ch}.tile--head .lede{margin-top:var(--s4);font-size:17px;line-height:1.6;max-width:60ch}
.facts{display:contents;margin:0}
.facts .stat{display:flex;flex-direction:column;gap:var(--s1);background:var(--paper);border:1px solid var(--rule);border-radius:var(--r-lg);padding:var(--s5);box-shadow:var(--shadow);min-height:132px;transition:transform var(--d-med) var(--ease),box-shadow var(--d-med) var(--ease)}
.facts .stat:hover{transform:translateY(-2px);box-shadow:var(--shadow-lift)}
.facts .stat:nth-child(1){background:var(--navy);border-color:var(--navy)}.facts .stat:nth-child(1) .stat__label{color:var(--on-navy-soft)}.facts .stat:nth-child(1) .stat__value{color:var(--orange-soft)}
.facts .stat:nth-child(4){background:var(--honey);border-color:var(--honey)}
.facts .stat__label{font-size:13px;color:var(--meta);font-weight:500}.facts .stat__value{font:800 30px/1.1 var(--display);color:var(--navy);letter-spacing:-.02em;margin-top:auto;white-space:nowrap}
@media (max-width:759px){.facts .stat__value{font-size:24px}.facts .stat:nth-child(4){grid-column:1/-1}}
.tile--sol{grid-column:1/-1;background:var(--band)}
@media (min-width:760px){.tile--sol{grid-column:span 4;display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.6fr);gap:var(--s8);align-items:start}}
.tile--sol h2{margin-bottom:var(--s3)}.sol-intro{display:flex;flex-wrap:wrap;gap:var(--s3)}.sol-intro p span{font-size:17px}
.sol-links{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:var(--s2)}
.sol-links a{display:flex;align-items:center;gap:var(--s3);min-height:52px;padding:0 var(--s4) 0 var(--s3);background:var(--paper);border:1px solid var(--rule);border-radius:var(--r-sm);color:var(--navy);font-weight:600;font-size:15px;text-decoration:none;transition:border-color var(--d-fast),transform var(--d-fast),box-shadow var(--d-med)}
.sol-links a::before{content:"";width:32px;height:32px;border-radius:var(--r-btn);background:var(--sicon) center/18px no-repeat var(--honey);flex:none}
.sol-links a:hover{border-color:var(--navy);transform:translateY(-1px);box-shadow:var(--shadow)}
.section{padding-block:var(--s10)}@media (min-width:960px){.section{padding-block:var(--s12)}}
.section h2{margin-bottom:var(--s5)}
.ledger{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr;gap:var(--s3)}
@media (min-width:600px){.ledger{grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s4)}}
@media (min-width:960px){.ledger{grid-template-columns:repeat(4,minmax(0,1fr))}.ledger--start li:first-child{grid-column:span 2;grid-row:span 2}.ledger--start li:nth-child(2){grid-column:span 2}.ledger--asset li:first-child{grid-column:span 2}}
a.card{position:relative;display:flex;flex-direction:column;gap:var(--s2);height:100%;padding:var(--s5);background:var(--paper);border:1px solid var(--rule);border-radius:var(--r-lg);text-decoration:none;color:var(--text);box-shadow:var(--shadow);transition:border-color var(--d-fast),transform var(--d-med) var(--ease),box-shadow var(--d-med) var(--ease)}
a.card:hover{border-color:var(--navy);transform:translateY(-3px);box-shadow:var(--shadow-lift)}
a.card::before{content:"";width:44px;height:44px;border-radius:var(--r-sm);background:var(--honey);margin-bottom:var(--s2)}
a.card::after{content:"";position:absolute;left:calc(var(--s5) + 11px);top:calc(var(--s5) + 11px);width:22px;height:22px;background:var(--orange);-webkit-mask:var(--icon) center/contain no-repeat;mask:var(--icon) center/contain no-repeat}
.ledger--start li:first-child a.card{background:linear-gradient(160deg,var(--navy),var(--navy-2));border-color:var(--navy);color:#fff}
.ledger--start li:first-child a.card::before{background:rgba(255,255,255,.12);width:56px;height:56px}.ledger--start li:first-child a.card::after{width:28px;height:28px;left:calc(var(--s5) + 14px);top:calc(var(--s5) + 14px);background:var(--orange-soft)}.ledger--start li:first-child .card__title{margin-top:auto}
.ledger--start li:first-child .card__title{color:#fff;font-size:26px}.ledger--start li:first-child .card__meta{color:var(--on-navy-soft);font-size:16px}.ledger--start li:first-child .card__icon{color:#fff}
.ledger--start li:nth-child(2) a.card{background:var(--wash)}
.card__title{font:700 17px/1.3 var(--display);color:var(--navy);letter-spacing:-.01em}.card__meta{font-size:14px;line-height:1.45;color:var(--meta)}.card__icon{position:absolute;right:var(--s4);top:var(--s5)}
.section--themes{background:var(--band)}
'''
V2_BODY = f'''
<main id="main">
  <section aria-labelledby="page-title"><div class="container bento">
    <div class="tile tile--head"><h1 id="page-title">{H1}</h1><p class="lede">{LEDE}</p></div>
    <dl class="facts">{facts()}</dl>
    <div class="tile tile--sol" aria-labelledby="h-solutions">
      <div><h2 id="h-solutions">Find a Solution</h2><div class="sol-intro"><p><span>{SOL_INTRO}</span> <a class="btn-a" href="{SOL_CTA[1]}">{SOL_CTA[0]}</a></p></div></div>
      <ul class="sol-links">{sols()}</ul>
    </div>
  </div></section>
  <section class="section" aria-labelledby="h-start"><div class="container"><h2 id="h-start">Start Here</h2>{cards(START,'ledger ledger--start')}</div></section>
  <section class="section" aria-labelledby="h-asset"><div class="container"><h2 id="h-asset">Mutual Funds by Asset Class</h2>{cards(ASSET,'ledger ledger--asset')}</div></section>
  <section class="section section--themes" aria-labelledby="h-themes"><div class="container"><h2 id="h-themes">Themes, Indices and More</h2>{cards(THEMES)}</div></section>
</main>'''

# ---------------------------------------------------------------- V3 Split Editorial
V3_CSS = BASE + r'''
/* V3 · Split Editorial. A two-column hero with a statement card and a growth line, products as a swipeable strip, asset classes as proportional bars, themes as a two-column index. */
.hero{padding-block:var(--s10) var(--s8);border-bottom:1px solid var(--rule);background:linear-gradient(180deg,var(--wash),#fff)}
.hero-grid{display:grid;gap:var(--s8);align-items:center}
@media (min-width:960px){.hero-grid{grid-template-columns:minmax(0,1fr) 440px;gap:var(--s12)}.hero{padding-block:var(--s16) var(--s12)}}
.hero h1{font-size:clamp(34px,4vw + 16px,58px)}.hero .lede{margin-top:var(--s5);font-size:17px;line-height:1.6;max-width:58ch}
.panel{--spark:var(--orange);background:var(--navy);color:#fff;border-radius:var(--r-lg);padding:var(--s5);position:relative;overflow:hidden;box-shadow:var(--shadow-lift)}
.panel .spark{position:absolute;left:0;right:0;bottom:0;height:38%;opacity:.9}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:var(--s2) var(--s4);margin:0;position:relative}
.facts .stat{display:flex;flex-direction:column;gap:2px;padding:var(--s3) 0;border-bottom:1px solid rgba(255,255,255,.14)}
.facts .stat:nth-child(n+3){border-bottom:0;padding-bottom:var(--s16)}
.facts .stat__label{font-size:12px;letter-spacing:.05em;text-transform:uppercase;color:var(--on-navy-soft);font-weight:600}.facts .stat__value{font:800 26px/1.1 var(--display);letter-spacing:-.02em;white-space:nowrap}
.facts .stat:first-child .stat__value{font-size:34px;color:var(--orange-soft)}
.section{padding-block:var(--s10)}@media (min-width:960px){.section{padding-block:var(--s14,56px)}}
.section h2{margin-bottom:var(--s4)}
.sol-intro{display:flex;flex-wrap:wrap;align-items:center;gap:var(--s3) var(--s4);margin-bottom:var(--s5)}
.sol-links{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:var(--s2)}
.sol-links a{display:inline-flex;align-items:center;gap:var(--s2);min-height:44px;padding:0 var(--s4) 0 var(--s3);border:1px solid var(--rule);border-radius:var(--r-sm);color:var(--navy);font-weight:600;font-size:15px;text-decoration:none;background:var(--paper);transition:background var(--d-fast),border-color var(--d-fast),color var(--d-fast)}
.sol-links a::before{content:"";width:18px;height:18px;background:var(--sicon) center/18px no-repeat;flex:none}.sol-links a:hover{background:var(--navy);border-color:var(--navy);color:#fff}
.section--start{background:var(--band)}
.strip{list-style:none;margin:0 calc(-1 * var(--gutter));padding:var(--s1) var(--gutter) var(--s4);display:flex;gap:var(--s4);overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:thin;scrollbar-color:var(--rule-2) transparent}
.strip li{flex:0 0 min(300px,82vw);scroll-snap-align:start}
.strip a.card{position:relative;display:flex;flex-direction:column;gap:var(--s2);height:100%;padding:var(--s5);background:var(--paper);border:1px solid var(--rule);border-radius:var(--r-md);text-decoration:none;color:var(--text);box-shadow:var(--shadow);transition:border-color var(--d-fast),transform var(--d-med) var(--ease),box-shadow var(--d-med) var(--ease)}
.strip a.card:hover{border-color:var(--navy);transform:translateY(-3px);box-shadow:var(--shadow-lift)}
.strip a.card::before{content:"";width:44px;height:44px;border-radius:var(--r-sm);background:var(--honey);margin-bottom:var(--s2)}
.strip a.card::after{content:"";position:absolute;left:calc(var(--s5) + 11px);top:calc(var(--s5) + 11px);width:22px;height:22px;background:var(--orange);-webkit-mask:var(--icon) center/contain no-repeat;mask:var(--icon) center/contain no-repeat}
.strip .card__icon{position:absolute;right:var(--s4);top:var(--s5)}
.card__title{font:700 17px/1.3 var(--display);color:var(--navy);letter-spacing:-.01em}.card__meta{font-size:14px;line-height:1.45;color:var(--meta)}
.bars{list-style:none;margin:0;padding:0;border-top:1px solid var(--rule)}
.bars a.card{display:grid;grid-template-columns:minmax(0,1fr) 20px;grid-template-areas:"title chev" "meta chev" "bar bar";column-gap:var(--s4);row-gap:var(--s1);padding:var(--s4) 0;border-bottom:1px solid var(--rule);text-decoration:none;color:var(--text);transition:background var(--d-fast)}
@media (min-width:760px){.bars a.card{grid-template-columns:minmax(220px,.9fr) minmax(0,1.6fr) minmax(0,1.6fr) 20px;grid-template-areas:"title meta bar chev";align-items:center;padding:var(--s4) var(--s2)}}
.bars a.card:hover{background:var(--band)}
.bars .card__title{grid-area:title}.bars .card__meta{grid-area:meta}.bars .card__icon{grid-area:chev;justify-self:end}
.bars a.card::after{content:"";grid-area:bar;height:10px;border-radius:2px;background:linear-gradient(90deg,var(--navy),var(--navy-2));width:calc(var(--v) / 614 * 100%);min-width:6px;transition:width var(--d-slow) var(--ease)}
.bars li:first-child a.card::after{background:linear-gradient(90deg,var(--orange-ink),var(--orange))}
.index{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr;gap:0 var(--s12)}
@media (min-width:760px){.index{grid-template-columns:1fr 1fr}}
.index a.card{display:grid;grid-template-columns:32px minmax(0,1fr) 20px;grid-template-areas:"icon title chev" "icon meta chev";column-gap:var(--s3);align-items:center;padding:var(--s3) 0;border-bottom:1px solid var(--rule);text-decoration:none;color:var(--text);min-height:60px}
.index a.card::before{content:"";grid-area:icon;width:32px;height:32px;border-radius:var(--r-btn);background:var(--fill)}
.index a.card::after{content:"";position:absolute;width:18px;height:18px;margin:7px;background:var(--navy);-webkit-mask:var(--icon) center/contain no-repeat;mask:var(--icon) center/contain no-repeat}
.index li{position:relative}.index a.card .card__title{grid-area:title;font-size:16px}.index a.card .card__meta{grid-area:meta}.index a.card .card__icon{grid-area:chev;justify-self:end}
.index a.card:hover .card__title{text-decoration:underline;text-underline-offset:3px}
'''
def bars(): return '<ul class="bars">' + ''.join(card(t,m,h,f' style="--v:{v}"') for t,m,h,v in ASSET) + '</ul>'
V3_BODY = f'''
<main id="main">
  <section class="hero" aria-labelledby="page-title"><div class="container hero-grid">
    <div><h1 id="page-title">{H1}</h1><p class="lede">{LEDE}</p></div>
    <div class="panel"><dl class="facts">{facts()}</dl>{SPARK}</div>
  </div></section>
  <section class="section" aria-labelledby="h-solutions"><div class="container">
    <h2 id="h-solutions">Find a Solution</h2>
    <div class="sol-intro"><p><span>{SOL_INTRO}</span> <a class="btn-a" href="{SOL_CTA[1]}">{SOL_CTA[0]}</a></p></div>
    <ul class="sol-links">{sols()}</ul>
  </div></section>
  <section class="section section--start" aria-labelledby="h-start"><div class="container"><h2 id="h-start">Start Here</h2>{cards(START,'strip')}</div></section>
  <section class="section" aria-labelledby="h-asset"><div class="container"><h2 id="h-asset">Mutual Funds by Asset Class</h2>{bars()}</div></section>
  <section class="section" aria-labelledby="h-themes"><div class="container"><h2 id="h-themes">Themes, Indices and More</h2>{cards(THEMES,'index')}</div></section>
</main>'''

for slug, cls, css, body in [('v1-night-desk','v-night',V1_CSS,V1_BODY),('v2-bento-board','v-bento',V2_CSS,V2_BODY),('v3-split-editorial','v-split',V3_CSS,V3_BODY)]:
    out = pathlib.Path(OUT)/slug/'index.html'; out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(cls, css, body)); print('wrote', out, out.stat().st_size)
