# KI Explorer Industry - Kiribati Datacenter Discovery via Trade Press, Local Media, Operators, Cables, and Directory Sources

Date: 2026-08-12. Scope: Kiribati datacenter and digital-infrastructure discovery through industry press, local media, operator/vendor pages, cable projects, directories, and division-level query patterns. Repo divisions: **Gilbert Islands**, **Line Islands**, **Phoenix Islands**.

Reliability grades: **A** = primary/official/operator/company filing/donor document; **B** = established trade press or local media with named operator/site/status; **C** = directory, market report, social post, promotional article, or unsourced aggregator; **U** = unverified. An entry's grade covers only the fact actually supported.

This is the final reviewed industry methodology layer. Source URLs listed as evidence were live-checked during review where feasible; blocked, rate-limited, or dead directory pages are labelled as leads and must not be treated as facility evidence.

---

## 0. Kiribati-specific industry frame

- Kiribati is a **very small, near-zero commercial datacenter market**. As of 2026-08 there is **no confirmed commercial colocation facility**, **no hyperscaler region**, and no public IXP was found in reviewed searches; PeeringDB should still be checked manually because automated access is often blocked. The realistic inventory is: a planned/procurement-stage domestic/containerized government data center + government cloud (World Bank P176108), two submarine cable landing stations (Tarawa/Nanikai for EMCS; Tabwakea/Kiritimati for SX NEXT), and telco/ISP network cores.
- **Do not conflate cables with datacenters.** The 2022 SX NEXT Kiritimati spur and the 2025/2026 EMCS Tarawa landing are the headline digital-infrastructure stories; both are interconnection anchors that could *enable* future facilities, not facilities themselves.
- **Status verbs are mandatory.** `landed`, `ready for service`, `construction complete`, `pending implementation`, `RFQ published`, `awarded`, `delivered`, `commissioned`, and `in service since` mean different things. EMCS especially: BNL reported the Tarawa landing on 2025-07-25; NEC announced construction completion and handover on 2026-05-15; re-check live RFS/retail service before marking operational service.
- **Asset classes to preserve separately:** procurement-stage government cloud/DC, existing ministry/server-room infrastructure, cable landing stations, telco exchanges/server rooms, satellite gateways, planned proposals. Kiribati coverage in trade press mostly concerns cables and telecom, not datacenters.
- **Power is the binding constraint.** Diesel-based PUB grid on South Tarawa (5 MW solar + 13 MWh BESS added under STREP) and small village grids elsewhere cannot support commercial-scale DC loads; treat any MW claim skeptically until PUB/grid evidence appears.
- **English is the search language.** Local language (Gilbertese) has no established datacenter vocabulary; use Gilbertese only for place names. English-language coverage comes mainly from regional/trade outlets (DCD, Submarine Networks, GeoCables, TeleGeography-driven press, commsupdate, Islands Business) plus government/donor material; local media is limited (Radio Kiribati/BPA, government press releases).
- **False-positive trap:** Australian **Christmas Island** (Indian Ocean) datacenter news (e.g., Google's reported AI-datacenter plan, late 2025) is NOT Kiribati's Kiritimati. Filter on "Kiribati" explicitly.

Verified anchor URLs:

- DCD, EMCS lands at Kiribati (2025-07-28): https://www.datacenterdynamics.com/en/news/east-micronesia-cable-system-lands-at-kiribati/
- DCD, Lynk + Vodafone Kiribati sat-to-mobile: https://www.datacenterdynamics.com/en/news/lynk-pairs-with-vodafone-to-bring-sat-to-mobile-services-to-kiribati/
- EMCS official site: https://www.eastmicronesiacable.com/ ; news: https://www.eastmicronesiacable.com/news ; the-project: https://www.eastmicronesiacable.com/the-project
- NEC EMCS construction completion: https://www.nec.com/en/press/202605/global_20260515_02.html
- BNL projects (Kiritimati + EMCS + outer-island networks): https://www.bnl.com.ki/projects ; EMCS landing blog: https://www.bnl.com.ki/blog/east-micronesia-cable-lands-in-first-pacific-location-of-kiribati
- Submarine Networks SX NEXT: https://www.submarinenetworks.com/en/systems/trans-pacific/southern-cross-next ; overview: https://www.submarinenetworks.com/en/systems/trans-pacific/southern-cross-next/southern-cross-next-cable-system-overview ; EMCS: https://www.submarinenetworks.com/en/systems/trans-pacific/emcs
- GeoCables EMCS: https://geocables.com/cable/east-micronesia-cable-system-emcs ; Tabwakea landing: https://geocables.com/location/tabwakea-kiribati
- Kiritimati/SX NEXT geography cross-check: https://www.submarinenetworks.com/en/systems/trans-pacific/southern-cross-next/southern-cross-next-cable-system-overview ; https://geocables.com/location/tabwakea-kiribati
- ZDNET, Pacific islands sign on for NEXT (BwebwerikiNET = BNL): https://www.zdnet.com/article/pacific-islands-sign-on-for-next-subsea-cable/
- Vodafone Kiribati: https://vodafone.com.ki/ ; services: https://vodafone.com.ki/Services ; ATH group structure: https://www.ath.com.fj/our-story/group-structure-2/
- Ocean Link GSMA membership: https://www.gsma.com/get-involved/gsma-membership/gsma_orgs/ocean-link-ltd/ ; TeleGeography-derived launch history: https://www.samenacouncil.org/samena_daily_news?news=91729
- LogCluster 3.4 Kiribati telecoms (ISPs incl. Speed Wave, Tentanini, TeniCom): https://lca.logcluster.org/34-kiribati-telecommunications
- ts2.tech Starlink in Kiribati (BNL open-access wholesale context): https://ts2.tech/en/starlink-in-kiribati/
- JICA/Yachiyo survey (Kiribati section: CCK/MICT/BNL/PUB roles, domestic DC need, planned small container-type data-center design, power constraints, Google cache/IXP considerations): https://openjicareport.jica.go.jp/pdf/1000057177.pdf
- World Bank P176108 procurement plan (lists containerized data center and Government cloud equipment, plus Phase 2 `KI-MICTTD-470992-GO-RFQ` as pending implementation): https://documents1.worldbank.org/curated/en/099031326045033591/pdf/P176108-c7747b0b-6787-4232-acf4-2a39d7d284a8.pdf
- Containerized DC / gov cloud tender mirrors, C-grade leads only: https://www.developmentaid.org/tenders/view/1622456/kiribati-digital-government-project-containerized-data-center-and-government-cloud-equipment-phase-2 ; https://www.kiribatitenders.com/tender/containerized-data-center-and-government-cloud-equipment-phase-2-83846bd.php
- MLPID (Line/Phoenix ministry): https://www.mlpid.gov.ki/ ; Invest in Kiribati: https://www.investinkiribati.mtcic.gov.ki/

---

## 1. High-signal industry and press sources

| Source | URL/search surface | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/news/ search `Kiribati` | Best free trade source: EMCS landing, Lynk/Vodafone sat-to-mobile, any future DC/cloud story. | B |
| Submarine Networks | https://www.submarinenetworks.com/en/systems/trans-pacific/emcs ; .../southern-cross-next | Cable system facts, landing stations, RFS dates. | B |
| GeoCables | https://geocables.com/cable/east-micronesia-cable-system-emcs ; https://geocables.com/location/tabwakea-kiribati | Cable geography/status; useful for landings and spur detail. | B |
| TeleGeography (via press) | GlobalComms/TeleGeography quotes in samenacouncil, commsupdate, etc. | Operator launch/status facts (e.g., Ocean Link Nov 2018 Tarawa, Oct 2019 Kiritimati). | B |
| commsupdate | https://www.commsupdate.com/ search `Kiribati` | Telecom licensing, cable, operator news. | B |
| NEC press releases | https://www.nec.com/en/press/ | EMCS construction completion (2026-05-15) - primary supplier evidence. | A |
| EMCS official site | https://www.eastmicronesiacable.com/ | Primary project site for RFS/landing announcements. | A |
| BNL (BwebwerikiNet) | https://www.bnl.com.ki/projects ; https://www.bnl.com.ki/blog/ | State operator; primary for Kiritimati/EMCS/backbone facts. | A |
| Islands Business | https://islandsbusiness.com/ search `Kiribati` | Regional business/telecom coverage; treat advertorials as C. | B/C |
| ZDNET / content-technology.com / subtelforum | https://www.zdnet.com/article/pacific-islands-sign-on-for-next-subsea-cable/ ; https://content-technology.com/asia-pacific-news/southern-cross-next-cable-lands-in-kiribati/ | SX NEXT landing/partners history. | B |
| ts2.tech (Starlink country pages) | https://ts2.tech/en/starlink-in-kiribati/ | Satellite access context (Starlink availability; BNL open-access wholesale). | C |
| BuddeCom / market reports | https://www.budde.com.au/Research/Kiribati-Telecoms-Mobile-and-Broadband-Statistics-and-Analyses | Market stats/background only; no facility proof. | C |
| Radio Kiribati / BPA; government press releases | https://www.mict.gov.ki/news-page ; official ministry pages | Official launches, licensing, cable milestones. | B+/A when quoting officials |
| DataCenterMap / Cloudscene / Baxtel | https://www.datacentermap.com/kiribati/ returned 429 during review; https://baxtel.com/data-center/kiribati returned 404 | Directory check only; expected empty or near-empty. Do not cite a directory absence as proof unless the page loads. | C |
| PeeringDB / PCH | https://www.peeringdb.com/ (manual browse often required) | IX/facility check; no KI entries surfaced in reviewed searches. | A for interconnection facts when listed |

Trade/local search patterns:

```text
site:datacenterdynamics.com/en/news/ Kiribati ("data center" OR "data centre" OR "cable" OR "cloud" OR "Lynk" OR "EMCS")
site:submarinenetworks.com Kiribati OR EMCS OR "Southern Cross NEXT"
site:geocables.com Kiribati OR Tabwakea OR Tarawa
site:commsupdate.com Kiribati
site:islandsbusiness.com Kiribati (telecom OR cable OR digital OR Vodafone)
site:eastmicronesiacable.com ("ready for service" OR "Kiribati" OR "Tarawa" OR "Nauru")
site:bnl.com.ki ("EMCS" OR "SX NEXT" OR "landing station" OR "fibre" OR "fiber")
"Kiribati" ("data center" OR "data centre" OR datacenter OR colocation) -"Christmas Island Australia"
```

---

## 2. Vendor/operator seed list

| Operator/developer | Primary URLs | Kiribati signal | Grade and handling |
|---|---|---|---|
| Vodafone Kiribati (ATHKL) | https://vodafone.com.ki/ ; https://www.ath.com.fj/our-story/group-structure-2/ | Incumbent (ATH, Fiji; acquired TSKL assets May 2015); mobile/fixed/broadband; core network in South Tarawa, presence on Kiritimati. | A for operator/ownership; C for facility details until explicit. Check enterprise/hosting pages. |
| Ocean Link Ltd | https://www.gsma.com/get-involved/gsma-membership/gsma_orgs/ocean-link-ltd/ ; JICA survey; launch history via samenacouncil/TeleGeography | Second operator (OceanCell/OceanNet/OceanTalk); South Tarawa and Kiritimati/remote-island activity. | A for existence (GSMA/JICA); C for facilities; official domain/contact remains a manual-check item. |
| BNL (BwebwerikiNet Limited) | https://www.bnl.com.ki/projects | State cable/infrastructure company: EMCS implementing agency, Kiritimati cable project, outer-island passive networks, planned South Tarawa fibre backbone O&M. | A for cable/network; not a DC operator. |
| Small ISPs: Speed Wave, Tentanini, TeniCom | https://lca.logcluster.org/34-kiribati-telecommunications | Retail ISPs (LogCluster); possible small server rooms. | C leads only. |
| Satellite: Kacific, Starlink, Lynk Global | https://www.datacenterdynamics.com/en/news/lynk-pairs-with-vodafone-to-bring-sat-to-mobile-services-to-kiribati/ ; https://ts2.tech/en/starlink-in-kiribati/ | Access/backhaul providers; Lynk-Vodafone sat-to-mobile (2024/25); Starlink availability. Gateways, not datacenters. | B for announcements; C for facilities. |
| Planned domestic/containerized government DC | JICA survey PDF; https://www.mict.gov.ki/kdgp ; World Bank P176108 procurement plan | Government hosting/cloud procurement; JICA describes need/design and WB plan lists Phase 2 pending implementation. | A for JICA/WB/MICT; do not count as built. |
| KDGP containerized DC + gov cloud | https://www.mict.gov.ki/kdgp ; World Bank P176108 procurement plan; tender mirrors | Procurement-stage government DC/cloud, Phase 2 `KI-MICTTD-470992-GO-RFQ`. | A for WB plan; C for mirrors; do not count as built. |

Operator query bundle:

```text
"Vodafone Kiribati" ("data center" OR "cloud" OR "hosting" OR "enterprise" OR "server")
site:vodafone.com.ki ("business" OR "enterprise" OR "internet" OR "fibre" OR "fiber")
"Ocean Link" Kiribati ("LTE" OR "4G" OR "internet" OR "server" OR "data")
"ATHKL" OR "Amalgamated Telecom Holdings Kiribati" ("data" OR "network" OR "investment")
"BNL" OR "BwebwerikiNet" Kiribati ("fibre" OR "fiber" OR "backbone" OR "landing" OR "data")
"Kacific" OR "Starlink" OR "Lynk" Kiribati
"Kiribati" ("government cloud" OR "national data center" OR "containerized data center")
```

---

## 3. Project/status watchlist

### 3.1 Current anchors to keep in scope

| Project | Division | Asset class | Current status | Best evidence |
|---|---|---|---|---|
| Planned domestic/containerized government data center | Gilbert Islands (Tarawa/South Tarawa) | Government hosting/cloud procurement | Planned/procurement-stage; JICA describes small container-type domestic DC need/design, and World Bank plan lists Phase 2 pending implementation | JICA survey PDF; MICT KDGP; World Bank P176108 procurement plan |
| SX NEXT Kiritimati spur - Tabwakea CLS | Line Islands (Kiritimati) | Cable landing station | SX NEXT branch to Tabwakea; use BNL/Submarine Networks/GeoCables for cable status and geography | BNL projects page; Submarine Networks; GeoCables Tabwakea |
| EMCS Tarawa/Nanikai CLS | Gilbert Islands (South Tarawa) | Cable landing station | Landed 2025-07-25; construction complete and handed over 2026-05-15; re-check RFS/retail service before marking live | EMCS site; BNL blog; NEC release; DCD |
| Vodafone Kiribati network core | Gilbert Islands (South Tarawa) | Telco core | Operational | Vodafone Kiribati site; ATH pages |
| Ocean Link network (Tarawa, Kiritimati) | Gilbert + Line Islands | Telco core | Operational since 2018/2019 | GSMA; TeleGeography via press |

### 3.2 Procurement, planned, or proposal

| Project | Division | Asset class | Current status | Handling |
|---|---|---|---|---|
| KDGP containerized data center + government cloud (P176108) | Gilbert Islands (Tarawa) | Government cloud/DC | Phase 2 `KI-MICTTD-470992-GO-RFQ` listed as pending implementation in World Bank 2026-03 procurement plan; tender mirrors show Mar 2026 notice and 2026-03-31 deadline | Track award/delivery on WB procurement + MICT; do not count as operational until commissioned. |
| South Tarawa fibre backbone / FTTH (World Bank) | Gilbert Islands | Network infrastructure | Planned/rolling out; BNL passive O&M expected | ts2.tech (C), BNL (A when official), WB PRCP Phase 4 docs |
| Kiritimati spur retail/mobile rollout (Vodafone, Ocean Link via BNL CLS) | Line Islands (Kiritimati) | Telecom services | Rolling out; JICA says BNL planned retail connections around Nov 2025 and that local access investment still lagged cable capacity | BNL site; JICA survey; GeoCables regional context |
| MLPID "world-class investment hub" ambitions for Line/Phoenix | Line Islands | Policy/investment frame | Vision/mission statement only | https://www.mlpid.gov.ki/ |
| Any future commercial DC proposal on Kiritimati | Line Islands | Planned proposal | None verified as of 2026-08 | Watch MLPID/MTCIC/BNL announcements |

Status-verification queries:

```text
"East Micronesia Cable" ("ready for service" OR "RFS" OR "in service" OR "operational") 2026
"EMCS" ("Tarawa" OR "Kiribati") ("completed" OR "ready" OR "landing")
"Southern Cross NEXT" "Kiritimati" ("in service" OR "live" OR "2022")
"Kiribati" "containerized data center" OR "government cloud" ("award" OR "contract" OR "delivery")
"OP00432633" OR "KI-MICTTD-470992-GO-RFQ"
"Kiribati Digital Government Project" ("data center" OR "cloud") ("phase 2" OR "RFQ" OR "award")
```

---

## 4. Hyperscaler/cloud discovery

Official cloud pages are useful mainly to prevent false positives. Kiribati has **no public AWS, Azure, Google Cloud, or Oracle OCI region** as of 2026-08. Any "cloud in Kiribati" claim is likely one of:

- government-hosted services on existing ministry/server-room infrastructure or the planned KDGP government cloud,
- telco/ISP hosting at Vodafone Kiribati or Ocean Link,
- out-of-country hyperscaler regions serving Kiribati customers,
- satellite-delivered SaaS/connectivity (Starlink, Kacific, Lynk), which is access, not hosting,
- a future proposal not yet built.

Queries:

```text
"AWS" "Kiribati" ("region" OR "availability zone" OR "edge" OR "Local Zone")
"Microsoft Azure" "Kiribati" ("region" OR "data center")
"Google Cloud" "Kiribati" ("region" OR "data center")
"Oracle Cloud" "Kiribati" ("region" OR "data center")
"cloud" "Kiribati" ("government" OR "Vodafone" OR "Ocean Link" OR "sovereign")
"sovereign cloud" OR "data residency" Kiribati
"Kiribati" "data center" ("Google" OR "Microsoft" OR "Amazon" OR "Oracle") -"Christmas Island"
```

---

## 5. Search vocabulary (English and local)

English terms (US + British spellings): `data center`, `data centre`, `datacenter`, `datacentre`, `server farm`, `server room`, `colocation`, `colo`, `hosting`, `cloud`, `government cloud`, `digital infrastructure`, `IXP`, `internet exchange`, `submarine cable`, `cable landing station`, `backbone`, `fibre/fiber`, `satellite gateway`, `Starlink`, `Kacific`, `telecom`, `broadband`.

Gilbertese: no established datacenter terms; use Gilbertese only for **place names** (Tarawa, Betio, Bairiki, Ambo, Nanikai, Bonriki, Bikenibeu, Eita, Teaoraereke, Abaiang, Kiritimati, Tabwakea, London, Banana, Teraina, Tabuaeran, Kanton, Abariringa, Betio). Include the English alias `Christmas Island` **plus `Kiribati`** for Kiritimati to avoid the Australian-territory false positive.

```text
"Kiribati" ("data center" OR "data centre" OR datacenter OR datacentre OR "server room" OR colocation)
"Kiribati" ("data center" OR "data centre") ("MW" OR "IT load" OR "racks" OR "GPU" OR "power")
"Kiribati" ("submarine cable" OR "landing station" OR "backbone" OR "fibre" OR "fiber")
"Kiribati" ("internet exchange" OR "IXP" OR "peering")
"Kiribati" ("satellite" OR "Starlink" OR "Kacific" OR "gateway") ("server" OR "data" OR "teleport")
"Kiribati" ("cloud" OR "hosting" OR "colocation") ("Vodafone" OR "Ocean Link" OR "government")
"Kiritimati" OR "Christmas Island Kiribati" ("data" OR "server" OR "compute" OR "AI")
"South Tarawa" OR "Betio" OR "Bairiki" ("server" OR "data" OR "exchange" OR "network")
```

---

## 6. Division enumeration method

Enumeration unit is the division (island group), but evidence is almost always an islet/town/site. Use `division -> islet/site -> operator -> status -> official cross-check`.

### 6.1 Gilbert Islands (real-activity division)

Targets: KDGP containerized DC/government cloud procurement, EMCS Nanikai/Tarawa CLS, Vodafone Kiribati and Ocean Link cores, bank/government server rooms, satellite gateways on South Tarawa.

```text
"South Tarawa" OR "Tarawa" ("data center" OR "data centre" OR "server room" OR "cloud" OR "container")
"Betio" OR "Bairiki" OR "Ambo" OR "Nanikai" OR "Bonriki" ("data" OR "server" OR "cable")
"Kiribati" ("national data center" OR "government data center" OR "government cloud")
"EMCS" OR "East Micronesia Cable" ("Tarawa" OR "Nanikai" OR "ready for service")
"Vodafone Kiribati" ("exchange" OR "core" OR "server" OR "data")
"{outer Gilbert atoll}" Kiribati ("server room" OR "telecom" OR "satellite" OR "Starlink")
```

### 6.2 Line Islands (watch division)

Targets: SX NEXT Tabwakea CLS, Vodafone/Ocean Link retail on Kiritimati, satellite gateways, any future DC/edge proposal tied to MLPID investment ambitions. Honest expectation: **no datacenter today**; cable landing + telecom only.

```text
"Kiritimati" OR "Christmas Island Kiribati" ("data center" OR "data centre" OR "server" OR "cloud" OR "compute")
"Kiritimati" ("SX NEXT" OR "Southern Cross NEXT" OR "Tabwakea" OR "landing station")
"Tabwakea" OR "London" OR "Banana" ("cable" OR "internet" OR "power" OR "data")
site:mlpid.gov.ki ("Kiritimati" OR "Line Islands") ("investment" OR "ICT" OR "data" OR "cable")
"Kiritimati" ("solar" OR "diesel" OR "power") ("MW" OR "plant" OR "grid")
```

### 6.3 Phoenix Islands (expected no activity)

Kanton (Abariringa) is the only settlement; PIPA covers most of the division. Record negative searches; watch for government/coastguard communications and telemetry equipment only.

```text
"Kanton" OR "Abariringa" OR "Phoenix Islands" ("data" OR "server" OR "internet" OR "telecom")
"Phoenix Islands" ("satellite" OR "radio" OR "communications") Kiribati
"Phoenix Islands Protected Area" ("telemetry" OR "data" OR "communications")
```

---

## 7. Known facilities/projects and evidence status (as of 2026-08)

| Name | Division | Asset class | Status | Evidence grade |
|---|---|---|---|---|
| Planned domestic/containerized government data center / KDGP government cloud | Gilbert Islands (Tarawa/South Tarawa) | Government hosting/cloud procurement | Planned/procurement-stage; Phase 2 pending implementation in World Bank 2026-03 plan | A for JICA/WB/MICT; not operational |
| KDGP containerized DC + gov cloud (P176108) | Gilbert Islands (Tarawa) | Government cloud/DC | Phase 2 `KI-MICTTD-470992-GO-RFQ` pending implementation in World Bank 2026-03 plan; not built/commissioned | A for World Bank plan; C for tender mirrors |
| EMCS Tarawa/Nanikai cable landing station | Gilbert Islands (South Tarawa) | Cable landing station | Landed 2025-07-25; complete and handed over 2026-05-15; re-check current RFS/retail service | A |
| SX NEXT Kiritimati spur - Tabwakea CLS | Line Islands (Kiritimati) | Cable landing station | In service since 2022-07 | A |
| Vodafone Kiribati core/network | Gilbert Islands; Kiritimati presence | Telco core | Operational | A operator; C facilities |
| Ocean Link core/network | Gilbert + Line Islands | Telco core | Operational since 2018/2019 | A operator (GSMA/TeleGeography); C facilities |
| South Tarawa fibre backbone / FTTH (WB) | Gilbert Islands | Network infrastructure | Planned/rolling out; BNL expected passive-network role | A for BNL/JICA context; B/C for secondary rollout reporting |
| Commercial colocation facilities | n/a | Colocation | **None confirmed** | n/a |
| Public internet exchange | n/a | IXP | **None surfaced** in reviewed searches; PeeringDB/PCH manual check still required | n/a |
| Hyperscaler cloud region | n/a | Cloud | **Absent** | A (official region pages) |

Expected yields if this methodology is executed today: Gilbert Islands ~2-4 records (KDGP/containerized DC procurement, EMCS CLS, telco cores/server-room leads), Line Islands ~1-2 records (SX NEXT CLS, satellite/telecom leads), Phoenix Islands 0 records (record `no_projects` after negative searches). This is a **tiny market**; do not inflate.

---

## 8. Update/re-check cadence

- **Monthly:** EMCS official site (RFS), BNL pages/blog, MICT news/tenders (KDGP phases, any new REOI/RFQ), WB procurement notices (P176108 awards), MLPID news, Vodafone Kiribati/Ocean Link announcements.
- **Quarterly:** DCD + Submarine Networks + GeoCables Kiribati keyword sweeps; PeeringDB/PCH and DataCenterMap/Cloudscene/Baxtel KI checks as manual/directory leads; hyperscaler region pages (absence re-check).
- **Event-driven:** EMCS in-service announcement; KDGP containerized DC award/delivery/commissioning; Data Protection Act 2025 commencement/regulations; any MLPID/MTCIC investment announcement pairing Kiritimati connectivity with land/power; any cable outage or RFS slip.
- **On every pass:** re-check time-sensitive statuses: EMCS RFS/retail service, WB/STEP award and completion fields for `KI-MICTTD-470992-GO-RFQ`, CCK licence lists, Ocean Link official domain/contact details, PeeringDB/PCH absence, and any MICT/MFED/BNL announcement that changes the planned DC from procurement to delivered/commissioned.
