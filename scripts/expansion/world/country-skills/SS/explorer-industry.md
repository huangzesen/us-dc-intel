# SS Explorer — Industry / Press / Vendor Discovery for South Sudan Datacentres

Date: 2026-08-12 (reviewed final). Country: **SS South Sudan**. Division model: **10 states**. Angle: **industry media, local press, operator/vendor pages, interconnection records, satellite/fibre ecosystem, and state-level search patterns** for finding datacentre-relevant projects.

Reliability grades: **A** = official/primary (operator page, government/NCA/MICT&PS statement, World Bank diagnostic/project document, cloud-provider page, PeeringDB API negative check), **B** = strong secondary (credible local press quoting officials, established trade press, ISOC pages, company pages for existence), **C** = aggregator, social post, old MoU, market-report snippet, paywalled summary, or unverifiable local mention.

---

## 0. South Sudan-specific frame

- South Sudan has **no commercial colocation market and no public facility registry**. The World Bank’s June 2022 diagnostic stated the country had **no fully functional carrier-neutral data centre and no IXP**; the government’s **national data centre (Juba) is under construction and “halfway complete” as of Apr 2026** (minister via Eye Radio). That NDC status is **B-grade until an official MICT&PS/NCA construction, tender, address, operator, or commissioning page appears**. Discovery therefore triangulates: **operator/press coverage of the NDC**, **telecom operators** (MTN, Zain, Digitel, Gemtel, historical Vivacell), **fibre players** (Liquid Intelligent Technologies, Muya Fiber, Nile Cable & Towers, Bayobab/MTN Digital Infrastructure), **satellite broadband** (Starlink et al.), the **SSIGW gateway**, **IXP/peering records** (absent), and **local press** (Eye Radio, Radio Tamazuj, Sudans Post, The City Review, Juba Echo, The Dawn, Sudan Tribune).
- **Everything of note is in Juba (Central Equatoria)**: NDC construction, SSIGW, Liquid/Muya PoPs, operator cores, the only bank/DFS infrastructure, and any plausible future colo. State capitals outside Juba are **negative or marginal** (telecom exchanges, bank server rooms, humanitarian ICT) — with one fibre corridor exception (Juba–Torit, Eastern Equatoria) and grid towns (Wau, Malakal).
- **Conflict context (2025–2026) dominates state-level expectations**: Nasir clashes Feb–Mar 2025 (Upper Nile), Machar’s Apr 2025 detention, postponed Dec 2026 elections, 2025–26 fighting in Upper Nile and Unity (Mayom/Koch), cattle raids in Jonglei/Warrap/Lakes, floods, and Sudan-war refugee influx into Northern Bahr el Ghazal/Upper Nile. Any state-level “data centre” hit in these states should be treated as either programme news or confusion with UN/NGO server rooms — verify before counting.
- **Connectivity**: Juba–Uganda fibre (~200 km, Liquid, from 2020; Muya parallel) is the only operational international terrestrial route evidenced in the World Bank diagnostic; ~300 km total operational fibre as of 2020 data (4% of population within 10 km of a fibre node); satellite (Starlink licensed 2024, plus VSAT) is the fallback. Additional fibre leads include NCT’s Juba–Torit Phase I and Bayobab Infra Solutions Ltd’s 15-year NCA licence effective 16 Oct 2025, but these are infrastructure authorisations/corridors, not DC records. No SS submarine cable (landlocked; Djibouti agreement for onward cable access). **No cloud regions** — AWS/Azure/GCP/OCI all absent.
- **Languages**: press and government are predominantly English; Arabic/Juba Arabic appear in radio (Radio Tamazuj, Miraya, Bakhita) and some official documents. English terms: `data centre`, `data center`, `datacentre`, `server room`, `server farm`, `colo`, `IXP`; Arabic: `مركز بيانات`, `خوادم`, `استضافة`, `سحابة`, `التحول الرقمي`.
- **Aggregator baseline (verified 2026-08-12)**: PeeringDB lists **zero SS IXPs** (API `https://www.peeringdb.com/api/ix?country=SS` returned `{"data": [], "meta": {}}`, A-negative); datacentermap has no South Sudan country page; colo.exchange/inflect/baxtel surfaced no SS facilities in searches (C-negative). Any new aggregator entry for SS is itself a discovery lead.

---

## 1. Local and regional press sources

| Source | URL / query route | Use | Grade |
|---|---|---|---|
| Eye Radio | https://eyeradio.org/; NDC status: https://www.eyeradio.org/ateny-outlines-s-sudans-digital-transformation-plans-at-nairobi-summit/; oversight committee: https://www.eyeradio.org/nca-establishes-gateway-and-data-center-oversight-committee/ | Best English source quoting officials: NDC construction “halfway complete” (30 Apr 2026), ICT Authority plan, Cybercrime Act 2025, Digitel state launches | B; use as official-position evidence only when quoting named officials |
| Radio Tamazuj | https://www.radiotamazuj.org/en | Local operator news (Digitel NBEG launch May 2026; Vivacell licence suspension 2018 retrospective); state-level items | B |
| Sudans Post | https://www.sudanspost.com/ | National/governance + technology items (EACO assemblies Jun 2025) | B |
| The City Review | https://cityreviewss.com/ (check liveness) | Economic/governance coverage of ICT, fibre, digital payments | B |
| Juba Echo | https://jubaecho.com/ | Local English daily; state and business items | B/C |
| The Dawn Newspaper | https://www.facebook.com/p/The-Dawn-Newspaper-61563177664636/ and https://x.com/dawn_newspaper | Local newspaper lead source; no stable `thedawn.com.ss` site was usable in checks, so prefer official/social pages or corroborate via Radio Tamazuj/MICT&PS | C/B |
| The Juba Mirror | https://thejubamirror.com/ | NCA 30-day ultimatum to unlicensed satellite providers (Apr 2024), social-media ban lift (Jan 2025) | B/C |
| Sudan Tribune | https://sudantribune.com/ | Regional coverage of South Sudan ICT/policy | B |
| Independent (Uganda) / BIRD Agency | https://www.independent.co.ug/ | Nov 2025 special report on Digitel vs MTN/Zain — market-share context | B |
| TechAfrica News | https://techafricanews.com/; NCA/NDC committee: https://techafricanews.com/2026/01/20/south-sudans-nca-establishes-gateway-services-and-data-center-oversight-committee/ | Starlink partnership (Jul 2024), NCA/NDC committee, China-Africa digital cooperation (Sep 2025), Digitel 5G trial (via LinkedIn, Jun 2024) | B |
| Ecofin Agency | https://www.ecofinagency.com/ and https://www.ecofinagency.com/news-digital/2201-52190-south-sudan-approves-9-billion-fiber-network-to-accelerate-digital-push | 22 Jan 2026: NCA gateway+NDC oversight committee, $9B fibre programme, EGDI stats | B |
| Connecting Africa | https://www.connectingafrica.com/ | Approved Starlink tariffs, telecom regulation | B |
| ITWeb Africa / Developing Telecoms / Telecom Review Africa / Africa Press | site-scoped | African telecom trade press; operator/regulator items | B |
| Digital Watch Observatory | https://dig.watch/countries/south-sudan | Digital-governance background, 2,400 km fibre plan context | B/C |
| ISOC South Sudan Chapter | https://internetsociety.org.ss/ and https://www.internetsociety.org/events/peering-roadshows/ | IXP Peering Roadshow & Workshop Juba (25 Jun 2025) — no IXP yet | B |
| BuddeComm | https://www.budde.com.au/Research/South-Sudan-Telecoms-Mobile-and-Broadband-Statistics-and-Analyses | Paywalled market reports (Starlink launch covering SS; BoSS NIPS launch) — use summaries only | C/B (paywalled) |
| Internews media/telecoms guide | https://internews.org/ (legacy guide) | Historical operator facts (Gemtel/Uganda Telecom switching) | B/C (dated) |

---

## 2. Operators, carriers and vendors

### 2.1 Mobile operators
- **MTN South Sudan** (https://www.mtn.com.ss/) — largest operator (~1.7M subs, 61.8% share, 2020); 15-year NCA licence signed Apr 2025; backhaul mostly microwave/satellite with Juba fibre access; core/DR rooms in Juba. **C/B** — no public colo/hosting page found; count only a named facility.
- **Zain South Sudan** (https://ss.zain.com/) — Zain Group subsidiary; 3G/4G in Juba/Central Equatoria; core in Juba. Group annual reports (zain.com) cover SS OPCO regulatory items. **C/B** — core/DR evidence only.
- **Digitel Holding Limited** (https://www.digitelss.com/) — first fully South Sudanese-owned operator; launched Jul 2021 (President Kiir inauguration); CEO De Chan Awuol; **5G trial Jun 2024**; launched **Torit (Oct 2024)** and **Northern Bahr el Ghazal (May 2026)**; HQ/switch in Juba. Aggressive capex vs MTN/Zain (Independent/BIRD Nov 2025). **C/B** — watch for any hosting/DC service.
- **Gemtel (Gemtel Green Network)** (https://gemtelgreen.com/) — licensed 2006, GSM in Juba and Yei; regional licence; sister Uganda Telecom historically handled switching (Kampala). **C** — historical/regional, no DC evidence.
- **Vivacell** — local operator; **licence suspended Feb 2018** (Radio Tamazuj). **C** — historical only.
- **Network of the World (NOW)** — early South Sudanese operator (pre-2013 research mentions); no current public DC evidence. **C** — historical.

### 2.2 Fibre, gateway and infrastructure carriers
- **Liquid Intelligent Technologies (Liquid Telecom)** — 2020 NCA agreement; **Juba–Uganda route (~200 km)**; likely Juba PoP/NOC but no public datacentre page. **A** for route existence (World Bank), **C** for facility details. Connectivity, not DC.
- **Muya Fiber Construction** — parallel Juba–Uganda route (World Bank 2022). **B/C**.
- **Nile Cable & Towers (NCT)** — https://nilecabletowers.com/project-gallery/ — **Juba–Torit fibre Phase I delivered 2022–2023** under NCA National Fiber Infrastructure License; first large-scale NCT backbone project. **B** (company page); verify licence via NCA.
- **Bayobab Infra Solutions Ltd / MTN Digital Infrastructure** — https://bayobab.africa/mtn-digital-infrastructure-secures-south-sudan-fibre-license-advancing-project-east-2-west/ — 15-year NCA licence to construct, install and operate electronic communications systems, effective 16 Oct 2025. **B** (company page); fibre authorisation, not DC.
- **SSIGW (South Sudan International Gateway)** — voice/SMS gateway since ~2014; monopoly context; MGI (mgi-management.com) involved in management/technical support; Jan 2026 NCA committee strengthened gateway/data-centre oversight. **A** for existence (World Bank), **B** for 2026 committee reporting; **not a datacentre** — separate record type.
- **National Data Centre (NDC)** — Juba, **under construction, halfway complete (Apr 2026)**; Gateway Services and Data Center Oversight Committee formed Jan 2026. **B** until an official site/procurement/commissioning record appears. Press-watch this: contractor award, site address, capacity numbers, commissioning events will be the first countable DC record in SS.

### 2.3 Satellite / VSAT and ISPs
- **Starlink** — NCA partnership 2024; approved tariffs; retail/enterprise broadband; possible future gateway/teleport (none public). **A** for licensing, **C** for facility.
- Other satellite/VSAT operators and ISPs (e.g., local VSAT resellers; “Juba Network Co.” appears in db-ip listings) — **C**; do not count as DCs.

### 2.4 Banks and digital finance (server-room leads, not DCs)
- **Bank of South Sudan (BoSS)** — National Instant Payment System (NIPS) launched (interoperability between banks and m-money); central-bank IT facilities in Juba. **C**.
- Commercial banks (Equity, KCB, Stanbic, EcoBank, Citi? etc.) and mobile money (MTN MoMo, Zain Cash, Digitel m-money ambitions) — server rooms in Juba only. **C**.

### 2.5 Equipment / EPC vendors (corroboration layer)
- Huawei, ZTE, Nokia, Ericsson, Vertiv, Generac, CAT, solar suppliers — appear in SS telecom tenders (e.g., network expansion, solar-hybrid power) and ministry procurement; a vendor press release naming a **data centre** in SS would be a major discovery signal. **B/C**.

---

## 3. Interconnection records

- **IXPs**: PeeringDB API `https://www.peeringdb.com/api/ix?country=SS` → **zero IX records (verified 2026-08-12)**; PCH/ISOC Pulse show no SS IXP; ISOC SS chapter workshop (Jun 2025) aimed at capacity-building — no IXP operational. Treat any “Juba IXP” as planned/absent. **A-negative** (registry check).
- **PeeringDB networks**: local operators (MTN, Zain, Digitel) are not systematically registered for SS in PeeringDB — the country filter is unreliable; use ASN records per operator instead (e.g., Zain SS ASN via ss.zain.com or bgp.he.net). **C**.
- **Fibre corridors**: Juba–Uganda (Liquid, Muya), Juba–Torit (NCT), Bayobab/MTN Digital Infrastructure licence, planned Juba–Kenya/Ethiopia/Sudan routes and Nile-waterway options (World Bank 2022; 2,400–2,700 km national backbone programme from Dec 2025). Fibre presence ≠ DC, but PoP/terminal buildings are candidate colo hosts later.
- **Submarine access**: landlocked; agreement with Djibouti for cable access (World Bank 2022). No landing station inside SS.

---

## 4. Search query patterns

### 4.1 English discovery queries
```text
"South Sudan" OR Juba "data centre" OR "data center" OR datacentre
"South Sudan" "national data centre" OR "national data center"
"South Sudan" "colo" OR "colocation" OR "server farm"
"South Sudan" IXP OR "internet exchange"
"South Sudan" "data protection" OR "cybercrime" (legislation watch)
Juba "server room" OR "server hosting" OR "cloud hosting"
"South Sudan" "data center" tender OR procurement OR contractor
site:eyeradio.org "data centre" OR "data center"
site:radiotamazuj.org "data centre" OR "data center" OR "خوادم"
site:sudanspost.com "data centre" OR "digital"
"Digitel" "South Sudan" "data" OR "server" OR "switch"
"Liquid" OR "Muya" OR "NCT" OR "Bayobab" "South Sudan" fiber OR fibre OR PoP
"Starlink" "South Sudan"
"SSIGW" OR "South Sudan International Gateway"
```

### 4.2 Arabic / mixed queries
```text
"مركز بيانات" OR "مركز البيانات" "جنوب السودان"
"خوادم" OR "استضافة" جوبا
"التحول الرقمي" "جنوب السودان"
"مركز البيانات الوطني" جوبا
"شبكة الألياف" OR "الألياف البصرية" "جنوب السودان"
"وزارة الاتصالات" "جنوب السودان" بيانات
```

### 4.3 Status-verb capture (map announcement to lifecycle)
`announces / plans / MoU / partnership` = intent (C); `licence / licence renewal / approved tariffs` = authorisation (A/B); `under construction / halfway complete` = build (A via official, B via press); `launched / commissioned / operational` = live (A via operator/gov); `trial` (Digitel 5G) = pilot (B/C). Date-stamp everything; NDC moved intent→construction between 2022 and 2026.

---

## 5. State-level sweep patterns (10 states)

Per state, four sweeps: ① press/vendor (state + capital + DC terms, EN/AR); ② operators (MTN/Zain/Digitel/Gemtel + capital); ③ official (Eye Radio/Radio Tamazuj/Sudans Post + mictps.gov.ss + nca.gov.ss); ④ interconnection/aggregators (IXP, PeeringDB, datacentermap).

| State | Capital | Expected result & special terms |
|---|---|---|
| Central Equatoria | Juba | **Only cluster**: NDC, SSIGW, Liquid/Muya PoPs, operator cores, bank/DFS, satellite; terms: Juba, Nimule, NDC, SSIGW |
| Western Bahr el Ghazal | Wau | Marginal; grid town (AfDB); humanitarian hub; terms: Wau, university ICT |
| Northern Bahr el Ghazal | Aweil | Negative/marginal; refugee ICT; Digitel ops May 2026; terms: Aweil, Digitel |
| Eastern Equatoria | Torit | Marginal; Juba–Torit fibre (NCT), Digitel Oct 2024; terms: Torit, Magwi, NCT |
| Western Equatoria | Yambio | Negative; terms: Yambio, Maridi |
| Jonglei | Bor | Negative; cattle raids/floods/White Army; terms: Bor, Pibor |
| Lakes | Rumbek | Negative; solar mini-grids; terms: Rumbek |
| Upper Nile | Malakal | Negative; **active conflict (Nasir)**; grid town; terms: Malakal, Nasir, Renk |
| Unity | Bentiu | Negative; **active conflict (Mayom/Koch)**; oil-field telecom; terms: Bentiu, Mayom, Koch |
| Warrap | Kuajok | Negative; cattle/instability; terms: Kuajok, Gogrial |

Quick template per state: `"{capital}" OR "{state}" "South Sudan" "data centre" OR "data center" OR "مركز بيانات"` + operator names.

---

## 6. Verification recipe

1. **Cross-check ≥2 independent channels** for any positive hit: e.g., NDC (Eye Radio minister quote + Ecofin committee + future MICT&PS page/tender); operator cores (operator page + press + NCA licence).
2. **Satellite imagery**: Juba (4.85°N, 31.6°E) — any NDC/colo construction is visible; date imagery to confirm “under construction” vs operational. Historical imagery also settles whether an old “data centre” report refers to a building that still exists.
3. **Capacity sanity**: no public MW/rack data for SS; if a number appears, check against power reality (grid unavailable outside Juba/Wau/Malakal; diesel gensets; fuel logistics) — a 10+ MW claim in SS is implausible without a power-plant-scale announcement.
4. **De-dup**: NDC vs SSIGW vs Liquid/Muya PoPs vs operator cores vs bank rooms — separate record types; one canonical record per physical site in Juba.
5. **Aggregator hygiene**: new SS entries on datacentermap/colo.exchange/inflect are leads only (C) until an operator/government source confirms.
6. **Date-stamp + conflict context**: any Upper Nile/Unity/Jonglei facility claim must be checked against 2025–26 security reports (Nasir, Mayom/Koch, White Army) — destroyed/looted telecom infrastructure is likely.

---

## 7. Suggested discovery pipeline (order of operations)

1. **Seed**: NDC status (Eye Radio Apr 2026 + Ecofin Jan 2026) — the only countable project; track MICT&PS/nca.gov.ss for capacity/address/tender.
2. **Operator sweep**: MTN, Zain, Digitel, Gemtel official pages + NCA licensing news (MTN 15-yr licence 2025; Digitel state launches) → Juba cores; negative elsewhere.
3. **Carrier sweep**: Liquid/Muya (Juba–Uganda), NCT (Juba–Torit), Bayobab/MTN Digital Infrastructure licence, SSIGW (gateway) → PoP/gateway records, not DCs.
4. **Interconnection negative checks**: PeeringDB IX (SS empty), ISOC chapter news, IXP workshop follow-ups (quarterly).
5. **Press watch**: Eye Radio/Radio Tamazuj/Sudans Post/Ecofin/TechAfrica for: NDC commissioning, ICT Authority establishment, Data Protection Act passage, fibre programme milestones (2,400–2,700 km), Starlink teleport, first colo announcement.
6. **State sweeps**: 10 states × 4 sweeps; expect defensible negatives except Central Equatoria (high) and Wau/Torit/Malakal (marginal).
7. **Verify** every positive per §6 before grading; never promote C to A without an official page.

---

## 8. Per-source grade summary

| Source | Grade |
|---|---|
| Eye Radio quoting minister (NDC, ICT Authority, cybercrime act) | B |
| World Bank Digital Economy Assessment (Jun 2022) | A |
| NCA official site / licences | A |
| Operator official pages (mtn.com.ss, ss.zain.com, digitelss.com, gemtelgreen.com) | A for corporate/service existence; B/C for inferred core-site or DC claims |
| Ecofin Agency, Connecting Africa, TechAfrica News | B |
| Radio Tamazuj, Sudans Post, The City Review, Juba Echo, The Dawn, Juba Mirror, Sudan Tribune | B (B/C for small outlets) |
| Independent/BIRD special report (Digitel) | B |
| Company pages for fibre (NCT) | B |
| PeeringDB API negative checks | A-negative (absence) |
| ISOC SS chapter | B |
| Aggregators (datacentermap, colo.exchange, inflect, baxtel) | C (empty for SS; new entries = leads) |
| Social media/LinkedIn posts (e.g., Digitel 5G trial) | C |
| BuddeComm/paywalled market reports | C/B |

---

*Reviewed final methodology note: source URLs and state coverage were checked on 2026-08-12. Partner file: `SS/explorer-official.md` (official/regulatory angle).*
