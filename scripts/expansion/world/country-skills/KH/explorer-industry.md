# KH Explorer - Industry / Vendor Discovery for Cambodia Datacenters

Date: 2026-08-12. Scope: Cambodia (KH) datacenter enumeration through Cambodian colo/provider pages, cloud-region documents, trade press, associations/regulators, and province-level English/Khmer query patterns. Reliability grades: **A** = primary government, regulator, operator, cloud-provider, Uptime Institute, PeeringDB, or investment-certificate source; **B** = established trade press / Cambodian business press with named project facts; **C** = directories, broker/market reports, hosting-location pages, social posts, MoUs, or unsourced reposts.

---

## 0. Cambodia-specific search model

Cambodia has no public facility registry and very little planning-permit visibility. Enumeration works by triangulating four channels:

1. **Telecom / data-center licensing**: Ministry of Post and Telecommunications (MPTC) licensing notices and Telecom Regulator of Cambodia (TRC) operator lists identify legal entities allowed to operate telecom/ISP/IDC-like services.
2. **Investment approvals**: Council for the Development of Cambodia (CDC) qualified investment project (QIP) announcements sometimes name data-center projects, investment amount, district, and jobs.
3. **Operator/vendor pages**: carrier, ISP, cloud, and colocation operators publish the most concrete facility facts, but often omit MW and exact technical capacity.
4. **Trade press + directories**: DCD, W.Media, Khmer Times, Phnom Penh Post, Construction & Property, DataCenterMap, Baxtel, PeeringDB, Cloudscene, and Uptime Institute awards lists fill gaps and surface new projects.

The market is overwhelmingly **Phnom Penh**:

- **Phnom Penh / Daun Penh / 7 Makara / Chamkarmon / Tonle Bassac / Srah Chork / Monivong**: ByteDC, Chaktomuk Data Center, Telcotech / Royal Group Elite DC1, Telcotech Kampus, Daun Penh Data Center, MekongNet IDC1/IDC2, HT Networks, Ezecom/SINET/MekongNet ISP facilities, Metfone/Viettel core network facilities, and the government National Data Center.
- **Kandal / Phnom Penh fringe**: sweep for spillover because Kandal surrounds the capital and hosts SEZ/logistics land, but current public evidence is weak-to-none for named DC projects.
- **Preah Sihanouk / Sihanoukville, Svay Rieng / Bavet, Koh Kong, Banteay Meanchey / Poipet, Kampong Speu**: sweep SEZ, cross-border cable, power, and "digital hub" announcements. Treat claims as **C** until there is operator, CDC, MPTC, or construction evidence.
- Other provinces mostly produce no hits beyond telecom POPs, e-government rooms, and cloud/hosting marketing.

## 1. English and Khmer query vocabulary

Use English first for trade press and operator pages, then Khmer for government/local press. Khmer search coverage is inconsistent; pair Khmer terms with English brand names and locations.

Core English nouns:

```text
data center
data centre
datacenter
Internet Data Center
IDC
colocation
co-location
carrier neutral
cloud data center
cloud service
server room
disaster recovery site
DR site
hyperscale
AI data center
national data center
```

Core Khmer terms:

```text
មជ្ឈមណ្ឌលទិន្នន័យ
មជ្ឈមណ្ឌលទិន្នន័យជាតិ
មជ្ឈមណ្ឌលទិន្នន័យកម្ពុជា
មជ្ឈមណ្ឌលទិន្នន័យ ភ្នំពេញ
សេវា cloud
ម៉ាស៊ីនមេ
មជ្ឈមណ្ឌលបច្ចេកវិទ្យា
បណ្តាញទូរគមនាគមន៍
ការវិនិយោគ
គម្រោងវិនិយោគ
សាងសង់
សម្ពោធ
អាជ្ញាបណ្ណ
```

Status and evidence words:

```text
CDC
Council for the Development of Cambodia
QIP
qualified investment project
MPTC
TRC
Telecommunication Regulator of Cambodia
Uptime Institute
Tier III
TCDD
designed facility
certification
groundbreaking
inaugurated
launched
opening
approved
construction
investment certificate
special purpose data center license
submarine cable
MCT cable
AAG cable
Phnom Penh Special Economic Zone
Sihanoukville Special Economic Zone
Manhattan SEZ
Poipet PP SEZ
```

High-yield query templates:

```text
"Cambodia" ("data center" OR "data centre" OR datacenter OR IDC) ("Phnom Penh" OR "Daun Penh" OR "Chamkarmon")
"Cambodia" ("data center" OR "data centre") ("Uptime Institute" OR "Tier III" OR TCDD)
"Cambodia" ("data center" OR "data centre") ("CDC" OR "Council for the Development of Cambodia" OR QIP OR approved)
"Cambodia" ("data center" OR "data centre") ("MPTC" OR "TRC" OR license OR licence)
"Cambodia" ("data center" OR "data centre") ("MW" OR "IT load" OR racks OR sqm OR "sq ft")
"Phnom Penh" ("colocation" OR "co-location" OR "Internet Data Center" OR IDC) ("Ezecom" OR SINET OR MekongNet OR Telcotech OR Metfone)
"{operator}" Cambodia ("data center" OR "data centre" OR colocation OR cloud)
"{operator}" Phnom Penh ("IDC" OR "data center" OR "PeeringDB" OR "Uptime")
site:mptc.gov.kh ("data center" OR "data centre" OR "មជ្ឈមណ្ឌលទិន្នន័យ")
site:trc.gov.kh Cambodia ("operator" OR "license" OR "ISP")
site:cdc.gov.kh ("data center" OR "data centre" OR "មជ្ឈមណ្ឌលទិន្នន័យ")
site:construction-property.com Cambodia "data center"
site:khmertimeskh.com Cambodia "data center"
site:phnompenhpost.com Cambodia "data center"
site:datacenterdynamics.com Cambodia "data center"
site:w.media Cambodia "data center"
site:uptimeinstitute.com Cambodia "data center"
site:peeringdb.com Cambodia ("Phnom Penh" OR "data center")
```

Khmer/local templates:

```text
"ភ្នំពេញ" "មជ្ឈមណ្ឌលទិន្នន័យ" ("សម្ពោធ" OR "សាងសង់" OR "វិនិយោគ")
"កម្ពុជា" "មជ្ឈមណ្ឌលទិន្នន័យ" ("អាជ្ញាបណ្ណ" OR "ក្រសួងប្រៃសណីយ៍" OR MPTC)
"កម្ពុជា" "មជ្ឈមណ្ឌលទិន្នន័យជាតិ" ("ជប៉ុន" OR "ជំនួយ" OR "សាងសង់")
"{province_khmer}" ("មជ្ឈមណ្ឌលទិន្នន័យ" OR "data center" OR IDC) ("វិនិយោគ" OR "សាងសង់" OR "SEZ")
```

Stage mapping:

- `MoU`, partnership, digital-hub ambition = **C** intent unless paired with site, investment certificate, or construction.
- CDC approval / QIP / investment certificate = **A-/B+** for legal entity, location, capex, and approval status; still verify construction separately.
- MPTC data-center license notice = **A** for licensing/legal eligibility; not proof the facility is built unless facility is named.
- Uptime TCDD / Tier III design certification = **A** for design certification; not proof of live service.
- Operator "launched", "inaugurated", service page, PeeringDB facility/org entry = **A-/B+** for operational presence; capacity may still be **B/C** if only in directories.

## 2. Primary government, regulator, and association sources

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Ministry of Post and Telecommunications (MPTC) | `https://mptc.gov.kh/` | Search MPTC news and licensing notices for "data center", "National Data Center", "special purpose data center license", and Khmer `មជ្ឈមណ្ឌលទិន្នន័យ`. A 2025 notice on applications for a license to establish and operate a data center is a key legal hook. | A |
| Telecom Regulator of Cambodia (TRC) | `https://trc.gov.kh/` | Operator/license universe: ISP, telecom, VoIP, infrastructure, and related licensees. Use to seed ISP/company pivots: Ezecom, SINET, Telcotech, MekongNet, Metfone/Viettel, Seatel, HT Networks, NeocomISP/NTC. | A |
| Council for the Development of Cambodia (CDC) | `https://cdc.gov.kh/` | QIP / investment-certificate announcements. Critical for Telcotech Kampus-style projects and any future provincial greenfield data center. Query English and Khmer. | A |
| Cambodia Digital Government Committee / Ministry digital-government pages | `site:gov.kh "National Data Center" Cambodia`, MPTC and DGC routes | Government national data center, e-government cloud, data-sovereignty infrastructure. Use as government-owned DC pipeline evidence. | A/B |
| Uptime Institute awards list | `https://uptimeinstitute.com/uptime-institute-awards/list` | Search Cambodia, Phnom Penh, ByteDC, Chaktomuk, Telcotech, Royal Group Elite DC1. Certifies design or constructed facility names; record exact award type. | A |
| PeeringDB | `https://www.peeringdb.com/` | Network/operator/facility evidence for Phnom Penh interconnection players. Useful for Chaktomuk, Viettel Cambodia/Metfone, and any exchange-connected site. | A-/B |
| Cambodia Chamber of Commerce / EuroCham / AmCham Cambodia / Cambodia Association of Finance & Technology | `site:cc-cambodia.org`, `site:eurocham-cambodia.org`, `site:amchamcambodia.net`, `site:caftcambodia.org` | Not DC associations, but useful for digital-economy events, cloud/security vendors, and operator membership leads. | B/C |
| Cambodia Securities Exchange (CSX) / bond filings | `https://csx.com.kh/`, Phnom Penh Post business coverage | Telcotech/Royal Group financing can mention data-center capex and telecom infrastructure. | A/B |

There is no strong evidence of a dedicated national "Cambodia Data Center Association" comparable to larger APAC markets. Use business chambers, telecom regulator/operator lists, and cloud/ICT events instead.

## 3. Cambodian operator and facility seed list

Official operator pages are **A** for claimed service presence. For MW/capacity, prefer operator/Uptime/CDC evidence; directories are discovery only unless cross-checked.

| Operator / facility | Primary routes | Location and query pivots | Notes |
|---|---|---|---|
| ByteDC Solutions / ByteDC Data Center | `https://bytedc.com/`, DCD, Khmer Times, Uptime Institute | `ByteDC Data Center`, `Global Tech Exchange`, `Land 356 Street R-4`, `Srah Chork`, `Daun Penh`, `Phnom Penh`, `3 MW`, `1000 racks` | Cambodia-Singapore-backed carrier-neutral Tier III design-certified facility in Phnom Penh, inaugurated 2023. Strong benchmark record. |
| Chaktomuk Data Center (CDC) / PNH1 | `https://www.chaktomuk-dc.com.kh/`, Uptime, PeeringDB, Baxtel/DataCenterMap | `Chaktomuk Data Center`, `PNH1`, `Tier III Plus`, `Phnom Penh` | Markets central Phnom Penh Tier III Plus design certification. Capacity not public; verify through Uptime and network entries. |
| Telcotech / Royal Group Elite DC1 | `https://www.telcotech.com.kh/`, Uptime, Phnom Penh Post, CSX | `Royal Group Elite DC1`, `Telcotech Data Centre`, `Telcotech colocation`, `AAG`, `MCT cable` | Royal Group-linked carrier-neutral operator; submarine cable ownership is useful evidence for serious infrastructure. Tier III design announcement in 2025. |
| Telcotech Kampus data center | Telcotech news, CDC, Construction & Property, Kampus/Keystone supplier pages | `Kampus Building`, `Monivong Boulevard`, `Tonle Bassac`, `Chamkarmon`, `US$27.7 million` | CDC-approved Phnom Penh data-center project. Treat as approved/under development until operator opening evidence is found. |
| National Data Center Cambodia | MPTC, Japan/JICA/Japanese embassy coverage, W.Media, Construction & Property, Baxtel | `National Data Center Cambodia`, `MPTC`, `Japan grant aid`, `US$30 million`, `3 MW`, `Phnom Penh` | Government-owned national data center. Track construction and handover dates through MPTC/Japan aid sources. |
| Kepstar Data Centre Management | DCD, W.Media, Network World, Baxtel | `Kepstar DC1`, `Kepstar DC2`, `Singtel advising`, `6.5 MW`, `3.5 MW`, `Cambodia Tech Expo` | Reported two-site program around Phnom Penh / DR site about 100 km away. Status and exact DC2 province need caution. |
| Ezecom / EZECOM | `https://www.ezecom.com.kh/`, Knight Frank Cambodia report, TRC | `Ezecom data center`, `EZECOM cloud`, `Royal Group ISP`, `Phnom Penh colocation` | Major fiber/ISP/cloud provider. Public facility details sparse; use as operator seed and cross-check via TRC, PeeringDB, customer hosting pages. |
| SINET Cambodia | `https://www.sinet.com.kh/`, TRC, Baxtel/Cloudscene | `SINET data center`, `SINET cloud`, `Phnom Penh IDC` | ISP/MSP operator. Directory evidence exists; seek official service pages or customer/network listings before grading above C/B. |
| MekongNet / Angkor Data Communication | `http://mekongnet.com.kh/`, DataCenterMap/DataCenterJournal, TRC | `MekongNet IDC1`, `MekongNet IDC2`, `AnAnA Building`, `SunCity Building`, `Norodom Blvd`, `Street 370` | Two Phnom Penh IDC facilities reported; strong local ISP seed, but MW not public. |
| Seatel / South East Asia Telecom | Seatel cloud pages if live, Baxtel, Network World, TRC | `Seatel Cloud Data Center`, `Cambodia 2 MW`, `Phnom Penh` | Mobile/satellite telecom operator with reported cloud data center. Capacity often directory-derived; verify with official Seatel materials if possible. |
| Daun Penh Data Center (DPDC) | DataCenters.com, DataCenterMap, Baxtel, Daun Penh Group/design pages | `Daun Penh Data Center`, `DPDC`, `Hun Sen Boulevard`, `Phnom Penh` | Commercial colo/hosting facility. Operator official public footprint is limited; use directories as C/B unless corroborated. |
| HT Networks | DataCenterMap, PeeringDB/company pages, TRC | `HTN-IDC`, `HT Networks IDC`, `Street 114`, `7 Makara`, `Phnom Penh` | Small colocation/network facility. |
| Metfone / Viettel Cambodia | PeeringDB, Metfone/Viettel pages, TRC | `Viettel Cambodia data center`, `Metfone IDC`, `Phnom Penh core network`, `PeeringDB org 9493` | Likely core-network/data-center infrastructure; do not count as commercial colo unless facility evidence is explicit. |
| NeocomISP / NTC | Knight Frank Cambodia, TRC, local hosting pages | `NeocomISP NTC data center`, `NTC Cambodia colocation` | Named in market reports but facility facts are weak. Treat as C seed until official/operator evidence is found. |

## 4. Cloud regions and hyperscaler checks

As of this methodology pass, no major global cloud provider has an official Cambodia region. Use official region/location pages as **A** for absence/presence, then pivot "Cambodia" references to partner/local-zone/CDN/edge deployments rather than assuming a physical cloud region.

| Provider | Route | Cambodia interpretation |
|---|---|---|
| AWS | `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/` | No Cambodia Region in the official region list; search for `AWS Cambodia Local Zone`, `AWS Phnom Penh edge`, and Cambodian partner announcements only. |
| Microsoft Azure | `https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/` | No Cambodia Azure geography/region. Cambodia references are customer/partner or network edge unless official docs change. |
| Google Cloud | `https://cloud.google.com/about/locations` | No Cambodia Google Cloud region. Search for CDN/partner/cache nodes and government cloud programs separately. |
| Oracle Cloud Infrastructure | `https://www.oracle.com/cloud/public-cloud-regions/` | No Cambodia OCI public region. Check for partner deployments only. |
| Alibaba Cloud | `https://www.alibabacloud.com/global-locations` | No Cambodia region in global locations; ASEAN regions in Singapore/Malaysia/Thailand/Indonesia can be mistaken for Cambodia coverage. |
| Huawei Cloud / Tencent Cloud | Official global region pages | No clearly official Cambodia public cloud region; search Khmer/English for partner cloud and telecom-hosted edge deployments. |

Cloud-region query templates:

```text
site:aws.amazon.com Cambodia "Region" "Local Zone"
site:azure.microsoft.com Cambodia "Azure region"
site:cloud.google.com Cambodia "region" "Cloud"
site:oracle.com Cambodia "cloud region"
site:alibabacloud.com Cambodia "region"
"Cambodia" ("cloud region" OR "availability zone" OR "local zone") ("AWS" OR Azure OR "Google Cloud" OR OCI OR Alibaba OR Huawei)
```

Do not turn "available to Cambodian customers" into a Cambodia facility. Require explicit country/city region, local zone, edge location, or named operator-hosted facility.

## 5. Trade press, directories, and market sources

| Source | Search route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | `site:datacenterdynamics.com Cambodia "data center"` | Best global trade feed for ByteDC, Kepstar, consortium/MoU history, and Cambodia launch coverage. | B+ |
| W.Media | `site:w.media Cambodia "data center"` | Strong APAC event/market coverage; useful for National Data Center and Kepstar/ByteDC items. | B |
| Khmer Times | `site:khmertimeskh.com Cambodia "data center"` | Local English business coverage; good for inaugurations, national data center, digital policy. | B |
| Phnom Penh Post | `site:phnompenhpost.com Cambodia "data center"` | Business and capital-market coverage; useful for Telcotech bond/Royal Group infrastructure context. | B |
| Construction & Property Cambodia | `site:construction-property.com Cambodia "data center"` | High-yield for CDC approvals, construction starts, public buildings, and Kampus/Telcotech-style projects. | B |
| Open Development Cambodia | `site:opendevelopmentcambodia.net Cambodia "data center"` | Good aggregator of local news/regulatory announcements with stable pages. Verify originals. | B/C |
| Knight Frank Cambodia / CBRE / JLL / Cushman reports | `Cambodia data centres report Knight Frank PDF`, broker pages | Market structure and operator names. Do not use aggregate MW or forecasts as facility proof. | B/C |
| Baxtel, DataCenterMap, DataCenters.com, Cloudscene, DataCenterJournal | Search Cambodia / Phnom Penh / operator | Facility discovery, address hints, MW when no other source exists. Always re-check operator/Uptime/PeeringDB. | C, sometimes B when corroborated |
| PeeringDB | Search Cambodia, Phnom Penh, operator names | Network presence and facility/org validation. Useful for active connectivity but not capacity. | A-/B |

Trade-press templates:

```text
site:datacenterdynamics.com Cambodia "ByteDC"
site:datacenterdynamics.com Cambodia "Kepstar"
site:datacenterdynamics.com Cambodia "Telcotech"
site:w.media Cambodia "National Data Center"
site:khmertimeskh.com "data center" "Phnom Penh"
site:phnompenhpost.com Telcotech "data center"
site:construction-property.com "data center" "CDC" "Phnom Penh"
"Cambodia data centres report" "Knight Frank" "ByteDC" "Ezecom"
"Cambodia" "data center" ("Baxtel" OR "DataCenterMap" OR "Cloudscene" OR "PeeringDB")
```

## 6. Province/autonomous-municipality enumeration patterns

Use the manifest spellings plus common English spellings and Khmer names. Start broad, then add data-center nouns, SEZ/industrial park terms, named operators, power/substation, and cable/connectivity terms.

Base per-division template:

```text
"{division}" ("data center" OR "data centre" OR datacenter OR IDC OR colocation OR "server farm" OR hyperscale)
"{common_spelling}" ("data center" OR "Internet Data Center" OR "cloud data center" OR "disaster recovery")
"{province_khmer}" ("មជ្ឈមណ្ឌលទិន្នន័យ" OR "data center" OR IDC)
"{division}" ("CDC" OR QIP OR "investment project" OR "special economic zone" OR SEZ) ("data center" OR "digital" OR cloud)
"{division}" ("substation" OR "power plant" OR "transmission line" OR MW OR MVA) ("data center" OR hyperscale OR "digital hub")
"{division}" ("Ezecom" OR SINET OR MekongNet OR Telcotech OR Metfone OR Seatel OR ByteDC OR Kepstar OR Chaktomuk)
site:cdc.gov.kh "{division}" ("data center" OR "digital" OR cloud OR "ICT")
site:mptc.gov.kh "{division}" ("data center" OR "មជ្ឈមណ្ឌលទិន្នន័យ")
site:khmertimeskh.com "{common_spelling}" "data center"
site:construction-property.com "{common_spelling}" "data center"
```

Priority groups:

| Division | Common spellings / Khmer anchors | Query pivots |
|---|---|---|
| Phnom Penh | `Phnom Penh`, `ភ្នំពេញ`, `Daun Penh`, `7 Makara`, `Chamkarmon`, `Tonle Bassac`, `Srah Chork`, `Monivong` | Full operator sweep; facility names; Uptime; PeeringDB; CDC; MPTC; construction and inauguration terms. |
| Kandaal | `Kandal`, `Kandaal`, `កណ្ដាល`, `Takhmao`, `Ang Snuol`, `Kien Svay` | Phnom Penh spillover, logistics/SEZ sites, backup/DR site, power-substation queries, Royal Group/PPSEZ. |
| Preah Sihanouk | `Sihanoukville`, `Preah Sihanouk`, `ព្រះសីហនុ`, `Sihanoukville SEZ`, `SSEZ` | SEZ and port digital hub claims, submarine cable landing, power/cooling, Chinese-language `西港 数据中心`. |
| Svaay Rieng | `Svay Rieng`, `Bavet`, `ស្វាយរៀង`, `Manhattan SEZ` | Border SEZ, Vietnam connectivity, industrial power. Search English, Khmer, and Chinese. |
| Banteay Mean Choay | `Banteay Meanchey`, `Poipet`, `បន្ទាយមានជ័យ`, `Poi Pet PP SEZ` | Thailand border/Poipet SEZ, cross-border fiber, disaster recovery. |
| Kaoh Kong | `Koh Kong`, `Kaoh Kong`, `កោះកុង`, `Dara Sakor`, `Neang Kok SEZ` | SEZ/port/energy projects; treat tourism/smart-city language as weak unless facility is named. |
| Kampong Spueu | `Kampong Speu`, `Kampong Spueu`, `កំពង់ស្ពឺ`, `Phnom Penh SEZ` | Capital fringe, manufacturing SEZ, land-bank/project company searches. |
| Siem Reab | `Siem Reap`, `Siem Reab`, `សៀមរាប` | Smart-city/tourism ICT may create false positives; require facility/operator proof. |
| Baat Dambang | `Battambang`, `Baat Dambang`, `បាត់ដំបង` | Regional telco POPs and DR site possibilities only. |
| Kampong Chaam / Tbong Khmum | `Kampong Cham`, `Tboung Khmum`, `Kampong Cham-Kratie corridor` | Industrial corridor and telco POP queries. |
| Kampot / Kaeb | `Kampot`, `Kep`, `កំពត`, `កែប` | Port/tourism false positives; check only if SEZ/digital hub appears. |
| Pousaat / Kracheh / Mondol Kiri / Rotanak Kiri / Preah Vihear / Stueng Traeng / Otdar Mean Chey / Pailin / Taakaev / Kampong Chhnang / Kampong Thum | common English variants: `Pursat`, `Kratie`, `Mondulkiri`, `Ratanakiri`, `Stung Treng`, `Oddar Meanchey`, `Takeo`, `Kampong Chhnang`, `Kampong Thom` | Low-priority sweep for government cloud rooms, telco core sites, power/hydropower-adjacent claims, and local press. Expect no_projects unless named facility evidence appears. |

Chinese-language sweep for Chinese-invested SEZs:

```text
"柬埔寨" ("数据中心" OR "云计算中心" OR IDC) ("金边" OR "西港" OR "西哈努克" OR "波贝" OR "柴桢")
"柬埔寨" "{province_chinese}" ("数据中心" OR "云服务" OR "机房")
"柬埔寨" ("经济特区" OR "园区") ("数据中心" OR "数字经济" OR "云计算")
```

Use Chinese hits as leads only; verify with CDC/MPTC/operator/local press before adding records.

## 7. Verification and grading rules

Evidence hierarchy:

1. **A**: MPTC/TRC license notices, CDC/QIP approval pages, Uptime Institute award list, operator official facility page, official cloud-provider region page, PeeringDB network/facility record for active interconnection.
2. **B**: DCD, W.Media, Khmer Times, Phnom Penh Post, Construction & Property, supplier case studies with named site/equipment, reputable real-estate reports naming operators.
3. **C**: Baxtel/DataCenterMap/Cloudscene/DataCenters.com when not corroborated, hosting provider "location" pages, market forecasts, broker aggregate capacity, MoUs without permits/construction.

Capacity rules:

- Cambodia operators often publish racks or building size but not MW. If MW comes only from Baxtel or a market report, store it with **B/C** confidence and note source.
- Separate `design capacity`, `critical IT load`, `built floor area`, and `racks`. Do not convert racks to MW unless explicitly required; small ISP racks may be much lower-density than hyperscale racks.
- For Uptime, record the exact award type: `Tier III Certification of Design Documents` is not the same as operational certification.
- For government facilities, distinguish national e-government infrastructure from commercial colocation.
- Avoid double-counting by matching `ultimate parent + facility/campus + address`: Telcotech/Royal Group, Ezecom/Telcotech/Royal Group links, and MekongNet/Angkor Data Communication names can appear under multiple brands.

Status rules:

- `approved` = CDC/QIP or government approval but no live service evidence.
- `construction` = groundbreaking, construction contract, equipment/supplier case, or official build update.
- `operational` = operator service page, launch/inauguration, PeeringDB active network/facility, Uptime constructed/operational certification, or multiple directory/customer records.
- `planned` = MoU, announced program, "largest data center" claim, or market-report pipeline only.

## 8. Recommended workflow

1. **Seed Phnom Penh** with known operator/facility names in section 3; query each across operator page, Uptime, PeeringDB, DCD/W.Media, Khmer Times, and directories.
2. **Build the licensed operator universe** from TRC/MPTC, then pivot every ISP/mobile/fiber operator into `data center`, `IDC`, `colocation`, and Khmer terms.
3. **Search CDC/QIP approvals** for "data center", "digital", "cloud", "ICT", and the operator legal names; classify CDC-only records as approved, not operational.
4. **Run province sweeps** using section 6, prioritizing Phnom Penh, Kandal, Preah Sihanouk, Svay Rieng, Banteay Meanchey/Poipet, Koh Kong, and Kampong Speu.
5. **Check cloud-provider official region pages** once per run so "Cambodia region" claims are either rejected or upgraded if a provider has changed its official footprint.
6. **Verify capacity/status** through the section 7 hierarchy before writing records; Cambodia market reports are useful discovery aids but are not facility-proof by themselves.

Pitfalls: "Cambodia cloud" often means hosted abroad; "available in Cambodia" is not a Cambodia region; MPTC license permission is not a built facility; Uptime design certification is not live status; Khmer/English transliterations vary heavily; and capital-market or bond articles may describe telecom capex without naming a specific data-center building.
