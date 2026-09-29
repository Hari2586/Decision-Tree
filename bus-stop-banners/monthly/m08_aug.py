"""August: Independence Day. India became independent in 1947. When will you? (retirement)"""
from framework import call, lockup, logo, qr_block, side_cta

KEY = "08-aug"
MSG = {"en": 'Hi! Bus stop ad: Plan my retirement.',
       "hi": 'Hi! Bus stop ad: Retirement planning karni hai.'}
NOTE = ("*Illustration at an assumed 6% p.a. inflation for understanding only. Actual inflation may differ.")
SIDE_NOTE = ''

T = {
    "en": dict(
        f_h1="India got its independence in 1947.", f_h2="When will you get yours?",
        f_sub="Plan your financial freedom: retire on your terms.",
        s_cap='Your financial freedom year.<br><span class="o">Let&rsquo;s fill in the blank.</span>',
        b_h1='Freedom needs <span class="o">a number.</span>',
        b_a="&#8377;50,000", b_al="monthly expenses today", b_b="&#8377;1.6 lakh*", b_bl="needed every month, 20 years later",
        b_sub="Build a corpus that pays you every month, just like a salary."),
    "hi": dict(
        f_h1="भारत 1947 में आज़ाद हुआ।", f_h2="आप कब होंगे?",
        f_sub="अपनी आर्थिक आज़ादी की योजना बनाइए, अपनी शर्तों पर रिटायर होइए।",
        s_cap='आपकी आर्थिक आज़ादी का साल।<br><span class="o">चलिए, खाली जगह भरें।</span>',
        b_h1='आज़ादी का भी <span class="o">एक नंबर होता है।</span>',
        b_a="&#8377;50,000", b_al="आज महीने का खर्च", b_b="&#8377;1.6 लाख*", b_bl="20 साल बाद हर महीने की ज़रूरत",
        b_sub="ऐसा फंड बनाइए जो सैलरी की तरह हर महीने आपको पैसा दे।"),
}

YEAR_CSS = """
.yr { font-family:'Lora', serif; font-weight:700; line-height:.9; letter-spacing:-.02em; }
.blank { color:var(--orange); }
.blank u { text-decoration:none; display:inline-block; border-bottom:.08em solid var(--orange); width:1.05em; height:.7em; margin-left:.04em; }
"""


def panels(lang, t):
    front = dict(bg="#fff", legal="navy", note=False, css=YEAR_CSS + """
.y1 { position:absolute; left:56px; top:22px; font-size:124px; color:var(--navy); }
.y2 { position:absolute; left:56px; top:142px; font-size:124px; }
.copy { position:absolute; left:560px; right:60px; top:48px; }
.copy .a { font-size:40px; color:var(--muted); font-family:var(--sans); font-weight:800; line-height:var(--lt); }
.copy .b { font-size:64px; margin-top:4px; }
.copy .c { font-size:22px; font-weight:600; margin-top:10px; }
.row { position:absolute; left:560px; right:60px; bottom:26px; display:flex; justify-content:space-between; align-items:center; }
.bar { position:absolute; left:500px; top:40px; bottom:30px; width:6px; background:var(--orange); }
""", html=f"""
<div class="y1 yr">1947</div><div class="y2 yr blank">20<u></u></div><div class="bar"></div>
<div class="copy"><div class="a">{t['f_h1']}</div><div class="b d o">{t['f_h2']}</div><div class="c">{t['f_sub']}</div></div>
<div class="row">{logo(42)}{call(44)}</div>""")

    back = dict(bg="var(--cream)", legal="navy", note=True, css=YEAR_CSS + """
.lg { position:absolute; left:44px; top:26px; }
.h1 { position:absolute; left:44px; width:360px; top:96px; font-size:46px; }
.flow { position:absolute; left:440px; right:320px; top:56px; display:flex; flex-direction:column; gap:12px; }
.bx { background:#fff; border-radius:14px; padding:14px 18px; box-shadow:0 2px 10px rgba(27,38,102,.07); }
.bx .v { font-family:var(--display); font-weight:var(--dw); font-size:44px; line-height:1.05; }
.bx .l { font-size:15px; color:var(--muted); font-weight:600; }
.bx.hl { background:var(--navy); } .bx.hl .v { color:var(--orange); } .bx.hl .l { color:rgba(255,255,255,.85); }
.ar { font-size:14px; font-weight:800; color:var(--orange); padding-left:18px; letter-spacing:.06em; }
.sub { position:absolute; left:44px; width:360px; bottom:26px; font-size:16px; font-weight:600; }
.cta { position:absolute; right:0; top:0; bottom:0; width:280px; background:var(--orange); color:#fff; display:flex;
  flex-direction:column; align-items:center; justify-content:center; gap:14px; }
.cta .call .ico { color:#fff; }
""", html=f"""
<div class="lg">{lockup(40)}</div>
<div class="h1 d">{t['b_h1']}</div>
<div class="flow"><div class="bx"><div class="v">{t['b_a']}</div><div class="l">{t['b_al']}</div></div>
<div class="ar">&darr; 6% &times; 20</div>
<div class="bx hl"><div class="v">{t['b_b']}</div><div class="l">{t['b_bl']}</div></div></div>
<div class="sub">{t['b_sub']}</div>
<div class="cta">{qr_block(lang, MSG[lang], 128, 14, label_color="#fff")}{call(26)}</div>""")
    return dict(front=front, back=back)


def side(lang, t):
    return dict(bg="#fff", note=False, css=YEAR_CSS + """
.lk { position:absolute; left:24px; top:18px; }
.yr { position:absolute; left:20px; top:52px; font-size:118px; }
.cap { position:absolute; left:24px; right:30px; top:180px; font-size:24px; color:var(--navy); }
body.hi .cap { font-size:23px; }
""", html=f"""
<div class="lk">{lockup(24)}</div>
<div class="yr blank">20<u></u></div>
<div class="cap d">{t['s_cap']}</div>
{side_cta(lang, MSG[lang])}""")
