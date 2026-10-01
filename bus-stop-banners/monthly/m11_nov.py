"""November: the festive bonus. Option A: spend it. Option B: grow it (lump sum investing)."""
from framework import call, lockup, logo, qr_block, side_cta

KEY = "11-nov"
MSG = {"en": 'Hi! Bus stop ad: Invest my bonus.',
       "hi": 'Hi! Bus stop ad: Bonus invest karna hai.'}
NOTE = ("*Illustration: &#8377;1 lakh invested once for 15 years at an assumed 12% p.a. return, for understanding only. "
              "Mutual funds do not guarantee returns; actual returns may be higher or lower.")
SIDE_NOTE = ''

T = {
    "en": dict(
        top="Your &#8377;1 lakh bonus. Two futures.", or_="OR",
        a_lbl="Option A", a_h="Spend it.", a_s="Gone in 2 weeks.",
        b_lbl="Option B", b_h="Invest it.", b_s="&asymp; &#8377;5.5 lakh* in 15 years.",
        s_alert=("Bank alert", "Bonus of &#8377;1,00,000 credited"), s_h="Give your bonus a job.",
        s_sub="Before the sales find one for it.",
        b_h1='Where will your bonus be <span class="o">next Diwali?</span>',
        b_sub="Spend a little, invest the rest. Lump sum or step-by-step (STP): we&rsquo;ll help you choose.",
        yrs=["Today", "5 yrs", "10 yrs", "15 yrs"]),
    "hi": dict(
        top="आपका &#8377;1 लाख का बोनस। दो रास्ते।", or_="या",
        a_lbl="रास्ता A", a_h="खर्च करें।", a_s="2 हफ़्ते में ख़त्म।",
        b_lbl="रास्ता B", b_h="निवेश करें।", b_s="15 साल में &asymp; &#8377;5.5 लाख*।",
        s_alert=("बैंक अलर्ट", "&#8377;1,00,000 का बोनस क्रेडिट हुआ"), s_h="अपने बोनस को काम पर लगाइए।",
        s_sub="इससे पहले कि सेल उसे खर्च करवा दे।",
        b_h1='अगली दिवाली <span class="o">आपका बोनस कहाँ होगा?</span>',
        b_sub="थोड़ा खर्च करें, बाकी निवेश करें। एकमुश्त या STP: हम चुनने में मदद करेंगे।",
        yrs=["आज", "5 साल", "10 साल", "15 साल"]),
}

BAG = ('<svg viewBox="0 0 64 64" width="100%" height="100%"><path d="M22 22v-6a10 10 0 0 1 20 0v6" stroke="{c}" stroke-width="4" '
       'fill="none"/><path d="M12 22h40l-3 34H15z" fill="{c}"/></svg>')
ARROW = ('<svg viewBox="0 0 64 64" width="100%" height="100%"><path d="M6 52 24 34l10 10 20-24" stroke="{c}" stroke-width="7" '
         'fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M40 16h18v18" stroke="{c}" stroke-width="7" '
         'fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def panels(lang, t):
    front = dict(bg="var(--orange)", legal="dark", note=True, css="""
.b { position:absolute; right:0; top:0; bottom:0; width:52%; background:var(--navy); }
.top { position:absolute; left:0; right:0; top:22px; text-align:center; z-index:2; }
.top span { background:#fff; color:var(--navy); font-weight:800; font-size:26px; padding:8px 22px; border-radius:40px;
  box-shadow:0 6px 16px rgba(0,0,0,.2); }
.or { position:absolute; left:48%; top:50%; width:84px; height:84px; margin:-30px 0 0 -42px; border-radius:50%; background:#fff;
  color:var(--navy); font-weight:800; font-size:28px; display:flex; align-items:center; justify-content:center; z-index:2;
  box-shadow:0 8px 20px rgba(0,0,0,.25); }
.side { position:absolute; top:72px; color:#fff; display:flex; gap:24px; align-items:center; }
.side.a { left:60px; } .side.bb { left:52%; margin-left:80px; }
.side .ic { width:96px; height:96px; flex:none; }
.side .l { font-size:20px; font-weight:800; opacity:.8; }
.side .h { font-family:var(--display); font-weight:var(--dw); font-size:50px; line-height:var(--lt); }
.side .s { font-size:24px; font-weight:700; }
.side.bb .s { color:var(--orange); }
.row { position:absolute; left:52%; margin-left:80px; right:60px; bottom:12px; display:flex; justify-content:space-between; align-items:center; color:#fff; }
""", html=f"""
<div class="b"></div><div class="top"><span>{t['top']}</span></div><div class="or">{t['or_']}</div>
<div class="side a"><div class="ic">{BAG.replace('{c}', '#fff')}</div><div><div class="l">{t['a_lbl']}</div><div class="h">{t['a_h']}</div><div class="s">{t['a_s']}</div></div></div>
<div class="side bb"><div class="ic">{ARROW.replace('{c}', '#FF4A00')}</div><div><div class="l">{t['b_lbl']}</div><div class="h">{t['b_h']}</div><div class="s">{t['b_s']}</div></div></div>
<div class="row">{logo(36, chip=True)}{call(42)}</div>""")

    vals = [1.12 ** y for y in (0, 5, 10, 15)]
    unit = "लाख" if lang == "hi" else "lakh"
    bars = ""
    for i, (v, y) in enumerate(zip(vals, t["yrs"])):
        bars += (f'<div class="bw"><div class="bv{" hl" if i == 3 else ""}">&#8377;{v:.1f} {unit}{"*" if i else ""}</div>'
                 f'<div class="br{" hl" if i == 3 else ""}" style="height:{170 * v / vals[-1]:.0f}px"></div><div class="by">{y}</div></div>')
    back = dict(bg="#fff", legal="dark", note=True, css="""
.lg { position:absolute; left:44px; top:26px; }
.h1 { position:absolute; left:44px; width:430px; top:92px; font-size:40px; }
.sub { position:absolute; left:44px; width:430px; bottom:26px; font-size:16px; font-weight:600; color:var(--muted); }
.bars { position:absolute; left:520px; top:40px; width:360px; height:270px; display:flex; align-items:flex-end; gap:20px; }
.bw { flex:1; display:flex; flex-direction:column; align-items:center; justify-content:flex-end; height:100%; }
.bv { font-weight:800; font-size:15px; margin-bottom:6px; white-space:nowrap; } .bv.hl { color:var(--orange); font-size:19px; }
.br { width:100%; background:var(--navy); border-radius:8px 8px 0 0; } .br.hl { background:var(--orange); }
.by { font-size:13px; color:var(--muted); margin-top:6px; }
.cta { position:absolute; right:0; top:0; bottom:0; width:280px; background:var(--orange); color:#fff; display:flex;
  flex-direction:column; align-items:center; justify-content:center; gap:14px; }
.cta .call .ico { color:#fff; }
""", html=f"""
<div class="lg">{lockup(40)}</div>
<div class="h1 d">{t['b_h1']}</div>
<div class="sub">{t['b_sub']}</div>
<div class="bars">{bars}</div>
<div class="cta">{qr_block(lang, MSG[lang], 128, 14, label_color="#fff")}{call(26)}</div>""")
    return dict(front=front, back=back)


def side(lang, t):
    return dict(bg="var(--navy)", note=False, css="""
.lk { position:absolute; left:24px; top:18px; }
.alert { position:absolute; left:24px; right:24px; top:62px; background:#fff; border-radius:14px; padding:10px 14px;
  display:flex; align-items:center; gap:12px; box-shadow:0 10px 24px rgba(0,0,0,.3); }
.alert .rs { width:36px; height:36px; flex:none; border-radius:50%; background:var(--orange); color:#fff; font-weight:800;
  font-size:20px; display:flex; align-items:center; justify-content:center; font-family:'DM Sans', sans-serif; }
.alert .k { font-size:12px; font-weight:700; color:var(--muted); }
.alert .v { font-size:16px; font-weight:800; color:var(--navy); white-space:nowrap; }
.hl { position:absolute; left:24px; right:24px; top:136px; color:#fff; font-size:32px; }
body.hi .hl { font-size:30px; }
.sub { position:absolute; left:24px; right:24px; top:210px; color:var(--orange); font-size:18px; font-weight:700; }
""", html=f"""
<div class="lk">{lockup(22, chip=True)}</div>
<div class="alert"><div class="rs">&#8377;</div><div><div class="k">{t['s_alert'][0]}</div><div class="v">{t['s_alert'][1]}</div></div></div>
<div class="hl d">{t['s_h']}</div><div class="sub">{t['s_sub']}</div>
{side_cta(lang, MSG[lang], color="#fff")}""")
