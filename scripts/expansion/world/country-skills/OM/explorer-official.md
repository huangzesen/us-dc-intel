# OM Explorer Official - Oman Datacenter Enumeration

Date: 2026-08-12. Scope: Sultanate of Oman (OM). Repo divisions: South Batina; North Batina; Buraymi; Interior; Muscat; Musandam; Southeastern; Northeastern; Central; Dhahira; Dhofar. Official Oman aliases: Al Batinah South, Al Batinah North, Al Buraimi, Ad Dakhiliyah, Muscat, Musandam, Ash Sharqiyah South, Ash Sharqiyah North, Al Wusta, Ad Dhahirah, Dhofar. Use the repo division name in records, but preserve official alias, wilayat, and zone.

Reliability grades: **A** = official government/regulator/municipality/free-zone/utility/cloud/operator source; **B** = established trade press, contractor/customer case study, or authoritative directory that names a facility; **C** = market report, aggregator, social post, sales listing, or crypto/promotional coverage used only as a lead. Be strict: a government policy target, MoU, cable landing, or cloud edge node is not a datacenter unless a facility is separately evidenced.

## 0. Oman-Specific Ground Rules

- There is no public national datacenter registry and no unified public planning-application search. Enumeration must triangulate official sources: `gov.om`, Muscat Municipality, governorate portals, OPAZ/SEZ/free-zone one-stop shops, Madayn, MTCIT, TRA, APSR/Nama/OETC/NPWP, operator pages, cloud-region pages, and official media.
- Oman has 11 governorates. The repo uses shortened English division names; always map them to the official English/Arabic names when searching. Division coverage is complete only when all 11 governorates have a documented positive or negative sweep.
- Municipality/zone permitting is fragmented. Muscat Municipality is the useful permit surface for Muscat. OPAZ and zone one-stop-shop services are the primary route inside Duqm, Sohar Free Zone, Salalah Free Zone, Al Mazunah and Khazaen-related economic zones. Madayn is primary for industrial cities and Knowledge Oasis Muscat.
- Power and connectivity are the best official corroborators. Large datacenter claims should be checked against APSR/Nama/OETC/NPWP and the relevant distribution/zone utility for MW, substation, MVA, self-generation, and solar claims.
- Cloud evidence must be classified precisely. AWS Muscat is an available Local Zone, not a full AWS Region. Oracle/Otech/ITHCA operate OCI Dedicated Region infrastructure in Oman, including Muscat primary and Ibri secondary evidence, but this is dedicated/sovereign cloud infrastructure rather than a generic public OCI commercial region. Azure and Google Cloud official region lists do not show an Oman public region.
- Cable landings are leads, not facilities. Barka and Salalah are high-priority because of 2Africa and related systems; Qalhat/Sur is high-priority for legacy subsea landings. A cable landing station can co-exist with a datacenter, but must be sourced as such.

Arabic terms to use with English queries: `مركز بيانات`, `مراكز البيانات`, `مراكز المعطيات`, `الحوسبة السحابية`, `الخدمات السحابية`, `السحابة الحكومية`, `تصريح بناء`, `ترخيص بناء`, `رخصة بناء`, `تخصيص أرض`, `محطة تحويل`, `ميغاواط`, `الكابلات البحرية`, `محطة إنزال الكابلات`, `تقييم الأثر البيئي`, `تعدين العملات الرقمية`, `الذكاء الاصطناعي`.

## 1. Verified Grade A Official Source Ledger

| Source | URL | Use | Grade notes |
|---|---|---|---|
| Unified Government Services Portal | https://gov.om/ and building permit service https://gov.om/w/get-building-permit | Service routing, building-permit requirements, entity pages, government news. | A for process/entity facts; not a public permit register. |
| Muscat Municipality | https://www.mm.gov.om/ and e-services https://www.mm.gov.om/EServices.aspx?ESID=2 | Building permits and municipal services for Muscat Governorate. | A for permit route; C for facility inference unless a named permit appears. |
| MTCIT | https://mtcit.gov.om/ | Digital economy, PDPL, accreditation, government cloud and hosting. | A. Key pages include cloud-hosting/data-center service and accreditation register. |
| MTCIT Cloud Hosting and Data Center Services | https://mtcit.gov.om/services-5/services-13/services-92/cloud-hosting-and-data-center-services-405 | Approval route for providers serving government. | A for accreditation criteria and service scope. |
| MTCIT approved provider register | https://mtcit.gov.om/register-of-approved-hosting-service-providers-and-data-centers | Lists approved hosting service providers/data centers; shows Oman Data Park/Otech contact and KOM4 address. | A for accredited provider evidence; still find physical sites separately. |
| TRA | https://tra.gov.om/ and projects page https://tra.gov.om/projects | Telecom/ICT licensing and projects, including data center/cloud service framework work. | A for regulator context; not a facility list. |
| Madayn / KOM | https://madayn.om/ and https://madayn.om/kom/ | Industrial cities and Knowledge Oasis Muscat, where Otech/Oman Data Park has KOM facilities. | A for zone/land/tenant context. |
| OPAZ | https://opaz.gov.om/ | Public Authority for Special Economic Zones and Free Zones. | A for zones, one-stop-shop, licensing route. |
| OPAZ Sohar Free Zone | https://opaz.gov.om/en/zones/sohar-free-zone | Official Sohar Free Zone page. | A for zone geography/licensing. |
| Zone services one-stop shop | https://zoneservices.gov.om/ | Investor applications for special economic zones and free zones. | A for permit/licensing route; site may be hard to crawl. |
| Sohar Port and Freezone | https://soharportandfreezone.om/ | Sohar land, utilities, investor announcements. | A for Sohar Freezone surface. |
| SEZAD / Duqm | https://duqm.gov.om/en | Duqm land/investment licensing and SEZ announcements. | A for Duqm route. |
| APSR | https://apsr.om/ | Electricity, water, wastewater regulation, licences, tariffs. | A for utility/regulatory corroboration. |
| Nama Power & Water Procurement | https://omanpwp.om/ | Power procurement and capacity planning. | A for supply context. |
| Ministry of Energy and Minerals | https://mem.gov.om/ | Energy, renewables, hydrogen and minerals policy; useful for green/hyperscale power claims. | A for policy/source context; not a facility register. |
| Environment Authority | https://www.ea.gov.om/en and permits center https://www.ea.gov.om/en/the-authority/authority-mandates/environmental-assessment-and-permits-center/ | Environmental permits and EIA route for large facilities, generators, fuel and water impacts. | A for EIA/permitting route. |
| Otech | https://otech.om/ | Operator evidence for Otech/Oman Data Park sites, cloud, AI, Oracle partnerships. | A for own claimed portfolio/status; cross-check certifications. |
| Otech Otech launch | https://otech.om/media-room/news-room/ktwzz82xf9w6b5mhseqfhl0v | Omantel launch of Otech; integration of Oman Data Park; Farq/Firq data center claim. | A for corporate/operator claim. |
| Otech OCI Ibri launch | https://otech.om/media-room/news-room/aks3z17sny1js3nrqaojp113 | OCI Secondary Dedicated Region in Ibri with ITHCA and Oracle. | A for operator claim; classify as OCI Dedicated Region, not ordinary public region. |
| Ooredoo Oman | https://www.ooredoo.om/ | Official Ooredoo Oman data-center announcements. | A for operator claims. |
| Ooredoo 2022 data-center groundbreaking | https://www.ooredoo.om/en/press-release/ooredoo-breaks-ground-on-three-new-data-centres/ | Barka, Salalah, Sohar construction; Muscat/Bawshar 2.5 MW facility; 2Africa landing role. | A for announced build and specs. |
| Ooredoo Sohar launch | https://www.ooredoo.om/en/press-release/ooredoos-new-data-centre-in-sohar-upgrades-omans-tech-game/ | Sohar 1,200 racks and up to 10 MW; Level 3+ standard. | A for operator status/specs; do not call Uptime certified without Uptime evidence. |
| Equinix Oman | https://www.equinix.com/data-centers/europe-colocation/oman-colocation/muscat-data-centers and https://www.equinix.com/data-centers/europe-colocation/oman-colocation/salalah-data-centers | MC1 and SN1 official market pages. | A even if curl returns 403; browser/search confirms pages. |
| Equinix MC1 press release | https://investor.equinix.com/news-events/press-releases/detail/210/equinix-and-omantel-enter-agreement-to-build-new-equinix | MC1/Omantel JV, phase/cabinet plan. | A. Physical Barka mapping also appears in trade press. |
| Equinix MC1 opening | https://investor.equinix.com/news-events/press-releases/detail/89/equinix-and-omantel-open-new-muscat-data-center | MC1 opened; 725 cabinets and expansion potential. | A. |
| Equinix SN1 opening | https://newsroom.equinix.com/2024-11-7-Equinix-and-Omantel-Officially-Open-Salalah-SN1%2C-the-Second-Carrier-Neutral-Data-Center-in-Oman | Salalah SN1 opened with Omantel. | A. |
| Datamount | https://www.datamount.om/ and https://www.datamount.om/about-us | Datamount facilities in Muscat and Al Dakhiliyah, Al Bandar expansion, Jabal Al Akhdar. | A for operator claim; B/C for third-party capacity. |
| AWS Local Zones | https://docs.aws.amazon.com/local-zones/latest/ug/available-local-zones.html and https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ | Oman (Muscat) Local Zone `me-south-1-mct-1a`. | A for Local Zone existence; not a full region. |
| Azure regions | https://learn.microsoft.com/en-us/azure/reliability/regions-list | Official public Azure region list. | A; no Oman public region found. |
| Google Cloud locations | https://cloud.google.com/about/locations | Official Google Cloud region/zone list. | A; no Oman cloud region found. |
| Oracle Dedicated Region | https://www.oracle.com/cloud/cloud-at-customer/dedicated-region/ | Explains OCI Dedicated Region model. | A for product type; use Otech/ITHCA/Oracle announcements for Oman sites. |
| Oman News Agency | https://omannews.gov.om/ | Official launch/news surface for Arabic and English government announcements. | A. |
| Oman Broadband | https://omanbroadband.om/ | National broadband infrastructure context and fiber routes. | A for fiber context; not datacenter evidence by itself. |
| Zain Omantel International | https://zainomantel.com/ | Wholesale telecom and subsea-cable partnership context. | A for ZOI role; facility evidence still needs site/operator corroboration. |

## 2. Official Search Templates

National and regulator:

```text
site:gov.om ("data center" OR "data centre" OR "مركز بيانات" OR "مراكز البيانات")
site:gov.om ("building permit" OR "تصريح بناء" OR "ترخيص بناء") ("Muscat" OR "Salalah" OR "Sohar" OR "Duqm" OR "Barka")
site:mtcit.gov.om ("Cloud Hosting and Data Center Services" OR "approved hosting" OR "data center" OR "مراكز البيانات")
site:mtcit.gov.om ("Oman Data Park" OR "Otech" OR "Oracle" OR "Ibri" OR "Muscat")
site:tra.gov.om ("data center" OR "data centre" OR "cloud computing" OR "مراكز البيانات" OR "الحوسبة السحابية")
site:omannews.gov.om ("data centre" OR "data center" OR "مركز بيانات" OR "مراكز البيانات")
```

Permits, zones, land:

```text
site:mm.gov.om ("data center" OR "مركز بيانات" OR "building permit" OR "تصريح بناء")
site:madayn.om ("data center" OR "data centre" OR "KOM" OR "Knowledge Oasis" OR "واحة المعرفة")
site:opaz.gov.om ("data center" OR "data centre" OR "cloud" OR "Sohar" OR "Salalah" OR "Khazaen")
site:zoneservices.gov.om ("data" OR "cloud" OR "permit" OR "building")
site:duqm.gov.om ("data center" OR "AI" OR "cloud" OR "مركز بيانات" OR "الذكاء الاصطناعي")
site:soharportandfreezone.om ("data center" OR "cloud data" OR "AI" OR "big data")
"تخصيص أرض" "مركز بيانات" عمان
```

Power and environment:

```text
site:apsr.om ("data center" OR "data centre" OR "self generation" OR "licence" OR "tariff")
site:omanpwp.om ("data center" OR "AI" OR "MW" OR "ميغاواط")
site:mem.gov.om ("data center" OR "AI" OR "green hydrogen" OR "renewable" OR "الذكاء الاصطناعي")
site:ea.gov.om ("data center" OR "environmental permit" OR "EIA" OR "تقييم الأثر البيئي")
"OETC" OR "الشركة العمانية لنقل الكهرباء" ("data center" OR "substation" OR "MVA" OR "محطة تحويل")
"Nama" "data center" Oman OR "مركز بيانات"
"Environment Authority" Oman ("data center" OR "تقييم الأثر البيئي")
"{operator}" "{wilayat}" ("MW" OR "MVA" OR "ميغاواط" OR "substation")
```

Cloud and operator official:

```text
site:docs.aws.amazon.com/local-zones "Oman (Muscat)" OR "me-south-1-mct-1a"
site:aws.amazon.com/localzones Oman OR Muscat
site:learn.microsoft.com/en-us/azure/reliability/regions-list Oman
site:cloud.google.com/about/locations Oman
site:oracle.com "Dedicated Region" Oman OR Ibri OR Muscat
site:otech.om ("data center" OR "Farq" OR "Firq" OR "Nizwa" OR "Ibri" OR "OCI" OR "Oracle")
site:ooredoo.om ("data centre" OR "data center" OR "Barka" OR "Salalah" OR "Sohar" OR "Bawshar")
site:equinix.com Oman ("MC1" OR "SN1" OR "Muscat" OR "Salalah")
site:datamount.om ("Al Bandar" OR "Jabal" OR "Dakhiliyah" OR "Tier III")
```

## 3. Facility Evidence Classification

Use these record-level statuses:

- `operational`: opened/launched by operator or government; backed by official/operator page where possible.
- `under_construction`: construction, groundbreaking, or active build from official/operator source.
- `land_or_permit`: lease, land allocation, building permit, one-stop-shop approval, or zone agreement without launch.
- `planned_or_mou`: MoU/JDA/cooperation agreement; do not count as active supply.
- `cloud_edge_or_dedicated_region`: cloud node/Local Zone/Dedicated Region. Record as digital infrastructure and search for host facility; do not merge with colocation capacity unless source ties them.
- `connectivity_only`: cable landing station, PoP, fiber route, IX, or telecom exchange with no DC evidence.
- `negative_sweep`: no facility found after official/operator/press searches; retain query log.

Capacity fields must stay separate: `it_mw`, `facility_power_mw`, `grid_connection_mva`, `solar_mwp`, `racks`, `white_space_sqm`, `land_area_sqm`, `mining_machines`, `announced_campus_mw`. Never combine crypto-mining power, hyperscale MoU MW, and colocation IT load.

## 4. Known Official/Primary Seeds

| Seed | Repo division | Official location mapping | Source grade | Handling |
|---|---|---|---|---|
| Ooredoo Muscat/Bawshar data center | Muscat | Bawshar, Muscat Governorate | A from Ooredoo 2022 page | Operational; 2.5 MW and 99.982%+ claimed by Ooredoo. Treat as Tier 3/Level 3+ claim unless Uptime certificate found. |
| Ooredoo Barka data center / 2Africa landing | South Batina | Barka, Al Batinah South | A from Ooredoo 2022 page for construction/landing role; seek launch source | Positive lead; verify operational status and exact site. |
| Ooredoo Sohar data center | North Batina | Sohar, Al Batinah North | A from Ooredoo 2024 page | Operational; 1,200 racks, up to 10 MW, Level 3+ standard claimed. |
| Ooredoo Salalah data center + CLS | Dhofar | Salalah, Dhofar | A/B: official Ooredoo/Gulf press and DCD; seek Ooredoo page if available | Operational/inaugurated; 125 racks growing to 500; combine only if source says DC+CLS. |
| Equinix MC1 | South Batina for physical Barka; often marketed as Muscat metro | Barka, Al Batinah South | A Equinix; B for Barka physical geography from trade press | Operational; keep alias `Muscat MC1`. |
| Equinix SN1 | Dhofar | Salalah | A Equinix newsroom and Equinix Oman page | Operational, carrier-neutral IBX with Omantel. |
| Otech/Oman Data Park KOM4 | Muscat | Knowledge Oasis Muscat/Rusayl | A MTCIT register + Otech; A/B solar claims | Operational; MTCIT register gives KOM4 address. |
| Otech/Farq or Firq data center | Interior | Firq/Nizwa, Ad Dakhiliyah | A Otech | Treat as launched/official operator claim; verify exact spelling Farq/Firq and operational readiness before capacity count. |
| Otech/OCI secondary dedicated region | Dhahira | Ibri, Ad Dhahirah | A Otech; Oracle product page A for Dedicated Region model | Cloud dedicated-region evidence; record separately from public cloud region. |
| Datamount Al Bandar | Muscat | Al Bandar/Seeb, Muscat Governorate | A Datamount; B Times of Oman for capacity | Operational/operator-claimed; capacity needs cross-check. |
| Datamount Jabal Al Akhdar | Interior | Al Jabal Al Akhdar, Ad Dakhiliyah | A Datamount | Operational/operator-claimed; verify exact address/certification. |
| Exahertz/Afaaq Salalah Free Zone | Dhofar | Salalah Free Zone | A/B if ONA/MTCIT/Observer; C crypto-only | Digital hosting/crypto mining; record separately from colo. |
| AWS Local Zone Muscat | Muscat | Muscat Local Zone, undisclosed host | A AWS docs | Available Local Zone; not a full region/facility count. |
| OCI Dedicated Regions with Otech/ITHCA/Oracle | Muscat and Dhahira | Muscat primary, Ibri secondary | A Otech/Oracle/ITHCA | Dedicated/sovereign cloud infrastructure; identify host facility if possible. |

## 5. Per-Division Official Strategy

### 5.1 South Batina (Al Batinah South)

Wilayats: Barka, Rustaq, Al Awabi, Nakhal, Wadi Al Maawil, Al Musannah. Priority: Barka.

Known positive leads: Equinix MC1 physically in Barka though branded Muscat; Ooredoo Barka data center and 2Africa landing; Khazaen Economic City/OPAZ leads.

```text
"Barka" "Equinix" "MC1"
"Barka" "Ooredoo" "data centre" OR "2Africa"
"بركاء" "مركز بيانات" OR "محطة إنزال الكابلات"
site:opaz.gov.om "Barka" OR "Khazaen" "data center"
"South Batinah" OR "Al Batinah South" "data center"
```

### 5.2 North Batina (Al Batinah North)

Wilayats: Sohar, Shinas, Liwa, Saham, Al Khaburah, Suwayq. Priority: Sohar/Sohar Free Zone.

Known positive leads: Ooredoo Sohar operational 10 MW/1,200-rack operator claim; Sohar Freezone cloud-data-center lease/project leads.

```text
site:ooredoo.om Sohar "data centre" "10 megawatts"
site:soharportandfreezone.om ("data center" OR "cloud data" OR "big data")
site:opaz.gov.om "Sohar Free Zone" "data center"
"صحار" "مركز بيانات" OR "المنطقة الحرة بصحار"
"North Batinah" OR "Al Batinah North" "data center"
```

### 5.3 Buraymi (Al Buraimi)

Wilayats: Al Buraimi, Mahdah, Al Sunaynah. UAE border; no verified datacenter seed found in this pass. Do a negative official/operator sweep and look for edge telecom, utility, and cross-border cloud mentions.

```text
"Buraymi" OR "Al Buraimi" OR "البريمي" ("data center" OR "data centre" OR "مركز بيانات")
"Mahdah" OR "محضة" "data center"
site:gov.om "البريمي" "مركز بيانات"
site:tra.gov.om "Buraimi" OR "البريمي" "cloud"
```

### 5.4 Interior (Ad Dakhiliyah)

Wilayats: Nizwa, Samail, Bahla, Adam, Al Hamra, Manah, Izki, Bidbid, Al Jabal Al Akhdar. Priorities: Firq/Nizwa, Jabal Al Akhdar, Samail Industrial Estate.

Known positive leads: Otech/Farq/Firq data center in Nizwa; Datamount Al Jabal Al Akhdar; possible crypto-mining expansion claims that require official confirmation.

```text
site:otech.om ("Firq" OR "Farq" OR "Nizwa" OR "نزوى") "data center"
site:datamount.om ("Jabal" OR "Akhdar" OR "Dakhiliyah")
"Al Jabal Al Akhdar" "data center" OR "الجبل الأخضر" "مركز بيانات"
"Nizwa" OR "Firq" "مركز بيانات" OR "أوتك"
site:madayn.om "Samail" "data"
```

### 5.5 Muscat

Wilayats: Muscat, Muttrah, Bawshar, Seeb, Al Amirat, Qurayyat. Priorities: Rusayl/KOM, Bawshar, Al Khuwair, Seeb/Al Bandar, undisclosed cloud hosts.

Known positive leads: Otech/Oman Data Park KOM4; Ooredoo Bawshar; Datamount Al Bandar and Muscat/Al Khuwair; AWS Local Zone Muscat; OCI Dedicated Region primary in Muscat.

```text
site:mm.gov.om ("data center" OR "مركز بيانات" OR "تصريح بناء")
site:mtcit.gov.om "Oman Data Park" "KOM4"
site:otech.om ("KOM" OR "Rusayl" OR "Muscat" OR "Oracle" OR "AWS")
site:ooredoo.om "Bawshar" "data centre"
site:datamount.om ("Al Bandar" OR "Muscat" OR "Al Khuwair")
site:docs.aws.amazon.com/local-zones "Oman (Muscat)"
"مسقط" "مركز بيانات" ("الروسيل" OR "الخوير" OR "بوشر" OR "السيب")
```

### 5.6 Musandam

Wilayats: Khasab, Bukha, Dibba Al Bayah, Madha. No verified datacenter seed found in this pass. Treat as negative-search unless telecom/defense/edge evidence appears.

```text
"Musandam" OR "مسندم" ("data center" OR "data centre" OR "مركز بيانات")
"Khasab" OR "خصب" "data center"
site:gov.om "مسندم" "مركز بيانات"
site:tra.gov.om "Musandam" OR "مسندم" "cloud"
```

### 5.7 Southeastern (Ash Sharqiyah South)

Wilayats: Sur, Jalan Bani Bu Ali, Jalan Bani Bu Hassan, Al Kamil Wal Wafi, Masirah. Priority: Qalhat/Sur cable landing evidence.

Known positive leads: Qalhat cable landing station for systems such as TGN-Gulf/SMW5; no verified colo/DC seed from this pass. Record cable as connectivity-only unless a DC is named.

```text
"Qalhat" OR "Sur" ("cable landing" OR "محطة إنزال الكابلات") ("TGN-Gulf" OR "SMW5")
"South Sharqiyah" OR "Ash Sharqiyah South" "data center"
"جنوب الشرقية" "مركز بيانات"
"Masirah" "data center"
```

### 5.8 Northeastern (Ash Sharqiyah North)

Wilayats: Ibra, Al Mudhaibi, Bidiyah, Al Qabil, Wadi Bani Khalid, Dima Wa Al Tayyin. No verified datacenter seed found in this pass. Do negative official/operator sweep.

```text
"Ibra" OR "إبراء" ("data center" OR "مركز بيانات")
"North Sharqiyah" OR "Ash Sharqiyah North" "data center"
"شمال الشرقية" "مركز بيانات"
site:gov.om "شمال الشرقية" "مركز بيانات"
```

### 5.9 Central (Al Wusta)

Wilayats: Haima, Mahout, Duqm, Al Jazer. Priority: Duqm/SEZAD.

Known positive leads: Otech/Oman Data Park Duqm DC in SEZAD from press/directory history; Duqm AI/green-energy policy leads. Need current official/operator reconfirmation before counting capacity.

```text
site:duqm.gov.om ("data center" OR "data centre" OR "AI" OR "مركز بيانات" OR "الذكاء الاصطناعي")
site:otech.om "Duqm" OR "الدقم" "data center"
"Oman Data Park" "Duqm" "data center"
"Al Wusta" OR "الوسطى" "data center" OR "مركز بيانات"
"Duqm" "green hydrogen" "data center"
```

### 5.10 Dhahira (Ad Dhahirah)

Wilayats: Ibri, Yanqul, Dhank. Priority: Ibri.

Known positive leads: Otech/ITHCA/Oracle OCI Secondary Dedicated Region in Ibri. This is cloud dedicated-region infrastructure; find host datacenter details before treating as generic colocation.

```text
site:otech.om ("Ibri" OR "عبري" OR "OCI Secondary Dedicated Region")
site:oracle.com Oman "Ibri" "Dedicated Region"
site:ithca.om "Ibri" "OCI"
"Ad Dhahirah" OR "Dhahira" OR "الظاهرة" "data center" OR "مركز بيانات"
"Yanqul" OR "Dhank" "data center"
```

### 5.11 Dhofar

Wilayats: Salalah, Taqah, Mirbat, Thumrait, Rakhyut, Dhalkut, Sadah, Shalim and the Hallaniyat Islands, Al Mazyunah, Muqshin. Priority: Salalah/Salalah Free Zone.

Known positive leads: Equinix SN1; Ooredoo Salalah DC+CLS; Exahertz/Afaaq data-hosting and crypto-mining facilities; multiple subsea-cable landings.

```text
site:equinix.com Oman Salalah SN1
site:ooredoo.om Salalah "data centre" OR "cable landing"
site:opaz.gov.om "Salalah Free Zone" "data center" OR "data centre"
site:omannews.gov.om "Salalah" "مركز بيانات" OR "تعدين"
"Salalah" "Exahertz" OR "Afaaq" "data hosting" OR "crypto mining"
"صلالة" ("مركز بيانات" OR "محطة إنزال الكابلات" OR "تعدين العملات")
"Dhofar" OR "ظفار" "data center"
```

## 6. Validation Workflow

1. Start with the known official/operator seeds above and create one candidate per physical site or cloud node.
2. Normalize division names: repo division, official governorate, Arabic governorate, wilayat, zone/industrial estate/free zone.
3. Assign evidence type and status. If only a cable, MoU, cloud Local Zone, or Dedicated Region is found, do not promote it to `operational_datacenter` without a host/facility source.
4. Run the permit/zone surface for the relevant governorate: Muscat Municipality, OPAZ/zoneservices, Madayn, SEZAD/Duqm, Sohar Port & Freezone, or governorate portal.
5. Run power corroboration: APSR, NPWP, OETC/Nama, distribution company, zone utility, and operator + MW/MVA/substation queries.
6. Check certification separately: Uptime Institute/TIA/ISO. Treat `Tier III`, `Level 3+`, and `built to Tier III standards` as operator claims unless certification list confirms.
7. Run Arabic official-media searches for `افتتاح`, `تدشين`, `إطلاق`, `وضع حجر الأساس`, `تخصيص أرض`, and `دخل الخدمة`.
8. For negative divisions, save query evidence. Buraymi, Musandam, Northeastern, and parts of Southeastern/Dhahira should not be left blank.

## 7. Reliability Notes

- Grade A is honest only for what the source directly says. Ooredoo can be A for Ooredoo's own Sohar launch and capacity claim; it is not A for independent certification unless a certifying body says so.
- Trade press such as DCD is B, even when highly useful, unless it reproduces or links an official release. Use it to fill physical geography, dates, and context, then seek official corroboration.
- Directories such as Data Center Map, Baxtel, Cloudscene, PeeringDB and Datacenters.com are C by default. Uptime Institute's certification list is A for certifications only.
- Market-size reports are C for enumeration. They may name investors/operators but should not create facilities.
- Crypto-mining sources require extra discipline: MTCIT/ONA/Oman Observer launch coverage can support a facility; crypto blogs and social posts are leads only.
