# UZ Explorer - Industry / Vendor Discovery Methodology

Date: 2026-08-12. Scope: industry-source methodology for discovering Uzbekistan data centers from operators, cloud providers, Uptime certifications, project developers, telecoms, investors, directories, and local-language web search.

Reliability grades:

| Grade | Source type |
|---|---|
| A | Operator official page, Uptime Institute, cloud-provider official region list, lender/investor official release, government/ministry source. |
| B | Data Center Dynamics, UzDaily, Gazeta.uz, Kun.uz, Daryo, Spot, Times of Central Asia, UzA, Trend, Tech.az, Telecom Review, Telecompaper when they quote named parties. |
| C | Data Center Map, Datacenters.com, Cloudscene, Baxtel, 2GIS/Yandex Maps, social posts, conference decks, unsourced marketing. |

Search languages:

- Uzbek: `ma'lumotlar markazi`, `ma'lumotlarni qayta ishlash markazi`, `server markazi`, `bulutli infratuzilma`, `quvvat`, `qurilish boshlandi`, `ishga tushirildi`.
- Russian: `дата-центр`, `центр обработки данных`, `ЦОД`, `серверная`, `облачная инфраструктура`, `МВт`, `началось строительство`, `введен в эксплуатацию`.
- English: `data center`, `datacenter`, `colocation`, `cloud hub`, `cloud region`, `hyperscale`, `AI-ready`, `sovereign cloud`, `MW`.

---

## 1. Market Buckets

1. State-aligned cloud/DC: UzCloud / UZINFOCOM, Digital Government Project Management Center, e-government DCs.
2. Incumbent telecom: Uzbektelecom / Uztelecom cloud hubs and regional IDCs; mobile operators Beeline Uzbekistan, Ucell, Mobiuz/UMS for core-network DCs.
3. Foreign hyperscale/AI developers: DataVolt, LinkWise, Muroosystems/Uzatom, possible Gulf/Saudi/Chinese investment vehicles.
4. Policy hubs with weak facility evidence: Karakalpakstan AI/DC incentive zone.
5. Directories/maps: use only as seed discovery, then verify with A/B sources.

---

## 2. Authoritative Industry Sources

### 2.1 Operators and Certification

| Source | URL | Use | Grade |
|---|---|---|---|
| UzCloud infrastructure | https://uzcloud.uz/en/infrastructure/data-centers | Officially claims 5 DCs across 4 regions, 61 modules, 299 IT racks, 5.1 MW, named site details including Akhangaran, Bukhara, and Kokand. | A |
| UzCloud about/services | https://uzcloud.uz/en/about | Connectivity, GPU-as-a-Service, managed cloud, in-country services. | A |
| UZINFOCOM | https://uzinfocom.uz | State IT integrator/operator context. | A |
| UZINFOCOM DC surface | https://dc.uz | Facility/service discovery; reconcile with UzCloud/Uptime. | A/B depending page detail |
| Uzbektelecom | https://uztelecom.uz | Incumbent telecom/operator disclosures. | A |
| Uztelecom Cloud | https://cloud.uztelecom.uz | Cloud services, GPU/cloud products, facility clues. | A |
| Uptime Uzbekistan country page | https://uptimeinstitute.com/uptime-institute-awards/country/id/UZ | Certification baseline and new entries. | A |
| Uptime list | https://uptimeinstitute.com/uptime-institute-awards/list | Global re-scan for Uzbekistan/client names. | A |

Verified Uptime facility pages:

- Uztelecom DC2, Akhangaran: https://uptimeinstitute.com/uptime-institute-awards/datacenter/uztelecom-dc2/1461
- Uztelecom Cloud Hub Kokand 1, Kokand: https://uptimeinstitute.com/uptime-institute-awards/datacenter/uztelecom-cloud-hub-kokand-1/2361
- Uztelecom Cloud Hub Bukhara 1, Bukhara: https://uptimeinstitute.com/uptime-institute-awards/datacenter/uztelecom-cloud-hub-bukhara-1/2410
- DC E-GOV Solnechniy, Tashkent: https://uptimeinstitute.com/uptime-institute-awards/datacenter/dc-egov-solnechniy/1659

Record the award type exactly. Current public evidence supports design-stage certification for these facilities unless the specific page/list shows a constructed-facility or operations award.

### 2.2 Foreign Developer and Finance Sources

| Developer/project | Best sources | Current handling |
|---|---|---|
| DataVolt TAS-1, Tashkent IT Park | Ministry: https://gov.uz/en/digital/news/view/10951 ; DataVolt/Beeline release: https://data-volt.com/media/breaking-news/datavolt-beeline-form-data-center-partnership-to-support-central-asias-digital-transformation/ ; DCD financing: https://www.datacenterdynamics.com/en/news/saudi-arabias-datavolt-to-develop-12mw-data-center-in-uzbekistan/ | A/B. 10 MW in ministry 2024 announcement; 12 MW IT capacity in 2026 DataVolt/finance coverage. Under construction/expected late 2026 if corroborated by current operator/lender page. |
| DataVolt New Tashkent | Ministry: https://gov.uz/en/digital/news/view/10951 | Planned, up to 250 MW on 25 ha in New Tashkent; keep separate from Tashkent City TAS-1. |
| DataVolt Bukhara | Ministry: https://gov.uz/en/digital/news/view/10951 ; Beeline/DataVolt release notes Bukhara cooperation MoU | Planned, 40 MW expandable to 250 MW on 25 ha; do not merge with LinkWise or Uzbektelecom Bukhara. |
| LinkWise Bukhara / Surxondaryo | DCD: https://www.datacenterdynamics.com/en/news/300mw-data-center-to-be-built-in-uzbekistan-with-chinas-linkwise/ ; UzDaily: https://www.uzdaily.uz/en/uzbekistan-to-build-300-mw-data-center-with-chinese-company/ ; Yuz.uz: https://yuz.uz/en/news/v-buxarskoy-oblasti-planiruetsya-stroitelstvo-data-tsentra-s-nagruzkoy-300-mvt | B planned/MoU. 300 MW Bukhara MoU; similar Surxondaryo facility discussed/planned. Need ministry/project-company evidence before upgrading. |
| Muroosystems / Uzatom Jizzakh SMR DC | DCD Uzbekistan coverage; search Uzatom/minenergy/lex.uz | B/C planned until official Uzbek nuclear/energy confirmation. Track 50 MW DC + 55 MWe SMR claim. |
| Core AI Holdings / other AI-DC investment claims | Press releases/trade press only | C unless a named Uzbek government page, land, utility, lender, or operator document appears. |
| Beeline Uzbekistan as TAS-1 tenant | DataVolt release above; Beeline/VEON official channels | Tenant/anchor-customer relationship, not a separate facility unless Beeline discloses its own DC. |

### 2.3 Trade Press and Directories

| Source | URL | Use | Grade |
|---|---|---|---|
| Data Center Dynamics Uzbekistan tag | https://www.datacenterdynamics.com/en/tags/uzbekistan/ | Best English DC trade watchlist. | B |
| UzDaily | https://www.uzdaily.uz | Local investment/operator coverage. | B |
| Gazeta.uz | https://www.gazeta.uz | Local policy/business coverage. | B |
| Kun.uz | https://kun.uz | Local UZ/RU/EN coverage. | B |
| Daryo | https://daryo.uz | Local business/energy coverage. | B |
| Spot.uz | https://www.spot.uz | Startup/investment coverage. | B |
| Times of Central Asia | https://timesca.com | Regional English coverage, including Karakalpakstan hub. | B |
| UzA | https://uza.uz | State-news follow-up to official events. | B+ |
| Telecom Review / Telecompaper | https://www.telecomreview.com ; https://www.telecompaper.com | Telecom/DC certification and financing leads. | B |
| Data Center Map Uzbekistan | https://www.datacentermap.com/uzbekistan/ | Seed names/addresses only. | C |
| Datacenters.com Uzbekistan | https://www.datacenters.com/locations/uzbekistan | Seed provider/location leads only. | C |
| Cloudscene | https://cloudscene.com/market/uzbekistan/all | Seed connectivity/provider leads only. | C |
| Baxtel | https://baxtel.com | Seed project pages only. | C |
| 2GIS / Yandex Maps | https://2gis.uz ; https://yandex.com/maps/ | Address discovery only. | C |

---

## 3. National Query Templates

### 3.1 Broad Discovery

```text
Uzbekistan "data center" "MW"
Uzbekistan "hyperscale" "data center"
Uzbekistan "AI-ready" "data center" "Tashkent"
Uzbekistan "sovereign cloud" "data center"
Uzbekistan "colocation" "Tier III"
Uzbekistan "cloud hub" "Uztelecom"
Узбекистан "дата-центр" "МВт"
Узбекистан "центр обработки данных" "строительство"
Узбекистан "ЦОД" "Tier III"
O'zbekiston "ma'lumotlar markazi" "quvvat"
O'zbekiston "bulutli infratuzilma" "data center"
```

### 3.2 Source-Restricted Sweeps

```text
site:datacenterdynamics.com/en/tags/uzbekistan/ Uzbekistan
site:datacenterdynamics.com Uzbekistan DataVolt OR LinkWise OR Uzatom
site:uzdaily.uz "data center" OR "дата-центр"
site:gazeta.uz "дата-центр" OR "data center"
site:kun.uz "дата-центр" OR "data center"
site:daryo.uz "дата-центр" OR "data center"
site:spot.uz "дата-центр" OR "ЦОД"
site:telecompaper.com Uzbektelecom "Tier-3" "data centre"
site:datacentermap.com/uzbekistan "Tashkent" "data center"
site:cloudscene.com/market/uzbekistan "data center"
```

### 3.3 Operator / Project Sweeps

```text
"DataVolt" "TAS-1" "Uzbekistan"
"DataVolt" "Tashkent IT Park" "12 MW"
"DataVolt" "New Tashkent" "250 MW"
"DataVolt" "Bukhara" "250 MW" OR "40 MW"
"Beeline Uzbekistan" "DataVolt" "data center"
"Uzbektelecom" OR "Uztelecom" "Cloud Hub" "Bukhara" OR "Kokand" OR "Akhangaran"
"UZINFOCOM" OR "UzCloud" "5 data centers" OR "Tier III"
"DC E-GOV Solnechniy" OR "Э-гов" "Solnechniy"
"LinkWise" OR "Linkwise" "Uzbekistan" "300 MW"
"Shanghai Linkwise Data Intelligence" "Bukhara"
"Uzatom" "data center" OR "дата-центр" "Jizzakh"
"Muroosystems" "Uzbekistan" "data center"
"Ucell" OR "Mobiuz" OR "Beeline Uzbekistan" "дата-центр" OR "ЦОД"
"TAS-IX" "data center" "Uzbekistan"
```

### 3.4 Status / Capacity Extraction

```text
"{project}" "MW" OR "МВт" OR "quvvat"
"{project}" "IT capacity" OR "IT load"
"{project}" "Tier III" OR "Tier 3" OR "Uptime"
"{project}" "groundbreaking" OR "construction began" OR "началось строительство" OR "qurilish boshlandi"
"{project}" "commissioned" OR "launched" OR "введен в эксплуатацию" OR "ishga tushirildi"
"{project}" "MoU" OR "memorandum" OR "меморандум" OR "kelishuv"
"{project}" "PPA" OR "tariff" OR "electricity" OR "подстанция"
```

Lifecycle verbs:

- English: signed, MoU, planned, financed, groundbreaking, construction began, expected online, launched, commissioned, operational.
- Russian: подписано, меморандум, планируется, финансирование, началось строительство, ввод, введен в эксплуатацию, запущен.
- Uzbek: kelishuv, memorandum, rejalashtirilmoqda, moliyalashtirish, qurilish boshlandi, foydalanishga topshirildi, ishga tushirildi.

---

## 4. Facility Seed Baseline

| Facility / project | Region bucket | Source-grade baseline | Status handling |
|---|---|---|---|
| DataVolt TAS-1 / Tashkent IT Park DC | Tashkent City | A ministry + A/B operator/lender/trade | Under construction/financed if latest operator/lender source confirms; 10 MW ministry, 12 MW later DataVolt/finance. |
| DataVolt New Tashkent | Tashkent Region | A ministry | Planned; up to 250 MW, 25 ha. |
| DataVolt Bukhara | Bukhara Region | A ministry + B trade/operator MoU | Planned; 40 MW expandable to 250 MW, 25 ha. |
| Uztelecom DC2 | Tashkent Region, Akhangaran | A Uptime | Certified design; verify operations separately. |
| Uztelecom Cloud Hub Kokand 1 | Fergana Region, Kokand | A Uptime | Certified design; verify operations separately. |
| Uztelecom Cloud Hub Bukhara 1 | Bukhara Region | A Uptime | Certified design; verify operations separately. |
| DC E-GOV Solnechniy | Tashkent City | A Uptime | Certified design/state facility; verify operations separately. |
| UzCloud / UZINFOCOM 5-site cloud | Akhangaran/Tashkent Region, Bukhara, Kokand/Fergana, other sites shown by operator page | A operator official | Operator-stated footprint/capacity; reconcile each site to physical facility and avoid double-counting Uzbektelecom cloud hubs unless ownership relationship is verified. |
| LinkWise Bukhara 300 MW | Bukhara Region | B official-adjacent/trade | Planned/MoU only. |
| LinkWise Surxondaryo 300 MW | Surxondaryo Region | B official-adjacent/trade | Discussed/planned only; weaker than Bukhara MoU. |
| Muroosystems/Uzatom SMR DC | Jizzakh Region | B/C trade until official | Planned lead only. |
| Karakalpakstan AI/DC hub | Karakalpakstan | B trade/policy, look for A decree | Policy/incentive, not facility. |
| Core AI Holdings claims | Unknown / Uzbekistan-wide | C | Do not count without site/operator/lender/government corroboration. |

---

## 5. Complete 14-Division Industry Strategy

Run each division in Uzbek, Russian, and English. Include capital/major city names because directories and telecom pages usually index by city.

| Division | City/name aliases | Industry/vendor approach |
|---|---|---|
| Andijan Region | Andijan, Andijon, Андижан | Low-yield but mandatory. Search Uzbektelecom regional IDC, Beeline/Ucell/Mobiuz core facilities, IT Park branch, 2GIS/Yandex address leads. Queries: `Andijon ma'lumotlar markazi`, `Андижан ЦОД`, `Andijan colocation`. |
| Bukhara Region | Bukhara, Buxoro, Бухара | High priority. Keep separate: Uztelecom Cloud Hub Bukhara 1, DataVolt Bukhara, LinkWise Bukhara. Queries: `Buxoro data center`, `Бухара дата-центр 300 МВт`, `Bukhara Cloud Hub`, `itpark-bukhara data center`. |
| Fergana Region | Fergana, Farg'ona, Фергана, Kokand, Qo'qon, Коканд | High priority due Kokand certification. Search Kokand/Qo'qon variants, Uzbektelecom, UzCloud, mobile core. Queries: `Qo'qon ma'lumotlar markazi`, `Коканд ЦОД`, `Uztelecom Cloud Hub Kokand`. |
| Jizzakh Region | Jizzakh, Jizzax, Джизак | Track SMR/DC project. Search nuclear/energy vendors plus official Uzatom. Queries: `Jizzax data center SMR`, `Джизак дата-центр атом`, `Muroosystems Uzbekistan Jizzakh`. |
| Namangan Region | Namangan, Наманган | Low-yield. IT Park branch is a campus lead, not DC. Search regional telecom rooms and directories. Queries: `Namangan data center`, `Наманган ЦОД`, `Namangan Uzbektelecom IDC`. |
| Navoiy Region | Navoi, Navoiy, Навои | Watch FEZ/industrial land/renewable-energy announcements; low current DC evidence. Queries: `Navoiy data center`, `Навои дата-центр СЭЗ`, `Navoi FEZ data center`. |
| Qashqadaryo Region | Qashqadaryo, Kashkadarya, Qarshi, Карши | Low-yield. Search telecom/operator and energy-intensive industry leads. Queries: `Qarshi ma'lumotlar markazi`, `Карши ЦОД`, `Kashkadarya data center`. |
| Republic of Karakalpakstan | Karakalpakstan, Qoraqalpog'iston, Каракалпакстан, Nukus, Нукус | Policy hub watch. Search for named investor/operator after incentive announcements. Queries: `Nukus data center`, `Каракалпакстан дата-центр`, `Karakalpakstan AI data center investor`. |
| Samarkand Region | Samarkand, Samarqand, Самарканд | IT Park campus/branch; watch tenants and local investment news. Queries: `Samarqand data center`, `Самарканд ЦОД`, `Samarkand IT Park cloud`. |
| Sirdaryo Region | Sirdaryo, Syrdarya, Сырдарья, Guliston, Gulistan | Low-yield; IT Park Gulistan branch lead. Queries: `Guliston data center`, `Гулистан ЦОД`, `Syrdarya data center MW`. |
| Surxondaryo Region | Surkhandarya, Surxondaryo, Сурхандарья, Termez, Termiz, Термез | Track LinkWise second-site claim only. Queries: `Surxondaryo data center`, `Термез дата-центр`, `Surkhandarya LinkWise 300 MW`. |
| Tashkent City | Tashkent, Toshkent shahri, Ташкент, Mirzo-Ulugbek | Highest priority. DataVolt TAS-1, DC E-GOV Solnechniy, UZINFOCOM/UzCloud sites, Uzbektelecom, Beeline/Ucell/Mobiuz core facilities, Data Center Map leads. Queries: `Tashkent data center 12 MW`, `Ташкент дата-центр МВт`, `TAS-1 DataVolt`, `Solnechniy E-GOV`. |
| Tashkent Region | Toshkent viloyati, Ташкентская область, Nurafshon, Yangi Toshkent, Akhangaran, Ахангаран | High priority. DataVolt New Tashkent planned site; Uztelecom DC2 Akhangaran; UzCloud Akhangaran sites. Queries: `Yangi Toshkent data center 250 MW`, `Ахангаран ЦОД`, `Akhangaran UzCloud data center`. |
| Xorazm Region | Khorezm, Xorazm, Хорезм, Urgench, Urganch, Ургенч | Low-yield; IT Park Urgench branch. Queries: `Urganch data center`, `Ургенч ЦОД`, `Xorazm ma'lumotlar markazi`. |

---

## 6. Cloud Region / Hyperscaler Signals

Official lists to check:

- AWS regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure geographies: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle public cloud regions: https://www.oracle.com/cloud/public-cloud-regions/
- Yandex Cloud regions: https://yandex.cloud/en/docs/overview/concepts/region

As of this methodology pass, do not seed AWS/Azure/GCP/OCI Uzbekistan facilities from non-official "coming soon" speculation. Government meetings with hyperscalers are demand/investment signals, not regions or facilities. Yandex Uzbekistan claims require an official Yandex region/location page or operator source.

Queries:

```text
site:aws.amazon.com Uzbekistan "region" OR "Local Zone"
site:azure.microsoft.com Uzbekistan "geography" OR "data center"
site:cloud.google.com Uzbekistan "locations" OR "region"
site:oracle.com Uzbekistan "public cloud region"
site:yandex.cloud Uzbekistan "region" OR "Tashkent"
"Uzbekistan" "cloud region" "AWS" OR "Azure" OR "Google Cloud" OR "Oracle"
```

---

## 7. Verification and Deduplication Rules

1. Do not double-count a physical facility across Uzbektelecom, UzCloud, UZINFOCOM, and Uptime. If ownership/operator is unclear, keep one facility record and add aliases/source notes.
2. Do not count tenants as facilities. Beeline capacity at DataVolt TAS-1 is a tenant/anchor-customer relationship unless Beeline discloses a separate facility.
3. Split DataVolt into at least three records: TAS-1 Tashkent City, New Tashkent/Tashkent Region, and Bukhara Region. The 500 MW country-program total is not a facility.
4. Treat all Uptime design-document awards as design-stage evidence. Upgrade only with constructed-facility certification, commissioning, operator service page, or current operations proof.
5. Treat MoUs as planned leads. LinkWise Bukhara and Surxondaryo remain MoU/planned until land, permit, financing, grid, construction, or operator evidence appears.
6. Treat Karakalpakstan as policy/incentive until a named project site/operator is found.
7. Use capacity hierarchy: operator/lender official IT MW > Uptime/operator facility spec > ministry announcement > trade press > directory.
8. Use status hierarchy: operational service page/commissioning > constructed/Uptime operations evidence > financing plus construction > groundbreaking > land/permit > MoU > policy talk > directory lead.
9. Preserve exact source dates and wording for "expected online", "planned", "up to", "load", "capacity", and "green energy".
10. For every record, store aliases in Uzbek/Russian/English and the division bucket. This prevents Tashkent City vs Tashkent Region and Kokand/Fergana mistakes.

---

## 8. Output Fields to Capture

Minimum fields for each candidate:

```text
facility_name
aliases
operator
owner_or_sponsor
tenant_anchor_customer
division
city_or_district
address_or_site_description
latitude_longitude_if_verified
status
status_evidence_url
status_evidence_grade
capacity_value
capacity_unit
capacity_type_it_load_facility_load_grid_or_unspecified
certification_type
certification_url
power_or_grid_evidence
source_notes
last_verified_date
```

Recommended source-note tags:

```text
operator official
government announcement
ministry energy MoU
Uptime design cert
trade press quoting operator
trade press quoting ministry
directory only
map/address only
policy hub no facility
tenant in third-party DC
```
