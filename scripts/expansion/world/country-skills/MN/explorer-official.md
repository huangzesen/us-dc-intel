# MN Explorer Official - Mongolia Datacenter Enumeration via Official, Regulatory, Cloud, and Power Sources

Date: 2026-08-11. Scope: methodology for enumerating data-center facilities and projects in Mongolia using official/regulatory records, cloud-region evidence, utility and construction approvals, operator pages, and strong trade press. Reliability grades: **A** = official/primary source; **B** = strong secondary or operator/trade source; **C** = weak aggregator/social/promotional source; **U** = searched but unverified/no project found.

---

## 0. Country-Specific Frame

- Mongolia is a small data-center market. Current known facility evidence is concentrated in **Ulaanbaatar**, with a meaningful secondary lead in **Darkhan-Uul / Darkhan** and a planned smart-city / renewable-powered data-center policy lead in **Tov aimag** near New Zuunmod / Hunnu City.
- Do not confuse **Mongolia (MN)** with **Inner Mongolia, China**. English search must exclude `Inner Mongolia`, `Hohhot`, `Ulanqab`, `Wulanchabu`, and Chinese province/city domains unless intentionally investigating cross-border context.
- The best official route is not a single national data-center registry. Build records from four independent tracks:
  1. construction / land / planning permits,
  2. electricity / grid / renewable-energy approvals,
  3. CRC telecom licensing, standards, ISP/network sources,
  4. operator, certification, and cloud/CDN footprint sources.
- Mongolian search terms matter. Use both Cyrillic and English:
  - `дата төв` = data center
  - `өгөгдлийн төв` = data/records center; can include generic information centers
  - `серверийн өрөө`, `сервер түрээс`, `зогсуур түрээс` = server room, server rental, rack rental
  - `үүлэн үйлчилгээ`, `клауд`, `хостинг`, `колокэйшн`, `сервер байршуулах` = cloud, hosting, colocation
  - `барилгын зөвшөөрөл`, `газрын зөвшөөрөл`, `техникийн нөхцөл`, `зураг төсөл` = construction permit, land permit, technical conditions, design
  - `эрчим хүч`, `дэд станц`, `цахилгаан хангамж`, `сэргээгдэх эрчим хүч` = energy, substation, power supply, renewable power

---

## 1. Grade-A Backbone: Official and Regulatory Sources

### 1.1 Communications Regulatory Commission of Mongolia (CRC / ХХЗХ)

Primary URLs:
- CRC main site: https://crc.gov.mn/ and English/admin mirror: https://admin.crc.gov.mn/
- CRC e-licensing platform link appears in CRC navigation as `customer.crc.gov.mn`.
- CRC statistics portal link appears as `statistic.crc.gov.mn`.
- CRC licensing summary: https://crc.gov.mn/licensing-under-mongolia
- CRC internet/network service section: https://admin.crc.gov.mn/list/internetijn-s-lzhee-jlchilgee/en
- CRC statistics page: https://www.crc.gov.mn/zax-zeel-une-tarif/statistik-data-2
- CRC data-center telecom infrastructure standard notice: https://admin.crc.gov.mn/articles/slug10228/en

Use CRC as an **operator/network lead source**, not a facility census. The CRC site exposes licensing, regulation, statistics, standards, and an e-licensing entry point. Its site navigation includes "Information communication network and services", "Licensing", "Obtaining new license", "Report form of license holders", and "Electronic licensing platform"; these are the tabs to inspect for licensed ISPs, telecom networks, IXP/internet interconnection, data services, and any license-holder lists.

Important source fact: CRC reported that Mongolia adopted a national standard for "Дата төвийн цахилгаан холбооны дэд бүтэц" (data-center telecommunications infrastructure) in 2015, developed with CRC involvement and based on ANSI/TIA-942 concepts. Use this for standards context and as a keyword seed (`MNS 6528`, `Дата төвийн цахилгаан холбооны дэд бүтэц`, `TIA-942`) when searching design/certification documents.

Queries:
```
site:crc.gov.mn "дата төв"
site:crc.gov.mn "MNS 6528" OR "Дата төвийн цахилгаан холбооны дэд бүтэц"
site:crc.gov.mn "интернэтийн үйлчилгээ" "тусгай зөвшөөрөл"
site:crc.gov.mn "тусгай зөвшөөрөл" ("хостинг" OR "дата төв" OR "сервер")
site:statistic.crc.gov.mn ("интернэт" OR "ISP" OR "суурин өргөн зурвас")
site:customer.crc.gov.mn ("интернэт" OR "харилцаа холбоо" OR "тусгай зөвшөөрөл")
```

Reliability: **A** for regulatory existence, license status, standards, and sector statistics; **B** for facility inference from a telecom/ISP license alone. A CRC license proves a company can operate telecom/internet services, not that it owns a data-center building.

### 1.2 Construction, Land, and Planning Permits

Primary URLs:
- Construction sector integrated system: https://mcis.gov.mn/
- Ministry of Urban Development, Construction and Housing: https://mcud.gov.mn/
- LegalInfo English Construction Law: https://legalinfo.mn/en/edtl/16532502207681
- Ulaanbaatar city portal: https://ulaanbaatar.mn/
- Ulaanbaatar land/urban agencies: search within `gazar.ub.gov.mn`, `uda.ub.gov.mn`, and city subdomains if live.
- Aimag/capital official websites: use the official `.gov.mn` pages for governor's office, land affairs, construction/urban-development department, and procurement/tender notices.

LegalInfo's English Construction Law is useful for evidence routing: it defines construction work permits, technical conditions for electricity/communications/utilities, and states that design drawings/topographical maps of buildings and facilities should be public. For a real data center, look for land decision, technical conditions, design approval, construction work permit, commissioning certificate, and utility connection documents.

Core Mongolian queries:
```
"дата төв" "барилгын зөвшөөрөл"
"дата төв" "газрын зөвшөөрөл"
"дата төв" "техникийн нөхцөл"
"дата төв" "зураг төсөл"
"серверийн өрөө" "барилгын зөвшөөрөл"
"зогсуур түрээс" "Улаанбаатар"
site:ulaanbaatar.mn "дата төв" ("захирамж" OR "барилга" OR "газар")
site:gazar.ub.gov.mn "дата төв"
site:mcis.gov.mn "дата төв"
site:mcud.gov.mn "дата төв"
```

English queries:
```
"Mongolia" "data center" "construction permit" -"Inner Mongolia"
"Ulaanbaatar" "data center" "building permit"
"Mongolia" "data centre" "technical conditions"
"Mongolia" "TIA-942" "data center"
```

Reliability: **A** for construction/land/commissioning records from government portals; **B** for planning studies or official speeches; **C** for investor-promotion material without permit identifiers.

### 1.3 Environmental and Energy Approvals

Primary URLs:
- Ministry of Energy: https://energy.gov.mn/
- Energy Regulatory Commission: https://erc.gov.mn/
- National Dispatching Center / grid context: search official pages for `Диспетчерийн үндэсний төв`.
- Ministry of Environment / EIA law and records: use LegalInfo EIA Law at https://legalinfo.mn/en/edtl/16230948947641 and search environment ministry/domain sources for project-specific EIA notices.
- Government procurement: https://www.tender.gov.mn/ and `shilendans.gov.mn` for state-budget spending.

Mongolia has acute power-system constraints, so large data-center projects should leave power evidence. Search for new substations, high-voltage connection, direct renewable PPAs, and "green data center" language. Energy Ministry posts in 2026 discussed data centers as an energy-demand and renewable-powered development topic; treat these as policy leads, not facility records, until tied to a named site.

Queries:
```
site:energy.gov.mn "дата төв"
site:energy.gov.mn "дата төв" "сэргээгдэх эрчим хүч"
site:erc.gov.mn "дата төв"
site:erc.gov.mn ("цахилгаан" OR "тусгай зөвшөөрөл") ("дата төв" OR "сервер")
"дата төв" "дэд станц" Монгол
"дата төв" "цахилгаан хангамж" Монгол
"дата төв" "нар" "салхи" Монгол
"data center" "renewable energy" Mongolia -"Inner Mongolia"
site:tender.gov.mn "дата төв" ("цахилгаан" OR "сервер" OR "барилга")
site:shilendans.gov.mn "дата төв"
```

Reliability: **A** for energy licenses, grid-connection approvals, PPAs/tenders, and environmental approvals; **B** for ministry policy posts and development-bank studies; **C** for articles that only say Mongolia has favorable climate/renewables.

### 1.4 Government Digital Infrastructure

Primary seed:
- Mongolian National Data Center: https://datacenter.gov.mn/ and https://datacenter.gov.mn/en/about-us

The National Data Center (MNDC) is the state facility/operator seed. Its official English page says MNDC was established by Government Resolution No. 183 on June 24, 2009, funded by government, and responsible for the national electronic data system. It also lists services such as web hosting, virtual servers, rack rental (`Зогсуур түрээс`), `gov.mn` domains, and government information security.

Queries:
```
site:datacenter.gov.mn ("өргөтгөл" OR "шинэчлэл" OR "тоног төхөөрөмж" OR "зогсуур")
"Үндэсний Дата Төв" "өргөтгөл"
"Үндэсний Дата Төв" "барилга"
"National Data Center" Mongolia "rack rental"
site:tender.gov.mn "Үндэсний Дата Төв" ("сервер" OR "цахилгаан" OR "өргөтгөл")
```

Reliability: **A** for MNDC official history/service pages and procurement notices; **B** for UN/World Bank summaries; **C** for social posts unless linked to procurement or official budgets.

---

## 2. Cloud, CDN, Certification, and Operator Sources

### 2.1 Hyperscale Cloud Regions

As of the official pages checked on 2026-08-11, AWS, Microsoft Azure, Google Cloud, and OCI do **not** publish a Mongolia cloud region. Use their official global infrastructure/location pages only to confirm absence and avoid double-counting edge/CDN POPs as full regions:

- AWS global infrastructure: https://aws.amazon.com/about-aws/global-infrastructure/ and https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones
- Oracle Cloud regions: https://www.oracle.com/cloud/public-cloud-regions/

Expected finding: Mongolia workloads are served from nearby Asia regions, not an in-country public-cloud region. Count only an official "Mongolia" or "Ulaanbaatar" region/zone/Local Zone if the provider page explicitly lists it.

### 2.2 CDN / Edge POPs

Cloudflare is the strongest public edge-cloud source. Its official blog announced **Ulaanbaatar, Mongolia** as city 154 on the Cloudflare network and said it had a data center in Ulaanbaatar. This is **A** for Cloudflare edge presence and **B** for physical facility inference because the host data-center operator is not named.

Queries:
```
site:blog.cloudflare.com Mongolia Ulaanbaatar "data center"
site:cloudflare.com Mongolia Ulaanbaatar network
"Akamai" Ulaanbaatar Mongolia "data center"
"Fastly" Ulaanbaatar Mongolia POP
"Google Global Cache" Mongolia ISP
"Meta" "Mongolia" cache "data center"
```

### 2.3 Certification Sources

Primary:
- Uptime Institute country awards page for Mongolia: https://uptimeinstitute.com/uptime-institute-awards/country/id/MN

Uptime's Mongolia list is a high-value facility seed. It lists certified facilities for Bank of Mongolia / NETC, Khan Bank, and XacBank in Ulaanbaatar, including Tier II and Tier III certifications. Use this as **A** for facility existence and certification status, but it does not provide MW or all market facilities.

Queries:
```
site:uptimeinstitute.com Mongolia "Data Center"
"Mongolia" "Tier III" "data centre"
"Монгол" "Tier III" "дата төв"
"TIA-942" "Mongolia" "data center"
"MNS 6528" "дата төв" "Улаанбаатар"
```

### 2.4 Local Operators and Colo Players

Seed operators to sweep:

| Operator / entity | Useful source | Notes | Grade |
|---|---|---|---|
| Mongolian National Data Center (MNDC) | https://datacenter.gov.mn/ | Government data center, `gov.mn`, hosting, virtual server, rack-rental services. | A |
| Mobicom Networks / Mobinet | https://en.mobicomnetworks.mn/service-7 and https://mobinet.mn/datacenter | Official page says data-center services include server hosting and rack rental and comply with Tier II / Tier III standards. Search Ulaanbaatar and Darkhan. | A/B |
| Unitel Group | https://www.unitel.mn/ and Data Center Map/DCD | Listed by data-center aggregators/trade press as Ulaanbaatar colocation; official site is broad telecom service, so verify by direct Unitel DC page or permit/tender. | B |
| S Systems / Shunkhlai Holding | https://www.sg.mn/en/business-sector/technology/0/ and http://www.ssystems.mn/ | Shunkhlai official page says it launched Mongolia's largest data-center project and established S Systems Data Center in 2022. | A/B |
| ICT Group JSC | Haskoning project page | Haskoning says ICT Group was opening a Tier III-standard facility in 2022 and already operated two data centers. Verify current operating status separately. | B |
| Khan Bank / XacBank / Bank of Mongolia NETC | Uptime Institute + bank official pages | Enterprise/banking DCs are important facility records but usually not retail colo. | A |
| Datacom, Gemnet, Mogul Service, Univision, Skymedia, ONDO, G-Mobile, Skytel | official company pages, CRC license, aggregators | Use as ISP/telecom seeds; confirm facility ownership before counting. | B/C |

Operator queries:
```
"Mobicom" OR "Mobinet" "дата төв"
"Мобиком" "дата төв" "Дархан"
"Unitel" "data center" Mongolia
"Юнител" "дата төв"
"S Systems" "data center" Mongolia
"Шунхлай" "дата төв"
"ICT Group" "Tier III" Mongolia "data centre"
"Khan Bank" "data center" "Ulaanbaatar"
"XacBank" "data center" "Ulaanbaatar"
"Bank of Mongolia" "NETC" "data center"
"Gemnet" "дата төв" OR "сервер"
"Mogul" "data center" "Ulaanbaatar"
```

---

## 3. Per-Division Enumeration Strategy

The manifest divisions are Mongolia's aimags plus the capital city: Orhon, Darhan uul, Hentiy, Hovsgol, Hovd, Uvs, Tov, Selenge, Suhbaatar, Omnogovi, Ovorhangay, Dzavhan, Dundgovi, Dornod, Dornogovi, Govi-Sumber, Govi-Altay, Bulgan, Bayanhongor, Bayan-Olgiy, Arhangay, Ulaanbaatar.

Use these exact division spellings for result output, but search with common English and Mongolian spellings.

### 3.1 Ulaanbaatar - Highest Priority

Known concentration: national government DC, bank DCs, telco/colo providers, CDN edge, and most ISP headquarters.

Search domains:
- `ulaanbaatar.mn`
- `gazar.ub.gov.mn`, `uda.ub.gov.mn`, and other city-agency subdomains
- `datacenter.gov.mn`
- CRC, Uptime, operator sites

Queries:
```
"Улаанбаатар" "дата төв"
"Ulaanbaatar" "data center" -"Inner Mongolia"
"Улаанбаатар" "серверийн өрөө" "зогсуур"
site:ulaanbaatar.mn "дата төв" ("захирамж" OR "барилга" OR "газар" OR "өргөтгөл")
site:gazar.ub.gov.mn "дата төв"
site:tender.gov.mn "Улаанбаатар" "дата төв"
site:tender.gov.mn "Үндэсний Дата Төв"
```

Verification emphasis: facility address/district, operator official page, Uptime/certification, procurement for UPS/generator/cooling, land/construction approvals.

### 3.2 Darhan uul / Darkhan-Uul - Secondary Priority

Darkhan has evidence of a geographically redundant Mobinet/Mobicom facility and is the main non-capital location to check. Official local site: https://darkhan.gov.mn/

Queries:
```
"Дархан" "дата төв"
"Дархан-Уул" "дата төв"
"Darkhan" "data center" Mongolia -"Inner Mongolia"
"Mobinet" "Darkhan" "data center"
site:darkhan.gov.mn "дата төв"
site:darkhan.gov.mn "Мобинет"
site:tender.gov.mn "Дархан" "дата төв"
site:energy.gov.mn "Дархан" ("дата төв" OR "дэд станц")
```

Reliability: **B** from trade/aggregator until matched to Mobicom/Mobinet official page, CRC license, local permit, or Uptime/TIA evidence.

### 3.3 Tov - Hunnu City / New Zuunmod Watchlist

Tov is important because the Hunnu City / New Zuunmod smart-city concept near the new airport is being discussed as a possible renewable/geothermal-powered data-center zone. Official local site: https://tov.gov.mn/

Queries:
```
"Төв аймаг" "дата төв"
"Хүннү хот" "дата төв"
"Шинэ Зуунмод" "дата төв"
"Сэргэлэн" "дата төв"
"Алтанбулаг" "дата төв"
"Hunnu City" "data center" Mongolia
"New Zuunmod" "data center"
site:tov.gov.mn "дата төв"
site:energy.gov.mn ("Хүннү хот" OR "Шинэ Зуунмод") ("эрчим хүч" OR "дата төв")
site:tender.gov.mn ("Хүннү хот" OR "Шинэ Зуунмод") ("дата төв" OR "цахилгаан")
```

Do not count Hunnu City as a facility unless a named site has permit/power/construction evidence. Current evidence is **B/C policy-pipeline** unless official project documents identify a developer, parcel, MW, or construction stage.

### 3.4 Orhon / Erdenet, Selenge, and Northern Industrial Corridor

These provinces have population, rail, industrial load, and cooler climate advantages, so they are plausible future edge/DR sites. Search Orhon with Erdenet; Selenge with Sukhbaatar, Zuunharaa, and border/rail terms.

Official sites discovered/seeded:
- Orhon/Erdenet: `erdenet.mn`
- Selenge: https://selenge.gov.mn/

Queries:
```
"Орхон" "дата төв"
"Эрдэнэт" "дата төв"
"Erdenet" "data center" Mongolia
site:erdenet.mn "дата төв"
"Сэлэнгэ" "дата төв"
"Сүхбаатар сум" "дата төв" "Сэлэнгэ"
"Зүүнхараа" "дата төв"
site:selenge.gov.mn "дата төв"
site:energy.gov.mn ("Эрдэнэт" OR "Сэлэнгэ" OR "Сүхбаатар") ("дэд станц" OR "цахилгаан")
```

### 3.5 Gobi / Renewable-Power Provinces: Omnogovi, Dornogovi, Dundgovi, Govi-Sumber, Govi-Altay

These are not current facility clusters, but they are the strongest long-term renewable-power and industrial-corridor candidates. Search for data-center investment promotion, renewable-energy auctions, SEZ/free-zone projects, substations, and mining-adjacent private networks.

Queries:
```
"Өмнөговь" "дата төв"
"Дорноговь" "дата төв"
"Дундговь" "дата төв"
"Говьсүмбэр" "дата төв"
"Говь-Алтай" "дата төв"
"Сайншанд" "дата төв"
"Замын-Үүд" "дата төв"
("Omnogovi" OR "Dornogovi" OR "Dundgovi") "data center" Mongolia
site:energy.gov.mn ("Өмнөговь" OR "Дорноговь" OR "Дундговь") "сэргээгдэх" "дата төв"
site:tender.gov.mn ("Өмнөговь" OR "Дорноговь" OR "Говьсүмбэр") ("сервер" OR "дата төв" OR "цахилгаан")
```

### 3.6 Remaining Aimags - Low Probability / Exhaustive Sweep

For Hentiy, Hovsgol, Hovd, Uvs, Suhbaatar, Ovorhangay, Dzavhan, Dornod, Bulgan, Bayanhongor, Bayan-Olgiy, and Arhangay, default expectation is **no large data-center projects** unless tied to a government digital-service room, bank/telecom DR site, or regional smart-city/renewable project.

Use this pattern for each:
```
"{Mongolian aimag name}" "дата төв"
"{Mongolian aimag name}" "сервер"
"{Mongolian aimag name}" "үүлэн үйлчилгээ"
"{English aimag name}" "data center" Mongolia -"Inner Mongolia"
site:{official-aimag-domain} "дата төв"
site:tender.gov.mn "{Mongolian aimag name}" ("дата төв" OR "сервер" OR "сүлжээ")
site:energy.gov.mn "{Mongolian aimag name}" ("дэд станц" OR "цахилгаан")
```

Name variants to include:

| Manifest division | Search names |
|---|---|
| Hentiy | Хэнтий, Khentii, Hentiy, Chinggis city |
| Hovsgol | Хөвсгөл, Khuvsgul, Khovsgol, Murun |
| Hovd | Ховд, Khovd |
| Uvs | Увс, Uvs, Ulaangom |
| Suhbaatar | Сүхбаатар аймаг, Sukhbaatar aimag, Baruun-Urt |
| Ovorhangay | Өвөрхангай, Uvurkhangai, Arvaikheer |
| Dzavhan | Завхан, Zavkhan, Uliastai |
| Dornod | Дорнод, Dornod, Choibalsan |
| Bulgan | Булган, Bulgan |
| Bayanhongor | Баянхонгор, Bayankhongor |
| Bayan-Olgiy | Баян-Өлгий, Bayan-Ulgii, Olgii |
| Arhangay | Архангай, Arkhangai, Tsetserleg |

---

## 4. Trade Press and Secondary Sources

Use these after official source sweeps, and always backfill with permit/operator evidence:

- Data Center Dynamics: strong English-language coverage of Mongolia's small market and sovereign-wealth-fund / Hunnu City pipeline. Example: https://www.datacenterdynamics.com/en/news/mongolias-sovereign-wealth-fund-looks-to-bring-in-data-center-development/
- The Tech Capital: useful for investment-development pipeline, often paywalled. Example search result title: "Mongolia lines up renewables-powered data centres under new sovereign fund".
- Data Center Map / Datacenters.com / Baxtel / RackCorp / ColocationM: useful facility/operator seeds, but treat as **B/C** unless an operator or official source confirms. These can surface S Systems, Mogul, Gemnet, Unitel, Mobinet, and MNDC.
- Mongolian local press: `ikon.mn`, `montsame.mn`, `news.mn`, `gogo.mn`, `itoim.mn`, `unread.today`. Use for launch/opening events, especially `Мобинет Дархан дата төв` and operator announcements. Grade **B** when the article identifies operator, place, and event date.
- Official Facebook pages for agencies/operators are common in Mongolia. Use only as **B/C**, but they can lead to formal tenders or decisions.

Queries:
```
site:datacenterdynamics.com Mongolia "data center"
site:thetechcapital.com Mongolia "data centre"
site:ikon.mn "дата төв" "Мобинет"
site:montsame.mn "дата төв"
site:news.mn "дата төв" "Улаанбаатар"
site:gogo.mn "дата төв"
site:datacentermap.com/mongolia Ulaanbaatar
site:baxtel.com "Ulaanbaatar" "data center"
```

---

## 5. Evidence and Status Rules

### 5.1 Evidence Hierarchy

1. **A - direct official/primary**: construction permit, land decision, commissioning certificate, EIA/energy/grid approval, CRC license-holder record, MNDC official page, Uptime Institute certification, operator official facility page, bank/central-bank official announcement.
2. **A-/B+ - strong operator/engineering evidence**: engineering consultant case study, named Tier/TIA design statement, audited bank or corporate report.
3. **B - strong secondary**: DCD, The Tech Capital, MONTsame, Ikon, Data Center Map, Datacenters.com, Baxtel, RackCorp when specific and current.
4. **C - weak**: generic "Mongolia wants data centers", social posts, investor-promotion pages with no parcel/developer/power details, SEO colocation pages.

### 5.2 Status Mapping

- `planned`: official strategy, investment promotion, smart-city plan, MOU, or fund pitch; no permit/construction.
- `permitted`: land/construction/energy/EIA approval with named site/developer, but no construction evidence.
- `construction`: groundbreaking, EPC tender award, construction contract, or visible construction progress.
- `operational`: operator page offering services at the facility, commissioning, Uptime Constructed Facility certification, government/bank announcement of live services, or credible facility listing confirmed by another source.
- `unknown`: strong evidence of a facility/project but no current operating status.

### 5.3 Capacity Rules

- Mongolia sources rarely publish IT MW. Do not infer MW from "Tier II/III" or rack-rental marketing.
- If a source gives total building area only, store area in notes, not `capacity_mw`.
- If power is available from grid connection/substation/tender, record as utility capacity in notes unless clearly stated as IT load.
- For government IT rooms and bank DCs, avoid counting as commercial colo unless public colocation/rack rental is explicitly offered.

### 5.4 De-Duplication Rules

- Ulaanbaatar operator aliases are common: Mobicom Networks, Mobinet, Newcom/Newcomm, and MobiCom may point to related facilities; resolve by address and facility name.
- Unitel / Univision / MCS Group references may describe telecom network services rather than data-center sites.
- Bank facilities may be primary, backup, technical center, and NETC records. Keep them separate only when Uptime or the bank lists distinct facility names/locations.
- Cloudflare Ulaanbaatar is an edge deployment inside an unnamed host facility; do not create a separate wholesale facility unless the host is identified.
- Exclude all Chinese Inner Mongolia projects unless the country code is CN.

---

## 6. Recommended Official/Regulatory Pipeline

1. **Seed Ulaanbaatar from primary lists**: MNDC official page, Uptime Mongolia awards, Mobicom/Mobinet official pages, S Systems official/Shunkhlai page, Cloudflare Ulaanbaatar blog, bank official pages.
2. **CRC operator sweep**: use CRC licensing/e-licensing/statistics to enumerate ISPs, network operators, hosting/domain providers; pivot each into `дата төв`, `сервер`, `зогсуур түрээс`, and `байршуулах` searches.
3. **Construction and land sweep**: search Ulaanbaatar city/land portals and `mcis.gov.mn` / `mcud.gov.mn` for permits, design approvals, land decisions, and commissioning. Repeat for Darkhan-Uul, Tov, Orhon, and Selenge.
4. **Energy sweep**: search Energy Ministry, ERC, National Dispatching Center, tender.gov.mn, and Shilendans for power feeds, substations, UPS/generator/cooling procurement, and renewable-powered DC pipeline.
5. **Cloud/CDN confirmation**: confirm no public-cloud region via AWS/Azure/GCP/OCI official region pages; record CDN/edge POPs separately when official.
6. **Trade press backfill**: use DCD, The Tech Capital, MONTsame, Ikon, Data Center Map, Datacenters.com, Baxtel, and RackCorp only to find leads; upgrade evidence through official/operator/permit sources.
7. **Division completion**: for each manifest aimag, run Mongolian + English queries and mark `no_projects=true` only after checking official aimag site, `tender.gov.mn`, `energy.gov.mn`, and at least one web/news query.

Practical pitfalls:
- `MN` search results are polluted by U.S. Minnesota (`MN`) and China's Inner Mongolia. Always add `Mongolia` / `Монгол` and exclude `"Inner Mongolia"`.
- A "data center" in Mongolian government text can mean a municipal information office or call center. Require server/rack/power/cooling/cloud/colocation context.
- Social posts often announce national ambition. Count a project only after a named developer, site, permit, procurement, or operator page appears.
- Mongolia's official material often uses Facebook and PDF attachments; search both web and document indexes.
