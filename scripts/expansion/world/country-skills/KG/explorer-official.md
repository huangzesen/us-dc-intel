# KG Explorer — Official / Regulatory / Cloud Pipeline for Kyrgyzstan Datacenter Enumeration

Date: 2026-08-12 (final reviewed layer). Scope: methodology for discovering Kyrgyzstan datacenter projects from official, regulatory, energy, procurement, government-IT, construction-permitting, and cloud-region sources.

Reliability grades: **A** = official/primary source or operator-owned disclosure; **B** = credible trade press / regulator-adjacent source / government-media interview; **C** = aggregators, directories, maps, marketing pages without regulatory corroboration; **U** = unverified claim that could not be confirmed live during this pass. **A grade covers only the specific fact actually supported by the cited source** — a government MOU page is A for "agreement signed" but NOT A for "facility built".

---

## 0. Structure facts (administrative, legal, registry)

### 0.1 Administrative divisions (9 coverage units)
Kyrgyzstan = 7 oblasts (regions) + 2 cities of republican significance. Cities and their surrounding oblasts are separate divisions — Bishkek is NOT part of Chuy oblast administratively, and Osh City is NOT part of Osh oblast (avoid conflation in the result schema).

| Division | Russian | Kyrgyz | Admin type |
|---|---|---|---|
| Bishkek | Бишкек | Бишкек | City of republican significance (capital) |
| Osh City | Ош (город) | Ош шаары | City of republican significance |
| Chuy | Чуйская область | Чүй облусу | Oblast (surrounds Bishkek; admin center Bishkek) |
| Osh | Ошская область | Ош облусу | Oblast (admin center Osh City) |
| Jalal-Abad | Джалал-Абадская область | Жалал-Абад облусу | Oblast |
| Batken | Баткенская область | Баткен облусу | Oblast |
| Naryn | Нарынская область | Нарын облусу | Oblast |
| Talas | Таласская область | Талас облусу | Oblast |
| Issyk-Kul | Иссык-Кульская область | Ысык-Көл облусу | Oblast |

Oblast centers: Chuy (Bishkek), Osh (Osh City), Jalal-Abad (Jalal-Abad), Batken (Batken), Naryn (Naryn), Talas (Talas), Issyk-Kul (Karakol / Каракол). District (rayon) and local-government sites live under `okmot.kg` subdomains (e.g. `trade.okmot.kg` exists; local aiyl-okmotu sites are weak sources).

### 0.2 National registries and portals (what exists / what does not)
- **Legal-entity registry** (Единый государственный реестр юридических лиц, филиалов/представительств, ЕГРЮЛФ(П)) — official public surface: https://record.minjust.gov.kg/ . Supporting service pages: https://egov.kg/ru/gov-services/2314 (extract from the register) and Tunduk catalog entry https://catalog.tunduk.kg/subsystems/detail/24 . Private mirrors such as `osoo.kg`, `reestr.kg`, and `analyt-kg.com` are discovery-only (**C**) unless the same entity data is confirmed at the Ministry of Justice registry.
- **Personal-data authority and registers**: https://dpa.gov.kg/ is the official agency surface. The legacy register of holders of personal-data massifs at https://registry.dpa.gov.kg/ remains live and explicitly notes that registration under the old personal-data law stopped when the Digital Code entered into force on 2026-02-05. Regulatory-acts surface: https://reestr.dpa.gov.kg/ .
- **Open data portal of state agencies**: https://data.gov.kg/ is the current open-data portal. Older Infocom-hosted references may appear in archived material; use `data.gov.kg` first.
- **Public procurement**: https://zakupki.gov.kg/ (official portal; new web-portal version piloted under Cabinet Order No. 302 of 2025-04-17 — see https://zakupki.gov.kg/popp/home.xhtml); legacy/tender surface: https://trade.okmot.kg (Ministry of Finance e-procurement, ЭГЗ); private aggregator: https://www.gostender.kg/. Search terms: `ЦОД`, `центр обработки данных`, `серверная`, `хостинг`, `облачные услуги`, `дата-центр`.
- **Construction / planning permits**: there is no single national public planning-permit search comparable to US/UK county systems. Relevant official surfaces are the Ministry of Construction page on egov.kg, the old landing page https://minstroy.gov.kg/ru, Bishkek architecture office https://bga.kg/ , and the online submission cabinet referenced by BGA/ministry notices (`cabinet.bga.gov.kg`). Treat these as lead sources; facility commissioning still needs procurement, local-government, operator, grid, or acceptance evidence.
- **Company disclosure**: joint-stock operators (e.g. KyrgyzTelecom OJSC) publish on `kt.kg`; no mandatory facility-level DC disclosure exists.

### 0.3 Legal / regulatory basis
- **Цифровой кодекс КР (Digital Code of the Kyrgyz Republic), Law No. 178 of 2025-07-31** — core codification for the digital environment: e-services, digital data, IT regulation, personal data, e-governance. Signed by the President (announced 2025-06-18, president.kg news 39423); entered into force 2026-02-05 (six months after publication; confirmed by registry.dpa.gov.kg notice). Official text: https://cbd.minjust.gov.kg/3-48/edition/35412/ru (Centralized Legal Database, CBD). **A** for existence/dates.
- **Law No. 179 of 2025-07-31** — on entry into force of the Digital Code; repealed Law KR No. 58 of 2008-04-14 «Об информации персонального характера» (personal data). Old-law text for historical reference: https://portal.tunduk.kg/assets/doc/personal_info_ru.pdf. **A** for the repeal fact (reestr.dpa.gov.kg/ru/npa/4).
- **Law «О связи»** (on communications) — sector law; telecom and postal licensing historically sat under the digital ministry / communications inspection service. Use CBD legal database search at https://cbd.minjust.gov.kg/ and the digital-services pages for the current responsible body after the 2026 reorganization.
- **Public procurement law and tenders** — implemented via https://zakupki.gov.kg/ and the new `popp` portal. Procurement records are **A** for lot names, purchaser, amounts, dates, addresses, and technical requirements visible in the record.
- **E-government / Taza Koom heritage**: state e-services portal https://egov.kg/ (also https://portal.tunduk.kg/) — the «Тундук» e-services system now operates under state enterprise **ГП «Инфоком»** (Infocom) at the State Registration Service (per kglabs/economist.kg reporting — **B**); Infocom is the operational owner of government e-gov infrastructure and the natural operator of any state data center.
- **Data protection post-Digital Code**: use https://dpa.gov.kg/ and https://registry.dpa.gov.kg/ to establish the current personal-data compliance regime. Do not infer data-localization or sovereign-hosting requirements from commentary; cite the Digital Code / implementing acts directly when those obligations matter.

---

## 1. Search vocabulary (Russian first, then Kyrgyz, then English)

Russian dominates official documents, procurement, and press. Kyrgyz appears on republic portals (egov.kg, gov.kg, kt.kg) and local okmot pages. English works only for flagship projects, investment promotion, and international press.

- English: `data center`, `datacenter`, `data centre`, `server farm`, `colocation`, `hosting`, `cloud`, `cloud region`, `digital infrastructure`, `internet exchange / IXP`, `submarine cable`, `landing station`, `edge node`, `CDN`.
- Russian: `дата-центр`, `датацентр`, `центр обработки данных`, `ЦОД`, `ЦХОД`, `серверная`, `серверное оборудование`, `колокация`, `хостинг`, `облачные услуги`, `облачная инфраструктура`, `цифровая инфраструктура`, `точка обмена трафиком`, `магистральный канал`, `подводный кабель`, `станция посадки кабеля`, `вычислительный центр`, `суперкомпьютер`, `ИИ-инфраструктура`, `майнинг`, `ферма`, `строительство ЦОД`, `технические условия`, `разрешение на строительство`, `электроснабжение`.
- Kyrgyz (rare in practice): `маалымат борбору` (data center), `сервер бөлмөсү` (server room), `хостинг`, `булут технологиялары` (cloud), `санарип инфраструктура` (digital infrastructure), `трафик алмашуу пункту` (IXP), `суу астындагы кабель` (submarine cable), `курулуш` (construction).

---

## 2. Official / regulatory pipeline

### 2.1 Digital transformation authority and communications regulator
- **Digital governance body** — historical ministry site: https://digital.gov.kg/ . As of the live review, the site and egov directory use «Министерство цифрового развития и инновационных технологий Кыргызской Республики» / МЦРИТ. However, Presidential Decree No. 154 of 2026-04-29 (`cbd.minjust.gov.kg/5-11103/edition/52497/ru`, also announced at https://president.kg/ru/news/21/40353) reorganized the ministry by attaching it to the Department of Affairs of the President, which became the legal successor and coordinator for digital transformation. Search both the legacy ministry name and `Управление делами Президента` for 2026+ items.
  - The legacy ministry site remains a useful primary source for pre-reorganization news and service pages, including the 2025 Inspur Yunzhou MOU and communications/postal service references.
  - For post-2026 records, prefer CBD, President/Cabinet announcements, egov agency pages, and procurement records over stale site headers.
- **Служба по регулированию и надзору в отрасли связи / communications inspection** — no reliable standalone regulator portal was found in the live pass. Its functions appear through digital.gov.kg/egov service pages and legal acts. For datacenter enumeration, use it for licensed telecom-operator lists, numbering, interconnection, and ISP enforcement signals, not as evidence that a physical DC exists.
- Utility: regulator action (e.g. 2025 TikTok blocking letters — toppress.kz) shows the regulator directs ISPs; for DC enumeration the regulator matters mainly for licensed-operator lists and ISP licensees.

### 2.2 Cabinet, President, investment promotion
- Cabinet of Ministers: https://www.gov.kg/ (NPA section https://www.gov.kg/ru/npa — search `ЦОД`, `дата-центр`, `цифровой`).
- President: https://president.kg/ (e.g. Digital Code signing news 39423).
- **National Investment Agency under the President of the Kyrgyz Republic** (created by Decree UP No. 115 of 2022-04-15): https://invest.gov.kg/ (RU/EN); news: https://invest.gov.kg/ru/news. Official channel for foreign-investor DC MOUs — grade **A for signed agreements/announcements**, **C for implied construction**. Use for the Inspur Yunzhou and other investor leads.

### 2.3 Energy / grid pipeline
- **OJSC «Национальная электрическая сеть Кыргызстана» (NESK)** — national high-voltage grid operator (successor of AO «Кыргызэнерго» transmission function): https://www.nesk.kg/ru/. News and investment pages reveal substations, power availability, and large-consumer connections (e.g. Issyk-Kul F1H2O power support news, 2026). Any DC above ~1 MW should be cross-checked against NESK grid-connection news. **A** for grid-level statements.
- **Ministry of Energy** — https://minenergo.gov.kg/ru . Search ministry news for power-supply MOUs, tariff policy, import constraints, and mining/DC power restrictions.
- **OJSC «Электрические станции»** (Electric Stations, generation) — https://www.energo-es.kg/ . Useful for hydropower assets and winter-preparation context; do not treat generation-company news as a grid-connection approval.
- Policy context (affects DC siting): Kyrgyzstan has hydropower-heavy generation but winter deficits and recurring restrictions on energy-intensive loads. Cabinet/CBD acts include mining-specific electricity/tariff classifications (search CBD for `майнинг`, `криптовалюта`, `расчетно-вычислительный центр блокчейна`). Treat high-MW «data center» announcements skeptically until the power source, tariff category, and connection point are confirmed.

### 2.4 Government IT / e-government surface
- **ГП «Инфоком»** (Infocom) — state enterprise associated with e-gov infrastructure and the «Тундук» ecosystem; use https://portal.tunduk.kg/ and current open-data portal https://data.gov.kg/ for primary service evidence. Infocom is a natural state-IT operator lead for national/G-Cloud infrastructure. **A- for state-IT service facts**; facility details are usually non-public.
- **egov.kg** — e-government portal (https://egov.kg/ru); services catalog may expose DC/hosting procurement demand.
- **High Technology Park (ПВТ/HTP)** — https://htp.kg/ (RU: https://htp.kg/ru/); special tax regime for IT exporters; HTP resident lists can surface hosting/cloud companies that later build or lease DC space. **A** for resident-regime facts; **C** for any implied facilities.
- **State data processing center (Государственный ЦОД)**: the digital ministry announced a design/procurement process in Aug 2023. The procurement lead at https://zakupki.gov.kg/popp/view/order/view.xhtml?id=394299634 and press coverage (24.kg / Economist.kg) describe a design assignment around 84.878m KGS, 1,400 sq m, and 150 racks. This is **A** for the tender and **B** for press-reported specs, but not evidence of a completed national facility. A separate 2026 Ministry of Internal Affairs procurement record (`id=563665919`) is for a ministry-owned DC/system with installation and commissioning at Bishkek, pr. Ch. Aitmatova 95; record separately and do not merge it with the national/state-cloud DC unless a source explicitly links them.

### 2.5 E-procurement pipeline
- https://zakupki.gov.kg/ (new portal, pilot 2025), https://trade.okmot.kg (ЭГЗ), https://www.gostender.kg/ (aggregator). Query patterns: `ЦОД`, `центр обработки данных`, `дата-центр`, `серверная`, `хостинг`, `облачные услуги`, `виртуальные серверы`, `электроснабжение`, `технические условия`. Procurement of hosting/DC services by ministries and akimats is the strongest **A-grade** evidence of state-sector DC usage; design/construction lots signal new facilities.

### 2.6 Cloud-region official pages (AWS / Azure / GCP / OCI / Yandex) — check each run
- AWS regions: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure geographies: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle Cloud regions: https://www.oracle.com/cloud/public-cloud-regions/
- Yandex Cloud regions: https://yandex.cloud/en/docs/overview/concepts/region
- As of the 2026-08-12 live review, no Kyrgyzstan public cloud region is listed on the official AWS, Azure, Google Cloud, Oracle Cloud, or Yandex Cloud region/location pages. Re-check these provider-owned pages every enumeration run; any KG hyperscaler-region claim must be backed by the provider’s official region list, not by local reseller marketing.

---

## 3. Query templates (official pipeline)

```text
site:digital.gov.kg "ЦОД"
site:digital.gov.kg "центр обработки данных"
site:digital.gov.kg "дата-центр"
site:digital.gov.kg "Inspur"
site:president.kg "цифровая трансформация" "Управление делами Президента"
site:cbd.minjust.gov.kg "ЦОД"
site:cbd.minjust.gov.kg "майнинг" "электроэнергия"
site:gov.kg "ЦОД"
site:gov.kg "центр обработки данных"
site:gov.kg "{division_ru}" "ЦОД" "строительство"
site:gov.kg "{division_ru}" "дата-центр" "разрешение"
site:invest.gov.kg "data center"
site:invest.gov.kg "центр обработки данных"
site:nesk.kg "центр обработки данных"
site:nesk.kg "дата-центр"
site:nesk.kg "электроснабжение" "майнинг"
site:nesk.kg "подстанция" "{city_ru}"
site:zakupki.gov.kg "ЦОД"
site:zakupki.gov.kg "центр обработки данных"
site:zakupki.gov.kg "серверная"
site:trade.okmot.kg "ЦОД"
site:trade.okmot.kg "хостинг"
site:data.gov.kg "центр обработки данных"
site:data.gov.kg "связи"
site:htp.kg "дата-центр"
site:htp.kg "cloud"
site:cbd.minjust.gov.kg "Цифровой кодекс"
"Кыргызстан" "центр обработки данных" "строительство" "{year}"
"Бишкек" "ЦОД" "конкурс"
"Бишкек" "ЦОД" "проектирование"
"{division_ru}" "дата-центр" "технические условия"
"{division_ru}" "ЦОД" "{city_ru}" "ввод в эксплуатацию"
"Кыргызстан" "майнинг" "электроэнергия" "ограничение"
site:invest.gov.kg "{project_name}" "меморандум"
site:gov.kg "{project_name}" "инвестиционное соглашение"
```

---

## 4. Per-division enumeration approach and realistic expectations

Market reality: the Kyrgyz commercial DC market is small and Bishkek-centric (one Tier-III-class commercial DC opened 2024; Data Center Map lists ~3 facilities, all in Bishkek). Outside Bishkek expect only legacy telecom exchanges, bank/server rooms, and possibly crypto farms. Prioritize Bishkek > Chuy > Osh City > others.

| Division | Anchors (RU) | Official/regulatory approach | Realistic expectation |
|---|---|---|---|
| Bishkek | Бишкек | digital.gov.kg legacy news, President/CBD after the 2026 reorganization, state ЦОД status, zakupki.gov.kg DC/hosting lots, NESK connections, BGA/Bishkek city architecture news | Primary hub: Datatime, KyrgyzTelecom DC/colo services, KG-IX, ISP/server rooms, state/MIA DC procurements. Expect the majority of all KG records |
| Chuy | Чуйская область | Oblast administration news; industrial-zone and mining-farm reports (Tokmok, Kant, Kara-Balta, Sokuluk, Lebedinovka); power connections via NESK/regional grid | Secondary: mining/HPC and Bishkek-adjacent operator leads. Data Center Map lists an NSP facility in Lebedinovka; treat as directory lead until operator/registry evidence confirms physical DC details |
| Osh City | Ош (город) | City administration news; KyrgyzTelecom and Aknet Osh branches, procurement by southern agencies, radio-monitoring/communications office signals | Low: regional telecom/server rooms and hosting sales offices; no independently confirmed commercial colo DC |
| Osh | Ошская область | Oblast administration; border-trade/industrial zones (Kara-Suu); Nookat-area ISPs (e.g. Eletcom) | Very low |
| Jalal-Abad | Джалал-Абадская область | Oblast administration; Tash-Kumyr coal/energy towns (possible energy-led leads); mining reports | Very low |
| Batken | Баткенская область | Oblast administration; border/security context (Tajikistan border) | Essentially none; check for any state edge infrastructure |
| Naryn | Нарынская область | Oblast administration; hydropower cascade context; no DC pull factors | Essentially none |
| Talas | Таласская область | Oblast administration; small economy | Essentially none |
| Issyk-Kul | Иссык-Кульская область | Oblast/Karakol administration; tourism-driven digital projects; F1H2O/power events; Cholpon-Ata | Very low; watch resort/event digital-infrastructure contracts |

Per-division official query template (substitute division/city in Russian and Kyrgyz):
```text
"{division_ru}" "{city_ru}" "дата-центр" "строительство"
"{division_ru}" "{city_ru}" "ЦОД" "тендер"
"{division_ru}" "{city_ru}" "центр обработки данных" "ввод в эксплуатацию"
"{division_ru}" "{city_ru}" "серверная" "технические условия"
"{division_ky}" "маалымат борбору" "курулуш"
"{division_ky}" "сервер" "санарип"
```

---

## 5. Reliability grades and the coverage rule

- **A** — official/primary: ministry/Cabinet/President decrees and news; procurement award documents (zakupki.gov.kg / trade.okmot.kg); NESK/energy documents; CBD legal texts; registry.dpa.gov.kg entries; operator-owned statements (e.g. datatime.kg for its own facility existence; kt.kg for KyrgyzTelecom services). Grade A **only for the fact the document states** (e.g. A for "design tender announced 2023", NOT for "DC operational").
- **B** — regulator-adjacent / reliable trade press: 24.kg, Economist.kg, Tazabek, Akchabar, Sputnik KG, Kabar (state agency), TAdviser/CNews product pages, kglabs.org technical write-ups, international press (DCD, Developing Telecoms) quoting named officials.
- **C** — aggregators/directories/maps: Data Center Map, datacenters.com, Cloudscene, hostings.info, 2GIS, Yandex Maps, ix.report stats (use for discovery only).
- **U** — unsupported or internally inconsistent claims; also any capacity figure where the source does not define IT load vs grid power vs marketing headline. Do not leave a claim at **U** in the final dataset if it can be resolved by primary/operator research.
- Rule: **an entry's grade covers only the fact actually supported.** If a facility claim rests on a marketing page but its address comes from 2GIS, record two facts with two grades.

---

## 6. Known facilities / projects and evidence status (as of 2026-08-12)

| # | Name / project | Division | Status | Evidence & grade |
|---|---|---|---|---|
| 1 | **Datatime / Datatime Bishkek KR Data Center Data 5** | Bishkek | Operational; opened 2024-06-10/11; Uptime Tier III Certification of Design Documents exists | Operator site https://datatime.kg/en/ and opening news (A for existence, launch, address Koytashsky lane 46/1, 500 kW+ marketing capacity, power/cooling descriptions); Uptime Institute project page https://uptimeinstitute.com/component/tierachievement/datacenter/datatime-bishkek-kr-data-center-data-5/2191 (A for Tier III Design certification only, not constructed-facility/operations certification); RackCorp partner page (B); DCD/24.kg/Economist/Sputnik for launch/funding context (B) |
| 2 | **Государственный ЦОД / national state DC design project** | Bishkek likely, exact site not public | Design/procurement lead, not confirmed operational | Procurement record `https://zakupki.gov.kg/popp/view/order/view.xhtml?id=394299634` (A for tender); 24.kg and Economist.kg Aug 2023 coverage (B, includes 84.878m KGS design budget and 150-rack/1,400 sq m reported specs). Require construction/commissioning evidence before counting |
| 3 | **MIA / GUFHO Ministry of Internal Affairs DC procurement** | Bishkek | Procurement in 2026 for DC with installation/commissioning | `https://zakupki.gov.kg/popp/view/order/view.xhtml?id=563665919` (A: purchaser, 127,988,941 KGS planned amount, delivery at Bishkek, pr. Ch. Aitmatova 95, 120-day delivery, DC/module/UPS/precision-cooling requirements). Count as a government DC procurement lead; operational status requires acceptance/commissioning record |
| 4 | **KyrgyzTelecom ЦОД / co-location services** | Bishkek plus telecom exchanges | Operational service offering; facility-level details limited | kt.kg DCASA page https://kt.kg/ru/dcasa-rus/ states co-location in KyrgyzTelecom data centers (A for service offering). TAdviser and 2017 press describe a planned/introduced Tier-III-level concept with 5 MW project capacity (B/C for historical lead, not current certification). Regional exchanges should be tagged `telecom exchange/server room` unless facility evidence exists |
| 5 | **Inspur Yunzhou Industrial Internet (China) cooperation** | Site not disclosed | MOU / planned lead only | Official digital.gov.kg post (2025) states an MoU covering digital technologies, DC construction, cloud, AI, and industrial internet (A for MoU intent only). No land, grid, construction, capacity, or commissioning evidence found; do not count as a facility |
| 6 | **Infocom / Тундук / G-Cloud infrastructure** | Bishkek likely | Operational state e-services platform; DC building non-public | portal.tunduk.kg, egov.kg, data.gov.kg, and Infocom references are A for services/platform operation. Building/site details need procurement/operator confirmation |

| 7 | **IFS data-center services** | Bishkek | Service offering / integrator lead | https://www.ifs.kg/centr-obrabotki-dannyh-data-centr/ (B/C: explicit service page, but not enough to count a standalone physical colocation facility without supporting evidence) |
| 8 | **KG-IX / IX.KG internet exchange** | Bishkek | Operational IX | PeeringDB https://www.peeringdb.com/ix/2145 (A for IX: 22 peers, 29 connections, 1.0T total capacity, Bishkek, KG-IX LLC); ix.kg and RIPE records (A/B depending page); Data Center Map IXP page and kglabs.org backbone write-up as discovery/context |
| 9 | **No subsea cable landing stations** | — | N/A — landlocked country | Methodological fact: Kyrgyzstan is landlocked; international connectivity is terrestrial through Kazakhstan/China/Tajikistan/Uzbekistan corridors. Use cable maps only to confirm there is no erroneous “landing station” record |
| 10 | **Uptime Institute certifications** | Bishkek | One KG Uptime record found: Datatime Tier III Design | Uptime project page is A for Design certification. No separate KG Constructed Facility or Operations certification was found in this pass |
| 11 | **Crypto-mining / blockchain computing centers** | Chuy, Jalal-Abad, Osh regions most likely | Separate category; not enterprise colo by default | CBD/ministry/press evidence supports mining-specific regulation and electricity treatment. Record as `mining/HPC` unless a source documents third-party colocation/cloud customers |

---

## 7. Update / re-check cadence

- **Monthly**: President/Cabinet/CBD and legacy digital.gov.kg news for `ЦОД/дата-центр`; zakupki.gov.kg for new DC/hosting lots; NESK and Minenergo news for grid/power items; PeeringDB KG-IX page for participant/capacity changes.
- **Quarterly**: re-check state ЦОД status (design → construction → commissioning verbs); re-run cloud-region official pages (AWS/Azure/GCP/OCI/Yandex) for any KG entry; Uptime Institute awards list for KG.
- **Semi-annually**: refresh the post-Decree-154 governance routing, check for a standalone communications-regulator site, confirm the legal-entity and open-data portals, and check Digital Code implementing acts on DC siting/localization.
- **Event-driven**: presidential/cabinet decrees; invest.gov.kg announcements (Chinese/Russian investor MOUs); energy-crisis regulations affecting mining/DC power.

## Quick URL index

- Digital transformation authority: legacy https://digital.gov.kg/ | egov directory https://egov.kg/ru/ministry/digital/1438 | Decree No. 154 https://cbd.minjust.gov.kg/5-11103/edition/52497/ru
- Cabinet of Ministers: https://www.gov.kg/ru | President: https://president.kg/
- National Investment Agency: https://invest.gov.kg/ru | news: https://invest.gov.kg/ru/news
- NESK (grid): https://www.nesk.kg/ru/
- Procurement: https://zakupki.gov.kg/ | https://trade.okmot.kg | https://www.gostender.kg/
- E-services/Тундук: https://portal.tunduk.kg/ | https://egov.kg/ | open data https://data.gov.kg/
- Legal entities: https://record.minjust.gov.kg/ | egov extract service https://egov.kg/ru/gov-services/2314
- Construction: https://egov.kg/ru/ministry/construction | https://minstroy.gov.kg/ru | https://bga.kg/
- HTP: https://htp.kg/
- CBD legal database: https://cbd.minjust.gov.kg/ (Digital Code: /3-48/edition/35412/ru)
- Personal data: https://dpa.gov.kg/ | https://registry.dpa.gov.kg/ | https://reestr.dpa.gov.kg/
- Cloud regions: AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ · Azure https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/ · GCP https://cloud.google.com/about/locations · OCI https://www.oracle.com/cloud/public-cloud-regions/ · Yandex https://yandex.cloud/en/docs/overview/concepts/region
- KG-IX (PeeringDB): https://www.peeringdb.com/ix/2145
- Datatime: https://datatime.kg/ | RackCorp KG: https://www.rackcorp.com/ru/network/datacenters/kyrgyzstan/datatime/
- KyrgyzTelecom: https://kt.kg/ru/ | DCASA https://kt.kg/ru/dcasa-rus/
- Data Center Map KG: https://www.datacentermap.com/kyrgyzstan/ (Bishkek: https://www.datacentermap.com/kyrgyzstan/bishkek/)

