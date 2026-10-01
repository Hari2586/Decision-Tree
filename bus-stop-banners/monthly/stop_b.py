"""Second bus stop: one product/planning topic per month, Hindi only.

Each topic picks a front, side and backdrop layout plus a palette, so neighbouring months never look alike.
Built by build.py into monthly/hi/<NN-mon>-b/.
"""
from framework import call, lockup, logo, qr_block, side_cta

PAL = {  # bg, ink, accent, soft text, chip logo?
    "navy": ("var(--navy)", "#fff", "var(--orange)", "rgba(255,255,255,.82)", True),
    "ink": ("var(--ink)", "#fff", "var(--orange)", "rgba(255,255,255,.82)", True),
    "orange": ("var(--orange)", "#fff", "var(--navy)", "rgba(255,255,255,.92)", True),
    "cream": ("var(--cream)", "var(--navy)", "var(--orange)", "var(--muted)", False),
    "white": ("#fff", "var(--navy)", "var(--orange)", "var(--muted)", False),
}

# ---------------------------------------------------------------- icons (brand colours via currentColor / vars)
O, N = "#FF4A00", "#16205B"


def svg(body, vb="0 0 120 120"):
    return f'<svg viewBox="{vb}" width="100%" height="100%">{body}</svg>'


ICON = {
    "target": lambda a, b: svg(
        f'<circle cx="56" cy="64" r="46" fill="none" stroke="{a}" stroke-width="9"/><circle cx="56" cy="64" r="28" '
        f'fill="none" stroke="{b}" stroke-width="9"/><circle cx="56" cy="64" r="10" fill="{a}"/>'
        f'<path d="M58 62 104 16" stroke="{b}" stroke-width="7" stroke-linecap="round"/>'
        f'<path d="M92 10h16v16l-9 3-10-10z" fill="{a}"/>'),
    "house_key": lambda a, b: svg(
        f'<path d="M60 10 10 52h13v52h74V52h13z" fill="{b}"/><rect x="50" y="70" width="20" height="34" rx="2" fill="{a}"/>'
        f'<circle cx="92" cy="92" r="16" fill="none" stroke="{a}" stroke-width="7"/>'
        f'<path d="M80 80 52 52m10 10-7 7m14 0-7 7" stroke="{a}" stroke-width="7" stroke-linecap="round"/>'),
    "woman": lambda a, b: svg(
        f'<circle cx="60" cy="40" r="24" fill="{b}"/><path d="M36 40c0-22 48-22 48 0v18c-6-10-10-22-24-22S42 48 36 58z" '
        f'fill="{a}"/><path d="M18 112c4-30 22-44 42-44s38 14 42 44z" fill="{b}"/>'
        f'<path d="M50 70 60 86l10-16" fill="none" stroke="{a}" stroke-width="6" stroke-linejoin="round"/>'),
    "baskets": lambda a, b: svg(
        "".join(f'<path d="M{x} 70h30l-4 30H{x + 4}z" fill="{b}"/><ellipse cx="{x + 15}" cy="62" rx="8" ry="10" fill="{a}"/>'
                for x in (6, 45, 84)), "0 0 120 110"),
    "pie": lambda a, b: svg(
        f'<circle cx="60" cy="60" r="48" fill="{b}"/><path d="M60 60V12a48 48 0 0 1 41.6 72z" fill="{a}"/>'
        f'<path d="M60 60l41.6 24A48 48 0 0 1 60 108z" fill="#fff"/>'),
    "suitcase": lambda a, b: svg(
        f'<rect x="20" y="38" width="80" height="62" rx="10" fill="{a}"/><path d="M46 38V26h28v12" fill="none" '
        f'stroke="{b}" stroke-width="7"/><path d="M42 38v62M78 38v62" stroke="{b}" stroke-width="6"/>'
        f'<circle cx="34" cy="106" r="5" fill="{b}"/><circle cx="86" cy="106" r="5" fill="{b}"/>'
        f'<path d="M70 16l34-8-6 8 10 6-36-2z" fill="{b}"/>'),
    "bank": lambda a, b: svg(
        f'<path d="M60 10 10 36h100z" fill="{a}"/><rect x="14" y="40" width="92" height="8" fill="{b}"/>'
        + "".join(f'<rect x="{x}" y="52" width="12" height="42" rx="2" fill="{b}"/>' for x in (22, 46, 70, 94 - 4))
        + f'<rect x="10" y="98" width="100" height="10" rx="2" fill="{a}"/>'),
    "cert": lambda a, b: svg(
        f'<rect x="10" y="20" width="100" height="72" rx="6" fill="#fff" stroke="{b}" stroke-width="5"/>'
        f'<path d="M24 40h56M24 54h72M24 68h44" stroke="{b}" stroke-width="5" stroke-linecap="round" opacity=".55"/>'
        f'<circle cx="88" cy="78" r="16" fill="{a}"/><path d="M80 92l-4 20 12-8 12 8-4-20" fill="{a}"/>'),
    "rise": lambda a, b: svg(
        "".join(f'<rect x="{10 + i * 26}" y="{100 - h}" width="18" height="{h}" rx="3" fill="{b}"/>'
                for i, h in enumerate((24, 40, 58, 80)))
        + f'<path d="M8 86 40 60l24 10 46-50" fill="none" stroke="{a}" stroke-width="8" stroke-linecap="round" '
          f'stroke-linejoin="round"/><path d="M92 16h20v20" fill="none" stroke="{a}" stroke-width="8" '
          f'stroke-linecap="round" stroke-linejoin="round"/>'),
    "tap": lambda a, b: svg(
        f'<path d="M14 30h50a14 14 0 0 1 14 14v12H62V46H14z" fill="{b}"/><rect x="34" y="16" width="12" height="16" '
        f'rx="3" fill="{b}"/><rect x="24" y="10" width="32" height="8" rx="4" fill="{a}"/>'
        + "".join(f'<circle cx="70" cy="{y}" r="{r}" fill="{a}"/>' for y, r in ((72, 7), (92, 6), (110, 5)))),
    "loan_sip": lambda a, b: svg(
        f'<path d="M44 14 8 44h10v40h52V44h10z" fill="{b}"/><rect x="36" y="58" width="16" height="26" fill="{a}"/>'
        f'<circle cx="92" cy="80" r="24" fill="{a}"/><text x="92" y="90" text-anchor="middle" font-family="DM Sans" '
        f'font-weight="800" font-size="28" fill="#fff">&#8377;</text>'
        f'<path d="M70 104c10 8 34 8 44-6" fill="none" stroke="{b}" stroke-width="5" stroke-linecap="round"/>'),
    "rings": lambda a, b: svg(
        f'<circle cx="46" cy="70" r="28" fill="none" stroke="{a}" stroke-width="9"/>'
        f'<circle cx="76" cy="70" r="28" fill="none" stroke="{b}" stroke-width="9"/>'
        f'<path d="M64 30l12-14 12 14-12 10z" fill="{a}"/>'),
    "pin": lambda a, b: svg(
        f'<path d="M60 8c-22 0-38 16-38 37 0 28 38 63 38 63s38-35 38-63C98 24 82 8 60 8z" fill="{a}"/>'
        f'<circle cx="60" cy="45" r="14" fill="#fff"/>'
        f'<path d="M10 112c20-14 30 4 50-6s32-8 50 2" fill="none" stroke="{b}" stroke-width="5" stroke-dasharray="3 8" '
        f'stroke-linecap="round"/>'),
}

# ---------------------------------------------------------------- topics
VAC_NOTE = ("*Illustration: &#8377;3 lakh goal in 3 years through a monthly SIP at an assumed 8% p.a. return. Not guaranteed. "
            "This assumption of returns is not indicative of future returns.")
CGB_NOTE = ("*Capital Gain Bonds: exemption on long-term capital gains from sale of land or building if invested within 6 months "
            "of transfer, up to &#8377;50 lakh per financial year, 5-year lock-in. Tax benefits as per current laws, subject to change.")
CFD_NOTE = ("*Corporate Fixed Deposits carry credit risk. Interest rates and terms vary by issuer and are subject to change. "
            "Read the offer terms carefully before investing.")
NCD_NOTE = ("*NCDs carry credit risk and depend on the issuer's ability to pay. Interest rates and terms vary by issue. "
            "Read the offer document carefully before investing.")
SWP_NOTE = "*SWP withdrawals are not guaranteed; they depend on the fund value and may reduce the capital invested."
EMI_NOTE = ("*Illustration: &#8377;30 lakh home loan at 8.5% p.a. for 20 years (EMI &asymp; &#8377;26,000, total interest "
            "&asymp; &#8377;32.5 lakh); SIP of &asymp; &#8377;3,300 a month for 20 years at an assumed 12% p.a. return. "
            "Not guaranteed. This assumption of returns is not indicative of future returns. Loan rates vary by lender.")
WED_NOTE = ("*Illustration: today&rsquo;s wedding cost of &#8377;20 lakh at an assumed 6% p.a. inflation for 15 years, "
            "for understanding only. Actual costs may differ.")

TOPICS = {
    "01-jan": dict(
        name="Financial Planning", msg="Hi! Bus stop ad: Financial planning karni hai.", note="",
        icon="target", front=("A", "navy"), side=("C", "cream"), back=("steps", "white"),
        kick="नया साल, नए लक्ष्य", h1="सपने तो सबके होते हैं।", h2="प्लान कितनों के पास है?",
        sub="घर, बच्चों की पढ़ाई, रिटायरमेंट: हर लक्ष्य का अपना प्लान।",
        s_h="आपके लक्ष्य", s_list=[("&#9744;", "अपना घर"), ("&#9744;", "बच्चों की पढ़ाई"), ("&#9744;", "आरामदायक रिटायरमेंट")],
        s_sub="हर डिब्बे पर &#10003; लगाने का प्लान।",
        b_h1='फ़ाइनेंशियल प्लान, <span class="o">3 आसान कदमों में।</span>',
        b_items=[("लक्ष्य लिखें", "क्या, कब और कितना"), ("आज की स्थिति", "आय, खर्च, बचत और बीमा"),
                 ("हर लक्ष्य का रास्ता", "SIP, FD, बॉन्ड: सही मिश्रण")]),
    "02-feb": dict(
        name="Capital Gain Bond", msg="Hi! Bus stop ad: Capital Gain Bonds ki jankari chahiye.", note=CGB_NOTE,
        icon="house_key", front=("C", "orange"), side=("B", "navy"), back=("grid", "cream"),
        stat="6 महीने", stat_l="प्रॉपर्टी बिक्री के बाद, टैक्स बचाने का समय*",
        kick="प्रॉपर्टी बेची है या बेचने वाले हैं?", h1="मुनाफ़ा आपका,", h2="टैक्स क्यों दें?*",
        sub="कैपिटल गेन बॉन्ड से लॉन्ग-टर्म कैपिटल गेन टैक्स बचाइए।*",
        s_big="&#8377;50 लाख*", s_h="तक हर वित्त वर्ष, कैपिटल गेन बॉन्ड में टैक्स-छूट वाला निवेश।*",
        b_h1='कैपिटल गेन बॉन्ड: <span class="o">4 ज़रूरी बातें।*</span>',
        b_items=[("6 महीने", "बिक्री के 6 महीने के अंदर निवेश"), ("&#8377;50 लाख तक", "हर वित्त वर्ष में"),
                 ("5 साल", "लॉक-इन अवधि"), ("सरकारी कंपनियाँ", "बॉन्ड जारी करने वाली संस्थाएँ")]),
    "03-mar": dict(
        name="Women", msg="Hi! Bus stop ad: Mahilaon ke liye investment planning.", note="",
        icon="woman", front=("B", "orange"), side=("A", "white"), back=("compare", "navy"),
        kick="महिला दिवस पर", h1="घर का बजट वो संभालती है।", h2="अब अपना निवेश भी।",
        sub="हर महिला के नाम, उसकी अपनी आर्थिक आज़ादी।",
        s_h="वो घर की CFO है।", s_sub="अपने लक्ष्यों के लिए आज से निवेश शुरू करें।",
        b_h1='आर्थिक आज़ादी, <span class="o">हर महिला का हक़।</span>',
        b_cols=(("सिर्फ़ बचत", ["पैसा अलमारी या खाते में", "महँगाई से घटती क़ीमत", "लक्ष्य अधूरे"]),
                ("बचत + निवेश", ["हर लक्ष्य के लिए प्लान", "SIP से नियमित निवेश", "अपने नाम पर संपत्ति"]))),
    "04-apr": dict(
        name="Asset Allocation", msg="Hi! Bus stop ad: Asset allocation samajhna hai.", note="",
        icon="baskets", front=("D", "cream"), side=("A", "orange"), back=("tiles", "white"), s_icon="pie",
        kick="नया वित्त वर्ष, नई शुरुआत", h1="सारे अंडे एक ही टोकरी में?", h2="पैसा भी बाँटकर रखिए।",
        sub="इक्विटी, डेट और गोल्ड: उम्र और लक्ष्य के हिसाब से सही मिश्रण।",
        s_h="एक टोकरी। सारे अंडे।", s_sub="और सारा जोखिम भी एक ही जगह।",
        b_h1='सही मिश्रण, <span class="o">सही संतुलन।</span>',
        b_items=[("इक्विटी", "लंबी अवधि में ग्रोथ की संभावना"), ("डेट", "स्थिरता और नियमित आय"),
                 ("गोल्ड", "मुश्किल वक़्त में संतुलन")],
        b_sub="सही मिश्रण आपकी उम्र, लक्ष्य और जोखिम उठाने की क्षमता पर निर्भर करता है।"),
    "05-may": dict(
        name="Vacation Planning", msg="Hi! Bus stop ad: Vacation ke liye planning karni hai.", note=VAC_NOTE,
        icon="suitcase", front=("A", "orange"), side=("B", "cream"), back=("steps", "navy"),
        kick="छुट्टियों का मौसम", h1="अगली छुट्टी EMI पर नहीं,", h2="SIP से।",
        sub="3 साल बाद &#8377;3 लाख का फ़ैमिली ट्रिप? हर महीने &asymp; &#8377;7,400 से शुरुआत।*",
        s_big="&asymp; &#8377;7,400*", s_h="हर महीने, 3 साल तक। फिर &#8377;3 लाख का फ़ैमिली ट्रिप।*",
        b_h1='घूमने का सपना, <span class="o">पहले से प्लान।</span>',
        b_items=[("मंज़िल चुनें", "कहाँ और कब जाना है"), ("बजट तय करें", "आज के हिसाब से खर्च"),
                 ("SIP शुरू करें", "हर महीने थोड़ा-थोड़ा")]),
    "06-jun": dict(
        name="Corporate Fixed Deposit", msg="Hi! Bus stop ad: Corporate FD ke options batayein.", note=CFD_NOTE,
        icon="bank", front=("D", "navy"), side=("C", "white"), back=("grid", "cream"),
        kick="FD रिन्यू करने से पहले", h1="बैंक FD के अलावा भी हैं", h2="कॉर्पोरेट FD के विकल्प।*",
        sub="रेटिंग, अवधि और ब्याज की तुलना करके चुनिए।",
        s_h="कॉर्पोरेट FD से पहले 3 सवाल", s_list=[("1", "क्रेडिट रेटिंग क्या है?"), ("2", "अवधि और ब्याज भुगतान?"),
                                                    ("3", "समय से पहले निकासी के नियम?")],
        s_sub="", b_h1='कॉर्पोरेट FD: <span class="o">समझदारी से चुनें।*</span>',
        b_items=[("क्रेडिट रेटिंग", "AAA, AA जैसी रेटिंग ज़रूर देखें"), ("अवधि", "1 से 5 साल तक के विकल्प"),
                 ("ब्याज भुगतान", "मासिक, तिमाही या सालाना"), ("तुलना", "अलग-अलग कंपनियों के ऑफ़र")]),
    "07-jul": dict(
        name="NCD", msg="Hi! Bus stop ad: NCD ke baare mein jaankari chahiye.", note=NCD_NOTE,
        icon="cert", front=("C", "cream"), side=("A", "navy"), back=("tiles", "white"),
        stat="NCD", stat_l="Non-Convertible Debentures",
        kick="तय आय चाहिए?", h1="तय ब्याज। तय अवधि।", h2="रेटेड कंपनियों से।*",
        sub="NCD के बारे में पूरी जानकारी: ब्याज, रेटिंग और अवधि।",
        s_h="नियमित आय का एक और विकल्प।", s_sub="NCD की पूरी जानकारी, एक कॉल में।*",
        b_h1='NCD में निवेश से पहले <span class="o">3 बातें देखें।*</span>',
        b_items=[("क्रेडिट रेटिंग", "कंपनी की साख"), ("कूपन और भुगतान", "ब्याज कितना और कब"),
                 ("अवधि और लिस्टिंग", "कब तक और कहाँ ट्रेड")],
        b_sub="हम आपको अलग-अलग इश्यू की तुलना समझाएँगे।"),
    "08-aug": dict(
        name="India Growth Story", msg="Hi! Bus stop ad: India growth story mein invest karna hai.", note="",
        icon="rise", front=("A", "white"), side=("A", "orange"), back=("steps", "ink"),
        kick="भारत आगे बढ़ रहा है।", h1="क्या आपका पैसा भी", h2="भारत के साथ बढ़ रहा है?",
        sub="म्यूचुअल फंड के ज़रिए भारत की कंपनियों की ग्रोथ में हिस्सेदार बनिए।",
        s_h="भारत बढ़ रहा है।", s_sub="आप भी साथ बढ़िए।",
        b_h1='भारत की ग्रोथ स्टोरी में <span class="o">आपकी हिस्सेदारी।</span>',
        b_items=[("बचत", "हर महीने एक तय रकम"), ("SIP", "म्यूचुअल फंड के ज़रिए"),
                 ("हिस्सेदारी", "भारत की कंपनियों की ग्रोथ में")]),
    "09-sep": dict(
        name="SWP", msg="Hi! Bus stop ad: SWP se monthly income chahiye.", note=SWP_NOTE,
        icon="tap", front=("D", "cream"), side=("C", "navy"), back=("compare", "white"),
        kick="रिटायरमेंट के बाद", h1="सैलरी रुक गई?", h2="हर महीने की आय जारी रखें।",
        sub="SWP: म्यूचुअल फंड से हर महीने एक तय रकम निकालें।*",
        s_h="SWP क्या देता है?", s_list=[("&#10003;", "हर महीने तय रकम*"), ("&#10003;", "बाकी पैसा निवेश में"),
                                          ("&#10003;", "ज़रूरत के हिसाब से बदलाव")], s_sub="",
        b_h1='रिटायरमेंट के बाद भी <span class="o">हर महीने &lsquo;सैलरी&rsquo;।</span>',
        b_cols=(("एकमुश्त रकम, बिना प्लान", ["खर्च का अंदाज़ा नहीं", "पैसा जल्दी ख़त्म होने का डर", "महँगाई का असर"]),
                ("SWP के साथ", ["हर महीने तय रकम*", "बाकी रकम निवेश में", "ज़रूरत के हिसाब से बदलाव"]))),
    "10-oct": dict(
        name="EMI Management with MF", msg="Hi! Bus stop ad: Home loan EMI ke saath SIP plan.", note=EMI_NOTE,
        icon="loan_sip", front=("C", "white"), side=("B", "orange"), back=("tiles", "cream"),
        stat="&asymp; &#8377;32.5 लाख*", stat_l="&#8377;30 लाख के होम लोन पर 20 साल का ब्याज*",
        kick="होम लोन लिया है?", h1="बैंक को दिया ब्याज,", h2="SIP से वापस पाइए।*",
        sub="EMI के साथ एक छोटी SIP: लोन ख़त्म होने तक ब्याज जितना फंड।*",
        s_big="EMI का &asymp; 13%*", s_h="SIP में लगाइए। 20 साल में ब्याज जितना फंड।*",
        b_h1='EMI भी, <span class="o">निवेश भी।</span>',
        b_items=[("&#8377;26,000", "होम लोन EMI, हर महीने*"), ("&asymp; &#8377;3,300", "साथ में SIP, हर महीने*"),
                 ("&asymp; &#8377;33 लाख*", "20 साल बाद SIP फंड*")],
        b_sub="लोन भी चुकता, और ब्याज जितना फंड भी।*"),
    "11-nov": dict(
        name="Marriage Planning", msg="Hi! Bus stop ad: Bachchon ki shaadi ki planning.", note=WED_NOTE,
        icon="rings", front=("A", "cream"), side=("C", "navy"), back=("steps", "white"),
        kick="शादियों का मौसम", h1="आज &#8377;20 लाख की शादी,", h2="15 साल बाद &asymp; &#8377;48 लाख।*",
        sub="बच्चों की शादी का सपना, आज से प्लान कीजिए।",
        s_h="शादी की तैयारी", s_list=[("&#10003;", "हॉल"), ("&#10003;", "कैटरिंग"), ("?", "शादी का फंड")], s_sub="",
        b_h1='धूमधाम वाली शादी, <span class="o">बिना कर्ज़ के।</span>',
        b_items=[("लक्ष्य तय करें", "कब और कितना"), ("महँगाई जोड़ें", "आज का खर्च, कल की क़ीमत*"),
                 ("SIP शुरू करें", "हर महीने थोड़ा-थोड़ा")]),
    "12-dec": dict(
        name="Financial Planning", msg="Hi! Bus stop ad: Mujhe financial plan chahiye.", note="",
        icon="pin", front=("D", "ink"), side=("A", "cream"), back=("grid", "orange"),
        kick="साल ख़त्म होने को है", h1="बिना GPS सफ़र?", h2="बिना प्लान निवेश?",
        sub="आपके लक्ष्यों तक पहुँचने का रास्ता: एक फ़ाइनेंशियल प्लान।",
        s_h="मंज़िल पता है?", s_sub="रास्ता हम दिखाएँगे।",
        b_h1='आपका फ़ाइनेंशियल प्लान <span class="o">किन बातों का ध्यान रखता है?</span>',
        b_items=[("लक्ष्य", "घर, पढ़ाई, शादी, रिटायरमेंट"), ("बीमा", "परिवार की सुरक्षा"),
                 ("निवेश", "सही मिश्रण, सही समय"), ("टैक्स", "हर साल समझदारी से बचत")]),
}


def icon(t, a=O, b=N, key="icon"):
    return ICON[t.get(key, t["icon"])](a, b)


# ---------------------------------------------------------------- fronts
def front(t):
    kind, pal = t["front"]
    bg, ink, acc, soft, chip = PAL[pal]
    ia, ib = (("#fff", N) if pal == "orange" else (O, "#fff") if pal in ("navy", "ink") else (O, N))
    base = f"""
.kick {{ font-size:21px; font-weight:700; color:{soft}; }}
.t1 {{ font-size:42px; color:{ink}; }} .t2 {{ font-size:42px; color:{acc}; }}
.sub {{ font-size:19px; font-weight:600; color:{soft}; margin-top:6px; }}
.row {{ position:absolute; bottom:14px; display:flex; align-items:center; justify-content:space-between; color:{ink}; }}
.row .call .ico {{ color:{'#fff' if pal == 'orange' else 'var(--orange)'}; }}
.vis {{ position:absolute; }}
"""
    copy = (f'<div class="kick">{t["kick"]}</div><div class="t1 d">{t["h1"]}</div><div class="t2 d">{t["h2"]}</div>'
            f'<div class="sub">{t["sub"]}</div>')
    row = f'<div class="row">{logo(34, chip=chip)}{call(42)}</div>'
    if kind == "A":  # visual left
        css = base + ".vis { left:70px; top:30px; width:240px; height:240px; } .copy { position:absolute; left:380px; right:60px; top:22px; } .row { left:380px; right:60px; }"
        html = f'<div class="vis">{icon(t, ia, ib)}</div><div class="copy">{copy}</div>{row}'
    elif kind == "D":  # visual right
        css = base + ".vis { right:70px; top:34px; width:230px; height:230px; } .copy { position:absolute; left:60px; right:380px; top:22px; } .row { left:60px; right:380px; }"
        html = f'<div class="copy">{copy}</div><div class="vis">{icon(t, ia, ib)}</div>{row}'
    elif kind == "C":  # big stat left
        css = base + f"""
.stat {{ position:absolute; left:60px; top:36px; width:420px; }}
.stat .v {{ font-family:var(--sans); font-weight:800; font-size:70px; line-height:1; color:{acc}; white-space:nowrap; }}
.stat .l {{ font-size:20px; font-weight:700; color:{ink}; margin-top:12px; }}
.vis {{ left:330px; top:150px; width:110px; height:110px; opacity:.95; }}
.copy {{ position:absolute; left:540px; right:60px; top:22px; }} .row {{ left:540px; right:60px; }}
.bar {{ position:absolute; left:500px; top:40px; bottom:40px; width:5px; background:{acc}; }}"""
        html = (f'<div class="stat"><div class="v">{t["stat"]}</div><div class="l">{t["stat_l"]}</div></div>'
                f'<div class="bar"></div><div class="copy">{copy}</div>{row}')
    else:  # B split
        css = base + """
.lh { position:absolute; left:0; top:0; bottom:0; width:48%; background:var(--orange); padding:44px 40px 0 60px; }
.rh { position:absolute; right:0; top:0; bottom:0; width:52%; background:var(--navy); padding:44px 60px 0 70px; }
.lh .kick { color:rgba(255,255,255,.92); } .lh .t1 { color:#fff; font-size:44px; margin-top:6px; }
.rh .t2 { color:#fff; font-size:44px; } .rh .t2 span { color:var(--orange); }
.rh .sub { color:rgba(255,255,255,.85); }
.vis { left:60px; bottom:18px; width:110px; height:110px; }
.row { left:calc(48% + 70px); right:60px; color:#fff; }
.or { position:absolute; left:48%; top:50%; transform:translate(-50%,-50%); width:72px; height:72px; border-radius:50%;
  background:#fff; color:var(--navy); font-size:28px; font-weight:800; display:flex; align-items:center; justify-content:center; }"""
        html = (f'<div class="lh"><div class="kick">{t["kick"]}</div><div class="t1 d">{t["h1"]}</div></div>'
                f'<div class="rh"><div class="t2 d"><span>{t["h2"]}</span></div><div class="sub">{t["sub"]}</div></div>'
                f'<div class="vis">{icon(t, "#fff", N)}</div><div class="or">&rarr;</div>'
                f'<div class="row">{logo(32, chip=True)}{call(40)}</div>')
    return dict(bg=bg, note=bool(t["note"]), css=css, html=html)


# ---------------------------------------------------------------- sides
def side(t):
    kind, pal = t["side"]
    bg, ink, acc, soft, chip = PAL[pal]
    ia, ib = (("#fff", N) if pal == "orange" else (O, "#fff") if pal in ("navy", "ink") else (O, N))
    cta = side_cta("hi", t["msg"], color=ink if pal != "orange" else "#fff",
                   icon="var(--navy)" if pal == "orange" else "var(--orange)")
    css = f"""
.lk {{ position:absolute; left:24px; top:18px; }}
.vis {{ position:absolute; right:22px; top:58px; width:92px; height:92px; }}
.sh {{ position:absolute; left:24px; right:24px; top:66px; color:{ink}; font-size:33px; }}
.ss {{ position:absolute; left:24px; right:24px; color:{acc}; font-size:21px; font-weight:700; }}
"""
    html = f'<div class="lk">{lockup(22, chip=chip)}</div>'
    if kind == "A":
        css += ".sh { right:130px; } .ss { top:166px; }"
        html += (f'<div class="vis">{icon(t, ia, ib, "s_icon" if "s_icon" in t else "icon")}</div>'
                 f'<div class="sh d">{t["s_h"]}</div><div class="ss">{t["s_sub"]}</div>')
    elif kind == "B":
        css += f""".big {{ position:absolute; left:22px; right:20px; top:60px; color:{acc}; font-family:var(--sans); font-weight:800;
  font-size:58px; line-height:1.05; white-space:nowrap; }}
.cap {{ position:absolute; left:24px; right:24px; top:138px; color:{ink}; font-size:20px; font-weight:700; line-height:1.3; }}"""
        html += f'<div class="big">{t["s_big"]}</div><div class="cap">{t["s_h"]}</div>'
    else:  # C checklist
        rows = "".join(f'<div class="ck"><span class="m">{m}</span><span>{x}</span></div>' for m, x in t["s_list"])
        css += f""".sh {{ top:54px; font-size:25px; }}
.cks {{ position:absolute; left:24px; right:24px; top:92px; }}
.ck {{ display:flex; align-items:center; gap:12px; font-size:18px; font-weight:700; color:{ink}; padding:2px 0; }}
.ck .m {{ width:26px; height:26px; flex:none; border-radius:50%; background:{acc}; color:{'var(--navy)' if pal == 'orange' else '#fff'};
  display:flex; align-items:center; justify-content:center; font-size:17px; font-weight:800; font-family:'DM Sans', sans-serif; }}
.ck:last-child {{ color:{acc}; }}"""
        html += f'<div class="sh d">{t["s_h"]}</div><div class="cks">{rows}</div>'
    return dict(bg=bg, note=bool(t["note"]), css=css, html=html + cta)


# ---------------------------------------------------------------- backdrops
def back(t):
    kind, pal = t["back"]
    bg, ink, acc, soft, chip = PAL[pal]
    dark = pal in ("navy", "ink", "orange")
    card_bg = "rgba(255,255,255,.08)" if pal in ("navy", "ink") else "#fff" if pal in ("cream", "orange") else "var(--cream)"
    card_ink = "#fff" if pal in ("navy", "ink") else "var(--navy)"
    card_soft = "rgba(255,255,255,.78)" if pal in ("navy", "ink") else "var(--muted)"
    cta_bg = "#fff" if dark else "var(--navy)"
    cta_ink = "var(--navy)" if dark else "#fff"
    css = f"""
.lg {{ position:absolute; left:44px; top:24px; }}
.h1 {{ position:absolute; left:44px; right:330px; top:84px; color:{ink}; font-size:36px; }}
.h1 .o {{ color:{acc if pal != 'orange' else 'var(--navy)'}; }}
.cta {{ position:absolute; right:0; top:0; bottom:0; width:280px; background:{cta_bg}; color:{cta_ink}; display:flex;
  flex-direction:column; align-items:center; justify-content:center; gap:14px; }}
.cta .call .ico {{ color:var(--orange); }}
.bs {{ position:absolute; left:44px; right:330px; bottom:20px; color:{soft}; font-size:16px; font-weight:600; }}
.card {{ background:{card_bg}; border-radius:12px; color:{card_ink}; }}
.card .a {{ font-weight:800; font-size:20px; }} .card .b {{ font-size:15px; color:{card_soft}; margin-top:3px; }}
"""
    html = (f'<div class="lg">{lockup(38, chip=chip)}</div><div class="h1 d">{t["b_h1"]}</div>'
            f'<div class="cta">{qr_block("hi", t["msg"], 128, 14, label_color="inherit")}{call(26)}</div>')
    if kind == "steps":
        cards = "".join(f'<div class="card st"><div class="n">{i + 1}</div><div><div class="a">{a}</div><div class="b">{b}</div></div></div>'
                        + ('<div class="ar">&rarr;</div>' if i < 2 else "") for i, (a, b) in enumerate(t["b_items"]))
        css += f""".row3 {{ position:absolute; left:44px; right:330px; top:170px; display:flex; align-items:center; gap:10px; }}
.st {{ flex:1; display:flex; gap:12px; align-items:center; padding:16px 14px; }}
.st .n {{ width:44px; height:44px; flex:none; border-radius:50%; background:var(--orange); color:#fff; font-size:24px; font-weight:800;
  display:flex; align-items:center; justify-content:center; font-family:'DM Sans', sans-serif; }}
.ar {{ color:{acc}; font-size:26px; font-weight:800; }}"""
        html += f'<div class="row3">{cards}</div>'
    elif kind == "tiles":
        cards = "".join(f'<div class="card tl"><div class="a d">{a}</div><div class="b">{b}</div></div>' for a, b in t["b_items"])
        css += """.row3 { position:absolute; left:44px; right:330px; top:148px; display:flex; gap:14px; }
.tl { flex:1; padding:12px 18px; border-top:6px solid var(--navy); }
.tl:last-child { border-top-color:var(--orange); } .tl .a { font-size:28px; white-space:nowrap; }
.tl:last-child .a { color:var(--orange); }"""
        html += f'<div class="row3">{cards}</div>'
    elif kind == "grid":
        cards = "".join(f'<div class="card gd"><div class="ck">&#10003;</div><div><div class="a">{a}</div><div class="b">{b}</div></div></div>'
                        for a, b in t["b_items"])
        css += """.grid { position:absolute; left:44px; right:330px; top:136px; display:grid; grid-template-columns:1fr 1fr; gap:10px 16px; }
.gd { display:flex; gap:12px; align-items:center; padding:8px 14px; }
.gd .ck { width:32px; height:32px; flex:none; border-radius:50%; background:var(--orange); color:#fff; font-weight:800;
  font-size:18px; display:flex; align-items:center; justify-content:center; }"""
        html += f'<div class="grid">{cards}</div>'
    else:  # compare
        (la, li), (ra, ri) = t["b_cols"]
        lis = lambda xs, m: "".join(f'<li><span class="m">{m}</span>{x}</li>' for x in xs)
        css += f""".cmp {{ position:absolute; left:44px; right:330px; top:148px; display:flex; gap:16px; }}
.col {{ flex:1; padding:14px 18px; }}
.col h3 {{ font-size:20px; font-weight:800; margin-bottom:6px; }}
.col ul {{ list-style:none; }} .col li {{ font-size:17px; padding:3px 0; display:flex; gap:10px; align-items:center; }}
.col .m {{ width:22px; height:22px; flex:none; border-radius:50%; display:flex; align-items:center; justify-content:center;
  font-size:13px; font-weight:800; font-family:'DM Sans', sans-serif; }}
.col.l {{ opacity:.9; }} .col.l .m {{ background:var(--lmuted); color:#fff; }}
.col.r {{ background:var(--orange); color:#fff; }} .col.r .m {{ background:#fff; color:var(--orange); }}"""
        html += (f'<div class="cmp"><div class="card col l"><h3>{la}</h3><ul>{lis(li, "&times;")}</ul></div>'
                 f'<div class="card col r"><h3>{ra}</h3><ul>{lis(ri, "&#10003;")}</ul></div></div>')
    if t.get("b_sub"):
        html += f'<div class="bs">{t["b_sub"]}</div>'
    return dict(bg=bg, note=bool(t["note"]), css=css, html=html)
