# BW Explorer Official — Botswana Datacenter Enumeration via Planning, Environmental, Energy, Cloud, and Regulator Sources

Date: 2026-08-12. Country: **BW Botswana**. Division model: **16 target divisions** used by this expansion pass (10 district councils + 6 city/town councils: Central; Chobe; Francistown; Gaborone; Ghanzi; Jwaneng; Kgalagadi; Kgatleng; Kweneng; Lobatse; North East; North West; Selibe Phikwe; South East; Southern; Sowa Town). Angle: **official/regulatory/energy/cloud pipeline** for finding commercial, government, telecom and hyperscale data-centre facilities. Status: **final methodology**.

Reliability grades:
- **A** = primary/official/legal source: council development-permission or building permit, DEA (Department of Environmental Affairs) EA authorization / EIS, BOCRA licence or licensee register, BERA/BPC official energy material, official operator or government page (BoFiNet, BTC, BDIH, Ministry pages), official cloud-provider statement.
- **B** = strong secondary source: established local business press (Mmegi, Botswana Guardian, Business Weekly, Weekend Post, Sunday Standard), trade press (DCD, Connecting Africa, Tech In Africa, Ecofin), Uptime Institute certification record, EU/D4D Hub market brief, developer/announcement releases.
- **C** = weak lead: aggregator directories (datacentermap, datacenters.com), generic market reports, social posts, unsupported directory entries.

---

## 0. Botswana-specific structure facts

- Botswana has **no public national data-centre planning register**. Enumeration works by joining: local-authority development permission -> Department of Environmental Affairs (DEA) environmental assessment -> BOCRA telecom/ICT licensing -> BPC/BERA energy evidence -> official operator pages.
- The current public market is small. Confirmed operational facilities are concentrated in Gaborone: BTC's **Sentlhaga Data Center** (official BTC page says Tier II and Uptime-certified), **BDIH Data Centre** (official BDIH page, Plot 69184, Block 8, 80 racks), and BoFiNet's **Digital Delta Data Centre (DDDC)** (official Digital Delta/BoFiNet pages; Tier III constructed-facility certification confirmed by BoFiNet in October 2025; launch reported by official/state and trade sources on 25 November 2025).
- Activity is concentrated in **Gaborone city / South East corridor** (BDIH Block 8 cluster: DDDC + BDIH DC; BTC Sentlhaga; Orange data-centre lead at/near BDIH/New Lobatse Road; Unitel colo lead). Secondary candidates: **Central district** (Palapye/Leupane/Morupule energy cluster, including AAAS Energy + ChillMine announced solar-powered data-centre campus lead), **Francistown / North East**, and **North West / Maun**. Most other divisions should be treated as negative searches unless a telecom exchange, government DC, SEZ, fibre route, mine, or power project appears.
- Coverage note: current gov.bw local-authority pages also expose **Orapa** council listings. This methodology follows the requested 16-division model; sweep `Orapa` as a **Central district alias** so Orapa mining/telecom/power leads are not missed.
- English is sufficient for nearly all official records. Use both `data centre` and `data center`, plus `datacentre`, `server room`, `server farm`, `colo`, `co-location`, `cloud`, `ICT hub`, `Tier III`, `hyperscale`, `MW`, `MVA`, `substation`, `racks`. Setswana is rarely used in official permitting; try it only as a secondary sweep (`lefelo la data`, `polokelo ya data`) and verify against English documents.
- Policy context that drives local hosting: **Data Protection Act 2024** (reported to have come into effect January 2025, succeeding/overhauling the 2018 Act; press links DDDC to data sovereignty), **Smart Botswana / Digital Transformation Strategy (SmartBots 2019–2036)**, Ministry of Communications and Innovation mandate, and the 2025/2026 Cybersecurity Bill/Act debate.
- **No hyperscaler operates a cloud region in Botswana** (checked AWS/Azure/GCP/OCI official region material; nearest regions are South Africa). Treat any hyperscaler mention as a metro/partner/edge seed only, never as facility evidence.

---

## 1. Grade A official portals and regulatory sources

### 1.1 Government of Botswana e-government portal (gov.bw)

- Government Information Portal: https://www.gov.bw/ — central Government Information Portal; the de-facto e-permitting hub. Services relevant to data-centre projects:
  - Environmental Assessment (EA) authorizations: https://www.gov.bw/environmental-management/application-environmental-assessment-ea-authorizations
  - Local authorities directory: https://www.gov.bw/local-authorities-view
  - Ministry of Local Government and Traditional Affairs: https://www.gov.bw/ministries/ministry-local-government-and-traditional-affairs
  - Trade licences, company/entity registration, work & residence permits (via BITC/BOSSC route).
- Ministry pages to site-search:
  - Ministry of Communications and Innovation: https://www.gov.bw/ministries/ministry-communications-and-innovation
  - Ministry of Minerals and Energy: https://www.gov.bw/ministries/ministry-minerals-and-energy (parent of BPC/BERA policy)
  - Ministry of Lands and Agriculture (land administration / DTRP).

Query templates:
```text
site:gov.bw "data centre"
site:gov.bw "data center"
site:gov.bw "data centre" "{district OR town}"
site:gov.bw "server" "cloud" "tender"
site:gov.bw ("Digital Delta" OR "BDIH" OR "BoFiNet")
site:gov.bw "environmental impact" "{operator}"
```

### 1.2 Planning and development permission (local authorities)

- Legal base: **Town and Country Planning Act (Cap 32:09, 1977)** — development permission is granted by the local authority (city/town/district council) as planning authority, with the Department of Town and Regional Planning (DTRP, Ministry of Lands and Agriculture) providing professional input and the Minister deciding appeals. Gaborone City Council is the planning authority for Gaborone (permit chain documented in the World Bank Doing Business Botswana profile: planning + building permit, then occupation permit).
- Botswana councils do **not** publish a public permit-search web portal. Practical route: (a) official council contact/tender notices, (b) web-indexed council minutes/notices, (c) DEA EA records (the most public paper trail), (d) gov.bw and press coverage of approvals.
- Land tenure angle: state land (e.g., BDIH Plot 69184, Block 8) allocated by Ministry of Lands; tribal land via Land Boards under the Tribal Land Act. Record plot numbers when sources give them — they are the most precise district/parcel evidence.

Council query templates:
```text
site:{council-domain} "data centre"
site:{council-domain} "data center"
site:{council-domain} "development permission" OR "planning" "{operator}"
"{council}" "data centre" "plot"
"{town}" "data centre" "development" "approval"
"Gaborone City Council" "data centre"
"{operator}" "{district}" "plot No" "data centre"
```

Extract from permit/planning documents: council, ward/location, plot number, road/industrial park, applicant/SPV, development description, floorspace, rack/data-hall count, IT load MW, utility import MVA, generator/fuel storage, water demand, EA authorization status, construction/occupation dates.

### 1.3 Environmental assessment (DEA)

- Legal base: **Environmental Assessment Act 2011** and **Environmental Assessment Regulations 2012**. Administered by the **Department of Environmental Affairs (DEA)**. The official service page below is the stable route; older direct Act PDF paths on gov.bw move periodically, so use the service page first and then site-search the Act/Regulations by title.
- Route for a data centre: screening -> scoping report & Terms of Reference -> EIS -> EA authorization. Public/consultation notices and EIS summaries are the most externally visible artefacts.
- gov.bw service page (A): https://www.gov.bw/environmental-management/application-environmental-assessment-ea-authorizations
- **EIA tracker (independent, B)**: https://www.eia.co.bw/tracker — community-run tracker of Botswana EIAs; useful discovery but not official.

Query templates:
```text
site:gov.bw "environmental impact" "data"
"{operator}" "environmental impact statement" Botswana
"{town}" "EIS" "Botswana" "data"
"{operator}" "EA authorization" Botswana
site:eia.co.bw "{town OR operator}"
"{operator}" "scoping report" Botswana
```

What to extract: EA reference, proponent, EIA practitioner, plot/coordinates, water & wastewater, diesel/fuel storage, generators, construction period, connected power/substation, public-participation notices, mitigation measures.

### 1.4 BOCRA (Botswana Communications Regulatory Authority)

- Mandate (CRA Act, sec 6(h)): licences, permits, permissions, concessions for telecommunications, internet, radio, broadcasting, postal. HQ Plot 50671 Independence Avenue, Gaborone.
- Licensing page: https://www.bocra.org.bw/licensing
- Framework categories: **Network Facilities Provider (NFP)** — own/operate physical infrastructure used to carry services (fibre, switches, base stations, cables); **Services and Applications Provider (SAP)** — services over NFP infrastructure; **Content Services Provider (CSP)** — broadcasting/content. A commercial data centre offering colocation/cloud/connectivity typically needs NFP (facilities) and/or SAP (services) licensing; legacy licence types (e.g., VANS) still appear in the application dropdown.
- Key documents (BOCRA site, A):
  - ICT licensing framework + documents: https://www.bocra.org.bw/ict-licensing-frameworks
  - ICT licence application requirements and fees: https://www.bocra.org.bw/sites/default/files/documents/ICT_LICENCE_APPLICATION_REQUIREMENTS_AND_FEES.pdf
  - NFP provisional licence application requirements: https://www.bocra.org.bw/sites/default/files/documents/NFP_PROVISIONAL_LICENCE_APPLICATION_REQUIREMENTS.pdf
  - **Licensee list** (search operator names here): https://www.bocra.org.bw/sites/default/files/LATEST%20BOCRA%20LICENSEE%20LIST%20AS%20%40%20END%20OF%20MARCH%202025....xlsx and https://www.bocra.org.bw/sites/default/files/documents/LICENSED_OPERATORS.pdf
  - Online licence verification: https://customerportal.bocra.org.bw/OnlineLicenseVerification/verify ; general online portal: https://op-web.bocra.org.bw/ . BOCRA's ASMS-WebCP registration endpoint is linked from the BOCRA homepage but can fail simple TLS/HEAD checks; prefer navigating to it from https://www.bocra.org.bw/ during live collection.
- Regulatory timeline facts (for notes): BOCRA rejected then licensed **Starlink/SpaceX** (operating licence granted May 2024; service launched ~Aug–Sep 2024) — satellite licensing is a live BOCRA category; BOCRA runs the **Botswana Internet Exchange (BINX)**, AS37771, Gaborone: https://www.binx.org.bw/ and https://www.peeringdb.com/ix/1409 (use PeeringDB participant lists to find which operators actually colocate/peer in-country).

Query templates:
```text
site:bocra.org.bw "data centre" OR "data center"
site:bocra.org.bw "NFP" "{operator}"
site:bocra.org.bw "{operator}" "licence"
"BOCRA" "{operator}" "licence" "data"
"Botswana" "{operator}" "VANS" OR "NFP" OR "SAP"
"{operator}" "BOCRA" "satellite"
```

Use BOCRA records as **operator/service-authority evidence**, not facility-count evidence (one licensee may run several facilities; a facility may be marketed under a parent name).

### 1.5 Government ICT / national data centre / state operators

- **Ministry of Communications and Innovation**: https://www.gov.bw/ministries/ministry-communications-and-innovation — search for `Digital Delta`, `data centres`, `cloud`, `data protection`, `digital transformation`, `SmartBots`.
- **SmartBots / Smart Botswana Strategy (2019–2036)**: https://smartbots.org.bw/strategy — national digital-transformation context. SmartBots government pages also appear under `smartbots.gov.bw` (for example public-sector transformation pages), but the host can be slow/timeout-prone; use search results or gov.bw/BDIH references as corroboration if the page does not load.
- **BDIH (Botswana Digital & Innovation Hub) Data Centre**: https://www.bih.co.bw/bdih-data-centre/ — Plot 69184, Block 8, Science & Technology Park, Gaborone. Official: 80 racks, Tier III compliant, colocation DCaaS, carrier-neutral (BoFiNet, VBN, BTC connected), 2 independent power circuits, UPS + 2 backup generators. Grade A for facility existence/specs.
- **BoFiNet (Botswana Fibre Networks)** — state fibre/backbone operator and DDDC operator: https://www.bofinet.co.bw/ ; DDDC marketing site: https://www.digitaldelta.co.bw/ (data-centre page: https://www.digitaldelta.co.bw/data_centre.php ; grounding-breaking page: https://www.digitaldelta.co.bw/a_new_home_for_your_data.php). DDDC facts verified from official pages: vendor-neutral Tier III data centre, 1,000 sqm DC1, Phase 1 Uptime Institute Tier III certified; located at Botswana Innovation Hub / BDIH Science & Technology Park, Block 8, Gaborone; groundbreaking 11 March 2021. BoFiNet's official news confirms Tier III Certification of Constructed Facility on 23 October 2025 / foil received 29 October 2025: https://www.bofinet.co.bw/news/article/bofinets-digital-delta-data-centre-achieves-tier-iii-certification-from-uptime-institute . Launch date 25 November 2025 is corroborated by official/state-social and DailyNews/trade press; use as A-/B unless a stable BoFiNet launch article is found.
- **BTC (Botswana Telecommunications Corporation)** — converged operator and colo provider: https://btc.bw/business/sentlhaga-data-center/ (Sentlhaga Data Center: BTC states Tier II, Uptime-certified, first certified DC in Botswana; 120 sqm DC floor; rack/power/diesel details should be extracted from the live page at collection time; Gaborone location details beyond BTC's page can be seeded from aggregators only). BTC cloud / Microsoft resale claims are service evidence, not Microsoft-facility evidence.
- **Data Protection Act 2024** (in force Jan 2025 per Botswana Guardian coverage of DDDC launch; earlier 2018 Act context) and the **Data Protection Act 2018** debate — official context for data-residency demand; search `site:gov.bw "Data Protection"`.

Query templates:
```text
site:bih.co.bw "data centre"
site:bofinet.co.bw "data centre" OR "Digital Delta"
site:digitaldelta.co.bw rack OR MW OR power
site:btc.bw "data centre" OR "Sentlhaga"
site:gov.bw "data protection" "data centre"
```

---

## 2. Power, grid, and energy evidence

- **Botswana Power Corporation (BPC)** — state utility (BPC Act; est. 1970), sole generator/transmitter/distributor/retailer: https://www.bpc.bw/. Data centres connect as large-power users; look for connection applications, dedicated feeders, substations, power-supply agreements, tariff approvals (BPC raised tariffs ~22% in 2020; cost-reflective tariff debate ongoing).
- **Botswana Energy Regulatory Authority (BERA)** — established by BERA Act 2016, operating since Sep 2017: https://www.bera.co.bw/. Electricity is governed by BERA Act + Electricity Supply Act + BPC Act. BERA authorises construction of significant electricity infrastructure and issues **generation licences** (e.g., Sese Power ~300 MW Mmamabula coal; Tlou Energy Lesedi CBM 10 MW PPA; Energy & Natural Resource Corp). Use BERA's electricity regulation page for current generation-licence and authorisation download links: https://www.bera.co.bw/electricity.php
- For a data centre: grid import via BPC is the norm; on-site diesel gensets for backup (fuel storage may trigger environmental/health approvals); on-site solar/embedded generation above thresholds may require BERA authorisation — verify per-project.
- **Generation geography** (useful for district seeds): Morupule A (~132 MW) and Morupule B (~600 MW) coal plants at **Palapye, Central District** (≈80% of domestic generation); Mmamabula coal site near the South Africa border (Central District); Tlou Lesedi CBM near Serowe (Central); utility-scale solar IPPs emerging around Jwaneng (Southern), Mmadinare (Central) and Maun (North West) — check BERA licences for exact locations.
- International interconnection: BoFiNet has capacity/consortium stakes in WACS, EASSy, EIG, Equiano; terrestrial fibre to WACS landing at Swakopmund (with Paratus) and to Johannesburg (with Broadband Infraco) — i.e., Gaborone is the natural interconnection hub.

Power query templates:
```text
site:bpc.bw "data centre" OR "data center"
site:bpc.bw "{operator}" "MVA" OR "substation"
site:bera.co.bw "generation licence" "{operator}"
site:bera.co.bw "{town}" "solar" OR "power"
"{operator}" "Botswana Power Corporation" "supply"
"{project}" "dedicated substation" Botswana
"{project}" "BPC" "power purchase" OR "connection"
"Morupule" "data centre"
"Palapye" "data centre" OR "data center"
```

What to extract: connection size MVA/MW, voltage level, customer/operator, substation/feeder, energisation date, power-supply agreement, standby generation, on-site solar claims, tariff class, and whether capacity is IT load or utility load.

---

## 3. Official cloud-region and edge signals

| Provider | Official source | Botswana signal | How to use |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Botswana region in official list (Africa: South Africa operational). | Tenant/partner/edge lead only; never infer an AWS facility in BW. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Botswana region listed. Azure reach in Botswana is via BTC Cloud Connect (Microsoft 365/Azure marketplace resold by BTC), not an Azure-owned facility. | Search BTC/BOCRA evidence only; mark as resale/partner presence. |
| Google Cloud | https://cloud.google.com/about/locations | No Botswana region. | Edge/partner lead only. |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No Botswana region (Africa: Johannesburg, Casablanca in official list). | Seed only. |
| Edge/POPs (Azure Front Door, CDNs) | vendor edge-location pages | Gaborone edge presence not confirmed in checked pages; treat as unverified lead. | Use to seed colocation/interconnection searches, not facilities. |

Cloud query templates:
```text
"Botswana" "cloud region"
"Gaborone" "Azure" OR "AWS" OR "Google Cloud" OR "Oracle" "data center"
"Botswana" "sovereign cloud"
"BTC" "Microsoft" "cloud" Botswana
site:aws.amazon.com Botswana
site:learn.microsoft.com Botswana "edge"
```

---

## 4. Official/operator facility seed list

Operator/government pages are primary statements of marketed facility existence and location. They are not substitutes for permit/EA/power evidence when grading construction status.

| Operator / project | Official source | Botswana footprint signal | Follow-up joins |
|---|---|---|---|
| BoFiNet Digital Delta Data Centre (DDDC / Digital Delta DC1) | https://www.bofinet.co.bw/ , https://www.digitaldelta.co.bw/ , https://www.digitaldelta.co.bw/data_centre.php | Gaborone, BDIH Science & Technology Park, Block 8; vendor-neutral; official Digital Delta page states 1,000 sqm DC1 and Phase 1 Tier III certification; BoFiNet confirms Uptime Tier III Constructed Facility certification in Oct 2025; launch date 25 Nov 2025 is press/state-news corroborated. D4D/industry sources describe expansion potential up to ~400 racks. | DEA EA record, GCC/planning record, BPC connection, BOCRA licensing, DCD/press for capacity; constructor Zhong Gan/CJIC. |
| BDIH Data Centre | https://www.bih.co.bw/bdih-data-centre/ | Plot 69184, Block 8, BDIH, Gaborone; 80 racks; Tier III compliant; DCaaS colocation; carrier-neutral | Same joins; BDIH tenders/annual reports; BPC feed. |
| BTC Sentlhaga Data Center | https://btc.bw/business/sentlhaga-data-center/ | Gaborone (Saint Josephs Rd per datacentermap); Tier II Uptime-certified; 120 sqm; 5 kW/rack; BTC Cloud Connect (Microsoft 365) | BTC annual reports, BOCRA register, Uptime Institute record, BPC feed evidence. |
| Orange Botswana Data Center | https://www.orange.co.bw/ ; listing https://www.datacenters.com/orange-business-botswana | New Lobatse Road, Gaborone; ~2 MW (aggregator figure — B) | BOCRA register, DEA, BPC; official Orange pages/case studies. |
| Unitel (Universal Telecom) | https://unitel.co.bw/ | BOCRA-licensed, Gaborone; fibre backbone + colocation/data-centre service (marketing-level claim — B/C) | BOCRA register, Unitel site, BPC. |
| AAAS Energy + ChillMine Palapye / Leupane data-centre campus | AAAS company site https://aaas.energy/ ; company press release via EIN; Botala/AAAS Leupane energy-hub disclosures | **Announced / MoU lead only** near Palapye, Central District; proposed solar+BESS-powered AI/hyperscale campus tied to Leupane/Botala energy hub. Do not count as operational or under construction until permit/EA, BERA/BPC, land, or operator construction evidence appears. | Search Botala Energy, AAAS Energy, ChillMine, Leupane, Palapye, BERA, BPC, DEA, council planning, and ASX/BSE disclosures. |
| Mascom / Orange / BTC core-network rooms | operator pages | Telecom internal data centres in Gaborone (Tsholetsa House etc.); not marketed as public colo | Record only if marketed as colo/cloud/Tier facility; otherwise note as internal. |

Operator query templates:
```text
"{operator}" "Botswana" "data centre" "MW"
"{operator}" "Botswana" "data center" "racks"
"{operator}" "BOCRA" licence
"{facility}" "Uptime Institute" Botswana
"Digital Delta" "BoFiNet"
"Sentlhaga" "BTC" "data centre"
"AAAS Energy" "ChillMine" "Palapye" "data center"
"Leupane Energy Hub" "data centre" OR "data center"
"{operator}" "plot No" Gaborone
```

---

## 5. Per-division enumeration strategy (16 divisions)

### 5.1 Standard per-division workflow
1. Official-domain sweep: gov.bw (ministry + service pages), BOCRA licensee list, BERA/BPC, DEA EA records, operator pages (BoFiNet/BTC/BDIH/Orange/Unitel), council notices, SEZA (if zone), BITC/BOSSC (if investor).
2. Search English variants: `data centre`, `data center`, `datacentre`, `server farm`, `server room`, `cloud`, `colo`, `co-location`, `Tier III`, `hyperscale`, `AI data centre`, `MW`, `MVA`, `substation`, `racks`.
3. Named-operator and anchor sweep: `BoFiNet`, `Digital Delta`, `BDIH`, `BTC`, `Sentlhaga`, `Orange`, `Unitel`, `Mascom`, `Liquid`, `Huawei`, `Starlink`, `Microsoft`, `AWS`, `Oracle`, `Teraco`, `Africa Data Centres`.
4. For each lead, obtain at least one primary source (operator page, permit/EA, BOCRA licence, BPC/BERA, or government announcement) before grading A; press fills capacity/status gaps only.

### 5.2 Division-by-division notes

- **Gaborone (city)** — highest density: BDIH (DDDC + BDIH DC, Block 8), BTC Sentlhaga, Orange Botswana (New Lobatse Rd), Unitel, telecom core sites, SSKIA SEZ adjacency. Query: `site:gov.bw`, `Gaborone City Council`, `Block 8`, `plot No`, operator names; search `Phakalane`, `Western Bypass`, `Tlokweng Road`, `Notwane`, `Gaborone West` industrial plots.
- **South East (district)** — Gaborone surroundings (Tlokweng, Ramotswa), SSKIA SEZ. Expect mostly edge/industrial leads; query `South East District Council`, `Tlokweng`, `SSKIA SEZ`, `airport` + `data`.
- **Kweneng (district)** — Molepolole, Mogoditshane (Gaborone exurb — possible spill-over industrial plots). Query `Kweneng District Council`, `Molepolole`, `Mogoditshane`, `data centre`.
- **Kgatleng (district)** — Mochudi; low yield. Query `Kgatleng District Council`, `Mochudi`, `data centre`.
- **Southern (district)** — Kanye, Moshupa, Jwaneng town; Jwaneng mine power/solar context. Query `Southern District Council`, `Jwaneng`, `Kanye`, `solar` + `data`.
- **Jwaneng (town)** — Debswana mine power assets; unlikely DC. Negative-search protocol.
- **Central (district)** — largest district; **Palapye/Morupule/Leupane energy cluster** (coal power, solar/BESS, future DC power-play interest), Serowe (Tlou Lesedi), Mahalapye, Letlhakane/Orapa (Debswana). The AAAS Energy + ChillMine Palapye/Leupane campus is an announced/MoU lead only until primary permits/energy/construction evidence appears. Query `Central District Council`, `Palapye`, `Morupule`, `Leupane`, `AAAS Energy`, `ChillMine`, `Botala`, `Serowe`, `Orapa`, `data centre`, `power`.
- **Selibe Phikwe (town)** — former mining town, industrial land, SEZ candidate. Query `Selibe Phikwe Town Council`, `data centre`, `industrial`.
- **Sowa Town** — soda-ash mining town; negative-search protocol.
- **North East (district)** — Francistown surrounds (Masunga, Tutume). Query `North East District Council`.
- **Francistown (city)** — second city; BTC/BoFiNet regional nodes, possible edge colo. Query `Francistown City Council`, `Francistown` + `data centre`, regional press (The Echo).
- **North West (district)** — Maun tourism hub, Ngamiland/Okavango; Maun solar; fibre to Namibia. Query `North West District Council`, `Maun`, `data centre`, `solar`.
- **Chobe (district)** — Kasane tourism gateway (SEZA 'Chobe Connect' events); very low yield. Query `Chobe District Council`, `Kasane`.
- **Ghanzi (district)** — western corridor (Trans-Kalahari Highway); low yield. Query `Ghanzi District Council`.
- **Kgalagadi (district)** — Tshabong/Hukuntsi; negative-search protocol.
- **Lobatse (town)** — industrial town (South East); low yield. Query `Lobatse Town Council`.

Negative-search protocol (defensible record): official district/council site + BOCRA licensee list + DEA EA sweep + named-operator sweep + `data centre/data center/datacentre/server farm/cloud` terms. Do not record data-collection offices, cyber cafés, computer labs, bank server rooms or council ICT rooms as datacentres unless the source describes actual hosting/colo/cloud infrastructure.

---

## 6. Practical grading and de-duplication rules

- **Facility exists (A)** only when an official operator/government page names the DC and location, or DEA/council/BOCRA/BPC documents identify it.
- **Under construction (A/B)** only with official/government/operator evidence of construction start; trade press alone is B unless it reproduces an official announcement.
- **Capacity (MW)**: distinguish IT load from utility load; do not convert MVA to MW unless the source states a conversion.
- **Cloud != facility**: hyperscaler mentions are seeds only; no operational BW region found.
- **BDIH cluster dedup**: DDDC (BoFiNet; 1,000 sqm DC1, industry brief says expandable to ~400 racks) and BDIH DC (80 racks) are two distinct facilities on the same park — do not merge; cross-check BDIH tenders for who operates the BDIH-branded DC.
- **Telecom internal rooms**: Mascom/Orange/BTC core-network rooms are not commercial DCs unless marketed as colo/cloud/Tier facilities.
- **Aggregator counts differ**: datacentermap lists ~5 facilities/3 operators; datacenters.com lists ~8; use them as discovery only and resolve each entry to an operator page.

---

## 7. Source priority checklist

1. Council development permission / building permit or official notice.
2. DEA EA authorization / EIS (Environmental Assessment Act 2011).
3. BOCRA licence / licensee register (NFP/SAP/VANS categories).
4. BPC/BERA official grid, tariff or licence evidence.
5. Official government/operator pages: gov.bw, BoFiNet, BTC, BDIH, Digital Delta, Ministry of Communications and Innovation.
6. SEZA (SEZ incentives/zones), BITC/BOSSC (investor route).
7. Uptime Institute certification records and official developer releases.
8. Local business press and trade press for discovery and secondary corroboration.

---

### Key primary URLs (quick list)
- gov.bw portal: https://www.gov.bw/
- EA authorization service: https://www.gov.bw/environmental-management/application-environmental-assessment-ea-authorizations
- BOCRA licensing + licensee list: https://www.bocra.org.bw/licensing
- BERA: https://www.bera.co.bw/ ; BPC: https://www.bpc.bw/
- BDIH DC: https://www.bih.co.bw/bdih-data-centre/
- BoFiNet: https://www.bofinet.co.bw/ ; Digital Delta: https://www.digitaldelta.co.bw/
- BTC Sentlhaga: https://btc.bw/business/sentlhaga-data-center/
- SmartBots: https://smartbots.org.bw/strategy
- SEZA: https://www.seza.co.bw/ ; BITC/BOSSC: https://www.bitc.co.bw/
