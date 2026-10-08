# MoneyHoney redesign: Phase 1 content inventory

Status: Phases 1 to 5 complete for the home page. Chosen design direction: B, "Clear Glass". Final page at `redesign/site/index.html`.

Source: uploaded `index.html` (home page). Captured 8 Oct 2026.
Scope note: only the home page was supplied. It links to 45 sub-pages (solutions, mutual funds, SIF, FDs, bonds, calculators, about, contact, etc.) whose HTML was not attached. Those pages are listed under "Linked pages not supplied" and are NOT inventoried.

Every row below is the exact text as it appears in the source. `&amp;` is shown as `&`, `&middot;` as `·`.
Rows tagged **[COMPLIANCE]** are regulatory or disclaimer text and must remain verbatim and visible.

---

## 0. Document head (not visible on page, must carry over)

| # | Element | Exact text |
|---|---|---|
| H1 | `<html lang>` | `en-IN` |
| H2 | `<title>` | MoneyHoney: Mutual Funds, SIFs, Screens and Calculators |
| H3 | meta description | Facts on 1,774 mutual fund schemes from 48 fund houses, plus SIF strategies, calculators and rule-based fund screens, as on 31 Aug 2026. |
| H4 | canonical | https://example.com/ |
| H5 | og:site_name | MoneyHoney |
| H6 | og:locale | en_IN |
| H7 | og:title | MoneyHoney: Mutual Funds, SIFs, Screens and Calculators |
| H8 | og:description | (same as H3) |
| H9 | og:url | https://example.com/ |
| H10 | og:image | https://example.com/assets/og/home.png (1200 x 630) |
| H11 | og:image:alt | MoneyHoney: Mutual Funds, SIFs and Calculators |
| H12 | twitter:card | summary_large_image |
| H13 | JSON-LD WebPage name | Mutual Funds, SIFs, Screens and Calculators |
| H14 | JSON-LD WebPage dateModified | 2026-10-05 |
| H15 | JSON-LD WebSite name | MoneyHoney |
| H16 | JSON-LD Organization name | MoneyHoney |
| H17 | JSON-LD Organization description **[COMPLIANCE]** | AMFI Registered Mutual Fund Distributor & SIF Distributor, ARN-000000 |

## 1. Demo notice strip (top of page)

| # | Element | Exact text |
|---|---|---|
| D1 | Note, bold lead word **[COMPLIANCE]** | **Demo.** Demo site for review. The registration details (ARN, CIN), commission rates, the sample IDCW Explorer and Screener analytics are placeholders or illustrations. This is not a live distributor website and not for investment decisions. |

## 2. Header

| # | Element | Exact text | Link target |
|---|---|---|---|
| N0 | Logo (inline SVG, 139 x 20), link aria-label | MoneyHoney home | ./index.html |
| N0a | Logo SVG aria-label | MoneyHoney | |
| N1 | Nav link | Solutions | solutions/index.html |
| N2 | Nav link | Mutual Funds | mutual-funds/index.html |
| N3 | Nav link | SIF | sif/index.html |
| N4 | Nav link | Fixed Deposits | fixed-deposits/index.html |
| N5 | Nav link | Bonds & NCDs | bonds/index.html |
| N6 | Nav link | Explore Funds | mutual-funds/explore/index.html |
| N7 | Nav link | Fund Screens | mutual-funds/screens/index.html |
| N8 | Nav link | Calculators | calculators/index.html |
| N9 | Nav link | NFOs & Dividends | mutual-funds/nfo/index.html |

Nav `aria-label`: Main.

## 3. Main: page head and intro

| # | Element | Exact text |
|---|---|---|
| M1 | H1 | Mutual Funds, SIFs, Screens and Calculators |
| M2 | Lede paragraph (contains a regulatory sentence) **[COMPLIANCE, last sentence]** | Facts on every open mutual fund scheme in India, organised by fund house, SEBI category, theme and index, with Specialised Investment Fund (SIF) strategies, calculators and rule-based fund screens. MoneyHoney is an AMFI-registered mutual fund and SIF distributor; nothing here is a recommendation. |

## 4. Main: fact tiles

| # | Label | Value |
|---|---|---|
| F1 | Mutual Fund Schemes | 1,774 |
| F2 | Fund Houses | 48 |
| F3 | SEBI Categories | 39 |
| F4 | Data As On | 31 Aug 2026 |

## 5. Main: Find a Solution

| # | Element | Exact text | Link target |
|---|---|---|---|
| S0 | H2 | Find a Solution | |
| S0a | Paragraph | Start from the problem you want to solve. | |
| S0b | Inline link inside S0a | See All Solutions | solutions/index.html |
| S1 | List link | SIP | solutions/sip/index.html |
| S2 | List link | Retirement | solutions/retirement/index.html |
| S3 | List link | Child Education | solutions/child-education/index.html |
| S4 | List link | Women and Money | solutions/women/index.html |
| S5 | List link | NRI Investing | solutions/nri/index.html |
| S6 | List link | Trusts | solutions/trusts/index.html |
| S7 | List link | Building Wealth | solutions/wealth/index.html |
| S8 | List link | Vacation Planning | solutions/vacation/index.html |
| S9 | List link | Marriage Planning | solutions/marriage/index.html |
| S10 | List link | EMI Management | solutions/emi-management/index.html |
| S11 | List link | Emergency Fund | solutions/emergency-fund/index.html |

## 6. Main: Start Here (link cards)

| # | Card title | Card meta text | Link target |
|---|---|---|---|
| C0 | H2 | Start Here | |
| C1 | Mutual Funds | 1,774 schemes by category and fund house | mutual-funds/index.html |
| C2 | Explore Funds | Filter every scheme by category, cost and risk | mutual-funds/explore/index.html |
| C3 | Fund Screens | Rule-based lists such as index funds under 0.50% cost | mutual-funds/screens/index.html |
| C4 | Calculators | SIP, lumpsum, SWP, goal and tax calculators | calculators/index.html |
| C5 | New Fund Offers | Open, upcoming and recently closed NFOs | mutual-funds/nfo/index.html |
| C6 | Dividend History (IDCW) | Past IDCW record dates and amounts per unit, scheme by scheme | mutual-funds/dividend-history/index.html |
| C7 | Specialised Investment Funds | SIF strategies for investments of ₹10,00,000 or more | sif/index.html |
| C8 | NCD IPOs | Sample NCD public issues: series, ratings and how to apply | bonds/ncd/index.html |
| C9 | Capital Gain Bonds | Save tax on a property gain: REC, PFC and IRFC series | bonds/capital-gain-bonds/index.html |
| C10 | RBI Bonds | Government of India bonds, interest every six months | bonds/rbi-bonds/index.html |
| C11 | Fixed Deposits | Company and bank FDs we offer, with rates and terms for your investor type. | fixed-deposits/index.html |

Note: C11 is the only card meta ending in a full stop. Preserved as is.

## 7. Main: Mutual Funds by Asset Class (link cards)

| # | Card title | Card meta text | Link target |
|---|---|---|---|
| A0 | H2 | Mutual Funds by Asset Class | |
| A1 | Equity Funds | 11 categories, 614 schemes | mutual-funds/asset/equity/index.html |
| A2 | Debt Funds | 16 categories, 434 schemes | mutual-funds/asset/debt/index.html |
| A3 | Hybrid Funds | 6 categories, 179 schemes | mutual-funds/asset/hybrid/index.html |
| A4 | Index Funds and Other Schemes | 4 categories, 506 schemes | mutual-funds/asset/index-and-other/index.html |
| A5 | Solution Oriented Funds | 2 categories, 41 schemes | mutual-funds/asset/solution-oriented/index.html |

## 8. Main: Themes, Indices and More (link cards)

| # | Card title | Card meta text | Link target |
|---|---|---|---|
| T0 | H2 | Themes, Indices and More | |
| T1 | Sector and Theme Funds | Sector and Theme Funds: Active and Index | mutual-funds/theme/index.html |
| T2 | Factor Funds | Factor Funds: Momentum, Quality and Value | mutual-funds/theme/factor/index.html |
| T3 | Index Funds and ETFs | Equity Index Funds and ETFs by Index | mutual-funds/index-funds/index.html |
| T4 | Target Maturity Funds | Target Maturity Funds by Maturity Year | mutual-funds/target-maturity/index.html |
| T5 | Open-Ended Debt Index Funds | Open-Ended Debt Index Funds and ETFs | mutual-funds/debt-index/index.html |
| T6 | International Funds | International Funds by Region | mutual-funds/international/index.html |
| T7 | Gold and Silver | Gold and Silver ETFs and FoFs by Metal | mutual-funds/gold-silver/index.html |
| T8 | Funds of Funds | Funds of Funds by Type | mutual-funds/fund-of-funds/index.html |

## 9. Footer

| # | Element | Exact text | Link target |
|---|---|---|---|
| L1 | Footer link | About | about/index.html |
| L2 | Footer link | Contact | contact/index.html |
| L3 | Footer link | Methodology | methodology/index.html |
| L4 | Footer link | Disclaimer | disclaimer/index.html |
| L5 | Footer link | Commission Disclosure | commission-disclosure/index.html |
| L6 | Footer link | Fund Houses We Distribute | mutual-funds/amc/index.html |
| L7 | Footer link | Site Map | site-map/index.html |
| R1 | Identity line **[COMPLIANCE]** | Money Honey Financial Services Private Limited · AMFI Registered Mutual Fund Distributor & SIF Distributor · ARN-000000 · Registered 1 Jan 2015, valid till 31 Dec 2027 | |
| R2 | Risk warning **[COMPLIANCE]** | Mutual Fund investments are subject to market risks, read all scheme related documents carefully. | |
| R3 | SIF risk warning **[COMPLIANCE]** | Investments in Specialized Investment Fund involves relatively higher risk including potential loss of capital, liquidity risk and market volatility. Please read all investment strategy related documents carefully before making the investment decision. | |

Footer nav `aria-label`: Footer. Footer carries `data-nosnippet`.

---

## Compliance register (all items tagged above, in one place)

| # | Where | Exact text |
|---|---|---|
| H17 | JSON-LD | AMFI Registered Mutual Fund Distributor & SIF Distributor, ARN-000000 |
| D1 | Demo strip | Demo. Demo site for review. The registration details (ARN, CIN), commission rates, the sample IDCW Explorer and Screener analytics are placeholders or illustrations. This is not a live distributor website and not for investment decisions. |
| M2 (last sentence) | Lede | MoneyHoney is an AMFI-registered mutual fund and SIF distributor; nothing here is a recommendation. |
| R1 | Footer | Money Honey Financial Services Private Limited · AMFI Registered Mutual Fund Distributor & SIF Distributor · ARN-000000 · Registered 1 Jan 2015, valid till 31 Dec 2027 |
| R2 | Footer | Mutual Fund investments are subject to market risks, read all scheme related documents carefully. |
| R3 | Footer | Investments in Specialized Investment Fund involves relatively higher risk including potential loss of capital, liquidity risk and market volatility. Please read all investment strategy related documents carefully before making the investment decision. |

Not present on this page: EUIN, CIN number, commission rates, "Past performance" disclaimer. If they exist on sub-pages, send those pages and they will be inventoried.

## Counts

| Group | Count |
|---|---|
| Headings (h1 + h2) | 5 |
| Paragraphs | 4 (demo note, lede, solutions intro, footer identity) + 2 footer warnings |
| Fact tiles | 4 |
| Nav links (header) | 9 |
| Solution links | 11 (+1 inline "See All Solutions") |
| Link cards | 11 + 5 + 8 = 24 (each with title and meta) |
| Footer links | 7 |
| Buttons | 0 (page has no `<button>` or `.btn`; all CTAs are links) |
| Form fields | 0 |
| Images | 0 (logo is inline SVG) |
| Total distinct text strings (body) | 94 |

## Linked pages not supplied (45)

about, contact, methodology, disclaimer, commission-disclosure, site-map,
solutions (index, sip, retirement, child-education, women, nri, trusts, wealth, vacation, marriage, emi-management, emergency-fund),
mutual-funds (index, explore, screens, nfo, dividend-history, amc, index-funds, target-maturity, debt-index, international, gold-silver, fund-of-funds, theme, theme/factor, asset/equity, asset/debt, asset/hybrid, asset/index-and-other, asset/solution-oriented),
sif, fixed-deposits, bonds (index, ncd, capital-gain-bonds, rbi-bonds), calculators.

## Current design facts (for reference, not content)

- Font: Inter 400 to 600, embedded as a base64 woff2 (57 KB inline).
- Brand tokens in file: navy `#16205B`, orange `#FF4A00`. The logo SVG uses the same two values. The brief specifies navy `#1B2666` and orange `#E8511A`.
- Design-system comment: "navy does the work", orange "at most one moment per screen", page always white.
- Layout: single column, max-width container, auto-fill card grids, sticky header on desktop only, horizontal-scroll nav on mobile.
