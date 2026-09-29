"""May: FD maturing? Don't renew on autopilot (fixed income options)."""
from framework import call, lockup, logo, qr_block, side_cta

KEY = "05-may"
MSG = {"en": 'Hi! Bus stop ad: My FD is maturing.',
       "hi": 'Hi! Bus stop ad: Meri FD mature ho rahi hai.'}
NOTE = ("*Returns, safety and tax treatment differ across products. Debt funds and debentures carry risk; "
              "read all offer documents carefully.")
SIDE_NOTE = 'Returns, safety and tax treatment differ across products. Debt funds and debentures carry risk.'

T = {
    "en": dict(
        toggle="Auto-renew FD", f_h1="FD maturing?", f_h2="Don&rsquo;t renew on autopilot.",
        f_sub="Compare FDs, bonds, debentures and more before you decide.*",
        s_big="5 options.<br>1 call.", s_list="FDs &bull; Debentures &bull; Gov. Bonds &bull; 54EC Bonds &bull; Debt Funds",
        b_h1='Before you renew, <span class="o">meet the other options.</span>',
        cards=[("FDs", "Fixed interest, tenure of your choice"), ("Debentures", "Fixed coupons from rated companies"),
               ("Gov. Bonds", "Backed by the Government of India"), ("54EC Bonds", "Save tax on property gains"),
               ("Debt Funds", "Flexible, market-linked")]),
    "hi": dict(
        toggle="FD ऑटो-रिन्यू", f_h1="FD मैच्योर हो रही है?", f_h2="बिना सोचे रिन्यू न करें।",
        f_sub="फ़ैसले से पहले FD, बॉन्ड, डिबेंचर और बाकी विकल्पों की तुलना करें।*",
        s_big="5 विकल्प।<br>1 कॉल।", s_list="FDs &bull; Debentures &bull; Gov. Bonds &bull; 54EC Bonds &bull; Debt Funds",
        b_h1='रिन्यू करने से पहले, <span class="o">बाकी विकल्प भी जानिए।</span>',
        cards=[("FDs", "तय ब्याज, अपनी पसंद की अवधि"), ("Debentures", "रेटेड कंपनियों से तय कूपन"),
               ("Gov. Bonds", "भारत सरकार द्वारा समर्थित"), ("54EC Bonds", "प्रॉपर्टी के मुनाफ़े पर टैक्स बचत"),
               ("Debt Funds", "लचीले, बाज़ार से जुड़े")]),
}

TOGGLE = """
.tg { position:relative; border-radius:999px; background:var(--orange); box-shadow:inset 0 -4px 0 rgba(0,0,0,.12); }
.tg .knob { position:absolute; top:8%; right:4%; height:84%; aspect-ratio:1; border-radius:50%; background:#fff;
  box-shadow:0 6px 16px rgba(0,0,0,.25); }
.tg .on { position:absolute; left:12%; top:50%; transform:translateY(-50%); color:#fff; font-family:'DM Sans'; font-weight:800; }
.hand { position:absolute; width:36%; height:0; border-top:6px dashed var(--navy); }
"""


def toggle(w, h, on_px):
    return (f'<div class="tg" style="width:{w}px;height:{h}px"><span class="on" style="font-size:{on_px}px">ON</span>'
            f'<div class="knob"></div></div>')


def panels(lang, t):
    front = dict(bg="var(--cream)", legal="navy", note=True, css=TOGGLE + """
.tw { position:absolute; left:70px; top:80px; }
.tlbl { position:absolute; left:74px; top:38px; font-size:28px; font-weight:800; color:var(--navy); }
.pause { position:absolute; left:420px; top:96px; width:92px; height:92px; border-radius:50%; background:var(--navy);
  display:flex; align-items:center; justify-content:center; gap:12px; box-shadow:0 8px 20px rgba(27,38,102,.3); }
.pause i { width:12px; height:40px; background:#fff; border-radius:3px; }
.copy { position:absolute; left:660px; right:60px; top:44px; }
.copy .a { font-size:40px; font-weight:800; color:var(--muted); line-height:var(--lt); }
.copy .b { font-size:58px; margin-top:2px; }
.copy .c { font-size:22px; font-weight:600; margin-top:12px; }
.row { position:absolute; left:660px; right:60px; bottom:24px; display:flex; justify-content:space-between; align-items:center; }
.chips { position:absolute; left:70px; bottom:22px; display:flex; gap:8px; flex-wrap:nowrap; width:560px; }
.chips span { border:2px solid var(--navy); border-radius:30px; padding:3px 10px; font-size:14px; font-weight:700; white-space:nowrap; }
""", html=f"""
<div class="tlbl">{t['toggle']}</div>
<div class="tw">{toggle(330, 124, 40)}</div>
<div class="pause"><i></i><i></i></div>
<div class="chips">{''.join(f'<span>{c[0]}</span>' for c in t['cards'])}</div>
<div class="copy"><div class="a">{t['f_h1']}</div><div class="b d">{t['f_h2']}</div><div class="c">{t['f_sub']}</div></div>
<div class="row">{logo(42)}{call(44)}</div>""")

    cards = "".join(f'<div class="cd"><div class="nm">{a}</div><div class="ds">{b}</div></div>' for a, b in t["cards"])
    back = dict(bg="#fff", legal="navy", note=True, css="""
.lg { position:absolute; left:44px; top:26px; }
.h1 { position:absolute; left:44px; right:320px; top:92px; font-size:38px; }
.cards { position:absolute; left:44px; right:320px; bottom:28px; display:grid; grid-template-columns:repeat(5,1fr); gap:10px; }
.cd { background:var(--cream); border-radius:12px; padding:14px 12px; border-top:5px solid var(--navy); min-height:118px; }
.cd:nth-child(odd) { border-top-color:var(--orange); }
.cd .nm { font-weight:800; font-size:19px; } .cd .ds { font-size:14px; color:var(--muted); margin-top:6px; line-height:1.3; }
.cta { position:absolute; right:0; top:0; bottom:0; width:280px; background:var(--cream); border-left:6px solid var(--orange);
  display:flex; flex-direction:column; align-items:center; justify-content:center; gap:14px; }
""", html=f"""
<div class="lg">{lockup(40)}</div>
<div class="h1 d">{t['b_h1']}</div>
<div class="cards">{cards}</div>
<div class="cta">{qr_block(lang, MSG[lang], 128, 14)}{call(26)}</div>""")
    return dict(front=front, back=back)


def side(lang, t):
    return dict(bg="var(--orange)", note=True, css=TOGGLE + """
.lk { position:absolute; left:24px; top:18px; }
.tw { position:absolute; right:24px; top:18px; }
.big { position:absolute; left:24px; right:24px; top:64px; color:#fff; font-family:var(--sans); font-weight:800;
  font-size:46px; line-height:1.02; }
body.hi .big { line-height:1.12; }
.list { position:absolute; left:24px; right:24px; top:168px; color:var(--navy); font-family:'DM Sans', sans-serif;
  font-size:15.5px; font-weight:700; line-height:1.4; text-wrap-style:balance; }
""", html=f"""
<div class="lk">{lockup(22, chip=True)}</div>
<div class="tw">{toggle(92, 40, 15)}</div>
<div class="big">{t['s_big']}</div><div class="list lat">{t['s_list']}</div>
{side_cta(lang, MSG[lang], color="#fff", icon="var(--navy)")}""")
