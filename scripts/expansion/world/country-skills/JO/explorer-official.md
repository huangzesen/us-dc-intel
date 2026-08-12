# JO Explorer Official - Jordan Datacenter Enumeration via Regulators, Permits, Power, Investment, and Official Operators

Date reviewed: 2026-08-12. Country: **JO Jordan**. Division model: **12 governorates**: Ajloun, Amman, Aqaba, Balqa, Irbid, Jerash, Karak, Madaba, Ma'an, Mafraq, Tafilah, Zarqa. The Royal Hashemite Court and jordan.gov.jo both publish the same 12-governorate list; use `Tafilah/Tafileh` and `Ma'an/Maan` as spelling variants.

Scope: official, regulatory, public-sector, investment, municipal, utility, certification, and operator-primary routes for finding operational, planned, under-construction, public-institutional, colocation, cloud, cable-landing-adjacent, and edge data-center assets in Jordan.

Use `explorer-industry.md` for trade press, directories, vendors, and broader discovery. This file is the source-of-truth for source grading, official URLs, and per-governorate official strategy.

## Reliability Grades

- **A**: primary evidence for the specific claim: Royal Hashemite Court, Jordan government, Petra, TRC, MoDEE, MOIN/Invest Jordan, ASEZA, municipality/GAM permit or occupancy record, Ministry of Environment/EIA record, EMRC/NEPCO/distribution-company record, official operator facility page, official financier page such as EBRD, or Uptime Institute certificate lookup. Grade the claim narrowly: an Uptime page is A for certification and facility name, not MW; an investment incentive page is A for incentive regime, not construction status.
- **B**: strong secondary evidence: Jordan Times, Zawya, MENAFN, Roya, Al-Mamlaka, Al-Ghad, Al-Rai, Addustour, Ammon, Xinhua carrying Royal Court text, DCD, Capacity, W.Media, Telecom Review, Developing Telecoms, The Fast Mode, SAMENA Council, intaj.net newsroom, contractor/supplier pages, or operator announcements syndicated outside the operator site. Use **B+** where the report reproduces a named official/operator release and no primary page is crawlable.
- **C**: weak lead: DataCenterMap, datacenters.com, colocationm, datacentercatalog, Baxtel, Cloudscene, PeeringDB, LinkedIn/social posts, market-report teasers, snippets without source trail, or generic consultant articles. C sources can create candidates and aliases; do not promote a facility from C alone.

Grade every URL/data point separately. Example: ADH existence and Aqaba location are A from adh.jo/EBRD/Uptime; ADH 12 MW is an operator/news ceiling and must be stored as announced maximum/design capacity unless a utility or phase commissioning source gives delivered MW.

## 0. Jordan Structure and Market Facts

- Jordan has **no public national data-center registry** and no complete open planning-permit portal. Enumeration must join operator pages, certificates, official inaugurations, investment/finance records, municipal/ASEZA permit evidence, environmental records, and utility evidence.
- The market is small and telco/operator-led. Confirmed high-yield geographies are **Amman**, **Aqaba**, and **Balqa**. Irbid has institutional/digital-skills leads. The remaining governorates are mostly industrial-estate, university, government-service, telco-edge, or negative sweeps.
- No official AWS, Microsoft Azure, Google Cloud, or Oracle OCI public-cloud region list shows a Jordan public cloud region as of this review date. Treat any "Jordan cloud region" article as B/C until the provider's official region page lists Jordan.
- Count physical data centers, data halls, government/institutional facilities, and commercial colocation separately. Do not count cloud products, IXPs, POPs, submarine-cable landings, telco exchanges, university IT offices, or "information centers" unless the source names data-center infrastructure: racks, MW/MVA, Tier, hosting/colocation, cooling, generators, cloud platform, NOC/SOC, or server halls.
- Capacity discipline: record only source-stated MW/MVA/racks/m2. Keep `design_capacity`, `announced_capacity`, `phase_capacity`, and `delivered/contracted_power` separate.

Core Arabic vocabulary:

```text
مركز بيانات / مراكز البيانات
داتا سنتر
مركز بيانات سحابي / السحابة الوطنية / الحوسبة السحابية
استضافة / استضافة مشتركة / كولوكيشن
التعافي من الكوارث
رفوف / ميجاواط / ميغاواط / ك.ف.أ / محول
رخصة أبنية / رخصة بناء / إذن أشغال / رخصة مهن
تقييم الأثر البيئي / موافقة بيئية
محطة تحويل / مغذي / ربط كهربائي / مولدات / تبريد
محطة هبوط الكابلات البحرية / نقطة تبادل إنترنت
افتتاح / دشن / أطلق / قيد الإنشاء / ترسية / عقد / تمويل
```

## 1. Official / Regulatory Routes

### 1.1 TRC - Telecommunications Regulatory Commission

Primary source: **TRC Jordan**, https://trc.gov.jo/.

Verified high-value routes:

| Route | URL | Use |
|---|---|---|
| TRC homepage | https://trc.gov.jo/ | Regulator news, consultations, laws, instructions. |
| ICT-sector file list | https://trc.gov.jo/AR/List/%D9%82%D8%B7%D8%A7%D8%B9_%D8%AA%D9%83%D9%86%D9%88%D9%84%D9%88%D8%AC%D9%8A%D8%A7_%D8%A7%D9%84%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA | TRC's AR-only ICT instructions/files; verified live and last-modified 2026-03-03. |
| Telecom sector | https://trc.gov.jo/AR/List/%D9%82%D8%B7%D8%A7%D8%B9_%D8%A7%D9%84%D8%A7%D8%AA%D8%B5%D8%A7%D9%84%D8%A7%D8%AA | Telecom licences, instructions, sector files. |
| Laws | https://trc.gov.jo/AR/List/%D8%A7%D9%84%D9%82%D9%88%D8%A7%D9%86%D9%8A%D9%86 | Legal basis. |
| Regulations | https://trc.gov.jo/AR/List/%D8%A7%D9%84%D8%A3%D9%86%D8%B8%D9%85%D8%A9 | Bylaws/regulations. |
| Instructions | https://trc.gov.jo/AR/List/%D8%A7%D9%84%D8%AA%D8%B9%D9%84%D9%8A%D9%85%D8%A7%D8%AA | Instructions including ICT/telecom obligations. |
| Reports/statistics | https://trc.gov.jo/AR/List/%D8%AA%D9%82%D8%A7%D8%B1%D9%8A%D8%B1_%D9%88_%D8%A7%D8%AD%D8%B5%D8%A7%D8%A1%D8%A7%D8%AA | Sector reports; useful for operator/license context, not DC census. |
| Spectrum e-service | https://rsmd.trc.gov.jo/trcjo/ | Spectrum management portal. |
| Type approval | https://etas.trc.gov.jo/Account/Login | Equipment/type-approval portal. |
| Numbering | https://nms.trc.gov.jo/NMS/ | Numbering portal. |
| Data/postal systems | https://edds.trc.gov.jo/ | TRC data/postal e-system. |

How to use:

- TRC is **A for telecom/ICT regulatory status**. It is not a data-center registry.
- Telco-owned facilities operated by Orange, Zain, and Umniah sit behind licensed telecom/ICT operators; an independent colo/cloud provider may need ICT/data-service licensing depending on service model. Verify the current instruction text and licensed-party pages at runtime.
- Absence from TRC pages is **not proof of absence**. Treat TRC as a legal-status join after an operator/project lead is found.

Queries:

```text
site:trc.gov.jo "data center" OR "data centre" OR datacenter
site:trc.gov.jo "مركز بيانات" OR "مراكز البيانات" OR "خدمات البيانات"
site:trc.gov.jo "استضافة" OR "الحوسبة السحابية" OR "cloud"
site:trc.gov.jo "ICT" "license" Jordan
site:trc.gov.jo "المرخص لهم" "خدمات البيانات"
"هيئة تنظيم قطاع الاتصالات" "مركز بيانات" "ترخيص"
"هيئة تنظيم قطاع الاتصالات" "استضافة" "الأردن"
```

Extract: legal operator, licence/service class, decision/instruction number, issue date, covered services, and whether the source says anything facility-specific.

### 1.2 MoDEE / NITC - Digital Policy and Government Cloud

Primary sources: **MoDEE**, https://www.modee.gov.jo/Default/EN and https://www.modee.gov.jo/Default/AR; **NITC legacy route**, https://nitc.gov.jo/Default/En (currently routes into MoDEE-style pages).

Verified/high-value routes:

| Route | URL | Use |
|---|---|---|
| MoDEE homepage EN | https://www.modee.gov.jo/Default/EN | Ministry programs, news, digital economy policy. |
| e-Government Program | https://www.modee.gov.jo/En/Pages/eGovernment_Program | Government digital-services and cloud/platform context. |
| Legislation and policies | https://www.modee.gov.jo/En/List/Legislation_and_policies | Policy/strategy PDFs and legal references. |
| Digital Transformation Strategy 2026-2028 PDF | https://www.modee.gov.jo/ebv4.0/root_storage/en/eb_list_page/jordanian_digital_transformation_strategy_and_the_implementation_plan_2026-2028.pdf | A-grade national digital-infrastructure strategy; use for policy, not facility count. |
| NITC legacy/default | https://nitc.gov.jo/Default/En | Government IT/NITC context; facility details usually not public. |

How to use:

- MoDEE is **A for national digital-infrastructure policy**, e-government, national cloud/government cloud, and ministry-sponsored platform announcements.
- MoDEE/NITC infrastructure is usually **government/institutional** unless a page names a commercial colocation offer.
- Do not infer facility address, MW, or operator solely from national-cloud language.

Queries:

```text
site:modee.gov.jo "data center" OR "data centre" OR datacenter
site:modee.gov.jo "مركز بيانات" OR "مراكز البيانات"
site:modee.gov.jo "cloud" "government" OR "Jordan Cloud"
site:modee.gov.jo "السحابة الوطنية" OR "السحابة الحكومية"
site:nitc.gov.jo "data center" OR "cloud" OR "مركز بيانات" OR "استضافة"
"National Cloud" Jordan "data center" OR hosting
"وزارة الاقتصاد الرقمي والريادة" "مركز بيانات" OR "السحابة"
```

### 1.3 MOIN / Invest Jordan / ASEZA / JIEC - Investment, Special Zones, Land

Primary sources:

| Entity | URL | Use |
|---|---|---|
| Ministry of Investment | https://www.moin.gov.jo/default/en | Investment-law and project/incentive context. |
| Invest Jordan | https://invest.jo/ | Per-governorate investment opportunity map and sector profiles. |
| Investment Environment Law legacy page | https://ida.jo/Pages/viewpage.aspx?pageID=52 | Legacy Investment Development Agency reference; verify current law through MOIN. |
| ASEZA homepage | https://aseza.jo/Default/En | Aqaba Special Economic Zone authority, permitting/investment context. |
| ASEZA investment incentives | https://aseza.jo/EN/Pages/Investment_Incentives | Verified live; A for single-window/incentive regime. |
| ASEZA start-your-work route | https://aseza.jo/En/Pages/Start_Your_Work_Now | Investor/licensing workflow. |
| Invest Jordan ASEZA profile | https://invest.jo/en/aqaba-special-economic-zone | Aqaba special-zone profile. |
| Jordan Industrial Estates Corporation | https://jiec.com/ | Industrial-estate land and governorate siting leads. |

How to use:

- MOIN/Invest Jordan/ASEZA/JIEC are **A for incentives, land, zone jurisdiction, and official opportunities**. They are not proof of a DC facility unless the page names a data-center project.
- **Aqaba projects inside ASEZA** should be checked through ASEZA routes, not ordinary municipal permit assumptions.
- JIEC estates matter for low-yield governorates (Zarqa, Mafraq, Karak, Ma'an, Irbid, Salt/Balqa, Aqaba) because DCs may be described as ICT/logistics/industrial infrastructure.

Queries:

```text
site:moin.gov.jo "data center" OR "data centre" OR "مركز بيانات"
site:invest.jo "data center" OR "مراكز البيانات" OR cloud
site:aseza.jo "data center" OR "digital hub" OR "Aqaba Digital Hub"
site:aseza.jo "مركز بيانات" OR "مركز العقبة الرقمي" OR "كابل بحري"
site:jiec.com "data center" OR "ICT" OR "مركز بيانات" OR "استضافة"
"Aqaba Special Economic Zone" "data center" permit OR license
"سلطة منطقة العقبة الاقتصادية الخاصة" "مركز بيانات" OR "مركز العقبة الرقمي"
```

### 1.4 Municipal / Building / Occupancy Permits

Jordanian building permits are municipal/local. There is no single national planning search comparable to UK planning portals.

Verified official routes:

| Route | URL | Use |
|---|---|---|
| Greater Amman Municipality e-services | https://www.amman.jo/ | GAM services, including planning/building services and tower permits. |
| GAM building permit request tracking | https://www.amman.jo/ar/building/ChkLand.aspx | Verified live AR service for following a building-permit request; needs known identifiers. |
| ASEZA | https://aseza.jo/Default/En | Aqaba special-zone investment/licensing/permitting authority. |

How to use:

- Permit records are **A when record-specific**: permit number, parcel, owner, use, date, municipality, status, supervising engineer, and occupancy/operation approval.
- Public search is limited and often requires a parcel/permit number or login. Use permits to confirm known projects, not as the only discovery path.
- For non-Amman governorates, search municipality names in Arabic and local press. Many municipalities publish service cards or meeting/news items rather than searchable permit ledgers.

Queries:

```text
"رخصة أبنية" "مركز بيانات" الأردن
"رخصة بناء" "مركز بيانات" الأردن
"إذن أشغال" "مركز بيانات" الأردن
site:amman.jo "مركز بيانات" OR "data center" OR "رخصة أبنية"
"أمانة عمان الكبرى" "مركز بيانات" "رخصة"
"بلدية" "مركز بيانات" "رخصة أبنية" إربد OR الزرقاء OR السلط OR الكرك OR مادبا
"Aqaba" "data center" "building permit" ASEZA
"سلطة منطقة العقبة" "رخصة" "مركز العقبة الرقمي"
```

### 1.5 Environment / EIA

Primary source: **Ministry of Environment**, https://www.moenv.gov.jo/.

Use:

- Ministry of Environment, EIA regulations, and project-specific approvals are **A for environmental clearance** when a record names the project.
- Data centers may not appear as a named EIA category. Search trigger activities: diesel generators, fuel storage, batteries, cooling/chillers, water abstraction, wastewater, noise, e-waste, substations, and large construction.
- Keep EIA status separate from operational status. Environmental approval does not prove construction completion.

Queries:

```text
site:moenv.gov.jo "data center" OR "مركز بيانات" OR "مراكز البيانات"
site:moenv.gov.jo "تقييم الأثر البيئي" "بيانات"
"تقييم الأثر البيئي" "مركز بيانات" الأردن
"وزارة البيئة" "مركز بيانات" "موافقة"
"Environmental Impact Assessment" "data center" Jordan
"مولدات ديزل" "مركز بيانات" الأردن
"خزانات وقود" "مركز بيانات" الأردن
"تبريد" "مركز بيانات" "تقييم الأثر"
```

### 1.6 Power / Grid - EMRC, NEPCO, JEPCO, IDECO, EDCO

Primary sources:

| Entity | URL | Use |
|---|---|---|
| EMRC | https://www.emrc.gov.jo/ | Electricity regulation, tariffs, licences, sector reports. |
| NEPCO | https://www.nepco.com.jo/en/default.aspx | Transmission grid owner/operator and single-buyer context; annual reports and tenders. |
| JEPCO | https://www.jepco.com.jo/en | Distribution in Amman/Zarqa/Madaba/Balqa area; confirm exact concession at runtime. |
| IDECO | https://www.ideco.com.jo/ | Distribution in north/northeast area including Irbid/Jerash/Ajloun/Mafraq; confirm exact concession at runtime. |
| EDCO | https://www.edco.jo/ | Distribution in south/east including Karak/Tafilah/Ma'an/Aqaba and areas outside JEPCO/IDECO; annual reports also disclose IDECO ownership context. |

Official power evidence is decisive for large DCs:

- NEPCO high-voltage connection, substation, transformer, or transmission tender.
- Distribution-company feeder/transformer/large-load connection.
- EMRC licence/tariff/large-consumer record.
- Project tender naming UPS, generators, MV/LV works, chillers, or substations.

Queries:

```text
site:nepco.com.jo "data center" OR "مركز بيانات" OR "Aqaba Digital Hub"
site:nepco.com.jo "substation" "Aqaba" OR "Amman" OR "Ain Al-Basha"
site:emrc.gov.jo "data center" OR "مركز بيانات" OR "large consumer"
site:jepco.com.jo "مركز بيانات" OR "data center" OR "محطة تحويل"
site:ideco.com.jo "مركز بيانات" OR "data center" OR "محطة تحويل"
site:edco.jo "مركز بيانات" OR "data center" OR "محطة تحويل"
"NEPCO" "data center" Jordan connection
"محطة تحويل" "مركز بيانات" الأردن
"كهرباء" "مركز بيانات" العقبة OR عمان OR الزرقاء OR إربد
```

Governorate utility guide for first-pass joins:

| Governorate | First utility to check | Notes |
|---|---|---|
| Amman | JEPCO, then NEPCO for large loads | GAM permit joins. |
| Zarqa | JEPCO | Industrial estate/QIZ leads. |
| Madaba | JEPCO | Institutional/municipal leads. |
| Balqa | JEPCO | Orange Ain Al-Basha; Salt/Al-Baqa'a terms. |
| Irbid | IDECO | Greater Irbid, universities, Al-Hassan estate. |
| Jerash | IDECO | Low yield. |
| Ajloun | IDECO | Low yield. |
| Mafraq | IDECO/EDCO boundary check | Prince Hassan Industrial City/east-area leads; confirm utility by site. |
| Karak | EDCO | Industrial estate/university. |
| Tafilah | EDCO | University/institutional. |
| Ma'an | EDCO | Development area/renewables. |
| Aqaba | EDCO plus NEPCO | ASEZA/ADH/cable landing. |

### 1.7 Official Cloud Region Checks

Re-check these provider pages before every production enumeration run:

| Provider | Official region page |
|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ |
| Microsoft Azure | https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies |
| Google Cloud | https://cloud.google.com/about/locations |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ |

As of 2026-08-12, do not count AWS/Azure/GCP/OCI Bahrain, UAE, Israel, Qatar, Saudi Arabia, or other regional capacity as Jordan. Local operator clouds (Orange, Zain, Umniah, ADH, MoDEE/NITC) must be tied to a physical Jordan facility or government hosting record.

## 2. Official / Primary Facility Seeds

| Facility / project | Governorate | URLs | Current evidence and grading |
|---|---|---|---|
| Aqaba Digital Hub (ADH) - Mega Data Center / Data Hall 1 & CLS | Aqaba | https://adh.jo/ ; https://adh.jo/hub/mega-data-center ; https://adh.jo/about/company ; https://www.ebrd.com/home/work-with-us/projects/psd/56562.html ; https://uptimeinstitute.com/component/tierachievement/datacenter/aqaba-digital-hub-data-center-data-hall-1--cls-unit/1718 ; https://uptimeinstitute.com/uptime-institute-awards/list | **A** for existence, Aqaba location, carrier-neutral DC/cable-landing/cloud/connectivity role, EBRD financing, and Uptime-listed facility/certification. EBRD states up to JOD 10m senior secured loan for growth of ADH's data-centre/fibre/subsea operation. ADH claims Jordan's largest carrier-neutral DC and AI-ready infrastructure. Uptime list shows TCDD/TCCF Tier III for Data Hall 1 & CLS Unit, Phase 1. Capacity claims vary by source/hall; record only exact source wording. |
| ADH City Data Center | Aqaba | https://adh.jo/hub/city-data-center | **A operator claim** for a Tier III-certified city-center carrier-neutral colocation/hosting/managed-services facility active since 2020. Verify whether it is a distinct site/data hall from the Mega DC before dedupe. |
| Orange Jordan - Ain Al-Basha Data Center | Balqa | https://intaj.net/orange-jordan-announces-the-inauguration-of-the-kingdoms-newest-most-sustainable-and-secure-data-center/ ; https://www.fananews.com/language/en/minister-of-digital-economy-opens-orange-jordans-data-centre-in-ain-al-basha/ | **B+/A-**: intaj/FANA carry operator/official inauguration reporting. Inaugurated 2025-05-28 in Ain Al-Basha, Balqa; source states designed/expandable to 500 racks and total capacity of 5 MW. Treat 5 MW as announced capacity, not delivered load. Seek Orange primary page and JEPCO/permit records for A-grade backfill. |
| Orange Jordan - Marj Al-Hammam Data Center | Amman | https://orange.jo/sites/default/files/documents/hosting_data_centers.pdf ; https://uptimeinstitute.com/component/tierachievement/datacenter/marj-alhammam-data-center/830 ; https://uptimeinstitute.com/uptime-institute-awards/client/jordan-telecom-group--orange-jordan/532 | **A** for operator hosting/DC service brochure and Uptime certification record; **B/C** for any capacity/address from directories. Use Amman/GAM/JEPCO joins for locality details. |
| Orange Jordan - Hashem Data Center | Amman | https://www.thefastmode.com/technology-solutions/40316-orange-jordan-s-hashem-data-center-earns-tier-iii-design-certification ; https://www.samenacouncil.org/samena_daily_news?news=104925 ; https://uptimeinstitute.com/uptime-institute-awards/client/jordan-telecom-group--orange-jordan/532 | **B+** for March 2025 Tier III Design certification and Medical City/Hashem naming from telecom press/SAMENA; check Uptime client/list pages for current certificate status. Do not use datacenters.com address/capacity without corroboration. |
| Zain Jordan - The Bunker | Amman | https://www.jo.zain.com/english/Business/Pages/CloudandHosting_Thebunker.aspx ; https://www.jo.zain.com/english/Business/Pages/FinanceAndInsurance_CloudandHostingSolutions.aspx ; https://uptimeinstitute.com/uptime-institute-awards/datacenter/zain-data-center--disaster-recovery-bunker/966 | **A** for Zain official page naming The Bunker at King Hussein Business Park, Amman, as a Tier III regional data/information storage facility with 99.982% availability claim; **A** for Uptime facility page if certificate details are present. Capacity remains unverified unless official source states it. |
| Umniah / Batelco Jordan - Data Center / Dahiyat Al-Rasheed colocation room | Amman | https://www.umniah.com/business/cloud/datacenter-colocation-service/ ; https://cloud.umniah.com/datacenter.php ; https://www.umniah.com/explore-umniah/umniah-data-center-is-the-first-and-only-in-jordan-to-grant-the-tier-iii-constructed-facility-certification/ ; https://uptimeinstitute.com/uptime-institute-awards/list/datacenter/dahiyat-alrasheed-colocation-room/921 | **A** for official colocation/DC service and Uptime-listed Dahiyat Al-Rasheed colocation room; official pages state industrial power-grid connection, redundant network, physical security/biometrics, and Tier III constructed-facility claim. Capacity not public. |
| Umniah new South Amman / large Tier III project | Amman | https://www.umniah.com/explore-umniah/umniah-data-center/ ; https://trismartgroup.com/new-page-60 | **A-/B** lead: Umniah official page says a new South Amman data center; Trismart says commencement of a new Tier III data center in Amman. Verify status, site, phase, and whether it is distinct from Dahiyat Al-Rasheed before counting. |
| NITC / MoDEE government hosting / national cloud | Amman likely; verify | https://www.modee.gov.jo/Default/EN ; https://www.modee.gov.jo/En/Pages/eGovernment_Program ; https://nitc.gov.jo/Default/En | **A for policy/government program**, **B/C for facility existence** unless a procurement/contract names a government data center. Count only as institutional/government when facility evidence is found. |
| Kalaam Telecom Jordan | Unverified | https://kalaam-telecom.com/ | **C/B lead only**: regional telecom/DC services and Jordan presence do not prove a Jordan DC. Count only after an official Jordan facility page, permit, customer page, or certificate appears. |

## 3. Governorate-by-Governorate Official Strategy

Run all 12 governorates even when expected yield is low. Record negative sweeps with terms used and date.

| Governorate (EN / AR) | Priority | Known seeds / expected yield | Official surfaces and strategy |
|---|---|---|---|
| **Amman / عمان** | HIGH | Orange Marj Al-Hammam; Orange Hashem; Zain The Bunker at King Hussein Business Park; Umniah/Dahiyat Al-Rasheed and South Amman lead; MoDEE/NITC; banks/universities; possible Kalaam lead. | Start with operator pages + Uptime country/client list. Join GAM permits (`amman.jo`, ChkLand), JEPCO/NEPCO, TRC licence context, MoDEE/NITC, KHBP, Medical City, Marj Al-Hammam, South Amman, Dahiyat Al-Rasheed, Sahab, Al-Muwaqqar. Directories are C seeds only. |
| **Aqaba / العقبة** | HIGH | ADH Mega Data Center, ADH City Data Center, cable landing/IXP/cloud services. | Use adh.jo, EBRD 56562, Uptime ADH, ASEZA incentives/licensing, EDCO/NEPCO connection evidence, Ministry of Environment, Royal Court/Petra/Zawya/Xinhua for inaugurations. Distinguish data centers from cable landing and AqabaIX. |
| **Balqa / البلقاء** | MEDIUM-HIGH | Orange Ain Al-Basha DC at/near former Al-Baqa'a satellite-station site; Salt/Al-Baqa'a institutional leads. | Search Orange/intaj/FANA, JEPCO, Balqa/Salt/Ain Al-Basha municipality, GAM spillover, Uptime, permits and power. Arabic variants: عين الباشا, البقعة, السلط. |
| **Irbid / إربد** | MEDIUM | MoDEE Northern Platform/digital-skills center lead; Yarmouk University/JUST institutional IT; Al-Hassan Industrial Estate; telco edge. | Use MoDEE/Petra for platform announcements, Greater Irbid Municipality, IDECO, JIEC Al-Hassan, universities. Count only if data-center infrastructure is named. |
| **Zarqa / الزرقاء** | MEDIUM-LOW | Industrial city/QIZ, municipal/government IT, telco edge, Amman spillover. | Query Zarqa municipality, JEPCO, JIEC estates, TRC/telco operators, Arabic local press. Reject generic industrial digitization unless hosting/racks/MW named. |
| **Mafraq / المفرق** | LOW | Prince Hassan Industrial City, logistics/border/refugee-response digital infrastructure, telco edge. | Query JIEC, Mafraq municipality, IDECO/EDCO boundary, investment map, Arabic press. Most results likely edge or institutional. |
| **Karak / الكرك** | LOW | Al-Hussein bin Abdullah II Industrial Estate; Mutah University; government services. | Query JIEC, Karak municipality, EDCO, Mutah University procurement/IT. Need rack/hosting/DC terms before counting. |
| **Ma'an / معان** | LOW-MEDIUM | Ma'an Development Area, renewables-adjacent land/power, university/institutional leads. | Query MOIN/Invest Jordan, Ma'an Development Area, Ma'an municipality, EDCO/NEPCO, Ministry of Environment. Watch for investment MoUs; keep planned until permit/construction. |
| **Madaba / مادبا** | LOW | Municipality/institutional IT, Amman spillover. | Query Madaba municipality, JEPCO, universities/hospitals, Arabic press. Do not count fintech/training MoUs as DCs. |
| **Tafilah / الطفيلة** | LOW | Tafila Technical University, renewables/wind/solar context, telco edge. | Query Tafilah municipality, EDCO, university procurement, Arabic press. Avoid confusing renewable power projects with DC projects. |
| **Jerash / جرش** | LOW | Jerash University, government/telco edge. | Query Jerash municipality, IDECO, university, Arabic press. Expected negative for commercial colo. |
| **Ajloun / عجلون** | LOW | Ajloun National University, government/telco edge. | Query Ajloun municipality, IDECO, university, Arabic press. Expected negative for commercial colo. |

Per-governorate official query template:

```text
"{governorate}" Jordan ("data center" OR "data centre" OR datacenter OR colocation OR hosting OR cloud)
"{governorate_ar}" ("مركز بيانات" OR "مراكز البيانات" OR "داتا سنتر" OR "استضافة" OR "سحابة")
site:modee.gov.jo "{governorate}" OR "{governorate_ar}" "مركز بيانات" OR cloud
site:trc.gov.jo "{governorate_ar}" "مركز بيانات" OR "استضافة"
site:petra.gov.jo "{governorate_ar}" "مركز بيانات" OR "سحابة" OR "رقمي"
site:nepco.com.jo "{governorate}" OR "{governorate_ar}" "data center" OR "محطة تحويل"
site:{utility_domain} "{governorate_ar}" "مركز بيانات" OR "محطة تحويل" OR "ربط"
"{municipality_ar}" "رخصة أبنية" "مركز بيانات"
"{operator}" "{governorate}" "data center" OR "{governorate_ar}" "مركز بيانات"
```

Name variants:

```text
Ajloun OR عجلون
Amman OR عمان
Aqaba OR العقبة
Balqa OR Balqa' OR Al-Balqa OR البلقاء OR السلط OR Salt
Irbid OR إربد
Jerash OR Jarash OR جرش
Karak OR Al Karak OR الكرك
Madaba OR مادبا
Ma'an OR Maan OR معان
Mafraq OR المفرق
Tafilah OR Tafileh OR Tafila OR الطفيلة
Zarqa OR الزرقاء
Ain Al-Basha OR عين الباشا
Al-Baqa'a OR Baqaa OR البقعة
Marj Al-Hammam OR مرج الحمام
Dahiyat Al-Rasheed OR ضاحية الرشيد
King Hussein Business Park OR مجمع الملك الحسين للأعمال
Medical City OR المدينة الطبية
```

## 4. Verification Rules and Pitfalls

- **No registry**: no_projects requires documented searches across official/operator/certificate/press/power/municipal surfaces. Do not infer absence from TRC or permit portals alone.
- **Official policy is not facility evidence**: MoDEE/MOIN/ASEZA strategies and incentives are A for policy but not operational status.
- **Certificate scope**: Uptime is A for named facility and certification type/status. It does not prove capacity, current utilization, customer availability, or exact address unless listed.
- **Capacity ceilings**: preserve source verbs such as `designed to accommodate`, `expandable to`, `up to`, `total capacity`, `phase 1`. Do not convert to operational IT load.
- **Aqaba dedupe**: ADH has City Data Center, Mega Data Center, cable landing, AqabaIX, cloud, and academy/newsroom pages. Dedupe by physical hall/campus and do not count IX/cable landing as separate DCs.
- **Amman dedupe**: Orange Marj Al-Hammam, Orange Hashem/Medical City, Umniah Dahiyat Al-Rasheed, Umniah South Amman, Zain Bunker/KHBP, and any directory aliases must be reconciled by operator + campus.
- **Arabic traps**: `مركز معلومات` often means an administrative information office. `مركز تكنولوجيا` or `منصة` may be training/startup space. Require DC infrastructure vocabulary.
- **Acronym traps**: EDCO electricity vs JEDCO SME/development agency; JIC legacy investment body now under MOIN; NITC vs NTC; TRC Jordan vs other-region regulators; ADH vs unrelated health/hospital acronyms.
- **Cloud-region trap**: local cloud services are not hyperscaler regions; regional AWS/Azure/GCP/OCI regions are not Jordan facilities.
- **Municipal limits**: GAM/ASEZA/municipal services can be login-gated or identifier-gated. Record search limitations rather than treating non-result as negative evidence.

## 5. Recommended Official Enumeration Pipeline

1. Pull Uptime country/list/client pages for Jordan and normalize facility names: ADH, Zain, Orange, Umniah.
2. Sweep official operator pages: ADH, Orange Jordan, Zain Jordan, Umniah; capture only directly stated facility, status, certification, capacity, and service claims.
3. Join official finance/inauguration: EBRD ADH, Royal Court/Petra/Zawya/Xinhua for ADH, intaj/FANA/Orange for Ain Al-Basha, MoDEE for policy/government-cloud context.
4. Run Amman, Aqaba, and Balqa deep dives through GAM/ASEZA/municipality, JEPCO/EDCO/NEPCO, Ministry of Environment, and local Arabic queries.
5. Run the remaining nine governorates with the table templates; record negative sweeps and classify institutional/telco-edge separately from commercial colocation.
6. Re-check AWS/Azure/GCP/OCI official region lists.
7. Reconcile directories only after A/B evidence exists; mark unresolved directory items as C candidates.
8. For each accepted record, store source bundle: one existence/status source, one locality source precise enough for governorate assignment, and one capacity/certification/source-specific claim if available.

Minimum strong record:

```text
A or B+ existence/status source
+ governorate-locality source
+ separate source for capacity/certification if the record stores MW/racks/Tier
```

Use `no_projects` for a governorate only after checking English/Arabic names, transliterations, operator names, municipality terms, JIEC/Invest Jordan, utility terms, and official/news source scopes.

<!-- END -->
