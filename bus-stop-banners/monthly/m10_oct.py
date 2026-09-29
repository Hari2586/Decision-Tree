"""October: Diwali. Crackers last 10 seconds, this gift lasts 18 years (gift a SIP to your child)."""
from framework import call, lockup, logo, qr_block, side_cta

KEY = "10-oct"
MSG = {"en": 'Hi! Bus stop ad: Gift a SIP this Diwali.',
       "hi": 'Hi! Bus stop ad: Diwali par SIP gift karni hai.'}
NOTE = ('*Illustration: &#8377;2,000 monthly SIP for 18 years at an assumed 12% p.a. return. Not guaranteed. '
        'This assumption of returns is not indicative of future returns.')
SIDE_NOTE = ('*Illustration: &#8377;2,000 monthly SIP for 18 years at an assumed 12% p.a. return. Not guaranteed. '
             'This assumption of returns is not indicative of future returns.')

T = {
    "en": dict(
        f_h1="Crackers last 10 seconds.", f_h2="This Diwali gift lasts 18 years.", f_sub="Gift your child a SIP.",
        s_big="SIP", s_dur="18 years", s_cap="&asymp; &#8377;15 lakh* by the time they turn 18.",
        b_h1='The gift that <span class="o">grows up with them.</span>',
        tag="For illustration only",
        steps=[("Birth", "&#8377;2,000 a month"), ("Age 6", "&asymp; &#8377;2.1 lakh*"), ("Age 12", "&asymp; &#8377;6.4 lakh*"),
               ("Age 18", "&asymp; &#8377;15 lakh*")],
        inv="Your total investment: &#8377;4.3 lakh",
        b_sub="Start a SIP in your child&rsquo;s name this festive season."),
    "hi": dict(
        f_h1="पटाखे 10 सेकंड चलते हैं।", f_h2="इस दिवाली का तोहफ़ा 18 साल चलेगा।", f_sub="अपने बच्चे को SIP गिफ़्ट करें।",
        s_big="SIP", s_dur="18 साल", s_cap="18 का होने तक &asymp; &#8377;15 लाख*।",
        b_h1='ऐसा तोहफ़ा, <span class="o">जो बच्चे के साथ बड़ा हो।</span>',
        tag="केवल उदाहरण के लिए",
        steps=[("जन्म", "&#8377;2,000 हर महीने"), ("6 साल", "&asymp; &#8377;2.1 लाख*"), ("12 साल", "&asymp; &#8377;6.4 लाख*"),
               ("18 साल", "&asymp; &#8377;15 लाख*")],
        inv="आपका कुल निवेश: &#8377;4.3 लाख",
        b_sub="इस त्योहार, अपने बच्चे के नाम पर SIP शुरू करें।"),
}

def diya(bowl="#E8511A", flame="#E8511A", glow="#E8511A", dots="#F4EFE9", gid="gl"):
    return (f'<svg viewBox="0 0 120 120" width="100%" height="100%"><defs><radialGradient id="{gid}"><stop offset="0" '
            f'stop-color="{glow}" stop-opacity=".5"/><stop offset="1" stop-color="{glow}" stop-opacity="0"/></radialGradient>'
            f'</defs><circle cx="60" cy="46" r="44" fill="url(#{gid})"/><path d="M60 18c8 12 12 20 12 27a12 12 0 0 1-24 0'
            f'c0-7 4-15 12-27z" fill="{flame}"/><path d="M60 32c4 6 6 10 6 14a6 6 0 0 1-12 0c0-4 2-8 6-14z" fill="#fff"/>'
            f'<path d="M14 66h92c-4 24-22 38-46 38S18 90 14 66z" fill="{bowl}"/><path d="M26 74h68" stroke="{dots}" '
            f'stroke-width="3" stroke-dasharray="2 7" stroke-linecap="round"/></svg>')


DIYA = diya()
SPARKLE = ("background-color:#0C1632; background-image:radial-gradient(circle, rgba(232,81,26,.6) 0 1.6px, transparent 2.2px), "
           "radial-gradient(circle, rgba(255,255,255,.35) 0 1.2px, transparent 1.8px); background-size:46px 46px, 73px 73px; "
           "background-position:0 0, 20px 30px;")


def panels(lang, t):
    front = dict(bg="#0C1632", legal="navy", note=False, css=f".stage {{ {SPARKLE} }}" + """
.dy { position:absolute; left:80px; top:30px; width:300px; height:300px; }
.copy { position:absolute; left:450px; right:60px; top:42px; color:#fff; }
.copy .a { font-size:40px; color:rgba(255,255,255,.75); font-family:var(--sans); font-weight:800; line-height:var(--lt); }
.copy .b { font-size:56px; color:var(--orange); margin-top:4px; }
.copy .c { font-size:24px; font-weight:700; margin-top:10px; }
.row { position:absolute; left:450px; right:60px; bottom:26px; display:flex; justify-content:space-between; align-items:center; color:#fff; }
.row .call .ico { color:var(--orange); }
""", html=f"""
<div class="dy">{DIYA}</div>
<div class="copy"><div class="a">{t['f_h1']}</div><div class="b d">{t['f_h2']}</div><div class="c">{t['f_sub']}</div></div>
<div class="row">{logo(40, chip=True)}{call(46)}</div>""")

    # growth journey: value of a Rs 2,000/month SIP at 12% p.a. (lakh), plotted on a rising path
    vals = [0.0, 2.1, 6.4, 15.3]
    W, H = 760, 150
    xs = [30, 270, 510, 730]
    ys = [H - 22 - v / vals[-1] * (H - 44) for v in vals]
    path = "M" + " ".join(f"{x},{y:.0f}" for x, y in zip(xs, ys))
    nodes = "".join(f'<circle cx="{x}" cy="{y:.0f}" r="{16 if i == 3 else 9}" fill="{"#E8511A" if i == 3 else "#fff"}" '
                    f'stroke="#E8511A" stroke-width="4"/>' for i, (x, y) in enumerate(zip(xs, ys)))
    labels = "".join(
        f'<div class="ms{" last" if i == 3 else " first" if i == 0 else ""}" style="left:{x}px;top:{y:.0f}px"><div class="v">{v}</div><div class="a">{a_}</div></div>'
        for i, ((a_, v), x, y) in enumerate(zip(t["steps"], xs, ys)))
    back = dict(bg="#0C1632", legal="navy", note=True, css=f".stage {{ {SPARKLE} }}" + """
.lg { position:absolute; left:44px; top:24px; }
.tag { position:absolute; left:400px; top:36px; color:#fff; font-size:13px; font-weight:700; letter-spacing:.06em;
  border:1.5px solid rgba(255,255,255,.55); border-radius:30px; padding:3px 12px; }
.h1 { position:absolute; left:44px; right:340px; top:82px; color:#fff; font-size:38px; }
.journey { position:absolute; left:44px; top:128px; width:760px; height:150px; }
.journey svg { position:absolute; left:0; top:0; }
.ms { position:absolute; transform:translate(-50%, -100%); margin-top:-16px; text-align:center; white-space:nowrap; color:#fff; }
.ms .v { font-family:var(--display); font-weight:var(--dw); font-size:22px; line-height:1.1; }
.ms .a { font-size:13px; opacity:.8; margin-top:2px; }
.ms.last { margin-top:-24px; } .ms.last .v { font-size:32px; color:var(--orange); }
.ms.first { transform:translate(-12%, -100%); }
.ms.first .v { font-family:var(--sans); font-weight:700; font-size:17px; }
.inv { position:absolute; left:44px; bottom:18px; color:rgba(255,255,255,.9); font-size:16px; font-weight:600; }
.inv b { color:var(--orange); }
.cta { position:absolute; right:0; top:0; bottom:0; width:300px; background:#fff; display:flex; flex-direction:column;
  align-items:center; justify-content:center; gap:12px; border-left:6px solid var(--orange); }
""", html=f"""
<div class="lg">{lockup(38, chip=True)}</div>
<div class="tag">{t['tag']}</div>
<div class="h1 d">{t['b_h1']}</div>
<div class="journey"><svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<path d="{path}" fill="none" stroke="#E8511A" stroke-width="4" stroke-dasharray="2 10" stroke-linecap="round"/>{nodes}</svg>{labels}</div>
<div class="inv">{t['inv']} &middot; {t['b_sub']}</div>
<div class="cta">{qr_block(lang, MSG[lang], 128, 14)}{call(26)}</div>""")
    return dict(front=front, back=back)


def side(lang, t):
    return dict(bg="var(--orange)", note=True, css="""
.lk { position:absolute; left:24px; top:18px; }
.dy { position:absolute; right:14px; top:60px; width:116px; height:116px; }
.stag { position:absolute; left:24px; top:62px; color:#fff; font-size:12px; font-weight:700; letter-spacing:.05em;
  border:1.5px solid rgba(255,255,255,.75); border-radius:30px; padding:2px 10px; }
.big { position:absolute; left:24px; top:84px; color:#fff; font-family:'DM Sans', sans-serif; font-weight:800; font-size:46px; line-height:1; }
.dur { position:absolute; left:24px; top:128px; color:var(--navy); font-family:var(--sans); font-weight:800; font-size:40px; line-height:1.05; }
.cap { position:absolute; left:24px; right:24px; top:176px; color:#fff; font-size:17px; font-weight:700; line-height:1.25; }
""", html=f"""
<div class="lk">{lockup(22, chip=True)}</div>
<div class="dy">{diya(bowl="#1B2666", flame="#fff", glow="#fff", dots="#E8511A", gid="gls")}</div>
<div class="stag">{t['tag']}</div><div class="big lat">{t['s_big']}</div><div class="dur">{t['s_dur']}</div><div class="cap">{t['s_cap']}</div>
{side_cta(lang, MSG[lang], color="var(--navy)", icon="#fff")}""")
