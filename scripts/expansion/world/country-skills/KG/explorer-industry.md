# KG Explorer — Industry/Vendor Discovery for Kyrgyzstan Datacenters

Date: 2026-08-12 (final reviewed layer). Scope: Kyrgyzstan datacenter enumeration from colo providers, cloud/hosting operators, IXPs, CDN nodes, trade press, associations, and directories. Grades: **A** = official/primary (government, operator official pages, cloud-provider official, Uptime certification, audited disclosure), **B** = credible trade press / regulator-adjacent / strong project database, **C** = weak directory/map/aggregator or announcement without hard project evidence, **U** = unsupported claim. A grade covers only the fact actually supported by that source.

---

## 0. Kyrgyzstan-specific frame

- Bilingual/trilingual search market. Search in **Russian** first (richest coverage for operators, hosting, and press), then **English**, then **Kyrgyz** (rare but appears on republic portals and operator sites). Terms: see explorer-official.md section 1; add industry-side vocabulary: `колокация`, `хостинг`, `VPS`, `облако`, `CDN`, `пиринг`, `трафик`, `майнинг-ферма`, `Tier III`, `стойка`, `сервер`.
- Market structure (four discovery buckets):
  1. **Incumbent/ISP telecom colo and hosting**: KyrgyzTelecom (kt.kg), Elcat (ЭлКат), Aknet, Megaline, Saima Telecom, Hoster.kg, IFS — most run server rooms/colo in Bishkek; regional footprint is legacy telecom exchanges.
  2. **Commercial colo/cloud**: Datatime (commercial ЦОД, Bishkek, launched 2024, Uptime Tier III Design certification) with RackCorp international presence; IFS data-center services.
  3. **State e-gov / sovereign cloud**: Infocom (ГП «Инфоком») operating «Тундук» e-services; any state DC would live here — details largely non-public.
  4. **Crypto-mining farms**: high-power facilities (Chuy/Jalal-Abad/Osh regions) that directories may label «data centers» — record separately unless enterprise colo/cloud evidence exists.
- **IXPs**: KG-IX / IX.KG in Bishkek; PeeringDB IX 2145 lists KG-IX LLC, 22 peers, 29 connections, 1.0T total capacity, and AS61399 presence. CDN/cache networks visible on PeeringDB include Akamai, Cloudflare, Gcore, PCH/RIPE DNS infrastructure, and local ISPs. kglabs.org provides useful narrative context but should not override PeeringDB/operator records.
- **No hyperscaler public cloud region** for KG as of the 2026-08-12 live review of AWS/Azure/GCP/OCI/Yandex official region/location pages. International clouds serve KG from foreign regions; local «cloud» offerings are hosted on KG operator infrastructure or partner platforms.
- Best starting geography: **Bishkek** first (all commercial DCs), then **Chuy** (mining farms, Bishkek-adjacent), then **Osh City** (regional telecom), then the remaining oblasts (expect near-zero).

---

## 1. Authoritative and strong sources

### 1.1 Government, investment, and regulatory sources

| Source | URL | Use | Grade |
|---|---|---|---|
| Digital transformation authority | https://digital.gov.kg/ plus Decree No. 154 at https://cbd.minjust.gov.kg/5-11103/edition/52497/ru | Legacy ministry news, state ЦОД project, Inspur MOU, licensing-service references. Since 2026-04-29 the ministry was reorganized into the Department of Affairs of the President; search both names | A for official statements |
| Cabinet of Ministers | https://www.gov.kg/ru | NPA search for `ЦОД`, `дата-центр`, `майнинг` | A |
| National Investment Agency | https://invest.gov.kg/ru | Investor MOUs (e.g. Inspur Yunzhou 2025); counterparties | A for agreements; C for implied construction |
| egov.kg / Тундук / open data | https://egov.kg/ · https://portal.tunduk.kg/ · https://data.gov.kg/ | State e-services, state IT infrastructure, agency directory | A for services |
| Public procurement | https://zakupki.gov.kg/ · https://trade.okmot.kg · https://www.gostender.kg/ | DC/hosting/cloud tenders by state bodies | A for award/contract signal |
| NESK (grid) | https://www.nesk.kg/ru/ | Grid connections, substation news, power availability | A for grid facts |
| Personal-data register | https://registry.dpa.gov.kg/ | Holders of personal-data massifs (Digital Code regime from 2026-02-05) | A for registry entry |
| High Technology Park | https://htp.kg/ | IT-resident regime; resident lists may surface cloud/hosting companies | A for regime; C for facilities |

Important: in Kyrgyzstan, **MOU/investment-agreement articles are common and must not be counted as construction** unless followed by land allocation, construction start, procurement, grid/power evidence, operator pages, or commissioning reports. The market is small — a single facility can dominate results; dedupe aggressively.

### 1.2 Operator, certification, and directory sources

| Source | URL | Use | Grade |
|---|---|---|---|
| Datatime (operator) | https://datatime.kg/ | Commercial ЦОД in Bishkek; opened 2024-06-10/11; markets 500 kW+ and colocation/cloud | A for operator-stated existence, address, services, and launch |
| RackCorp KG page | https://www.rackcorp.com/ru/network/datacenters/kyrgyzstan/datatime/ | International colo/cloud partner presence in Datatime | B |
| Uptime Institute Datatime record | https://uptimeinstitute.com/component/tierachievement/datacenter/datatime-bishkek-kr-data-center-data-5/2191 | Datatime Bishkek KR Data Center Data 5, Bishkek, Kyrgyzstan | A for Tier III Design certification only |
| KyrgyzTelecom | https://kt.kg/ru/ · https://kt.kg/ru/dcasa-rus/ | Incumbent services; official DCASA page states co-location in KyrgyzTelecom data centers | A for service offering; B/C for historical 2017 facility specs unless current primary evidence is found |
| Aknet | https://www.aknet.kg/ | Cloud/hosting services («Управляемое облако», web hosting, dedicated web servers) | A- for service offering; C for facility specs |
| Megaline | https://megaline.kg/ | ISP with an official business hosting page; no standalone DC evidence found | A- for hosting service; C for any facility inference |
| Elcat (ЭлКат) | https://www.elcat.kg/ and legacy hosting surface https://www.alliance.web.kg/ | Major ISP; PeeringDB confirms ElCat AS8449 at KG-IX. Legacy hosting pages may be intermittent | A/B for network presence; C for facility inference |
| Saima Telecom | https://www.saimatelecom.kg/ | Major ISP; PeeringDB confirms Saimanet at KG-IX. No official colo/DC page found in this pass | A/B for network presence; C for facility inference |
| Hoster.kg | https://hoster.kg/ | Local hosting provider | C |
| IFS | https://www.ifs.kg/centr-obrabotki-dannyh-data-centr/ | System integrator offering data-center services | B/C |
| PeeringDB KG-IX | https://www.peeringdb.com/ix/2145 | IX participants, capacity (22 peers, ~1 Tbps), facility links | A for IX data |
| RIPE NCC member records | https://www.ripe.net/membership/member-support/list-of-members/kg/ix/ | KG-IX LLC LIR record (Razzakova 55, Bishkek) | A |
| ix.report | https://ix.report/ix/kg-ix-bishkek/ | IX stats mirror | C |
| Data Center Map KG | https://www.datacentermap.com/kyrgyzstan/ (Bishkek: https://www.datacentermap.com/kyrgyzstan/bishkek/) | Directory leads for Bishkek/Lebedinovka facilities; corroborate names and addresses before counting | B/C |
| Uptime Institute awards | https://uptimeinstitute.com/uptime-institute-awards/list | Re-check for KG entries; Datatime has a direct Tier III Design project page | A if entry exists |
| hostings.info KG | https://ru.hostings.info/hostings/country/kyrgyzstan-hosting | Hosting-provider ratings for KG | C |
| 2GIS / Yandex Maps | https://2gis.kg/bishkek/search/Дата-центры | Local address discovery (datacenters rubric exists in Bishkek) | C |
| kglabs.org | https://kglabs.org/the-layer-you-dont-see-internet-backbone/ | KG internet backbone/IXP technical history (KG-IX 2017, Fergana IXP attempt, CDN nodes) | B |

---

## 2. Query templates

### 2.1 National discovery (Google/Bing/Yandex)
```text
Kyrgyzstan "data center" "Bishkek"
"Кыргызстан" "ЦОД" "Бишкек"
"Кыргызстан" "центр обработки данных" "Бишкек"
"Кыргызстан" "дата-центр" "Бишкек"
"Kyrgyzstan" "colocation"
"Кыргызстан" "колокация"
"Кыргызстан" "размещение серверов"
"Kyrgyzstan" "cloud" "hosting"
"Кыргызстан" "облако" "хостинг"
"Kyrgyzstan" "Tier III" "data center"
Кыргызстан "центр обработки данных" "запуск"
Кыргызстан "центр обработки данных" "открытие"
Кыргызстан "центр обработки данных" "ввод в эксплуатацию"
"Кыргызтелеком" "ЦОД"
"Кыргызтелеком" "дата-центр"
"Кыргызтелеком" "центр обработки данных"
"Datatime" "ЦОД" "Бишкек"
"RackCorp" "Kyrgyzstan" "data center"
"Saima" "дата-центр" "Бишкек"
"Saima" "ЦОД" "Бишкек"
"Акнет" "хостинг" "дата-центр"
"ЭлКат" "хостинг" "ЦОД"
"Мегалайн" "хостинг" "дата-центр"
```

### 2.2 IXP / interconnection sweeps
```text
site:peeringdb.com Kyrgyzstan Bishkek
site:peeringdb.com/ix KG-IX
"KG-IX" participants Bishkek
"KG-IX" capacity Bishkek
"IX.KG" "Kyrgyz Internet Exchange"
Kyrgyzstan "internet exchange" "Bishkek"
site:ix.report kg-ix-bishkek
Kyrgyzstan CDN node Apple "KG-IX"
Kyrgyzstan CDN node Meta "KG-IX"
Kyrgyzstan CDN node TikTok "KG-IX"
```

### 2.3 Status and capacity extraction
```text
"{project}" "МВт"
"{project}" "kW"
"{project}" "мощность" "стойк"
"{project}" "Tier III" "Uptime"
"{project}" "запущен"
"{project}" "введен в эксплуатацию"
"{project}" "строительство началось"
"{project}" "меморандум"
"{project}" "соглашение"
"{operator}" "годовой отчет" "дата-центр"
"{operator}" "ЦОД" "{city_ru}"
"{operator}" "хостинг" "тарифы" "Бишкек"
```

Lifecycle verbs:
- English: `planned`, `signed`, `MOU`, `construction began`, `breaks ground`, `launched`, `commissioned`, `go live`.
- Russian: `планируется`, `подписали меморандум`, `соглашение`, `началось строительство`, `заложили`, `открыли`, `запущен`, `введен в эксплуатацию`, `завершено строительство`.
- Kyrgyz: `пландалууда`, `меморандумга кол коюлду`, `курулушу башталды`, `ишке киргизилди`.

---

## 3. Key vendors and project families to seed

### 3.1 Incumbent telecom and colo/cloud operators

- **KyrgyzTelecom (ОАО «Кыргызтелеком»)** — state incumbent, kt.kg; official DCASA page states co-location in KyrgyzTelecom data centers with power, conditioning, and security. TAdviser and 2017 press describe a historical Tier-III-level/5 MW concept; keep those as historical leads unless current kt.kg/procurement evidence confirms present capacity.
- **Datatime** — commercial ЦОД in Bishkek, opened 2024-06-10/11; operator page lists Koytashsky lane 46/1, 500 kW+ commercial IT data center positioning, dual 6 kV city substation supply, 1 MW generators, UPS and rack pricing. Uptime Institute has a direct project page for **Tier III Certification of Design Documents** for Datatime Bishkek KR Data Center Data 5. Do not upgrade that to constructed-facility or operations certification without a matching Uptime record.
- **Elcat (ОСОО «ЭлКат»)** — major ISP/network; PeeringDB confirms ElCat AS8449 at KG-IX. Use `elcat.kg`, `alliance.web.kg`, PeeringDB, and procurement records as discovery, but do not count an Elcat DC without an official/current facility page or contract.
- **Aknet (Акнет)** — aknet.kg; offers managed cloud with RackCorp and has Bishkek/Osh branches. **A- for service offering; C for facility specs unless a physical colo/DC source is found.**
- **Megaline (Мега-Лайн)** — megaline.kg; official hosting page exists. **A- for hosting service; C until facility evidence.**
- **Saima Telecom** — saimatelecom.kg; major private ISP and PeeringDB KG-IX participant. **A/B for network presence; C for colo/DC inference.**
- **Hoster.kg** — local hosting provider (since 2004 per hostings.info). **C.**
- **IFS** — system integrator with an explicit data-center service page (ifs.kg). **B/C.**
- **Regional ISPs** (Homeline homeline.kg, NeoTelecom neotelecom.kg, Eletcom eletcom.kg in Nookat/Osh region, etc.) — small operators; server rooms, not commercial DCs. **C.**
- Rule: many of these are tenants inside each other's colo rooms — record the physical facility and the tenant separately to avoid double counting.

### 3.2 Hyperscale, AI, and high-power projects

- **Inspur Yunzhou Industrial Internet Co., Ltd (China)** — official digital.gov.kg article states an MoU on digital technologies, construction of data-processing centers, cloud solutions, AI, and industrial internet. **A for MoU intent only; no site/capacity/construction evidence.**
- **Государственный ЦОД (state data center)** — 2023 design tender and press-reported specs exist; 2026 MIA DC procurement exists separately. Do not count either as an operating national DC without commissioning/acceptance or operator evidence.
- **Crypto-mining farms** — historically concentrated in Chuy (Tokmok/Kant/Kara-Balta/Lebedinovka area), Jalal-Abad, Osh regions; policy-restricted during winter power deficits and regulated separately in energy/tax/legal acts. High-MW «data center» listings in these regions are usually mining — tag `mining/HPC` unless colo/cloud customers are documented.
- **Public cloud regions**: AWS, Azure, Google Cloud, Oracle, and Yandex show no KG public cloud region on official pages as of 2026-08-12. Local «cloud» (Aknet/RackCorp, Hoster, RackCorp/Datatime) runs on KG operator/partner infrastructure. Any claim of a hyperscaler KG region needs the provider official page as evidence.

---

## 4. Per-division industry enumeration approach

For every division run the division/city in English + Russian (+ Kyrgyz where useful); directories list cities more often than oblasts.

| Division | Industry/vendor approach | Expected yield |
|---|---|---|
| Bishkek | Priority: Datatime, KyrgyzTelecom DCASA/ЦОД, Aknet/RackCorp, Elcat/Megaline/Hoster/IFS service claims, KG-IX participants, 2GIS «Дата-центры» rubric, Data Center Map Bishkek leads | Highest — most KG records |
| Chuy | Mining-farm checks (Tokmok, Kant, Kara-Balta, Sokuluk, Lebedinovka), Bishkek-adjacent industrial zones, NESK/power news, NSP/Data Center Map lead in Lebedinovka | Low-moderate (mostly mining or directory leads) |
| Osh City | KyrgyzTelecom Osh exchange, southern hosting resellers, radio-monitoring office | Low |
| Osh | Regional ISPs (e.g. Eletcom in Nookat), border-trade zones | Very low |
| Jalal-Abad | Energy towns (Tash-Kumyr), mining reports | Very low |
| Batken | None expected; check state edge infrastructure | Essentially none |
| Naryn | Hydropower cascade context only | Essentially none |
| Talas | None expected | Essentially none |
| Issyk-Kul | Karakol/Cholpon-Ata tourism-digital projects, event infrastructure (F1H2O 2026) | Very low |

Per-division templates: `"{city_ru}" "дата-центр"`, `"{city_ru}" "ЦОД"`, `"{city_ru}" "серверная"`, `"{city_ru}" "хостинг"`, then `"{city_ru}" "майнинг" "электроэнергия"` and `"{city_ru}" "ферма" "электроэнергия"` to separate mining.

---

## 5. Trade press and association watchlist

- **Local press (RU)**: 24.kg (https://24.kg/), Economist.kg (https://economist.kg/), Tazabek (https://www.tazabek.kg/), Akchabar (https://akchabar.kg/), Kabar (state agency, https://kabar.kg/), Sputnik Кыргызстан (https://ru.sputnik.kg/), Kaktus.media (https://kaktus.media/), mes.kg tech section. Grade B; reconcile numbers against operator/government pages.
- **Regional/international tech press**: TAdviser (https://www.tadviser.ru/ — has ЦОД Кыргызтелеком product page), CNews, Data Center Dynamics (https://www.datacenterdynamics.com/), Developing Telecoms, Telecom Review. Grade B/C depending on sourcing.
- **Associations/communities**: no dedicated national datacenter-industry association was found in this pass. Use High Technology Park resident lists (htp.kg), RIPE NCC/PeeringDB community records, ISOC/KG internet-community mentions, and local IT events as lead sources only.
- **Directories**: Data Center Map, datacenters.com, Cloudscene, hostings.info, 2GIS, Yandex Maps — discovery surfaces only; corroborate before counting.

---

## 6. Verification and grading rules

1. **Do not double count operator vs tenant.** Example: international clouds (e.g. RackCorp) and local hosters may resell inside Datatime — record the physical DC once; cloud providers as tenants/partners.
2. **Separate enterprise DC from mining/HPC.** High-MW «data center» entries in Chuy/Jalal-Abad/Osh are usually mining farms; tag them separately unless colo/cloud customers are documented.
3. **Use exact certification stage.** Datatime has Uptime Tier III Design certification; this is not the same as Tier Certification of Constructed Facility or Operations. Marketing phrases such as `Tier III*` are lower-grade unless tied to the Uptime page.
4. **Capacity hierarchy**: operator official IT MW/racks (A) > operator official pages without numbers (A-/B) > government project pages (A/B by stage) > trade press (B) > directories/maps (C).
5. **Status hierarchy**: operational page/certification/commissioning report > construction-start release > procurement/grid/power contract > investment treaty/MOU > directory-only lead. One Uptime KG project record was found (Datatime Tier III Design); no separate constructed-facility or operations certification was found.
6. **Local-language aliases**: Bishkek/Бишкек; Osh/Ош; Chuy/Чуй; Jalal-Abad vs Жалал-Абад vs Джалал-Абад; Issyk-Kul vs Иссык-Куль vs Ысык-Көл; Karakol/Каракол; Naryn/Нарын; Batken/Баткен; Talas/Талас.
7. **Boundary check**: Bishkek vs Chuy oblast; Osh City vs Osh oblast — bucket by physical municipality, not marketing metro.

Recommended output notes should preserve source class: `operator official`, `government agreement`, `trade press`, `directory only`, `mining/HPC`, `tenant in third-party DC`, or `MOU only`.

---

## 7. Update / re-check cadence

- **Monthly**: PeeringDB KG-IX page (peers/capacity); 24.kg/Economist.kg/Tazabek searches for `ЦОД/дата-центр/хостинг`; aknet.kg/kt.kg/datatime.kg service-page diffs.
- **Quarterly**: re-run cloud-region official pages (AWS/Azure/GCP/OCI/Yandex) for any KG entry; Uptime Institute awards/project list for KG; Data Center Map KG page for new facilities; check whether Datatime advances beyond Design certification.
- **Semi-annually**: check for a national DC association or IT-union formation; refresh Elcat/Saima/Megaline facility evidence; re-check Inspur Yunzhou status (MOU → land → construction).
- **Event-driven**: invest.gov.kg and president.kg announcements; energy-crisis regulations; new IXPs or CDN node announcements at KG-IX/IX.KG.

## Quick URL index

- Datatime: https://datatime.kg/ · RackCorp KG: https://www.rackcorp.com/ru/network/datacenters/kyrgyzstan/datatime/
- KyrgyzTelecom: https://kt.kg/ru/ · DCASA https://kt.kg/ru/dcasa-rus/ · Aknet: https://www.aknet.kg/ · Aknet cloud https://aknet.kg/dlja_biznesa/oblachnye_servisy/ · Megaline hosting https://megaline.kg/dlya-biznesa/uslugi/hosting/ · Saima: https://www.saimatelecom.kg/ · Hoster.kg: https://hoster.kg/ · IFS: https://www.ifs.kg/centr-obrabotki-dannyh-data-centr/ · Elcat: https://www.elcat.kg/
- KG-IX PeeringDB: https://www.peeringdb.com/ix/2145 · ix.report: https://ix.report/ix/kg-ix-bishkek/ · RIPE KG LIR: https://www.ripe.net/membership/member-support/list-of-members/kg/ix/
- Data Center Map KG: https://www.datacentermap.com/kyrgyzstan/ · Bishkek: https://www.datacentermap.com/kyrgyzstan/bishkek/ · IXP: https://www.datacentermap.com/ixp/kyrgyz-internet-exchange/
- Uptime Institute awards: https://uptimeinstitute.com/uptime-institute-awards/list
- hostings.info KG: https://ru.hostings.info/hostings/country/kyrgyzstan-hosting
- kglabs.org backbone: https://kglabs.org/the-layer-you-dont-see-internet-backbone/
- 2GIS Bishkek datacenters rubric: https://2gis.kg/bishkek/search/Дата-центры
- Cross-reference official pipeline: explorer-official.md (same folder) for ministry/regulator/energy/procurement surfaces.



