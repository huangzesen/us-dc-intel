# QA Explorer Official - Qatar Datacenter Enumeration via Government, Regulator, Utility, Free-Zone, Cloud, and Procurement Sources

Date: 2026-08-12. Scope: State of Qatar (QA). Division model: **municipality (baladiyah)**. The required repo divisions are **Doha; Al Khor; Ash Shamal; Al Rayyan; Al Shahaniya; Umm Salal; Al Wakrah; Al Daayen**.

Reliability grades used here: **A** = official, regulator, utility, government-media, cloud-provider, operator-owned, or named certification source for the specific fact cited; **B** = strong trade press, contractor case study, recognized industry database, or regulator-adjacent source; **C** = directory, market report, social post, SEO listing, or old syndication useful only as a lead; **U** = unresolved lead with insufficient live evidence. Grade the fact, not the source: a cloud-provider page is A for a region's existence, but never for a hidden physical address.

---

## 0. Qatar-specific structural facts

- Qatar has 8 municipalities: Doha, Al Khor, Ash Shamal, Al Rayyan, Al Shahaniya, Umm Salal, Al Wakrah, and Al Daayen. The official open-data building-permit dataset uses the same coverage with spelling variants: Doha, Rayyan, Wakrah, Umm Slal, Al-Daayen, Al-Khor, Al-Shamal, and Al-Shahhaniya. Source: https://www.data.gov.qa/explore/dataset/total-building-permits-issued-by-municipality-and-type-of-building-type-of-permit/ (A).
- There is no public national datacenter registry and no public searchable building-permit register for individual datacenter projects. Enumeration must triangulate official/operator statements, CRA telecom records, MCIT services, free-zone pages, Kahramaa/Ashghal infrastructure records, procurement portals, cloud-region pages, IX/cable records, and industry press.
- Qatar's fixed telecom licensees are Ooredoo QPSC, Vodafone Qatar QPSC, Qatar National Broadband Network Company (Qnbn) QPJSC, and additional narrower fixed/satellite/VSAT licensees on CRA's individual-license page. Source: https://www.cra.gov.qa/Services/Telecommunications/Licensing/Individual-Licenses (A).
- CRA was established by Emiri Decree No. 42 of 2014; use CRA as the primary regulator for telecom, interconnection, spectrum, and cloud-policy documents. CRA English portal: https://www.cra.gov.qa/en (A).
- CRA Decision No. (12) of 2026 on access to Submarine Cable Landing Station (SCLS) International Connectivity Services was announced by QNA on 2026-07-20. Use it as official support for cable-landing-access context, not as evidence for any datacenter building. Source: https://qna.org.qa/en/News-Area/News/2026-7/20/cra-boosts-access-to-global-connectivity-through-submarine-cable-network (A).
- National privacy baseline: Law No. 13 of 2016 concerning personal-data privacy is described by NCSA's personal-data privacy page. Source: https://ncsa.gov.qa/ar/pages/personal-data-privacy-personal-data-privacy-protection-law (A). QFC firms also have QFC Data Protection Regulations and Rules 2021, in force from 2022-06-19. Source: https://www.qfc.qa/en/operating-with-qfc/data-protection (A).

---

## 1. Search vocabulary

Core English terms:

```text
"data center" OR "data centre" OR datacenter OR datacentre
"colocation" OR "co-location" OR hosting OR "managed hosting" OR "cloud region"
"internet exchange" OR IXP OR "submarine cable" OR "cable landing station"
"hyperscale" OR "AI infrastructure" OR "digital infrastructure" OR "data hall"
```

Core Arabic terms:

```text
"مركز بيانات" OR "مركز البيانات" OR "مراكز البيانات"
"استضافة" OR "استضافة مشتركة" OR "الحوسبة السحابية" OR "خدمات سحابية"
"نقطة تبادل الإنترنت" OR "مركز تبادل الإنترنت"
"الكابلات البحرية" OR "محطة هبوط الكابلات البحرية"
"البنية التحتية الرقمية" OR "الذكاء الاصطناعي"
```

Official-process Arabic:

```text
"هيئة تنظيم الاتصالات" "مركز بيانات"
"وزارة الاتصالات وتكنولوجيا المعلومات" "مركز البيانات الحكومي"
"رخصة بناء" OR "تصريح بناء" OR "ترخيص البناء"
"شهادة الإنجاز" OR "كهرماء" OR "محطة فرعية" OR "المناقصات"
```

Municipality names:

```text
Doha = "الدوحة"; Al Khor = "الخور"; Ash Shamal = "الشمال";
Al Rayyan = "الريان"; Al Shahaniya = "الشحانية"; Umm Salal = "أم صلال";
Al Wakrah = "الوكرة"; Al Daayen = "الضعاين";
Umm Qarn = "أم قرن"; Lusail = "لوسيل"; Umm Alhoul = "أم الحول";
Ras Bufontas = "راس بوفنطاس"; Ras Laffan = "رأس لفان"; Mesaieed = "مسيعيد"
```

---

## 2. Official and regulator pipeline

### 2.1 CRA - telecom, interconnection, cable access, cloud policy

Use:

- CRA English portal and documents: https://www.cra.gov.qa/en (A)
- CRA individual licenses: https://www.cra.gov.qa/Services/Telecommunications/Licensing/Individual-Licenses (A)
- QNA report on CRA Decision No. (12) of 2026: https://qna.org.qa/en/News-Area/News/2026-7/20/cra-boosts-access-to-global-connectivity-through-submarine-cable-network (A)
- CRA public consultation on cloud policy statement: https://www.cra.gov.qa/press-releases/cra-publishes-a-public-consultation-on-a-cloud-policy-statement-in-qatar (A for policy existence only)

Queries:

```text
site:cra.gov.qa ("data centre" OR "data center" OR "مركز بيانات")
site:cra.gov.qa ("cloud" OR "cloud policy" OR "internet exchange" OR "cable landing")
site:cra.gov.qa ("Ooredoo" OR "Vodafone" OR "Qnbn") "Individual Licenses"
"CRA" Qatar "Decision No. (12) of 2026" "SCLS"
"هيئة تنظيم الاتصالات" "الكابلات البحرية" قطر
```

### 2.2 MCIT, government hosting, and government data

Use:

- MCIT Government Data Center service: https://www.mcit.gov.qa/en/services/government-data-center (A; official page, but may return 403 to automated fetches). The page supports existence of a government hosting facility that provides space, power, cooling, physical security, and connectivity for government entities. It does not publish a street address; do not assign a site municipality unless another source names the location.
- Hukoomi service pages are useful for e-service routing and procurement discovery; prefer MCIT's own Government Data Center page for the GDC description because the Hukoomi shared-GDC project URL may block automated retrieval.
- MCIT Digital Agenda 2030: https://www.mcit.gov.qa/en/about-us/digital-agenda-2030 (A; official page, but may return 403 to automated fetches)
- Qatar Open Data Portal: https://www.data.gov.qa/ (A)

Queries:

```text
site:mcit.gov.qa ("Government Data Center" OR "data centre" OR "مركز البيانات الحكومي")
site:hukoomi.gov.qa ("Shared Government Data Center" OR "Government Data Center")
site:data.gov.qa ("building permits" OR "electricity" OR "municipality")
"مركز البيانات الحكومي" قطر
```

### 2.3 Planning and building permits

Use:

- Ministry of Municipality portal: https://www.mme.gov.qa/ (A)
- Hukoomi building-permit service examples linking into the Building Permits System: https://hukoomi.gov.qa/en/services/request-permit-to-add-building-to-existing-one-small-additions (A)
- Open-data aggregate building-permits dataset by municipality and type: https://www.data.gov.qa/explore/dataset/total-building-permits-issued-by-municipality-and-type-of-building-type-of-permit/ (A)
- QNA report on the 2025 AI-powered building permit system: https://qna.org.qa/en/News-Area/News/2025-10/26/municipality-minister-ai-powered-building-permit-issuance-system-is-a-qualitative-achievement (A)

Rules:

- Qatar's public permit data is aggregate, not project-level. Use it to understand municipal construction volume and permit categories only.
- A datacenter facility record needs an operator, government announcement, utility/NOC evidence, procurement reference, or strong press naming the project. Do not infer a datacenter from a non-residential permit count.

Queries:

```text
site:mme.gov.qa OR site:mun.gov.qa ("data centre" OR "data center" OR "مركز بيانات")
site:data.gov.qa "Total Building Permits Issued" municipality
"Ministry of Municipality" Qatar "building permit" "data center"
"بلدية الدوحة" "رخصة بناء" "مركز بيانات"
"رخصة بناء" "مركز بيانات" قطر
```

### 2.4 Utility, public works, and cooling signals

Use:

- Kahramaa: https://km.qa/ (A for utility services/news it publishes)
- Ashghal: https://www.ashghal.gov.qa/ (A for public-works services/news it publishes)
- US ITA district-cooling regulatory summary: https://www.trade.gov/market-intelligence/qatar-energy-district-cooling-services-regulations (B+ official-US market intelligence)

Rules:

- Kahramaa substation or power-connection evidence can confirm the scale of a named project, but a substation alone is not a datacenter.
- District-cooling operators and service areas are secondary indicators for West Bay, Lusail, Education City/QSTP, and large mixed-use zones; they are not facility proof.

Queries:

```text
site:km.qa ("data centre" OR "data center" OR "مركز بيانات" OR "substation" OR "MW")
site:ashghal.gov.qa ("data centre" OR "data center" OR ICT OR "government building")
"Kahramaa" "data centre" Qatar
"district cooling" "data centre" Doha OR Lusail OR QSTP
"كهرماء" "مركز بيانات"
```

### 2.5 Free zones, investment promotion, and special regimes

Use:

- Qatar Free Zones Authority: https://qfz.gov.qa/ (A)
- Ras Bufontas page: https://qfz.gov.qa/ras-bufontas-4/ (A). Ras Bufontas is the airport free zone adjacent to Hamad International Airport; treat it as a Doha/HIA-area lead unless project evidence supplies a more precise municipality boundary.
- Umm Alhoul page: https://qfz.gov.qa/_umm_alhoul/ (A). Umm Alhoul is the port free zone near Hamad Port and maps to Al Wakrah.
- QFZ home page, which explicitly includes cloud data services among hosted sectors: https://qfz.gov.qa/ (A for sector positioning only)
- Invest Qatar: https://www.invest.qa/ (A for promotion/facts it publishes)
- QFC Data Protection Office: https://www.qfc.qa/en/operating-with-qfc/data-protection (A)

Queries:

```text
site:qfz.gov.qa ("data centre" OR "data center" OR "cloud data" OR "cloud" OR "مركز بيانات")
site:qfz.gov.qa ("Ras Bufontas" OR "Umm Alhoul") ("data" OR "digital" OR "cloud")
site:invest.qa ("data centre" OR "data center" OR "digital infrastructure" OR "cloud")
"Q Data QFZ" "Qatar Free Zones" "data centre"
"Ras Bufontas" "data centre" OR "cloud data services"
"Umm Alhoul" "data centre" OR "cloud data services"
```

### 2.6 Procurement

Use:

- Hukoomi service for searching government tenders: https://hukoomi.gov.qa/en/services/search-tenders-on-government-procurement-portal (A for the service path)
- Agency-level procurement/news pages at Kahramaa, Ashghal, QFZ, MCIT, QNBN, QatarEnergy, Ooredoo, Vodafone Qatar, and MEEZA.

Queries:

```text
"Unified Website of State Procurement" Qatar "data centre"
site:hukoomi.gov.qa tenders ("data centre" OR ICT OR hosting OR cloud)
site:km.qa tenders ("ICT" OR "data centre")
site:ashghal.gov.qa tenders ("data centre" OR ICT)
site:qfz.gov.qa tender ("data centre" OR "cloud")
site:qatarenergy.qa ("data centre" OR ICT OR "Ras Laffan")
```

### 2.7 Cloud-region official pages

| Provider | Official source | Qatar signal as of 2026-08 | How to use |
|---|---|---|---|
| Google Cloud | https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones | Doha region `me-central1` with zones `me-central1-a/b/c` listed as Doha, Qatar. Google launch blog: https://cloud.google.com/blog/products/infrastructure/new-google-cloud-region-now-open-in-qatar | A for cloud-region existence; never infer buildings or addresses. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | Qatar Central, programmatic name `qatarcentral`, physical location Doha, Qatar, availability zone support. | A for cloud-region existence; never infer buildings or addresses. |
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Qatar Region listed; nearest Middle East Regions include UAE and Bahrain. | A for absence of a listed Region; Qatar edge/PoP claims require separate evidence. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No Qatar public cloud region listed. MCIT has Oracle dedicated-cloud/licensing agreements, but that is not a public OCI Qatar Region. | A for absence of public Region; do not count partner/dedicated deployments as public region facilities. |

Cloud pivot queries:

```text
"Google Cloud" "Doha" "me-central1" "MEEZA" OR "QFZ" OR "QSTP"
"Azure" "Qatar Central" "qatarcentral" "MEEZA" OR "Microsoft"
"AWS" Qatar ("edge location" OR CloudFront OR Outposts)
"Oracle" Qatar ("dedicated cloud" OR "public cloud region")
```

---

## 3. Division-by-division official enumeration

### 3.1 Doha

Confirmed/strong leads:

- Ooredoo Qatar Data Centres: Ooredoo's official page says five Qatar facilities covering about 60,000 sq ft and offering hosting, colocation, cloud, and disaster-recovery services. Source: https://www.ooredoo.qa/web/en/business/ict-solutions/qatar-data-centre/ (A for portfolio claim; C for individual addresses unless confirmed elsewhere).
- Government Data Center / GDC2: MCIT and Hukoomi confirm government-hosting services, and Ooredoo has an official GDC2 service page at https://www.ooredoo.qa/web/en/business/ict-solutions/government-data-centre/ (A for service existence; municipality unknown unless a source names the site).
- Microsoft Azure Qatar Central and Google Cloud Doha are Doha metro-level cloud-region facts only (A for region existence; not physical facilities).
- Doha IX is hosted in Ooredoo data centers per DE-CIX/Ooredoo announcements. Sources: https://www.de-cix.net/en/about-de-cix/media/press-releases/ooredoo-and-de-cix-bring-world-class-internet-exchange-to-qatar-with-doha-ix and https://www.ooredoo.qa/web/en/press-release/ooredoo-launches-doha-ix-qatars-first-commercial-internet-exchange-point-in-partnership-with-de-cix/ (A for IXP launch/hosting by Ooredoo; no building address).
- Ooredoo Doha Cable Landing Station and Vodafone Qatar North Doha Cable Landing Station are cable/connectivity assets, not datacenter records by themselves. Source: https://www.submarinenetworks.com/en/stations/asia/qatar (B).
- Ras Bufontas Free Zone is adjacent to Hamad International Airport and should be searched for cloud/data-service tenants. QFZ sector language supports "cloud data services" as a sector, not a particular datacenter. Source: https://qfz.gov.qa/ras-bufontas-4/ and https://qfz.gov.qa/ (A).

Queries:

```text
"Doha" "data centre" (Ooredoo OR Vodafone OR "Government Data Center" OR "Doha IX")
"Ooredoo" "Qatar Data Centre" "60,000"
"Government Data Center" "GDC2" Ooredoo Qatar
"Doha IX" "Ooredoo data centers"
"Ras Bufontas" ("data centre" OR "cloud data services")
"الدوحة" "مركز بيانات" "أوريدو"
```

### 3.2 Al Rayyan

Confirmed/strong leads:

- Education City / QSTP is in Al Rayyan. QSTP official address: https://www.qf.org.qa/research/qatar-science-and-technology-park (A for anchor).
- MEEZA M-VAULT 4 and M-VAULT 5 are stated in operator/press sources as QSTP facilities. M-VAULT 4 operator release: https://www.meeza.net/meeza-reveals-the-launch-of-its-4th-m-vault-4-data-center-building-in-concurrence-with-its-13th-anniversary-celebrations/ (A). M-VAULT 5 operator release: https://www.meeza.net/meeza-launches-the-5th-m-vault-data-center-building-to-boost-cloud-services-in-qatar-and-region/ (A).
- DCD confirms M-VAULT 5 and M-VAULT 4 at QSTP and MEEZA financing/expansion context: https://www.datacenterdynamics.com/en/news/qatari-data-center-firm-meeza-secures-219m-funding-to-fuel-44mw-expansion/ (B).
- MEEZA has a QSTP directory entry stating a network of Tier III M-VAULT datacentres: https://qstp.qa/directory/meeza-qstp-llc/ (A for tenant/profile; not all facility locations).

Queries:

```text
"QSTP" OR "Qatar Science and Technology Park" ("data centre" OR "M-VAULT" OR MEEZA)
"M-VAULT 4" QSTP
"M-VAULT 5" QSTP
"Education City" "data centre" Qatar
"الريان" "مركز بيانات" "ميزة"
```

### 3.3 Al Daayen

Confirmed/strong leads:

- QIX publishes its point location as **MEEZA (MV2) Datacenter, Umm Qarn, Qatar**. Umm Qarn is the administrative seat of Al Daayen. Source: https://www.qix.qa/contactus.html (A for QIX point location). Use this to map QIX/MV2 to Al Daayen unless a later official MEEZA page gives a different precise boundary.
- MEEZA M-VAULT 2 is listed by Data Center Map at Umm Qarn with 15 MW and LEED/Tier claims; search `Data Center Map M-VAULT 2 Umm Qarn` because the directory may return HTTP 429 to automated fetches. Treat this as C-grade address/capacity evidence and confirm with operator or Uptime before using as authoritative.
- Lusail / Energy City Qatar are Al Daayen anchors. Treat the 2007 Energy City Qatar datacenter MoU as historical only unless current official evidence appears.

Queries:

```text
"Umm Qarn" "MEEZA" OR "M-VAULT 2" OR "QIX"
site:qix.qa "Meeza (MV2)" "Umm Qarn"
"Al Daayen" "data centre" OR "مركز بيانات"
"Lusail" ("data centre" OR "ICT infrastructure" OR "edge")
"Energy City Qatar" "data centre"
```

### 3.4 Al Wakrah

Confirmed/strong leads:

- Umm Alhoul Free Zone is near Hamad Port and maps to Al Wakrah. QFZ page: https://qfz.gov.qa/_umm_alhoul/ (A for zone location and focus sectors).
- Q Data QFZ/Syntys facilities are stated to be in Qatar Free Zones, but public Syntys materials do not name Ras Bufontas versus Umm Alhoul. Keep municipality **unknown/Qatar Free Zones** until a source names the zone. Source: https://syntys.com/newsroom (A for acquisition/capacity; U for exact zone).
- Mesaieed/Hamad Port industrial IT should be searched as edge/enterprise infrastructure, not commercial colocation unless named.

Queries:

```text
"Umm Alhoul" ("data centre" OR "cloud data services" OR ICT)
"Hamad Port" ("data centre" OR ICT OR "digital")
"Mesaieed" ("data centre" OR ICT OR "مركز بيانات")
"Q Data QFZ" "Umm Alhoul" OR "Ras Bufontas"
"الوكرة" "مركز بيانات"
```

### 3.5 Al Khor

Anchors: Ras Laffan Industrial City and Al Khor city. Expected result is industrial/telecom edge only unless QatarEnergy, Kahramaa, a contractor, or an operator names a facility.

```text
"Ras Laffan" ("data centre" OR "data center" OR ICT OR "control room")
"Al Khor" "data centre" OR "مركز بيانات"
site:qatarenergy.qa "Ras Laffan" ("data" OR ICT OR "digital")
"الخور" "مركز بيانات"
```

### 3.6 Ash Shamal

Expected negative for commercial colocation/hyperscale. Search Madinat ash Shamal, Al Ruwais, and Arabic names; document absence.

```text
"Ash Shamal" Qatar "data center"
"Madinat ash Shamal" OR "Al Ruwais" ("data centre" OR ICT)
"الشمال" "قطر" "مركز بيانات"
```

### 3.7 Al Shahaniya

Expected negative for commercial colocation/hyperscale. Search Al Shahaniya and Dukhan. Treat oil/industrial control systems as enterprise/edge leads only.

```text
"Al Shahaniya" "data centre" OR "data center"
"Dukhan" ("data centre" OR ICT OR "digital")
"الشحانية" "مركز بيانات"
```

### 3.8 Umm Salal

Expected negative for commercial colocation/hyperscale. Watch for government edge, telecom exchange, or QNBN fibre-related records.

```text
"Umm Salal" "data centre" OR "data center"
"أم صلال" "مركز بيانات"
"Umm Slal" ICT Qatar
```

---

## 4. Known official/primary evidence matrix

| Facility / project | Municipality | Evidence status | Grade |
|---|---|---|---|
| Ooredoo Qatar Data Centres portfolio | Doha / Qatar; individual sites unpublished | Ooredoo states five facilities and about 60,000 sq ft: https://www.ooredoo.qa/web/en/business/ict-solutions/qatar-data-centre/ | A for portfolio; C/U for individual site addresses |
| Ooredoo GDC2 / government-hosting service | Site not public | MCIT/Hukoomi/Ooredoo confirm government-hosting service and Tier III GDC2 wording; no public street address found | A for service; U for site |
| Syntys acquisition of Q Data QFZ | Qatar Free Zones; exact zone unresolved | Syntys says Q Data QFZ operates hyperscale facilities in Qatar Free Zones, 5 MW live + 7.5 MW under development: https://syntys.com/newsroom | A for acquisition/capacity; U for zone |
| MEEZA M-VAULT 4 | Al Rayyan, QSTP | MEEZA official launch page says the fourth M-VAULT building is the biggest datacenter building in Qatar | A |
| MEEZA M-VAULT 5 | Al Rayyan, QSTP | MEEZA official launch page names QSTP | A |
| MEEZA M-VAULT 2 / QIX point | Al Daayen, Umm Qarn | QIX contact page names MEEZA MV2 Datacenter, Umm Qarn; Data Center Map gives MV2 address/capacity | A for QIX point; C for directory capacity/address |
| Google Cloud Doha `me-central1` | Doha metro only | Google official region/zone docs list Doha zones | A for region |
| Microsoft Azure Qatar Central `qatarcentral` | Doha metro only | Microsoft Learn lists Qatar Central, Doha, availability-zone support | A for region |
| Doha IX | Doha/Ooredoo facilities; no address | Ooredoo and DE-CIX official releases say hosted in Ooredoo data centers | A for IXP |
| QIX | Al Daayen lead via MV2/Umm Qarn | qix.qa official site and contact page | A for IXP/location |
| Cable landing stations | Doha / Halul offshore | Submarine Networks lists Ooredoo Doha CLS, Ooredoo Halul Island CLS, Vodafone Qatar North Doha CLS | B; use as connectivity evidence |
| AWS public Region | None in Qatar | AWS official regions page has no Qatar Region | A for absence |
| Oracle OCI public Region | None in Qatar | Oracle public-region page has no Qatar public cloud region | A for absence |

---

## 5. Normalization rules

- Do not count cloud regions, availability zones, IXPs, cable landing stations, telecom exchanges, or investment funds as datacenter buildings unless there is independent facility evidence.
- Keep **QIX** and **Doha IX** separate. QIX has an official MV2/Umm Qarn point; Doha IX is the Ooredoo + DE-CIX commercial IX hosted in Ooredoo data centers.
- Keep **MEEZA M-VAULT 2** (Umm Qarn/Al Daayen lead) separate from **M-VAULT 4/5** (QSTP/Al Rayyan).
- Keep **Qatar Free Zones** projects unmapped between Ras Bufontas and Umm Alhoul until the zone is named.
- Capacity fields must distinguish IT load MW, gross/installed capacity, grid import, solar/self-supply, square footage, and financial investment.

Recommended record fields:

```text
facility_name
aliases
operator_current
operator_legacy
municipality
district_or_landmark
free_zone_or_master_developer
status
evidence_grade
evidence_type
evidence_urls
permit_or_licence_refs
it_load_mw
gross_or_installed_mw
grid_import_mw_or_mva
space_sq_ft
cloud_region_or_ix_role
mapping_confidence
notes_on_uncertainty
```

---

## 6. Re-check cadence

- Monthly: CRA press/documents, MCIT/Hukoomi GDC pages, QFZ/Invest Qatar news, Ooredoo/Syntys pages, MEEZA news, DCD Qatar tag, Gulf Times/Peninsula/QNA data-centre searches.
- Quarterly: Google/Azure/AWS/Oracle official region lists; qix.qa and Doha IX/DE-CIX pages; PeeringDB; Submarine Networks and TeleGeography; Uptime Institute certification directory.
- Every 6 months: open-data building-permit dataset; negative searches for Al Khor, Ash Shamal, Al Shahaniya, and Umm Salal; Q Data QFZ exact-zone search; MEEZA M-VAULT 6/7/8 expansion status.
