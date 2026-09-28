"""March: the tax-saving deadline, told with a tear-off calendar (ELSS last call)."""
from framework import call, logo, qr_block

KEY = "03-mar"
MSG = {"en": "Hi MoneyHoney! I saw your bus stop ad. I want to save tax before 31 March.",
       "hi": "Namaste MoneyHoney! Maine bus stop par aapka ad dekha. Mujhe 31 March se pehle tax bachana hai."}
NOTE = {"en": "*Under the old tax regime, 30% slab plus 4% cess, on &#8377;1.5 lakh invested in ELSS. Tax benefits "
              "as per current laws, subject to change. ELSS is subject to market risk.",
        "hi": "*पुरानी टैक्स व्यवस्था में 30% स्लैब + 4% सेस, ELSS में &#8377;1.5 लाख निवेश पर। टैक्स लाभ मौजूदा "
              "कानूनों के अनुसार, बदल सकते हैं। ELSS में बाज़ार जोखिम है।"}
T = {
    "en": dict(
        mon="MARCH", f_h1="The last date to save tax this year.",
        f_h2="Invest in ELSS before 31 March. Save up to &#8377;46,800*.",
        l_big="Tick.<br>Tock.", l_sub="Tax-saving time is running out.",
        r_h="After 31 March, this year&rsquo;s tax saving is gone.",
        b_h1='3 steps. 1 call. <span class="o">Done before 31 March.</span>',
        steps=[("Call or scan", "Talk to us today"), ("Quick KYC", "If not already done"),
               ("Invest in ELSS", "Save up to &#8377;46,800*")]),
    "hi": dict(
        mon="मार्च", f_h1="इस साल टैक्स बचाने की आख़िरी तारीख़।",
        f_h2="31 मार्च से पहले ELSS में निवेश करें। &#8377;46,800* तक बचाएँ।",
        l_big="टिक।<br>टिक।", l_sub="टैक्स बचाने का समय ख़त्म हो रहा है।",
        r_h="31 मार्च के बाद इस साल की टैक्स बचत का मौका ख़त्म।",
        b_h1='3 कदम। 1 कॉल। <span class="o">31 मार्च से पहले काम पूरा।</span>',
        steps=[("कॉल या स्कैन", "आज ही बात करें"), ("आसान KYC", "अगर पहले नहीं हुआ"),
               ("ELSS में निवेश", "&#8377;46,800* तक बचत")]),
}


def calendar(w, mon, day_px, band_px, rot=-4):
    return (f'<div class="cal" style="width:{w}px;transform:rotate({rot}deg)"><div class="band" style="font-size:{band_px}px">'
            f'<i></i><i></i>{mon}</div><div class="day" style="font-size:{day_px}px">31</div></div>')


CAL = """
.cal { background:#fff; border-radius:14px; overflow:hidden; box-shadow:0 16px 40px rgba(12,22,50,.3); text-align:center; }
.cal .band { background:var(--navy); color:#fff; font-family:'DM Sans'; font-weight:800; letter-spacing:.2em; padding:.55em 0 .45em;
  position:relative; }
body.hi .cal .band { font-family:'Mukta'; letter-spacing:.05em; }
.cal .band i { position:absolute; top:-.3em; width:.5em; height:1em; border-radius:.3em; background:#C9CFE0; }
.cal .band i:first-child { left:25%; } .cal .band i:nth-child(2) { right:25%; }
.cal .day { font-family:'Lora', serif; font-weight:700; color:var(--navy); line-height:1.05; padding-bottom:.05em; }
"""


def panels(lang, t):
    front = dict(bg="var(--orange)", legal="dark", note=True, css=CAL + """
.calw { position:absolute; left:70px; top:34px; }
.torn { position:absolute; left:290px; top:60px; width:170px; height:220px; background:rgba(255,255,255,.28); border-radius:14px; transform:rotate(9deg); }
.copy { position:absolute; left:520px; right:60px; top:48px; }
.copy .a { font-size:50px; color:#fff; font-family:var(--sans); font-weight:800; line-height:var(--lt); }
.copy .b { font-size:27px; color:var(--navy); font-weight:700; margin-top:14px; }
.row { position:absolute; left:520px; right:60px; bottom:28px; display:flex; align-items:center; justify-content:space-between; }
.pill { background:var(--navy); color:#fff; border-radius:60px; padding:12px 26px; }
""", html=f"""
<div class="torn"></div>
<div class="calw">{calendar(250, t['mon'], 150, 26)}</div>
<div class="copy"><div class="a">{t['f_h1']}</div><div class="b">{t['f_h2']}</div></div>
<div class="row">{logo(36, chip=True)}<div class="pill">{call(40)}</div></div>""")

    left = dict(bg="#fff", legal="dark", note=False, css="""
.col { position:absolute; left:28px; right:26px; top:28px; }
.big { font-size:92px; color:var(--navy); font-family:var(--sans); font-weight:800; line-height:.95; }
body.hi .big { font-size:84px; line-height:1.12; }
.bar { width:90px; height:8px; background:var(--orange); margin:18px 0 14px; }
.sub { font-size:22px; font-weight:700; color:var(--orange); }
.bot { position:absolute; left:30px; right:26px; bottom:14px; display:flex; justify-content:space-between; align-items:center; }
""", html=f"""
<div class="col"><div class="big">{t['l_big']}</div><div class="bar"></div><div class="sub">{t['l_sub']}</div></div>
<div class="bot">{call(26)}{logo(22)}</div>""")

    right = dict(bg="var(--navy)", legal="dark", note=False, css=CAL + """
.calw { position:absolute; left:34px; top:28px; }
.rh { position:absolute; left:30px; right:26px; top:196px; color:#fff; font-size:27px; }
.bot { position:absolute; left:30px; bottom:14px; color:#fff; }
.lg { position:absolute; right:24px; top:34px; }
""", html=f"""
<div class="calw">{calendar(130, t['mon'], 74, 15, rot=-6)}</div><div class="lg">{logo(24, chip=True)}</div>
<div class="rh d">{t['r_h']}</div>
<div class="bot">{call(28)}</div>""")

    steps = "".join(f'<div class="st"><div class="nm d">{i + 1}</div><div><div class="a">{a}</div><div class="b">{b}</div></div></div>'
                    + ('<div class="ar">&rarr;</div>' if i < 2 else "") for i, (a, b) in enumerate(t["steps"]))
    back = dict(bg="var(--cream)", legal="dark", note=True, css=CAL + """
.lg { position:absolute; left:44px; top:26px; }
.calw { position:absolute; left:760px; top:20px; }
.h1 { position:absolute; left:44px; right:420px; top:112px; font-size:40px; }
.steps { position:absolute; left:44px; right:330px; bottom:30px; display:flex; align-items:center; gap:10px; }
.st { flex:1; display:flex; gap:12px; align-items:center; background:#fff; border-radius:12px; padding:12px 14px;
  box-shadow:0 2px 10px rgba(27,38,102,.07); }
.st .nm { width:44px; height:44px; flex:none; border-radius:50%; background:var(--orange); color:#fff; font-size:26px;
  display:flex; align-items:center; justify-content:center; line-height:1; }
.st .a { font-weight:800; font-size:18px; } .st .b { font-size:13.5px; color:var(--muted); margin-top:2px; }
.ar { color:var(--orange); font-size:26px; font-weight:800; }
.cta { position:absolute; right:0; top:0; bottom:0; width:290px; background:var(--orange); color:#fff;
  display:flex; align-items:center; justify-content:center; flex-direction:column; gap:16px; }
.cta .call .ico { color:#fff; }
""", html=f"""
<div class="lg">{logo(44)}</div>
<div class="calw">{calendar(120, t['mon'], 66, 13, rot=5)}</div>
<div class="h1 d">{t['b_h1']}</div>
<div class="steps">{steps}</div>
<div class="cta">{qr_block(lang, MSG[lang], 128, 14, label_color="#fff")}{call(26)}</div>""")
    return dict(front=front, left=left, right=right, back=back)
