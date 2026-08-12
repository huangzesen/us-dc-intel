# BH Explorer Official - Bahrain Datacenter Enumeration via Official, Regulatory, Utility, and Planning Sources

Date: 2026-08-12. Scope: Kingdom of Bahrain (BH). Subnational type: **governorate**. Required repo divisions from `world-manifest.jsonl`: **Capital Governorate; Southern Governorate; Muharraq Governorate; Northern Governorate**.

Reliability grades: **A** = primary official/operator/regulator/utility/certifier source for the exact fact cited; **B** = strong trade press, contractor, or recognized local media with named facts; **C** = directory, market-report, social, or unattributed lead; **U** = unresolved. Grade the fact, not the publisher: an official AWS page is A for `me-south-1`, but not for a street address AWS does not publish.

---

## 0. Bahrain-specific operating model

- Bahrain is small and centralized: four governorates, one national electricity and water utility (**EWA**), one telecom regulator (**TRA**), and a national building-permit workflow through **Benayat/MOMAA**. There is no public national datacenter registry and no public searchable datacenter-permit register.
- Use official sources to prove authority routing, land-use context, utility/regulatory context, and operator/government claims. Use trade/directories only to discover leads and then validate them here.
- Confirm every candidate against the four repo divisions. The corrected division anchors are:
  - **Capital Governorate**: Manama, Al Seef/Seef District, Bahrain Bay, Diplomatic Area, Juffair, Hoora, Salmaniya, Umm Al Hassam.
  - **Southern Governorate**: Riffa, Awali, Askar, Zallaq, Al Dur, Salman Industrial City/US Trade Zone corridor, Beyon Data Oasis/White Space DC where the operator says southern Bahrain.
  - **Muharraq Governorate**: Muharraq, Hidd, Arad, Busaiteen, Bahrain International Airport, Amwaj Islands, Bahrain Logistics Zone / port-adjacent leads.
  - **Northern Governorate**: Hamala, Saar, Budaiya, Diraz, Barbar, Hamad Town and nearby residential/suburban leads. Batelco's current official DC page gives **Building 1095, Road 1425, Block 1014, Hamala Bahrain**, so that record belongs in Northern unless a separate site is proven.
- Keep infrastructure classes separate. Do not count cloud regions, IXPs, cable landing stations, power plants, enterprise hosting services, or MoUs as physical datacenters without separate facility evidence.
- Use both English and Arabic: `data center`, `data centre`, `datacenter`, `مركز بيانات`, `مراكز البيانات`, `تصريح بناء`, `رخصة بناء`, `بنات`, `هيئة الكهرباء والماء`, `هيئة تنظيم الاتصالات`, `الحوسبة السحابية`, `السحابة الحكومية`.

---

## 1. Planning, permitting, and land-use sources

### 1.1 Benayat / MOMAA building-permit route

- **Benayat Building Permit Portal**: https://www.mun.gov.bh/newportal/en/municipal-affairs/projects/building-permit-portal-benayat-0 . Verified official description: Benayat is Bahrain's official system for issuing building permits for all building-project types. Use this as A-grade evidence for permit routing, not as a public project registry.
- **Benayat public site**: https://www.benayat.bh/ and building-permit services https://www.benayat.bh/building-permits/ . Verified as the current service surface; the public portal does not expose a full searchable permit database.
- **National portal construction/urban planning**: https://www.bahrain.bh/ . Search for Benayat/building services when MOMAA URLs move.

Queries:

```text
site:mun.gov.bh "data center" OR "data centre" OR datacenter OR "مركز بيانات"
site:benayat.bh "data center" OR "data centre" OR "مركز بيانات"
site:benayat.bh "building permit" "industrial"
"Benayat" "data center" Bahrain
"Bahrain" "building permit" "data center"
"البحرين" "تصريح بناء" "مركز بيانات"
```

### 1.2 UPDA land-use and planning checks

- **UPDA Construction Regulations Simulator**: https://upda.gov.bh/WebsiteEService/en/building-regulation . Verified official tool for land-use/building-regulation checks.
- **Planning approval route**: https://planning.bh/en/planning_approval.html . Use for parcel suitability, permitted use, parking, and planning conditions; applications are routed through approved engineering offices.

Queries:

```text
site:upda.gov.bh "data center" OR "data centre" OR "مركز بيانات"
site:planning.bh "data center" OR "data centre" OR "industrial"
"Urban Planning and Development Authority" Bahrain "data center"
"Bahrain" "National Detail Land Use Plan" "industrial" "data"
```

### 1.3 Commercial registration and industrial land

- **Sijilat / Commercial Registration**: https://www.sijilat.bh/ and public CR search https://www.sijilat.bh/public-search-cr/search-cr-2.aspx . Verified official MOIC commercial-registration portal. A-grade for entity existence and registered details; not a facility proof by itself.
- **MOIC Bahrain International Investment Park (BIIP)**: https://www.moic.gov.bh/en/node/2751 and official BIIP site https://www.biip.com.bh/ . Verified official investment-park surfaces. BIIP is relevant for industrial/ICT land leads; do not infer a datacenter tenant unless tenant/project evidence exists.
- **BIIP location ambiguity**: official and secondary material describe BIIP as part of Salman Industrial City and/or near Hidd/port/airport. For division assignment, record the source's exact place string and verify parcel location through UPDA/MOMAA before choosing Southern vs Muharraq.

Queries:

```text
site:sijilat.bh "data center" OR "مركز بيانات" OR "cloud"
site:moic.gov.bh "data center" OR "digital infrastructure" OR "Salman Industrial City" OR "BIIP"
site:biip.com.bh "data center" OR "ICT" OR "cloud" OR "investor"
"BIIP" "data center" Bahrain
"Salman Industrial City" "data center" OR "digital infrastructure"
"Bahrain Logistics Zone" "data center" OR "ICT"
```

---

## 2. Utility, procurement, and energy evidence

### 2.1 EWA and Tender Board

- **EWA official site**: https://www.ewa.bh/ . Use for electricity/water authority context, service rules, annual/statistical reporting, and tender links.
- **EWA tenders page**: https://www.ewa.bh/en/tenders . Verified current EWA tender surface; active documents may require request by email.
- **Bahrain Tender Board**: https://www.tenderboard.gov.bh/ . Verified official procurement portal. Search EWA, ICT, BIX, substation, fiber, and facility-management tenders. Tenders are A-grade for the procurement fact and B/A for project details depending on specificity.

Queries:

```text
site:ewa.bh "data center" OR "data centre" OR "مركز بيانات"
site:ewa.bh "substation" OR "محطة تحويل" OR "large load"
site:tenderboard.gov.bh "data center" OR "data centre" OR "مركز بيانات"
site:tenderboard.gov.bh EWA substation ICT BIX
"EWA" Bahrain "data center" "substation"
"هيئة الكهرباء والماء" "مركز بيانات"
```

Energy rules:

- Record grid import (`MVA`/`MW`), IT load (`MW`), generator capacity, and solar/PV (`MWp`) as separate fields.
- Do not count power plants such as Al Dur as datacenters. Use them only for grid/geography context.
- For Beyon White Space/Data Oasis, official Beyon material says the facility is connected to the company's Solar Park; record renewable-supply evidence separately from IT capacity.

---

## 3. Telecom, cloud, government, and data-policy sources

### 3.1 TRA and telecom licensing

- **TRA official site**: https://www.tra.org.bh/en/ . Verified current regulator surface.
- **Licence applications**: https://www.tra.org.bh/en/category/applying-for-available-licences . Verified licence route.
- **Licensees**: https://www.tra.org.bh/en/category/licensees . Use to verify telecom operators behind datacenter/connectivity claims.
- **eTRA portal**: https://etra.tra.org.bh/ . Use for licence-management context.

Queries:

```text
site:tra.org.bh "data center" OR "data centre" OR "cloud" OR "مركز بيانات"
site:tra.org.bh "licence" "international connectivity" OR "cable landing"
site:tra.org.bh "licensees" Batelco OR stc OR Zain OR Kalaam
"هيئة تنظيم الاتصالات" "مركز بيانات"
```

### 3.2 iGA government cloud and government data centers

- **iGA official site**: https://www.iga.gov.bh/en/ . A-grade source for government digital-infrastructure programs.
- **Operations and Governance page**: https://www.iga.gov.bh/en/article/operations-and-governance . Verified statement that iGA manages and develops the government data center and provides IT infrastructure services. A-grade for government DC program existence; physical address is not public.
- **Cloud strategy / AWS migration statement**: https://www.iga.gov.bh/en/article/85-of-government-data-transfer-to-amazon-more-than-300-sites-connected-to-the-government-data-network . A-grade for public-sector cloud migration context.
- **Projects & Initiatives**: https://www.iga.gov.bh/en/category/projects-and-initiatives . Use for current cloud-first and government network leads.

Queries:

```text
site:iga.gov.bh "data center" OR "data centre" OR "government data center" OR "مركز بيانات"
site:iga.gov.bh "cloud" OR "cloud first" OR "Amazon"
"iGA" Bahrain "data center" "government"
"هيئة المعلومات والحكومة الإلكترونية" "مركز بيانات"
```

### 3.3 EDB, official media, and sovereign cloud

- **Bahrain EDB**: https://www.bahrainedb.com/ . A/B for investment announcements and sector strategy; use as lead/context, then confirm facility status elsewhere.
- **BNA**: https://www.bna.bh/ . Official news feed; search English and Arabic for `data centre`, `cloud`, `Beyon`, `Tencent`, `AWS`, `Oracle`.
- **Beyon Solutions + iGA + Oracle Sovereign HyperCloud**: official Beyon announcement https://beyon.com/2025/11/02/beyon-solutions-and-the-information-egovernment-authority-sign-agreement-to-launch-kingdom-of-bahrains-first-sovereign-hypercloud/ . A-grade for the agreement and locally operated Bahrain data-sovereignty claim; U until the physical site and operating facility are tied to a named DC.

Queries:

```text
site:bahrainedb.com "data center" OR "data centre" OR "cloud" OR "ICT"
site:bna.bh "data centre" OR "data center" OR "مركز بيانات" OR "cloud"
site:beyon.com "Sovereign HyperCloud" OR "Oracle Alloy" OR "data centre"
"Bahrain" "sovereign cloud" "Beyon Solutions" "Oracle"
```

### 3.4 Cloud-provider official checks

| Provider | Official source | Bahrain status and use |
|---|---|---|
| AWS | Launch blog https://aws.amazon.com/blogs/aws/now-open-aws-middle-east-bahrain/ ; regions docs https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html ; health dashboard https://health.aws.amazon.com/health/status | A for **Middle East (Bahrain) `me-south-1`**, opened 2019-07-30 with 3 AZs. AWS does not publish site addresses. Use AWS Health Dashboard as current A-grade operational-status source; 2026 incident reporting is B unless directly from AWS Health. |
| Microsoft Azure | Regions list https://learn.microsoft.com/en-us/azure/reliability/regions-list and Microsoft Saudi announcement https://news.microsoft.com/source/emea/2026/02/microsoft-confirms-saudi-arabia-datacenter-region-available-for-customers-to-run-cloud-workloads-from-q4-2026/ | No Bahrain Azure region. Saudi Arabia East is announced for Q4 2026; do not create Bahrain records from Azure claims. |
| Google Cloud | Locations https://cloud.google.com/about/locations ; Doha launch https://cloud.google.com/blog/products/infrastructure/new-google-cloud-region-now-open-in-qatar | No Bahrain GCP region. Doha `me-central1` is regional context only. |
| Oracle OCI | Public regions https://www.oracle.com/cloud/public-cloud-regions/ | No public OCI Bahrain region in the standard list. Bahrain sovereign service is via Beyon Solutions/Oracle Alloy; verify physical footprint separately. |
| Tencent Cloud | Tencent official 2021 expansion note https://www.tencent.com/en-us/articles/2201165.html and regions docs https://www.tencentcloud.com/document/product/213/6091 | A/B for Tencent's announcement that its first Bahrain IDC was planned by end-2021; U for current operational physical facility until visible in official region/IDC pages or another primary source. |
| Huawei / Alibaba | Official cloud region/location pages | No verified Bahrain public cloud region in reviewed official sources. Treat Bahrain claims as C/U until a primary page is found. |

Cloud queries:

```text
"AWS" "me-south-1" Bahrain "data center" OR "facility" OR "site"
"Amazon Data Services" Bahrain permit EWA substation lease
"Tencent Cloud" Bahrain IDC operational official
"Oracle Alloy" "Beyon Solutions" "local data centres" Bahrain
"Microsoft" Bahrain "data center" -UAE -Saudi
"Google Cloud" Bahrain "region" -Doha
```

---

## 4. Division-by-division official workflow

### 4.1 Capital Governorate

Likely official leads: iGA government data-center program in Manama/government campus context, Kalaam Al Seef DC operator claim, Manama enterprise hosting/cloud offices, BIX/CLS infrastructure context. Do **not** place Batelco's current Tier III page here unless a separate Manama facility page appears; the verified current Batelco DC address is Hamala.

```text
"Manama" "data center" OR "data centre" OR "مركز بيانات"
"Al Seef" OR "Seef District" "data centre" OR "مركز بيانات"
site:iga.gov.bh "data center" "Manama"
site:mun.gov.bh "Capital Governorate" "data center"
site:upda.gov.bh "Manama" "data center" OR "industrial"
```

### 4.2 Southern Governorate

Official anchor: **Beyon White Space Data Centre / Data Oasis**, commissioned 2025-11-02, 6,000 sqm within a 140,000 sqm Data Oasis site in southern Bahrain. A-grade source: https://beyon.com/2025/11/02/batelco-by-beyon-announces-commissioning-of-bahrains-first-white-space-data-centre-during-gateway-gulf-2025/ . Watch Salman Industrial City, Askar, Riffa, and US Trade Zone for land/power expansions.

```text
"Beyon" "Data Oasis" "southern Bahrain" "data centre"
"White Space Data Centre" Bahrain
"Salman Industrial City" "data center" OR "digital infrastructure"
"Askar" OR "Riffa" "data centre" OR "مركز بيانات"
site:mun.gov.bh "Southern Governorate" "data center"
```

### 4.3 Muharraq Governorate

Primary official lead areas: Hidd, Bahrain Logistics Zone, Khalifa Bin Salman Port, BIIP/industrial-park claims, airport/port connectivity. Expect many negative results; log searched terms rather than padding.

```text
"Hidd" OR "الحد" "data centre" OR "مركز بيانات"
"Bahrain Logistics Zone" "data center" OR "ICT"
"Khalifa Bin Salman Port" "data center" OR "cable" OR "ICT"
"BIIP" "Hidd" "data centre"
site:mun.gov.bh "Muharraq" "data center"
```

### 4.4 Northern Governorate

Official anchor: **Batelco by Beyon data center**, current official page says Hamala address and Tier III claim: https://www.batelco.com/business/data-center/ . Additional C-grade AWS Hamala/Saar leads must remain unconfirmed unless AWS/operator/permit evidence emerges.

```text
"Hamala" OR "الحمّلة" "data center" OR "data centre" OR "AWS" OR "Batelco"
"Saar" Bahrain "data center" OR "AWS"
"Hamad Town" "data centre" OR "مركز بيانات"
"Northern Governorate" Bahrain "data centre"
site:mun.gov.bh "Northern Governorate" "data center"
```

---

## 5. Minimum evidence and normalization rules

- Positive facility record: require an operator facility page, official government/utility/regulator record, Uptime/certifier record, permit/land/power evidence, or multiple strong B-grade sources naming the site.
- Planned project: allowed only with named developer plus concrete official/trade evidence. Mark `announced`/`MoU`/`planned`; do not mark operational without launch/commissioning/operator page.
- Cloud regions: record as cloud-region evidence only. AWS `me-south-1` proves Bahrain region existence, not building count or street address.
- Directories: Data Center Map, Baxtel, Cloudscene, PeeringDB, Inflect, market reports, and social posts are C leads unless independently confirmed.
- Division assignment: use source place string first, then verify against UPDA/MOMAA maps. Hamala/Saar -> Northern; Manama/Al Seef -> Capital; Hidd -> Muharraq; Riffa/Askar/SIC/southern Bahrain -> Southern.
- Capacity fields: separate `it_load_mw`, `grid_mva_or_mw`, `gross_power_mw`, `solar_mwp`, and `floor_area_sqm`. For Data Oasis, 140,000 sqm is campus/site area; 6,000 sqm is the White Space DC facility area.
- Expected yield: Capital 2-5 positive/lead records, Southern 2-4, Muharraq 0-2, Northern 1-3. If a division has no confirmed facilities, write `no_projects: true` plus the negative searches.
