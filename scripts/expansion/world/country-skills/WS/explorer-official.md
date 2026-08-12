# WS Explorer Official - Samoa Datacenter Enumeration via Official/Regulatory Sources

Date: 2026-08-12. Scope: Independent State of Samoa (WS), all 11 itumalo/districts: A'ana, Aiga-i-le-Tai, Atua, Fa'asaleleaga, Gaga'emauga, Gagaifomauga, Palauli, Satupa'itea, Tuamasaga, Va'a-o-Fonoti, Vaisigano. Angle: official/regulatory discovery for operational, planned, and false-positive datacenter candidates.

Reliability grades used by this explorer: **A** = primary government, regulator, state-owned enterprise, public utility, official company registry, official cloud/provider page, official multilateral project document, or legislation; **B** = reputable local/regional/trade press or multilateral project page with named parties and dates; **C** = directory, cable tracker, map, social page, SEO hosting page, or unattributed aggregate. Use Grade C only as a lead or negative-control note; do not use it to establish a facility.

## 0. Verified Country Baseline

- Samoa has no public datacenter registry, no DC-specific license class, no public national planning-permit search portal, and no verified public commercial colocation market found in this pass.
- The verified facility universe is small: SSCC cable landing/cable-station facilities at Apia and Tuasivi; licensed telecom operator core/switch/ISP premises concentrated in Apia; the Government of Samoa data-center upgrade/establishment funded under the World Bank Digitally Connected and Resilient Samoa Project (DCRSP, P180807); and private enterprise/server-room leads that require primary evidence before counting.
- Treat **Apia / Tuamasaga** as the primary search geography. Treat **Tuasivi / Fa'asaleleaga** as the only non-Apia facility-grade telecom lead. All other districts are expected to yield telecom towers, cabinets, power assets, or public-service ICT rooms rather than datacenters.
- Do not conflate Samoa (WS) with American Samoa (AS). ASH, Hawaiki, Pago Pago/Tafuna facilities, and Le Vasa American Samoa cable assets are outside WS scope except as onward-connectivity context through the Samoa-American Samoa path.
- Cable landing stations are not datacenters by default. Record them as `telecom_cable_station` or `colo_adjacent_telecom` only when the RIO/FAA or another primary source supports equipment access, interconnection, or colocation-like service.
- Samoa has no AWS, Azure, Google Cloud, or Oracle public cloud region in the official region lists checked. Use official cloud pages for absence checks and do not promote resellers, Starlink, or VPS marketing to facility inventory.
- English is sufficient for official-source searching. Use Samoa/Samoan spelling variants only for place normalization: Savai'i/Savaii, Upolu, Tuasivi, Va'a-o-Fonoti/Vaa O Fonoti, Aiga-i-le-Tai/Aiga i le Tai.

## 1. Official Sources To Check First

### 1.1 Office of the Regulator (OOTR)

Primary sources:

- OOTR home/about: https://regulator.gov.ws/ . The page identifies OOTR as Samoa's regulator for telecommunications, broadcasting, postal, and electricity, established in 2006 under the Telecommunications Act 2005, with electricity added under 2010 legislation. Address: MKR Apartments, Savalalo, Apia.
- Telecommunications licensing page: https://regulator.gov.ws/index.php/telecommunications-regulation/telecommunications/licensing
- Current/linked telecom licensee PDFs:
  - https://regulator.gov.ws/images/Telecommunications_Licensing_Rule/List-of-Telecommunications-Licensees-Final-2022_v3.pdf
  - fallback older URL found in search: https://www.regulator.gov.ws/images/List-of-Telecommunications-Licensees.pdf
- Telecommunications Orders: https://www.regulator.gov.ws/index.php/telecommunications-regulation/telecommunications/telecommunications-orders . This page includes regulator orders through 2026 and confirms repeated approvals of SSCC RIOs, Digicel/Vodafone retail tariffs, and Starlink-related orders.
- Publications / Annual Reports: https://regulator.gov.ws/index.php/2-uncategorised/57-publication
- Annual Data Collection: https://regulator.gov.ws/index.php/homepage/2-other-matters/uncategorised/82-annual-data-collection
- ICT Sector Plan 2022/23-2026/27: https://regulator.gov.ws/images/Sector_Plan/ICTSP-2022-2027_English-Version_Signed.pdf
- Digital Samoa Project page: https://www.regulator.gov.ws/index.php/91-digital-samoa-project

Use:

- Start every operator enumeration with OOTR. A license is **A-grade for operator existence and service authorization**, but it is not proof of a datacenter.
- Extract licensed carrier/ISP names, license class, orders, tariff approvals, and any annual-report references to international gateways, fiber, IXP, hosting, or data-center infrastructure.
- Current known licensed/service-provider leads from OOTR pages and search snippets include SamoaTel/SamoaTel Ltd, Vodafone Samoa, Digicel Samoa Ltd, Computer Services Ltd/CSL, BlueWave, Samoa Broadband Company, Samoa Submarine Cable Company, and Starlink Samoa Ltd. Verify against the live licensee PDF before recording status.

Queries:

```text
site:regulator.gov.ws ("data center" OR "data centre" OR datacenter OR "government data" OR IXP OR hosting OR colocation)
site:regulator.gov.ws "List of Telecommunications Licensees" OR "Telecommunications Licensees"
site:regulator.gov.ws SamoaTel OR Vodafone OR Digicel OR "Computer Services" OR CSL OR BlueWave OR Starlink
site:regulator.gov.ws "Reference Interconnection Offer" OR RIO OR "Samoa Submarine Cable Company"
site:regulator.gov.ws "annual report" (telecommunications OR broadband OR internet OR cable)
site:regulator.gov.ws "Digital Samoa" "data center" OR "data centre"
```

### 1.2 MCIT, MyGov, Ministry of Finance, and World Bank DCRSP

Primary sources:

- MCIT: https://mcit.gov.ws/
- MCIT Digital Samoa page: https://mcit.gov.ws/publications/digital-samoa/ . This page states that DCRSP is World Bank-financed, implemented by MCIT and OOTR, with Ministry of Finance as executive agency. Component 1 includes national fibre, Government Intranet enhancement, and the upgrade/establishment of a secure and resilient government data center plus broadband pilots.
- One Government Portal / MyGov: https://mygov.gov.ws/
- Ministry of Finance: https://www.mof.gov.ws/ . Check tender advertisements, contracts awarded, development programmes, and DCRSP/World Bank posts.
- World Bank DCRSP project page: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099093024135596945
- World Bank procurement-plan anchor found for P180807: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099082025234031313 . Use this plus the main project page to navigate to current downloadable PDFs because World Bank document-file URLs are unstable.

Verified signals:

- DCRSP is the highest-confidence Samoa datacenter lead. It is **planned/implementation-stage government infrastructure**, not a confirmed operational commercial DC.
- World Bank ISR snippets found in 2026 list intermediate indicators for renewable energy consumed in the government data center and data-centre capacity added. The January 2026 and July 2026 snippets still showed 0 current progress against those indicators, with targets to October 2029. Keep status conservative until procurement/completion records are found.
- Do not assign a precise site, capacity, tier, or power draw unless a MCIT/MOF/World Bank procurement or project document names it. Apia/Tuamasaga is the likely administrative location, but this is an inference.

Queries:

```text
site:mcit.gov.ws ("data center" OR "data centre" OR "Digital Samoa" OR DCRSP OR P180807)
site:mygov.gov.ws ("data center" OR "data centre" OR "digital" OR "government services")
site:mof.gov.ws (DCRSP OR "Digitally Connected" OR "data center" OR "data centre" OR "government intranet")
site:documents.worldbank.org P180807 Samoa ("data center" OR "data centre" OR IXP OR "government intranet")
site:documents1.worldbank.org P180807 Samoa ("Data Centre capacity" OR "government data center" OR "renewable energy consumed")
"Digitally Connected and Resilient Samoa Project" (tender OR procurement OR "data center" OR "data centre")
```

### 1.3 Samoa Submarine Cable Company (SSCC)

Primary sources:

- SSCC official site: https://www.ssccsamoa.com/
- RIO page: https://www.ssccsamoa.com/about/rio-reference-interconnection-offer/
- 2026 RIO PDF: https://www.ssccsamoa.com/wp-content/uploads/2026/03/Rio-2026.pdf
- Progress page: https://www.ssccsamoa.com/home/progress/
- SSCC news archive: https://www.ssccsamoa.com/news/
- ADB Samoa Submarine Cable Project: https://www.adb.org/projects/47320-001/main

Verified signals:

- SSCC's home page states it offers Leased Capacity, IRU, and Facility Access Agreements, and that the Tui-Samoa cable is complete.
- The progress page shows permitting, cable landing station/civil work, dry plant, installation/commissioning, and overall progress at 100%, with Apia and Savai'i land routes called out.
- The 2026 RIO is the strongest facility evidence. It says SSCC offers capacity and services to OOTR-licensed service providers and includes Access Guidelines for colocation/interconnection services. It defines cable stations at Apia (Samoa), Tuasivi (Samoa), and Suva (Fiji), and defines a facility as a cable station or other location where SSCC permits customer equipment to connect to the SSCC network.
- ADB states the Tui-Samoa cable was officially launched in February 2018; OOTR/ICTSP also references Tui-Samoa launched in February 2018 and Manatua in November 2019. Use those official dates instead of vague RFS estimates unless a newer primary source supersedes them.

How to classify:

- Apia cable station: **A**, `telecom_cable_station`, `colo_adjacent_interconnection`, district Tuamasaga.
- Tuasivi cable station: **A**, `telecom_cable_station`, `colo_adjacent_interconnection`, district Fa'asaleleaga.
- Manatua Apia landing: **A/B depending on source used**. SSCC confirms consortium participation; use SubCom/consortium/trade sources for route/date and SSCC/RIO for Samoa facility access.
- Do not record these as retail datacenters unless a later primary source names rack colocation or datacenter service open to customers.

Queries:

```text
site:ssccsamoa.com RIO OR "Reference Interconnection Offer" OR "Facility Access" OR FAA
site:ssccsamoa.com "Cable Station" OR "Cable Landing Station" OR CLS OR Apia OR Tuasivi
site:ssccsamoa.com Manatua OR "Tui-Samoa" OR "Tui Samoa"
site:adb.org "Samoa Submarine Cable Project" "February 2018" OR "Tui Samoa"
"Samoa Submarine Cable Company" ("Apia" OR "Tuasivi") ("cable station" OR "landing station" OR RIO)
```

### 1.4 Planning, building, fire, and environmental approvals

Primary sources:

- MWTI home: https://www.mwti.gov.ws/ . The page lists PUMA as a division and says the Building Regulatory Division manages building permits and inspections.
- MWTI PUMA page: https://www.mwti.gov.ws/puma/ . It states PUMA processes and grants Development Consent Applications for development under the Act.
- PUMA forms/guidelines page: https://www.mwti.gov.ws/puma-2/
- Development Consent Application Form: https://www.mwti.gov.ws/wp-content/uploads/2022/09/Development-Consent-Application-Form_English.pdf
- Development Consent info sheet: https://www.mwti.gov.ws/wp-content/uploads/2022/09/INFOSHEET_Development-Consent-Application_2022-MWTI.pdf
- Building Permit Application Form: https://www.mwti.gov.ws/wp-content/uploads/2024/08/Building-Permit-Application-Form.pdf
- Planning and Urban Management Act 2004, FAO/FAOLEX mirror: https://faolex.fao.org/docs/pdf/sam51784.pdf . Use MWTI pages first and the FAOLEX copy as legislation mirror if MWTI PDFs move.
- Fire/emergency services: Samoa Fire and Emergency Services Authority (SFESA/FESA) approvals are referenced in MWTI building-permit forms; confirm current form requirements when checking a build.

Use:

- Any new datacenter building should leave traces through PUMA development consent, MWTI building permit, FESA/SFESA fire compliance, EPC connection, and project procurement. Samoa does not expose an online permit database, so absence is a weak negative signal.
- Grade **A** only when an official approval, project document, tender, or permit names the facility/site.

Queries:

```text
site:mwti.gov.ws PUMA ("data center" OR "data centre" OR telecommunications OR ICT OR "server room")
site:mwti.gov.ws "Development Consent" ("data center" OR "data centre" OR telecommunications OR cable OR ICT)
site:mwti.gov.ws "Building Permit" ("data center" OR "data centre" OR telecommunications OR ICT)
"Planning and Urban Management Act 2004" Samoa ("telecommunications" OR "ICT" OR "data centre" OR "data center")
"Samoa" (PUMA OR "development consent") ("data center" OR "data centre" OR "cable landing" OR telecommunications)
```

### 1.5 Energy and grid approvals

Primary sources:

- Electric Power Corporation: https://www.epc.ws/
- OOTR electricity regulation/orders: https://regulator.gov.ws/index.php/electricity-regulation/electricity-orders and https://regulator.gov.ws/index.php/electricity-regulation
- ADB Samoa energy project page/news, including Samoa solar/BESS support: https://www.adb.org/projects/46044-002/main and https://www.adb.org/news/adb-samoa-sign-landmark-agreement-solar-power-projects

Verified signals:

- EPC says it operates 8 hydro plants (7 Upolu, 1 Savai'i), solar farms at Apolima, Tuanaimato, Vaitele, Tanugamanono, Salelologa, and Mapuifagalele, a wind farm at Vailoa Aleipata, and diesel plants at Fiaga and Salelologa. EPC says it supplies all Samoa and has connected up to 99% of the population.
- EPC names hydro locations: Taelefaga, Lalomauga, Alaoa, Loto Samasoni, Fale ole Fee, Fuluasou, Tafitoala-Fausaga, and Vailoa Palauli.
- Any MW-scale datacenter would be a notable load on Samoa's small island grids and should have EPC/ADB/energy-sector traces. Do not accept large-load claims without power evidence.

Queries:

```text
site:epc.ws ("data center" OR "data centre" OR "large customer" OR "industrial" OR MW OR "connection")
site:epc.ws (Apia OR Tuasivi OR Salelologa OR Vaitele OR Fiaga) (power OR grid OR substation)
site:regulator.gov.ws electricity ("large customer" OR tariff OR connection OR "industrial")
"Samoa" EPC ("data center" OR "data centre" OR "large load" OR "MW")
"Samoa" (solar OR BESS OR substation) (Apia OR Salelologa OR Tuasivi OR Vaitele)
```

### 1.6 Company and legal-entity verification

Primary sources:

- Samoa Business Registry / MCIL: https://www.businessregistries.gov.ws/ . The site states that companies and the public can access company information through the online Samoa Company Registry.
- MCIL: https://mcil.gov.ws/

Use:

- Verify legal names and Samoa registration for operators, resellers, contractors, and any project vehicle. Use this especially for foreign/reseller claims and for names that are easy to confuse with American Samoa entities.
- A registry hit is **A-grade for legal existence**, but still not facility evidence.

Queries:

```text
site:businessregistries.gov.ws "Samoa Submarine Cable" OR SamoaTel OR "Computer Services" OR Starlink OR BlueWave
site:mcil.gov.ws ("foreign investment" OR "business licence" OR telecommunications OR ICT)
"Samoa Company Registry" ("data center" OR "data centre" OR hosting OR telecommunications)
"Starlink Samoa Ltd" "Samoa Company Registry" OR "businessregistries.gov.ws"
```

### 1.7 Official cloud-region absence checks

Use only official provider pages for A-grade absence/presence:

| Provider | Official page | Samoa signal |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; https://aws.amazon.com/about-aws/global-infrastructure/localzones/ | No WS Region/Local Zone found in this pass. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No WS public region found. |
| Google Cloud | https://cloud.google.com/about/locations ; https://datacenters.google/locations/ | No WS region/owned datacenter found; Samoa references are cable/connectivity, not cloud-region evidence. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No WS public region found. |

Queries:

```text
"Samoa" ("AWS Region" OR "AWS Local Zone" OR "Azure region" OR "Google Cloud region" OR "OCI region")
"Samoa" ("cloud region" OR hyperscale OR "data residency" OR "sovereign cloud")
```

## 2. Current Official Facility / Project Seed List

| Candidate | District | Status | Source grade | How to record |
|---|---:|---|---|---|
| SSCC Apia cable station / access point | Tuamasaga | Operational telecom cable station; interconnection/colocation-adjacent access under RIO | A | `telecom_cable_station`, not retail DC. Source: SSCC RIO 2026 + SSCC progress/home. |
| SSCC Tuasivi cable station / Savai'i access point | Fa'asaleleaga | Operational telecom cable station; interconnection/colocation-adjacent access under RIO | A | `telecom_cable_station`, not retail DC. Source: SSCC RIO 2026 + SSCC progress/home. |
| Government of Samoa data-center upgrade/establishment under DCRSP P180807 | Site not disclosed; likely Tuamasaga until evidence says otherwise | Planned / implementation-stage; World Bank indicators show capacity target through Oct 2029 | A | `government_data_center_project`; do not mark operational or assign exact site/capacity without procurement/completion evidence. |
| SamoaTel/state telecom core/gateway premises | Tuamasaga | Licensed telecom infrastructure lead | A for license/operator; B/C for facility inference | Record only if OOTR annual report, SamoaTel primary page, tender, or press names a switch/gateway/server facility. |
| Digicel Samoa / Vodafone Samoa core facilities | Tuamasaga | Licensed mobile operator network infrastructure | A for operator/license; B/C for facility inference | Telecom core only unless primary source names hosting/DC/colo. |
| CSL / Computer Services Ltd server-hosting premises | Tuamasaga | Licensed ISP/ICT provider with web/domain/backups/network services | A for official company services; C/B for physical server-room inference | Count only with primary facility/service-page proof. |
| Starlink Samoa Ltd | National service | Licensed connectivity service | A for license/government press; not a DC | Negative-control: connectivity only. |

## 3. Per-District Official Enumeration Strategy

Run the generic sweep once per district, then use the district-specific route below.

Generic sweep:

```text
"{District}" Samoa ("data center" OR "data centre" OR datacenter OR colocation OR hosting OR "server room" OR "cable station" OR "landing station" OR fibre OR fiber OR broadband OR ICT)
site:regulator.gov.ws "{District}" (telecommunications OR internet OR broadband OR cable OR electricity)
site:mcit.gov.ws "{District}" OR site:mof.gov.ws "{District}" (ICT OR digital OR broadband OR "data center" OR "data centre")
site:mwti.gov.ws "{District}" ("Development Consent" OR PUMA OR telecommunications OR ICT OR cable)
site:epc.ws "{District}" (grid OR power OR substation OR solar OR hydro)
```

| District | Expected yield | Official-first route | Notes / assignment rules |
|---|---|---|---|
| Tuamasaga | Highest | OOTR, MCIT/MOF/World Bank DCRSP, SSCC Apia/RIO, EPC, MWTI/PUMA, company registry | Assign Apia, Savalalo, Sogi, Matefele, Maluafou, Vaitele, Tuanaimato, Faleata, Moto'otua, Letogo, and Mulinu'u to Tuamasaga unless a source states another district. This is the default for government, operator HQ, bank, and private hosting leads. |
| Fa'asaleleaga | Medium | SSCC RIO/progress for Tuasivi; SamoaTel/operator searches for Salelologa/Tuasivi; EPC Salelologa grid | Tuasivi is the only A-grade non-Apia cable-station lead. Salelologa is a commercial/utility hub, but do not infer a DC from telecom presence. |
| A'ana | Low | MWTI/PUMA for Faleolo-area developments; EPC and airport/telecom records | Faleolo airport telecom and solar/power assets are not DCs. Record `no_projects` unless a primary build/procurement record appears. |
| Aiga-i-le-Tai | Very low | MWTI/PUMA and press for Mulifanua/Manono/Apolima; EPC Apolima solar | Ferry/airport-adjacent telecom and Apolima solar are false positives. |
| Atua | Low | EPC hydro/wind/solar terms; PUMA/MNRE for east/south Upolu development | Includes Lalomauga, Aleipata, Lotofaga/Lepa/Falealili areas depending on local naming; power assets are not DCs. |
| Va'a-o-Fonoti | Low | EPC Taelefaga hydro; PUMA and village-level sweep | Treat Taelefaga hydro as energy context only. |
| Gaga'emauga | Very low | Generic telecom/power sweep; note Upolu/Savai'i split/enclaves | Watch for Saleaula/Fagamalo telecom-only hits; no DC evidence found. |
| Gagaifomauga | Very low | Generic telecom/power sweep | North Savai'i coverage/tower hits only expected. |
| Palauli | Low | EPC Vailoa Palauli hydro; Salelologa-adjacent checks if source uses broad geography | Hydro asset only unless project evidence appears. |
| Satupa'itea | Very low | Generic telecom/power sweep | South Savai'i; telecom cabinets/towers only expected. |
| Vaisigano | Very low | Generic telecom/power sweep for Asau/Vaisala/Sataua | Northwest Savai'i; no facility-grade DC evidence found. |

Coverage check: this table covers all 11 districts exactly once.

## 4. False Positives And Grading Rules

- **American Samoa contamination**: reject Pago Pago, Tafuna, 'Ili'ili, ASH, Hawaiki, ASTCA-only, and Le Vasa AS-side assets as WS facilities. Keep only as onward-connectivity notes when relevant to SAS/Apia.
- **Cable station vs datacenter**: SSCC Apia/Tuasivi are A-grade telecom facilities with interconnection/colocation-adjacent access. They are not public retail datacenters unless future primary evidence says so.
- **Government DC timing**: DCRSP is A-grade as a funded government project. It remains planned/implementation-stage until MCIT/MOF/World Bank documents show procurement, completion, or operations.
- **License vs facility**: OOTR licenses prove a telecom/operator role. They do not prove a datacenter, hosting room, NOC, or switch site.
- **Starlink/satellite**: Starlink Samoa Ltd and approved Starlink resellers are connectivity, not datacenter capacity.
- **Reseller/VPS pages**: offshore SEO pages listing 'Samoa VPS' or 'Apia dedicated servers' are Grade C and should be ignored unless they provide a physical Samoa operator/site and an OOTR or registry anchor.
- **Power claims**: any >0.5 MW claim needs EPC or project-document evidence. Samoa's small island grids make large DC loads implausible without public utility traces.

## 5. Source Quick List

- OOTR: https://regulator.gov.ws/ ; licensing https://regulator.gov.ws/index.php/telecommunications-regulation/telecommunications/licensing ; telecom orders https://www.regulator.gov.ws/index.php/telecommunications-regulation/telecommunications/telecommunications-orders ; licensee PDF https://regulator.gov.ws/images/Telecommunications_Licensing_Rule/List-of-Telecommunications-Licensees-Final-2022_v3.pdf ; ICTSP https://regulator.gov.ws/images/Sector_Plan/ICTSP-2022-2027_English-Version_Signed.pdf ; Digital Samoa https://www.regulator.gov.ws/index.php/91-digital-samoa-project
- MCIT/MyGov/MOF/World Bank: https://mcit.gov.ws/publications/digital-samoa/ ; https://mygov.gov.ws/ ; https://www.mof.gov.ws/ ; https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099093024135596945
- SSCC: https://www.ssccsamoa.com/ ; RIO page https://www.ssccsamoa.com/about/rio-reference-interconnection-offer/ ; RIO 2026 PDF https://www.ssccsamoa.com/wp-content/uploads/2026/03/Rio-2026.pdf ; progress https://www.ssccsamoa.com/home/progress/ ; ADB Tui-Samoa project https://www.adb.org/projects/47320-001/main
- Planning/building: https://www.mwti.gov.ws/ ; PUMA https://www.mwti.gov.ws/puma/ ; forms https://www.mwti.gov.ws/puma-2/ ; development-consent form https://www.mwti.gov.ws/wp-content/uploads/2022/09/Development-Consent-Application-Form_English.pdf ; building permit form https://www.mwti.gov.ws/wp-content/uploads/2024/08/Building-Permit-Application-Form.pdf ; PUM Act mirror https://faolex.fao.org/docs/pdf/sam51784.pdf
- Energy: https://www.epc.ws/ ; OOTR electricity orders https://regulator.gov.ws/index.php/electricity-regulation/electricity-orders ; ADB energy https://www.adb.org/projects/46044-002/main
- Registry: https://www.businessregistries.gov.ws/ ; https://mcil.gov.ws/
- Connectivity/operator context: Starlink license https://www.samoagovt.ws/2025/01/press-release-starlink-samoa-cheapest-tariff-in-the-world/ ; Digicel/Telstra https://www.digicelpacific.com/news/telstra-acquires-digicel-pacific ; CSL https://csl.ws/
- Cloud absence: AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Google Cloud https://cloud.google.com/about/locations ; OCI https://www.oracle.com/cloud/public-cloud-regions/

Refresh instruction: on future runs, re-check OOTR licensee PDFs/orders, SSCC RIO version, World Bank P180807 ISR/procurement, MCIT/MOF tenders, and official cloud region pages before changing facility status.
