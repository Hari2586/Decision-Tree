"""Builds themed campaign panels (SIP, Retirement, Child Education, ELSS) for the bus stop.

Each theme gets a 4x4 side panel and a 12x4 backdrop, written to themes/.
Reuses the brand pieces from build.py. Scale: 100px = 1 foot.
"""
from build import (HERE, LOGO, QR, PHONE_ICON, PHONE_DISPLAY, DISCLAIMER, page, services_html)

OUT = HERE / "themes"

def T(**kw):
    kw.setdefault("ops", ["+", "="])
    return kw


SIP_NOTE = ("*Illustration at an assumed 12% p.a. return for understanding only. Mutual funds do not guarantee "
            "returns; actual returns may be higher or lower.")
SIP_SNOTE = "*Illustration at assumed 12% p.a. Not a guaranteed return."
ELSS_NOTE = ("*Under the old tax regime, 30% slab plus 4% cess, on &#8377;1.5 lakh invested. Tax benefits as per "
             "current laws, subject to change. ELSS is subject to market risk.")
ELSS_SNOTE = "*Old tax regime, 30% slab + 4% cess. ELSS has market risk."

# One campaign per month, keyed so files sort in calendar order.
THEMES = {
    "01-jan-new-year-sip": T(
        side_pre="New year. New habit.",
        side_stat="&#8377;50 lakh<sup>*</sup>",
        side_caption="is what &#8377;5,000 a month can grow to in 20 years with a SIP.",
        cta="Ask for your free SIP plan",
        back_pre="This year&rsquo;s best resolution",
        back_h1='Small steps today.<br><span class="o">A big destination tomorrow.</span>',
        tiles=[("&#8377;5,000", "every month in a SIP"), ("20 years", "of staying invested"),
               ("&asymp; &#8377;50 lakh<sup>*</sup>", "you invest only &#8377;12 lakh")],
        ops=["&times;", "="],
        back_line="Start with any amount. Compounding works best when you start early.",
        snap="Take a photo. Start your SIP with one call.",
        note=SIP_NOTE, side_note=SIP_SNOTE),
    "02-feb-elss-tax-saving": T(
        side_pre="Paying too much tax?",
        side_stat="&#8377;46,800<sup>*</sup>",
        side_caption="is how much tax you can save a year with ELSS under Section 80C.",
        cta="Get a free tax-saving check",
        back_pre="Tax season is here",
        back_h1='Save tax.<br><span class="o">Grow wealth. At the same time.</span>',
        tiles=[("&#8377;1.5 lakh", "invested in ELSS"), ("Section 80C", "deduction claimed"),
               ("&#8377;46,800<sup>*</sup>", "tax saved in a year")],
        back_line="Only a 3-year lock-in: the shortest among 80C options.",
        snap="Take a photo. Save tax with one call.",
        note=ELSS_NOTE, side_note=ELSS_SNOTE),
    "03-mar-elss-last-call": T(
        side_pre="Last call for tax saving",
        side_stat="31 March",
        side_caption="is the last day to save up to &#8377;46,800<sup>*</sup> tax with ELSS this year.",
        cta="Call before the deadline",
        back_pre="The tax year ends on 31 March",
        back_h1='Don&rsquo;t pay tax you could have saved.<br><span class="o">There&rsquo;s still time. Just.</span>',
        tiles=[("ELSS", "tax-saving mutual fund"), ("Before 31 March", "invest up to &#8377;1.5 lakh"),
               ("&#8377;46,800<sup>*</sup>", "tax saved in a year")],
        back_line="We&rsquo;ll help you finish your tax-saving investment quickly and correctly.",
        snap="Take a photo. Call before 31 March.",
        note=ELSS_NOTE, side_note=ELSS_SNOTE),
    "04-apr-step-up-sip": T(
        side_pre="Got a raise this April?",
        side_stat="&#8377;99 lakh<sup>*</sup>",
        side_caption="from a &#8377;5,000 SIP raised 10% every year, in 20 years.",
        cta="Step up your SIP today",
        back_pre="New financial year. New salary.",
        back_h1='Your salary grew.<br><span class="o">Let your SIP grow with it.</span>',
        tiles=[("&#8377;5,000", "monthly SIP to start"), ("+10% a year", "step-up for 20 years"),
               ("&asymp; &#8377;99 lakh<sup>*</sup>", "vs &asymp; &#8377;50 lakh without step-up")],
        back_line="A small yearly top-up can almost double your final corpus.",
        snap="Take a photo. Step up your SIP with one call.",
        note=SIP_NOTE, side_note=SIP_SNOTE),
    "05-may-fixed-income": T(
        side_pre="FD maturing soon?",
        side_stat="5 options",
        side_caption="FDs, Debentures, Gov. Bonds, Capital Gain Bonds and Debt Funds, compared for you.",
        cta="Get a free comparison",
        back_pre="Before you renew that FD",
        back_h1='Compare before you reinvest.<br><span class="o">One call. Every option.</span>',
        tiles=[("FDs &amp; Debentures", "fixed-income choices"), ("Gov. Bonds", "backed by the government"),
               ("Your best fit", "for income, safety and tax")],
        back_line="We explain the interest, lock-in and tax of each, in plain language.",
        snap="Take a photo. Compare your options with one call.",
        note="*Returns, safety and tax treatment differ across products. Debt funds are subject to market risk; "
             "read all offer documents carefully.",
        side_note="*Features differ by product. Debt funds have market risk."),
    "06-jun-child-education": T(
        side_pre="Your child&rsquo;s dream college?",
        side_stat="&#8377;84 lakh<sup>*</sup>",
        side_caption="is what a &#8377;20 lakh degree today may cost in 15 years.",
        cta="Get a free education plan",
        back_pre="Schools reopen. Dreams grow.",
        back_h1='They dream big.<br><span class="o">Let&rsquo;s make sure money never stops them.</span>',
        tiles=[("&#8377;20 lakh", "a degree costs today"), ("15 years", "of 10% education inflation"),
               ("&asymp; &#8377;84 lakh<sup>*</sup>", "needed when they&rsquo;re 18")],
        back_line="Start a goal-based plan today, so the fees are ready on time.",
        snap="Take a photo. Plan their future with one call.",
        note="*Illustration at an assumed 10% p.a. education cost inflation for understanding only. "
             "Actual costs may differ.",
        side_note="*Illustration at an assumed 10% p.a. education inflation."),
    "07-jul-emergency-fund": T(
        side_pre="Is your money monsoon-ready?",
        side_stat="6 months",
        side_caption="of expenses: the emergency fund every family should keep ready.",
        cta="Build your rainy-day fund",
        back_pre="Save for a rainy day",
        back_h1='Job loss. Hospital bill. Urgent repair.<br><span class="o">Be ready before it rains.</span>',
        tiles=[("&#8377;40,000", "monthly expenses"), ("6 months", "of cover"),
               ("&#8377;2.4 lakh<sup>*</sup>", "your emergency fund")],
        ops=["&times;", "="],
        back_line="Keep it safe, easy to withdraw, and separate from your long-term money.",
        snap="Take a photo. Plan your safety net with one call.",
        note="*Example for illustration only. Your emergency fund depends on your own expenses and needs.",
        side_note="*Amount depends on your own monthly expenses."),
    "08-aug-retirement-freedom": T(
        side_pre="This Independence Day",
        side_stat="&#8377;1.6 lakh<sup>*</sup>",
        side_caption="a month is what today&rsquo;s &#8377;50,000 expenses may cost you in 20 years.",
        cta="Get a free retirement check",
        back_pre="Plan your financial freedom",
        back_h1='Your salary stops one day. Your expenses don&rsquo;t.<br><span class="o">Is your retirement ready?</span>',
        tiles=[("&#8377;50,000", "monthly expenses today"), ("20 years", "of 6% inflation"),
               ("&#8377;1.6 lakh<sup>*</sup>", "needed every month")],
        back_line="Build a retirement corpus that pays you every month, like a salary.",
        snap="Take a photo. Plan your retirement with one call.",
        note="*Illustration at an assumed 6% p.a. inflation for understanding only. Actual inflation may differ.",
        side_note="*Illustration at an assumed 6% p.a. inflation."),
    "09-sep-capital-gain-bonds": T(
        side_pre="Sold a property?",
        side_stat="6 months",
        side_caption="is all you have to save capital gains tax with 54EC bonds.<sup>*</sup>",
        cta="Ask about 54EC bonds",
        back_pre="Sold land or a building?",
        back_h1='Don&rsquo;t lose your profit to tax.<br><span class="o">Section 54EC can help.</span>',
        tiles=[("Property gain", "long-term, land or building"), ("6 months", "to invest in 54EC bonds"),
               ("Tax saved<sup>*</sup>", "on up to &#8377;50 lakh a year")],
        back_line="Government-backed issuers. 5-year lock-in. We handle the paperwork.",
        snap="Take a photo. Save capital gains tax with one call.",
        note="*Section 54EC: exemption on long-term capital gains from land or building, investment up to "
             "&#8377;50 lakh per financial year, 5-year lock-in. Tax benefits as per current laws, subject to change.",
        side_note="*Sec 54EC, up to &#8377;50 lakh per year, 5-year lock-in."),
    "10-oct-diwali-gift-sip": T(
        side_pre="This Diwali, gift a future",
        side_stat="&#8377;15 lakh<sup>*</sup>",
        side_caption="from a &#8377;2,000 monthly SIP gifted from birth till your child turns 18.",
        cta="Gift a SIP this Diwali",
        back_pre="A gift that keeps growing",
        back_h1='Sweets finish. Toys break.<br><span class="o">A SIP keeps growing for 18 years.</span>',
        tiles=[("&#8377;2,000", "monthly SIP from birth"), ("18 years", "of growing together"),
               ("&asymp; &#8377;15 lakh<sup>*</sup>", "you invest only &#8377;4.3 lakh")],
        ops=["&times;", "="],
        back_line="Start a SIP in your child&rsquo;s name this festive season.",
        snap="Take a photo. Gift a SIP with one call.",
        note=SIP_NOTE, side_note=SIP_SNOTE),
    "11-nov-bonus-lump-sum": T(
        side_pre="Got a festive bonus?",
        side_stat="&#8377;5.5 lakh<sup>*</sup>",
        side_caption="is what a &#8377;1 lakh bonus invested today can grow to in 15 years.",
        cta="Invest your bonus wisely",
        back_pre="Don&rsquo;t let your bonus disappear",
        back_h1='Spend a little. Invest the rest.<br><span class="o">Let your bonus work for you.</span>',
        tiles=[("&#8377;1 lakh", "bonus invested once"), ("15 years", "of staying invested"),
               ("&asymp; &#8377;5.5 lakh<sup>*</sup>", "your bonus, grown")],
        ops=["&times;", "="],
        back_line="Lump sum or step-by-step (STP): we&rsquo;ll help you choose.",
        snap="Take a photo. Invest your bonus with one call.",
        note=SIP_NOTE, side_note=SIP_SNOTE),
    "12-dec-portfolio-review": T(
        side_pre="Year-end check-up",
        side_stat="&#8377;0",
        side_caption="is what our portfolio review costs. Know where your money stands.",
        cta="Book your free review",
        back_pre="The year is ending. Is your money on track?",
        back_h1='You get a health check every year.<br><span class="o">Does your money?</span>',
        tiles=[("Your money", "FDs, funds, bonds, all of it"), ("Free review", "with an expert"),
               ("A clear plan", "for the year ahead")],
        back_line="Bring your statements. Leave with clarity, and no obligation.",
        snap="Take a photo. Book your free review with one call.",
        note="*Free, no-obligation portfolio review. Recommendations depend on your goals and risk profile.",
        side_note="*Free, no-obligation portfolio review."),
}

# ---------------------------------------------------------------- SIDE 4x4
SIDE_CSS = """
.banner { display:flex; flex-direction:column; }
.top { height:66px; display:flex; align-items:center; justify-content:center; background:#fff;
  border-bottom:5px solid var(--orange); flex:none; }
.top .logo { height:46px; }
.body { flex:1; min-height:0; background:var(--navy); color:#fff; padding:16px 26px 0; display:flex; flex-direction:column; }
.pre { font-size:15px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--orange); }
.stat { font-family:'Lora',serif; font-weight:700; font-size:54px; line-height:1; margin-top:8px; color:#fff; white-space:nowrap; }
.stat sup { font-size:.4em; color:var(--orange); vertical-align:top; position:relative; top:.25em; }
.cap { font-size:16px; line-height:1.28; margin-top:6px; color:rgba(255,255,255,.9); }
.cap sup { color:var(--orange); }
.pill { align-self:flex-start; background:var(--orange); color:#fff; font-weight:800; font-size:14px;
  letter-spacing:.06em; text-transform:uppercase; padding:5px 14px; border-radius:40px; margin-top:8px; }
.callrow { display:flex; align-items:center; gap:14px; margin-top:auto; margin-bottom:5px; }
.qr { width:74px; height:74px; padding:5px; border-radius:6px; flex:none; }
.call .lbl { font-size:13px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--orange); }
.call .num { font-size:30px; font-weight:800; line-height:1.05; white-space:nowrap; }
.call .num .ico { color:var(--orange); }
.call .scan { font-size:12px; color:rgba(255,255,255,.75); margin-top:2px; }
.snote { font-size:8.4px; color:rgba(255,255,255,.7); margin-bottom:5px; }
.foot { background:var(--orange); color:#fff; padding:4px 10px 5px; text-align:center; flex:none; }
.foot .amfi { font-size:10.5px; font-weight:700; white-space:nowrap; }
.foot .disc { font-size:7.2px; margin-top:1px; }
"""


def side(t):
    return f"""
<div class="top"><img class="logo" src="data:image/png;base64,{LOGO}" alt="MoneyHoney"></div>
<div class="body">
  <div class="pre">{t['side_pre']}</div>
  <div class="stat">{t['side_stat']}</div>
  <div class="cap">{t['side_caption']}</div>
  <div class="pill">{t['cta']}</div>
  <div class="callrow">
    <div class="qr">{QR}</div>
    <div class="call">
      <div class="lbl">Call now</div>
      <div class="num">{PHONE_ICON} {PHONE_DISPLAY[4:]}</div>
      <div class="scan">Scan the code to call &bull; +91</div>
    </div>
  </div>
  <div class="snote">{t['side_note']}</div>
</div>
<div class="foot">
  <div class="amfi">AMFI Registered Mutual Fund Distributor | ARN NO-60930 | Since 2008</div>
  <div class="disc">Mutual Fund investments are subject to market risks, read all scheme related documents carefully.</div>
</div>
"""


# ---------------------------------------------------------------- BACKDROP 12x4
BACK_CSS = """
.banner { background:var(--cream); display:grid; grid-template-columns: minmax(0,1fr) 360px; grid-template-rows: 1fr 62px; }
.main { grid-column:1; grid-row:1; padding:22px 36px 0 40px; display:flex; flex-direction:column; min-height:0; }
.head { display:flex; align-items:center; justify-content:space-between; }
.head .logo { height:50px; }
.head .tagline { font-size:15px; text-align:right; }
.head .trusted { font-size:15px; text-align:right; }
.pre { font-size:14px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:var(--muted); margin-top:8px; }
h1 { font-family:'Lora',serif; font-weight:700; font-size:31px; line-height:1.1; margin-top:3px; }
.eq { display:flex; align-items:stretch; gap:10px; margin-top:10px; }
.tile { flex:1; min-width:0; background:#fff; border-radius:10px; padding:10px 14px; box-shadow:0 2px 8px rgba(27,38,102,.06);
  border-top:5px solid var(--navy); }
.tile.last { border-top-color:var(--orange); background:var(--navy); color:#fff; }
.tile .v { font-family:'Lora',serif; font-weight:700; font-size:27px; line-height:1.05; white-space:nowrap; }
.tile.last .v { color:#fff; }
.tile .v sup { font-size:.45em; color:var(--orange); }
.tile .l { font-size:13px; color:var(--muted); margin-top:3px; }
.tile.last .l { color:rgba(255,255,255,.85); }
.op { font-family:'Lora',serif; font-weight:700; font-size:40px; color:var(--orange); align-self:center; }
.line { font-size:15px; font-weight:500; margin-top:8px; }
.bottom { margin-top:auto; margin-bottom:6px; }
.note { font-size:10.5px; color:var(--muted); line-height:1.3; }
.amfi { font-size:12.5px; margin-top:3px; }
.amfi b { font-weight:800; }
.side { grid-column:2; grid-row:1; background:var(--navy); color:#fff; padding:24px 26px 0; display:flex;
  flex-direction:column; align-items:center; text-align:center; }
.side .pill { background:var(--orange); color:#fff; font-weight:800; font-size:15px; letter-spacing:.06em;
  text-transform:uppercase; padding:7px 16px; border-radius:40px; }
.side .num { font-size:40px; font-weight:800; margin-top:12px; white-space:nowrap; }
.side .num .ico { color:var(--orange); }
.side .qr { width:112px; height:112px; padding:8px; border-radius:8px; margin-top:10px; }
.side .scan { font-size:14px; margin-top:6px; }
.side .scan b { color:var(--orange); }
.side .snap { font-size:14px; margin-top:auto; margin-bottom:12px; color:rgba(255,255,255,.8); }
.strip { grid-column:1 / 3; grid-row:2; background:var(--orange); color:#fff; display:flex; flex-direction:column;
  justify-content:center; }
.strip .services { font-size:21px; font-weight:700; gap:16px; }
.strip .services .sep { color:rgba(255,255,255,.7); }
.disc { font-size:7.6px; text-align:center; margin-top:2px; padding:0 20px; }
"""


def backdrop(t):
    tiles = []
    for i, (v, l) in enumerate(t["tiles"]):
        if i:
            tiles.append(f'<div class="op">{t["ops"][i - 1]}</div>')
        last = " last" if i == len(t["tiles"]) - 1 else ""
        tiles.append(f'<div class="tile{last}"><div class="v">{v}</div><div class="l">{l}</div></div>')
    return f"""
<div class="main">
  <div class="head">
    <img class="logo" src="data:image/png;base64,{LOGO}" alt="MoneyHoney">
    <div><div class="tagline">Think Big &bull; Act Fast</div><div class="trusted">(Trusted Since 2008)</div></div>
  </div>
  <div class="pre">{t['back_pre']}</div>
  <h1>{t['back_h1']}</h1>
  <div class="eq">{''.join(tiles)}</div>
  <div class="line">{t['back_line']}</div>
  <div class="bottom">
    <div class="note">{t['note']}</div>
    <div class="amfi">AMFI Registered Mutual Fund Distributor &nbsp;<span class="o">|</span>&nbsp; <b>ARN NO-60930</b></div>
  </div>
</div>
<div class="side">
  <div class="pill">{t['cta']}</div>
  <div class="num">{PHONE_ICON} {PHONE_DISPLAY[4:]}</div>
  <div class="qr">{QR}</div>
  <div class="scan"><b>Scan to call</b> &bull; +91 77380 32704</div>
  <div class="snap">{t['snap']}</div>
</div>
<div class="strip">
  <div class="services">{services_html()}</div>
  <div class="disc">{DISCLAIMER}</div>
</div>
"""


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for key, t in THEMES.items():
        label = key.replace("-", " ").title()
        (OUT / f"{key}-side-4x4.html").write_text(page(f"MoneyHoney {label} Side", 400, 400, SIDE_CSS, side(t)))
        (OUT / f"{key}-backdrop-12x4.html").write_text(
            page(f"MoneyHoney {label} Backdrop", 1200, 400, BACK_CSS, backdrop(t)))
        print("wrote", key)
