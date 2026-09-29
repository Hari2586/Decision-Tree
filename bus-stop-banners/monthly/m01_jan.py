"""January: the one New Year resolution that keeps itself (SIP)."""
from framework import call, logo, qr_block

KEY = "01-jan"
MSG = {"en": "Hi MoneyHoney! I saw your bus stop ad. I want to start a SIP.",
       "hi": "Namaste MoneyHoney! Maine bus stop par aapka ad dekha. Mujhe SIP shuru karni hai."}
NOTE = {"en": "*Illustration at an assumed 12% p.a. return for understanding only. Mutual funds do not guarantee "
              "returns; actual returns may be higher or lower.",
        "hi": "*12% वार्षिक अनुमानित रिटर्न पर केवल समझाने हेतु उदाहरण। म्यूचुअल फंड रिटर्न की गारंटी नहीं देते; "
              "वास्तविक रिटर्न कम या ज़्यादा हो सकते हैं।"}
T = {
    "en": dict(
        list_title="New Year Resolutions", items=["Gym every day", "No sweets", "Read more books"], sip="Start a SIP",
        f_h1="Most resolutions quit by February.", f_h2="This one runs for 20 years.",
        l_lbl="Resolution #1", l_item="Gym daily", l_cap="Lasted 12 days.",
        r_lbl="Resolution #2", r_item="Start a SIP", r_cap="Still running 20 years later.", r_stat="&asymp; &#8377;50 lakh*",
        b_lbl="The resolution that keeps itself", b_h1='Set it once.<br><span class="o">It shows up every month.</span>',
        b_sub="&#8377;5,000 a month in a SIP, for 20 years.", b_inv="You invest &#8377;12 lakh",
        b_val="&asymp; &#8377;50 lakh*", b_y1="Year 1", b_y20="Year 20"),
    "hi": dict(
        list_title="नए साल के संकल्प", items=["रोज़ जिम", "मिठाई बंद", "ज़्यादा किताबें पढ़ना"], sip="SIP शुरू करना",
        f_h1="ज़्यादातर संकल्प फ़रवरी तक टूट जाते हैं।", f_h2="यह वाला 20 साल चलता है।",
        l_lbl="संकल्प #1", l_item="रोज़ जिम", l_cap="12 दिन चला।",
        r_lbl="संकल्प #2", r_item="SIP शुरू करना", r_cap="20 साल बाद भी जारी।", r_stat="&asymp; &#8377;50 लाख*",
        b_lbl="जो संकल्प खुद निभता है", b_h1='एक बार शुरू कीजिए।<br><span class="o">हर महीने खुद चलता है।</span>',
        b_sub="SIP में हर महीने &#8377;5,000, 20 साल तक।", b_inv="आपका निवेश &#8377;12 लाख",
        b_val="&asymp; &#8377;50 लाख*", b_y1="साल 1", b_y20="साल 20"),
}


def _sip_bars():
    vals, fv = [], 0.0
    for m in range(240):
        fv = (fv + 5000) * 1.01
        if m % 12 == 11:
            vals.append(fv)
    top = vals[-1]
    bars = []
    for i, v in enumerate(vals):
        h = 150 * v / top
        inv = 150 * 5000 * 12 * (i + 1) / top
        x = 14 + i * 26
        bars.append(f'<rect x="{x}" y="{160 - h:.1f}" width="18" height="{h:.1f}" rx="3" fill="#E8511A"/>'
                    f'<rect x="{x}" y="{160 - inv:.1f}" width="18" height="{inv:.1f}" rx="3" fill="#1B2666"/>')
    return "".join(bars)


PAPER = """
.paper { position:absolute; background:#fff; transform:rotate(-2.5deg); box-shadow:0 10px 30px rgba(27,38,102,.16);
  background-image:repeating-linear-gradient(#fff 0 39px, #D9E1EF 39px 40px); border-radius:4px; }
.paper::before { content:''; position:absolute; top:0; bottom:0; left:46px; width:2px; background:rgba(232,81,26,.45); }
.strike { text-decoration:line-through; text-decoration-color:var(--orange); text-decoration-thickness:4px; }
.circled { display:inline-block; border:4px solid var(--orange); border-radius:50%; padding:0 18px; margin-left:-18px; }
"""


def panels(lang, t):
    items = "".join(f'<li class="strike">{i}</li>' for i in t["items"])
    front = dict(bg="var(--cream)", legal="navy", note=False, css=PAPER + """
.paper { left:56px; top:22px; width:470px; height:250px; padding:6px 30px 0 70px; }
.paper .t { font-size:34px; color:var(--navy); line-height:40px; }
.paper ul { list-style:none; font-size:32px; line-height:40px; color:var(--navy); margin-top:6px; }
.copy { position:absolute; left:600px; right:56px; top:52px; }
.copy .d { font-size:46px; }
.row { position:absolute; left:600px; right:56px; bottom:34px; display:flex; align-items:center; justify-content:space-between; }
""", html=f"""
<div class="paper h"><div class="t">{t['list_title']}</div>
<ul>{items}<li><span class="circled">{t['sip']}</span></li></ul></div>
<div class="copy"><div class="d">{t['f_h1']}</div><div class="d o">{t['f_h2']}</div></div>
<div class="row">{logo(46)}{call(46)}</div>""")

    left = dict(bg="var(--cream)", legal="navy", note=False, css=PAPER + """
.paper { left:26px; right:26px; top:70px; height:180px; padding:10px 20px 0 64px; }
.lbl { font-size:30px; color:var(--muted); line-height:40px; }
.item { font-size:52px; line-height:60px; color:var(--navy); margin-top:8px; }
.cap { position:absolute; left:30px; right:30px; top:268px; font-size:34px; }
.top { position:absolute; left:30px; top:20px; }
.bot { position:absolute; left:30px; bottom:18px; }
""", html=f"""
<div class="top">{logo(30)}</div>
<div class="paper h"><div class="lbl">{t['l_lbl']}</div><div class="item strike">{t['l_item']}</div></div>
<div class="cap d">{t['l_cap']}</div>
<div class="bot">{call(28)}</div>""")

    right = dict(bg="var(--navy)", legal="dark", note=True, css="""
.top { position:absolute; left:28px; top:18px; }
.lbl { position:absolute; left:32px; top:84px; font-size:30px; color:var(--orange); }
.item { position:absolute; left:48px; top:122px; font-size:50px; color:#fff; }
.item .circled { display:inline-block; border:4px solid var(--orange); border-radius:50%; padding:2px 18px; margin-left:-18px; }
.cap { position:absolute; left:32px; right:28px; top:208px; color:#fff; font-size:24px; }
.stat { font-size:40px; color:var(--orange); margin-top:4px; }
.bot { position:absolute; left:32px; bottom:16px; color:#fff; }
""", html=f"""
<div class="top">{logo(28, chip=True)}</div>
<div class="lbl h">{t['r_lbl']}</div>
<div class="item h"><span class="circled">{t['r_item']}</span></div>
<div class="cap d">{t['r_cap']}<div class="stat d">{t['r_stat']}</div></div>
<div class="bot">{call(28)}</div>""")

    back = dict(bg="var(--cream)", legal="navy", note=True, css="""
.copy { position:absolute; left:44px; top:30px; width:430px; }
.lbl { font-size:14px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); }
.copy .d { font-size:35px; margin-top:10px; }
.sub { font-size:18px; margin-top:16px; color:var(--navy); font-weight:500; }
.brand { position:absolute; left:44px; bottom:22px; }
.chart { position:absolute; left:480px; top:36px; width:500px; height:250px; }
.chart .c1 { position:absolute; left:14px; top:0; font-size:15px; color:var(--navy); font-weight:700; }
.chart .c2 { position:absolute; right:0; top:0; text-align:right; font-size:34px; color:var(--orange); }
.chart svg { position:absolute; left:0; bottom:22px; }
.chart .ax { position:absolute; bottom:0; font-size:13px; color:var(--muted); }
.cta { position:absolute; right:0; top:0; bottom:0; width:200px; background:var(--navy); color:#fff;
  display:flex; flex-direction:column; align-items:center; justify-content:center; gap:12px; }
.key { display:flex; gap:16px; position:absolute; left:14px; top:26px; font-size:13px; color:var(--muted); }
.key i { display:inline-block; width:12px; height:12px; border-radius:3px; margin-right:5px; vertical-align:-1px; }
""", html=f"""
<div class="copy"><div class="lbl">{t['b_lbl']}</div><div class="d">{t['b_h1']}</div><div class="sub">{t['b_sub']}</div></div>
<div class="brand">{logo(40)}</div>
<div class="chart">
  <div class="c2 d">{t['b_val']}</div>
  <div class="key"><span><i style="background:#1B2666"></i>{t['b_inv']}</span></div>
  <svg width="500" height="160" viewBox="0 0 540 160">{_sip_bars()}</svg>
  <div class="ax" style="left:14px">{t['b_y1']}</div><div class="ax" style="right:14px">{t['b_y20']}</div>
</div>
<div class="cta">{qr_block(lang, MSG[lang], 118, 13, label_color="#fff")}{call(22)}</div>""")
    return dict(front=front, left=left, right=right, back=back)
