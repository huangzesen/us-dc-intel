# SB Explorer Official — Solomon Islands Datacenter Enumeration

Date: 2026-08-12. Status: final source-verification pass. Scope: official/regulatory methodology for enumerating data centers and datacenter-like ICT/telecom facilities in the Solomon Islands (SB): licensing and regulation, planning/building permits, energy/grid approvals, government digital-infrastructure records, cloud-region checks, and per-province query patterns. Reliability grades: **A** = official/primary source (government/regulator/statutory body/SOE page, act/regulation text, official project record); **B** = strong secondary/trade press or named operator/vendor release; **C** = directory/social/aggregate/unverified lead only.

---

## 0. Market shape (official lens)

- Solomon Islands is a **least-developed, small-island state** with a very small datacenter footprint: ISOC Pulse's SB country report lists **1 active data center**, 9 active networks, and ISP share led by Solomon Telekom/Our Telekom. Treat any claimed facility as a notable event and verify it against the sources below. Source: https://pulse.internetsociety.org/en/reports/sb/ (**B** for market indicator; not a facility registry).
- **Capital Territory (Honiara)** on Guadalcanal is the only real hosting/colo geography today. Everything else is cable-landing, provincial-government server rooms, telco network cores, or donor-funded facilities (e.g., the Noro Data Centre in Western Province).
- Market share context (ISOC Pulse 2026, **B** as market indicator): Solomon Telekom Co Ltd ~89% of ISP share, SpaceX Starlink ~23%, SATSOL ~2%, Bemobile Solomon Islands Ltd <1%, Solomon Islands Submarine Cable Company <1%.
- Internet usage ~29% (2024), GCI security score 17.7/100 (2024) — cyber/security readiness is low; do not assume certified Tier facilities exist.

### Verified official anchors (2026-08-12)

| Anchor | Verified URL | Grade | Datacenter use |
|---|---|---:|---|
| Telecommunications regulator | https://www.tcsi.org.sb/ ; about page https://www.tcsi.org.sb/index.php/about ; MCA statutory-body page https://www.mca.gov.sb/about-us/statutory-bodies/regulators/telecommunication-commission-solomon-islands.html | A | Confirms TCSI, not "TSPL", as statutory regulator under the Telecommunications Act 2009. |
| Telecommunications Act 2009 | TCSI copy https://www.tcsi.org.sb/index.php/library/legislation/49-telecommunications-act-2009 ; Parliament copy https://parliament.gov.sb/files/legislation/Acts/Telecommunications_Act%202009.pdf | A | Licence/operator authority; no public DC-specific licence class found. |
| Physical planning authority | https://www.lands.gov.sb/enquiries/physical-planning-enquiries.html ; division page https://www.lands.gov.sb/divisions/physical-planning.html | A | Honiara and provincial Town and Country Planning Boards approve developments in Control of Development Areas; no public online permit search found. |
| Cable operation / SIDN | https://www.tcsi.org.sb/index.php/market/international-connectivity/submarine-cable ; SISCC systems https://siscc.com.sb/systems | A | Official/regulatory confirmation of commercial operation since 1 Feb 2020 and domestic landings Auki, Noro, Taro, Honiara. |
| Noro Data Centre | https://solomons.gov.sb/prime-minister-hands-over-noro-fisheries-mcs-building-and-data-centre/ and https://solomons.gov.sb/prime-minister-hands-over-noro-fisheries-complex-and-provincial-data-centre/ | A | Best confirmed non-Honiara government datacenter/DR lead; Western Province. |
| Second international cable / ACS-1 | AIFFP official page https://www.aiffp.gov.au/investments/investment-list/strengthening-solomon-islands-digital-connectivity and announcement https://www.aiffp.gov.au/news/australia-announces-second-international-submarine-telecommunications-cable-provide-critical-digital-resilience-solomon-islands | A for funding/project; B for contractor details | Connectivity/CLS project; do not count as operational DC before SISCC/AIFFP completion evidence. |

### Naming / regulator note (important)

The parent brief referenced “regulator **TSPL**”. **No official Solomon Islands regulator named “TSPL” was found in this research.** The statutory telecommunications regulator is the **Telecommunication Commission Solomon Islands (TCSI)**, established under the **Telecommunications Act 2009** and operating under the **Ministry of Communication and Aviation (MCA)**. “TSPL” plausibly abbreviates MCA’s *Telecommunications and Postal Services (licensing)* portfolio. Use `TSPL Solomon Islands licence` as a search term, but treat **TCSI / MCA** as authoritative and grade on the actual source.

---

## 1. Official / regulatory backbone

### 1.1 Telecommunications regulation — MCA and TCSI

**Ministry of Communication and Aviation (MCA)** — policy owner; portfolio covers telecommunications, postal services, aviation:

- Ministry site: https://www.mca.gov.sb/ (Joomla; news + tenders at https://www.mca.gov.sb/opportunities/tenders.html)
- Relevant legislation page: https://www.mca.gov.sb/compliance/relevant-legislation.html (Telecommunications Act 2009 PDF at https://www.mca.gov.sb/resources/legislation/4-telecommunications-act-2009.html)
- MCA “ICT Services Development” division: https://www.mca.gov.sb/ict-services.html — national ICT policy / e-government / digital-development role; search for digital-economy and national data-centre items.
- MCA news: watch items like the SiCERT cybersecurity project launch (https://www.mca.gov.sb/news-updates/520-solomon-islands-launches-sicert-project-to-combat-cybersecurity-threats.html) and SINBIP (Solomon Islands National Broadband Infrastructure Project) handovers.

**Telecommunication Commission Solomon Islands (TCSI)** — statutory regulator for licensing, spectrum, competition, pricing, universal access:

- Home: https://www.tcsi.org.sb/
- Legislation library (Telecommunications Act 2009, regulations, gazette notices): https://www.tcsi.org.sb/library/legislation
- Act text (parliament copy): https://parliament.gov.sb/files/legislation/Acts/Telecommunications_Act%202009.pdf
- Gazette notices (e.g., Gazette No. 156 / Supplement No. 61 of 8 Dec 2023, TCSI Directives under s.25 and Part 11A): https://solomons.gov.sb/wp-content/uploads/2023/12/Gaz-No.-156-Sup-No.-61-Friday-8th-December-2023.pdf
- Annual reports / market statistics: https://www.tcsi.org.sb/index.php/library/annual-reports/ (2018–2020 reports listed; request newer by email)
- Technical reports library (incl. “Cable Systems Access, IXP and Caching” which recommends a Honiara IXP): https://tcsi.org.sb/index.php/library/technical-reports/84-cable-systems-access-ixp-and-caching/file
- Submarine cable / international connectivity page: https://tcsi.org.sb/index.php/market/international-connectivity/submarine-cable (confirms SISCC commercial operation since 1 Feb 2020, 4 wholesale operators connected)

A TCSI licence proves telecom/ICT authority, not a physical data center — grade **A for operator/licence existence**, then require facility evidence. The licence types under the Act are essentially network/service licences and radio-frequency licences (individual + class regimes); there is **no public datacenter-specific licence register**.

Queries:

```text
site:tcsi.org.sb ("data centre" OR "data center" OR "cloud" OR "IXP" OR "submarine cable")
site:tcsi.org.sb "annual report" ("data centre" OR "international connectivity" OR "licence")
site:mca.gov.sb ("ICT" OR "digital" OR "broadband") ("data centre" OR "cloud" OR "Honiara")
site:mca.gov.sb ("national data centre" OR "data sovereignty" OR "e-government")
"TSPL" "Solomon Islands" "licence" OR "license" telecommunications
"Telecommunications Act 2009" "Solomon Islands" ("data centre" OR "facility" OR "infrastructure")
"solomon islands" gazette "data centre" OR "data center" OR "cable landing"
```

### 1.2 Planning / building permits

**Ministry of Lands, Housing and Survey — Physical Planning Division** is the national reference point:

- Physical Planning Enquiries: https://www.lands.gov.sb/enquiries/physical-planning-enquiries.html — confirms that **Honiara Town and Country Planning Board** and **Provincial Town and Country Planning Boards** consider/approve developments in **Control of Development Areas**; enquiries go to the relevant provincial government or Honiara City Council.
- Physical Planning Division: https://www.lands.gov.sb/divisions/physical-planning.html — names Honiara, Guadalcanal, Malaita, Western, Choiseul, Isabel, Renbel, Makira, and Temotu Town and Country Planning Boards. Central Province/Tulagi is not named in that list; for Central leads, route enquiries through Central Provincial Government plus MLHS Physical Planning.
- Honiara process (per Ministry of Lands): http://www.honiaracitycouncil.com/rates-business-and-development/building-development-in-honiara/how-to-build-in-honiara/ (page is JS-heavy; use search snippets)
- Legal base: Planning and Development Act (as amended) PDF: https://solomons.gov.sb/wp-content/uploads/2020/02/Planning-and-Development-Act-as-amended.pdf ; historical Town and Country Planning Act; Land and Titles Act governs leasehold/customary land.

Permits are issued by **municipal/provincial boards, not a national e-portal** — there is **no online planning-permit database** equivalent to UK/AU/NZ. Expect to find permit decisions only in: local press reports, HCC council minutes, provincial assembly papers, or project documents of donor-funded works. Grade **A** only when a board resolution/notice/permit names the site; use **B** for named press/project facts and **C** for unsourced directory/social claims.

Queries:

```text
"Town and Country Planning Board" ("data centre" OR "data center" OR "ICT" OR "telecommunications") "Solomon Islands"
"Honiara City Council" ("building permit" OR "planning approval" OR "development application") ("data" OR "telecom" OR "ICT")
"planning permit" "{province}" "Solomon Islands" ("data centre" OR "telecommunications" OR "tower")
"Planning and Development Act" "Solomon Islands" ("telecommunications" OR "ICT infrastructure")
site:lands.gov.sb "planning" "{province}"
site:solomons.gov.sb ("planning" OR "building") ("data centre" OR "telecommunications")
```

### 1.3 Environmental and other project approvals

- EIA responsibility sits with the Ministry of Environment, Climate Change, Disaster Management and Meteorology (MECDM) and provincial/MECDM processes; donor-funded projects publish EIA/PER documents, e.g., the Coral Sea Cable PER hosted on the SPREP Solomon Islands data portal: https://solomonislands-data.sprep.org/system/files/4131708-REP-A-Solomon_Cables_PER.pdf (**A** for the project record).
- Use SPREP data portals and World Bank/ADB project pages to find approval documents for large ICT/energy works (Tina River Hydro, cable projects, provincial powerhouses).

Queries:

```text
site:solomonislands-data.sprep.org ("cable" OR "telecommunications" OR "data") "environmental"
"environment impact assessment" "Solomon Islands" ("data centre" OR "cable landing" OR "telecommunications")
site:adb.org "Solomon Islands" "ICT" OR "cable" OR "broadband"
site:worldbank.org "Solomon Islands" ("telecommunications" OR "electricity" OR "ICT")
```

### 1.4 Energy / grid approvals — Solomon Power and MMERE

**Solomon Islands Electricity Authority (SIEA), trading as Solomon Power** — state utility (established under the Electricity Act framework):

- Site: https://www.solomonpower.com.sb/ (charges, tenders at /careers/tenders/, projects at /project/ and /projects/)
- Current projects page examples: Buala Powerhouse Development (Isabel; diesel gensets), Fiu River Mini Hydro Power Project (500kW, US$15m), Buala Mini Hydro Refurbishment (World Bank), Noro Powerhouse Development (Western; 3×500kW diesel), Honiara Power Station generation upgrade (2×1.5MW Caterpillar), 11kV switchgear, 33kV underground cable.
- Tina River Hydropower Development Project (TRHDP, 15 MW, first utility-scale renewable) + 66kV transmission to the **Honiara national grid via Lungga Power Station**; completion ~early 2028. Sources: https://tina-hydro.com/ ; https://solomonpower.com.sb/projects/66kv-transmission-project/ ; ADB project page https://www.adb.org/projects/50240-001/main ; SMEC appointment https://www.smec.com/general/strengthening-solomon-islands-grid-smec-appointed-for-tina-river-transmission-system/ ; construction news via SIBC (https://www.sibconline.com.sb/cheaper-cleaner-electricity-moves-closer-for-honiara/) and Solomon Star.
- Grid reality: **Honiara grid (Lungga) is the only real grid**; provincial centres are diesel/solar-hybrid **outstations** (Buala, Noro, Gizo, Munda, Auki, Kirakira, Lata, Tulagi, Taro, etc.). Policy owner: Ministry of Mines, Energy and Rural Electrification (MMERE).

Implication for enumeration: any serious DC load must sit on the Honiara grid or have dedicated generation. For provincial facility claims, check Solomon Power project/tender pages and MMERE policy documents; grade **A** when Solomon Power/MMERE documents name the site/load, **B** when press-only.

Queries:

```text
site:solomonpower.com.sb ("data centre" OR "data center" OR "ICT" OR "cloud") OR ("{town}" "powerhouse" OR "grid" OR "connection")
site:solomonpower.com.sb ("Lungga" OR "Honiara" OR "Tina River") ("grid" OR "transmission" OR "renewable")
"Solomon Power" ("data centre" OR "ICT" OR "server") "Honiara"
"Tina River" ("data centre" OR "grid" OR "reliability") "Honiara"
"Electricity Act" "Solomon Islands" ("SIEA" OR "Solomon Power") "licence"
```

### 1.5 Cable landing and ICT infrastructure permits

- **Solomon Islands Submarine Cable Company Limited (SISCC)** — state-backed JV (ICSI 51% / SINPF 49%), operator of CS² and SIDN; official site https://siscc.com.sb/ (systems: https://siscc.com.sb/systems). SISCC is the lead SOE for landing-station infrastructure (Honiara CLS; SIDN landings at Auki, Noro, Taro).
- Second international cable **Adamasia Cable System 1 (ACS-1)** — branch of Google’s Bulikula; Australia-funded (~AU$104m AIFFP); SISCC owner/operator; DXN modular CLS contract AU$1.2m, facility due Apr 2027, cable late 2027 (DCD 2026-08-04, **B**): https://www.datacenterdynamics.com/en/news/dxn-commissioned-to-build-au12m-solomon-islands-cable-landing-station/
- Landing stations are the closest thing to “official facility records” outside Honiara; each CLS is a potential micro-DC/network node to record only with primary evidence (SISCC pages, TCSI cable page, government handover articles).

Queries:

```text
site:siscc.com.sb ("landing station" OR "CLS" OR "SIDN" OR "ACS-1" OR "Adamasia")
site:siscc.com.sb ("Auki" OR "Noro" OR "Taro" OR "Honiara")
"Solomon Islands Submarine Cable Company" ("landing station" OR "data centre" OR "CLS")
"Adamasia" OR "ACS-1" "Solomon Islands" ("landing station" OR "data")
"cable landing station" "Solomon Islands" ("{town}")
```

---

## 2. Government digital-infrastructure records

- **Noro Data Centre (Noro, Western Province)** — the clearest official government DC evidence: PM handover records for the Noro Fisheries MCS Building / Fisheries Complex and Data Centre, 10-13 Nov 2025 (World Bank/FFA/Australia funded; contractors Reeves International and TCS International; Western Provincial Government partner): https://solomons.gov.sb/prime-minister-hands-over-noro-fisheries-complex-and-provincial-data-centre/ and https://solomons.gov.sb/prime-minister-hands-over-noro-fisheries-mcs-building-and-data-centre/ (**A** for announcement and location). Island Sun (2025-11-12) describes backup/data-protection role for critical government records: https://theislandsun.com.sb/noro-hosts-important-offices/ (**B** for function detail). Count as government/provincial DR/data-centre lead; seek operations/capacity details before assigning tier/colo status.
- **National data centre — pipeline signal**: Solomon Star (2025-05-01) reports PM discussions with Huawei on digital transformation incl. “the strategic importance of establishing a national data centre to ensure data sovereignty”: https://www.solomonstarnews.com/pm-acknowledges-huaweis-support-to-telecommunication-service/ (**B**; aspirational, no site confirmed — do NOT count as built).
- **SINBIP** (Solomon Islands National Broadband Infrastructure Project, China-assisted): official government records state the programme targets 161 mobile tower sites; 14 sites were delivered under SINBIP in 2024 and all 161 towers were reported completed/handover in 2026. Sources: https://solomons.gov.sb/solomon-tower-limited-delivered-14-mobile-tower-sites-under-the-solomon-islands-national-broadband-infrastructure-project-sinbip/ and https://solomons.gov.sb/from-vision-to-reality-161-telecommunications-towers-delivered-nationwide/ (**A** for official tower programme). This is provincial connectivity infrastructure, not DCs; use tower sites only as edge-node leads.
- e-government / digital-government records: MCA ICT Services Development division and solomons.gov.sb news; search for e-Government Strategy, National ICT Policy, Data Management/Sharing policy, and SiCERT (CERT-SB) updates.
- **Data protection**: no comprehensive data-protection law confirmed as of this draft; third-party legal summaries (e.g., https://generisonline.com/understanding-data-protection-and-privacy-laws-in-the-solomon-islands/ , Nov 2024) describe a developing landscape (**C**). Do not assume a DP law anchors a hosting/sovereignty requirement; verify any claims against solomons.gov.sb legislation lists.

Queries:

```text
site:solomons.gov.sb ("data centre" OR "data center" OR "national data" OR "e-government")
site:solomons.gov.sb ("digital government" OR "ICT policy" OR "data management")
site:mca.gov.sb ("data centre" OR "data sovereignty" OR "national data" OR "SiCERT" OR "cyber")
"Noro Data Centre" OR "Noro data centre" "Solomon Islands"
"national data centre" "Solomon Islands" (Huawei OR China OR Australia OR ADB)
"Data Protection" "Solomon Islands" bill OR act OR draft
```

---

## 3. Cloud-region checks

No major hyperscaler lists a Solomon Islands public cloud region as of this draft. Check official lists before recording anything:

- AWS regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and Local Zones: https://aws.amazon.com/about-aws/global-infrastructure/localzones/
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations ; Google-owned DCs: https://datacenters.google/locations/
- Oracle OCI public regions: https://www.oracle.com/cloud/public-cloud-regions/

Relevant SB cloud signals are **connectivity-led** (Google’s Bulikula via ACS-1 branch; satellite providers), not regional presence. Record any “cloud” mention as sovereign/partner/local-cloud until a physical in-country facility is evidenced.

Queries:

```text
"Solomon Islands" "AWS" ("region" OR "local zone" OR "edge")
"Solomon Islands" "Azure" OR "Microsoft" "region"
"Solomon Islands" "Google Cloud" OR "Bulikula" OR "ACS-1"
"Solomon Islands" "Oracle Cloud" OR "OCI"
"Solomon Islands" ("cloud region" OR "hyperscale")
```

---

## 4. Per-province enumeration patterns

Solomon Islands coverage unit is **9 provinces + the Honiara Capital Territory**: Central, Choiseul, Guadalcanal, Isabel, Makira-Ulawa, Malaita, Rennell and Bellona, Temotu, Western, and Capital Territory (Honiara). General pattern per division: (1) Honiara/provincial planning office / Town and Country Planning Board for permits; (2) Solomon Power outstation projects for power evidence; (3) SISCC/ACS-1/SINBIP connectivity records; (4) local press (Solomon Star, Island Sun, Solomon Times, SIBC); (5) donor project pages (World Bank, ADB, Australia/AIFFP, China). No division has an online permit search; treat search engines + press + donor records as the enumeration surface.

| Division | Main town / route | Official strategy | Expected DC yield |
|---|---|---|---|
| Capital Territory | Honiara | HCC/Honiara Board, TCSI/MCA, SISCC Honiara CLS, Our Telekom exchange/NOC, Solomon Power Honiara/Lungga grid | High for telco/government/server-room leads |
| Guadalcanal | Henderson, Lungga, Tetere, Tina River corridor | Guadalcanal Board, Solomon Power Lungga/Tina River, airport/industrial-corridor tenders | Medium for Honiara-adjacent power/telecom infrastructure; do not double-count Honiara |
| Central | Tulagi | Central Provincial Government + MLHS Physical Planning; Solomon Power Tulagi/outstation; AIFFP/shipyard search | Low; telecom/power leads only |
| Choiseul | Taro | Choiseul Board, SISCC/SIDN Taro landing, provincial-capital relocation records | Medium for CLS/telecom node; low for DC |
| Isabel | Buala | Isabel Board, Solomon Power Buala powerhouse/mini-hydro, provincial ICT records | Low |
| Makira-Ulawa | Kirakira | Makira Board, Solomon Power Kirakira/outstation, rural connectivity/donor searches | Very low |
| Malaita | Auki | Malaita Board, SISCC/SIDN Auki landing, Solomon Power Auki, provincial admin | Medium for CLS/telecom node; low for DC |
| Rennell and Bellona | Tingoa | Renbel Board, satellite/rural-connectivity and disaster-resilience records | Very low |
| Temotu | Lata | Temotu Board, Lata/Santa Cruz connectivity and airfield/development records | Very low |
| Western | Gizo, Noro, Munda | Western Board, Noro Data Centre, SISCC/SIDN Noro landing, Solomon Power Noro, port/fisheries records | High relative to provinces; Noro DC is confirmed |

### Capital Territory (Honiara) — PRIMARY
Admin: Honiara City Council (HCC); planning via Honiara Town and Country Planning Board. All commercial colo/hosting evidence concentrates here (Our Telekom HQ/exchange, bmobile, SISCC Honiara CLS, banks/state enterprises, government ministries).

```text
site:honiaracitycouncil.com ("data" OR "telecommunications" OR "building permit")
"Honiara" ("data centre" OR "data center" OR "colocation" OR "hosting" OR "server room")
"Honiara" ("Our Telekom" OR "bmobile" OR "SISCC" OR "CLS") ("data" OR "exchange" OR "facility")
"Honiara" ("bank" OR "CBSI" OR "SINPF") "data centre" OR "DR site"
```

### Guadalcanal Province (Honiara sits on Guadalcanal; provincial centre at Honiara/Tetere)
Watch: Henderson airport corridor, Lungga Power Station area, Guadalcanal Plains (Tina River transmission corridor), any industrial estates near Tenaru/Tetere.

```text
"Guadalcanal" ("data centre" OR "data center" OR "telecommunications") "Solomon Islands"
"Lungga" OR "Henderson" OR "Tetere" OR "Tenaru" ("data" OR "ICT" OR "telecom")
"Guadalcanal Provincial Government" ("ICT" OR "digital" OR "data")
"Tina River" "transmission" "Guadalcanal"
```

### Central Province (Tulagi)
Watch: Tulagi Shipyard Rehabilitation (AIFFP-funded; potential industrial/ICT adjacency), provincial admin, Solomon Power outstation.

```text
"Central Province" "Solomon Islands" ("data" OR "ICT" OR "telecommunications")
"Tulagi" ("shipyard" OR "broadband" OR "cable" OR "data")
"Tulagi" "Solomon Power" OR "powerhouse" OR "electricity"
```

### Isabel Province (Buala)
Watch: Solomon Power Buala Powerhouse Development + Buala Mini Hydro Refurbishment (World Bank) — power evidence for any Buala ICT claim.

```text
"Isabel Province" OR "Buala" ("data" OR "ICT" OR "broadband" OR "telecom")
"Buala" ("powerhouse" OR "mini hydro" OR "electricity")
"Buala" "Solomon Power" "diesel" OR "hydro"
```

### Western Province (Gizo / Noro / Munda) — SECONDARY
Watch: **Noro** (fisheries MCS Data Centre 2025, SIDN landing, Solomon Power Noro powerhouse, Noro SEZ/port potential), Gizo (provincial capital, tourism/telecom), Munda (airport, tourism).

```text
"Noro" ("data centre" OR "data center" OR "fisheries" OR "landing station" OR "powerhouse")
"Western Province" "Solomon Islands" ("data" OR "ICT" OR "broadband" OR "cloud")
"Gizo" OR "Munda" ("data centre" OR "telecom" OR "broadband")
"Noro" "World Bank" OR "FFA" "data"
```

### Choiseul Province (Taro)
Watch: Taro SIDN landing station; proposed relocation of provincial capital to Taro Island; satellite-only backhaul beyond cable.

```text
"Choiseul" OR "Taro" "Solomon Islands" ("landing station" OR "cable" OR "broadband" OR "data")
"Taro" "SIDN" OR "cable landing" OR "submarine"
"Choiseul Province" ("ICT" OR "telecommunications" OR "digital")
```

### Malaita Province (Auki)
Watch: Auki CLS (SIDN; opened — Solomon Star https://www.solomonstarnews.com/auki-cable-landing-station-opened-d76/ ), second-largest population, provincial admin.

```text
"Auki" ("cable landing station" OR "data" OR "broadband" OR "ICT")
"Malaita" ("data centre" OR "telecommunications" OR "digital government")
"Auki" "Solomon Power" OR "powerhouse" OR "electricity"
"Malaita Provincial Government" ("ICT" OR "e-services")
```

### Makira-Ulawa Province (Kirakira)
Remote; no cable landing; satellite/microwave backhaul; watch provincial ICT grants and solar mini-grids.

```text
"Makira" OR "Kirakira" ("telecommunications" OR "broadband" OR "solar" OR "data")
"Makira-Ulawa" ("ICT" OR "digital" OR "government")
```

### Temotu Province (Lata)
Most remote populated province (Santa Cruz); watch MCA aviation/airfield works (Santa Cruz Airfield upgrade; Vanikoro geotech) as development signals; satellite-only connectivity.

```text
"Temotu" OR "Lata" ("telecommunications" OR "broadband" OR "data" OR "ICT")
"Santa Cruz" OR "Vanikoro" "Solomon Islands" ("airfield" OR "development")
```

### Rennell and Bellona Province (Tingoa)
Most isolated; no commercial DC potential expected; check only for donor rural-connectivity or disaster-recovery claims.

```text
"Rennell" OR "Bellona" ("telecommunications" OR "satellite" OR "data" OR "connectivity")
```

---

## 5. Trade press / secondary (official-file quick list)

Full operator-facing source map is in `explorer-industry.md`. For official-file backfill: Solomon Star (https://www.solomonstarnews.com/), Island Sun (https://theislandsun.com.sb/), Solomon Times (https://www.solomontimes.com/), SIBC (https://www.sibconline.com.sb/), DataCenterDynamics (https://www.datacenterdynamics.com/en/tags/solomon-islands/), Developing Telecoms, BuddeComm Solomon Islands market report (https://www.budde.com.au/Research/Solomon-Islands-Telecoms-Mobile-and-Broadband-Statistics-and-Analyses). Grade **B** for named/dated project facts; **C** for broad claims.

---

## 6. Honest-confidence notes

- No public national datacenter registry, online permit portal, or DC-specific licence exists; enumeration is triangulation across TCSI/MCA, Ministry of Lands/provincial boards, Solomon Power, SISCC, donor project pages, and press.
- The “1 active data center” (ISOC Pulse 2026) likely corresponds to the telco/government hosting node in Honiara (and/or the Noro DC); both need site-level verification before counting.
- TSPL: not found as an official regulator; treat as an alias for MCA/TCSI licensing functions (see §0 note).
- All per-province templates are seeds; every record must carry a source URL and grade.
