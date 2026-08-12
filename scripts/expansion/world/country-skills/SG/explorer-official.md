# SG Explorer Official - Singapore Datacenter Enumeration Methodology

Date reviewed: 2026-08-12. Country: **SG Singapore**. Division model: **district**. Divisions covered: **Central Singapore; North East; North West; South East; South West** (the five Community Development Council / CDC districts). Scope: official, regulatory, statutory, procurement, utility, and cloud-region sources for enumerating Singapore datacenter projects.

Reliability grades:
- **A** = primary / legally accountable source for the specific fact cited: IMDA, MDDI, MTI, EDB, URA, BCA, EMA, SP Group, GovTech, GeBIZ, ACRA, SGX, REIT annual reports, official cloud-region pages, or operator-owned facility pages.
- **B** = reliable secondary source: Data Center Dynamics, The Business Times, The Straits Times, CNA, Reuters, Bloomberg, FT, W.Media, The Edge Singapore, reputable contractor releases, or law-firm notes that accurately describe the statutory process.
- **C** = lead source only: aggregator directories, broker pages, market-research counts, event pages, social posts, job ads, or unsourced lists.
- **U** = unsupported after checking. Keep U only as a temporary work queue item, and never count it as a facility.

**Grade rule:** a grade applies only to the fact the cited source supports. A cloud-region page is A for region existence, not for physical addresses. An operator page is A for facilities, addresses, status, and marketed capacity it publishes, but not for undisclosed site coordinates. A press article is B for the named project facts in that article. Aggregators remain C even when they are accurate.

---

## 0. Singapore-Specific Structure Facts

- Singapore is a city-state and has no state/province tier. The requested division layer is the **five CDC districts**: Central Singapore, North East, North West, South East, and South West. The official People's Association CDC directory and SGDI both list these five districts: https://www.pa.gov.sg/our-network/community-development-councils/community-development-councils/ and https://www.sgdi.gov.sg/other-organisations/community-development-councils
- Datacenter siting evidence normally uses **URA planning areas, estates, roads, or postal districts**, not CDC names. Always geocode a facility to an address / planning area first, then assign a CDC district. CDC districts are constituency-based and can move after elections; if an address sits near a boundary, record the planning area and mark the CDC assignment for manual GIS review.
- There is **no public national datacenter registry** and no public planning-application database that can be searched by datacenter use. Enumeration must join multiple trails: IMDA/EDB capacity allocation, URA planning controls, BCA/IMDA Green Mark records, energy / grid announcements, GeBIZ procurement, statutory filings, operator facility pages, and reputable press.
- Singapore sources usually spell the term **data centre**. US operators and global cloud pages often use **data center**. Use both.

---

## 1. Official / Regulatory Pipeline

### 1.1 IMDA and EDB - capacity allocation and digital infrastructure policy

Primary sources:
- IMDA home: https://www.imda.gov.sg/
- Pilot DC-CFA launch: https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2022/launch-of-pilot-data-centre---call-for-application-to-support-sustainable-growth-of-dcs
- Pilot DC-CFA selections, 14 July 2023: https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2023/four-data-centre-proposals-selected-as-part-of-pilot-data-centre-call-for-application
- Green Data Centre Roadmap: https://www.imda.gov.sg/how-we-can-help/green-dc-roadmap
- Green Data Centre Roadmap press release: https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2024/sg-announces-green-data-centre-roadmap
- DC-CFA2 page: https://www.imda.gov.sg/proposal-submission/call-for-application-data-centre-2
- DC-CFA2 factsheet: https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/factsheets/2025/launch-of-second-data-centre
- EDB home: https://www.edb.gov.sg/
- EDB Equinix SG6 announcement: https://www.edb.gov.sg/en/about-edb/media-releases-publications/equinix-advances-ai-with-high-performance-data-center-in-singapore.html

Method:
1. Treat IMDA/EDB DC-CFA material as the controlling official trail for **new incremental capacity** after the moratorium. The pilot DC-CFA selected four proposals and IMDA says about 80 MW would be awarded. Verified awardees: **AirTrunk-ByteDance consortium, Equinix, GDS, and Microsoft**. Use this as A-grade for the award/capacity-allocation fact only.
2. Treat DC-CFA2 as the current official pipeline. IMDA launched it on **1 December 2025** for **at least 200 MW** of capacity, with potentially more through green-energy pathways. As of this review, keep award results uncounted until IMDA/EDB publish selections.
3. Use the Green Data Centre Roadmap as policy context. It supports the near-term **at least 300 MW** additional-capacity target and the sustainability screen, not individual facility existence.
4. Use EDB releases to corroborate investment and operator commitments. EDB pages usually do not provide full addresses; do not infer addresses.

Official query templates:

```text
site:imda.gov.sg "data centre" Singapore
site:imda.gov.sg "DC-CFA" OR "Call for Application" "data centre"
site:imda.gov.sg "Green Data Centre Roadmap"
site:imda.gov.sg "Data Centre 2" "200MW"
site:edb.gov.sg "data centre" Singapore
site:edb.gov.sg "{operator}" "data centre"
"DC-CFA" "{operator}" Singapore
"Data Centre Call for Application" "AirTrunk" OR "Equinix" OR "GDS" OR "Microsoft"
```

### 1.2 MDDI / MTI / Parliament - ministerial and national-policy trail

Primary sources:
- MDDI digital infrastructure page: https://www.mddi.gov.sg/what-we-do/digital-development/digital-infrastructure/
- Digital Connectivity Blueprint launch speech: https://www.mddi.gov.sg/newsroom/speech-by-minister-josephine-teo-at-the-digital-connectivity-blueprint-launch/
- MTI ST Engineering Data Centre groundbreaking speech, 25 June 2024: https://www.mti.gov.sg/newsroom/speech-by-sms-low-yen-ling-at-st-engineering-data-centre-groundbreaking-ceremony/
- Parliament search: https://sprs.parl.gov.sg/search/ and https://www.parliament.gov.sg/

Method:
- MDDI is A-grade for national digital-infrastructure strategy, including the Digital Connectivity Blueprint goals such as doubling submarine-cable landing capacity within 10 years.
- MTI speeches are A-grade for the ceremony and facts stated by the minister. The ST Engineering speech supports that the fourth Singapore DC was under groundbreaking on 25 June 2024, planned operational by 2026, and intended to lift the group's Singapore DC portfolio to more than 30 MW.
- Parliament Q&A is A-grade for policy positions, but usually does not name private facility addresses.

```text
site:mddi.gov.sg "data centre"
site:mddi.gov.sg "Digital Connectivity Blueprint" "data centre"
site:mti.gov.sg "data centre" "groundbreaking"
site:mti.gov.sg "ST Engineering" "data centre"
site:sprs.parl.gov.sg "data centre"
site:parliament.gov.sg "data centre"
```

### 1.3 URA - land use and planning permission

Primary sources:
- URA home: https://www.ura.gov.sg/
- URA SPACE / Master Plan map: https://eservice.ura.gov.sg/maps/
- URA Development Control Handbooks: https://www.ura.gov.sg/guidelines/development-control/development-control-handbooks/
- B2 Allowable Uses: https://www.ura.gov.sg/guidelines/development-control/development-control-handbooks/non-residential/b2/allowable-uses/
- URA Circulars: https://www.ura.gov.sg/guidelines/circulars/

Verified rule: URA's B2 Allowable Uses page states that **Data Farms/Data Centres require prior planning permission** for assessment with technical agencies. Record this as A-grade regulatory context.

Method:
1. Start with address or estate from a primary operator / official / press source.
2. Use URA SPACE to record the Master Plan zoning and planning area.
3. Search URA circulars and development-control pages for policy changes affecting B1/B2/BP locations.
4. Do not interpret a missing web-search result as denial or absence of permission; Singapore's planning-permission records are not a complete public searchable facility registry.

```text
site:ura.gov.sg "data centre"
site:ura.gov.sg "Data Farms" "Data Centres"
site:ura.gov.sg "Business 2" "data centre"
site:ura.gov.sg "Business 1" "data centre"
"{address}" "URA" "data centre"
"{estate}" "planning permission" "data centre" Singapore
```

### 1.4 BCA / CORENET - building control and Green Mark

Primary sources:
- BCA home: https://www1.bca.gov.sg/
- BCA Green Mark other schemes page: https://www1.bca.gov.sg/sustainability/greenmark/other-green-mark-schemes/
- BCA-IMDA Green Mark for Data Centres: https://www.imda.gov.sg/how-we-can-help/bca-imda-green-mark-for-data-centres-scheme
- CORENET: https://www.corenet.gov.sg/
- Singapore Green Building Council summary of GMDC:2024 launch: https://www.sgbc.sg/gmdc2024/

Method:
- Use Green Mark only as certification evidence. It is A-grade for the certification fact if found on BCA/IMDA/operator pages, but not for facility completion unless the source says the building is operational.
- CORENET is an official electronic-submission system, but not a public datacenter register. Use it as process context, not as a facility count.
- DC-CFA2 requires applicants to meet the current BCA-IMDA Green Mark for Data Centres 2024 framework; confirm exact requirements from the IMDA DC-CFA2 page at each refresh.

```text
site:imda.gov.sg "Green Mark for Data Centres"
site:www1.bca.gov.sg "Green Mark" "Data Centres"
"BCA-IMDA Green Mark" "{operator}" "data centre"
"CORENET" "data centre" Singapore
```

### 1.5 EMA / SP Group - energy and grid

Primary sources:
- EMA: https://www.ema.gov.sg/
- SP Group: https://www.spgroup.com.sg/
- SP Services: https://eservices.spgroup.com.sg/

Method:
- There is no public registry of datacenter grid connections. Use EMA/SP sources for policy, grid-planning, green-energy import, and named connection announcements.
- Treat operator financing or PPA announcements as A when operator-owned, B when press-only, and never as proof that a facility is live unless energisation/opening is stated.

```text
site:ema.gov.sg "data centre"
site:spgroup.com.sg "data centre"
"{operator}" "SP Group" Singapore "data centre"
"{operator}" "green loan" "data centre" Singapore
"data centre" "grid connection" Singapore "MW"
```

### 1.6 GovTech / GeBIZ - public-sector procurement

Primary sources:
- GovTech: https://www.tech.gov.sg/
- GeBIZ: https://www.gebiz.gov.sg/

Method:
- Search GeBIZ for data-centre hosting, colocation, disaster recovery, managed hosting, cloud migration, and government cloud tenders. GeBIZ is A-grade for a public contract and vendor award, but usually not for the physical location because tenders often procure services from third-party colocation providers.
- GovTech material confirms whole-of-government cloud and hosting strategy, not private facility inventory.

```text
site:gebiz.gov.sg "data centre"
site:gebiz.gov.sg "colocation"
site:gebiz.gov.sg "data centre hosting"
site:tech.gov.sg "data centre"
site:tech.gov.sg "Government on Commercial Cloud" OR "GCC"
```

### 1.7 ACRA / SGX / REIT filings - legal entities and asset ownership

Primary sources:
- ACRA: https://www.acra.gov.sg/
- BizFile: https://www.bizfile.gov.sg/
- SGX: https://www.sgx.com/
- Keppel DC REIT publications: https://www.keppeldcreit.com/en/investor-relations/publications/

Method:
- Use ACRA/BizFile to resolve legal entities and UENs behind brands and SPVs. This is the join key for tenders, financing, permits, and operator pages.
- Use SGX and REIT annual reports for ownership, asset names, leases, and sometimes addresses. Annual reports are A-grade for portfolio composition and ownership percentages.

```text
site:acra.gov.sg "{legal_entity}"
site:bizfile.gov.sg "{legal_entity}"
site:sgx.com "Keppel DC REIT" "Singapore" "data centre"
site:keppeldcreit.com "KDC SGP" "annual report"
"{operator legal entity}" "UEN" "Singapore"
```

### 1.8 Cloud-region official pages

Primary sources:
- AWS Regions / AZs: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html and https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Microsoft Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle Cloud Singapore region: https://www.oracle.com/asean/cloud/cloud-regions/singapore/
- Oracle regions / availability domains: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm
- Alibaba Cloud global locations: https://www.alibabacloud.com/en/global-locations
- Alibaba Cloud regions and zones docs: https://www.alibabacloud.com/help/en/cloud-migration-guide-for-beginners/latest/regions-and-zones

Verified region facts:
- AWS **ap-southeast-1 Asia Pacific (Singapore)** is listed by AWS with **3 AZs**.
- Microsoft Azure **Southeast Asia** is listed by Microsoft with location **Singapore** and region ID **southeastasia**.
- Google Cloud **asia-southeast1** is listed as Singapore on Google Cloud locations.
- Oracle's **Singapore / ap-singapore-1** is an official OCI region.
- Alibaba Cloud lists **Singapore / ap-southeast-1** with **4 zones**.

Rule: cloud-region facts are A-grade for service-region existence only. They do not identify individual campuses, addresses, CDC districts, or MW.

---

## 2. Search Vocabulary

```text
"data centre" Singapore
"data center" Singapore
"datacenter" Singapore
"Data Farms" "Data Centres" Singapore
"DC-CFA" Singapore
"Call for Application" "data centre" Singapore
"Green Data Centre Roadmap" Singapore
"BCA-IMDA Green Mark" "data centre"
"planning permission" "data centre" Singapore
"Business 1" OR "Business 2" "data centre" Singapore
"colocation" Singapore
"hyperscale data centre" Singapore
"AI-ready data centre" Singapore
"cloud region" Singapore
"availability zone" Singapore
"Internet Data Centre" OR "IDC" Singapore
"cable landing station" Singapore
"submarine cable" OR "undersea cable" Singapore
"Internet exchange" OR "IXP" Singapore
```

Local-language terms, useful mainly for press completeness:

```text
"pusat data" Singapura
"pusat data raya" Singapura
"infrastruktur digital" Singapura
数据中心 新加坡
数据中心 新加坡 建设
云计算 新加坡
海底光缆 新加坡
互联网交换中心 新加坡
தரவு மையம் சிங்கப்பூர்
```

High-value place terms:

```text
Ayer Rajah, one-north, Alexandra, Bukit Merah, Kallang, Genting Lane
Tai Seng, Kaki Bukit, Ubi, Chai Chee, Tampines, Defu, Serangoon, Loyang, Changi, Tanah Merah
Woodlands, Sungei Kadut, Sembawang, Yishun
Jurong, Jurong East, Jurong West, International Business Park, Jalan Buroh, Tanjong Kling, Tuas, Boon Lay, Pioneer, Gul, Sunview Drive, Jalan Tukang
Punggol Digital District, Seletar
```

---

## 3. Per-Division Enumeration Approach

Always store both fields:
- `planning_area_or_estate`: URA planning area / industrial estate / address-derived place.
- `division`: one of Central Singapore, North East, North West, South East, South West.

### 3.1 Central Singapore

Likely pattern: dense smaller colocation, carrier hotels, enterprise DCs, and operator sites in central industrial / business-park pockets. Priority areas include Ayer Rajah / one-north, Alexandra / Bukit Merah, Genting Lane, Kallang, Bendemeer, Toa Payoh, Bishan, Ang Mo Kio, Downtown Core, Tanjong Pagar, Marina Bay, and part of Queenstown.

```text
"Ayer Rajah" "data centre" Singapore
"one-north" "data centre" Singapore
"Genting Lane" "data centre" Singapore
"Kallang" "data centre" OR "colocation" Singapore
"Alexandra" OR "Bukit Merah" "data centre" Singapore
"Raffles Place" OR "Tanjong Pagar" OR "Marina Bay" "carrier hotel" Singapore
```

### 3.2 North East

Likely pattern: lower current density; watch Defu, Hougang/Serangoon North industrial areas, and Punggol Digital District. Keppel lists KDC SGP 1 in Serangoon North. STT GDC lists STT Singapore 1/2/3 in Defu; CDC assignment can be sensitive because Defu/Hougang/Geylang-adjacent boundaries should be checked with GIS.

```text
"Defu" "data centre" Singapore
"STT Singapore" "Defu"
"Serangoon North" "data centre" Singapore
"Keppel DC Singapore 1" "Serangoon North"
"Punggol Digital District" "data centre" OR "digital infrastructure"
"Hougang" OR "Sengkang" OR "Seletar" "data centre" Singapore
```

### 3.3 North West

Likely pattern: established northern cluster around Woodlands and nearby industrial estates. Global Switch publishes a Woodlands facility at 7 Woodlands Height; Keppel lists DC1 in Woodlands. Search Sungei Kadut, Sembawang, Yishun, and Marsiling for additional enterprise / edge sites.

```text
"Woodlands" "data centre" Singapore
"Global Switch" "7 Woodlands Height"
"Keppel" "Woodlands" "data centre"
"Sungei Kadut" "data centre" Singapore
"Sembawang" OR "Yishun" OR "Marsiling" "data centre" Singapore
```

### 3.4 South East

Likely pattern: major hub. Includes Tampines Industrial Park, Changi / Loyang / Tanah Merah cable-landing corridor, Kaki Bukit, Chai Chee, Paya Lebar, Ubi, and Tai Seng. Operator evidence: AirTrunk SGP1 at Loyang; Keppel SGP 2/3/4 in Tampines; Global Switch Tai Seng; Equinix SG2/SG4 in Tai Seng from operator/aggregator cross-checks; StarHub/CMI Tai Seng entries need primary confirmation.

```text
"Tampines Industrial Park" "data centre" Singapore
"Keppel DC Singapore 2" OR "Keppel DC Singapore 3" OR "Keppel DC Singapore 4"
"Loyang" "data centre" Singapore
"AirTrunk" "SGP1" "Loyang"
"Changi North" OR "Tanah Merah" "cable landing" Singapore
"Tai Seng" "data centre" Singapore
"Global Switch" "2 Tai Seng Avenue"
"Kaki Bukit" OR "Chai Chee" OR "Ubi" "data centre" Singapore
```

### 3.5 South West

Likely pattern: Singapore's largest hyperscale / industrial DC geography. Includes Jurong East/West, International Business Park, Jalan Buroh, Tanjong Kling, Tuas, Boon Lay, Pioneer/Gul, Sunview Drive, Jalan Tukang, Clementi, West Coast, and part of Queenstown. Verified official/operator leads include Digital Realty SIN10 at 29A International Business Park, DayOne SG1 at 21 Jalan Buroh / Jurong East campus, Nxera DC Tuas, Equinix SG5 at 6 Sunview Drive, Equinix SG6 under construction, and ST Engineering Data Centre@Boon Lay.

```text
"Jurong" "data centre" Singapore
"International Business Park" "data centre" Singapore
"29A International Business Park" "Digital Realty"
"Jalan Buroh" "data centre" Singapore
"DayOne" "SG1" "Jurong East"
"Tuas" "data centre" OR "cable landing" Singapore
"Nxera" "DC Tuas" "58MW"
"Boon Lay" "data centre" "ST Engineering"
"Sunview Drive" OR "Jalan Tukang" "Equinix"
"Tanjong Kling" "data centre" Singapore
```

---

## 4. Known Official / Primary-Source Leads

These are not a complete facility registry. They are anchors to seed enumeration.

| Facility / project | Division | Status / fact supported | Evidence | Grade |
| --- | --- | --- | --- | --- |
| Pilot DC-CFA | n/a | About 80 MW selected in 2023 across AirTrunk-ByteDance, Equinix, GDS, Microsoft | IMDA 2023 selection release | A for allocation |
| DC-CFA2 | n/a | Launched 1 Dec 2025; at least 200 MW available, more possible via green-energy pathways | IMDA DC-CFA2 page / factsheet | A for programme |
| Green Data Centre Roadmap | n/a | Sustainable-growth policy and at least 300 MW additional-capacity target | IMDA roadmap | A for policy |
| AWS ap-southeast-1 | n/a | Singapore region, 3 AZs | AWS docs | A for cloud region |
| Microsoft Azure Southeast Asia | n/a | Singapore Azure region, region ID southeastasia | Microsoft Learn | A for cloud region |
| Google Cloud asia-southeast1 | n/a | Singapore cloud region | Google Cloud locations | A for cloud region |
| Oracle Cloud Singapore | n/a | OCI Singapore / ap-singapore-1 region | Oracle pages/docs | A for cloud region |
| Alibaba Cloud Singapore | n/a | Singapore / ap-southeast-1 region; 4 zones listed | Alibaba Cloud pages/docs | A for cloud region |
| Equinix SG6 | South West | 9-storey SG6, expected Q1 2027, 20 MW when fully built, pilot DC-CFA award | EDB + Equinix announcements | A |
| Equinix SG5 | South West | 6 Sunview Drive; opened 2021 | Equinix SG5 facility page | A |
| Digital Realty SIN10 | South West | 29A International Business Park facility | Digital Realty SIN10 page | A |
| Keppel DC Singapore 1 | North East, check GIS | Serangoon North Industrial Estate facility | Keppel Data Centres Singapore page | A |
| Keppel DC Singapore 2/3/4 | South East | Tampines Industrial Park facilities | Keppel Data Centres Singapore page | A |
| Keppel DC Singapore 5 | South West | Jurong facility | Keppel Data Centres Singapore page | A |
| Keppel DC DC1 | North West | Woodlands facility | Keppel Data Centres Singapore page | A |
| Keppel DC Singapore 7/8 | Division requires address/GIS | Keppel Data Centre Campus adjacent facilities; KDC SGP 7 Green Mark Platinum stated | Keppel Data Centres Singapore page | A for existence/certification |
| STT Singapore 1/2/3, Defu | North East or South East boundary check | STT pages list Defu campus; STT Singapore 1 13 MW, STT Singapore 2 12 MW; DCD confirms Defu 3 opened in 2022 | STT GDC + DCD | A/B |
| Nxera DC Tuas | South West | DC Tuas, up to 58 MW IT load, PUE/Green Mark claims, integrated with submarine cable landing station | Nxera page; Singtel opening release dated 9 Feb 2026 | A |
| DayOne SG1 | South West | Jurong East campus; 39,978 sqm GFA; 20 MW; RFS 2027; site at 21 Jalan Buroh | DayOne Singapore page; Business Times for groundbreaking | A/B |
| Global Switch Tai Seng | South East | 17 MW, 2 Tai Seng Avenue | Global Switch Singapore page | A |
| Global Switch Woodlands | North West | 22 MW, 7 Woodlands Height | Global Switch Singapore page | A |
| AirTrunk SGP1 | South East | Loyang campus open; 60+ MW design claim from AirTrunk release; address/capacity cross-checks available in aggregators | AirTrunk SGP1 and 2020 release; BT for opening | A/B/C by fact |
| ST Engineering Data Centre@Boon Lay | South West | Jalan Boon Lay fourth Singapore DC; groundbreaking 25 Jun 2024; operational target 2026; $120m capex; PUE 1.25 design | ST Engineering release; MTI speech | A |
| Changi North / Tanah Merah / Tuas cable landing sites | South East / South West | Designated submarine cable landing areas; cable counts from cable-industry sources | IMDA submarine-cable guidance; Submarine Networks | A/B |

Do not count policy targets, CFA allocations, cloud AZ counts, IXP PoPs, or submarine cable landing stations as datacenter facilities.

---

## 5. Validation Checklist

For every candidate row:
1. Confirm the source URL is live and the page actually states the claimed fact.
2. Split facts by grade: existence, address, capacity, status, certification, ownership, cloud-region existence, and division assignment may each have different grades.
3. Geocode address with OneMap / URA SPACE and record the URA planning area.
4. Assign one of the five CDC districts; mark `division_check_needed` if the site is near a constituency boundary or if only an estate-level location is available.
5. For post-2019 greenfield projects, search DC-CFA / DC-CFA2 and operator releases.
6. For facility counts, use only A/B facility evidence. Aggregator totals are lead lists only.

---

## 6. Re-check Cadence

- **Monthly:** IMDA/EDB/MDDI/MTI newsrooms; DC-CFA2 page; GeBIZ; major operator news pages.
- **Quarterly:** URA circulars and SPACE zoning checks for new addresses; BCA/IMDA Green Mark pages; EMA/SP Group energy announcements; SGX/REIT disclosures.
- **On milestones:** re-check DC-CFA2 after application close, shortlist, award, groundbreaking, and energisation announcements.
- **Semi-annually:** re-run all operator and aggregator lead queries; re-check every `division_check_needed` with GIS.
- **Annually:** refresh CDC district mapping because constituency-based boundaries can change.

---

## 7. Red Flags

- A cloud region is not a physical facility list.
- A CFA award is capacity allocation, not proof of a completed building.
- A Green Mark certificate is not proof of ownership, address, or live service unless the source states those facts.
- Singapore market reports often quote different facility totals because they mix hyperscale, colocation, edge, under-construction, and cloud sites.
- CDC boundaries do not align cleanly with URA planning areas. Always preserve the original address/planning-area evidence.
