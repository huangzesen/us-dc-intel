# SS Explorer Official — South Sudan Datacentre Enumeration via Regulator (NCA), Ministry (MICT&PS), National Data Centre, Energy, Cloud, Gateway and Operator Sources

Date: 2026-08-12 (reviewed final). Country: **SS South Sudan**. Division model: **10 states**. Angle: **official/regulatory/energy/cloud/gateway pipeline** for finding commercial, government, telecom and banking data-centre facilities.

Reliability grades:
- **A** = primary/official/legal source: NCA licence or official page, MICT&PS/NCA/state government official material, World Bank diagnostic/project documents, official operator page, official cloud-provider statement, PeeringDB API negative check.
- **B** = strong secondary source: credible local press quoting officials (Eye Radio, Radio Tamazuj, Sudans Post), established trade press (Ecofin Agency, Connecting Africa, TechAfrica News, Telecompaper), company pages for existence, reputable association pages.
- **C** = weak lead: generic market report, social post, unsupported directory entry, old MoU, marketing page.

---

## 0. South Sudan-specific structure facts

- South Sudan has **no public datacentre planning-permit register**, no state-level e-permitting portal, and **no national facility registry**. There is also **no public data-centre/colocation licence class** at the regulator: datacentre operation falls under general telecom/ICT licensing, which is why enumeration must join licensing records (NCA), ministry announcements (MICT&PS), the national data-centre project, the international gateway (SSIGW), fibre-infrastructure licences, energy context, and operator pages.
- **The regulator is the National Communication Authority (NCA), NOT “NTC”.** The parent task brief said “regulator NTC”; no entity named NTC (National Telecommunication(s) Corporation) was found for South Sudan. “NTC” in the region belongs to Sudan’s National Telecom Corporation and Pakistan’s NTC — do not confuse them with the South Sudanese NCA. See §1.
- **National Data Centre (NDC), Juba — the only countable government DC seed.** Per the Minister of ICT&Postal Services (Ateny Wek Ateny, via Eye Radio, 30 Apr 2026), construction of a **national data centre is ongoing and “halfway complete”** (capacity/location not yet published). In January 2026 the NCA formally established a **Gateway Services and Data Center Oversight Committee**, with technical support from Swiss firm MGI Communications AG, to strengthen control of gateway services and national data-centre infrastructure. The World Bank’s June 2022 diagnostic confirmed South Sudan then had **no fully functional carrier-neutral data centre and no Internet Exchange Point (IXP)**, and recommended a carrier-neutral, private-owned/managed DC doubling as an IXP in Juba to attract content caches (Akamai, Google, Meta). Treat the NDC as **B until an official MICT&PS/NCA construction, tender, commissioning, address or operator page is published**; press quoting officials is not the same as an official facility record.
- **Connectivity is fibre-thin and satellite-heavy.** First international fibre route: **Juba–Uganda (~200 km)** built by **Liquid Intelligent Technologies** under a 2020 NCA agreement; **Muya Fiber Construction** runs a parallel route. Only ~300 km of operational fibre existed as of 2020 data (Hamilton Research via World Bank Table 6); only 4% of the population lives within 10 km of a fibre node and 7% within 50 km. MICT&PS World Bank/EARDIP procurement files still describe South Sudan as lacking adequate backbone and international redundancy. In July 2025 parliament approved a budget exceeding **US$9 billion** for a national fibre-optic backbone; construction of **2,400 km** was announced to start December 2025, and the minister cited **~2,700 km** in April 2026. Zain and MTN backhaul is still mostly microwave + satellite.
- **Energy is a hard constraint.** There is **no national grid** — the AfDB Infrastructure Action Plan notes only isolated networks serving **Juba, Malakal and Wau** (plus Renk). Juba’s grid depends on the **Juba Thermal Power Station (~33 MW diesel, expansion to 100 MW planned)** operated around the **South Sudan Electricity Corporation (SSEC)**; outages are frequent and fuel supply is unreliable. Any datacentre therefore needs **on-site generation (diesel/gensets, solar hybrid) and UPS** — power evidence is a corroborating trail, not a facility record. See §4.
- **Cloud-region absence (A-negative).** AWS, Azure, Google Cloud and OCI official region lists contain **no South Sudan region** as of the methodology date. In-country connectivity comes from satellite broadband (Starlink licensed/partnered 2024) and the Juba–Uganda fibre; treat any “cloud region” claim as a service/partner lead, not a facility.
- **Conflict context is mandatory for grading.** Civil war Dec 2013–2018 (R-ARCSS 2018); renewed tension with the **Nasir clashes (Feb–Mar 2025, Upper Nile)** between SSPDF and the White Army; First Vice-President Riek Machar placed under house arrest Apr 2025; elections postponed to Dec 2026; 2025–2026 fighting in **Upper Nile and Unity** (Mayom/Koch), cattle raids in Jonglei/Warrap/Lakes, and Sudan-war spillover (refugees into Northern Bahr el Ghazal and Upper Nile). Every status claim about state-level ICT must be date-stamped and re-verified.
- **Languages**: English is the working language of government and all key official/operator pages (nca.gov.ss, mictps.gov.ss, operator sites); local press is predominantly English; Juba Arabic and Arabic appear in radio/broadcast and some official material. Use English variants (`data centre`, `data center`, `datacentre`, `server room`, `server farm`, `cloud`, `colocation`, `IXP`, `Tier`) plus Arabic (`مركز بيانات` data centre, `خوادم` servers, `استضافة` hosting, `سحابة`/`الحوسبة السحابية` cloud, `التحول الرقمي` digital transformation).
- **Digital-economy baseline**: South Sudan ranked **second-to-last on the UN E-Government Development Index (0.1191 of 1; telecom-infrastructure sub-index 0.0547)** — expect almost no e-government digital infrastructure outside Juba (Ecofin, 22 Jan 2026).

---

## 1. Grade A official regulator — National Communication Authority (NCA)

- **National Communication Authority (NCA)**: https://www.nca.gov.ss/ — established under the **National Communication Act, 2012**, fully operational June 2015; parent ministry: Ministry of Information, Communication Technology and Postal Services. HQ Juba. The NCA site and `https://www.nca.gov.ss/directorates/office-of-the-director-general` identify **Hon. Rizig Dominic Samuel** as Director General; older 2025 coverage naming Gieth Kon Mathiang Kun is historical. Directorates include Spectrum Management, Technical Services, Regulations & Enforcement, Research & Planning.
- Mandate: licensing and regulating telecommunications, broadcasting, postal and ICT service providers; spectrum and numbering; type approval and standards; universal access (via the Universal Service and Access Fund); consumer protection. 2024–2026 milestones relevant to enumeration: **Starlink partnership/licensing for national internet access (2024)** and approved Starlink tariffs; **Apr 2024 ultimatum to unlicensed satellite service providers** to register; **15-year licence with MTN South Sudan (11 Apr 2025; official MICT&PS page: `https://mictps.gov.ss/govt-inks-licence-agreement-granting-mtn-15-more-years-in-south-sudan/`)**; **EACO 30th Annual Assemblies hosted in Juba and NCA chairmanship (June 2025)**; **Jan 2026 Gateway Services and Data Center Oversight Committee** (with MGI Communications AG).
- **Licensing evidence trail** (each licence = authorisation, not a facility): national operator licences (MTN South Sudan, Zain South Sudan, Digitel Holding Ltd), regional licences (historical: Gemtel, Vivacell — Vivacell’s licence suspended Feb 2018), **satellite/VSAT licences** (Starlink et al.), **fibre-infrastructure licences** (Liquid Intelligent Technologies, Muya Fiber Construction, Nile Cable & Towers — “National Fiber Infrastructure License”), Bayobab Infra Solutions Ltd / MTN Digital Infrastructure fibre licence effective 16 Oct 2025 (`https://bayobab.africa/mtn-digital-infrastructure-secures-south-sudan-fibre-license-advancing-project-east-2-west/`), and the **SSIGW international gateway** arrangement. No public DC/colo licence class or DC registry was found on nca.gov.ss — note this absence as a finding, not a gap in research.
- **Universal Service and Access Fund (USAF)**: established 2020 as an NCA secretariat (Ministerial Order No. 8/2020), funded by **2% of ICT licensee revenue**; no implementation agency set up as of 2022 (World Bank) — USAF is a future funder of backbone/DC projects, watch for it.

NCA query templates:
```text
site:nca.gov.ss "data centre" OR "data center"
site:nca.gov.ss "licence" OR "license" OR "licensing"
site:nca.gov.ss "gateway" OR "SSIGW"
site:nca.gov.ss "satellite" OR "Starlink"
site:nca.gov.ss "Universal Service" OR "USAF"
site:nca.gov.ss MTN OR Zain OR Digitel OR Gemtel
"National Communication Act 2012" South Sudan "data centre"
"South Sudan" "NCA" "data center" OR "colocation" OR "colo"
"South Sudan" "gateway" "licence" NCA
"مركز بيانات" OR "مركز البيانات" جنوب السودان
"الهيئة الوطنية للاتصالات" جنوب السودان
```
What to extract: licence class and holder, corporate legal name (MTN South Sudan Ltd, Zain South Sudan Ltd, Digitel Holding Limited, Gemtel, Vivacell...), licence date/term, service scope (mobile, fixed, fibre, satellite, gateway, cloud if ever stated). NCA records prove authorisation, not facility count.

---

## 2. Ministry of Information, Communication Technology and Postal Services (MICT&PS)

- **MICT&PS**: https://mictps.gov.ss/ (site self-describes as “Ministry of ICT & Postal Services – South Sudan”; also seen as motps.goss.org in older Facebook branding). Minister and government spokesperson: **Ateny Wek Ateny** (confirmed in 2026 coverage; Eye Radio photo credit “Ministry of ICT&Postal Services-Republic of South Sudan”).
- **National data centre (NDC)** — see §3: minister stated April 2026 it is **under construction and halfway complete**.
- **National ICT Authority**: the government is in the process of **establishing a national ICT Authority** to guide digital transformation (minister, 15th Connected Africa Summit, Nairobi, Apr 2026).
- **Legislation**: **Cybercrime and Computer Misuse Act 2025** — passed 2025, presidential assent 2026; **Data Protection Act** in progress (2026); a draft Data Protection bill existed since ~2021 (World Bank). These are governance signals; DCs will face compliance but there is no DC-specific permit regime yet.
- **National fibre backbone programme**: >US$9B approved Jul 2025; 2,400 km construction start announced Dec 2025 (minister later cited ~2,700 km, Apr 2026); “Dig Once” Ministerial Order requiring conduits in road construction (World Bank 2022); presidential decree ordering digitisation of all public institutions (≈Jan 2026, per Ecofin). All programme evidence — do not count as facilities.
- **e-government**: UN EGDI 0.1191 (2nd-last, per Ecofin). Government systems remain paper-heavy; the NDC project is the flagship digital-infrastructure line.

MICT&PS query templates:
```text
site:mictps.gov.ss "data centre" OR "data center"
site:mictps.gov.ss "fiber" OR "fibre" OR "backbone"
site:mictps.gov.ss "ICT Authority" OR "digital transformation"
site:mictps.gov.ss "cybercrime" OR "data protection"
"Ministry of ICT" "South Sudan" "national data centre"
"Ateny Wek Ateny" "data centre" OR "fiber" OR "digital"
"التحول الرقمي" جنوب السودان
"مركز البيانات الوطني" جنوب السودان
```

---

## 3. National Data Centre (NDC) and the international gateway (SSIGW)

- **National Data Centre (NDC)**: government project in Juba. Evidence chain: (a) World Bank June 2022 diagnostic — no carrier-neutral DC or IXP existed; recommended a carrier-neutral DC + IXP in Juba; (b) Eye Radio, 20 Jan 2026 (`https://www.eyeradio.org/nca-establishes-gateway-and-data-center-oversight-committee/`) / TechAfrica News, 20 Jan 2026 (`https://techafricanews.com/2026/01/20/south-sudans-nca-establishes-gateway-services-and-data-center-oversight-committee/`) / Ecofin, 22 Jan 2026 — NCA established a **Gateway Services and Data Center Oversight Committee** with MGI Communications AG technical support; (c) Eye Radio, 30 Apr 2026 (`https://www.eyeradio.org/ateny-outlines-s-sudans-digital-transformation-plans-at-nairobi-summit/`) — minister: national data centre **under construction, halfway complete**. Grade: **B** for current construction status because the facility facts are press-mediated even when quoting officials; promote to **A** only when an NCA/MICT&PS page, procurement record, commissioning notice or official operator page names the site. **Capacity, address, operator/contractor and timeline are not public** — mark all as unknown. Do not double-count the NDC with any “national data centre” mention in old programme documents.
- **South Sudan International Gateway (SSIGW)**: international voice/SMS gateway facility, operational since ~2014; the World Bank 2022 diagnostic describes it as creating an artificial monopoly that raised international calling/SMS prices, and quotes an SSIGW CEO; footnote cites mgi-management.com (MGI) involvement. The Jan 2026 NCA committee explicitly targets gateway-services control and revenue/governance digitisation. Grade **A** for existence (World Bank diagnostic), **B** for 2026 committee reporting, but SSIGW is a **telecoms gateway facility, not a datacentre** — list separately, do not count as a DC.
- **IXP status**: no IXP in PeeringDB for SS (API `https://www.peeringdb.com/api/ix?country=SS` checked 2026-08-12 returned `{"data": [], "meta": {}}`); ISOC South Sudan chapter ran an IXP Peering Roadshow/Workshop in Juba (25 Jun 2025; `https://www.internetsociety.org/events/peering-roadshows/` and `https://internetsociety.org.ss/news-and-events/`); PIDA/PAP listed a South Sudan IXP project (2021). Treat “Juba IXP” as **planned/absent**, not operational.

NDC/gateway query templates:
```text
"national data centre" OR "national data center" "South Sudan" OR Juba
"SSIGW" OR "South Sudan International Gateway"
site:ecofinagency.com "South Sudan" "data center"
site:eyeradio.org "data centre" OR "data center"
site:mictps.gov.ss "national data"
"Juba" "data centre" construction
"وزارة الاتصالات" جنوب السودان "مركز البيانات"
```

---

## 4. Energy and grid evidence

- **No national grid** (AfDB South Sudan Infrastructure Action Plan): isolated networks serve only **Juba, Malakal and Wau** (plus Renk). Every other state capital runs on diesel gensets/small solar; grid power is not available as a DC input outside those towns.
- **Juba Thermal Power Station**: ~33 MW diesel-fired thermal plant (Wikipedia; Global Energy Monitor — some units not operating), expansion to ~100 MW reported; owner/operator orbit: **South Sudan Electricity Corporation (SSEC)** (parastatal, generation+distribution). Frequent load-shedding and fuel shortages — mission-critical facilities (operator cores, banks) run their own generators; expect genset/UPS evidence for any real DC in Juba.
- **Other state capitals**: solar-hybrid mini-grids and donor-funded power projects (e.g., World Bank South Sudan Energy Access Project P178891) — programme evidence only.
- Use power facts to corroborate a facility (substation, MVA, generator/diesel storage, fuel contracts) but never to create a facility record by itself.

Energy query templates:
```text
"data centre" OR "data center" Juba generator OR diesel OR substation
"Juba Thermal Power Station" OR SSEC capacity
"South Sudan" "no national grid" electricity
site:afdb.org "South Sudan" "isolated networks"
"قوة كهرباء" OR "مولدات" "مركز بيانات" جوبا
```

---

## 5. Official cloud-region and edge signals

| Provider | Official source | South Sudan signal | How to use |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No SS region on official list | A-negative: no facility inference; monitor official page for changes |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No SS region (Africa: South Africa North/West) | A-negative: no facility inference |
| Google Cloud | https://cloud.google.com/about/locations | No SS region | A-negative: no facility inference |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No SS region | A-negative: no facility inference |
| Starlink / LEO satellite | NCA partnership 2024; approved tariffs (Connecting Africa); BuddeComm notes Starlink launch covering SS | Satellite broadband = connectivity, not a DC; a Starlink ground station/teleport inside SS would be a facility lead (none found public) | A for licensing, C for any facility inference |
| Liquid / Muya fibre | NCA 2020 agreement (World Bank); Liquid Juba PoP ~200 km route to Uganda | Carrier PoPs/terminals in Juba = interconnection points, not DCs | B for PoP existence; do not count as DC |

Cloud query templates:
```text
"cloud region" OR "region" "South Sudan" AWS OR Azure OR Google OR Oracle
site:aws.amazon.com "South Sudan"
"Starlink" "South Sudan" ground station OR teleport OR data
"مركز بيانات" OR "سحابة" جنوب السودان
```

---

## 6. Official/operator facility seed list (what actually exists to enumerate)

| Entity / project | Official / primary source | South Sudan signal | Follow-up joins |
|---|---|---|---|
| **National Data Centre (NDC)** | MICT&PS minister via Eye Radio (30 Apr 2026); NCA committee via Eye Radio/TechAfrica/Ecofin (Jan 2026); World Bank 2022 baseline | Juba; **under construction, halfway complete** as of Apr 2026; capacity/address/operator unpublished | Grade B until an official page/procurement/commissioning record is found; track MICT&PS site, tender/procurement records, contractor press, satellite imagery of Juba; verify address before adding to registry |
| **SSIGW (international gateway)** | World Bank 2022 diagnostic; Ecofin Jan 2026; mgi-management.com | Juba; voice/SMS gateway operational since ~2014; monopoly context; revenue digitisation in progress | A for existence; NOT a DC — separate record type (gateway) |
| **Liquid Intelligent Technologies — Juba PoP / Uganda route** | NCA 2020 agreement; World Bank 2022 | Juba; ~200 km fibre to Uganda; carrier PoP and NOC | A for route/agreement (WB); C for any facility details; connectivity, not DC |
| **Muya Fiber Construction** | World Bank 2022 | Juba; parallel fibre route to Uganda | B/C; connectivity only |
| **Nile Cable & Towers (NCT)** | https://nilecabletowers.com/project-gallery/ | **Juba–Torit fibre (Phase I), delivered 2022–2023** under an NCA National Fiber Infrastructure License; Eastern Equatoria corridor | B (company page) — verify via NCA licence registry; fibre, not DC |
| **Bayobab Infra Solutions / MTN Digital Infrastructure** | https://bayobab.africa/mtn-digital-infrastructure-secures-south-sudan-fibre-license-advancing-project-east-2-west/ | 15-year licence from NCA to construct/install/operate electronic communications systems, effective 16 Oct 2025 | B (company page); fibre/infrastructure authorisation, not DC |
| **MTN South Sudan** | https://www.mtn.com.ss/ | Nationwide mobile (largest subscriber base ~1.7M, 2020); core/DR equipment rooms in Juba; 15-year NCA licence 2025 | C/B — no public colo page; only count a facility if a named site/service appears |
| **Zain South Sudan** | https://ss.zain.com/ | 3G/4G network; core in Juba; group annual reports | C/B — core/DR evidence only |
| **Digitel Holding Limited** | https://www.digitelss.com/ | First fully South Sudanese-owned operator, launched Jul 2021 (Kiir inauguration); 5G trial Jun 2024; launched Torit (Oct 2024) and Northern Bahr el Ghazal (May 2026); HQ/switch Juba | C/B — mobile operator; switch sites ≠ public DC unless colo/hosting service appears |
| **Gemtel (Gemtel Green Network)** | https://gemtelgreen.com/ | Licensed 2006; GSM launched in Juba and Yei; regional licence; ~0.5M subs (C); sister Uganda Telecom for switching (B/C) | C — historical/regional; no DC evidence |
| **Vivacell** | Radio Tamazuj (2026 retrospective) | Local operator; licence suspended Feb 2018 | C — historical only |
| **Bank of South Sudan / banks** | BoSS NIPS launch (BuddeComm summary); commercial banks (Equity, KCB, Stanbic, EcoBank...) | Central-bank national instant payment system (NIPS) launched; bank server rooms in Juba | C — banking server rooms are not public DCs unless colo/hosting is evidenced |
| **Starlink / satellite operators** | NCA (2024); Connecting Africa | Licensed satellite broadband service | A for licensing; C for any facility |

Operator query templates:
```text
"{operator}" "South Sudan" "data centre" OR "data center" OR server
site:{operator-domain} "data centre" OR colocation OR hosting
"MTN South Sudan" OR "Zain South Sudan" "data centre" Juba
"Digitel" "South Sudan" switch OR "data centre"
"Juba" "server room" OR "server farm" bank OR telecom
"خوادم" OR "مركز بيانات" جوبا جنوب السودان
```

---

## 7. State-by-state enumeration approach (10 states)

### 7.1 Standard state workflow
For each of the 10 states:
1. Official-domain searches: state government/ministry pages (mostly thin), mictps.gov.ss, nca.gov.ss, operator pages.
2. English variants: `data centre`, `data center`, `datacentre`, `server room`, `server farm`, `cloud`, `colocation`, `IXP`, `Tier`, `MW`.
3. Arabic variants: `مركز بيانات`, `خوادم`, `استضافة`, `سحابة`, `التحول الرقمي` (radio/press use Arabic occasionally).
4. Operator sweep per state capital: MTN, Zain, Digitel (+ historically Gemtel/Vivacell) + local ISPs.
5. Security context per state (2025–2026): record negative sweeps defensibly with state + operator + ministry queries; do not treat conflict reports as DC evidence.

### 7.2 State coverage matrix (10 states)

| State | Capital / main towns | Expected DC result | Source route and special terms |
|---|---|---|---|
| Central Equatoria | Juba, Yei, Kajo-Keji, Nimule, Lainya | **HIGH (only real cluster)**: NDC (under construction), SSIGW, Liquid/Muya PoPs, operator cores, fibre corridor to Uganda | `Juba`, `Nimule`, NDC, SSIGW, Liquid, Muya, Starlink; WB broadband coverage ~59% |
| Western Bahr el Ghazal | Wau | Marginal: Wau has an isolated grid (AfDB); humanitarian/logistics hub; telecom exchanges, bank branches; Digitel/MTN/Zain sites | `Wau` + DC terms; WB coverage ~63% (best in country) — but no DC seed |
| Northern Bahr el Ghazal | Aweil | Marginal/negative: Sudan-war refugee influx, humanitarian ICT; Digitel launched operations May 2026 | `Aweil`, Digitel, refugee/ICT programmes |
| Eastern Equatoria | Torit, Magwi, Kapoeta | Marginal/negative: **Juba–Torit fibre (NCT Phase I 2022–23)**; Digitel launch Oct 2024; future Kenya/Ethiopia border routes | `Torit`, `Magwi`, NCT, Digitel |
| Western Equatoria | Yambio, Maridi | Negative/marginal: low connectivity; UNMISS presence | `Yambio`, `Maridi` + DC terms |
| Jonglei | Bor, Pibor | Negative: cattle raids, floods, White Army activity | `Bor`, `Pibor` + DC terms; coverage ~20% |
| Lakes | Rumbek | Negative: coverage ~59% but no DC seeds; donor solar mini-grids only | `Rumbek` + DC terms |
| Upper Nile | Malakal, Nasir, Renk, Kodok | Negative: **active conflict 2025–26 (Nasir, White Army)**; Malakal/Renk isolated grids (AfDB) | `Malakal`, `Nasir`, `Renk` + DC terms; coverage ~13% (lowest) |
| Unity | Bentiu, Mayom, Koch | Negative: **active conflict 2025–26 (Mayom/Koch clashes)**; oil-field telecom only | `Bentiu`, `Mayom`, `Koch` + DC terms; coverage ~20% |
| Warrap | Kuajok, Gogrial | Negative: cattle/instability; coverage ~17% | `Kuajok`, `Gogrial` + DC terms |

### 7.3 Priority tiers

| Tier | States | Expected results | Queries to add |
|---|---|---|---|
| 1 — Central Equatoria | Central Equatoria (Juba) | NDC construction status, SSIGW, Liquid/Muya PoPs, operator cores, bank/DFS infrastructure, satellite teleports | `Juba "data centre"`, `"national data centre" Juba`, `Juba IXP`, `SSIGW`, `Liquid Juba PoP`, satellite imagery |
| 2 — Fibre/grid corridors | Western Bahr el Ghazal (Wau), Eastern Equatoria (Torit), Upper Nile (Malakal) | Grid towns + fibre corridor towns; telecom exchanges/bank rooms; NCT Juba–Torit | `Wau "data centre"`, `Torit fiber NCT`, `Malakal ICT` |
| 3 — Defensible negatives | Northern Bahr el Ghazal, Western Equatoria, Jonglei, Lakes, Unity, Warrap | Negative or humanitarian-ICT only; conflict zones (Upper Nile/Unity) | state + `data centre`/`مركز بيانات` + operator sweep; note security context |

### 7.4 State quick queries (English)
```text
Juba OR "Central Equatoria" "South Sudan" "data centre" OR "data center"
Wau OR "Western Bahr el Ghazal" "South Sudan" "data centre" OR "data center"
Aweil OR "Northern Bahr el Ghazal" "South Sudan" "data centre" OR "data center"
Torit OR "Eastern Equatoria" "South Sudan" "data centre" OR "data center"
Yambio OR "Western Equatoria" "South Sudan" "data centre" OR "data center"
Bor OR Jonglei "South Sudan" "data centre" OR "data center"
Rumbek OR Lakes "South Sudan" "data centre" OR "data center"
Malakal OR "Upper Nile" "South Sudan" "data centre" OR "data center"
Bentiu OR Unity "South Sudan" "data centre" OR "data center"
Kuajok OR Warrap "South Sudan" "data centre" OR "data center"
"South Sudan" "server room" OR "server farm" OR "colo" OR "colocation"
```

### 7.5 State quick queries (Arabic / mixed)
```text
"مركز بيانات" OR "خوادم" جوبا
"مركز بيانات" وا أو "البحر الغربي"
"مركز بيانات" أويل أو "البحر الشمالي"
"مركز بيانات" توريت أو "شرق الاستوائية"
"مركز بيانات" يامبيو أو "غرب الاستوائية"
"مركز بيانات" بور أو جونقلي
"مركز بيانات" رمبيك أو البحيرات
"مركز بيانات" ملكال أو "أعالي النيل"
"مركز بيانات" بانتيو أو الوحدة
"مركز بيانات" كواجوك أو واراب
"التحول الرقمي" "جنوب السودان"
```

---

## 8. Practical grading and de-duplication rules

- **Facility exists (A)** when an official government/operator page names the DC/service and location. As of 2026-08-12, **no South Sudan DC has a public A-grade facility record**. The **NDC (Juba, under construction)** is the only countable project lead, but current construction status is B because it comes via press reports quoting officials; SSIGW qualifies as an A-grade gateway facility via World Bank, not as a DC.
- **Facility exists (B/C)** when only press, company pages, or aggregators support it (operator cores, NCT fibre, Digitel switches, bank server rooms).
- **Status claims are date-sensitive**: NDC status changed from “planned” (2022 WB) → “committee established” (Jan 2026) → “under construction, halfway” (Apr 2026). Always record evidence date.
- **Cloud region != facility**: no hyperscaler region; satellite and fibre PoPs are connectivity, not DCs.
- **Government programme ambiguity**: “digital transformation”, fibre backbone, ICT Authority, Data Protection Act are programme/legal evidence, not facility records.
- **De-duplication**: NDC (gov project) vs SSIGW (gateway) vs Liquid/Muya PoPs (carriers) vs operator cores (MTN/Zain/Digitel) — keep one canonical record per physical site; Juba is the only city where any of these exist.
- **Aggregators are empty for SS**: datacentermap lists no South Sudan country page; PeeringDB has zero SS IXPs (API-verified 2026-08-12); colo.exchange/inflect/baxtel surfaced no SS entries in searches — treat absence as C-negative and re-check quarterly.
- **Telecom switches / bank server rooms are not commercial datacentres**; exclude unless a source describes hosting/colocation/cloud services at a named facility.

---

## 9. Source priority checklist

1. NCA official site and licensing material (nca.gov.ss) — regulator, licences, gateway, satellite, USAF.
2. MICT&PS (mictps.gov.ss) + ministerial statements via Eye Radio/other press — NDC status, ICT Authority, legislation, fibre programme.
3. World Bank South Sudan Digital Economy Assessment (June 2022, thedocs.worldbank.org) — baseline diagnostic: no carrier-neutral DC, no IXP, fibre routes, coverage table, SSIGW.
4. Ecofin Agency (`https://www.ecofinagency.com/news-digital/2201-52190-south-sudan-approves-9-billion-fiber-network-to-accelerate-digital-push`) and parallel Eye Radio/TechAfrica coverage — Jan 2026 Gateway Services and Data Center Oversight Committee, $9B fibre programme, EGDI.
5. Operator official pages (mtn.com.ss, ss.zain.com, digitelss.com, gemtelgreen.com, nilecabletowers.com).
6. Energy evidence (AfDB Infrastructure Action Plan; Juba Thermal Power Station/SSEC; generator/diesel corroboration).
7. Cloud-provider official region lists (AWS/Azure/GCP/OCI) — A-negative checks.
8. Reputable press (Eye Radio, Radio Tamazuj, Sudans Post, Ecofin, Connecting Africa, TechAfrica News) for dated status updates.
9. Aggregators (datacentermap, colo.exchange, inflect, PeeringDB) for negative/discovery checks only.

---

*Reviewed final methodology note: source URLs and state coverage were checked on 2026-08-12. Partner file: `SS/explorer-industry.md` (press/vendor angle).*
