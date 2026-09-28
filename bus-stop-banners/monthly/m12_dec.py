"""December: year-end. Annual health check-up done? Book your annual wealth check-up (free portfolio review)."""
from framework import call, logo, qr_block

KEY = "12-dec"
MSG = {"en": "Hi MoneyHoney! I saw your bus stop ad. I want a free portfolio review.",
       "hi": "Namaste MoneyHoney! Maine bus stop par aapka ad dekha. Mujhe free portfolio review chahiye."}
NOTE = {"en": "*Free, no-obligation portfolio review. Recommendations depend on your goals and risk profile.",
        "hi": "*मुफ़्त, बिना किसी बाध्यता के पोर्टफोलियो रिव्यू। सुझाव आपके लक्ष्यों और जोखिम प्रोफ़ाइल पर निर्भर करते हैं।"}
T = {
    "en": dict(
        f_a="Annual health check-up?", f_a2="Done.", f_b="Annual wealth check-up?", f_b2="Book it free.*",
        l_title="Health report", l_rows=["BP", "Sugar", "Cholesterol"],
        r_big="Portfolio", r_cap="When was its last check-up? Get it checked, free.*",
        b_h1='Your free <span class="o">wealth check-up</span> covers:',
        items=[("Goals", "Are your goals on track?"), ("Asset mix", "Right mix for your age and risk?"),
               ("Overlaps &amp; costs", "Paying twice for the same thing?"), ("Tax", "Are you saving all you can?")]),
    "hi": dict(
        f_a="सालाना हेल्थ चेक-अप?", f_a2="हो गया।", f_b="सालाना वेल्थ चेक-अप?", f_b2="मुफ़्त में बुक करें।*",
        l_title="हेल्थ रिपोर्ट", l_rows=["BP", "शुगर", "कोलेस्ट्रॉल"],
        r_big="पोर्टफोलियो", r_cap="इसका आख़िरी चेक-अप कब हुआ था? मुफ़्त जाँच करवाएँ।*",
        b_h1='आपके मुफ़्त <span class="o">वेल्थ चेक-अप</span> में:',
        items=[("लक्ष्य", "क्या लक्ष्य सही रास्ते पर हैं?"), ("एसेट मिक्स", "उम्र और जोखिम के हिसाब से सही?"),
               ("ओवरलैप और खर्च", "एक ही चीज़ के लिए दो बार पैसा?"), ("टैक्स", "क्या पूरी बचत हो रही है?")]),
}


def ecg(w, h, color_a="#1B2666", color_b="#E8511A", split=.55):
    mid = h * .6
    pts, x = [], 0
    beat = [(0, 0), (10, 0), (16, -18), (22, 30), (30, -70), (38, 40), (44, 0), (70, 0)]
    xa = w * split
    while x + 70 <= xa:
        pts += [(x + dx, mid + dy) for dx, dy in beat]
        x += 70
    a = " ".join(f"{px:.0f},{py:.0f}" for px, py in pts)
    b = f"{x:.0f},{mid:.0f} {x + (w - x) * .35:.0f},{mid - 30:.0f} {x + (w - x) * .55:.0f},{mid - 12:.0f} {w - 6:.0f},{h * .08:.0f}"
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><polyline points="{a}" fill="none" stroke="{color_a}" '
            f'stroke-width="5" stroke-linejoin="round"/><polyline points="{b}" fill="none" stroke="{color_b}" stroke-width="7" '
            f'stroke-linejoin="round" stroke-linecap="round"/><path d="M{w - 30} {h * .08 - 2:.0f}h24v24" fill="none" '
            f'stroke="{color_b}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def panels(lang, t):
    front = dict(bg="#fff", legal="navy", note=True, css="""
.line { position:absolute; left:40px; right:40px; bottom:22px; opacity:.95; }
.a { position:absolute; left:60px; top:36px; font-size:34px; font-weight:800; color:var(--muted); font-family:var(--sans); }
.a b { color:#1F9D55; }
.b { position:absolute; left:60px; top:84px; font-size:58px; }
.b span { color:var(--orange); }
.row { position:absolute; right:60px; top:36px; display:flex; flex-direction:column; align-items:flex-end; gap:12px; }
""", html=f"""
<div class="line">{ecg(1420, 170)}</div>
<div class="a">{t['f_a']} <b>{t['f_a2']} &#10003;</b></div>
<div class="b d">{t['f_b']} <span>{t['f_b2']}</span></div>
<div class="row">{call(44)}{logo(34)}</div>""")

    rows = "".join(f'<div class="r"><span>{r}</span><b>&#10003;</b></div>' for r in t["l_rows"])
    left = dict(bg="var(--cream)", legal="navy", note=False, css="""
.card { position:absolute; left:28px; right:28px; top:28px; background:#fff; border-radius:12px; padding:14px 20px;
  box-shadow:0 6px 18px rgba(27,38,102,.1); border-top:8px solid var(--navy); }
.card .tt { font-size:18px; font-weight:800; color:var(--muted); text-transform:uppercase; letter-spacing:.1em; }
.r { display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid #EEF0F6; padding:9px 0; font-size:30px; font-weight:800; }
.r:last-child { border:0; } .r b { color:#1F9D55; font-size:34px; }
.bot { position:absolute; left:30px; bottom:14px; } .lg { position:absolute; right:24px; bottom:16px; }
""", html=f"""
<div class="card"><div class="tt">{t['l_title']}</div>{rows}</div>
<div class="bot">{call(26)}</div><div class="lg">{logo(20)}</div>""")

    right = dict(bg="var(--navy)", legal="dark", note=True, css="""
.big { position:absolute; left:28px; top:60px; color:#fff; font-family:var(--sans); font-weight:800; font-size:52px; line-height:1.1; }
.qm { position:absolute; right:28px; top:24px; color:var(--orange); font-family:'Lora'; font-weight:700; font-size:100px; line-height:1; }
.cap { position:absolute; left:30px; right:26px; top:146px; color:var(--orange); font-size:24px; }
.line { position:absolute; left:0; right:0; top:236px; opacity:.9; }
.bot { position:absolute; left:30px; bottom:14px; color:#fff; } .lg { position:absolute; left:28px; top:24px; }
""", html=f"""
<div class="lg">{logo(20, chip=True)}</div><div class="qm">?</div>
<div class="big">{t['r_big']}</div><div class="cap d">{t['r_cap']}</div>
<div class="line">{ecg(400, 70, 'rgba(255,255,255,.5)', '#E8511A', .5)}</div>
<div class="bot">{call(28)}</div>""")

    items = "".join(f'<div class="it"><div class="ck">&#10003;</div><div><div class="a">{a}</div><div class="b">{b}</div></div></div>'
                    for a, b in t["items"])
    back = dict(bg="#fff", legal="navy", note=True, css="""
.lg { position:absolute; left:44px; top:26px; }
.h1 { position:absolute; left:44px; right:320px; top:88px; font-size:38px; }
.items { position:absolute; left:44px; right:320px; top:160px; display:grid; grid-template-columns:1fr 1fr; gap:12px 18px; }
.it { display:flex; gap:12px; align-items:flex-start; background:var(--cream); border-radius:12px; padding:12px 14px; }
.ck { width:34px; height:34px; flex:none; border-radius:50%; background:var(--orange); color:#fff; font-weight:800; font-size:20px;
  display:flex; align-items:center; justify-content:center; }
.it .a { font-weight:800; font-size:19px; } .it .b { font-size:14px; color:var(--muted); margin-top:2px; }
.cta { position:absolute; right:0; top:0; bottom:0; width:280px; background:var(--navy); color:#fff; display:flex;
  flex-direction:column; align-items:center; justify-content:center; gap:14px; }
""", html=f"""
<div class="lg">{logo(42)}</div>
<div class="h1 d">{t['b_h1']}</div>
<div class="items">{items}</div>
<div class="cta">{qr_block(lang, MSG[lang], 128, 14, label_color="#fff")}{call(26)}</div>""")
    return dict(front=front, left=left, right=right, back=back)
