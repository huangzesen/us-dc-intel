# KZ Explorer - Official / Regulatory / Cloud Pipeline for Kazakhstan Datacenter Enumeration

Date: 2026-08-12. Scope: methodology for discovering Kazakhstan datacenter projects from official, regulatory, energy, cloud-region, incumbent-operator, and trade-press sources. Reliability grades: **A** = official/primary source or operator legal disclosure; **B** = credible trade press / official-media interview / third-party certification directory; **C** = directories, maps, social posts, marketing pages without regulatory corroboration.

Kazakhstan has no single public planning-permit search that works like a US county portal or UK planning portal. The practical pipeline is: national digital-infrastructure policy + regional akimat/government news, construction/eGov systems, KEGOC/grid documents, operator annual reports, official cloud-region pages, and trade press. The strongest search languages are Russian and Kazakh; English works for flagship projects and investment promotion only.

---

## 1. National Official Backbone

### 1.1 Digital regulator / policy owner

- **Ministry of Artificial Intelligence and Digital Development** (`gov.kz/memleket/entities/maidd`) is the lead public source for cloud, AI infrastructure, telecom, and datacenter policy. It is the successor surface for the former Digital Development Ministry pages; also check the **Committee of Telecommunications** entity pages (`gov.kz/memleket/entities/telecom`).
- Important official pages:
  - Ministry home: https://www.gov.kz/memleket/entities/maidd?lang=en
  - Data Center Valley / Firebird / NVIDIA package: https://www.gov.kz/memleket/entities/maidd/press/news/details/1240802?lang=en
  - Data Center Valley / Aleria MOU: https://www.gov.kz/memleket/entities/maidd/press/news/details/1211917?lang=en
  - IDC-backed market snapshot: https://www.gov.kz/memleket/entities/maidd/press/news/details/1169498?lang=ru
  - 2026 telecom/datacenter infrastructure law: https://www.gov.kz/memleket/entities/maidd/press/news/details/1244531?lang=ru
- Enumeration value: **A for policy/project existence and stated government targets**, not for built capacity unless construction/commissioning is explicitly stated. The ministry says the 2025 commercial DC market reached **4,000 racks at 91% utilization** and that Data Center Valley in Ekibastuz has **300 MW available power with phased expansion to 1 GW**. Treat these as national benchmark figures, not facility-level inventory.

### 1.2 Prime Minister / President / Kazakh Invest

- Prime Minister: https://primeminister.kz/en/news
- President / Akorda: https://www.akorda.kz
- Kazakh Invest regional project pages: https://invest.gov.kz and regional mirrors such as `pavlodar.invest.gov.kz`, `abai.invest.gov.kz`, `ekr.invest.gov.kz`.
- Example official investment page for **AI HUB / Data Center Valley (Ekibastuz)**: https://abai.invest.gov.kz/doing-business-here/invest-projects/40348/
- Enumeration value: **A for signed agreements, government-priority status, region/site, strategic-object classification, and investment-promotion terms**; **B/C for future phase capacity** if no permit, grid connection, or construction evidence is attached.

### 1.3 Construction and permitting surfaces

Use these as project-verification channels rather than expecting an open national list of all permits.

- **eGov construction services**: https://egov.kz. Relevant service names include obtaining architectural-planning specifications and technical conditions (`архитектурно-планировочное задание`, `технические условия`) and building permit / commissioning services.
- **e-License**: https://elicense.kz. Useful for construction, telecom, and regulated activity licenses at company level.
- **Unified Construction Portal / Qportal**: referenced by government as `Qportal.kz`, integrating planning, expertise, and construction-monitoring systems.
- **e-Qurylys**: https://about.equrylys.kz/ and `equrylys.kz`; government and legal materials describe it as the construction-sector information system.
- **State Urban Planning Cadastre / AIS GGK**: https://gov.ggk.kz and https://aisggk.kz. It contains urban-planning cadastre/geospatial material, zoning, master-plan, and engineering-network context. It is useful for parcel/site confirmation, not a complete DC keyword registry.
- **Adilet legal database**: https://adilet.zan.kz. Use for Construction Code, telecom/datacenter law text, permit rules, and ministerial orders.
- Local authorities: each oblast/city has architecture, construction, land relations, energy, entrepreneurship/investment, and digitalization departments under `gov.kz/memleket/entities/<region>-...`.
- Query pattern:
  - `site:gov.kz "{region_ru}" "дата-центр" "строительство"`
  - `site:gov.kz "{city_ru}" "центр обработки данных" "разрешение"`
  - `site:gov.kz "{region_ru}" "архитектурно-планировочное задание" "ЦОД"`
  - `site:gov.kz "{region_ru}" "технические условия" "центр обработки данных"`
  - `site:gov.ggk.kz OR site:aisggk.kz "{city_ru}" "дата-центр"`

---

## 2. Energy / Grid Pipeline

Datacenter scale in Kazakhstan is power-led. Always verify whether claimed MW is IT load, grid connection, substation capacity, generation allocation, or future energy-reserve headline.

- **KEGOC** (system operator / national grid): https://www.kegoc.kz/en/
  - Grid access / technical conditions: https://www.kegoc.kz/en/electric-power/deyatelnost-kompanii/poryadok-dostupa-k-natsionalnoy-elektricheskoy-seti/
  - Kazakhstan electric power overview: https://www.kegoc.kz/en/electric-power/
  - Investment projects and press releases reveal transmission constraints, substations, North-South transit, West-zone integration, and southern-zone reinforcement.
- **Ministry of Energy**: https://www.gov.kz/memleket/entities/energo. Search ministry news for hyperscale DC power memoranda and long-term consumer/generation mechanisms.
- **Regional energy departments / natural monopoly utilities**: search the relevant akimat and distribution companies for grid-connection notices, substation upgrades, and land/power memoranda.
- Official policy signal: the 2026 telecom/datacenter law says datacenters will be treated as **strategic objects** and introduces a **70/30 mechanism** to attract private investment in generation expansion with digital miners and DC operators as long-term electricity consumers.
- Query pattern:
  - `site:kegoc.kz "data center" Kazakhstan`
  - `site:kegoc.kz "дата-центр" OR "центр обработки данных"`
  - `site:gov.kz "гипермасштабных центров обработки данных" "Министерство энергетики"`
  - `site:gov.kz "{region_ru}" "подстанция" "дата-центр"`
  - `"{project}" "МВт" "подстанция" "Экибастуз" OR "Павлодар"`
- Evidence rule: **A** for KEGOC/system-operator or ministry documents that name project, connection, substation, or MW. **B** for trade press quoting government or operator MW. **C** for marketing statements such as "cheap electricity" with no connection evidence.

---

## 3. Cloud Region / Hyperscaler Pipeline

### 3.1 Operational cloud-region checks

- **Yandex Cloud** is the only clearly documented active public-cloud region found in Kazakhstan:
  - Region docs: https://yandex.cloud/en/docs/overview/concepts/region
  - Launch blog: https://yandex.cloud/en/blog/posts/2024/04/yandex-cloud-in-kazakhstan
  - Region code: `kz1`, availability zone `kz1-a`; launch blog says the local data center is in **Karaganda**, with offices in **Almaty** and **Astana**. **Grade A** for active cloud region and Karaganda siting.
- **Google Cloud / AWS / Azure / OCI**:
  - Google locations: https://cloud.google.com/about/locations
  - AWS regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
  - Azure geographies: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/
  - Oracle regions: https://www.oracle.com/cloud/public-cloud-regions/
  - As of this research pass, their official global-region pages do **not** show a Kazakhstan public cloud region. Treat announcements about Google/AWS/Microsoft/Oracle interest or hosted infrastructure as **B leads** until confirmed on provider official region/location pages or by a signed local operator source.
- Local sovereign-cloud / hosted-cloud names to query: `Kazakhtelecom`, `Kazteleport`, `Freedom Telecom`, `Freedom Data Centers`, `PS Cloud Services`, `NLS Kazakhstan`, `Beeline Kazakhstan`, `VK Cloud`, `Yandex Cloud`, `Aitu Cloud`, `National Information Technologies`.

### 3.2 Cloud-region query templates

```
site:yandex.cloud Kazakhstan "kz1"
site:yandex.cloud "Karaganda" "data center"
site:cloud.google.com Kazakhstan "region"
site:aws.amazon.com Kazakhstan "Local Zone" OR "Wavelength"
site:azure.microsoft.com Kazakhstan "region" OR "sovereign cloud"
site:oracle.com Kazakhstan "cloud region"
"Kazakhstan" "Google Cloud" "data center" "Akashi"
"Kazakhstan" "sovereign cloud" "data center"
```

---

## 4. Operator / Colo Player Sweep

### 4.1 Incumbent and telecom operators

- **Kazakhtelecom JSC**: https://telecom.kz and B2B pages under https://b2b.telecom.kz. Annual reports are the best official source:
  - 2021 annual IT section: https://ar2021.telecom.kz/en/information-technology.html
  - 2022 annual IT section: https://ar2022.telecom.kz/ru/information-technology.html
  - 2021 says Kazakhtelecom had the country's largest network of **25 data centers**, about **1,500 racks**, 98% utilization, plus a **3.3 MW** modular DPC in Almaty and new 100-seat Kosshi/Akmola facility. 2022 says **27 data centers**, more than **1,600 racks**, 95-98% utilization, and 54% commercial DC market share. **Grade A for company footprint and disclosed counts; B for facility-specific attribution unless the report names the facility.**
- **Kazteleport JSC**: important Tier III operator in Almaty/Sairam and Ereymentau/Astana; cross-check with Uptime Institute award pages and DCD.
- **Transtelecom / TTC**: telecom/railway fiber operator; data-center listings exist in several regions. Verify via official TTC pages and tenders before counting.
- **National Information Technologies JSC (NIT)**: government IT/eGov infrastructure; likely owner/operator of state facilities. Public footprint may be incomplete for security reasons.
- **Beeline Kazakhstan / VEON**: sovereign AI/cloud DC announcements, especially Almaty/Hyper Cloud.

### 4.2 Private / hyperscale / hosting operators

- **AKASHI Data Center**: https://akashi.cloud. Astana Tier IV-focused campus; official page claims 4,224 racks and 100 MW IT capacity. Treat official page as **A-/B+** for design capacity; confirm construction/commissioning via Astana akimat, e-Qurylys/Qportal, grid, and Uptime Institute.
- **Enegix**: https://enegix.net/en. Ekibastuz/Pavlodar grid-powered campus; official site claims 150+50 MW. Important distinction: much legacy/crypto-server-farm capacity should be tagged separately if methodology distinguishes enterprise colo vs mining/HPC facilities.
- **Freedom Telecom / Freedom Data Centers**: Karaganda, Alatau/Almaty, and regional Freedom Cloud leads. Use operator pages, Uptime Institute, Yandex Cloud PoP/docs, and local permits.
- **PS Cloud Services / PS.kz**: https://www.ps.kz/en/about/data-center. Almaty data center network; official page has interconnect/peering details.
- **NLS Kazakhstan**, **Megakhost**, **Qazmin**, regional hosting operators: usually **C** from directories until official company pages, licenses, or permits are found.

Operator query templates:
```
site:telecom.kz OR site:b2b.telecom.kz "ЦОД" "{city_ru}"
site:ar202*.telecom.kz "дата-центров" "стоек"
site:kazteleport.kz "Data Center" OR "ЦОД"
site:uptimeinstitute.com "Kazakhstan" "Data Center"
site:ps.kz "data center" "Almaty"
site:veon.com "Beeline Kazakhstan" "data center"
site:akashi.cloud "MW" "Astana"
site:enegix.net "Ekibastuz" "MW"
```

---

## 5. Region-by-Region Enumeration Strategy

Use Kazakhstan's 17 regions plus 3 cities of republican significance. Search in Russian first, then Kazakh, then English. Russian terms usually produce the richest government and trade results.

Core terms:
- English: `data center`, `datacenter`, `cloud region`, `colocation`, `sovereign cloud`, `AI infrastructure`, `hyperscale`.
- Russian: `дата-центр`, `центр обработки данных`, `ЦОД`, `коммерческий ЦОД`, `облачная инфраструктура`, `суверенное облако`, `строительство ЦОД`, `стойки`, `мегаватт`, `подстанция`.
- Kazakh: `деректер орталығы`, `деректерді өңдеу орталығы`, `ДӨО`, `бұлттық инфрақұрылым`, `жасанды интеллект инфрақұрылымы`, `құрылыс`, `электр қуаты`.

| Division | Russian/Kazakh anchors | Official/regulatory focus | Operator/cloud focus |
|---|---|---|---|
| Astana | `Астана`, `Нұр-Сұлтан`, `Астана қаласы` | City akimat construction/land pages, MAIDD, telecom committee, NIT/gov cloud, Akashi permits | AKASHI, Kazakhtelecom Astana, Kazteleport Ereymentau/Astana, government DC |
| Almaty City | `Алматы қаласы`, `Алматы` | City architecture, Alatau SEZ/technopark, seismic/fire/building approvals | Kazakhtelecom modular DC, Kazteleport Sairam/Masanchi/Khan Tengri, PS.kz, Beeline/Hyper Cloud, Freedom |
| Shymkent | `Шымкент` | City akimat, industrial zones, Kazakhtelecom legacy IDC | Kazakhtelecom Shymkent, telecom/hosting directories |
| Pavlodar | `Павлодар`, `Экибастуз` | Highest priority. Data Center Valley, power/substations, Ministry of Energy, KEGOC, coal/generation, investment agreements | Data Center Valley, Kazakhtelecom, Enegix, Firebird/NVIDIA/Aleria leads |
| Karaganda | `Караганда`, `Қарағанды`, `Темиртау` | Industrial-zone and power searches, Yandex Cloud local-region evidence, Temirtau hyperscale proposals | Yandex Cloud `kz1`, Freedom Cloud Karaganda, GK Hyperscale/Temirtau leads |
| Akmola | `Акмолинская область`, `Ақмола`, `Косшы`, `Ерейментау`, `Акколь` | Astana-adjacent land/power, Kosshi/Akkol/Ereymentau permits | Kazteleport Ereymentau, Kazakhtelecom Kosshi/Akkol, GK Hyperscale near Astana |
| Almaty Region | `Алматинская область`, `Алатау`, `Қонаев` | Alatau special economic/technopark, land and grid near Almaty | Freedom Cloud Alatau, Beeline/Freedom overflow from Almaty metro |
| Abai | `Абайская область`, `Семей`, `Бахты` | Border/logistics investment proposals, Chinese investor MOUs | Proposed Chinese-backed DC near Bakhty; weak until permit/grid |
| Aktobe | `Актюбинская область`, `Актобе` | Industrial/energy projects and crypto-server-farm filters | Freedom/Qazmin/AQ Group map leads; verify carefully |
| Atyrau | `Атырауская область`, `Макат` | Oil/gas power and industrial land; mobile gas power plant leads | Makat DC/energy project leads; distinguish mining/industrial HPC |
| West Kazakhstan | `Западно-Казахстанская область`, `Уральск` | Regional akimat, power constraints, NIT/government facility | NIT Uralsk, Transtelecom, local hosting |
| Jambyl | `Жамбылская область`, `Тараз` | Energy projects, industrial zones, southern grid reinforcement | No strong known lead; search official pages first |
| Jetisu | `Жетысу`, `Талдыкорган` | Regional akimat and industrial zones | No strong known lead |
| Kostanay | `Костанайская область`, `Костанай` | Regional industrial/digitalization pages | Weak directory leads only |
| Kyzylorda | `Кызылординская область`, `Қызылорда` | Regional akimat; legacy Kazakhtelecom IDC | Kazakhtelecom Kyzylorda |
| Mangystau | `Мангистауская область`, `Актау`, `SEZ Seaport Aktau` | Prime Minister/Kazakh Invest project pages, gas-power connection, SEZ land | Digital Silk Route / Aktau DC leads |
| North Kazakhstan | `Северо-Казахстанская область`, `Петропавловск` | Regional akimat and fiber/edge facilities | No strong known lead |
| Turkistan | `Туркестанская область`, `Туркестан` | Southern grid reinforcement, new-city digital infrastructure | No strong known lead |
| Ulytau | `Ұлытау`, `Жезказган` | Mining/industrial power, regional investment pages | No strong known lead |
| East Kazakhstan | `Восточно-Казахстанская область`, `Усть-Каменогорск`, `Өскемен` | Regional construction/architecture pages, industrial power | Transtelecom / local telecom leads |

Region query template:
```
site:gov.kz "{region_ru}" ("дата-центр" OR "центр обработки данных" OR "ЦОД")
site:gov.kz "{city_ru}" ("строительство" OR "запуск" OR "меморандум") ("дата-центр" OR "ЦОД")
site:gov.kz "{region_ru}" ("подстанция" OR "электроснабжение" OR "технические условия") ("дата-центр" OR "ЦОД")
site:invest.gov.kz "{region_en}" "data center"
site:{regional-invest-subdomain}.invest.gov.kz "Data Center Valley" OR "data center"
"{city_ru}" "дата-центр" "стоек" OR "МВт"
"{city_ru}" "центр обработки данных" "Tier III" OR "Tier IV"
"{city_kk}" "деректер орталығы" "құрылыс"
```

---

## 6. Trade Press / Secondary Sources

Use these for leads and lifecycle events, then confirm via official/operator sources.

- **Data Center Dynamics**: https://www.datacenterdynamics.com. Strong for Yandex, Kazteleport, Kazakhtelecom, Beeline, and hyperscale announcements. **Grade B** unless it links to operator release.
- **Interfax**: https://interfax.com/newsroom/. Often quotes Kazakhstan officials and gives dates/MW for Data Center Valley. **B+**, **A- only when reproducing official statement with named speaker/date**.
- **Astana Times**: https://astanatimes.com. English official-adjacent national press; good for policy and investment announcements. **B**.
- **Qazinform**: https://qazinform.com. State news agency; useful for official interviews and investment announcements. **B+**.
- **Kursiv**, **Kapital.kz**, **Profit.kz**, **The Tech/Kazakhstan tech press**, **Times of Central Asia**, **Eurasianet**: useful for market and power-risk context. **B/C depending on sourcing**.
- Directories: **Uptime Institute awards**, **Data Center Map**, **Datacenters.com**, **Cloudscene**, **Baxtel**, **ColoMap**, **Yandex Maps/2GIS**. Use as discovery surfaces, not final proof unless certification/operator data is linked.

Trade query template:
```
site:datacenterdynamics.com Kazakhstan "data center"
site:interfax.com Kazakhstan "data center" "MW"
site:astanatimes.com Kazakhstan "data center"
site:qazinform.com Kazakhstan "data center" "Akashi" OR "Google Cloud"
site:kz.kursiv.media Kazakhstan "data center"
site:profit.kz "дата-центр" Казахстан
site:kapital.kz "дата-центр" Казахстан
site:uptimeinstitute.com "Kazakhstan" "data center"
```

---

## 7. Evidence Grading and Status Rules

### 7.1 Evidence hierarchy

| Grade | Source type in Kazakhstan |
|---|---|
| **A** | MAIDD/Prime Minister/Ministry of Energy/KEGOC documents naming a project or policy; eGov/e-Qurylys/Qportal permit output; akimat land/construction/commissioning notices; operator annual reports; official cloud-region docs; Uptime certification for named facility existence/certification |
| **B** | DCD, Interfax, Astana Times, Qazinform, Kursiv, Profit/Kapital when citing named officials/operators; operator press releases without permit/grid proof; Kazakh Invest project pages for investment leads |
| **C** | Data Center Map, Datacenters.com, Cloudscene, Baxtel, ColoMap, Yandex Maps, 2GIS, marketing decks, social posts, SEO pages |

### 7.2 Status mapping

- `MOU / memorandum / investment proposal / strategic agreement` = planned lead only.
- `land allocated / SEZ project / Kazakh Invest project card` = planned; count only if site and sponsor are named.
- `architectural-planning assignment / technical conditions / construction permit / e-Qurylys record` = permitted or pre-construction, depending on document.
- `groundbreaking / construction began / under construction` = construction, preferably with akimat/operator evidence.
- `commissioned / launched / opened / cloud region active / services available` = operational.
- `MW available / reserved power / generation mechanism` is not IT capacity unless the source says IT load or facility capacity.
- Treat crypto-mining/server farms separately from enterprise/colo/cloud DCs if the downstream schema allows. Kazakhstan has many power-led mining facilities that directories may label "data centers."

### 7.3 Pitfalls

- Government megaproject announcements can combine multiple future phases; avoid counting the full 1 GW Data Center Valley as built capacity.
- "Kazakhstan region" in cloud docs may mean billing/control-plane region or one availability zone, not a multi-AZ hyperscale region.
- Almaty vs Almaty Region and Astana vs Akmola are easily conflated. Bucket by physical municipality/oblast, not marketing metro.
- Russian transliteration varies: `Karaganda/Karagandy/Қарағанды`, `Ust-Kamenogorsk/Oskemen/Өскемен`, `Akkol/Aqkol`, `Kosshi/Qosshy`.
- Some state/government cloud facilities may be intentionally under-described; absence of public permit/news is not proof of absence.

---

## 8. Recommended Enumeration Workflow

1. **Seed national official leads**: MAIDD, Prime Minister, Ministry of Energy, Kazakh Invest, Akorda; extract project name, sponsor, region, MW/racks, and status verb.
2. **Cloud-region check**: verify Yandex `kz1` and scan AWS/Azure/GCP/OCI official region pages for any Kazakhstan change; record "no official public region" for providers not listed.
3. **Incumbent operator sweep**: Kazakhtelecom annual reports + B2B pages; Kazteleport, Transtelecom, Freedom, Beeline, PS.kz, Akashi, Enegix official pages.
4. **Region permit/grid pass**: for each division, run Russian/Kazakh `site:gov.kz` searches for DC terms plus construction, land, technical conditions, substation, and commissioning terms.
5. **KEGOC/energy cross-check**: for anything above a few MW, search project and region against KEGOC, Ministry of Energy, local utilities, and akimat energy departments.
6. **Certification/directory backfill**: Uptime Institute first, then Data Center Map / Datacenters.com / Cloudscene / Baxtel / Yandex Maps / 2GIS. Use these to discover aliases and addresses, then re-check official sources.
7. **Resolve status and dedupe**: group records by physical campus, operator/SPV, address, substation/power source, and phase. Keep Data Center Valley / Ekibastuz phases separate from existing Enegix and Kazakhtelecom Pavlodar facilities.

## Quick URL Index

- MAIDD: https://www.gov.kz/memleket/entities/maidd?lang=en
- Telecom Committee: https://www.gov.kz/memleket/entities/telecom?lang=en
- Prime Minister: https://primeminister.kz/en/news
- Ministry of Energy: https://www.gov.kz/memleket/entities/energo?lang=en
- KEGOC: https://www.kegoc.kz/en/
- KEGOC grid access: https://www.kegoc.kz/en/electric-power/deyatelnost-kompanii/poryadok-dostupa-k-natsionalnoy-elektricheskoy-seti/
- eGov: https://egov.kz
- e-License: https://elicense.kz
- e-Qurylys: https://about.equrylys.kz/
- State Urban Planning Cadastre: https://gov.ggk.kz / https://aisggk.kz
- Adilet legal database: https://adilet.zan.kz
- Kazakh Invest: https://invest.gov.kz
- Yandex Cloud Kazakhstan region docs: https://yandex.cloud/en/docs/overview/concepts/region
- Yandex Cloud Kazakhstan launch: https://yandex.cloud/en/blog/posts/2024/04/yandex-cloud-in-kazakhstan
- Kazakhtelecom annual reports: https://ar2021.telecom.kz/en/information-technology.html / https://ar2022.telecom.kz/ru/information-technology.html
- AKASHI: https://akashi.cloud
- Enegix: https://enegix.net/en
- PS.kz data centers: https://www.ps.kz/en/about/data-center
