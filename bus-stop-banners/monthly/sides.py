"""The single 4x4 side panel for each month: hook + punchline + WhatsApp QR + number.

One side panel is installed per shelter, so it carries the whole story on its own (problem, then answer)
and, with the backdrop, one of the two places people can scan.
"""
import m02_feb
import m03_mar
import m05_may
import m06_jun
import m07_jul
import m09_sep
import m10_oct
import m11_nov
import m12_dec
from framework import call, logo, qr_svg, TEXT

MINI_NOTE = """<div class="mn h"><s>{a}</s><s>{b}</s><span>{c}</span></div>"""

# bg, mode (light / dark / orange), accent, legal theme, extra stage css
THEME = {
    "01-jan": ("var(--cream)", "light", "var(--orange)", "navy", ""),
    "02-feb": ("var(--navy)", "dark", "var(--orange)", "dark", ""),
    "03-mar": ("var(--orange)", "orange", "var(--navy)", "dark", ""),
    "04-apr": ("#fff", "light", "var(--orange)", "navy", ""),
    "05-may": ("var(--navy)", "dark", "var(--orange)", "dark", ""),
    "06-jun": ("var(--orange)", "orange", "var(--navy)", "dark", ""),
    "07-jul": ("#0C1632", "dark", "var(--orange)", "navy", f".stage {{ {m07_jul.RAIN} }}"),
    "08-aug": ("#fff", "light", "var(--orange)", "navy", ""),
    "09-sep": ("var(--cream)", "light", "var(--orange)", "navy", ""),
    "10-oct": ("#0C1632", "dark", "var(--gold)", "navy", f".stage {{ {m10_oct.SPARKLE} }}"),
    "11-nov": ("var(--navy)", "dark", "var(--orange)", "dark", ""),
    "12-dec": ("#fff", "light", "var(--orange)", "navy", ""),
}

COPY = {
    "01-jan": dict(
        en=("Most resolutions quit by February.", "A SIP keeps going for 20 years.", False),
        hi=("ज़्यादातर संकल्प फ़रवरी तक टूट जाते हैं।", "SIP 20 साल तक चलती रहती है।", False)),
    "02-feb": dict(
        en=("Investment proofs pending?", "Save up to &#8377;46,800* in tax with ELSS.", True),
        hi=("Investment proofs बाकी हैं?", "ELSS से &#8377;46,800* तक टैक्स बचाइए।", True)),
    "03-mar": dict(
        en=("Tick. Tock.", "Save tax with ELSS before 31 March.*", True),
        hi=("टिक। टिक।", "31 मार्च से पहले ELSS से टैक्स बचाइए।*", True)),
    "04-apr": dict(
        en=("Salary +10%. SIP +0%?", "Step it up: &asymp; &#8377;99 lakh* vs &#8377;50 lakh.", True),
        hi=("सैलरी +10%। SIP +0%?", "SIP बढ़ाइए: &#8377;50 लाख की जगह &asymp; &#8377;99 लाख*।", True)),
    "05-may": dict(
        en=("FD maturing?", "Compare 5 options before you renew.*", True),
        hi=("FD मैच्योर हो रही है?", "रिन्यू से पहले 5 विकल्पों की तुलना करें।*", True)),
    "06-jun": dict(
        en=("School today. College in 15 years.", "A &#8377;20 lakh degree may cost &asymp; &#8377;84 lakh*.", True),
        hi=("आज स्कूल। 15 साल बाद कॉलेज।", "&#8377;20 लाख की डिग्री &asymp; &#8377;84 लाख* की हो सकती है।", True)),
    "07-jul": dict(
        en=("Nobody buys an umbrella mid-storm.", "Keep 6 months of expenses ready.*", True),
        hi=("तूफ़ान के बीच छाता कोई नहीं खरीदता।", "6 महीने के खर्च पहले से तैयार रखें।*", True)),
    "08-aug": dict(
        en=("India became free in 1947.", "When will you? Plan your retirement.", False),
        hi=("भारत 1947 में आज़ाद हुआ।", "आप कब होंगे? रिटायरमेंट की planning कीजिए।", False)),
    "09-sep": dict(
        en=("Sold a property?", "6 months to save tax with 54EC bonds.*", True),
        hi=("प्रॉपर्टी बेची?", "54EC बॉन्ड से टैक्स बचाने के लिए 6 महीने हैं।*", True)),
    "10-oct": dict(
        en=("Crackers last 10 seconds.", "A SIP gift lasts 18 years.", False),
        hi=("पटाखे 10 सेकंड चलते हैं।", "SIP का तोहफ़ा 18 साल चलता है।", False)),
    "11-nov": dict(
        en=("Bonus: spend it or grow it?", "&#8377;1 lakh &rarr; &asymp; &#8377;5.5 lakh* in 15 years.", True),
        hi=("बोनस: खर्च करें या बढ़ाएँ?", "&#8377;1 लाख &rarr; 15 साल में &asymp; &#8377;5.5 लाख*।", True)),
    "12-dec": dict(
        en=("Health check-up: done.", "Wealth check-up: book it free.*", True),
        hi=("हेल्थ चेक-अप: हो गया।", "वेल्थ चेक-अप: मुफ़्त बुक करें।*", True)),
}


def visual(key, lang):
    hi = lang == "hi"
    if key == "01-jan":
        return MINI_NOTE.format(a="जिम" if hi else "Gym", b="डाइट" if hi else "Diet", c="SIP &#10003;")
    if key == "02-feb":
        return m02_feb.BELL
    if key == "03-mar":
        return m03_mar.calendar(96, "मार्च" if hi else "MARCH", 54, 11, rot=5)
    if key == "04-apr":
        return '<div class="bigv">+10%<span>&uarr;</span></div>'
    if key == "05-may":
        return m05_may.toggle(104, 46, 17)
    if key == "06-jun":
        return m06_jun.icon(m06_jun.CAP, "#1B2666", "#fff")
    if key == "07-jul":
        return m07_jul.umb("#E8511A", "#fff")
    if key == "08-aug":
        return '<div class="yr blank">20<u></u></div>'
    if key == "09-sep":
        return m09_sep.clock(92, "50%")
    if key == "10-oct":
        return m10_oct.DIYA
    if key == "11-nov":
        return m11_nov.ARROW.replace("{c}", "#E8511A")
    return m12_dec.ecg(110, 70)


def side_panel(mod, lang):
    key = mod.KEY
    bg, mode, accent, legal_theme, extra = THEME[key]
    setup, punch, note = COPY[key][lang]
    ink = "var(--navy)" if mode == "light" else "#fff"
    css = m03_mar.CAL + m05_may.TOGGLE + m09_sep.CLOCK + extra + f"""
.lg {{ position:absolute; left:26px; top:18px; }}
.vis {{ position:absolute; right:18px; top:12px; width:110px; height:104px; display:flex; align-items:center; justify-content:center; }}
.vis > svg {{ width:100%; height:100%; }}
.setup {{ position:absolute; left:26px; right:140px; top:62px; color:{ink}; font-family:var(--sans); font-weight:800;
  font-size:21px; line-height:1.18; opacity:.9; }}
.punch {{ position:absolute; left:26px; right:20px; top:128px; color:{accent}; font-size:31px; }}
.cta {{ position:absolute; left:26px; right:20px; bottom:12px; display:flex; align-items:center; gap:14px; color:{ink}; }}
.cta .qr {{ width:90px; height:90px; background:#fff; padding:6px; border-radius:7px; flex:none; }}
.cta .qr svg {{ display:block; }}
.cta .sl {{ font-size:13px; font-weight:700; opacity:.85; margin-bottom:5px; }}
.cta .call .ico {{ color:{'#fff' if mode == 'orange' else 'var(--orange)'}; }}
.mn {{ background:#fff; transform:rotate(-4deg); box-shadow:0 6px 14px rgba(27,38,102,.15); padding:8px 14px; color:var(--navy);
  font-size:22px; line-height:1.15; display:flex; flex-direction:column; border-radius:4px; }}
.mn s {{ text-decoration-color:var(--orange); text-decoration-thickness:3px; }}
.mn span {{ border:3px solid var(--orange); border-radius:50%; padding:0 8px; margin-left:-8px; }}
.bigv {{ font-family:'DM Sans'; font-weight:800; font-size:30px; color:var(--orange); white-space:nowrap; }}
.yr {{ white-space:nowrap; font-family:'Lora', serif; font-weight:700; font-size:50px; color:var(--orange); line-height:1; }}
.yr u {{ text-decoration:none; display:inline-block; border-bottom:.08em solid var(--orange); width:1.05em; height:.7em; margin-left:.04em; }}
"""
    html = f"""
<div class="lg">{logo(22, chip=mode != 'light')}</div>
<div class="vis">{visual(key, lang)}</div>
<div class="setup">{setup}</div>
<div class="punch d">{punch}</div>
<div class="cta"><div class="qr">{qr_svg(mod.MSG[lang])}</div>
<div><div class="sl">{TEXT[lang]['scan']}</div>{call(29)}</div></div>"""
    return dict(bg=bg, legal=legal_theme, note=note, css=css, html=html)
