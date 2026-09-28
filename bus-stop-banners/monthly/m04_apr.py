"""April: appraisal season. Your salary got a hike, give your SIP one too (step-up SIP)."""
from framework import call, logo, qr_block

KEY = "04-apr"
MSG = {"en": "Hi MoneyHoney! I saw your bus stop ad. I want to step up my SIP.",
       "hi": "Namaste MoneyHoney! Maine bus stop par aapka ad dekha. Mujhe apni SIP badhani hai."}
NOTE = {"en": "*Illustration: &#8377;5,000 monthly SIP for 20 years at an assumed 12% p.a. return, with and without a "
              "10% yearly step-up, for understanding only. Mutual funds do not guarantee returns.",
        "hi": "*उदाहरण: &#8377;5,000 मासिक SIP, 20 साल, 12% वार्षिक अनुमानित रिटर्न पर, 10% सालाना step-up के साथ और "
              "बिना, केवल समझाने हेतु। म्यूचुअल फंड रिटर्न की गारंटी नहीं देते।"}
T = {
    "en": dict(
        sal="Salary", sip="SIP", f_h1="Your salary got a hike.", f_h2="Did your SIP?",
        f_sub="Raise your SIP by 10% every year and see the difference.",
        l_lbl="Appraisal result", l_big="+10%", l_cap="Congrats on the hike! Now pass it on to your SIP.",
        r_a="&#8377;50 lakh", r_b="&#8377;99 lakh*", r_cap="Same &#8377;5,000 SIP. Just 10% more every year.",
        b_h1='Step-up SIP: <span class="o">the easiest raise you&rsquo;ll ever give yourself.</span>',
        b_flat="Regular SIP &asymp; &#8377;50 lakh*", b_step="Step-up SIP &asymp; &#8377;99 lakh*", b_y="20 years"),
    "hi": dict(
        sal="सैलरी", sip="SIP", f_h1="आपकी सैलरी बढ़ी।", f_h2="क्या आपकी SIP बढ़ी?",
        f_sub="हर साल SIP को 10% बढ़ाइए और फ़र्क देखिए।",
        l_lbl="अप्रेज़ल का नतीजा", l_big="+10%", l_cap="हाइक की बधाई! अब यह SIP को भी दीजिए।",
        r_a="&#8377;50 लाख", r_b="&#8377;99 लाख*", r_cap="वही &#8377;5,000 की SIP। बस हर साल 10% ज़्यादा।",
        b_h1='Step-up SIP: <span class="o">खुद को दिया गया सबसे आसान इंक्रीमेंट।</span>',
        b_flat="सामान्य SIP &asymp; &#8377;50 लाख*", b_step="Step-up SIP &asymp; &#8377;99 लाख*", b_y="20 साल"),
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
            f'<line x1="0" y1="{h}" x2="{w}" y2="{h}" stroke="#C9CFE0" stroke-width="2"/></svg>')


def _stairs(n, w, h, color="#E8511A"):
    sw, sh = w / n, h / n
    d = f"M0 {h} " + " ".join(f"V{h - (i + 1) * sh:.1f} H{(i + 1) * sw:.1f}" for i in range(n)) + f" V{h} Z"
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><path d="{d}" fill="{color}"/></svg>'


def panels(lang, t):
    front = dict(bg="#fff", legal="navy", note=True, css="""
.meters { position:absolute; left:60px; top:44px; width:520px; }
.m { display:flex; align-items:center; gap:18px; border-bottom:3px solid #EEF0F6; padding:12px 0; }
.m .k { width:150px; font-size:30px; font-weight:700; color:var(--muted); }
.m .v { font-family:'DM Sans'; font-weight:800; font-size:78px; line-height:1; }
.m .arr { font-size:60px; font-weight:800; }
.m.up .v, .m.up .arr { color:var(--navy); }
.m.flat .v, .m.flat .arr { color:#B7BDCC; }
.q { position:absolute; left:470px; top:222px; font-family:'Lora'; font-weight:700; font-size:90px; color:var(--orange); }
.copy { position:absolute; left:660px; right:60px; top:48px; }
.copy .a { font-size:52px; } .copy .b { font-size:52px; color:var(--orange); }
.copy .c { font-size:21px; margin-top:12px; color:var(--muted); font-weight:600; }
.row { position:absolute; left:660px; right:60px; bottom:26px; display:flex; justify-content:space-between; align-items:center; }
.st { position:absolute; left:0; bottom:0; opacity:.07; }
""", html=f"""
<div class="meters"><div class="m up"><div class="k">{t['sal']}</div><div class="v">+10%</div><div class="arr">&uarr;</div></div>
<div class="m flat"><div class="k">{t['sip']}</div><div class="v">+0%</div><div class="arr">&rarr;</div></div></div>
<div class="q">?</div>
<div class="copy"><div class="a d">{t['f_h1']}</div><div class="b d">{t['f_h2']}</div><div class="c">{t['f_sub']}</div></div>
<div class="row">{logo(42)}{call(44)}</div>""")

    left = dict(bg="var(--navy)", legal="dark", note=False, css="""
.lbl { position:absolute; left:30px; top:78px; color:rgba(255,255,255,.7); font-size:17px; font-weight:700; letter-spacing:.12em; text-transform:uppercase; }
.big { position:absolute; left:24px; top:98px; color:#fff; font-family:'DM Sans'; font-weight:800; font-size:108px; line-height:1; }
.big span { color:var(--orange); font-size:.6em; vertical-align:.45em; }
.cap { position:absolute; left:30px; right:26px; top:236px; color:#fff; font-size:22px; }
.lg { position:absolute; left:28px; top:22px; }
.bot { position:absolute; left:30px; bottom:14px; color:#fff; }
.env { position:absolute; right:24px; top:22px; width:64px; height:44px; border:3px solid rgba(255,255,255,.35); border-radius:6px; }
.env::after { content:''; position:absolute; left:6px; right:6px; top:4px; height:22px; border-bottom:3px solid rgba(255,255,255,.35);
  border-right:3px solid rgba(255,255,255,.35); transform:skewY(0) rotate(0); }
""", html=f"""
<div class="lg">{logo(24, chip=True)}</div>
<div class="lbl">{t['l_lbl']}</div><div class="big">+10%<span>&uarr;</span></div>
<div class="cap d">{t['l_cap']}</div><div class="bot">{call(28)}</div>""")

    right = dict(bg="#fff", legal="navy", note=True, css="""
.stairs { position:absolute; right:0; bottom:0; }
.a { position:absolute; left:30px; top:40px; font-family:'DM Sans'; font-weight:800; font-size:40px; color:#B7BDCC;
  text-decoration:line-through; text-decoration-thickness:4px; }
.b { position:absolute; left:28px; top:88px; font-size:72px; color:var(--orange); white-space:nowrap; }
.cap { position:absolute; left:30px; right:150px; top:186px; font-size:19px; font-weight:700; color:var(--navy); line-height:1.3; }
.bot { position:absolute; left:30px; bottom:14px; }
.lg { position:absolute; right:24px; top:24px; }
""", html=f"""
<div class="stairs">{_stairs(8, 150, 150)}</div><div class="lg">{logo(22)}</div>
<div class="a">{t['r_a']}</div><div class="b d">{t['r_b']}</div><div class="cap">{t['r_cap']}</div>
<div class="bot">{call(28)}</div>""")

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
<div class="lg">{logo(42)}</div>
<div class="h1 d">{t['b_h1']}</div>
<div class="chart">{_chart(380, 256)}</div>
<div class="lab up"><i></i>{t['b_step']}</div><div class="lab fl"><i></i>{t['b_flat']}</div>
<div class="ax"><span>0</span><span>{t['b_y']}</span></div>
<div class="cta">{qr_block(lang, MSG[lang], 124, 14, label_color="#fff")}{call(24)}</div>""")
    return dict(front=front, left=left, right=right, back=back)
