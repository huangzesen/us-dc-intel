# KE Explorer Official - Kenya Datacenter Enumeration via Planning, Environmental, Energy, Cloud, Colo, and Regulator Sources

Date: 2026-08-12. Country: **KE Kenya**. Division model: **47 counties**. Angle: **official/regulatory/cloud pipeline** for finding commercial, hyperscale, government, and telecom data-centre facilities.

Reliability grades:
- **A** = primary/official/legal source: county permit workflow, NEMA EIA/SEA/EIA licence material, NCA project registration, CA Kenya licence register/market structure, Kenya Power/KETRACO/EPRA/KenGen official material, official cloud-provider statement, official operator page.
- **B** = strong secondary source: trade press, Uptime Institute certification record, SEZ/developer announcement, investor/partner press release, reputable datacenter directory when corroborated.
- **C** = weak lead: generic market report, social post, unsupported directory entry, county ICT strategy without facility evidence.

---

## 0. Kenya-specific structure facts

- Kenya does **not** have one complete public datacenter planning-register search. Enumeration works by joining county development approvals, NEMA environmental records, NCA construction registration, CA Kenya telecom licensing, power-grid evidence, official cloud-region pages, and operator pages.
- Most high-recall public evidence is **not labelled as a planning permit**. Use the Kenyan approval chain: county construction/development permit -> NEMA EIA/ESIA/SEA -> NCA project registration -> Kenya Power/KETRACO connection/substation/tender evidence -> CA Kenya telecom/service licensing if commercial services are offered.
- Datacenter activity is highly clustered around **Nairobi City**, **Kiambu/Tatu City/Ruiru/Limuru/Thika**, **Mombasa**, **Konza/Machakos-Makueni-Kajiado boundary**, **Nakuru/Olkaria/Naivasha**, and **Kisumu**. Most other counties will be negative searches unless a government/county data centre, telecom exchange, SEZ, geothermal park, or fibre landing/route project appears.
- English is sufficient for most official records. Use both spellings: `data centre` and `data center`; also try `datacentre`, `server room`, `server farm`, `cloud`, `colocation`, `co-location`, `ICT hub`, `Tier III`, `hyperscale`, `substation`, `MVA`, `MW`, and named operators.
- Treat cloud-region evidence as **metro/county seeds only**. Microsoft/G42 announced an East Africa Azure cloud region tied to an Olkaria green data-centre campus; Oracle announced intent to open a Kenya public cloud region. AWS and Google official public-region lists did not show a Kenya region in the checked pages; their edge/partner presence should not be converted into facility records without local evidence.

---

## 1. Grade A official portals and regulatory sources

### 1.1 County development and construction permitting

- **KenInvest eProcedures / Kenya Investment Facilitation Portal**: https://eprocedures.investkenya.go.ke/
  - Official `.go.ke` portal managed by Kenya Investment Authority. It indexes property/environment/building procedures, construction permits for several counties, NCA project registration, NEMA EIA licences, CA telecom licences, and energy permits.
  - Use the procedure database by sector `Information and communication technology`, `Energy`, and `Building and construction`, then location/county. The portal explicitly lists construction permits for counties including Nairobi, Kisumu, Mombasa, Uasin Gishu, Kilifi, Meru, Nyeri, Laikipia, Nakuru, Nyandarua, Makueni, Lamu, Busia, Narok, Siaya, Kirinyaga, Embu, etc.
  - Grade **A** for procedure requirements and named official routing. Grade **A** for any official permit/certificate obtained from the linked county/NCA/NEMA system.
- **Nairobi Planning and Development Management System**: https://edev.nairobiservices.go.ke/
  - Official Nairobi plan portal. Use for Nairobi City projects, especially Mombasa Road/Cabanas, Sameer Business Park, Karen/Langata, Upper Hill, Westlands, and industrial sites.
  - If public search is account-gated, use it as an official workflow reference, then search the web for indexed PDFs/notices from `nairobi.go.ke`, `nairobiservices.go.ke`, applicant names, LR numbers, and ward/location names.
- **National Construction Authority (NCA)**: https://www.nca.go.ke/ and project registration page https://www.nca.go.ke/project-registration
  - NCA states that construction projects are registered through its project-registration portal. Use this as a construction-stage confirmation path after county/NEMA evidence.
  - Search patterns:
```text
site:nca.go.ke "data centre"
site:nca.go.ke "data center"
site:nca.go.ke "Konza" "Data Centre"
site:nca.go.ke "Tatu City" "data centre"
site:nca.go.ke "project registration" "{operator}"
```

County permit query templates:
```text
site:{county-domain} "data centre"
site:{county-domain} "data center"
site:{county-domain} datacentre
site:{county-domain} "server room" "construction"
site:{county-domain} "development permission" "data centre"
site:{county-domain} "construction permit" "data centre"
site:{county-domain} "change of user" "data centre"
"{county}" "data centre" "EIA"
"{county}" "data center" "NEMA"
"{operator}" "{county}" "LR No" "data centre"
```

Extract from permit/planning documents: county, sub-county/ward, LR/plot number, road/industrial park, applicant/proponent/SPV, development description, floorspace, rack/data-hall count, IT load MW, utility import MVA, generator/fuel storage, water demand, EIA licence/status, NCA registration, construction/occupation dates.

### 1.2 NEMA environmental approvals

- **National Environment Management Authority (NEMA)**: https://nema.go.ke/
- EIA service page: https://nema.go.ke/services/environment-impact-assessment-eia/
- NEMA publication/upload search is high value because many study reports are public PDFs under `https://nema.go.ke/wp-content/uploads/`.
- Datacenters may appear as commercial/ICT buildings, industrial parks, SEZ facilities, substations, fibre projects, backup-generator/fuel-storage projects, or components within SEA/EIA reports. NEMA is high precision but not complete.

NEMA query templates:
```text
site:nema.go.ke/wp-content/uploads "data centre" Kenya
site:nema.go.ke/wp-content/uploads "data center" Kenya
site:nema.go.ke/wp-content/uploads "datacentre"
site:nema.go.ke/wp-content/uploads "server room"
site:nema.go.ke/wp-content/uploads "{operator}" "Environmental Impact"
site:nema.go.ke/wp-content/uploads "{project}" "Environmental and Social Impact Assessment"
site:nema.go.ke/wp-content/uploads "Tatu City" "data centre"
site:nema.go.ke/wp-content/uploads "KenGen Green Energy Park" "data"
site:nema.go.ke/wp-content/uploads "Konza" "data centre"
site:nema.go.ke/wp-content/uploads "substation" "data centre"
```

What to extract: NEMA reference/report number, proponent, EIA expert, LR/plot, coordinates, water and wastewater, DG sets and fuel storage, noise/air-quality modelling, construction period, connected power/substation, public-participation notices, mitigation measures. Grade **A** for NEMA-hosted EIA/ESIA/SEA reports and EIA licences; grade **B** for trade press summarizing NEMA documents.

### 1.3 Communications Authority of Kenya licensing

- **CA Kenya Market Structure**: https://www.ca.go.ke/market-structure
  - CA says the current telecommunications market structure was established in April 2026 under the Unified Licensing Framework. The market structure includes Network Facilities Provider Tier 1/2/3 licences and Applications Service Provider (ASP) licences.
  - CA's revised licence terms are relevant because commercial data centres may now fall under telecom infrastructure/service licensing when they deploy commercial communications infrastructure, provide colocation/cloud/connectivity, or interconnect third parties.
- **CA Licensee Register**: https://www.ca.go.ke/licensee-register
  - Use the `Register of Telecommunications Licensees as at June 2026` and older registers to search operator legal names: `IX AFRICA`, `AFRICA DATA CENTRES`, `ICOLO`, `DIGITAL REALTY`, `SAFARICOM`, `AIRTEL`, `LIQUID`, `PAIX`, `WANANCHI`, `KONZA`, `ECOCLOUD`, `G42`, `ORACLE`, `MICROSOFT`.
- **CA License Application Forms & Fees**: https://www.ca.go.ke/license-application-forms-fees
  - Use for licence-category fee/requirement context and form names.

CA query templates:
```text
site:ca.go.ke "data centres" "Network Facilities Provider"
site:ca.go.ke "Commercial Data Centres"
site:ca.go.ke "IX AFRICA" "licence"
site:ca.go.ke "AFRICA DATA CENTRES" "licence"
site:ca.go.ke "ICOLO" "licence"
site:ca.go.ke "SAFARICOM" "data centre"
site:ca.go.ke "Register of Telecommunications Licensees" "{operator}"
```

Use CA records as **operator/service-licence evidence**, not necessarily facility-count evidence. A licensed company may operate multiple facilities, and a facility may be marketed through a parent/subsidiary name.

### 1.4 Government cloud / ICT Authority / Konza

- **Ministry of Information, Communications and the Digital Economy**: https://ict.go.ke/
  - Search ministry news and policy PDFs for `data centres`, `cloud services`, `Kenya Cloud Policy`, `sovereign cloud`, `Digital Superhighway`, `AI Infrastructure`, and named projects.
  - Useful official context: 2026 ministry news includes government commitment to data centres/cloud services; 2026 Kenya Cloud Policy implementation material discusses government cloud providers/data centres.
- **ICT Authority**: https://icta.go.ke/
  - Search ICTA project pages for Government Data Centre, virtual/cloud services, disaster recovery, county mini data centres, and government cloud providers.
- **Konza Technopolis Development Authority**: https://konza.go.ke/ and Konza Cloud page https://konza.go.ke/konza-cloud/
  - Grade **A** for the Konza National Data Centre / Konza Cloud existence and official service description. County attribution is tricky because Konza is commonly described across the Machakos/Makueni/Kajiado buffer/planning area; assign to the parcel-confirmed county when a source gives the LR/parcel, otherwise note the boundary caveat.

---

## 2. Power, grid, geothermal, and energy evidence

### 2.1 Kenya Power and distribution connection evidence

- **Kenya Power (KPLC)**: https://kplc.co.ke/
  - Kenya Power transmits, distributes, and retails electricity nationally. Use as the main trail for service applications, tenders, substations, large commercial/industrial connections, fibre-on-power-line connectivity, and power-capacity constraints.
  - High-yield search terms: `Kenya Power`, `KPLC`, `MVA`, `MW`, `substation`, `dedicated feeder`, `33kV`, `66kV`, `132kV`, `power supply agreement`, `Tatu City substation`, `Olkaria`, `Mombasa Road`, `Sameer`, `Cabanas`, `Karen`, `Ruiru`, `Limuru`.
- **KETRACO**: https://www.ketraco.co.ke/
  - Use for transmission substations, high-voltage grid projects, fibre/transmission corridors, and state/captive data-centre tenders. KETRACO had a public EOI for a commercial Tier IV data-centre solution; treat such tenders as **A** for the tender and **B** for facility inference unless a site/project is named.
- **EPRA statistics**: https://www.epra.go.ke/statistics-0
  - Use for national electricity generation, peak demand, renewable share, tariffs, and energy-sector context. Do not use national statistics as facility evidence.
- **KenGen Green Energy Park / Olkaria**: https://greenenergypark.kengen.co.ke/
  - Use for Olkaria/Nakuru geothermal-powered projects, including EcoCloud/Project Eagle and Microsoft/G42 leads. Join to NEMA SEA/EIA and Kenya Power/KETRACO/KenGen grid evidence before grading construction status as A.

Power query templates:
```text
site:kplc.co.ke "data centre"
site:kplc.co.ke "data center"
site:kplc.co.ke "{operator}" "MVA"
site:kplc.co.ke "{project}" "substation"
site:ketraco.co.ke "data centre"
site:ketraco.co.ke "data center" "Tier IV"
site:ketraco.co.ke "{county}" "132/33"
site:epra.go.ke "data centre"
"{operator}" "Kenya Power" "data centre"
"{project}" "power supply agreement"
"{project}" "dedicated substation"
"Tatu City" "135MVA" "data centre"
"Olkaria" "data center" "geothermal" "KenGen"
```

What to extract: connection size MVA/MW, voltage level, customer/operator, substation/feeders, energisation date, power-supply agreement, standby generation, on-site solar/geothermal claims, tariff/open-access details, and whether capacity is IT load or utility load.

---

## 3. Official cloud-region and edge signals

| Provider | Official source | Kenya signal | How to use |
|---|---|---|---|
| Microsoft Azure / G42 | Microsoft announcement: https://news.microsoft.com/source/2024/05/22/microsoft-and-g42-announce-1-billion-comprehensive-digital-ecosystem-initiative-for-kenya/ ; Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list | Microsoft/G42 announced a green Olkaria data-centre campus to run Azure in a new East Africa Cloud Region, targeted within 24 months of definitive agreements. Azure public-region list checked here did not list Kenya. | Seed **Nakuru/Olkaria/Naivasha** and CA/KenGen/NEMA searches. Grade A for Microsoft announcement; verify current project status via official agreements and energy/permitting. |
| Oracle OCI | Oracle blog: https://blogs.oracle.com/cloud-infrastructure/oci-announces-plans-to-expand-in-africa ; OCI region list: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | Oracle announced intent to open a new public cloud region in Kenya. OCI region list checked here listed Johannesburg and Casablanca in Africa but not Kenya as operational. | Seed **Nairobi/iXAfrica** and government cloud searches; do not mark operational region unless current OCI regions page lists it or Oracle publishes launch. |
| AWS | AWS regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Kenya region found in official region list checked here. Africa region signal is South Africa, with edge/local infrastructure possible. | Use only as tenant/partner/edge lead; do not infer a Kenya AWS facility. |
| Google Cloud | Google locations: https://cloud.google.com/about/locations | No Kenya region found in official locations page checked here. | Use only as tenant/edge/partner lead unless official Google source announces Kenya. |
| Microsoft edge | Azure Front Door POP locations: https://learn.microsoft.com/en-us/azure/frontdoor/edge-locations-by-region and abbreviation page https://learn.microsoft.com/en-us/azure/frontdoor/edge-locations-by-abbreviation | Microsoft documentation lists Nairobi/NBO as an edge POP. | Edge POP is not a datacenter campus; use to seed colocation/interconnection searches only. |

Cloud query templates:
```text
"East Africa Cloud Region" Kenya
"Olkaria" "Azure" "data center"
"G42" "EcoCloud" "Olkaria" "data center"
site:oracle.com Kenya "public cloud region"
site:oracle.com "Nairobi" "cloud region"
site:aws.amazon.com Kenya "Local Zone"
site:cloud.google.com Kenya "region"
site:learn.microsoft.com "NBO" "Nairobi" "Azure Front Door"
```

---

## 4. Official/operator facility seed list

Operator pages are primary statements for marketed facility existence, city, and often capacity. They are **not** substitutes for county/NEMA/NCA/power evidence when classifying a project as permitted or under construction.

| Operator / project | Official source | Kenya footprint signal | Follow-up joins |
|---|---|---|---|
| iXAfrica NBOX1 / NBOX2 | https://ixafrica.co.ke/ and NBOX1 page https://ixafrica.co.ke/ixafrica-putting-kenya-on-the-map-as-a-data-centre-leader/ | NBOX1 at Cabanas/Mombasa Road, Nairobi; official 22.5 MW design capacity. Site/news also references Oracle/sovereign-cloud collaborations and planned NBOX2/Tilisi expansion. | Search Nairobi eDevelopment, NEMA uploads, NCA, CA register, Kenya Power. For NBOX2, search Tilisi/Kiambu county and SEZ/planning material. |
| Africa Data Centres / Cassava NBO1 | https://www.africadatacentres.com/nairobi/ | NBO1 at Sameer Business Park, Mombasa Road, Nairobi; official page gives 7.5 MW available site capacity and 4 Uptime Tier III-certified data halls. | Search Sameer/Nairobi permits, NEMA, CA register, Kenya Power; search official ADC/Cassava expansion announcements for second/third Nairobi facilities. |
| Digital Realty / iColo | Digital Realty Nairobi: https://www.digitalrealty.com/data-centers/emea/nairobi ; iColo: https://www.icolo.io/ | Digital Realty lists Nairobi NBO1 and NBO2 on Langata South Road/LRC Road. iColo homepage lists Mombasa One/Miritini 0.9 MW and Mombasa Two/Nyali 1.75 MW. | Search Nairobi/Karen/Langata and Mombasa/Nyali/Miritini county/NEMA/NCA permits, Kenya Power, CA register. |
| Safaricom | Wholesale data-centre page: https://www.safaricom.co.ke/wholesale/wholesale_product_categories/data_centre/ | Official page states data centres are located in Thika, Nairobi, and Kisumu. Other public evidence identifies Limuru/Redhill expansion. | Search Safaricom annual reports, CA register, Uptime Institute, Kiambu/Kisumu/Nairobi permits, NCA, Kenya Power. |
| Airtel Africa / Nxtra | https://www.airtel.africa/data-centers | Airtel says Nxtra began construction of a new data centre in Kenya on 2025-09-09. Tatu City and government/press releases identify Tatu City SEZ/Kiambu and 44 MW. | Search Kiambu/Tatu City approvals, SEZ Authority, NEMA, NCA, CA register, Kenya Power/Tatu City substation. |
| Tatu City SEZ | https://www.tatucity.com/news/tatu-city-cements-status-as-east-africas-data-centre-hub/ | Private SEZ/developer source for Tatu City as a data-centre hub and Nxtra location; use as B/A- depending on whether it links official SEZ/government evidence. | Join to Kiambu county, SEZ Authority, NEMA, NCA, Kenya Power. |
| Konza National Data Centre / Konza Cloud | https://konza.go.ke/konza-cloud/ | Government/KoTDA official source for national cloud/data-centre services at Konza. | Resolve county attribution by parcel/planning document; search Konza public notices, PPP Directorate, ICTA, NCA, Uptime Institute. |
| PAIX Nairobi | https://www.paix.io/ and Africa50 project page https://www.africa50.com/our-funds/projects/paix-data-centers/ | Official PAIX/Africa50 sources confirm PAIX has Kenya operating assets; trade press places Nairobi-1 at Britam Tower/Upper Hill. | Search Nairobi permits, Britam Tower, CA register, NEMA, Kenya Power. |
| Wananchi / Zuku | https://zuku.co.ke/ and Wananchi Group pages | Wananchi/Zuku are telecom/fibre operators and possible colocation/POP leads. Public official data-centre evidence is thinner than Safaricom/iColo/ADC; use as operator-search term, not a confirmed facility list. | Search CA register, Zuku/Wananchi careers/procurement, Nairobi/Mombasa POPs, `data centre`, `core network`, `server room`. |
| EcoCloud / Project Eagle / KenGen Green Energy Park | https://greenenergypark.kengen.co.ke/ plus Microsoft/G42 official announcement | Olkaria/Nakuru geothermal-powered data-centre lead; trade press reports Project Eagle and Microsoft/G42 capacity figures. | Require KenGen/NEMA/KETRACO/Kenya Power/project-company evidence for status and capacity. |

Operator query templates:
```text
"{operator}" "Kenya" "data centre" "MW"
"{operator legal name}" "Kenya" "data center" "NEMA"
"{operator}" "Kenya Power" "MVA"
"{operator}" "Communications Authority" licence
"{facility}" "Uptime Institute" Kenya
"{facility}" "NCA" Kenya
"{facility}" "LR No" Kenya
```

---

## 5. County enumeration strategy for 47 counties

### 5.1 Standard county workflow

For each county:
1. Run official-domain searches first: county site, KenInvest eProcedures, NEMA uploads, NCA, CA register, KPLC/KETRACO, ICTA/ICT ministry, SEZ Authority if relevant.
2. Search English variants: `data centre`, `data center`, `datacentre`, `server farm`, `server room`, `cloud`, `colocation`, `co-location`, `Tier III`, `hyperscale`, `AI data centre`, `MVA`, `substation`.
3. Search named operators and anchors: `iXAfrica`, `Africa Data Centres`, `Digital Realty`, `iColo`, `Safaricom`, `Airtel`, `Nxtra`, `PAIX`, `Wananchi`, `Liquid`, `Oracle`, `Microsoft`, `G42`, `EcoCloud`, `Konza`, `KenGen`.
4. For each lead, try to obtain at least one primary source: official operator page, county/NEMA/NCA permit, CA licence, power-grid evidence, or government announcement.
5. Use trade press/directories only to fill capacity/status gaps or to identify alternate names. Mark capacity as null when not directly supported.

### 5.2 High-yield county clusters

- **Nairobi City**: highest density. Search Nairobi eDevelopment, NEMA, CA register, Kenya Power, and operator pages for iXAfrica/Cabanas/Mombasa Road, Africa Data Centres/Sameer, Digital Realty/iColo Langata/Karen, PAIX/Britam/Upper Hill, Safaricom Nairobi, Wananchi/Zuku, Liquid, cloud/edge POPs.
- **Kiambu**: Tatu City/Ruiru, Limuru/Redhill, Thika, Tilisi. Search Nxtra/Airtel, Tatu City, Safaricom, iXAfrica NBOX2/Tilisi, Kiambu construction permits, NEMA, NCA, Kenya Power substations.
- **Mombasa**: iColo MBA1 Miritini and MBA2 Nyali, subsea cable landing ecosystem, port/industrial power. Search Mombasa county permits, NEMA, Kenya Power, CA register, `Miritini`, `Nyali`, `undersea cable`, `carrier neutral`.
- **Machakos / Makueni / Kajiado**: Konza boundary cluster. Do not duplicate blindly; note parcel uncertainty. Search KoTDA, Konza Cloud, ICTA, PPP Directorate, NEMA, NCA, and county planning/public notices.
- **Nakuru**: Olkaria/Naivasha geothermal cluster. Search KenGen Green Energy Park, EcoCloud, G42, Microsoft, NEMA SEA/EIA, KETRACO/Kenya Power, EPRA. Watch project status carefully because power/contract issues may delay or scale projects.
- **Kisumu**: Safaricom official page says Kisumu data centre; search county permits, NEMA, Uptime/directories, Kenya Power, telecom operators.
- **Uasin Gishu / Eldoret, Mombasa corridor, Lamu, Busia, Kilifi, SEZ counties**: search SEZ/industrial park and fibre/power terms, but expect fewer confirmed commercial facilities.
- **Low-yield counties**: for rural/no-lead counties, a defensible negative search should include official county site + NEMA + named-operator sweep + `data centre/data center/datacentre/server farm/cloud` terms. Avoid recording data-collection offices, cyber cafes, computer labs, or county GIS offices as datacenters unless the source describes actual hosting/colo/cloud/server infrastructure.

---

## 6. Practical grading and de-duplication rules

- **A facility exists (A)** when an official operator/government page names the data centre and location, or when NEMA/county/NCA/CA/power documents identify it.
- **A project is under construction (A/B)** only when official operator/government/NCA/NEMA evidence says construction started. Trade press alone is **B** unless it reproduces an official announcement.
- **Capacity (MW)** should distinguish IT load from total utility load. If a source says MVA, record separately in notes rather than converting unless the source gives conversion.
- **Cloud region != facility**. Record Microsoft/G42 and Oracle as cloud/project seeds unless official operational-region pages confirm launch and local facility evidence exists.
- **Konza duplication**: Konza spans/affects multiple counties in public descriptions. Prefer one canonical record with parcel-confirmed county; add boundary notes only where the source explicitly justifies multi-county ambiguity.
- **Telecom/county ICT rooms**: Safaricom/telecom data centres may be valid if marketed as wholesale/colo/cloud/Tier facilities. County "data centers" for GIS/statistics or call centres are not commercial datacenters unless they host server infrastructure; grade cautiously.

---

## 7. Source priority checklist

1. County development/building permit or public notice.
2. NEMA EIA/ESIA/SEA report or licence.
3. NCA project registration / construction compliance.
4. Kenya Power/KETRACO/KenGen/EPRA official grid or energy evidence.
5. CA Kenya market-structure/licence-register evidence for operator/service authority.
6. Official cloud provider or operator page.
7. Uptime Institute certification and official SEZ/developer releases.
8. Trade press/directories for discovery and secondary corroboration.

