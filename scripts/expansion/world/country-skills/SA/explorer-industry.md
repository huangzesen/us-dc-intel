# SA Explorer — Industry, Trade Press, Vendors, and Arabic/English Query Patterns

Date: 2026-08-12. Scope: how to enumerate Saudi Arabia datacenter projects from industry/trade press, vendor disclosures, regulator lists, and repeatable English + Arabic search patterns. Reliability grades: **A** = official/primary regulator, operator, exchange, permit, or cloud-region source; **B** = strong trade press / market-intelligence / contractor evidence; **C** = weak directory, social, or unverifiable aggregator evidence.

---

## 0. Saudi Market Shape: Search the Hubs First

Saudi datacenter discovery is concentrated rather than evenly distributed. Start with these hubs, then sweep the rest of the 13 regions for institutional / telco / edge facilities.

- **Riyadh Region**: Riyadh city is the largest commercial and government-cloud cluster. Key subareas: Digital City / Al Raidah, Khurais Road, Al Malqa / Diriyah edge, New Industrial Area, Princess Nourah University, MODON First Technology Park / east Riyadh.
- **Eastern Province**: Dammam, Al Khobar, Dammam Second Industrial City, and King Salman Energy Park (**SPARK**, near Abqaiq/Buqayq) are the main hyperscale/colo cluster. Google Cloud's Dammam region and planned Microsoft Saudi Arabia East region make Eastern Province especially important.
- **Makkah Region**: Jeddah and Makkah host west-coast carrier, cloud, Hajj/Umrah, and subsea-gateway capacity. Search Jeddah, Makkah, Rabigh, King Abdullah Economic City (**KAEC**) separately.
- **Tabuk Region / NEOM**: Oxagon/NEOM is a mega-campus pipeline geography; treat signed investment announcements as **planned** until CST registration, permit, construction, or contractor evidence appears.
- **Medina and Qassim**: center3/STC has known facilities in Madinah and Buraydah; search telco and government continuity projects.
- Other regions mostly yield university, ministry, enterprise DR, or telco edge sites, not hyperscale campuses. Use Arabic queries and CST/municipal sources before declaring no public project.

Main sector terms:

| English | Arabic |
|---|---|
| data center / datacenter | مركز بيانات / مراكز البيانات |
| cloud data center | مركز بيانات سحابي / مراكز بيانات سحابية |
| colocation | استضافة مشتركة / خدمات استضافة |
| hyperscale | فائق النطاق / هايبرسكيل |
| AI data center / AI factory | مركز بيانات للذكاء الاصطناعي / مصنع ذكاء اصطناعي |
| disaster recovery | التعافي من الكوارث |
| racks | رفوف / الرفوف |
| megawatt / MW | ميجاواط / ميغاواط |
| building permit | رخصة بناء |
| land lease | تأجير أرض / عقد إيجار أرض |
| industrial city / technology zone | مدينة صناعية / منطقة تقنية |
| inaugurated / launched | دشن / افتتح / أطلق |
| signed / awarded | وقع / ترسية / أبرم |
| under construction | قيد الإنشاء / يجري تنفيذ |

---

## 1. Highest-Value Primary Sources

### 1.1 CST registered datacenter service providers (Grade A)

- **Communications, Space & Technology Commission (CST)**: registered Data Center Services Providers list: https://www.cst.gov.sa/en/knowledge-center/digital-knowledge/data-center/data-centers-providers
- Arabic page: https://www.cst.gov.sa/knowledge-center/digital-knowledge/data-center/data-centers-providers
- Registration service: https://www.cst.gov.sa/en/business/services/Datacenter-registration
- SPA notice on CST Data Center Services Regulations: https://www.spa.gov.sa/en/N2022766

Why it matters:

- CST's provider list is the best Saudi facility/operator seed because the page states that **each data center has a separate registration according to classification and stage of development**.
- Categories to capture: **Qualifying, Limited, Standard, Advanced**. Qualifying can mean under development; Limited/Standard/Advanced usually indicate existing/new commercial facilities with increasing compliance scope.
- CST is facility/provider-level evidence for legal service status, but it does not reliably expose MW, exact address, or all planned campuses. Join to operator pages, Saudi Exchange announcements, contractors, and trade press for capacity and status.

Search patterns:

```text
site:cst.gov.sa/en/knowledge-center/digital-knowledge/data-center "Registered Data Center Services Providers"
site:cst.gov.sa "Data Center Services Regulation" "Saudi Arabia"
site:cst.gov.sa "Data Center Registration" "Qualifying" "Advanced"
site:cst.gov.sa/knowledge-center "مراكز البيانات" "مقدمي الخدمة"
site:cst.gov.sa "تسجيل مراكز البيانات" "مركز بيانات"
```

Extraction note: the CST page is a Next/Sitecore page. The rendered page and `__NEXT_DATA__` payload include the registry component and classification lists; if scraping is difficult, use browser automation and capture facility/provider rows, category, and city filters.

### 1.2 Balady / municipal building and business-license surfaces (Grade A when record-specific)

- Balady building permit service: https://balady.gov.sa/en/services/issuing-building-permit
- Balady building permit inquiry: https://balady.gov.sa/en/services/building-permit-inquiry
- Ministry of Municipalities and Housing permit inquiry: https://momah.gov.sa/en/e-services/inquiring-about-building-license
- Balady activity standard page includes activity code **631126 - تقديم خدمات مراكز البيانات**: https://apps.balady.gov.sa/LicenseStandard/Default?sid=7010
- Balady consultation/requirements page for datacenters: https://balady.gov.sa/ar/consultations/اشتراطات-مراكز-البيانات

Use:

- Balady is the municipal channel for building permits and commercial activity licensing. Public search is limited and often login-oriented, so use it primarily for verification when a project owner/address/permit number is known.
- Search web-indexed Balady/MOMAH pages for Arabic terms, then pivot to municipality/emirate pages.

Queries:

```text
site:balady.gov.sa "مركز بيانات" "رخصة بناء"
site:balady.gov.sa "مراكز البيانات" "اشتراطات"
site:momah.gov.sa "مركز بيانات" "رخصة"
"631126" "تقديم خدمات مراكز البيانات"
"{city_ar}" "مركز بيانات" "رخصة بناء"
"{operator_ar}" "رخصة بناء" "مركز بيانات"
```

### 1.3 MODON industrial cities and technology zones (Grade A/B)

- MODON: https://modon.gov.sa/
- MODON annual reports: https://modon.gov.sa/ar/MediaCenter/AnnualReports/

Why it matters:

- MODON oversees industrial cities and technology zones where multiple Saudi datacenter projects are being sited. Public reports and news mention advanced datacenter zones and, in Arabic newsletters, datacenter counts such as "24 مراكز بيانات" as a program-level signal.
- MODON was reported as announcing LEAP 2025 datacenter contracts/leases with **DataVolt, Gulf Data Hub, and Ezditek**; the DataVolt Riyadh lease was a 55,000 sqm plot at First Technology Park in east Riyadh. Treat MODON announcements as **A** when directly on MODON/official pages, **B** when only reported by DCD/Total Telecom.

Queries:

```text
site:modon.gov.sa "DataVolt" "data center"
site:modon.gov.sa "Gulf Data Hub" "data center"
site:modon.gov.sa "Ezditek" "data center"
site:modon.gov.sa "مركز بيانات" "داتا فولت"
site:modon.gov.sa "مراكز البيانات" "الرياض"
site:modon.gov.sa "مراكز البيانات" "المدينة الصناعية"
"مدن" "مركز بيانات" "الرياض" "جدة" "الدمام"
```

### 1.4 Saudi Exchange / Tadawul disclosures (Grade A for listed-company contracts)

- Saudi Exchange announcements: https://www.saudiexchange.sa/wps/portal/saudiexchange/newsandreports/issuer-news/issuer-announcements
- MIS / Al Moammar Information Systems ticker **7200** is the key listed datacenter contractor/operator pivot. Its Sahayeb / Saudi Data Center Fund disclosures are often more concrete than press.

High-signal examples to search:

- MIS / Saudi Data Center Fund 1 framework and expansion announcements.
- MIS Aramco datacenter leasing framework dated 2026-08-05 in Arabic search snippets.
- MIS HUMAIN AI private datacenter design/build and hosting contracts.

Queries:

```text
site:saudiexchange.sa "Data Center" "MIS" "Sahayeb"
site:saudiexchange.sa "data center facilities located in Riyadh and Dammam"
site:saudiexchange.sa "Saudi Data Center Fund 1" "MW"
site:saudiexchange.sa "مراكز البيانات" "المعمر" "ام آي اس"
site:saudiexchange.sa "تأجير مراكز البيانات" "أرامكو"
site:saudiexchange.sa "هيوماين" "مركز بيانات" "المعمر"
site:argaam.com "MIS" "Saudi Data Center Fund" "data center"
site:argaam.com "مراكز البيانات" "المعمر" "هيوماين"
```

### 1.5 Cloud-region official pages (Grade A for city/region existence)

Use official hyperscaler region documents to confirm operational/planned cloud regions, then identify host/local partner through trade press and CST/operator evidence.

| Provider | Saudi official evidence | Enumeration value |
|---|---|---|
| Google Cloud | Dammam region docs: https://docs.cloud.google.com/docs/dammam-region-access and locations page https://cloud.google.com/about/locations | Operational Dammam cloud region; search Dammam/Eastern Province and Aramco/Google partner references. |
| Oracle Cloud | Public regions: https://www.oracle.com/sa/cloud/public-cloud-regions/ and OCI region docs: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | Saudi Arabia West (Jeddah, `me-jeddah-1`) and Saudi Arabia Central (Riyadh, `me-riyadh-1`). Oracle says center3 is host partner for Riyadh. |
| AWS | Official 2024 announcement: https://press.aboutamazon.com/2024/3/aws-to-launch-an-infrastructure-region-in-the-kingdom-of-saudi-arabia | Planned Saudi Arabia Region in 2026, three AZs, >US$5.3bn investment. Locations not disclosed; search construction/power/land evidence around Riyadh/Eastern/Jeddah. |
| Microsoft Azure | Microsoft source post, Feb 2026: https://news.microsoft.com/source/emea/2026/02/microsoft-confirms-saudi-arabia-datacenter-region-available-for-customers-to-run-cloud-workloads-from-q4-2026/ and Microsoft Datacenters page: https://datacenters.microsoft.com/home/ | Saudi Arabia East region available Q4 2026; Microsoft says construction completed on three sites. Trade press places it in Eastern Province. |
| Alibaba Cloud / SCCC | Search STC/Saudi Cloud Computing Company official and press; no universal region docs as clean as OCI/GCP. | Two Riyadh availability-zone datacenters reported via SCCC/STC-Alibaba JV; verify via CST/provider and operator evidence. |
| Huawei Cloud | Huawei Saudi Class C compliance page: https://www.huaweicloud.com/intl/en-us/securecenter/compliance/compliance-center/ksa-classc.html | Cloud service compliance evidence, not physical facility evidence; search CST Class C and partner host separately. |

Cloud search patterns:

```text
"Saudi Arabia" "cloud region" "data centers located in" "Riyadh"
"Saudi Arabia East" "datacenter region" "Eastern Province" Microsoft
"Dammam region" "Google Cloud" "Saudi Arabia"
"me-riyadh-1" "center3" "Oracle"
"me-jeddah-1" "Oracle" "Saudi Arabia West"
"AWS Region" "Saudi Arabia" "three Availability Zones" "2026"
"المنطقة السحابية" "السعودية" "مراكز بيانات"
"منطقة سحابية" "الدمام" "جوجل كلاود"
```

---

## 2. Industry and Trade Press Sources (Grade B unless they cite primary filings)

Best recurring sources:

- **Data Center Dynamics (DCD)**: https://www.datacenterdynamics.com/ — best English trade press for center3, QST, DataVolt, Oracle, Google, Khazna, DAMAC/EDGNEX, Gulf Data Hub.
- **MEED**: https://www.meed.com/ — strong for Gulf construction/project status; often paywalled but snippets reveal location/MW/stage.
- **W.Media**: https://w.media/ — strong Middle East datacenter announcements.
- **Capacity Media**: https://www.capacitymedia.com/ — telecom, subsea, cloud, and datacenter deals.
- **Total Telecom / Developing Telecoms / Telecom Review**: useful for operator PR syndication.
- **Data Centre Magazine / Data Center Knowledge / Dgtl Infra / DC Post MEA**: useful secondary confirmation.
- **Argaam**: https://www.argaam.com/ — important Saudi listed-company and Arabic/English business news, especially MIS/Sahayeb.
- **Saudi Press Agency (SPA)**: https://www.spa.gov.sa/ — official event/news feed. Treat as **A-/B+**: good for signed MoUs and ministry statements, but still verify whether a project moved beyond ceremony.
- **S&P Global Market Intelligence**: strong market framing; its public Saudi data-center market page identifies Riyadh, Dammam, and Jeddah as the main sites of choice and flags Center3, DAMAC, QST, DataVolt, ZeroPoint, and HUMAIN.
- **Directories**: DataCenterMap, Baxtel, Datacenters.com, DC Byte, Reboot Monkey. Use as **C/B- leads**, never final source for MW unless no better source exists. They can be useful for aliases and old telco sites.

Trade-press query templates:

```text
site:datacenterdynamics.com/en/news Saudi Arabia data center Riyadh Dammam Jeddah
site:datacenterdynamics.com/en/news "Saudi Arabia" "MW" "data center"
site:meed.com "Saudi" "data centre" "Riyadh" "Dammam" "Jeddah" "Neom"
site:w.media "Saudi Arabia" "data center" "MW"
site:capacitymedia.com "Saudi Arabia" "data centre" "center3" OR "DataVolt"
site:argaam.com "data center" "Saudi" "MIS" OR "Sahayeb"
site:argaam.com "مراكز البيانات" "السعودية" "المعمر"
site:spa.gov.sa "data center" "Saudi Arabia" "LEAP"
site:spa.gov.sa "مراكز البيانات" "ليب" "السعودية"
```

Status verbs to capture:

- English: `announces`, `signs`, `land lease`, `breaks ground`, `secures financing`, `awards contract`, `under construction`, `go-live`, `launches`, `opens`, `expands`.
- Arabic: `أعلن`, `وقعت`, `توقيع اتفاقية`, `عقد إيجار`, `ترسية`, `دشن`, `افتتح`, `أطلق`, `قيد الإنشاء`, `تشغيل`, `توسعة`.

---

## 3. Major Operators and Developer Pivots

Use this table as the core vendor sweep. For each company, run English + Arabic name searches plus CST registry checks and city-specific queries.

| Operator / developer | Where to look | Known Saudi geographies / notes | Grade guidance |
|---|---|---|---|
| **center3 / stc Group** | https://center3.com/ and global network map https://center3.com/global-network | Official site says Saudi DCs are in Riyadh, Jeddah, and Dammam; network map buckets: KSA Central, Eastern, Western, Northern, Southern. DCD reports target of 300MW by 2027 and 1GW by 2030. | Official location existence **A-**; expansion totals **B** unless facility-specific. |
| **STC legacy / Saudi Telecom** | stc annual reports, center3, CST, Uptime Institute, DCD | Older facilities include Al Raidah Digital City and 2021 launches in Riyadh/Jeddah/Madinah. Watch for same sites rebranded under center3. | **A/B** depending source. |
| **Mobily / Etihad Etisalat** | CST list, Mobily official, Uptime, DataCenterMap | Riyadh Khurais, Malga/Melgha, Jeddah, Khobar/Dammam; often telco/enterprise colo rather than hyperscale. | CST/operator **A**; directory capacity **C**. |
| **Zain KSA** | CST, Zain annual reports, Ericsson/Uptime, directory leads | Riyadh and Jeddah-style telco cloud/edge facilities. | **A/B** for official; **C** for maps. |
| **Salam / Integrated Telecom Company (ITC)** | CST, Salam official, telecom press | CST lists Riyadh cloud facilities; Salam owns national fiber and Jeddah/Khobar cable landing infrastructure. | CST **A**; facility MW usually unknown. |
| **NourNet** | https://nour.net.sa/data-center/tier-3-data-center-in-ksa/ | Officially describes a Tier-3 Riyadh datacenter north of Riyadh, 4,500 sqm, 450 racks, 10 MVA allocation. | **A-** operator official. |
| **Quantum Switch Tamasuk (QST)** | https://qst.com.sa/ and https://www.quantumswitch.com/ news | QST official says 300MW plan: six 50MW facilities by 2026; DCD/MEED place facilities in Riyadh, Dammam, Jeddah, NEOM; first Dammam site at SPARK near Abqaiq. Quantum Switch home page lists Dammam capacity of 9MW. | Operator/news **A-/B**; 300MW is program-level planned capacity. |
| **DataVolt** | https://data-volt.com/ and NEOM official release https://www.neom.com/en-us/newsroom/datavolt-signs-agreement-with-neom | Riyadh First Technology Park MODON lease, Yanbu leads, and NEOM Oxagon 1.5GW AI factory campus with first phase target around 2028 per NEOM/DCD. | NEOM release **A-** for signed agreement; capacity/stage **B** until permits/CST/construction. |
| **EDGNEX / DAMAC Digital / DAMAC Data Centres** | https://damacdigital.com/ plus DCD/Baxtel/contractors | Dammam operational/under construction; Riyadh campus. DCD reported a 20MW Riyadh facility; contractors mention Dammam/Riyadh work and expansion from 20MW to 55MW. | Operator page broad **A-**; facility specifics often **B/C**. |
| **Gulf Data Hub (GDH)** | https://www.gulfdatahub.ae/ | Official location page includes Jeddah and Dammam; S&P/DCD report Saudi facilities in Jeddah/Dammam and Riyadh/Dammam expansions. | Official location **A-**; MW via S&P/DCD **B**. |
| **Sahayeb / Saudi Data Center Fund 1 / MIS** | https://sahayeb.sa/ and Saudi Exchange ticker 7200 | Official site says 6 datacenters, 24MW initial capacity, 120MW expandability; Saudi Exchange mentions Riyadh and Dammam facilities and MIS expansion/contracts. | Saudi Exchange **A**; Sahayeb official **A-**. |
| **Ezditek** | Operator site/social, DCD/Data Centre Review, MODON | RUH01 at Princess Nourah University; planned multi-city 170MW program references include Riyadh, Jeddah, Dammam. | **B** until CST/permit/operator facility pages. |
| **Khazna Data Centers** | https://khaznadatacenters.com/ press releases | Official 2025 release names Dammam site with up to 200MW AI-ready capacity; new Saudi country head. | Operator press **A-/B**; planned until construction/permit. |
| **HUMAIN** | PIF/HUMAIN official, Saudi Exchange/MIS, AirTrunk/Blackstone press | AI infrastructure demand driver; contracts with MIS and AirTrunk partnership for Riyadh campus. | **A** when Saudi Exchange/PIF; otherwise **B**. |
| **ZeroPoint DC / NEOM digital infrastructure** | NEOM, DataCenterMap, trade press | NEOM/Tabuk pipeline; directory claims require primary confirmation. | Often **C** unless NEOM/operator official. |
| **Cloud host partners** | Oracle/Google/AWS/Microsoft official plus CST/operator | Oracle Riyadh host partner center3; Google Dammam linked in press to Aramco partnership; Microsoft/AWS locations not fully public. | Cloud region city **A**, physical facility **B/C** until confirmed. |

Arabic operator names useful for search:

```text
سنتر3 OR سنتر 3 OR مركز 3 OR center3
الاتصالات السعودية OR اس تي سي OR stc
موبايلي OR اتحاد اتصالات
زين السعودية
سلام OR شركة الاتصالات المتكاملة
كوانتم سويتش تماسك OR كوانتوم سويتش OR تماسك
داتا فولت OR داتافولت
داماك الرقمية OR إدج نكس OR ادجنكس
جلف داتا هب OR مركز بيانات الخليج
سحايب OR صحائب OR المعمر لأنظمة المعلومات OR ام آي اس
ازدتك OR إزديتك
خزنة OR خازنة
هيوماين OR شركة المستقبل للذكاء الاصطناعي
نيوم OR أوكساجون
```

---

## 4. English + Arabic Discovery Queries

### 4.1 National broad sweep

```text
"Saudi Arabia" ("data center" OR datacenter OR "data centre") ("MW" OR megawatt OR racks OR "under construction" OR "land lease")
"Saudi Arabia" "AI data center" OR "AI factory" "MW"
"Saudi Arabia" "data center" "LEAP 2025" OR "LEAP 2026"
"Saudi Arabia" "data center" ("MODON" OR "SPARK" OR "Oxagon" OR "NEOM" OR "Digital City")
"Saudi Arabia" "data center" ("Riyadh" OR "Jeddah" OR "Dammam" OR "Khobar" OR "Madinah" OR "Buraydah")
"Saudi Arabia" "data center" "Saudi Exchange" OR "Tadawul"
"Saudi Arabia" "data center" "Aramco" OR "HUMAIN" OR "PIF"
```

Arabic broad sweep:

```text
"مركز بيانات" "السعودية" ("ميجاواط" OR "ميغاواط" OR "رفوف" OR "رخصة" OR "ترسية" OR "تدشين" OR "افتتاح")
"مراكز البيانات" "السعودية" ("الرياض" OR "جدة" OR "الدمام" OR "الخبر" OR "نيوم")
"مركز بيانات" "السعودية" "ليب"
"مركز بيانات" "مدن" "الرياض"
"مركز بيانات" "سبارك" OR "مدينة الملك سلمان للطاقة"
"مركز بيانات" "أوكساجون" OR "نيوم"
"مراكز البيانات" "أرامكو" "تأجير"
"مركز بيانات" "هيوماين" "ترسية"
```

### 4.2 Capacity extraction

```text
"{project/operator}" ("MW" OR "megawatt" OR "MVA" OR "IT load" OR racks OR "raised floor")
"{project/operator}" ("capacity" OR "expandable" OR "phase 1" OR "first phase")
"{project/operator}" ("design certification" OR "Tier III" OR "Tier IV" OR Uptime)
"{operator_ar}" ("ميجاواط" OR "ميغاواط" OR "ميغا فولت أمبير" OR "رفوف" OR "سعة" OR "المرحلة الأولى")
```

### 4.3 Status extraction

```text
"{project}" ("breaks ground" OR "construction" OR "go live" OR "opened" OR "launched" OR "operational")
"{project}" ("secures financing" OR "awarded" OR "contractor" OR "EPC" OR "design and build")
"{project_ar}" ("قيد الإنشاء" OR "بدء الأعمال" OR "ترسية" OR "افتتاح" OR "تدشين" OR "تشغيل" OR "المرحلة الأولى")
```

### 4.4 Contractor and supplier backfill

Saudi datacenter projects often leak through EPC/MEP/cooling contractor portfolios before operators disclose details.

```text
"Saudi Arabia" "data center" ("EPC" OR "MEP" OR "design and build" OR "cooling" OR "genset")
"Riyadh" "data center" "contractor" "MW"
"Dammam" "data center" "SPARK" "contractor"
"Jeddah" "data center" "MEP"
"مركز بيانات" "الرياض" "مقاول" OR "الأعمال الكهروميكانيكية"
"مركز بيانات" "الدمام" "تبريد" OR "مولدات"
```

Known contractor/supplier pivots from public snippets: Group AMANA for QST Dammam, EAMFCO/ABL for EDGNEX/DAMAC, LG/Shaker for DataVolt/NEOM cooling, Vertiv for GDH case studies, Alekhtiar for Mobily facility work.

---

## 5. Province-by-Province Enumeration Map

The world manifest uses governorate-level divisions. For efficiency, sweep at **region/province + major city/governorate** level first, then assign results to GeoNames admin2 governorates by address.

For each row, run both the English and Arabic templates:

```text
"{region_or_city}" ("data center" OR datacenter OR "data centre" OR "cloud region" OR "AI factory") ("MW" OR "racks" OR "construction" OR "launched")
"{city_ar}" ("مركز بيانات" OR "مراكز البيانات" OR "مركز بيانات سحابي") ("ميجاواط" OR "رفوف" OR "رخصة" OR "ترسية" OR "افتتاح" OR "تدشين")
site:cst.gov.sa "{city_en_or_ar}" "Data Center"
site:balady.gov.sa "{city_ar}" "مركز بيانات"
site:modon.gov.sa "{city_ar}" "مركز بيانات"
```

| Region | Arabic region / priority place names | How to query / expected yield |
|---|---|---|
| **Riyadh Region** | منطقة الرياض; الرياض; الدرعية; الخرج; المدينة الرقمية; طريق خريص; الملز/الملقا; جامعة الأميرة نورة; المدينة الصناعية الجديدة; وادي الرياض للتقنية | Highest priority. Query center3/STC, Mobily, NourNet, Oracle Riyadh, SCCC/Alibaba, Sahayeb, DataVolt/MODON, Ezditek RUH01, DAMAC/EDGNEX, HUMAIN/AirTrunk/MIS. Use `site:saudiexchange.sa "الرياض" "مراكز البيانات"` and `site:modon.gov.sa "الرياض" "مركز بيانات"`. |
| **Eastern Province** | المنطقة الشرقية; الدمام; الخبر; الظهران; الأحساء; الجبيل; بقيق; سبارك; مدينة الملك سلمان للطاقة; المدينة الصناعية الثانية بالدمام | Highest priority. Query Google Cloud Dammam, Microsoft Saudi Arabia East, QST SPARK/Dammam, center3 Dammam/Khobar, DAMAC/EDGNEX Dammam, GDH Dammam, Khazna Dammam, Sahayeb Dammam, Aramco/MIS leasing. Include SPARK/Abqaiq and Dammam Second Industrial City terms. |
| **Makkah Region** | منطقة مكة المكرمة; جدة; مكة; رابغ; مدينة الملك عبدالله الاقتصادية / KAEC; الشعيبة | High priority. Query Oracle Jeddah, center3 Jeddah/Makkah, GDH Jeddah, QST Jeddah planned, Mobily/Zain/STC west-coast sites, Hajj/Umrah government datacenters, cable landing/gateway references. |
| **Medina Region** | منطقة المدينة المنورة; المدينة المنورة; ينبع; العلا | Medium. Query center3 Al-Madinah, DataVolt Yanbu, YASREF/industrial datacenters, Royal Commission/Yanbu industrial city, AlUla smart-city/edge. |
| **Tabuk Region** | منطقة تبوك; تبوك; نيوم; أوكساجون; ضباء; حقل; شرما | High pipeline, lower operational evidence. Query DataVolt NEOM/Oxagon, QST NEOM planned, ZeroPoint DC, center3 Haql cable landing, NEOM digital infrastructure. Treat MoUs as planned until construction/CST. |
| **Al-Qassim Region** | منطقة القصيم; بريدة; عنيزة | Medium. Query center3 Buraydah / NEIDC-Qassim, STC/Mobily/Zain, regional government DR, universities. |
| **Asir Region** | منطقة عسير; أبها; خميس مشيط; بيشة | Low/medium. Query regional government, university, telco edge, healthcare clusters; use Arabic only before no-project. |
| **Jazan Region** | منطقة جازان; جازان; بيش; صبيا; أبو عريش | Low/medium. Query Jazan City for Primary and Downstream Industries, port/industrial city, Aramco/smart city, university/government DR. |
| **Hail Region** | منطقة حائل; حائل | Low/medium. Known weak directory leads for CenterServ Ha'il; verify with CST/operator before counting. Query university/regional government/telco. |
| **Al Bahah Region** | منطقة الباحة; الباحة; بلجرشي | Low. Mostly government/university/edge. Arabic search critical. |
| **Al Jawf Region** | منطقة الجوف; سكاكا; القريات; دومة الجندل | Low. Query renewable/industrial or university facilities; beware false hits for generic "data center" services. |
| **Najran Region** | منطقة نجران; نجران; شرورة | Low. Mostly university/government institutional datacenters. Do not count training/development centers as commercial colocation unless facility evidence exists. |
| **Northern Borders Region** | منطقة الحدود الشمالية; عرعر; رفحاء; طريف | Low. Query Northern Borders University, regional government, telco edge, Aramco/mining/industrial projects. |

For individual governorates, add transliteration variants:

```text
"Al Khobar" OR Khobar OR الخبر
"Dammam" OR Ad Dammam OR الدمام
"Abqaiq" OR Buqayq OR بقيق
"Jiddah" OR Jeddah OR جدة
"Makkah" OR Mecca OR مكة
"Al Madinah" OR Medina OR المدينة المنورة
"Yanbu" OR "Yanbu al Bahr" OR ينبع
"Buraydah" OR بريدة
"Haql" OR حقل
```

---

## 6. Verification and Evidence Grading

### 6.1 Evidence hierarchy

1. **A — regulator/permit/exchange/operator official**: CST registered datacenter provider page; Balady/MOMAH permit or activity license pages; MODON official land/industrial-city announcements; Saudi Exchange/Tadawul disclosures; official cloud region pages; operator facility pages with location/capacity; Uptime Institute certified-facility pages when they name city/operator.
2. **B — strong secondary**: DCD, MEED, W.Media, Capacity Media, Argaam, S&P Global, Dgtl Infra, Total Telecom, Developing Telecoms, contractor portfolio pages, supplier case studies.
3. **C — directories/aggregators/social**: DataCenterMap, Baxtel, Datacenters.com, DC Byte, Reboot Monkey, LinkedIn posts, broker pages, generic "top datacenter" blogs. Use them as leads and alias maps.

### 6.2 Status normalization

- `signed`, `MoU`, `agreement`, `land lease`, `investment plan`: **planned** unless permit/construction evidence exists.
- `financing secured`, `contract awarded`, `EPC`, `design and build`: **planned/construction**, depending wording and contractor mobilization.
- `breaks ground`, `under construction`, `construction works advanced`: **construction**.
- `launched`, `opened`, `go-live`, `available`, CST registered as non-Qualifying: **operational**, unless the source clearly describes future availability.
- Cloud region pages prove **cloud service region existence**, not exact building ownership or address. Count physical facilities only when the region can be tied to a host/operator/city and not double-counted.

### 6.3 Saudi-specific pitfalls

- **Program MW vs facility MW**: QST 300MW, center3 1GW/300MW, DataVolt 1.5GW, Khazna 200MW, and Sahayeb 120MW are program/campus maximums. Do not assign the full number to a single facility unless the source says so.
- **City vs governorate mismatch**: "Dammam market" may mean Dammam city, Al Khobar, Dhahran, SPARK near Abqaiq, or Dammam Second Industrial City. Assign by the most precise site clue.
- **NEOM/Oxagon inflation**: treat NEOM mega-campus announcements as planned; look for Oxagon land lease, EPC, cooling equipment, grid/substation, or CST registration before advancing stage.
- **Arabic "مركز معلومات" vs "مركز بيانات"**: many government "information centers" are offices, not datacenters. Require facility/infrastructure terms: racks, power, cooling, hosting, colocation, cloud, DR.
- **Subsea/cable landing vs datacenter**: Jeddah, Khobar, Dammam, and Haql have cable/gateway infrastructure. Count a cable landing station only if the project scope includes datacenter/colo/hosting facility.
- **Directory stale capacity**: Saudi directory entries often repeat marketing MW or mix MVA with IT load. Prefer Saudi Exchange, operator pages, or trade press citing project finance.
- **Hijri dates**: Saudi Exchange and Arabic official pages often show Hijri + Gregorian. Always record Gregorian equivalent if shown.

---

## 7. Recommended Saudi Enumeration Pipeline

1. **CST seed**: scrape/manual-export registered Data Center Services Providers; capture provider, facility name, city, category, and page date. This is the base legal-service list.
2. **Operator sweep**: run the table in §3 for center3, Mobily, Salam, Zain, NourNet, QST, DataVolt, DAMAC/EDGNEX, GDH, Sahayeb/MIS, Ezditek, Khazna, HUMAIN, and ZeroPoint. Capture official page + capacity source separately.
3. **Cloud-region join**: add Oracle Riyadh/Jeddah, Google Dammam, Microsoft Saudi Arabia East, AWS Saudi planned region, SCCC/Alibaba Riyadh. Do not infer addresses beyond public host/city evidence.
4. **Riyadh/Eastern/Jeddah deep dive**: run Arabic and English city templates plus MODON/Balady/Saudi Exchange queries. These three markets should receive the most time.
5. **NEOM/Oxagon pipeline check**: search NEOM, Oxagon, Tabuk, Duba, Haql with DataVolt/QST/ZeroPoint/center3. Keep stage conservative.
6. **Contractor/supplier backfill**: search EPC/MEP/cooling suppliers for facility details, especially for DAMAC/EDGNEX, QST, GDH, and DataVolt.
7. **Remaining regions**: Arabic-first searches for universities, regional emirates, municipalities, telcos, and government DR centers. Most will be no-project or institutional-only.
8. **Dedupe**: normalize by ultimate parent + campus + phase + precise locality. Example: STC legacy facility may appear as STC, center3, cloud host partner, or Uptime-certified site.

Minimum source bundle for a strong record:

```text
1 official/regulator/operator source for existence/status
+ 1 capacity/status source from Saudi Exchange, operator, trade press, or contractor
+ 1 locality source precise enough for region/governorate assignment
```

Use a **no_projects** result only after checking: English name, Arabic name, major transliterations, `"مركز بيانات"`, `"مراكز البيانات"`, `"data center"`, `"datacenter"`, telco/operator names, and nearest hub spillover.

