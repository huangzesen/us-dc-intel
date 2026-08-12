# BG Explorer — Official / Regulatory / Cloud Pipeline for Bulgaria Datacenter Enumeration

Date: 2026-08-11. Scope: how to enumerate Bulgaria datacenter projects using official, regulatory, energy, cloud, colo/operator, procurement, and trade-press sources. Reliability grades: **A** = official/primary registry, permit, regulator, operator page, cloud provider page, or legally accountable filing; **B** = strong secondary/trade press or association/source quoting a named party; **C** = weak aggregator, marketplace listing, unsourced local article, or stale facility directory.

---

## 0. Bulgaria-specific structure

- Bulgaria is a **municipal-permit country** for datacenter construction. The important planning documents are normally held by the municipality / chief architect (`главен архитект`) rather than one national planning portal. The same project can appear as `център за данни`, `дейта център`, `data center`, `информационен център`, `изчислителен център`, `сървърно помещение`, `колокационен център`, or under a telecom/industrial building title.
- Sofia is the primary market. The best official municipal register is Sofia Municipality's Architecture and Urban Planning portal (NAG): https://nag.sofia.bg/pages/render/187. It links searchable registers for building permits, infrastructure permits, commissioning certificates, design visas, urban-planning orders, and change-of-use permits. Start every Sofia search there.
- For non-Sofia provinces, there is no consistent national building-permit search UI. Each municipality publishes `Разрешения за строеж`, `Съобщения по чл.149 ЗУТ`, `Устройство на територията`, or file registers on its own website, many on `*.egov.bg`.
- Large datacenters leave stronger evidence in **grid connection, EIA, procurement, land, and telecom/operator records** than in generic building-permit statistics.
- Bulgaria has 28 NUTS3 administrative districts / provinces. NSI confirms 28 administrative districts and 265 municipalities as of 2025: https://www.nsi.bg/en/press-release/administrative-territorial-and-territorial-division-of-the-republic-of-bulgaria-2025-9010. Work province -> municipality -> permit/EIA/grid/operator.

---

## 1. Core Bulgarian vocabulary and query templates

Use both English and Bulgarian. Cyrillic queries usually find permits and local-government pages; English finds operator and trade-press pages.

### 1.1 Facility/project terms

```
"център за данни"
"дейта център"
"дата център"
"data center" OR "data centre"
"колокационен център" OR "колокация"
"сървърно помещение"
"изчислителен център"
"облачен център" OR "облачна инфраструктура"
"резервен център за данни"
"авариен център за данни"
"център за възстановяване при бедствия"
"HPC" OR "суперкомпютър" OR "изкуствен интелект" "център за данни"
```

### 1.2 Planning / construction status terms

```
"разрешение за строеж" "център за данни" "{province_or_city}"
"съобщение" "чл.149" "ЗУТ" "център за данни"
"виза за проектиране" "център за данни"
"подробен устройствен план" OR "ПУП" "център за данни"
"одобрен инвестиционен проект" "дейта център"
"удостоверение за въвеждане в експлоатация" "център за данни"
"Акт 16" "дейта център"
"промяна на предназначението" "сървърно"
```

### 1.3 Energy / grid / EIA terms

```
"присъединяване" "център за данни" "ЕСО"
"искана мощност" "център за данни"
"подстанция" "център за данни"
"110 kV" "дейта център"
"ОВОС" "център за данни"
"инвестиционно предложение" "център за данни"
"РИОСВ" "дейта център"
"решение за преценяване" "център за данни"
```

### 1.4 Procurement / public-sector IT terms

```
site:app.eop.bg "център за данни"
site:app.eop.bg "Data център"
site:app.eop.bg "резервен център за данни"
site:app.eop.bg "непрекъснато ел. захранване" "център за данни"
site:app.eop.bg "колокация" "център за данни"
```

### 1.5 Operator discovery terms

```
"колокация" "{city}" "България"
"data center" "{city}" Bulgaria colocation
"дейта център" "{city}" "ISO 27001"
"Tier III" "София" "дейта център"
"carrier neutral" Sofia Bulgaria data center
```

---

## 2. Official / regulatory source stack

### 2.1 Construction permits and commissioning

**Sofia Municipality NAG registers — Grade A**

- Register landing page: https://nag.sofia.bg/pages/render/187.
- Key registers: building permits (`Разрешения за строеж`), infrastructure permits (`Разрешения за строеж на благоустройствени обекти`), commissioning certificates (`Удостоверения за въвеждане в експлоатация`), design visas (`Визи за проектиране`), change of use (`Разрешения за промяна на предназначението`), and urban-planning orders.
- Commissioning register direct page observed: https://nag.sofia.bg/RegisterCertificateForExploitationBuildings.
- Sofia publishes administrative acts after issuance / entry into force. NAG stated that its building-permit register included tens of thousands of records and that its registers support search/export/map linkage: https://nag.sofia.bg/Pages/SinglePublication/RjeS6BaVwnY%3D and https://nag.sofia.bg/Pages/SinglePublication/eU_nm6OM4KA%3D.
- Use for: exact address, district, cadastral identifier (`идентификатор КККР`), permit/commissioning number, issuer, beneficiary/owner, and status.

**Other municipalities — Grade A when on official municipal domain**

- Pattern: search `{municipality} "Разрешения за строеж"` or `{municipality}.egov.bg "център за данни"`.
- Many municipal notices cite Art. 149 of the Spatial Development Act (`чл.149 ЗУТ`) and are posted as individual pages. Example of an official municipal building-permit notice format: https://tutrakan.egov.bg/TUTRAKAN/home.nsf/pages/bg/NT00016286?OpenDocument=.
- Use the chief architect issuing authority and appeal/entry-into-force language to separate draft notices from effective permits.

**Legal process reference — Grade B**

- CMS summarizes Bulgarian datacenter consenting steps: investment design to local municipality, construction permit from the chief architect, grid connection contract, then use permit after construction: https://cms.law/en/int/expert-guides/cms-expert-guide-on-real-estate-data-centre-consenting/bulgaria.
- Treat as process guidance only; verify every facility in municipal records.

### 2.2 Environment / EIA

**MOEW public EIA registers — Grade A**

- Bulgarian page: https://www.moew.government.bg/bg/prevantivna-dejnost/ovos/publichni-registri-po-ovos/.
- English page: https://www.moew.government.bg/en/prevention/eia/public-registers-eia/.
- MOEW says the centralized public EIA register gives access to data and documents for investment proposals handled by MOEW and the 16 Regional Inspectorates of Environment and Water (`РИОСВ`), including current and completed procedures and decisions.
- Query all terms: `център за данни`, `дейта център`, `data center`, `сървърно помещение`, `подстанция`, `дизелов генератор`, plus operator/SPV names.
- EIA documents are good for parcel location, diesel-generator counts, cooling/water systems, power supply description, and whether the project was screened out or required full EIA.

**Regional RIEW / РИОСВ sites — Grade A**

- If the MOEW central search is weak, search per regional inspectorate: `site:riosv-{city}.com "център за данни"` or `site:riosv*.bg "инвестиционно предложение" "дейта център"`.
- Priority RIEWs by datacenter likelihood: Sofia, Pernik/Sofia-region, Plovdiv, Stara Zagora, Burgas, Varna, Ruse, Shumen, Haskovo.

### 2.3 Energy / grid

**ESO EAD — transmission grid operator, Grade A**

- Main site: https://www.eso.bg/ and English overview: https://www.eso.bg/?en=.
- ESO states it operates and maintains Bulgaria's transmission network and controls the Bulgarian power system. Use this as the transmission-grid source.
- Connection pages: https://www.eso.bg/doc/?joining= and https://www.eso.bg/doc?joining-request=.
- ESO connection access can require registration/e-signature, so public evidence may be partial. Still search ESO pages and PDF plans for substation upgrades, customer connection requests, and 110/220/400 kV works.
- Ten-year transmission development plans (`План за развитие на електропреносната мрежа`) are useful for regional capacity and named substation upgrades: example plan page/PDF surfaced at https://www.eso.bg/fileObj.php?oid=5010.

**Distribution operators — Grade A/B depending on public notice detail**

- Sofia/west Bulgaria: Electrohold / ERM West (formerly CEZ distribution). Search: `site:ermzapad.bg "център за данни"` and `site:electrohold.bg "присъединяване"`.
- North-east Bulgaria: Energo-Pro. Search: `site:energo-pro.bg "център за данни"`.
- South-east Bulgaria: EVN Bulgaria. Search: `site:evn.bg "център за данни"`.
- For medium-sized colos, distribution-grid connection notices may be more relevant than ESO.

**Energy regulator EWRC / КЕВР — Grade A for energy licenses, weaker for facility discovery**

- Site: https://www.ewrc.bg/.
- Use for electricity market/license context, complaints, tariff decisions, and named network disputes. Most datacenters will not have EWRC licenses unless paired with generation/storage/trading.

### 2.4 Telecom regulator / operator universe

**Communications Regulation Commission (CRC / КРС) — Grade A**

- Main site: https://www.crc.bg/.
- English page on public electronic communications notification: https://crc.bg/en/articles/2203/notification-of-public-electronic-communications-networks-and-services.
- CRC is the Bulgarian communications regulator. It maintains public registers of undertakings that notify intent to provide public electronic communications networks/services. This is an **operator-side registry**, not a facility registry.
- Use CRC to seed Bulgarian network/ISP/telecom names, then pivot each undertaking into municipal permits, EIA, official colo pages, and procurement.
- Queries:
  ```
  site:crc.bg "Регистър" "предприятия" "електронни съобщителни"
  site:crc.bg "Нетерра" OR "Нетера" OR "Telepoint" OR "Виваком" OR "A1" OR "Еволинк"
  site:crc.bg "годишен отчет" "пренос на данни" "достъп до интернет"
  ```

### 2.5 Public procurement

**Public Procurement Agency / CAIS EOP — Grade A for contracts**

- Public Procurement Agency: https://www2.aop.bg/en/home/.
- CAIS EOP register: https://app.eop.bg/.
- AOP describes the Public Procurement Portal as a centralized information system updated daily. Use it for government datacenter upgrades, power/cooling works, colocation services, disaster-recovery services, and telecom tenders.
- Example result language: `Изграждане и осигуряване на непрекъснато ел. захранване за Център за данни (Data център)` appears in CAIS EOP result pages. Treat procurement as facility evidence only when it names a physical site or required hosting territory.

### 2.6 Corporate, land, cadastre

- Commercial Register / Registry Agency: https://portal.registryagency.bg/ and company reports page https://portal.registryagency.bg/CR/reports. **Grade A** for legal entity identity, UIC/EIK, filings, ownership, and annual statements.
- BULSTAT: https://www.bulstat.bg/. **Grade A** for entity identifiers when not in the commercial register.
- Cadastre / cadastral identifiers usually appear in NAG/municipal permits. Use cadastral identifier (`идентификатор`) to join municipal permits, EIA notices, and satellite/site mapping. Public map access may be constrained; prefer official permit text when available.

---

## 3. Cloud and edge region official pages

Use official cloud pages as **presence signals**, not as physical-campus disclosure. As of this research pass, Bulgaria is primarily an edge/colo/interconnection market rather than a named AWS/Azure/GCP public cloud region.

| Provider | Bulgaria signal | Source / query | Grade | Enumeration use |
|---|---:|---|---|---|
| AWS | No named Bulgaria AWS Region found; nearest official Local Zone signals include Athens/Istanbul/Warsaw, not Sofia in search results | AWS Regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/; Local Zones: https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ | A for absence/presence on official list | Search for Direct Connect partners and on-ramps in Sofia colos rather than AWS campus. |
| Microsoft Azure | No Azure public cloud region in Bulgaria found in official regions list; Azure Front Door lists Sofia as an edge POP | Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list; Azure Front Door edge POPs include Sofia: https://learn.microsoft.com/en-us/azure/frontdoor/edge-locations-by-region | A | Edge POP/on-ramp, not a hyperscale datacenter region. Pivot to Equinix/Digital Realty/Telepoint connectivity claims. |
| Google Cloud | No Bulgaria cloud region expected; verify against official locations page before each refresh | https://cloud.google.com/about/locations | A | Absence check; search for Cloud CDN/edge only. |
| Oracle Cloud | Search results did not verify a Sofia OCI region; official Oracle public cloud regions page should be checked for live list | https://www.oracle.com/cloud/public-cloud-regions/ | A | Confirm absence/presence. Do not infer a physical facility from Oracle Sofia office pages. |
| Cloudflare / Akamai / CDN edge | Sofia POPs may appear on vendor network maps and PeeringDB | Official network maps per vendor; PeeringDB facility/IX records | A/B | Edge presence helps identify interconnection facilities but is not a datacenter project by itself. |

Cloud query templates:

```
site:aws.amazon.com "Sofia" "Local Zone"
site:learn.microsoft.com "Sofia, Bulgaria" "Azure"
site:cloud.google.com "Sofia" "Bulgaria" "locations"
site:oracle.com "Sofia" "cloud region"
"Sofia" "cloud on-ramp" "data center"
"София" "cloud on-ramp" "дейта център"
```

---

## 4. Major colo / datacenter operators to seed

Operator official pages are **A for existence and location when operator-owned**, **B for capacity unless independently confirmed by permit/EIA/grid/filing**.

| Operator / brand | Facilities and source | Notes |
|---|---|---|
| **Equinix Bulgaria** | Sofia overview: https://www.equinix.com/data-centers/europe-colocation/bulgaria-colocation/sofia-data-centers; SO1: https://www.equinix.com/data-centers/europe-colocation/bulgaria-colocation/sofia-data-centers/so1; SO2: https://www.equinix.com/data-centers/europe-colocation/bulgaria-colocation/sofia-data-centers/so2 | Equinix lists SO1 and SO2 in Sofia, with SO1 address in Druzhba-1 and SO2 at Nedelcho Bonchev. Use NAG permits/commissioning to validate expansions. |
| **Digital Realty / Telepoint** | Digital Realty official acquisition release: https://investor.digitalrealty.com/news-releases/news-release-details/digital-realty-enters-bulgaria-acquisition-highly-connected; Telepoint: https://telepoint.bg/ and contacts: https://telepoint.bg/contacts | Digital Realty entered Bulgaria in 2026 via Telepoint; release says two Sofia datacenters, one highly interconnected with 110+ network service providers and cloud on-ramps. Telepoint also lists Sofia Center, Sofia East, and Montana contact/location signals; reconcile with acquisition wording. |
| **Neterra / Sofia Data Center (SDC)** | https://sdc.bg/ and Bulgarian page https://sdc.bg/bg | SDC says Neterra operates four datacenters: SDC 1, SDC 2, SDC Stolnik, SDC Ruse. DCD reported SDC 2 opened in Sofia in 2022 with 2 MW / 1,400 sqm: https://www.datacenterdynamics.com/en/news/neterra-launches-data-center-in-sofia-bulgaria/. |
| **Evolink** | Colocation overview: https://www.evolink.com/services/colocation; Sofia 1: https://www.evolink.com/services/colocation/evolink-datacenter-sofia-1; Sofia 2: https://www.evolink.com/services/colocation/evolink-datacenter-sofia-2 | Evolink lists Sofia datacenter services and site capacities in sqm. Use Sofia NAG and operator pages for facility-level records. |
| **Daticum** | https://daticum.com/en/data-centre/ | Daticum lists a Sofia datacenter at 135 Tsarigradsko Shose Blvd. Cross-check against NAG and owner entity. |
| **Vivacom / Bulgarian Telecommunications Company** | https://www.vivacom.bg/ | Incumbent telco. Official public facility pages are less transparent; use CRC, procurement, annual reports, and facility directories as leads, then verify. Search `Виваком център за данни`, `BTC data center`, `Kaspichan`, `София дата център`. |
| **A1 Bulgaria** | https://www.a1.bg/ | Major telecom/cloud provider. Search official pages and CAIS EOP for `A1 център за данни`, `A1 cloud`, `колокация`. |
| **ITD Network, Networx, S3, ESCOM, EXA/Interoute/GTT assets** | Operator pages and PeeringDB / facility directories as leads | Regional colos may appear in Ruse, Haskovo, Shumen/Varna, and Sofia. Treat directories as C until official page or permit confirms. |

Aggregator backfill (C unless verified): DataCenterMap Bulgaria/Sofia, Baxtel, Cloudscene, DC Atlas, DataCenterPlatform. They are useful for missed operator names, aliases, addresses, and live/claimed MW, but do not count a new facility from them alone.

---

## 5. Trade press and business press

Use trade press for change detection and project announcements; upgrade evidence only after official confirmation.

| Source | URL | Grade | Use |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/ | B | Good for Neterra SDC 2 opening, Digital Realty/Telepoint acquisition, hyperscale news. |
| SeeNews | https://seenews.com/ | B | Balkan business news; useful for investments, telco transactions, energy/grid projects. |
| Capital.bg / Dnevnik | https://www.capital.bg/ and https://www.dnevnik.bg/ | B | Bulgarian business/local policy context; often names investors and municipal issues. |
| Investor.bg / Money.bg / News.bg | https://www.investor.bg/, https://money.bg/, https://news.bg/ | B/C | Leads for AI/datacenter political announcements; verify against permits. |
| BTA / BNR | https://www.bta.bg/ and https://bnr.bg/ | B | Official-ish newswire/radio; good for government statements. BNR/BTA reported 2026 political claims of three datacenter agreements, but treat as C until named investors/permits appear. |
| Company press rooms | Equinix, Digital Realty, Telepoint, Neterra, Evolink, Daticum | A/B | A for self-owned facility existence; B for marketing capacity claims. |

Trade-press queries:

```
site:datacenterdynamics.com Bulgaria "data center"
site:seenews.com Bulgaria "data centre" OR "data center"
site:capital.bg "дейта център" OR "център за данни"
site:bnr.bg "център за данни" "България"
"Bulgaria" "AI data center" "Sofia"
"България" "AI" "център за данни"
```

---

## 6. Per-province enumeration matrix

For every province, run the baseline. Add the priority notes below.

Baseline per province `{oblast}` and administrative center `{city}`:

1. Municipal permits: `"{city}" "разрешения за строеж" "център за данни"`; `site:{municipality_domain} "дейта център"`; `"{city}" "чл.149" "ЗУТ" "център за данни"`.
2. EIA: `site:moew.government.bg "{oblast}" "център за данни"`; `site:riosv* "{city}" "инвестиционно предложение" "дейта център"`.
3. Grid: `site:eso.bg "{city}" "присъединяване"` plus `"подстанция" "{city}" "център за данни"`.
4. Operators: `"{city}" "колокация"` and `"{city}" "data center" Bulgaria`.
5. Procurement: `site:app.eop.bg "{city}" "център за данни"` and `site:app.eop.bg "{oblast}" "резервен център за данни"`.
6. Company register pivot: any SPV/operator name -> Registry Agency -> ownership/UIC -> repeat permit/EIA search with exact Bulgarian company name.

| Province / district | Bulgarian name | Priority and local approach |
|---|---|---|
| Blagoevgrad | Благоевград | Border/education/business services market, but low known colo density. Search Blagoevgrad municipality permits, RIEW Blagoevgrad, Southwest University/HPC procurements, and industrial-zone announcements. |
| Burgas | Бургас | Black Sea cable/port/industrial demand. Search Burgas municipality, RIEW Burgas, port/industrial-zone power works, `Бургас "колокация"`, and disaster-recovery procurements. |
| Dobrich | Добрич | Lower priority; search municipality permits and Energo-Pro/grid notices. Watch wind/renewables co-location claims but require permits. |
| Gabrovo | Габрово | Lower priority; technical university/public IT tenders may mention server rooms rather than true DCs. Use CAIS EOP and municipal registers. |
| Haskovo | Хасково | Regional colo leads (ESCOM/Haskovo in aggregators). Verify through Haskovo municipal permits, RIEW Haskovo, CRC/operator records, and official operator page. |
| Kardzhali | Кърджали | Low priority; search RIEW Haskovo/Kardzhali jurisdiction, municipal permits, and telecom operator expansions. |
| Kyustendil | Кюстендил | Low priority; search cross-border fiber/industrial power and municipal permits. |
| Lovech | Ловеч | Low priority; use baseline. |
| Montana | Монтана | Medium because Telepoint lists a Montana datacenter/location. Search Telepoint official pages, Montana municipality permits, RIEW Montana, `бул. Трети Март 78`, and CRC/company filings. |
| Pazardzhik | Пазарджик | Medium as Plovdiv-adjacent industrial/logistics market. Search municipal permits, RIEW Pazardzhik, substations, and `Тракия икономическа зона` spillover. |
| Pernik | Перник | Medium/high as Sofia spillover with cheaper land/power. Search Pernik municipality, RIEW Sofia/Pernik, ESO substation works, and `София област` operator expansions. |
| Pleven | Плевен | Low/medium; search municipal permit pages and public-sector backup-center procurement. |
| Plovdiv | Пловдив | High non-Sofia priority: major city, industrial zones, 6 urban districts. Search Plovdiv municipality permits, RIEW Plovdiv, Trakia Economic Zone, EVN grid works, and cloud/colo marketing. |
| Razgrad | Разград | Low priority; use baseline plus industrial park power works. |
| Ruse | Русе | Medium/high: SDC Ruse / Neterra signal and Danube fiber route. Search `SDC Русе`, Ruse municipality permits, RIEW Ruse, Networx/Ruse operators, and cross-border Romania connectivity. |
| Shumen | Шумен | Medium because Kaspichan/Vivacom-style leads often fall in Shumen province. Search Kaspichan municipality, Shumen/RIEW Varna-Shumen, Energo-Pro, `Каспичан "център за данни"`, `Мадарски конник`. |
| Silistra | Силистра | Low priority; use municipal `egov.bg` building-permit notices and RIEW Ruse/Silistra. |
| Sliven | Сливен | Low/medium; industrial power and telecom nodes. Use baseline. |
| Smolyan | Смолян | Low priority; use baseline, public-sector IT/server-room procurements. |
| Sofia City | София-град / Столична община | Highest priority. Use NAG registers first, then operator pages for Equinix SO1/SO2, Digital Realty/Telepoint Sofia Center/East, Neterra SDC 1/2, Evolink Sofia 1/2, Daticum, Vivacom/A1. Search by address, cadastral ID, and district (`Дружба`, `Младост`, `Овча купел`, `Искър`, `Слатина`). |
| Sofia Province | Софийска област | High spillover. Key terms: Stolnik/Столник, Bozhurishte/Божурище, Elin Pelin/Елин Пелин, Kostinbrod/Костинброд, Ihtiman/Ихтиман. Search municipality permits and ESO 110 kV substations. Neterra SDC Stolnik is a required seed. |
| Stara Zagora | Стара Загора | Medium/high for power availability and industrial brownfield. Search Maritsa energy complex, ESO/EVN substations, RIEW Stara Zagora, and AI/datacenter investment announcements. |
| Targovishte | Търговище | Low priority; use baseline. |
| Varna | Варна | High coastal/IX/fiber market. Search Varna municipality, RIEW Varna, port/cable landing references, `Варна "колокация"`, and Energo-Pro grid works. Watch aggregator claims for Vivacom/Kaspichan but bucket by real municipality/province. |
| Veliko Tarnovo | Велико Търново | Low/medium; central location and public-sector DR potential. Use baseline. |
| Vidin | Видин | Low/medium; Danube/cross-border fiber. Search municipal permits and ESO substations. |
| Vratsa | Враца | Low/medium; energy/industrial potential. Use baseline plus nuclear/energy-area data links only if facility-specific. |
| Yambol | Ямбол | Low priority; use baseline. |

---

## 7. Recommended enumeration workflow

1. **Seed known operators and facilities**: Equinix SO1/SO2, Digital Realty/Telepoint Sofia Center/East, Neterra SDC 1/2/Stolnik/Ruse, Evolink Sofia 1/2, Daticum Sofia, Vivacom/A1 official datacenter/cloud offerings, ITD/Networx/ESCOM regional leads.
2. **Sofia official verification**: for each Sofia seed, search NAG building permits, infrastructure permits, design visas, and commissioning certificates by operator, street, district, and cadastral identifier.
3. **Sofia spillover sweep**: Sofia Province and Pernik with `Столник`, `Божурище`, `Елин Пелин`, `Костинброд`, `Перник`, `подстанция`, `110 kV`, and operator names.
4. **EIA sweep**: MOEW public EIA register + RIEW pages for every seed and every province query. Capture decisions, screening outcomes, diesel-generator/cooling details, and exact site.
5. **Grid sweep**: ESO connection/ten-year plan and distribution operator notices. Use substation names to find hidden projects where the permit title is generic industrial/warehouse.
6. **CRC operator expansion**: build the telecom/ISP universe from CRC public undertaking records and annual report material; pivot each undertaking into facility and permit searches.
7. **Procurement backfill**: CAIS EOP for public-sector datacenters, colocation contracts, power/cooling upgrades, and disaster-recovery sites. Do not count a government server-room procurement as a commercial datacenter unless the scope/location supports it.
8. **Trade press delta watch**: DCD, SeeNews, Capital/Dnevnik, BTA/BNR, company press rooms. Promote leads only after permit/EIA/operator-page confirmation.
9. **Deduplicate by site**: match on address/cadastral ID/substation/operator graph. Bulgarian facilities are often marketed under brand name, legal entity, street address, and telecom-node name separately.

---

## 8. Evidence grading rules for Bulgaria

| Evidence item | Grade | How to use |
|---|---|---|
| Municipal building permit / infrastructure permit / commissioning certificate from NAG or official municipality | A | Confirms legal construction/commissioning stage, site, beneficiary, permit number. |
| MOEW/RIEW EIA register decision or investment proposal | A | Confirms project description, environmental stage, location, generators/cooling/power details. |
| ESO or distribution operator connection document / named substation work | A | Confirms power-path evidence; may not prove datacenter use unless project/customer named. |
| CRC public electronic communications undertaking register | A | Confirms operator/provider status, not facility existence. |
| CAIS EOP public procurement notice/contract | A | Confirms public project or purchased service; only facility-grade if physical hosting/construction site is named. |
| Registry Agency / BULSTAT | A | Confirms legal identity/UIC/ownership; use to join SPVs. |
| Official operator datacenter page | A for existence/location, B for capacity | Good seed; capacity is marketing unless permit/grid/EIA confirms. |
| Official cloud provider region/edge page | A | Region/edge presence only; usually not a site-level disclosure. |
| DCD / SeeNews / Capital / BTA / BNR | B | Good leads and transaction/status evidence; verify with official source. |
| DataCenterMap / Baxtel / Cloudscene / DC Atlas / DataCenterPlatform | C | Lead source only; verify each facility elsewhere. |

Status vocabulary:

- `виза за проектиране`, `ПУП`, `инвестиционно предложение` = early planning.
- `разрешение за строеж` = permitted construction, not necessarily started.
- `откриване на строителна площадка`, `започва строителство`, `първа копка` = construction start.
- `Акт 15`, `Акт 16`, `удостоверение за въвеждане в експлоатация` = commissioning / operational readiness.
- `открит`, `в експлоатация`, `работещ`, `operational` = operational; still verify with commissioning/operator page.

Pitfalls:

- `център за данни` in Bulgarian public procurement often means an enterprise/server room inside an office building, not a commercial colocation facility.
- `дата център` is common informal spelling; include it despite being less formal.
- Sofia and Sofia Province are separate provinces. `SDC Stolnik` is in Sofia Province, not Sofia City.
- Facility directories may misplace Kaspichan/Varna/Sofia addresses. Always re-bucket by official municipality/cadastral address.
- A cloud edge POP or network on-ramp is not a hyperscale region. Record it as interconnection evidence unless a physical datacenter operator/site is named.
