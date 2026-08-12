# NA Explorer Official - Namibia Datacenter Enumeration

Date: 2026-08-12. Country: Namibia (NA). Scope: official/regulatory-first methodology for identifying data centres, cable landing facilities, colocation rooms, and large ICT/server infrastructure in Namibia.

Reliability grades:
- A: primary source: government ministry/agency, regulator, municipality/local authority, Government Gazette, official company/operator page, official cloud-region page, BIPA registry.
- B: strong secondary source: established press/trade source naming operator, site/town, date, and project details.
- C: weak lead: aggregator, social media, consultant slide, unsourced announcement, or ambiguous "ICT/data" reference.

Use B/C material only to generate leads. Promote a record to A only after matching it to an official operator page, municipal/building record, Gazette/regulatory record, procurement notice, or registry entry.

## 0. Country Structure and Search Logic

Namibia has 14 first-level regions: Erongo, Hardap, //Karas, Kavango East, Kavango West, Khomas, Kunene, Ohangwena, Omaheke, Omusati, Oshana, Oshikoto, Otjozondjupa, and Zambezi. The main official statistical source for regional profiles is the Namibia Statistics Agency: https://nsa.org.na/document-category/regional-profiles/

There is no single national public register of data centres or building permits. Enumeration is therefore a cross-checking exercise:
1. Start with known operators and subsea/cable landing evidence.
2. Verify site facts through local authority planning/building-control records.
3. Check MEFT environmental records for listed activities that accompany data centres: diesel storage, backup generation, substations, water/cooling, telecoms infrastructure, construction in sensitive areas.
4. Check ECB/MME/NamPower/RED sources for generation, supply, wheeling, and grid-connection evidence.
5. Check CRAN licence categories and Gazette notices for telecoms/network-facility evidence.
6. Use BIPA to confirm legal names behind project proponents.
7. Use the Gazette and public procurement portals to catch state ICT/data-centre projects.

Priority geography:
- Priority 1: Khomas (Windhoek/Brakwater) and Erongo (Swakopmund/Walvis Bay). These are the only regions with confirmed commercial/cable-linked data-centre evidence.
- Priority 2: Oshana and Otjozondjupa because they sit on northern and central transport/power/telecom corridors.
- Priority 3/watch: //Karas and Hardap because of renewable power, hydrogen, mining, and port-adjacent industry.
- Priority 4: remaining regions, searched mainly to confirm absence and capture telecom/government ICT rooms.

## 1. Official Source Stack

### 1.1 Local Authority Planning and Building Control

Planning/building evidence is A-grade when it comes from a municipality, town council, regional council, or Gazette notice.

Core legal context:
- Local Authorities Act, 1992 and local authority building control.
- Town Planning Ordinance, 1954: town planning schemes, rezoning, consent-use, departures, building-line relaxations, and amendments often appear in the Government Gazette.
- Townships and Division of Land Ordinance, 1963: township establishment and land division, with Ministry of Urban and Rural Development involvement where relevant.

Verified portals and starting points:
- City of Windhoek: https://www.windhoekcc.org.na/
- City of Windhoek Building Control: https://www.windhoekcc.org.na/building-control/
- City of Windhoek engineering drawing submission: https://www.windhoekcc.org.na/submission-approval-of-drawings-for-private-developments/
- Municipality of Swakopmund: https://swakopmun.com/
- Swakopmund Design & Building Division: https://swakopmun.com/index/notices_item/11
- Municipality of Walvis Bay: https://www.walvisbaycc.org.na/
- Legal Assistance Centre Gazette PDFs, useful for town-planning schemes and amendments: https://www.lac.org.na/index.php/laws/gazettes/
- NamibLII Gazettes: https://namiblii.org/gazettes/
- Ministry of Justice Gazette portal: https://moj.gov.na/government-gazzete

Municipal query templates:
```text
site:windhoekcc.org.na "data centre"
site:windhoekcc.org.na "data center"
site:windhoekcc.org.na "server room"
site:windhoekcc.org.na "building plan" "data"
site:windhoekcc.org.na "Brakwater" "Paratus"
site:swakopmun.com "data centre"
site:swakopmun.com "building plan" "data"
site:walvisbaycc.org.na "data centre"
site:walvisbaycc.org.na "building plan" "data"
"data centre" "town planning scheme" Namibia
"data centre" "rezoning" Namibia
"data centre" "consent use" Namibia
"data centre" "building plan" Windhoek
"server hall" "building plan" Namibia
"diesel storage" "data centre" Namibia
```

Extract: local authority, council item/date, building-plan number, erf/farm/portion, street/town, landowner, applicant, operator, use class/zoning, floor area, generator/diesel details, power demand, water/cooling note, objections, approval conditions, completion/occupancy status.

### 1.2 MEFT Environmental Clearance / EIA

Environmental clearance is A-grade when sourced from MEFT, the Environmental Commissioner, a Government Gazette, or a government-hosted EIA/ECC record. Consultant-hosted EIAs are B unless they include a signed official clearance.

Verified portals:
- Ministry of Environment, Forestry and Tourism: https://www.meft.gov.na/
- MEFT EIA portal: https://eia.meft.gov.na/ (may block or time out under automated fetch; use browser and search-engine cache/index)
- EIA Tracker Namibia: https://eia-tracker.org.na/ (C/B lead source; corroborate against MEFT/Gazette)
- Environmental Information Service eLibrary: https://the-eis.com/elibrary/ (C/B lead source; corroborate against MEFT/Gazette)

Relevant triggers to search: storage of diesel or hazardous substances, backup generation, solar/embedded generation, transmission lines/substations, telecoms masts/fibre/cable landing facilities, water abstraction, industrial construction, and coastal/Dorob-sensitive construction.

Environmental query templates:
```text
site:eia.meft.gov.na "data centre"
site:eia.meft.gov.na "data center"
site:eia.meft.gov.na "server"
site:eia.meft.gov.na "Paratus"
site:eia.meft.gov.na "Telecom Namibia"
site:eia.meft.gov.na "cable landing"
site:eia.meft.gov.na "diesel storage"
"environmental clearance certificate" "data centre" Namibia
"EIA" "data centre" Namibia
"scoping report" "data centre" Namibia
"public participation" "data centre" Namibia
"Swakopmund" "cable landing station" "environmental"
```

Extract: MEFT application/reference, proponent, environmental assessment practitioner, listed activities, coordinates/erf/farm, generator rating, diesel volumes, grid connection, water source, public-participation dates, Environmental Commissioner decision, appeal status, renewal/transfer status.

### 1.3 Power and Grid Evidence

Power evidence is essential because data centres usually surface through large connections, substations, standby generation, or self-generation.

Verified portals:
- Ministry of Mines and Energy / Ministry of Mines, Energy and Industry: https://www.mme.gov.na/
- Electricity Control Board: https://www.ecb.org.na/
- ECB Licensing: https://www.ecb.org.na/licensing/
- ECB Public Notices: https://www.ecb.org.na/media-centre/public-notices/
- NamPower: https://www.nampower.com.na/
- Erongo RED: https://erongored.com/
- CENORED: https://cenored.com.na/
- NORED: https://www.nored.com.na/
- City of Windhoek: https://www.windhoekcc.org.na/

Regional distribution map for searches:
- Khomas: City of Windhoek Electricity inside Windhoek; NamPower/other local authority routes outside municipal supply areas.
- Erongo: Erongo RED and municipal/port/industrial loads around Swakopmund, Walvis Bay, Arandis, Usakos, Karibib, Omaruru.
- Otjozondjupa, Omaheke, parts of Kunene and Oshikoto: CENORED/NamPower.
- Oshana, Ohangwena, Omusati, Oshikoto, Kavango East, Kavango West: NORED plus Oshakati Premier Electric for Oshakati.
- Hardap, //Karas, Zambezi and remote areas: local authority/NamPower context; verify case by case.

Power query templates:
```text
site:ecb.org.na "data centre"
site:ecb.org.na "data center"
site:ecb.org.na "Paratus"
site:ecb.org.na "Telecom Namibia"
site:ecb.org.na "generation licence" "Windhoek"
site:ecb.org.na "generation licence" "Swakopmund"
site:ecb.org.na "MVA"
site:nampower.com.na "data centre"
site:nampower.com.na "substation" "Brakwater"
site:nampower.com.na "substation" "Swakopmund"
"Electricity Control Board" "licence application" "data centre"
"NamPower" "data centre" Namibia
"Erongo RED" "data centre"
"CENORED" "data centre"
"NORED" "data centre"
```

Extract: applicant, licence type/status, MW/MVA/kVA, grid node/substation, RED/local authority, wheeling/offtake, standby generation, solar/IPP tie-in, Gazette/public-hearing reference, decision date.

### 1.4 CRAN Telecoms Evidence

CRAN evidence is A-grade for telecoms licensing but not by itself proof of a data centre. Use it to verify network/service operators and cable/network-facility projects.

Verified portals:
- CRAN: https://www.cran.na/
- Licensing: https://www.cran.na/licensing/
- Telecommunications Licensees: https://www.cran.na/telecommunications-licensees/
- Public Hearings: https://www.cran.na/public-hearings/
- Notices: https://www.cran.na/notices/
- Government Gazettes: https://www.cran.na/government-gazettes/
- Infrastructure Sharing: https://www.cran.na/infrastructure-sharing/

Relevant categories to inspect: Class ECS, ECNS, Comprehensive ECS/ECNS, Network Facilities, individual licences, spectrum licences, infrastructure-sharing notices, cable landing/network facility matters, and Gazette decisions.

CRAN query templates:
```text
site:cran.na "data centre"
site:cran.na "data center"
site:cran.na "Paratus"
site:cran.na "Telecom Namibia"
site:cran.na "Liquid"
site:cran.na "MTC"
site:cran.na "Network Facilities"
site:cran.na "cable landing"
site:cran.na "licence application" "Gazette"
"CRAN" "Network Facilities Licence" Namibia
"CRAN" "public hearing" "Paratus"
"CRAN" "Starlink Internet Services Namibia" "Gazette"
```

Extract: licensee legal name, licence category, services/network scope, coverage area, spectrum if any, application date, objection/public hearing, Gazette number, approval/refusal status.

### 1.5 Gazette, Registry, Procurement, and Investment Sources

Use these to resolve official names and capture government ICT/data-centre work:
- NamibLII Gazettes: https://namiblii.org/gazettes/ (for example, 2026 index: https://namiblii.org/gazettes/na/2026)
- Legal Assistance Centre Gazettes: https://www.lac.org.na/index.php/laws/gazettes/
- Ministry of Justice Gazette portal: https://moj.gov.na/government-gazzete
- Parliament legislation: https://www.parliament.na/legislation/
- BIPA registry search: https://www.bipa.na/search/
- Namibia e-Procurement portal: https://eprocurement.gov.na/
- Ministry of Finance and Public Enterprises: https://mfpe.gov.na/
- Namibia Investment Promotion and Development Board: https://www.nipdb.com/
- MICT / government portal: https://www.gov.na/

Registry/procurement query templates:
```text
site:namiblii.org/gazettes "data centre" Namibia
site:namiblii.org/gazettes "data center" Namibia
site:namiblii.org/gazettes "Paratus"
site:namiblii.org/gazettes "Telecom Namibia"
site:eprocurement.gov.na "data centre"
site:eprocurement.gov.na "datacenter"
site:mfpe.gov.na "Data Centre"
site:gov.na "National Data Centre"
site:mict.gov.na "National Data Centre"
site:nipdb.com "data centre"
"Government Data Centre" Namibia procurement
"National Data Centre" Namibia "Strategic Plan"
```

Known official-government lead status: references to a "Data Centre of the Government" and "National Data Centre" exist in procurement/press contexts, but treat a new national facility as C/B until tied to an official strategic plan, budget vote, tender, award, site, or Gazette record.

## 2. Official Operator and Cloud-Region Seeds

Confirmed operator pages:
- Paratus Namibia data-centre services: https://paratus.africa/namibia/business-solutions/data-center-solutions/ (A). Confirms Armada Data Center service offering.
- Paratus Group data-centre services: https://paratus.africa/services/data-center-services/ (A).
- Paratus Namibia: https://paratus.africa/namibia/ (A).
- Telecom Namibia Infinitum co-location: https://www.telecom.na/tn-mobile/prepaid-plans/91-products/infinitum/133-co-location-corporate-solution (A).
- Telecom Namibia Infinitum FAQ: https://www.telecom.na/faq-s/90-products/corporate-products/118-infinitum-co-location-service (A).
- MTC Namibia: https://www.mtc.com.na/ (A for operator; do not infer a data centre without a specific page/filing).
- Liquid data centres: https://liquid.tech/data-centres/ (A for Liquid portfolio; as of this methodology, no Namibia data-centre page confirmed).

Official hyperscale region pages:
- AWS regions: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Microsoft Azure geographies/regions: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle cloud regions: https://www.oracle.com/cloud/public-cloud-regions/

Current interpretation: these official cloud pages show Africa/South Africa cloud-region presence but no Namibia cloud region. Do not record a hyperscale Namibia facility unless an official provider page or regulator/permit record names Namibia.

Subsea/cable sources to use as official or strong operator evidence:
- 2Africa official site: https://www.2africacable.net/
- Submarine Networks Equiano/Namibia articles: https://www.submarinenetworks.com/
- GeoCables Swakopmund inventory: https://geocables.com/location/swakopmund-namibia
- DCD Namibia tag/news: https://www.datacenterdynamics.com/en/tags/namibia/

Cable landing stations are not always commercial colocation data centres. Record them separately unless the source explicitly says colocation, data centre, hosting, or customer racks.

## 3. Known Namibia Facilities / Leads to Resolve

1. Paratus Armada Data Center, Brakwater/Windhoek, Khomas.
   - A source: Paratus Namibia data-centre page.
   - B corroboration: DCD reported launch in August 2022; Namibian/Namibian Sun/Republikein reported N$123m, Brakwater campus, DC1/DC2 halls and energy centres.
   - Still seek A-grade municipal/ECC/power records: City of Windhoek/Brakwater planning record, MEFT/EIA, ECB/NamPower/City Electricity connection.

2. Telecom Namibia Infinitum co-location, Windhoek, Khomas.
   - A source: Telecom Namibia Infinitum co-location product/FAQ pages.
   - Aggregators listing a "Telecom Namibia Datacenter" are C cross-checks only.
   - Still seek A-grade facility specifics: address, building-plan/ECC/power evidence, annual report or tender records.

3. Swakopmund cable landing/data-centre infrastructure, Erongo.
   - A/B sources: Paratus/Telecom Namibia/Google partner announcements and trade press around Equiano; DCD report on Telecom Namibia Equiano cable landing station; 2Africa official site for cable system status.
   - Treat as cable landing/ICT infrastructure unless a source explicitly establishes customer colocation/data-centre service.

4. National/Government Data Centre.
   - Current status: lead only unless tied to official strategic plan, budget, procurement, award, or site.
   - Search eProcurement, MFPE, MICT/gov.na, OPM records, and Gazette.

5. MTC, Liquid, banks, and enterprise ICT rooms.
   - Current status: operator/network leads only. Promote only with specific facility evidence.

## 4. Region-by-Region Official Strategy

For every region, run the standard sweep:
```text
"data centre" "{region}"
"data center" "{region}"
"colocation" "{region}"
"server room" "{main town}"
"data hall" "{main town}"
"building plan" "{main town}" "data"
"environmental clearance" "{main town}" "data"
"substation" "{main town}" "data centre"
"CRAN" "{main town}" "licence"
```

### Erongo - Priority 1
Main towns/sites: Swakopmund, Walvis Bay, Arandis, Usakos, Karibib, Omaruru.

Why: Swakopmund is Namibia's cable-landing hub; Walvis Bay is the port/industrial hub; Erongo RED is an important power source.

Official sources: Municipality of Swakopmund, Municipality of Walvis Bay, Erongo RED, NamPort (https://www.namport.com.na/), MEFT/EIA, CRAN, NamPower, Gazette.

Queries:
```text
"Swakopmund" "cable landing station"
"Swakopmund" "data centre"
"Walvis Bay" "data centre"
site:swakopmun.com "data centre"
site:walvisbaycc.org.na "data centre"
site:erongored.com "data centre"
site:nampower.com.na "Swakopmund" "substation"
```

Watch for: Equiano/WACS/2Africa landing facilities, Paratus and Telecom Namibia facilities, port/free-zone ICT, hydrogen/renewable-powered compute claims. Record cable landing stations separately from colocation sites.

### Hardap - Priority 3
Main towns/sites: Mariental, Rehoboth, Aranos.

Why: solar and central-south grid activity make it a power watch region, but no confirmed data-centre facility is known.

Official sources: Mariental Municipality, Rehoboth Town Council, Hardap Regional Council, NamPower, ECB, MEFT/EIA, Gazette.

Queries:
```text
"Mariental" "data centre"
"Rehoboth" "data centre"
"Hardap" "data centre"
"Hardap" "generation licence" "ECB"
site:namiblii.org/gazettes "Hardap" "data centre"
```

### //Karas - Priority 3 / Energy Watch
Main towns/sites: Keetmanshoop, Luderitz, Rosh Pinah, Oranjemund, Aus, Tsau //Khaeb.

Why: green hydrogen, wind/solar, mining, and port expansion are potential compute triggers, but current evidence is watch-list only.

Official sources: //Karas Regional Council, Luderitz and Keetmanshoop local authorities, NamPower, ECB, MME, MEFT/EIA, NamPort, Gazette.

Queries:
```text
"//Karas" "data centre"
"Karas" "data center"
"Luderitz" "data centre"
"Keetmanshoop" "data centre"
"green hydrogen" "data centre" Namibia
"Tsau //Khaeb" "data centre"
```

### Kavango East - Priority 4
Main towns/sites: Rundu, Divundu.

Why: northern/eastern population corridor and government telecom demand; no confirmed commercial data centre.

Official sources: Rundu local authority/regional council, NORED, NamPower, CRAN, MEFT/EIA, Gazette.

Queries:
```text
"Rundu" "data centre"
"Kavango East" "data centre"
"Rundu" "server room"
site:nored.com.na "Rundu"
```

### Kavango West - Priority 4
Main towns/sites: Nkurenkuru.

Why: low expected commercial data-centre probability; sweep for public-sector ICT, telecom nodes, and power projects.

Official sources: Kavango West Regional Council/local authority, NORED, NamPower, CRAN, MEFT/EIA, Gazette.

Queries:
```text
"Nkurenkuru" "data centre"
"Kavango West" "data centre"
"Kavango West" "server room"
```

### Khomas - Priority 1
Main towns/sites: Windhoek, Brakwater, Hosea Kutako corridor, Prosperita, Northern Industrial.

Why: capital city and confirmed colocation market. Known leads are Paratus Armada and Telecom Namibia Infinitum.

Official sources: City of Windhoek, NamPower, City of Windhoek Electricity, MEFT/EIA, CRAN, BIPA, eProcurement/MFPE/MICT for government ICT, Gazette.

Queries:
```text
"Windhoek" "data centre"
"Windhoek" "data center"
"Brakwater" "Armada" "data centre"
"Telecom Namibia" "Infinitum" "co-location"
site:windhoekcc.org.na "data centre"
site:windhoekcc.org.na "building plan" "Brakwater"
site:mfpe.gov.na "Data Centre" "Government"
```

### Kunene - Priority 4
Main towns/sites: Opuwo, Khorixas, Outjo.

Why: low commercial probability; check mining/tourism/telecom infrastructure and CENORED/NamPower power evidence.

Official sources: Kunene Regional Council/local authorities, CENORED where applicable, NamPower, MEFT/EIA, CRAN, Gazette.

Queries:
```text
"Opuwo" "data centre"
"Kunene" "data centre"
"Outjo" "server room"
site:cenored.com.na "Opuwo"
```

### Ohangwena - Priority 4
Main towns/sites: Eenhana, Helao Nafidi, Oshikango.

Why: border/trade corridor with telecom demand; no known commercial data centre.

Official sources: Ohangwena Regional Council/local authorities, NORED, NamPower, CRAN, MEFT/EIA, Gazette.

Queries:
```text
"Eenhana" "data centre"
"Oshikango" "data centre"
"Ohangwena" "server room"
site:nored.com.na "Ohangwena"
```

### Omaheke - Priority 4
Main towns/sites: Gobabis, Otjinene.

Why: eastern corridor; low expected commercial probability, but CENORED/NamPower and government ICT can surface leads.

Official sources: Gobabis local authority, Omaheke Regional Council, CENORED, NamPower, CRAN, MEFT/EIA, Gazette.

Queries:
```text
"Gobabis" "data centre"
"Omaheke" "data centre"
"Gobabis" "server room"
site:cenored.com.na "Gobabis"
```

### Omusati - Priority 4
Main towns/sites: Outapi, Ruacana, Oshikuku.

Why: northern public-service and telecom demand; no known commercial data centre.

Official sources: Omusati Regional Council/local authorities, NORED, NamPower, CRAN, MEFT/EIA, Gazette.

Queries:
```text
"Outapi" "data centre"
"Omusati" "data centre"
"Ruacana" "server room"
site:nored.com.na "Omusati"
```

### Oshana - Priority 2
Main towns/sites: Oshakati, Ongwediva, Ondangwa.

Why: northern commercial/government hub and power-distribution focus. Check for enterprise hosting, bank/government ICT rooms, and telecom POPs.

Official sources: Oshakati local authority, Oshakati Premier Electric, NORED, NamPower, CRAN, MEFT/EIA, Gazette.

Queries:
```text
"Oshakati" "data centre"
"Ongwediva" "data centre"
"Ondangwa" "data centre"
"Oshana" "server room"
"Oshakati Premier Electric" "data centre"
```

### Oshikoto - Priority 4
Main towns/sites: Tsumeb, Omuthiya, Grootfontein interface.

Why: mining/industrial and northern corridor; no confirmed commercial data centre.

Official sources: Oshikoto Regional Council/local authorities, NORED/CENORED by town, NamPower, CRAN, MEFT/EIA, Gazette.

Queries:
```text
"Tsumeb" "data centre"
"Omuthiya" "data centre"
"Oshikoto" "server room"
site:nored.com.na "Tsumeb"
site:cenored.com.na "Tsumeb"
```

### Otjozondjupa - Priority 2
Main towns/sites: Okahandja, Otjiwarongo, Grootfontein.

Why: central corridor near Windhoek, industrial land, and CENORED footprint. A plausible future edge/DR location.

Official sources: local authorities, Otjozondjupa Regional Council, CENORED, NamPower, CRAN, MEFT/EIA, Gazette.

Queries:
```text
"Okahandja" "data centre"
"Otjiwarongo" "data centre"
"Grootfontein" "data centre"
"Otjozondjupa" "server room"
site:cenored.com.na "data centre"
```

### Zambezi - Priority 4
Main towns/sites: Katima Mulilo, Ngoma border corridor.

Why: border/transit corridor; low commercial probability but check government ICT, telecom POPs, and regional power projects.

Official sources: Zambezi Regional Council/local authority, NamPower/local distribution, CRAN, MEFT/EIA, Gazette.

Queries:
```text
"Katima Mulilo" "data centre"
"Zambezi" "data centre" Namibia
"Katima Mulilo" "server room"
"Zambezi" "telecom" "licence" Namibia
```

## 5. Namibia-Specific Query Vocabulary

English:
```text
"data centre"
"data center"
"datacenter"
"colocation"
"co-location"
"server room"
"server hall"
"data hall"
"hosting facility"
"cloud services"
"Tier III"
"Tier 3"
"carrier neutral"
"cable landing station"
"network facilities licence"
"backup generator"
"diesel storage"
"substation"
"MVA"
"MW"
"environmental clearance certificate"
"town planning scheme"
"rezoning"
"consent use"
"building line relaxation"
```

Afrikaans/German variants:
```text
"data sentrum" Namibia
"rekenaarsentrum" Namibia
"kolokasie" Namibia
"Rechenzentrum" Namibia
site:republikein.com.na "data sentrum"
site:az.com.na "Rechenzentrum"
```

## 6. Record Schema and De-Duplication

For each candidate, store:
- Name and aliases.
- Operator and legal entity; BIPA status if available.
- Region, town, precise site: erf/farm/portion/street/coordinates.
- Facility type: commercial colocation, operator POP, cable landing station, government data centre, enterprise/server room, power/telecom-only lead.
- Status: rumour/lead, announced, planning/EIA, permitted, under construction, operational, expansion, decommissioned.
- Source grade and source URL for each fact.
- Planning/building refs.
- MEFT/ECC refs.
- ECB/MME/NamPower/RED refs and MW/MVA/kVA.
- CRAN licence/Gazette refs.
- Connectivity: cable, fibre, IX/peering, carrier-neutral evidence.
- Capacity: racks, halls, sqm, MW/MVA, redundancy, Tier claims.
- Last checked date.

De-duplicate by `(operator/legal entity, town/site, project name, capacity)`. One project may appear as press release, building plan, EIA, electricity licence, CRAN notice, and operator page.

## 7. Pitfalls and Grade Rules

- Do not treat a telecom licence as proof of a data centre.
- Do not treat a cable landing station as customer colocation unless the source explicitly says colocation/data-centre services are offered there.
- Do not infer a Namibia hyperscale region from South Africa cloud regions or Google Equiano.
- Do not promote MTC/Liquid/bank/government ICT rooms to data centres without facility-specific evidence.
- Aggregator listings such as DataCenterMap/DataCenters.com are C leads unless they link to an official page.
- Social posts can preserve dates and wording but remain C unless mirrored by an official page, Gazette, or reputable press.
- Gazette/regulator/municipal facts override press timing.
