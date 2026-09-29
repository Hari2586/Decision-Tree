"""March: the tax-saving deadline, told with a tear-off calendar (ELSS last call)."""
from framework import call, lockup, logo, qr_block, side_cta

KEY = "03-mar"
MSG = {"en": 'Hi! Bus stop ad: Save tax before 31 March.',
       "hi": 'Hi! Bus stop ad: 31 March se pehle tax bachana hai.'}
NOTE = ("*Under the old tax regime, 30% slab plus 4% cess, on &#8377;1.5 lakh invested in ELSS. Tax benefits "
              "as per current laws, subject to change. ELSS is subject to market risk.")
SIDE_NOTE = ''

T = {
    "en": dict(
        mon="MARCH", f_h1="The last date to save tax this year.",
        f_h2="Invest in ELSS before 31 March. Save up to &#8377;46,800*.",
        s_big="Tick.<br>Tock.", s_sub="Tax-saving time is running out.",
        b_h1='3 steps. 1 call. <span class="o">Done before 31 March.</span>',
        steps=[("Call or scan", "Talk to us today"), ("Quick KYC", "If not already done"),
               ("Invest in ELSS", "Save up to &#8377;46,800*")]),
    "hi": dict(
        mon="मार्च", f_h1="इस साल टैक्स बचाने की आख़िरी तारीख़।",
        f_h2="31 मार्च से पहले ELSS में निवेश करें। &#8377;46,800* तक बचाएँ।",
        s_big="टिक।<br>टिक।", s_sub="टैक्स बचाने का समय निकल रहा है।",
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
.cal .band i { position:absolute; top:-.3em; width:.5em; height:1em; border-radius:.3em; background:var(--lmuted); }
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
<div class="lg">{lockup(40)}</div>
<div class="calw">{calendar(120, t['mon'], 66, 13, rot=5)}</div>
<div class="h1 d">{t['b_h1']}</div>
<div class="steps">{steps}</div>
<div class="cta">{qr_block(lang, MSG[lang], 128, 14, label_color="#fff")}{call(26)}</div>""")
    return dict(front=front, back=back)


HOURGLASS = ('<svg viewBox="0 0 64 64" width="100%" height="100%"><rect x="12" y="4" width="40" height="6" rx="3" fill="#1B2666"/>'
             '<rect x="12" y="54" width="40" height="6" rx="3" fill="#1B2666"/><path d="M17 10h30c0 12-9 17-12 22 3 5 12 10 '
             '12 22H17c0-12 9-17 12-22-3-5-12-10-12-22z" fill="none" stroke="#1B2666" stroke-width="3" stroke-linejoin="round"/>'
             '<path d="M25 22h14c-1.6 3.6-4.6 5.6-7 8.2-2.4-2.6-5.4-4.6-7-8.2z" fill="#E8511A"/>'
             '<path d="M32 33v12" stroke="#E8511A" stroke-width="2" stroke-dasharray="2 2"/>'
             '<path d="M20 52c2-6.5 7-9 12-9s10 2.5 12 9z" fill="#E8511A"/></svg>')


def side(lang, t):
    return dict(bg="#fff", note=False, css="""
.lk { position:absolute; left:24px; top:18px; }
.hg { position:absolute; right:30px; top:66px; width:100px; height:100px; }
.flow { position:absolute; left:24px; right:24px; top:54px; }
.big { font-family:var(--sans); font-weight:800; font-size:58px; line-height:.98; color:var(--navy); }
body.hi .big { font-size:56px; line-height:1.05; }
.bar { width:84px; height:7px; background:var(--orange); margin:12px 0 10px; }
.sub { font-size:20px; font-weight:700; color:var(--orange); }
""", html=f"""
<div class="lk">{lockup(24)}</div>
<div class="hg">{HOURGLASS}</div>
<div class="flow"><div class="big">{t['s_big']}</div><div class="bar"></div><div class="sub">{t['s_sub']}</div></div>
{side_cta(lang, MSG[lang])}""")
