# SD Explorer Official — Sudan Datacentre Enumeration via Regulator, Ministry, NIC, Energy, Cloud and Operator Sources

Date: 2026-08-12. Country: **SD Sudan**. Division model: **18 states**. Angle: **official/regulatory/cloud pipeline** for finding commercial, hyperscale, government, telecom and banking data-centre facilities.

Reliability grades:
- **A** = primary/official/legal source: TPRA licence or official page, MTDT/NIC/SIXP official material, SUNA official report, state/government announcement, operator official facility page, official cloud-provider statement.
- **B** = strong secondary source: credible trade/local press (Dabanga, Actum Sudan, Sudan Tribune), PeeringDB/PCH records, Uptime-type or operator corroborated announcements, reputable aggregator when it reproduces operator data.
- **C** = weak lead: generic market report, social post, unsupported directory entry, NGO/think-tank snippet without facility evidence, old MoU.

---

## 0. Sudan-specific structure facts

- Sudan has **no public datacentre planning-permit register** and no state-level e-permitting portal for buildings. There is no national facility registry. Enumeration works by joining: **TPRA telecom licensing** (including a data-centre/cloud licence class), **MTDT digital-transformation announcements** (3x3 plan, Baladna, CONSOLEX), **NIC/NDC/SIXP** government infrastructure, **SUNA** official reporting, **operator official pages** (mainly Sudatel/Sudani), **energy/grid context**, and **IXP/network registries** (PeeringDB).
- The commercial market is tiny and effectively **Sudatel/Sudani-led**. Sudatel is the only operator found with current official public colocation/hosting/DC service pages: its own site describes a Khartoum Sudatel Data Center and states that the group operates **two Tier III data centers**. Sudatel/Sudani offers colocation, dedicated servers, virtual servers/VPS, SAN/storage, IaaS/cloud hosting and business hosting. The **National Information Center (NIC)** is the state IT infrastructure body and runs government hosting/VPS services; its National Data Centre/NDC and Sudan Internet Exchange Point (SIXP) evidence is strongest in Khartoum. Zain Sudan, MTN Sudan and legacy Canar/Sudani have telecom core/DR/server-room evidence, but no public marketed colocation facility page was found for them.
- **War context is mandatory for grading.** Since 15 April 2023 the country has been at war (SAF vs RSF). Much of Khartoum was contested or RSF-held from April 2023 until the SAF recapture of key sites in March 2025 and the army's May 2025 claim that Khartoum state was free of RSF. The internationally recognised government operated from **Port Sudan** during the war. RSF occupation/seizure of ISP data-centre facilities in Khartoum was widely reported as a cause of the **February 2024** nationwide internet shutdown. Drone attacks and combat damaged Khartoum power/telecom infrastructure in 2025. The main **state data centre in Khartoum (1,300 m2)** was reported reactivated after rehabilitation on **9 October 2025** (SUNA post; Actum Sudan summarising Minister Ahmed Dardiri). Any Khartoum-facility status claim must be date-stamped and re-verified.
- **Languages**: Arabic is primary for official/press material; English is used on TPRA, MTDT, Sudatel and NIC pages. Use both: `data centre` / `data center` / `datacentre` and Arabic: `مركز بيانات` (data centre), `مركز البيانات الوطني` (national data centre), `مركز البيانات القومي`, `استضافة` (hosting), `خوادم` (servers), `سحابة`/`الحوسبة السحابية` (cloud), `التحول الرقمي` (digital transformation), `شبكة المعلومات القومية` (national information network).
- **No hyperscaler cloud region** in Sudan on AWS/Azure/GCP/OCI official region lists as of methodology date; no verified hyperscaler on-ramp in-country; one aggregator claims zero direct on-ramps as of Sep 2025 with nearest hubs Marseille/Nairobi, but treat this as C-grade context. Treat any "cloud region" claim as a service/partner lead, not a facility.
- **Energy**: market aggregators claim industrial power around US$0.10/kWh and a large hydro share, but these are C-grade planning inputs unless corroborated by energy statistics. Severe load-shedding, fuel constraints and war damage mean **on-site generation/UPS evidence is expected** for any mission-critical facility. Power evidence (substations, generators, MVA, diesel storage) is a useful secondary trail but must not be converted into facility records by itself.

---

## 1. Grade A official regulator — TPRA

- **Telecommunications and Post Regulatory Authority (TPRA)**: https://tpra.gov.sd/en/ (English) and https://tpra.gov.sd/ (Arabic). Founded under the **Telecommunications and Post Regulating Act, 2018**; regulates wire, cellular, satellite and cable telecoms and postal services.
- **Licensing page**: https://tpra.gov.sd/en/services/telecom-licensing/ — live/verified during final review. It describes licence classes under the **Licensing Regulation for the Telecommunications and Postal Sector of 2019** and includes a **third-class licence granted to entities delivering cloud computing services through their private data centers, restricted to Software-as-a-Service (SaaS)**. This is the closest thing Sudan has to a public data-centre/cloud authorisation regime. Use it for service authorisation and licensee discovery; it does **not** prove a named physical facility or facility count by itself.
- **Sudan CERT**: https://tpra3.onespace.sd/en/home/ — Sudan Computer Emergency Response Team, established January 2010 as a TPRA initiative; useful for cyber-incident context on DCs (e.g. shutdowns, breaches).
- TPRA also issues landing rights for foreign satellites, device licences, and operator/service licences; look for published **licensee lists/registers** on the site (search `site:tpra.gov.sd` with operator legal names).

TPRA query templates:
```text
site:tpra.gov.sd "data centre"
site:tpra.gov.sd "data center"
site:tpra.gov.sd "cloud" "licence"
site:tpra.gov.sd "Licensing Regulation" "2019"
site:tpra.gov.sd "third-class" "cloud"
site:tpra.gov.sd Sudatel OR Zain OR MTN OR Sudani OR Canar
"Sudan" "data centre" "licence" TPRA
"اللائحة التنظيمية للتراخيص" "مركز بيانات" السودان
```

What to extract: licence class and holder, service scope (SaaS/cloud/colocation), licence number/date, corporate legal name (Sudatel Telecom Group, Zain Sudan Ltd, MTN Sudan, EBS...). TPRA records prove *authorisation*, not facility count — one licence can cover multiple facilities and vice versa.

---

## 2. Ministry of Digital Transformation and Telecommunications (MTDT)

- **Ministry of Digital Transformation and Telecommunications (MTDT)**: https://mtdt.gov.sd/ (Arabic) / https://mtdt.gov.sd/en (English). Search news and program pages for `data centre`, `مركز بيانات`, `cloud`, `e-government`, `التحول الرقمي`.
- **Programs and projects**: https://mtdt.gov.sd/en/programs — ministry program listing; includes digital-transformation program material (grade A for program existence, B/C for facility inference).
- **3x3 Digital Transformation Plan / CONSOLEX**: ministry/government mirrors describe phase-two digital-transformation work and a unified API gateway integrating government systems. Treat as e-government programme evidence, not a facility, unless a later MTDT/SUNA item names a hosting site or operator.
- **State data centre reactivation (9 Oct 2025)**: SUNA's Arabic post and Actum Sudan's 17 Oct 2025 summary report Minister Ahmed Dardiri confirming restoration/reactivation of the country's **main data centre in Khartoum — 1,300 m2 — equipped with cloud computing, data protection and AI-support systems**, intended to host government systems centrally. Grade **A** for the SUNA/ministerial announcement and **B** for Actum's English synthesis; grade current operational status separately and re-verify because Khartoum infrastructure remained fragile after the 2025 recapture.
- **Baladna platform** (Oct 2025): national IT/digital-transformation platform launched at a high-level meeting; **Khartoum chosen as pilot**. This is programme evidence and a tenant/demand signal. Do not count it as a facility unless a later official source names a data-centre site/operator.
- **SUNA (Sudan News Agency)**: https://suna-sd.net/ (Arabic; English mirror https://suna-news.net/en). Official news agency — primary channel for government DC/ICT announcements; search `مركز البيانات`, `البيانات الوطني`, `التحول الرقمي`.

MTDT/SUNA query templates:
```text
site:mtdt.gov.sd "data centre" OR "data center"
site:mtdt.gov.sd "مركز البيانات"
site:mtdt.gov.sd "التحول الرقمي" "بيانات"
site:suna-sd.net "مركز البيانات"
site:suna-sd.net "data centre" OR "digital transformation"
"خادم" OR "سيرفر" "وزارة التحول الرقمي" السودان
```

---

## 3. National Information Center (NIC) / National Data Centre (NDC) / SIXP

- **National Information Center (NIC, المركز القومي للمعلومات)**: https://www.nic.gov.sd/public/home — established by Constitutional Decree 363/1999, law enacted 1999, officially opened 30/09/2001; re-organised under the **National Information Center Act 2010** (repealing the 1999 act). Listed as an MTDT-affiliated body: https://mtdt.gov.sd/ar/digital/almrkz-alqwmy-llmlwmat. Mandate includes building and operating the **national information network** (شبكة المعلومات القومية) — i.e. the national backbone and data-centre infrastructure.
- **National Data Centre (NDC)**: hosted by NIC in Khartoum; evidence of existence/operation: ITU forum agenda (2016) listing "National Data Center, National Information Center, Sudan" staff; Sudan IXP traffic research referencing NDC + Sudanese Universities Information Network (SUIN) traffic at SIXP (ResearchGate paper, grade C for specifics but confirms NDC+SUIN interconnect).
- **SIXP (Sudan Internet Exchange Point)**: https://www.peeringdb.com/ix/2320 and http://www.sixp.sd — PeeringDB lists NIC as organisation, Khartoum as city, 4 peers (PCH AS42, PCH AS3856, Sudatel Telecom Group AS15706, Zain AS36998), prefixes 196.223.20.0/24 and 2001:43f8:7f0:1::/64, ~4G total capacity, last updated **2020-01-22**. PCH's IXP directory, however, marks SIXP **Defunct** and lists no facilities/switches. Treat SIXP as a **B-grade historical/stale interconnection lead**, not current operating proof; re-verify through NIC/SIXP, PeeringDB updates, live route-server stats, or operator confirmation before using it as facility evidence.
- **Reorganisation lead (May 2026, local press, grade C/B until official)**: local Arabic press reported NIC being transformed/renamed into the **Sudanese Data and Artificial Intelligence Authority (هيئة البيانات والذكاء الاصطناعي السودانية)**. Do not use the new name as A-grade until nic.gov.sd, mtdt.gov.sd, a decree, or SUNA confirms it. As of final review, MTDT still carried an NIC page with the 1999/2010 mandate and government hosting/VPS services.

NIC/SIXP query templates:
```text
site:nic.gov.sd "data centre" OR "مركز البيانات"
site:nic.gov.sd "شبكة المعلومات القومية"
"مركز البيانات الوطني" السودان
"National Data Centre" Sudan NIC
site:peeringdb.com/ix/2320
"SIXP" Sudan "National Information Center"
"مركز القومي للمعلومات" "مركز البيانات"
```

---

## 4. Energy and grid evidence

- Sudan has no public DC-specific energy register. Use energy evidence as a corroborating trail: transmission/substation references, power-supply agreements, generator/diesel claims, hydropower siting (Nile), and war-related power outages.
- **Ministry of Energy and Petroleum** (no verified public DC register found; search ministry news for `substation`, `grid`, `power supply`).
- **SETCo (Sudan Electricity Transmission Company)** — transmission operator; search for substation projects near Khartoum/Port Sudan and for `data centre` mentions.
- Aggregator context (inflect.com/datacenters/emea/sudan, grade C): industrial power ~$0.10/kWh, large Nile-hydro component, no direct cloud on-ramps as of Sep 2025, and redundant onsite generation expected for mission-critical facilities; disaster risk high, especially flooding. Use only as planning context.
- War: drone strikes damaged Khartoum power infrastructure in 2025 (Actum/SUNA, B); Feb 2024 nationwide shutdown after RSF occupied Khartoum data centres (B).

Energy query templates:
```text
"data centre" "substation" Sudan OR Khartoum OR "Port Sudan"
"data center" "generator" OR "diesel" Khartoum
"power supply agreement" "data centre" Sudan
"MVA" "data centre" Khartoum
site:setco.sd OR site:moep.gov.sd "data centre"
"انقطاع الكهرباء" "مركز بيانات" السودان
```

---

## 5. Official cloud-region and edge signals

| Provider | Official source | Sudan signal | How to use |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Sudan region on official list; Africa coverage includes South Africa; monitor only official AWS region/local-zone pages for future changes. | A-negative: do not infer facility. Use only as tenant/edge lead. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Sudan region; Africa public regions listed are South Africa North/West. | A-negative: no facility inference. |
| Google Cloud | https://cloud.google.com/about/locations | No Sudan region. | A-negative: no facility inference. |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No Sudan region; official list includes Morocco West (Casablanca) and South Africa Central (Johannesburg). | A-negative: no facility inference. |
| Local clouds | Sudani cloud https://cloud.sudani.sd/ ; NIC services | In-country cloud/hosting operated by Sudatel and NIC. | A for service existence; facility = Sudatel/NIC sites (join to operator pages). |

Cloud query templates:
```text
"cloud region" Sudan AWS OR Azure OR Google OR Oracle
site:cloud.sudani.sd "data center"
"السحابة" السودان "مركز بيانات"
```

---

## 6. Official/operator facility seed list

Operator pages are primary statements for marketed facility existence and city; they are not substitutes for operational-status evidence (especially in wartime).

| Operator / project | Official source | Sudan footprint signal | Follow-up joins |
|---|---|---|---|
| Sudatel Data Center / SDC Khartoum | https://sudani.sd/en/sdc/ ; https://www.sudatel.sd/en/data-center/ ; https://sudatel.sd/en/business-solutions/ | Official pages: largest/most advanced Sudan DC; 14,000 m2 facility, four equipped rooms with nearly 1,000 servers each; built to Tier IV standards on the DC page, while business page says the group operates two Tier III DCs. Services: colocation, dedicated/virtual servers, SAN storage, backup/recovery, firewall, DR, IaaS/cloud hosting; PaaS/SaaS described on business page. Contact/address pages place Sudatel at Sinkat Street, Khartoum; aggregators also use Sinkat Street. | Grade A for operator existence/service claims; grade tier claims as operator-stated, not certified, unless Uptime/independent certification appears. Join to war-status reporting, TPRA licence, power/generator evidence, and AS15706/SIXP only as stale network context. |
| Sudatel DC Port Sudan / SAS1 Port Sudan | Sudatel official business page says the group operates **two Tier III data centers** and lists EASSy, SAS1, SAS2 connectivity; Sudatel FY2025 release cites strategic stakes in EASSy/SAS-1/SAS-2, 25,000 km terrestrial fibre, 11,000 km subsea investments and Tier III+ DC infrastructure. Aggregators (C) identify Dim Al-Nour Street / SAS1 Port Sudan. | Red Sea state / Port Sudan — war-time government and telecom hub; data-centre existence is A at group/two-DC level, but exact Port Sudan street/capacity/status remains C unless confirmed by Sudatel/SUNA/cable operator. | Join to submarine-cable landing evidence (Submarine Cable Map/TeleGeography, EASSy/SAS1/SAS2 pages), TPRA, Port Sudan relocation reporting, and any Sudatel NOC/DR announcements. |
| NIC / State National Data Centre (NDC) | https://www.nic.gov.sd/ ; MTDT NIC page https://mtdt.gov.sd/ar/digital/almrkz-alqwmy-llmlwmat ; SUNA/Actum 2025 reactivation | State NDC in Khartoum; MTDT page assigns NIC the national information network and lists VPS/web-hosting services; Oct 2025 rehabilitation/reactivation of a 1,300 m2 state data centre announced by minister via SUNA. | Grade A for NIC mandate and SUNA/ministerial reactivation; resolve exact address and whether the 1,300 m2 state DC is physically the NIC/NDC site before de-duplicating. |
| Canar / Sudani legacy facility | inflect.com/datacenters/emea/sudan (C): "Canar Telecom Sudan Khartoum", Al-Mashtal Street, Khartoum | Legacy fixed-line operator facility (Canar merged into Sudani). | Verify current operator (Sudani) and whether it is a distinct facility vs Sudatel SDC; join TPRA and PeeringDB. |
| Zain Sudan core/DR | PeeringDB AS36998 at SIXP (stale B); Zain/Totogi/CSG press and case studies (2024-2025); Zain annual reports (official) | Evidence supports lost/disrupted on-prem telecom infrastructure, production/DR migration to Totogi on AWS, and group lobbying for fixed/data-centre-service rights. It does **not** identify a countable public Sudan colocation DC. | Treat as B/C operator-core/DR evidence only. Do not count as commercial facility unless Zain publishes a named site or regulator licence/facility evidence. |
| MTN Sudan | https://www.mtn.sd/ | Official site verified live; describes nationwide telecom infrastructure and digital-solutions ambitions but no public data-centre page was found. Expected core/server rooms in Khartoum. | C-grade lead only; search `MTN Sudan` + `data centre`/`مركز بيانات` + TPRA licences. |
| Electronic Banking Services (EBS) | LinkedIn/search lead; Sudan Tribune/CBOS-related press for SWIFT service-bureau status | Banking-sector centralised payment/SWIFT-service processing; likely technical facilities in Khartoum, but no verified official facility page found. | C-grade; join CBOS (Central Bank of Sudan) ICT reports and banking-press coverage. |

Operator query templates:
```text
"{operator}" Sudan "data centre" OR "data center" MW
"{operator}" Khartoum OR "Port Sudan" "مركز بيانات"
site:{operator-domain} "data centre"
"Sudatel" "Port Sudan" "data centre"
"Zain" OR "MTN" Sudan "data centre" "كهر" (power)
```

---

## 7. State-by-state enumeration approach (18 states)

### 7.1 Standard state workflow

For each of the 18 states:
1. Official-domain searches: state government site (where online), MTDT, SUNA, NIC, TPRA, operator pages.
2. English variants: `data centre`, `data center`, `datacentre`, `server room`, `server farm`, `cloud`, `colocation`, `hyperscale`, `Tier III`, `MW`.
3. Arabic variants: `مركز بيانات`, `مركز البيانات`, `استضافة`, `خوادم`, `سيرفرات`, `سحابة`.
4. Operator sweep: Sudatel/Sudani, Zain, MTN, NIC, EBS + state capital.
5. War-safety note: in active-conflict states (Darfur, Kordofan, parts of Blue Nile/Sennar), absence of evidence is the expected outcome; record negative search defensibly (state ministry + SUNA + operator sweep).

### 7.2 State coverage matrix (18 states)

Use this checklist to confirm that every first-order division has been swept. Only Khartoum and Red Sea have countable DC seeds; the other 16 states are negative/marginal unless a named state/NIC/operator facility appears.

| State | Capital / main towns | Expected DC result | Source route and special terms |
|---|---|---|---|
| Khartoum | Khartoum, Bahri/Khartoum North, Omdurman | **High**: Sudatel SDC, NIC/NDC/state DC, SIXP lead, telecom/banking core sites | `الخرطوم`, `مركز بيانات`, RSF occupation, rehabilitation, Sinkat, NIC, Sudatel |
| Red Sea | Port Sudan | **High**: Sudatel second DC / SAS1 lead, cable landings, war-time government hub | `بورتسودان`, EASSy, SAS1, SAS2, Dim Al-Nour, DR, NOC |
| River Nile | Atbara, Shendi, Berber | Negative/marginal: telecom exchanges, fibre corridor only | SUNA/state + Sudatel/Zain/MTN + `نهر النيل` |
| Northern | Dongola, Karima, Wadi Halfa | Negative/marginal: Nile corridor telecom | `الشمالية`, Dongola, Wadi Halfa + DC terms |
| Gezira | Wad Madani | Negative/marginal, war-disrupted telecom restoration leads only | `الجزيرة`, `ود مدني`, internet restoration, server room |
| White Nile | Kosti, Rabak, Ed Dueim | Negative/marginal: transport corridor telecom | `النيل الأبيض`, Kosti, Rabak + DC terms |
| Kassala | Kassala | Negative/marginal: east/refugee corridor ICT, GSM restoration | `كسلا`, LogCluster/ETC, state ICT |
| Gedaref / Al Qadarif | Gedaref | Negative/marginal: border/agriculture ICT | `القضارف`, Gedaref + DC terms |
| Sennar | Sennar/Singa | Negative/marginal; note 2025 blackout/power/drones only as context | `سنار`, Singa + DC terms |
| Blue Nile | Ed Damazin | Negative/marginal; drone/power outage context only | `النيل الأزرق`, Damazin, `الدمازين` |
| North Kordofan | El Obeid | Negative; active/legacy conflict, telecom outage leads only | `شمال كردفان`, El Obeid + DC terms |
| South Kordofan | Kadugli | Negative; active conflict | `جنوب كردفان`, Kadugli + DC terms |
| West Kordofan | Al-Fulah, Babanusa | Negative; oil/telecom corridor only | `غرب كردفان`, Al-Fulah, Babanusa |
| North Darfur | El Fasher | Negative; conflict zone | `شمال دارفور`, El Fasher + DC terms |
| South Darfur | Nyala | Negative; conflict zone | `جنوب دارفور`, Nyala + DC terms |
| West Darfur | El Geneina | Negative; conflict zone | `غرب دارفور`, Geneina + DC terms |
| East Darfur | Ed Daein | Negative; conflict zone | `شرق دارفور`, Ed Daein + DC terms |
| Central Darfur | Zalingei | Negative; conflict zone | `وسط دارفور`, Zalingei/`زالنجي` + DC terms |

### 7.3 Priority tiers

| Tier | States | Expected results | Queries to add |
|---|---|---|---|
| 1 — Khartoum | Khartoum (incl. Khartoum North/Bahri, Omdurman) | Highest density: Sudatel SDC, NIC/NDC, SIXP, Zain/MTN core, banking DCs; war-damage/occupation history (2023-2025), Oct 2025 rehabilitation, Baladna pilot. | `Khartoum "data centre"`, `الخرطوم "مركز بيانات"`, `RSF "data centre"`, `"main data centre" rehabilitation` |
| 2 — Red Sea | Red Sea (Port Sudan) | Sudatel DC Port Sudan, EASSy/SAS1/SAS2 landings, government relocation, digital-hub news. | `"Port Sudan" "data centre" OR "مركز بيانات"`, `cable landing EASSy SAS1 SAS2` |
| 3 — Nile corridor | River Nile (Atbara/Shendi), Northern (Dongola/Karima), Gezira (Wad Madani), White Nile (Kosti/Rabak) | Marginal: state ICT programmes, telecom exchanges, bank branches; commercial DC unlikely. | state name + `data centre`/`مركز بيانات` + `server room`; state gov ICT pages |
| 4 — East/Central | Kassala, Gedaref, Sennar, Blue Nile (Ed Damazin) | War-affected/refugee corridors; expect negative or humanitarian-ICT items only. | state name + `data centre`; SUNA sweep; humanitarian ICT (LogCluster notes Port Sudan/Kassala GSM restored) |
| 5 — Kordofan & Darfur | North/South/West Kordofan; North/South/West/East/Central Darfur (Zalingei) | Active/legacy conflict zones; treat as no-commercial-DC; defensible negative search only. | state name + `data centre`/`مركز بيانات`; SUNA + state ministry; do not count NGO server rooms as DCs |

### 7.4 State quick queries (English)

```text
Khartoum Sudan "data centre" OR "data center" OR datacentre
"Port Sudan" OR "Red Sea" Sudan "data centre" OR "data center"
"River Nile" OR Atbara Sudan "data centre" OR "data center"
Northern OR Dongola Sudan "data centre" OR "data center"
Gezira OR "Wad Madani" Sudan "data centre" OR "data center"
"White Nile" OR Kosti Sudan "data centre" OR "data center"
Kassala Sudan "data centre" OR "data center"
Gedaref Sudan "data centre" OR "data center"
Sennar Sudan "data centre" OR "data center"
"Blue Nile" OR "Ed Damazin" Sudan "data centre" OR "data center"
"North Kordofan" OR "South Kordofan" OR "West Kordofan" Sudan "data centre"
"North Darfur" OR "South Darfur" OR "West Darfur" OR "East Darfur" OR "Central Darfur" Sudan "data centre"
```

### 7.5 State quick queries (Arabic)

```text
الخرطوم "مركز بيانات"
"بورتسودان" OR "البحر الأحمر" "مركز بيانات"
"نهر النيل" OR عطبرة "مركز بيانات" السودان
"الجزيرة" OR "ود مدني" "مركز بيانات" السودان
"النيل الأبيض" OR كوستي "مركز بيانات" السودان
كسلا "مركز بيانات" السودان
القضارف "مركز بيانات" السودان
سنار "مركز بيانات" السودان
"النيل الأزرق" "مركز بيانات" السودان
"شمال كردفان" OR "جنوب كردفان" OR "غرب كردفان" "مركز بيانات"
"شمال دارفور" OR "جنوب دارفور" OR "غرب دارفور" OR "شرق دارفور" OR "وسط دارفور" "مركز بيانات"
```

---

## 8. Practical grading and de-duplication rules

- **Facility exists (A)** when an official operator/government page names the DC/service and location or when an official page states the operator has a defined facility footprint (Sudatel SDC Khartoum; Sudatel group two-DC statement; NIC/NDC/state DC). Street-level details still need their own grade.
- **Facility exists (B/C)** when only aggregators, stale interconnection databases, trade press, or local press support it (Canar Al-Mashtal, Port Sudan street/capacity, Zain core, MTN core, EBS).
- **Status claims are date-sensitive**: between 2023 and 2025, Khartoum facilities were occupied, damaged or offline; the state DC was rehabilitated Oct 2025. Always record the date of the evidence and re-verify current operation.
- **Cloud region != facility**: no hyperscaler region; local cloud (Sudani/NIC) maps to Sudatel/NIC sites only.
- **Government "data centre" ambiguity**: Baladna, 3x3 plan, CONSOLEX and state ICT programs are programme evidence, not facility records, unless a named site/operator is given.
- **De-duplication**: Sudatel SDC Khartoum appears as Sudatel DC Khartoum (datacentermap), "SDC" (sudani.sd), Sudatel Data Center (official), possibly confused with the Canar/Sudani Al-Mashtal facility — keep one canonical record per physical site (Sinkat St vs Al-Mashtal St) and note uncertainty.
- **Aggregator counts differ** (DataCenterMap 2 Sudatel sites, DataCenterPlatform 3 incl. Canartel, Inflect 1 Canar): same small pool of facilities; use aggregators only for discovery of names/addresses, never for A-grade status or capacity.
- **Telecom switches / server rooms** are not commercial datacentres; exclude unless the source describes hosting/colocation/cloud services at a named facility.

---

## 9. Source priority checklist

1. TPRA licence class/page and licensee records (data-centre/cloud/SaaS licence).
2. MTDT + SUNA official announcements (state DC rehabilitation, 3x3 plan, Baladna, e-government).
3. NIC official site + NDC/SIXP records (nic.gov.sd, sixp.sd, PeeringDB ix 2320).
4. Operator official facility pages (Sudatel/Sudani; Zain/MTN where they publish).
5. Energy/grid evidence (substation, generator, hydro context) as corroboration only.
6. Cable-consortium records (EASSy, SAS1, SAS2) for Port Sudan connectivity.
7. Reputable press (Dabanga, Actum Sudan, Sudan Tribune) for status updates, dated.
8. Aggregators (datacentermap, datacenterplatform, inflect, colo.exchange) for discovery only.
