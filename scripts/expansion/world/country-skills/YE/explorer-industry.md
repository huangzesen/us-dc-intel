# YE Explorer Industry - Yemen Datacenter Enumeration via Trade Press, Operator Pages, Local Media, and Arabic/English Search Patterns

Date: 2026-08-12. Country: **YE Yemen**. Scope: industry / press / vendor-led discovery for Yemeni data centers and institutional compute facilities, with official verification routes for every lead. Division model: 22 first-level divisions in this expansion manifest (Abyan, Aden, Amran, Beida, Dhale, Dhamar, Hadhramaut, Hajjah, **Western Coast = Al Hudaydah/Hodeidah search space**, Ibb, Jouf, Lahij, Marib, Mahra, Mahwit, Raymah, Sanaa City, Saada, Shabwah, Sanaa, Socotra, Taiz).

Reliability grades: **A** = official / primary for the exact fact claimed (MTIT Aden or Sana'a, Saba news agency either variant, PTC/YemenNet official or Saba-reported statement, TeleYemen, AdenNet + RIPE record, NIC, CSO, UN/World Bank/ITU document, official operator page, official cloud-region page, Uptime record). **B** = strong secondary / trade press (Sana'a Center for Strategic Studies, Yemen Monitor, Barran Press, Aden Times, DCD, Capacity Media, Developing Telecoms, Telecompaper, TeleGeography/Submarine Cable Map, BuddeComm, GSMA, vendor case study naming client and site). **C** = weak lead (DataCenterMap, datacenters.com, Cloudscene, Baxtel, Inflect, PeeringDB-only records, Wikipedia, social posts, market-report PR snippets, inaccessible snippets, yemenhr.com tender aggregator unless original opened).

---

## 0. Yemen market frame

- Yemen has **no mature commercial colocation market and no public data-center registry**. Data-center-class infrastructure is **state-carrier, government, banking, oil, university, UN-mission, or small hosting-provider** infrastructure, concentrated in **Sana'a (Ansar Allah-controlled) and Aden (IRG-controlled)**, with strategic outposts at cable landings (Aden, Al Ghaydah/Mahra, Al Hudaydah/Western Coast) and oil/governorate nodes (Hadhramaut, Marib, Shabwah, Taiz).
- **Dual-administration rule**: since 2014-2015 there are two governments; institutions exist twice (MTIT, NIC, Central Bank, even the news agency 'Saba'). Always record which side controls the evidence; never merge the two evidence sets silently.
- **Sources are Arabic-first.** High-value English sources: UN/World Bank documents, DCD/Capacity/Developing Telecoms, TeleGeography, BuddeComm, Sana'a Center. Arabic sources: Saba (both variants), Al-Masirah (Houthi), Al-Thawra, Yemen Monitor, Barran Press, Aden Times, Al-Masdar Online, Al-Ayyam, and Facebook/Telegram of operators and NICs.
- **War status matters for every lead**: World Bank and Sana'a Center work document severe telecom damage, fuel/power constraints, institutional fragmentation, and repeated submarine-cable outages. World Bank's 2023 broadband-redundancy study treats FALCON and Aden-Djibouti as Yemen's only active subsea cables at that time; AAE-1 at Aden exists as a landing but should not be treated as stable active Yemen capacity without a fresh status source. Do not mark war-zone facilities operational without date-stamped evidence.
- **Power**: grid is unreliable; diesel + solar at sites. Do not infer MW-scale DCs. Treat kW/kVA claims cautiously and only when site-named.
- **No hyperscaler region**: AWS/Azure/GCP/OCI official region lists show no Yemen region as of 2026-08-12; `Yemen cloud` claims are hosting/sovereign services, not hyperscaler regions.

Core query set (EN + AR):

```text
Yemen "data center" OR "data centre" OR datacenter (Sana'a OR Aden OR Mukalla)
اليمن "مركز بيانات" (صنعاء OR عدن OR المكلا)
اليمن "مراكز البيانات" "الحوسبة السحابية"
Yemen "sovereign cloud" OR "cloud" hosting Sana'a OR Aden
"TeleYemen" OR "YemenNet" OR "AdenNet" "data center"
"البنك المركزي اليمني" "مركز بيانات" OR "أنظمة الحاسوب"
Yemen bank "disaster recovery" "data center"
"Sabafon" OR "Yemen Mobile" OR "YOU Yemen" "data center" OR "core network"
Yemen university "data center" OR "server room" OR "e-learning"
Yemen submarine cable landing station "Aden" OR "Ghaydah" OR "Hodeidah"
```

Arabic vocabulary for status and facility words:

```text
مركز بيانات = data center
مراكز البيانات = data centers
مركز المعلومات = information center
غرفة الخوادم = server room
استضافة المواقع = web hosting
الحوسبة السحابية = cloud computing
محطة الأرضية = earth station
كبل بحري = submarine cable
تدشين / افتتاح / إطلاق = inauguration / launch (operational claim)
مذكرة تفاهم = MoU (planned)
مناقصة / مزاد = tender / auction (procurement)
التحول الرقمي = digital transformation
اليمن = Yemen; عدن = Aden; صنعاء = Sana'a; المكلا = Mukalla; الحديدة = Al Hudaydah; الغيضة = Al Ghaydah
```

---

## 1. High-signal trade and press sources

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Saba (Aden variant, IRG) | https://www.sabanew.net/ | Official ministry/government announcements incl. telecom, AdenNet, infrastructure | A |
| Saba (Sana'a variant, Ansar Allah) | https://www.saba.ye/ | Official announcements from Sana'a-side MTIT, YemenNet, NIC; includes PTC report describing hosted-server spaces in DATA CENTER facilities and 69 hosted companies (`https://saba.ye/ar/news3243831.htm`) | A (for Sana'a-side facts) |
| Al-Masirah (Ansar Allah) | https://english.masirahtv.net/ | Houthi-side telecom/infrastructure coverage | A/B (state-aligned media) |
| Yemen Monitor | https://www.yemenmonitor.com/ | IRG-side project news (e.g., PM Bin Brik Aden telecom plan, 2025-06-22) | B |
| Barran Press | https://en.barran.press/ | Ministry statements in EN (e.g., AdenNet Phase 2, Nov 2024) | B |
| Aden Times | http://aden-tm.net/ | Southern business/telecom coverage | B/C |
| Al-Masdar Online / Al-Ayyam / Al-Thawra | site-scoped | Local EN/AR reporting on telecom, banks, universities | B/C |
| Sana'a Center for Strategic Studies | https://sanaacenter.org/ (telecom paper https://sanaacenter.org/publications/policy-research/12721) | Authoritative sector structure, cables, war damage | B (research org) |
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/news/ | Global DC trade press; sparse Yemen coverage; use Yemen-tag search | B when present |
| Capacity Media | https://capacitymedia.com/ | Connectivity/cable news; Yemen cables occasionally | B |
| Developing Telecoms / Telecompaper | site-scoped | Telecom regulatory/operator news | B |
| TeleGeography | https://www.submarinecablemap.com/ and https://www2.telegeography.com/ | Cable landings (FALCON, AAE-1, Aden-Djibouti) | B/A |
| AAE-1 consortium | https://www.aaeone.com/ | AAE-1 system route and Aden/TeleYemen landing evidence | A/B for cable landing; status still needs current evidence |
| BuddeComm / market reports | https://www.budde.com.au/Research/Yemen-Telecoms-Mobile-and-Broadband-Statistics-and-Analyses | Market structure, operator shares, MTN exit | B/C |
| GSMA / ITU ICT-Eye | https://www.gsma.com/ , https://www.itu.int/net4/ITU-D/icteye/ | Subscriber/penetration stats; context | B/A |
| World Bank / UN documents | https://documents.worldbank.org/ , https://www.ungm.org/ | ICT policy notes, Yemen Economic Updates, UN procurement for telecom/data | A/B |
| CodaStory / Recorded Future | internet-in-conflict coverage | Context on internet control (YemenNet seizure, AdenNet creation) | C/B |
| Operator / vendor pages | Sabafon, YOU, Yemen Mobile, Y Telecom, TeleYemen, YemenNet, AdenNet, NIC, Huawei, ZTE | Service/facility claims; A for service, B/C for facility detail | A/B/C |
| Directories | DataCenterMap, datacenters.com, Cloudscene, Baxtel, Inflect, PeeringDB | Facility names/addresses; must be corroborated. Example: Inflect lists "Yemen Net Al Hudaydah" with power claims; keep C until PTC/YemenNet/official evidence supports address/capacity. | C |

Trade-press query templates:

```text
site:datacenterdynamics.com Yemen "data center"
site:datacenterdynamics.com "TeleYemen" OR "Yemen" cable OR gateway
site:capacitymedia.com Yemen cable OR "data centre"
site:developingtelecoms.com Yemen
site:telecompaper.com Yemen
site:sanaacenter.org Yemen telecommunications "data"
site:yemenmonitor.com "telecommunications" OR "internet" OR "data"
site:barran.press "AdenNet" OR "data"
"Yemen" "data center" "Saudi" OR "UAE" OR "China" OR "Huawei"
"اليمن" "مركز بيانات" "هواوي" OR "السعودية" OR "الإمارات"
```

Status-language interpretation:

- `مذكرة تفاهم` / `MoU` / `اتفاق` / `partnership` = planned / lead. Verify site and stage.
- `مناقصة` / `tender` / `عطاء` = procurement. Stronger when the original buyer document or UNGM/WB notice is opened.
- `تدشين` / `افتتاح` / `إطلاق` / `inaugurated` / `launched` = operational claim. Verify with official operator/ministerial source.
- `دمار` / `destroyed` / `out of service` = damaged/unused. For status-sensitive cable leads such as FALCON Hudaydah or AAE-1 Aden, record the exact current status from dated evidence; do not rely on stale status labels.
- `استضافة` / `cloud` / `VPS` / `hosting` = service evidence only unless a physical facility is named.

## 2. Operator and vendor sweep

| Operator / entity | Main URL | Likely geography | Search / verification notes |
|---|---|---|---|
| TeleYemen | https://www.teleyemen.com.ye/ and https://website.teleyemen.com.ye/ | Sole international gateway; hosting on TeleYemen servers; Sana'a HQ and branches in Aden/Hodeidah/Mukalla/Seiyun; VSAT/data services | A for gateway/hosting/branch facts. Landing stations: Aden (Aden-Djibouti, AAE-1), Al Ghaydah (FALCON), Al Hudaydah (FALCON, status-sensitive). |
| YemenNet / PTC | yemen.gov.ye, Saba Sana'a PTC report `https://saba.ye/ar/news3243831.htm` | Sana'a ADSL platform core; PTC DATA CENTER hosted-server spaces; governorate switching centers | A for state-ISP and PTC hosting/data-center service; C for DC inference from bulletin or directory data. |
| AdenNet | https://www.adennet4g.net/ ; RIPE member page; AS204317 | Aden core network; 4G Phase 2 to Abyan/Lahij/Hadhramaut | A for ASN/coverage/service; B for any named facility; no official physical DC page as of 2026-08-12. |
| Yemen Mobile | state CDMA/3G/4G operator | Core network Sana'a; ~40% 2019 share | B for core-network DC lead; verify via operator/news. |
| Sabafon | sabafon.com (verify live) | Sana'a HQ; GSM/4G; Al-Ahmar Group + Batelco ownership | B for core DC lead; operator pages sparse. |
| YOU (Yemeni Omani United, ex-MTN Yemen) | official page (verify live) | Sana'a legacy MTN core; Emerald Int'l ownership after MTN exit; 4G | B/C; MTN exit documented by BuddeComm/reports. |
| Y Telecom | (bankrupt 2020, restarted in Aden on 4G) | Legacy Sana'a; Aden 4G restart | C lead; verify current status. |
| National Information Center | https://yemennic.net/ plus historical/successor NIC mirrors discovered in batch work | National databases/e-government hosting | A for role; B/C for facility detail. |
| Central Bank of Yemen | CBY Aden vs CBY Sana'a | Core banking systems; financial DR | B/C; search `البنك المركزي` + `أنظمة`/`مركز بيانات`. |
| Commercial banks / microfinance | e.g., National Microfinance Foundation (WhatsApp/mobile banking) | Sana'a/Aden/Taiz; DR sites | C leads; small server rooms, not commercial DCs. |
| Universities | Sana'a University, Aden University, Hadhramout University, Ibb, Dhamar, Taiz | e-learning/IT centers | C; institutional compute only. |
| Oil & gas entities | Safer/Aden Refinery, ministry of oil | Server rooms at refineries/fields (Marib, Shabwah, Hadhramaut, Aden) | C; industrial compute, not DCs. |
| YemenHosting (yemenhosting.com) | https://www.yemenhosting.com/ | Sana'a (Driving Street), small hosting | C; local web hosting - confirm physical server location. |
| UN missions (UNMHA/OSESGY) | ungm.org notices | Aden 4G/data procurement (e.g., UNGM Notice 228625, 2024) | A for procurement existence; implies host infrastructure, not a DC. |
| Vendors (Huawei, ZTE, Schneider, Vertiv) | vendor pages + case studies | Integrators for state/operator projects | A for vendor service claim; B/C for facility detail. |
| Yemen Computer Company (YCC) | https://www.yccnet.com/ | Offers data-center infrastructure design/build services in Yemen | B/C integrator lead only; not proof of an operated YCC data center. |

Vendor / operator query templates:

```text
"{operator}" "data center" OR "مركز بيانات" Yemen
"{operator}" "core network" OR "server" Sana'a OR Aden
"{operator}" "Tier" OR "Uptime" Yemen
"{operator}" "استضافة" OR "cloud" اليمن
"{operator}" "مولد" OR "طاقة شمسية" OR "كهرباء"
"{operator}" "مذكرة تفاهم" OR "اتفاقية" "مركز بيانات"
"Huawei" OR "ZTE" Yemen "data center" OR "مركز بيانات"
```

Facility-address pivots:

```text
"Aden" "gateway" "TeleYemen" OR "كبل بحري"
"الغيضة" "كبل" OR "محطة"
"الحديدة" "كبل بحري" OR "محطة أرضية"
"صنعاء" "مبنى تيليمن" OR "الشركة اليمنية للاتصالات الدولية"
"Al-Mulla" "Aden" "AdenNet" (RIPE address)
```

---

## 3. Directory and aggregator handling

| Directory / lead source | What it can provide | Caveats |
|---|---|---|
| DataCenterMap Yemen https://www.datacentermap.com/yemen/ | Yemen market/facility names (if any listed) | C by default; may be empty or stale; verify every entry. |
| datacenters.com Yemen https://www.datacenters.com/locations/yemen | Provider/location index | C; often sparse. |
| Cloudscene | Provider profiles (e.g., Yemen hosting) | C/B-; verify with operator. |
| Baxtel | Trade directory/news | B for sourced news, C for directory data. |
| Inflect | Example lead: Yemen Net Al Hudaydah / YemenNet PTC with power/cooling claims | C; useful as a search pivot only. Do not accept MW/power/address claims without PTC/YemenNet/Saba/CSO corroboration. |
| PeeringDB | ASNs (e.g., AdenNet AS204317), interconnection nodes | Proves network presence only; not MW or DC status. |
| RIPE member list | AdenNet registration (Al-Mulla, Aden) | A-grade registration record; address only. |
| whtop.com reviews | Hosting provider reviews (e.g., YemenHosting Sana'a) | C lead. |
| yemenhr.com tenders | Aggregated tenders | C unless original document opened. |

Directory upgrade workflow:

1. Capture exact name, address, city, operator, capacity from directory.
2. Search exact name + operator official domain.
3. Search MTIT (both sides), Saba, NIC, CSO, UNGM for the entity or project.
4. If no primary support appears, keep as **C** with a caveat.

Directory query templates:

```text
site:datacentermap.com/yemen "{operator}"
site:datacenters.com/locations/yemen "{operator}"
site:cloudscene.com Yemen "{operator}"
site:baxtel.com Yemen "data center"
site:inflect.com Yemen "YemenNet" OR "Yemen Net"
"{operator}" site:peeringdb.com Yemen
"{operator}" site:ripe.net Yemen
```

---

## 4. Official verification routes for press/operator leads

Every industry lead should be checked against these primary routes:

| Route | URL | What to verify |
|---|---|---|
| Saba (Aden + Sana'a) | https://www.sabanew.net/ , https://www.saba.ye/ | Ministry announcements, inaugurations, project status |
| MTIT statements | via Saba / yemen.gov.ye / ministry pages | Licenses, spectrum, 4G, infrastructure projects |
| PTC / YemenNet | yemen.gov.ye (Sana'a) | Landline/ADSL platform, switching centers |
| TeleYemen | https://www.teleyemen.com.ye/ | Gateway/hosting services, landing stations |
| AdenNet + RIPE | https://www.adennet4g.net/ , RIPE member list | 4G network, ASN, coverage, any facility claims |
| NIC | yemennic.net plus any verified successor/mirror domain | National data systems hosting |
| CSO | http://www.cso-yemen.com/ , demo1.cso-ye.org | Statistical yearbook telecom chapter |
| UNGM / World Bank | https://www.ungm.org/ , https://documents.worldbank.org/ | UN/development procurement and projects |
| Cloud region pages | AWS/Azure/GCP/OCI official region lists | Confirm no Yemen public region |
| TeleGeography | https://www.submarinecablemap.com/ | Cable landings and status |
| Sana'a Center | https://sanaacenter.org/ | Sector structure, war damage, cables |

Verification templates:

```text
site:sabanew.net "{operator}" OR "{project}" "مركز بيانات"
site:saba.ye "{operator}" OR "{project}"
site:yemen.gov.ye "{project}"
site:teleyemen.com.ye "{project}" OR "{operator}"
site:adennet4g.net "{project}"
site:ungm.org Yemen "{project}"
"{project}" site:submarinecablemap.com
```

---

## 5. Governorate-by-governorate industry search matrix

Use the 22 manifest divisions. For each, run EN + AR universal templates, plus the pass list (state operator -> ministry/procurement -> cable -> energy).

### 5.1 Highest priority

| Division | Localities / terms | Industry/operator seeds |
|---|---|---|
| **Sanaa City** | صنعاء; Hadda, Al-Safia, 60 Meter St; Tahrir | YemenNet/PTC core, TeleYemen gateway, NIC (yemennic.net), Sabafon/YOU/Yemen Mobile/Y-Telecom HQs, CBY Sana'a, universities, ministries. Wartime airstrike risk - status-check everything. |
| **Aden** | عدن; Al-Mulla, Crater, Khormaksar, Ma'alla, Al-Tawahi, Buraiqeh, Aden Free Zone | AdenNet core/4G, TeleYemen Aden gateway + cable landing (Aden-Djibouti, AAE-1), CBY Aden, CSO-Aden, UN missions, banks, free-zone ICT, PM modernization plan leads. |
| **Hadhramaut** | المكلا Mukalla, سيئون Sayun, وادي حضرموت; al-Wadiyah crossing | AdenNet Phase 2, oil sector, Hadhramout University, port digital infrastructure. |
| **Mahra** | الغيضة Al Ghaydah | Active FALCON landing - strategic facility; port/cable station checks. |
| **Western Coast (Al Hudaydah/Hodeidah)** | الحديدة Al Hudaydah, Hodeidah, coastal | FALCON landing, heavy war damage, and directory-only YemenNet/PTC leads; verify status and primary support before any operational or capacity claim. |
| **Taiz** | تعز; city + districts | War-damaged telecom; university/bank leads; status-critical. |

### 5.2 Medium priority

| Division | Search focus |
|---|---|
| Marib | Oil/gas hub; enterprise/telco nodes; front line - verify physical presence. |
| Shabwah / Lahij / Abyan | Southern corridor; AdenNet Phase 2; oil infrastructure (Shabwah); mostly negative unless named. |
| Ibb / Dhamar | Universities and ICT training centers; institutional only. |
| Saada / Hajjah / Jouf / Amran / Beida / Dhale | War-affected; negative-search defaults; any lead needs fresh status source. |

### 5.3 Lower priority / negative-search divisions

For **Sanaa (governorate), Mahwit, Raymah, Socotra**: run EN+AR negative-search checklist (`data center / مركز بيانات / استضافة / غرفة خوادم / محطة أرضية / كبل بحري`), plus operator/ministry pass; expect `no_projects`. Socotra has no known cable landing in the verified cable-source set; do not invent leads.

### 5.4 Full 22-division quick matrix

Use this exact checklist in batch work so that the manifest's 22 divisions are covered once each.

| Division | Arabic / locality pivots | Industry-search expectation |
|---|---|---|
| Abyan | أبين, زنجبار | AdenNet Phase 2 / southern mobile coverage; likely no DC |
| Aden | عدن, المعلا, خور مكسر, التواهي, كريتر | AdenNet core lead, TeleYemen Aden branch/gateway/cables, banks, UN/OSESGY procurement |
| Amran | عمران | Conflict/status search; likely negative |
| Beida | البيضاء | Conflict/status search; likely negative |
| Dhale | الضالع | Southern corridor; likely mobile/network only |
| Dhamar | ذمار | University/IT-center server-room leads only |
| Hadhramaut | حضرموت, المكلا, سيئون, الوديعة | AdenNet Phase 2, TeleYemen Mukalla/Seiyun, oil/port institutional systems |
| Hajjah | حجة, حرض | Haradh land-route/status leads only |
| Western Coast | الحديدة, Hodeidah, Al Hudaydah | FALCON landing and YemenNet/PTC directory pivots; operational status critical |
| Ibb | إب | University/government ICT leads only |
| Jouf | الجوف, الحزم | Frontline; likely negative |
| Lahij | لحج | AdenNet Phase 2 / southern corridor; likely no DC |
| Marib | مأرب | Oil/gas and government-held telecom nodes; status-sensitive |
| Mahra | المهرة, الغيضة, شحن | FALCON Al Ghaydah and Oman route leads |
| Mahwit | المحويت | Low-yield negative search |
| Raymah | ريمة | Low-yield negative search |
| Sanaa City | أمانة العاصمة, صنعاء | PTC/YemenNet DATA CENTER service, TeleYemen HQ, NIC, mobile cores, banks |
| Saada | صعدة | Heavy war damage; fresh status required |
| Shabwah | شبوة, عتق | Oil/gas and southern telecom nodes |
| Sanaa | محافظة صنعاء | Distinguish from Sanaa City; mostly negative |
| Socotra | سقطرى, حديبو | Remote island; no verified DC/cable lead |
| Taiz | تعز | University/bank/telecom server-room leads; status-sensitive |

---

## 6. Candidate handling examples

- **TeleYemen gateway (Sana'a/Aden)**: TeleYemen official page = A for gateway/hosting service and branch facts; facility-level capacity null unless disclosed. Landing stations per TeleGeography/Submarine Cable Map, AAE-1 consortium, World Bank, and Sana'a Center = B/A, with current status date-stamped.
- **AdenNet core (Aden)**: RIPE AS204317 + official 4G program = A for network; physical data center = B lead until an official facility page appears.
- **YemenNet/PTC ADSL platform and hosted-server data centers (Sana'a)**: state-ISP role = A; Saba Sana'a PTC report = A for PTC data-center hosting service; physical address/capacity from CSO bulletins or directories = C unless primary source corroborates it.
- **NIC national systems (Sana'a / Aden)**: NIC role = A; facility detail = B/C. Dual NICs - record which side.
- **Mobile operator cores (Sabafon/YOU/Yemen Mobile/Y-Telecom)**: operator pages/news = B for core-DC lead; no public capacity specs found in the verified source sweep.
- **CBY / bank systems**: core banking + DR leads = B/C; count as institutional, not commercial.
- **FALCON Al Ghaydah landing**: cable station = B/A facility; **FALCON Al Hudaydah and AAE-1 Aden** require current status evidence. Record `active`, `damaged`, `unused`, or `unknown_current_status` from a dated cable/operator/government source; do not rely on stale 2017-era labels.
- **University IT centers**: count as institutional compute only when a page names a data center/server room; do not count ICT training centers.
- **YemenHosting / Sakhr Net / small web hosts (Sana'a or unspecified)**: hosting provider = C; confirm physical server location before any facility record.

---

## 7. Output discipline

- Prefer Arabic names from the governing authority (Aden or Sana'a); include English alias.
- **Control-side note is mandatory** (IRG/Aden vs Ansar Allah/Sana'a); never merge evidence sets across sides without flagging.
- `capacity_mw` only when the source gives MW/IT load for that exact facility; kW/kVA/generators/solar/sqm in notes.
- `evidence_grade=A` only when the source is official/primary for the fact claimed.
- Mark `no_projects` only after official + media + operator + cable checks per the pass list.
- URLs/entity facts spot-checked 2026-08-12; re-validate per batch, especially cable status, active-conflict governorate status, and any directory-derived capacity or address.
