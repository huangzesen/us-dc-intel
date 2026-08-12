# NG Explorer Official - Nigeria Datacenter Enumeration via NCC, Planning, Environment, Power, Cloud, and Operator Sources

Date: 2026-08-12. Country: **NG Nigeria**. Division model: **36 states + Abuja Federal Capital Territory**. Angle: **official/regulatory/primary-source methodology** for enumerating commercial, hyperscale, telecom, bank, government, and edge data-centre facilities.

Reliability grades:
- **A** = official/primary source: state/FCT planning or building-control record, Federal Ministry of Environment/EAD EIA disclosure, NERC captive-generation permit or electricity order, NCC licence/register entry, official cloud-provider page, official operator facility page, Uptime Institute certification record, official government data-centre/cloud page.
- **B** = strong secondary source: trade press, exchange/IXP/subsea operator page, state investment-promotion release, reputable local business press, vendor case study, financing/government MoU with named site.
- **C** = weak lead: generic market report, directory-only facility, social post, procurement rumour, unimplemented MoU, state ICT plan that says "data centre" without site/status.

---

## 0. Nigeria-specific structure facts

- Nigeria does **not** have one national public datacenter registry. Enumeration requires joining: **state/FCT development permits**, **Federal Ministry of Environment EIA disclosures**, **NCC communications licences**, **NERC captive-power permits and MYTO/customer feeder orders**, **cloud-provider region/edge pages**, **official operator pages**, and **Uptime certifications**.
- The legal planning unit is usually **state or FCT**, but practical siting is city/locality-first: `Lagos`, `Lekki`, `Victoria Island`, `Eko Atlantic`, `Ikoyi`, `Ikeja`, `Oregun`, `Yaba`, `Abuja`, `Kano`, `Port Harcourt`, `Eket`, `Sagamu`, `Atakobo`, `Calabar`, `Makurdi`, `Aba`, `Umuahia`, `Enugu`, `Ibadan`, `Kaduna`, and `Benin City`.
- Most large commercial/hyperscale evidence is in **Lagos State**. Secondary clusters are **FCT Abuja**, **Rivers/Port Harcourt**, **Kano**, **Ogun/Sagamu-Ijebu East**, **Akwa Ibom/Eket**, **Cross River/Calabar**, **Benue/Makurdi**, and selected state-government ICT/data centres.
- Search both spellings: `data centre`, `data center`, and `datacentre`. Also use `server room`, `server farm`, `colocation`, `co-location`, `carrier neutral`, `cloud`, `sovereign cloud`, `hyperscale`, `AI-ready`, `Tier III`, `Tier IV`, `Uptime`, `NERC/CPG`, `captive power`, `MVA`, `MW`, `substation`, `33kV`, `132kV`, `building permit`, `development permit`, `EIA`, `ESIA`, and `Environmental Impact Assessment`.
- Nigerian official records are mainly English. Local-language search is low yield for commercial facilities, but Yoruba/Hausa/Igbo terms can help with state-government ICT publicity; always verify with English official documents.

---

## 1. Official/regulatory portals and how to use them

### 1.1 Nigerian Communications Commission (NCC)

Primary sources:
- NCC list of licensees: https://ncc.gov.ng/industry/licensing/list-licensees
- NCC licensing documents and frameworks: https://ncc.gov.ng/industry/licensing/licensing-documents-frameworks
- NCC licensing application process: https://ncc.gov.ng/industry/licensing/licensing-application-process
- NCC press release on Microsoft/data-centre infrastructure: https://ncc.gov.ng/media-centre/press-releases/ncc-charges-microsoft-deepen-presence-nigeria-data-centre
- NCC press release on Galaxy Backbone: https://www.ncc.gov.ng/media-centre/press-releases/ncc-strengthens-ties-galaxy-backbone-digital-connectivity

Use NCC as **operator/service evidence**, not as a complete physical-facility register. The licensee page includes categories relevant to datacenter discovery: `Collocation/Infrastructure`, `Infrastructure Sharing and Co-location Services`, `International Data Access`, `International Cable Infrastructure & Landing Station`, `Internet Service Provider`, `Interconnect Exchange`, `National Long Distance`, `Unified Access Services`, and regional `Open Access Fibre Infrastructure Network (Infraco)` licences.

High-yield NCC names and categories:
- `MainOne`, `Equinix`, `MDXi`, `MainData`, `Teleafrica/Medallion`, `Digital Realty`, `Rack Centre`, `Open Access Data Centres`, `WIOCC`, `Africa Data Centres`, `MTN Nigeria`, `Airtel`, `Nxtra`, `Galaxy Backbone`, `21st Century Technologies`, `ipNX`, `Cyberspace`, `Inq.Digital`, `NTT`, `Broadbased`, `Zinox`, `Fleek`, `Raeanna`, `Oodua Infraco`.
- NCC's Infraco licence geography is useful for **state-level fibre and edge-data-centre leads**: Lagos, FCT, North West, North East, South East, South South, and South West groups.

NCC query templates:

```text
site:ncc.gov.ng "data centre" Nigeria
site:ncc.gov.ng "data center" Nigeria
site:ncc.gov.ng "Collocation/Infrastructure" "{operator}"
site:ncc.gov.ng "International Data Access" "{operator}"
site:ncc.gov.ng "International Cable Infrastructure" Lagos
site:ncc.gov.ng "Open Access Fibre Infrastructure Network" "{state}"
site:ncc.gov.ng "{operator}" "licence"
site:ncc.gov.ng "Galaxy Backbone" "data centre"
```

Extract: licensee legal name, licence category, address, issue/expiry dates, covered states, cable landing/interconnect role, and whether the licence proves only telecom service capability or a named physical datacenter.

### 1.2 State/FCT planning, building control, and development permits

There is no national planning-permit portal for datacenters. Datacenter construction should route through the state/FCT physical planning authority and building-control agency where the parcel sits.

High-yield official routes:
- **Lagos State Physical Planning Permit Authority (LASPPPA)**: Lagos State permit/news pages at https://lagosstate.gov.ng/ and agency references under https://lagosstate.gov.ng/government/mdas/l
- **Lagos State Building Control Agency (LASBCA)**: https://lasbca.lagosstate.gov.ng/about/
- **Lagos State Infrastructure Maintenance and Regulatory Agency (LASIMRA)** for telecom ducts/masts/fibre infrastructure: search Lagos State releases, e.g. LASIMRA enumeration notices.
- **FCT Department of Development Control / Abuja Metropolitan Management Council / FCTA**: use FCTA pages and web-indexed notices for Abuja data-centre, telecom, and government facilities.
- **State ministries of physical planning / urban development / lands** for Ogun, Rivers, Akwa Ibom, Cross River, Kano, Benue, Kaduna, Oyo, Edo, Enugu, and other state capitals.

Core permit queries:

```text
site:lagosstate.gov.ng "data centre" "planning permit"
site:lagosstate.gov.ng "data center" "building permit"
site:lasbca.lagosstate.gov.ng "data centre"
site:lagosstate.gov.ng "Kasi Cloud" "groundbreaking"
site:lagosstate.gov.ng "Eko Atlantic" "data centre"
site:fcta.gov.ng "data centre" Abuja
site:fcta.gov.ng "development control" "data centre"
site:{state-domain} "data centre" "building permit"
site:{state-domain} "data center" "development permit"
site:{state-domain} "physical planning" "data centre"
site:{state-domain} "urban development" "data centre"
```

For each permit/planning record, extract: state, LGA, town/locality, plot/parcel, street/industrial park/SEZ, applicant/proponent/SPV, development description, floor area, number of floors/data halls, electrical import MVA/MW, generators/fuel storage, water/cooling needs, approval/inspection/occupancy status, and permit dates.

### 1.3 Federal Ministry of Environment / EIA disclosures

Primary sources:
- Federal Ministry of Environment: https://environment.gov.ng/
- Environmental Assessment Department (EAD): https://ead.gov.ng/
- EAD public disclosures and uploaded EIA/ESIA PDFs: `https://ead.gov.ng/wp-content/uploads/`

Large datacenters may appear in EIA channels through land development, diesel/fuel storage, gas plants, substations, cooling/water abstraction, telecom/security infrastructure, industrial parks, or energy parks rather than a "data centre" category. EAD has public disclosures that mention regional data centres and central command facilities; EAD uploads also contain digital-infrastructure stakeholders such as TCN, Medallion Data Centre, MainOne, WIOCC, MTN, Airtel, GBB, Meta, and fibre/power actors.

EIA query templates:

```text
site:ead.gov.ng "data centre" Nigeria
site:ead.gov.ng "data center" Nigeria
site:ead.gov.ng "datacentre"
site:ead.gov.ng/wp-content/uploads "data centre"
site:ead.gov.ng/wp-content/uploads "data center"
site:ead.gov.ng/wp-content/uploads "{operator}" "Environmental Impact Assessment"
site:ead.gov.ng/wp-content/uploads "{project}" "EIA"
site:environment.gov.ng "data centre"
"{operator}" "{state}" "EIA" "data centre"
"{project}" "Environmental Impact Assessment" Nigeria "data centre"
```

Extract: EIA registration/reference, proponent, location coordinates/parcel, LGA/state, project components, diesel/gas/storage details, power plant/substation link, public-disclosure date, approval/certification status, and whether the EIA covers a datacenter itself or enabling infrastructure.

### 1.4 NERC, power permits, MYTO orders, and grid evidence

Primary sources:
- Nigerian Electricity Regulatory Commission (NERC): https://nerc.gov.ng/
- NERC captive-generation permit CSV: https://nerc.gov.ng/wp-content/uploads/2023/12/Captive-Power-Generation-Permit-2.csv
- NERC annual reports, MYTO tariff/order PDFs, and distribution-company orders: search https://nerc.gov.ng/
- Transmission Company of Nigeria (TCN): https://tcn.org.ng/ and related federal power/ministry pages.

NERC captive-generation records are high value because Nigerian datacenters often use dedicated/captive power. The public CSV has named examples including:
- `Rack Centre Limited`, `NERC/CPG/165`, `10.00 MW`, `18 Jagal Close`, `Oregun`, `Lagos`.
- `Open Access Data Centre Limited`, `NERC/CPG/177`, `3.20 MW`, `Plot 99/100 Silverbird Road`, `Ikate Elegushi`, `Lagos`, issued `04 December 2023`.
- Multiple `MTN Nigeria Communications Limited` switch/data-centre related permits, including Ojota, Ibadan, Enugu, Abuja, Apapa, Kano, Kaduna, Uselu and other switch sites.
- NERC annual report appendix also repeats `Open Access data centre Limited, Lagos State, 3.20 MW`.

NERC/power query templates:

```text
site:nerc.gov.ng "data centre"
site:nerc.gov.ng "data center"
site:nerc.gov.ng "Open Access data centre"
site:nerc.gov.ng "Rack Centre"
site:nerc.gov.ng "MTN Nigeria" "Switch"
site:nerc.gov.ng "{operator}" "NERC/CPG"
site:nerc.gov.ng "{operator}" "MVA"
site:nerc.gov.ng "{facility}" "33kV"
site:nerc.gov.ng "{facility}" "MYTO"
"{operator}" "captive power" "data centre" Nigeria
"{project}" "substation" "data centre" Nigeria
"{project}" "gas power plant" "data centre" Nigeria
```

Use NERC as **A for power permit/customer evidence** and **B/A- for facility inference** unless the permit explicitly names a datacenter facility. Capture whether MW is generation capacity, site load, utility committed power, or IT load.

### 1.5 Federal digital-government and IT regulatory sources

Primary sources:
- National Information Technology Development Agency (NITDA): https://nitda.gov.ng/
- Federal Ministry of Communications, Innovation and Digital Economy: https://fmcide.gov.ng/ or successor official ministry domains; older policy PDFs also appear under NITDA.
- Galaxy Backbone: https://galaxybackbone.com.ng/
- National Data Strategy PDF: https://nitda.gov.ng/wp-content/uploads/2022/11/Final-Draft-National-Data-Strategy.pdf
- NITDA IT service-provider lists, e.g. https://nitda.gov.ng/wp-content/uploads/2024/05/LIST-OF-LICENSED-IT-SERVICE-PROVIDER-COMPANIES-1.pdf

Use these for government cloud/data-centre policy, government shared-services facilities, state-government data-centre procurements, and IT service-provider verification. NITDA documents mention cloud-first/data-infrastructure objectives and agencies such as NCC, Galaxy Backbone, and private organisations. Galaxy Backbone's own FAQ states it operates a Tier III Data Center in Abuja and a Tier IV Data Center in Kano: https://galaxybackbone.com.ng/ufaqs/does-galaxy-backbone-operate-a-datacentre/

Government-cloud queries:

```text
site:nitda.gov.ng "data centre" Nigeria
site:nitda.gov.ng "cloud-first" "data infrastructure"
site:nitda.gov.ng "Galaxy Backbone" "data centre"
site:galaxybackbone.com.ng "data centre"
site:galaxybackbone.com.ng "Abuja" "Kano" "Tier"
site:{state-domain} "state data centre"
site:{state-domain} "data center" "ICT"
site:{state-domain} "e-government" "data centre"
```

### 1.6 Official cloud-region and edge signals

Cloud pages are **A for cloud-region/local-zone existence** but are not exact facility addresses.

| Provider | Official source | Nigeria signal | Enumeration use |
|---|---|---|---|
| AWS | AWS Local Zones docs: https://docs.aws.amazon.com/local-zones/latest/ug/available-local-zones.html ; AWS regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | AWS docs list `Nigeria (Lagos)` Local Zone `af-south-1-los-1a`, parent region `af-south-1`. No Nigeria AWS Region found on official regions page. | Seed Lagos operator/colo/interconnection searches. Treat as Local Zone/edge infrastructure, not a full AWS Region. |
| Microsoft Azure | Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list | Official list checked did not show a Nigeria region; Africa entries are South Africa North/West. NCC has urged Microsoft to deepen Nigerian data-centre infrastructure. | Use Microsoft/NCC as policy/demand lead only unless a Microsoft page announces Nigeria region/facility. |
| Google Cloud | Google Cloud locations: https://cloud.google.com/about/locations ; Compute regions/zones: https://docs.cloud.google.com/compute/docs/regions-zones | Official locations checked did not show a Nigeria region; Google Equiano subsea cable and edge/CDN presence may seed Lagos/OADC/MainOne searches. | Edge/subsea/partner lead only; do not infer a GCP Nigerian region. |
| Oracle OCI | Oracle Africa public cloud regions: https://www.oracle.com/africa/cloud/public-cloud-regions/ ; OCI regions docs: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | Official pages checked did not show a Nigeria OCI public region. | Use as customer/partner lead only. |

Cloud queries:

```text
"AWS Local Zone" Lagos Nigeria "af-south-1-los-1a"
site:docs.aws.amazon.com "Nigeria (Lagos)" "Local Zone"
site:learn.microsoft.com Azure Nigeria "region"
site:cloud.google.com Nigeria "region"
site:oracle.com Nigeria "cloud region"
"Nigeria" "cloud region" "data centre" "{provider}"
```

### 1.7 Uptime Institute certification records

Primary source:
- Uptime Institute country awards for Nigeria: https://uptimeinstitute.com/uptime-institute-awards/country/id/NG

Use Uptime to verify facility identity, city/state, design/constructed/operational certification, and operator names. High-yield records include Galaxy Backbone Abuja/Kano, GTBank Lagos, Lagos State Data Centre, MainOne Lekki/LG02, MTN Ojota, and other Nigerian facilities as listed by Uptime.

Query templates:

```text
site:uptimeinstitute.com/uptime-institute-awards/country/id/NG "{operator}"
site:uptimeinstitute.com "Nigeria" "Tier III" "Data Center"
site:uptimeinstitute.com "Kano" "Galaxy Backbone"
site:uptimeinstitute.com "Lagos State Data Centre"
site:uptimeinstitute.com "Ojota Data Center"
```

---

## 2. Official/operator facility seed list

Operator pages are **A for current self-claimed locations and broad capacities**, but still join to state/FCT planning, EIA, NCC, NERC, and Uptime before assigning construction/operational status.

| Operator / project | Official source | Nigeria footprint signal | Follow-up joins |
|---|---|---|---|
| Equinix / MainOne / MDXi | MainOne: https://mainone.net/ ; Equinix Lagos page: https://www.equinix.com/data-centers/europe-colocation/nigeria-colocation/lagos-data-centers ; MainOne Lekki II release: https://mainone.net/mainone-expands-digital-footprint-with-the-launch-of-mdxi-lekki-ii-data-center-2/ | Lagos/Lekki LG1/LG2/LG3 signals; Equinix page says Lagos has three IBX data centers. Equinix PR1 Port Harcourt announcement is at https://www.equinix.com/newsroom/press-releases/2025/04/equinix-to-open-first-data-center-in-port-harcourt-and-bring-2africa-subsea-cable-to-nigeria | Search Lagos/Rivers permits, NCC MainOne/International Data Access/cable landing, NERC, Uptime, 2Africa/MainOne landing-station sources. |
| Rack Centre | https://rack-centre.com/ and LGS2 page https://rack-centre.com/lagos-data-centre-campus-expansion/data-centre-campus-lgs-2-expansion/ | Oregun/Ikeja Lagos campus. LGS2 page gives 12 MW IT power, 25 MVA utility supply, six 2 MW data halls. | NERC CPG record names Rack Centre at 18 Jagal Close, Oregun, Lagos. Search LASPPPA/LASBCA, NCC, Uptime, Ikeja Electric. |
| Africa Data Centres / Cassava | https://www.africadatacentres.com/lagos/ | LOS1 Lagos official page; Lagos data centre for West Africa cloud/carrier-neutral services. | Search Eko Atlantic/Lagos planning, NERC, NCC, Uptime, local press for critical IT load and go-live status. |
| Open Access Data Centres / WIOCC | https://www.openaccessdc.net/lagos | OADC Lagos official page gives 7,200 m2 technical space, 24 MW site load, Equiano landing-station role. | NERC CPG record names Open Access Data Centre at Plot 99/100 Silverbird Road, Ikate Elegushi, Lagos, 3.20 MW. Search EIA, Lagos permits, Uptime, WIOCC/Equiano. |
| Digital Realty / Medallion | Digital Realty Lagos: https://www.digitalrealty.com/data-centers/emea/lagos ; Medallion rebrand/new Lagos release: https://www.digitalrealty.com/about/newsroom/press-releases/123225/medallion-opens-new-data-centre-in-lagos-and-rebrands-to-digital-realty- | Lagos/Victoria Island/Lekki carrier-neutral interconnect facilities. | Search NCC Teleafrica/Medallion International Data Access and Collocation, Lagos permits, NERC/MYTO feeder docs. |
| Galaxy Backbone | https://galaxybackbone.com.ng/ ; FAQ: https://galaxybackbone.com.ng/ufaqs/does-galaxy-backbone-operate-a-datacentre/ | Official FAQ says Tier III Abuja and Tier IV Kano data centers. NCC release corroborates public-sector Tier III primary and secondary facilities. | Search FCT/Kano government notices, NITDA, Uptime, NCC, NERC/TCN. |
| Kasi Cloud | https://www.kasicloud.com/ ; NSIA release: https://nsia.com.ng/kasi-cloud-ltd-breaks-ground-in-lagos-nigeria-on-new-hyperscale-data-center/ | Official site says sustainable Africa datacenter platform, office in Lekki, LOS campus and coming DNEK campus in Eket, Akwa Ibom; NSIA release covers Lagos groundbreaking. | Search Lagos planning/EIA/NERC, Akwa Ibom/Eket official notices, DCD/Capacity Media for stage and capacity. |
| MTN Nigeria | https://www.mtn.ng/ and NCC/NERC/Uptime records | Telco data centres/switches in Lagos, Abuja, Ibadan, Enugu, Kano, Kaduna, Uselu, Owerri and others. | NERC CPG entries and Uptime Ojota record are primary. Distinguish commercial cloud/colo from internal switch facilities. |
| Airtel / Nxtra | Airtel Africa datacenter page: https://www.airtel.africa/data-centers | Nxtra/Airtel hyperscale programme includes African hubs; Nigeria/Lagos Eko Atlantic leads appear in industry coverage. | Search Eko Atlantic/Lagos planning, NERC, NCC Airtel/Telesonic records, official Airtel/Nxtra releases. |
| 21st Century Technologies / ipNX / Cyberspace / inq.Digital / NTT | Official operator sites + NCC licence register | Smaller Lagos enterprise, metro fibre, cloud/colocation, ISP and edge leads. | Verify with NCC, Uptime, operator facility page, and state planning/power evidence before counting. |

---

## 3. State-by-state enumeration strategy

For each state/FCT:
1. Run official-domain searches: state/FCT website, physical planning/building-control agency, EAD/Federal Ministry of Environment, NCC, NERC, NITDA/Galaxy Backbone, Uptime.
2. Run town/locality searches with English variants: `data centre`, `data center`, `datacentre`, `server room`, `server farm`, `colocation`, `cloud`, `Tier III`, `Tier IV`, `MW`, `MVA`, `captive power`, `building permit`, `EIA`.
3. Run operator names: `Equinix`, `MainOne`, `MDXi`, `Rack Centre`, `Africa Data Centres`, `OADC`, `WIOCC`, `Digital Realty`, `Medallion`, `Galaxy Backbone`, `MTN`, `Airtel`, `Nxtra`, `Kasi Cloud`, `21st Century`, `ipNX`, `Cyberspace`, `NTT`, `inQ`, `Zinox`, `Broadbased`, `Fleek`, `Raeanna`, `Oodua Infraco`.
4. For any MoU/press lead, require at least one primary source or mark as B/C planned/announced. Do not upgrade a state ICT room, statistics data centre, command centre, bank DC, or telecom switch to commercial colocation without evidence of hosting/colo services.

Universal state templates:

```text
"{state}" Nigeria "data centre"
"{state}" Nigeria "data center"
"{state}" Nigeria datacentre
"{state}" Nigeria "server room" "data centre"
"{state capital}" Nigeria "data centre"
"{state}" Nigeria "state data centre"
"{state}" Nigeria "cloud" "data centre"
"{state}" Nigeria "EIA" "data centre"
"{state}" Nigeria "building permit" "data centre"
"{state}" Nigeria "captive power" "data centre"
site:ncc.gov.ng "{state}" "Collocation/Infrastructure"
site:nerc.gov.ng "{state}" "{operator}" "NERC/CPG"
site:ead.gov.ng "{state}" "data centre"
site:uptimeinstitute.com "Nigeria" "{state or city}"
```

### 3.1 Priority clusters and state-specific routes

| State/FCT | Main localities | Official-first method |
|---|---|---|
| Lagos | Lekki, Victoria Island, Ikoyi, Ikeja, Oregun, Eko Atlantic, Ikate Elegushi, Yaba, Apapa, Ojota, Gbagada, Ajao Road | Highest priority. Search LASPPPA/LASBCA/LASIMRA, EAD, NCC, NERC, Uptime, Eko Atlantic, and operator pages for Equinix/MainOne/MDXi, Rack Centre, ADC, OADC, Digital Realty/Medallion, Kasi, MTN, Airtel/Nxtra, 21st Century, ipNX, Cyberspace, NTT/inQ. |
| Abuja Federal Capital Territory | CBD, Maitama, Garki, Wuse, Utako, Gwarinpa, Abuja municipal area | Search FCTA development control, Galaxy Backbone, NCC/NITDA/NERC, Uptime, federal procurement, `National Shared Services Centre`, `Government Cloud`, `Abuja data centre`. |
| Kano | Kano city, Ahmadu Bello Way, Challawa | Search Galaxy Backbone Kano, Uptime, Kano State ICT, NERC MTN/Kano Switch and captive power, NCC Infraco North West. |
| Rivers | Port Harcourt, Bonny, Onne, Trans Amadi, Rumuolumeni | Search Equinix PR1/MainOne/2Africa, Rivers State planning, EAD, NERC/TCN/oil-gas captive power, NCC/cable landing, interconnectnigeria leads. |
| Ogun | Sagamu, Flowergate Industrial Park, Atakobo/Ijebu East, Ota, Abeokuta | Search Ogun planning, EIA, NERC, MainOne Sagamu historic lead, Tetracore/Huawei/Atakobo Energy Park. Verify old Sagamu announcements before counting. |
| Akwa Ibom | Eket, Uyo, Qua Iboe area | Search Kasi Cloud DNEK/Eket, Akwa Ibom official planning/EIA, NERC/oil-gas power, NCC South South Infraco. |
| Cross River | Calabar, Tinapa/free-trade-zone area | Search Cross River planning, Nugi Group, 9mobile state-government proposal, EAD, hydro/gas/solar power claims, NCC South South Infraco. |
| Benue | Makurdi | Search Benue Digital Infrastructure Company, UniCloud Africa, state official/MoU pages, EIA, NERC, Africa Data Centres disaster-recovery references. |
| Abia | Aba, Umuahia, Ohafia, Owaza River | Search Abia State/WIOCC/OADC digital infrastructure MoU, state broadband duct project, EAD, NCC South East Infraco, NERC. |
| Enugu | Enugu city, Independence Layout | Search NCC/NERC MTN Enugu switch, state ICT, Zinzara/Collocation licence, Enugu planning and EIA. |
| Oyo | Ibadan | Search MTN Ibadan Switch NERC record, Oyo planning, FarmKonnect precision-data centre, state ICT/e-government. |
| Kaduna | Kaduna city, Kakuri, Kachia corridor | Search MTN Kaduna Switch NERC, Kaduna State ICT/Bureau of Statistics, NCC North West Infraco, state planning/EIA. |
| Edo | Benin City, Uselu | Search MTN Uselu NERC lead, Edo State data center/digital government, state ICT agency, EIA/planning. |
| Borno | Maiduguri | Search Borno State Data Center, World Bank/eHealth Africa, state reconstruction/ICT docs, EAD. |
| Bayelsa | Yenagoa, ICT Village, creek/off-grid oil-gas areas | Search Bayelsa official ICT Village, EAD, NERC/oil-gas power, social/off-grid mining leads as C unless official. |
| Sokoto, Yobe, Zamfara, Ebonyi, Anambra, Bauchi, Delta, Ekiti, Gombe, Imo, Jigawa, Kebbi, Kogi, Katsina, Kwara, Nasarawa, Niger, Ondo, Osun, Plateau, Taraba | State capitals and government-house/ICT hub locations | Mostly government ICT rooms, state data centres, telecom switches, or negative searches. Use official state domains, NITDA, NCC, NERC, and Uptime; mark no-project only after both English variants and operator terms fail. |

### 3.2 Local-language secondary checks

Use sparingly; commercial sources are English.

```text
"{state}" "ile data" "data centre" Nigeria
"{town}" "kituo cha data" Nigeria
"{state}" "cibiyar bayanai" "ICT"
"{state}" "data centre" "Igbo" "ICT"
```

Do not count a local-language hit unless it identifies a physical facility, operator/proponent, function, and state/LGA location.

---

## 4. Evidence extraction checklist

For every candidate record, capture:
- `country_code=NG`, state/FCT, LGA, city/town, locality/street/plot, coordinates if available.
- Facility/project name and aliases: e.g. `LG1`, `LG2`, `LG3`, `LGS1`, `LGS2`, `LOS1`, `PR1`, `DNEK`, `Kano Data Center`, `National Shared Services Centre`.
- Developer/operator/legal owner/SPV and parent group.
- Status and date basis: announced, MoU, permit, EIA disclosure, captive-power permit, construction, commissioned, operational.
- Capacity fields separately: IT load MW, site load MW/MVA, captive generation MW, utility import MVA, racks, white space, data halls, storage PB.
- Primary-source URLs: state/FCT planning, EAD, NCC, NERC, Uptime, operator page, cloud-provider page.
- Caveats: telecom switch vs commercial colocation, government ICT room vs datacenter, cloud local zone vs cloud region, MoU vs construction, old unbuilt project vs active facility.
