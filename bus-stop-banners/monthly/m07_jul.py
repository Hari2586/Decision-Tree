"""July: monsoon. Nobody buys an umbrella in the middle of a storm (emergency fund)."""
from framework import call, lockup, logo, qr_block, side_cta

KEY = "07-jul"
MSG = {"en": 'Hi! Bus stop ad: Build my emergency fund.',
       "hi": 'Hi! Bus stop ad: Emergency fund banana hai.'}
NOTE = ("*Example for illustration only. Your emergency fund depends on your own expenses and needs.")
SIDE_NOTE = ''

T = {
    "en": dict(
        f_h1="Nobody buys an umbrella in the middle of a storm.",
        f_h2="Build your emergency fund before you need it.",
        s_words=["Job loss.", "Hospital bill.", "Urgent repair."], s_cap="Life doesn&rsquo;t check the forecast.",
        b_h1='How big should <span class="o">your umbrella</span> be?',
        b_sub="Keep 6 months of expenses set aside, easy to withdraw, and separate from long-term money.",
        eq=[("&#8377;40,000", "monthly expenses"), ("6 months", "of cover"), ("&#8377;2.4 lakh*", "emergency fund")]),
    "hi": dict(
        f_h1="तूफ़ान के बीच कोई छाता नहीं खरीदता।",
        f_h2="इमरजेंसी फंड ज़रूरत से पहले बनाइए।",
        s_words=["नौकरी जाना।", "अस्पताल का बिल।", "अचानक मरम्मत।"], s_cap="मुसीबत मौसम देखकर नहीं आती।",
        b_h1='आपका <span class="o">छाता</span> कितना बड़ा हो?',
        b_sub="6 महीने के खर्च अलग रखें, जो ज़रूरत पड़ने पर आसानी से निकल सकें।",
        eq=[("&#8377;40,000", "महीने का खर्च"), ("6 महीने", "की सुरक्षा"), ("&#8377;2.4 लाख*", "इमरजेंसी फंड")]),
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
.u { position:absolute; left:90px; top:18px; width:250px; height:250px; }
.dry { position:absolute; left:92px; top:168px; width:256px; height:160px; background:#0C1632;
  clip-path:polygon(0 0, 100% 0, 88% 100%, 12% 100%); opacity:.9; }
.copy { position:absolute; left:440px; right:60px; top:44px; color:#fff; }
.copy .a { font-size:50px; } .copy .b { font-size:30px; color:var(--orange); font-weight:800; margin-top:14px; font-family:var(--sans); }
.row { position:absolute; left:440px; right:60px; bottom:26px; display:flex; justify-content:space-between; align-items:center; color:#fff; }
""", html=f"""
<div class="u">{umb('#E8511A', '#fff')}</div>
<div class="copy"><div class="a d">{t['f_h1']}</div><div class="b">{t['f_h2']}</div></div>
<div class="row">{logo(40, chip=True)}{call(46)}</div>""")

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
<div class="lg">{lockup(38, chip=True)}</div>
<div class="h1 d">{t['b_h1']}</div>
<div class="eq"><div class="t"><div class="v">{eq[0][0]}</div><div class="l">{eq[0][1]}</div></div><div class="op">&times;</div>
<div class="t"><div class="v">{eq[1][0]}</div><div class="l">{eq[1][1]}</div></div><div class="op">=</div>
<div class="t hl"><div class="v">{eq[2][0]}</div><div class="l">{eq[2][1]}</div></div></div>
<div class="sub">{t['b_sub']}</div>
<div class="cta">{qr_block(lang, MSG[lang], 128, 14)}{call(26)}</div>""")
    return dict(front=front, back=back)


def side(lang, t):
    words = "".join(f"<div>{w}</div>" for w in t["s_words"])
    return dict(bg="#0C1632", note=False, css=f".stage {{ {RAIN} }}" + """
.lk { position:absolute; left:24px; top:18px; }
.u { position:absolute; right:22px; top:14px; width:62px; height:62px; }
.words { position:absolute; left:24px; right:24px; top:68px; color:#fff; font-family:var(--sans); font-weight:800;
  font-size:36px; line-height:1.12; }
body.hi .words { font-size:34px; line-height:1.2; }
.words div:nth-child(2) { color:var(--orange); }
.cap { position:absolute; left:24px; right:24px; top:198px; color:rgba(255,255,255,.88); font-size:20px; }
""", html=f"""
<div class="lk">{lockup(22, chip=True)}</div>
<div class="u">{umb('#E8511A', '#fff')}</div>
<div class="words">{words}</div><div class="cap d">{t['s_cap']}</div>
{side_cta(lang, MSG[lang], color="#fff")}""")
