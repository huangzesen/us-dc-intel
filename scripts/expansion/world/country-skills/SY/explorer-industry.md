# SY Explorer Industry - Syria Datacenter Press, Vendor, and Market Discovery

Date reviewed: 2026-08-12. Scope: Syrian Arab Republic (SY). Use this file for non-official discovery of datacenter, cloud, hosting, subsea, IXP, telecom, vendor, and industrial-park leads, then verify against official or operator-primary evidence.

Reliability grades:

- **A**: primary or official source used from the industry workflow: SANA, MOCT, SYTPRA, SIA, Syrian Telecom/operator pages, official cloud-region pages, Uptime Institute certification list.
- **B**: established trade press, wire services, legal/investment guides, vendor case studies, and named conference material.
- **C**: directories, LinkedIn/X/Instagram/Facebook/Telegram, market-report PR, old promotional items, commercial listings, and unsourced local press.

Market posture: Syria remains a very thin commercial datacenter market. Most positive evidence is program-level, connectivity-level, or small private/government hosting. Treat the current market as discovery-heavy and facility-light. The strongest verified facility-style leads during review are Mijad/Sham Cloud in Damascus and the Ministry of Higher Education IT center in Damascus; both still need operator/spec/certification follow-up before being treated like conventional commercial colocation inventory.

## 1. High-Signal Industry Sources

| Source | URL / search surface | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/tags/syria/ | Best data-center/trade feed for Go MoU, STC/SilkLink, Medusa, Aletar outage, and future build announcements. | B |
| Capacity Media | `site:capacitymedia.com Syria Tartous Medusa Ugarit cable data centre` | Wholesale/carrier and cable-routing discovery. | B |
| Developing Telecoms | https://developingtelecoms.com/ | Ugarit/cable/telecom construction and maintenance agreements. | B |
| Submarine Networks | https://www.submarinenetworks.com/ | Aletar, Medusa, landing-point, and route-diversity context. | B/C |
| TeleGeography Submarine Cable Map | https://www.submarinecablemap.com/landing-point/tartous-syria | Landing-point inventory and cable cross-checks. | B/C |
| Reuters/AP/AFP | site-scoped searches | Regulatory, sanctions, investment, telecom, and power milestones. | B+ |
| Syria Report | https://syria-report.com/ | Business, investment, telecom, energy, and company-registration leads. | B |
| Enab Baladi English | https://english.enabbaladi.net/ | Syrian local telecom, Ugarit, policy, and internet-service reporting. | B |
| Rest of World | https://restofworld.org/ | Syrian tech ecosystem and startup context; usually not facility proof. | B-/C+ |
| Legal/investment guides | Examples: Al Arabia Law, SIMA Insights, ASBC, Ethmaar | Ownership caps, licensing routes, and sector-entry rules; verify against SIA/SYTPRA. | B-/C+ |
| Uptime Institute | https://uptimeinstitute.com/tier-certification/tier-certification-list | Certification verification. Use only direct list/certificate evidence. | A if matched |
| Directories | Data Center Map, Baxtel, Cloudscene, Datacenters.com, PeeringDB | Expect sparse/no Syrian results; use as C leads only. | C |

Core industry queries:

```text
site:datacenterdynamics.com Syria ("data center" OR "data centre" OR SilkLink OR Medusa OR Ugarit)
site:capacitymedia.com Syria ("data centre" OR "submarine cable" OR Tartous OR Ugarit)
site:developingtelecoms.com Syria ("Ugarit" OR "Syrian Telecom" OR "submarine cable")
site:submarinenetworks.com Syria ("Aletar" OR "Medusa" OR "Tartous")
site:syria-report.com Syria ("telecom" OR "data centre" OR "data center" OR electricity)
site:english.enabbaladi.net Syria ("Ugarit" OR "SilkLink" OR "internet" OR "data center")
```

## 2. Verified Industry and Press Anchors

### SilkLink / STC

- DCD, 2026-02-12: https://www.datacenterdynamics.com/en/news/stc-group-wins-bid-to-run-syrias-silklink-telecoms-infrastructure/
- Official RFI cross-check: https://silklink.moct.gov.sy/pages/introduction.html

DCD reports STC won the SilkLink bid and describes a large fiber-network investment with datacenters and submarine cable landing stations. The official SilkLink RFI confirms the 4,500 km-class backbone concept indirectly via project scope, 10 Tbps initial/25 Tbps future capacity, five IXPs, Syrian Telecom operation, and MOCT regulation. Grade **B for DCD build details**, **A for official RFI scope**. Do not count SilkLink datacenters until an official or operator source names specific facilities.

Queries:

```text
"STC" "SilkLink" Syria "data centers"
"سيلك لينك" "STC" "مراكز بيانات"
"SilkLink" "Damascus" "Aleppo" "Tartous" "Palmyra" "Qamishli"
```

### Go / Etihad Atheeb MoU

- DCD, 2025-07-28: https://www.datacenterdynamics.com/en/news/saudi-arabian-telco-go-signs-data-center-mou-with-syrian-government/

This is a datacenter-relevant MoU with the Syrian government, but DCD states facility details are unclear. Grade **B MoU lead**. Record `status=MoU`, not planned/operational facility, unless MOCT/SIA/SANA later names site, land, capacity, or construction.

Queries:

```text
"Etihad Atheeb" OR "Go Telecom" Syria "data center" MoU
"جو" OR "اتحاد عذيب" "سوريا" "مركز بيانات"
```

### Medusa / Tartous

- Medusa official news: https://medusascs.com/news/tartous-syria-medusa-signs-agreement-with-syria-telecom-to-establish-a-new-east-to-west-route/
- MOCT official project page: see official methodology file.
- DCD Syria tag also tracks Medusa Syria coverage: https://www.datacenterdynamics.com/en/tags/syria/

Classify as **connectivity/landing station** in Tartus. Landing stations may contain telecom rooms, but they are not commercial datacenters without hosting/colo evidence.

Queries:

```text
"Medusa" "Tartous" "Syria Telecom" "landing"
"Medusa" "Syria" "data center" OR "landing station"
"طرطوس" "Medusa" OR "ميدوسا" "كابل بحري"
```

### Ugarit / Ugarit 2

- SANA English first-phase official story: https://sana.sy/en/syria/354083/
- Developing Telecoms Ugarit maintenance/construction coverage: https://developingtelecoms.com/telecom-technology/optical-fixed-networks/20663-maintenance-agreement-signed-for-syria-cyprus-cable.html

Use Ugarit for submarine connectivity and Tartous/Cyprus route discovery. Do not infer a datacenter unless a landing-station facility with hosting/colo is named.

Queries:

```text
"Ugarit 2" OR "UGARIT-2" "Syrian Telecom" CYTA UNIFI
"أوغاريت 2" OR "Ugarit" "طرطوس" "قبرص"
"UNIFI Communications" "Syria" "data center" OR "submarine cable"
```

### Aletar / Existing Cable Risk

- DCD, 2026-06-18: https://www.datacenterdynamics.com/en/news/syria-provides-internet-through-alternative-routes-after-sabotage-of-subsea-cable/
- Submarine Networks Aletar coverage: https://www.submarinenetworks.com/en/systems/asia-europe-africa/aletar/syrian-telecom-claims-sabotage-on-aletar

Use as route-diversity and outage-risk evidence. It supports why Tartus and alternate corridors matter; it is not datacenter evidence.

### Mijad / Sham Cloud

- SANA official anchor: https://sana.sy/economy/2464512/
- LinkedIn lead: https://sy.linkedin.com/company/mijadtechnology
- Sham Cloud social lead: https://www.facebook.com/shamcloud/
- Uptime verification surface: https://uptimeinstitute.com/tier-certification/tier-certification-list

SANA reports Mijad Technical Services, Sham Cloud, an agreement with Damascus University, and an MoU involving CanaGulf and Uptime Institute representation to qualify datacenters. Treat this as the strongest current private Syrian datacenter/cloud lead. Grade **A for SANA-reported existence/agreements**, **C for social claims**, and **A only if Uptime list confirms a certification**.

Queries:

```text
"Mijad" OR "مجاد" "data center" Syria
"Mijad Technology" "Sham Cloud" "Tier III"
"مجاد" "شام كلاود" "مركز البيانات"
site:uptimeinstitute.com "Syria" "Mijad" OR "Sham Cloud"
```

### Ministry of Higher Education IT Center

- SANA official anchor: https://sana.sy/education/2350216/

This is a public-sector/education hosting lead in Damascus. It names data-center management and hosting services, but not commercial colocation. Grade **A for government/education facility function**.

Queries:

```text
"مركز تكنولوجيا المعلومات" "دمشق" "مركز بيانات" "استضافة"
"COMSATS" "COMSTECH" "Damascus" "data center"
"وزارة التعليم العالي" "مركز بيانات" "استضافة"
```

## 3. Operator and Vendor Lead List

| Entity | Source surfaces | How to use | Grade |
|---|---|---|---|
| Syrian Telecom | https://www.syriantelecom.com.sy/ ; https://www.telecomsy.com/ | Backbone, international gateway, landing-station, hosting-service, and exchange/POP leads. | A for own claims |
| STC Group | DCD + STC official search | SilkLink operator/developer lead; verify site details with MOCT/SANA/STC. | B/A |
| Go / Etihad Atheeb | DCD + company releases | MoU lead only. | B |
| Mijad Technical Services / Sham Cloud | SANA + social/company pages | Private cloud/datacenter lead; verify certification and address. | A/C |
| CanaGulf | SANA + company search | Certification/advisory partner lead for Mijad and Syrian DC standards. | B/C |
| Uptime Institute | Official certification list | Confirms tier only if facility appears directly. | A |
| Syriatel | official pages + searches | Mobile core/network rooms; not colo unless hosting/DC service is named. | A/C |
| MTN Syria / Zain | SANA/SYTPRA + operator pages | Licence and future mobile-core infrastructure; avoid double-counting during rebrand. | A for licence |
| UNIFI / CYTA | Ugarit coverage and company releases | Submarine cable, route, landing-station leads. | B/A if official |
| Medusa consortium | Medusa official + MOCT + DCD | Tartous landing lead. | A/B |
| Banks / public sector | Central Bank, commercial banks, vendor case studies | Enterprise datacenter leads; normally private and hard to verify. | B/C |

Operator/vendor queries:

```text
"Syrian Telecom" ("hosting" OR "colocation" OR "data center" OR "landing station")
"الشركة السورية للاتصالات" ("استضافة" OR "مركز بيانات" OR "محطة إنزال")
"Syriatel" OR "سيريتل" ("مركز بيانات" OR "استضافة" OR "core network")
"Zain Syria" OR "زين سوريا" ("data center" OR "core network" OR "5G")
"CanaGulf" "Syria" "data center" "Uptime"
"Uptime Institute" "Syria" "data center"
"Central Bank of Syria" OR "مصرف سورية المركزي" ("data center" OR "مركز بيانات")
```

## 4. Cloud and Directory Checks

Official public-cloud region pages remain negative for Syria:

- AWS: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Azure: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud: https://cloud.google.com/about/locations
- Oracle Cloud: https://www.oracle.com/cloud/public-cloud-regions/

Use directories only as leads:

```text
site:datacentermap.com Syria "data center"
site:baxtel.com Syria "data center"
site:cloudscene.com Syria "data center"
site:datacenters.com Syria "data center"
site:peeringdb.com Syria "IXP" OR "Syrian Telecom"
site:uptimeinstitute.com/tier-certification/tier-certification-list Syria
```

Negative directory results are useful. Record them as `no directory/certification listing found on date checked`, not as proof that no private/government facility exists.

## 5. Arabic and English Search Library

Core Arabic terms:

- Data center: `مركز بيانات`, `مراكز البيانات`, `مركز المعطيات`, `مراكز المعطيات`
- Hosting/cloud: `استضافة`, `خدمات الاستضافة`, `خوادم`, `حوسبة سحابية`, `سحابة`, `سحابة سيادية`
- Connectivity: `نقطة تبادل إنترنت`, `نقطة تبادل`, `كابل بحري`, `محطة إنزال`, `ألياف ضوئية`
- Project status: `مذكرة تفاهم`, `اتفاقية`, `ترخيص`, `إجازة استثمار`, `تخصيص أرض`, `وضع حجر الأساس`, `بدء الأعمال`, `افتتاح`, `تدشين`, `إطلاق`
- Power: `كهرباء`, `محطة تحويل`, `أحمال`, `مولدات`, `طاقة شمسية`, `بطاريات`, `ميغاواط`

General Arabic queries:

```text
"سوريا" ("مركز بيانات" OR "مركز المعطيات" OR "مراكز البيانات") ("شركة" OR "استثمار" OR "افتتاح")
"سوريا" ("استضافة" OR "حوسبة سحابية" OR "خوادم") ("مجاد" OR "شام كلاود" OR "وزارة الاتصالات")
"سوريا" "مذكرة تفاهم" "مركز بيانات"
"سوريا" "تطوير مراكز البيانات" "Uptime"
"سوريا" "كابل بحري" "طرطوس" "محطة إنزال"
"سوريا" "نقطة تبادل إنترنت" "سيلك لينك"
```

General English queries:

```text
"Syria" ("data center" OR "data centre" OR datacenter OR datacentre) ("Damascus" OR "Aleppo" OR "Tartous")
"Syria" ("cloud" OR hosting OR colocation) ("Mijad" OR "Sham Cloud" OR "Syrian Telecom")
"Syria" "national data center"
"Syria" "data center" ("MoU" OR "memorandum" OR "investment")
"Syria" "cable landing station" ("Tartous" OR "Latakia")
"Syria" ("IXP" OR "internet exchange point") ("Damascus" OR "Aleppo" OR "Qamishli" OR "Palmyra")
"Syria" "data center" ("power" OR "electricity" OR "generator" OR "solar")
```

## 6. Complete Division Strategy - 14 Governorates

Run each division in English and Arabic. Record negative results explicitly for low-probability divisions.

### Damascus

Priority: commercial/private cloud, government DCs, university/education hosting, banks, telecom HQ.

```text
"Damascus" ("data center" OR "data centre" OR hosting OR cloud) Syria
"دمشق" ("مركز بيانات" OR "استضافة" OR "خوادم" OR "حوسبة سحابية")
"Mijad" OR "Sham Cloud" "Damascus" "data center"
"مجاد" OR "شام كلاود" "دمشق" "مركز بيانات"
"Damascus University" "cloud infrastructure" "Mijad"
```

### Daraa

Priority: Jordan/Nasib fiber corridor, border connectivity, telecom restoration.

```text
"Daraa" ("fiber" OR "data center" OR "data centre" OR "Jordan Syria")
"Nasib" OR "Naseeb" "fiber" "Syria"
"درعا" ("ألياف" OR "ربط" OR "نصيب" OR "مركز بيانات")
```

### Deir Ezzor

Priority: reconstruction, utility constraints, eastern investment incentives, telecom restoration.

```text
"Deir Ezzor" OR "Deir ez-Zor" ("data center" OR "fiber" OR "telecom")
"دير الزور" ("مركز بيانات" OR "ألياف" OR "اتصالات" OR "محطة تحويل")
"SilkLink" "Deir Ezzor" OR "دير الزور"
```

### Hasaka

Priority: Qamishli planned IXP, northeast connectivity, authority validation.

```text
"Hasaka" OR "Al-Hasakah" ("data center" OR "IXP" OR "fiber")
"Qamishli" ("internet exchange" OR "IXP" OR "data center")
"الحسكة" OR "القامشلي" ("مركز بيانات" OR "نقطة تبادل" OR "ألياف")
"SilkLink" "Qamishli" OR "سيلك لينك" "القامشلي"
```

### Homs

Priority: Hassia industrial city, central power corridor, Tadmur/Palmyra planned IXP.

```text
"Homs" ("data center" OR "data centre" OR hosting) Syria
"Hassia" OR "Hisya" ("data center" OR "telecom" OR "industrial city")
"Palmyra" OR "Tadmur" ("IXP" OR "internet exchange" OR "fiber")
"حمص" OR "حسياء" OR "تدمر" ("مركز بيانات" OR "ألياف" OR "نقطة تبادل")
```

### Aleppo

Priority: second-city enterprise demand, Sheikh Najjar industrial city, SilkLink IXP.

```text
"Aleppo" ("data center" OR "data centre" OR hosting OR cloud) Syria
"Sheikh Najjar" ("data center" OR "telecom" OR "industrial city")
"حلب" ("مركز بيانات" OR "استضافة" OR "خوادم" OR "حوسبة")
"الشيخ نجار" ("مركز بيانات" OR "اتصالات" OR "استضافة")
"SilkLink" "Aleppo" OR "سيلك لينك" "حلب"
```

### Hama

Priority: negative documentation, industrial/electricity restoration.

```text
"Hama" ("data center" OR "data centre" OR hosting) Syria
"حماة" ("مركز بيانات" OR "استضافة" OR "خوادم" OR "اتصالات")
"شركة كهرباء حماة" ("محطة تحويل" OR "أحمال")
```

### Idlib

Priority: service restoration, new investment visits, no-facility documentation.

```text
"Idlib" ("data center" OR "data centre" OR hosting OR telecom) Syria
"إدلب" ("مركز بيانات" OR "استضافة" OR "خوادم" OR "اتصالات")
"هيئة الاستثمار السورية" "إدلب" ("اتصالات" OR "تقانة")
```

### Latakia

Priority: coastal connectivity, port, university IT, possible edge/landing spillover.

```text
"Latakia" OR "Lattakia" ("data center" OR "data centre" OR "cable landing")
"اللاذقية" ("مركز بيانات" OR "استضافة" OR "كابل بحري" OR "محطة إنزال")
"Tishreen University" OR "جامعة تشرين" ("data center" OR "مركز بيانات")
```

### Quneitra

Priority: negative documentation, SIA branch and local services.

```text
"Quneitra" ("data center" OR "data centre" OR hosting) Syria
"القنيطرة" ("مركز بيانات" OR "استضافة" OR "خوادم" OR "اتصالات")
"شركة كهرباء القنيطرة" ("محطة تحويل" OR "أحمال")
```

### Raqqa

Priority: reconstruction and fiber route leads, not conventional DCs.

```text
"Raqqa" ("data center" OR "data centre" OR fiber OR telecom) Syria
"الرقة" ("مركز بيانات" OR "ألياف" OR "اتصالات" OR "خوادم")
"SilkLink" "Raqqa" OR "سيلك لينك" "الرقة"
```

### Damascus Countryside

Priority: Adra Industrial City, airport belt, industrial land/power.

```text
"Damascus Countryside" OR "Rif Dimashq" ("data center" OR "data centre" OR hosting)
"Adra Industrial City" "data center" Syria
"ريف دمشق" ("مركز بيانات" OR "استضافة" OR "خوادم")
"عدرا" OR "مدينة عدرا الصناعية" ("مركز بيانات" OR "اتصالات" OR "استضافة")
"Damascus International Airport" "data center" OR "مطار دمشق الدولي" "خوادم"
```

### Suwayda

Priority: negative documentation, local utility, public-service digitization.

```text
"Suwayda" OR "Sweida" ("data center" OR "data centre" OR hosting) Syria
"السويداء" ("مركز بيانات" OR "استضافة" OR "خوادم" OR "اتصالات")
"شركة كهرباء السويداء" ("محطة تحويل" OR "أحمال")
```

### Tartus

Priority: Medusa, Ugarit/Aletar, SilkLink IXP, landing-station follow-up.

```text
"Tartous" OR "Tartus" ("data center" OR "data centre" OR "landing station" OR Medusa OR Ugarit)
"طرطوس" ("مركز بيانات" OR "كابل بحري" OR "محطة إنزال" OR "نقطة تبادل")
"Medusa" "Tartous" "Syria Telecom"
"Ugarit 2" OR "UGARIT-2" "Tartous"
"Aletar" "Tartous" "Alexandria"
```

## 7. Validation Rules

1. Promote a lead to **operational facility** only with an operator/government/certification source naming live facility function.
2. Promote a lead to **under construction** only with construction, EPC, land, permit, power connection, or official progress evidence.
3. Keep **MoUs** as MoUs. Go/Etihad Atheeb is not a facility until more evidence appears.
4. Keep **SilkLink IXPs** as connectivity until the IXP sites are launched or a colocated facility is named.
5. Keep **Medusa, Ugarit, and Aletar** as submarine/landing-station evidence unless hosting or meet-me services are named.
6. Keep **Zain, Syriatel, MTN** as telecom/mobile infrastructure leads; do not count mobile core networks as commercial colocation.
7. Verify **Uptime/Tier** claims directly against Uptime Institute before using any tier in a record.
8. For every positive candidate, search power terms and store `power_evidence` separately from bandwidth/cable capacity.

Recommended record fields:

```text
project_or_facility_name
aliases_ar_en
owner_operator
governorate
repo_division
facility_type
status
source_grade
source_urls
source_date
capacity_mw_racks_or_tbps
power_evidence
connectivity_evidence
certification_evidence
classification_notes
```
