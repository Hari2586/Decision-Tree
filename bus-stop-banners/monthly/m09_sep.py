"""September: sold a property? The tax-saving clock has started (Capital Gain Bonds)."""
from framework import call, lockup, logo, qr_block, side_cta

KEY = "09-sep"
MSG = {"en": 'Hi! Bus stop ad: I sold a property. Capital Gain Bonds?',
       "hi": 'Hi! Bus stop ad: Property bechi hai, Capital Gain Bonds?'}
NOTE = ("*Capital Gain Bonds: exemption on long-term capital gains from land or building, investment up to &#8377;50 lakh "
              "per financial year within 6 months of transfer, 5-year lock-in. Tax benefits as per current laws, subject to change.")
SIDE_NOTE = ''

T = {
    "en": dict(
        sold="SOLD", f_h1="Sold a property?", f_h2="The tax-saving clock has started.",
        f_sub="Invest in Capital Gain Bonds within 6 months of the sale.*",
        s_big="Congrats on the sale!", s_cap="Now let&rsquo;s protect the profit.", s_ask="Ask us about Capital Gain Bonds.",
        b_h1='Your profit worked hard. <span class="o">Don&rsquo;t hand it to tax.</span>',
        months=["Sale", "M1", "M2", "M3", "M4", "M5", "M6"], end="Capital Gain Bonds",
        facts=["Up to &#8377;50 lakh a financial year", "5-year lock-in", "Issued by government-owned companies"]),
    "hi": dict(
        sold="बिक गया", f_h1="प्रॉपर्टी बेची?", f_h2="टैक्स बचाने की घड़ी चल रही है।",
        f_sub="बिक्री के 6 महीने के अंदर कैपिटल गेन बॉन्ड में निवेश करें।*",
        s_big="बिक्री की बधाई!", s_cap="अब मुनाफ़े को बचाने की बारी।", s_ask="कैपिटल गेन बॉन्ड के बारे में पूछिए।",
        b_h1='मेहनत का मुनाफ़ा, <span class="o">टैक्स में क्यों जाए?</span>',
        months=["बिक्री", "M1", "M2", "M3", "M4", "M5", "M6"], end="कैपिटल गेन बॉन्ड",
        facts=["प्रति वित्त वर्ष &#8377;50 लाख तक", "5 साल का लॉक-इन", "सरकारी कंपनियों द्वारा जारी"]),
}

HOUSE = ('<svg viewBox="0 0 100 100" width="100%" height="100%"><path d="M50 8 6 46h12v44h64V46h12z" fill="{c1}"/>'
         '<rect x="40" y="62" width="20" height="28" rx="2" fill="{c2}"/><rect x="24" y="52" width="14" height="14" rx="2" fill="{c2}"/>'
         '<rect x="62" y="52" width="14" height="14" rx="2" fill="{c2}"/></svg>')


def clock(size, pct_css):
    return (f'<div class="clk" style="width:{size}px;height:{size}px;background:conic-gradient(var(--orange) 0 {pct_css}, '
            f'rgba(255,255,255,.15) {pct_css} 100%)"><div class="in"></div><i class="hd1"></i><i class="hd2"></i></div>')


CLOCK = """
.clk { position:relative; border-radius:50%; }
.clk .in { position:absolute; inset:14%; border-radius:50%; background:var(--navy); }
.clk .hd1, .clk .hd2 { position:absolute; left:50%; bottom:50%; width:6%; margin-left:-3%; background:#fff; border-radius:4px; transform-origin:bottom center; }
.clk .hd1 { height:30%; transform:rotate(0deg); } .clk .hd2 { height:22%; transform:rotate(120deg); }
.clk::before { content:''; position:absolute; left:50%; top:-10%; width:18%; height:12%; margin-left:-9%; background:var(--navy); border-radius:4px; }
.tag { position:absolute; background:var(--orange); color:#fff; font-weight:800; border-radius:6px; transform:rotate(-8deg);
  box-shadow:0 6px 14px rgba(0,0,0,.2); font-family:var(--sans); }
"""


def house(c1, c2):
    return HOUSE.replace("{c1}", c1).replace("{c2}", c2)


def panels(lang, t):
    front = dict(bg="var(--cream)", legal="navy", note=True, css=CLOCK + """
.hs { position:absolute; left:60px; top:60px; width:230px; height:230px; }
.tag { left:200px; top:70px; font-size:30px; padding:6px 16px; }
.ck { position:absolute; left:330px; top:90px; }
.copy { position:absolute; left:620px; right:60px; top:44px; }
.copy .a { font-size:40px; font-weight:800; color:var(--muted); font-family:var(--sans); line-height:var(--lt); }
.copy .b { font-size:48px; margin-top:4px; } .copy .c { font-size:22px; font-weight:600; margin-top:12px; }
.row { position:absolute; left:620px; right:60px; bottom:26px; display:flex; justify-content:space-between; align-items:center; }
""", html=f"""
<div class="hs">{house('#16205B', '#F4EFE9')}</div><div class="tag">{t['sold']}</div>
<div class="ck">{clock(200, '50%')}</div>
<div class="copy"><div class="a">{t['f_h1']}</div><div class="b d">{t['f_h2']}</div><div class="c">{t['f_sub']}</div></div>
<div class="row">{logo(42)}{call(44)}</div>""")

    months = "".join(f'<div class="mo{" s" if i == 0 else ""}">{m}</div>' for i, m in enumerate(t["months"]))
    facts = "".join(f"<li>{f}</li>" for f in t["facts"])
    back = dict(bg="#fff", legal="navy", note=True, css="""
.lg { position:absolute; left:44px; top:26px; }
.h1 { position:absolute; left:44px; right:320px; top:88px; font-size:36px; }
.tl { position:absolute; left:44px; right:320px; top:176px; display:flex; align-items:center; gap:6px; }
.mo { flex:1; text-align:center; background:var(--cream); border-radius:8px; padding:10px 0; font-weight:800; font-size:16px; color:var(--navy); }
.mo.s { background:var(--navy); color:#fff; }
.end { flex:1.6; text-align:center; background:var(--orange); color:#fff; border-radius:8px; padding:10px 0; font-weight:800; font-size:16px; }
.facts { position:absolute; left:44px; right:320px; bottom:24px; display:flex; gap:12px; list-style:none; }
.facts li { flex:1; border-left:5px solid var(--orange); padding:4px 10px; font-size:15px; font-weight:700; }
.cta { position:absolute; right:0; top:0; bottom:0; width:280px; background:var(--navy); color:#fff; display:flex;
  flex-direction:column; align-items:center; justify-content:center; gap:14px; }
""", html=f"""
<div class="lg">{lockup(40)}</div>
<div class="h1 d">{t['b_h1']}</div>
<div class="tl">{months}<div class="end">&rarr; {t['end']}</div></div>
<ul class="facts">{facts}</ul>
<div class="cta">{qr_block(lang, MSG[lang], 128, 14, label_color="#fff")}{call(26)}</div>""")
    return dict(front=front, back=back)


def side(lang, t):
    return dict(bg="var(--cream)", note=False, css=CLOCK + """
.lk { position:absolute; left:24px; top:18px; }
.hs { position:absolute; right:24px; top:60px; width:100px; height:100px; }
.tag { right:88px; top:58px; font-size:17px; padding:3px 10px; }
.big { position:absolute; left:24px; right:150px; top:66px; font-size:34px; }
.cap { position:absolute; left:24px; right:24px; top:168px; font-size:23px; color:var(--orange); }
.ask { position:absolute; left:24px; right:24px; top:204px; font-size:16px; font-weight:700; color:var(--navy); }
""", html=f"""
<div class="lk">{lockup(24)}</div>
<div class="hs">{house('#16205B', '#F4EFE9')}</div><div class="tag">{t['sold']}</div>
<div class="big d">{t['s_big']}</div><div class="cap d">{t['s_cap']}</div><div class="ask">{t['s_ask']}</div>
{side_cta(lang, MSG[lang])}""")
