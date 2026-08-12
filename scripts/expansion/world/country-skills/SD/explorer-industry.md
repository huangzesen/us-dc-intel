# SD Explorer — Industry / Press / Vendor Discovery for Sudan Datacentres

Date: 2026-08-12. Scope: Sudan (SD) datacentre enumeration from industry media, local business press, operator/vendor pages, interconnection records, and state-level search patterns. Reliability grades: **A** = official/primary (operator page, government/SUNA/TPRA/NIC document, cloud-provider page), **B** = strong secondary (trade press, established local press, PeeringDB/PCH, vendor press release), **C** = aggregator, social post, old MoU, market-report snippet, or unverifiable local mention.

---

## 0. Sudan-specific frame

- Sudan has **no public facility registry** and only a handful of known datacentre assets. Discovery works by triangulating **operator pages (Sudatel/Sudani)**, **government/SUNA reporting** (state DC, 3x3 digital-transformation plan, Baladna), **interconnection records** (SIXP/PeeringDB), **cable-consortium material** (EASSy, SAS1, SAS2 at Port Sudan), **aggregators** (datacentermap, datacenterplatform, inflect, colo.exchange), and **local press** (Dabanga, Sudan Tribune, Altaghyeer, Actum Sudan).
- Commercial and state activity is concentrated in **two clusters**:
  - **Khartoum state** (Khartoum city, Bahri/Khartoum North, Omdurman): Sudatel Data Center (SDC), NIC National Data Centre + SIXP, legacy Canar/Sudani facility (Al-Mashtal St), Zain/MTN core and DR, banking/e-payment (EBS/CBOS) facilities.
  - **Red Sea state / Port Sudan**: Sudatel second-DC/SAS1 lead, EASSy/SAS1/SAS2 cable landings, de-facto war-time government and telecom relocation hub. Sudatel officially states it operates two Tier III DCs, but aggregators supply the Port Sudan street/capacity details.
  - All other 16 states are expected **negative or marginal** (state ICT programmes, telecom exchanges, bank server rooms only).
- **War context dominates**: since April 2023, Khartoum data centres/ISP facilities were reportedly seized or occupied (Feb 2024 nationwide shutdown), internet was repeatedly shut down, SAF retook key Khartoum sites in March 2025 and claimed Khartoum state clear in May 2025, and the main state DC (1,300 m2) was rehabilitated/reactivated on **9 October 2025**. Status claims must carry a date and be re-verified; many pre-2023 press items describe facilities whose current state is unknown.
- **Languages**: English for trade press and operator EN pages; Arabic for local press and government material. Use both spellings `data centre` / `data center` / `datacentre` and Arabic `مركز بيانات`, `استضافة`, `خوادم`, `سيرفرات`, `سحابة`.
- **Hyperscale/cloud**: official AWS, Azure, Google Cloud and OCI region lists show no Sudan region as of Aug 2026. Aggregator data also claims no direct cloud on-ramp in Sudan as of Sep 2025, but keep that on-ramp point C-grade. Local cloud/hosting is offered by **Sudani (cloud.sudani.sd)** and NIC. Zain Group is lobbying for "right to offer fixed/data-centre services" in annual-report regulatory priorities, but that is not a facility.

---

## 1. Industry and local press sources

Use press to discover project names, operators, states, status verbs, and war-impact facts; then verify with an operator, TPRA/MTDT/SUNA, NIC, or cable-consortium source.

| Source | URL / query route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/news/ | Global trade feed; direct Sudan coverage is rare but appears via Africa-wide items (Sudatel, Zain). Use `site:` queries. | B |
| Capacity Media / Developing Telecoms / Balancing Act / IT News Africa / CIO Africa | site-scoped searches | African telecom/digital-infra trade press; useful for Zain Sudan, MTN Sudan, Sudatel, cable and data-centre announcements. | B |
| SUNA (Sudan News Agency) | https://suna-sd.net/ , EN mirror https://suna-news.net/en | Official state news; primary for government DC/ICT announcements (Oct 2025 state DC reactivation). | A when quoting officials |
| Dabanga | https://www.dabangasudan.org/ | Strong independent Sudan news (EN/AR); war/internet-shutdown and infrastructure damage coverage. | B |
| Sudan Tribune | https://sudantribune.com/ | Sudan-focused press; ICT/digital and government items. | B |
| Altaghyeer | https://www.altaghyeer.info/ | Independent Arabic Sudan press; e-government/ICT items. | B/C |
| Actum Sudan (Substack) | https://actumsudan.substack.com/ | Concise Sudan policy/digital briefs (e.g. "Sudan Pushes Digital Transformation with Reopening of Khartoum Data Centre", Oct 2025). | B |
| Sudan Horizon / khatwapress / ecosudan / alnilin | site-scoped | Local Arabic outlets for NIC reorganisation ("Sudanese Data and Artificial Intelligence Authority", May 2026), Baladna, ministry news. | B/C |
| Zain Group annual reports | https://zain.com/ | Official group disclosures incl. Sudan OPCO status and data-centre-services ambitions. | A/B |
| Totogi / Light Reading / cloudcomputing-news | https://totogi.com/newsroom/ , https://www.lightreading.com/ , https://www.cloudcomputing-news.net/ | Zain Sudan BSS-on-cloud + production/DR hosting (2025); Zain Sudan connectivity restoration during war. | B |
| PeeringDB / PCH / sixp.sd | https://www.peeringdb.com/ix/2320 , https://www.pch.net/ixp/details/1312 , http://www.sixp.sd | PeeringDB lists SIXP in Khartoum with PCH, Sudatel AS15706 and Zain AS36998, but last update is 2020-01-22; PCH marks SIXP **Defunct** with no facilities/switches. Use as a stale/historical interconnection lead only. | B/C |
| Aggregators: DataCenterMap, DataCenterPlatform, Inflect, DC Hub, colo.exchange, PQ.Hosting | https://www.datacentermap.com/sudan/ , https://datacenterplatform.com/countries/sudan/ , https://inflect.com/datacenters/emea/sudan | Discovery only: Sudatel DC Khartoum (Sinkat St), Sudatel DC Port Sudan/SAS1 (Dim Al-Nour St), Canar/Canartel/Canar Telecom Sudan (Al-Mashtal St). Aggregator counts conflict (1-3), so never use alone for A-grade status/capacity. | C |
| Vendor case studies | Huawei, ZTE, Ericsson, Vertiv, Schneider, diesel/gen suppliers | Construction/equipment evidence if it names a Sudan site; usually B/C. | B/C |

Trade-press query templates:
```text
site:datacenterdynamics.com/en/news/ Sudan "data centre"
site:developingtelecoms.com Sudan "data centre" OR "data center"
site:balancingact-africa.com Sudan data centre
site:cioafrica.co OR site:itnewsafrica.com Sudan "data centre"
site:dabangasudan.org "data centre" OR "مركز بيانات" OR "internet shutdown"
site:sudantribune.com "data centre" OR "التحول الرقمي"
site:suna-sd.net "مركز البيانات" OR "data centre"
"Sudan" "data centre" "Port Sudan" OR Khartoum 2024 OR 2025
```

Capture the exact lifecycle/status verb and date: `announces`/`MoU`/`plans` = intent (C/B); `rehabilitates`/`reactivates`/`reopens` = post-war restoration (B/A if official); `occupied`/`damaged`/`shutdown` = war status (B, date-stamp); `operational`/`launched`/`hosts` = operational signal (verify with operator/official page for A).

---

## 2. Operator and vendor sweep

| Operator / project | Official / primary URL | Sudan signals | Notes |
|---|---|---|---|
| Sudatel Telecom Group / Sudani | https://www.sudatel.sd/ , https://sudani.sd/ , DC pages https://sudani.sd/en/sdc/ and https://www.sudatel.sd/en/data-center/ , business page https://sudatel.sd/en/business-solutions/ , cloud https://cloud.sudani.sd/ | Official Khartoum DC page: 14,000 m2, 4 rooms nearly 1,000 servers each, Tier IV-standard claim; services include colocation, dedicated/virtual servers, SAN/storage, DR, IaaS. Business page states Sudatel operates **two Tier III data centers** and offers PaaS/SaaS; FY2025 release cites Tier III+ DC infrastructure and EASSy/SAS-1/SAS-2 stakes. | A for official service/facility existence; tier is operator-stated unless certification appears. Port Sudan street/capacity is C until Sudatel or SUNA confirms. Verify Khartoum operational status post-war. |
| Zain Sudan | https://www.zain.com/ (group), PeeringDB AS36998, Totogi/CSG/cloud case studies | Strong evidence for disrupted on-prem telecom infrastructure and migration of charging/production/DR workloads to Totogi on AWS in 2024-2025; no public marketed Sudan colocation page found; group regulatory priorities include right to offer fixed/data-centre services. | B/C for operator-core lead only; A/B for group disclosures and vendor migration facts. Do not count as a public DC. |
| MTN Sudan | https://www.mtn.sd/ | Official site verified live; expected core/server rooms in Khartoum, but no public DC page/evidence found. | C lead only. |
| NIC / National Data Centre / SIXP | https://www.nic.gov.sd/ , MTDT NIC page, http://www.sixp.sd | State NDC + national information network/government hosting in Khartoum; 1,300 m2 state DC reactivation announced Oct 2025. SIXP is stale/possibly defunct per PCH. Local 2026 rename/reorganisation reports remain unconfirmed officially. | A for NIC mandate/state DC announcement; B/C for SIXP current status and rename lead. |
| Canar / Canartel (legacy fixed-line, Sudatel/Sudani family) | Inflect entry: Canar Telecom Sudan, Al-Mashtal St, Khartoum; DataCenterPlatform Canartel DC | Legacy operator facility; possibly distinct from Sudatel SDC, possibly duplicate/legacy listing. | C; join TPRA/Sudani/legal-address evidence before counting. |
| Electronic Banking Services (EBS) | LinkedIn/search lead; CBOS/Sudan Tribune press for SWIFT-service-bureau status | National e-payment / banking infrastructure lead; centralised payment and SWIFT-service processing imply technical facilities, but no verified public DC page found. | C lead; join CBOS/banking press before counting. |
| SUDASAT | Sudatel Wikipedia (B) | Satellite backhaul/enterprise connectivity (Sudatel 60%); satellite ground infrastructure, not a DC per se. | Exclude as DC unless hosting evidence appears. |
| ISPs / hosting resellers | e.g. legacy ISPs, local web hosts | Small server rooms/VPS resale on Sudatel/Canar infrastructure. | C; do not double-count behind Sudatel facilities. |
| Vendors | Huawei, ZTE, Ericsson, Totogi, Schneider, Vertiv, diesel genset suppliers | Equipment/construction evidence if a named Sudan site is given. | B/C. |

Operator query templates:
```text
"{operator}" Sudan "data centre" OR "data center" ("MW" OR racks OR hosting OR colocation)
"{operator}" Khartoum OR "Port Sudan" "مركز بيانات" OR استضافة
site:{operator-domain} "data centre" OR "data center" OR cloud
"Sudatel" "data centre" "Sinkat" OR "Port Sudan"
"Zain Sudan" "data centre" OR hosting OR "disaster recovery"
"MTN Sudan" "data centre" OR "server" Khartoum
```

---

## 3. Official/semi-official channels to pivot from press

| Channel | URL / route | How to use | Grade |
|---|---|---|---|
| TPRA | https://tpra.gov.sd/en/ , licensing https://tpra.gov.sd/en/services/telecom-licensing/ | Licence classes incl. third-class cloud-via-private-data-centre (SaaS) licence per 2019 Licensing Regulation; licensee records. | A when record found |
| MTDT | https://mtdt.gov.sd/ , programs https://mtdt.gov.sd/en/programs | 3x3 digital-transformation plan, CONSOLEX API gateway, Baladna platform; ministry news. | A for programme/announcement |
| SUNA | https://suna-sd.net/ | Official DC reactivation and e-government announcements. | A when quoting officials |
| NIC / SIXP | https://www.nic.gov.sd/ , http://www.sixp.sd , PeeringDB ix 2320 | NDC, national information network, IXP members. | A/B |
| Cable consortia | EASSy (eassy.org), SAS1/SAS2 (via Sudatel/STC pages) | Port Sudan landing points and PoPs; connectivity, not DC capacity. | B |
| CBOS / Central Bank of Sudan | https://cbos.gov.sd/ | Banking-sector ICT context; no public DC register found. | B/C |
| State governments | state-name + `gov.sd` domains (many offline post-war) | State ICT/digital programmes; mostly programme-level, not facility records. | C unless facility named |

Pivot templates:
```text
site:tpra.gov.sd "{operator}" licence
"{project}" site:suna-sd.net OR site:mtdt.gov.sd
"{project}" "مركز البيانات" السودان
"{project}" EIA OR permit OR licence OR TPRA Sudan
```

---

## 4. English and Arabic search patterns

### 4.1 English
```text
"{state}" Sudan ("data centre" OR "data center" OR datacentre) ("MW" OR racks OR hosting OR colocation)
"{town}" Sudan ("data centre" OR "data center") (reopened OR reactivated OR operational OR construction)
"{state}" Sudan (colocation OR "carrier-neutral" OR hyperscale OR cloud)
"{state}" Sudan ("Tier III" OR "Tier IV") "data centre"
"{operator}" "{state OR town}" Sudan "data centre"
"{project}" ("MW" OR "IT load" OR racks OR sqm OR "square metres")
"{project}" (rehabilitation OR reopening OR occupation OR damage OR shutdown)
```

### 4.2 Arabic
- data centre: `مركز بيانات` (also `مركز البيانات`, `مركز بيانات ضخم`)
- national data centre: `مركز البيانات الوطني` / `المركز القومي للبيانات`
- hosting: `استضافة`; servers: `خوادم` / `سيرفرات`; cloud: `سحابة` / `الحوسبة السحابية`
- digital transformation: `التحول الرقمي`; e-government: `الحكومة الإلكترونية`; ICT: `تقنية المعلومات`
- open/launch: `افتتاح` / `إعادة تأهيل` (rehabilitation) / `تفعيل` (activation)

```text
"{state}" "مركز بيانات" السودان
"{state}" "استضافة" OR "خوادم" السودان
"الخرطوم" OR "بورتسودان" "مركز البيانات"
"إعادة تأهيل" "مركز البيانات" السودان
"التحول الرقمي" "مركز بيانات" السودان
```

Do not count an Arabic-language hit as a commercial datacentre unless it identifies a physical facility with compute/hosting function, an operator/owner, and a stage.

---

## 5. State-level enumeration method (18 states)

Run four passes per state:
1. **Press/vendor pass**: state + main towns + DC terms (EN + AR).
2. **Operator pass**: Sudatel/Sudani, Zain, MTN, NIC, EBS + state capital.
3. **Official pass**: SUNA, MTDT, NIC, TPRA, state gov ICT pages.
4. **Interconnection/aggregator pass**: SIXP/PeeringDB, datacentermap, datacenterplatform, inflect; verify before grading above C.

### 5.1 Exact 18-state coverage matrix

| State | Main towns/localities | Expected result | Notes |
|---|---|---|---|
| Khartoum | Khartoum, Bahri/Khartoum North, Omdurman | Positive/high | Sudatel SDC, NIC/NDC/state DC, SIXP lead, Canar/Canartel, Zain/MTN/EBS core leads; always date status. |
| Red Sea | Port Sudan | Positive/high | Sudatel second DC/SAS1 lead, EASSy/SAS1/SAS2 cable landings, government/telecom relocation. |
| River Nile | Atbara, Shendi, Berber | Negative/marginal | Fiber/telecom corridor; no commercial DC found. |
| Northern | Dongola, Karima, Wadi Halfa | Negative/marginal | Nile corridor; telecom/server-room leads only. |
| Gezira | Wad Madani, Hasaheisa | Negative/marginal | War-disrupted telecom restoration and university/ICT leads only. |
| White Nile | Kosti, Rabak, Ed Dueim | Negative/marginal | Transport/telecom corridor only. |
| Kassala | Kassala | Negative/marginal | Humanitarian/telecom restoration leads only. |
| Gedaref / Al Qadarif | Gedaref | Negative/marginal | Border/agricultural ICT only. |
| Sennar | Sennar, Singa | Negative/marginal | Power/blackout context only unless a site is named. |
| Blue Nile | Ed Damazin | Negative/marginal | Power/drone/telecom context only. |
| North Kordofan | El Obeid | Negative | Active/legacy conflict; no commercial DC expected. |
| South Kordofan | Kadugli | Negative | Active conflict; no commercial DC expected. |
| West Kordofan | Al-Fulah, Babanusa | Negative | Oil/telecom corridor only. |
| North Darfur | El Fasher | Negative | Conflict zone; do not count NGO/server rooms. |
| South Darfur | Nyala | Negative | Conflict zone. |
| West Darfur | El Geneina | Negative | Conflict zone. |
| East Darfur | Ed Daein | Negative | Conflict zone. |
| Central Darfur | Zalingei | Negative | Conflict zone; include Zalingei/زالنجي variants. |

### 5.2 Priority clusters

| State | Main towns/localities | Seeds | Query notes |
|---|---|---|---|
| Khartoum | Khartoum, Bahri/Khartoum North, Omdurman | Sudatel SDC (Sinkat St), NIC/NDC, SIXP, Canar Al-Mashtal, Zain/MTN core, EBS | Highest priority; add war-status terms (RSF, occupation, rehabilitation, Feb 2024 shutdown). |
| Red Sea | Port Sudan | Sudatel DC Port Sudan (Dim Al-Nour St), EASSy/SAS1/SAS2 landings, gov relocation | Second priority; cable + relocation + digital-hub terms. |
| River Nile | Atbara, Shendi, Berber | Telecom/rail corridor facilities | Marginal; expect negative. |
| Northern | Dongola, Karima, Wadi Halfa | Nile corridor telecom | Marginal; expect negative. |
| Gezira | Wad Madani, Hasaheisa | Agriculture-state ICT, university ICT | Marginal; expect negative post-war. |
| White Nile | Kosti, Rabak, Ed Dueim | Transport corridor telecom | Marginal; expect negative. |
| Kassala / Gedaref / Sennar / Blue Nile | state capitals | Refugee/humanitarian corridors; LogCluster notes Port Sudan/Kassala GSM restored | Negative unless ICT reporting appears. |
| North/South/West Kordofan | El Obeid, Kadugli, Babanusa | Active/legacy conflict | No commercial DC expected. |
| North/South/West/East/Central Darfur | El Fasher, Nyala, Geneina, Zalingei, Ed Daein | Conflict zones; Zalingei = Central Darfur local variant | No commercial DC expected; defensible negative search only. |

### 5.3 Exact 18-state quick queries (EN + AR)
```text
Khartoum Sudan "data centre" OR "data center" OR datacentre OR "مركز بيانات"
"Red Sea" OR "Port Sudan" Sudan "data centre" OR "مركز بيانات"
"River Nile" OR Atbara Sudan "data centre" OR "مركز بيانات"
Northern OR Dongola Sudan "data centre" OR "مركز بيانات"
Gezira OR "Wad Madani" Sudan "data centre" OR "مركز بيانات"
"White Nile" OR Kosti Sudan "data centre" OR "مركز بيانات"
Kassala Sudan "data centre" OR "مركز بيانات"
Gedaref Sudan "data centre" OR "مركز بيانات"
Sennar Sudan "data centre" OR "مركز بيانات"
"Blue Nile" OR "Ed Damazin" Sudan "data centre" OR "مركز بيانات"
"North Kordofan" OR "South Kordofan" OR "West Kordofan" Sudan "data centre"
"North Darfur" OR "South Darfur" OR "West Darfur" OR "East Darfur" OR "Central Darfur" OR Zalingei Sudan "data centre"
```

---

## 6. Hyperscaler and cloud-region handling

| Provider | Official/primary URL | Sudan signal | How to use |
|---|---|---|---|
| AWS / Azure / GCP / OCI | official region pages (see explorer-official.md §5) | No Sudan region on official lists. On-ramp absence is C-grade aggregator context unless verified by the provider/interconnect operator. | A-negative for regions; do not infer facilities. |
| Sudani cloud | https://cloud.sudani.sd/ | In-country VPS/hosting/connectivity on Sudatel DC infrastructure. | A for service; facility = Sudatel sites. |
| NIC/government cloud | https://www.nic.gov.sd/ + MTDT programs | State hosting/cloud services on NDC. | A for service; facility = NDC site. |
| Zain ambitions | Zain annual report 2023 (B) | Group seeking data-centre-services licence rights incl. Sudan. | Monitor for future facility announcements. |

---

## 7. Evidence grading and common pitfalls

### 7.1 Grade per data point
- **A**: operator official facility page (Sudatel/Sudani, NIC); SUNA/official announcement; TPRA licence record; cable-consortium official page.
- **B**: DCD/Developing Telecoms/Balancing Act/IT News Africa/CIO Africa, Dabanga, Sudan Tribune, Actum Sudan, Zain Group reports, Totogi/Light Reading, PeeringDB/PCH.
- **C**: aggregator facility pages, market-report snippets, social posts, pre-2023 "plans/MoU" articles without later evidence.

### 7.2 Sudan-specific pitfalls
- **War-status decay**: anything written 2023-2025 about Khartoum DCs may be obsolete within weeks (occupation, damage, shutdown, March/May 2025 recapture claims, Oct 2025 rehabilitation). Date every record; prefer Oct 2025+ sources for Khartoum status and still re-check current operation.
- **Sudatel vs Canar/Canartel vs Sudani naming**: Sudatel, Sudani and legacy Canar/Canartel are the same corporate family or legacy-adjacent listings; Sinkat St (SDC) and Al-Mashtal St (Canar) may be distinct sites or duplicate legacy entries. Avoid double-counting without address-level/operator confirmation.
- **"Data centre" in Arabic press** often means a government IT room, records centre, or telecom exchange. Require compute/hosting function + operator + location.
- **Aggregator duplication**: datacentermap (2), datacenterplatform (3), inflect (1) all point to the same small pool; reconcile by operator+street before recording.
- **Government programmes vs facilities**: 3x3 plan, CONSOLEX, Baladna, state ICT plans are programmes; record as facilities only when a named site/operator appears.
- **No hyperscaler region**: any "cloud region" claim should be treated as service/partner news, not new-build evidence.


## 8. Final verification notes added 2026-08-12

- Verified live/accessible: TPRA telecom licensing page with cloud-via-private-data-center SaaS third-class licence language; Sudatel/Sudani DC, business and cloud pages; MTDT NIC page; PeeringDB SIXP page; PCH SIXP page; major hyperscaler region lists.
- Corrected grades: SIXP current operation downgraded to stale B/C because PCH marks it defunct; Port Sudan exact address/capacity kept C because official Sudatel evidence confirms two DCs and cable assets but not the street details; Zain kept as operator-core/DR lead, not a countable commercial facility.
- Coverage complete: all 18 Sudan states are enumerated above; only Khartoum and Red Sea have positive facility seeds, with the other 16 states requiring defensible negative sweeps.
