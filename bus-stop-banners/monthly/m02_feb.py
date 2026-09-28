"""February: HR is asking for tax-saving proofs (ELSS)."""
from framework import call, logo, qr_block

KEY = "02-feb"
MSG = {"en": "Hi MoneyHoney! I saw your bus stop ad. I want to save tax with ELSS.",
       "hi": "Namaste MoneyHoney! Maine bus stop par aapka ad dekha. Mujhe ELSS se tax bachana hai."}
NOTE = {"en": "*Under the old tax regime, 30% slab plus 4% cess, on &#8377;1.5 lakh invested. Tax benefits as per "
              "current laws, subject to change. ELSS is subject to market risk.",
        "hi": "*पुरानी टैक्स व्यवस्था में 30% स्लैब + 4% सेस, &#8377;1.5 लाख निवेश पर। टैक्स लाभ मौजूदा कानूनों के "
              "अनुसार, बदल सकते हैं। ELSS में बाज़ार जोखिम है।"}
T = {
    "en": dict(
        app="HR Team", now="now", n_title="Reminder: Submit your investment proofs",
        n_body="The last date for tax-saving declarations is approaching. Please upload your proofs...",
        f_h1="Got this message too?", f_h2="Save up to &#8377;46,800* in tax with ELSS.",
        l_h="Investment proofs pending?", l_sub="Don&rsquo;t let the deadline decide your tax.",
        r_stat="&#8377;46,800*", r_cap="tax you could save with ELSS.", r_sub="Only a 3-year lock-in.",
        b_h1='Tax saving that <span class="o">also grows your money.</span>',
        cols=[("&#8377;1.5 lakh", "80C limit you can invest"), ("3 years", "shortest lock-in under 80C"),
              ("&#8377;46,800*", "maximum tax saved a year")],
        b_sub="Proofs pending with HR? We&rsquo;ll help you invest and get the proof in time."),
    "hi": dict(
        app="HR टीम", now="अभी", n_title="रिमाइंडर: अपने investment proofs जमा करें",
        n_body="टैक्स बचत declarations की आख़िरी तारीख़ पास है। कृपया अपने proofs अपलोड करें...",
        f_h1="आपको भी यह मैसेज आया?", f_h2="ELSS से &#8377;46,800* तक टैक्स बचाइए।",
        l_h="Investment proofs बाकी हैं?", l_sub="टैक्स का फ़ैसला deadline पर मत छोड़िए।",
        r_stat="&#8377;46,800*", r_cap="तक टैक्स की बचत ELSS से।", r_sub="सिर्फ़ 3 साल का लॉक-इन।",
        b_h1='ऐसी टैक्स बचत, <span class="o">जो पैसा भी बढ़ाए।</span>',
        cols=[("&#8377;1.5 लाख", "80C में निवेश की सीमा"), ("3 साल", "80C में सबसे छोटा लॉक-इन"),
              ("&#8377;46,800*", "साल में अधिकतम टैक्स बचत")],
        b_sub="HR को proof देना है? हम निवेश और proof, दोनों समय पर करवाने में मदद करेंगे।"),
}

BELL = ('<svg viewBox="0 0 64 64" width="100%" height="100%"><path fill="#E8511A" d="M32 6c-2.4 0-4 1.7-4 3.9v1.8C19.9 '
        '13.4 15 20.3 15 28.6v11.2L10 46v3h44v-3l-5-6.2V28.6c0-8.3-4.9-15.2-13-16.9V9.9C36 7.7 34.4 6 32 6zm-6 46a6 6 '
        '0 0 0 12 0H26z"/><circle cx="48" cy="14" r="9" fill="#fff"/><text x="48" y="18.5" text-anchor="middle" '
        'font-family="DM Sans" font-weight="800" font-size="13" fill="#1B2666">1</text></svg>')

CARD = """
.notif { position:absolute; background:#fff; border-radius:22px; box-shadow:0 18px 40px rgba(0,0,0,.35); color:var(--ink); }
.notif .hd { display:flex; align-items:center; gap:10px; color:var(--muted); font-weight:600; }
.notif .ic { background:var(--orange); color:#fff; font-weight:800; border-radius:9px; display:flex; align-items:center;
  justify-content:center; font-family:'DM Sans'; }
.notif .ti { font-weight:800; color:var(--ink); line-height:1.2; }
.notif .bd { color:var(--muted); line-height:1.35; }
"""


def panels(lang, t):
    front = dict(bg="var(--navy)", legal="dark", note=True, css=CARD + """
.stage { background:radial-gradient(circle at 20% 50%, #26338a 0, var(--navy) 60%); }
.notif { left:60px; top:70px; width:560px; padding:20px 26px 22px; transform:rotate(-2deg); }
.notif .hd { font-size:17px; } .notif .ic { width:34px; height:34px; font-size:14px; }
.notif .hd .sp { flex:1; } .notif .ti { font-size:25px; margin-top:12px; } .notif .bd { font-size:18px; margin-top:6px; }
.ghost { position:absolute; left:80px; top:58px; width:530px; height:180px; border-radius:22px; background:rgba(255,255,255,.12);
  transform:rotate(3deg); }
.copy { position:absolute; left:700px; right:56px; top:54px; color:#fff; }
.copy .a { font-size:50px; font-family:var(--sans); font-weight:800; line-height:var(--lt); }
.copy .b { font-size:40px; margin-top:10px; }
.row { position:absolute; left:700px; right:56px; bottom:30px; display:flex; align-items:center; justify-content:space-between; color:#fff; }
""", html=f"""
<div class="ghost"></div>
<div class="notif"><div class="hd"><div class="ic">HR</div><span>{t['app']}</span><span class="sp"></span><span>{t['now']}</span></div>
<div class="ti">{t['n_title']}</div><div class="bd">{t['n_body']}</div></div>
<div class="copy"><div class="a">{t['f_h1']}</div><div class="b d o">{t['f_h2']}</div></div>
<div class="row">{logo(40, chip=True)}{call(44)}</div>""")

    left = dict(bg="var(--navy)", legal="dark", note=False, css="""
.bell { position:absolute; left:30px; top:36px; width:120px; height:120px; }
.h1 { position:absolute; left:30px; right:26px; top:172px; color:#fff; font-size:38px; font-weight:800; line-height:var(--lt); }
.sub { position:absolute; left:30px; right:26px; top:262px; color:rgba(255,255,255,.8); font-size:17px; }
.bot { position:absolute; left:30px; right:26px; bottom:16px; display:flex; justify-content:space-between; align-items:center; color:#fff; }
.lg { position:absolute; right:26px; top:30px; }
""", html=f"""
<div class="bell">{BELL}</div><div class="lg">{logo(24, chip=True)}</div>
<div class="h1">{t['l_h']}</div><div class="sub">{t['l_sub']}</div>
<div class="bot">{call(28)}</div>""")

    right = dict(bg="var(--orange)", legal="dark", note=True, css="""
.lg { position:absolute; left:28px; top:24px; }
.stat { position:absolute; left:26px; top:92px; color:#fff; font-size:76px; white-space:nowrap; }
.cap { position:absolute; left:30px; right:24px; top:198px; color:#fff; font-size:23px; font-weight:700; line-height:1.25; }
.sub { position:absolute; left:30px; top:262px; background:var(--navy); color:#fff; font-size:16px; font-weight:700;
  padding:5px 12px; border-radius:30px; }
.bot { position:absolute; left:30px; bottom:16px; color:var(--navy); }
.bot .call .ico { color:var(--navy); }
""", html=f"""
<div class="lg">{logo(26, chip=True)}</div>
<div class="stat d">{t['r_stat']}</div><div class="cap">{t['r_cap']}</div><div class="sub">{t['r_sub']}</div>
<div class="bot">{call(30)}</div>""")

    cols = "".join(f'<div class="col"><div class="v d">{v}</div><div class="l">{l}</div></div>' for v, l in t["cols"])
    back = dict(bg="#fff", legal="dark", note=True, css=CARD + """
.top { position:absolute; left:44px; right:330px; top:28px; display:flex; align-items:center; justify-content:space-between; }
.h1 { position:absolute; left:44px; right:330px; top:84px; font-size:36px; }
.cols { position:absolute; left:44px; right:330px; top:170px; display:flex; gap:14px; }
.col { flex:1; border-top:5px solid var(--navy); padding-top:10px; }
.col:last-child { border-top-color:var(--orange); }
.col .v { font-size:36px; white-space:nowrap; } .col:last-child .v { color:var(--orange); }
.col .l { font-size:15px; color:var(--muted); margin-top:4px; }
.sub { position:absolute; left:44px; right:330px; bottom:22px; font-size:16px; font-weight:600; }
.cta { position:absolute; right:0; top:0; bottom:0; width:290px; background:var(--navy); color:#fff;
  display:flex; align-items:center; justify-content:center; gap:18px; flex-direction:column; }
.cta .notif { position:static; transform:none; padding:10px 14px; width:230px; border-radius:14px; }
.cta .notif .ti { font-size:14px; margin:0; }
.tag { font-size:15px; font-weight:700; color:var(--muted); }
""", html=f"""
<div class="top">{logo(44)}<div class="tag">{t['app']} &middot; {t['n_title']}</div></div>
<div class="h1 d">{t['b_h1']}</div>
<div class="cols">{cols}</div>
<div class="sub">{t['b_sub']}</div>
<div class="cta">{qr_block(lang, MSG[lang], 128, 14, label_color="#fff")}{call(26)}</div>""")
    return dict(front=front, left=left, right=right, back=back)
