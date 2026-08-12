# SB Explorer Industry — colo providers, cloud, trade press, and province queries

Date: 2026-08-12. Status: final source-verification pass. Scope: industry/vendor-side methodology for enumerating data centers and datacenter-like ICT/telecom facilities in the Solomon Islands (SB): operator and colo seed list, cloud/sovereign-cloud sweep, connectivity pivots, trade press, directories, and repeatable per-province query templates. Reliability grades: **A** = official/primary (operator page, SOE/government page, regulator, cloud-provider official region list, contractor project page); **B** = strong secondary/trade press/local business press/vendor case study with named details; **C** = directory/map/social/market-report snippet/unverified lead only.

---

## 0. Solomon Islands-specific frame

- No public national datacenter registry exists. Enumeration works by triangulating **operator pages**, **state-owned enterprise (SOE) pages** (SISCC, Solomon Power, Our Telekom, SINPF/ICSI portfolio), **MCA/TCSI licensing and policy material**, **donor project records** (World Bank, ADB, Australia/AIFFP, China), **subsea cable/IXP sources**, **trade press**, and **directories**.
- Tiny market: ISOC Pulse's SB report lists **1 active data center**, 9 active networks, ~29% internet penetration, and an ISP market dominated by Solomon Telekom (~89%), with Starlink (~23%) and SATSOL (~2%) notable: https://pulse.internetsociety.org/en/reports/sb/ (**B** — useful market indicator, not a facility register).
- Hard facility evidence is concentrated in **Honiara (Capital Territory)**; the only confirmed non-Honiara government facility is the **Noro Data Centre (Western Province)**, handed over Nov 2025. Secondary watch sites are cable landings (Auki/Malaita, Noro/Western, Taro/Choiseul), provincial capitals with donor power/ICT works (Buala/Isabel, Tulagi/Central), and the ACS-1 landing (site TBD, CLS due Apr 2027).
- Sources are English-language. Search both `data centre` and `data center`, plus `datacenter`, `colocation`, `co-location`, `hosting`, `server room`, `DR site`, `disaster recovery`, `cloud`, `sovereign cloud`, `government cloud`, `e-government`, `IXP`, `cable landing station`, `CLS`, `SIDN`, `CS2`, `Coral Sea Cable`, `Bulikula`, `ACS-1`, `Adamasia`, `tower`, `SINBIP`, `microwave`, `VSAT`, `Starlink`, `Kacific`, `O3b`.
- **Local-language (Pijin) searching has very low yield** for commercial DCs. Use sparingly: `data senta`, `stoa blong data`, `intanet`, `kabel`, `taoa`, `pawa`, `gavman`, `seva`. Verify all hits against English official/operator sources.
- Do not overcount: in SB, “data centre” often means a cable landing station, telco network core/ops room, provincial server room, fisheries MCS facility, cloud product, or donor project room. Count a record only with a physical facility/operator, hosting/compute/colo/DR function, and a town/province/site signal.

---

## 1. Source map and grades

### 1.1 Primary / official sources

| Source | URL | Use | Grade |
|---|---|---|---|
| Solomon Islands Submarine Cable Company (SISCC) | https://siscc.com.sb/ ; systems https://siscc.com.sb/systems | SOE operator of CS² + SIDN; cable/CLS status, wholesale operators (4 connected since Feb 2020), ACS-1/Bulikula progress, landing towns (Honiara, Auki, Noro, Taro). | A |
| Our Telekom (Solomon Telekom Co Ltd) | https://www.ourtelekom.com.sb/ ; exchange/data-centre article https://www.ourtelekom.com.sb/sinpf-board-members-and-sinpf-investment-team-visit-our-telekom/ | Incumbent telco (~89% ISP share); operator article confirms Honiara technical premises, data hosting systems, Exchange Building, main Data Centre room, and NOC. JV: SINPF 97.32% / ICSI 2.68% on the same operator article. | A for operator pages and room existence; B/C until hosting/colo product and current operating status are confirmed |
| bmobile-Vodafone Solomon Islands | https://www.bmobile.com.sb/ | Mobile operator (ATH/Vodafone brand; Bemobile Solomon Islands Ltd, AS132462); operates in Guadalcanal, Malaita, Western, Central provinces; HQ Mendana Ave, Honiara. Usually network-core infrastructure; count only with hosting/colo/DR evidence. | A for operator pages; B/C for facilities |
| SATSOL Limited | https://satsol.net/ | Local ISP / digital TV / Starlink business reseller; rural/provincial connectivity; possible VSAT/head-end sites in Honiara — not colo unless a primary facility page says so. | A for operator page; B/C for facility inference |
| Solomon Islands Submarine Cable Company — PeeringDB org | https://www.peeringdb.com/org/23922 | Interconnection presence of SISCC; proves network layer, not DC capacity. | B/C |
| TCSI — submarine cable page | https://tcsi.org.sb/index.php/market/international-connectivity/submarine-cable | Regulator confirmation of SISCC commercial operation and wholesale operators. | A |
| Solomon Power (SIEA) | https://www.solomonpower.com.sb/ | Grid/outstation evidence for any large-load or provincial facility claim (Lungga/Honiara grid, Tina River, Buala/Noro/Fiu). | A/B |
| Ministry of Communication and Aviation (MCA) | https://www.mca.gov.sb/ | Policy/digital-development; SiCERT, SINBIP, ICT Services Development; national data-centre and data-sovereignty statements. | A |
| TCSI | https://www.tcsi.org.sb/ | Licensing context for all operators; annual reports and market stats; IXP/caching technical report (recommends Honiara IXP). | A |
| Noro Data Centre handover (SIG) | https://solomons.gov.sb/prime-minister-hands-over-noro-fisheries-mcs-building-and-data-centre/ | Government record of the Noro (Western Province) data centre/DR facility, Nov 2025. | A for announcement; B until ops details |
| Island Sun — Noro DC article | https://theislandsun.com.sb/noro-hosts-important-offices/ | Confirms Noro DC role as government backup/DR site (“major disasters affecting Honiara”). | B |
| Solomon Star — Huawei / national DC | https://www.solomonstarnews.com/pm-acknowledges-huaweis-support-to-telecommunication-service/ | 2025 signal that a national data centre is discussed for data sovereignty — pipeline only. | B |
| DataCenterMap Solomon Islands | https://www.datacentermap.com/solomon-islands/ and SATSOL profile https://www.datacentermap.com/c/satsol-limited/ | Directory lead source. Its SATSOL profile claims a Honiara data center with backup/cooling/security, but this is **C only** until SATSOL publishes the facility or another primary/strong secondary source confirms it. | C |
| Wikipedia — Telecommunications in Solomon Islands | https://en.wikipedia.org/wiki/Telecommunications_in_the_Solomon_Islands | Quick operator/network context (STCL/Our Telekom, bmobile, TTV, Satsol). | C (use only as seed) |

### 1.2 Trade press, local press, directories

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Solomon Star | https://www.solomonstarnews.com/ | Best local press for ICT/cable/power project news (Auki CLS opening, Huawei/PM national DC, Tina River, SINBIP towers). | B |
| Island Sun | https://theislandsun.com.sb/ | Daily; Noro DC, Our Telekom/Solomon Tower deal, government ICT stories. | B |
| Solomon Times | https://www.solomontimes.com/ | Business/ICT coverage; search `data centre`, `cable`, `telecom`. | B/C |
| SIBC | https://www.sibconline.com.sb/ | National broadcaster; project milestones (Tina River transmission construction etc.). | B |
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/tags/solomon-islands/ | International DC/cable coverage: ACS-1/DXN CLS (2026), Coral Sea Cable, connectivity. | B |
| Developing Telecoms | https://developingtelecoms.com/ | bmobile-Vodafone/SpeedCast backhaul, Pacific telecom upgrades. | B |
| BuddeComm | https://www.budde.com.au/Research/Solomon-Islands-Telecoms-Mobile-and-Broadband-Statistics-and-Analyses | Market stats; operator list incl. Kacific, O3b, Interchange Ltd, SISCC. | B/C |
| Submarine Networks / SubTel Forum / TeleGeography map | https://www.submarinenetworks.com/en/systems/asia-australia/coral-sea/coral-sea-cable-system-overview ; https://subtelforum.com/coral-sea-cable-installed-in-papua-new-guinea-solomon-islands/ ; https://www.submarinecablemap.com/ | CS² and SIDN route/landing detail; ACS-1 updates. | B/C |
| ISOC Pulse | https://pulse.internetsociety.org/en/reports/sb/ | 1 active DC, 9 networks, ISP shares, IXP/caching status. | B (indicator context) |
| LinkedIn/Facebook (Our Telekom, SISCC, bmobile, ministers) | operator pages | Launch/handover photos and announcements; discovery only. | C/B- |

High-value trade queries:

```text
site:datacenterdynamics.com/en/news/ "Solomon Islands" ("data center" OR "data centre" OR "cable")
site:datacenterdynamics.com/en/news/ ("SISCC" OR "ACS-1" OR "Adamasia" OR "Bulikula" OR "Coral Sea")
site:solomonstarnews.com ("data centre" OR "data center" OR "cable" OR "broadband")
site:theislandsun.com.sb ("data centre" OR "Noro" OR "telecom" OR "digital")
site:solomontimes.com ("data centre" OR "cloud" OR "ICT" OR "cable")
site:sibconline.com.sb ("Tina River" OR "data" OR "broadband" OR "grid")
site:developingtelecoms.com "Solomon Islands"
"Solomon Islands" "data centre" OR "data center" 2023..2026
```

---

## 2. Operator, colo, and telecom seed list

| Operator / developer | Primary / useful URL | SB geography signals | Notes |
|---|---|---|---|
| Solomon Telekom Co Ltd — Our Telekom | https://www.ourtelekom.com.sb/ | Honiara HQ/exchange; national fixed/mobile network; TTV subsidiary | Incumbent with the largest in-country hosting/telco infrastructure. Search `enterprise`, `hosting`, `business`, `cloud`, `leased line`, `data`. |
| bmobile-Vodafone (Bemobile Solomon Islands Ltd) | https://www.bmobile.com.sb/ ; AS132462 | Honiara HQ (Mendana Ave); Guadalcanal, Malaita, Western, Central provinces | 3G/4G mobile; enterprise backhaul via SpeedCast (Developing Telecoms, B). Count only explicit hosting/colo/DR. |
| SATSOL Limited | https://satsol.net/ | Honiara; provincial wireless/Starlink services | Local ISP/digital TV/Starlink reseller. DataCenterMap has a Honiara DC claim; hold at C pending SATSOL confirmation. |
| SISCC | https://siscc.com.sb/ | Honiara CLS (Lengakiki); Auki, Noro, Taro SIDN landings; ACS-1 site TBD | Wholesale cable operator; CLSs are micro-DC candidates — verify with primary pages. |
| Solomon Tower Limited (STL) | official SINBIP records: https://solomons.gov.sb/solomon-tower-limited-delivered-14-mobile-tower-sites-under-the-solomon-islands-national-broadband-infrastructure-project-sinbip/ ; https://solomons.gov.sb/from-vision-to-reality-161-telecommunications-towers-delivered-nationwide/ ; Our Telekom/STL press via Island Sun https://theislandsun.com.sb/our-telekom-and-solomon-tower-sign-landmark-agreement/ | National tower portfolio (161 towers via SINBIP; STL-Our Telekom agreement) | Tower infrastructure, not DCs; edge-node leads only. |
| Interchange Limited | BuddeComm list; local search | Honiara ISP/telecom | Small ISP/telecom; verify status via TCSI/licence and press. |
| TTV (Solomon Telekom TV subsidiary) | Wikipedia/Our Telekom | Honiara broadcast | Broadcast head-end, not colo. |
| Central Bank of Solomon Islands (CBSI) | https://www.cbsi.com.sb/ | Honiara | Enterprise DR/hosting; check annual reports for IT infrastructure projects. |
| SINPF / ICSI | https://www.sinpf.org.sb/ ; ICSI pages | Honiara; SISCC & Our Telekom shareholder | Shareholder context; any data-centre procurement by SINPF/ICSI portfolio companies. |
| Noro Fisheries MCS Data Centre | solomons.gov.sb handover (see §1.1) | Noro, Western Province | Government DR/backup DC (World Bank/FFA/Australia; Reeves International + TCS International contractors). |
| Commercial banks (BSP, ANZ, Westpac, NBC) | bank sites | Honiara branches | Enterprise server rooms/DR sites; capture only with press/tender evidence. |

Operator sweep templates:

```text
site:ourtelekom.com.sb ("data" OR "hosting" OR "enterprise" OR "cloud" OR "business")
site:bmobile.com.sb ("data" OR "enterprise" OR "cloud" OR "business")
site:siscc.com.sb ("landing station" OR "CLS" OR "data" OR "wholesale")
"Our Telekom" ("data centre" OR "data center" OR "server" OR "hosting") "Honiara"
"bmobile" ("data centre" OR "core network" OR "server") "Honiara"
"SINPF" OR "ICSI" ("data centre" OR "ICT" OR "infrastructure")
"CBSI" OR "Central Bank of Solomon Islands" ("data centre" OR "DR" OR "IT infrastructure")
"Solomon Tower" ("data" OR "edge" OR "ICT" OR "tower")
```

---

## 3. Cloud-region and sovereign-cloud sweep

No global hyperscaler public cloud region exists in Solomon Islands as of this pass. Do not infer a region from sales/partner/reseller presence. Use official lists for A-grade absence/presence and operator/SOE pages for in-country sovereign facilities.

| Provider | Official page / route | SB signal | Grade |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Local Zones https://aws.amazon.com/about-aws/global-infrastructure/localzones/ | No SB Region/Local Zone found. | A for absence |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No SB public region found; nearest practical regions are Australia/SEA. | A |
| Google Cloud | https://cloud.google.com/about/locations ; https://datacenters.google/locations/ | No SB region/owned DC. Google relevant only via Bulikula (Pacific Connect) and its ACS-1 branch — connectivity, not cloud region. | A for region list; B for cable press |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No SB public region found. | A |
| Sovereign/local cloud | SIG/SOE announcements, MCA digital-government docs | National data-centre discussion (Huawei, 2025) and Noro DC are the only sovereign-hosting signals; both need status verification. | B until physical/operational evidence |

Queries:

```text
"Solomon Islands" ("AWS region" OR "Azure region" OR "Google Cloud region" OR "OCI region")
"Solomon Islands" "sovereign cloud" OR "government cloud" OR "national data centre"
"Solomon Islands" ("data residency" OR "data sovereignty") "data centre"
"Solomon Islands" ("Starlink" OR "Kacific" OR "O3b") ("data centre" OR "gateway" OR "edge")
```

---

## 4. Connectivity and interconnection pivots

Facility discovery in SB is often easier through cable/network records than through real estate.

| Pivot | Source / URL | How to use | Grade |
|---|---|---|---|
| Coral Sea Cable System (CS²) | https://siscc.com.sb/systems ; https://www.coralseacablecompany.com/the-system ; https://www.coralseacablesystem.com.au/countries/solomon-islands | Sydney–Honiara international cable (2 fibre pairs, up to 20 Tbps); commercial since Feb 2020; Honiara landing (Lengakiki CLS). Landing stations = candidate micro-DC nodes. | A/B |
| Solomon Islands Domestic Network (SIDN) | SISCC systems page; Solomon Star Auki CLS article https://www.solomonstarnews.com/auki-cable-landing-station-opened-d76/ | 730km domestic cable Honiara–Auki–Noro–Taro; each landing is a provincial connectivity node. | A/B |
| Adamasia Cable System 1 (ACS-1) | DCD 2026-08-04 https://www.datacenterdynamics.com/en/news/dxn-commissioned-to-build-au12m-solomon-islands-cable-landing-station/ ; SISCC news | Second international cable; Bulikula (Google) branch; AIFFP-funded ~AU$104m; DXN modular CLS due Apr 2027, cable late 2027; landing site TBD — watch for site announcements. | B |
| IXP / caching | TCSI technical report (https://tcsi.org.sb/index.php/library/technical-reports/84-cable-systems-access-ixp-and-caching/file) ; ISOC Pulse | Honiara IXP recommended (Marketplace IXP proposal); treat as planned until an operator/TCSI confirms live peering. | B/C |
| Satellite (Starlink, Kacific/O3b, SpeedCast backhaul) | ISOC Pulse ISP shares; Developing Telecoms bmobile-SpeedCast article | Provincial connectivity layer; Starlink ~23% share (B); gateways/VSAT head-ends are edge candidates, not DCs. | B/C |
| SINBIP (China-assisted broadband, 161 towers) | MCA news; Solomon Star Jul 2026 | Provincial tower/backhaul program; edge-node leads per province. | B |

Connectivity queries:

```text
"Coral Sea Cable" ("Honiara" OR "landing" OR "CLS" OR "Lengakiki")
"Solomon Islands Domestic Network" OR SIDN ("Auki" OR "Noro" OR "Taro" OR "Honiara")
"ACS-1" OR "Adamasia" "Solomon Islands" ("landing" OR "CLS" OR "site")
"Bulikula" "Solomon Islands" OR "SISCC"
"Solomon Islands" "IXP" OR "Internet Exchange" Honiara
site:peeringdb.com ("Solomon Islands" OR "Honiara")
```

---

## 5. National query templates

### 5.1 Facility discovery

```text
"Solomon Islands" ("data centre" OR "data center" OR "datacenter" OR "colo" OR "colocation" OR "hosting")
"Solomon Islands" ("data centre" OR "data center") (Honiara OR "Capital Territory" OR Guadalcanal OR Malaita OR Western OR Isabel OR Choiseul OR Central OR "Makira-Ulawa" OR Makira OR Temotu OR Rennell OR Bellona)
"Solomon Islands" ("server room" OR "DR site" OR "disaster recovery" OR "backup site") ("government" OR "bank" OR "ministry")
"Solomon Islands" ("cloud" OR "sovereign cloud" OR "government cloud") ("data centre" OR "provider")
"Solomon Islands" "data centre" (2021 OR 2022 OR 2023 OR 2024 OR 2025 OR 2026)
```

### 5.2 Government / procurement sweep

```text
site:solomons.gov.sb ("data centre" OR "data center" OR "ICT" OR "digital")
site:mca.gov.sb ("data centre" OR "broadband" OR "digital" OR "cyber" OR "SiCERT")
site:tcsi.org.sb ("data" OR "cable" OR "IXP" OR "annual report")
site:lands.gov.sb ("planning" OR "land")
"Solomon Islands" ("tender" OR "procurement") ("data centre" OR "ICT infrastructure" OR "hosting")
"Solomon Islands" ("World Bank" OR "ADB" OR "AIFFP") ("data centre" OR "ICT" OR "digital" OR "cable")
```

### 5.3 Cloud and operator sweep

```text
"Solomon Islands" ("Our Telekom" OR "bmobile" OR "Satsol" OR "SISCC") ("data centre" OR "hosting" OR "cloud")
"Solomon Islands" ("Google" OR "Microsoft" OR "AWS" OR "Oracle" OR "Alibaba") ("data centre" OR "cloud" OR "region")
"Solomon Islands" ("Huawei" OR "China") ("data centre" OR "broadband" OR "ICT")
```

When a hit appears, capture: source URL + date; operator/agency; facility name; town/province; function (colo, hosting, DR, CLS, core, edge, cache, government DC); status verb (`proposed`, `planned`, `under construction`, `handed over`, `opened`, `operational`, `upgraded`); capacity/power claims; funding source; and grade. If a claim says “cloud” without a physical site, mark **service-only, not a facility**.

---

## 6. Per-division query templates

Coverage must include all **9 provinces + Honiara Capital Territory**: Central, Choiseul, Guadalcanal, Isabel, Makira-Ulawa, Malaita, Rennell and Bellona, Temotu, Western, and Capital Territory. Industry enumeration should route each division through the likely operator/connectivity layer below before accepting a facility claim.

| Division | Industry route | Expected yield / caution |
|---|---|---|
| Capital Territory | Our Telekom, bmobile, SATSOL, SISCC Honiara CLS, banks/SINPF/CBSI, DataCenterMap leads | Highest yield. Count telco/hosting/DC only with operator or strong secondary evidence; directory claims remain C. |
| Guadalcanal | Honiara-adjacent Henderson/Lungga/Tina River corridor, bmobile/Our Telekom network, power press | Honiara spillover risk; assign facilities by legal/admin site. |
| Central | Tulagi, bmobile coverage, Our Telekom provincial office, Solomon Power outstation | Low; telecom cabinets/towers only unless facility named. |
| Choiseul | Taro SIDN landing, Our Telekom/bmobile coverage, provincial admin | CLS/telecom node, not retail DC. |
| Isabel | Buala, Solomon Power Buala, Our Telekom provincial office | Low; power/telecom leads only. |
| Makira-Ulawa | Kirakira, rural connectivity/SINBIP, satellite | Very low. |
| Malaita | Auki SIDN landing, bmobile/Our Telekom, Solomon Power Auki | CLS/telecom node; no public colo evidence. |
| Rennell and Bellona | Tingoa, satellite/Starlink/rural connectivity | Very low; expect no_projects. |
| Temotu | Lata/Santa Cruz, satellite/rural connectivity | Very low; expect no_projects. |
| Western | Noro Data Centre, Noro SIDN landing, Gizo/Munda, SATSOL/Our Telekom/bmobile, Noro powerhouse/port/fisheries | Highest non-Honiara yield; Noro DC is the confirmed government facility. |

### Capital Territory (Honiara) — PRIMARY
```text
"Honiara" ("data centre" OR "data center" OR "colo" OR "hosting" OR "server")
"Honiara" ("Our Telekom" OR "bmobile" OR "SISCC" OR "CBSI" OR "SINPF") ("data" OR "ICT" OR "cloud")
"Honiara" ("Lengakiki" OR "Point Cruz" OR "Ranadi" OR "Mendana") ("cable" OR "data" OR "telecom")
"Honiara" "Tier" ("III" OR "3") ("data centre" OR "facility")
```

### Guadalcanal Province
```text
"Guadalcanal" ("data centre" OR "ICT" OR "telecom") "Solomon Islands"
"Guadalcanal" ("Henderson" OR "Lungga" OR "Tetere" OR "Tenaru") ("data" OR "ICT" OR "grid")
"Tina River" ("transmission" OR "grid" OR "Honiara")
```

### Central Province (Tulagi)
```text
"Central Province" OR "Tulagi" ("data" OR "ICT" OR "broadband" OR "telecom") "Solomon Islands"
"Tulagi" ("shipyard" OR "rehabilitation" OR "cable" OR "power")
```

### Isabel Province (Buala)
```text
"Isabel" OR "Buala" ("data" OR "ICT" OR "telecom" OR "broadband") "Solomon Islands"
"Buala" ("powerhouse" OR "hydro" OR "electricity" OR "Solomon Power")
```

### Western Province (Gizo/Noro/Munda) — SECONDARY
```text
"Noro" ("data centre" OR "data center" OR "fisheries" OR "landing station" OR "powerhouse")
"Western Province" OR "Gizo" OR "Munda" ("data" OR "ICT" OR "cloud" OR "broadband")
"Noro" ("World Bank" OR "FFA" OR "Australia") "data"
```

### Choiseul Province (Taro)
```text
"Choiseul" OR "Taro" ("landing station" OR "cable" OR "data" OR "ICT") "Solomon Islands"
"Taro" ("SIDN" OR "capital" OR "relocation" OR "submarine")
```

### Malaita Province (Auki)
```text
"Auki" ("cable landing station" OR "data" OR "broadband" OR "ICT")
"Malaita" ("data centre" OR "digital" OR "telecommunications" OR "e-services")
"Auki" ("Solomon Power" OR "powerhouse" OR "electricity")
```

### Makira-Ulawa Province (Kirakira)
```text
"Makira" OR "Kirakira" ("telecom" OR "broadband" OR "solar" OR "data") "Solomon Islands"
```

### Temotu Province (Lata)
```text
"Temotu" OR "Lata" ("telecom" OR "broadband" OR "data" OR "ICT") "Solomon Islands"
"Santa Cruz" OR "Vanikoro" ("airfield" OR "development" OR "connectivity")
```

### Rennell and Bellona Province (Tingoa)
```text
"Rennell" OR "Bellona" ("telecom" OR "satellite" OR "connectivity" OR "data") "Solomon Islands"
```

---

## 7. Expected outcome and honest-confidence notes

- Realistic enumeration outcome for SB: **1–4 counted facilities/leads** — (1) Our Telekom Exchange Building / main Data Centre room in Honiara (operator article confirms the room and NOC; public colo function not confirmed), (2) Noro Data Centre (Western Province, government/provincial DR), (3) SATSOL Honiara data-centre claim from DataCenterMap only if SATSOL or strong secondary evidence confirms it, (4) possibly an enterprise/bank or ministry server room in Honiara. Everything else is cable/edge/network infrastructure to record only with explicit facility evidence.
- All directory entries (DataCenterMap etc.) are thin/stale for SB; grade C until operator confirmation. The SATSOL directory claim is a lead, not an accepted facility by itself.
- Satellite ISPs and Starlink have meaningful market share but no public in-country DC evidence; do not count gateways without primary sources.
- Every record needs: URL + date + grade + province + status verb + facility function. Do not duplicate records across the two explorer files; the parent merges into SKILL.md.
