# LY Explorer Official - Libya Datacenter Enumeration via GACI, LPTIC/LTT, Municipal Permits, GECOL, Cloud, Colo, and Trade Sources

Date: 2026-08-12. Country: **LY Libya**. Division model: **22 popularates** (`Benghazi`, `Butnan`, `Derna`, `Ghat`, `Green Mountain`, `Western Mountain`, `Jafara`, `Jufra`, `Kufra`, `Murqub`, `Misrata`, `Meadows`, `Murzuq`, `Nalut`, `Nuqat al Khams`, `Sabha`, `Sirte`, `Tripoli`, `Oases`, `Wadi al Hayaa`, `Wadi ash Shati`, `Zawiya`). Angle: **official/regulatory/cloud pipeline** for finding commercial, telecom, government, university, free-zone, and edge data-center facilities.

Reliability grades:
- **A** = official/primary source: GACI/CIM official record, IANA ccTLD record/report, LPTIC/LTT/Almadar/Libyana/Hatif official page, municipality building-license/planning record, official free-zone/university/government page, GECOL tender/project/power record, UNGM/UNDP procurement, official cloud-provider location page, official operator facility page.
- **B** = strong secondary source: Libya Herald, Libya Observer, Libya Monitor, Data Center Dynamics, Telecompaper, official vendor/customer case study, standards/certification page, reputable international procurement/trade press with named site and proponent.
- **C** = weak lead: DataCenterMap/datacenters.com/ColocationM/directory-only facility page, LinkedIn/social post, generic market report, unimplemented MoU, press item saying "digital transformation" or "cloud" without a named facility.

---

## 0. Libya-specific structure facts

- Libya does **not** have a single public national datacenter register. Enumeration requires joining **GACI/CIM telecom and digital-infrastructure signals**, **LPTIC and subsidiary operator pages**, **municipality building-license evidence**, **GECOL power/tender records**, **free-zone/university/government procurement**, **official hyperscaler region lists**, **local operator pages**, and **trade press/directories**.
- The highest-yield cities are **Tripoli**, **Benghazi**, **Misrata**, and **Sabha**. Secondary leads exist in **Murzuq**, **Derna**, **Tobruk/Butnan**, **Sirte**, **Zawiya**, **Al-Khums/Murqub**, and southern/oil-field municipalities when a government, telecom, university, port/free-zone, banking, oil/gas, or power-control system appears.
- The official search language is mostly **Arabic**. English is essential for cloud pages, IANA, UNGM, DCD, Telecompaper, vendor pages, and Libya Herald. Use both British and US spellings plus Arabic: `data centre`, `data center`, `datacenter`, `مركز بيانات`, `مراكز البيانات`, `مركز استضافة البيانات`, `مركز معلومات`, `مركز تقنية المعلومات`, `الحوسبة السحابية`, `استضافة`, `مركز خوادم`.
- Facility names are often hidden behind telecom-service language. Search `LTT`, `LPTIC`, `Almadar`, `Libyana`, `Hatif Libya`, `Libyan International Telecom Company`, `Aljeel Aljadeed`, `Libyan Spider`, `Qabas`, `TransSahara`, `Tatweer`, `Misrata Free Zone`, `University of Tripoli`, `Fezzan University`, and local municipalities.
- Treat most **cloud/5G/digital-transformation** announcements as leads until a physical facility is named. In Libya, a "cloud" offer may be hosted in a local private data center, a telecom data center, or an external hyperscaler/partner region.

Core vocabulary:

```text
data centre
data center
datacenter
IDC
Internet Data Center
hosting centre
data hosting centre
colocation
co-location
cloud services
sovereign cloud
root server
DNS root
5G core
server room
backup site
disaster recovery
Tier 3 / Tier III
Uptime
MW / MVA / kV / 11 kV / 30 kV / 66 kV / 220 kV
generator / UPS / cooling / fire suppression / CCTV
building permit / construction license / planning permit
```

Arabic terms:

```text
مركز بيانات
مراكز بيانات
مراكز البيانات
مركز استضافة البيانات
مركز معلومات
مركز تقنية المعلومات
مركز اتصالات
مركز خوادم
غرفة الخوادم
غرفة السيرفرات
الحوسبة السحابية
الخدمات السحابية
استضافة
استضافة المواقع
خوادم الجذر
السيادة الرقمية
رخصة بناء
تراخيص البناء
المخطط العمراني
اللجنة المعمارية
الشركة العامة للكهرباء
محطة كهرباء
مولدات احتياطية
مزود طاقة غير منقطع
تبريد ذكي
إطفاء الحريق
الألياف البصرية
```

---

## 1. Grade A official/regulatory routes

### 1.1 GACI / CIM - communications and informatics regulator

Primary sources:
- General Authority of Communications and Informatics (GACI/CIM): https://www.cim.gov.ly/
- IANA `.LY` delegation record: https://www.iana.org/domains/root/db/ly.html
- IANA 2025 transfer report: https://www.iana.org/reports/2025/ly-report-20251030.html

Why it matters:
- GACI is Libya's main communications/informatics authority for telecom and national digital-infrastructure signals. IANA's 2025 `.LY` transfer report states that GACI was established under GNU Council of Ministers Decision No. 49 of 2022 and assigned `.LY` domain management responsibilities under Resolution No. 985; it also identifies LPTIC/LTT as legacy technical operators for `.LY`.
- The IANA delegation record gives **GACI at Telecom Tower, Al Zawia Street, Tripoli** as ccTLD manager and **Libya Telecom and Technology (LTT)** as technical contact. This is A-grade evidence for regulator/operator identity and Tripoli network-governance infrastructure, not by itself a commercial datacenter record.
- GACI news is high value for `root servers`, `digital sovereignty`, `5G`, `telecom licenses`, `frequency allocation`, and operator enforcement. Use GACI/CIM and LANA/official reposts before relying on social snippets.

GACI query templates:

```text
site:cim.gov.ly "مركز بيانات"
site:cim.gov.ly "مراكز البيانات"
site:cim.gov.ly "خوادم الجذر"
site:cim.gov.ly "السيادة الرقمية"
site:cim.gov.ly "ترخيص" "اتصالات"
site:cim.gov.ly "الحوسبة السحابية"
site:cim.gov.ly "الجيل الخامس" "مركز"
"General Authority of Communications and Informatics" Libya "data center"
"GACI" Libya "root servers" "Tripoli" "Benghazi"
site:lana.gov.ly "الهيئة العامة للاتصالات والمعلوماتية" "مركز بيانات"
site:lana.gov.ly "General Authority of Communications and Informatics" "data center"
```

Extract: authority/decision, license or policy type, operator legal name, facility city, any site owner such as Almadar/LTT/Libyana, root/DNS/5G role, dates, and whether the source proves a facility or only a regulatory/policy function.

### 1.2 LPTIC and state telecom subsidiaries

Primary sources:
- LPTIC digital transformation: https://lptic.ly/digital-transformation/
- LPTIC companies pages: https://lptic.ly/our-companies/
- LTT business data-center/hosting service: https://ltt.ly/business/Dcenter
- LTT contact/location pages: https://www.ltt.ly/contact

Why it matters:
- LPTIC is the state-owned telecom holding company. Its digital-transformation page is an A-grade seed for **comprehensive data centers in Tripoli and Misrata** and should be followed by municipal/GECOL/operator searches for exact status and capacity.
- LTT's Arabic business page for hosting/data-center services is A-grade operator evidence that LTT markets a data-center service; use it to pivot to Tripoli, LTT IDC, Alshut Road, `.LY` technical operations, and DDoS/service-stability press.
- LPTIC subsidiaries are the main telecom facility candidates: `Libya Telecom and Technology (LTT)`, `Almadar Aljadid`, `Libyana`, `Hatif Libya`, `Libyan International Telecom Company`, `Aljeel Aljadeed`, `Al-Bunya Investment & Services`, and `Libya Post`.

LPTIC/LTT query templates:

```text
site:lptic.ly "data center"
site:lptic.ly "data centers" "Tripoli" "Misrata"
site:lptic.ly "digital transformation" "data centers"
site:lptic.ly "Almadar" "data center"
site:lptic.ly "Libyana" "data center"
site:ltt.ly "مركز البيانات"
site:ltt.ly "خدمات الاستضافات"
site:ltt.ly "استضافة" "مركز البيانات"
site:ltt.ly "طرابلس" "مركز البيانات"
"LTT Internet Data Center" Libya
"Libya Telecom and Technology" "data centre"
"Libya Telecom and Technology" "DDoS" "data centre"
"Almadar Aljadid" "data center" Tripoli Benghazi
"Libyana" "data center" Libya
```

Extract: legal entity, subsidiary relationship, facility city, service name, address/contact, hosting/colo/cloud service class, resilience claims, cyber/root-server role, and whether the page proves a physical facility or only a service.

### 1.3 Municipal building licenses and urban-planning records

Primary/legal routes:
- Tripoli Center Municipality building-license department: https://tripoli.gov.ly/department/%D8%B1%D8%AE%D8%B5-%D8%A7%D9%84%D8%A8%D9%86%D8%A7%D8%A1/
- Libya building-license regulation, Minister of Local Government Decision No. 225 of 2018: https://lawsociety.ly/legislation/%D9%82%D8%B1%D8%A7%D8%B1-%D8%B1%D9%82%D9%85-225-%D9%84%D8%B3%D9%86%D8%A9-2018-%D9%85-%D8%A8%D8%B4%D8%A3%D9%86-%D9%84%D8%A7%D8%A6%D8%AD%D8%A9-%D8%AA%D8%B1%D8%A7%D8%AE%D9%8A%D8%B5-%D8%A7%D9%84%D8%A8/
- Municipality official domains and Facebook pages where no searchable portal exists.

Handling:
- Libya has municipality-level building licensing rather than a public national planning-register search. Decision No. 225/2018 includes the building-license form fields to extract: municipality, license number, date, owner, national ID, locality, neighborhood, street, board/map number, parcel number, engineering office, architectural committee record, and conditions.
- Use a municipality page as A-grade evidence for the **permit workflow**. Use an actual published license, municipal announcement, or official construction/project page as A-grade project evidence. If public search is unavailable, run web-indexed Arabic queries against each municipality and the operator/project name.

Permit query templates:

```text
site:tripoli.gov.ly "مركز بيانات"
site:tripoli.gov.ly "رخصة بناء" "مركز"
site:tripoli.gov.ly "رخص البناء" "اتصالات"
site:{municipality-domain} "مركز بيانات"
site:{municipality-domain} "مركز استضافة البيانات"
site:{municipality-domain} "رخصة بناء" "مركز بيانات"
site:{municipality-domain} "اللجنة المعمارية" "اتصالات"
site:{municipality-domain} "المخطط العمراني" "مركز"
"{city Arabic}" "مركز بيانات" "رخصة بناء"
"{city English}" "data center" "building permit" Libya
"{operator}" "{city}" "رخصة بناء"
"{operator}" "{city}" "المخطط العمراني"
```

Extract: municipality, popularate, city/locality, parcel/plot/street, applicant/proponent, engineering office, license/committee record number, project description, floors/building area, generator/fuel/cooling notes, approval/construction/occupancy status, and date.

### 1.4 GECOL - power, substations, tenders, and grid constraints

Primary source:
- General Electricity Company of Libya (GECOL): https://www.gecol.ly/
- GECOL projects: https://www.gecol.ly/GProjects/ViewProjects
- GECOL tenders and bids: https://www.gecol.ly/GTendersandBids/

Why it matters:
- Libya's grid reliability is a core siting/status constraint. Many facilities emphasize backup generators, UPS, independent feeds, or free-zone/private power. GECOL records are most useful for substations, MV/HV connections, tenders, telecom-site power work, and city-level power availability.
- GECOL is not a datacenter registry. Grade A for power project/tender facts; grade B/A- for datacenter inference unless the record explicitly names the facility or operator.

Power query templates:

```text
site:gecol.ly "مركز بيانات"
site:gecol.ly "مراكز البيانات"
site:gecol.ly "مركز معلومات"
site:gecol.ly "اتصالات" "ك.ف"
site:gecol.ly "LTT"
site:gecol.ly "ليبيا للاتصالات والتقنية"
site:gecol.ly "المدار الجديد"
site:gecol.ly "ليبيانا"
site:gecol.ly "طرابلس" "محطة" "اتصالات"
site:gecol.ly "بنغازي" "محطة" "اتصالات"
site:gecol.ly "مصراتة" "محطة" "اتصالات"
"{operator}" "GECOL" "data center"
"{facility}" "مولدات" "مركز بيانات"
"{facility}" "UPS" Libya
"{facility}" "MVA" Libya
```

Extract: customer/operator, city, substation/feeders, voltage level, transformer/MVA, generation or backup capacity, tender number/date, contractor, completion/energization date, and whether the evidence is dedicated to a datacenter or broader telecom/ICT infrastructure.

### 1.5 Free-zone, university, municipal-data-hub, and international procurement routes

Primary/strong sources:
- Misrata Free Zone official site: https://www.mfzly.com/en/
- MFZ investment/news pages: https://www.mfzly.com/en/investment and https://www.mfzly.com/en/post.php
- University of Tripoli Faculty of IT data-center item: https://uot.edu.ly/it/news-details.php?id=6538&lang=en
- UNGM/UNDP Libya procurement notice UNDP-LBY-00644: https://www.ungm.org/Public/Notice/301177

Why it matters:
- Free zones and universities are often better documented than ordinary permits. MFZ is a high-yield Misrata search target because trade press reports a Huawei-built data-hosting centre with 40 km fibre, racks, dual power, backup energy, cooling, fire/security, and cloud storage; verify with MFZ official pages/social posts when possible.
- University of Tripoli is A-grade for a small institutional data center in Tripoli when its own page/news item is accessible.
- UNGM/UNDP is A-grade procurement evidence for **Sebha Municipality-University Data Center / Multi-Stakeholder Data Hub** and **Murzuq Data Center hosted at Fezzan University**.

Queries:

```text
site:mfzly.com "data center"
site:mfzly.com "data hosting"
site:mfzly.com "مركز بيانات"
site:mfzly.com "مركز استضافة البيانات"
site:mfzly.com "Huawei" "data"
"Misrata Free Zone" "data hosting centre"
site:uot.edu.ly "Data Center" "Faculty of IT"
site:uot.edu.ly "مركز بيانات"
site:ungm.org Libya "data center"
site:ungm.org "UNDP-LBY" "Data Center"
site:procurement-notices.undp.org Libya "data center"
"Sebha" "Municipality-University Data Center"
"Murzuq" "municipal data center"
"Fezzan University" "data center"
```

Extract: public entity, city/popularate, procurement reference, beneficiary, university/municipality host, project scope, status, contractor if disclosed, and whether the result is a governance data hub/server room or commercial datacenter.

---

## 2. Official cloud-region and edge checks

Cloud-provider pages are **A for the existence/absence of named public regions/local zones** but do not give facility addresses.

| Provider | Official source | Libya signal checked | Enumeration use |
|---|---|---|---|
| AWS | Regions/AZ page https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and Local Zones list https://docs.aws.amazon.com/local-zones/latest/ug/available-local-zones.html | No Libya AWS Region or Local Zone found in official pages checked. Middle East/Africa nearby infrastructure exists outside Libya. | Use only for edge/partner/Outposts leads; do not infer a Libya AWS facility. |
| Microsoft Azure | Azure regions list https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Libya public Azure region found in official list checked. | Search local partners and government cloud only; do not count an Azure region. |
| Google Cloud | Locations page https://cloud.google.com/about/locations and Google data centers page https://datacenters.google/ | No Libya Google Cloud region or Google-owned data-center campus found in official pages checked. | Google Workspace/partner pages are service evidence only. |
| Oracle OCI | Public cloud regions https://www.oracle.com/cloud/public-cloud-regions/ and OCI regions docs https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No Libya public OCI region found in official lists checked. Qabas and Libyan Spider may be Oracle/Google partners, not Oracle/Google regions. | Use partner status as a lead for Tripoli cloud providers, not hyperscaler facility evidence. |

Cloud query templates:

```text
site:aws.amazon.com Libya "Local Zone"
site:docs.aws.amazon.com/local-zones Libya
site:learn.microsoft.com Azure Libya "region"
site:cloud.google.com Libya "region"
site:datacenters.google Libya
site:oracle.com Libya "cloud region"
"Libya" "cloud region" "data center" AWS
"Libya" "cloud region" Azure
"Libya" "Oracle Partner" "data center"
"Libyan Spider" "Google Cloud Partner" "data center"
```

---

## 3. Official/operator and strong-lead facility seed list

Operator pages are primary for self-claimed facilities and services; still join to municipal, GECOL, GACI, and procurement evidence before assigning precise status or capacity.

| Operator / project | Source | Libya footprint signal | Follow-up joins |
|---|---|---|---|
| LPTIC digital-transformation data centers | https://lptic.ly/digital-transformation/ | LPTIC says it is setting up comprehensive data centers in **Tripoli** and **Misrata**. | Search LPTIC/LTT subsidiaries, Tripoli/Misrata municipalities, GECOL, MFZ, LANA, Libya Herald. |
| Libya Telecom & Technology (LTT) hosting/data center | https://ltt.ly/business/Dcenter and IANA `.LY` technical contact | LTT markets data-center/hosting services and is `.LY` technical operator/contact in Tripoli. | Search LTT IDC, Alshut Road, Tripoli municipality, GECOL, Telecompaper DDoS, DataCenterMap only as C corroboration. |
| Almadar Aljadid data centers / root servers | GACI/LANA/Libya Herald searches; LPTIC Almadar page | Strong lead for **Tripoli** and **Benghazi** Almadar data centers hosting root-server infrastructure. | Prefer GACI/CIM/LANA official posts; verify Almadar facility pages, GECOL, municipal evidence. |
| Libyan Spider Tripoli data center | https://libyanspider.com/libyan-spider-opens-new-data-center-in-tripoli-to-enhance-security-and-availability/ and https://libyanspider.com/iaas/ | Official company page says a new data center opened in **Tripoli**; services include hosting/cloud/IaaS. | Search ISO certificates, Tripoli permits, GECOL, partner pages; avoid treating Google/Cloudflare partner status as a hyperscaler facility. |
| Qabas Tripoli data centers | https://qbs.ly/our-expertise/data-center-in-libya/ | Qabas states it operates Tripoli-based data centers with colocation, cloud, private enterprise solutions, backup generators, independent internet links, security, fire suppression, and future Tripoli expansion. | Search legal/operator address, Tripoli permits, GECOL, client case studies. |
| TransSahara / Tatweer Tier 3 data center | Libya Herald and DCD reports; directory leads | 2019/2022 trade coverage describes a Tier 3/Huawei modular data center, commonly tied to **Tripoli** and Benghazi-signing context; directories also list TransSahara in Benghazi/Misrata/Sabha. | Need operator page, permit, GECOL, or launch evidence before upgrading directory-only city records above C. |
| Misrata Free Zone data-hosting centre | MFZ official site plus Libya Herald report | MFZ/Misrata lead for a data-hosting centre serving investors; trade report names Huawei build, 14 racks, fibre, dual power, backup energy, cooling/security. | Search MFZ Arabic/English posts, Misrata municipality, GECOL, Huawei Libya, investment-zone records. |
| University of Tripoli Faculty of IT data center | https://uot.edu.ly/it/news-details.php?id=6538&lang=en | University page/news item identifies completion of a data-center installation in Tripoli, donated by Almadar Aljadid and Huawei Libya. | Treat as institutional/education data center; do not count as commercial colo. |
| Sebha / Murzuq municipal data hubs | https://www.ungm.org/Public/Notice/301177 | UNDP procurement describes rehabilitation/scaling of the Sebha Municipality-University Data Center and revitalization/completion of Murzuq Data Center hosted at Fezzan University. | Search UNDP documents, Sebha/Murzuq municipalities, Fezzan University, Statistics Bureau, Ministry of Social Affairs. |
| Libyana, Hatif Libya, LITC, Aljeel Aljadeed | LPTIC company pages and operator domains | Likely telecom core/switch/server-room infrastructure in Tripoli, Benghazi, Misrata, Sabha, and regional offices. | Search Arabic terms plus city names; require facility-specific proof before counting. |

---

## 4. Trade press, directories, and certification checks

High-yield secondary sources:
- Libya Herald: https://libyaherald.com/
- Libya Observer: https://libyaobserver.ly/
- Libya Monitor: https://www.libyamonitor.com/
- Data Center Dynamics: https://www.datacenterdynamics.com/
- Telecompaper: https://www.telecompaper.com/
- DataCenterMap Libya/operator pages: https://www.datacentermap.com/
- Datacenters.com and ColocationM for weak facility leads.
- Uptime Institute country awards: search https://uptimeinstitute.com/ for Libya/operator names. No reliable Libya country facility list was found during this pass; use direct search by operator/facility.

Trade/directory query templates:

```text
site:libyaherald.com Libya "data centre"
site:libyaherald.com Libya "data center"
site:libyaherald.com "Misrata Free Zone" "data hosting centre"
site:libyaherald.com "root servers" "Tripoli" "Benghazi"
site:libyaobserver.ly Libya "data center"
site:libyaobserver.ly "General Authority for Communications and Informatics" "data center"
site:datacenterdynamics.com Libya "data center"
site:telecompaper.com Libya "data centre"
site:datacentermap.com/libya "{city}"
site:uptimeinstitute.com Libya "Data Center"
"{operator}" Libya "Tier III"
"{operator}" Libya "Huawei FusionModule"
```

Use:
- **B** when trade press names the proponent, city/site, project type, date, and status and is consistent with official/operator evidence.
- **C** for directory-only facilities unless an official operator page, procurement, permit, or power record verifies the facility.
- Do not use market-size reports to create facilities.

---

## 5. Division-by-division enumeration strategy

### 5.1 Standard workflow for every popularate

1. Search Arabic and English terms with the popularate name, main cities, and operator names.
2. Search official/regulatory first: `cim.gov.ly`, `lptic.ly`, `ltt.ly`, municipality sites/pages, `gecol.ly`, free-zone/university/government pages, UNGM/UNDP.
3. Search operator pages for Qabas, Libyan Spider, LTT, Almadar, Libyana, Hatif Libya, LITC, TransSahara, MFZ, and university/municipality names.
4. Use trade press/directories to discover alternate facility names, then try to corroborate with A-grade sources.
5. Distinguish commercial/colo/cloud datacenters from institutional data hubs, telecom exchanges, university labs, server rooms, and root/DNS infrastructure.
6. Extract and normalize: `division`, `city`, `neighborhood/street/parcel`, `developer/operator`, `facility_name`, `status`, `capacity_mw`, `racks`, `power feed/backup`, `source grade`, `evidence date`, and `notes`.

### 5.2 High-yield popularates and city pivots

- **Tripoli**: highest priority. Search Tripoli Center Municipality, LPTIC/LTT, Almadar, Libyan Spider, Qabas, University of Tripoli, GACI/CIM, GECOL, and Libya Herald/DCD. City terms: `Tripoli`, `طرابلس`, `Telecom Tower`, `Al Zawia Street`, `Alshut Road`, `طريق الشط`, `Taqseem El-mayet`.
- **Benghazi**: search GACI/Almadar root-server leads, TransSahara/Benghazi directories, LTT modular/container leads, Benghazi municipality, eastern-government communications ministry pages, GECOL. Arabic: `بنغازي`.
- **Misrata**: search LPTIC Tripoli/Misrata data-center program, MFZ data-hosting centre, TransSahara Misrata, Misrata municipality, GECOL, Huawei/MFZ posts. Arabic: `مصراتة`, `المنطقة الحرة مصراتة`.
- **Sabha**: search UNDP/UNGM Sebha Municipality-University Data Center, TransSahara Sabha directory lead, Sabha municipality, University of Sabha/Fezzan University, GECOL southern-grid records. Arabic variants: `سبها`, `سبھا`.
- **Murzuq**: search UNGM/UNDP Murzuq Data Center hosted at Fezzan University, municipality and governance-data-hub terms. Arabic: `مرزق`.
- **Derna / Green Mountain / Butnan / Tobruk / Oases / Kufra**: lower-yield; focus on telecom exchanges, post-disaster reconstruction digital infrastructure, universities, hospitals, oil/gas/power control rooms, and municipal projects. Arabic: `درنة`, `الجبل الأخضر`, `طبرق`, `الكفرة`, `الواحات`.
- **Sirte / Jufra / Wadi ash Shati / Wadi al Hayaa / Ghat / Murzuq**: focus on government/university data hubs, military/oil/gas/airport/power infrastructure, and any UNDP or development-agency procurement. Arabic: `سرت`, `الجفرة`, `وادي الشاطئ`, `وادي الحياة`, `غات`.
- **Zawiya / Nuqat al Khams / Murqub / Western Mountain / Jafara / Nalut / Meadows**: expect sparse public results. Search municipal building permits, telecom/ISP offices, refinery/port/free-zone digital infrastructure, and GECOL records. Arabic: `الزاوية`, `النقاط الخمس`, `المرقب`, `الجبل الغربي`, `الجفارة`, `نالوت`, `المروج`.

Per-division query skeleton:

```text
"{division English}" Libya "data center"
"{city English}" Libya "data centre"
"{city Arabic}" "مركز بيانات"
"{city Arabic}" "مركز استضافة البيانات"
"{city Arabic}" "رخصة بناء" "اتصالات"
"{city Arabic}" "الشركة العامة للكهرباء" "اتصالات"
site:cim.gov.ly "{city Arabic}"
site:lptic.ly "{city English}" "data center"
site:ltt.ly "{city Arabic}" "مركز البيانات"
site:gecol.ly "{city Arabic}" "اتصالات"
site:ungm.org Libya "{city English}" "data center"
site:libyaherald.com "{city English}" "data centre"
site:datacentermap.com/libya "{city English}"
```

### 5.3 Negative-search standard

Mark a division `no_projects=true` only after searching:
- English + Arabic data-center terms.
- Main city and common alternate transliterations.
- GACI/LPTIC/LTT/GECOL official domains.
- Municipality/free-zone/university/government entity where present.
- Telecom/operator names and trade/directories.

For negative notes, mention the exact city variants searched and whether results only showed telecom offices, hosting services without site, ordinary data/statistics centers, or unrelated "data" uses.

---

## 6. Source grading and status rules

- **Operational**: requires official operator/government page, procurement completion, certification, or strong trade report naming launch/opening. Directory-only operational claims stay C and should be marked uncertain unless corroborated.
- **Under construction**: requires permit, tender award, official construction update, vendor deployment page, or official project page. MoUs and strategy announcements are planned/leads.
- **Planned**: official strategy/MoU/procurement concept, operator expansion plan, or public tender not yet awarded/completed.
- **Capacity**: use MW/MVA/rack counts only when directly stated. Do not infer MW from generic backup-generator mentions. Distinguish IT load, site load, generation capacity, and utility connection.
- **Location**: prefer municipality/city and street/parcel from permits or official contact pages. If only city is known, leave finer location null and note the evidence.
- **Facility type**: label as `commercial colo/cloud`, `telecom/internal`, `government/institutional`, `university/municipal data hub`, `free-zone investor service`, or `edge/root/DNS` to avoid over-counting server rooms and DNS nodes as full datacenters.
