# RU Explorer Official - Russia Datacenter Enumeration via Planning, Grid, Cloud, Colo, and Regulators

Date: 2026-08-12. Scope: Russian Federation (RU), 85 repo divisions: republics, krais, oblasts, autonomous okrugs/oblast, and federal cities. Angle: **official/regulatory/cloud pipeline**. Reliability grades: **A** = official/primary source, **B** = strong secondary/trade/association source, **C** = weak/aggregate/unverified.

---

## 0. Russia-specific structural facts

- Russia has no mature, complete, public building-permit search for all datacenters. Enumeration must join **regional GISOGD / construction-permit registers**, **EGRZ project-expertise records**, **Rosseti/grid connection signals**, **MinTsifry/Roskomnadzor regulatory registers**, **official cloud-zone pages**, **operator facility pages**, and Russian trade press.
- Use Russian terms first. `ЦОД`, `центр обработки данных`, `дата-центр`, `data center`, `datacenter`, `машинный зал`, `серверная`, `объект ИТ-инфраструктуры`, `облачная платформа`, `модульный ЦОД`, `майнинг`, and `вычислительный центр` return different slices. Avoid counting mining farms as normal datacenters unless the project is explicitly being converted to cloud/AI/colocation.
- Construction evidence is fragmented by region and municipality. The strongest sequence is usually: investment memorandum / land allocation -> **ГПЗУ** -> **проектная документация / экспертиза** -> **разрешение на строительство** -> **разрешение на ввод в эксплуатацию** -> operator launch.
- Power is often the gating constraint. Keep `технологическое присоединение`, `технические условия`, `питающий центр`, `подстанция`, `ПС`, `МВА`, `кВ`, `лимит мощности`, and `договор энергоснабжения` as first-class discovery terms. Rosseti and regional grid companies are Grade A for process and some project-specific signals, but connection applications are not always public.
- A new **MinTsifry register of datacenters** is the emerging regulatory backbone. The ministry page says the July 2025 law provides for a register of datacenters located in Russia. Use it as Grade A when records become searchable; until then, use MinTsifry pages and named official/trade confirmations as leads.
- Roskomnadzor's personal-data operator register is not a facility list, but it can validate legal entities and sometimes data-localization representations. Do not infer facility location from personal-data compliance alone.
- Cloud-region pages are metro/region seeds. Russian providers usually disclose availability zones but not exact buildings. Western hyperscalers do not publish Russia regions; AWS and Microsoft official pages confirm no Russian cloud region and suspended new Russia sales/signups in 2022.

Lifecycle terms:

```text
инвестиционный проект
резидент ОЭЗ / ТОР / индустриального парка
земельный участок / аренда / выкуп
ГПЗУ / градостроительный план земельного участка
проект планировки территории / ППТ
проект межевания территории / ПМТ
проектная документация
положительное заключение экспертизы
разрешение на строительство
разрешение на ввод объекта в эксплуатацию
технологическое присоединение
пусконаладочные работы
введен в промышленную эксплуатацию
запуск / открыт / расширение
```

Only treat `разрешение на строительство`, `положительное заключение экспертизы` plus site identity, `разрешение на ввод`, or operator launch as strong build evidence. Treat investment-portal and governor announcements as planned until matched to permit/grid/operator records.

---

## 1. Official and regulatory sources

### 1.1 Planning, permits, cadastral, and project-expertise records

- **GIS EGRZ / ЕГРЗ**: https://egrz.ru/ and Glavgosexpertiza description https://gge.ru/services/egrz/. The Unified State Register of Expert Conclusions contains conclusions on project documentation and engineering survey results for capital-construction projects. Search by exact Russian terms, operator/SPV, region, and address. **Grade A** for existence of project expertise, object title, applicant/developer, and expert conclusion status; public detail can be limited.
- **Regional GISOGD / ИСОГД portals**: each subject maintains urban-planning information systems under local ministries/departments of construction. There is not one consistent public interface. Search `ГИСОГД {region}`, `ИСОГД {region}`, `реестр разрешений на строительство {region}`, `разрешения на ввод {region}`, and the local construction authority. **Grade A** when the record or downloadable register is official.
- **Moscow construction-supervision permits**: Mosgosstroynadzor publishes issued construction permits by year at https://www.mos.ru/stroinadzor/razresheniia-na-stroitelstvo/. **Grade A** for Moscow City permit existence and date; search downloaded yearly files for `ЦОД`, `центр обработки данных`, operator names, and addresses.
- **Moscow Oblast issued permits**: regional pages such as https://minzhil.mosreg.ru/dokumenty/gosudarstvennye-uslugi/vydannye-razresheniya/vydannye-razreseniya-na-stroitelstvo publish issued construction-permit files. Also use Mosreg construction-supervision registers such as https://gusn.mosreg.ru/. **Grade A** for Moscow Oblast when hosted by official `mosreg.ru`.
- **Rosreestr / cadastral data**: https://rosreestr.gov.ru/ and official public cadastral-map references help verify parcels, building areas, ownership hints, and addresses after a lead is known. **Grade A** for cadastral facts; it does not identify datacenter use reliably.
- **Zakupki.gov.ru / EIS procurement**: https://zakupki.gov.ru/ is the official procurement system for 44-FZ/223-FZ. It is high-yield for government/regional datacenters, modernization, engineering design, UPS/generator/cooling tenders, and contracts naming addresses. **Grade A** for tender/contract existence; `поставка серверного оборудования` alone is not a facility.
- **GIS Torgi and investment maps**: https://torgi.gov.ru/ for public land/property auctions; https://invest.gov.ru/ and regional investment portals for industrial sites and investment projects. **Grade A** for official land/investment records, but treat as planned until permits/grid evidence appears.

Planning query templates:

```text
site:egrz.ru ("ЦОД" OR "центр обработки данных" OR "дата-центр")
site:egrz.ru "{operator}" "{region}"
"{region}" "ГИСОГД" ("ЦОД" OR "центр обработки данных")
"{region}" "реестр разрешений на строительство" "ЦОД"
"{municipality}" "разрешение на строительство" ("ЦОД" OR "центр обработки данных" OR "дата-центр")
"{operator}" "{city}" "разрешение на строительство"
"{SPV}" "положительное заключение экспертизы"
"{address}" "центр обработки данных" "разрешение на ввод"
site:zakupki.gov.ru ("ЦОД" OR "центр обработки данных") "{region}"
site:torgi.gov.ru ("ЦОД" OR "дата-центр" OR "центр обработки данных")
```

Practical fields to extract: object title, applicant/developer/SPV, address/cadastral number, land plot size, building area, number of machine halls/racks, design/IT/grid MW, expert conclusion number, permit number/date, commissioning permit, and relation to industrial park/OEZ/TOR.

### 1.2 Grid and energy evidence

- **Rosseti / Россети**: main site https://www.rosseti.ru/ and regional subsidiaries. Rosseti announced an updated electric-grid services portal at https://www.rosseti.ru/press-center/news/rosseti-zapustili-obnovlennyy-portal-elektrosetevykh-uslug/. The unified TP route is commonly referenced as `Портал-ТП.рф`; regional examples include Rosseti Volga linking to `https://портал-тп.рф/platform/portal/tehprisEE_connection`. **Grade A** for process, tariffs, and some connection notices.
- **Regional Rosseti companies**: use the holding geography and local subsidiaries: Rosseti Moscow Region, Lenenergo, Center, Center and Volga Region, Volga, Ural, Siberia, Kuban, Northern Caucasus, North-West, Tomsk, Tyumen, etc. Their procurement plans, grid-development programs, and TP pages can mention named datacenters, substations, and feeder centers. **Grade A** when hosted by the grid operator.
- **Federal Grid / high-voltage clues**: large campuses may require 110/220/500 kV substations or transmission-level connection. Search Rosseti annual reports and subsidiary procurement files for `ЦОД`, `дата-центр`, `технологическое присоединение`, `ПС`, `МВА`, and exact SPV names.
- **Regional tariff/energy committees**: sometimes publish individual TP fee decisions for high-load consumers. Search `индивидуальная плата за технологическое присоединение ЦОД {region}` and `решение РЭК ЦОД`.

Grid query templates:

```text
site:rosseti.ru ("ЦОД" OR "дата-центр" OR "центр обработки данных") ("технологическое присоединение" OR "подстанция" OR "МВА")
site:rosseti.ru "{operator}" "{region}" ("ПС" OR "МВА" OR "кВ")
site:{rosseti-subsidiary-domain} ("ЦОД" OR "дата-центр") "технологическое присоединение"
"{project}" "технологическое присоединение" "МВт"
"{project}" "технические условия" "подключение" "питающий центр"
"{city}" "ЦОД" ("подстанция" OR "ПС" OR "110 кВ" OR "220 кВ" OR "500 кВ")
"{operator}" "ЦОД" "получила технические условия"
"{region}" "индивидуальная плата" "технологическое присоединение" "ЦОД"
```

Energy caution: keep separate fields for `IT load`, `total supplied power`, `contracted/grid connection capacity`, `transformer/substation MVA`, `diesel generator capacity`, and `long-term campus plan`. Russian articles often use `мощность` ambiguously.

### 1.3 MinTsifry, Roskomnadzor, and digital-policy registers

- **MinTsifry DC register**: https://digital.gov.ru/activity/gos-uslugi/reestr-czentrov-obrabotki-dannyh-czod. The ministry page states the July 2025 law provides for a register of datacenters located in Russia. Use this as the future Grade A facility register; watch for downloadable/searchable records and annual confirmation requirements.
- **Gosuslugi IT accreditation register**: https://www.gosuslugi.ru/itorgs. Search by INN or company name for datacenter operators, cloud providers, and SPVs. **Grade A** for accredited legal-entity status, not facility existence.
- **Roskomnadzor personal-data operator register**: https://pd.rkn.gov.ru/operators-registry/operators-list/. Search by INN/name for operators. **Grade A** for personal-data operator registration; not a physical datacenter list.
- **Roskomnadzor localization context**: RKN materials and Federal Law 152-FZ / 242-FZ create demand for in-country storage. Use as regulatory context and as a legal-entity pivot. Do not count a facility only because an operator says it complies with 152-FZ.
- **FSTEC/FSB certification references**: official or operator pages may mention 152-FZ, FSTEC order 21, FSB crypto licensing, PCI DSS, Uptime Tier. These validate suitability for regulated workloads, not location by themselves.

Regulator query templates:

```text
site:digital.gov.ru "реестр центров обработки данных"
site:digital.gov.ru ("ЦОД" OR "дата-центр") "{operator}"
site:gosuslugi.ru/itorgs "{operator}" OR "{INN}"
site:pd.rkn.gov.ru/operators-registry "{operator}" OR "{INN}"
"{operator}" "152-ФЗ" "ЦОД" "{city}"
"{operator}" "ФСТЭК" "ЦОД" "{city}"
```

---

## 2. Official cloud-region and availability-zone seeds

Cloud providers usually confirm region/AZ names but not physical sites. Create cloud seed records and then pivot to operator campuses, EGRZ/GISOGD, Rosseti, and procurement evidence.

| Provider | Official source | Russia signal | Reliability / use |
|---|---|---|---|
| Yandex Cloud | Regions: https://yandex.cloud/en/docs/overview/concepts/region; AZs: https://yandex.cloud/en/docs/overview/concepts/geo-scope | Russia region with `ru-central1-a`, `ru-central1-b`, `ru-central1-d`, `ru-central1-e`, and `ru-central1-m` for BareMetal | A for region/AZ existence; C for exact building. Search Yandex, Yandex Cloud, `ru-central1`, Vladimir/Ryazan/Moscow-area leads only when independently sourced. |
| VK Cloud | Glossary: https://mcs.mail.ru/docs/ru/additionals/start/start-intro/help-glossary; docs/search for Moscow region/AZs | VK docs define availability zone as one or more datacenters; docs expose Moscow-region usage and zone labels such as GZ1 / ME1 in product docs and announcements | A for provider/AZ concept; B for facility mapping unless an official VK/Rostelecom page names the DC. |
| Cloud.ru / former SberCloud | AZ docs: https://cloud.ru/docs/advanced/overview/az-and-endpoints; release notes: https://cloud.ru/docs/advanced/overview/release-notes | Advanced platform has resource AZs including AZ1/AZ2/AZ3 and later AZ5 in docs/release notes | A for cloud-zone existence; C for exact building. Pivot to Sberbank/SberCloud/Cloud.ru/SPV, Skolkovo/Balakovo/Domodedovo leads. |
| Selectel Cloud | Datacenters: https://selectel.ru/about/data-centers/; locations/docs: https://docs.selectel.ru/en/infrastructure/locations/ | Official pages list Moscow, Saint Petersburg, Leningrad Oblast, and partner Novosibirsk infrastructure | A for operator facility list; verify new builds through permits/grid. |
| Rostelecom / RTK-DC cloud | Example public cloud page: https://msk.rt.ru/b2b/public-cloud; corporate news: https://www.company.rt.ru/press/news/ | Geo-distributed Tier III network, own sites in Moscow, Saint Petersburg, Yekaterinburg, Novosibirsk, Vladivostok and others | A when facility launch is on `company.rt.ru`/`rt.ru`; regional service pages alone can be generic. |
| AWS | Regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html; AWS Russia/Belarus update: https://www.aboutamazon.com/news/aws/updates-to-amazons-retail-entertainment-and-aws-businesses-in-russia-and-belarus | No AWS Russia region; AWS said it would not accept new Russia/Belarus-based AWS signups in 2022 | A for absence of Russia region / commercial status; do not seed physical RU sites. |
| Microsoft Azure | Regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list; Russia sales suspension: https://blogs.microsoft.com/on-the-issues/2022/03/04/microsoft-suspends-russia-sales-ukraine-conflict/ | No public Azure Russia region; Microsoft suspended new sales of products/services in Russia in 2022 | A for absence of Russia public region / commercial status; do not seed physical RU sites. |
| Google Cloud / OCI | Official global location pages | No Russian public cloud region in official global tables | A for absence of official RU region; use only if an official partner/on-ramp source names Russian infrastructure. |

Cloud query templates:

```text
"Yandex Cloud" "ru-central1" "дата-центр"
"Яндекс" "зона доступности" "ЦОД"
"VK Cloud" "зона доступности" "Москва" "ЦОД"
"VK Cloud" "ME1" "Медведково"
"Cloud.ru" "зона доступности" "ЦОД"
"SberCloud" "ЦОД" "зона доступности"
"AWS" "Russia" "Region" "data centers"
"Microsoft Azure" "Russia" "region"
```

---

## 3. Official colo/operator seed list

Use operator pages as first-pass seeds, then validate expansions with permits, EGRZ, grid, and regional investment sources.

| Operator | Official URL(s) | Facility/geography seed | Reliability |
|---|---|---|---|
| Rostelecom / RTK-DC / DataLine | https://www.company.rt.ru/press/news/ and regional service pages such as https://msk.rt.ru/b2b/public-cloud | Moscow/DataLine/NORD campuses, Saint Petersburg, Novosibirsk, Vladivostok, Yekaterinburg, Nizhny Novgorod, Sakhalin, Murmansk, Stavropol and regional launches | A for official launch pages; B/C for generic regional service pages without a facility address. |
| DataPro | https://datapro.ru/ and official PDFs such as https://datapro.ru/public/documents/pdf1.pdf / https://datapro.ru/public/documents/pdf3.pdf | Moscow/Tver and Moscow-region campuses; official PDFs give addresses such as Aviamotornaya 69 and Ryabinovaya 53 str. 3 plus rack/power design details | A for official PDF facts; verify status/current capacity. |
| Selectel | https://selectel.ru/about/data-centers/ | Moscow, Saint Petersburg, Leningrad Oblast, partner Novosibirsk; official page says 6 own DCs plus partner site | A for official list/capacity; use press page for new Moscow 20 MW build and grid-TU clues. |
| IXcellerate | https://www.ixcellerate.com/data-centers/; North campus https://www.ixcellerate.com/data-centers/moscow-north-campus/; South/Veshki pages | Moscow North, Moscow South, Veshki; official pages disclose MOS facility capacities, rack counts, addresses/contact pages, and future campus plans | A for official facility/campus pages; distinguish commissioned phase from full campus plan. |
| Yandex | Yandex Cloud docs and Yandex corporate/news pages | Moscow/Central Russia AZs, Yandex-owned/leased campuses, possible large AI/cloud expansions | A only when official; often requires trade/permit corroboration for exact sites. |
| VK / VK Tech | VK Cloud docs/news | Moscow cloud availability zones, partner/operator datacenters | A/B depending on whether VK or partner names the site. |
| Sber / Cloud.ru | Cloud.ru docs/news, Sberbank official releases | Skolkovo/Balakovo/Domodedovo and cloud-zone infrastructure leads | A for official Sber/Cloud.ru pages; B for press-cited capacity until primary permit/operator source found. |
| Key Point, 3data, Linx/Xelent, M1/Stack, Goznak, MegaFon, Beeline/VimpelCom, MTS, MTS Web Services, GreenMDC/DataDome | official operator pages/news | Important regional and edge coverage outside Moscow/Saint Petersburg | Prefer official operator pages; use CNews/IKS/ServerNews/DCD as B discovery. |

Operator query templates:

```text
"{operator}" "ЦОД" "{city}" "мощность"
"{operator}" "дата-центр" "{region}" "стойк"
"{operator}" "{facility code}" ("разрешение на строительство" OR "технологическое присоединение")
"{operator}" "{city}" ("введен в эксплуатацию" OR "запустил" OR "открыл")
site:company.rt.ru ("ЦОД" OR "дата-центр") "{city}"
site:selectel.ru ("ЦОД" OR "data center") "20 МВт"
site:ixcellerate.com "{campus}" "MW"
site:datapro.ru "ул." "ЦОД" "стой"
```

---

## 4. Per-division enumeration workflow

Apply the same sweep to all 85 divisions, then prioritize metros and energy-rich industrial regions.

1. **National seed pass**: MinTsifry DC register page, operator official pages, Yandex/VK/Cloud.ru/Selectel/Rostelecom cloud pages, EGRZ, Rosseti search, Zakupki.gov.ru, and existing repo RU result leads.
2. **Regional official pass**: for each subject, search the regional construction ministry, GISOGD/ISOGD, investment portal, OEZ/TOR/industrial park resident lists, governor press releases, and regional Rosseti subsidiary.
3. **Municipality pass**: for candidate cities/industrial parks, search city administration, council/decree pages, land-use documents, public hearings, and local permit registers.
4. **Grid validation**: search Rosseti/subsidiary/procurement/tariff committee for the project/operator plus `технологическое присоединение`, `ПС`, `МВА`, and `кВ`.
5. **Legal-entity pivot**: search INN/name in Gosuslugi IT register, Roskomnadzor PD registry, EGRZ, procurement, and business registries. Use exact SPV names from permits and investment agreements.
6. **Status reconciliation**: if a site is only in an investment portal or press quote, mark `planned/announced`; upgrade only with EGRZ/permit/grid/operator commissioning evidence.

### 4.1 Priority geography

- **Moscow City and Moscow Oblast**: highest density. Search Mosgosstroynadzor permit files, Mosreg issued permits, EGRZ, Rosseti Moscow Region, Moscow energy/substation terms, and operator pages for IXcellerate, DataPro, Rostelecom/DataLine, Selectel, 3data, M1/Stack, Yandex, VK, Sber/Cloud.ru.
- **Saint Petersburg and Leningrad Oblast**: Selectel, Rostelecom, Linx/Xelent, telecom/operator edge sites. Search `gov.spb.ru`, `lenobl.ru`, Lenenergo/Rosseti North-West, `ТЭК`, `ЦОД`, `Торфяная`, `Цветочная`, `Дубровка`.
- **Tver / Udomlya**: Rosatom/Rostelecom/Atomdata nuclear-adjacent campus and possible power-rich expansions. Search Rosatom, Rosenergoatom, Atomdata, Kalinin NPP, EGRZ, Rosseti Center.
- **Saratov / Balakovo**: Sberbank megacenter lead. Search Sber/SberCloud/Cloud.ru, Balakovo permits, Saratov investment portal, Rosseti Volga, `Шоссе Металлургов`.
- **Sverdlovsk / Yekaterinburg and Urals**: Key Point, MegaFon, industrial parks, strong grid/HPC demand. Search CRAFT industrial park, Rosseti Ural, regional investment portal.
- **Novosibirsk / Siberia**: Rostelecom, Key Point, Selectel partner, academic/HPC cluster. Search Novosibirsk permits, Rosseti Siberia, regional ministry, `Академгородок`.
- **Nizhny Novgorod, Samara, Tatarstan, Perm, Chelyabinsk, Krasnodar/Rostov**: regional telco/cloud and industrial demand. Use city permits, regional IT ministries, Rosseti subsidiaries, and operator official pages.
- **Far East / Arctic**: Vladivostok, Khabarovsk, Sakhalin, Murmansk, Buryatia, Yakutia. Search TOR/ASEZ resident lists, Far East investment map, Rosseti East, local grid shortage terms, and distinguish cloud/AI datacenters from mining.
- **Low-density republics/autonomous regions**: search official regional government IT/ministry pages and Zakupki for government datacenter modernization; expect small government/telecom server-room evidence rather than commercial colo campuses.

### 4.2 Division query bundle

For every division `{region}` and its capital/largest cities `{city}`:

```text
"{region}" ("ЦОД" OR "центр обработки данных" OR "дата-центр")
"{region}" "ГИСОГД" ("ЦОД" OR "дата-центр")
"{region}" "реестр разрешений на строительство" "центр обработки данных"
"{city}" "ЦОД" "разрешение на строительство"
"{city}" "ЦОД" "технологическое присоединение"
"{city}" "ЦОД" "подстанция"
"{region}" "инвестиционный проект" "дата-центр"
"{region}" ("ОЭЗ" OR "ТОР" OR "индустриальный парк") "ЦОД"
site:zakupki.gov.ru "{region}" ("ЦОД" OR "центр обработки данных")
site:{regional-government-domain} ("ЦОД" OR "центр обработки данных")
```

English backup:

```text
"{region}" Russia "data center" "MW"
"{city}" Russia "data center" "Rostelecom"
"{city}" Russia "data center" "Selectel" OR "IXcellerate" OR "DataPro"
"Russia" "data center" "grid connection" "{region}"
```

---

## 5. Reliability, status, and extraction rules

### 5.1 Evidence hierarchy

| Source | Grade | Use |
|---|---:|---|
| MinTsifry DC register once searchable | A | Facility/operator registration, regulated DC status, annual confirmation. |
| EGRZ / Glavgosexpertiza records | A | Project-expertise existence, object title, developer/applicant, design documentation status. |
| Regional GISOGD / official permit registers | A | Construction permit, commissioning permit, address, dates, sometimes area. |
| Moscow/Mosreg construction-supervision permit files | A | High-value permit sweep for densest market. |
| Rosseti/regional grid company/tariff decisions | A | Grid process, TP, substation/MVA/kV, sometimes capacity constraints. |
| Zakupki.gov.ru official procurement | A | Government DC creation/modernization, equipment, design/build contracts. |
| Roskomnadzor PD registry / Gosuslugi IT accreditation | A for legal entity | Entity/regulatory validation; not physical facility evidence. |
| Official cloud-region/AZ pages | A for cloud region/AZ | Confirms provider infrastructure region; not exact facility. |
| Official colo/operator facility pages | A- | Facility/campus existence and marketed capacity; confirm expansion status where possible. |
| CNews, IKS Media, ServerNews, TelecomDaily, DCD, ComNews, RBC/TASS/Interfax | B | Strong discovery/status leads; verify with primary records. |
| DatacenterMap, Baxtel, Ocolo, TAdviser, Wikipedia, reseller pages | C | Lead generation and cross-check only unless they link primary records. |

### 5.2 Status model

- `rumor/lead`: only aggregate directory, social post, or unsourced market mention.
- `announced`: official/trade announcement without land, permit, EGRZ, or grid evidence.
- `site selection`: investment agreement, land auction/allocation, OEZ/TOR resident status, or industrial-park record.
- `under review`: EGRZ/expertise/permit/grid process visible but no final approval.
- `permitted`: construction permit, positive expertise plus clear project identity, or official permission record.
- `under construction`: permitted plus construction announcement, tender for works, or official progress update.
- `commissioning`: `разрешение на ввод`, acceptance, PNR, customer migration, or official launch pending.
- `operational`: operator page, official launch, certification, customer availability, or inspection/procurement evidence of operating facility.
- `expansion`: new building/module/power phase at an existing campus.
- `mining-only`: crypto/mining facility; exclude from commercial DC totals unless explicitly cloud/AI/colocation.

### 5.3 Capacity fields to keep separate

- `rack_count`: `стойко-мест`, `стойки`, `шкафы`.
- `server_room_m2`: `площадь машинных залов`, `полезная площадь`.
- `building_m2`: total building/campus area.
- `it_mw`: only explicit `IT-мощность`, `полезная ИТ-нагрузка`, or equivalent.
- `supplied_power_mw`: `подведенная мощность`, `общая мощность объекта`; not necessarily IT load.
- `grid_mw_or_mva`: TP, substation, feeder-center, transformer, or connection capacity.
- `generator_mw`: diesel/gas-piston backup or autonomous power plant capacity.
- `campus_plan_mw`: long-term planned campus number; record separately from commissioned MW.

### 5.4 Red flags

- Regional Rostelecom pages may advertise data-center services to local customers without a physical facility in that region. Count only if an address, launch, technical center, or local official source confirms the facility.
- `ЦОД` in government procurement can mean a software/data-processing system, a server room, or traffic-control center. Count as datacenter only when facility-grade infrastructure is described.
- Mining farms often use `дата-центр` language and large MW. Tag separately unless the operator/offical record says cloud/AI/colocation workloads.
- Exact cloud AZ location is usually intentionally hidden. Do not map `ru-central1-a` or VK/Cloud.ru AZs to a city/building without a second primary source.
- Sanctions/business-exit pages are useful for AWS/Microsoft availability but are not evidence of local facilities.
