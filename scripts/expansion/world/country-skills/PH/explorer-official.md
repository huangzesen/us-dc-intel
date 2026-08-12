# PH Explorer Official - Philippines Datacenter Enumeration Methodology

Date: 2026-08-12. Country: **PH Philippines**. Scope: official, regulatory, energy, environmental, incentives, privacy, and government-cloud sources for enumerating Philippine datacenter projects. Use this file for A-grade evidence and for upgrading or downgrading industry leads.

The Philippines does **not** publish a single national datacenter registry. A reliable census must be assembled from LGU permits, NTC registrations, DICT/GovCloud records, DENR-EMB ECC/CNC records, energy and grid evidence, PEZA/BOI incentives, NPC privacy registration, official operator pages, and official cloud infrastructure pages.

Current division coverage: use **18 regions**, not the older 17-region list. The Philippine Statistics Authority PSGC page states that there are 18 regions as of 31 July 2025, and PSA's 2024 PSGC update records the creation of the **Negros Island Region (NIR)** under RA 12000. NIR comprises Negros Occidental, Bacolod City, Negros Oriental, and Siquijor. Do not leave Negros Occidental only in Western Visayas or Negros Oriental/Siquijor only in Central Visayas for current work.

Reliability grades:

- **A** = primary or legally accountable source: LGU permit/ordinance, NTC issuance or registry, DICT circular/accreditation/FOI disclosure, DOE/ERC/NGCP/utility record, DENR-EMB ECC/CNC record, NPC registration, PEZA/BOI registration/release, official operator facility page, official cloud infrastructure page, statutory filing, annual report.
- **B** = credible secondary source with named facts: PNA, Reuters/AP, BusinessWorld, Inquirer, Philstar, Manila Bulletin, Manila Standard, BusinessMirror, Rappler, DCD, W.Media, law-firm alert that identifies the statute/order, contractor release.
- **C** = discovery lead only: directories, broker pages, social posts, conference agendas, reposted MoUs, unsourced market lists, job ads, and generic "cloud region" marketing.

## 0. Philippines-Specific Official Facts

- **Permitting is local.** Building permits, occupancy permits, zoning/locational clearances, business permits, electrical permits, and fire-safety inspections are issued by the city or municipality. RA 11032 requires streamlined/electronic business one-stop shops, but there is no national planning-permit portal comparable to Malaysia OSC.
- **NTC regulates telecommunications; DICT sets ICT policy.** Datacenter operators can appear in NTC records as value-added service (VAS) providers, data-transmission participants, telecom affiliates, or cable-landing/backbone entities. Treat entity registration as evidence of service authority, not proof of a specific building.
- **DTIP regime is new.** RA 12234, the Konektadong Pinoy Act, created the current open-access data-transmission framework. NTC MC 002-02-2026 prescribes DTIP eligibility and obligations. The NTC site may block automated access, so preserve screenshots/PDF copies when manually accessible and cross-check with law-firm summaries only as B-grade support.
- **Data-center SRF exemption is a regulatory lead.** NTC MO 001-02-2026 reportedly exempts data centers from annual Supervision and Regulation Fees for calendar years 2025-2028. Use the NTC memorandum if available; use Quisumbing Torres/Baker McKenzie only as B-grade confirmation.
- **Environmental records are unusually useful.** DENR-EMB's ECC Online public search allows searching approved/denied applications by project name, proponent, location, or ECC reference number with a minimum 10-character keyword.
- **Energy is often the strongest official trail.** Meralco dominates Metro Manila, Bulacan, Rizal, Cavite, Laguna, and parts of Batangas/Quezon. Outside Meralco, use regional private utilities and electric cooperatives, plus ERC, DOE, and NGCP.
- **Cloud regions:** as of this methodology date, AWS has Manila Local Zone and Direct Connect infrastructure, but no full AWS Philippines Region. Microsoft Azure, Google Cloud, and Oracle OCI official region lists do not show a full Philippines cloud region. Treat "Philippines cloud region" claims as C until an official region page exists.
- **Foreign land ownership is restricted.** Foreign datacenter investors normally use long leases, joint ventures, REIT/platform structures, or PEZA/BOI structures. Land ownership evidence rarely appears in public permit portals.

## 1. Official Source Register

| Lane | Source | URL / query surface | Use | Grade |
|---|---|---|---|---|
| Administrative regions | PSA PSGC | `https://psa.gov.ph/classification/psgc/regions` | Current 18-region coverage and region/province assignment | A |
| Negros Island Region | PSA PSGC update; RA 12000 text | `https://psa.gov.ph/content/second-quarter-2024-psgc-updates-creation-negros-island-region-and-correction-names-two`; `https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/97490` | NIR correction and component provinces | A |
| Telecom regulator | NTC | `https://ntc.gov.ph/`; `https://ntc.gov.ph/registry-of-data-transmission-industry-participants/` | DTIP, VAS, public telecom, cable landing, orders | A when NTC record is retrieved |
| DTIP framework | RA 12234; NTC MC 002-02-2026 | `https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/99600`; NTC MC PDF; law-firm summaries | Data-transmission authority, ISP/backbone/CLS screening | A for law/NTC, B for law firm |
| VAS | NTC VAS rules and regional NTC service lists | NTC central/regional sites; eLibrary VAS/VoIP circulars | Hosting/colocation/connectivity legal-entity seeds | A |
| DICT/GovCloud | DICT | `https://dict.gov.ph/`; Cloud First Policy/GovCloud circulars | GovCloud accreditation, NGDC, regional gov DCs | A |
| Environment | DENR-EMB ECC Online | `https://ecconline.emb.gov.ph/live/`; `https://ecconline.emb.gov.ph/live/search.aspx`; `https://cnconline.emb.gov.ph/` | ECC/CNC, proponent, site, EMB region | A |
| Energy | DOE, ERC, NGCP, utilities | `https://www.doe.gov.ph/`; `https://www.erc.gov.ph/`; `https://www.ngcp.com.ph/`; utility sites | PSA, MVA/MW, substations, energization | A |
| Incentives | PEZA, BOI/SIPP | `https://www.peza.gov.ph/`; `https://boi.gov.ph/`; `https://boi.gov.ph/strategic-investment-priority-plan/` | Registered projects and IT parks/buildings | A |
| Privacy | National Privacy Commission | `https://privacy.gov.ph/`; `https://npcregistration.privacy.gov.ph/` | PIC/PIP/DPO legal-entity seed | A |
| Cloud infrastructure | AWS, Azure, Google, Oracle official lists | AWS Local Zones/Direct Connect; Azure regions list; Google Cloud locations; OCI regions | Confirm or reject PH cloud-region claims | A |

## 2. Core Query Vocabulary

English:

```text
data center Philippines
data centre Philippines
datacenter Philippines
"data center" "{operator}" "{city_or_province}"
"colocation" "{operator}" Philippines
"hyperscale" "Philippines"
"AI data center" Philippines
"building permit" "data center" "{city}"
"occupancy permit" "data center" "{city}"
"locational clearance" "data center" "{city}"
"business permit" "data center" "{city}"
"Environmental Compliance Certificate" "data center"
"ECC" "data center" Philippines
"Meralco" "data center"
"ERC" "data center" "power supply agreement"
"NGCP" "data center"
"PEZA" "data center"
"BOI" "data center" "SIPP"
"NTC" "value-added service" "data center"
"NTC" "DTIP" "{operator}"
"GovCloud" "DICT" "data center"
"cloud region" Philippines
"AWS Local Zone" Manila
```

Filipino/Taglish variants:

```text
"data center" OR "datacenter" "{lgu_or_city}"
"malaking data center"
"serbisyo ng cloud"
"Sanggunian" "data center"
"ordinansa" OR "ordinance" "data center"
"paglulunsad" OR "groundbreaking" "data center"
"business permit" "data center"
"building permit" "data center"
```

Status/evidence words:

```text
announces / launches / opens / ready for service / operational
groundbreaking / breaks ground / topped out / under construction
planned / proposed / MoU / memorandum of agreement / investment pledge
ECC / CNC / EIA / IEE
PSA / power supply agreement / RCOA / retail electricity
MVA / MW / substation / 230kV / 115kV / 69kV / energized
PEZA registration / BOI registration / SIPP
DTIP / VAS / certificate of registration / SRF
```

## 3. LGU Permit Stack

Official datacenter records normally start at the LGU. For every facility lead, identify the exact city/municipality and barangay, then search the local records.

Permits and records to pull:

1. **Zoning / locational clearance** from the city/municipal planning and development office.
2. **Building permit** under the National Building Code, including electrical, mechanical, plumbing, sanitary, and fire-safety sub-permits.
3. **Occupancy permit / certificate of occupancy** as operating evidence.
4. **Business permit / mayor's permit**, including annual renewals.
5. **Sanggunian ordinances, resolutions, and minutes** for zoning changes, land-use approvals, road closures, and local incentives.
6. **BFP Fire Safety Inspection Certificate** and fire-safety permit trail.
7. **Local water and sanitary permits** for cooling, wastewater, fuel storage, and backup-generation impacts.

LGU query templates:

```text
site:qcgov.ph "data center"
site:quezoncity.gov.ph "data center"
site:taguig.gov.ph "data center"
site:makati.gov.ph "data center" OR "colocation"
site:pasigcity.gov.ph "data center"
site:paranaquecity.gov.ph "data center"
site:cityofmuntinlupa.gov.ph "data center"
"{city_lgu_domain}.gov.ph" "data center"
"{operator}" "{city}" "building permit"
"{operator}" "{city}" "occupancy permit"
"{operator}" "{city}" "business permit"
"{operator}" "{city}" "locational clearance"
"{city}" "data center" "Sanggunian"
"{city}" "data center" "ordinance"
```

Grade: A for actual LGU permit/ordinance/minutes; B for official LGU press releases that name the project; C for permit brokers or real-estate marketing.

## 4. NTC Regulator Trail

Use NTC records to identify the regulated entity and service lane. Do not use NTC registration alone as proof of a physical datacenter site.

What to extract:

1. **DTIP registration** under RA 12234 and NTC MC 002-02-2026: participant name, tier/category, validity, service area, allocated assets, compliance conditions, and registration date.
2. **VAS registration**: certificate holder, service description, validity, renewal status, and regional/central office source. This is the likely trail for hosting, managed services, and colocation providers.
3. **Legacy public telecommunications authority**: franchise/CPCN/provisional authority for PLDT, Globe/Innove, Converge, DITO, PT&T, ETPI/Eastern Telecom, and other carriers.
4. **Cable landing / international gateway / backbone authorizations**: useful for subsea-backed clusters in La Union, Batangas, Cavite, Aurora/Baler, Cagayan/Claveria, Davao/Digos, and similar nodes.
5. **SRF exemption records**: MO 001-02-2026 or successor orders naming data centers and fee treatment.

NTC query templates:

```text
site:ntc.gov.ph "data center"
site:ntc.gov.ph "DTIP" "{operator}"
site:ntc.gov.ph "Data Transmission Industry Participants"
site:ntc.gov.ph "VAS" "{operator}"
site:ntc.gov.ph "value-added service" "{operator}"
site:ntc.gov.ph "Supervision and Regulation Fees" "data centers"
site:ntc.gov.ph "cable landing" "{operator}"
site:region7.ntc.gov.ph "{operator}" "VAS"
site:ntcr4a.com "{operator}" "VAS"
"NTC" "DTIP" "{operator}" Philippines
"NTC" "value-added service" "{operator}" Philippines
"NTC" "data centers" "SRF" "2028"
```

Reliability rules:

- A = retrieved NTC order, registry row, certificate, or official regional NTC page.
- B = law-firm or credible press summary that identifies the exact NTC order/circular.
- C = operator marketing that says "licensed" without a certificate or order number.

## 5. DICT / GovCloud / Government Data Centers

DICT records identify government cloud providers and public-sector datacenter projects. Government facilities may not publish commercial-level capacity or address detail; preserve the exact public wording.

Sources and uses:

- DICT main site: `https://dict.gov.ph/`
- Cloud First Policy and GovCloud accreditation circulars: search DICT PDFs and `cms-cdn.e.gov.ph`.
- FOI portal: `https://www.foi.gov.ph/agencies/dict/`, search "National Government Data Center", "GovCloud", "NGDC".
- eGovPH/government portal: `https://www.gov.ph/` and `https://egovapp.ph/`.
- BCDA/JHMC/DICT records for the **North Luzon Data Center** at Camp John Hay/Baguio.

DICT query templates:

```text
site:dict.gov.ph "data center"
site:dict.gov.ph "National Government Data Center"
site:dict.gov.ph "GovCloud" "accredited"
site:dict.gov.ph "Cloud First Policy"
site:foi.gov.ph "National Government Data Center" "DICT"
"North Luzon Data Center" "DICT" "BCDA" "John Hay"
"regional data center" "DICT" "{region}"
"GovCloud" "{operator}" Philippines
```

Grade: A for DICT circulars, accreditation lists, FOI responses, and official BCDA/JHMC records; B for credible press describing official DICT projects.

## 6. Energy and Grid Enumeration

Energy records often reveal more than planning records. Always search the utility and regulatory trail for large campuses.

National and utility sources:

- DOE: `https://www.doe.gov.ph/`
- ERC: `https://www.erc.gov.ph/`
- NGCP: `https://www.ngcp.com.ph/`
- Meralco: `https://www.meralco.com.ph/`
- NEA electric cooperative references: `https://www.nea.gov.ph/`
- IEMOP/WESM: `https://www.iemop.ph/`
- Regional utilities: Davao Light, Visayan Electric/VECO, CEPALCO, MORE Power, electric cooperatives such as PELCO/TARELCO/CENECO.

What to extract:

1. Customer/project name in a PSA, RCOA contract, energization notice, grid-connection agreement, or substation project.
2. MW/MVA load, voltage, transformer capacity, dedicated substation, feeder names, and energization date.
3. ERC decisions or filings approving a supply arrangement or rate impact.
4. NGCP transmission projects that name a large load, industrial park, or connection point.
5. Backup generation and fuel storage from EMB/LGU records.

Energy query templates:

```text
site:meralco.com.ph "data center"
"Meralco" "{operator}" MW OR MVA
"Meralco" "data center" "substation"
site:erc.gov.ph "data center"
site:erc.gov.ph "{operator}" "power supply agreement"
site:doe.gov.ph "data center"
site:ngcp.com.ph "data center"
"{operator}" "{city}" "PSA" "power"
"{operator}" "{city}" "substation"
"data center" "VECO" OR "Visayan Electric"
"data center" "Davao Light"
"data center" "CEPALCO"
"data center" "MORE Power"
```

Grade: A when DOE/ERC/NGCP/utility names the customer, project, load, or grid asset; B for operator-stated power details; C for generic "power secured" claims.

## 7. DENR-EMB Environmental Trail

Use DENR-EMB for project-level location, proponent, and environmental conditions.

Sources:

- EMB main site: `https://emb.gov.ph/`
- ECC Online: `https://ecconline.emb.gov.ph/live/`
- ECC public search: `https://ecconline.emb.gov.ph/live/search.aspx`
- CNC Online: `https://cnconline.emb.gov.ph/`
- EIA Division: `https://eia.emb.gov.ph/`

What to extract:

- ECC/CNC reference number, issuance date, proponent, project name, project description, location, EMB regional office, and approval/denial status.
- Conditions mentioning cooling, water source, wastewater, backup generators, fuel tanks, air/noise permits, construction traffic, flood or seismic risks.
- Alternative proponent names: SPVs, landowners, industrial park operators, construction subsidiaries, or utility project names.

Environmental query templates:

```text
site:ecconline.emb.gov.ph "{operator}"
site:ecconline.emb.gov.ph "data center"
"Environmental Compliance Certificate" "{operator}" Philippines
"ECC" "data center" "{city}"
"CNC" "{operator}" "data center"
site:emb.gov.ph "data center"
"{industrial_park}" "ECC" "data center"
"{barangay}" "{city}" "data center" "ECC"
```

Grade: A for EMB records. Absence from public search is not proof of no ECC/CNC; repeat with legal-entity, SPV, park, and barangay keywords.

## 8. NPC Privacy Trail

The National Privacy Commission regulates Personal Information Controllers and Personal Information Processors under RA 10173 and NPC circulars. NPC registration is useful for entity normalization and compliance evidence, but it is not physical-facility evidence.

Sources:

- NPC: `https://privacy.gov.ph/`
- PIC/PIP guidance: `https://privacy.gov.ph/pips-and-pics/`
- Registration guidance: `https://privacy.gov.ph/pips-and-pics/register/`
- NPCRS portal: `https://npcregistration.privacy.gov.ph/`

Queries:

```text
site:privacy.gov.ph "{operator}" "PIC"
site:privacy.gov.ph "{operator}" "PIP"
"National Privacy Commission" "{operator}" "data center"
"NPCRS" "{operator}" Philippines
```

Grade: A for NPC records; use only as a legal-entity seed unless paired with a facility source.

## 9. PEZA / BOI / SIPP Incentive Trail

Use PEZA/BOI to locate registered IT parks, IT buildings, and incentivized datacenter projects.

Sources:

- PEZA: `https://www.peza.gov.ph/`
- BOI: `https://boi.gov.ph/`
- SIPP: `https://boi.gov.ph/strategic-investment-priority-plan/`
- 2026 SIPP approval release: `https://pco.gov.ph/news_releases/president-marcos-approves-2026-strategic-investment-priority-plan/`
- CREATE/CREATE MORE legal framework for incentives.

What to extract:

1. Registered enterprise name, project title, registered activity, registered location, investment amount, and status.
2. PEZA IT park/building hosting clues: Eastwood Cyberpark, BGC/Taguig IT parks, Makati CBD IT buildings, Laguna Technopark, Cebu IT Park, Clark/Subic ecozones, Carmelray/LISP/industrial parks.
3. BOI/SIPP category: datacenter development, digital infrastructure, AI/data science, off-grid/renewable infrastructure where explicitly listed.

Queries:

```text
site:peza.gov.ph "data center"
site:peza.gov.ph "{operator}"
"PEZA" "data center" "{city}"
"IT Park" "data center" "{city}" PEZA
site:boi.gov.ph "data center"
site:boi.gov.ph "{operator}" "data center"
"BOI" "data center" "{operator}"
"SIPP" "data center" 2026 Philippines
"CREATE MORE" "data center" Philippines
```

Grade: A for PEZA/BOI official registration and releases; B for credible press recaps; C for incentive consultants.

## 10. Official Cloud Infrastructure Checks

Always check official provider infrastructure pages before accepting cloud-region claims.

| Provider | Official pages | PH status as of 2026-08-12 | Enumeration use |
|---|---|---|---|
| AWS | `https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/`; `https://aws.amazon.com/directconnect/locations/`; AWS "What's New" | Manila Local Zone is official; Direct Connect is present near/in ePLDT Makati infrastructure and 100G expansion was announced in 2025. No full PH Region listed. | A for Local Zone/Direct Connect existence; B/C for physical node address unless AWS or host confirms. |
| Microsoft Azure | `https://learn.microsoft.com/en-us/azure/reliability/regions-list`; `https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/` | No public Azure Philippines Region in official region lists. | Do not count PH region rumors. Track Microsoft PH AI/digital-infra announcements separately. |
| Google Cloud | `https://cloud.google.com/about/locations`; `https://datacenters.google/locations/` | No Google Cloud Philippines Region and no Google-owned Philippines datacenter location on official list. | Treat talks/rumors as leads only. |
| Oracle OCI | `https://www.oracle.com/cloud/cloud-regions/` | No OCI Philippines Region. | Track only official future-region announcements. |

Cloud queries:

```text
"AWS Local Zone" Manila
"AWS Direct Connect" Makati Philippines
"Azure" "Philippines" "region" "Microsoft Learn"
"Google Cloud" "Philippines" "region"
"Oracle" "Philippines" "cloud region"
```

## 11. Division-by-Division Official Strategy

### Tier 1 - National Capital Region (NCR)

Key LGUs: Makati, Pasig, Taguig, Quezon City, Parañaque, Muntinlupa, Pasay, Mandaluyong.

Known official lanes: VITRO Makati/Pasig/Parañaque, STT Makati/Fairview, Equinix/TIM Manila, Converge Pasig/Parañaque leads, AWS Direct Connect/Local Zone ecosystem, Meralco supply, PEZA IT buildings.

```text
"Makati" "data center" "building permit"
"VITRO Makati" "Meralco"
"Pasig" "data center" "Converge"
"Quezon City" "Fairview" "data center" "building permit"
"Parañaque" "data center" "Converge"
"Taguig" "AWS Local Zone" OR "Direct Connect"
site:qcgov.ph "data center"
site:makati.gov.ph "data center"
site:pasigcity.gov.ph "data center"
"NCR" "data center" "ECC"
```

### Tier 1 - CALABARZON (Region IV-A)

Provinces: Cavite, Laguna, Batangas, Rizal, Quezon.

Clusters: Sta. Rosa/Laguna, General Trias/Cavite, Cainta/Rizal, Batangas/Nasugbu subsea and industrial parks, Meralco fringe.

```text
"Sta. Rosa" OR "Santa Rosa" "data center" "VITRO"
"Pulong Santa Cruz" "data center"
"General Trias" "data center" "STT" OR "Cavite"
"Cainta" "SpaceDC" "MNL1"
"Laguna" "data center" "ECC"
"Batangas" "data center" "substation"
"Nasugbu" "cable landing"
"Calamba" OR "Biñan" OR "Cabuyao" "data center"
```

### Tier 1 - Central Luzon (Region III)

Provinces: Aurora, Bataan, Bulacan, Nueva Ecija, Pampanga, Tarlac, Zambales.

Clusters: Clark/Angeles, New Clark City/Capas, Subic, Bataan/AFAB, Bulacan, Baler/Aurora cable landing.

```text
"Clark Global City" "data center" "DITO"
"Clark Freeport" "data center" CDC
"New Clark City" "data center" BCDA
site:newclark.ph "data center"
"Subic" "data center" SBMA
"Bataan" "data center" AFAB
"Bulacan" "data center" "Meralco"
"Baler" OR "Aurora" "cable landing" "data center"
"Pampanga" "data center" PELCO
"Tarlac" "data center" TARELCO
```

### Tier 2 - Central Visayas (Region VII)

Current after NIR: Bohol and Cebu remain core; Negros Oriental and Siquijor are NIR.

Clusters: Cebu City, Mandaue, Lapu-Lapu/Mactan, Cebu IT Park, Cebu Business Park, VECO service area.

```text
"Cebu" "data center" "VITRO" OR "ePLDT"
"Mandaue" "data center" "VECO"
"Cebu IT Park" "data center"
"Lapu-Lapu" OR "Mactan" "data center"
site:cebucity.gov.ph "data center"
"Cebu" "data center" "ECC"
```

### Tier 2 - Davao Region (Region XI)

Provinces/cities: Davao City, Davao de Oro, Davao del Norte, Davao del Sur, Davao Occidental, Davao Oriental.

Clusters: Davao City STT/Globe and cable landing, Digos Apricot landing, Davao Light.

```text
"Davao" "data center" "STT" OR "Globe"
"Davao City" "data center" "Davao Light"
"Digos" "cable landing" "Apricot"
"Bifrost" "Davao" "data center"
site:davaocity.gov.ph "data center"
"Davao" "data center" "ECC"
```

### Tier 2 - Negros Island Region (NIR)

Components: Negros Occidental including Bacolod City, Negros Oriental, and Siquijor.

Expect BPO/edge/disaster-recovery leads in Bacolod and Dumaguete; use current NIR assignment in records.

```text
"Bacolod" "data center"
"Negros Occidental" "data center"
"Dumaguete" "data center"
"Negros Oriental" "data center"
"Siquijor" "data center"
"Negros Island Region" "DICT" "data center"
"Bacolod" "data center" "CENECO"
```

### Tier 2 - Western Visayas (Region VI)

Current after NIR: Aklan, Antique, Capiz, Guimaras, and Iloilo. Bacolod/Negros Occidental are NIR.

Cluster: Iloilo City/Iloilo Business Park, MORE Power, BPO/edge.

```text
"Iloilo" "data center" "MORE Power"
"Iloilo Business Park" "data center"
"Western Visayas" "data center" DICT
"Aklan" OR "Capiz" OR "Antique" OR "Guimaras" "data center"
```

### Tier 2 - Ilocos Region (Region I) and CAR

Ilocos clusters: La Union cable landings at Luna/San Fernando, Ilocos Norte legacy leads. CAR cluster: Baguio/Camp John Hay North Luzon Data Center.

```text
"La Union" "cable landing" "data center"
"San Fernando" OR "Luna" "La Union" "data center"
"Baguio" "data center" "John Hay"
"North Luzon Data Center" "DICT"
"Cordillera" "data center" DICT
"Benguet" "data center"
```

### Tier 2 - Cagayan Valley (Region II)

Clusters: Claveria/Cagayan cable landing, Tuguegarao regional government/edge.

```text
"Claveria" "Cagayan" "cable landing"
"Claveria" "data center"
"Tuguegarao" "data center"
"Cagayan Valley" "data center" DICT
```

### Tier 2 - Northern Mindanao (Region X)

Clusters: Cagayan de Oro/CEPALCO, Phividec Industrial Estate, Iligan.

```text
"Cagayan de Oro" "data center" CEPALCO
"Phividec" "data center" OR "ICT"
"Misamis Oriental" "data center"
"Iligan" "data center"
"Northern Mindanao" "data center" DICT
```

### Tier 3 - Bicol (V), Eastern Visayas (VIII), Zamboanga Peninsula (IX), Soccsksargen (XII), Caraga (XIII), BARMM, Mimaropa (IV-B)

Expect government, telco edge, disaster recovery, cable/backbone, and energy-led leads rather than commercial hyperscale campuses.

```text
"Bicol" OR "Legazpi" OR "Naga" "data center"
"Tacloban" OR "Leyte" "data center"
"Zamboanga" "data center"
"General Santos" OR "Koronadal" "data center"
"Butuan" OR "Surigao" "data center"
"Cotabato City" OR "BARMM" "data center"
"Puerto Princesa" OR "Palawan" "data center"
"Mimaropa" "data center" DICT
"{city}" "data center" government OR DICT
```

## 12. Minimum Official Record Schema

```text
country: PH
region_current: one of the 18 PSGC regions
province
city_or_municipality
barangay_or_site
facility_or_project_name
operator_brand
legal_entity
status: proposed | MoU-only | permit-stage | under-construction | ready-for-service | operating | cancelled
evidence_grade: A | B | C
official_sources: LGU | NTC | DICT | EMB | DOE/ERC/NGCP/utility | PEZA | BOI | NPC | cloud-official
permit_numbers
ecc_or_cnc_reference
ntc_registration_type: DTIP | VAS | PTE | CLS | unknown
power_MW_or_MVA
utility_or_grid_node
incentive_registration
source_urls
source_dates
notes_on_uncertainty
```

## 13. Red Flags

- Old 17-region coverage is stale after RA 12000/NIR. Reassign Negros and Siquijor records using current PSGC.
- "Manila" usually means Metro Manila marketing, not necessarily the City of Manila. Resolve to Makati, Pasig, Taguig, Quezon City, Parañaque, etc.
- DTIP/VAS registration confirms a legal/service lane, not a physical facility.
- ECC/CNC absence in public search is not dispositive; search SPV, landowner, park, barangay, utility-project, and contractor names.
- MoUs and presidential investment meetings are not facilities until paired with LGU, EMB, utility, PEZA/BOI, or operator facility evidence.
- Subsea cable landing stations are connectivity anchors, not colocation datacenters unless separately evidenced.
- Power capacity claims need utility/ERC/NGCP corroboration before being stored as operating MW.
