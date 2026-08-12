# AE Explorer - Industry / Press / Vendor Discovery for UAE Datacenters

Date: 2026-08-12. Scope: how to enumerate United Arab Emirates (AE) datacenter projects through English and Arabic search, trade press, vendor/operator pages, official media offices, free-zone ecosystems, and emirate/division query patterns. Reliability grades: **A** = primary/official/operator/regulator/government media; **B** = established trade press, strong market intelligence, or contractor/customer case study; **C** = directories, social posts, old PR syndication, commercial listings, or local promotional coverage used mainly as leads.

---

## 0. UAE-specific frame

- The UAE does **not** expose a single national public datacenter registry. Enumeration works by triangulating: operator facility/press pages, cloud-region pages, government media offices, free-zone/industrial-zone authorities, building-permit service surfaces, power/water utility announcements, Uptime Institute certifications, carrier/cable landing materials, trade press, and directories.
- The main commercial clusters are **Dubai** and **Abu Dhabi**, with secondary/emerging activity in **Sharjah**, **Ajman**, **Fujairah**, and **Ras Al Khaimah**. **Umm Al Quwain** and smaller inland divisions usually need negative-search documentation rather than project enumeration.
- UAE geography is often published as an **emirate**, **free zone**, **industrial zone**, or named master development rather than a street address. Important location anchors: **Masdar City**, **Yas Island**, **KIZAD/KEZAD**, **ICAD/Mussafah**, **Dubai Silicon Oasis**, **Dubai Production City / IMPZ**, **Dubai Internet City**, **Dubai Design District**, **Dubai Marina**, **Jebel Ali / JAFZA**, **Warsan**, **Mohammed bin Rashid Al Maktoum Solar Park / Saih Al-Dahal**, **Fujairah cable landing / SmartHub**, **Kalba / COMTECH Freezone**, **Sharjah Research Technology and Innovation Park**, and **Innovation City / RAK Digital Assets Oasis**.
- English coverage is strongest for hyperscale, wholesale, cloud regions, free zones, and investment announcements. Arabic coverage is essential for official government-media reposts, local economic-zone announcements, MoUs, construction ceremonies, and emirate-specific authority material.
- Common failure mode: treating an MoU, "AI campus", cloud region, or free-zone initiative as an operational facility. Capture status verbs exactly: `announced`, `MoU`, `land lease`, `secured power`, `groundbreaking`, `under construction`, `launched`, `inaugurated`, `operational`, `campus build-out`.

Primary/source examples:

- Khazna official site says it has **30 live data centers**, **6 ongoing projects**, and **673 MW** across the portfolio: https://khaznadatacenters.com/ .
- G42 official Stargate UAE announcement describes a **1 GW** Stargate compute cluster inside a **5 GW UAE-U.S. AI Campus in Abu Dhabi**: https://www.g42.ai/resources/news/global-tech-alliance-launches-stargate-uae .
- Microsoft Learn lists **UAE North (Dubai)** and **UAE Central (Abu Dhabi)** Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list .
- AWS opened the **Middle East (UAE)** region with three Availability Zones: https://aws.amazon.com/blogs/aws/now-open-aws-region-in-the-united-arab-emirates-uae/ .
- Oracle docs list **UAE Central (Abu Dhabi), me-abudhabi-1** and **UAE East (Dubai), me-dubai-1**: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm .

---

## 1. High-signal trade press and market sources

Use these to discover project names, developer entities, MW claims, timelines, and free-zone locations; then verify with operator/government/permit evidence.

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | `https://www.datacenterdynamics.com/en/news/?tag=uae`, plus operator/emirate scoped queries | Best UAE datacenter construction and site-selection feed. Good for Khazna, Moro Hub, Gulf Data Hub, Pure DC, Equinix, Sharjah, Ajman, Ras Al Khaimah, Stargate UAE, and status changes. | B |
| W.Media | `https://w.media/`, query `site:w.media UAE "data center"` | APAC/GCC DC trade press. Good for Moro Hub, Khazna/BEEAH, conference ecosystem, and vendor partnership leads. | B |
| Data Centre Magazine / Data Center Knowledge | `site:datacentremagazine.com UAE "data centre"`, `site:datacenterknowledge.com UAE "data center"` | Market narratives and major AI/cloud summaries; useful to seed operators and recent geopolitical/outage context. Verify facility details. | B-/C+ |
| Construction Week Middle East | `site:constructionweekonline.com UAE "data centre"` | Strong for contractors, MEP, construction awards, and project-delivery leads; verify with operator/government pages. | B |
| MEED / Zawya / AGBI / Arabian Business / Gulf Business / Khaleej Times / The National | site-scoped searches | Good for investment, government partnerships, free-zone announcements, and Arabic/English syndicated official news. Often paywalled or broad; verify capacity/status. | B-/C+ |
| Fast Company Middle East / TahawulTech / ITP.net / Telecom Review Arabia | site-scoped searches | Useful for tech-policy and cloud-provider announcements; often repeats press releases. | B-/C+ |
| DC Byte / Structure Research / CBRE / JLL / Cushman / Arizton / ResearchAndMarkets | site-scoped or report pages | Market sizing, active-operator lists, pipeline context. Treat as aggregate context, not facility proof. | B/C |
| Data Center Map / Baxtel / Datacenters.com / PeeringDB / Cloudscene / Uptime Institute certificates | directory searches | Useful for legacy Etisalat/e&, Khazna aliases, PeeringDB facility IDs, network ecosystem, and addresses. Must be cross-checked. | C+, except Uptime certifications are A for certified facility name/status. |

DCD query patterns:

```text
site:datacenterdynamics.com/en/news/ "UAE" "data center" "{operator}"
site:datacenterdynamics.com/en/news/ "United Arab Emirates" "data center" "{emirate}"
site:datacenterdynamics.com/en/news/ "Khazna" "Ajman" "100MW"
site:datacenterdynamics.com/en/news/ "Moro Hub" "Warsan" OR "Solar Park"
site:datacenterdynamics.com/en/news/ "Gulf Data Hub" "KIZAD" OR "Dubai Silicon Oasis"
site:datacenterdynamics.com/en/news/ "Sharjah" "data center" "Kalba"
site:datacenterdynamics.com/en/news/ "Ras Al Khaimah" "data center" "Innovation City"
```

Regional press query patterns:

```text
site:w.media UAE "data center" Khazna
site:constructionweekonline.com UAE "data centre" "Khazna" OR "Moro Hub"
site:zawya.com UAE "data center" "{operator}"
site:arabianbusiness.com UAE "data centre" "{emirate}"
site:gulfbusiness.com UAE "data centre" Khazna BEEAH
site:thenationalnews.com UAE "data centre" "Abu Dhabi" OR "Dubai"
site:khaleejtimes.com UAE "data center" "Dubai Silicon Oasis"
```

---

## 2. Official media, free-zone, utility, and permit surfaces

These are not complete public registries, but they give A-grade leads for project existence, government support, land/power readiness, and construction milestones.

| Source | URL / search route | Use | Grade |
|---|---|---|---|
| WAM / Emirates News Agency | https://www.wam.ae/ | Federal and emirate-level official announcements. Search English and Arabic for `data centre`, `مركز بيانات`, operator names. | A |
| Dubai Media Office | https://mediaoffice.ae/ | Dubai government announcements, including DIEZ/VOLT and DEWA/Moro Hub items. | A |
| Abu Dhabi Media Office | https://www.mediaoffice.abudhabi/ | Abu Dhabi government announcements, DMT/ADIO/industrial strategy, major infrastructure and permit statistics. | A |
| Sharjah Government Media Bureau | https://sgmb.ae/ | Arabic/English Sharjah government releases; useful for SCTA, BEEAH, DataCanvas/AI Caravan, Kalba/COMTECH. | A |
| TAMM / Abu Dhabi DMT | https://www.tamm.abudhabi/ and DMT service pages | Building-permit and municipal-service surface for Abu Dhabi Municipality, Al Ain, and Al Dhafra. Usually not a searchable public planning register, but strong for knowing permitting authority. | A for authority route |
| Dubai Municipality / Build in Dubai | https://www.dm.gov.ae/ and https://buildindubai.gov.ae/ | Dubai building-permit service route. Use for authority identification, service names, and requirements; public application details may be limited. | A for authority route |
| Dubai Development Authority (DDA) | https://dda.gov.ae/ | Permits/NOCs for Dubai development/free-zone areas under DDA; official final building permit service confirms permit route. | A for authority route |
| Trakhees / PCFC | https://pcfc.ae/ | Building, EHS, green-building and NOC rules for JAFZA/Ports/Jebel Ali and other PCFC areas; important for Jebel Ali/JAFZA datacenters. | A for authority route |
| KEZAD / AD Ports Group | https://www.kezadgroup.com/ | Abu Dhabi industrial/free-zone land and lease ecosystem, especially KIZAD/KEZAD and Mussafah/ICAD. | A/B |
| Masdar City Free Zone | https://masdarcityfreezone.com/ | Masdar City free-zone context; useful for Khazna AUH6, Equinix AD1, and AI/data-center setup material. | A/B |
| Dubai Silicon Oasis / DIEZ | https://www.diez.ae/ and Dubai Media Office | Dubai Silicon Oasis project leads: Gulf Data Hub, VOLT/DIEZ AI-ready DC, startups/free-zone tenants. | A/B |
| Utilities: DEWA, Etihad Water and Electricity, TAQA/ADDC/AADC, SEWA, FEWA/EWE | authority sites + news pages | Look for substation, power-supply, solar/green DC, district cooling, and HT/MW connection evidence. | A when official |

Permit/official query patterns:

```text
site:wam.ae "data centre" "United Arab Emirates"
site:wam.ae "data center" Khazna OR "Moro Hub" OR "Gulf Data Hub"
site:wam.ae "مركز بيانات" "الإمارات"
site:mediaoffice.ae "data centre" "Dubai Silicon Oasis" OR "Moro Hub" OR "VOLT"
site:mediaoffice.abudhabi "data centre" "Khazna" OR "G42" OR "Masdar City"
site:sgmb.ae "مركز بيانات" "الشارقة"
site:sgmb.ae "data center" Sharjah SCTA
site:tamm.abudhabi "Permit to Build" "Industrial" "data"
site:dmt.gov.ae "building permits" "data center" "Abu Dhabi"
site:buildindubai.gov.ae "Permit for a New Building" "data center"
site:dm.gov.ae "data center" "building permit"
site:dda.gov.ae "Final Building Permit" "data center"
site:pcfc.ae Trakhees "Green Building" "data center"
site:dewa.gov.ae "data centre" "Moro Hub" "Warsan"
site:etihadwe.ae "Khazna" "Ajman" "data center"
```

---

## 3. Vendor/operator seed list

Operator pages are **A for claimed owned/marketed presence**, **B for capacity** unless facility specs or formal filings give exact load. Treat directories and old brand pages as leads.

| Operator / developer | Primary URLs | UAE location signals | Grade notes |
|---|---|---|---|
| Khazna Data Centers | https://khaznadatacenters.com/ ; news/press pages; G42 news | Largest UAE wholesale platform after G42/e& combination. Look for Abu Dhabi/Masdar, Dubai, Ajman QAJ1, Sharjah/Kalba, and Stargate UAE infrastructure. Site states 30 live DCs, 6 ongoing projects, 673 MW portfolio. | A for own claims; B for facility-level MW until page/press confirms. |
| G42 / Core42 / Injazat lineage | https://www.g42.ai/ ; https://core42.ai/ | Abu Dhabi AI/cloud/sovereign compute ecosystem; Stargate UAE and Microsoft/G42 expansion are major leads. | A for official partnership/project statements; C for exact facility address unless disclosed. |
| e& / Etisalat / SmartHub | https://www.eand.com/ | Legacy Etisalat DCs, SmartHub Fujairah/Kalba, telecom/coastal cable landing hubs, wholesale tenant relationship with Khazna. | A for official e& releases; B/C for old directory-only Etisalat sites. |
| Moro Hub / Digital DEWA | https://www.morohub.com/ ; DEWA news | Dubai Marina, MBR Solar Park, Warsan green datacenter, Dubai government cloud/smart-city workloads. | A for DEWA/Moro pages; B for W.Media/DCD. |
| Gulf Data Hub (GDH) | https://www.gulfdatahub.ae/ | Dubai Silicon Oasis campus; Abu Dhabi/KIZAD or ICAD project leads; Middle East locations graphic includes Dubai and Abu Dhabi. | A for own site presence; B/C for capacity from market intelligence. |
| Equinix | Dubai: https://www.equinix.com/data-centers/europe-colocation/united-arab-emirates-colocation/dubai-data-centers ; Abu Dhabi AD1 page | DX1/DX2/DX3 in Dubai; AD1 in Abu Dhabi/Masdar City. Dubai page lists three IBX campuses and UAE-IX. | A for facility pages/specs. |
| Pure Data Centres | https://pure-dc.com/locations/abu-dhabi/ | Abu Dhabi / Yas Island campus and later-phase filings reported by DCD. | A for location page; B for planning/capacity via trade press. |
| du / Emirates Integrated Telecommunications Company | https://www.du.ae/ | Telecom/operator DCs, cloud services, and possible Microsoft/AWS partner signals; often not facility-specific. | A for official services, B/C for facility evidence unless named. |
| Pacific Controls / Pacific Controls Cloud Services | official pages + directories | Dubai/Jebel Ali/TechnoPark legacy cloud/DC assets; verify current status carefully. | B/C |
| XDS Data Centres | official/social + DCD | Sharjah Research Technology and Innovation Park 1 MW immersion-cooled facility. | B until operator page gives durable facility specs. |
| BEEAH Digital / One Data Center SPV / Khazna Sharjah JV | https://www.beeahgroup.com/ and Khazna press | Sharjah/Kalba Tier 3 DC, SCTA collaboration, renewable/waste-to-energy angle. | A for JV/official press; B for construction status until later proof. |
| VOLT UAE / DIEZ | Dubai Media Office + DCD | AI-ready Dubai Silicon Oasis project announced with DIEZ and Schneider Electric support. | A for Dubai official announcement; B for MW from trade press. |
| Siada / Innovation City / IOPn | Innovation City/Siada official channels + DCD | Ras Al Khaimah sovereign AI/GPU data center. | B unless operator/free-zone primary details are found. |
| Quantum Switch Tamasuk / Edgnex / DAMAC / other Gulf entrants | official + trade press | Monitor for UAE project announcements and free-zone land; market reports list them as entrants but not always UAE facility evidence. | B/C |

Operator queries:

```text
site:{operator-domain} UAE "data center" "{emirate}"
site:{operator-domain} UAE "data centre" "{free zone}"
"{operator}" "{emirate}" ("MW" OR "MVA" OR "IT capacity" OR "data halls" OR "racks")
"{operator}" "{free zone}" ("groundbreaking" OR "breaks ground" OR "construction" OR "inaugurated" OR "launched")
"{operator}" ("DEWA" OR "Etihad Water and Electricity" OR "ADDC" OR "SEWA") "data center"
"{operator}" "Uptime Institute" "United Arab Emirates"
"{operator}" "LEED" "data center" "UAE"
```

---

## 4. Hyperscaler/cloud official pages

These are **A for cloud-region existence** and usually **C for physical-site inference**. Use them to seed a facility search, not to place a physical datacenter without corroborating operator/permit evidence.

| Provider | Official URL | UAE signal |
|---|---|---|
| AWS | https://aws.amazon.com/local/uae/ ; https://aws.amazon.com/blogs/aws/now-open-aws-region-in-the-united-arab-emirates-uae/ ; AWS regions docs | Middle East (UAE), `me-central-1`, three Availability Zones, opened 2022. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list ; https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | UAE North = Dubai (`uaenorth`), UAE Central = Abu Dhabi (`uaecentral`). |
| Oracle Cloud | https://www.oracle.com/cloud/public-cloud-regions/ ; https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm | UAE East (Dubai), `me-dubai-1`; UAE Central (Abu Dhabi), `me-abudhabi-1`. |
| Google Cloud | https://cloud.google.com/about/locations ; https://docs.cloud.google.com/compute/docs/regions-zones | No UAE Compute Engine region shown on official region/zone lists as of this research; do not infer a UAE physical Google region from partner/local office claims. |
| IBM / SAP / Salesforce / Alibaba / Huawei Cloud / Cloudflare / Akamai | official region/location pages + partner press | Often cloud PoPs, SaaS residency, or partner-hosted services. Verify whether it is physical DC, cloud region, edge PoP, or tenant deployment. |

Cloud-to-facility pivot queries:

```text
"AWS" "UAE" "Availability Zone" "data center" Dubai Abu Dhabi
"Microsoft" "UAE North" Dubai "data center" "Khazna" OR "e&" OR "G42"
"Microsoft" "UAE Central" Abu Dhabi "data center" "G42"
"Oracle" "me-dubai-1" "data center" Dubai
"Oracle" "me-abudhabi-1" "data center" Abu Dhabi
"Google Cloud" "UAE" "region" "data residency" -jobs
"cloud region" "UAE" "Khazna" OR "Equinix" OR "Gulf Data Hub"
```

---

## 5. English and Arabic search patterns

### 5.1 English terms

Use both US/British spellings and local infrastructure nouns:

```text
"United Arab Emirates" ("data center" OR "data centre" OR datacenter OR datacentre) "{emirate}"
"{emirate}" "{division}" ("data center" OR "data centre") ("MW" OR "MVA" OR "IT load" OR "racks" OR "data halls")
"{free zone}" ("data center" OR "data centre" OR "AI data center" OR "cloud region")
"{industrial zone}" ("hyperscale" OR "colocation" OR "wholesale data center")
"{emirate}" ("groundbreaking" OR "breaks ground" OR "foundation stone" OR "construction progress") "data center"
"{emirate}" ("inaugurated" OR "launched" OR "operational" OR "goes live") "data center"
"{operator}" "{emirate}" ("power capacity" OR "Etihad Water and Electricity" OR DEWA OR ADDC OR SEWA)
"{operator}" "{emirate}" ("LEED" OR "Uptime Tier III" OR "Estidama" OR "green building")
```

Named-place expansion:

```text
"Masdar City" "data center" Khazna OR Equinix
"Yas Island" "data center" "Pure DC"
"KIZAD" OR "KEZAD" "data center" "Gulf Data Hub"
"Dubai Silicon Oasis" "data center" "Gulf Data Hub" OR VOLT OR DIEZ
"Dubai Production City" OR "IMPZ" "Equinix" "DX3"
"Dubai Internet City" "Khazna" "DXB2" OR "DXB3"
"Jebel Ali" OR "JAFZA" "Khazna" "data center"
"Warsan" "Moro Hub" "data center"
"Saih Al-Dahal" OR "MBR Solar Park" "Moro Hub" "data centre"
"Fujairah" "SmartHub" "data center" e&
"Kalba" "data center" "Khazna" OR BEEAH OR SCTA
"Sharjah Research Technology and Innovation Park" "data center"
"Innovation City" "Ras Al Khaimah" "data center" Siada
```

### 5.2 Arabic terms

Arabic sources often use singular/plural and center/centre variants. Use Arabic for official releases and local government media; translate leads back into English/operator sources for final proof.

Core nouns:

- data center: `مركز بيانات`, `مركز البيانات`, `مراكز بيانات`, `مراكز البيانات`
- data centre project: `مشروع مركز بيانات`, `مشاريع مراكز البيانات`
- AI data center: `مركز بيانات للذكاء الاصطناعي`, `مراكز بيانات للذكاء الاصطناعي`, `بنية تحتية للذكاء الاصطناعي`
- cloud / sovereign cloud: `سحابة`, `حوسبة سحابية`, `سحابة سيادية`, `خدمات سحابية`
- digital infrastructure: `البنية التحتية الرقمية`, `البنية الرقمية`, `التحول الرقمي`
- launch/opening: `افتتاح`, `تدشين`, `إطلاق`, `دخل الخدمة`
- construction: `إنشاء`, `بناء`, `بدء الأعمال الإنشائية`, `وضع حجر الأساس`, `كسر الأرض`
- land/power: `تخصيص أرض`, `تأجير أرض`, `الطاقة الكهربائية`, `قدرة`, `ميغاواط`, `ميجاواط`
- green/sustainable: `مركز بيانات أخضر`, `مستدام`, `الطاقة الشمسية`, `إعادة تدوير المياه`

Arabic templates:

```text
"الإمارات" ("مركز بيانات" OR "مراكز بيانات") ("خزنة" OR "خزنا" OR Khazna)
"أبوظبي" "مركز بيانات" ("مصدر" OR "مدينة مصدر" OR "جزيرة ياس" OR "كيزاد" OR "مصفح")
"دبي" "مركز بيانات" ("واحة دبي للسيليكون" OR "جبل علي" OR "مرسى دبي" OR "ورسان")
"الشارقة" "مركز بيانات" ("كلباء" OR "بيئة" OR "هيئة الشارقة لتقنيات الاتصال")
"عجمان" "مركز بيانات" ("خزنة" OR "100 ميغاواط")
"الفجيرة" "مركز بيانات" ("سمارت هب" OR "اتصالات" OR "e&")
"رأس الخيمة" "مركز بيانات" ("مدينة الابتكار" OR "سحابة سيادية")
"أم القيوين" "مركز بيانات"
site:wam.ae "مركز بيانات" "الإمارات"
site:mediaoffice.ae "مركز بيانات" "دبي"
site:sgmb.ae "مركز بيانات" "الشارقة"
site:dewa.gov.ae "مركز بيانات" "مورو"
```

Arabic stage mapping:

- `مذكرة تفاهم` / `اتفاقية` / `شراكة` = intent or framework; **C/B** unless land, power, or construction is stated.
- `تخصيص أرض` / `تأمين الأراضي` / `تأجير الأرض` = land signal; **A/B** if official authority.
- `وضع حجر الأساس` / `بدء الأعمال الإنشائية` = construction-start signal; **B/A** depending on source.
- `افتتاح` / `تدشين` / `إطلاق` / `دخل الخدمة` = operational/opening signal; verify with operator page or certification.

---

## 6. Emirate and division enumeration method

The manifest uses municipality/city-area divisions. Enumerate by **emirate -> named free zone/industrial area -> operator/press sweep -> official-media/permit/utility cross-check -> division mapping**.

### 6.1 Abu Dhabi: Abu Dhabi Municipality, Al Ain Municipality, Al Dhafra

Primary targets: Abu Dhabi city, Masdar City, Yas Island, KIZAD/KEZAD, ICAD/Mussafah, Khalifa City, Al Ain, Al Dhafra/Hameem-area AI campus leads.

Key developers/sources:

- **Khazna**: AUH6 Masdar City, Abu Dhabi expansions, Stargate UAE infrastructure. Use Khazna/G42 pages first, then DCD and directories.
- **G42/Core42/Microsoft/Oracle/OpenAI/NVIDIA/Cisco/SoftBank**: Stargate UAE and UAE-U.S. AI Campus, likely Abu Dhabi/Al Dhafra area but exact municipal mapping may need land/road evidence.
- **Equinix AD1**: Masdar City / Abu Dhabi IBX official page.
- **Pure DC**: Abu Dhabi/Yas Island campus.
- **Gulf Data Hub**: KIZAD/ICAD project leads.
- **Etisalat/e&**: Al Ain and Abu Dhabi legacy facilities, SmartHub/telecom sites.
- Authorities: TAMM/DMT, Abu Dhabi Media Office, ADIO, KEZAD/AD Ports, Masdar City Free Zone, ADDC/AADC/TAQA.

Queries:

```text
"Abu Dhabi" "data center" "Masdar City" Khazna Equinix
"Abu Dhabi" "data centre" "Yas Island" "Pure DC"
"KIZAD" OR "KEZAD" "data center" "Gulf Data Hub"
"ICAD" OR "Mussafah" "data center" "Abu Dhabi"
"Al Ain" "data center" "Etisalat" OR Khazna
"Al Dhafra" "data center" "Stargate UAE" OR "AI Campus"
"Hameem Road" "data center" "Abu Dhabi"
site:mediaoffice.abudhabi "data centre" "G42" OR "Khazna"
site:tamm.abudhabi "Permit to Build a New Industrial Warehouse" "Department of Municipalities"
site:kezadgroup.com "data center" OR "digital infrastructure"
site:masdarcityfreezone.com "data center" OR "AI"
"Abu Dhabi" "مركز بيانات" "مدينة مصدر"
"الظفرة" "مركز بيانات" "ستارغيت الإمارات"
```

Division mapping notes:

- Map **Masdar City, Yas Island, Abu Dhabi city, Khalifa City, Mussafah/ICAD** to `Abu Dhabi - Abu Dhabi Municipality` unless a source places it in Al Ain/Al Dhafra.
- Map **Al Ain / Tawam / Al Foah / Al Hili** to `Abu Dhabi - Al Ain Municipality`.
- Map **Hameem Road, Liwa, Madinat Zayed, Al Dhafra desert/solar/energy corridor** to `Abu Dhabi - Al Dhafra` only when location evidence is explicit. If official source says only "Abu Dhabi", keep emirate-level uncertainty in notes.

### 6.2 Dubai: Sectors 1-9

Primary targets: Dubai Internet City, Dubai Design District, Dubai Marina, Dubai Production City/IMPZ, Dubai Silicon Oasis, Jebel Ali/JAFZA, Warsan, MBR Solar Park/Saih Al-Dahal, Dubai International Airport, Deira/Umm Hurair legacy telecom sites.

Key developers/sources:

- **Moro Hub / Digital DEWA**: Dubai Marina, Warsan, MBR Solar Park; DEWA pages are A-grade.
- **Khazna**: Dubai Internet City, Dubai Design District, Ibn Battuta/Jebel Ali, DXB9/Jebel Ali/Etisalat Earth Station.
- **Gulf Data Hub**: Dubai Silicon Oasis campus.
- **Equinix**: DX1/DX2/DX3; official page lists three Dubai IBX campuses and UAE-IX.
- **VOLT UAE / DIEZ**: Dubai Silicon Oasis AI-ready DC; use Dubai Media Office and DCD.
- **AWS / Microsoft / Oracle**: cloud regions in Dubai; do not map to a physical sector without corroboration.
- Authorities: Dubai Media Office, Dubai Municipality / Build in Dubai, Dubai Development Authority, DIEZ/DSO, Trakhees/PCFC/JAFZA, DEWA.

Queries:

```text
"Dubai" "data center" "Dubai Silicon Oasis" "Gulf Data Hub"
"Dubai Silicon Oasis" "data center" VOLT DIEZ Schneider
"Dubai Internet City" "Khazna" "data centre"
"Dubai Design District" "Khazna" "DXB2"
"Ibn Battuta" "Khazna" "DXB3"
"Jebel Ali" "Khazna" "DXB8" OR "DXB9" OR "Etisalat Earth Station"
"Dubai Production City" OR "IMPZ" "Equinix" "DX3"
"Dubai Marina" "Moro Hub" "data center"
"Warsan" "Moro Hub" "Green Data Centre"
"Mohammed bin Rashid Al Maktoum Solar Park" "data center" "Moro Hub"
"Saih Al-Dahal" "data centre" "Moro Hub"
"Dubai International Airport" "modular data center" Huawei
site:mediaoffice.ae "data centre" "Dubai Silicon Oasis" OR "Moro Hub"
site:dewa.gov.ae "data centre" "Moro Hub"
site:buildindubai.gov.ae "Permit for a New Building" "data center"
site:dda.gov.ae "data center" "building permit"
site:pcfc.ae Trakhees "data center" "Jebel Ali"
"دبي" "مركز بيانات" "واحة دبي للسيليكون"
"دبي" "مركز بيانات" "جبل علي"
"ديوا" "مركز بيانات" "مورو"
```

Sector mapping notes:

- `Sector 1`: Deira/old Dubai and port/creek-side legacy telecom. Expect few public wholesale leads; search Etisalat, du, airport/port networks.
- `Sector 2`: DXB airport/Al Garhoud/airport-side infrastructure. Search Dubai Airports + Huawei modular DC and telecom facilities.
- `Sector 3`: central/coastal business districts including Dubai Design District, Dubai Marina, Umm Hurair-type legacy listings. Good for Khazna DXB2, Moro Hub Dubai Marina, Etisalat directories.
- `Sector 4`: Ras Al Khor/Nad Al Hammar/Creek/Warqaa style districts. Mostly negative unless new industrial/utility projects appear.
- `Sector 5`: Jebel Ali/JAFZA/Ibn Battuta/Etisalat Earth Station. Strong Khazna/JAFZA/Trakhees route.
- `Sector 6`: Dubai Silicon Oasis, Dubai Production City/IMPZ, DSO/DIEZ technology clusters. Strong GDH, Equinix DX3, VOLT/DIEZ route.
- `Sector 7`: inland/residential or lower-signal sector in previous sweeps. Use negative documentation plus generic Dubai/DEWA searches.
- `Sector 8`: Warsan/eastern utility area. Strong Moro Hub Warsan route.
- `Sector 9`: southern desert/Al Marmoom/Saih Al-Dahal/MBR Solar Park. Strong Moro Hub solar-powered DC route.

### 6.3 Sharjah: Sharjah, Kalba, Hamriyah, Dhaid, Khor Fakkan, Dibba Al Hesn, Al Madam, Al Batayih, Milehah

Primary targets: Sharjah city/SRTI Park, Kalba/COMTECH Freezone, Hamriyah Free Zone, Al Dhaid/Tawi Al Saman, Khor Fakkan/Dibba coastal telecom/cable facilities.

Key developers/sources:

- **Khazna/BEEAH/SCTA**: Sharjah Tier 3 network and Kalba first/largest facility.
- **XDS Data Centres**: SRTI Park immersion-cooled facility.
- **Etisalat/e&**: Al Dhaid IPTV modular DC, Kalba/SmartHub, coastal/telecom infrastructure.
- **DataCanvas / AI Caravan / SCTA**: Sharjah data-center/AI-infrastructure MoU; treat as planned unless site/capacity follows.
- Authorities: Sharjah Government Media Bureau, SCTA, BEEAH, Hamriyah Free Zone, Sharjah Municipality, SEWA.

Queries:

```text
"Sharjah" "data center" "SCTA" OR "BEEAH" OR "Khazna"
"Kalba" "data center" "COMTECH Freezone" OR "BEEAH"
"Sharjah Research Technology and Innovation Park" "data center" XDS
"Al Dhaid" "Etisalat" "Modular Data Center" "Tawi Al Saman"
"Hamriyah Free Zone" "data center" Huawei OR "FusionModule"
"Khor Fakkan" OR "Dibba Al Hesn" "data center" "Etisalat" OR "submarine cable"
site:sgmb.ae "مركز بيانات" "الشارقة"
site:khaznadatacenters.com "Sharjah" "Tier 3 data center"
site:beeahgroup.com "data centre" "Sharjah"
site:sewa.gov.ae "data center" OR "مركز بيانات"
"الشارقة" "مركز بيانات" "كلباء"
"هيئة الشارقة لتقنيات الاتصال" "مركز بيانات"
"الذيد" "مركز بيانات" "اتصالات"
```

Division mapping notes:

- Map **SRTI Park / University City / Sharjah city** to `Sharjah - Sharjah`.
- Map **Kalba / COMTECH Freezone** to `Sharjah - Kalba`.
- Map **Hamriyah Free Zone** to `Sharjah - Al Hamriyah`.
- Map **Al Dhaid / Tawi Al Saman** to `Sharjah - Dhaid`.
- For **Khor Fakkan / Dibba Al Hesn** coastal telecom leads, require operator/cable landing proof before counting a DC.
- **Al Madam, Al Batayih, Milehah** are likely negative unless industrial/utility or government DC leads emerge.

### 6.4 Ajman: Ajman, Manama, Masfut

Primary targets: Ajman city and industrial/free-zone areas. Manama and Masfut are low-probability and need explicit negative searches.

Key developers/sources:

- **Khazna QAJ1**: 100 MW AI-optimized Ajman datacenter. DCD says it receives electricity from Etihad Water and Electricity; use Khazna/DCD/EWE searches.
- Authorities: Digital Ajman, Ajman Municipality and Planning Department, Ajman Free Zone, Etihad Water and Electricity.

Queries:

```text
"Ajman" "data center" Khazna QAJ1 "100MW"
"Ajman" "data centre" "Etihad Water and Electricity"
"Ajman Free Zone" "data center"
"Ajman Municipality" "data center" "building permit"
"Manama" "Ajman" "data center" OR "data centre"
"Masfut" "data center" OR "data centre"
site:ajman.ae "data center" OR "مركز بيانات"
site:etihadwe.ae "Ajman" "data center" OR "Khazna"
"عجمان" "مركز بيانات" "خزنة"
"مصـفوت" OR "مصفوت" "مركز بيانات"
"المنامة" "عجمان" "مركز بيانات"
```

Division mapping notes:

- Map city/industrial-area projects to `Ajman - Ajman` unless source explicitly places the site in Manama or Masfut.
- For `Ajman - Manama` and `Ajman - Masfut`, document searched terms and mark no public project if only Ajman-city Khazna results appear.

### 6.5 Fujairah: Al Fujairah Municipality, Dibba Al Fujairah Municipality

Primary targets: Fujairah city/cable landing area, e& SmartHub/telecom campus, port/free-zone facilities. Dibba is lower signal.

Key developers/sources:

- **e& / Etisalat SmartHub Fujairah**: cable landing and Tier III facility expansion.
- Authorities: Fujairah Municipality, Fujairah Free Zone, Fujairah Port, Etihad Water and Electricity.

Queries:

```text
"Fujairah" "SmartHub" "data center" e&
"Fujairah" "data centre" "cable landing" OR "submarine cable"
"Etisalat" "Fujairah" "Tier III" "data center"
"Fujairah Free Zone" "data center"
"Dibba Al Fujairah" "data center" OR "data centre"
site:eand.com "Fujairah" "SmartHub Data Centre"
site:fujmun.gov.ae "data center" OR "مركز بيانات"
"الفجيرة" "مركز بيانات" "سمارت هب"
"دبا الفجيرة" "مركز بيانات"
```

Division mapping notes:

- Map Fujairah city/port/cable landing facilities to `Fujairah - Al Fujairah Municipality`.
- Map Dibba-specific sources only to `Fujairah - Dibba Al Fujairah Municipality`; otherwise do not infer from generic Fujairah.

### 6.6 Ras Al Khaimah

Primary targets: RAK city, Innovation City / RAK Digital Assets Oasis, RAK Economic Zone (RAKEZ), Al Hamra industrial/logistics areas.

Key developers/sources:

- **Siada / Innovation City / IOPn**: sovereign AI/GPU datacenter in Innovation City.
- Authorities: RAK Government portal, RAKEZ, Innovation City / RAK DAO, Etihad Water and Electricity.

Queries:

```text
"Ras Al Khaimah" "data center" "Innovation City"
"RAK Digital Assets Oasis" "data center" OR "sovereign cloud"
"RAKEZ" "data center" OR "AI infrastructure"
"Siada" "Ras Al Khaimah" "data center"
site:rak.ae "data center" OR "مركز بيانات"
"رأس الخيمة" "مركز بيانات" "مدينة الابتكار"
"رأس الخيمة" "سحابة سيادية" "مركز بيانات"
```

Division mapping notes:

- The manifest has one division, `Ras Al Khaimah - Ras Al Khaimah`; map all verified RAK emirate projects here unless a later manifest is more granular.

### 6.7 Umm Al Quwain

Primary targets: UAQ Free Trade Zone, industrial area, port/logistics, Etihad Water and Electricity. Expect negative results unless a new free-zone/edge site emerges.

Queries:

```text
"Umm Al Quwain" "data center" OR "data centre" OR datacenter
"UAQ Free Trade Zone" "data center"
"Umm Al Quwain" "cloud" "data center"
site:uaq.ae "data center" OR "مركز بيانات"
site:etihadwe.ae "Umm Al Quwain" "data center"
"أم القيوين" "مركز بيانات"
"المنطقة الحرة أم القيوين" "مركز بيانات"
```

Division mapping notes:

- The manifest has one division, `Umm Al Quwain - Umm AL Quwain`. Record negative searches with both English spelling variants: `Umm Al Quwain`, `Umm al-Qaiwain`, `UAQ`, `أم القيوين`.

---

## 7. Validation and evidence grading

Minimum evidence for a positive facility/project:

1. **Operational facility**: operator page, government/utility announcement, Uptime certification, PeeringDB/IX listing plus operator confirmation, or multiple strong trade sources.
2. **Construction**: official groundbreaking/construction-progress release, contractor case study, permit/NOC reference, utility power-connection evidence, or DCD/Construction Week with named site and MW.
3. **Planned**: MoU or official partnership only if a developer, emirate/free zone, intended facility type, and at least one concrete location/capacity/land/power statement are present.
4. **Cloud region**: record as cloud-region evidence only. Do not create a physical facility record unless a physical site/operator/city-area source exists.

Source-grade rules:

- **A**: operator facility/press page; WAM or emirate media office; DMT/TAMM/Dubai Municipality/DDA/Trakhees/KEZAD/free-zone authority; DEWA/EWE/SEWA/ADDC/AADC; Uptime Institute certification; official cloud-region docs.
- **B**: DCD, W.Media, Construction Week Middle East, The National, Gulf Business, Zawya, MEED, Fast Company Middle East, DC Byte, vendor case studies from Schneider/Huawei/Vertiv/Turner & Townsend/contractors.
- **C**: Data Center Map, Baxtel, Datacenters.com, Cloudscene, LinkedIn/X/Instagram posts, market-report PR summaries, Wikipedia, old reseller/integrator listings.

Capacity handling:

- Prefer **IT load MW** over utility feed or gross power. If a source says "capacity" without IT/electrical distinction, store the value but note ambiguity.
- Separate **current operational phase** from **full campus build-out**. Stargate UAE, Khazna 1GW, and Dubai/Sharjah AI MoUs are especially prone to future-buildout inflation.
- For free-zone or utility-led announcements, confirm whether the asset is a commercial colocation/wholesale facility, sovereign/government cloud, internal enterprise data center, telecom exchange, cable landing station, or modular server room.

---

## 8. Quick source checklist for future AE runs

Run this sequence for each division:

1. Search operator + division/free-zone: Khazna, G42/Core42, e&/Etisalat/SmartHub, Moro Hub, GDH, Equinix, Pure DC, du, XDS, BEEAH, VOLT, Siada.
2. Search official media: WAM, Dubai Media Office, Abu Dhabi Media Office, Sharjah Government Media Bureau, DEWA, EWE, DMT/TAMM, DDA/Build in Dubai/Trakhees, KEZAD, DSO/DIEZ, RAKEZ.
3. Search trade press: DCD first, then W.Media, Construction Week, Zawya/MEED/Arabian Business/Gulf Business/The National/Khaleej Times/Fast Company ME.
4. Search certifications/directories: Uptime Institute, PeeringDB, Data Center Map, Baxtel, Datacenters.com, Cloudscene.
5. Search Arabic local names and variant spellings; record negative searches for Manama, Masfut, Dibba, Al Madam, Al Batayih, Milehah, Umm Al Quwain.
6. Only map to a manifest division when a named district/free-zone/landmark supports it; otherwise keep the note at emirate level and mark mapping confidence.
