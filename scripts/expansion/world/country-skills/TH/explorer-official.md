# TH Explorer Official - Thailand Datacenter Enumeration Methodology

Date: 2026-08-12. Scope: official, regulatory, utility, cloud, and operator-primary methods for enumerating Thailand datacenter projects across Bangkok, provinces, and Phatthaya. Reliability grades: **A** = official/primary registry, permit, utility, cloud, or operator source; **B** = strong secondary/trade/legal analysis; **C** = weak aggregate or press-only lead.

---

## 0. Thailand structure to keep in mind

- Thailand has one special metropolitan administration (**Bangkok**), 76 provinces, and **Phatthaya/Pattaya** as a special administrative city in Chon Buri. Treat Bangkok, Samut Prakan, Nonthaburi, Pathum Thani, Chon Buri, Rayong, and Chachoengsao as the highest-priority enumeration belt.
- The data-center boom is concentrated around **Bangkok metro** and the **Eastern Economic Corridor (EEC)**: Chon Buri, Rayong, and Chachoengsao. BOI releases repeatedly name Bangkok, Chachoengsao, Chonburi, Pathum Thani, Rayong, and Samut Prakan as data-center locations.
- Thailand does not appear to have one public planning-permit portal that reliably lists all private datacenter building permits. Build the census from **BOI approvals + NBTC telecom licenses + ONEP EIA records + local building-control authorities + EGAT/MEA/PEA power evidence + official cloud/colo pages**.
- Thai sources use both English and Thai terms. Search both: `data center`, `data centre`, `IDC`, `colocation`, `cloud region`, and Thai `ศูนย์ข้อมูล`, `ดาต้าเซ็นเตอร์`, `ศูนย์ดาต้า`, `คลาวด์`, `โคโลเคชั่น`, `ศูนย์บริการข้อมูล`.

---

## 1. Highest-value official sources

### 1.1 Board of Investment (BOI) - project approvals and promoted companies

- Main BOI site: https://www.boi.go.th/en/index/
- Press releases: https://www.boi.go.th/index.php?language=en&page=press_releases2
- OSOS BOI news mirror: https://osos.boi.go.th/EN/news/
- BOI promoted-company database / statistics links: https://www.boi.go.th/index.php?language=en&page=form_promoted_companies
- e-Investment Promotion system: https://boi-investment.boi.go.th/public/index_en.php

Use BOI as the first official project seed list. BOI press releases name specific project companies, provinces, investment value, and sometimes **IT load MW**. Examples already visible in official BOI/OSOS releases:

- 2025 board approval: three projects in Bangkok, Chonburi, and Rayong totaling 90.9 billion baht and almost 350 MW IT load, including Beijing Haoyang Cloud Data Technology in WHA Eastern Seaboard Industrial Estate 4, Rayong; Empyrion Digital in Bangkok; GSA Data Center 02 in Chonburi. URL: https://osos.boi.go.th/EN/news/2187/Thailand-BOI-Approves-200-Billion-Baht-Investments-in-Rail-a/
- 2025 BOI approval wave: Digital Edge DC (Thailand) in Chonburi at about 96 MW; Galaxy Peak Data Center in Rayong at about 160 MW. URL: https://osos.boi.go.th/EN/news/2205/Thailand-BOI-Approves-Higher-Tech-HRD-Requirements-for-Data/
- 2026 first board meeting: seven data center/data hosting projects; BOI says 2025 applications included 36 data center projects worth THB 728 billion across Bangkok, Chachoengsao, Chonburi, Pathum Thani, Rayong, and Samut Prakan. URL: https://www.boi.go.th/index.php?_module=news&from_page=press_releases2&language=en&page=press_releases_detail&topic_id=138444
- 2026 approval wave: Skyline Data Center and Cloud Services in Chachoengsao at 200 MW, Bridge Data Centres IIO in Chonburi at 134 MW, plus large TikTok/System data-hosting investment. URL: https://osos.boi.go.th/EN/news/2386/Thailand-Approves-29-Billion-Investment-Wave-as-Data-Center/

BOI query templates:

```text
site:boi.go.th "data center" "IT load" Thailand
site:osos.boi.go.th "data center" "IT load" "Chonburi"
site:boi.go.th "data hosting" "Thailand" "MW"
site:boi.go.th "ศูนย์ข้อมูล" "เมกะวัตต์"
site:osos.boi.go.th "Data Center" "Rayong" "BOI"
```

Grade: **A** for approval, applicant, province, investment, and stated IT load. Caveat: BOI approval is not proof of construction or operation; cross-check with permits, utility readiness, operator announcements, and imagery.

### 1.2 NBTC telecom licensing - operator census

- NBTC home: https://www.nbtc.go.th/Home.aspx?lang=en-us
- Telecom-license search: https://searchtelecomlicense.nbtc.go.th/
- Telecom license portal: https://telecom-license.nbtc.go.th/
- Telecommunications Business Act English PDF: https://www.nbtc.go.th/getattachment//law/law_noti/%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A8-%281%29/TELECOMMUNICATIONS-BUSINESS-ACT-B-E-2544-%282001%29/%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A8%E0%B8%AF.pdf?lang=th-TH
- NBTC licensing criteria PDF: https://telecom-license.nbtc.go.th/getattachment/Information/Criteria-and-procedure/C-Pfortelelicense/Criteriaprocedurefortelelicense.pdf.aspx
- NBTC nature/categories PDF: https://telecom-license.nbtc.go.th/getattachment/Information/Criteria-and-procedure/C-Pfortelelicense/NatureandCatagoriesoftelelicense.pdf.aspx

NBTC is the best official **operator** census. The telecom-license search exposes company name, registration number, license type, authorized service, license number, and old license number. Search authorized-service strings for `Data Center`, `Colocation`, `Hosting`, `Cloud`, and Thai service wording. NBTC quarterly reports have historically counted data-center licensees and services; query PDFs for `Data Center (Colocation, Web/Mail server, etc.)`.

NBTC query templates:

```text
site:nbtc.go.th "Data Center" "ใบอนุญาต"
site:telecom-license.nbtc.go.th "Data Center" "Colocation"
site:nbtc.go.th "รายงานการอนุญาต" "Data Center"
"searchtelecomlicense.nbtc.go.th" "Data Center"
```

Grade: **A** for license existence and legal operating authority. Caveat: this is not facility-level; one licensee may run multiple sites, and license scope/status must be joined to BOI/local permit/operator evidence.

### 1.3 Planning and construction permits

- BOI OSOS construction-permit guide: https://osos.boi.go.th/en/how-to/139/Dealing-with-Construction-Permits/
- Bangkok Metropolitan Administration (BMA): https://www.bangkok.go.th/ and district portals under `webportal.bangkok.go.th`
- Bangkok building-inspection dashboard/open contracting entry point: https://opencontract.bangkok.go.th/bkkbuilding.html
- Department of Public Works and Town & Country Planning (DPT): https://www.dpt.go.th/

The practical rule from OSOS: Bangkok building permits are handled through Bangkok authorities; outside Bangkok, contact the local Sub-district Administration Office / municipality / local building-control authority. For enumeration, do not expect a complete national online permit search. Instead:

1. Start with BOI/NBTC/operator leads.
2. For each site province and district, search the local authority site for building-control terms and the company/project name.
3. Search industrial estate and EEC authority pages when the site is inside an estate.
4. Use local permit hits as status evidence only when they identify project, land plot, building type, or owner.

Thai planning/building query terms:

```text
"{company}" "{province}" "ขออนุญาตก่อสร้าง"
"{project}" "ใบอนุญาตก่อสร้าง"
"{province}" "ดาต้าเซ็นเตอร์" "ก่อสร้าง"
"{district}" "ศูนย์ข้อมูล" "อาคาร"
site:bangkok.go.th "data center" "building permit"
site:webportal.bangkok.go.th "ดาต้าเซ็นเตอร์"
site:dpt.go.th "ศูนย์ข้อมูล" "ก่อสร้าง"
```

Grade: **A** when from BMA/local government/DPT/industrial-estate authority. Grade **C** for consultant summaries of Thai permit process unless they point to the primary issuing authority.

### 1.4 Environmental review - ONEP Smart EIA Plus

- ONEP Smart EIA Plus: https://eia.onep.go.th/
- EIA list/search page: https://eia.onep.go.th/site/eia
- ONEP EIA division: https://eiathailand.onep.go.th/
- EIA manuals/FAQ: https://eiathailand.onep.go.th/faq.aspx

Use ONEP to search IEE/EIA/EHIA records and monitor submissions. Data centers may appear under building, energy, industrial-estate, backup-generation, or infrastructure categories rather than a clean `data center` category. Search by applicant SPV, industrial estate, district, and Thai/English project name. EIA records can reveal project stage, land parcel, generator/cooling/water details, and sometimes total power.

ONEP query terms:

```text
ดาต้าเซ็นเตอร์
ศูนย์ข้อมูล
Data Center
ศูนย์บริการข้อมูล
คลาวด์
Colocation
ชื่อบริษัท / company name
ชื่อเขตนิคมอุตสาหกรรม / industrial estate name
```

Grade: **A** for project existence, location, and environmental status. Caveat: absence from ONEP is not proof of no project; applicability depends on project characteristics and related infrastructure.

### 1.5 Power and utility evidence - EGAT, MEA, PEA, ERC

- EGAT: https://www.egat.co.th/home/en/
- EGAT data-center grid readiness release, 2026-02-16: https://www.egat.co.th/home/en/20260216e/
- EGAT data-center hub power release, 2026-06-16: https://www.egat.co.th/home/en/20260616e/
- PEA English site: https://www.pea.co.th/en
- PEA service area: https://www.pea.co.th/en/about-pea/pea-service
- PEA tariff/services: https://www.pea.co.th/en/our-services/tariff
- Metropolitan Electricity Authority (Bangkok/Nonthaburi/Samut Prakan): https://www.mea.or.th/
- Energy Regulatory Commission: https://www.erc.or.th/

Utility boundary matters:

- **MEA** covers Bangkok, Nonthaburi, and Samut Prakan.
- **PEA** distributes electricity in 74 provinces outside Bangkok/Nonthaburi/Samut Prakan.
- **EGAT** owns/operates generation and transmission; its releases are useful for transmission/substation readiness, especially in EEC areas.

Use power evidence to verify large BOI claims and identify under-construction clusters. EGAT said in 2026 it was strengthening the EEC grid to support data-center investment and referenced data-center-related transmission upgrades. PEA pages give service territory and commercial/industrial context; PEA/MEA local notices may mention high-voltage connection, substation work, outages, or transformer upgrades.

Power query templates:

```text
site:egat.co.th "data center" Thailand
site:egat.co.th "ดาต้าเซ็นเตอร์" "สถานีไฟฟ้า"
site:pea.co.th "data center" "Chonburi"
site:pea.co.th "ดาต้าเซ็นเตอร์" "ไฟฟ้า"
site:mea.or.th "data center" "Samut Prakan"
site:erc.or.th "data center" "direct PPA"
```

Grade: **A** for utility statements, grid interconnection, tariff, or substation evidence. Caveat: utility readiness does not name every customer; use it mainly to validate province-level feasibility and very large MW claims.

---

## 2. Official cloud-region and hyperscaler seeds

Cloud region pages are **A** for existence, city/country, region code, and status. They do not disclose exact sites or MW; use them as anchors and then cross-check against BOI/operator/local records.

| Provider | Official source | Thailand signal |
|---|---|---|
| AWS | https://aws.amazon.com/blogs/aws/announcing-the-new-aws-asia-pacific-thailand-region/ and https://aws.amazon.com/local/thailand/ | AWS Asia Pacific (Thailand) Region launched 2025-01-07 with three Availability Zones, API name `ap-southeast-7`; AWS says data centers are located in Thailand and long-term investment exceeds US$5B. |
| Google Cloud | https://cloud.google.com/blog/products/infrastructure/google-cloud-launches-new-region-in-bangkok-thailand and https://docs.cloud.google.com/compute/docs/regions-zones | Bangkok region `asia-southeast3` launched 2026-01-21 with three zones; Compute docs list Bangkok, Thailand zones. |
| Microsoft Azure | https://news.microsoft.com/apac/2024/05/01/microsoft-announces-significant-commitments-to-enable-a-cloud-and-ai-powered-future-for-thailand/ and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | Microsoft announced intent to establish a Thailand datacenter region; Azure geography page lists **Thailand South** as planned/intent. |
| Oracle/AIS | https://www.oracle.com/news/announcement/advanced-info-service-selects-oracle-alloy-to-build-thailands-first-locally-owned-and-operated-hyperscale-cloud-2024-08-01/ and https://www.ais.th/en/business/enterprise/technology-and-solution/cloud-and-data-center/ais-cloud/overview | AIS selected Oracle Alloy to launch locally operated hyperscale cloud; AIS page markets AIS Cloud + OCI with local Thailand data centers. |
| Alibaba/Tencent/Huawei | Use official global region docs and Thai operator pages; verify with BOI/NBTC | Useful secondary cloud seeds, but record only where the official region page identifies Bangkok/Thailand. |

Cloud query templates:

```text
"Thailand" "cloud region" site:aws.amazon.com
"asia-southeast3" "Bangkok" site:cloud.google.com
"Thailand South" site:azure.microsoft.com
"Thailand South" site:learn.microsoft.com azure
"AIS Cloud" "Oracle Alloy" site:oracle.com OR site:ais.th
```

---

## 3. Official/primary colocation and telecom-operator seeds

Use these pages for facility names, province/city, status hints, capacity where disclosed, and operator aliases to search in BOI/NBTC/ONEP/local portals.

| Operator | Official source | Enumeration notes |
|---|---|---|
| True IDC | https://www.trueidc.com/en/ and https://www.trueidc.com/en/about | Official page lists East Bangna, Midtown Ratchada, Midtown Pattanakarn, North Muangthong and claims 150+ MW national power capacity. Search True IDC news for new AI/hyperscale groundbreaking. |
| AIS / GSA | https://www.ais.th/en/business/enterprise/technology-and-solution/cloud-and-data-center/ais-data-center/ais-data-center and GSA announcement https://www.ais.th/en/business/news-and-activity/announcements/gulf_Singtel_and_ais_kick_off_the_establishment_of_the_new_data_center | AIS page lists AIS data-center locations including GSA Samut Prakan and regional sites; GULF/Singtel/AIS GSA release gives 20+ MW construction start. |
| NT / CAT / TOT successor | https://www.ntdatacenter.net/locations/ and https://www.ntplc.co.th/en/enterprise/products-and-services/digital/idc-cloud | NT Data Center official page lists 9 data centers across 8 provinces: Bangrak, Nonthaburi 1/2, Sriracha, Phra Khanong, Chiang Mai, Khon Kaen, Hat Yai, with MW/rack details for some. |
| STT GDC Thailand | https://www.sttelemediagdc.com/th-en/locations and https://www.sttelemediagdc.com/th-en/locations/bangkok | Official Thailand location page lists 3 Bangkok data centers and 49 MW IT load; Bangkok page details Hua Mak/STT Bangkok campus. |
| Equinix | https://newsroom.equinix.com/2024-10-27-Equinix-Intends-to-Invest-Approximately-500-Million-to-Bring-Future-Proof-Digital-Infrastructure-to-Thailand | Equinix announced planned Thailand entry, about US$500M phased investment and Bangkok land acquisition. Treat as planned until official IBX page/permit/BOI evidence confirms facility status. |
| CtrlS / NT | NT official collaboration release: https://www.ntplc.co.th/en/news/update-news/news29 | NT says CtrlS is building a Chonburi hyperscale data center on 10 acres / 25 rai with design capacity up to 150 MW and NT as connectivity partner. |

Operator query templates:

```text
site:trueidc.com "data center" "Bangna"
site:trueidc.com "7th Data Center" "groundbreaking"
site:ais.th "GSA DATA CENTER" "Samut Prakan"
site:ais.th "AIS Data Center" "Khon Kaen" OR "Chiang Mai"
site:ntdatacenter.net "NT Data Center" "MW"
site:sttelemediagdc.com/th-en "Bangkok" "IT load"
site:newsroom.equinix.com "Thailand" "Bangkok" "data center"
site:ntplc.co.th "CtrlS" "Chonburi" "150 MW"
```

Grade: **A** for official operator-listed facilities and status; **B** for marketing capacity claims unless supported by BOI/permit/utility evidence.

---

## 4. Division-by-division enumeration strategy

### 4.1 Tier 1: Bangkok metro

Divisions: Bangkok, Samut Prakan, Nonthaburi, Pathum Thani.

Workflow:

1. Pull BOI approvals mentioning Bangkok, Samut Prakan, Nonthaburi, Pathum Thani, Nava Nakorn, Bang Na, Ratchada, Muang Thong, and Phra Khanong.
2. Search NBTC license registry for True IDC, AIS, GSA Data Center, NT, Telehouse, Empyrion, DAMAC/Edgnex/NextGen/Skyline, Bridge, and local SPVs.
3. For Bangkok, search BMA/district web portals; for Samut Prakan/Nonthaburi/Pathum Thani, search province/municipality/subdistrict pages and MEA or PEA depending on utility territory.
4. Search ONEP by company and Thai project name.
5. Verify with official operator pages: True IDC, AIS/GSA, NT, STT GDC, Equinix, Telehouse/KDDI if official Thailand page appears.

High-yield local terms:

```text
กรุงเทพมหานคร ดาต้าเซ็นเตอร์
สมุทรปราการ ศูนย์ข้อมูล
นนทบุรี data center
ปทุมธานี Data Center Nava Nakorn
บางนา ดาต้าเซ็นเตอร์
รัชดา ศูนย์ข้อมูล
```

### 4.2 Tier 2: EEC and eastern corridor

Divisions: Chon Buri, Rayong, Chachoengsao, plus nearby Prachin Buri/Nakhon Nayok/Sa Kaeo/Chanthaburi/Trat as lower-priority spillover checks.

Workflow:

1. BOI search by province and industrial estate names: Amata City Chonburi, WHA Eastern Seaboard Industrial Estate 4, EEC, Sriracha, Chachoengsao.
2. Search EEC Office and industrial-estate/developer sites for project pages and land-allocation announcements.
3. Search EGAT/PEA for substation/transmission upgrades, because EEC projects can be 100-300+ MW.
4. Search ONEP by estate/project/SPV.
5. Cross-check official operator leads: NT Sriracha, CtrlS Chonburi, BOI-approved Digital Edge, Galaxy Peak, Haoyang, Bridge Data Centres, Skyline/DAMAC, Google/AWS-related BOI records where public.

Queries:

```text
"Chonburi" "data center" "IT load" site:boi.go.th OR site:osos.boi.go.th
"Rayong" "data center" "WHA Eastern Seaboard Industrial Estate 4"
"Chachoengsao" "data center" "200 megawatts"
"ชลบุรี" "ดาต้าเซ็นเตอร์" "เมกะวัตต์"
"ระยอง" "ศูนย์ข้อมูล" "นิคม"
"ฉะเชิงเทรา" "data hosting"
site:egat.co.th "EEC" "data center"
```

### 4.3 Tier 3: Regional edge and state/telco facilities

Divisions with known official or strong leads include Chiang Mai, Khon Kaen, Phuket, Songkhla/Hat Yai, and possibly Nakhon Ratchasima.

Workflow:

1. Start with NT official locations and AIS official data-center page.
2. Search NBTC for regional operators and local hosting/ISP names.
3. Search provincial pages and ONEP by Thai terms; these are often small edge/telco/server-room facilities with no MW.
4. Use trade/aggregate sources only to suggest names, then require operator/NBTC/local confirmation.

Queries:

```text
"เชียงใหม่" "ศูนย์ข้อมูล" "AIS" OR "NT"
"ขอนแก่น" "Data Center" "AIS" OR "NT"
"ภูเก็ต" "data center" "ใบอนุญาต"
"หาดใหญ่" "NT Data Center"
"นครราชสีมา" "ดาต้าเซ็นเตอร์"
```

### 4.4 Remaining provinces

For all other provinces, use a quick negative-evidence sweep:

1. BOI province + `data center` / `data hosting`.
2. NBTC license search for province-name operators if any.
3. ONEP Thai/English keyword search.
4. PEA/province/local authority search for `ดาต้าเซ็นเตอร์`, `ศูนย์ข้อมูล`, and `cloud`.
5. Record `no_projects` only after no BOI/NBTC/ONEP/operator/local hits are found and no industrial-estate lead is active.

---

## 5. Reliability grading and status rules

Grade each **data point**, not just each project:

| Source | Grade | Use |
|---|---|---|
| BOI approval release / promoted-company database | A | Project company, province, investment, stated IT load, approval date. |
| NBTC telecom-license registry | A | Operator authority, license type/service, legal entity alias. |
| ONEP Smart EIA Plus | A | Project existence, environmental status, location, technical details. |
| BMA/province/municipality/DPT/industrial-estate permits | A | Building/control status, plot, owner, construction status. |
| EGAT/MEA/PEA/ERC official records | A | Grid readiness, service area, power connection, tariff/interconnection context. |
| Official cloud-region pages | A for existence/status; no grade for MW | Region code, launch/planned status, country/city. |
| Operator official pages/news | A for existence/location/status; B for marketing capacity | Facility list, product status, design capacity where disclosed. |
| Legal firm/regulatory analysis | B | Interpret NBTC/BOI rule changes, but verify rules on official sources. |
| DatacenterDynamics, Capacity, W.Media, Baxtel, Data Center Map | B/C | Discovery leads and cross-checks; not final evidence without primary confirmation. |
| LinkedIn/social posts/aggregators | C | Lead only. |

Status rules:

- **Approved**: BOI approval or official license/project approval, no construction evidence.
- **Construction**: official groundbreaking, building permit, utility construction, operator construction update, or credible EIA/construction filing.
- **Operational**: official launch, cloud GA, operator facility page accepting service, certification/incident report naming active site, or utility/customer-service evidence.
- **Planned/announced**: corporate intent, land acquisition, MOU, or market-entry announcement only.

Avoid double counting:

- Match by ultimate parent + Thai SPV + campus/industrial estate + province.
- Hyperscaler regions may use several undisclosed AZ facilities; count the cloud region as a cloud-infrastructure record, not as three separate physical datacenters unless individual sites are independently named.
- BOI data-hosting projects may cover server installation across multiple provinces; split only when official province-level sites are named.

Capacity sanity checks:

- Prefer BOI-stated **IT load MW** over marketing "power capacity" unless the operator defines it.
- For utility/grid releases, distinguish transmission support capacity from committed IT load.
- Treat 100+ MW EEC projects as approved/design-scale until building, EIA, or power-connection evidence shows phase status.

---

## 6. Recommended official-first pipeline

1. **BOI sweep**: scrape/search BOI and OSOS for `data center`, `data hosting`, `IT load`, `MW`, and Thai equivalents; create project seeds with SPV, province, investment, IT load, date.
2. **NBTC operator sweep**: search `searchtelecomlicense.nbtc.go.th` for every SPV/operator and service keyword; add license records and aliases.
3. **Operator/cloud sweep**: collect official facility/region pages for AWS, Google Cloud, Azure, Oracle/AIS, True IDC, AIS/GSA, NT, STT GDC, Equinix, CtrlS/NT.
4. **Permit/EIA sweep**: for each seed, search ONEP Smart EIA Plus, BMA/local authority/DPT, industrial-estate pages, and EEC pages.
5. **Power validation**: check EGAT/MEA/PEA/ERC for the province/site and use utility territory to test feasibility of large MW claims.
6. **Province negative sweep**: for low-signal provinces, run Thai + English province queries across BOI, NBTC, ONEP, PEA/local sites before marking no projects.
7. **Evidence grading**: assign grade per field; never promote a press-only planned project above C/B unless official evidence confirms it.

---

## 7. Quick source index

- BOI: https://www.boi.go.th/en/index/
- BOI press releases: https://www.boi.go.th/index.php?language=en&page=press_releases2
- OSOS BOI news: https://osos.boi.go.th/EN/news/
- BOI promoted companies/statistics: https://www.boi.go.th/index.php?language=en&page=form_promoted_companies
- NBTC license search: https://searchtelecomlicense.nbtc.go.th/
- NBTC telecom-license portal: https://telecom-license.nbtc.go.th/
- ONEP Smart EIA Plus: https://eia.onep.go.th/
- ONEP EIA division: https://eiathailand.onep.go.th/
- OSOS construction permits: https://osos.boi.go.th/en/how-to/139/Dealing-with-Construction-Permits/
- DPT: https://www.dpt.go.th/
- BMA: https://www.bangkok.go.th/
- EGAT: https://www.egat.co.th/home/en/
- MEA: https://www.mea.or.th/
- PEA: https://www.pea.co.th/en
- ERC: https://www.erc.or.th/
- AWS Thailand: https://aws.amazon.com/local/thailand/
- Google Cloud locations: https://cloud.google.com/about/locations
- Google Compute regions/zones: https://docs.cloud.google.com/compute/docs/regions-zones
- Azure global infrastructure/geographies: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies
- Oracle Alloy / AIS: https://www.oracle.com/news/announcement/advanced-info-service-selects-oracle-alloy-to-build-thailands-first-locally-owned-and-operated-hyperscale-cloud-2024-08-01/
- True IDC: https://www.trueidc.com/en/
- AIS Data Center: https://www.ais.th/en/business/enterprise/technology-and-solution/cloud-and-data-center/ais-data-center/ais-data-center
- AIS Cloud: https://www.ais.th/en/business/enterprise/technology-and-solution/cloud-and-data-center/ais-cloud/overview
- NT Data Center: https://www.ntdatacenter.net/locations/
- NT IDC/cloud: https://www.ntplc.co.th/en/enterprise/products-and-services/digital/idc-cloud
- STT GDC Thailand: https://www.sttelemediagdc.com/th-en/locations
- Equinix Thailand announcement: https://newsroom.equinix.com/2024-10-27-Equinix-Intends-to-Invest-Approximately-500-Million-to-Bring-Future-Proof-Digital-Infrastructure-to-Thailand
