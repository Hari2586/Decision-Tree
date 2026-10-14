"""Generate the scroll-craft home page for MoneyHoney from the locked original.

Usage: python3 scrollcraft_home.py <original index.html> <head fragment> <mh.css> <out index.html>

Every visible string is lifted from the original file by regex; this script
adds layout, data-sc-* attributes, CSS and page JS only.
"""
import re, sys, html

orig, headfrag, mhcss, out = sys.argv[1:5]
S = open(orig, encoding='utf-8').read()
HEAD = open(headfrag, encoding='utf-8').read().strip()
MH = open(mhcss, encoding='utf-8').read()

def grab(pattern, s=S, flags=re.S):
    m = re.search(pattern, s, flags)
    assert m, pattern
    return m

demo = grab(r'<div class="demo-strip"[^>]*>.*?</div>\s*</div>').group(0)
header = grab(r'<header class="mh-header">.*?</header>').group(0)
logo = grab(r'<a class="mh-logo".*?</a>', header).group(0)
nav = grab(r'<nav class="mh-header__nav".*?</nav>', header).group(0)
footer = grab(r'<footer class="site-foot".*?</footer>').group(0)
main = grab(r'<main class="container" id="main">(.*?)</main>').group(1)

h1 = grab(r'<h1>(.*?)</h1>', main).group(1)
lede = grab(r'<p class="lede">(.*?)</p>', main).group(1)
stats = re.findall(r'<span class="stat__label">(.*?)</span><span class="stat__value">(.*?)</span>', main)
assert len(stats) == 4
h2s = re.findall(r'<h2>(.*?)</h2>', main)
assert len(h2s) == 4, h2s
sol_p = grab(r'<h2>Find a Solution</h2>\s*<p>(.*?)</p>', main).group(1)
sol_items = re.findall(r'<li><a href="([^"]+)">(.*?)</a></li>', grab(r'<ul class="sol-links">(.*?)</ul>', main).group(1))
assert len(sol_items) == 11
grids = re.findall(r'<div class="linkgrid">(.*?)</div>', main)
assert len(grids) == 3
def cards(g):
    return re.findall(r'<a class="card" href="([^"]+)">(.*?)<span class="card__meta">(.*?)</span></a>', g)
start, asset, themes = [cards(g) for g in grids]
assert (len(start), len(asset), len(themes)) == (11, 5, 8)

# asset class counts, read from the page itself
asset_n = [int(re.search(r'(\d+) schemes', m).group(1)) for _, _, m in asset]
assert sum(asset_n) == 1774, asset_n

# icon rules lifted from mh.css, re-scoped to this page
icon_rules = []
for ln in MH.splitlines():
    if ln.startswith('.ledger a.card') and '--icon' in ln and '::after' not in ln:
        icon_rules.append(ln.replace('.ledger a.card', '.card'))
    if ln.startswith('[href$=') and '--sicon' in ln:
        icon_rules.append(re.sub(r',\.sol-[a-z-]+', '', ln))
ICONS = '\n'.join(icon_rules)

# ------------------------------------------------------------------ markup
def stat_html(i, label, value):
    digits = re.sub(r'[^\d]', '', value)
    tick = f' data-tick="{value}"' if digits and re.fullmatch(r'[\d,]+', value) else ''
    return (f'<div class="plate"><span class="plate__label">{label}</span>'
            f'<span class="plate__value"{tick}>{value}</span></div>')

facts = '\n      '.join(stat_html(i, l, v) for i, (l, v) in enumerate(stats))

sol_lis = []
for i, (href, txt) in enumerate(sol_items):
    s = 0.06 + i * 0.065
    sol_lis.append(f'<li data-sc-reveal="left" data-sc-reveal-at="{s:.3f} {s+0.12:.3f}"><a href="{href}">{txt}</a></li>')
SOL = '\n        '.join(sol_lis)

rail_cards = []
for i, (href, title, meta) in enumerate(start):
    rail_cards.append(f'<a class="card" style="--i:{i+1}" href="{href}" data-sc-tilt="6">{title}<span class="card__meta">{meta}</span></a>')
RAIL = '\n          '.join(rail_cards)

plates = []
for i, (href, title, meta) in enumerate(asset):
    s = 0.06 + i * 0.16
    n = asset_n[i]
    meta2 = meta.replace(f'{n} schemes', f'<span data-sc-count="0 {n}" data-sc-count-at="{s:.2f} {s+0.12:.2f}">{n}</span> schemes')
    plates.append(f'<a class="card card--navy" style="--i:{i}" href="{href}" data-sc-cue="{s:.2f} 1 0.08 0.05">{title}<span class="card__meta">{meta2}</span></a>')
PLATES = '\n          '.join(plates)

shelves = '\n          '.join(f'<a class="card card--row" href="{href}">{title}<span class="card__meta">{meta}</span></a>' for href, title, meta in themes)

segs = '\n      '.join(f'<i class="seg" style="--w:{n}"></i>' for n in asset_n)

room_ids = ['room-solutions', 'room-start', 'room-asset', 'room-themes']
h_ids = ['h-solutions', 'h-start', 'h-asset', 'h-themes']
markers = '\n      '.join(f'<button type="button" class="shelf__room" data-room="{r}" aria-labelledby="{h}" data-label="{t}"></button>'
                          for r, h, t in zip(room_ids, h_ids, h2s))

CSS = r"""
:root{
  --sc-canvas:#FFFFFF;--sc-surface:#F5F6FC;--sc-ink:#141A3B;--sc-ink-soft:#5D637C;
  --sc-accent:#C4410E;--sc-accent-ink:#FFFFFF;
  --sc-font-display:"Manrope",system-ui,sans-serif;--sc-font-text:"Figtree",system-ui,sans-serif;--sc-font-mono:"Figtree",system-ui,sans-serif;
  --sc-r-sm:4px;--sc-r-md:6px;--sc-r-lg:8px;--sc-r-pill:6px;
  --sc-shadow-color:232 40% 22%;
  --sc-maxw:78rem;
  --navy:#1B2666;--navy2:#2A3A8F;--ink2:#0F163F;--orange:#E8511A;--orange-soft:#FFB28F;--orange-ink:#B03A0B;
  --honey:#FDEDE5;--wash:#F1F3FC;--band:#F5F6FC;--rule:#E1E4F0;--rule2:#C9CFEA;
  --shelf-w:56px;--shelf-h:48px;
}
body{background:var(--sc-canvas)}
a{color:inherit}
.t-display{font-family:var(--sc-font-display);font-weight:800;line-height:1.02;letter-spacing:-0.025em;text-wrap:balance;margin:0;color:var(--sc-ink)}
.t-xl{font-size:clamp(2.3rem,1.5rem+3.4vw,4.4rem)}
.t-lg{font-size:clamp(1.9rem,1.3rem+2.4vw,3.2rem)}
.t-md{font-size:clamp(1.5rem,1.2rem+1.4vw,2.2rem)}
.wrap{width:100%;max-width:var(--sc-maxw);margin-inline:auto;padding-inline:var(--sc-gutter)}

/* ---- header (static: the shelf rail is the page's index) ---- */
.demo-strip{background:var(--honey);color:var(--orange-ink);font-size:var(--sc-t-sm);line-height:1.45;padding:8px 0}
.demo-strip .container{max-width:var(--sc-maxw);margin-inline:auto;padding-inline:var(--sc-gutter)}
.mh-header{border-bottom:1px solid var(--rule);background:#fff;position:relative;z-index:5}
.mh-header__inner{max-width:var(--sc-maxw);margin-inline:auto;padding:14px var(--sc-gutter);display:flex;align-items:center;gap:var(--sc-6);flex-wrap:wrap}
.mh-logo{display:inline-flex;padding:6px 0;border-radius:var(--sc-r-sm)}
.mh-logo svg{height:22px;width:auto}
.mh-header__nav{display:flex;flex-wrap:wrap;gap:4px 2px;margin-left:auto}
.mh-header__nav a{font-weight:600;font-size:0.9rem;color:var(--navy);text-decoration:none;padding:7px 8px;border-radius:var(--sc-r-sm);transition:background var(--sc-d-fast) var(--sc-ease-out)}
.mh-header__nav a:hover{background:var(--wash);text-decoration:underline;text-underline-offset:.22em}
.mh-header__nav a:active{transform:translateY(1px)}

/* ---- rooms ---- */
.room{position:relative}
@media (min-width:861px){ .room>.wrap, .room [data-sc-stage]>.wrap{padding-right:calc(var(--sc-gutter) + var(--shelf-w) + 12px)} }
.room [data-sc-stage]{display:flex;flex-direction:column;justify-content:center}
.room--band{background:var(--band)}
.room--wash{background:var(--wash)}
.room--navy{background:var(--navy);--sc-ink:#fff;--sc-ink-soft:#C9CFEA;--sc-accent:#FFB28F;--sc-accent-ink:#1B2666;color:var(--sc-ink)}
.room--close{background:var(--ink2);--sc-ink:#fff;--sc-ink-soft:#C9CFEA;--sc-accent:#FFB28F;--sc-accent-ink:#0F163F;color:var(--sc-ink)}

/* ---- act 1: the title wall ---- */
.hero{overflow:clip;padding-block:clamp(3rem,7vw,6rem) clamp(3.5rem,8vw,7rem);isolation:isolate}
.hero__grid{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:clamp(2rem,5vw,5rem);align-items:center;position:relative;z-index:2}
.hero h1{font-size:clamp(2.3rem,1.5rem+3.4vw,4.4rem)}
.hero .lede{margin:var(--sc-5) 0 0;max-width:52ch;color:var(--sc-ink-soft);font-size:var(--sc-t-lg);line-height:1.5;text-wrap:pretty}
.hero .lede{font-size:clamp(1.05rem,0.95rem+0.5vw,1.25rem)}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.plate{background:#fff;border:1px solid var(--rule);border-radius:var(--sc-r-md);padding:18px 18px 16px;display:flex;flex-direction:column;gap:10px;box-shadow:var(--sc-e1);position:relative}
.plate::before{content:"";position:absolute;left:18px;top:0;width:28px;height:3px;background:var(--orange);border-radius:0 0 2px 2px}
.plate__label{font-size:var(--sc-t-xs);font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--sc-ink-soft)}
.plate__value{font-family:var(--sc-font-display);font-weight:800;font-size:clamp(1.6rem,1.2rem+1.6vw,2.6rem);line-height:1;letter-spacing:-0.02em;font-variant-numeric:tabular-nums;color:var(--navy)}
.facts .plate:nth-child(2){margin-top:28px}.facts .plate:nth-child(4){margin-top:28px}
.plane{position:absolute;inset:-20% 0;pointer-events:none;z-index:0}
.plane--wall{background-image:linear-gradient(var(--rule) 1px,transparent 1px),linear-gradient(90deg,var(--rule) 1px,transparent 1px);background-size:64px 64px;opacity:.55;mask-image:radial-gradient(70% 90% at 70% 40%,#000 30%,transparent 100%)}
.plane--mark{inset:auto -6% -34% auto;width:min(44vw,560px);aspect-ratio:1;opacity:.5}
.plane--mark svg{width:100%;height:100%;overflow:visible}
.plane--mark path{fill:var(--honey)}

/* ---- act 2: the solution wall ---- */
.wall .wrap{padding-block:var(--sc-6)}
.wall__head{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.3fr);gap:var(--sc-6);align-items:end;margin-bottom:var(--sc-7)}
.wall__head p{margin:0;font-size:var(--sc-t-lg);color:var(--sc-ink-soft);max-width:38ch;line-height:1.45}
.wall__head p a{color:var(--sc-accent);font-weight:600;text-decoration-thickness:2px}
.wall__head p a:hover{color:var(--orange-ink)}
.sol-links{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:12px}
.sol-links li{clip-path:inset(0 0 0 0)}
.sol-links a{display:inline-flex;align-items:center;gap:12px;background:#fff;border:1px solid var(--rule);border-radius:var(--sc-r-md);padding:12px 20px 12px 12px;font-weight:700;font-size:1.05rem;color:var(--navy);text-decoration:none;box-shadow:var(--sc-e1);transition:transform var(--sc-d-fast) var(--sc-ease-out),border-color var(--sc-d-fast) var(--sc-ease-out)}
.sol-links a::before{content:"";flex:none;width:34px;height:34px;border-radius:var(--sc-r-sm);background:var(--sicon) center/18px no-repeat var(--honey)}
.sol-links a:hover{border-color:var(--rule2);transform:translateY(-2px)}
.sol-links a:active{transform:translateY(1px)}

/* ---- the card schema (one label format for every object) ---- */
.card{position:relative;display:grid;grid-template-columns:44px 1fr;grid-template-rows:auto auto;column-gap:14px;row-gap:4px;align-content:start;padding:18px;background:#fff;border:1px solid var(--rule);border-radius:var(--sc-r-md);text-decoration:none;color:var(--sc-ink);font-family:var(--sc-font-display);font-weight:800;font-size:1.2rem;line-height:1.15;letter-spacing:-0.01em;box-shadow:var(--sc-e1);transition:box-shadow var(--sc-d-base) var(--sc-ease-out),border-color var(--sc-d-fast) var(--sc-ease-out)}
.card::before{content:"";grid-row:1/3;width:44px;height:44px;border-radius:var(--sc-r-sm);background:var(--honey);align-self:start}
.card::after{content:"";position:absolute;left:29px;top:29px;width:22px;height:22px;background:var(--navy);-webkit-mask:var(--icon) center/contain no-repeat;mask:var(--icon) center/contain no-repeat}
.card__meta{display:block;grid-column:2;font-family:var(--sc-font-text);font-weight:400;font-size:var(--sc-t-sm);line-height:1.45;color:var(--sc-ink-soft);letter-spacing:0}
.card:hover{border-color:var(--rule2);box-shadow:var(--sc-e2)}
.card:active{transform:translateY(1px)}

/* ---- act 3: the rail ---- */
.rail{align-items:center;gap:20px;padding-inline:var(--sc-gutter);width:max-content}
.rail__lead{flex:none;width:min(26rem,70vw);padding-right:var(--sc-6)}
.rail>.card{flex:none;width:clamp(17rem,21vw,20rem);min-height:11.5rem;align-content:space-between}
.rail>.card::after{top:29px}
.rail__tail{flex:none;width:14vw}
@media (prefers-reduced-motion:no-preference){
  .rail>.card{transform:translateY(18px) scale(.97);transition:transform 520ms var(--sc-ease-out)}
  .rail>.card.is-set{transform:none}
}
@media (prefers-reduced-motion:reduce){
  /* the rail relays out as a wrapped grid: every door reachable, no static pin */
  #room-start{height:auto !important}
  #room-start [data-sc-stage]{position:static;height:auto;overflow:visible;display:block;padding-block:var(--sc-8)}
  .rail{flex-wrap:wrap;width:auto;max-width:var(--sc-maxw);margin-inline:auto;align-items:stretch}
  .rail__lead{width:100%;padding:0 0 var(--sc-5)}
  .rail>.card{width:clamp(16rem,30%,20rem);min-height:0}
  .rail__tail{display:none}
}

/* ---- act 4: the navy room (peak) ---- */
.asset .wrap{padding-block:var(--sc-6)}
.asset__grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.25fr);gap:var(--sc-7);align-items:start}
.asset__head{order:2;text-align:right;position:sticky;top:0}
.asset__head h2{color:#fff}
.plates{display:grid;gap:14px}
.card--navy{background:var(--navy2);border-color:#3A4AA3;color:#fff;box-shadow:var(--sc-e2);margin-left:calc(var(--i) * 5%)}
.card--navy .card__meta{color:#D5DAF2}
.card--navy::before{background:var(--honey)}
.card--navy::after{background:var(--navy)}
.card--navy:hover{border-color:#5563B8}
.card--navy [data-sc-count]{font-weight:600;color:#fff}

/* ---- act 5: the specialist shelves ---- */
.themes{padding-block:clamp(4rem,8vw,7rem)}
.themes__grid{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.6fr);gap:var(--sc-7)}
.shelves{display:grid;grid-template-columns:1fr 1fr;gap:14px 20px}
.shelves .card--row:nth-child(2n){transform:translateY(2.25rem)}
.card--row{grid-template-columns:36px 1fr;padding:14px 16px;font-size:1.05rem;background:#fff}
.card--row::before{width:36px;height:36px}
.card--row::after{left:23px;top:23px;width:20px;height:20px}
.card--row .card__meta{font-size:var(--sc-t-xs)}
[data-sc-stagger] > .card--row.sc-in:nth-child(2n){transform:translateY(2.25rem)}

/* ---- the close: colophon plate ---- */
.colophon{max-width:66rem;margin-inline:auto;padding-inline:var(--sc-gutter);display:grid;grid-template-columns:var(--shelf-w) minmax(0,1fr);gap:var(--sc-7);align-items:center}
.dock{width:var(--shelf-w);height:56vh;border:1px dashed rgba(255,255,255,.18);border-radius:var(--sc-r-md)}
.site-foot__links{display:flex;flex-wrap:wrap;gap:6px 20px;margin-bottom:var(--sc-6)}
.site-foot__links a{color:#fff;font-weight:600;font-size:var(--sc-t-sm);text-decoration-color:rgba(255,255,255,.4)}
.site-foot__links a:hover{text-decoration-color:#fff}
.site-foot__id{margin:0 0 var(--sc-5);color:#C9CFEA;font-size:var(--sc-t-sm);line-height:1.6;max-width:70ch}
.site-foot__warn{margin:0;color:#fff;font-size:var(--sc-t-base);line-height:1.55;max-width:70ch;padding-left:16px;border-left:1px solid var(--orange-soft)}
.site-foot__warn + .site-foot__warn{margin-top:var(--sc-4)}

/* ---- the shelf rail (signature) ---- */
.shelf{position:fixed;z-index:var(--sc-z-chrome);right:14px;top:50%;width:var(--shelf-w);height:56vh;transform:translateY(-50%);background:#fff;border:1px solid var(--rule);border-radius:var(--sc-r-md);box-shadow:var(--sc-e2);display:flex;flex-direction:column;align-items:center;padding:12px 0;gap:14px;will-change:transform}
.shelf--dock{transition:transform 640ms var(--sc-ease-out)}
.shelf__rooms{display:flex;flex-direction:column;gap:8px}
.shelf__room{position:relative;width:12px;height:12px;border:1.5px solid var(--navy);border-radius:2px;background:#fff;padding:0;cursor:pointer}
.shelf__room.is-here{background:var(--navy)}
.shelf__room::after{content:attr(data-label);position:absolute;right:calc(100% + 16px);top:50%;transform:translateY(-50%);white-space:nowrap;background:var(--navy);color:#fff;font-size:12px;font-weight:600;padding:5px 9px;border-radius:var(--sc-r-sm);opacity:0;pointer-events:none;transition:opacity var(--sc-d-fast) var(--sc-ease-out)}
.shelf__room:hover::after,.shelf__room:focus-visible::after{opacity:1}
.shelf__gauge{flex:1;width:14px;display:flex;flex-direction:column;gap:3px;min-height:0}
.seg{flex:var(--w) 1 0;position:relative;background:var(--rule);border-radius:2px;overflow:hidden;min-height:3px}
.seg::before{content:"";position:absolute;inset:0;background:var(--orange);transform-origin:50% 100%;transform:scaleY(var(--f,0))}
.shelf__total{min-height:1.2em;font-family:var(--sc-font-display);font-weight:800;font-size:13px;letter-spacing:-0.01em;color:var(--navy);font-variant-numeric:tabular-nums}
.shelf__total::after{content:attr(data-n)}
.shelf.is-full .shelf__total{color:var(--sc-accent)}
.shelf.is-full .seg::before{background:var(--orange)}

/* ---- mobile composition ---- */
@media (max-width:860px){
  :root{--shelf-w:48px}
  body{padding-bottom:calc(var(--shelf-h) + 24px)}
  .room [data-sc-stage]{padding-bottom:calc(var(--shelf-h) + 20px)}
  .hero{padding-block:2.5rem 3rem}
  .hero__grid{grid-template-columns:1fr;gap:2rem}
  .hero h1{font-size:clamp(2rem,1.4rem+3.6vw,2.6rem)}
  .facts .plate:nth-child(2),.facts .plate:nth-child(4){margin-top:0}
  .plane--mark{width:70vw;inset:auto -20% -20% auto}
  .wall__head{grid-template-columns:1fr;gap:var(--sc-3);margin-bottom:var(--sc-5)}
  .wall__head p{font-size:var(--sc-t-base)}
  .sol-links{gap:8px}
  .sol-links a{padding:9px 12px 9px 9px;font-size:var(--sc-t-sm)}
  .sol-links a::before{width:26px;height:26px;background-size:16px}
  .rail{gap:14px}
  .rail__lead{width:78vw}
  .rail>.card{width:72vw;min-height:10rem}
  .asset__grid{grid-template-columns:1fr;gap:var(--sc-5)}
  .asset__head{order:0;text-align:left;position:static}
  .plates{gap:10px}
  .card--navy{margin-left:0;padding:12px 14px;font-size:1.05rem}
  .card--navy::before{width:36px;height:36px}.card--navy::after{left:19px;top:19px;width:20px;height:20px}
  .card{grid-template-columns:36px 1fr}
  .themes{padding-block:3rem}
  .themes__grid{grid-template-columns:1fr;gap:var(--sc-5)}
  .shelves{grid-template-columns:1fr;gap:10px}
  .shelves .card--row:nth-child(2n),[data-sc-stagger] > .card--row.sc-in:nth-child(2n){transform:none}
  .colophon{grid-template-columns:1fr;gap:var(--sc-5);padding-block:var(--sc-5)}
  .dock{width:100%;height:var(--shelf-h)}
  .site-foot__warn{font-size:var(--sc-t-sm)}
  .shelf{right:14px;left:14px;top:auto;bottom:14px;width:auto;height:var(--shelf-h);transform:none;flex-direction:row;padding:0 14px;gap:14px}
  .shelf__rooms{flex-direction:row}
  .shelf__room::after{right:auto;left:50%;top:auto;bottom:calc(100% + 14px);transform:translateX(-50%)}
  .shelf__gauge{flex:1;width:auto;height:12px;flex-direction:row}
  .seg{min-height:0;min-width:3px}
  .seg::before{transform-origin:0 50%;transform:scaleX(var(--f,0))}
}
@media (prefers-reduced-motion:reduce){
  .shelf,.shelf--dock{transition:none}
  .rail>.card{transform:none}
}
"""

JS = r"""
(function(){
  var rm = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function(s, r){ return (r||document).querySelector(s); };
  var $$ = function(s, r){ return Array.prototype.slice.call((r||document).querySelectorAll(s)); };
  var clamp = function(v){ return v < 0 ? 0 : v > 1 ? 1 : v; };
  var easeOut = function(t){ return 1 - Math.pow(1 - t, 3); };

  /* 1. the four facts tick up once, on arrival (the kit's count device is
        scrubbed inside an act, and this hero is a flow act) */
  var ticks = $$('[data-tick]');
  if (ticks.length && !rm && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){
        if (!e.isIntersecting) return;
        io.unobserve(e.target);
        var el = e.target, target = el.getAttribute('data-tick');
        var n = parseInt(target.replace(/,/g,''), 10), comma = target.indexOf(',') > -1;
        var t0 = performance.now();
        (function frame(now){
          var k = easeOut(clamp((now - t0) / 1400));
          var v = Math.round(n * k);
          el.textContent = comma ? v.toLocaleString('en-US') : String(v);
          if (k < 1) requestAnimationFrame(frame); else el.textContent = target;
        })(t0);
      });
    }, { threshold: 0.5 });
    ticks.forEach(function(el){ el.textContent = '0'; io.observe(el); });
  }

  /* 2. rail cards settle as they arrive (position-based, so it is right at
        every viewport width) */
  var railCards = $$('.rail > .card');
  if (railCards.length && !rm && 'IntersectionObserver' in window) {
    var io2 = new IntersectionObserver(function(es){
      es.forEach(function(e){ if (e.isIntersecting) { e.target.classList.add('is-set'); io2.unobserve(e.target); } });
    }, { threshold: 0.5 });
    railCards.forEach(function(c){ io2.observe(c); });
  }

  /* 3. the shelf: room markers, the gauge, the dock */
  var shelf = $('.shelf'), act4 = $('#room-asset'), close = $('.room--close');
  var segs = $$('.seg', shelf), total = $('.shelf__total', shelf);
  var counts = segs.map(function(s){ return parseInt(s.style.getPropertyValue('--w'), 10); });
  var windows = counts.map(function(_, i){ return 0.06 + i * 0.16; });
  var rooms = $$('.shelf__room', shelf).map(function(b){ return { b: b, s: document.getElementById(b.getAttribute('data-room')) }; });
  rooms.forEach(function(r){
    r.b.addEventListener('click', function(){
      var y = r.s.getBoundingClientRect().top + scrollY;
      window.scrollTo({ top: y, behavior: rm ? 'auto' : 'smooth' });
    });
  });
  var planes = $$('.plane'), hero = $('.hero');
  var docked = false, base = null, lastSig = '';

  function frame(){
    var vh = innerHeight;
    /* current room */
    rooms.forEach(function(r){
      var rc = r.s.getBoundingClientRect();
      r.b.classList.toggle('is-here', rc.top <= vh / 2 && rc.bottom >= vh / 2);
    });
    /* gauge from the peak act's progress */
    var p = parseFloat(getComputedStyle(act4).getPropertyValue('--sc-p')) || 0;
    var sum = 0, fills = [];
    segs.forEach(function(s, i){
      var f = clamp((p - windows[i]) / 0.12);
      s.style.setProperty('--f', f.toFixed(3));
      sum += f * counts[i]; fills.push(Math.round(f * 20));
    });
    var n = Math.round(sum);
    total.setAttribute('data-n', n ? n.toLocaleString('en-US') : '');
    shelf.classList.toggle('is-full', n >= counts.reduce(function(a, b){ return a + b; }, 0));
    /* dock onto the colophon once the close is pinned */
    var want = close.getBoundingClientRect().top <= 1;
    if (want !== docked) {
      docked = want;
      if (docked) {
        if (!base) { shelf.style.transform = ''; shelf.classList.remove('shelf--dock'); base = shelf.getBoundingClientRect(); }
        var slot = $('.dock', close).getBoundingClientRect();
        shelf.classList.add('shelf--dock');
        var dx = slot.left - base.left, dy = slot.top - base.top;
        var mobile = matchMedia('(max-width: 860px)').matches;
        shelf.style.transform = (mobile ? '' : 'translateY(-50%) ') + 'translate(' + dx.toFixed(1) + 'px,' + dy.toFixed(1) + 'px)';
      } else {
        shelf.style.transform = '';
        setTimeout(function(){ if (!docked) shelf.classList.remove('shelf--dock'); }, 700);
      }
      shelf.setAttribute('data-sc-verify-hold', docked ? 'true' : 'false');
    }
    var sig = fills.join('') + (docked ? 'D' : 'U');
    if (sig !== lastSig) { lastSig = sig; shelf.setAttribute('data-sc-verify-state', sig); }
    /* hero planes: two depths, driven from page scroll while the wall is on screen */
    if (!rm && planes.length) {
      var hr = hero.getBoundingClientRect();
      if (hr.bottom > 0) {
        planes.forEach(function(pl){
          var rate = parseFloat(pl.getAttribute('data-rate')) || 0;
          pl.style.transform = 'translate3d(0,' + (scrollY * rate).toFixed(1) + 'px,0)';
        });
      }
    }
    requestAnimationFrame(frame);
  }
  base = null;
  addEventListener('resize', function(){ base = null; if (docked) { docked = false; shelf.style.transform = ''; } });
  requestAnimationFrame(frame);
})();
"""

mark_svg = re.search(r'<svg[^>]*>(.*?)</svg>', logo, re.S).group(1)
mark_paths = re.findall(r'<path d="([^"]+)" fill="#FF4A00"/>', mark_svg)[:2]
MARK = ''.join(f'<path d="{d}"/>' for d in mark_paths)

page = f'''<!doctype html>
<html lang="en-IN">
<head>
{HEAD}
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='4' fill='%231B2666'/><circle cx='16' cy='18' r='5' fill='%23E8511A'/></svg>">
<link rel="stylesheet" href="assets/scrollcraft.css">
<style>{CSS}
{ICONS}
</style>
</head>
<body>
<span data-sc-progress></span>

{header.replace('<header class="mh-header">', '<header class="mh-header">\n  ' + demo, 1)}

<main id="main">

  <section class="room hero" data-sc-act="flow">
    <div class="plane plane--wall" data-rate="-0.18" aria-hidden="true"></div>
    <div class="plane plane--mark" data-rate="0.12" aria-hidden="true"><svg viewBox="0 0 22 20" xmlns="http://www.w3.org/2000/svg">{MARK}</svg></div>
    <div class="wrap hero__grid">
      <div data-sc-in data-sc-stagger="80">
        <h1 class="t-display t-xl">{h1}</h1>
        <p class="lede">{lede}</p>
      </div>
      <div class="facts" data-sc-in data-sc-stagger="70">
      {facts}
      </div>
    </div>
  </section>

  <section class="room room--band wall" id="room-solutions" data-sc-act="pin" data-sc-span="2.4">
    <div data-sc-stage>
      <div class="wrap">
        <div class="wall__head" data-sc-cue="0 1 0 0.06">
          <h2 class="t-display t-lg" id="h-solutions">{h2s[0]}</h2>
          <p>{sol_p}</p>
        </div>
        <ul class="sol-links">
        {SOL}
        </ul>
      </div>
    </div>
  </section>

  <section class="room start" id="room-start" data-sc-act="pan" data-sc-span="3.2">
    <div data-sc-stage>
      <div class="rail" data-sc-pan="0.03">
        <div class="rail__lead"><h2 class="t-display t-lg" id="h-start">{h2s[1]}</h2></div>
          {RAIL}
        <div class="rail__tail" aria-hidden="true"></div>
      </div>
    </div>
  </section>

  <section class="room room--navy asset" id="room-asset" data-sc-act="pin" data-sc-span="4">
    <div data-sc-stage>
      <div class="wrap asset__grid">
        <div class="asset__head" data-sc-cue="0 1 0 0.05">
          <h2 class="t-display t-lg" id="h-asset">{h2s[2]}</h2>
        </div>
        <div class="plates">
          {PLATES}
        </div>
      </div>
    </div>
  </section>

  <section class="room room--wash themes" id="room-themes" data-sc-act="flow">
    <div class="wrap themes__grid">
      <div data-sc-in><h2 class="t-display t-lg" id="h-themes">{h2s[3]}</h2></div>
      <div class="shelves" data-sc-in data-sc-stagger="60">
          {shelves}
      </div>
    </div>
  </section>

</main>

<div class="room room--close" data-sc-act="pin" data-sc-span="1.2">
  <div data-sc-stage>
    <div class="colophon" data-sc-cue="0 1 0 0">
      <div class="dock" aria-hidden="true"></div>
      {footer}
    </div>
  </div>
</div>

<aside class="shelf" data-sc-verify-state="" data-sc-verify-hold="false">
  <div class="shelf__rooms">
      {markers}
  </div>
  <div class="shelf__gauge" aria-hidden="true">
      {segs}
  </div>
  <div class="shelf__total" aria-hidden="true" data-n=""></div>
</aside>

<script src="assets/scrollcraft.js"></script>
<script>ScrollCraft.mount(document.body);</script>
<script>{JS}</script>
</body>
</html>
'''
# the footer's own .container wrapper needs no padding inside the plate
page = page.replace('<footer class="site-foot" data-nosnippet>\n  <div class="container">', '<footer class="site-foot" data-nosnippet>\n  <div class="colophon__text">')
open(out, 'w', encoding='utf-8').write(page)
print('wrote', out, len(page), 'bytes')
