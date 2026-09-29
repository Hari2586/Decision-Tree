"""June: schools reopen. First day of school today, first day of college in 15 years (child education)."""
from framework import call, logo, qr_block

KEY = "06-jun"
MSG = {"en": "Hi MoneyHoney! I saw your bus stop ad. I want to plan for my child's education.",
       "hi": "Namaste MoneyHoney! Maine bus stop par aapka ad dekha. Mujhe bachche ki padhai ke liye planning karni hai."}
NOTE = {"en": "*Illustration at an assumed 10% p.a. education cost inflation for understanding only. Actual costs may differ.",
        "hi": "*10% वार्षिक अनुमानित शिक्षा महँगाई पर केवल समझाने हेतु उदाहरण। वास्तविक खर्च अलग हो सकता है।"}
T = {
    "en": dict(
        f_h1="Today: first day of school.", f_h2="In 15 years: first day of college.",
        f_q="Will the fees be ready?", t_a="Age 3 &middot; &#8377;20 lakh today", t_b="Age 18 &middot; &asymp; &#8377;84 lakh*",
        l_age="Age 3", l_cap="Packing the school bag today.",
        r_age="Age 18", r_cap="Is the college fund packed too?",
        b_h1='Their dreams have a due date. <span class="o">Let&rsquo;s be ready.</span>',
        b_sub="Cost of a &#8377;20 lakh degree as your child grows up*", yrs=["Today", "+5 yrs", "+10 yrs", "+15 yrs"]),
    "hi": dict(
        f_h1="आज: स्कूल का पहला दिन।", f_h2="15 साल बाद: कॉलेज का पहला दिन।",
        f_q="क्या फीस तैयार होगी?", t_a="उम्र 3 &middot; आज &#8377;20 लाख", t_b="उम्र 18 &middot; &asymp; &#8377;84 लाख*",
        l_age="उम्र 3", l_cap="आज स्कूल बैग तैयार।",
        r_age="उम्र 18", r_cap="क्या कॉलेज फंड भी तैयार है?",
        b_h1='सपनों की भी एक तारीख़ होती है। <span class="o">चलिए, तैयार रहें।</span>',
        b_sub="बच्चे के बड़े होने के साथ &#8377;20 लाख की डिग्री का खर्च*", yrs=["आज", "+5 साल", "+10 साल", "+15 साल"]),
}

BAG = ('<svg viewBox="0 0 64 64" width="100%" height="100%"><path d="M22 14a10 10 0 0 1 20 0v4h-5v-4a5 5 0 0 0-10 0v4h-5z" '
       'fill="{c2}"/><rect x="10" y="18" width="44" height="42" rx="10" fill="{c1}"/><rect x="18" y="36" width="28" '
       'height="16" rx="4" fill="{c2}"/><rect x="29" y="34" width="6" height="6" rx="1.5" fill="{c1}"/></svg>')
CAP = ('<svg viewBox="0 0 64 64" width="100%" height="100%"><path d="M32 12 2 26l30 14 30-14z" fill="{c1}"/><path d="M14 '
       '32v12c0 5 8 9 18 9s18-4 18-9V32L32 41z" fill="{c1}"/><path d="M55 29v16" stroke="{c2}" stroke-width="3"/>'
       '<circle cx="55" cy="47" r="3.5" fill="{c2}"/></svg>')


def icon(svg, c1, c2):
    return svg.replace("{c1}", c1).replace("{c2}", c2)


def panels(lang, t):
    front = dict(bg="var(--navy)", legal="dark", note=True, css="""
.copy { position:absolute; left:60px; top:24px; right:520px; color:#fff; }
.copy .a { font-size:44px; } .copy .b { font-size:44px; color:var(--orange); }
.copy .q { font-size:26px; font-weight:700; margin-top:10px; color:rgba(255,255,255,.85); }
.tl { position:absolute; left:60px; right:520px; bottom:12px; height:86px; }
.tl .ln { position:absolute; left:74px; right:74px; top:36px; border-top:5px dotted rgba(255,255,255,.5); }
.tl .ic { position:absolute; top:0; width:74px; height:74px; }
.tl .ic.a { left:0; } .tl .ic.b { right:0; }
.tl .la { position:absolute; left:88px; top:48px; color:#fff; font-size:18px; font-weight:700; }
.tl .lb { position:absolute; right:88px; top:48px; color:var(--orange); font-size:18px; font-weight:800; }
.side { position:absolute; right:0; top:0; bottom:0; width:460px; background:var(--cream); display:flex; flex-direction:column;
  align-items:center; justify-content:center; gap:22px; }
""", html=f"""
<div class="copy"><div class="a d">{t['f_h1']}</div><div class="b d">{t['f_h2']}</div><div class="q">{t['f_q']}</div></div>
<div class="tl"><div class="ln"></div><div class="ic a">{icon(BAG, '#fff', '#E8511A')}</div><div class="ic b">{icon(CAP, '#E8511A', '#fff')}</div>
<div class="la">{t['t_a']}</div><div class="lb">{t['t_b']}</div></div>
<div class="side">{logo(50)}{call(48)}</div>""")

    left = dict(bg="var(--cream)", legal="navy", note=False, css="""
.ic { position:absolute; left:30px; top:34px; width:150px; height:150px; }
.age { position:absolute; left:30px; top:196px; font-size:62px; font-family:var(--sans); font-weight:800; line-height:1; color:var(--navy); }
.cap { position:absolute; left:30px; right:26px; top:266px; font-size:22px; font-weight:600; color:var(--muted); }
.bot { position:absolute; left:30px; bottom:14px; }
.lg { position:absolute; right:24px; top:30px; }
""", html=f"""
<div class="ic">{icon(BAG, '#1B2666', '#E8511A')}</div><div class="lg">{logo(22)}</div>
<div class="age">{t['l_age']}</div><div class="cap">{t['l_cap']}</div><div class="bot">{call(28)}</div>""")

    right = dict(bg="var(--orange)", legal="dark", note=False, css="""
.ic { position:absolute; right:26px; top:34px; width:160px; height:160px; }
.age { position:absolute; left:30px; top:196px; font-size:62px; font-family:var(--sans); font-weight:800; line-height:1; color:#fff; }
.cap { position:absolute; left:30px; right:26px; top:262px; font-size:21px; color:var(--navy); }
.bot { position:absolute; left:30px; bottom:14px; color:#fff; }
.bot .call .ico { color:var(--navy); }
.lg { position:absolute; left:28px; top:30px; }
""", html=f"""
<div class="ic">{icon(CAP, '#1B2666', '#fff')}</div><div class="lg">{logo(22, chip=True)}</div>
<div class="age">{t['r_age']}</div><div class="cap d">{t['r_cap']}</div><div class="bot">{call(28)}</div>""")

    costs = [20 * 1.1 ** y for y in (0, 5, 10, 15)]
    unit = "लाख" if lang == "hi" else "lakh"
    bars = ""
    for i, (c, y) in enumerate(zip(costs, t["yrs"])):
        h = 170 * c / costs[-1]
        lab = f"&#8377;{c:.0f} {unit}" + ("*" if i else "")
        bars += (f'<div class="bw"><div class="bv{" hl" if i == 3 else ""}">{lab}</div>'
                 f'<div class="br{" hl" if i == 3 else ""}" style="height:{h:.0f}px"></div><div class="by">{y}</div></div>')
    back = dict(bg="var(--cream)", legal="navy", note=True, css="""
.lg { position:absolute; left:44px; top:26px; }
.h1 { position:absolute; left:44px; width:430px; top:90px; font-size:36px; }
.bars { position:absolute; left:520px; top:40px; width:380px; height:270px; display:flex; align-items:flex-end; gap:22px; }
.bw { flex:1; display:flex; flex-direction:column; align-items:center; justify-content:flex-end; height:100%; }
.bv { font-weight:800; font-size:15px; margin-bottom:6px; white-space:nowrap; } .bv.hl { color:var(--orange); font-size:19px; }
.br { width:100%; background:var(--navy); border-radius:8px 8px 0 0; } .br.hl { background:var(--orange); }
.by { font-size:13px; color:var(--muted); margin-top:6px; }
.sub { position:absolute; left:44px; width:430px; bottom:26px; font-size:15px; color:var(--muted); font-weight:600; }
.ics { position:absolute; left:44px; top:218px; display:flex; gap:12px; align-items:center; }
.ics .i { width:52px; height:52px; } .ics .dots { width:120px; border-top:4px dotted var(--navy); }
.cta { position:absolute; right:0; top:0; bottom:0; width:260px; background:var(--navy); color:#fff; display:flex;
  flex-direction:column; align-items:center; justify-content:center; gap:14px; }
""", html=f"""
<div class="lg">{logo(42)}</div>
<div class="h1 d">{t['b_h1']}</div>
<div class="ics"><div class="i">{icon(BAG, '#1B2666', '#E8511A')}</div><div class="dots"></div><div class="i">{icon(CAP, '#E8511A', '#1B2666')}</div></div>
<div class="sub">{t['b_sub']}</div>
<div class="bars">{bars}</div>
<div class="cta">{qr_block(lang, MSG[lang], 124, 14, label_color="#fff")}{call(24)}</div>""")
    return dict(front=front, left=left, right=right, back=back)
