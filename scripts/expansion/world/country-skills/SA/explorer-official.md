# SA Explorer — Official / Regulatory / Cloud Pipeline for Saudi Arabia Datacenter Enumeration

Date: 2026-08-12. Country: **SA Saudi Arabia**. Division model for world expansion: **governorates nested under regions** (GeoNames admin2; examples: `Riyadh Region - Ar Riyad`, `Eastern Province - Ad Dammam`, `Mecca Region - Jiddah`, `Tabuk Region - Duba'`). Focus: official/regulatory/cloud pipeline: Vision 2030 / MCIT / CST regulation, municipal and environmental permits, SEC / National Grid power evidence, official hyperscale cloud regions, and priority colo/operator sources.

Reliability grades used here:
- **A** = primary / official / legally accountable source: CST data-center or cloud registration, MCIT / SPA / Vision 2030 / SDAIA / NEOM / MODON announcement, Balady municipal permit, NCEC environmental permit, SEC / National Grid interconnection or tender, official cloud-region page, operator official facility page, Saudi Exchange / annual report.
- **B** = strong secondary source: established trade press, official event coverage with named parties but no permit, paid directory snippet corroborated by an operator/regulator, Uptime certificate lookup.
- **C** = weak lead: market-report teasers, LinkedIn / social posts, directory-only capacity, consultant articles with no primary document.

---

## 0. Saudi-Specific Structure Facts

Saudi Arabia is better approached as a **regulated digital-infrastructure market plus permit joins**, not as a single open planning database.

1. **CST is the key regulator.** The Communications, Space and Technology Commission (formerly CITC) issued the **Provision of Data Centers Services Regulation**, decision no. `502/1445`, dated 2023-08-22, and announced that it entered into force on 2024-01-01. CST also maintains public pages for **registered data center service providers** and **registered cloud computing service providers**. These are the best A-grade starting points for commercial / carrier-neutral facilities, but they are not guaranteed to expose full address, MW, or all captive enterprise facilities.
2. **Cloud computing is separately registered.** CST cloud registration categories include Qualifying / Class A / Class B / Class C; Google Cloud documentation says CST granted Google Cloud a Class C license for the Dammam region. Use cloud registration to find facility-level partners and sovereignty restrictions, then pivot to data-center service-provider registrations and operator pages.
3. **Planning evidence is fragmented.** Use **Balady** and Ministry of Municipalities and Housing services for building permits / completion certificates, plus local Amanah / municipality pages. Many public records require Nafath login or permit number, so public recall is lower than UK-style planning registers.
4. **Environmental evidence is NCEC-led.** The National Center for Environmental Compliance has an eCompliance / environmental-permit service. Datacenters may trigger NCEC permitting through diesel generators, fuel storage, battery systems, chillers, water use, wastewater, e-waste, and construction impacts.
5. **Power is often the decisive proof.** Saudi Electricity Company / Saudi Energy and its wholly owned **National Grid SA** subsidiary plan, operate, and maintain the transmission network. Search for EHV substations, high-load customer connections, 110/132/380 kV works, and SEC tenders around known campuses.
6. **Hyperscale / AI announcements are large and often phased.** Treat 1.5 GW / 1 GW / 300 MW / 200 MW figures as **program or campus-plan capacity** unless a permit, energization, annual report, or operator spec sheet assigns capacity to a specific site and phase.

Highest-priority geographies:
- **Riyadh Region - Ar Riyad / Ad Dir`iyah / Huraymila'**: center3 / stc, Azure Saudi Arabia East business presence, Oracle Riyadh, Huawei / Alibaba / SCCC, Sahayeb, Ezditek, DataVolt MODON, HUMAIN, government SDAIA facilities.
- **Eastern Province - Ad Dammam / Al Khubar / Al Jubayl / Al Ahsa'**: Google Cloud Dammam `me-central2`, Azure Saudi Arabia East AZs, Khazna Dammam, Mobily Dammam, QST, Sahayeb, industrial and energy-adjacent sites.
- **Mecca Region - Jiddah / Makkah al Mukarramah / Rabigh**: Oracle Jeddah, center3 / Mobily / Salam facilities, cable landing and coastal connectivity, Hajj / government resilience facilities.
- **Tabuk Region - Duba' / Tabuk / Haql**: NEOM / OXAGON / TONOMUS / DataVolt / Oracle NEOM plans and Red Sea cable landing stations.
- **Medina Region - Al Madinah al Munawwarah / Yanbu` al Bahr**: center3 Al-Madinah and Yanbu industrial / energy leads.
- **Al-Qassim Region - Governorate of Unaizah**: Mobily Unaizah / edge facility leads.

---

## 1. Official / Regulatory Backbone

### 1.1 CST Data Center Services

- Registered data center providers: https://www.cst.gov.sa/en/knowledge-center/digital-knowledge/data-center/data-centers-providers
- Data-center knowledge page: https://www.cst.gov.sa/en/knowledge-center/digital-knowledge/data-center
- Regulation page: https://www.cst.gov.sa/en/regulations-and-licenses/regulations/Document-1546
- Registration service: https://www.cst.gov.sa/en/business/services/Datacenter-registration
- Enforcement announcement: https://www.cst.gov.sa/en/media-center/news/CST-Announces-that-the-Data-Center-Services-Regulations-Document-has-Entered-Into-Force

Use: A-grade operator/facility seed. The registration service says the request is made through CST's Business Portal via Nafath and has a 15-day process time. The regulation page frames data centers as part of the Kingdom's goal to be a regional data-processing and digital-content hub. CST's public provider page should be scraped / checked manually for provider name, facility name, city, registration category, and status.

Grade: **A** for provider authorization, named facility, city, and registration class. **B** for capacity unless CST publishes MW or certification evidence.

Query templates:
```text
site:cst.gov.sa "Data Centers Service Providers" "Riyadh"
site:cst.gov.sa "Data Centers Service Providers" "Dammam"
site:cst.gov.sa "Data Centers Service Providers" "Jeddah"
site:cst.gov.sa "Registered Data Center Services Providers" "center3"
site:cst.gov.sa "Registered Data Center Services Providers" "Mobily"
site:cst.gov.sa "Registered Data Center Services Providers" "Salam"
site:cst.gov.sa "QST Data Centre"
site:cst.gov.sa "Khurais DC"
```

Arabic:
```text
site:cst.gov.sa "مراكز البيانات" "الرياض"
site:cst.gov.sa "مقدمي خدمات مراكز البيانات"
site:cst.gov.sa "تسجيل مركز بيانات"
site:cst.gov.sa "خدمات مراكز البيانات" "جدة"
site:cst.gov.sa "خدمات مراكز البيانات" "الدمام"
```

### 1.2 CST Cloud Computing Registration

- Cloud computing page: https://www.cst.gov.sa/en/knowledge-center/digital-knowledge/cloud-computing
- Registered cloud providers: https://www.cst.gov.sa/en/knowledge-center/digital-knowledge/cloud-computing/cloud-computing-providers
- Cloud registration service: https://www.cst.gov.sa/en/business/services/Cloud-Computing-Registration
- Cloud regulations: https://www.cst.gov.sa/en/regulations-and-licenses/regulations/Document-1550
- Provider guide: https://www.cst.gov.sa/en/regulations-and-licenses/other-documents/Document-1552

Use: confirm that a hyperscaler or local CSP is authorized to provide cloud services in KSA and identify its class. The cloud registration service lists certification requirements for datacenters, including Tier 2 / ISO 27001 for Class A and Tier 3 construction + operational sustainability certificates for Class B / C.

Grade: **A** for cloud-provider registration and class. Use as a lead only for physical facilities unless the registration names a facility / region.

Query templates:
```text
site:cst.gov.sa "Cloud Computing Services Providers" "Class C"
site:cst.gov.sa "Cloud Computing Registration" "Class C"
site:cst.gov.sa "Google Cloud" "Class C"
site:cst.gov.sa "Oracle" "Class C"
site:cst.gov.sa "Alibaba Cloud" "Class C"
site:cst.gov.sa "Huawei Cloud" "Class C"
```

### 1.3 MCIT / Vision 2030 / SDAIA / SPA Strategy Leads

- MCIT: https://mcit.gov.sa/en
- MCIT LEAP 2023 data-center announcement: https://mcit.gov.sa/en/news/leap-23-announces-580-million-investment-data-center-and-2-tech-skills-academies
- Vision 2030 HUMAIN page: https://www.vision2030.gov.sa/en/explore/projects/humain
- SDAIA National Data & AI Strategy: https://sdaia.gov.sa/en/SDAIA/SdaiaStrategies/Pages/NationalStrategyForDataAndAI.aspx
- Saudi Press Agency search / examples: https://www.spa.gov.sa/ and https://www.spa.gov.sa/2250494
- U.S. International Trade Administration market note on the national strategy: https://www.trade.gov/market-intelligence/saudi-arabia-ict-new-data-center-strategy-accelerate-ai-and-cloud-expansion

Use: seed national programs and official MoUs. MCIT / SPA pages are A-grade for signed government programs such as the Hyperscale Data Center Enablement Initiative and MCIT partnerships, but they often omit governorate and permit status. ITA is **B** as a government trade summary; it is useful for the MCIT/SDAIA 1.5 GW by 2030 target when the original strategy page is not public or is hard to retrieve.

Query templates:
```text
site:mcit.gov.sa "data center" "Saudi Arabia"
site:mcit.gov.sa "data centre" "LEAP"
site:spa.gov.sa "data center" "Ministry of Communications"
site:spa.gov.sa "data center" "SDAIA"
site:vision2030.gov.sa "data centers" "HUMAIN"
site:sdaia.gov.sa "data center" "Riyadh"
```

Arabic:
```text
site:mcit.gov.sa "مركز بيانات" "ليب"
site:spa.gov.sa "مراكز البيانات" "وزارة الاتصالات"
site:spa.gov.sa "مركز بيانات" "سدايا"
site:vision2030.gov.sa "مراكز البيانات" "هيوماين"
```

### 1.4 Saudi Exchange / Listed-Company Filings

- Saudi Exchange issuer / disclosures entry point: https://www.saudiexchange.sa/
- stc group subsidiaries: https://www.stc.com.sa/content/stcgroupwebsite/sa/en/who-we-are/group-subsidiaries.html
- stc Annual Report 2022 subsidiaries page: https://www.stc.com.sa/content/dam/stc/stc-annual-report-2022/en/subsidiaries.html
- stc Annual Report 2023 year-in-review: https://www.stc.com.sa/content/dam/stc/stc-annual-report-2023/year-in-review.html
- MIS / Sahayeb subsidiaries: https://www.mis.com.sa/about-us/subsidiaries/

Use: A-grade capacity and corporate-structure evidence where filings are official. stc's 2022 annual report says center3 owns stc Group's digital infrastructure assets, including data centers and submarine cables, and references a capacity / DC access base up to 125 MW with a plan to raise it to 300 MW. stc's 2023 year-in-review says center3 completed a 9.6 MW expansion of its Khurais hyperscaler-grade data center in Riyadh. MIS's official subsidiaries page says Sahayeb has 6 data centers in Riyadh and Dammam, 24 MW initial capacity, and 120 MW expandability.

Grade: **A** for annual-report facts, ownership, and named capacity; **B** for forward-looking capacity plans.

Query templates:
```text
site:saudiexchange.sa "data center" "stc"
site:saudiexchange.sa "center3"
site:saudiexchange.sa "Mobily" "data center"
site:saudiexchange.sa "Al Moammar" "data center"
site:stc.com.sa "center3" "MW"
site:mis.com.sa "Sahayeb" "MW"
```

---

## 2. Planning, Permits, Environment, and Energy

### 2.1 Municipal / Building Permits — Balady and Local Amanah

- Balady building permit service: https://balady.gov.sa/en/services/issuing-building-permit
- Ministry of Municipalities and Housing building permit inquiry: https://momah.gov.sa/en/e-services/inquiring-about-building-license
- National portal mirror: https://my.gov.sa/en/services/19127

Use: A-grade evidence for construction authorization, fencing permit, building permit, correction of permit data, and completion certificate when accessible. Public search often requires a permit number, owner ID, or Nafath login. Therefore use Balady primarily after an operator page, contractor page, or tender gives a plot / district / permit number.

What to extract: municipality / Amanah, permit number, parcel / plot, owner or legal entity, building use, area sqm, floors, issue date, status, supervising engineering office, completion certificate.

Query templates:
```text
site:balady.gov.sa "data center" "building permit"
site:momah.gov.sa "data center" "building permit"
"Balady" "data center" "Riyadh"
"building permit" "data center" "Dammam" "Saudi Arabia"
"completion certificate" "data center" "Saudi Arabia"
```

Arabic:
```text
site:balady.gov.sa "مركز بيانات" "رخصة بناء"
site:momah.gov.sa "مركز بيانات" "رخصة بناء"
"رخصة بناء" "مركز بيانات" "الرياض"
"شهادة إتمام بناء" "مركز بيانات"
"الأمانة" "مركز بيانات" "الدمام"
```

### 2.2 Environmental Permits — NCEC

- NCEC: https://www.ncec.gov.sa/
- NCEC environmental permit service: https://www.ncec.gov.sa/ar/eServices/EservicesDirectory/Environmentalpermit/Pages/default.aspx
- eCompliance portal: https://ecompliance.ncec.gov.sa/

Use: A-grade environmental-permit and compliance evidence where public permit records or PDFs are available. Datacenters are not always named as a special class; search by operator, project, diesel generator, fuel tank, battery, chiller, cooling plant, wastewater, and industrial city.

What to extract: permit number, applicant, activity, coordinates / city, environmental classification, generator count and MW/MVA, fuel storage, water draw, wastewater / STP, noise / air-quality mitigation, validity, inspection or violation history.

Query templates:
```text
site:ncec.gov.sa "data center" "Riyadh"
site:ncec.gov.sa "data centre" "Dammam"
site:ncec.gov.sa "diesel generator" "data center"
site:ecompliance.ncec.gov.sa "data center"
"NCEC" "data center" "environmental permit" "Saudi Arabia"
```

Arabic:
```text
site:ncec.gov.sa "مركز بيانات" "تصريح بيئي"
site:ncec.gov.sa "مراكز البيانات" "التصريح البيئي"
"مولدات ديزل" "مركز بيانات" "الرياض"
"خزانات وقود" "مركز بيانات" "الدمام"
"المركز الوطني للرقابة على الالتزام البيئي" "مركز بيانات"
```

### 2.3 Power and Grid — Saudi Energy / SEC / National Grid SA

- Saudi Energy / Saudi Electricity Company: https://www.se.com.sa/en
- National Grid SA introduction: https://www.se.com.sa/en/Whoweare/National-Grid-SA/Introduction/
- SEC open data: https://www.se.com.sa/en/Open-Data/Open-Data/
- Government procurement / Etimad overview: https://www.mof.gov.sa/en/eservices/Pages/Etimad.aspx and https://ncgr.gov.sa/en/etimad-platform

Use: A-grade evidence for grid connection, new substations, transmission works, utility tenders, and government data-center operations contracts. National Grid SA is SEC's transmission subsidiary and the official target for 110/132/380 kV connection evidence. SEC open-data is useful for network context; detailed customer interconnection records may not be public.

Search around known project names and industrial zones, not only "data center". High-value terms include `380 kV`, `132 kV`, `110 kV`, `substation`, `load`, `bulk supply`, `grid connection`, `energization`, `GIS`, `transformer`, `National Grid SA`.

Query templates:
```text
site:se.com.sa "data center"
site:se.com.sa "data centre"
site:se.com.sa "National Grid" "data center"
site:se.com.sa "380 kV" "data center"
site:se.com.sa "132 kV" "Riyadh" "data center"
site:se.com.sa "Dammam" "substation" "data center"
site:etimad.sa "data center" "SEC"
"Saudi Electricity Company" "data center" "Riyadh"
"National Grid SA" "data center" "Dammam"
```

Arabic:
```text
site:se.com.sa "مركز بيانات"
site:se.com.sa "مراكز البيانات"
site:se.com.sa "محطة تحويل" "مركز بيانات"
site:se.com.sa "الشبكة الوطنية" "مركز بيانات"
"الشركة السعودية للكهرباء" "مركز بيانات"
"محطة 380 ك.ف" "مركز بيانات"
"محطة 132 ك.ف" "الرياض" "مركز بيانات"
```

### 2.4 Industrial Land / Special Zones / Mega-Projects

- MODON: https://modon.gov.sa/
- NEOM: https://www.neom.com/
- OXAGON / DataVolt NEOM announcement: https://www.neom.com/en-us/newsroom/datavolt-signs-agreement-with-neom
- MISA: https://misa.gov.sa/
- Economic Cities and Special Zones Authority: https://ecza.gov.sa/
- Royal Commission for Jubail and Yanbu: https://www.rcjy.gov.sa/

Use: A-grade for land lease, industrial-city siting, special-zone status, and official mega-project announcements. MODON is especially relevant to Riyadh First Technology Park / First Industrial City leads. NEOM is the official source for OXAGON and TONOMUS-related data-center announcements. RCJY matters for Jubail and Yanbu industrial facilities and energy-intensive campuses.

Query templates:
```text
site:modon.gov.sa "data center" "Riyadh"
site:modon.gov.sa "DataVolt" "data center"
site:neom.com "data center" "DataVolt"
site:neom.com "Oracle" "data center"
site:misa.gov.sa "data center" "Saudi Arabia"
site:ecza.gov.sa "cloud" "data center"
site:rcjy.gov.sa "data center" "Yanbu"
site:rcjy.gov.sa "data center" "Jubail"
```

Arabic:
```text
site:modon.gov.sa "مركز بيانات"
site:modon.gov.sa "داتا فولت"
site:neom.com "مركز بيانات" "أوكساجون"
site:misa.gov.sa "مراكز البيانات"
site:rcjy.gov.sa "مركز بيانات" "ينبع"
```

---

## 3. Official Cloud Provider Region Pages

Cloud-region pages are **A-grade for region/city or region/area existence**, but not exact facility addresses. Use them to seed local CST, Balady, NCEC, SEC, and operator searches.

| Provider | Official source | Saudi region signal | Enumeration value |
|---|---|---|---|
| AWS | Press release: https://press.aboutamazon.com/2024/3/aws-to-launch-an-infrastructure-region-in-the-kingdom-of-saudi-arabia ; global regions: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | AWS announced a Saudi Arabia Region for 2026, with three Availability Zones at launch and planned investment above USD 5.3B. | Search for AWS, Amazon Web Services EMEA SARL, local contractors, and HUMAIN / Riyadh AI Zone in Riyadh and Eastern Province; exact AZ locations are undisclosed. |
| Microsoft Azure | Microsoft EMEA release: https://news.microsoft.com/source/emea/2026/02/microsoft-confirms-saudi-arabia-datacenter-region-available-for-customers-to-run-cloud-workloads-from-q4-2026/ ; Azure geography list: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | Saudi Arabia East region available for customer workloads from Q4 2026; Microsoft says the region is in Eastern Province and includes three AZs with independent power/cooling/networking. | Prioritize `Eastern Province - Ad Dammam`, `Al Khubar`, and nearby industrial municipalities; search Microsoft + Balady/NCEC/SEC + local contractors. |
| Google Cloud | Dammam region access: https://docs.cloud.google.com/docs/dammam-region-access ; locations: https://cloud.google.com/about/locations | Dammam `me-central2`; Google says KSA customers purchase through CNTXT and CST granted a Class C license for Google Cloud in the Dammam region. | Strong A-grade Dammam seed. Search CNTXT, Aramco Digital, Google Cloud, Dammam, Class C, and NCEC/SEC records. |
| Oracle OCI | Riyadh region: https://www.oracle.com/sa/cloud/cloud-regions/riyadh/ ; Oracle regions: https://www.oracle.com/cloud/public-cloud-regions/ | Jeddah region launched in 2020; Riyadh region is Oracle's second Saudi cloud region; NEOM region has been announced/planned in Oracle / NEOM coverage. | Join Oracle Jeddah/Riyadh/NEOM to center3 / NEOM / TONOMUS and CST cloud registration. |
| Huawei Cloud | Compliance page: https://www.huaweicloud.com/intl/en-us/securecenter/compliance/compliance-center/ksa-classc.html | Huawei Cloud states it holds Saudi Class C registration; Riyadh cloud-region launch is widely reported but verify through CST and Huawei official docs. | Use as a Riyadh cloud seed; do not count a physical site without CST / operator / permit evidence. |
| Alibaba Cloud / SCCC | stc history page: https://www.stc.com.sa/content/stcgroupwebsite/sa/en/who-we-are/our-history.html | stc says it established SCCC in 2022 with Alibaba Cloud, eWTP Arabia, SCAI, and SITE to provide cloud computing services in Saudi Arabia. | Search Saudi Cloud Computing Company / SCCC / Alibaba in CST cloud list and Riyadh data-center records. |

Cloud query templates:
```text
"AWS" "Saudi Arabia Region" "Availability Zones"
"AWS" "HUMAIN" "AI Zone" "Riyadh" "data center"
"Microsoft" "Saudi Arabia East" "Eastern Province" "availability zones"
"Google Cloud" "me-central2" "Dammam" "CNTXT"
"Oracle Cloud" "Riyadh Region" "center3"
"Oracle Cloud" "Jeddah Region" "data center"
"Huawei Cloud" "Riyadh Region" "Class C"
"Alibaba Cloud" "SCCC" "Riyadh" "data centers"
```

---

## 4. Colo / Operator Seed List

Operator pages are primary for existence and marketed services, but not always primary for exact capacity. Confirm with CST registration, Saudi Exchange filings, Balady/NCEC/SEC, and Uptime / ISO certificates.

| Operator / entity | Official / strong source | Saudi footprint signal | Follow-up official joins |
|---|---|---|---|
| center3 / stc Group | center3 https://center3.com/ ; stc subsidiaries https://www.stc.com.sa/content/stcgroupwebsite/sa/en/who-we-are/group-subsidiaries.html ; stc annual reports | center3 is wholly owned by stc and owns group infrastructure assets including data centers and submarine cables; center3 markets carrier-neutral data centers in Riyadh, Jeddah, and Dammam; stc reported a 9.6 MW Khurais expansion in Riyadh. | CST data-center providers, Saudi Exchange filings, SEC / National Grid, Balady, NCEC, cable landing permits. |
| Mobily | Official colocation: https://www.mobily.com.sa/wps/portal/web/business/digital/hosting-and-cloud/details/co-location-service | Mobily says its data centers are strategically located in Riyadh, Jeddah, Dammam, and Unaizah. | CST provider list for named Mobily facilities; Saudi Exchange / Mobily filings; Balady/NCEC/SEC in those four cities. |
| Salam / Integrated Telecom Company | Official colocation: https://salam.sa/en/business/managed-services/colocation-hosting | Salam says it has 6 datacenters in Riyadh, Jeddah, and Al Khobar. | CST provider list often gives facility names; search former ITC branding and Salam Narjis / Riyadh cloud data-center terms. |
| Sahayeb Data Park / MIS | MIS subsidiaries: https://www.mis.com.sa/about-us/subsidiaries/ | MIS says Sahayeb has 6 datacenters in Riyadh and Dammam, 24 MW initial capacity and 120 MW expandability. | Saudi Exchange MIS announcements, CST provider list, SEC/National Grid interconnection, Balady/NCEC permits. |
| QST / Quantum Switch Tamasuk | QST Saudi: https://qst.com.sa/ ; QST announcement: https://www.quantumswitch.com/2022/02/07/quantum-switch-tamasuk-to-deliver-data-centre-capacity-to-the-kingdom-of-saudi-arabia/ | QST announced an MCIT agreement for hyperscale / colocation data centers; trade coverage reports a 300 MW program by 2026. | MCIT / SPA original agreement, CST provider list, Balady/NCEC/SEC by Riyadh/Dammam/Jeddah/NEOM. |
| DataVolt | NEOM official: https://www.neom.com/en-us/newsroom/datavolt-signs-agreement-with-neom | NEOM announced a phased OXAGON AI/data-center campus with DataVolt and a first phase expected operational by 2028; separate MODON / Riyadh and Yanbu leads should be verified locally. | NEOM / OXAGON, MODON, RCJY, CST registration, NCEC and SEC connection evidence. |
| TONOMUS / NEOM Tech & Digital / Ezditek | NEOM site and SPA / PR sources; use operator official pages where available | NEOM hyperscale data-center program and Oracle tenancy are strong Tabuk / NEOM seeds; Ezditek has Riyadh and national expansion leads. | NEOM official, CST, Balady/NCEC/SEC, contractor EPC pages. |
| Khazna | Official press release: https://khaznadatacenters.com/press-release/khazna-data-centers-names-new-country-head-and-advances-expansion-plans-in-saudi-arabia-in-support-of-vision-2030/ | Khazna says its first Saudi data center is in Dammam and is intended for cloud / AI hyperscale workloads; DCD reports 225,000 sqm land and up to 200 MW capacity. | Dammam municipality / industrial-city land records, CST registration, NCEC, SEC/National Grid. |
| Equinix | EMEA locations: https://www.equinix.com/data-centers/europe-colocation ; trade LEAP 2025 reports | Equinix does not yet show a Saudi facility on the public locations page; trade coverage says it pledged a USD 1B / 100 MW Saudi data center at LEAP 2025. | Treat as **B** until Equinix adds an official Saudi page or a CST / permit record appears; search Jeddah/Riyadh/Dammam. |
| Orixcom | Equinix partner directory: https://www.equinix.com/partners/partner-directory/orixcom ; Orixcom platform pages https://www.orixcom.com/ | Orixcom provides colocation/connectivity solutions across global data centers and is an Equinix reseller partner; no Saudi-owned facility found in official pages. | Use as a connectivity/reseller lead only; do not count as a Saudi facility without a facility page or CST registration. |
| Gulf Data Hub / DAMAC Digital / Edgnex / Pure DC / AirTrunk / HUMAIN | Official pages and SPA/MCIT/Vision 2030 event releases | Important planned / developing operators in Riyadh, Dammam, Jeddah, NEOM and AI infrastructure. | Require CST / permit / power confirmation before operational counting; many leads are MoUs or pre-development. |

Operator query templates:
```text
"{operator}" "CST" "data center" "Saudi Arabia"
"{operator}" "Balady" "building permit" "data center"
"{operator}" "NCEC" "environmental permit"
"{operator}" "Saudi Electricity Company" "substation"
"{operator}" "National Grid SA" "MW"
"{operator}" "Saudi Exchange" "data center"
"{operator}" "Uptime Institute" "Saudi Arabia"
```

Arabic:
```text
"{operator}" "مركز بيانات" "الرياض"
"{operator}" "مركز بيانات" "الدمام"
"{operator}" "رخصة بناء" "مركز بيانات"
"{operator}" "تصريح بيئي"
"{operator}" "الشركة السعودية للكهرباء"
"{operator}" "محطة تحويل"
```

---

## 5. Per-Division Enumeration Workflow

Run governorate-by-governorate, but start with regional hubs and known operator cities.

### Step A — seed from CST provider registries

1. Open CST registered data-center providers and cloud providers.
2. Export / manually capture every provider, facility name, city, class, and status.
3. Map cities to repo divisions:
   - Riyadh / Al Malqa / Khurais / Narjis / Princess Nourah University -> usually `Riyadh Region - Ar Riyad` or `Riyadh Region - Ad Dir\`iyah` depending exact district.
   - Dammam / Industrial City 2 / Adamah -> `Eastern Province - Ad Dammam`.
   - Al Khobar -> `Eastern Province - Al Khubar`.
   - Jeddah -> `Mecca Region - Jiddah`.
   - Makkah -> `Mecca Region - Makkah al Mukarramah`.
   - Madinah -> `Medina Region - Al Madinah al Munawwarah`.
   - Yanbu -> `Medina Region - Yanbu\` al Bahr`.
   - Duba / OXAGON / Port of NEOM -> usually `Tabuk Region - Duba'`.
   - Haql cable landing -> `Tabuk Region - Haql`.
   - Unaizah -> `Al-Qassim Region - Governorate of Unaizah`.
4. Grade CST-listed existence as **A**. Leave capacity null unless separately evidenced.

### Step B — cloud-region and AI-program joins

For each cloud region / program:
1. Record official cloud region, launch status, and region name.
2. Search the provider + CST + local partner (CNTXT, center3, SCCC, HUMAIN, SITE, TONOMUS).
3. Search Balady/NCEC/SEC around the announced city / province.
4. Do not split AZs into separate facilities unless a permit / operator record reveals separate physical sites.

### Step C — permit and utility confirmation

For every candidate facility:
1. Search Balady / municipality with exact facility, district, parcel, and operator legal name.
2. Search NCEC / eCompliance for environmental permit and generator/fuel/cooling records.
3. Search SEC / National Grid for substation, connection, and transformer evidence.
4. Search Etimad / MOF / NCGR for government data-center tenders and awards. Etimad may require login; web-indexed tender snippets can still expose procurement titles and agencies.

### Step D — corporate filings and certificates

1. For stc / center3, Mobily, MIS / Sahayeb and other listed entities, search Saudi Exchange, annual reports, investor decks, and official press releases.
2. Check Uptime Institute certificate lookup for exact facility names, certification type, and city; treat as **A** for certificate status but not MW.
3. Use operator pages as the facility seed and filings / permits for capacity.

### Step E — status grading

Recommended lifecycle mapping:
- **Announced / MoU**: SPA / MCIT / LEAP / operator press only, no land/permit/power -> `announced`, grade **B/C** depending source.
- **Planned**: official land lease, NEOM/MODON site, CST qualifying registration, or cloud-region commitment -> `planned`, grade **A/B**.
- **Construction**: Balady building permit, contractor EPC page with official client, NCEC permit, or SEC connection works -> `construction`, grade **A/B**.
- **Operational**: CST active provider listing, cloud region live, operator facility page selling service, completion certificate, Uptime operational sustainability, or annual-report operational capacity -> `operational`, grade **A** when primary.

---

## 6. High-Value Saudi Search Playbook

### 6.1 English discovery queries

```text
"Saudi Arabia" "data center" "CST"
"Saudi Arabia" "data centre" "CST"
"Saudi Arabia" "data center" "Class C"
"Saudi Arabia" "data center" "building permit"
"Saudi Arabia" "data center" "environmental permit"
"Saudi Arabia" "data center" "National Grid"
"Saudi Arabia" "data center" "Saudi Electricity Company"
"Riyadh" "data center" "Khurais"
"Dammam" "data center" "Industrial City 2"
"Jeddah" "data center" "Oracle"
"NEOM" "data center" "OXAGON"
"Yanbu" "data center" "RCJY"
```

### 6.2 Arabic discovery queries

```text
"مركز بيانات" "الرياض"
"مراكز البيانات" "الرياض"
"مركز بيانات" "الدمام"
"مركز بيانات" "جدة"
"مركز بيانات" "نيوم"
"مركز بيانات" "أوكساجون"
"مركز بيانات" "رخصة بناء"
"مركز بيانات" "تصريح بيئي"
"مركز بيانات" "الشركة السعودية للكهرباء"
"مركز بيانات" "محطة تحويل"
"مركز بيانات" "وزارة الاتصالات وتقنية المعلومات"
"مركز بيانات" "هيئة الاتصالات والفضاء والتقنية"
"مراكز البيانات" "سدايا"
"مركز بيانات" "مدن"
```

### 6.3 Document and tender queries

```text
filetype:pdf "data center" "Saudi Arabia" "MW"
filetype:pdf "data center" "Riyadh" "substation"
filetype:pdf "data center" "Dammam" "environmental"
filetype:pdf "center3" "MW" "data center"
filetype:pdf "Mobily" "data center" "annual report"
filetype:pdf "Al Moammar" "Sahayeb" "data center"
site:etimad.sa "مركز بيانات"
site:etimad.sa "data center"
site:etimad.sa "مراكز البيانات"
site:etimad.sa "مركز معلومات"
```

### 6.4 Legal-name pivots

Use English and Arabic brand variants:
```text
center3 OR "Digital Centers for Data and Telecommunications Company" OR "سنتر3"
stc OR "Saudi Telecom Company" OR "الاتصالات السعودية"
Mobily OR "Etihad Etisalat" OR "موبايلي" OR "اتحاد اتصالات"
Salam OR "Integrated Telecom Company" OR "سلام" OR "شركة الاتصالات المتكاملة"
Sahayeb OR "Sahayeb Data Park" OR "سحايب"
"Al Moammar Information Systems" OR MIS OR "المعمر لأنظمة المعلومات"
QST OR "Quantum Switch Tamasuk" OR "كوانتوم سويتش"
DataVolt OR "داتا فولت"
Khazna OR "خزنة"
CNTXT OR "كونتكست"
SCCC OR "Saudi Cloud Computing Company" OR "الشركة السعودية للحوسبة السحابية"
TONOMUS OR "NEOM Tech & Digital"
```

---

## 7. Evidence Pitfalls and Normalization

- **CST provider registration is not necessarily a full facility census.** It is high quality for commercial service providers; captive enterprise, government, university, refinery, and telecom network facilities may only appear in tenders, operator pages, or contractor references.
- **Cloud regions are not exact addresses.** AWS, Azure, Google, Oracle and Huawei region pages should seed metro/province searches only. Do not create multiple AZ facilities unless a primary record identifies them.
- **Capacity figures are often program totals.** Examples: national 1.5 GW strategy target, center3 300 MW / 1 GW roadmap, QST 300 MW program, Khazna 200 MW campus, DataVolt 1.5 GW OXAGON plan. Store the scope in notes and avoid assigning total program MW to one facility unless the source does.
- **Arabic/English transliteration causes duplicates.** Dammam / Ad Dammam, Jeddah / Jiddah, Khobar / Al Khubar, Madinah / Medina, Khurais / Khurays, Malga / Malqa / Melgha, Duba / Duba', NEOM / Oxagon / Port of NEOM, center3 / stc all need alias reconciliation.
- **Industrial and government data centers may not be colocation.** SEC, universities, Aramco / YASREF, ministries, SDAIA / NIC and airport/port systems may be valid datacenter records but should be marked captive/government when not commercial colo.
- **Saudi sources often announce investment at LEAP.** LEAP announcements are useful leads, but require at least one of CST registration, land, building permit, environmental permit, power connection, or operator facility page to count as construction/operational.

Suggested per-source grade summary:

| Source | Grade |
|---|---|
| CST data-center provider list / regulation / data-center registration | A |
| CST cloud provider list / cloud regulations / cloud registration class | A |
| Balady building permit or completion certificate | A |
| NCEC environmental permit / inspection / violation record | A |
| SEC / National Grid SA connection, substation, tender, or open-data record | A |
| MCIT / SPA / Vision 2030 / SDAIA / NEOM / MODON official announcement | A for announcement/land/program existence; B for unpermitted future capacity |
| Saudi Exchange filings / annual reports | A |
| Operator official facility page | A for existence/service city; B for design capacity unless phase-specific |
| Uptime Institute certificate lookup | A for certification status and facility name |
| DCD / Capacity / MEED / Arab News / Gulf Business / Telecom Review | B |
| DatacenterMap / Baxtel / Datacenters.com / OCOLO | B/C, depending corroboration |
| Market-report teasers and social posts | C |

---

## 8. Recommended Pipeline Order

1. **CST sweep first**: pull registered data-center providers and registered cloud providers; map each city/facility to a governorate.
2. **Official cloud sweep**: AWS Saudi Arabia Region, Azure Saudi Arabia East, Google Dammam, Oracle Jeddah/Riyadh/NEOM, Huawei Riyadh, Alibaba/SCCC. Keep these as region/city seeds until facility evidence appears.
3. **Operator official sweep**: center3/stc, Mobily, Salam, Sahayeb/MIS, QST, DataVolt, TONOMUS/Ezditek, Khazna, Equinix, Orixcom. Capture exact facility names and marketed cities.
4. **Permit joins**: Balady/MoMRAH, local Amanah, NCEC/eCompliance, MODON/NEOM/RCJY/MISA/ECZA, then SEC/National Grid / Etimad.
5. **Filing / certificate validation**: Saudi Exchange, annual reports, Uptime, ISO and contractor EPC references.
6. **Deduplicate by campus**: normalize by `(ultimate operator, campus/facility alias, city/governorate, phase)` and keep program-scale capacity separate from phase/facility capacity.

For production enumeration, the highest-yield first pass is: **CST provider list -> center3/Mobily/Salam/Sahayeb official pages -> cloud region pages -> Balady/NCEC/SEC joins for Riyadh, Dammam, Jeddah, NEOM/Duba, Khobar, Madinah, Yanbu, Unaizah**.
