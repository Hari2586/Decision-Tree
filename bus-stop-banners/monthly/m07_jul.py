"""July: monsoon. Nobody buys an umbrella in the middle of a storm (emergency fund)."""
from framework import call, logo, qr_block

KEY = "07-jul"
MSG = {"en": "Hi MoneyHoney! I saw your bus stop ad. I want to build an emergency fund.",
       "hi": "Namaste MoneyHoney! Maine bus stop par aapka ad dekha. Mujhe emergency fund banana hai."}
NOTE = {"en": "*Example for illustration only. Your emergency fund depends on your own expenses and needs.",
        "hi": "*केवल उदाहरण। आपका emergency fund आपके अपने खर्चों और ज़रूरतों पर निर्भर करता है।"}
T = {
    "en": dict(
        f_h1="Nobody buys an umbrella in the middle of a storm.",
        f_h2="Build your emergency fund before you need it.",
        l_words=["Job loss.", "Hospital bill.", "Urgent repair."], l_cap="Life doesn&rsquo;t check the forecast.",
        r_big="6 months", r_cap="of expenses, kept ready. Your financial umbrella.",
        b_h1='How big should <span class="o">your umbrella</span> be?',
        b_sub="Keep 6 months of expenses safe, easy to withdraw, and separate from long-term money.",
        eq=[("&#8377;40,000", "monthly expenses"), ("6 months", "of cover"), ("&#8377;2.4 lakh*", "emergency fund")]),
    "hi": dict(
        f_h1="तूफ़ान के बीच कोई छाता नहीं खरीदता।",
        f_h2="Emergency fund ज़रूरत से पहले बनाइए।",
        l_words=["नौकरी जाना।", "अस्पताल का बिल।", "अचानक मरम्मत।"], l_cap="मुसीबत मौसम देखकर नहीं आती।",
        r_big="6 महीने", r_cap="के खर्च, हमेशा तैयार। यही है आपका financial छाता।",
        b_h1='आपका <span class="o">छाता</span> कितना बड़ा हो?',
        b_sub="6 महीने के खर्च सुरक्षित रखें, आसानी से निकालने लायक और लंबी अवधि के पैसों से अलग।",
        eq=[("&#8377;40,000", "महीने का खर्च"), ("6 महीने", "की सुरक्षा"), ("&#8377;2.4 लाख*", "emergency fund")]),
}

UMBRELLA = ('<svg viewBox="0 0 120 120" width="100%" height="100%"><path d="M60 10C30 10 8 32 6 58c6-6 12-6 18 0 6-6 12-6 18 '
            '0 6-6 12-6 18 0 6-6 12-6 18 0 6-6 12-6 18 0 6-6 12-6 18 0C112 32 90 10 60 10z" fill="{c1}"/><path d="M60 '
            '10c-12 10-18 28-18 48M60 10c12 10 18 28 18 48" stroke="{c2}" stroke-width="2.5" fill="none" opacity=".35"/>'
            '<path d="M60 58v42a8 8 0 0 1-16 0" stroke="{c2}" stroke-width="5" fill="none" stroke-linecap="round"/></svg>')
RAIN = ("background-color:#0C1632; background-image:repeating-linear-gradient(105deg, rgba(255,255,255,.07) 0 2px, "
        "transparent 2px 26px), repeating-linear-gradient(105deg, rgba(255,255,255,.04) 0 1px, transparent 1px 13px);")


def umb(c1, c2):
    return UMBRELLA.replace("{c1}", c1).replace("{c2}", c2)


def panels(lang, t):
    front = dict(bg="#0C1632", legal="navy", note=False, css=f".stage {{ {RAIN} }}" + """
.u { position:absolute; left:70px; top:30px; width:300px; height:300px; }
.dry { position:absolute; left:92px; top:168px; width:256px; height:160px; background:#0C1632;
  clip-path:polygon(0 0, 100% 0, 88% 100%, 12% 100%); opacity:.9; }
.copy { position:absolute; left:440px; right:60px; top:44px; color:#fff; }
.copy .a { font-size:50px; } .copy .b { font-size:30px; color:var(--orange); font-weight:800; margin-top:14px; font-family:var(--sans); }
.row { position:absolute; left:440px; right:60px; bottom:26px; display:flex; justify-content:space-between; align-items:center; color:#fff; }
""", html=f"""
<div class="u">{umb('#E8511A', '#fff')}</div>
<div class="copy"><div class="a d">{t['f_h1']}</div><div class="b">{t['f_h2']}</div></div>
<div class="row">{logo(40, chip=True)}{call(46)}</div>""")

    words = "".join(f"<div>{w}</div>" for w in t["l_words"])
    left = dict(bg="#0C1632", legal="navy", note=False, css=f".stage {{ {RAIN} }}" + """
.words { position:absolute; left:30px; right:24px; top:34px; color:#fff; font-size:42px; font-family:var(--sans); font-weight:800; line-height:var(--lt); }
.words div:nth-child(2) { color:var(--orange); }
.cap { position:absolute; left:30px; right:24px; top:228px; color:rgba(255,255,255,.85); font-size:24px; }
.bot { position:absolute; left:30px; bottom:14px; color:#fff; }
.lg { position:absolute; right:24px; bottom:14px; }
""", html=f"""
<div class="words">{words}</div><div class="cap d">{t['l_cap']}</div>
<div class="bot">{call(26)}</div><div class="lg">{logo(18, chip=True)}</div>""")

    right = dict(bg="var(--orange)", legal="navy", note=True, css="""
.u { position:absolute; right:24px; top:20px; width:118px; height:118px; }
.big { position:absolute; left:28px; top:156px; color:#fff; font-size:70px; font-family:var(--sans); font-weight:800; line-height:1; }
.cap { position:absolute; left:30px; right:26px; top:232px; color:var(--navy); font-size:20px; font-weight:700; line-height:1.3; }
.bot { position:absolute; left:30px; bottom:14px; color:#fff; }
.bot .call .ico { color:var(--navy); }
.lg { position:absolute; left:28px; top:28px; }
""", html=f"""
<div class="lg">{logo(22, chip=True)}</div><div class="u">{umb('#fff', '#1B2666')}</div>
<div class="big">{t['r_big']}</div><div class="cap">{t['r_cap']}</div><div class="bot">{call(28)}</div>""")

    eq = t["eq"]
    back = dict(bg="#0C1632", legal="navy", note=True, css=f".stage {{ {RAIN} }}" + """
.lg { position:absolute; left:44px; top:26px; }
.h1 { position:absolute; left:44px; right:340px; top:92px; color:#fff; font-size:40px; }
.eq { position:absolute; left:44px; right:340px; top:170px; display:flex; align-items:center; gap:14px; }
.eq .t { flex:1; background:rgba(255,255,255,.06); border:2px solid rgba(255,255,255,.18); border-radius:12px; padding:10px 14px; color:#fff; }
.eq .t.hl { background:var(--orange); border-color:var(--orange); }
.eq .v { font-family:var(--display); font-weight:var(--dw); font-size:32px; line-height:1.1; white-space:nowrap; }
.eq .l { font-size:14px; opacity:.85; margin-top:2px; }
.eq .op { color:var(--orange); font-size:36px; font-weight:800; }
.sub { position:absolute; left:44px; right:340px; bottom:26px; color:rgba(255,255,255,.8); font-size:16px; }
.cta { position:absolute; right:0; top:0; bottom:0; width:300px; background:#fff; display:flex; flex-direction:column;
  align-items:center; justify-content:center; gap:12px; }
.cta .u { width:70px; height:70px; position:absolute; top:16px; right:18px; opacity:.9; }
""", html=f"""
<div class="lg">{logo(40, chip=True)}</div>
<div class="h1 d">{t['b_h1']}</div>
<div class="eq"><div class="t"><div class="v">{eq[0][0]}</div><div class="l">{eq[0][1]}</div></div><div class="op">&times;</div>
<div class="t"><div class="v">{eq[1][0]}</div><div class="l">{eq[1][1]}</div></div><div class="op">=</div>
<div class="t hl"><div class="v">{eq[2][0]}</div><div class="l">{eq[2][1]}</div></div></div>
<div class="sub">{t['b_sub']}</div>
<div class="cta">{qr_block(lang, MSG[lang], 128, 14)}{call(26)}</div>""")
    return dict(front=front, left=left, right=right, back=back)
