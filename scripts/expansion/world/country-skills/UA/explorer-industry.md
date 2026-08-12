# UA Explorer - Industry, Vendor, Cloud, Trade Press, and Oblast Query Patterns

Date: 2026-08-12. Scope: Ukraine datacenter enumeration methodology focused on Ukrainian colo/cloud providers, industry and trade-press sources, cloud-region signals, association/regulatory lists, and oblast-level query patterns. Reliability grades: **A** = official/primary source, operator-owned page, official registry, or cloud-provider region list; **B** = established trade press, association page, legal/market analysis, or strong directory with operator corroboration; **C** = aggregator/directory/market snippet that needs verification.

---

## 0. Ukraine-specific frame

- Ukraine does **not** have a single public national facility register for commercial data centers. Enumeration should use a combined path: **operator/vendor page -> IT Ukraine / NCEC / State Special Communications cloud-DC provider list -> Data Center Map/Inflect/Cloudscene seed -> trade press -> e-construction/EIA/local council records**.
- The market is **Kyiv-heavy**, with secondary known or likely clusters in **Odesa**, **Kharkiv**, **Dnipro/Dnipropetrovsk**, **Lviv**, **Rivne**, **Kremenchuk/Poltava**, and **Vinnytsia**. Many non-Kyiv entries are small colo/server-room facilities rather than wholesale data centers.
- War conditions matter. For front-line, occupied, or disputed divisions (**Donetsk, Luhansk, Kherson, Zaporizhzhia, Crimea, Sevastopol, parts of Kharkiv/Mykolaiv**) treat directory entries and pre-2022 pages as **status-uncertain** unless a current operator page, peering record, regulator filing, or 2024-2026 local source confirms operation.
- Ukrainian/Russian terms both matter because older Ukrainian provider pages and directories often use Russian. Search with: **дата-центр**, **дата центр**, **ЦОД**, **центр обробки даних**, **центр оброблення даних**, **центр обработки данных**, **колокація**, **колокейшн**, **розміщення серверів**, **оренда стійки**, **серверна**, **хмарні послуги**, **хмарний провайдер**, **резервне копіювання**, **ДГУ**, **дизель-генератор**, **електроживлення**, **підстанція**, **технічні умови**, **містобудівні умови та обмеження**, **дозвіл на будівельні роботи**, **введення в експлуатацію**, **ОВД / оцінка впливу на довкілля**.
- Cloud-region pages are **A for logical region existence or absence**, not facility address. As of this pass, AWS, Azure, Google Cloud, and OCI official region lists show **no Ukraine hyperscale cloud region**. Google lists Kyiv as a network edge/peering metro, which is an interconnection signal, not a cloud region.
- Ukraine introduced a formal public-sector framework for **cloud services and data-center services**. The State Service of Special Communications and Information Protection (SSSCIP) publishes a list of cloud/DC service providers; this is an **operator/provider evidence channel**, not necessarily a facility census.

---

## 1. Industry, association, and trade-press sources

### 1.1 Association and regulatory/provider lists

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| IT Ukraine Association | https://itukraine.org.ua/en/ ; `site:itukraine.org.ua/en "data center" Ukraine` | Best industry-association context. Member pages and articles identify operators such as Parkovyi and discuss Ukrainian DC/cloud market transformation. | B |
| IT Ukraine article on Ukrainian data centers | https://itukraine.org.ua/en/transformation-of-ukrainian-data-centers-path-to-the-european-cloud-market/ | Useful market framing: Ukrainian commercial DCs are mostly classic colocation/server-rental providers; named providers are good leads. Verify each facility with operator pages. | B |
| SSSCIP cloud/DC provider list | https://cip.gov.ua/ua/statics/cloud-dc-services | Official list of providers of cloud services and/or data-center services for regulated public-sector use. Use as a provider/operator seed and compliance signal. | A for provider-list status; B/C for physical facility inference |
| Cabinet of Ministers Resolution No. 154 / cloud and DC services | https://zakon.rada.gov.ua/go/154-2025-%D0%BF | Official rules for cloud services and/or data-center services linked to state information resources and restricted information. Helps explain why the SSSCIP list matters. | A |
| NCEC / National Commission for Electronic Communications | https://nkek.gov.ua/en and https://nkek.gov.ua/ | Telecom regulator. Use for electronic-communications provider context, spectrum decisions, and large telco moves such as Kyivstar. It is not a DC facility register. | A for telecom regulatory context |
| Ukrainian Internet Association (InAU) | https://inau.ua/ ; query `site:inau.ua "дата-центр" OR "ЦОД"` | ISP/IX/provider ecosystem, UA-IX context, telecom policy. Useful for member/provider pivots; verify facility claims elsewhere. | B |
| UA-IX | https://www.ua-ix.net/ ; query `UA-IX дата-центр`, `site:ua-ix.net Kyiv data center` | Interconnection signal for Kyiv facilities/operators. Good for active network presence, not a complete DC list. | B/C |
| PeeringDB | https://www.peeringdb.com/ | Search Ukrainian facilities, networks, and IXPs; confirms active interconnection participants where facility records exist. | B/C |

### 1.2 Trade press and market discovery

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) Ukraine tag | https://www.datacenterdynamics.com/en/news/?tag=ukraine | Best international DC trade feed. Use for Kyivstar AI DC plans, VEON/Kyivstar rebuild investment, AWS partnership/lab, war/resilience context. | B |
| W.Media | https://w.media/ ; `site:w.media Ukraine "data center"` | APAC/EMEA data-center trade coverage. Good for Kyivstar/VEON and regional AI/cloud investment leads. | B |
| Interfax-Ukraine | https://interfax.com.ua/ ; `site:interfax.com.ua data center Ukraine Energoatom Hotmine` | Strong Ukrainian business wire. Useful for older large project announcements such as Energoatom/Hotmine Zaporizhzhia. Verify current status. | B |
| Ukrinform | https://www.ukrinform.net/ ; `site:ukrinform.net Ukraine data center Energoatom` | Official/state news agency; useful for public-sector and state-company project announcements. | B |
| Liga.net / AIN.UA / dev.ua / MC.today / Forbes Ukraine | Queries: `site:ain.ua "дата-центр"`, `site:dev.ua "ЦОД"`, `site:forbes.ua "дата-центр"` | Ukrainian tech/business press. Good for provider profiles, cloud services, telecom investments, acquisitions, and wartime infrastructure changes. | B/C |
| CEE Legal Matters / Ukrainian law firms | Example: https://ceelegalmatters.com/ukraine/28910-new-regulation-of-cloud-and-data-center-services-in-ukraine | Regulatory context for the 2025 cloud/DC framework. Use to understand compliance and registry terms; cite official law for final evidence. | B |
| Schneider Electric / Vertiv / ITG / integrator case studies | Example: https://itg.com.ua/en/construction-and-commissioning-of-data-centers/ | Engineering/vendor ecosystem and possible project-delivery case studies. Usually lead discovery only unless the client/site is explicit. | C+/B- |

### 1.3 Directories and aggregators

| Source | URL | Use | Grade |
|---|---|---|---|
| Data Center Map Ukraine | https://www.datacentermap.com/ukraine/ and city pages such as https://www.datacentermap.com/ukraine/kiev/ | Main seed list for Kyiv, Kharkiv, Odesa, Dnipro, Rivne, Kremenchuk, Vinnytsia, etc. Coverage can be stale; verify with operator pages and current status. | C+ |
| Inflect Ukraine | https://inflect.com/datacenters/emea/ukraine | Broad facility/location seed list with addresses. Use for aliases and candidate addresses, not as final proof. | C+ |
| Datacenters.com Ukraine | https://www.datacenters.com/locations/ukraine | Commercial directory. Useful for provider/facility discovery where operator pages are hard to find. | C |
| Cloudscene Ukraine/Kyiv | https://cloudscene.com/market/data-centers-in-ukraine/kiev | Market and interconnection overview. Good for scale/context; verify records elsewhere. | C |
| Baxtel Ukraine | https://baxtel.com/data-center/ukraine | Currently weak/empty for Ukraine in this pass. Use only as negative/coverage check. | C- |

---

## 2. Core Ukrainian query patterns

### 2.1 National industry sweep

```text
Ukraine "data center" Kyiv Odesa Kharkiv Dnipro Lviv "colocation"
Ukraine "data centre" "Kyivstar" "GigaCenter" "De Novo" "Parkovyi"
"дата-центр" Україна Київ Одеса Харків Дніпро Львів колокація
"дата центр" Україна "розміщення серверів" "оренда стійки"
"ЦОД" Україна Київ "колокейшн" OR "колокація"
"центр обробки даних" Україна "хмарні послуги"
"центр обработки данных" Украина Киев Одесса Харьков Днепр
site:itukraine.org.ua/en "data center" Ukraine
site:datacenterdynamics.com/en/news/ Ukraine "data center"
site:w.media Ukraine "data center" Kyivstar VEON
site:interfax.com.ua Ukraine "data center" Energoatom Hotmine Kyivstar
site:ukrinform.net Ukraine "data center" "Zaporizhzhia" OR "Kyivstar"
```

### 2.2 Operator and facility verification

```text
"{operator}" "data center" Ukraine official
"{operator}" "дата-центр" Київ OR Україна
"{operator}" "ЦОД" "колокація" OR "колокейшн"
"{operator}" "Tier III" "Ukraine" OR "Україна"
"{operator}" "ISO 27001" "КСЗІ" "дата-центр"
"{facility name}" "адреса" "дата-центр"
"{facility name}" "ДГУ" OR "дизель-генератор" OR "UPS" OR "ДБЖ"
"{facility name}" "стійок" OR "rack" OR "rack spaces" OR "кВт" OR "МВт"
```

### 2.3 Construction, environmental, and local-government follow-up

```text
site:e-construction.gov.ua "дата-центр" "{city}"
site:e-construction.gov.ua "центр обробки даних" "{city}"
site:e-construction.gov.ua "ЦОД" "{city}"
site:data.gov.ua "Реєстр будівельної діяльності" "дата-центр"
site:eia.menr.gov.ua "дата-центр" OR "центр обробки даних"
site:eco.gov.ua "дата-центр" "ОВД"
site:{city-council-domain} "дата-центр" "містобудівні умови"
site:{city-council-domain} "центр обробки даних" "дозвіл на будівельні роботи"
site:{oblast-admin-domain} "дата-центр" OR "ЦОД" OR "хмарні послуги"
"{city}" "дата-центр" "містобудівні умови та обмеження"
"{city}" "дата-центр" "технічні умови" "електропостачання"
"{city}" "дата-центр" "підстанція" OR "ДГУ" OR "дизель-генератор"
```

### 2.4 Official/public-record surfaces

| Channel | URL / pattern | What it confirms | Grade |
|---|---|---|---|
| Unified State Electronic System in Construction (ЄДЕССБ) | https://e-construction.gov.ua/ and https://e-construction.gov.ua/reestri | Building activity register, construction map, declarative/permit documents, commissioning. Search by keyword/address once a lead is known. Martial-law restrictions may limit fields. | A |
| ЄДЕССБ open data | https://data.gov.ua/dataset/24c0ce1c-8cc5-4f4c-9847-d713043a6a8a | Monthly ZIP datasets for construction-register documents. Best bulk-search route for `дата-центр`, `ЦОД`, `центр обробки даних`, operator names, and addresses. | A |
| EIA register / EcoSystem | https://eia.menr.gov.ua/ and https://eco.gov.ua/registers/yediniy | Environmental impact assessment records; useful for large projects with generators/substations/cooling, though many small colo sites may not trigger EIA. | A |
| Local councils and oblast military administrations | `site:{rada/oda domain} "дата-центр"` | Urban-planning conditions, land allocations, local investment projects, public hearings, reconstruction plans. | A/B |
| Prozorro public procurement | https://prozorro.gov.ua/ | Government/server-room/cloud/DC service tenders; useful for state or municipal data centers and provider names. | A/B |
| State Special Communications provider list | https://cip.gov.ua/ua/statics/cloud-dc-services | Officially listed providers for cloud/DC services under the public-sector regime. Use as a provider seed and compliance signal. | A/B |
| NCEC | https://nkek.gov.ua/ | Telecom provider/regulatory context, large telco decisions, spectrum and network investment signals. | A |

---

## 3. Vendor/operator seed list by cluster

Operator pages are **A for current marketed service/facility claim**, **B for capacity/certification unless supported by certificate or spec sheet**, and **C for exact physical location if the address is only from a directory**.

### 3.1 Kyiv City and Kyiv Oblast

Kyiv is the first-pass cluster. Search both `Kyiv` and older spellings `Kiev`, plus Ukrainian `Київ` and Russian `Киев`. Distinguish **Kyiv City** from **Kyiv Oblast**; many directory pages say Kyiv/Kiev even when the physical address is suburban.

Primary operators and leads:

- **De Novo** - official: https://denovo.ua/en/data-center and https://denovo.ua/en/services/colocation/ . Operator says the data center was commissioned in 2010, second phase in 2017, with 360 rack-spaces. Grade A.
- **Parkovyi / DataPark** - official: https://datapark.ua/eng/about-us/ and IT Ukraine member page https://itukraine.org.ua/en/members/the-parkovyi-data-center/ . Parkovyi is a major Kyiv commercial DC with Uptime/Tier III and CIPS/KСЗІ claims. Grade A/B.
- **GigaCenter / GigaCloud** - official: https://gigacenter.ua/ and GigaCloud DC context https://gigacloud.ua/en/why-gigacloud/ . GigaCloud says its equipment is in five data centers, including Ukrainian and Polish facilities; use this to pivot to GigaCenter, BeMobile, Lviv/Poland locations. Grade A/B.
- **Kyivstar** - data-center services and Azure Stack/cyber certification context on Kyivstar pages; company page https://kyivstar.ua/about/kyivstar-today-eng . Trade press reported a 2026 AI data-center plan; verify site/MW only after Kyivstar or government publishes details. Grade A for current telco/operator, B for planned AI DC.
- **Datagroup** - official data center page https://www.datagroup.ua/en/b2b/data-centr and cloud page noting Datagroup Cloud is physically in Datagroup's own Kyiv data center: https://www.datagroup.ua/en/smb/hmarni-rishennia/cloud-servers-datagroup . Grade A/B.
- **Volia Data Center** - official: https://dc.volia.com/ and English business page https://volia.com/eng/business/data-center/ . Grade A.
- **Cosmonova / BeMobile** - official Cosmonova DC page https://cosmonova.net/en/dc and Ukrainian/Russian variants. Cosmonova states its Kyiv data center launched in 2013 at Hrinchenka/Грінченка 2/1; BeMobile is also a Kyiv colo lead from directories/operator pages. Grade A/B.
- **Lanet Business** - official: https://lanet.business/data-center/ . Kyiv data-center service/colo lead. Grade A/B.
- **Adamant, United DC, NewTelco Kyiv, SerinIX KV01, Kievline, UKRCOM, FreeHost/hosters** - use Data Center Map/Inflect/PeeringDB as seed lists, then operator domains and address searches for validation. Grade C until official corroboration.

Kyiv templates:

```text
"дата-центр" Київ De Novo Parkovyi GigaCenter Kyivstar Datagroup Volia Cosmonova
"дата центр" Київ "розміщення серверів" "колокація"
"ЦОД" Київ "стійок" OR "rack" OR "МВт" OR "кВт"
"центр обробки даних" Київ "хмарні послуги"
"Kyivstar" "AI data center" Ukraine OR "штучний інтелект" "дата-центр"
site:e-construction.gov.ua "дата-центр" "Київ"
site:e-construction.gov.ua "центр обробки даних" "Київ"
site:kyivcity.gov.ua "дата-центр" OR "центр обробки даних"
site:kyivcity.gov.ua "містобудівні умови" "дата-центр"
site:koda.gov.ua "дата-центр" OR "ЦОД"
site:data.gov.ua "Київ" "дата-центр" "Реєстр будівельної діяльності"
```

### 3.2 Odesa Oblast

Known/likely operators include **TENET**, **Data Center Arnautsky**, **HyperHost**, and telecom/hosting facilities around Odesa city.

- **Data Center Arnautsky** - official: https://dca.com.ua/ . Odesa address shown as Velyka Arnautska 2-A; services include colo, dedicated/virtual servers, hosting. Grade A.
- **TENET** - official business/DC pages should be searched by `TENET дата-центр Одеса`; Data Center Map has Odesa listing. Grade A if official service page confirms.
- **HyperHost** - official datacenter page https://hyperhost.ua/en/info/datacenter ; directory places an Odesa facility, but operator may use multiple/partner DCs. Grade B/C until exact location confirmed.

Odesa templates:

```text
"дата-центр" Одеса TENET "Арнаутський" HyperHost
"дата центр" Одеса "Велика Арнаутська" OR "Большая Арнаутская"
"ЦОД" Одеса "колокація" OR "колокейшн"
site:omr.gov.ua "дата-центр" OR "центр обробки даних"
site:omr.gov.ua "містобудівні умови" "дата-центр"
site:oda.od.gov.ua "дата-центр" OR "ЦОД"
site:e-construction.gov.ua "Одеса" "дата-центр"
```

### 3.3 Kharkiv Oblast

Directory seeds include **Ukrnames DC1/DC2**, **ITL**, **Infiumhost/InfiumDC**, and **Layer1**. Because of wartime risk and proximity to the front, current operation should be verified with current operator pages, peering records, or 2024-2026 posts.

Kharkiv templates:

```text
"дата-центр" Харків Ukrnames ITL Infiumhost Layer1
"ЦОД" Харків "колокейшн" OR "колокація"
"центр обработки данных" Харьков Ukrnames ITL Infiumhost
"Himnaziyna Embankment" Ukrnames "data center"
"Гімназійна набережна" Ukrnames "дата-центр"
site:city.kharkiv.ua "дата-центр" OR "ЦОД"
site:kharkivoda.gov.ua "дата-центр" OR "центр обробки даних"
site:e-construction.gov.ua "Харків" "дата-центр"
```

### 3.4 Dnipropetrovsk Oblast / Dnipro

Directory seeds include **Datasfera**, **SerinIX DK01**, and **Omega Telecom** in Dnipro/Dnipropetrovsk. Also search the Dnipropetrovsk Investment Agency and industrial/reconstruction material for ICT projects.

Dnipropetrovsk templates:

```text
"дата-центр" Дніпро Datasfera SerinIX "Omega Telecom"
"дата центр" Днепр "колокейшн" OR "ЦОД"
"центр обробки даних" "Дніпропетровська область"
site:dniprorada.gov.ua "дата-центр" OR "ЦОД"
site:adm.dp.gov.ua "дата-центр" OR "центр обробки даних"
site:dia.dp.gov.ua "data center" OR "дата-центр"
site:e-construction.gov.ua "Дніпро" "дата-центр"
```

### 3.5 Lviv Oblast

Lviv is a resilience/relocation and western-Ukraine cloud/colo target. Parkovyi/IT Ukraine mentions server-equipment placement in Kyiv and Lviv; GigaCloud materials mention Ukrainian and Polish data centers. Verify whether Lviv is owned, partner-operated, or only a service location.

Lviv templates:

```text
"дата-центр" Львів "колокація" OR "розміщення серверів"
"ЦОД" Львів "хмарні послуги" OR "серверна"
"Parkovyi" Lviv "data center" OR "Львів"
"GigaCloud" Львів "data center" OR "дата-центр"
site:city-adm.lviv.ua "дата-центр" OR "центр обробки даних"
site:loda.gov.ua "дата-центр" OR "ЦОД"
site:e-construction.gov.ua "Львів" "дата-центр"
```

### 3.6 Poltava Oblast / Kremenchuk

Known seed: **ColoCall** Kremenchuk/Poltava from Data Center Map plus operator colocation page https://www.colocall.net/en/services/colocation/ . Confirm address and current status with operator/local records.

Poltava templates:

```text
"дата-центр" Кременчук ColoCall
"дата-центр" Полтава "колокація" OR "ЦОД"
"ColoCall" Kremenchuk "data center" OR "colocation"
site:kremen.gov.ua "дата-центр" OR "ЦОД"
site:rada-poltava.gov.ua "дата-центр" OR "центр обробки даних"
site:poda.gov.ua "дата-центр" OR "ЦОД"
site:e-construction.gov.ua "Кременчук" "дата-центр"
```

### 3.7 Rivne Oblast

Known seeds: **Campus Networks** and **Datagroup Rivne** from directories/operator service pages. Treat as small colo/telecom facilities unless official specs say otherwise.

Rivne templates:

```text
"дата-центр" Рівне "Campus Networks" Datagroup
"ЦОД" Рівне "колокація" OR "сервер"
site:rivne-rada.gov.ua "дата-центр" OR "ЦОД"
site:rivneoda.gov.ua "дата-центр" OR "центр обробки даних"
site:e-construction.gov.ua "Рівне" "дата-центр"
```

### 3.8 Vinnytsia Oblast

Known seed: **IP-Connect DC-16 Vinnytsia** from Data Center Map. Needs operator/domain validation.

Vinnytsia templates:

```text
"дата-центр" Вінниця "IP-Connect" OR "DC-16"
"ЦОД" Вінниця "колокація" OR "розміщення серверів"
site:vmr.gov.ua "дата-центр" OR "центр обробки даних"
site:vin.gov.ua "дата-центр" OR "ЦОД"
site:e-construction.gov.ua "Вінниця" "дата-центр"
```

### 3.9 Zaporizhzhia Oblast

Major historical lead: **Energoatom / Hotmine / Yom Capital Zaporizhzhia data processing center** near Zaporizhzhia NPP, reported in 2020 by Ukrinform and Interfax-Ukraine with very large power figures. No recent completion evidence found in this pass; treat as **announced/stale** until Energoatom, local authority, e-construction, EIA, or current trade press confirms construction.

Zaporizhzhia templates:

```text
"Zaporizhzhia" "data center" Energoatom Hotmine Yom Capital
"Запоріжжя" "дата-центр" Енергоатом Hotmine
"Запорожье" "центр обработки данных" Энергоатом
"Запорізька АЕС" "центр обробки даних" OR "дата-центр"
site:energoatom.com.ua "дата-центр" OR "data center" OR Hotmine
site:zp.gov.ua "дата-центр" OR "ЦОД"
site:zoda.gov.ua "дата-центр" OR "центр обробки даних"
site:e-construction.gov.ua "Запоріжжя" "дата-центр"
site:eia.menr.gov.ua "Запоріжжя" "центр обробки даних"
```

### 3.10 Crimea and Sevastopol

Repo divisions include `Crimea` and `Sevastopol`. Treat as **disputed/occupied territory** and keep Ukraine country assignment per manifest, while recording the de facto operator/source context. Directory/operator seeds include **Miranda-Media** Simferopol and Sevastopol pages under Russian domains/directories. Use caution: current status may be real, but legal jurisdiction, sanctions, and source bias require explicit notes.

Crimea/Sevastopol templates:

```text
"дата-центр" Симферополь Miranda-Media
"ЦОД" Севастополь "Miranda-Media" OR "Миранда-Медиа"
"data center" Crimea Simferopol Sevastopol Miranda-Media
site:miranda-media.ru "дата-центр" "Симферополь" OR "Севастополь"
```

---

## 4. Oblast-by-oblast quick templates

Use this section for divisions without known confirmed projects. Always search English, Ukrainian, and older Russian spellings where applicable.

| Repo division | Local names / anchor cities | Copy-paste query templates |
|---|---|---|
| Vinnytsia | Вінниця / Vinnytsia | `"дата-центр" Вінниця`, `"ЦОД" Вінниця колокація`, `site:vin.gov.ua "центр обробки даних"`, `site:e-construction.gov.ua Вінниця "дата-центр"` |
| Volyn | Луцьк / Lutsk | `"дата-центр" Луцьк`, `"ЦОД" Волинь`, `site:lutskrada.gov.ua "дата-центр"`, `site:voladm.gov.ua "центр обробки даних"` |
| Luhansk | Луганськ / Luhansk | `"дата-центр" Луганськ`, `"ЦОД" Луганск`, `site:loga.gov.ua "дата-центр"`; mark status uncertain/occupied unless current evidence exists |
| Dnipropetrovsk | Дніпро / Dnipro, Кривий Ріг | `"дата-центр" Дніпро Datasfera SerinIX`, `"ЦОД" Кривий Ріг`, `site:adm.dp.gov.ua "дата-центр"` |
| Donetsk | Донецьк / Donetsk, Краматорськ | `"дата-центр" Донецьк`, `"ЦОД" Донецк`, `"data center" Donetsk colocation`; mark status uncertain/occupied where relevant |
| Zhytomyr | Житомир / Zhytomyr | `"дата-центр" Житомир`, `"ЦОД" Житомир`, `site:zt-rada.gov.ua "центр обробки даних"`, `site:oda.zht.gov.ua "дата-центр"` |
| Transcarpathia | Ужгород / Uzhhorod, Мукачево | `"дата-центр" Ужгород`, `"ЦОД" Закарпаття`, `"data center" Uzhhorod`, `site:carpathia.gov.ua "дата-центр"` |
| Zaporizhzhia | Запоріжжя / Zaporizhzhia | `"Запоріжжя" "дата-центр" Енергоатом`, `"Zaporizhzhia" "data center" Hotmine`, `site:zoda.gov.ua "центр обробки даних"` |
| Ivano-Frankivsk | Івано-Франківськ | `"дата-центр" Івано-Франківськ`, `"ЦОД" Івано-Франківськ`, `site:if.gov.ua "дата-центр"` |
| Kyiv City | Київ / Kyiv | `"дата-центр" Київ De Novo Parkovyi GigaCenter Kyivstar`, `site:kyivcity.gov.ua "дата-центр"`, `site:e-construction.gov.ua Київ "центр обробки даних"` |
| Kyiv | Київська область, Бровари, Бориспіль, Біла Церква | `"дата-центр" "Київська область"`, `"ЦОД" Бровари OR Бориспіль`, `site:koda.gov.ua "дата-центр"` |
| Kirovohrad | Кропивницький / Kropyvnytskyi | `"дата-центр" Кропивницький`, `"ЦОД" Кіровоград`, `site:kr-rada.gov.ua "центр обробки даних"`, `site:koda.gov.ua "дата-центр" -kyiv` |
| Sevastopol | Севастополь | `"дата-центр" Севастополь Miranda-Media`, `"ЦОД" Севастополь`; mark disputed/occupied |
| Crimea | Крим, Сімферополь | `"дата-центр" Сімферополь`, `"ЦОД" Крым`, `"data center" Crimea Simferopol`; mark disputed/occupied |
| Lviv | Львів | `"дата-центр" Львів колокація`, `"Parkovyi" Lviv "data center"`, `site:loda.gov.ua "дата-центр"` |
| Mykolaiv | Миколаїв / Mykolaiv | `"дата-центр" Миколаїв`, `"ЦОД" Николаев`, `site:mkrada.gov.ua "центр обробки даних"`, `site:mk.gov.ua "дата-центр"` |
| Odesa | Одеса / Odessa | `"дата-центр" Одеса TENET Арнаутський HyperHost`, `site:omr.gov.ua "дата-центр"`, `site:e-construction.gov.ua Одеса "дата-центр"` |
| Poltava | Полтава, Кременчук | `"дата-центр" Кременчук ColoCall`, `"ЦОД" Полтава`, `site:poda.gov.ua "дата-центр"` |
| Rivne | Рівне | `"дата-центр" Рівне Campus Networks Datagroup`, `"ЦОД" Рівне`, `site:rivneoda.gov.ua "центр обробки даних"` |
| Sumy | Суми / Sumy | `"дата-центр" Суми`, `"ЦОД" Сумы`, `site:smr.gov.ua "дата-центр"`, `site:sm.gov.ua "центр обробки даних"` |
| Ternopil | Тернопіль | `"дата-центр" Тернопіль`, `"ЦОД" Тернопіль`, `site:ternopilcity.gov.ua "дата-центр"` |
| Kharkiv | Харків / Kharkiv | `"дата-центр" Харків Ukrnames ITL Infiumhost Layer1`, `site:city.kharkiv.ua "ЦОД"`, `site:e-construction.gov.ua Харків "дата-центр"` |
| Kherson | Херсон / Kherson | `"дата-центр" Херсон`, `"ЦОД" Херсон`, `site:khersonoda.gov.ua "центр обробки даних"`; mark wartime/current-status uncertainty |
| Khmelnytskyi | Хмельницький | `"дата-центр" Хмельницький`, `"Khmelnytskyi Data center"`, `site:khm.gov.ua "дата-центр"`, `site:adm-km.gov.ua "центр обробки даних"` |
| Cherkasy | Черкаси | `"дата-центр" Черкаси`, `"ЦОД" Черкаси`, `site:chmr.gov.ua "дата-центр"`, `site:ck-oda.gov.ua "центр обробки даних"` |
| Chernihiv | Чернігів | `"дата-центр" Чернігів`, `"ЦОД" Чернигов`, `site:chernigiv-rada.gov.ua "дата-центр"`, `site:cg.gov.ua "центр обробки даних"` |
| Chernivtsi | Чернівці | `"дата-центр" Чернівці`, `"ЦОД" Черновцы`, `site:city.cv.ua "дата-центр"`, `site:bukoda.gov.ua "центр обробки даних"` |

---

## 5. Cloud-region and edge-provider checks

| Provider | Official source | Ukraine signal | How to use |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Ukraine region on official AWS region list in this pass. DCD reports Kyivstar has partnered with AWS on a generative AI lab, but that is not a Ukrainian AWS region. | A for absence/presence of AWS region; B for partnership leads |
| Microsoft Azure | https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies and Microsoft Learn regions list | No Ukraine Azure region on official region list in this pass. Kyivstar references Azure Stack/cloud services; treat as local/private/partner cloud unless Azure region docs show otherwise. | A for Azure region status |
| Google Cloud | https://cloud.google.com/about/locations and edge locations https://docs.cloud.google.com/vpc/docs/edge-locations | No Ukraine cloud compute region in this pass. Google lists **Kyiv, Ukraine** as a network edge location/metro for connectivity. | A for edge/region distinction |
| Oracle Cloud Infrastructure | https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm | No Ukraine OCI region in this pass. | A |
| Ukrainian clouds | De Novo, GigaCloud, Datagroup, Kyivstar, Volia, Parkovyi, Cosmonova, United DC, etc. | Local cloud/colo services hosted in Ukrainian and European data centers. | Use operator pages and SSSCIP list first; directories second. |

Cloud query templates:

```text
"AWS" Ukraine "region" "Availability Zone" "Kyivstar"
"Azure" Ukraine "region" "data center" "Kyivstar" OR "Azure Stack"
"Google Cloud" Kyiv Ukraine "edge locations" "Cloud Interconnect"
"Oracle Cloud" Ukraine "region"
site:cip.gov.ua "хмарних послуг" "центру обробки даних" "{provider}"
site:zakon.rada.gov.ua "хмарних послуг" "центру обробки даних"
```

---

## 6. Enumeration workflow

1. **Start with Kyiv operator pages.** Build the initial facility table from De Novo, Parkovyi/DataPark, GigaCenter/GigaCloud, Kyivstar, Datagroup, Volia, Cosmonova/BeMobile, Lanet, Adamant/United DC/NewTelco/SerinIX/Kievline/UKRCOM leads.
2. **Cross-check provider legitimacy.** Search the SSSCIP provider list, NCEC/provider context, IT Ukraine member pages, PeeringDB, UA-IX, and operator certificates such as Uptime, ISO 27001, PCI DSS, and KСЗІ where published.
3. **Use directories only as seeds.** Data Center Map/Inflect/Cloudscene can expose city/operator/address aliases, but every record should be upgraded with an official operator page, current peering record, local-government/construction record, or 2024-2026 press evidence.
4. **Run oblast templates for non-Kyiv divisions.** Prioritize Odesa, Kharkiv, Dnipro, Lviv, Rivne, Poltava/Kremenchuk, Vinnytsia, and Zaporizhzhia before lower-density oblasts.
5. **For large/new projects, verify public records.** Search ЄДЕССБ web + data.gov.ua ZIPs, EIA registers, local council/oblast administration pages, Prozorro tenders, and power/substation terms.
6. **Classify wartime and occupied-territory records explicitly.** Do not mark Donetsk/Luhansk/Crimea/Sevastopol/Kherson/Zaporizhzhia facilities operational from a stale directory alone.

## 7. Evidence grading rules for Ukraine

- **Grade A**: operator-owned facility/service page with current claim; SSSCIP provider list; official law/regulator page; ЄДЕССБ construction record; EIA record; Prozorro tender/award; official cloud region/edge-location docs.
- **Grade B**: DCD/W.Media/Interfax/Ukrinform/IT Ukraine article; credible legal analysis of cloud/DC regulation; PeeringDB/UA-IX active interconnection evidence; operator blog with indirect facility context.
- **Grade C**: Data Center Map, Inflect, Datacenters.com, Cloudscene, Baxtel, marketplace listings, old forum/blog posts, or third-party address/spec pages without operator corroboration.
- **Status discipline**: `operational` needs current operator/peering/regulator/local evidence; `planned/announced` is appropriate for Kyivstar AI DC or Energoatom/Hotmine Zaporizhzhia until construction evidence appears; `unknown` is appropriate for old/occupied-territory directory entries.
