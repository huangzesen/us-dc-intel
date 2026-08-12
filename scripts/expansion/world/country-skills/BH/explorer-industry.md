# BH Explorer Industry - Bahrain Datacenter Discovery via Operators, Press, Directories, IXP, and Cable Records

Date: 2026-08-12. Scope: Kingdom of Bahrain (BH). Division model: **governorate**. Required repo divisions from `world-manifest.jsonl`: **Capital Governorate; Southern Governorate; Muharraq Governorate; Northern Governorate**.

Reliability grades: **A** = operator-owned, government/regulator/utility, official cloud/provider, official IXP, or certifier source for the exact fact; **B** = high-signal trade press, contractor case study, or recognized local media with named facts; **C** = directory, market report, PeeringDB-only, social, SEO listing, or unattributed address/capacity lead; **U** = unresolved. Do not create a facility from a cloud region, IXP, cable landing station, partner service, or MoU unless a separate source confirms a physical datacenter.

---

## 0. Market frame and corrected anchors

- Bahrain is a small connectivity-led market. The realistic nationwide yield is low: roughly 6-12 confirmed/lead records, plus IX/cable/cloud-region context.
- The hyperscale anchor is **AWS Middle East (Bahrain) `me-south-1`**, officially opened 2019-07-30 with 3 AZs. AWS does not disclose physical addresses; all Manama/Hamala/Saar building placements from directories remain C-grade until primary evidence is found.
- The strongest verified operator anchors are:
  - **Batelco by Beyon data center, Hamala**: official page https://www.batelco.com/business/data-center/ claims Bahrain's first and only Tier III certified data center and gives **Building 1095, Road 1425, Block 1014, Hamala Bahrain**. Treat as Northern Governorate unless boundary evidence contradicts.
  - **Beyon White Space Data Centre / Data Oasis, southern Bahrain**: official Beyon release https://beyon.com/2025/11/02/batelco-by-beyon-announces-commissioning-of-bahrains-first-white-space-data-centre-during-gateway-gulf-2025/ says the 6,000 sqm White Space DC is commissioned and forms part of a 140,000 sqm Data Oasis site in southern Bahrain. Treat as Southern Governorate.
  - **Kalaam Telecom data center, Al Seef/Manama**: official page https://kalaam-telecom.com/kalaam-data-center/ says the facility is in the heart of Al Seef district, Manama. Treat as Capital Governorate.
  - **iGA government data center program**: official iGA page https://www.iga.gov.bh/en/article/operations-and-governance says iGA manages and develops the government data center. A for program, U for address/division unless a named site is found.
- 2026 AWS caveat: AWS Health Dashboard pages and trade press reported ME-SOUTH-1 impact from March 2026 drone-strike-related incidents. Use https://health.aws.amazon.com/health/status as A-grade current status; The Register, DCD, Developing Telecoms, Network World, etc. are B-grade historical incident evidence.

---

## 1. High-signal sources to search

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Beyon / Batelco | https://beyon.com/ ; https://www.batelco.com/business/data-center/ | Operator-controlled facility claims, White Space/Data Oasis, sovereign cloud, Qareeb partnership | A for own facts |
| Kalaam Telecom | https://kalaam-telecom.com/kalaam-data-center/ | Al Seef/Manama DC location and services | A for own facts |
| Qareeb Data Centres | https://www.qareebdc.com/ and Batelco announcement https://www.batelco.com/business/batelco-by-beyon-and-qareeb-data-centers-announce-strategic-partnership-to-launch-bahrains-first-edge-data-center/ | Edge DC partnership; verify whether this is the White Space facility lease or a distinct site before adding | A/B for announcement; U for distinct facility |
| DCD | https://www.datacenterdynamics.com/ search Bahrain | Construction/operator coverage; Batelco-Qareeb, Tencent, AWS incident reporting | B |
| Developing Telecoms / Network World / The Register / DCK | site searches | AWS 2026 incident and telecom/DC news | B |
| BNA / EDB / iGA | https://www.bna.bh/ ; https://www.bahrainedb.com/ ; https://www.iga.gov.bh/en/ | Official announcements and investment-policy leads | A/B |
| Data Center Map / Baxtel / Cloudscene / Inflect / PeeringDB | directory searches | Address/building/IX leads only | C unless independently confirmed |
| Market reports / GlobeNewswire / Arizton | example: https://www.globenewswire.com/news-release/2024/07/23/2917037/0/en/Bahrain-Data-Center-Market-Investment-Analysis-Report-2024-2029-Featuring-Key-DC-Investors-Batelco-Tencent-Cloud-and-Zain-New-Entrants-Gulf-Data-Hub.html | Investor list, market size, GDH plan lead | C for facility proof |

Queries:

```text
site:beyon.com Bahrain "data centre" OR "data center" OR "Data Oasis" OR "White Space"
site:batelco.com Bahrain "data centre" OR "data center" OR Qareeb OR Hamala
site:kalaam-telecom.com "data center" OR "data centre" "Al Seef"
site:datacenterdynamics.com Bahrain "data center" OR "data centre" OR Batelco OR Qareeb OR Tencent OR AWS
site:developingtelecoms.com Bahrain "data centre" OR AWS OR Batelco
site:bna.bh "data centre" OR "data center" OR "مركز بيانات" OR Tencent OR Beyon
site:bahrainedb.com "data center" OR "cloud" OR Tencent OR AWS
```

---

## 2. Operator and project seed list

| Operator / project | Primary evidence | Division handling | Current grade |
|---|---|---|---|
| Batelco by Beyon DC | https://www.batelco.com/business/data-center/ | Official address says Hamala -> **Northern Governorate**. Do not use older Manama directory placement without proof. | A for operator/address/Tier III claim; verify Uptime certificate separately if needed |
| Beyon White Space DC / Data Oasis | https://beyon.com/2025/11/02/batelco-by-beyon-announces-commissioning-of-bahrains-first-white-space-data-centre-during-gateway-gulf-2025/ | Operator says southern Bahrain -> **Southern Governorate**. Record 6,000 sqm facility and 140,000 sqm campus separately. | A |
| Kalaam Telecom DC | https://kalaam-telecom.com/kalaam-data-center/ | Al Seef, Manama -> **Capital Governorate** | A for location/service; capacity U unless specified |
| iGA government DC | https://www.iga.gov.bh/en/article/operations-and-governance | Bahrain-wide/government; division U until named site | A for program; U for address |
| AWS `me-south-1` | https://aws.amazon.com/blogs/aws/now-open-aws-middle-east-bahrain/ ; https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | Bahrain-wide undisclosed. Directory placements in Manama/Hamala/Saar remain C. | A for region/AZ count; C/U for facilities |
| AWS 2026 incident | AWS Health Dashboard plus DCD/The Register/Developing Telecoms/Network World | Status overlay, not a new facility | A for AWS Health, B for media |
| Tencent Cloud Bahrain IDC | Tencent official expansion note https://www.tencent.com/en-us/articles/2201165.html ; PRNewswire/EDB announcement https://www.prnewswire.com/news-releases/tencent-cloud-deploys-its-first-mena-region-internet-data-centre-hub-in-bahrain-301237067.html | Bahrain-wide until site shown. Search Tencent region/IDC pages for current listing. | A/B for announcement; U for current operational site |
| Beyon Solutions / Oracle Sovereign HyperCloud | https://beyon.com/2025/11/02/beyon-solutions-and-the-information-egovernment-authority-sign-agreement-to-launch-kingdom-of-bahrains-first-sovereign-hypercloud/ | Claims locally operated cloud and data entirely within Bahrain; physical facility/site U. | A for agreement; U for physical DC |
| Qareeb edge DC with Batelco | https://www.batelco.com/business/batelco-by-beyon-and-qareeb-data-centers-announce-strategic-partnership-to-launch-bahrains-first-edge-data-center/ ; DCD coverage https://www.datacenterdynamics.com/en/news/batelco-to-lease-bahrain-data-center-to-qareeb-data-centers/ | Likely tied to Batelco/Beyon facilities; verify if distinct from White Space before adding separate record. | A/B announcement; U distinct site |
| Gulf Data Hub Bahrain | Market report only unless GDH publishes a Bahrain page | Do not add as confirmed. Search official GDH and KKR/GDH announcements. | C lead |
| stc Bahrain / Zain Bahrain | Official operator pages + TRA licensee checks | Enterprise hosting/cloud lead only unless a named Bahrain DC page appears. | B/C/U |
| BIX / cable landing stations | Tender Board/BNA/Batelco/cable-system pages | IX/cable infrastructure context; do not count as DC without colocation proof. | A/B context |

Operator queries:

```text
"Batelco" "Hamala" "data center" OR "data centre"
"Building 1095" "Road 1425" "Block 1014" "Hamala"
"Beyon" "White Space Data Centre" "Data Oasis"
"Kalaam" "Al Seef" "data center"
"Qareeb" "Batelco" "edge data center" Bahrain
"Tencent Cloud" Bahrain IDC operational official
"Gulf Data Hub" Bahrain "data center" official
"stc Bahrain" OR "Zain Bahrain" "data center" OR "data centre" OR colocation
```

---

## 3. Cloud and hyperscaler checks

| Provider | Official URL | Bahrain signal |
|---|---|---|
| AWS | https://aws.amazon.com/blogs/aws/now-open-aws-middle-east-bahrain/ ; https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html ; https://health.aws.amazon.com/health/status | `me-south-1`, Middle East (Bahrain), 3 AZs. Use only for cloud-region record unless physical evidence exists. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Saudi Q4 2026 official announcement https://news.microsoft.com/source/emea/2026/02/microsoft-confirms-saudi-arabia-datacenter-region-available-for-customers-to-run-cloud-workloads-from-q4-2026/ | No Bahrain region. Saudi/UAE are regional context only. |
| Google Cloud | https://cloud.google.com/about/locations ; Doha launch https://cloud.google.com/blog/products/infrastructure/new-google-cloud-region-now-open-in-qatar | No Bahrain region. Doha is context only. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No public OCI Bahrain region in standard list; Bahrain sovereign deployment is Beyon/Oracle Alloy, physical site U. |
| Tencent Cloud | https://www.tencentcloud.com/document/product/213/6091 ; https://www.tencent.com/en-us/articles/2201165.html | Bahrain IDC was announced/planned; verify current operational status on official locations/docs before upgrading. |
| Huawei / Alibaba | official region lists | No verified Bahrain public region found; claims remain C/U. |

Cloud-to-facility queries:

```text
"AWS" "Bahrain" "Hamala" OR "Saar" OR "Manama" "data center"
"Amazon Data Services" Bahrain "EWA" OR "permit" OR "lease"
"Tencent Cloud" Bahrain "region" OR "IDC" site:tencentcloud.com OR site:tencent.com
"Oracle Alloy" "Beyon" "local data centres" Bahrain
"Huawei Cloud" Bahrain region official
```

---

## 4. Division workflow

### 4.1 Capital Governorate

Targets: Manama, Al Seef, Bahrain Bay, Diplomatic Area, Juffair, Hoora, Salmaniya, Umm Al Hassam. Confirmed/strong leads: Kalaam Al Seef DC; iGA government DC program if a Manama site emerges; AWS/directory Manama leads are C only; BIX/cable ecosystem is context.

```text
"Manama" "data center" OR "data centre" OR "مركز بيانات"
"Al Seef" OR "Seef District" "data centre" Kalaam
"Bahrain Bay" "data center" OR "cloud"
site:datacentermap.com/bahrain/manama Bahrain "data center"
"المنامة" "مركز بيانات"
"السيف" "مركز بيانات"
```

### 4.2 Southern Governorate

Targets: Data Oasis/White Space, Riffa, Askar, Awali, Salman Industrial City, US Trade Zone, Al Dur (power context only), Zallaq. Confirmed anchor: Beyon White Space DC / Data Oasis. Leads: Beyon/Oracle sovereign cloud, Qareeb if tied to southern facility, GDH C-lead, SIC land/power searches.

```text
"Beyon" "Data Oasis" "data centre"
"White Space Data Centre" Bahrain
"Beyon Solutions" "Oracle" "Sovereign HyperCloud"
"Salman Industrial City" "data centre" OR "digital infrastructure"
"Askar" OR "Riffa" "data centre" OR "مركز بيانات"
"Gulf Data Hub" Bahrain
```

### 4.3 Muharraq Governorate

Targets: Hidd, Muharraq, Arad, Busaiteen, Bahrain International Airport, Amwaj, Bahrain Logistics Zone, Khalifa Bin Salman Port, BIIP if source says Hidd. Expect negative-heavy results; do not move BIIP into Southern or Muharraq without parcel evidence.

```text
"Hidd" OR "الحد" "data centre" OR "مركز بيانات"
"Muharraq" "data center" OR "data centre" OR "مركز بيانات"
"Bahrain Logistics Zone" OR "Khalifa Bin Salman Port" "data centre" OR "ICT"
"BIIP" "Hidd" "data centre"
"Amwaj Islands" "data centre" OR "network"
```

### 4.4 Northern Governorate

Targets: Hamala, Saar, Budaiya, Diraz, Barbar, Hamad Town. Confirmed anchor: Batelco by Beyon Hamala DC. C leads: AWS Hamala/Saar directory/building records. Search for permit/utility/operator corroboration before any AWS site record is upgraded.

```text
"Hamala" OR "الحمّلة" "data centre" OR "data center" OR "Batelco" OR "AWS"
"Saar" Bahrain "data center" OR "AWS"
"Hamad Town" "data centre" OR "مركز بيانات"
"Northern Governorate" Bahrain "data centre"
"المحافظة الشمالية" "مركز بيانات"
```

---

## 5. Arabic discovery patterns

```text
"البحرين" "مركز بيانات" "باتلكو" OR "بيون" OR "أمازون" OR "تينسنت"
"البحرين" "مراكز البيانات" "المنامة" OR "السيف" OR "الحمّلة"
"البحرين" "الحوسبة السحابية" "السحابة الحكومية" OR "السيادية"
"البحرين" "افتتاح" OR "تدشين" "مركز بيانات"
"البحرين" "مذكرة تفاهم" "مركز بيانات" OR "سحابة"
site:bna.bh "مركز بيانات" OR "مراكز البيانات" OR "الحوسبة السحابية"
site:batelco.com "مركز بيانات" OR "مراكز البيانات"
```

Arabic status mapping:

- `مذكرة تفاهم` / `اتفاقية` / `شراكة` = MoU/agreement/partnership; not operational unless launch/commissioning is stated.
- `تخصيص أرض` / `تأجير أرض` = land signal.
- `وضع حجر الأساس` / `بدء الأعمال الإنشائية` = construction-start signal.
- `افتتاح` / `تدشين` / `إطلاق` / `دخول الخدمة` = launch/operational signal, still verify with operator/government source.

---

## 6. Reliability and normalization rules

- A-grade facility evidence: operator facility page, government/utility/regulator record, certifier record, permit/land/power record, or official commissioning release.
- B-grade: DCD, Developing Telecoms, The Register, Network World, Data Center Knowledge, W.Media, Capacity Media, ITP, Trade Arabia, Gulf Daily News, Biz Bahrain, contractor/vendor case study.
- C-grade: directories, market reports, PeeringDB, Inflect, social posts, SEO pages, unattributed address/capacity records.
- Status values: `announced | MoU | planned | land lease | secured power | under construction | commissioned | operational | impaired | retired | unknown`.
- Normalize names: `Batelco` / `Batelco by Beyon` -> Beyon Group; `VIVA Bahrain` -> `stc Bahrain`; `White Space Data Centre` -> Beyon/Batelco facility at Data Oasis; `me-south-1` -> AWS Middle East (Bahrain).
- Separate fields: `facility_name`, `operator_current`, `operator_legacy`, `governorate`, `named_place`, `industrial_zone_if_any`, `evidence_grade`, `evidence_urls`, `status`, `floor_area_sqm`, `site_area_sqm`, `it_load_mw`, `grid_mva_or_mw`, `solar_mwp`, `cloud_region_or_ix_role`, `notes_on_uncertainty`.
- Honest expected coverage: Capital 1-3 confirmed plus leads; Southern 1-3 confirmed/planned; Muharraq 0-2 mostly land/industrial leads; Northern 1 confirmed plus C-grade AWS leads. Record negative searches for sparse divisions instead of padding with IX/cable/cloud pseudo-records.
