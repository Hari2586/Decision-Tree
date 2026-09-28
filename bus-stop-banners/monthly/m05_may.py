"""May: FD maturing? Don't renew on autopilot (fixed income options)."""
from framework import call, logo, qr_block

KEY = "05-may"
MSG = {"en": "Hi MoneyHoney! I saw your bus stop ad. My FD is maturing, please help me compare options.",
       "hi": "Namaste MoneyHoney! Maine bus stop par aapka ad dekha. Meri FD mature ho rahi hai, options samjhaiye."}
NOTE = {"en": "*Returns, safety and tax treatment differ across products. Debt funds and debentures carry risk; "
              "read all offer documents carefully.",
        "hi": "*अलग-अलग उत्पादों में रिटर्न, सुरक्षा और टैक्स अलग होते हैं। डेट फंड और डिबेंचर में जोखिम है; "
              "सभी दस्तावेज़ ध्यान से पढ़ें।"}
T = {
    "en": dict(
        toggle="Auto-renew FD", f_h1="FD maturing?", f_h2="Don&rsquo;t renew on autopilot.",
        f_sub="Compare FDs, bonds, debentures and more, in one call.*",
        l_q="Auto-renew?", l_cap="Wait. Compare first.",
        r_big="5 options.<br>1 call.", r_list="FDs &bull; Debentures &bull; Gov. Bonds &bull; 54EC Bonds &bull; Debt Funds",
        b_h1='Before you renew, <span class="o">meet the other options.</span>',
        cards=[("FDs", "Fixed interest, tenure of your choice"), ("Debentures", "Fixed coupons from rated companies"),
               ("Gov. Bonds", "Backed by the Government of India"), ("54EC Bonds", "Save tax on property gains"),
               ("Debt Funds", "Flexible, market-linked")]),
    "hi": dict(
        toggle="FD ऑटो-रिन्यू", f_h1="FD मैच्योर हो रही है?", f_h2="बिना सोचे रिन्यू न करें।",
        f_sub="FD, बॉन्ड, डिबेंचर और बाकी विकल्प, एक ही कॉल में तुलना करें।*",
        l_q="ऑटो-रिन्यू?", l_cap="रुकिए। पहले तुलना करें।",
        r_big="5 विकल्प।<br>1 कॉल।", r_list="FD &bull; डिबेंचर &bull; सरकारी बॉन्ड &bull; 54EC बॉन्ड &bull; डेट फंड",
        b_h1='रिन्यू करने से पहले, <span class="o">बाकी विकल्प भी जानिए।</span>',
        cards=[("FD", "तय ब्याज, अपनी पसंद की अवधि"), ("डिबेंचर", "रेटेड कंपनियों से तय कूपन"),
               ("सरकारी बॉन्ड", "भारत सरकार द्वारा समर्थित"), ("54EC बॉन्ड", "प्रॉपर्टी के मुनाफ़े पर टैक्स बचत"),
               ("डेट फंड", "लचीले, बाज़ार से जुड़े")]),
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
.tw { position:absolute; left:70px; top:92px; }
.tlbl { position:absolute; left:74px; top:38px; font-size:28px; font-weight:800; color:var(--navy); }
.pause { position:absolute; left:470px; top:74px; width:92px; height:92px; border-radius:50%; background:var(--navy);
  display:flex; align-items:center; justify-content:center; gap:12px; box-shadow:0 8px 20px rgba(27,38,102,.3); }
.pause i { width:12px; height:40px; background:#fff; border-radius:3px; }
.copy { position:absolute; left:660px; right:60px; top:44px; }
.copy .a { font-size:40px; font-weight:800; color:var(--muted); line-height:var(--lt); }
.copy .b { font-size:58px; margin-top:2px; }
.copy .c { font-size:22px; font-weight:600; margin-top:12px; }
.row { position:absolute; left:660px; right:60px; bottom:24px; display:flex; justify-content:space-between; align-items:center; }
.chips { position:absolute; left:70px; bottom:34px; display:flex; gap:8px; flex-wrap:wrap; width:540px; }
.chips span { border:2px solid var(--navy); border-radius:30px; padding:4px 12px; font-size:16px; font-weight:700; }
""", html=f"""
<div class="tlbl">{t['toggle']}</div>
<div class="tw">{toggle(380, 150, 44)}</div>
<div class="pause"><i></i><i></i></div>
<div class="chips">{''.join(f'<span>{c[0]}</span>' for c in t['cards'])}</div>
<div class="copy"><div class="a">{t['f_h1']}</div><div class="b d">{t['f_h2']}</div><div class="c">{t['f_sub']}</div></div>
<div class="row">{logo(42)}{call(44)}</div>""")

    left = dict(bg="var(--navy)", legal="dark", note=False, css=TOGGLE + """
.q { position:absolute; left:30px; top:44px; color:#fff; font-size:48px; font-family:var(--sans); font-weight:800; line-height:var(--lt); }
.tw { position:absolute; left:30px; top:130px; }
.cap { position:absolute; left:30px; right:26px; top:250px; color:var(--orange); font-size:30px; }
.bot { position:absolute; left:30px; bottom:14px; color:#fff; }
.lg { position:absolute; right:24px; bottom:14px; }
""", html=f"""
<div class="q">{t['l_q']}</div><div class="tw">{toggle(210, 84, 26)}</div>
<div class="cap d">{t['l_cap']}</div><div class="bot">{call(26)}</div><div class="lg">{logo(20, chip=True)}</div>""")

    right = dict(bg="var(--orange)", legal="dark", note=True, css="""
.big { position:absolute; left:28px; top:40px; color:#fff; font-size:66px; font-family:var(--sans); font-weight:800; line-height:var(--lt); }
.list { position:absolute; left:30px; right:26px; top:216px; color:var(--navy); font-size:17px; font-weight:700; line-height:1.45; }
.bot { position:absolute; left:30px; bottom:14px; color:var(--navy); }
.bot .call .ico { color:var(--navy); }
.lg { position:absolute; right:24px; bottom:14px; }
""", html=f"""
<div class="lg">{logo(20, chip=True)}</div>
<div class="big">{t['r_big']}</div><div class="list">{t['r_list']}</div><div class="bot">{call(28)}</div>""")

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
<div class="lg">{logo(42)}</div>
<div class="h1 d">{t['b_h1']}</div>
<div class="cards">{cards}</div>
<div class="cta">{qr_block(lang, MSG[lang], 128, 14)}{call(26)}</div>""")
    return dict(front=front, left=left, right=right, back=back)
