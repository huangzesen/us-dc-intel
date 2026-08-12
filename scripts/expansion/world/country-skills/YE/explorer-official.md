# YE Explorer Official - Yemen Datacenter Enumeration via Dual Ministries, PTC/TeleYemen, AdenNet, NIC, Cables, Procurement and Cloud-Region Absence

Date: 2026-08-12. Country: **YE Yemen**. Division model: **22 first-level divisions in this expansion manifest**: Abyan, Aden, Amran, Beida, Dhale, Dhamar, Hadhramaut, Hajjah, **Western Coast (Al Hudaydah/Hodeidah governorate equivalent in this manifest)**, Ibb, Jouf, Lahij, Marib, Mahra, Mahwit, Raymah, Sanaa City (Amanat Al Asimah), Saada, Shabwah, Sanaa, Socotra, Taiz. Angle: **official / regulatory / state-operator / public-procurement / cable-and-cloud-authority pipeline** for enumerating operational, war-damaged, planned, and institutional data-center facilities in Yemen.

Reliability grades:
- **A** = official / primary source for the exact fact claimed: MTIT (Aden or Sana'a) page or statement, Public Telecom Corporation (PTC) / YemenNet official or Saba-reported statement, TeleYemen official page, AdenNet official / RIPE registration, National Information Center (NIC) page, CSO publication, Saba official news agency (Aden/IRG or Sana'a/Ansar Allah variant), UN / World Bank project document, ITU official record, official operator facility page, official cloud-region page, Uptime certification record.
- **B** = strong secondary: Sana'a Center for Strategic Studies research, Yemen Monitor / Barran Press / Aden Times reporting citing officials, DCD / Capacity Media / Developing Telecoms / Telecompaper / TeleGeography, BuddeComm / market reports, vendor case study naming client and site, World Bank / UNDP country briefs.
- **C** = weak lead: DataCenterMap / datacenters.com / Cloudscene / Baxtel / Inflect / PeeringDB-only records, Wikipedia, social posts, tender aggregators (yemenhr.com unless original document opened), inaccessible snippets, directory-only addresses, and generic hosting-provider marketing that does not name the physical server location.

---

## 0. Yemen-specific structural facts

- Yemen has **no national data-center registry, no independent telecom regulator, and no open planning-permit database**. Enumeration must be assembled from **state operators (PTC/YemenNet, TeleYemen, AdenNet), the National Information Center (NIC), ministries, cable landing stations, public procurement (UN/World Bank/ministry tenders), universities, banks, and press**.
- **Dual authority is the single most important frame.** Since 2014-2015 there are two governments claiming the telecom sector: the **internationally recognized government (IRG) operating from Aden** (Ministry of Telecommunications and Information Technology, Aden Net, Saba-Aden, Central Bank of Yemen-Aden branch) and the **Ansar Allah (Houthi) de facto administration in Sana'a** (MTIT Sana'a, YemenNet/PTC assets in Sana'a, National Information Center yemennic.net, Masirah/Al-Thawra media). Institutions, licenses, fees, and even the NIC and Central Bank exist **twice** (Aden vs Sana'a). Record which authority controls the facility and which evidence set supports it.
- **Regulation is not separated from operation.** The MTIT (both variants) grants licenses, manages the numbering plan and spectrum, and simultaneously operates state networks (PTC landline/YemenNet, TeleYemen gateway) - there is no ARPCE/TDRA-style independent regulator. Legal base: Telecommunications Law No. 38 of 1991 as amended by Law No. 33 of 1996 (WTO accession doc WTACCYEM4A1_LEG_16.pdf). A draft independent-regulator law has been pending since before the war.
- **War damage is material.** The World Bank Yemen Dynamic Needs Assessment Phase 3 and 2023 international-broadband redundancy study, plus Sana'a Center sector work, document severe telecom damage, institutional fragmentation, fuel/power constraints, and repeated submarine-cable outage risk. Treat every facility lead in active-frontline or heavily bombed governorates (Saada, Western Coast/Al Hudaydah, Taiz, Marib, Jouf, Hajjah, Beida) with a fresh status check.
- **Power is the binding constraint, not land.** National grid (Public Electricity Corporation) output is far below demand; facilities run on diesel generators (fuel crises), batteries, and post-2015 solar. Do not infer MW-scale data centers; record kVA/kW only when tied to a named facility. A MW-class commercial colo build is not evidenced as of 2026-08-12.
- **International connectivity is the state's strategic asset.** TeleYemen's official pages describe it as Yemen's sole licensed international telecommunications gateway since 1971/1972 and as 100% state-owned since 2004, with 75% PTC and 25% Yemen Post/Post Savings ownership. Landing stations and cable-adjacent facilities: **Aden** (Aden-Djibouti and AAE-1 landing; TeleYemen Aden branch), **Al Ghaydah (Mahra)** (FALCON landing), and **Al Hudaydah / Western Coast** (FALCON landing, status-sensitive). World Bank's 2023 broadband-redundancy study states FALCON and Aden-Djibouti were the only active subsea cables at that time and treats AAE-1 as not then providing Yemen active redundancy. Land routes: al-Wadiyah (Saudi border, Hadhramaut-side crossing), Haradh (Hajjah), Shihin (Oman border, unstable/cyclone-affected).
- **No hyperscaler public cloud region exists in Yemen.** AWS, Microsoft Azure, Google Cloud, and Oracle OCI official global-region lists show no Yemen region as of 2026-08-12. Local `cloud` claims are hosting/sovereign-cloud services from state operators, banks, universities, and small providers, not hyperscaler regions.
- **Language**: Arabic is primary for official and press sources; English for UN/World Bank, trade press, cable and cloud pages. Search all of: `data center`, `datacenter`, `data centre`, `مركز بيانات`, `مراكز البيانات`, `مركز المعلومات`, `استضافة`, `الحوسبة السحابية`, `غرفة الخوادم`, `محطة الأرضية`, `كبل بحري`.

Core English/Arabic vocabulary:

```text
data center / datacenter / data centre
مركز بيانات (markaz bayanat)
مراكز البيانات (marakiz al-bayanat)
مركز المعلومات (markaz al-ma'lumat) = information center
مركز المعلومات الوطني (national information center)
استضافة المواقع (istidafa al-mawaqi') = web hosting
الحوسبة السحابية (al-hawsaba al-sahabiya) = cloud computing
غرفة الخوادم (ghurfat al-khawadim) = server room
محطة الأرضية (mahattat al-ardhiya) = (earth) station
كبل بحري (kabl bahri) = submarine cable
الشبكة اليمنية للإنترنت (YemenNet)
الموجات المباشرة للبيانات (data transmission)
ترخيص (tarikhis) = license
مزاد (mazad) / مناقصة (munaqasa) = tender
كهرباء (kahraba') = electricity
مولد كهربائي (mowallid) = generator
الطاقة الشمسية (solar)
محافظة (muhafazah) = governorate
عدن (Aden) / صنعاء (Sana'a)
```

---

## 1. Grade A official / regulatory routes

### 1.1 The two Ministries of Telecommunications (MTIT Aden / MTIT Sana'a)

Primary sources:
- **IRG MTIT (Aden)**: ministry portal and statements carried by **Saba News Agency (Aden variant)** https://www.sabanew.net/ and the AdenNet/TeleYemen/PTC branches based in Aden. English coverage of ministry moves: Yemen Monitor, Barran Press, Aden Times.
- **Ansar Allah MTIT (Sana'a)**: ministry statements carried by **Saba (Sana'a variant)** https://www.saba.ye/ and **Al-Masirah** https://english.masirahtv.net/ ; government portal http://www.yemen.gov.ye/ (Sana'a-side infographics on telecom infrastructure indicators, e.g., `انفوجرافيك` uploads).

Why it matters:
- The MTIT is simultaneously **regulator and operator-owner**; its statements announce network projects, cable restorations, licenses, and (rarely) data-center builds. PM Bin Brik (IRG) directed an urgent Aden telecom-modernization plan on 2025-06-22 (Yemen Monitor 143571) - a B-grade lead signal for future DC/telecom infrastructure in Aden.
- Frequency/license records: MTIT grants/licenses to Sabafon, MTN Yemen (now YOU), Y-Telecom, Yemen Mobile; 4G licenses were a wartime sticking point (only Yemen Mobile had 3G/4G permission historically; AdenNet launched as IRG 4G ISP in June 2018).

MTIT query templates:

```text
site:sabanew.net "مركز بيانات" OR "data center"
site:saba.ye "مركز بيانات" OR "data center"
site:masirahtv.net "data center" OR "مركز بيانات"
site:yemen.gov.ye "مركز البيانات"
"وزارة الاتصالات وتقنية المعلومات" "مركز بيانات"
"وزارة الاتصالات" عدن "مركز بيانات"
"وزارة الاتصالات" صنعاء "مركز بيانات"
"ministry of telecommunications" Yemen "data center"
"التحول الرقمي" اليمن "مراكز البيانات"
```

Extract: which authority (Aden vs Sana'a), project name, governorate, stage words (`إطلاق` launch, `افتتاح` inauguration, `تدشين` inauguration, `توقيع` signing, `مذكرة تفاهم` MoU), partners (Saudi/Emirati/Chinese vendors), and any site/capacity.

### 1.2 Public Telecom Corporation (PTC) / YemenNet

Primary source: **Public Telecom Corporation (PTC)** - the state landline operator and, through **YemenNet**, the dominant fixed internet platform. PTC/YemenNet core switching and internet platform facilities are centered in **Sana'a** (captured by Ansar Allah in 2014-2015; IRG treats YemenNet as Houthi-controlled).

Why it matters:
- YemenNet runs the national ADSL/broadband platform; its **internet platform data center / server rooms in Sana'a** are the closest thing to a national carrier data center in the north.
- A Sana'a-side Saba report on PTC internet services states that PTC offered secure, cooled, cabinet-equipped `DATA CENTER` spaces for hosted servers and had **69 hosted companies** during the first half of that reporting year (`https://saba.ye/ar/news3243831.htm`). This is an A-grade source for PTC-operated server-hosting/data-center service existence; it still does not disclose MW, rack count, street address, or a commercial colocation market comparable to Gulf facilities.
- PTC annual statistical bulletins / CSO yearbooks describe switching centers, internet nodes, subscribers, and data transmission. These are A-grade for telecom infrastructure counts, but only C-grade for data-center inference unless the bulletin names a data center or server-hosting facility.

PTC/YemenNet queries:

```text
"YemenNet" "data center" OR "مركز بيانات" OR "غرفة الخوادم"
"الشبكة اليمنية للإنترنت" "مركز البيانات"
"المؤسسة العامة للاتصالات" "data center"
"المؤسسة العامة للاتصالات" "مراكز بيانات" "DATA CENTER"
"المؤسسة العامة للاتصالات" "استضافة مكانية" "السيرفرات"
"Public Telecom Corporation" Yemen "data center" OR "server"
site:cso-yemen.com "الاتصالات" "التقنية" "مراكز"
"سوبر نت" OR "Super Net" Yemen ISP
```

Count YemenNet/PTC facilities as **state carrier / institutional** data centers. Grade A only when an official PTC/YemenNet/Saba/CSO source names the facility/service; do not import directory MW values without primary support.

### 1.3 TeleYemen - sole international gateway (A-grade anchor entity)

Primary source: **TeleYemen (Yemen International Telecommunications Company)** https://www.teleyemen.com.ye/ (Arabic; EN pages under `/index.php/en/`; legacy mirror https://website.teleyemen.com.ye/).

Why it matters:
- TeleYemen official pages state that it is the **sole licensed international telecommunications gateway** and list web/email hosting, VSAT/data communication, Y.Net and branch/contact presences. The TeleYemen hosting page states hosting is provided on TeleYemen servers; the contact page lists head office in Sana'a (26-Sept/Al-Tahreer building) and branches in Aden, Hodeidah, Mukalla, and Seiyun.
- TeleYemen gateway, hosting, and cable-landing facilities in **Sana'a and Aden** are the country's most concrete state carrier/international-gateway data-center-class facilities. Any IRG/private project promising international-grade data-center capacity should be tested against TeleYemen Aden or the Sana'a-side gateway.

TeleYemen queries:

```text
site:teleyemen.com.ye "استضافة" OR "بيانات" OR "data"
"TeleYemen" "gateway" Aden OR Sana'a
"TeleYemen" "data center" OR "hosting"
"تيليمن" "مركز البيانات"
"Yemen International Telecommunications" "data center"
"الشركة اليمنية للاتصالات الدولية" "data"
site:teleyemen.com.ye hosting OR webhosting OR clouding
site:website.teleyemen.com.ye "Hosting is provided in our servers"
"TeleYemen" "Aden" "cable landing station"
```

Grade **A** for the gateway/hosting service and TeleYemen branch facts, **B/A** for cable landing facts when joined to TeleGeography/Submarine Cable Map or AAE-1 consortium pages. Keep `capacity_mw` null unless an official source gives MW/kVA for a named facility.

### 1.4 AdenNet - IRG 4G ISP (Aden)

Primary source: **AdenNet** https://www.adennet4g.net/ ; RIPE member record https://www.ripe.net/membership/member-support/list-of-members/ye/adennet/ (A-grade registration: Aden, Al-Mulla Main Street); AS204317 (ipregistry).

Why it matters:
- Created/launched in June 2018 by the IRG as the alternative ISP to Houthi-controlled YemenNet; Saba Aden and secondary coverage place the launch in Aden. AdenNet Phase 2 expansion was reported by Barran Press as a ministry/Saba-backed statement covering Abyan, Lahij, and Hadhramaut; verify the underlying Saba notice where possible.
- AdenNet's **core network / server facilities in Aden** are the most likely IRG-side state data-center lead in the south. Official evidence is currently network-level (AdenNet service pages, RIPE/ASN registration, Saba launch/coverage statements); record a physical data center as **B lead** until an official facility page or procurement document names the site.

AdenNet queries:

```text
site:adennet4g.net "مركز" OR "data" OR "خوادم"
"AdenNet" "data center" OR "core network" OR "server"
"Aden Net" "4G" "Aden" "مركز البيانات"
"عدن نت" OR "أدن نت" "مركز البيانات"
AS204317 "Aden Net"
```

### 1.5 National Information Center (NIC) - dual institutions

Primary sources:
- **NIC public portal** https://yemennic.net/ - national information systems, databases, government-service directories, and official country data.
- **NIC / historical portal references** https://yemen-nic.info/sectors/information/ and any IRG-side mirror or successor domain discovered during batch work.

Why it matters:
- The NIC is the **state data-hosting institution**. Its official `about` page says it builds, manages, and develops a national information system, operates databases and automated processing, and builds/runs computer networks for information exchange. Its published databases include research, publications, and Yemeni personalities. That is A-grade for institutional data-hosting role, but only B/C for a physical facility unless a page names the server room/data center.
- Do not conflate NIC data centers with commercial colocation.

NIC queries:

```text
site:yemennic.net "مركز البيانات" OR "خوادم" OR "data"
"المركز الوطني للمعلومات" "عدن" "مركز البيانات" OR "data"
"المركز الوطني للمعلومات" "مركز البيانات"
"National Information Center" Yemen "data center" OR "server"
"المركز الوطني للمعلومات" صنعاء "قاعدة بيانات"
```

### 1.6 Central Statistical Organization (CSO)

Primary source: **CSO** http://www.cso-yemen.com/ and Aden-side portal https://demo1.cso-ye.org/ (reactivated in Aden Aug 2022).

Why it matters: CSO **Statistical Yearbooks** (Chapter Communications & Information Technology) are the only systematic official source of telecom infrastructure counts (switching centers, internet nodes, subscribers) per governorate - useful for negative-search discipline and historical facility counts (Grade A for the statistic, C for any DC inference).

```text
site:cso-yemen.com "الاتصالاات" OR "الاتصالات وتقنية المعلومات"
"Central Statistical Organization" Yemen telecom yearbook "مراكز"
```

### 1.7 Public procurement and donor routes (the best new-project detector)

Primary routes:
- **UNGM / UN Global Marketplace** https://www.ungm.org/ - UN system notices for Yemen telecom/data work (e.g., Provision of 4G Data Services (GSM) for OSESGY/UNMHA in Aden, UNGM Notice 228625, 2024 - A-grade evidence that UN missions buy telecom capacity in Aden; implies host-side infrastructure but not a facility).
- **World Bank project documents** https://documents.worldbank.org/ - e.g., 'Yemen Information and Communication Technology (ICT)' policy note 2017 (documents/curated/en/337651508409897554) and Yemen Economic Updates; any Yemen digital-transformation project with data-center component would appear here (Grade A for existence of project; verify physical sites separately).
- **Yemen HR tenders platform** https://yemenhr.com/tenders - aggregated Yemeni public/private tenders; **C** unless the original buyer document is opened.
- **Sana'a Center / ITU / GSMA** publications for context and sector structure (B/A).

Procurement query templates:

```text
site:ungm.org Yemen "4G" OR "telecommunications" OR "data" Aden
site:documents.worldbank.org Yemen ICT "data center" OR "e-government"
Yemen "مناقصة" "مركز بيانات" OR "data center"
"اليمن" "مناقصة" "خوادم" OR "استضافة"
Yemen tender "data center" Sana'a OR Aden OR Hadhramaut
site:yemenhr.com "data center" OR "مركز بيانات"
```

### 1.8 Energy context (do not over-read)

Primary source: **Public Electricity Corporation (PEC)** and Sana'a Center electricity-sector research (e.g., https://sanaacenter.org/publications/policy-research/14292).

Handling: national grid supply is minimal; facilities rely on diesel + solar. Only record kVA/MW when a named DC site discloses it. Solar-plus-storage micro-grids at telecom sites are common post-2015 but are not data centers.

### 1.9 Submarine cable landing stations (physical small facilities)

Primary source: **TeleGeography Submarine Cable Map** https://www.submarinecablemap.com/ and the Sana'a Center telecom paper (Jan 2021, https://sanaacenter.org/publications/policy-research/12721) for Yemen's cable status.

Yemen cable inventory (as of TeleGeography/Submarine Cable Map pages, AAE-1 consortium pages, Sana'a Center 2021 sector paper, World Bank 2023 broadband-redundancy study, and later cable-repair reporting; re-verify each batch):

| Cable | Landing site (division) | Status lead | Enumeration use |
|---|---|---|---|
| FALCON (FLAG/FALCON) | **Al Ghaydah (Mahra)** and **Al Hudaydah / Western Coast** | Active-status evidence is strongest for Al Ghaydah / FALCON; Hudaydah is status-sensitive and war-affected | Landing station buildings = small critical facilities; grade B/A for landing-point existence, but operational status must be dated |
| Aden-Djibouti / Yemen-Djibouti | **Aden** | World Bank 2023 study treats FALCON and Aden-Djibouti as Yemen's only active subsea cables at that time | Landing station in Aden; Grade B/A for cable fact |
| AAE-1 | **Aden** | AAE-1 consortium and TeleGeography list Aden/TeleYemen; World Bank 2023 study indicates it was not an active redundancy path for Yemen at that time; 2024-2025 Red Sea cable incidents and repairs make status volatile | Count landing-site equipment/facility only with status note; do not treat as stable active Yemen capacity without fresh evidence |
| Land routes | al-Wadiyah (Hadhramaut/Saudi), Haradh (Hajjah), Shihin (Mahra/Oman) | Mixed/unstable; World Bank 2023 notes Oman terrestrial connectivity active but unstable and Saudi links mainly inactive | Terrestrial gateways, not DCs unless a named gateway/server facility is documented |

Cable query templates:

```text
"FALCON" cable Yemen "Aden" OR "Hodeidah" OR "Ghaydah"
"AAE-1" Yemen Aden "landing"
"Aden-Djibouti" submarine cable Yemen
site:submarinecablemap.com Yemen
"كبل بحري" "عدن" OR "الحديدة" OR "الغيضة"
```

### 1.10 Official public cloud region pages (absence evidence)

| Provider | Official source | Yemen signal | Enumeration use |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No Yemen region in official list, checked 2026-08-12 | Absence evidence; search only edge/partner/customer leads |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | No Yemen region in official list, checked 2026-08-12 | Absence evidence; local sovereign/hosted-cloud claims only |
| Google Cloud | https://cloud.google.com/about/locations | No Yemen region in official list, checked 2026-08-12 | Absence evidence; nearby Middle East regions are not Yemen |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No Yemen region in official list, checked 2026-08-12 | Absence evidence; partner/customer leads only |
| Huawei / Huawei Cloud | https://e.huawei.com/en/solutions/data-center | Vendor/integrator role for state projects only; no public Yemen Huawei Cloud region | Verify via ministry/NIC/UN evidence before counting |

---

## 2. Official operator / public-entity seed list

| Entity | Official source | Yemen footprint signal | Follow-up |
|---|---|---|---|
| MTIT (IRG, Aden) | Saba Aden https://www.sabanew.net/ + Yemen Monitor | AdenNet 4G program; PM Bin Brik modernization plan (2025-06-22); licenses/fees | Search ministry statements for DC/cloud/infrastructure projects in Aden/Abyan/Lahij/Hadhramaut |
| MTIT (Ansar Allah, Sana'a) | Saba Sana'a https://www.saba.ye/ + yemen.gov.ye + Al-Masirah | YemenNet/PTC oversight; telecom-infrastructure indicator infographics; condemnations of telecom strikes | Search for Sana'a DC/cloud/e-government announcements |
| PTC / YemenNet | PTC via Saba Sana'a report `https://saba.ye/ar/news3243831.htm`, CSO bulletins, yemen.gov.ye | Landline + ADSL platform core in Sana'a; PTC-hosted server spaces in DATA CENTER facilities; governorate switching centers | A for PTC hosting service/data-center claim; C for inferred per-governorate DCs |
| TeleYemen | https://www.teleyemen.com.ye/ and https://website.teleyemen.com.ye/ | Sole international gateway; servers for hosting; Sana'a HQ and Aden/Hodeidah/Mukalla/Seiyun branches; VSAT/data services | A-grade anchor for gateway/hosting-service claims; cable landing stations in Aden/Ghaydah/Hudaydah require cable-source joins |
| AdenNet | https://www.adennet4g.net/ + RIPE member page | IRG 4G ISP; core in Aden; Phase 2 (2024) to Abyan/Lahij/Hadhramaut | Verify whether a named Aden data center exists beyond network core |
| National Information Center | https://yemennic.net/ plus historical/successor NIC mirrors discovered in batch work | National databases/e-government hosting | Institutional DC evidence; record which authority/source controls the evidence |
| CSO | http://www.cso-yemen.com/ + demo1.cso-ye.org | Statistical yearbooks (telecom chapter) | Historical infrastructure counts per governorate |
| Yemen Mobile | state-owned CDMA/3G/4G operator | Core network Sana'a; largest subscriber base (~40% 2019) | Core DC = state-carrier facility lead (B) |
| Central Bank of Yemen | CBY Aden (IRG) vs CBY Sana'a (Ansar Allah) | Banking systems hosting; financial-sector DR | Search bank-system data center / core banking leads (B/C) |
| UN / World Bank / ITU programs | ungm.org, documents.worldbank.org, ITU | UNMHA/OSESGY 4G, FTTH/ADSL and leased-line procurement; 2017 ICT policy note; 2023 broadband-redundancy study | New project announcements with DC components; procurement alone is not a facility |

---

## 3. Division enumeration strategy (22 divisions)

### 3.1 National workflow per division

Run four passes per division:
1. **State-operator pass**: which of PTC/YemenNet, TeleYemen, AdenNet, NIC, mobile operators (Sabafon, YOU, Yemen Mobile, Y Telecom) has presence there; search `"{governorate}" "data center"` + Arabic `"{muhafazah_ar}" "مركز بيانات"`.
2. **Government/procurement pass**: ministry statements (Saba Aden/Sana'a), UNGM, World Bank, university tenders, yemenhr.com leads.
3. **Cable/connectivity pass**: landing stations (Aden, Al Ghaydah, Al Hudaydah), border land routes, TeleYemen gateway presence.
4. **Energy/context pass**: PEC grid reality, diesel/solar at any named site; record kW only when site-named.

Universal templates (EN):

```text
"{governorate}" "data center" Yemen
"{governorate}" datacenter OR "data centre"
"{governorate}" "server room" OR "hosting"
"{governorate}" "telecommunications" "مركز"
"{governorate}" "Tier" "data center"
"{governorate}" "4G" "AdenNet" OR "YemenNet"
"{governorate}" "central bank" OR "bank" "data center"
"{governorate}" "university" "data center" OR "server"
"{governorate}" "cable landing station" OR "محطة الأرضية"
```

Universal templates (AR):

```text
"{muhafazah_ar}" "مركز بيانات"
"{muhafazah_ar}" "مركز المعلومات" "خوادم"
"{muhafazah_ar}" "استضافة المواقع"
"{muhafazah_ar}" "الحوسبة السحابية"
"{muhafazah_ar}" "محطة الأرضية" OR "كبل بحري"
"{muhafazah_ar}" "مناقصة" "خوادم"
"{muhafazah_ar}" "البنك المركزي" "أنظمة"
```

### 3.2 Priority division clusters

| Division | Why high priority | Official query notes |
|---|---|---|
| **Sanaa City** | Capital (Ansar Allah-controlled): MTIT Sana'a, PTC/YemenNet core, TeleYemen gateway/earth station, NIC (yemennic.net), mobile operator HQs (Sabafon, YOU legacy MTN, Yemen Mobile, Y Telecom legacy), Central Bank Sana'a, universities, ministries' server rooms | Search `صنعاء` + `مركز بيانات`, YemenNet platform, TeleYemen hosting, NIC databases, bank core systems. Wartime airstrike risk - verify current status. |
| **Aden** | IRG interim capital: MTIT Aden, AdenNet core/4G, TeleYemen Aden gateway + cable landing (Aden-Djibouti, AAE-1), CBY Aden, CSO-Aden, UN missions (UNMHA/OSESGY), banks, Aden Free Zone | Search `عدن` + `مركز بيانات`, AdenNet official, PM modernization plan, UNGM notices, free-zone ICT projects |
| **Hadhramaut** | Al-Wadiyah border crossing, oil sector (Mukalla/Sayun), AdenNet Phase 2, STC-affiliated southern institutions | Search Mukalla/Sayun/Al-Wadiyah + data/telecom; university Hadhramaut; oil-company server rooms |
| **Mahra** | Al Ghaydah port = active FALCON landing - strategic international facility | Search `الغيضة` + cable/landing; port digital infrastructure |
| **Western Coast (Al Hudaydah / Hodeidah)** | FALCON landing; war-damaged telecom; Inflect-style directory claims for YemenNet/PTC in Al Hudaydah require primary corroboration | Verify status of any DC/server lead; do not mark operational without fresh source |
| **Taiz** | Third-largest city; war-damaged telecom; university + bank leads | Search Taiz + server room/DC; status-critical |
| **Marib** | Oil/gas hub, government-held, active front line; enterprise/telco nodes | Search Marib + data/telecom; verify physical presence |
| **Shabwah / Lahij / Abyan** | Southern corridor, AdenNet Phase 2 coverage, oil infrastructure | Search each + `مركز بيانات`; mostly negative unless ministry/AdenNet/UN names a site |
| **Saada / Hajjah / Jouf / Amran / Beida / Dhale / Ibb / Dhamar** | War-affected north/center; institutional leads only | Negative-search defaults; universities (Ibb, Dhamar) may have IT centers |
| **Sanaa (governorate), Mahwit, Raymah** | Rural; low yield | Negative-search; no verified DC leads as of 2026-08-12 |
| **Socotra** | Remote island; no cable landing; minimal infrastructure | Negative-search; no verified DC projects as of 2026-08-12 |

### 3.3 Full 22-division checklist

Use this list to prevent accidental omission. `Western Coast` is the project manifest label for the Al Hudaydah/Hodeidah governorate search space.

| Division | Arabic / locality pivots | Official seed expectation |
|---|---|---|
| Abyan | أبين, زنجبار | AdenNet Phase 2 / southern telecom coverage; likely negative for DCs |
| Aden | عدن, المعلا, خور مكسر, التواهي, كريتر | AdenNet, TeleYemen branch/gateway/cables, CBY Aden, UN procurement |
| Amran | عمران | War/status checks; negative unless PTC/mobile facility named |
| Beida | البيضاء | War/status checks; negative unless PTC/mobile facility named |
| Dhale | الضالع | Southern corridor; negative unless mobile/PTC facility named |
| Dhamar | ذمار | University/government server-room leads only |
| Hadhramaut | حضرموت, المكلا, سيئون, الوديعة | AdenNet Phase 2, TeleYemen Mukalla/Seiyun branches, oil/port/server-room leads |
| Hajjah | حجة, حرض | Haradh terrestrial-route damage; status-sensitive |
| Western Coast | الحديدة, Hodeidah, Al Hudaydah | FALCON landing/status; PTC/YemenNet directory claims need official source |
| Ibb | إب | University/government server-room leads only |
| Jouf | الجوف, الحزم | Frontline; negative unless named facility |
| Lahij | لحج | AdenNet Phase 2 / southern corridor; likely negative |
| Marib | مأرب | Oil/gas, government-held telecom nodes; status-sensitive |
| Mahra | المهرة, الغيضة, شحن | FALCON Al Ghaydah; Oman terrestrial route; cable/gateway leads |
| Mahwit | المحويت | Low-yield negative search |
| Raymah | ريمة | Low-yield negative search |
| Sanaa City | أمانة العاصمة, صنعاء | PTC/YemenNet DATA CENTER service, TeleYemen HQ, NIC, mobile cores, CBY Sana'a |
| Saada | صعدة | Heavy war damage; no operational claim without fresh evidence |
| Shabwah | شبوة, عتق | Oil/gas + southern telecom nodes; likely institutional only |
| Sanaa | محافظة صنعاء | Rural ring around capital; distinguish from Sanaa City |
| Socotra | سقطرى, حديبو | No cable landing; negative unless named satellite/edge facility |
| Taiz | تعز | University/bank/telecom leads; status-sensitive |

### 3.4 Lower-yield / negative-search handling

For any division, mark `no_projects` only after: (1) EN + AR queries for `data center / مركز بيانات / استضافة / غرفة خوادم`; (2) operator/state-entity pass (YemenNet/TeleYemen/AdenNet/mobile operators/NIC); (3) ministry + UN/procurement pass; (4) cable-landing check. Distinguish **generic ICT training centers, internet cafes, cyber labs, and call centers** from physical data centers.

---

## 4. Output discipline (official angle)

- Prefer Arabic official names from the governing authority (Aden or Sana'a); include English alias.
- Record **control-side** (IRG/Aden vs Ansar Allah/Sana'a) as a required note field; never mix evidence sets across sides without flagging.
- `capacity_mw` only when the source gives MW/IT load for the exact facility; kVA/kW/generators/solar/sqm go to notes.
- `evidence_grade=A` only for official/primary source of the claimed fact; `status` words: `إطلاق`/`افتتاح` (launch/inauguration) = operational claim; `مذكرة تفاهم` (MoU) = planned; `مناقصة` (tender) = procurement.
- Re-verify the hyperscaler-region absence and cable status on every batch; both change over time.
- URLs and entity facts were verified/spot-checked 2026-08-12. Re-validate per batch, especially cable status, dual-authority ministry pages, and any active-conflict governorate status claim.
