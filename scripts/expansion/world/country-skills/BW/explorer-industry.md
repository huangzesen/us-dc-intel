# BW Explorer — Industry / Press / Vendor Discovery for Botswana Datacentres

Date: 2026-08-12. Scope: Botswana (BW) datacentre enumeration from industry media, local business press, operator/vendor pages, cloud-region announcements, and per-division search patterns. Status: **final methodology**.

Reliability grades: **A** = official/primary source (operator page, government agency, council/DEA/BOCRA/BERA document, cloud-provider page), **B** = strong secondary/trade press, established local business press, industry association, or vendor case study, **C** = aggregator, social post, old MoU, market-report snippet, or unverifiable local mention.

---

## 0. Botswana-specific frame

- Botswana has no public national facility registry and no hyperscale region. Discovery works by triangulating **operator pages (BoFiNet/Digital Delta, BTC Sentlhaga, BDIH, Orange Botswana, Unitel)**, **local business press (Mmegi, Botswana Guardian, DailyNews, Business Weekly, Weekend Post, Sunday Standard, The Patriot)**, **trade press (DCD, Connecting Africa, Tech In Africa, Ecofin, TechFinancials)**, **government procurement/tenders (gov.bw)**, **BOCRA licensing news**, **DEA EIA records**, **power/energy news (BPC/BERA, Morupule/Leupane)**, and **IXP/interconnection evidence (BINX/PeeringDB)**.
- Commercial activity is almost entirely in **Gaborone city / South East corridor**, with the BDIH Block 8 cluster as the anchor (Digital Delta DDDC + BDIH DC), plus BTC Sentlhaga and Orange Botswana leads. Out-of-Gaborone candidates are second-order: **Palapye/Leupane/Serowe/Selebi-Phikwe** (Central, energy/industrial, including the AAAS Energy + ChillMine announced campus lead), **Francistown** (North East), and **Maun** (North West).
- Division coverage follows the requested **16 target divisions**: Central; Chobe; Francistown; Gaborone; Ghanzi; Jwaneng; Kgalagadi; Kgatleng; Kweneng; Lobatse; North East; North West; Selibe Phikwe; South East; Southern; Sowa Town. Current government local-authority pages also expose Orapa; treat `Orapa` as a Central-district alias for search coverage unless the upstream division model changes.
- Both spellings `data centre` / `data center` are used; also search `datacentre`, `colo`, `co-location`, `cloud`, `sovereign cloud`, `Tier II`, `Tier III`, `Uptime Institute`, `racks`, `MW`, `MVA`, `substation`, `server infrastructure`, `digital hub`, `innovation hub`, `BDIH`, `Digital Delta`.
- English dominates business/permitting coverage. Setswana is rarely used for commercial DC announcements; use it only as a secondary check (e.g., `lefelo la data`) and verify with English/official documents.
- Watch lifecycle verbs carefully: `announces`, `signs MoU`, `plans`, `feasibility` = intent (C/B); `breaks ground`, `starts construction`, `completes phase` = pipeline (B, A if official); `opened`, `launched`, `operational`, `Uptime certified` = operational signal (verify with operator/Uptime page for A).

---

## 1. Industry and trade press sources

Use press to discover project names, operators, districts, capacity claims and status verbs; then verify with an operator, council, DEA, BOCRA, BERA/BPC or government source.

| Source | URL / query route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/news/ | Global trade feed; covered Botswana's DDDC launch (Dec 2025), Chinese-built DDDC delivery expectation (2023), and AAAS Energy + ChillMine Palapye/Leupane campus announcement (2025). | B; A only for linked primary docs |
| Connecting Africa | https://www.connectingafrica.com/ | African digital-infrastructure trade press; DDDC Tier III carrier-neutral coverage (Nov 2025). | B |
| Tech In Africa | https://www.techinafrica.com/ | Pan-African tech press; Liquid Gaborone metro ring, Starlink licence coverage. | B |
| Ecofin Agency | https://www.ecofinagency.com/ | Africa business/digital press; DDDC inauguration summary (Nov 2025). | B |
| TechFinancials | https://techfinancials.co.za/ | Southern-African tech finance press; BoFiNet digital-access/capacity stories. | B |
| WeAreTech Africa / CIO Africa | https://www.wearetech.africa/ , https://cioafrica.co/ | African ICT press; Botswana digital-priorities coverage under Minister Tshere. | B |
| Mmegi | https://www.mmegi.bw/ | Leading local daily; energy (Tlou licence), ICT policy, BPC/BOCRA/BoFiNet stories. | B (A if quoting official docs) |
| DailyNews (government newspaper) | https://dailynews.gov.bw/news-list/srccategory/35 | State newspaper; national projects, BoFiNet fibre, government ICT. Use for launch dates and official quotes, but still resolve facility facts to operator/government pages where possible. | B (A- for verbatim official notices/quotes) |
| Botswana Guardian / Midweek Sun | https://www.botswanaguardian.co.bw/ | Local daily; DDDC launch detail, digital-economy coverage. | B |
| The Patriot on Sunday | https://www.thepatriot.co.bw/ | Weekend local; business/ICT features. | B/C |
| Weekend Post | https://www.weekendpost.co.bw/ | Local weekly; energy/ICT investigative items. | B/C |
| Sunday Standard | https://www.sundaystandard.info/ | Local weekly; BoFiNet/EASSy-WACS shareholder detail, BOSSC/BITC stories. | B |
| Business Weekly & Review | https://businessweekly.co.bw/ | Local business weekly; BTC, telecoms, economy. | B/C |
| BW TechZone | https://www.bwtechzone.com/ | Local tech blog; DDDC launch, Liquid Gaborone ring, data-protection commentary. | B/C |
| The Voice / The Gazette / YourBotswana | https://thevoicebw.com/ , https://www.thegazette.news/ , https://yourbotswana.com/ | Local outlets; regional development and trade news. | C/B |
| Africa Data Centres Association / D4D Hub | https://africadca.org/ ; D4D Hub/Xalam Botswana market brief: https://cms.d4dhub.eu/assets/Initiatives/Data-Governance-in-Africa/Digital-Investment-Facility/2507_Country-Market-Briefs/Data-Center-Market-Brief-Botswana.pdf | Industry association + EU-funded market brief (demand/supply/regulatory context). Good for market size and supply context, not facility proof. | B |
| PeeringDB / BINX | https://www.peeringdb.com/ix/1409 , https://www.binx.org.bw/ | Botswana Internet Exchange, Gaborone (AS37771); participant lists show who actually colocates/peers. | B |
| DC Byte / Baxtel / datacentermap / datacenters.com / DataCenterMap | https://www.datacentermap.com/botswana/ , https://www.datacenters.com/locations/botswana | Discovery indexes (~5 facilities/3 operators per datacentermap; ~8 per datacenters.com). Aggregators misplace capacity and status; never use alone. | C |
| Vendor case studies | Siemon, Schneider Electric, Vertiv, Huawei, ZTE, Caterpillar, electrical/mechanical contractors | Equipment-delivery evidence for DDDC (Zhong Gan/CJIC built it) and future builds; capacity often absent. | B/C |

Trade-press query templates:
```text
site:datacenterdynamics.com/en/news/ Botswana "data center"
site:datacenterdynamics.com/en/news/ Botswana "data centre"
site:connectingafrica.com Botswana "data center"
site:techinafrica.com Botswana "data centre"
site:ecofinagency.com Botswana "data centre"
site:mmegi.bw "data centre" OR "data center"
site:businessweekly.co.bw "data centre" OR "data center"
site:bwtechzone.com "data centre" OR "Digital Delta"
site:thepatriot.co.bw "data centre"
site:sundaystandard.info "data centre" OR "BoFiNet"
"Botswana" "data centre" "{operator OR district OR town}"
"Botswana" "data center" "MW" OR "racks"
```

---

## 2. Operator and developer sweep

Official operator pages are **A for current claimed locations and facility existence**. Marketing-page capacities are **A-/B** unless facility-level IT load or a primary announcement backs them.

| Operator / developer | Official / primary URL | Botswana signals | Notes |
|---|---|---|---|
| BoFiNet / Digital Delta Data Centre (DDDC) | https://www.bofinet.co.bw/ , https://www.digitaldelta.co.bw/ | Gaborone, BDIH Block 8; vendor-neutral; official pages state 1,000 sqm DC1 and Tier III certification; BoFiNet confirms Uptime Tier III Constructed Facility certification in Oct 2025; launch reported 25 Nov 2025 by DailyNews/trade press; D4D/industry sources describe expansion potential up to ~400 racks. | Anchor facility. DCD/Botswana Guardian/Connecting Africa cover launch and delays. Search `Digital Delta`, `DDDC`, `BoFiNet data centre`. |
| BDIH Data Centre | https://www.bih.co.bw/bdih-data-centre/ | Plot 69184, Block 8, BDIH, Gaborone; 80 racks; Tier III compliant; DCaaS colocation; carrier-neutral (BoFiNet, VBN, BTC) | Distinct from DDDC; check BDIH tenders/annual reports and news for operator and expansion. |
| BTC (Botswana Telecommunications Corporation) | https://btc.bw/business/sentlhaga-data-center/ | Sentlhaga Data Center, Gaborone; Tier II Uptime-certified (first certified DC in BW); 120 sqm; 5 kW/rack; BTC Cloud Connect (Microsoft 365) | Official page has full specs; business press covers BTC's financials and DC ambitions. |
| Orange Botswana | https://www.orange.co.bw/ | New Lobatse Road, Gaborone DC; ~2 MW per aggregator listing | Verify via Orange enterprise pages/case studies and BOCRA register. |
| Unitel (Universal Telecom) | https://unitel.co.bw/ | Gaborone; BOCRA-licensed; fibre backbone + colocation/data-centre service claim | Small operator; confirm colo scope via site/BOCRA. |
| AAAS Energy + ChillMine / Leupane-Palapye campus | AAAS site https://aaas.energy/ ; ChillMine site https://chillmine.io/about/ ; company press release via EIN; DCD/Renewables Now/Ecofin coverage | Announced solar/BESS-powered data-centre campus lead near Palapye / Leupane Energy Hub, Central District. Energy hub is associated with Botala/AAAS solar development; press release claims AI/hyperscale target. | Treat as **B/C pipeline lead only**. Do not count as facility, construction, or capacity until DEA/BERA/BPC/council/operator construction evidence is found. Search `Leupane Energy Hub`, `Botala`, `AAAS Energy`, `ChillMine`, `Palapye`. |
| Mascom Wireless | https://www.mascom.bw/ | Mobile operator, HQ Tsholetsa House, Gaborone; internal core network (5G launched 2024) | Internal DC only; record only if colo/cloud marketed. |
| Liquid Intelligent Technologies / Africa Data Centres | https://liquid.tech/local-offices/country/botswana/ , https://www.africadatacentres.com/ | Gaborone office (Plot 54374 CBD); Gaborone Metro Ring; VSAT/international connectivity; no confirmed Botswana ADC facility | Operator presence != facility; do not infer a Liquid/ADC DC without local evidence. |
| Starlink / SpaceX | https://www.starlink.com/ | BOCRA operating licence May 2024; service launched ~Aug–Sep 2024 after initial rejection (Oct 2023) and temporary ban | Satellite ISP, not a DC; use as BOCRA-licensing context and connectivity lead. |
| Huawei / ZTE / Zhong Gan / China Jiangxi Int'l (CJIC) | vendor pages + DCD | DDDC built by Zhong Gan with CJIC backing (DCD) | Use as builder/equipment evidence for DDDC and future Chinese-funded builds; B/C. |
| AWS / Microsoft / Google / Oracle | official region pages (see official file §3) | No BW cloud region; Azure reach via BTC Cloud Connect (Microsoft 365) | Seed/partner evidence only. |

Vendor/operator query templates:
```text
"{operator}" Botswana "data centre" OR "data center"
"{operator}" Botswana "racks" OR "MW"
"{operator}" "BOCRA" licence
"Digital Delta" OR "DDDC" "BoFiNet"
"Sentlhaga" "BTC" "data centre"
"AAAS Energy" "ChillMine" "data center" Botswana
"Leupane Energy Hub" "data centre" OR "data center"
"{operator}" "BDIH" OR "Block 8" OR "plot" Gaborone
"{operator}" "Uptime Institute" Botswana
"Botswana" "data centre" "Zhong Gan" OR "CJIC" OR "Huawei"
```

---

## 3. Official and semi-official channels to pivot from press

Every press lead should be verified against one or more of these primary routes.

| Channel | URL / route | How to use | Grade |
|---|---|---|---|
| gov.bw e-services | https://www.gov.bw/ | EA authorizations, planning permission, trade licences, ministry pages (Communications & Innovation; Minerals & Energy) | A |
| BOCRA | https://www.bocra.org.bw/licensing + licensee list xlsx/PDF (see official file §1.4) | Confirm operator licences (NFP/SAP/VANS); search operator legal names | A |
| DEA environmental assessment | https://www.gov.bw/environmental-management/application-environmental-assessment-ea-authorizations ; tracker https://www.eia.co.bw/tracker | EIS/EA authorization for projects incl. ICT buildings, substations, generator/fuel storage | A (official) / B (tracker) |
| BPC / BERA | https://www.bpc.bw/ , https://www.bera.co.bw/ | Power connection, tariff, generation licences, IPP announcements | A |
| Councils | Gaborone City Council; town/district councils | Development permission and building permits (no public portal; use notices/press/minutes) | A when record found |
| SEZA | https://www.seza.co.bw/ | 9 SEZs (incl. Sir Seretse Khama International Airport zone; Palapye/industrial candidates) + investor incentives; press for zone designations | A for zones/incentives |
| BITC / BOSSC | https://www.bitc.co.bw/ | Botswana One Stop Service Centre (launched Oct 2017): company registration, licensing, work/residence permits, land access | A for process; B for investor announcements |
| Uptime Institute | https://uptimeinstitute.com/ (BoFiNet client page exists) | Certification records for Sentlhaga (Tier II) and DDDC (Tier III) | A for certification records |
| BINX / PeeringDB | https://www.binx.org.bw/ , https://www.peeringdb.com/ix/1409 | Interconnection/colo presence proof | B |

---

## 4. Per-division industry-search guidance (16 target divisions)

For each division: (1) run press site-scoped sweeps below; (2) run official sweeps from the official file §5; (3) for any lead, require one primary source before grading A.

Division-specific notes and seeds:

- **Gaborone** — anchor district. Press terms: `Digital Delta`, `BDIH`, `Sentlhaga`, `Orange Botswana data centre`, `Unitel`, `Block 8`, `plot No`, `Tlokweng Road`, `New Lobatse Rd`, `Phakalane`, `Western Bypass`. Events: Botswana Tech Summit & Expo (annual, Gaborone), BDIH events.
- **South East** — Tlokweng/Ramotswa; SSKIA SEZ. Terms: `South East District`, `Tlokweng`, `SSKIA`, `airport` + `data centre`.
- **Kweneng** — Molepolole, Mogoditshane. Terms: `Kweneng`, `Molepolole`, `Mogoditshane` + `data centre`/`cloud`; The Voice covers this area.
- **Kgatleng** — Mochudi; low yield. Terms: `Kgatleng`, `Mochudi`.
- **Southern** — Kanye/Moshupa; Jwaneng mine energy. Terms: `Southern District`, `Kanye`, `Jwaneng solar` + `data`.
- **Jwaneng (town)** — mine power/solar news; negative-search protocol for DCs.
- **Central** — Palapye/Morupule/Leupane energy cluster, Serowe (Tlou Lesedi), Mahalapye, Letlhakane/Orapa, and industrial/mining towns. Terms: `Palapye` + `data centre`, `Leupane Energy Hub`, `AAAS Energy`, `ChillMine`, `Botala`, `Morupule` + `data`, `Selebi-Phikwe` + `data`, `Serowe` + `data`, `Orapa` + `cloud`; watch power-linked AI/DC speculation and require primary evidence before status upgrades.
- **Selibe Phikwe (town)** — industrial town; terms `Selibe Phikwe` and spelling variant `Selebi-Phikwe` + `industrial` + `data`.
- **Sowa Town** — negative-search protocol.
- **North East** — Francistown surrounds; terms `North East District`, `Masunga`.
- **Francistown (city)** — second city; terms `Francistown` + `data centre`/`colo`/`cloud`, regional press (The Echo), `Francistown City Council`.
- **North West** — Maun; terms `Maun` + `data`, `Ngamiland`, `Okavango`, `Maun solar`.
- **Chobe** — Kasane; SEZA Chobe Connect events; terms `Chobe`, `Kasane` + `data` (very low yield).
- **Ghanzi** — Trans-Kalahari corridor; terms `Ghanzi` + `data` (low yield).
- **Kgalagadi** — Tshabong/Hukuntsi; negative-search protocol.
- **Lobatse (town)** — industrial town; terms `Lobatse` + `data` (low yield).

Negative-search protocol: local press sweep + council site + BOCRA licensee list + named-operator sweep + `data centre/data center/datacentre/server farm/cloud` terms, then record a defensible negative. Do not count cyber cafés, computer labs, bank server rooms or council ICT rooms as datacentres.

---

## 5. Grading, lifecycle and de-duplication rules

- **A facility exists (A)** only when an official operator/government page names the DC and location, or DEA/council/BOCRA/BPC documents identify it. Press alone is B.
- **Capacity claims**: distinguish IT load vs utility load; aggregator MW figures (e.g., Orange ~2 MW) are B/C until an operator source confirms.
- **Cloud != facility**: no operational hyperscaler region in Botswana; hyperscaler mentions are seeds.
- **BDIH cluster dedup**: DDDC (BoFiNet; 1,000 sqm DC1, industry brief says expandable to ~400 racks) and BDIH DC (80 racks) are separate facilities on the same park; do not merge.
- **Lifecycle verbs** drive status: MoU/plan = C/B; construction start = B (A if official); operational/Uptime-certified = verify for A.
- **Aggregator counts differ** (datacentermap ~5, datacenters.com ~8): resolve each entry to an operator page before recording.

---

## 6. Source priority checklist

1. Operator/government page (BoFiNet, BTC, BDIH, Digital Delta, Orange, Unitel, gov.bw).
2. Council development permission / building permit; DEA EA authorization/EIS.
3. BOCRA licence/licensee register; BPC/BERA energy evidence.
4. Uptime Institute certification records.
5. SEZA/BITC/BOSSC official material for investment/zone context.
6. Established local business press (Mmegi, Botswana Guardian, Business Weekly, Weekend Post, Sunday Standard) and trade press (DCD, Connecting Africa, Tech In Africa, Ecofin) for discovery and corroboration.
7. BINX/PeeringDB for interconnection proof; aggregators and vendor case studies as C-level leads only.

---

### Key primary URLs (quick list)
- BoFiNet: https://www.bofinet.co.bw/ ; Digital Delta: https://www.digitaldelta.co.bw/
- BDIH DC: https://www.bih.co.bw/bdih-data-centre/
- BTC Sentlhaga: https://btc.bw/business/sentlhaga-data-center/
- Orange Botswana: https://www.orange.co.bw/ ; Unitel: https://unitel.co.bw/
- BOCRA: https://www.bocra.org.bw/licensing ; BERA: https://www.bera.co.bw/ ; BPC: https://www.bpc.bw/
- gov.bw: https://www.gov.bw/ ; SEZA: https://www.seza.co.bw/ ; BITC: https://www.bitc.co.bw/
- D4D Hub / Xalam Botswana market brief: https://cms.d4dhub.eu/assets/Initiatives/Data-Governance-in-Africa/Digital-Investment-Facility/2507_Country-Market-Briefs/Data-Center-Market-Brief-Botswana.pdf
