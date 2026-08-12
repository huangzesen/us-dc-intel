# UA Explorer Official - Ukraine Datacenter Enumeration via Construction, Energy, Telecom Regulator, Cloud, and Colo Sources

Date: 2026-08-12. Country: **UA Ukraine**. Division model in `world-manifest.jsonl`: 24 oblasts plus **Kyiv City**, **Crimea**, and **Sevastopol**. Angle: official/regulatory/cloud-first enumeration for data-center facilities and projects.

Reliability grades:
- **A** = primary / legally accountable source: Ukrainian government portal, ЄДЕССБ construction record, DIAM/state architectural control, city/oblast council or military administration, NERC/NEURC, Ukrenergo/DSO, NCEC/NKЕК, official cloud-region page, official operator facility page, securities filing, or statutory certification.
- **B** = strong secondary source: recognized trade press, Interfax-Ukraine/Ukrinform/state media, official partner or contractor case study, reputable international datacenter press.
- **C** = weak lead: directories, market maps, reseller pages, job ads, social media, unsourced local articles, or MoU-only announcements with no land/power/permit trail.

---

## 0. Ukraine-specific structural facts

- Ukraine has **no single public datacenter registry**. Build the census by joining **ЄДЕССБ construction documents**, municipal planning decisions, **DIAM** construction-control records, **NERC/NEURC + Ukrenergo + distribution-system operator** grid-connection evidence, **NCEC/NKЕК** telecom-provider registers, official cloud/colo pages, and trade press.
- The key official construction portal is the **Unified State Electronic System in the Construction Sector / ЄДЕССБ**: https://e-construction.gov.ua/. Its registry page exposes categories for declarative/permitting documents, urban planning conditions and restrictions, project documentation, acts of readiness for operation, technical conditions, energy certificates, participants in construction, and related records: https://e-construction.gov.ua/reestri. Use it as the Grade-A backbone for new construction, reconstruction, commissioning, and cost/status fields.
- The public portal can be searched directly and through web engines. High-value object pages look like `https://e-construction.gov.ua/permits_doc_detail/{id}` or `https://e-construction.gov.ua/document_detail/doc_id%3D{id}/optype%3D...`; they can show document type, registration number, status, authority, object name, consequence class, customer, designer, address, construction dates, and estimated construction cost.
- Ukrainian construction records often do **not** use the English term `data center`. Search Ukrainian and Russian variants: `дата-центр`, `дата центр`, `центр обробки даних`, `центр обработки данных`, `ЦОД`, `ЦОДД`, `серверна`, `серверний центр`, `хмарний дата-центр`, `обчислювальний центр`, `центр зберігання та обробки даних`.
- NCEC/NKЕК is the current electronic-communications regulator: https://nkek.gov.ua/. Older Ukrainian sources may say **NCCIR / НКРЗІ** for the predecessor commission. The NKЕК provider-register page is https://nkek.gov.ua/spozhyvacham-posluh/reiestry-postachalnykiv and links the **Register of providers of electronic communications networks and/or services**. This is an **operator/connectivity census**, not a facility census.
- Energy evidence is crucial because Ukrainian public facility pages rarely disclose MW. For large projects, look for non-standard grid connection, substations, transformer capacity, diesel generator permits, or utility technical conditions. Start with NERC/NEURC (`НКРЕКП`) connection process pages such as https://www.nerc.gov.ua/sferi-diyalnosti/elektroenergiya/priyednannya-do-elektrichnih-merezh/poryadok-priyednannya-elektroustanovok-do-elektrichnih-merezh and calculators at https://www.nerc.gov.ua/calculator-standart / https://www.nerc.gov.ua/calculator-nonstandart. For transmission-level loads, use Ukrenergo connection procedure: https://ua.energy/protsedura-pryyednannya/.
- War/occupation status materially affects verification. Treat Crimea, Sevastopol, parts of Donetsk/Luhansk/Zaporizhzhia/Kherson as special cases: record de jure Ukrainian division, de facto/occupation note, source jurisdiction, and current-operability uncertainty. Do not infer current operation from pre-2022 or Russian-directory evidence without fresh corroboration.

Lifecycle vocabulary:

`меморандум / намір / інвестпроєкт` < `містобудівні умови та обмеження (МУО)` < `технічні умови` < `дозвіл на виконання будівельних робіт` < `відомості про виконання будівельних робіт / початок` < `акт готовності` < `сертифікат прийняття в експлуатацію` < `введено в експлуатацію / запущено / надає послуги`.

Only count `дозвіл`, `виконання будівельних робіт`, `акт готовності`, `сертифікат`, or operator-confirmed launch as strong facility evidence. Treat MoUs and investment-promotion pages as planned leads until matched to permit/power/operator records.

---

## 1. Ukrainian, Russian, and English query patterns

### 1.1 Core Ukrainian/Russian terms

```text
дата-центр
дата центр
центр обробки даних
центр зберігання та обробки даних
центр обробки та зберігання даних
ЦОД
серверна
серверний центр
хмарний дата-центр
хмарний провайдер
колокація OR колокейшн
розміщення серверів
обчислювальний центр
AI дата-центр
суверенний дата-центр
центр обработки данных
дата-центр Украина
ЦОД Украина
```

### 1.2 Construction / planning / permitting

Substitute `{oblast}`, `{city}`, `{hromada}`, `{operator}`, `{legal_entity}`, `{address}`.

```text
site:e-construction.gov.ua "дата-центр"
site:e-construction.gov.ua "центр обробки даних"
site:e-construction.gov.ua "ЦОД" "Назва об’єкта"
site:e-construction.gov.ua "{operator}" "дозвіл на виконання будівельних робіт"
site:e-construction.gov.ua "{operator}" "сертифікат" "прийняття в експлуатацію"
site:e-construction.gov.ua "{address}" "дозвіл"
site:e-construction.gov.ua "{city}" "серверна"
"{city}" "дата-центр" "дозвіл на виконання будівельних робіт"
"{city}" "центр обробки даних" "містобудівні умови"
"{hromada}" "дата-центр" "містобудівні умови та обмеження"
"{operator}" "{city}" "містобудівні умови"
"{operator}" "{city}" "сертифікат готовності"
"{legal_entity}" "ЄДЕССБ"
"{legal_entity}" "ДІАМ" "дозвіл"
```

Municipal portals usually use Ukrainian only:

```text
site:kyivcity.gov.ua "дата-центр"
site:kmr.gov.ua "центр обробки даних"
site:city-adm.lviv.ua "дата-центр"
site:omr.gov.ua "дата-центр"
site:city.kharkiv.ua "дата-центр"
site:dniprorada.gov.ua "дата-центр"
site:{city-domain} "серверна" "технічні умови"
site:{oblast-admin-domain} "центр обробки даних"
```

### 1.3 Energy / grid / generators / environment

```text
"{operator}" "{city}" "технічні умови" "електропостачання"
"{operator}" "{city}" "приєднання до електричних мереж"
"{operator}" "{city}" "нестандартне приєднання"
"дата-центр" "приєднання до електричних мереж" "{oblast}"
"центр обробки даних" "трансформаторна підстанція" "{city}"
"дата-центр" "МВт" "{city}"
"ЦОД" "МВт" "Україна"
"дата-центр" "дизель-генератор" "{city}"
"дата-центр" "резервне живлення" "{city}"
site:nerc.gov.ua "дата-центр"
site:ua.energy "дата-центр"
site:ua.energy "приєднання" "центр обробки даних"
site:{dso-domain} "дата-центр" "приєднання"
site:{dso-domain} "{operator}" "технічні умови"
```

Key energy sources:
- NERC/NEURC (`НКРЕКП`) main site and connection pages: https://www.nerc.gov.ua/.
- Ukrenergo transmission connection procedure: https://ua.energy/protsedura-pryyednannya/.
- Ukrenergo market/datahub context: https://ua.energy/datahub/.
- DTEK Kyiv Electric Networks / Kyiv oblast and city: https://www.dtek-kem.com.ua/ua/connections.
- DTEK Dnipro/Kyiv/Odesa/Donetsk regional DSO pages where applicable.
- Lvivoblenergo: https://loe.lviv.ua/.
- Kharkivoblenergo: https://www.oblenergo.kharkov.ua/.
- Poltavaoblenergo, Sumyoblenergo, Rivneoblenergo, etc. Search each DSO with candidate operator/legal names.

Energy records prove grid status, requested power, or backup-power details. They do **not** prove a datacenter unless the same legal entity/project also appears in construction/operator evidence.

### 1.4 Telecom regulator / provider registry

```text
site:nkek.gov.ua "дата-центр"
site:nkek.gov.ua "центр обробки даних"
site:nkek.gov.ua "Реєстр постачальників" "{operator}"
site:nkek.gov.ua "Київстар" "рішення"
site:nkek.gov.ua "постачальників електронних комунікаційних мереж" "{legal_entity}"
"НКЕК" "{operator}" "електронних комунікацій"
"НКРЗІ" "{operator}" "дата-центр"
```

Use NCEC/NKЕК to normalize legal names, telecom-service status, and operator identity. It is **A** for regulatory status and **supporting evidence only** for a facility.

### 1.5 English discovery and trade-press patterns

```text
"Ukraine" "data center" "building permit"
"Kyiv" "data center" "construction permit"
"Ukraine" "data center" "grid connection" MW
"Ukraine" "sovereign AI data center"
"Kyivstar" "AI data center" Ukraine MW
"De Novo" "data center" Kyiv
"GigaCloud" "data centers" Ukraine Kyiv Lviv Warsaw
"Parkovyi" "data center" Kyiv
"Zaporizhzhia" "data center" Energoatom Hotmine
"Kherson" "data center" TECHIIA Ecotechnopark
"Lviv" "data center" "official"
"Odesa" "data center" "TENET"
```

---

## 2. Official / regulatory source backbone

### 2.1 ЄДЕССБ construction registry

Primary sources:
- ЄДЕССБ portal: https://e-construction.gov.ua/. **Grade A**.
- Registry front door: https://e-construction.gov.ua/reestri. **Grade A**.
- Public map/search from the portal menus (`Карта`, `Пошук`) and direct indexed pages such as `/permits_doc_detail/` and `/document_detail/`. **Grade A**.
- DIAM / State Inspection of Architecture and Urban Planning: https://diam.gov.ua/. **Grade A** for construction-control process and official news; use ЄДЕССБ object pages for record detail where possible.

Fields to extract:
- document type: `Містобудівні умови та обмеження`, `дозвіл на виконання будівельних робіт`, `відомості про виконання будівельних робіт`, `акт готовності`, `сертифікат прийняття в експлуатацію`;
- current document status and registration number;
- issuing authority: DIAM, former DABI, city architecture department, hromada;
- object name and construction type (`нове будівництво`, `реконструкція`, `капітальний ремонт`);
- customer/investor, designer, contractor, technical supervisor;
- address, cadastral/administrative details, consequence class (`СС1/СС2/СС3`);
- declared start/end dates and estimated construction cost;
- linked `технічні умови` or project documentation if visible.

Important caveat: many operating Kyiv/Lviv/Odesa facilities pre-date ЄДЕССБ public coverage or were built as telecom/office/technical reconstructions. For legacy facilities, official operator page + NCEC + property/permit archive is often the strongest available public trail.

### 2.2 City / oblast planning and procurement

Use city councils, oblast military administrations, hromada portals, and Prozorro procurement as secondary official discovery:

```text
site:prozorro.gov.ua "дата-центр" "{city}"
site:prozorro.gov.ua "центр обробки даних" "{oblast}"
site:prozorro.gov.ua "серверна" "дизель-генератор"
site:{city-domain} "МУО" "дата-центр"
site:{city-domain} "технічні умови" "серверна"
site:{oblast-domain} "інвестиційний проект" "дата-центр"
```

Procurement is usually **A** for public-sector small/server-room work, equipment, generator, or cloud-service purchases, but it rarely proves a commercial wholesale facility. Use it to find government datacenters and operator relationships; do not convert a cloud-services tender into a physical facility without supporting evidence.

### 2.3 Energy / grid process

Primary sources:
- NERC/NEURC connection procedure and calculators: https://www.nerc.gov.ua/sferi-diyalnosti/elektroenergiya/priyednannya-do-elektrichnih-merezh/poryadok-priyednannya-elektroustanovok-do-elektrichnih-merezh, https://www.nerc.gov.ua/calculator-standart, https://www.nerc.gov.ua/calculator-nonstandart. **Grade A** for process, tariffs, and formulas.
- Ukrenergo connection procedure: https://ua.energy/protsedura-pryyednannya/. **Grade A** for transmission-connection process.
- DSO connection pages by region, especially DTEK Kyiv Electric Networks: https://www.dtek-kem.com.ua/ua/connections. **Grade A** for utility process and published connection materials.

What to extract:
- standard vs non-standard connection;
- requested/contracted capacity in kW/MW or transformer MVA;
- connection point / substation;
- line works, new transformer substation, diesel generators, batteries/UPS;
- date of application, technical conditions, connection agreement, energization;
- whether wartime temporary connection rules apply.

Store power evidence separately from facility capacity:

```text
requested_connection_mw
contracted_power_mw
it_load_mw
backup_generator_mw
substation_mva
connection_status
connection_source_url
```

### 2.4 NCEC / NKЕК telecom-provider registry

Primary source:
- NKЕК provider registers: https://nkek.gov.ua/spozhyvacham-posluh/reiestry-postachalnykiv. **Grade A**.
- NKЕК decisions and registry of decisions: https://nkek.gov.ua/ under `Засідання` / `Прийняті рішення` / `Реєстр рішень НКЕК`. **Grade A**.

Use cases:
- normalize legal names for operators such as Kyivstar, Datagroup/Volia, Adamant, Cosmonova/BeMobile, UARNet, TENET, RX-NAME, ITL, local ISPs;
- identify network-service providers that may own telecom rooms/colo;
- pivot from provider legal name to ЄДЕССБ, municipal planning, operator official pages, and procurement.

Not a datacenter census. Do not count a provider as a facility unless a facility address/service page or permit exists.

### 2.5 Cloud-region official pages

As of this methodology date, no major global public-cloud provider has an official Ukraine public cloud region in the standard region lists checked. Official pages are still useful to avoid false positives:

| Provider | Official source | Ukraine signal | Enumeration use |
|---|---|---|---|
| AWS | AWS Local Zones locations: https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ and docs list: https://docs.aws.amazon.com/local-zones/latest/ug/available-local-zones.html | No Kyiv/Ukraine Local Zone found in official list at check date. AWS has Ukraine-government data-resilience/support stories, but not a Ukraine region. | Use as negative control. Search Direct Connect/partner pages only as connectivity leads; do not count an AWS Ukraine DC without official region/local-zone evidence. |
| Microsoft Azure | Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list and geographies: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | No Azure Ukraine region found; nearest major CEE official signal is Poland. | Treat Azure in Ukraine as partner/cloud-service usage unless Microsoft announces a Ukraine region. |
| Google Cloud | Locations: https://cloud.google.com/about/locations and Compute Engine region docs: https://docs.cloud.google.com/compute/docs/regions-zones | No Google Cloud Ukraine region found in official locations at check date. | Connectivity/partner lead only. |
| Oracle Cloud | OCI public cloud regions: https://www.oracle.com/ua/cloud/public-cloud-regions/ and docs: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | Oracle has Ukraine-market pages but no Ukraine public cloud region found in region list. | Connectivity/partner lead only. |
| Domestic cloud | De Novo, GigaCloud, Tucha, Volia/Datagroup, Parkovyi | Domestic provider regions/availability zones may be real facilities or leased colo. | Use official provider pages as A for service existence; still verify physical facility and address via operator/property/permit evidence. |

---

## 3. Official / operator seed list

Operator official pages are **A** for existence of offered services and marketed location, but capacity claims need separate grading. Use these as pivots into ЄДЕССБ, NKЕК, DSO, municipal, and trade-press searches.

| Operator / project | Official source | Footprint signal | Follow-up joins |
|---|---|---|---|
| De Novo | https://denovo.ua/en and Ukrainian pages under https://denovo.ua/ | Ukrainian cloud/IaaS/PaaS and data-center services; public pages refer to own Kyiv data center and services for government/enterprise. | Search `De Novo`, `Де Ново`, address `Північно-Сирецька`, ЄДЕССБ, NKЕК, DTEK Kyiv, certifications. |
| GigaCloud / GigaCenter | https://gigacloud.ua/ and https://gigacenter.ua/ | GigaCloud says equipment is in five data centers, including three in Ukraine and two in Poland; GigaCenter markets a Tier III Kyiv data center. | Search GigaCloud/GigaCenter legal entities, Kyiv/Lviv/Warsaw availability zones, ЄДЕССБ, DSO, DSUA. |
| Parkovyi Data Center / Datapark | https://parkovyi-dc.com/en/ and https://datapark.ua/ | Kyiv data center and sovereign-cloud positioning; co-founder of Ukrainian Digital Sovereignty Alliance. | Search `Парковий дата-центр`, `КВЦ Парковий`, Kyiv permits, power, DSUA. |
| Kyivstar | https://kyivstar.ua/en/business/products/data-center and VEON release https://www.veon.com/newsroom/press-releases/kyivstar-signs-mou-with-ukraines-ministry-of-economy-to-accelerate-ai-infrastructure-and-digital-growth | Existing business data-center/colo services; 2026 VEON/Ministry MoU to explore a sovereign AI-ready data center in Ukraine. | For existing facilities search Dehtiarivska/Khvoyki street, Kyivstar legal names, NKЕК, Kyiv permits. For AI DC require future site/power/permit before counting beyond planned. |
| Datagroup / Volia | https://www.datagroup.ua/en/services/data-centers and https://dc.volia.com/ | Telecom and data-center/hosting services, including Volia DC. | Search Datagroup/Volia legal entities, Kyiv/Rivne/other listed markets, DSO, NKЕК. |
| Adamant | https://adamant.ua/data-center/colocation | Kyiv colocation/data-center services, Tier-III marketing, telecom operator history. | Search Adamant legal entity, Kyiv permits, power/generator evidence, NKЕК. |
| Cosmonova / BeMobile | https://cosmonova.net.ua/en/data-center/ and https://bemobile.ua/en/colocation/ | Kyiv colocation/data-center services. | Search Cosmonova/BeMobile legal entities, Kyiv permits, power, NKЕК. |
| UARNet | https://www.uar.net/en/services/datacenter/ | Lviv data-center services. | Search Lviv city permits, Lvivoblenergo, university/research network records. |
| TENET | https://www.tenet.ua/en/business/data-center | Odesa data-center/colocation services. | Search Odesa city/oblast, DTEK Odesa, NKЕК. |
| RX-NAME | https://rx-name.net/datacenter | Mykolaiv data-center/hosting infrastructure. | Search Mykolaiv city/oblast, DSO, NKЕК. |
| HyperHost | https://hyperhost.ua/en/info/datacenter | Hosting/data-center infrastructure, often directory-listed in Odesa. | Confirm physical address and operator-owned/leased status before grading above C/B. |
| ITL / Ukrnames / Infiumhost / Layer1 | operator pages plus Kharkiv directory leads | Kharkiv hosting/colo cluster. | Wartime operability must be confirmed with current official/operator source; search Kharkiv permits and utility records. |
| Energoatom / Hotmine Zaporizhzhia concept | Energoatom official site https://energoatom.com.ua/en/about plus 2020 Ukrinform/Interfax coverage | Pre-war announced very large data-processing center near Zaporizhzhia NPP; no current build evidence located. | Treat as B/C planned/historical lead unless new Energoatom, oblast, ЄДЕССБ, or power record appears. |
| TECHIIA / Kherson Ecotechnopark concept | UkraineInvest and TECHIIA press pages | Announced 500 MW / $1bn data-center concept in Kherson region before full-scale war. | Treat as investment-promotion lead only unless current Kherson official/permit/power records exist. |

Trade press / secondary feeds:
- Data Center Dynamics: https://www.datacenterdynamics.com/; useful for Kyivstar AI DC and international context. **B**.
- Interfax-Ukraine: https://en.interfax.com.ua/ and Ukrainian/Russian mirrors. **B/B+** for signed agreements and company quotes.
- Ukrinform: https://www.ukrinform.net/. State media, good for official-announcement leads. **B+** for event truth, not capacity proof.
- DataCenterMap / Datacenters.com / Inflect: useful as **C** seeds only; re-verify every facility through operator, permit, or regulator evidence.

---

## 4. Per-division enumeration matrix

Run the same baseline in every division:

```text
site:e-construction.gov.ua ("дата-центр" OR "центр обробки даних" OR "ЦОД" OR "серверна") "{division}"
"{division}" ("дата-центр" OR "центр обробки даних" OR "ЦОД") ("дозвіл" OR "МУО" OR "сертифікат" OR "введено в експлуатацію")
"{division}" ("дата-центр" OR "ЦОД") ("МВт" OR "приєднання" OR "технічні умови" OR "підстанція")
site:nkek.gov.ua "{operator}" "{division}"
```

Then apply division-specific pivots:

| Division | Priority search approach |
|---|---|
| Kyiv City | Highest priority. Search Kyiv official domains (`kyivcity.gov.ua`, `kmr.gov.ua`), ЄДЕССБ, DTEK Kyiv Electric Networks, and NKЕК for De Novo, Parkovyi/Datapark, GigaCenter/GigaCloud, Kyivstar, Volia/Datagroup, Adamant, Cosmonova/BeMobile. Query addresses from official pages and directories separately. |
| Kyiv Oblast | Search around Bucha, Brovary, Boryspil, Vyshhorod, Fastiv, Bila Tserkva, industrial/logistics parks, and Kyiv-adjacent substations. Use `site:e-construction.gov.ua "Київська область" "дата-центр"` plus DTEK Kyiv Regional Electric Networks. Watch for facilities bucketed incorrectly as Kyiv City. |
| Lviv | Priority western hub. Search UARNet, GigaCloud/GigaTrans, De Novo Lviv references, Lviv IT cluster, `city-adm.lviv.ua`, Lvivoblenergo, and industrial parks. Include Ukrainian and English (`Lviv data center`, `Львів ЦОД`). |
| Odesa | Search TENET, HyperHost, Datagroup/Volia, port/logistics-adjacent telecom facilities, Odesa city council `omr.gov.ua`, DTEK Odesa, and NKЕК. Wartime resilience/generator references may be stronger than permit records. |
| Kharkiv | Search Ukrnames, ITL, Infiumhost, Layer1, Kharkiv city/oblast portals, Kharkivoblenergo. Treat current operation carefully because of frontline proximity; require recent operator status or official records for operational classification. |
| Dnipropetrovsk | Search Dnipro city council, Dnipropetrovsk OVA, DTEK Dnipro Grids, Datasfera, SerinIX, Omega Telecom, industrial-power terms, and `Дніпро ЦОД`. |
| Zaporizhzhia | Search Energoatom/Hotmine historical project, Zaporizhzhia OVA/city, Ukrenergo/DSO, NPP-related official sources. Because of occupation/frontline conditions, treat 2020 megaproject articles as historical planned leads unless current official records are found. |
| Kherson | Search TECHIIA/Ecotechnopark historical concept, Kherson OVA/city, hromada investment pages, DSO. Occupation/war damage makes current permit/power verification mandatory. |
| Mykolaiv | Search RX-NAME, Mykolaiv city/oblast, Mykolaivoblenergo, `центр обробки даних Миколаїв`, `дата-центр Миколаїв`. |
| Poltava | Search ColoCall/Kremenchuk, Poltava/Kremenchuk city portals, Poltavaoblenergo, telecom operators. |
| Rivne | Search Datagroup, Campus Networks, Rivne city/oblast, Rivneoblenergo. Also search NPP-energy-adjacent rumors separately but require permits/power. |
| Vinnytsia | Search IP-Connect/DC-16 leads, Vinnytsia city/oblast, Vinnytsiaoblenergo, e-government/server-room procurement. |
| Khmelnytskyi | Search municipal investment-project pages, Khmelnytskyi NPP adjacency, city/oblast portals, Khmelnytskoblenergo, `інвестпроєкт дата-центр`. Treat promotion pages as C until permit/power appears. |
| Cherkasy | Low known density. Search city/oblast, Cherkasyoblenergo, public-sector data center/procurement, local ISPs. |
| Chernihiv | Low known density. Search Chernihiv city/oblast, Chernihivoblenergo, `серверна`, `центр обробки даних`, wartime reconstruction tenders. |
| Chernivtsi | Low known density. Search city/oblast, Chernivtsioblenergo, local ISPs, government server rooms. |
| Ternopil | Low known density. Search city/oblast, Ternopiloblenergo, local ISPs, public-sector server-room procurements. |
| Sumy | Low known density/frontier risk. Require recent official/operator evidence. Search Sumy city/oblast, Sumyoblenergo, local ISP terms. |
| Kirovohrad | Search Kropyvnytskyi/Kirovohrad OVA, local DSO, `серверна`, `дата-центр`, investment pages. |
| Zhytomyr | Search Zhytomyr city/oblast, DSO, investment parks, e-government data center tenders. |
| Volyn | Search Lutsk/Volyn portals, Volynoblenergo, border-connectivity and local ISP terms. |
| Transcarpathia | Search Uzhhorod/Zakarpattia portals, cross-border connectivity/backup sites, Zakarpattiaoblenergo, local hosting. |
| Ivano-Frankivsk | Search city/oblast, Prykarpattyaoblenergo, local IT/telecom providers, public-sector server rooms. |
| Donetsk | Treat as special status. Search Ukrainian OVA and operator pages for government-controlled areas; separately record Russian/occupation sources only with jurisdiction note. Do not count current operation from old Donetsk directory pages without current source. |
| Luhansk | Same as Donetsk; high uncertainty. Search Ukrainian OVA, displaced administration procurement, and operator continuity notices. |
| Crimea | Special status/occupied. Ukrainian methodology should bucket to Crimea but record source jurisdiction. Russian operator pages (e.g., Simferopol) are C unless corroborated and should be flagged de facto/Russian-administered. |
| Sevastopol | Same as Crimea; source jurisdiction and sanctions/occupation note required. |

---

## 5. Verification and grading rules

### 5.1 Evidence hierarchy

1. **A - facility permit / commissioning**: ЄДЕССБ permit, construction-start record, act of readiness, commissioning certificate, DIAM record, municipal MOU only if paired with permit/land/power.
2. **A - energy/power**: NERC/Ukrenergo/DSO connection record, technical conditions, transformer/substation record, official power agreement, environmental/generator permit naming the project.
3. **A - regulator/operator identity**: NKЕК provider registry and decisions for legal name/connectivity status.
4. **A-/B - operator official page**: official data-center page proves marketed service/location; capacity and Tier claims remain marketing unless certified/filing-backed.
5. **B - trade press/state media**: DCD, Interfax-Ukraine, Ukrinform, Light Reading, W.Media when they quote a company/government and name a project/status.
6. **C - directories/aggregators**: DataCenterMap, Datacenters.com, Inflect, cloud-market lists, job ads. Use as leads only.

### 5.2 Status classification

- `announced`: MoU, investment-promotion page, press quote, no site/power/permit.
- `planned`: site or public authority named, early planning/MUO/technical conditions, no building permit.
- `permitted`: ЄДЕССБ/DIAM permit or equivalent construction approval exists.
- `under_construction`: permit plus start/construction evidence, contractor/progress, or official groundbreaking with permit context.
- `operational`: official operator service page for the facility, commissioning certificate, or recent customer/service evidence.
- `unknown`: directory-only, old pre-war source, or occupied-area source with no current corroboration.

### 5.3 Capacity rules

- Prefer MW/MVA from grid/utility records or official project documents. Store as requested/contracted/IT load separately.
- If only racks are stated, do not convert to MW unless a source states rack density or power. Ukrainian facilities are often retail colo; rack counts can imply very different loads.
- Large pre-war concepts such as Zaporizhzhia or Kherson megaprojects should keep announced MW in notes, but status must remain `announced/planned` unless current permits/power/construction are found.
- Official cloud-provider region lists are negative controls. Do not infer an AWS/Azure/GCP/OCI physical Ukraine data center from cloud-sales activity or disaster-response support.

### 5.4 Alias / duplicate handling

Normalize each record by:

```text
ultimate_parent
local_legal_entity
facility_brand
facility_address_or_hromada
division_bucket
source_jurisdiction
permit_registration_number
grid_connection_id_or_substation
operator_url
```

Common duplicate traps:
- Kyiv City vs Kyiv Oblast bucket mismatch.
- GigaCloud vs GigaCenter vs GigaTrans.
- Parkovyi vs Datapark vs `Парковий`.
- Datagroup vs Volia after corporate combinations.
- Cosmonova vs BeMobile.
- Ukrainian/Russian/English spelling variants: `Kyiv/Kiev`, `Odesa/Odessa`, `Kharkiv/Kharkov`, `Dnipro/Dnipropetrovsk`, `Mykolaiv/Nikolaev`, `Lviv/Lvov`.
- Occupied-territory records listed under Russia in international directories while repo bucket remains UA.

---

## 6. Recommended discovery pipeline

1. **Seed known operators** from official pages in section 3, NKЕК provider register, and existing directory leads. Normalize legal names and aliases.
2. **Run ЄДЕССБ searches** for core Ukrainian/Russian facility terms plus operator legal names and known addresses. Capture permit/commissioning fields and document IDs.
3. **Run city/oblast portal searches** for Kyiv, Lviv, Odesa, Kharkiv, Dnipro, Mykolaiv, Poltava/Kremenchuk, Rivne, Vinnytsia, Khmelnytskyi, Zaporizhzhia, and Kherson first. Use municipal `МУО`, land, council, and investment-project records for early-stage leads.
4. **Power cross-check** through NERC/Ukrenergo process pages and the relevant DSO for each candidate. Search for `технічні умови`, `нестандартне приєднання`, substations, generator permits, and transformer capacity.
5. **Cloud/colo validation**: use AWS/Azure/GCP/OCI official region pages as negative controls, then domestic provider pages for actual Ukraine facilities. Verify any "cloud region" claim as physical facility vs leased colo vs foreign-region service.
6. **Trade-press watch**: monitor DCD, Interfax-Ukraine, Ukrinform, Light Reading, W.Media, and operator news for Kyivstar AI DC, DSUA/GigaCloud/De Novo/Parkovyi sovereign-cloud moves, and revived post-war reconstruction projects.
7. **Grade each data point separately**: official page may be A for existence, C for capacity if no MW source, and B for project timing if only trade press exists.

Pitfalls recap: ЄДЕССБ keyword gaps; legacy facilities built before public records; Kyiv City/Kyiv Oblast confusion; Ukrainian/Russian spelling drift; telecom-provider registry is not a facility registry; cloud-sales presence is not a cloud region; pre-war megaproject announcements require current re-verification; occupied-area sources need jurisdiction and status notes.
