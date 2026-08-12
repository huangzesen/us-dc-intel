# SY Explorer Official - Syria Datacenter Enumeration from Official Sources

Date reviewed: 2026-08-12. Scope: Syrian Arab Republic (SY). Use this file for official, regulator, investment, utility, government-media, and operator-primary discovery of datacenter, cloud, hosting, IXP, and cable-landing infrastructure.

Reliability grades used here:

- **A**: Syrian government/ministry/regulator/investment authority/governorate source; SANA official news; operator official page; official cloud-region documentation; Uptime Institute certification list if a Syrian award is found.
- **B**: established trade press, wire services, legal/investment guides, vendor case studies, or conference material with named parties.
- **C**: directories, social posts, marketing pages, market-report PR, and unsourced local articles. Use only as leads.

Core rule: Syria has no public datacenter registry and no public online planning-permit register. A record is only a datacenter facility when evidence names an operating or planned facility. National digital programs, mobile licences, IXPs, cable landings, MoUs, and cloud-provider aspirations are leads unless a site, owner/operator, facility type, status, and source date are stated.

## 1. Verified Official Source Surfaces

### Ministry of Communications and Information Technology (MOCT)

- Main site: https://moct.gov.sy/
- Projects page: https://moct.gov.sy/projects
- SilkLink project page: https://moct.gov.sy/project/salik-link
- Syrian building telecom code consultation: https://moct.gov.sy/project/%D9%85%D8%B4%D8%B1%D9%88%D8%B9-%D8%A7%D9%84%D9%83%D9%88%D8%AF-%D8%A7%D9%84%D8%B3%D9%88%D8%B1%D9%8A-%D9%84%D9%84%D8%A7%D8%AA%D8%B5%D8%A7%D9%84%D8%A7%D8%AA-%D9%81%D9%8A-%D8%A7%D9%84%D8%A8%D9%86%D8%A7%D8%A1-%D9%84%D9%84%D9%85%D8%B4%D8%A7%D9%88%D8%B1%D8%A9-%D8%A7%D9%84%D8%B9%D8%A7%D9%85%D8%A9
- Medusa/Tartous cable landing project page: https://moct.gov.sy/project/%D8%A5%D9%86%D8%B2%D8%A7%D9%84-%D8%A3%D9%88%D9%84-%D9%83%D8%A7%D8%A8%D9%84-%D8%A8%D8%AD%D8%B1%D9%8A-%D8%AF%D9%88%D9%84%D9%8A-%D9%81%D9%8A-%D8%B3%D9%88%D8%B1%D9%8A%D8%A7---%D8%A8%D9%88%D8%A7%D8%A8%D8%A9-%D8%B1%D9%82%D9%85%D9%8A%D8%A9-%D8%AC%D8%AF%D9%8A%D8%AF%D8%A9-%D9%84%D9%84%D8%A7%D9%86%D9%81%D8%AA%D8%A7%D8%AD-%D8%B9%D9%84%D9%89-%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%85
- Government data/service carrier project: https://moct.gov.sy/project/%D9%86%D8%A7%D9%82%D9%84-%D8%A7%D9%84%D8%AE%D8%AF%D9%85%D8%A7%D8%AA-%D8%A7%D9%84%D8%AD%D9%83%D9%88%D9%85%D9%8A
- Official Telegram feed: https://t.me/moct_gov

Use MOCT for strategic programs, RFIs, telecom rules, cable/IXP announcements, and national digital infrastructure. MOCT pages are **A** for official intent and scope; they are not facility proof unless the page names a physical datacenter site.

Queries:

```text
site:moct.gov.sy ("مركز بيانات" OR "مركز المعطيات" OR "مراكز البيانات")
site:moct.gov.sy ("استضافة" OR "حوسبة سحابية" OR "سحابة")
site:moct.gov.sy ("سيلك لينك" OR SilkLink OR "نقطة تبادل")
site:moct.gov.sy ("كابل بحري" OR "محطة إنزال" OR طرطوس)
site:moct.gov.sy ("رخصة" OR "ترخيص" OR "طلب معلومات" OR RFI)
```

### Digital Syria

- Main site: https://www.digitalsyria.sy/
- Project catalog: https://digitalsyria.sy/explore/projects
- National Data Center project: https://www.digitalsyria.sy/project/113-mshroaa-mrkz-almaatyat-alotny
- Government electronic data carrier project: https://www.digitalsyria.sy/project/116-mshroaa-nakl-albyanat-alhkomy-alalktrony
- Open government data platform: https://www.digitalsyria.sy/project/125-ttoyr-mns-albyanat-almftoh

The National Data Center page is a verified **A-grade program lead**. It states a strategic initiative to create infrastructure for secure collection, storage, and management of national data, with MOCT as responsible entity and government bodies as participants. It does **not** publish a governorate, site address, MW, racks, operator, or opening date. Record it as `program-level/planned`, not as an operational facility.

Queries:

```text
site:digitalsyria.sy ("مركز المعطيات الوطني" OR "مركز بيانات" OR "البيانات الوطنية")
site:digitalsyria.sy ("حوسبة" OR "سحابة" OR "استضافة" OR "منصة")
"مشروع مركز المعطيات الوطني" ("وزارة الاتصالات" OR "الهيئة الوطنية")
```

### Telecom Regulator - SYTPRA

- Main site: https://sytpra.gov.sy/
- Licensed-entities directory: https://sytpra.gov.sy/pages/%D8%AF%D9%84%D9%8A%D9%84-%D8%A7%D9%84%D9%85%D8%B1%D8%AE%D8%B5-%D9%84%D9%87%D9%85
- Standard telecom licences: https://sytpra.gov.sy/pages/%D8%A7%D8%AA%D8%B5%D8%A7%D9%84%D8%A7%D8%AA/%D8%A7%D9%84%D8%AA%D8%B1%D8%A7%D8%AE%D9%8A%D8%B5-%D8%A7%D9%84%D9%86%D9%85%D8%B7%D9%8A%D8%A9
- Licensing regulations: https://sytpra.gov.sy/pages/%D9%84%D9%88%D8%A7%D8%A6%D8%AD-%D8%AA%D9%86%D8%B8%D9%8A%D9%85%D9%8A%D8%A9/%D9%84%D9%88%D8%A7%D8%A6%D8%AD-%D8%A7%D9%84%D8%AA%D8%B1%D8%A7%D8%AE%D9%8A%D8%B5
- Contact page: https://sytpra.gov.sy/pages/%D8%A7%D8%AA%D8%B5%D9%84-%D8%A8%D9%86%D8%A7

SYTPRA is **A** for licence facts and licensed telecom/ISP entities. It is not a datacenter registry. Use it to identify ISPs, mobile operators, value-added service providers, IPTV providers, and app providers that may later appear in hosting/cloud searches.

Queries:

```text
site:sytpra.gov.sy ("مركز بيانات" OR "استضافة" OR "حوسبة سحابية")
site:sytpra.gov.sy ("دليل المرخص لهم" OR "المرخص لهم" OR "خدمات الانترنت الثابت")
site:sytpra.gov.sy ("زين" OR "رخصة المشغل الخليوي")
"الهيئة الناظمة للاتصالات والبريد" ("مركز بيانات" OR "استضافة" OR "سحابة")
```

### SANA Official News

- Arabic: https://sana.sy/
- English: https://sana.sy/en/

SANA is **A** for official announcements and named government statements. Verify whether an article is about Syria or a foreign item; SANA also republishes international science/technology stories that mention datacenters.

Verified datacenter-relevant SANA anchors:

- Mijad/Sham Cloud agreements at Syria HiTech 12, Damascus, 2026-05-01: https://sana.sy/economy/2464512/ . This is the strongest current positive private-sector lead. It names Mijad Technical Services, Sham Cloud, Damascus exhibition context, use of Mijad cloud infrastructure, a Mijad private datacenter, and an MoU with CanaGulf and Uptime Institute representation to qualify datacenters. Grade **A for the SANA-reported statements**, but verify Uptime certification directly before recording any certified tier.
- Ministry of Higher Education IT center in Damascus, 2025-12-10: https://sana.sy/education/2350216/ . Names a Damascus information technology center managing a data center and hosting services. Grade **A for official/public-sector facility function**, classify as government/education hosting, not commercial colo unless service terms prove external customers.
- Zain second mobile operator licence, 2026-07-05: https://sana.sy/economy/syrian-economy/2519276/ . Confirms licence, investment, and 5G/infrastructure ambitions; no datacenter site is named. Grade **A for licence**, not facility evidence.

Queries:

```text
site:sana.sy ("مركز بيانات" OR "مركز المعطيات" OR "مراكز البيانات") سوريا -نيويورك -الفضاء
site:sana.sy ("استضافة" OR "خدمات الاستضافة" OR "حوسبة سحابية")
site:sana.sy ("مجاد" OR "شام كلاود" OR "Uptime Institute")
site:sana.sy ("سيلك لينك" OR "كابل بحري" OR "محطة إنزال" OR "طرطوس")
site:sana.sy ("زين" "رخصة" "الاتصالات")
site:sana.sy/en ("data center" OR "data centre" OR hosting OR cloud) Syria
```

### Syrian Investment Authority

- Main/current site: https://invest.gov.sy/ ; legacy domain https://sia.gov.sy/ redirects to it.
- News: https://invest.gov.sy/Home/News
- Branches by governorate: https://invest.gov.sy/Home/Braches
- Opportunities map: https://invest.gov.sy/Home/InvestmentMap

SIA is **A** for investment licences, one-stop-shop branches, and official investment announcements. The public site did not expose a searchable datacenter licence register during review. Use SIA as a cross-check for any large telecom, ICT, hosting, industrial-park, or foreign-investor project.

Queries:

```text
site:invest.gov.sy ("مركز بيانات" OR "مراكز البيانات" OR "حوسبة سحابية")
site:invest.gov.sy ("اتصالات" OR "تقانة المعلومات" OR "خدمات رقمية")
site:invest.gov.sy ("إجازة استثمار" OR "رخصة استثمار" OR "فرصة استثمارية")
"هيئة الاستثمار السورية" ("مركز بيانات" OR "اتصالات" OR "تقانة")
```

### Syrian Telecom and Mobile Operators

- Syrian Telecom: https://www.syriantelecom.com.sy/ and https://www.telecomsy.com/
- Syriatel: https://syriatel.sy/
- MTN Syria: check current operating/rebrand pages before use.
- Zain Syria: use SYTPRA/SANA/MOCT licence releases until an official operating site is live.

Operator pages are **A** for their own services and announced infrastructure. Legacy exchanges, mobile core rooms, and network POPs are not commercial datacenters unless the operator or a reliable source names hosting, cloud, colocation, datacenter services, or a certified facility.

Queries:

```text
site:syriantelecom.com.sy ("مركز بيانات" OR "استضافة" OR "سحابة" OR "خوادم")
site:telecomsy.com ("مركز بيانات" OR "استضافة" OR "cloud" OR "hosting")
"الشركة السورية للاتصالات" ("مركز بيانات" OR "استضافة" OR "كابل بحري")
"Syrian Telecom" ("data center" OR "data centre" OR hosting OR "landing station")
site:syriatel.sy ("مركز بيانات" OR "استضافة" OR "cloud")
```

### Utility and Power Authorities

Electricity is a gating condition for any Syrian facility. Use official power sources to avoid mistaking telecom programs for buildable datacenter sites.

- Ministry of Electricity: locate the current official domain through SANA/MOCT links before quoting a URL.
- Public Establishment for Generation and Transmission of Electricity (PEEGT): search Arabic name `المؤسسة العامة لتوليد ونقل الكهرباء`.
- Governorate electricity companies: search by `شركة كهرباء دمشق`, `شركة كهرباء حلب`, etc.
- National Energy Research Center: use for renewable-energy context only.

Queries:

```text
"وزارة الكهرباء" ("مركز بيانات" OR "أحمال كبيرة" OR "محطة تحويل")
"المؤسسة العامة لتوليد ونقل الكهرباء" ("محطة تحويل" OR "إعادة تأهيل")
"شركة كهرباء {governorate_ar}" ("مركز بيانات" OR "أحمال" OR "محطة تحويل")
"كهرباء" "مركز بيانات" "سوريا" ("مولد" OR "طاقة شمسية" OR "بطاريات")
```

## 2. Connectivity Programs: How to Classify

### SilkLink

- Official RFI: https://silklink.moct.gov.sy/pages/introduction.html
- MOCT project page: https://moct.gov.sy/project/salik-link

The RFI states fiber backbone objectives, ITU-T G.652/G.655 fiber, 10 Tbps initial and 25 Tbps future capacity, five IXPs in Damascus, Aleppo, Tartous, Palmyra, and Qamishli, wholesale internet services, Syrian Telecom operation, and MOCT regulation. Grade **A for program design**. Do not count the five IXPs as operating datacenters unless later evidence says a colocated facility or meet-me room is operational.

### Medusa landing in Tartous

- MOCT project: https://moct.gov.sy/project/%D8%A5%D9%86%D8%B2%D8%A7%D9%84-%D8%A3%D9%88%D9%84-%D9%83%D8%A7%D8%A8%D9%84-%D8%A8%D8%AD%D8%B1%D9%8A-%D8%AF%D9%88%D9%84%D9%8A-%D9%81%D9%8A-%D8%B3%D9%88%D8%B1%D9%8A%D8%A7---%D8%A8%D9%88%D8%A7%D8%A8%D8%A9-%D8%B1%D9%82%D9%85%D9%8A%D8%A9-%D8%AC%D8%AF%D9%8A%D8%AF%D8%A9-%D9%84%D9%84%D8%A7%D9%86%D9%81%D8%AA%D8%A7%D8%AD-%D8%B9%D9%84%D9%89-%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%85
- Medusa page: https://medusascs.com/news/tartous-syria-medusa-signs-agreement-with-syria-telecom-to-establish-a-new-east-to-west-route/

Grade **A/B+ for cable landing agreement**, depending on source. Record as `cable landing/landing station lead`, not datacenter, unless facility services are later published.

### Ugarit / Ugarit 2

- SANA English first-phase Ugarit 2 story: https://sana.sy/en/syria/354083/

Use official SANA/MOCT first, then trade/wire coverage for construction and maintenance details. Classify as submarine connectivity and landing-station evidence unless hosting/colo is named.

## 3. Hyperscaler Region Check

Official cloud-region pages are **A negative evidence** for Syria as of this review:

- AWS Regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle Cloud regions: https://www.oracle.com/cloud/public-cloud-regions/

None lists a Syrian public cloud region. Statements about possible partnerships with Google, Amazon, Oracle, or Microsoft are aspirational unless an official provider region/zone/local-zone/edge announcement names Syria.

## 4. Official Evidence Classification

Use these statuses exactly:

- `operational`: facility is live/opened and owner/operator is named.
- `under_construction`: construction start, EPC, power connection, or physical build is named.
- `licensed`: SYTPRA/SIA/MOCT licence exists but no site is proven.
- `program-level`: national program, Digital Syria project, RFI, or strategy.
- `MoU`: non-binding or framework agreement; do not count as a facility.
- `connectivity`: IXP, cable landing, backbone, or transit route only.
- `negative`: official cloud-region list or source sweep found no Syria facility.

Minimum fields for any positive candidate:

```text
project_or_facility_name
aliases_ar_en
operator_or_owner
governorate
repo_division
facility_type (commercial colo / cloud / government DC / enterprise DC / IXP / landing station / mobile core / hosting)
status
source_grade
source_urls
source_date
site_confidence
power_evidence
connectivity_evidence
notes
```

## 5. Complete Division Strategy - 14 Governorates

The repo divisions are the 14 Syrian governorates. SANA navigation and official investment branch structures expose these governorates; use the names below as the canonical coverage checklist.

### Damascus

Highest-priority division. Known official leads include MOCT, SYTPRA, SIA headquarters, Syrian Telecom HQ functions, Digital Syria, Mijad/Sham Cloud, and the Ministry of Higher Education IT center. Search for government DCs, private cloud, hosting services, bank/ministry infrastructure, and Uptime certification follow-up.

```text
"دمشق" ("مركز بيانات" OR "مركز المعطيات" OR "مراكز البيانات" OR "استضافة")
site:sana.sy "دمشق" ("مركز بيانات" OR "خدمات الاستضافة" OR "حوسبة سحابية")
"مجاد" OR "شام كلاود" "دمشق" "مركز بيانات"
"مركز تكنولوجيا المعلومات" "دمشق" "مركز بيانات" "استضافة"
"وزارة الاتصالات" "دمشق" "مركز المعطيات الوطني"
```

### Daraa

Southern connectivity and Jordan/Nasib corridor division. Low datacenter probability; search fiber, border connectivity, electricity, and governorate services.

```text
"درعا" ("مركز بيانات" OR "استضافة" OR "خوادم")
"درعا" ("ألياف" OR "ربط" OR "نصيب" OR "الأردن")
"Nasib" OR "Naseeb" "Syria" "fiber" "Daraa"
site:sana.sy "درعا" ("اتصالات" OR "ألياف" OR "مركز بيانات")
```

### Deir Ezzor

Eastern reconstruction division. Very low near-term DC probability; search telecom rebuild, SilkLink routing, SIA incentives, and utility rehabilitation.

```text
"دير الزور" ("مركز بيانات" OR "استضافة" OR "خوادم")
"دير الزور" ("اتصالات" OR "ألياف" OR "محطة تحويل")
"Deir Ezzor" OR "Deir ez-Zor" "data center" Syria
site:sana.sy "دير الزور" ("اتصالات" OR "ألياف" OR "مركز")
```

### Hasaka

Northeast division; Qamishli is a named planned SilkLink IXP. Verify operating authority carefully because local telecom administration may differ by period and area.

```text
"الحسكة" ("مركز بيانات" OR "استضافة" OR "خوادم")
"القامشلي" ("نقطة تبادل" OR "IXP" OR "مركز بيانات" OR "ألياف")
"Qamishli" "internet exchange" OR "IXP" "Syria"
"SilkLink" OR "سيلك لينك" "Qamishli" OR "القامشلي"
```

### Homs

Central industrial/power corridor; Hassia industrial city and Palmyra/Tadmur planned SilkLink IXP are the main leads.

```text
"حمص" ("مركز بيانات" OR "استضافة" OR "خوادم")
"حسياء" OR "حسيا" ("مركز بيانات" OR "اتصالات" OR "استضافة")
"تدمر" OR "Palmyra" OR "Tadmur" ("نقطة تبادل" OR "IXP" OR "ألياف")
site:sana.sy "حمص" ("اتصالات" OR "مركز بيانات" OR "محطة تحويل")
```

### Aleppo

Second-highest priority after Damascus. Search Sheikh Najjar industrial city, university/enterprise hosting, telecom restoration, and SilkLink IXP.

```text
"حلب" ("مركز بيانات" OR "مركز المعطيات" OR "استضافة" OR "خوادم")
"الشيخ نجار" OR "Sheikh Najjar" ("مركز بيانات" OR "اتصالات" OR "استضافة")
"Aleppo" "data center" OR "data centre" Syria
"سيلك لينك" "حلب" OR "SilkLink" "Aleppo"
site:sana.sy "حلب" ("مركز بيانات" OR "اتصالات" OR "حوسبة")
```

### Hama

Low-density central division. Run negative documentation plus utility/industrial-zone checks.

```text
"حماة" ("مركز بيانات" OR "استضافة" OR "خوادم")
"Hama" "data center" OR "data centre" Syria
site:sana.sy "حماة" ("اتصالات" OR "ألياف" OR "مركز بيانات")
"شركة كهرباء حماة" ("أحمال" OR "محطة تحويل")
```

### Idlib

Rebuild and service-normalization division. DC probability is low; document negative searches and watch SIA/governorate investment visits.

```text
"إدلب" ("مركز بيانات" OR "استضافة" OR "خوادم")
"Idlib" "data center" OR "data centre" Syria
site:sana.sy "إدلب" ("اتصالات" OR "ألياف" OR "استثمار")
site:invest.gov.sy "إدلب" ("تقانة" OR "اتصالات" OR "استثمار")
```

### Latakia

Coastal port/university division. Search cable-landing spillover, Tishreen University, port connectivity, and edge/hosting sites.

```text
"اللاذقية" ("مركز بيانات" OR "استضافة" OR "خوادم")
"اللاذقية" ("كابل بحري" OR "محطة إنزال" OR "ألياف")
"Latakia" OR "Lattakia" ("data center" OR "data centre" OR "cable landing")
"جامعة تشرين" OR "Tishreen University" ("مركز بيانات" OR "استضافة")
```

### Quneitra

Lowest-probability southwest division. Use negative-documentation searches and SIA/governorate branch checks.

```text
"القنيطرة" ("مركز بيانات" OR "استضافة" OR "خوادم")
"Quneitra" "data center" OR "data centre" Syria
site:sana.sy "القنيطرة" ("اتصالات" OR "ألياف" OR "مركز بيانات")
site:invest.gov.sy "القنيطرة" ("تقانة" OR "اتصالات")
```

### Raqqa

Eastern/northern reconstruction division. Search telecom restoration, SilkLink corridor language, and public-service digitization.

```text
"الرقة" ("مركز بيانات" OR "استضافة" OR "خوادم")
"Raqqa" "data center" OR "data centre" Syria
"سيلك لينك" "الرقة" OR "SilkLink" "Raqqa"
site:sana.sy "الرقة" ("اتصالات" OR "ألياف" OR "مركز بيانات")
```

### Damascus Countryside

Priority industrial/land division. Adra Industrial City and Damascus International Airport area are the main search pivots.

```text
"ريف دمشق" ("مركز بيانات" OR "استضافة" OR "خوادم")
"عدرا" OR "مدينة عدرا الصناعية" ("مركز بيانات" OR "اتصالات" OR "استضافة")
"Adra Industrial City" "data center" Syria
"مطار دمشق الدولي" ("مركز بيانات" OR "اتصالات" OR "خوادم")
site:sana.sy "ريف دمشق" ("مركز بيانات" OR "اتصالات" OR "استثمار")
```

### Suwayda

Low-probability southern division. Search public-service digitization, local hosting, and utility constraints; expect negative results.

```text
"السويداء" ("مركز بيانات" OR "استضافة" OR "خوادم")
"Suwayda" OR "Sweida" "data center" OR "data centre" Syria
site:sana.sy "السويداء" ("اتصالات" OR "ألياف" OR "مركز بيانات")
"شركة كهرباء السويداء" ("أحمال" OR "محطة تحويل")
```

### Tartus

Highest coastal priority. Verified official leads include the Medusa landing agreement and SilkLink planned IXP. Treat landing stations and IXPs as connectivity unless hosting/colo is later named.

```text
"طرطوس" ("مركز بيانات" OR "استضافة" OR "خوادم")
"طرطوس" ("كابل بحري" OR "محطة إنزال" OR "نقطة تبادل" OR "سيلك لينك")
"Tartous" OR "Tartus" ("Medusa" OR "landing station" OR "data center")
"Ugarit" OR "UGARIT-2" "Tartous" OR "طرطوس"
site:moct.gov.sy "طرطوس" ("كابل بحري" OR "محطة إنزال")
```

## 6. Final Official Workflow

1. Run national official sweeps: MOCT, Digital Syria, SYTPRA, SIA, SANA AR/EN, Syrian Telecom.
2. Extract only named projects and classify by status: operational, construction, licence, program-level, MoU, connectivity, or negative.
3. Route each lead to one of the 14 governorates only when a source names a city, governorate, industrial city, port, university, or landing/IXP location.
4. Run the complete division query set above and record negative searches for low-probability governorates.
5. Check power evidence for every facility candidate using Ministry of Electricity, PEEGT, and governorate electricity-company queries.
6. Check official hyperscaler region pages and record the negative Syria finding.
7. Verify certification claims directly against Uptime Institute before assigning any tier/certified status.
8. Do not upgrade MoUs, SilkLink IXPs, Medusa/Ugarit cable landings, Zain/mobile core needs, or government aspirations into datacenter facilities without explicit site-level evidence.
