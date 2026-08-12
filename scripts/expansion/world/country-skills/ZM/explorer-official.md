# ZM Explorer Official - Zambia Datacenter Enumeration via Regulators, Power, Investment, Government Cloud, and Councils

Date: 2026-08-12. Country: **ZM Zambia**. Division model: **10 provinces**: Central; Copperbelt; Eastern; Luapula; Lusaka; Muchinga; Northern; North-Western; Southern; Western. Angle: **official/regulatory-first datacenter discovery**. Use industry and press sources only as leads unless they are operator-owned pages.

Reliability grades are field-level, not record-level:
- **A** = primary source for the specific field: regulator/government/operator page, ZICTA licence or consultation, ZEMA EIA/EPB/EIS page, ERB licence/statistics page, ZESCO/CEC/NWEC power document, ZDA SEZ/MFEZ page or certificate, Data Protection Commission portal/legal text, Smart Zambia/INFRATEL/ZNDC page, council planning/building record, official hyperscale region page.
- **B** = strong named secondary source: Parliament record, ZANIS, Lusaka Times, Times of Zambia, Zambia Daily Mail, News Diggers, DCD, ITWeb Africa, Developing Telecoms, Connecting Africa, Capacity, vendor case study, PeeringDB/IXP page for network presence.
- **C** = lead only: directory entry, social post, generic market report, old MoU with no site/power/permit evidence, unsupported capacity/address claim.

Do not count a datacenter from a legal demand driver, licence class, fibre route, IXP membership, cloud resale, or MoU alone. Count only when a named operator or public body is tied to a physical facility or data-centre service; keep status values separate: `operational`, `under construction`, `approved`, `planned`, `MoU/intent`, `lead only`.

---

## 0. Official Zambia Facts That Shape Enumeration

- Zambia has **no public national datacenter register** and no single national planning-permit database. Enumerate by joining official surfaces: ZICTA licensing, ZEMA EIA/EPB/EIS documents, ERB/ZESCO/CEC/NWEC power evidence, ZDA SEZ/MFEZ instruments, Data Protection Commission registration/localisation requirements, Smart Zambia/INFRATEL/ZNDC government cloud records, and city/municipal/town council planning/building records.
- Zambia is divided into **ten provinces**. ZamStats' *Zambia in Figures 2018* lists Central, Copperbelt, Eastern, Luapula, Lusaka, Muchinga, Northern, North Western, Southern, and Western. Use exactly these ten divisions, normalising `North Western` to `North-Western` in records.
- Confirmed official/operator-grade datacenter seeds are concentrated in **Lusaka**: **INFRATEL / Zambia National Data Centre** (three national Tier III data centres; government cloud/colocation), **Paratus Zambia** (Tier III-by-design commercial data center in Lusaka), and **Liquid Intelligent Technologies Zambia** (Azure Stack/local cloud launch; MoU to launch a new data centre). Telco cores at Zamtel, MTN Zambia, and Airtel Zambia are infrastructure leads, not open-colo facilities unless a source says so.
- Power is a gating filter. ERB says energy enterprises require licences under the Energy Regulation Act No. 12 of 2019. ZESCO is the national utility. **CEC** is the Copperbelt mining-power authority. **NWEC** is a Solwezi/Kalumbila/North-Western distribution lead. During load-shedding periods, backup generation, fuel storage, UPS, solar/captive generation, and PSAs are decisive evidence fields.
- Local planning is decentralised. Use the Urban and Regional Planning Act context and council planning/building departments, especially Lusaka City Council's City Planning Department. The Ministry of Local Government and Rural Development lists local-authority websites; the eRegistry lists permit procedures such as building-plan submission and MFEZ procedures.
- Data Protection Act No. 3 of 2021 and the Data Protection (General) Regulations, 2024 are A-grade demand/legal context. The DPC registration portal asks whether data is stored outside Zambia and flags separate authorisation for storage/transfer outside Zambia. This is **not facility proof**.
- Official public cloud-region status, checked against provider region pages on 2026-08-12: no AWS, Microsoft Azure public cloud, Google Cloud, or Oracle OCI public region is listed in Zambia. Treat Azure Stack/partner/local cloud as local/private/hybrid cloud, not an Azure public region.

Primary URLs verified for use:
- ZICTA: https://www.zicta.zm/ ; licensing: https://www.zicta.zm/services/licensing
- ZEMA: https://www.zema.org.zm/ ; services: https://www.zema.org.zm/our-services/ ; EIA docs: https://www.zema.org.zm/docs-category/environmental-impact-statements/ ; EIA calls: https://www.zema.org.zm/docs-category/eia-call-for-comments/
- ERB: https://www.erb.org.zm/ ; licensing: https://www.erb.org.zm/licensing/ ; statistics: https://www.erb.org.zm/statistics/ ; licensing hub: https://portal.erb.org.zm/information_hub
- ZESCO: https://www.zesco.co.zm/
- CEC: https://www.cec.com.zm/ ; local power: https://www.cec.com.zm/local-power-supply-business/
- NWEC: https://www.northwesternenergycorp.com/
- ZDA: https://zda.org.zm/ ; SEZ page: https://zda.org.zm/special-economic-zones/
- eRegistry/BRRA: https://www.businesslicenses.gov.zm/ ; MFEZ procedure: https://www.businesslicenses.gov.zm/business-procedures/details/multi-facility-economic-zone ; building plans: https://www.businesslicenses.gov.zm/license/id/473
- Data Protection Commission: https://www.dataprotection.gov.zm/ ; registration portal: https://registration.dataprotection.gov.zm/
- Smart Zambia Institute: https://www.szi.gov.zm/
- INFRATEL: https://infratel.co.zm/ ; data centre services: https://infratel.co.zm/data-center-services/ ; company profile: https://infratel.co.zm/company-profile/ ; FAQs: https://infratel.co.zm/faqs/
- Lusaka City Council: https://www.lcc.gov.zm/ ; city planning: https://www.lcc.gov.zm/city-planning-department/
- Local-authority website index: https://www.mlgrd.gov.zm/?page_id=4743
- Lusaka IXP: https://lusakaixp.co.zm/
- Cloud region pages: AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Google https://cloud.google.com/about/locations ; Oracle https://www.oracle.com/cloud/public-cloud-regions/

---

## 1. ZICTA - ICT Licensing and Gateway Evidence

ZICTA regulates Zambia's ICT sector. Its licensing page is an A-grade surface for licence procedures and regulated operator existence, but not for floor area, MW, racks, or operational datacenter status unless the document explicitly names a facility.

Use ZICTA to verify:
- Operator legal names and licence classes.
- Gateway/international-data licence claims, especially Paratus and other carriers.
- Consultations, spectrum notices, market reports, and enforcement notices that mention data centres, cloud, hosting, network infrastructure, or international gateways.

Query templates:
```text
site:zicta.zm "data centre" OR "data center"
site:zicta.zm "gateway licence" OR "data gateway"
site:zicta.zm "class licensing" OR "licensing framework"
site:zicta.zm "Paratus" OR "Liquid" OR "INFRATEL" OR "Zamtel" OR "MTN" OR "Airtel"
"ZICTA" "data gateway licence" Zambia
"ZICTA" "network infrastructure" "data centre" Zambia
"{operator}" "ZICTA" "licence" Zambia
```

Extraction fields: licence holder, licence class/type, issue/renewal date, licence number if public, authorised services, gateway rights, province/town if stated, source URL, grade.

---

## 2. ZEMA - Environmental and Generator/Fuel Trail

ZEMA is useful because datacenters may appear as ICT buildings, commercial buildings, substations, backup-generator plants, petroleum/fuel-storage facilities, e-waste facilities, or SEZ tenant developments. ZEMA's document archive and EIA call-for-comments pages are official A-grade surfaces when the ZEMA page or government-hosted document is opened.

Query templates:
```text
site:zema.org.zm "data centre" OR "data center"
site:zema.org.zm "server" OR "ICT" OR "telecommunications"
site:zema.org.zm "generator" "Lusaka" "data"
site:zema.org.zm "fuel storage" "ICT" OR "telecom"
site:zema.org.zm "Environmental Project Brief" "Lusaka" "ICT"
site:zema.org.zm "Environmental Impact Statement" "substation" "Lusaka"
"ZEMA" "Project Brief" "{operator}" Zambia
"{project}" "EIA" "backup generators" Zambia
```

Extract: ZEMA title/reference, proponent, plot/stand/farm number, ward/district/province, project category, consultant, public-comment dates, decision/approval conditions, generator rating, fuel capacity, water/cooling/waste impacts, and appeal status. Do not infer a datacenter from a telecom tower or e-waste project without a facility tie.

---

## 3. Power Trail - ERB, ZESCO, CEC, NWEC

Use power evidence to separate a credible datacenter from a cloud/hosting marketing claim.

Official source roles:
- **ERB**: licence requirement and licensee information for generation, transmission, distribution, supply, petroleum storage, and large backup/captive-power arrangements.
- **ZESCO**: national grid connections, substations, feeders, tenders, energisation notices, PSAs.
- **CEC**: Copperbelt power supply and wheeling; strong for Ndola/Kitwe/Chambishi data-centre or mine-ICT leads.
- **NWEC**: North-Western/Solwezi/Kalumbila distribution lead.

Query templates:
```text
site:erb.org.zm "{operator}" "licence"
site:erb.org.zm "data centre" OR "data center" OR "ICT"
site:zesco.co.zm "data centre" OR "data center" OR "server"
site:zesco.co.zm "{operator}" "substation" OR "MVA" OR "33kV" OR "66kV" OR "132kV"
site:cec.com.zm "data centre" OR "ICT" OR "cloud"
site:cec.com.zm "Ndola" OR "Kitwe" "substation" "MVA"
site:northwesternenergycorp.com "Solwezi" OR "Kalumbila" OR "data"
"{project}" "power supply agreement" Zambia
"{project}" "captive power" OR "PPA" Zambia
```

Preserve units exactly. Record whether a number is IT MW, facility MW, connected load, MVA, generator kVA, or solar/captive MW. Never convert MVA to IT load unless the source does.

---

## 4. ZDA, SEZ, MFEZ, and Investment Records

ZDA's SEZ page is official A-grade for zone existence and broad sector suitability. It currently describes functional SEZ/MFEZ/IP infrastructure and names relevant zones including **Jiangxi MFEZ in Chibombo, Central Province**, **Kalumbila MFEZ in North-Western**, **Lusaka East MFEZ**, and other SEZs. Use ZDA/ZCCZ/LS-MFEZ pages to locate potential ICT tenants, but grade tenant claims separately.

High-yield zones:
- Lusaka East MFEZ / ZCCZ and Lusaka South MFEZ: Lusaka ICT/DC demand, airport/fibre/power adjacency.
- Chambishi MFEZ / ZCCZ and Copperbelt Province SEZ / industrial parks: mining/industrial power demand.
- Jiangxi MFEZ: Chibombo/Central industrial lead; likely low DC yield but official zone coverage.
- Kalumbila MFEZ: North-Western mining-supply-chain lead.
- Kafue/other developing zones: monitor only if ICT/cloud/data-centre tenants appear.

Query templates:
```text
site:zda.org.zm "data centre" OR "data center" OR "ICT" OR "cloud"
site:zda.org.zm "Lusaka East" "ICT" OR "technology"
site:zda.org.zm "Lusaka South" "ICT" OR "data"
site:zda.org.zm "Chambishi" "ICT" OR "data"
site:zda.org.zm "Jiangxi" "ICT" OR "data"
site:zda.org.zm "Kalumbila" "ICT" OR "data centre"
site:lsmfez.co.zm "ICT" OR "data centre" OR "cloud"
"{operator}" "ZDA" "investment" Zambia
"{operator}" "multi-facility economic zone" Zambia
```

Extract: investor/SPV, certificate/licence number, zone, plot, district/province, sector, announced capex, power/water/fibre claims, and source type.

---

## 5. Data Protection Commission - Localisation Demand

The DPC portal and DPC pages are A-grade for registration and localisation workflow. They do not prove where a facility is.

Use DPC evidence for:
- Demand screening: sectors likely to require domestic hosting (financial, telecom, health, government, education, mobile money, cloud service providers).
- Identifying registered controllers/processors if a public register/export is available.
- Cross-border-transfer or outside-Zambia storage authorisation signals.

Query templates:
```text
site:dataprotection.gov.zm "data centre" OR "data center" OR "hosting"
site:dataprotection.gov.zm "store personal data outside Zambia"
site:dataprotection.gov.zm "data controller" "processor" "registration"
site:registration.dataprotection.gov.zm "Data Protection Act" "Act No. 3 of 2021"
"Zambia" "data localisation" "data centre"
"{operator}" "data processor" "Zambia"
```

---

## 6. Smart Zambia, INFRATEL, and ZNDC

Treat **INFRATEL / Zambia National Data Centre** as a first-class official/operator seed. INFRATEL's official pages state it operates three national Tier III data centres and provides data-centre, cloud, colocation, backup, and digital services. Parliament records state ZNDC was formed to oversee and operate three data centres delivered under Smart Zambia Phase I, and that a Tier 3 Zambia National Data Centre had been established and commissioned with backup/disaster-recovery sites.

Key source uses:
- INFRATEL data centre services, company profile, FAQs, white papers: A for services and operator claims.
- Smart Zambia and Parliament records: A/B+ for government mandate, phase history, and e-government use.
- Office of the Vice President and Smart Zambia pages for the **May 2026 Zambia-Huawei National AI Data Centre MoU**: A for MoU/intent only. Do not mark operational until site, permit, power, procurement, or operator commissioning evidence appears.

Query templates:
```text
site:infratel.co.zm "data centre" OR "data center" OR "Tier III"
site:infratel.co.zm "three" "data centres"
site:infratel.co.zm "Azure Stack" OR "local cloud" OR "colocation"
site:szi.gov.zm "data centre" OR "National Data Centre" OR "ZNDC"
site:parliament.gov.zm "Zambia National Data Centre"
site:ovp.gov.zm "National AI Data Centre" Huawei
"SMART Zambia" "Huawei" "AI data centre"
"Zambia National Data Centre" "disaster recovery" "Kitwe" OR "Roma"
```

Extract: facility/operator name, number of sites, site names or addresses if public, tier wording (`Tier III`, `Tier III by design`, `Tier 3`), service types, public/private customer availability, disaster-recovery relation, Azure Stack/local cloud status, and commissioning dates.

---

## 7. Council Planning and Building Permits

The council trail is mandatory for new-build confirmation, but many Zambian councils publish little searchable permit data. Use the MLGRD local-authority index to find official council sites, then search council pages, minutes, procurement notices, planning departments, and eCouncil/ZamPortal services.

Known official council anchors:
- Lusaka: https://www.lcc.gov.zm/ ; planning: https://www.lcc.gov.zm/city-planning-department/
- Copperbelt: Ndola City Council and Kitwe City Council via MLGRD index; Kitwe: https://www.kitwecouncil.gov.zm/
- Central: Kabwe Municipal Council https://www.kabwecouncil.gov.zm/
- Eastern: Chipata City Council https://www.chipatacouncil.gov.zm/
- North-Western: Solwezi Municipal Council https://www.solwezicouncil.gov.zm/
- Muchinga: Chinsali Council https://www.chinsalicouncil.gov.zm/
- Western: Mongu Municipal Council https://www.mongucouncil.gov.zm/
- For Luapula, Northern, and Southern, use MLGRD index plus Mansa, Kasama, Choma, and Livingstone council channels if websites are unavailable or intermittently down.

Query templates:
```text
site:lcc.gov.zm "data centre" OR "data center" OR "INFRATEL" OR "Paratus" OR "Liquid"
site:{council-domain} "data centre" OR "data center" OR "server" OR "ICT"
site:{council-domain} "building permit" OR "planning permission" OR "development permission"
"{council}" "planning permission" "{operator}" Zambia
"{capital}" "stand" "data centre" Zambia
site:businesslicenses.gov.zm "building plans" "Lusaka"
```

Extract: application number, applicant, plot/stand/farm, ward, land-use category, approval/decision date, conditions, building-use wording, occupancy/completion certificate, and whether the record is a council page, council minute, eRegistry procedure, or social channel.

---

## 8. Official Cloud-Region Status

| Provider | Official source | Zambia status | Enumeration rule |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and AWS docs | No Zambia Region found; Africa Region is South Africa/Cape Town (`af-south-1`) | Treat reseller, partner, Direct Connect, or edge/cache claims as non-region evidence |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Zambia public Azure region found | Azure Stack in Zambia is local/hybrid cloud, not a public Azure region |
| Google Cloud | https://cloud.google.com/about/locations | No Zambia region found; Africa region is Johannesburg (`africa-south1`) | CDN/cache evidence is network/edge only |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No Zambia region found; Africa commercial region is Johannesburg | Recheck official page before accepting any OCI Zambia claim |
| Huawei Cloud | https://www.huaweicloud.com/intl/en-us/ | No official Zambia public cloud region found | Huawei/Smart Zambia records are government/AI/DC project evidence, not public-cloud region proof |

Annual verification query:
```text
site:aws.amazon.com Zambia "Region"
site:learn.microsoft.com/azure "Zambia" "region"
site:cloud.google.com/about/locations Zambia
site:oracle.com/cloud "Zambia" "region"
"Zambia" "cloud region" "official"
```

---

## 9. Per-Province Official Enumeration Strategy

Run every province, even if expected yield is low. The objective is complete coverage, not only Lusaka hits.

| Province | Capital | Official anchors | Strategy and honest expected yield |
|---|---|---|---|
| **Lusaka** | Lusaka | LCC; ZICTA; ZEMA HQ/docs; ERB/ZESCO; ZDA Lusaka East/South/Kafue zones; Smart Zambia; INFRATEL; Lusaka IXP | **Highest yield.** Confirm INFRATEL/ZNDC, Paratus, Liquid/Azure Stack, telco HQ cores, banks, government cloud. Search council permits, ZEMA generator/fuel/storage records, ZESCO connections, and ZICTA gateway/licence notices. |
| **Copperbelt** | Ndola | Ndola/Kitwe councils; CEC; Chambishi/ZCCZ; CPSEZ/industrial parks; ZICTA regional telecom leads | **Medium watch.** Look for DR sites, mine-adjacent ICT rooms, telco switch sites, INFRATEL backup/DR references, CEC power records. Do not count mine IT rooms unless named as hosting/DC facilities. |
| **Southern** | Choma | Choma and Livingstone councils; ZESCO; tourism/border agencies; Liquid/Zamtel fibre route leads | **Low watch.** Query Livingstone/Choma permits, ZEMA records for generators/fuel at ICT/telco facilities, and cross-border/tourism DR hosting. |
| **Central** | Kabwe | Kabwe council; ZESCO; Jiangxi MFEZ/Chibombo; possible parastatal rail/agriculture ICT | **Low watch.** Query Kabwe/Chibombo, Jiangxi MFEZ tenants, government websites/server rooms, and ZEMA ICT or e-waste docs. |
| **Eastern** | Chipata | Chipata council; ZESCO; ZEMA regional office references; Malawi-border trade agencies | **Low watch.** Query Chipata, ZANIS/provincial government ICT, mobile-money/bank infrastructure, and council permits. |
| **Luapula** | Mansa | Mansa council via MLGRD/off-grid directory; ZESCO; ZEMA regional-office mentions | **Very low watch.** Search Mansa/Luapula for ICT rooms, government e-services, tower power upgrades, and provincial tenders. |
| **Muchinga** | Chinsali | Chinsali council; ZESCO; Mpika/transport-corridor projects; ZEMA docs | **Very low watch.** Search Chinsali/Mpika for government ICT, backbone sites, and ZEMA records; expect connectivity more than DCs. |
| **Northern** | Kasama | Kasama council via MLGRD/off-grid directory; ZESCO; Mbala/Mpulungu logistics | **Very low watch.** Search Kasama/Mbala/Mpulungu for government ICT, port/logistics systems, and local server-room evidence. |
| **North-Western** | Solwezi | Solwezi council; NWEC; Kalumbila MFEZ; mines/FQM suppliers; ZESCO/ERB | **Medium-low watch.** Mining and Kalumbila power make this the strongest non-Lusaka/Copperbelt province. Query Solwezi/Kalumbila, NWEC, ZEMA, ERB, and mine DR/ICT procurement. |
| **Western** | Mongu | Mongu council; ZESCO; provincial administration/e-government; Barotseland/Lozi press | **Very low watch.** Query Mongu/Western for government ICT, council permits, and ZANIS leads. |

Province query block:
```text
"{province}" "data centre" OR "data center" Zambia
"{capital}" "data centre" OR "server room" OR "hosting" Zambia
site:{council-domain} "ICT" OR "server" OR "building permit"
site:zema.org.zm "{capital}" "ICT" OR "generator" OR "substation"
site:erb.org.zm "{capital}" "licence" OR "substation"
site:zanis.gov.zm "{province}" "ICT" OR "digital" OR "data"
"{province}" "MFEZ" OR "industrial park" "ICT" Zambia
"{capital}" "INFRATEL" OR "Zamtel" OR "MTN" OR "Airtel" OR "Liquid" OR "Paratus"
```

---

## 10. Extraction Checklist

For every candidate, record these fields and grades independently:
- Facility/operator: legal name, brand, SPV, government body.
- Status: MoU/intent, announced, approved, under construction, operational, closed/unknown.
- Location: province, district, city/town, plot/stand/address, coordinates, source precision.
- Official permits: ZICTA licence, ZEMA EPB/EIS/decision, ERB/power licence, ZESCO/CEC/NWEC connection, ZDA/SEZ certificate, council planning/building/occupancy record.
- Technical: tier wording exactly as published, IT load/facility load/MVA, racks/cabinets, halls, backup generators, UPS, fuel storage, cooling/water, certifications.
- Connectivity: carriers, IXP membership, gateway licence, fibre routes, meet-me-room, CDN/cache presence.
- Cloud/service: colocation, cloud, Azure Stack/local cloud, backup/DR, government-only/private-sector availability.
- Sources: URL, title, publisher, date accessed, publication date, grade, quoted field.

Red flags: `cloud region` without official hyperscale page; `Tier III` without `by design`/certification distinction; directory address without operator page; MoU counted as construction; social post treated as primary; power MVA converted to MW; province missing because no hits were found.
