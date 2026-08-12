# BY Explorer Industry - Belarus Datacenter Lead Generation

Date: 2026-08-12. Scope: Belarus (BY), all 7 divisions: Brest; Gomel; Grodno; Minsk; Minsk City; Mogilev; Vitebsk.

Purpose: find operator, trade-press, directory, peering, market, and siting leads for datacenter enumeration, then send each candidate to `explorer-official.md` for official/operator verification.

Review status: final methodology pass completed with live URL and search verification in August 2026. Use this file for discovery only. Use `explorer-official.md` to decide final facility status, division assignment, and evidence grade.

## 0. Market Frame

Belarus is a small, Minsk-first, state-influenced datacenter market. Confirmed public operator anchors are concentrated in Minsk City and nearby Minsk Oblast:

- Beltelecom commercial datacenter/hosting services: https://datacenter.by/ and https://beltelecom.by/business/hosting .
- beCloud Republican Data Processing Centre (RCOD) in Kolodishchi, Minsk district: https://becloud.by/contacts/ and https://becloud.by/customers/regulations-rcod/ .
- A1 Digital Tier III-class commercial datacenter services: https://a1digital.by/data-center/ .
- MTS Cloud / MTS datacenter infrastructure: https://cloud.mts.by/ and https://cloud.mts.by/company/about/ .
- Datahata colocation/hosting service claim: https://www.datahata.by/ .

No verified public commercial datacenter was found in Brest, Gomel, Grodno, Mogilev, or Vitebsk Oblasts during this review. Those divisions still require explicit negative sweeps because regional Beltelecom, FEZ, procurement, server-room, and government IT leads can appear.

Belarus is landlocked; ignore submarine-cable landing workflows. Connectivity research should focus on overland fiber, Beltelecom, mobile operators, and BY-IX. BY-IX/PeeringDB evidence is useful for interconnection context, but an IXP is not a datacenter unless a facility/colocation claim is separately supported.

Sanctions since 2021-2022 make new Western hyperscale investment unlikely. Do not use sanctions commentary as facility evidence. Official AWS, Azure, Google Cloud, and Oracle Cloud infrastructure pages did not list Belarus public regions/local zones as of this review.

Discovery chain:

```text
lead from operator/trade/directory/procurement
-> operator-owned page or official/procurement record
-> EGR legal entity lookup
-> cadastre / municipal / state-expertise check if address or parcel is known
-> energy and connectivity context
-> directory/PeeringDB cross-check
-> final grade per fact in explorer-official.md
```

## 1. Reliability Grades For Lead Handling

- **A**: operator-owned current facility/project/service page or operator press release; official investment-promotion page only for the promoted offer; official procurement/municipal/register record.
- **B**: established trade/business/construction press, PeeringDB/interconnection evidence, company annual/project reports, telecom/IT association material.
- **C**: directories, aggregators, social media, commercial tender monitors, old mirrors, unsourced market reports, or promotional capacity claims.
- **U**: unresolved lead. Search again before use.

Grade the supported fact only. Example: a directory may be useful for an address lead but remains C until an operator page, EGR/cadastre record, procurement document, or municipal source corroborates it.

## 2. Search Vocabulary

Russian, primary:

```text
центр обработки данных
ЦОД
дата-центр
датацентр
серверная
колокация
размещение оборудования
хостинг
облако
облачные вычисления
облачные сервисы
стойко-место
точка обмена трафиком
магистральный кабель
резервное питание
дизельные генераторы
трансформаторная подстанция
госэкспертиза
госзакупки
```

Belarusian, secondary:

```text
цэнтр апрацоўкі дадзеных
дата-цэнтр
серверная
серверны пакой
калакацыя
хостінг
воблака
воблачныя вылічэнні
лічбавая інфраструктура
пункт абмену трафікам
```

English:

```text
Belarus data center
Belarus data centre
Minsk data center Tier III
Belarus colocation
Belarus cloud provider data center
Beltelecom data center
beCloud RCOD Kolodishchi
A1 Digital data center Minsk
MTS Cloud data center Minsk
Belarus internet exchange BY-IX
Belarus hyperscale data center
```

## 3. Strong Industry And Trade Sources

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Beltelecom TsOD | https://datacenter.by/ ; https://datacenter.by/razmeshchenie-oborudovaniya ; https://beltelecom.by/business/hosting | State operator commercial hosting/colocation/datacenter offer. | A for operator offer; regional locations need corroboration |
| beCloud | https://becloud.by/ ; https://becloud.by/contacts/ ; https://becloud.by/customers/regulations-rcod/ | RCOD and national cloud platform; Kolodishchi address. | A |
| A1 Digital | https://a1digital.by/ ; https://a1digital.by/data-center/ ; https://a1digital.by/services/colocation/ | Commercial Tier III-class datacenter services. | A for operator claim |
| MTS Cloud | https://cloud.mts.by/ ; https://cloud.mts.by/company/about/ ; https://cloud.mts.by/support/articles/data-tsentr-i-oblachnaya-infrastruktura/ | MTS Cloud services and Minsk/own-infrastructure claims. | A for operator claim |
| NTSEU | https://nces.by/ ; https://nces.by/oblachnoe_hranilishche/ | State cloud/storage/e-government platform. | A, but not commercial colo |
| Datahata | https://www.datahata.by/ | Colocation/hosting service lead. | A for service claim; address needs corroboration |
| Serverspace Belarus | https://serverspace.by/ | Cloud/VPS provider; check infrastructure page and whether it is a tenant in beCloud RCOD before counting. | A for service claim; tenant footprint if hosted in RCOD |
| hoster.by | https://hoster.by/ | Hosting/VPS lead; verify own-facility claim before counting. | A for service claim, C for facility census until corroborated |
| besthost.by | https://besthost.by/ | Hosting/VPS lead. | A/C as above |
| hostfly.by | https://www.hostfly.by/ | Hosting/VPS lead. | A/C as above |
| bcr.by / Rekun | https://www.bcr.by/ | Hosting/IT services lead. | A/C as above |
| Onliner Tech | https://tech.onliner.by/ ; queries below | Historical operator articles: Beltelecom, velcom/A1, MTS. | B |
| OfficeLife | https://officelife.by/ | Business press; useful for RCOD/Tier reporting. | B |
| BELTA | https://belta.by/ | State news agency; Beltelecom/state modernization leads. | B |
| ComNews | https://www.comnews.ru/ ; Belarus DC market article search | Telecom trade market mapping. | B |
| TAdviser | https://www.tadviser.ru/ | Project-history and area/capacity leads; confirm with primary sources. | B/C depending on sourcing |
| Dev.by | https://dev.by/ | IT-market news and hiring signals. | B when article is sourced |
| PeeringDB | https://www.peeringdb.com/ ; BY-IX org 598/search country BY | Interconnection signal only. | B for peering, not facility existence |

Useful press queries:

```text
site:tech.onliner.by "дата-центр" velcom
site:tech.onliner.by "ЦОД" Белтелеком
site:tech.onliner.by "МТС" "дата-центр"
site:officelife.by beCloud РЦОД Tier III
site:belta.by Белтелеком ЦОД
site:comnews.ru Беларусь дата-центры
site:dev.by Беларусь ЦОД
```

## 4. Directories And Aggregators

Use these for aliases, candidate addresses, and seed lists only. Do not final-count a facility from a directory alone.

| Source | URL | Use | Grade |
|---|---|---|---|
| DataCenterMap | https://www.datacentermap.com/belarus/ ; https://www.datacentermap.com/belarus/minsk/ | Belarus/Minsk facility and operator leads. | C |
| Datacenters.com | https://www.datacenters.com/locations/belarus ; https://www.datacenters.com/locations/belarus/minsk | Provider/address leads. | C |
| Inflect | https://inflect.com/datacenters/emea/belarus/minsk | Address/operator leads. | C |
| DataCenterJournal | https://www.datacenterjournal.com/data-centers/belarus/minsk/ | Roundup leads. | C |
| Baxtel | https://baxtel.com/data-center/belarus | Quick long-tail leads. | C |
| Cloudscene | https://cloudscene.com/ | Colocation/cloud-provider leads. | C |
| DC-Union base | https://base.dcunion.ru/index.php?title=Рынок_ЦОД_Белоруссии | Market list; useful for MTS/address leads but not final proof. | C |
| Zakupki monitors | https://zakupki.by/ ; https://tenders.by/ | Tender leads. Confirm on goszakupki.by or issuer page. | C |

## 5. Operator And Project Seeds

### 5.1 Beltelecom TsOD

Primary evidence: https://datacenter.by/ and https://beltelecom.by/business/hosting . The operator offers colocation/hosting/datacenter services. Historical press identifies earlier Minsk facilities, including a Zakharova 55 reference; treat historical addresses as B until current operator or municipal confirmation is found.

Regional Beltelecom TsOD claims appear in market/trade material, but this review did not verify Brest/Gomel/Grodno/Mogilev/Vitebsk-specific public addresses. Carry as leads only.

```text
Белтелеком ЦОД адрес
"Захарова 55" "Белтелеком" "ЦОД"
Белтелеком "центр обработки данных" областной
site:beltelecom.by ЦОД
site:datacenter.by размещение оборудования
```

Grade: A for current operator service pages; B/C for historical or regional claims depending on source.

### 5.2 beCloud / RCOD

Primary evidence: https://becloud.by/contacts/ and https://becloud.by/customers/regulations-rcod/ confirm RCOD at `агрогородок Колодищи, ул. Центральная, 22`, Minsk district, Minsk Oblast. beCloud service rules and platform pages support the national cloud / republican platform role. Trade sources report size, phased development, and Tier III/Uptime-related claims; verify certification currency directly before using those as final facts.

```text
"Республиканский центр обработки данных" beCloud
beCloud Колодищи Центральная 22
beCloud РЦОД Tier III
site:becloud.by РЦОД
site:becloud.by Центральная 22
```

Grade: A for operator address/service facts; B for trade-reported area/certification history.

### 5.3 A1 Digital / A1 Belarus / velcom legacy

Primary evidence: https://a1digital.by/data-center/ and https://a1digital.by/services/colocation/ . A1 states the datacenter was built in 2017 and markets it as Tier III-class / highest reliability level in Belarus. Historical velcom/A1 launch and tour articles are useful B-grade context. Exact physical address was not confirmed from the public operator pages during this review.

```text
A1 Digital дата-центр Минск
A1 "дата-центр" адрес
velcom "дата-центр" Tier III
site:a1digital.by дата-центр
site:a1digital.by colocation
```

Grade: A for operator service and Tier-class claim; B for press history; address remains unconfirmed unless sourced elsewhere.

### 5.4 MTS Belarus / MTS Cloud

Primary evidence: https://cloud.mts.by/ , https://cloud.mts.by/company/about/ , and https://cloud.mts.by/support/articles/data-tsentr-i-oblachnaya-infrastruktura/ . MTS Cloud says it uses its own/protected Minsk datacenter infrastructure; the about page states 78 racks, and newer news pages state services are based on two datacenters. Directory references to pr. Nezavisimosti 95 should be treated as C until confirmed as a facility address rather than a corporate address.

```text
МТС Cloud дата-центр Минск
МТС Беларусь ЦОД
МТС Cloud "78 серверных стоек"
МТС Cloud "два дата-центра"
site:cloud.mts.by дата-центр
site:mts.by ЦОД
```

Grade: A for operator infrastructure/service claims; C for directory-only addresses.

### 5.5 Other Minsk hosting and colocation leads

- Datahata: https://www.datahata.by/ . Count as an operator service lead; verify building/site before final facility census.
- Serverspace.by: https://serverspace.by/ . Check whether the Belarus offering is a tenant footprint at beCloud RCOD; avoid double-counting.
- hoster.by, besthost.by, hostfly.by, bcr.by: service leads only unless an own datacenter, address, or colocation facility is explicitly supported.
- Belweb/Belhost and older brands: verify current operations before use.

```text
Datahata колокация Минск
Serverspace beCloud РЦОД
hoster.by дата-центр
besthost.by ЦОД
hostfly.by колокация
bcr.by дата-центр
```

### 5.6 IXP and connectivity

- BY-IX: search PeeringDB org 598 and the BY-IX domain. Use as interconnection evidence, not facility evidence.
- Overland transit: search Beltelecom international network/fiber gateway material for context only.

```text
BY-IX Минск PeeringDB
"точка обмена трафиком" Минск BY-IX
Белтелеком международные каналы связи
Беларусь транзитный магистральный кабель
```

### 5.7 Government, banking, and closed-sector leads

NTSEU state cloud is a verified state platform, but not a public colocation facility. National Bank, railway, ministry, and OAC/CII references may indicate closed IT infrastructure; do not count without facility-level official evidence.

```text
НЦЭУ облачное хранилище
НЦЭУ центр обработки данных
Нацбанк ЦОД Беларусь
БелЖД ЦОД
ОАЦ критическая информационная инфраструктура ЦОД
```

## 6. National Query Sweeps

English:

```text
"Belarus" "data center" Beltelecom beCloud A1 MTS
"Belarus" "data centre" Minsk colocation
"Minsk" "data center" "Tier III"
"Belarus" "AI data center"
"Belarus" hyperscale datacenter
"Belarus" "internet exchange" BY-IX
site:datacenterdynamics.com Belarus "data center"
```

Russian:

```text
"ЦОД" Беларусь "стойки"
"дата-центр" Минск Tier III
"центр обработки данных" Колодищи
"Республиканский центр обработки данных"
"ЦОД" "облачная платформа" Беларусь
"дата-центр" "ПВТ"
"дата-центр" "СЭЗ"
Белтелеком beCloud А1 МТС ЦОД
filetype:pdf ЦОД Беларусь строительство
```

Official cross-checks:

```text
site:egr.gov.by Белтелеком
site:egr.gov.by "Белорусские облачные технологии"
site:goszakupki.by ЦОД
site:goszakupki.by дата-центр
site:gse.by ЦОД
site:mpt.gov.by дата-центр
site:energo.by ЦОД
map.nca.by Колодищи Центральная 22
```

## 7. Division Discovery Strategy

Run all 7 divisions. Do not close a non-Minsk division solely because the market is Minsk-heavy.

### Minsk City and Minsk Oblast

```text
"Минск" "ЦОД" Белтелеком beCloud А1 МТС
"Колодищи" "Центральная 22" "РЦОД"
"Захарова 55" "ЦОД"
A1 Digital "дата-центр" Минск
МТС Cloud "дата-центр" Минск
site:tech.onliner.by "дата-центр" Минск
site:officelife.by РЦОД
site:comnews.ru Беларусь дата-центры
site:minsk.gov.by ЦОД
site:minsk-region.gov.by ЦОД
site:mrik.gov.by ЦОД
```

Expectation: all verified public commercial/operator anchors are in these two divisions. RCOD belongs to Minsk Oblast, not Minsk City.

### Brest, Gomel, Grodno, Mogilev, Vitebsk

For each oblast capital and FEZ:

```text
"{city}" "ЦОД"
"{city}" "дата-центр"
"{city}" "серверная"
"{city}" "колокация"
"{city}" Белтелеком "ЦОД"
"{FEZ name}" "дата-центр"
site:goszakupki.by "{city}" ЦОД
site:gse.by "{city}" ЦОД
site:{oblast-portal} ЦОД
```

Specific additions:

```text
"Островец" "ЦОД"
"БелАЭС" "дата-центр"
"Новополоцк" "дата-центр"
"Могилёв" "ЦОД"
```

Expectation: likely `no_projects` outside Minsk/Minsk Oblast unless regional Beltelecom or procurement evidence appears. Treat FEZ and NPP power narratives as siting leads only.

## 8. Evidence Handling

Status labels:

- `operational`: current operator page/release or reliable launch/commissioning press.
- `tenant/service footprint`: provider service running inside another facility, such as a cloud provider hosted at RCOD; do not double-count as a separate facility.
- `construction`: permit, state-expertise, contractor, procurement, or municipal evidence.
- `planned`: named project/site without construction proof.
- `siting lead`: FEZ, NPP, grid, or investment-promotion offer only.
- `unknown/historical`: old press or directory evidence without current corroboration.
- `not datacenter`: IXP-only, server room only, government IT unit, or generic cloud/software service.

Aliases:

```text
Beltelecom / РУП Белтелеком / ЦОД Белтелеком
beCloud / ООО Белорусские облачные технологии / РЦОД / RCOD / республиканская платформа
A1 / A1 Digital / А1 ИКТ сервисы / velcom
MTS Belarus / МТС Беларусь / МТС Cloud
NTSEU / НЦЭУ / Национальный центр электронных услуг
BY-IX / by-ix.net
Datahata / Датахата
HTP / ПВТ / Парк высоких технологий
Astravets NPP / БелАЭС / Островецкая АЭС
```

Common false positives:

- `ЦОД` used for an ordinary server room or internal data-processing department.
- Ministry/bank/enterprise information centres without hosting/colo/cloud/facility evidence.
- BY-IX, telecom POPs, and IP transit nodes without colocation/rack claims.
- Cloud MSP/reseller pages that run inside another operator facility.
- Crypto-mining or AI headlines without named operator, site, and construction/procurement evidence.
- FEZ and investment-map project ideas that are not active projects.

Recommended capture fields:

```text
name
division
city_or_settlement
raion
address_or_public_location
operator
legal_entity_aliases
UNP
status
capacity_mw
racks
white_space
power_connection_kv
tier_or_certification
source_urls
evidence_date
evidence_grade
official_verification_needed
notes
```

## 9. Update Cadence

- **Quarterly**: operator pages (datacenter.by, beltelecom.by, becloud.by, a1digital.by, cloud.mts.by, datahata.by); goszakupki.by and zakupki.butb.by sweeps; tech.onliner.by, BELTA, OfficeLife, ComNews searches.
- **Semi-annual**: full 7-division sweep; EGR lookups for known operators; directory cross-checks for changed addresses/aliases.
- **Annual**: PeeringDB/BY-IX status; Uptime certification status for RCOD/A1 claims; official AWS/Azure/GCP/OCI region pages; sanctions/regulatory review; FEZ/HTP project search.
- **Trigger events**: new digital-economy or personal-data law, NPP/grid programme, FEZ/HTP datacenter announcements, MTS/A1 ownership changes, or major procurement mentioning `ЦОД`, `дата-центр`, `серверная`, or `облачная платформа`.
