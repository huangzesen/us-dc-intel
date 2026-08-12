# UZ Explorer - Official / Regulatory / Energy Methodology

Date: 2026-08-12. Scope: official-source methodology for enumerating data centers, cloud infrastructure, and data-center energy projects in Uzbekistan.

Reliability grades used here:

| Grade | Meaning for Uzbekistan DC enumeration |
|---|---|
| A | Primary source: lex.uz law/decree; president.uz; Ministry of Digital Technologies/gov.uz; Ministry of Energy; Uptime Institute certification; operator official infrastructure page; cloud-provider official region list. |
| B | State media or credible trade/local press that quotes a named ministry, operator, lender, or investor. Good lead source, but re-check against A-grade sources before counting capacity/status. |
| C | Directory/map/social/marketing-only item or unverifiable investment claim. Use for discovery only. |

Core rule: separate **facility existence**, **location**, **capacity**, **certification type**, and **status**. Uzbekistan announcements often combine multiple phases and MoUs; do not count MoU/master-plan MW as built IT load.

---

## 1. National Official Backbone

### 1.1 Ministry of Digital Technologies

Primary URLs:

- Ministry portal: https://digital.uz
- Government portal section: https://gov.uz/en/digital
- Decrees/decisions page: https://gov.uz/en/digital/pages/decrees_and_decisions_of_the_president
- Licensing page: https://gov.uz/en/digital/pages/licensing
- Certification page: https://gov.uz/en/digital/pages/certification
- Telecom activity page: https://gov.uz/en/digital/activity_page/telecommunication
- AI activity page: https://gov.uz/en/digital/activity_page/sun-iy-intellekt
- Regional departments: https://gov.uz/en/digital/departments/regional

Verified A-grade example:

- DataVolt announcement: https://gov.uz/en/digital/news/view/10951 . The ministry states that DataVolt's first phase is a 10 MW, USD 150M green data center in IT Park Tashkent; phase 2 is up to 250 MW on 25 ha in New Tashkent; phase 3 is 40 MW expandable to 250 MW on 25 ha in Bukhara region; total program target is USD 5B by 2030. Treat phase 1 as a facility lead with construction evidence; treat phase 2/3 as planned until land/construction/grid evidence is found.
- Enterprise Uzbekistan launch/legal regime: https://gov.uz/en/digital/news/view/105735 . This is a policy/investment-zone anchor, not a facility.

Ministry queries:

```text
site:gov.uz/en/digital "data center"
site:gov.uz/en/digital "DataVolt" OR "DATAVOLT"
site:gov.uz/en/digital "Enterprise Uzbekistan" "data center"
site:digital.uz "data center" OR "дата-центр" OR "ma'lumotlar markazi"
site:gov.uz/en/digital "AI" "infrastructure" "data"
```

### 1.2 Legal Base - lex.uz

Use lex.uz as the authoritative legal database. Verified legal anchors:

- Digital Uzbekistan 2030, Presidential Decree DP-6079, 2020-10-05: https://lex.uz/en/docs/7008256 . Policy driver for e-government, IT export, connectivity, and digital infrastructure.
- International Digital Technologies Center / Enterprise Uzbekistan, Presidential Decree DP-25, 2024-02-01: https://lex.uz/docs/6957961 . Legal/investment regime for foreign digital-technology companies in the IT Park area.
- Telecommunications Law LRU-1015, 2024-12-27: https://lex.uz/en/docs/7287371 . Current telecom regulatory frame; use for operator/network licensing context.
- Personal Data Law LRU/ZRU-547, 2019-07-02: https://lex.uz/docs/4831939 . Local personal-data processing requirements are a demand-side driver for domestic cloud/DC services; do not treat the law as facility evidence.
- AI Strategy to 2030, Presidential Resolution RP-358, 2024-10-14: https://lex.uz/en/docs/7159258 . Contains AI/data-processing infrastructure actions, including computing capacity for AI projects; use as policy driver only.

lex.uz queries:

```text
site:lex.uz "дата-центр" OR "центр обработки данных" OR "ЦОД"
site:lex.uz "data center" "Uzbekistan"
site:lex.uz "ma'lumotlar markazi" OR "ma'lumotlarni qayta ishlash markazi"
site:lex.uz "IT Park" "дата-центр"
site:lex.uz "искусственный интеллект" "вычислительные мощности"
site:lex.uz "personal data" "technical means physically located"
```

### 1.3 IT Park Uzbekistan

Primary URLs:

- IT Park Uzbekistan: https://www.it-park.uz/en
- Infrastructure/branches: https://www.it-park.uz/en/itpark/infrastructure
- Bukhara branch/campus: https://itpark-bukhara.uz

Verified A-grade points:

- IT Park's infrastructure page lists the republican office in Tashkent and branch/campus locations, including future branches in Nukus, Bukhara, Namangan, Samarkand, Gulistan, and Urgench. It also lists Andijan as a branch/location. Use this page as an official branch/campus source, not as proof of data-center facilities.
- DataVolt TAS-1 sits within IT Park Tashkent according to the Ministry/DataVolt announcements. Count it under Tashkent City, not Tashkent Region.

Queries:

```text
site:it-park.uz "data center" OR "дата-центр"
site:it-park.uz "DataVolt" OR "DATAVOLT"
site:it-park.uz "Bukhara" "data center"
site:it-park.uz "Nukus" OR "Karakalpakstan" "data center"
site:it-park.uz "Samarkand" "infrastructure"
```

### 1.4 Construction, Land, Cadastre, and Hokimiyat Surfaces

There is no open, county-style planning database comparable to US permit portals. Use these sources as verification channels:

- Unified government services portal: https://my.gov.uz . Relevant services include construction-permit and property/cadastre workflows. A-grade for service existence; per-project records may require authentication.
- Ministry of Construction and Housing and Communal Services: https://mc.uz
- Construction supervision / acceptance systems: https://nazorat.mc.uz
- Cadastre Agency official gov.uz section: https://gov.uz/en/kadastr . The standalone agency domain `kadastr.uz` is also referenced by official contact pages but may time out under automated checks.
- Regional/city administrations on gov.uz, e.g. https://gov.uz/en/andijan and https://gov.uz/en/buxoro . Prefer gov.uz regional sections when old standalone hokimiyat domains are stale.

Project verification checklist:

```text
"{project}" "yer ajratish" OR "land allocation"
"{project}" "qurilish boshlandi" OR "началось строительство" OR "groundbreaking"
"{project}" "foydalanishga topshirildi" OR "введен в эксплуатацию" OR "commissioned"
site:my.gov.uz "{project}" OR "{site}"
site:nazorat.mc.uz "{project}" OR "{site}"
site:kadastr.uz "{project}" OR "{site}"
site:gov.uz/en/{region_slug} "data center" OR "дата-центр"
```

---

## 2. Energy / Grid Pipeline

Data-center projects in Uzbekistan are power-led. Always distinguish:

- IT load vs total facility load vs grid-connection capacity.
- Operational power supply vs proposed tariff/PPA/MoU.
- Renewable-energy claim vs contracted generation or storage.

Primary and strong sources:

- Ministry of Energy: https://minenergy.uz . Search for data-center MoUs, electricity supply, tariffs, grid connections, renewables, and large industrial consumers.
- National Electric Grid of Uzbekistan JSC: verify the current official domain each run; use it for transmission/substation evidence.
- Regional Electric Networks / Hududiy Elektr Tarmoqlari: distribution-side technical conditions and regional grid news.
- Uzenergosotish: electricity procurement/sales counterparty created in 2023; use for supply/tariff signals.
- President's press service: https://president.uz . Use for national infrastructure initiatives and tariff/incentive statements.

Verified leads:

- LinkWise / Shanghai Linkwise Data Intelligence, Bukhara 300 MW: DCD and Uzbek state/local press report a 2025-07-24 Ministry of Energy MoU for a 300 MW data center in Bukhara and a possible similar facility in Surxondaryo. Use as B-grade planned/MoU unless a minenergy.uz page or signed project-company resolution is retrieved. DCD: https://www.datacenterdynamics.com/en/news/300mw-data-center-to-be-built-in-uzbekistan-with-chinas-linkwise/ ; Uzbek state-newspaper mirror: https://yuz.uz/en/news/v-buxarskoy-oblasti-planiruetsya-stroitelstvo-data-tsentra-s-nagruzkoy-300-mvt
- Karakalpakstan incentives: trade press reports an October 2025 presidential proposal/decree track to make Karakalpakstan a DC/AI hub with preferential electricity and tax incentives. Treat as policy/hub evidence until a named operator/site appears. TimesCA: https://timesca.com/karakalpakstan-to-become-data-center-hub-under-uzbekistans-digital-strategy/ ; also watch official Enterprise/IT Park pages.
- Jizzakh SMR-powered DC: trade press reports an Uzatom-Muroosystems plan for a 50 MW DC powered by a 55 MWe RITM-200N SMR. Treat as B-grade planned until Uzatom/lex.uz/minenergy confirms site, grid interconnection, and schedule.

Energy queries:

```text
site:minenergy.uz "data center" OR "дата-центр" OR "центр обработки данных"
site:minenergy.uz "LinkWise" OR "Linkwise" OR "Shanghai Linkwise"
site:minenergy.uz "Бухар" "300" "МВт" "дата"
site:minenergy.uz "Сурхандар" "300" "МВт" "дата"
site:president.uz "data center" OR "дата-центр" OR "ma'lumotlar markazi"
site:president.uz "Karakalpakstan" "data center" OR "дата-центр"
"Uzbekistan" "data center" "tariff" OR "electricity" OR "PPA"
"дата-центр" "Узбекистан" "подстанция" OR "техусловия" OR "электроэнергия"
```

---

## 3. Regulator / Licensing Pipeline

Primary surfaces:

- Agency for Regulation of Telecommunications, gov.uz section: https://gov.uz/en/ttsa
- Ministry licensing: https://gov.uz/en/digital/pages/licensing
- Ministry certification: https://gov.uz/en/digital/pages/certification
- Ministry state-control page: https://gov.uz/en/digital/pages/state_control

Method:

- Colocation/hosting/cloud facility operation is usually not a standalone public "data center license" category. Verify whether the operator also holds telecom/network/data-transmission licenses.
- Use regulator pages for operator identity, telecom services, spectrum/network approvals, and inspection records. Do not infer a physical DC just because an entity has a telecom license.
- For e-government or state-cloud facilities, cross-check the responsible institution: UZINFOCOM, Digital Government Project Management Center, Ministry of Digital Technologies, and Uzbektelecom.

Queries:

```text
site:gov.uz/en/ttsa "license" "telecommunication"
site:gov.uz "лицензия" "центр обработки данных"
site:gov.uz "Uzbektelecom" "license" "data"
site:gov.uz "UZINFOCOM" "data center"
site:lex.uz "лицензирование" "телекоммуникаций" "LRU-1015"
```

---

## 4. Cloud Region / Sovereign Cloud Check

Official public cloud region lists to re-check every run:

- AWS: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Microsoft Azure: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/
- Google Cloud: https://cloud.google.com/about/locations
- Oracle Cloud: https://www.oracle.com/cloud/public-cloud-regions/
- Yandex Cloud region concept page: https://yandex.cloud/en/docs/overview/concepts/region

As of this pass, no AWS, Azure, Google Cloud, or Oracle public cloud region is listed in Uzbekistan. Yandex Cloud has a Kazakhstan region in public docs; treat Uzbekistan-region claims as unverified unless Yandex publishes an official region/location page.

Domestic official cloud/DC sources:

- UzCloud infrastructure page: https://uzcloud.uz/en/infrastructure/data-centers . Officially claims 5 data centers across 4 regions, 61 modules, 299 IT racks, and 5.1 MW capacity, with named sites in Akhangaran, Bukhara, Kokand, and Tashkent-region/other locations shown on the page. Grade A for operator-stated footprint/capacity; still reconcile site names with Uptime entries and physical addresses.
- UzCloud about page: https://uzcloud.uz/en/about . Officially lists 40 Gbps TAS-IX connectivity and GPU-as-a-Service on NVIDIA DGX B200. Grade A for service claim.
- UZINFOCOM: https://uzinfocom.uz
- UZINFOCOM/data-center service surface: https://dc.uz
- Uzbektelecom cloud: https://cloud.uztelecom.uz

Queries:

```text
site:aws.amazon.com Uzbekistan "region" OR "Local Zone"
site:azure.microsoft.com Uzbekistan "geography" OR "region"
site:cloud.google.com Uzbekistan "region" OR "locations"
site:oracle.com Uzbekistan "cloud region"
site:yandex.cloud Uzbekistan "region" OR "Tashkent"
site:uzcloud.uz "data centers" "Uzbekistan"
site:dc.uz "Tier III" OR "ЦОД" OR "data center"
site:cloud.uztelecom.uz "GPU" OR "data center"
```

---

## 5. Uptime / Certification Baseline

Primary country page: https://uptimeinstitute.com/uptime-institute-awards/country/id/UZ

Verified current entries from Uptime pages:

| Data center | Client | Location | Evidence | Grade |
|---|---|---|---|---|
| Uztelecom DC2 | JSC Uzbektelecom | Akhangaran, Tashkent Region | https://uptimeinstitute.com/uptime-institute-awards/datacenter/uztelecom-dc2/1461 | A |
| Uztelecom Cloud Hub Kokand 1 | JSC Uzbektelecom | Kokand, Fergana Region | https://uptimeinstitute.com/uptime-institute-awards/datacenter/uztelecom-cloud-hub-kokand-1/2361 | A |
| Uztelecom Cloud Hub Bukhara 1 | JSC Uzbektelecom | Bukhara | https://uptimeinstitute.com/uptime-institute-awards/datacenter/uztelecom-cloud-hub-bukhara-1/2410 | A |
| DC E-GOV Solnechniy | E-Government Project Management Center | Tashkent | https://uptimeinstitute.com/uptime-institute-awards/datacenter/dc-egov-solnechniy/1659 | A |

Important: Uptime pages identify the project/client/location and award surface. If the award image or page text says **Tier III Certification of Design Documents**, record it as design certification only; do not mark operational/constructed solely from a design award.

---

## 6. Complete 14-Division Official Strategy

Uzbekistan has 14 first-level divisions for this work: 12 regions (viloyatlar), the Republic of Karakalpakstan, and Tashkent City. Use Uzbek, Russian, and English aliases.

| Division | Aliases / capital | Official surfaces | Known official or official-adjacent DC focus |
|---|---|---|---|
| Andijan Region | Andijon / Андижан; Andijan | https://gov.uz/en/andijan ; IT Park branch/location on IT Park infrastructure page | No verified standalone DC. Search Uzbektelecom regional IDC, UZINFOCOM/UzCloud footprint, telecom core rooms. |
| Bukhara Region | Buxoro / Бухара; Bukhara | https://gov.uz/en/buxoro ; https://itpark-bukhara.uz ; Ministry of Digital Technologies; Ministry of Energy | Uztelecom Cloud Hub Bukhara 1 (Uptime); DataVolt Bukhara 40->250 MW planned; LinkWise 300 MW MoU planned. |
| Fergana Region | Farg'ona / Фергана; Fergana, Kokand/Qo'qon | gov.uz regional section; Uptime; Uzbektelecom | Uztelecom Cloud Hub Kokand 1 (Uptime). Search Kokand/Qo'qon specifically. |
| Jizzakh Region | Jizzax / Джизак; Jizzakh | gov.uz regional section; Uzatom/minenergy/lex.uz | SMR-powered 50 MW DC is B-grade planned; require Uzatom/government confirmation before count beyond lead. |
| Namangan Region | Namangan / Наманган | gov.uz regional section; IT Park infrastructure | IT Park branch planned/listed; no verified DC. Search Uzbektelecom and regional digitalization news. |
| Navoiy Region | Navoiy / Навои; Navoi | gov.uz regional section; FEZ Navoi; Ministry of Energy | No verified DC. Watch FEZ/industrial-energy land and renewable projects. |
| Qashqadaryo Region | Qashqadaryo / Кашкадарья; Qarshi/Карши | gov.uz regional section; regional grid/energy | No verified DC. Low-yield official pass still required. |
| Republic of Karakalpakstan | Qoraqalpog'iston / Каракалпакстан; Nukus | gov.uz regional section; president.uz; IT Park infrastructure (Nukus); Ministry of Energy | Policy/hub incentive track for AI/DC investment; no verified operator/facility unless new official project page found. |
| Samarkand Region | Samarqand / Самарканд; Samarkand | https://gov.uz/en/samarqand ; https://samarkand.uz/en/regional_government ; IT Park | IT Park Samarkand campus/branch construction; no verified DC beyond campus/tenant leads. |
| Sirdaryo Region | Sirdaryo / Сырдарья; Guliston/Gulistan | gov.uz regional section; IT Park infrastructure (Gulistan/Guliston); regional grid | No verified DC. Search Guliston/Gulistan variants. |
| Surxondaryo Region | Surxondaryo / Сурхандарья; Termez/Termiz | gov.uz regional section; Ministry of Energy | LinkWise second 300 MW facility discussed only; planned lead, not counted. |
| Tashkent City | Toshkent shahri / город Ташкент; Mirzo-Ulugbek district | https://tashkent.uz ; gov.uz Tashkent City section; Ministry; IT Park | DataVolt TAS-1 at IT Park; DC E-GOV Solnechniy; UZINFOCOM/UzCloud city/state sites; telecom core DCs. |
| Tashkent Region | Toshkent viloyati / Ташкентская область; Nurafshon, Yangi Toshkent, Akhangaran | gov.uz regional section; New Tashkent directorate/news; Uptime | Uztelecom DC2 in Akhangaran; DataVolt New Tashkent 250 MW planned on 25 ha. |
| Xorazm Region | Xorazm / Хорезм; Urgench/Urganch | https://gov.uz/en/xorazm ; IT Park infrastructure (Urgench) | IT Park branch planned/listed; no verified DC. |

Per-division query template:

```text
site:gov.uz/en/{division_slug} "data center" OR "дата-центр" OR "ma'lumotlar markazi"
site:gov.uz "{division_uz}" "data center" OR "дата-центр" OR "ЦОД"
site:{known_hokimiyat_domain} "data center" OR "дата-центр" OR "ma'lumotlar markazi"
site:president.uz "{division_or_city}" "data center" OR "дата-центр"
site:minenergy.uz "{division_or_city}" "МВт" "дата-центр" OR "электроэнергия"
site:it-park.uz "{city_or_division}" "data center" OR "infrastructure"
"{city}" "data center" "MW" OR "Tier III"
"{city_ru}" "ЦОД" OR "центр обработки данных" "МВт"
"{city_uz}" "ma'lumotlar markazi" OR "server markazi"
```

---

## 7. Status and Evidence Rules

| Evidence found | Enumeration status |
|---|---|
| Cloud-provider official region page listing Uzbekistan | Cloud region exists; record exact location/region name. |
| Operator official facility/service page with location/capacity | Operational or announced according to page wording; record exact wording/date. |
| Uptime design certification | Certified design; not proof of constructed/operational facility. |
| Uptime constructed-facility or operational-sustainability award | Strong constructed/operational evidence; still record award type. |
| Ministry/president groundbreaking or construction-start announcement | Under construction if source says construction began/groundbreaking. |
| lex.uz decree, investment agreement, MoU, land allocation | Planned lead unless source also proves construction/commissioning. |
| Ministry of Energy MoU/tariff/PPA | Energy-backed planned lead; verify project sponsor/site and whether MW is load or grid capacity. |
| Directory-only listing | C-grade discovery lead; do not count without A/B corroboration. |

Pitfalls:

- DataVolt has multiple Uzbekistan phases; keep TAS-1, New Tashkent, and Bukhara as separate records.
- New Tashkent and Akhangaran are Tashkent Region, not Tashkent City.
- Bukhara has at least three distinct leads: Uzbektelecom/Uptime, DataVolt planned phase, LinkWise MoU.
- Kokand is in Fergana Region.
- Karakalpakstan is currently a policy/incentive hub unless a named site/operator is verified.
- LinkWise and SMR projects are planned leads until official project-company, permit, grid, or construction evidence is retrieved.
- Data-localization and AI laws drive demand but are not facility evidence.

---

## 8. Recommended Official Workflow

1. Run lex.uz policy/legal queries for new decrees, AI/data-processing infrastructure, telecom licensing, personal-data localization, and Enterprise Uzbekistan updates.
2. Search Ministry of Digital Technologies, IT Park, and president.uz for named projects, phases, ceremonies, land, MW, and status verbs.
3. Search Ministry of Energy and grid/operator sources for each MW-scale project; record whether the number is IT load, facility load, or proposed connection.
4. Re-scan Uptime country/list pages for Uzbekistan; record certification type exactly.
5. Re-check official AWS/Azure/GCP/OCI/Yandex region pages; record "not listed" only with date.
6. For all 14 divisions, run Uzbek/Russian/English gov.uz, hokimiyat, IT Park, and minenergy queries using the matrix above.
7. Dedupe by physical site/campus and sponsor/SPV; record operator, tenant, project phase, and source grade separately.

## Quick URL Index

- Ministry of Digital Technologies: https://digital.uz ; https://gov.uz/en/digital
- DataVolt ministry announcement: https://gov.uz/en/digital/news/view/10951
- Enterprise Uzbekistan ministry announcement: https://gov.uz/en/digital/news/view/105735
- Digital Uzbekistan 2030: https://lex.uz/en/docs/7008256
- Enterprise Uzbekistan decree DP-25: https://lex.uz/docs/6957961
- Telecom law LRU-1015: https://lex.uz/en/docs/7287371
- Personal Data Law LRU/ZRU-547: https://lex.uz/docs/4831939
- AI Strategy RP-358: https://lex.uz/en/docs/7159258
- Telecom regulator: https://gov.uz/en/ttsa
- IT Park: https://www.it-park.uz/en ; https://www.it-park.uz/en/itpark/infrastructure
- my.gov.uz: https://my.gov.uz
- Construction ministry/supervision: https://mc.uz ; https://nazorat.mc.uz
- Cadastre Agency: https://gov.uz/en/kadastr
- Ministry of Energy: https://minenergy.uz
- Uptime Uzbekistan: https://uptimeinstitute.com/uptime-institute-awards/country/id/UZ
- UzCloud: https://uzcloud.uz/en/infrastructure/data-centers ; https://uzcloud.uz/en/about
- UZINFOCOM / DC: https://uzinfocom.uz ; https://dc.uz
- Uztelecom cloud: https://cloud.uztelecom.uz
