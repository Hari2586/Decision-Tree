"""October: Diwali. Crackers last 10 seconds, this gift lasts 18 years (gift a SIP to your child)."""
from framework import call, logo, qr_block

KEY = "10-oct"
MSG = {"en": "Hi MoneyHoney! I saw your bus stop ad. I want to gift a SIP to my child this Diwali.",
       "hi": "Namaste MoneyHoney! Maine bus stop par aapka ad dekha. Mujhe is Diwali bachche ko SIP gift karni hai."}
NOTE = {"en": "*Illustration: &#8377;2,000 monthly SIP for 18 years at an assumed 12% p.a. return, for understanding only. "
              "Mutual funds do not guarantee returns; actual returns may be higher or lower.",
        "hi": "*उदाहरण: &#8377;2,000 मासिक SIP, 18 साल, 12% वार्षिक अनुमानित रिटर्न पर, केवल समझाने हेतु। म्यूचुअल फंड "
              "रिटर्न की गारंटी नहीं देते; वास्तविक रिटर्न कम या ज़्यादा हो सकते हैं।"}
T = {
    "en": dict(
        f_h1="Crackers last 10 seconds.", f_h2="This Diwali gift lasts 18 years.", f_sub="Gift your child a SIP.",
        l_rows=[("Sweets", "2 days"), ("Crackers", "10 seconds"), ("New clothes", "1 season")], l_q="Most Diwali gifts don&rsquo;t last.",
        r_big="SIP", r_dur="18 years", r_cap="&asymp; &#8377;15 lakh* by the time they turn 18.",
        b_h1='The gift that <span class="g">grows up with them.</span>',
        eq=[("&#8377;2,000", "a month, from birth"), ("18 years", "of growing together"), ("&asymp; &#8377;15 lakh*", "you invest only &#8377;4.3 lakh")],
        b_sub="Start a SIP in your child&rsquo;s name this festive season."),
    "hi": dict(
        f_h1="पटाखे 10 सेकंड चलते हैं।", f_h2="इस दिवाली का तोहफ़ा 18 साल चलेगा।", f_sub="अपने बच्चे को SIP गिफ़्ट करें।",
        l_rows=[("मिठाई", "2 दिन"), ("पटाखे", "10 सेकंड"), ("नए कपड़े", "1 सीज़न")], l_q="ज़्यादातर दिवाली तोहफ़े टिकते नहीं।",
        r_big="SIP", r_dur="18 साल", r_cap="18 का होने तक &asymp; &#8377;15 लाख*।",
        b_h1='ऐसा तोहफ़ा, <span class="g">जो बच्चे के साथ बड़ा हो।</span>',
        eq=[("&#8377;2,000", "हर महीने, जन्म से"), ("18 साल", "साथ-साथ बढ़ते हुए"), ("&asymp; &#8377;15 लाख*", "आपका निवेश सिर्फ़ &#8377;4.3 लाख")],
        b_sub="इस त्योहार, अपने बच्चे के नाम पर SIP शुरू करें।"),
}

DIYA = ('<svg viewBox="0 0 120 120" width="100%" height="100%"><defs><radialGradient id="gl"><stop offset="0" stop-color="#F6B53D" '
        'stop-opacity=".55"/><stop offset="1" stop-color="#F6B53D" stop-opacity="0"/></radialGradient></defs>'
        '<circle cx="60" cy="46" r="44" fill="url(#gl)"/><path d="M60 18c8 12 12 20 12 27a12 12 0 0 1-24 0c0-7 4-15 12-27z" '
        'fill="#F6B53D"/><path d="M60 32c4 6 6 10 6 14a6 6 0 0 1-12 0c0-4 2-8 6-14z" fill="#fff"/><path d="M14 66h92c-4 '
        '24-22 38-46 38S18 90 14 66z" fill="#E8511A"/><path d="M26 74h68" stroke="#F6B53D" stroke-width="3" '
        'stroke-dasharray="2 7" stroke-linecap="round"/></svg>')
SPARKLE = ("background-color:#0C1632; background-image:radial-gradient(circle, rgba(246,181,61,.55) 0 1.6px, transparent 2.2px), "
           "radial-gradient(circle, rgba(255,255,255,.35) 0 1.2px, transparent 1.8px); background-size:46px 46px, 73px 73px; "
           "background-position:0 0, 20px 30px;")


def panels(lang, t):
    front = dict(bg="#0C1632", legal="navy", note=False, css=f".stage {{ {SPARKLE} }}" + """
.dy { position:absolute; left:80px; top:30px; width:300px; height:300px; }
.copy { position:absolute; left:450px; right:60px; top:42px; color:#fff; }
.copy .a { font-size:40px; color:rgba(255,255,255,.75); font-family:var(--sans); font-weight:800; line-height:var(--lt); }
.copy .b { font-size:56px; color:var(--gold); margin-top:4px; }
.copy .c { font-size:24px; font-weight:700; margin-top:10px; }
.row { position:absolute; left:450px; right:60px; bottom:26px; display:flex; justify-content:space-between; align-items:center; color:#fff; }
.row .call .ico { color:var(--gold); }
""", html=f"""
<div class="dy">{DIYA}</div>
<div class="copy"><div class="a">{t['f_h1']}</div><div class="b d">{t['f_h2']}</div><div class="c">{t['f_sub']}</div></div>
<div class="row">{logo(40, chip=True)}{call(46)}</div>""")

    rows = "".join(f'<div class="r"><span>{a}</span><b>{b}</b></div>' for a, b in t["l_rows"])
    left = dict(bg="#0C1632", legal="navy", note=False, css=f".stage {{ {SPARKLE} }}" + """
.rows { position:absolute; left:28px; right:26px; top:26px; }
.r { display:flex; justify-content:space-between; align-items:baseline; border-bottom:2px dashed rgba(255,255,255,.25); padding:8px 0; color:#fff; }
.r span { font-size:24px; font-weight:600; opacity:.85; } .r b { font-size:30px; font-weight:800; color:var(--gold); }
.q { position:absolute; left:28px; right:26px; bottom:52px; color:#fff; font-size:24px; }
.bot { position:absolute; left:28px; bottom:14px; color:#fff; } .bot .call .ico { color:var(--gold); }
.lg { position:absolute; right:24px; bottom:14px; }
""", html=f"""
<div class="rows">{rows}</div><div class="q d">{t['l_q']}</div>
<div class="bot">{call(26)}</div><div class="lg">{logo(18, chip=True)}</div>""")

    right = dict(bg="var(--orange)", legal="navy", note=True, css="""
.dy { position:absolute; right:14px; top:8px; width:112px; height:112px; }
.big { position:absolute; left:28px; top:40px; color:#fff; font-family:'DM Sans'; font-weight:800; font-size:64px; line-height:1; }
.dur { position:absolute; left:28px; top:112px; color:var(--navy); font-family:var(--sans); font-weight:800; font-size:56px; line-height:1.05; }
.cap { position:absolute; left:30px; right:26px; top:212px; color:#fff; font-size:22px; font-weight:700; }
.bot { position:absolute; left:30px; bottom:14px; color:var(--navy); } .bot .call .ico { color:#fff; }
.lg { position:absolute; right:24px; bottom:16px; }
""", html=f"""
<div class="dy">{DIYA.replace('#E8511A', '#1B2666')}</div>
<div class="big">{t['r_big']}</div><div class="dur">{t['r_dur']}</div><div class="cap">{t['r_cap']}</div>
<div class="bot">{call(26)}</div><div class="lg">{logo(18, chip=True)}</div>""")

    eq = t["eq"]
    back = dict(bg="#0C1632", legal="navy", note=True, css=f".stage {{ {SPARKLE} }}" + """
.lg { position:absolute; left:44px; top:26px; }
.h1 { position:absolute; left:44px; right:340px; top:92px; color:#fff; font-size:40px; }
.eq { position:absolute; left:44px; right:340px; top:180px; display:flex; align-items:center; gap:12px; }
.eq .t { flex:1; border:2px solid rgba(246,181,61,.5); border-radius:12px; padding:10px 14px; color:#fff; background:rgba(12,22,50,.7); }
.eq .t.hl { background:var(--gold); border-color:var(--gold); color:var(--ink); }
.eq .v { font-family:var(--display); font-weight:var(--dw); font-size:30px; white-space:nowrap; line-height:1.1; }
.eq .l { font-size:14px; opacity:.85; margin-top:2px; }
.eq .op { color:var(--gold); font-size:34px; font-weight:800; }
.sub { position:absolute; left:44px; right:340px; bottom:26px; color:rgba(255,255,255,.85); font-size:17px; font-weight:600; }
.cta { position:absolute; right:0; top:0; bottom:0; width:300px; background:#fff; display:flex; flex-direction:column;
  align-items:center; justify-content:center; gap:12px; border-left:6px solid var(--gold); }
""", html=f"""
<div class="lg">{logo(40, chip=True)}</div>
<div class="h1 d">{t['b_h1']}</div>
<div class="eq"><div class="t"><div class="v">{eq[0][0]}</div><div class="l">{eq[0][1]}</div></div><div class="op">&times;</div>
<div class="t"><div class="v">{eq[1][0]}</div><div class="l">{eq[1][1]}</div></div><div class="op">=</div>
<div class="t hl"><div class="v">{eq[2][0]}</div><div class="l">{eq[2][1]}</div></div></div>
<div class="sub">{t['b_sub']}</div>
<div class="cta">{qr_block(lang, MSG[lang], 128, 14)}{call(26)}</div>""")
    return dict(front=front, left=left, right=right, back=back)
