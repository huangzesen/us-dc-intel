# BY Explorer Official - Belarus Datacenter Enumeration

Date: 2026-08-12. Scope: Belarus (BY), all 7 divisions used by `world-manifest.jsonl`: Brest; Gomel; Grodno; Minsk; Minsk City; Mogilev; Vitebsk.

Purpose: enumerate datacenter facilities and projects from official, regulatory, municipal, energy, register, procurement, and operator-primary sources. Use this file for final verification; use `explorer-industry.md` for broader lead generation.

Review status: final methodology pass completed with live URL and search verification in August 2026. Facts are graded by the source that supports the specific fact, not by the general reputation of the entity.

## 0. Belarus Structure Facts And Caveats

Belarus has 6 oblasts (Brest, Gomel, Grodno, Mogilev, Minsk, Vitebsk) plus Minsk City, which has special status at the same administrative rank as an oblast. Required division coverage is therefore exactly: Brest; Gomel; Grodno; Minsk; Minsk City; Mogilev; Vitebsk.

Practical searches must be done below the division level. Construction permissions, land decisions, utility connections, and public notices normally surface through oblast executive committees and city/district executive committees rather than a national construction-permit portal.

Important absences:

- No public Belarus datacenter registry was found.
- No national open construction-permit database was found.
- No official public-cloud infrastructure page for AWS, Microsoft Azure, Google Cloud, or Oracle Cloud lists a Belarus region or local zone as of this review.
- Belarus is landlocked; submarine cable landing-station searches are false positives. Use overland fiber and IXP queries for connectivity context only.

False-positive rules:

- `ЦОД` / `центр обработки данных` may describe a server room, ministry IT unit, bank processing office, or software platform. Count only where facility, hosting, colocation, cloud infrastructure, telecom infrastructure, HPC, or construction evidence is explicit.
- Telecom POPs, exchange points, and BY-IX entries are not datacenters without colocated rack/hosting/facility claims.
- FEZ land/power offers, NPP power narratives, and investment-map entries are siting leads only until tied to a named operator and site.
- Do not infer undisclosed state/security facilities from regulator references or critical-information-infrastructure rules.

## 1. Reliability Grades

Grades apply to the fact supported by the cited source.

- **A**: official government, regulator, register, procurement, municipal, cadastre, operator-owned facility/project/service page, operator press release, or official public-cloud infrastructure page.
- **B**: established business/trade/construction press, PeeringDB/interconnection evidence, company annual/project reports, industry-association material.
- **C**: directories, aggregators, social media, procurement monitors that are not the official portal, unsourced market reports, or promotional capacity claims not tied to a named project.
- **U**: unresolved lead. Do not use as final evidence until confirmed or rejected.

Examples:

- A1 Digital's own page is Grade A for the fact that A1 markets/operates a Tier III-class data center service; it is not independent proof of Uptime certification currency.
- beCloud's contacts/regulations pages are Grade A for RCOD location at Kolodishchi, Tsentralnaya 22. Trade articles about area or certification are Grade B unless the certificate itself is retrieved.
- A directory address is Grade C until corroborated by an operator, register, cadastre, or municipal/procurement record.

## 2. Official And Primary Source Inventory

### 2.1 Legal and regulatory sources

- National Legal Internet Portal: https://pravo.by/ . Use exact regnum/guid links when possible.
- Personal data law: Law of 07.05.2021 No. 99-Z, `О защите персональных данных`: https://pravo.by/document/?guid=12551&p0=H12100099 . Pravo.by notes the law entered into force on 15.11.2021 in its public explainer: https://pravo.by/novosti/novosti-pravo-by/2022/november/72150/ . Grade A.
- Data protection authority: National Centre for Personal Data Protection (NCPDP / НЦЗПД): https://cpd.by/ . Grade A. Do not use `pdp.by` as an assumed authority domain.
- Telecom law: Law of 19.07.2005 No. 45-Z, `Об электросвязи`: https://pravo.by/document/?guid=3961&p0=H10500045 . Grade A. Note: the draft reference to No. 429-Z was wrong; No. 429-Z is not the telecom law.
- Information law: Law of 10.11.2008 No. 455-Z, `Об информации, информатизации и защите информации`: https://etalonline.by/document/?regnum=h10800455 and Pravo search views under `H10800455`. Grade A.
- Digital economy decree: Presidential Decree No. 8 of 21.12.2017, `О развитии цифровой экономики`: https://pravo.by/document/?guid=12551&p0=Pd1700008 . Grade A.
- HTP founding decree: Presidential Decree No. 12 of 22.09.2005, `О Парке высоких технологий`: https://pravo.by/document/?guid=3871&p0=Pd0500012 . Grade A.
- Public procurement law: Law of 13.07.2012 No. 419-Z, `О государственных закупках товаров (работ, услуг)`: use Pravo/Etalon search if needed; procurement evidence should come from the active portal below.
- State programme `Цифровое развитие Беларуси` 2021-2025: https://www.mpt.gov.by/ru/gosudarstvennaya-programma-cifrovoe-razvitie-belarusi-na-2021-2025-gody . Grade A for programme content.
- State programme `Цифровая Беларусь` 2026-2030: https://www.mpt.gov.by/ru/gosprogramma-cifrovaya-belarus-na-2026-2030-gody-kak-budet-formirovatsya-ekosistema-cifrovykh . Grade A for programme content.

### 2.2 ICT, cybersecurity, and state IT bodies

- Ministry of Communications and Informatization: https://www.mpt.gov.by/ . Grade A.
- BelGIE / РУП `БелГИЭ`: https://belgie.by/ru/ ; contacts confirm it is subordinate to Minsvyazi: https://belgie.by/ru/contacts/ . Grade A for telecom oversight/equipment and information-system-registration context; not a facility registry.
- Operational and Analytical Centre under the President (OAC): https://www.oac.gov.by/ . Grade A for information-security regulation; not a facility registry.
- National Centre for Electronic Services (NTSEU / НЦЭУ): https://nces.by/ ; cloud storage service page: https://nces.by/oblachnoe_hranilishche/ . Grade A for state e-government/cloud services. Treat as a state platform, not public colocation, unless a facility page or procurement record says otherwise.
- beCloud / ООО `Белорусские облачные технологии`: https://becloud.by/ ; contacts: https://becloud.by/contacts/ ; RCOD access regulations: https://becloud.by/customers/regulations-rcod/ . Grade A for operator/platform/facility-location facts.

### 2.3 Operator-primary datacenter evidence

- Beltelecom datacenter: https://datacenter.by/ ; colocation page: https://datacenter.by/razmeshchenie-oborudovaniya ; hosting page: https://beltelecom.by/business/hosting . Grade A for Beltelecom service/facility offer. Historical and regional-address facts need separate evidence.
- beCloud RCOD: https://becloud.by/contacts/ and https://becloud.by/customers/regulations-rcod/ confirm the Republican Data Processing Centre at `Минский район, агрогородок Колодищи, ул. Центральная, 22`. Grade A.
- A1 Digital datacenter: https://a1digital.by/data-center/ and https://a1digital.by/services/colocation/ . Grade A for A1's own Tier III-class data-center/colocation service claims; exact physical address is not public on those pages.
- MTS Cloud: https://cloud.mts.by/ ; infrastructure article https://cloud.mts.by/support/articles/data-tsentr-i-oblachnaya-infrastruktura/ ; about page https://cloud.mts.by/company/about/ . Grade A for MTS Cloud service and own-infrastructure claims. The about page states a protected Minsk data center with 78 racks; newer MTS Cloud news states services use two data centers. Exact site addresses require stronger evidence.
- Datahata: https://www.datahata.by/ . Grade A for service claims; facility address and ownership require corroboration.

### 2.4 Registers, cadastre, planning, and procurement

- EGR legal entity register: https://egr.gov.by/ ; Ministry of Justice EGR page: https://minjust.gov.by/directions/unified_state_register/ . Grade A for legal-entity identity and registered addresses.
- National Cadastre Agency: https://nca.by/ ; public cadastral map: https://map.nca.by/ . Grade A for parcel/cadastre checks, but free public views may not identify a building as a datacenter.
- State construction expertise: https://gse.by/ ; personal cabinet https://mygse.by/ . Grade A when a project/finding is public; absence of search results is not absence of construction.
- Ministry of Architecture and Construction: https://www.masa.gov.by/ . Grade A for construction-sector regulation.
- Official procurement portal GIS `Госзакупки`: https://goszakupki.by/ ; all purchases: https://goszakupki.by/purchases/all . Grade A for public procurement notices and awards.
- BUTB procurement/trading platform: https://zakupki.butb.by/ . Grade A/B depending on procurement type and issuer.
- Commercial tender monitors: https://zakupki.by/ and https://tenders.by/ . Grade C lead-generation only.

### 2.5 Energy and siting context

- Ministry of Energy: https://minenergo.gov.by/ . Grade A.
- Belenergo: https://www.energo.by/ . Grade A.
- Regional power companies should be searched by official domain and operator name: Brestenergo, Vitebskenergo, Gomelenergo (`https://www.gomelenergo.by/` confirmed), Grodnoenergo, Minskenergo, Mogilevenergo.
- Belarusian NPP / Astravets NPP: https://www.belaes.by/ru/ . Grade A for power-generation context only; not datacenter evidence.

Energy query terms:

```text
технологическое присоединение ЦОД
присоединение к электросетям дата-центр
трансформаторная подстанция ЦОД
резервное питание ИБП дата-центр
дизельные генераторы ЦОД
10 кВ ЦОД
110 кВ ЦОД
330 кВ ЦОД
выделенная мощность дата-центр
```

### 2.6 Official division and municipal portals

Use these as required search surfaces for division closure:

| Division | Official portal surfaces | Notes |
|---|---|---|
| Brest | https://brest-region.gov.by/en/ ; Brest city https://city-brest.gov.by/en/ | Search oblast, Brest city, Brest district, and FEZ Brest. |
| Gomel | https://gomel-region.gov.by/en/ ; Gomel city https://gomel.gov.by/en/ | Gomel city `curl` may be slow; search indexing confirms the official city portal. Include FEZ Gomel-Raton. |
| Grodno | https://www.grodno-region.gov.by/ ; Grodno city https://grodno.gov.by/en/ | Include Ostrovets/Astravets NPP as power context only; FEZ Grodnoinvest as siting lead only. |
| Minsk | https://minsk-region.gov.by/ ; English mirror https://eng.minsk-region.gov.by/ ; Minsk district https://www.mrik.gov.by/en/ | RCOD is in Minsk district, Kolodishchi. Search district-level portals for Kolodishchi, Smolevichi, Logoysk leads. |
| Minsk City | https://minsk.gov.by/en/ | Capital portal returned transient 503 to `curl` during review, but official search result and mirrors confirm the surface. Highest expected yield. |
| Mogilev | https://mogilev-region.gov.by/ ; Mogilev city search surface `mogilev.gov.by` | Search oblast, city, and FEZ Mogilev. |
| Vitebsk | https://vitebsk-region.gov.by/en/ ; Vitebsk city search surface `vitebsk.gov.by` | Search oblast, city, Novopolotsk/FEZ Vitebsk when leads appear. |

### 2.7 Investment promotion and FEZ sources

- National Agency of Investment and Privatization: https://investinbelarus.by/ ; investment map/project database: https://map.investinbelarus.by/investbase/ . Grade A for official promotion of an offer; Grade C for uncommitted capacity/project claims.
- Hi-Tech Park: https://park.by/ ; Ministry of Economy HTP profile: https://economy.gov.by/ru/pvt-ru/ . Grade A for resident/status/program facts, not for facility existence unless a named datacenter project appears.
- FEZ administrations: Brest, Gomel-Raton, Grodnoinvest, Minsk, Mogilev, Vitebsk. Grade A for land/utility offers; siting lead only unless tied to a named datacenter project.

### 2.8 Official public-cloud region check

Re-check these official pages annually and after major cloud announcements:

- AWS Regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- AWS Local Zones: https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/
- Microsoft Azure global infrastructure: https://azure.microsoft.com/en-us/explore/global-infrastructure/
- Google Cloud locations: https://cloud.google.com/about/locations
- Google Compute regions/zones: https://cloud.google.com/compute/docs/regions-zones
- Oracle Cloud public regions: https://www.oracle.com/cloud/public-cloud-regions/

As of the August 2026 review, these official pages do not list a Belarus public region or local zone. This is Grade A evidence only for absence from public cloud-region lists; it does not prove absence of leased, network, CDN, reseller, or private enterprise presence.

## 3. Core Query Templates

Russian and Belarusian:

```text
"центр обработки данных" Беларусь
"ЦОД" Беларусь Минск
"дата-центр" Беларусь
"колокация" Минск
"размещение оборудования" "ЦОД" Беларусь
"серверная" "разрешение на строительство" Беларусь
"ЦОД" "госэкспертиза" Беларусь
"ЦОД" "трансформаторная подстанция"
"дата-центр" "дизельные генераторы"
"облачная платформа" Беларусь
"Республиканский центр обработки данных"
"точка обмена трафиком" Минск
"цэнтр апрацоўкі дадзеных"
"дата-цэнтр" Мінск
```

Official/procurement searches. Run separately; do not rely on a single `OR` line in search engines that ignore boolean syntax:

```text
site:goszakupki.by ЦОД
site:goszakupki.by дата-центр
site:goszakupki.by серверная
site:goszakupki.by облачная платформа
site:zakupki.butb.by ЦОД
site:gse.by ЦОД
site:gse.by дата-центр
site:mpt.gov.by ЦОД
site:belgie.by "государственная регистрация" "информационных систем"
filetype:pdf ЦОД строительство Беларусь
```

English:

```text
"Belarus" "data center"
"Belarus" "data centre"
"Minsk" "data center" "Tier III"
"Belarus" colocation operator
"Beltelecom" "data center"
"beCloud" "RCOD" Kolodishchi
"A1 Digital" "data center" Minsk
"MTS Cloud" "data center" Minsk
"Belarus" "internet exchange" BY-IX
"Belarus" "hyperscale" "data center"
```

## 4. Per-Division Enumeration Approach

A division can be marked `no_projects: true` only after checking the relevant official portal(s), goszakupki.by, gse.by, known operator pages, industry seeds in `explorer-industry.md`, and at least one Russian query sweep for the oblast/capital city name.

### Brest

Expected yield: low. No verified public commercial facility in Brest Oblast was found in this review. Historical/trade references to Beltelecom regional TsODs are leads only until a Brest-specific operator page, address, procurement, or municipal record is found.

```text
"Брест" "ЦОД"
"Брест" "дата-центр"
"Брест" "серверная"
"Брест" "колокация"
site:brest-region.gov.by ЦОД
site:city-brest.gov.by ЦОД
site:goszakupki.by Брест ЦОД
site:gse.by Брест ЦОД
"СЭЗ Брест" "дата-центр"
```

### Gomel

Expected yield: low. No verified public commercial facility in Gomel Oblast was found in this review. Treat FEZ Gomel-Raton and Beltelecom regional references as leads only.

```text
"Гомель" "ЦОД"
"Гомель" "дата-центр"
"Гомель" "серверная"
"Гомель" "колокация"
site:gomel-region.gov.by ЦОД
site:gomel.gov.by ЦОД
site:goszakupki.by Гомель ЦОД
site:gse.by Гомель ЦОД
"Гомель-Ратон" "дата-центр"
```

### Grodno

Expected yield: low. Astravets NPP in Grodno Oblast is important energy context but not datacenter evidence. No verified public commercial facility in Grodno Oblast was found in this review.

```text
"Гродно" "ЦОД"
"Гродно" "дата-центр"
"Гродно" "серверная"
"Гродно" "колокация"
"Островец" "ЦОД"
"БелАЭС" "дата-центр"
site:grodno-region.gov.by ЦОД
site:grodno.gov.by ЦОД
site:goszakupki.by Гродно ЦОД
site:gse.by Гродно ЦОД
"Гродноинвест" "дата-центр"
```

### Minsk

Expected yield: medium. One verified flagship facility is in Minsk Oblast: beCloud RCOD at Minsk district, Kolodishchi, Tsentralnaya 22. Search Minsk district and nearby industrial/FEZ areas for expansion or new siting leads.

```text
"Колодищи" "ЦОД"
"Колодищи" "дата-центр"
"Республиканский центр обработки данных" beCloud
"Минский район" "ЦОД"
"Минская область" "дата-центр"
"Смолевичи" "дата-центр"
"Логойск" "ЦОД"
site:minsk-region.gov.by ЦОД
site:mrik.gov.by ЦОД
site:goszakupki.by "Минский район" ЦОД
site:gse.by "Минский район" ЦОД
```

### Minsk City

Expected yield: highest. Verified current operator/service anchors include Beltelecom datacenter services, A1 Digital datacenter, MTS Cloud/MTS data-center infrastructure, NTSEU state cloud services, Datahata service claims, and BY-IX as an interconnection signal. Exact facility addresses are public only for some historical/state entries; do not invent addresses.

```text
"Минск" "ЦОД"
"Минск" "дата-центр"
"Минск" "колокация"
"Захарова 55" "Белтелеком"
"A1 Digital" "дата-центр" Минск
"МТС Cloud" "дата-центр" Минск
"НЦЭУ" "облачное хранилище"
"BY-IX" Минск
site:minsk.gov.by ЦОД
site:goszakupki.by Минск ЦОД
site:gse.by Минск ЦОД
```

### Mogilev

Expected yield: low. No verified public commercial facility in Mogilev Oblast was found in this review. Treat FEZ Mogilev and Beltelecom regional references as leads only.

```text
"Могилев" "ЦОД"
"Могилёв" "ЦОД"
"Могилев" "дата-центр"
"Могилев" "серверная"
"Могилев" "колокация"
site:mogilev-region.gov.by ЦОД
site:mogilev.gov.by ЦОД
site:goszakupki.by Могилев ЦОД
site:gse.by Могилев ЦОД
"СЭЗ Могилев" "дата-центр"
```

### Vitebsk

Expected yield: low. No verified public commercial facility in Vitebsk Oblast was found in this review. Search Novopolotsk/industrial zones when broader ICT or energy leads appear.

```text
"Витебск" "ЦОД"
"Витебск" "дата-центр"
"Витебск" "серверная"
"Витебск" "колокация"
"Новополоцк" "дата-центр"
site:vitebsk-region.gov.by ЦОД
site:vitebsk.gov.by ЦОД
site:goszakupki.by Витебск ЦОД
site:gse.by Витебск ЦОД
"СЭЗ Витебск" "дата-центр"
```

## 5. Known Facilities, Platforms, And Evidence Status

| Facility / project | Division / city | Evidence | Status | Existence grade |
|---|---|---|---|---|
| Beltelecom datacenter services | Minsk City primarily; possible regional network leads | https://datacenter.by/ ; https://datacenter.by/razmeshchenie-oborudovaniya ; https://beltelecom.by/business/hosting | operational service/facility offer | A for operator service; regional locations require corroboration |
| Beltelecom historical TsOD, Zakharova 55 | Minsk City | Onliner/trade historical reporting; search query `"Захарова 55" "Белтелеком" "ЦОД"` | historical/likely operational, but current facility status needs operator or municipal proof | B |
| beCloud Republican Data Processing Centre (RCOD) | Minsk Oblast, Minsk district, Kolodishchi | https://becloud.by/contacts/ ; https://becloud.by/customers/regulations-rcod/ | operational | A |
| beCloud national cloud / republican platform | Physical facility is RCOD; company HQ in Minsk City | https://becloud.by/ and current service rules on becloud.by | operational platform | A |
| A1 Digital data center | Minsk City | https://a1digital.by/data-center/ ; https://a1digital.by/services/colocation/ | operational | A for operator claim; independent certification/address evidence needed for those specific facts |
| MTS Cloud / MTS datacenter infrastructure | Minsk City for public claim; exact sites not public | https://cloud.mts.by/ ; https://cloud.mts.by/company/about/ ; https://cloud.mts.by/support/articles/data-tsentr-i-oblachnaya-infrastruktura/ | operational; MTS pages state own/protected Minsk DC and newer two-DC service base | A for operator claim; address C if sourced only from directories |
| NTSEU state cloud / e-government services | Minsk City | https://nces.by/ ; https://nces.by/oblachnoe_hranilishche/ | operational state platform, not commercial colo | A |
| Datahata colocation/hosting service | Minsk City lead | https://www.datahata.by/ | operational service claim | A for service; facility address needs corroboration |
| BY-IX | Minsk City | PeeringDB org 598 and BY-IX domain/search leads | operational IXP; not a datacenter | B for peering evidence |
| Astravets NPP | Grodno Oblast, Ostrovets district | https://www.belaes.by/ru/ | energy context only | A for NPP existence, not DC evidence |
| AWS/Azure/GCP/OCI public cloud regions | n/a | official global infrastructure pages in 2.8 | no Belarus public region/local zone listed | A for absence from official lists |

## 6. Record Fields And Status Rules

Recommended record fields:

```text
name
division
city_or_settlement
raion
address_or_public_location
operator
legal_entity
UNP
status
capacity_mw
racks
white_space
power_connection_kv
tier_or_certification
construction_evidence_url
operator_evidence_url
energy_evidence_url
register_evidence_url
evidence_date
evidence_grade
notes
```

Status labels:

- `operational`: current operator page/release or reliable press with launch/commissioning evidence.
- `tenant/service footprint`: branded environment inside another facility; do not double-count as a separate building.
- `construction`: permit, state-expertise, contractor, procurement, or municipal evidence with no launch yet.
- `planned`: named project/site without construction proof.
- `siting lead`: FEZ, NPP, grid, or investment-promotion offer only.
- `unknown/historical`: old press or directory lead without current corroboration.
- `not datacenter`: IXP-only, server room only, ministry IT office, or power/connectivity context only.

## 7. Update Cadence

- **Quarterly**: Beltelecom, beCloud, A1 Digital, MTS Cloud, Datahata, goszakupki.by, zakupki.butb.by, gse.by, and Minsvyazi news.
- **Semi-annual**: full 7-division sweep, including oblast/city portals and EGR lookups for known operators.
- **Annual**: cloud-region pages, PeeringDB country/BY-IX check, Uptime certification checks for RCOD/A1 claims, sanctions/regulatory review, FEZ/HTP project search.
- **Trigger events**: new digital-economy or personal-data laws, NPP/grid programme announcements, FEZ/HTP datacenter announcements, MTS/A1 ownership changes, public procurements mentioning `ЦОД`, `дата-центр`, `серверная`, or `облачная платформа`.
