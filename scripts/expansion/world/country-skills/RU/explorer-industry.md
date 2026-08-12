# RU Explorer Industry — Russian Trade Press, Vendors, and Regional Query Patterns

Date: 2026-08-11. Scope: how to enumerate Russian Federation datacenter / data centre / center of data processing projects through Russian-language industry/trade press, vendor pages, and Yandex-first regional search. Reliability grades: **A** = official/primary source; **B** = established trade press, analyst ranking, or vendor official page for existence; **C** = directories, maps, local promotion, social posts, or unverified aggregators.

---

## 0. Market structure that should drive enumeration

- Russia is highly concentrated in **Moscow / Moscow Oblast** and **Saint Petersburg / Leningrad Oblast**, but 2025-2028 expansion language increasingly points to regional sites where power is available: **Kaluga, Tver/Udomlya, Sverdlovsk/Yekaterinburg, Novosibirsk, Irkutsk, Krasnoyarsk, Khakassia, Murmansk, Primorye/Vladivostok, Tatarstan/Innopolis, Nizhny Novgorod, Samara, Krasnodar, Dagestan**.
- Commercial colocation enumeration is unusually well served by **CNews Analytics** and **ComNews Vision** rankings. CNews 2025 lists the leading providers and rack counts: RTK-DC, IXcellerate, Rosatom, DataPro, Selectel, MWS, Linx Datacenter, 3data, DataHouse, Key Point, Oxygen, Stack Telecom, DataSpace, DCN1, and smaller Moscow/regional operators. Source: https://www.cnews.ru/reviews/tsentry_obrabotki_dannyh_2025/review_table/55cae216fad4d9ab5a3fd9b4a5e9141e23f0f1af. **Grade B**.
- ComNews has a dedicated datacenter feed and an annual "Vision: Key commercial datacenters in Russia and CIS" package. Use it as the best trade-press cross-check for operator legal entities and expansion plans. Sources: https://www.comnews.ru/datacenter and https://www.comnews.ru/vision/8/datacenters2024. **Grade B**.
- A new **MinTsifry register of Russian data centers** is the official channel created by the 2025 datacenter law, but current ministry material says the register exists as a service/filing mechanism rather than a complete public facility list. Use article-level confirmations of specific inclusions, not as a complete census. Source: https://digital.gov.ru/activity/gos-uslugi/reestr-czentrov-obrabotki-dannyh-czod. **Grade A for legal framework; incomplete for enumeration**.
- Official vendor pages are often the quickest seed for live/announced campuses, but capacity is marketing capacity unless backed by permit, commissioning, or ranking data. Treat exact address/rack/MW on official pages as **A-/B**, then verify status with trade press, local construction notices, or maps.

---

## 1. Russian/Yandex search patterns

### 1.1 Engines and operators

- **Yandex Search** is mandatory for local Russian coverage. Official Yandex docs support `site:`, `host:`, `rhost:`, `url:`, `mime:`, `lang:`, and `date:` operators; `mime:pdf`, `lang:ru`, and `date:20250101..20261231` are useful for regional PDFs and fresh articles. Docs: https://yandex.com/support/search/en/query-language/qlanguage and https://yandex.com/support/search/en/query-language/search-operators. **Grade A for syntax**.
- **Google/Bing** often surface English operator pages, Data Center Dynamics, and PDFs mirrored outside Russia; they are weaker for small Russian municipal pages.
- **Yandex Maps and 2GIS** catch operating facilities and local names. Use them as **C/B-** seeds only; always pivot to operator or press pages.
- **Telegram/VK** are real announcement channels for Russian DC operators. Search via web index first (`site:t.me/s/`, `site:vk.com`) and grade as **C** unless it is the operator's verified channel and has photos/commissioning details.

### 1.2 Core vocabulary

Use all variants; Russian sources mix terms heavily:

```
ЦОД
центр обработки данных
центры обработки данных
дата-центр
дата центр
центр хранения и обработки данных
стойко-места
серверные стойки
ИТ-стойки
мощность МВт
подведенная мощность
коммерческий ЦОД
модульный ЦОД
edge-ЦОД
облачная зона
зона доступности
машинный зал
```

Status verbs:

```
построит / построят       planned, weak until permit/start
анонсировал / планирует   planned
соглашение / инвестпроект planned, C unless backed by site work
приступил к строительству construction started
получил разрешение        permit signal
введен в эксплуатацию     operational/commissioned
запущен / открыл          operational
расширил / ввел зал       expansion
сертифицирован Tier       certification evidence, not capacity proof
```

### 1.3 Copy-paste query templates

Discovery by subject/city/operator:

```
"{регион}" ("ЦОД" | "дата-центр" | "центр обработки данных") ("построит" | "строительство" | "ввод" | "запуск" | "открыл")
"{город}" ("ЦОД" | "дата-центр") ("стойк" | "МВт" | "Tier III" | "Tier IV")
"{оператор}" ("ЦОД" | "дата-центр") ("{регион}" | "{город}") ("стойк" | "МВт" | "в эксплуатацию")
"{индустриальный парк}" ("ЦОД" | "дата-центр" | "центр обработки данных")
```

Trade-press scoped:

```
("ЦОД" | "дата-центр") "{регион}" site:cnews.ru
("ЦОД" | "дата-центр") "{регион}" site:market.cnews.ru
("ЦОД" | "дата-центр") "{регион}" site:comnews.ru
("центр обработки данных" "{оператор}") site:comnews.ru
```

Yandex filters:

```
"{регион}" "ЦОД" lang:ru date:20240101..20261231
"{регион}" "центр обработки данных" mime:pdf
"{город}" "дата-центр" site:{regional-domain}.ru
"{регион}" "ЦОД" rhost:ru.* date:2025*
```

Permits, construction, and local government:

```
"{регион}" "ЦОД" "разрешение на строительство"
"{город}" "центр обработки данных" "разрешение на строительство"
"{регион}" "ЦОД" "ввод в эксплуатацию"
"{город}" "дата-центр" "госстройнадзор"
"{регион}" "ЦОД" "инвестиционный проект"
"{регион}" "ЦОД" "индустриальный парк"
"{регион}" "ЦОД" "технологическое присоединение"
```

Directories/maps as seeds:

```
"{город}" "дата-центр" site:alldc.ru
"{город}" "ЦОД" site:telecombloger.ru/dcmap
"{город}" "дата-центр" site:2gis.ru
"{город}" "дата-центр" site:yandex.ru/maps
```

---

## 2. Industry/trade press to monitor

| Source | URL | How to use | Grade |
|---|---|---|---|
| CNews "Центры обработки данных" annual reviews | https://www.cnews.ru/reviews/tsentry_obrabotki_dannyh_2025/ | Start with rankings; capture rack counts, new racks, planned launches, and operator universe. CNews 2025 says top-30 commercial capacity rose from 73.6k to 78.7k rack places and lists 40 providers in the table. | B |
| CNews / CNews Market news | https://www.cnews.ru/ and https://market.cnews.ru/ | Search by exact region/operator. Good for project announcements: e.g., Kaluga/Yandex, Wildberries Dubna/Naro-Fominsk, Key Point regional projects. | B |
| ComNews datacenter feed | https://www.comnews.ru/datacenter | Best recurring telecom trade feed for Russian DC builds, regulation, and operator statements. | B |
| ComNews Vision 2024 map/ranking | https://www.comnews.ru/vision/8/datacenters2024 | Annual package with operator legal entities, rankings, Uptime-certified facilities, and a map/PDF. | B |
| iKS-Consulting DC market reports | https://survey.iksconsulting.ru/page82045366.html | Strong market totals and regional trends; often cited by operators. Many details may be paywalled. | B |
| TAdviser | https://www.tadviser.ru/ | Useful timeline/aggregation per operator/project; verify every important fact elsewhere. | C+/B- |
| DCD Russia tag | https://www.datacenterdynamics.com/en/news/?tag=russia | English-language cross-check for larger operator launches and sanctions-era context. | B |
| allDC map/catalog | https://alldc.ru/dcs/map/ | Facility directory by city; useful for names/addresses, not authoritative capacity. | C |
| Telecombloger DC map | https://telecombloger.ru/dcmap | Local directory/news feed; useful seed for smaller operators. | C |

---

## 3. Major vendor/operator pivots by region

### 3.1 National/top commercial operators

| Operator | Official / strong source | Regional focus to query | Notes |
|---|---|---|---|
| **RTK-DC / Rostelecom Data Centers / DataLine / SafeData / M9 / RTCloud** | https://www.rt-dc.ru/about/data-tsentry/ | Moscow, Saint Petersburg, Yekaterinburg/Sverdlovsk, Novosibirsk, Nizhny Novgorod, Udomlya/Tver, plus legacy Rostelecom regional sites | CNews ranks RTK-DC first in 2025 with 39 DCs and 27,823 rack places. Use RTK pages plus local `Ростелеком-ЦОД {город}`. |
| **IXcellerate** | https://www.ixcellerate.com/data-centers/ | Moscow City and Moscow Oblast/Mytyshchi/Veshki; south Moscow/Biryulyovo | Official page lists three Moscow campuses and Veshki with 7,500 rack spaces / 130+ MW planned. |
| **Rosatom / Atomdata** | https://atomdata.ru/centers/ | Tver/Udomlya, Saint Petersburg/Xelent, Tatarstan/Innopolis, Moscow/StoreData/Moscow-2, Arctic/Murmansk if live | Operator page lists Kalininsky, Xelent, Innopolis, StoreData, Moscow-2. Cross-check Arctic status in ComNews/CNews. |
| **DataPro** | https://datapro.ru/ | Moscow, Moscow Oblast, Tver/other expansion announcements | CNews top-4; official pages plus CNews/ComNews for capacity. |
| **Selectel** | https://selectel.ru/about/data-centers/ and https://docs.selectel.ru/infrastructure/locations/ | Saint Petersburg, Leningrad Oblast, Moscow, Novosibirsk | Official pages list owned DCs in Moscow, Saint Petersburg, and Leningrad Oblast; docs expose exact FIAS addresses and current location names. |
| **MWS / MTS Web Services / MTS** | https://mws.ru/ and MTS press | Moscow, Moscow Oblast, telecom-region cloud sites | CNews 2025 ranks MWS sixth; search both `MWS ЦОД` and `МТС дата-центр`. |
| **Linx Datacenter** | https://linxdatacenter.com/ | Saint Petersburg, Moscow | Strong official campus pages; cross-check ComNews/CNews. |
| **3data** | https://3data.ru/ | Moscow metro small/edge DCs; some regional partner points | Many small facilities; avoid double-counting metro-edge rooms as large campuses. |
| **DataHouse / Filanco** | https://datahouse.ru/ | Moscow, Saint Petersburg | Trade rankings plus official pages. |
| **Key Point** | https://keypoint-group.ru/ | Dubna-M/Moscow Oblast, Vladivostok/Primorye, Novosibirsk, Yekaterinburg/Sverdlovsk, Saint Petersburg, Dagestan, Krasnodar, Irkutsk, Moscow | Official page explicitly lists regional Tier III/IV network and rack/MW/year per planned site. |
| **Oxygen** | https://oxygen.ru/ | Moscow, Yekaterinburg/Sverdlovsk | Search `Oxygen МСК-2`, `Oxygen ЕКБ-1`, ComNews map PDFs. |
| **Stack Telecom / M1, DataSpace, DCN1, TrustInfo/I-Teco/K2, Goznak, Ostankino, Miran, Nubes, TechnoGorod, IT-Park, Digital Region** | CNews/ComNews rankings, official pages | Mostly Moscow/Saint Petersburg/Tatarstan/Samara/Mordovia | Smaller but enumerated in CNews 2025 table; pivot each legal/brand name into city searches. |

### 3.2 Captive cloud/platform and enterprise projects

- **Yandex**: search `Яндекс ЦОД Калуга Грабцево`, `Яндекс ЦОД Владимир`, `Яндекс дата-центр Сасово`, `Yandex Cloud зоны доступности`. Kaluga project is repeatedly cited in CNews/trade summaries as 63 MW / 3,800 racks planned; verify live status with local Kaluga and Yandex announcements.
- **Cloud.ru / Sber**: search `Cloud.ru ЦОД Московская область`, `Сбер ЦОД`, `SberCloud центр обработки данных`. Strong for Moscow Oblast and new cloud capacity.
- **VK Cloud / VK**: search `VK ЦОД`, `VK Cloud дата-центр`, `ВК центр обработки данных`.
- **Wildberries/RVБ**: search `Wildberries ЦОД Дубна`, `Wildberries ЦОД Наро-Фоминск`, `РВБ дата-центр`.
- **X5 / retail, banks, Rutube/Gazprom-Media, government agencies**: captive builds may not appear in colocation rankings; use local government and construction-permit queries.
- **Mining/HPC/AI projects**: Siberia and Far East announcements often blur datacenter, mining, and AI compute. Query both `ЦОД для ИИ`, `вычислительный центр`, `майнинг дата-центр`, and exclude pure mining if the target dataset is non-mining DCs.

---

## 4. Regional enumeration strategy

For every federal subject, run the common query bundle below, then add the regional pivots in the table.

Common bundle:

```
"{RU_NAME}" ("ЦОД" | "дата-центр" | "центр обработки данных")
"{CAPITAL_OR_MAJOR_CITY}" ("ЦОД" | "дата-центр") ("стойк" | "МВт" | "в эксплуатацию")
"{RU_NAME}" ("ЦОД" | "дата-центр") site:cnews.ru
"{RU_NAME}" ("ЦОД" | "дата-центр") site:comnews.ru
"{RU_NAME}" ("ЦОД" | "дата-центр") ("разрешение на строительство" | "инвестиционный проект" | "индустриальный парк")
"{RU_NAME}" ("ЦОД" | "центр обработки данных") mime:pdf lang:ru
```

Subject-specific Russian names and high-value pivots:

| Manifest division | Russian query name(s) | First pivots/operators/places |
|---|---|---|
| Adygea | Республика Адыгея, Адыгея, Майкоп | Low-probability; search government digitization and modular/edge DC. |
| Altai Republic | Республика Алтай, Горно-Алтайск | Low-probability; use `правительство Республики Алтай ЦОД` and telecom edge. |
| Altai | Алтайский край, Барнаул | Search `Барнаул ЦОД`, regional government, Rostelecom/MTS. |
| Amur | Амурская область, Благовещенск | Energy-rich border region; search AI/mining separately and exclude pure mining. |
| Arkhangelsk | Архангельская область, Архангельск | Query `Арктика ЦОД`, regional government, Rosatom/Arctic claims. |
| Astrakhan | Астраханская область, Астрахань | Telecom/regional gov edge; low commercial probability. |
| Bashkortostan | Республика Башкортостан, Башкирия, Уфа | Search Ufa, Rostelecom, MTS, local technopark. |
| Belgorod | Белгородская область, Белгород | Search local gov, telecom, disaster-recovery facilities. |
| Bryansk | Брянская область, Брянск | Low-probability; query local operator rooms and government IT. |
| Buryatia | Республика Бурятия, Улан-Удэ | Search power/cold-climate, telecom edge. |
| Chechnya | Чеченская Республика, Чечня, Грозный | Search regional digital ministry, sovereign/government DC. |
| Chelyabinsk | Челябинская область, Челябинск | Industrial-power region; search `индустриальный парк ЦОД`, local DC operators. |
| Chukotka | Чукотский автономный округ, Анадырь | Low-probability edge/satellite telecom; avoid mining false positives. |
| Chuvashia | Чувашская Республика, Чебоксары | Search gov/regional telecom. |
| Dagestan | Республика Дагестан, Махачкала | Key Point announced Dagestan site; query `Кей Поинт Дагестан ЦОД`, government investment news. |
| Ingushetia | Республика Ингушетия, Магас, Назрань | Low-probability; government IT and telecom edge. |
| Irkutsk | Иркутская область, Иркутск, Братск | High-value power region; query Cloud X, Key Point Irkutsk, AI DC, hydropower, `154 МВт ЦОД`. |
| Ivanovo | Ивановская область, Иваново | Low-probability; government/telecom. |
| Kamchatka | Камчатский край, Петропавловск-Камчатский | Edge/telecom; search regional digital ministry. |
| Kabardino-Balkaria | Кабардино-Балкария, КБР, Нальчик | Low-probability; government/telecom. |
| Karachay-Cherkessia | Карачаево-Черкесия, КЧР, Черкесск | Low-probability; government/telecom. |
| Krasnodar | Краснодарский край, Краснодар, Сочи | Key Point announced Krasnodar; also resort/edge and telecom sites. |
| Kemerovo | Кемеровская область, Кузбасс, Кемерово, Новокузнецк | Energy/coal region; separate mining from enterprise DC. |
| Kaliningrad | Калининградская область, Калининград | Edge/connectivity; query sovereign cloud and telecom. |
| Kurgan | Курганская область, Курган | Low-probability; government/telecom. |
| Khabarovsk | Хабаровский край, Хабаровск | Far East telecom/edge; cross-check with Vladivostok/Primorye operators. |
| Yugoria | Ханты-Мансийский автономный округ, ХМАО, Югра, Сургут, Ханты-Мансийск | Oil/gas captive DCs and power-rich mining false positives; query `ЦОД Югра нефтегаз`. |
| Kirov | Кировская область, Киров | Low-probability; local operator/government. |
| Khakassia | Республика Хакасия, Абакан, Саяногорск | Energy-rich; ComNews noted builds in Khakassia. Separate mining/HPC. |
| Kalmykia | Республика Калмыкия, Элиста | Low-probability; government/telecom. |
| Kaluga | Калужская область, Калуга, Грабцево | High-value: Yandex Kaluga / industrial park Grabtsevo; search local permits and CNews. |
| Komi | Республика Коми, Сыктывкар | Cold/power edge; query government/telecom, mining exclusions. |
| Kostroma | Костромская область, Кострома | Low-probability; government/telecom. |
| Karelia | Республика Карелия, Петрозаводск | Cold-climate/power claims; verify against operator pages. |
| Kursk | Курская область, Курск | Power/nuclear-adjacent; search Rosatom and regional investment news. |
| Krasnoyarsk | Красноярский край, Красноярск, Железногорск | High-value power/cold region; search AI/HPC DC, mining exclusion, ComNews. |
| Leningrad | Ленинградская область, Всеволожск, Невская Дубровка, Шушары | Selectel Dubrovka, SPb spillover, NK Park Shushary; search Gosstroynadzor/SPb+Lenoblast. |
| Lipetsk | Липецкая область, Липецк | Industrial SEZ; query `ОЭЗ Липецк ЦОД`. |
| Magadan | Магаданская область, Магадан | Edge/mining risk; verify non-mining use. |
| Mari El | Марий Эл, Йошкар-Ола | Low-probability; government/telecom. |
| Mordovia | Республика Мордовия, Саранск | `Госинформ Мордовия ЦОД`, ComNews/CNews smaller operators. |
| Moscow | Московская область, Подмосковье, Дубна, Наро-Фоминск, Мытищи, Вешки | Top priority: IXcellerate Veshki, Key Point Dubna-M, Wildberries, Cloud.ru, DataPro, DataSpace spillover. Use permits and local investment portals. |
| Moscow City | Москва | Top priority: RTK-DC/DataLine/M9/SafeData, IXcellerate, DataPro, 3data, DataSpace, Oxygen, Stack/M1, DCN1, many small operators. Use `stroi.mos.ru`, `mos.ru`, operator pages. |
| Murmansk | Мурманская область, Мурманск | Arctic/cold-climate DC claims; query Rosatom Arctic, ports/energy; verify status. |
| Nenetsia | Ненецкий автономный округ, НАО, Нарьян-Мар | Very low-probability; edge/government only. |
| Novgorod | Новгородская область, Великий Новгород | Low/medium; SPb spillover and industrial parks. |
| Nizhny Novgorod | Нижегородская область, Нижний Новгород | RTK expansion and regional cloud; search CNews/ComNews. |
| Novosibirsk | Новосибирская область, Новосибирск, Толмачево | Key Point live site, Selectel location docs, Siberian operator Sibtelco; high priority. |
| Omsk | Омская область, Омск | Search `ЦОД Омский`, local gov/industrial park; older project names need freshness checks. |
| Orenburg | Оренбургская область, Оренбург | Energy/mining false positives; government/telecom. |
| Oryol | Орловская область, Орел | Low-probability; government/telecom. |
| Perm | Пермский край, Пермь | Industrial-power region; query enterprise captive DC and telecom. |
| Penza | Пензенская область, Пенза | Low/medium; government/telecom. |
| Primorye | Приморский край, Владивосток | Key Point Vladivostok; Far East commercial DC; search port/connectivity. |
| Pskov | Псковская область, Псков | Low-probability; government/telecom. |
| Rostov | Ростовская область, Ростов-на-Дону | Key Point earlier roadmaps mention Rostov; search regional investment and telecom. |
| Ryazan | Рязанская область, Рязань, Сасово | Search Yandex legacy/rumored Sасово, local gov, telecom. |
| Yakutia | Республика Саха, Якутия, Якутск | Edge pilots/cold climate; distinguish mining. |
| Sakhalin | Сахалинская область, Южно-Сахалинск | Edge pilots and Key Point roadmap mentions; search regional digital ministry. |
| Samara | Самарская область, Самара, Тольятти, Жигулевская долина | Digital Region / Zhigulevskaya Dolina, telecom/regional DC. |
| Saratov | Саратовская область, Саратов | Low/medium; government/telecom. |
| North Ossetia | Северная Осетия, РСО-Алания, Владикавказ | Low-probability; government/telecom. |
| Smolensk | Смоленская область, Смоленск | Low-probability; government/telecom. |
| Saint Petersburg | Санкт-Петербург, Петербург, СПб | Top priority: Selectel, Linx, Xelent/Rosatom, Miran, DataHouse, OBIT, Key Point SPb, NK Park Shushary. Search `Госстройнадзор Петербурга ЦОД`. |
| Stavropol | Ставропольский край, Ставрополь | Key Point roadmap mentions; regional investment and telecom. |
| Sverdlovsk | Свердловская область, Екатеринбург | High priority: Key Point Yekaterinburg, Oxygen EKB-1, RTK, Ural industrial parks. |
| Tatarstan | Республика Татарстан, Татарстан, Казань, Иннополис | Rosatom Atomdata Innopolis, IT-Park, Stack Kazan; search official Tatarstan/SEZ Innopolis. |
| Tambov | Тамбовская область, Тамбов | Low-probability; government/telecom. |
| Tomsk | Томская область, Томск | University/science/captive compute; search `суперкомпьютерный центр` and non-colo DC. |
| Tula | Тульская область, Тула | Moscow spillover; search industrial parks and `дата-центр Тула`. |
| Tver | Тверская область, Удомля, Тверь | High priority: Rosatom/Atomdata Kalininsky at Udomlya; DataPro/RTK spillover. |
| Tuva | Республика Тыва, Кызыл | Very low-probability; edge/government. |
| Tyumen | Тюменская область, Тюмень | Oil/gas captive and power; search `Тюмень ЦОД`, Rostelecom/MTS. |
| Udmurtia | Удмуртская Республика, Ижевск | Government/telecom; low/medium. |
| Ulyanovsk | Ульяновская область, Ульяновск | Industrial/SEZ; government/telecom. |
| Volgograd | Волгоградская область, Волгоград | Telecom/regional operators; low/medium. |
| Vladimir | Владимирская область, Владимир | Search Yandex/enterprise DC rumors and Moscow spillover; verify with local sources. |
| Vologda | Вологодская область, Вологда, Череповец | Industrial-power; government/telecom. |
| Voronezh | Воронежская область, Воронеж | Regional hub; search telecom/local operators and captive enterprise DC. |
| Yamalia | Ямало-Ненецкий автономный округ, ЯНАО, Салехард, Новый Уренгой | Oil/gas captive, edge, mining false positives; search Gazprom/energy. |
| Yaroslavl | Ярославская область, Ярославль | Moscow spillover; government/telecom. |
| Jewish Autonomous Oblast | Еврейская автономная область, ЕАО, Биробиджан | Very low-probability; edge/government. |
| Transbaikalia | Забайкальский край, Чита | Energy/mining border region; verify non-mining DCs. |

---

## 5. Verification and grading rules

1. **Start with CNews/ComNews rankings** to build the commercial-operator universe, then pivot each operator into official facility pages and region-specific searches.
2. **Count a facility as operational only when the wording is `введен в эксплуатацию`, `запущен`, `открыл`, `начал оказывать услуги`, or the official operator page lists it as an active datacenter.** `Построит`, `планирует`, `анонсировал`, and `соглашение` remain planned.
3. **Separate rack places from server racks and IT load from facility power.** Russian sources use `стойко-места`, `ИТ-стойки`, `серверные стойки`, `подведенная мощность`, and `мощность ЦОД` inconsistently. Preserve the original unit.
4. **Watch Moscow/Moscow Oblast aliasing.** A site may be reported as Moscow while legally in Mytishchi, Dubna, Naro-Fominsk, or another oblast municipality. Store exact municipality when available.
5. **Avoid mining contamination.** Siberia/Far East power-rich regions have many `майнинг` announcements. Unless the target includes mining facilities, require colocation/cloud/enterprise IT language or named non-mining customers.
6. **Use maps/directories only to seed.** Yandex Maps, 2GIS, allDC, and Telecombloger are useful for names and addresses but should not carry capacity/status without operator or press corroboration.
7. **For public-sector/captive DCs, use local construction and government sources.** Queries for `разрешение на строительство`, `госстройнадзор`, `МаИП`, `ОЭЗ`, `инвестиционный проект`, `ПЗЗ`, `ввод в эксплуатацию`, and `технологическое присоединение` often expose projects before operator marketing.

Recommended evidence grades:

| Evidence | Grade |
|---|---|
| MinTsifry register inclusion / official law/regulation / city construction permit / government commissioning notice | A |
| Operator official facility page for existence/location | A-/B |
| Operator official page for design rack/MW capacity | B |
| CNews Analytics / ComNews Vision rankings and maps | B |
| CNews/ComNews/DCD article about specific start/opening | B |
| iKS-Consulting summary totals | B |
| TAdviser, allDC, Telecombloger, Yandex Maps, 2GIS | C seed unless verified |
| Telegram/VK/local promotional posts | C, or B- if official operator account with corroboration |

---

## 6. Practical pipeline

1. Pull the latest **CNews Analytics** table and **ComNews Vision** package; normalize operator names, legal entities, rack places, planned launches, and facility counts.
2. For every top-40 operator, crawl official pages and news for `ЦОД`, `дата-центр`, `стойк`, `МВт`, `в эксплуатацию`, and region names.
3. Run the subject table queries for all 84 manifest divisions, prioritizing: Moscow City, Moscow Oblast, Saint Petersburg, Leningrad, Tver, Kaluga, Sverdlovsk, Novosibirsk, Irkutsk, Krasnoyarsk, Khakassia, Primorye, Tatarstan, Nizhny Novgorod, Samara, Krasnodar, Dagestan, Murmansk.
4. For each candidate, verify status with at least two of: operator page, CNews/ComNews, government/permit page, credible map/address, satellite imagery.
5. Store aliases aggressively: Russian brand, English brand, legal entity, campus name, city/municipality, industrial park, and federal subject. Russia DC projects are often reported under different labels in different sources.

