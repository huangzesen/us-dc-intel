# KZ Explorer — Industry/Vendor Discovery for Kazakhstan Datacenters

Date: 2026-08-12. Scope: Kazakhstan datacenter enumeration from colo providers, cloud regions, trade press, associations/investment bodies, and region-specific query patterns. Reliability grades: **A** = official/primary (government, operator official, cloud-provider official, Uptime certification, audited issuer disclosure), **B** = strong secondary/trade press or credible project database, **C** = weak directory/map/aggregator or announcement without hard project evidence.

---

## 0. Kazakhstan-specific frame

- Kazakhstan is a bilingual/trilingual search market. Search in **English**, **Russian**, and **Kazakh**. Russian usually gives the broadest coverage for commercial operators and government news; Kazakh catches gov.kz reposts and local-akimat pages. Core terms:
  - English: `data center`, `datacenter`, `cloud region`, `colocation`, `Tier III`, `Tier IV`, `AI infrastructure`, `hyperscale`, `digital mining`.
  - Russian: `центр обработки данных`, `ЦОД`, `дата-центр`, `дата центр`, `облачный регион`, `колокация`, `серверная`, `майнинг дата-центр`, `строительство ЦОД`, `инвестиционный проект`.
  - Kazakh: `деректерді өңдеу орталығы`, `деректер орталығы`, `дата орталығы`, `бұлттық`, `цифрлық инфрақұрылым`, `майнинг`.
- The national market splits into four discovery buckets:
  1. **Classic telecom/colo and sovereign cloud**: Kazakhtelecom, Kazteleport, Freedom Cloud/Freedom Telecom, Transtelecom, PS/NAT/NLS/Serverspace-hosted facilities.
  2. **New hyperscale/AI projects**: Data Center Valley in Ekibastuz, Akashi in Astana, GK Hyperscale Akmola/Temirtau, Beeline/Hyper Cloud in Almaty, Freedom Cloud Alatau.
  3. **Public cloud regions/PoPs**: Yandex Cloud has an explicit Kazakhstan region/PoP; global US hyperscalers are prospects/partners but do not show a public Kazakhstan region on their official region lists as of this date.
  4. **Digital-mining data centers**: Kazakhstan has many high-power mining facilities that directories may label as data centers. Record them separately unless there is enterprise colo/cloud evidence.
- Best starting geography: **Astana, Almaty City/Almaty Region, Karaganda, Pavlodar/Ekibastuz, Akmola, Aktau/Mangystau, Atyrau**, then Kazakhtelecom regional IDCs in every oblast center.

---

## 1. Authoritative and strong sources

### 1.1 Government, investment, and regulatory sources

| Source | URL | Use | Grade |
|---|---|---|---|
| Prime Minister of Kazakhstan | https://primeminister.kz/en/news/data-center-valley-kazakhstan-government-firebird-and-nvidia-sign-10-billion-package-of-agreements-in-artificial-intelligence-31516 | Primary source for Data Center Valley / Firebird / NVIDIA / Kazakhtelecom agreements and AI infrastructure claims. | A |
| GOV.KZ / Ministry of AI & Digital Development and regional akimats | https://www.gov.kz/ | Search national and oblast press releases for `ЦОД`, `дата-центр`, `деректерді өңдеу орталығы`, project MOUs, telecom strategy, e-government DPCs. | A for official announcement; C for MOU-only projects |
| Astana Hub | https://astanahub.com/ | Strong source for technology-sector investment announcements, including GK Hyperscale. | B+ |
| Invest Kazakhstan | https://invest.gov.kz/ | Investment treaty / KGIR / investor announcement source; good for proposed projects and counterparties. | B+ |
| AIFC | https://aifc.kz/ | Sector discussions, investor positioning, digital-infrastructure policy; rarely facility-level but useful for names. | B |
| eGov licensing / eLicense | https://egov.kz/cms/en/news/digital-mining and https://egov.kz/cms/en/services/licensing/passEL4-L23_mcriap | Digital mining licensing; use to separate mining data centers from enterprise colo/cloud. | A |
| RSP business inspection register | https://rsp.gov.kz/ru/plan and https://rsp.gov.kz/ru/rsp | Search object names such as `центр обработки данных`; can reveal facility addresses/operators such as Kazakhtelecom Astana. | A for registry entry, but not capacity |
| Kazakhstan public procurement | https://www.goszakup.gov.kz/ | Search tenders/contracts for `ЦОД`, `серверная`, `дата-центр`, `облачные услуги`, `хостинг`, `электроснабжение`; useful for government IDC/hosting evidence. | A for award/contract signal |
| Bureau of National Statistics | https://stat.gov.kz/en/industries/business-statistics/stat-service/ | Sector stats include service categories for server-room/data-center activities; use as macro context, not facility list. | A for aggregate stats |

Important: in Kazakhstan, **MOU/investment-agreement articles are common and should not be counted as construction** unless followed by land allocation, construction start, procurement, grid/power evidence, Uptime certification, operator page, or trade-press construction reporting.

### 1.2 Operator, certification, and directory sources

| Source | URL | Use | Grade |
|---|---|---|---|
| Kazakhtelecom annual reports | https://ar2021.telecom.kz/en/information-technology.html | Primary corporate source; 2021 report says Kazakhtelecom had 25 data centers nationally and gives example capacity additions. | A |
| Kazteleport / Uptime listings | https://uptimeinstitute.com/uptime-institute-awards/datacenter/kazteleport-sairam-data-center-/1403 | Certification-level source for named Kazteleport facilities and Tier evidence. | A |
| Freedom Cloud / Freedom Cloud Holding | https://fch.kz/en/freedom-cloud-holding/ | Operator source; states Freedom cloud/data-center footprint and service lines. | A- |
| Akashi Data Center | https://akashi.cloud/ | Official source for Astana Tier IV project, rack count, IT MW, build status. | A |
| VEON / Beeline Kazakhstan | https://www.veon.com/newsroom/press-releases/veons-beeline-kazakhstan-breaks-ground-for-hyper-cloud-data-center-to-offer-sovereign-enterprise-ai-and-digital-services | Official source for Hyper Cloud construction in Almaty. | A |
| Yandex Cloud Kazakhstan region | https://yandex.cloud/en/blog/posts/2024/04/yandex-cloud-in-kazakhstan and https://yandex.cloud/en/docs/overview/concepts/region | Official source for Kazakhstan cloud region. | A |
| Yandex Cloud Interconnect PoPs | https://yandex.cloud/en/docs/interconnect/concepts/pops | Official PoP table; identifies Freedom Telecom data center in Karaganda. | A |
| Enegix | https://enegix.net/en | Official source for Ekibastuz high-power grid-connected campus. Treat as crypto/HPC unless enterprise colo evidence appears. | A |
| Uptime Institute awards search | https://uptimeinstitute.com/uptime-institute-awards/list | Facility names, tier certifications, operators; reliable existence/certification source. | A |
| Data Center Dynamics Kazakhstan tag | https://www.datacenterdynamics.com/en/news/?tag=kazakhstan | Best trade press for project starts, capacity numbers, cloud-region launches. | B |
| Data Center Map Kazakhstan | https://www.datacentermap.com/kazakhstan/ | Broad facility seed list by city/operator; capacity and addresses need verification. | B/C |
| Datacenters.com Kazakhstan | https://www.datacenters.com/locations/kazakhstan | Broad facility seed list; useful for obscure colo names, weaker for capacity. | C unless corroborated |
| Cloudscene Kazakhstan | https://cloudscene.com/market/kazakhstan/all | Market and provider directory; good seed list, verify elsewhere. | C |
| Yandex Maps / 2GIS | https://yandex.com/maps/ and https://2gis.kz/ | Local address discovery for small facilities and crypto farms; weak evidence only. | C |

---

## 2. Query templates

### 2.1 National discovery

Use Google/Bing/Yandex; for gov.kz pages, exact Russian/Kazakh terms often work better than English.

```text
Kazakhstan "data center" "MW" "racks"
Kazakhstan "hyperscale data center" "Astana" OR "Almaty" OR "Ekibastuz"
Kazakhstan "cloud region" "data center"
Kazakhstan "colocation" "Tier III" "Almaty"
Kazakhstan "digital mining" "data center" "MW"

site:gov.kz "центр обработки данных" "строительство"
site:gov.kz "дата-центр" "инвестиционный проект"
site:gov.kz "деректерді өңдеу орталығы" "жоба"
site:primeminister.kz "data center" Kazakhstan
site:astanahub.com "data center" Kazakhstan
site:invest.gov.kz "центр обработки данных"
site:goszakup.gov.kz "ЦОД" OR "центр обработки данных"
site:rsp.gov.kz "центр обработки данных" "{city}"
```

### 2.2 Operator/vendor sweeps

```text
"Kazakhtelecom" "data center" "{city}"
"Казахтелеком" "центр обработки данных" "{city}"
"Kazteleport" "data center" "Sairam" OR "Ereymentau" OR "Aktau"
"Казтелепорт" "ЦОД" "{city}"
"Freedom Cloud" "data center" "Kazakhstan" "{city}"
"Freedom Telecom" "дата-центр" "{city}"
"Yandex Cloud" "Kazakhstan region" "Karaganda"
"Beeline Kazakhstan" "Hyper Cloud" "Almaty"
"AKASHI" "data center" "Astana"
"Enegix" "Ekibastuz" "data center" "MW"
"Transtelecom" "data center" "Kazakhstan" "{city}"
"NAT Kazakhstan" "data center"
"NLS Kazakhstan" "data center"
```

### 2.3 Status and capacity extraction

```text
"{project name}" "MW" OR "МВт" OR "қуаты"
"{project name}" "racks" OR "стойк" OR "стоек" OR "серверлік"
"{project name}" "Tier III" OR "Tier IV" OR "Uptime Institute"
"{project name}" "construction began" OR "началось строительство" OR "құрылысы басталды"
"{project name}" "commissioned" OR "launched" OR "введен в эксплуатацию" OR "іске қосылды"
"{operator}" "annual report" "data centers" Kazakhstan
```

Lifecycle verbs:
- English: `signed`, `agreement`, `planned`, `construction began`, `breaks ground`, `launched`, `commissioned`, `go live`.
- Russian: `подписали соглашение`, `меморандум`, `планируется`, `началось строительство`, `заложили`, `введен в эксплуатацию`, `запущен`.
- Kazakh: `келісім`, `жоспарлануда`, `құрылысы басталды`, `іске қосылды`, `пайдалануға берілді`.

---

## 3. Key vendors and project families to seed

### 3.1 Incumbent telecom and colo/cloud operators

- **Kazakhtelecom JSC** — national incumbent and likely the broadest regional IDC footprint. The 2021 integrated report states a network of 25 data centers across Kazakhstan. Seed every oblast-center query with `Казахтелеком ЦОД {city}` and cross-check with KASE issuer news, annual reports, RSP object registry, and Data Center Map. **Grade A for annual-report totals; facility-level capacity often missing.**
- **Kazteleport JSC** — Halyk Bank subsidiary, strong enterprise/cloud provider. Known facilities include Sairam/Almaty and Ereymentau/Astana; Uptime listings provide certification evidence. Search `Kazteleport Sairam`, `Kazteleport Ereymentau`, `Kazteleport Aktau`, `Казтелепорт ЦОД`. **Grade A where Uptime/operator evidence exists.**
- **Freedom Cloud / Freedom Telecom / Freedom Data Centers** — rapidly expanding local cloud/colo network. Official Freedom Cloud Holding page says 7 Tier III data centers; Yandex Cloud docs identify Freedom Telecom Karaganda as a PoP. Search every regional capital plus `Freedom Data Centers` in Yandex Maps/2GIS. **Grade A- for official footprint; verify each site.**
- **Beeline Kazakhstan / VEON / Hyper Cloud Solution** — Almaty sovereign enterprise/AI cloud data center under construction; official VEON release is primary. **Grade A.**
- **Transtelecom (TTC)** — telecom operator with facility/directory hits in Oskemen/Ust-Kamenogorsk, Uralsk and likely other rail/telecom nodes. Search Russian name variants: `Транстелеком ЦОД`, `АО Транстелеком дата-центр`. **Usually C until corroborated.**
- **NAT Kazakhstan, PS Cloud Services, NLS Kazakhstan, Serverspace/Falconcloud-hosted clusters** — smaller hosting/cloud providers, often colocated inside Kazteleport/Kazakhtelecom. Record the physical facility and tenant separately to avoid double counting.

### 3.2 Hyperscale, AI, and high-power projects

- **Data Center Valley / Ekibastuz (Pavlodar Region)** — government/Kazakhtelecom/Firebird/NVIDIA project. Prime Minister source describes strategic agreements and a large GPU cluster; later trade press reports discuss 125 MW/250 MW/1 GW phasing. Treat official government source as A for agreement; count capacity by phase only where construction/deployment is explicit.
- **Akashi Data Center / Astana** — official site reports 4,224 racks and 100 MW IT capacity across four buildings; use as a primary project source, then cross-check Uptime/Astana Times/DCD for status.
- **GK Hyperscale / Akmola + Temirtau** — Astana Hub/QazProjects/Kursiv sources describe two Tier III 100 MW facilities. As of this methodology, this is a planned investment: record as planned unless construction evidence appears.
- **Freedom Cloud Alatau Technopark / Almaty area** — Freedom/Turlov/QazProjects sources report construction start, 480 racks and 7.2 MW IT capacity; verify whether the site belongs to Almaty City vs Almaty Region/Alatau SEZ in the result schema.
- **Enegix / Ekibastuz** — official site lists 150+50 MW grid-powered campus. This is high-power crypto/HPC infrastructure; include, but mark mining/HPC if no enterprise colo/cloud evidence.
- **Makat Data Center / Atyrau Region** — power-provider evidence reported 40 MW mobile gas plant for a data center. Verify operator and whether it is mining before classifying as enterprise DC.
- **Digital Silk Route / Aktau SEZ** — older official/PM investment material mentions an Aktau data-center project tied to dedicated generation. Treat as planned/stale unless recent construction evidence exists.

### 3.3 Public cloud regions and hyperscaler signals

- **Yandex Cloud** — has an official Kazakhstan region and Karaganda/Freedom Telecom PoP. Count the underlying facility as Freedom Telecom Karaganda unless Yandex discloses a distinct owned DC.
- **AWS, Microsoft Azure, Google Cloud, Oracle Cloud** — check official region lists every run:
  - AWS: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
  - Azure: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/
  - Google Cloud: https://cloud.google.com/about/locations
  - Oracle Cloud: https://www.oracle.com/cloud/public-cloud-regions/
  As of 2026-08-12, these official lists do not show a public Kazakhstan region. Treat articles saying Amazon/Microsoft/Google are "interested" or "expected" as demand/prospect evidence, not facilities.

---

## 4. Region-by-region enumeration approach

For every division, run `{division/city}` in English plus Russian and Kazakh names. Use oblast capital names too, because directories list cities more often than oblasts.

| Division | Primary search anchors | Industry/vendor approach |
|---|---|---|
| Abai | Semey / `Семей`, Bakhty / `Бахты`, `Абай облысы` | Search Chinese-investor and border/logistics announcements: `Бахты дата-центр`, `Semey data center`, `Абай "центр обработки данных"`. Expect planned/MOU projects; verify with gov.kz akimat pages. |
| Akmola | Kokshetau / `Кокшетау`, Ereymentau / `Ерейментау`, Astana-adjacent industrial zones | Search Kazteleport Ereymentau and GK Hyperscale Akmola. Query `Ерейментау ЦОД`, `Акмолинская область дата-центр`, `Akmola hyperscale data center`. |
| Aktobe | Aktobe / `Актобе`, Kuraily / `Курайлы` | Start with Yandex/2GIS local entries, then verify `Freedom Data Centers Aktobe`, `Qazmin`, `AQ Group`. Watch for crypto farms. |
| Almaty Region | Alatau / `Алатау`, Konaev / `Қонаев`, Ili district / `Іле ауданы`, Kaskelen | Freedom Cloud Alatau, Beeline/Hyper Cloud if outside city boundary, technopark/SEZ pages. Query `Алатау технопарк дата-центр`, `Іле деректерді өңдеу орталығы`. |
| Atyrau | Atyrau / `Атырау`, Makat / `Мақат` | High-power/oilfield-adjacent projects. Query `Макат дата-центр`, `Makat data center`, `Атырау ЦОД МВт`; verify power plant vs IT load. |
| West Kazakhstan | Uralsk / `Уральск` / `Орал`, Bayterek district | Search NIT/Kazakhtelecom legacy facilities and TTC/hosting entries: `Уральск центр обработки данных`, `Орал деректер орталығы`. |
| Jambyl | Taraz / `Тараз`, Shu / `Шу` | Low expected yield. Search Kazakhtelecom regional IDC and gov procurement: `Тараз ЦОД`, `Жамбыл "центр обработки данных"`. |
| Jetisu | Taldykorgan / `Талдыкорган`, Tekeli | Low expected yield. Search local akimat + Kazakhtelecom: `Жетісу деректерді өңдеу орталығы`, `Талдыкорган ЦОД`. |
| Karaganda | Karaganda / `Караганда` / `Қарағанды`, Temirtau / `Темиртау` | Priority region: Freedom/Yandex Cloud Karaganda, GK Hyperscale Temirtau, Kazakhtelecom regional sites. Query `Freedom Cloud Karagandy`, `Yandex Cloud Kazakhstan Karaganda`, `Темиртау дата-центр`. |
| Kostanay | Kostanay / `Костанай` / `Қостанай`, Rudny | Mostly directory/procurement. Query `Костанай дата-центр`, `Қостанай деректерді өңдеу орталығы`, then validate weak 2GIS/Yandex entries. |
| Kyzylorda | Kyzylorda / `Кызылорда` / `Қызылорда` | Kazakhtelecom legacy IDC likely. Query `Кызылорда интернет дата центр Казахтелеком`, KASE/Kazakhtelecom releases. |
| Mangystau | Aktau / `Актау` / `Ақтау`, SEZ Seaport Aktau | Digital Silk Route/Aktau energy-linked project, Kazteleport Aktau. Query `Актау ЦОД`, `порт Актау дата-центр`, `Digital Silk Route Kazakhstan data center`. |
| Pavlodar | Pavlodar / `Павлодар`, Ekibastuz / `Экибастуз` | Highest priority: Data Center Valley, Enegix, Kazakhtelecom Pavlodar. Query `Экибастуз Data Center Valley`, `Экибастуз дата-центр 125 МВт`, `Enegix Ekibastuz`. |
| North Kazakhstan | Petropavl / `Петропавловск`, `Северо-Казахстанская область` | Low yield; search regional e-gov/telecom. `Петропавловск ЦОД`, `СКО центр обработки данных`. |
| Turkistan | Turkistan / `Туркестан`, Kentau | Search smart-city/e-government hosting and Kazakhtelecom regional site. `Туркестан дата-центр`, `Түркістан деректерді өңдеу орталығы`. |
| Ulytau | Zhezkazgan / `Жезказган`, Satbayev | Low yield; watch mining/industrial power. `Ұлытау дата орталығы`, `Жезказган ЦОД`, `Жезказган майнинг дата-центр`. |
| East Kazakhstan | Oskemen / `Усть-Каменогорск` / `Өскемен`, Ridder | Search TTC/Kazakhtelecom/directory leads. `Усть-Каменогорск дата-центр`, `Өскемен деректер орталығы`, `Transtelecom Ust-Kamenogorsk`. |
| Astana | Astana / `Астана`, `Нұр-Сұлтан`, Ereymentau spillover | Priority city: Akashi, Kazakhtelecom Astana, Kazteleport Ereymentau, government DC/NIT. Search RSP for object addresses and Uptime for certifications. |
| Almaty City | Almaty / `Алматы` | Priority city: Kazteleport Sairam/Masanchi/Khan Tengri, Kazakhtelecom modular DPC, PS/NAT/NLS, Beeline/Hyper Cloud, Freedom/Alatau boundary. Query by street/facility aliases. |
| Shymkent | Shymkent / `Шымкент` | Kazakhtelecom legacy IDC and smart-city/government hosting. `Шымкент интернет дата центр`, `Шымкент ЦОД Казахтелеком`. |

---

## 5. Trade press and association watchlist

- **Data Center Dynamics (DCD)** Kazakhstan tag: best English trade press for operator launches and MW claims.
- **Astana Times**, **Kursiv**, **The Times of Central Asia**, **Eurasianet**, **Telecom Review Asia**, **Developing Telecoms**, **Interfax**, **Profit.kz**: good for regional tech/infrastructure announcements. Grade B; verify numbers against operator/gov pages.
- **QazProjects**: useful project database for Kazakhstan investment projects; good seed source but still secondary. Grade B/C depending on whether it cites official decisions.
- **Astana Hub / AIFC / Invest Kazakhstan events**: watch KGIR, Digital Bridge, AI Forum, and AIFC infrastructure panels for new MoUs. Treat as lead-generation until backed by construction evidence.
- **Uptime Institute awards**: watch for new Kazakhstan entries; certification entries often reveal exact project names before broad press coverage.
- **Cloud/directories**: Data Center Map, Datacenters.com, Cloudscene, Baxtel, Colomap, Yandex Maps, 2GIS. Use them to find names/addresses, then corroborate.

---

## 6. Verification and grading rules

1. **Do not double count operator vs tenant.** Example: Yandex Cloud Kazakhstan may run on Freedom Telecom Karaganda infrastructure; record the physical DC once and Yandex as cloud tenant/region evidence unless a distinct Yandex-owned facility is proven.
2. **Separate enterprise DC from mining/HPC.** Enegix, AQ Group, Makat-style high-MW sites may be mining or energy-backed compute. Include them, but mark notes as mining/HPC unless colocation/cloud customers are documented.
3. **Treat `planned up to 1 GW` as master-plan capacity.** For Data Center Valley, count only named built/under-construction phases in project outputs. Keep the 1 GW figure in notes.
4. **Boundary check Almaty City vs Almaty Region.** Alatau/technopark projects may be near Almaty but outside the city schema division. Use operator address, SEZ/akimat page, or cadastral source when possible.
5. **Capacity hierarchy:** operator official IT MW/racks or Uptime certification (A) > listed issuer annual report (A) > government project page (A/B depending on stage) > DCD/Interfax/Kursiv (B) > directories/maps (C).
6. **Status hierarchy:** operational page/certification/commissioning report > construction-start release > procurement/grid/power contract > investment treaty/MOU > directory-only lead.
7. **Local-language aliases matter:** Astana also appears in old records as `Нур-Султан`; Oskemen as `Усть-Каменогорск`; Uralsk as `Орал`; Kyzylorda as `Кызылорда`; Karaganda as `Караганда/Қарағанды`.

Recommended output notes should preserve the source class: `operator official`, `government agreement`, `trade press`, `directory only`, `mining/HPC`, `tenant in third-party DC`, or `MOU only`.

