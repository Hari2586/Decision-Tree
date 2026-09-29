"""April: appraisal season. Your salary got a hike, give your SIP one too (step-up SIP)."""
from framework import call, lockup, logo, qr_block, side_cta

KEY = "04-apr"
MSG = {"en": 'Hi! Bus stop ad: I want to step up my SIP.',
       "hi": 'Hi! Bus stop ad: Meri SIP badhani hai.'}
NOTE = ("*Illustration: &#8377;5,000 monthly SIP for 20 years at an assumed 12% p.a. return, with and without a "
              "10% yearly step-up, for understanding only. Mutual funds do not guarantee returns.")
SIDE_NOTE = "*Illustration: &#8377;5,000/month SIP for 20 years at an assumed 12% p.a.; step-up adds 10% a year."

T = {
    "en": dict(
        sal="Salary", sip="SIP", f_h1="Your salary got a hike.", f_h2="Did your SIP?",
        f_sub="Let your SIP grow with your salary.",
        s_a="&#8377;50 lakh*", s_b="&#8377;99 lakh*", s_cap="Same &#8377;5,000 start. Just 10% more each year.",
        b_h1='Step-up SIP: <span class="o">the easiest raise you&rsquo;ll ever give yourself.</span>',
        b_flat="Regular SIP &asymp; &#8377;50 lakh*", b_step="Step-up SIP &asymp; &#8377;99 lakh*", b_y="20 years"),
    "hi": dict(
        sal="सैलरी", sip="SIP", f_h1="आपकी सैलरी बढ़ी।", f_h2="क्या आपकी SIP बढ़ी?",
        f_sub="अपनी SIP को भी सैलरी के साथ बढ़ने दीजिए।",
        s_a="&#8377;50 लाख*", s_b="&#8377;99 लाख*", s_cap="वही &#8377;5,000 की शुरुआत। बस हर साल 10% ज़्यादा।",
        b_h1='स्टेप-अप SIP: <span class="o">खुद को दिया गया सबसे आसान इंक्रीमेंट।</span>',
        b_flat="सामान्य SIP &asymp; &#8377;50 लाख*", b_step="स्टेप-अप SIP &asymp; &#8377;99 लाख*", b_y="20 साल"),
}


def _series(step):
    out, fv, amt = [], 0.0, 5000.0
    for y in range(20):
        for _ in range(12):
            fv = (fv + amt) * 1.01
        out.append(fv)
        amt *= 1 + step
    return out


def _chart(w, h):
    flat, up = _series(0), _series(.10)
    top = up[-1]

    def pts(vals):
        return " ".join(f"{(i + 1) * w / 20:.1f},{h - v / top * (h - 8):.1f}" for i, v in enumerate(vals))
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<polygon points="0,{h} {pts(up)} {w},{h}" fill="rgba(232,81,26,.14)"/>'
            f'<polyline points="0,{h} {pts(up)}" fill="none" stroke="#E8511A" stroke-width="5" stroke-linejoin="round"/>'
            f'<polyline points="0,{h} {pts(flat)}" fill="none" stroke="#1B2666" stroke-width="4" stroke-dasharray="10 8"/>'
            f'<line x1="0" y1="{h}" x2="{w}" y2="{h}" stroke="#B0B8C5" stroke-width="2"/></svg>')


def _stairs(n, w, h, color="#E8511A"):
    sw, sh = w / n, h / n
    d = f"M0 {h} " + " ".join(f"V{h - (i + 1) * sh:.1f} H{(i + 1) * sw:.1f}" for i in range(n)) + f" V{h} Z"
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><path d="{d}" fill="{color}"/></svg>'


def panels(lang, t):
    front = dict(bg="#fff", legal="navy", note=True, css="""
.meters { position:absolute; left:60px; top:44px; width:520px; }
.m { display:flex; align-items:center; gap:18px; border-bottom:3px solid var(--line); padding:12px 0; }
.m .k { width:150px; font-size:30px; font-weight:700; color:var(--muted); }
.m .v { font-family:'DM Sans'; font-weight:800; font-size:78px; line-height:1; }
.m .arr { font-size:60px; font-weight:800; font-family:'DM Sans', sans-serif; }
.m.up .v, .m.up .arr { color:var(--navy); }
.m.flat .v { color:var(--lmuted); }
.m.flat .arr { color:var(--orange); font-family:'Lora', serif; font-weight:700; font-size:78px; line-height:1; }
.copy { position:absolute; left:660px; right:60px; top:48px; }
.copy .a { font-size:52px; } .copy .b { font-size:52px; color:var(--orange); }
.copy .c { font-size:19px; margin-top:6px; color:var(--muted); font-weight:600; }
.row { position:absolute; left:660px; right:60px; bottom:26px; display:flex; justify-content:space-between; align-items:center; }
.st { position:absolute; left:0; bottom:0; opacity:.07; }
""", html=f"""
<div class="meters"><div class="m up"><div class="k">{t['sal']}</div><div class="v">+10%</div><div class="arr">&uarr;</div></div>
<div class="m flat"><div class="k">{t['sip']}</div><div class="v">+0%</div><div class="arr">?</div></div></div>
<div class="copy"><div class="a d">{t['f_h1']}</div><div class="b d">{t['f_h2']}</div><div class="c">{t['f_sub']}</div></div>
<div class="row">{logo(42)}{call(44)}</div>""")

    back = dict(bg="var(--cream)", legal="navy", note=True, css="""
.lg { position:absolute; left:44px; top:26px; }
.h1 { position:absolute; left:44px; width:420px; top:88px; font-size:34px; }
.chart { position:absolute; left:500px; top:30px; }
.lab { position:absolute; left:520px; font-weight:800; font-size:17px; white-space:nowrap; display:flex; align-items:center; gap:10px; }
.lab i { display:inline-block; width:34px; border-top:5px solid var(--orange); }
.lab.fl i { border-top:4px dashed var(--navy); }
.lab.up { color:var(--orange); top:44px; }
.lab.fl { color:var(--navy); top:74px; }
.ax { position:absolute; left:500px; top:292px; font-size:13px; color:var(--muted); width:380px; display:flex; justify-content:space-between; }
.cta { position:absolute; right:0; top:0; bottom:0; width:260px; background:var(--navy); color:#fff; display:flex;
  flex-direction:column; align-items:center; justify-content:center; gap:14px; }
""", html=f"""
<div class="lg">{lockup(40)}</div>
<div class="h1 d">{t['b_h1']}</div>
<div class="chart">{_chart(380, 256)}</div>
<div class="lab up"><i></i>{t['b_step']}</div><div class="lab fl"><i></i>{t['b_flat']}</div>
<div class="ax"><span>0</span><span>{t['b_y']}</span></div>
<div class="cta">{qr_block(lang, MSG[lang], 124, 14, label_color="#fff")}{call(24)}</div>""")
    return dict(front=front, back=back)


def side(lang, t):
    return dict(bg="#fff", note=True, css="""
.lk { position:absolute; left:24px; top:18px; }
.stairs { position:absolute; right:24px; top:16px; }
.a { position:absolute; left:24px; top:54px; font-family:'DM Sans', sans-serif; font-weight:800; font-size:26px; line-height:1;
  color:var(--lmuted); text-decoration:line-through; text-decoration-color:var(--orange); text-decoration-thickness:4px; }
.b { position:absolute; left:22px; top:90px; font-size:58px; color:var(--orange); white-space:nowrap; line-height:1.06; }
.cap { position:absolute; left:24px; right:40px; top:162px; font-size:19px; font-weight:700; color:var(--navy); line-height:1.25; }
""", html=f"""
<div class="lk">{lockup(24)}</div>
<div class="stairs">{_stairs(6, 70, 70)}</div>
<div class="a">{t['s_a']}</div><div class="b d">{t['s_b']}</div><div class="cap">{t['s_cap']}</div>
{side_cta(lang, MSG[lang])}""")
