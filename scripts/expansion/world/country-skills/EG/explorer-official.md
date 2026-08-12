# EG Explorer Official - Egypt Datacenter Enumeration via NTRA, Planning, Power, Cloud, Colo, and Governorate Sources

Date: 2026-08-12. Country: **EG Egypt**. Division model: **27 governorates**: Alexandria, Aswan, Asyut, Red Sea, Beheira, Beni Suef, Cairo, Dakahlia, Damietta, Faiyum, Gharbia, Giza, Ismailia, South Sinai, Qalyubia, Kafr el-Sheikh, Qena, Luxor, Minya, Monufia, Matrouh, Port Said, Sohag, Al Sharqia, North Sinai, Suez, New Valley. Angle: **official/regulatory/cloud pipeline** for finding commercial, hyperscale, government, telecom, and enterprise datacenter facilities.

Reliability grades:
- **A** = primary/official source: NTRA licence/framework/press release, MCIT/ITIDA/SIS/governorate/new-city authority page, local building-permit or technology-centre record, EETC/EgyptERA/EEHC/Ministry of Electricity/NREA page, EEAA environmental record, official cloud-provider page, official operator page.
- **B** = strong secondary source: trade press, Uptime Institute certification, engineering/contractor page, GAFI/investment-zone lead, datacenter press release by an investor/partner when the operator/site is named.
- **C** = weak lead: market-report snippet, directory-only listing, social post, generic ICT/offshoring statement, vendor case study without site details.

---

## 0. Egypt-specific structural facts

- Egypt does **not** have one public national planning register for datacenters. Enumeration should join **NTRA licensing**, governorate/local building-permit services, New Urban Communities Authority (NUCA) / new-city authorities, GAFI/free-zone/investment-zone leads, electricity and renewable-energy evidence, environmental approvals, cloud-region pages, official operator pages, and trade press.
- **NTRA is more important in Egypt than in many countries.** NTRA has a specific framework for establishing/operating datacenters and providing hosting/cloud computing services, and its licence descriptions identify separate `Data center` and `Cloud computing` licences. Treat an NTRA data-center licence as Grade **A** operator/service evidence, but still verify each physical facility via planning, power, environmental, operator, or contractor sources.
- Planning is fragmented between **ordinary governorate/local administration**, **new urban communities/new cities**, **technology parks**, **free zones**, and major national projects such as the **New Administrative Capital**. For Cairo/Giza/New Cairo/6th of October/Maadi/Smart Village/New Administrative Capital/10th of Ramadan/New Borg El Arab/East Port Said/New Alamein, do not assume the ordinary governorate portal is the only permitting authority.
- Official government service routing is improving but not necessarily public-searchable. Use **Local Services Portal** (`https://lgs.gov.eg/`), **Digital Egypt** (`https://digital.gov.eg/` / `https://egypt.gov.eg/`), governorate portals, district technology centres, and NUCA/new-city authority pages for workflow terms; then search indexed PDFs/news by project/operator/plot.
- Power is a decisive lead. Large projects may surface through **EETC** grid-connection studies, **EgyptERA** licences/direct-sale/wheeling rules, **EEHC/Ministry of Electricity** announcements, **NREA/PV Hub** renewable supply, and named substations. Keep total utility supply, renewable PPA size, IT load MW, and backup-generator capacity as separate fields.
- Arabic is mandatory for high recall. Use English variants `data center`, `data centre`, `datacenter`, `cloud`, `hosting`, `colocation`, `hyperscale`, `AI data center`, `server room`, `Tier III`, `Tier IV`, `substation`, `MW`, `MVA`, and Arabic variants `مركز بيانات`, `مراكز بيانات`, `مركز داتا`, `سنتر داتا`, `مركز حوسبة`, `الحوسبة السحابية`, `استضافة`, `خدمات الاستضافة`, `تراخيص مراكز البيانات`, `رخصة بناء`, `تصريح بناء`, `المركز التكنولوجي`, `محطة محولات`, `ميجاوات`, `م.ف.أ`.

---

## 1. Grade A official/regulatory portals and how to use them

### 1.1 NTRA datacenter and cloud licensing

Primary URLs:
- **NTRA datacenter/cloud framework**: https://www.tra.gov.eg/en/regulatory-framework-for-establishing-operating-data-centers-and-providing-hosting-and-cloud-computing-services/
- **NTRA approval announcement for the framework**: https://www.tra.gov.eg/en/ntra-approves-a-regulatory-framework-to-establish-data-centers-in-egypts-market/
- **NTRA licence brief PDF**: https://www.tra.gov.eg/wp-content/uploads/2023/10/Licenses-Brief-Description-.pdf
- **NTRA telecommunications service licensees PDF**: https://www.tra.gov.eg/wp-content/uploads/2023/10/Telecommunication-Services-Licensees.pdf
- **NTRA global peering licence terms PDF**: https://www.tra.gov.eg/wp-content/uploads/2020/11/Rules-and-conditions-Global-Peering.translation-last-version.pdf
- **NTRA sitemap for regulatory-framework discovery**: https://www.tra.gov.eg/en/sitemap/

How to use:
- Search NTRA first for every operator or project. NTRA licences can identify companies allowed to establish/operate datacenters or provide cloud services, and peering licences may mention content hosting centers, Telecom Egypt exchanges, and NTRA prior approval for sites.
- Extract: legal entity, licence type (`Data center`, `Cloud computing`, `Global Peering`, `Class A/B/C`, telecom infrastructure leasing), licence duration, issue date, permitted services, whether the licence is for facilities, cloud services, hosting, colocation, peering, or telecom network infrastructure, and any named site.
- Do not convert a cloud-services licence into a facility record unless a datacenter site is separately named. A cloud provider can be NTRA-accredited without owning the building.

NTRA queries:

```text
site:tra.gov.eg "data center" "license" Egypt
site:tra.gov.eg "data centers" "cloud computing services"
site:tra.gov.eg "Establishing and operating data centers"
site:tra.gov.eg "Telecommunication Services Licensees" "Data Center"
site:tra.gov.eg filetype:pdf "Data center" "Cloud computing"
site:tra.gov.eg "{operator}" "Data Center"
site:tra.gov.eg "{operator}" "Cloud computing"
site:tra.gov.eg "{operator}" "Global Peering"
site:tra.gov.eg "مراكز البيانات" "ترخيص"
site:tra.gov.eg "الحوسبة السحابية" "ترخيص"
"NTRA" "data center" "{operator}"
"الجهاز القومي لتنظيم الاتصالات" "مركز بيانات" "{operator}"
```

High-value NTRA licence-name pivots: `Telecom Egypt`, `Raya`, `Raya Data Center`, `GPX`, `Orange Egypt`, `Orange Business`, `e& Egypt`, `Etisalat Misr`, `Vodafone Egypt`, `Hassan Allam`, `Khazna`, `Benya`, `Huawei Cloud`, `Heca Data`, `Renergy`, `ECC Solutions`, `Noor`, `Link Datacenter`, `WE`, `Egyptian Banks Company`, `EGID`.

### 1.2 National ICT, technology park, and government-announcement sources

Primary URLs:
- **MCIT**: https://mcit.gov.eg/
- **ITIDA Maadi Technology Park**: https://itida.gov.eg/English/Pages/MaadiPark.aspx
- **ITIDA industry/outlook/offshoring pages**: https://itida.gov.eg/English/Programs/Industry-Outlook/Pages/default.aspx and https://itida.gov.eg/English/Pages/Outsourcing-Egypt.aspx
- **State Information Service (SIS)**: https://sis.gov.eg/en/
- **Ministry of Planning, Economic Development and International Cooperation**: https://mped.gov.eg/

Use these as Grade **A** government-context and project-announcement sources. ITIDA is especially important for **Maadi Technology Park**, whose official page states that the park has datacenters and gives a Cairo address. SIS and ministry pages are useful for national strategy, smart-government complexes, renewable-power/data-center policy, and ministerial MoUs.

Queries:

```text
site:mcit.gov.eg "data center" Egypt
site:mcit.gov.eg "data centre" OR datacenter OR "cloud services"
site:mcit.gov.eg "مركز بيانات" OR "مراكز البيانات" OR "الحوسبة السحابية"
site:itida.gov.eg "data center" OR "data centers" OR "Maadi Technology Park"
site:sis.gov.eg "data center" "Egypt"
site:sis.gov.eg "National Data Centers Strategy"
site:sis.gov.eg "مركز بيانات" OR "مراكز البيانات"
site:mped.gov.eg "data center" OR "spatial data center" OR "digital transformation"
site:mped.gov.eg "مركز بيانات" OR "مركز البيانات المكاني"
```

Extract: government project owner, site/governorate, whether the reference is a commercial datacenter or a government/service/spatial-data center, project stage, named investor/operator, target capacity, and whether the announcement is only an MoU.

### 1.3 Building permits, local services, and new-city authorities

Primary routing URLs:
- **Local Services Portal / بوابة خدمات المحليات**: https://lgs.gov.eg/
- **Digital Egypt / Egypt government services**: https://digital.gov.eg/ and https://egypt.gov.eg/
- **Ministry of Local Development**: https://mld.gov.eg/
- **NUCA / New Urban Communities Authority**: https://www.newcities.gov.eg/english/aboutus/about_authority/default.aspx and https://nuca.gov.eg/
- **SIS note on NUCA online services for Egyptians abroad**, including construction/licensing services: https://sis.gov.eg/en/egyptians-abroad-portal/government-services/new-urban-communities-authority-nuca-launches-online-services-for-egyptians-abroad/

Practical method:
- For ordinary urban/rural areas, start from the relevant **governorate portal** and `lgs.gov.eg` service terms (`رخصة بناء`, `شهادة صلاحية`, `تعديل ترخيص`, `تصالح`, `المركز التكنولوجي`). Public file search is limited, so use service portals for workflow and then search indexed governorate news/PDFs.
- For new cities and satellite cities, search **NUCA**, **newcities.gov.eg**, the city development authority (`جهاز تنمية مدينة ...`), and Ministry of Housing pages. This is critical for **6th of October, Sheikh Zayed, New Cairo, Badr, Obour, 10th of Ramadan, New Borg El Arab, New Damietta, New Beni Suef, New Minya, New Asyut, New Qena, New Sohag, New Aswan, New Alamein, East Port Said, New Administrative Capital**.
- For strategic/new-capital projects, search **ACUD / Administrative Capital for Urban Development**, official New Administrative Capital material, Ministry of Housing, and contractor/operator pages. The New Administrative Capital is administratively associated with the Cairo-region planning ecosystem but may not appear cleanly in Cairo governorate records.
- For investment/free zones, search **GAFI**, `investinegypt.gov.eg`, free-zone authority pages, and zone managers. GAFI industrial-zone and investment-zone pages are useful official seed sources, not direct building-permit proof.

Planning queries:

```text
site:lgs.gov.eg "رخصة بناء" "مركز بيانات"
site:digital.gov.eg "رخصة بناء" OR "تراخيص البناء"
site:egypt.gov.eg "building permit" Egypt
site:mld.gov.eg "مركز بيانات" OR "مراكز البيانات" OR "تراخيص البناء"
site:newcities.gov.eg "data center" OR "مركز بيانات"
site:nuca.gov.eg "data center" OR "مركز بيانات" OR "رخصة بناء"
site:gafi.gov.eg "data center" OR "مركز بيانات"
site:investinegypt.gov.eg "data center" OR "مركز بيانات"
"جهاز تنمية مدينة {new-city}" "مركز بيانات"
"محافظة {governorate-ar}" "مركز بيانات" "رخصة بناء"
"{operator}" "رخصة بناء" "مركز بيانات"
"{operator}" "قطعة أرض" "مركز بيانات"
"{operator}" "مدينة {new-city}" "data center"
```

Data to extract from planning/building material: permit number, plot/parcel/block, city/district, technology park/free zone/new-city authority, applicant/proponent, owner/developer/operator, described use (`data center`, `server building`, `telecom exchange`, `ICT building`), land area, built-up area, floors, data halls/racks, MVA/MW, generators/fuel tanks, cooling/water system, construction/operation dates, completion certificate, and appeals/conditions.

### 1.4 Environmental approval and EIA route

Primary URLs:
- **Egyptian Environmental Affairs Agency (EEAA)**: https://www.eeaa.gov.eg/
- **Ministry of Environment**: https://www.eeaa.gov.eg/

Egyptian EIA evidence may not use the English phrase `data center`. Search for backup generators, fuel storage, cooling, substations, industrial/service buildings, ICT buildings, and technology parks. EEAA and the competent administrative authority/governorate are the preferred Grade **A** sources when a signed approval, EIA requirement, or official public notice is found. Consultant-hosted EIA documents are Grade **B+** unless the government approval letter is included.

Environmental queries:

```text
site:eeaa.gov.eg "data center" OR "data centre" OR datacenter
site:eeaa.gov.eg "مركز بيانات" OR "مراكز البيانات"
site:eeaa.gov.eg "{operator}" "تقييم الأثر البيئي"
site:eeaa.gov.eg "{project}" "مولدات" OR "خزانات وقود"
"مركز بيانات" "تقييم الأثر البيئي" مصر
"data center" "Environmental Impact Assessment" Egypt
"data center" "diesel generators" Egypt "EEAA"
"Maadi Technology Park" "environmental" "data center"
```

Extract: approval/reference number, competent administrative authority, project location and coordinates, proponent, EIA category, generator count/rating, diesel/fuel tank volume, water/cooling demand, wastewater, air/noise controls, construction phase, public consultation, and conditions.

---

## 2. Power, grid, renewable, and utility evidence

Primary URLs:
- **Ministry of Electricity and Renewable Energy**: https://www.moee.gov.eg/english_new/home.aspx
- **Egyptian Electricity Holding Company (EEHC)**: https://www.eehc.gov.eg/CMSEehc/en
- **Egyptian Electric Utility and Consumer Protection Regulatory Agency (EgyptERA)**: https://www.egyptera.org/en/
- **Egyptian Electricity Transmission Company (EETC)**: search through Ministry/EEHC pages and official announcements; EETC often appears in ministry/SIS/Ahram announcements.
- **Egypt PV Hub**: https://pv-hub.org/?lang=en&page_id=8731
- **New and Renewable Energy Authority (NREA)**: https://www.nrea.gov.eg/

How to use:
- Search **EETC + operator/project** for grid-connection studies, substations, power-supply MoUs, and wheeling/direct-supply arrangements. A 2026 EETC/Heca Data MoU reported by Ahram/Egypt Today is a model lead: use trade press as a lead, then find the originating Ministry of Electricity statement if possible.
- Use **EgyptERA** for electricity licences, connection guidance, daily observatory/tariff context, private generation, distribution, direct sales, and wheeling/regulatory rules. Grade **A** when EgyptERA names the customer/operator/project; otherwise treat it as sector context.
- Use **EEHC/Ministry of Electricity/SIS** for national strategy and named data-center-energy announcements, including plans to match available sites with renewable energy, grid readiness, telecom readiness, and investment incentives.
- Use **NREA/PV Hub** and renewable-project announcements for green datacenter leads in Red Sea, Suez, Aswan, New Valley, South Sinai, Matrouh, and Benban/Kom Ombo corridors. A renewable project next to a datacenter is not IT load unless the source ties it to the facility.

Power queries:

```text
site:moee.gov.eg "data center" OR "data centre" OR datacenter
site:moee.gov.eg "مركز بيانات" OR "مراكز البيانات"
site:eehc.gov.eg "data center" OR "مركز بيانات"
site:egyptera.org "data center" OR "مركز بيانات" OR "{operator}"
site:nrea.gov.eg "data center" OR "مركز بيانات"
site:pv-hub.org "data center" OR "مركز بيانات"
"EETC" "data center" Egypt
"Egyptian Electricity Transmission Company" "data center"
"الشركة المصرية لنقل الكهرباء" "مركز بيانات"
"{operator}" "EETC" "MW" OR "MVA"
"{operator}" "محطة محولات" "مركز بيانات"
"{project}" "renewable energy" "data center" Egypt
"{project}" "solar" "wind" "data center" Egypt
```

Extract: requested/contracted MVA, IT load MW, grid import capacity, voltage level, substation/feeder, connection-study status, wheeling/direct-supply licence, PPA counterparty, renewable MW, battery/storage if any, energisation date, backup generation, fuel storage, and whether power is committed, proposed, or merely strategic.

---

## 3. Official cloud-region and edge signals

Cloud pages are Grade **A** for cloud-region/edge existence but **not** exact building addresses. Use them to seed NTRA, operator, planning, and power searches.

| Provider | Official source | Egypt signal | Enumeration use |
|---|---|---|---|
| Huawei Cloud | Launch: https://www.huawei.com/en/news/2024/5/huawei-cloud-goes-live-in-egypt ; Huawei Cloud launch: https://www.huaweicloud.com/intl/en-us/news/20240523155312706.html ; infrastructure page: https://www.huaweicloud.com/intl/en-us/about/global-infrastructure.html | Official Cairo/Egypt cloud region, listed as `AF-Cairo`; launch announced in May 2024. | Seed **Cairo/Giza/New Cairo/Maadi/Smart Village** and NTRA accreditation/licence searches. Verify facility/operator/host through NTRA, operator, planning, power, or trade press. |
| Microsoft Azure | Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Azure Front Door POP region list: https://learn.microsoft.com/en-us/azure/frontdoor/edge-locations-by-region ; abbreviation list: https://learn.microsoft.com/en-us/azure/frontdoor/edge-locations-by-abbreviation | No Egypt Azure public region in the checked regions list; Microsoft Front Door lists Cairo POPs/`CAI`. | Treat Cairo POPs as edge/interconnection leads only, not cloud-region/datacenter-campus proof. Search for Microsoft partner/hosting/NTRA records if a local cloud claim appears. |
| AWS | Regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Local Zones: https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ ; AWS Africa: https://aws.amazon.com/local/africa/ | No Egypt AWS region or GA Local Zone found in checked official region/location pages. AWS Outposts availability in Egypt is customer-prem/edge service, not a public region. | Do not create an Egypt AWS facility record from regional sales/Outposts material. Use only as a tenant/partner lead if NTRA or operator evidence names a site. |
| Google Cloud | Locations: https://cloud.google.com/about/locations ; Compute regions/zones: https://docs.cloud.google.com/compute/docs/regions-zones | No Egypt public Google Cloud region in checked official pages. | Use only as enterprise/partner/edge lead; no Egypt datacenter inference without primary local evidence. |
| Oracle OCI | Public regions: https://www.oracle.com/cloud/public-cloud-regions/ ; OCI regions docs: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No Egypt OCI public region confirmed in checked official pages. | Use Oracle Egypt announcements only as cloud-market leads unless Oracle's official regions page lists an Egypt region or local operator/NTRA evidence names a facility. |

Cloud queries:

```text
"Huawei Cloud" "Cairo Region" "Egypt" "data center"
site:huaweicloud.com Egypt "AF-Cairo"
site:tra.gov.eg "Huawei Cloud" "Egypt" "NTRA"
"Azure Front Door" "Cairo" "CAI" "Egypt"
site:learn.microsoft.com "CAI" "Cairo, Egypt"
site:aws.amazon.com Egypt "Local Zone" OR "Outposts"
site:cloud.google.com Egypt "region" OR "Cairo"
site:oracle.com "Egypt" "cloud region" OR "OCI"
```

---

## 4. Official/operator facility seed list

Operator pages are Grade **A** for marketed facility existence and broad location when they are official. They are not enough by themselves for planning status, exact address, or utility load unless the page includes those facts.

| Operator / project | Official or strong source | Egypt footprint signal | Follow-up joins |
|---|---|---|---|
| Telecom Egypt / Regional Data Hub (RDH) | Telecom Egypt IR press release: https://ir.te.eg/en/CorporateNews/PressRelease/132/Telecom-Egypt-is-building-Egypt-s-largest-international-data-center ; RDH2 press release: https://ir.te.eg/en/CorporateNews/PressRelease/211/Telecom-Egypt-s-Regional-Data-Hub-2-Awarded-Tier-III-Design-Certification ; Uptime award: https://uptimeinstitute.com/uptime-institute-awards/datacenter/telecom-egypt-regional-data-hub/1295 | Smart Village / West Cairo / 6th of October / Giza lead; RDH2 Tier III design certification and submarine-cable hub framing. | Search NTRA licensees, Smart Village/6th of October/NUCA, EETC/EEHC, contractor pages, completion status, and any Helios carve-out filings. |
| Maadi Technology Park / ITIDA | https://itida.gov.eg/English/Pages/MaadiPark.aspx | ITIDA official page says Maadi Technology Park has datacenters and gives the Maadi/Cairo address. | Search ITIDA/MCIT, Cairo governorate/Maadi permits, Khazna/Benya, NTRA, power and environmental records. |
| Khazna / Benya Maadi hyperscale project | Khazna official press release: https://khaznadatacenters.com/press-release/khazna-data-centers-plans-to-enter-egypt-with-benya-group-to-set-up-the-countrys-first-hyper-scale-data-center-in-maadi-technology-park-with-a-total-investment-of-usd-250m/ | Proposed hyperscale datacenter at Maadi Technology Park, Cairo; official operator/investor source. | Verify current status through NTRA licence, ITIDA/MCIT, Cairo/Maadi planning, EETC power, EEAA environmental approvals, and construction/trade press. |
| Huawei Cloud Cairo Region | https://www.huawei.com/en/news/2024/5/huawei-cloud-goes-live-in-egypt and https://www.huaweicloud.com/intl/en-us/about/global-infrastructure.html | Public cloud Cairo/Egypt region; exact facility/host not disclosed on official cloud pages. | Search NTRA accreditation/licence, Telecom Egypt/Raya/GPX/Orange/Benya/operator partnerships, and Cairo/Giza power/planning evidence. |
| GPX Global Systems | https://gpxglobal.net/ | Official GPX page references Cairo datacenter and 2023 major expansion of Cairo data center. | Search GPX Cairo 1/Cairo 2, NTRA, New Cairo/Cairo permits, EETC/EEHC, Uptime, and DCD/trade press for expansion MW/sqm. |
| Raya Data Center / Raya IT | https://www.rayadatacenter.com/ ; https://raya-it.net/solution-data-center/ ; Raya Holding/Africa50 announcement: https://rayacorp.com/raya-holding-announces-15-million-investment-in-raya-data-center-from-africa50-to-build-a-tier-iii-data-center-in-egypt/ | Official Raya pages give 6th of October/Giza contact; Raya IT says data centers in 6th of October, Maadi, and New Cairo; Africa50-backed new Tier III lead. | Search Giza/Cairo/New Cairo/NUCA, NTRA, Africa50, EETC, EEAA, and contractor pages. |
| Orange Egypt / Orange Business | Orange Egypt hosting page: https://www.orange.eg/en/business/business-solutions/hosting-and-data-center ; Orange Business Grifols Egypt release: https://www.orange-business.com/en/press/grifols-egypt-collaborates-orange-business-deliver-new-data-center-communications | Orange Egypt says it owns/operates a private datacenter; Orange Business built/operates customer datacenter infrastructure for Grifols Egypt in the New Administrative Capital. | Search NTRA, Orange Egypt legal names, New Administrative Capital/ACUD, Cairo-region power, EEAA, and customer project pages. |
| e& Egypt / Etisalat Misr / Vodafone Egypt / WE | NTRA licensee records and operator pages | Mobile/fixed operators can operate exchange/core/datacenter sites; directories often place telecom facilities in Smart Village, Cairo, Giza, and exchanges. | Require official operator, NTRA, Uptime, contractor, or planning evidence before counting facility records. |
| ECC Solutions / Link Datacenter / Noor / Egyptian enterprise providers | Operator pages, NTRA records, Uptime/certification records, directories | Smaller enterprise/cloud/hosting datacenter leads, usually Greater Cairo. | Search exact legal names + NTRA + `Tier III` + Arabic terms + 6th of October/New Cairo/Maadi/Smart Village. |
| Government/smart-city datacenters | SIS, MCIT, MPED, governorate pages | Examples include smart-government service complexes, spatial-data centers, and government datacenter components. | Mark as government/enterprise/internal unless colocation/cloud services are offered; do not mix with commercial colo inventory. |

Operator queries:

```text
"{operator}" Egypt "data center" "MW"
"{operator}" Egypt "data centre" "Tier III"
"{operator}" "مركز بيانات" مصر
"{operator}" "NTRA" "data center"
"{operator legal name}" "Telecommunication Services Licensees"
"{facility}" "Uptime Institute" Egypt
"{facility}" "EETC" OR "Egyptian Electricity Transmission Company"
"{facility}" "محطة محولات" OR "ميجاوات"
"{facility}" "رخصة بناء" OR "تصريح بناء"
```

---

## 5. Trade press and secondary-source triage

Use trade press for discovery and status gaps, then try to backfill with official/operator evidence.

High-value secondary sources:
- **Ahram Online**: https://english.ahram.org.eg/ - useful for ministry/EETC announcements; example EETC/Heca Data MoU.
- **Egypt Today**: https://www.egypttoday.com/ - government and data-center energy MoU coverage.
- **Data Center Dynamics**: https://www.datacenterdynamics.com/ - strong datacenter-specific project reporting.
- **W.Media**: https://w.media/ - MENA/Africa datacenter licence and operator reporting.
- **International Trade Administration Egypt datacenters note**: https://www.trade.gov/market-intelligence/egypt-data-centers - market/context lead; not a facility registry.
- **Uptime Institute awards/certifications**: https://uptimeinstitute.com/uptime-institute-awards/ - certification evidence for named facilities, but not necessarily ownership or exact permit status.
- **Engineering/contractor pages**: e.g. ECG's RDH2 page https://www.ecgsa.com/telecom-egypt-regional-data-hub-2-rdh2-data-center/ can provide land area, built-up area, IT load, rack count, and status; grade **B** unless the client/operator confirms.

Trade-press queries:

```text
site:datacenterdynamics.com Egypt "data center"
site:w.media Egypt "data centre" OR "data center" "NTRA"
site:english.ahram.org.eg "data centre" OR "data center" Egypt
site:egypttoday.com "data center" "EETC"
site:trade.gov "Egypt Data Centers"
site:uptimeinstitute.com Egypt "data center"
"Egypt" "data center" "NTRA license"
"Egypt" "hyperscale data center" "Maadi Technology Park"
"Egypt" "green data center" "MW"
```

---

## 6. Governorate enumeration strategy

### 6.1 Standard governorate workflow

For each governorate:
1. Search NTRA and official operator pages by known local anchors: `Telecom Egypt`, `Raya`, `GPX`, `Orange`, `Huawei Cloud`, `Khazna`, `Benya`, `Hassan Allam`, `Heca Data`, `Renergy`, `e& Egypt`, `Vodafone`, `Noor`, `ECC`.
2. Search governorate portal + Local Services Portal terms: `رخصة بناء`, `تصريح بناء`, `المركز التكنولوجي`, `قطعة أرض`, `منطقة صناعية`, `منطقة حرة`, `مركز بيانات`, `مراكز البيانات`.
3. If the candidate is in a new city, search NUCA/newcities and the `جهاز تنمية مدينة {city}` rather than only the governorate.
4. Search power and environmental sources: `EETC`, `EgyptERA`, `EEHC`, `وزارة الكهرباء`, `محطة محولات`, `MW`, `MVA`, `EEAA`, `تقييم الأثر البيئي`, `مولدات`, `خزانات وقود`.
5. Use cloud/edge pages only to seed metro searches. Do not infer physical facility count from cloud regions, availability zones, or POPs.
6. Use trade press/directories to find alternate names and addresses, then verify with at least one A source where possible.

Template:

```text
site:{governorate-domain} ("data center" OR "data centre" OR datacenter OR "مركز بيانات" OR "مراكز البيانات")
site:{governorate-domain} ("رخصة بناء" OR "تصريح بناء" OR "المركز التكنولوجي") ("مركز بيانات" OR "{operator}")
"{governorate}" "data center" Egypt
"{governorate-ar}" "مركز بيانات"
"{city-or-district}" "{operator}" "data center"
"{city-or-district-ar}" "{operator}" "مركز بيانات"
"{operator}" "{governorate}" "NTRA"
"{operator}" "{governorate}" "EETC" OR "محطة محولات"
"{operator}" "{governorate}" "EEAA" OR "تقييم الأثر البيئي"
```

### 6.2 High-yield governorates

- **Cairo**: Search Cairo Governorate, Maadi, Maadi Technology Park, New Cairo (also NUCA), New Administrative Capital/ACUD, Nasr City, Mokattam, Heliopolis, and Cairo technology centres. Key leads: ITIDA Maadi Technology Park, Khazna/Benya Maadi, GPX Cairo/New Cairo, Raya Maadi/New Cairo, Orange/New Administrative Capital customer infrastructure, Huawei Cloud Cairo region/edge claims. Queries: `site:cairo.gov.eg "مركز بيانات"`, `"Maadi Technology Park" "data center"`, `"New Cairo" "GPX" "data center"`, `"العاصمة الإدارية" "مركز بيانات"`, `"القاهرة" "الحوسبة السحابية"`.
- **Giza**: Highest confirmed commercial cluster because of Smart Village and 6th of October. Search Giza Governorate, Smart Village, 6th of October City Authority, Sheikh Zayed, NUCA, Telecom Egypt RDH/RDH2, Raya 6th of October, e&/Etisalat Smart Village, and CAIX/peering references. Queries: `"Smart Village" "Regional Data Hub"`, `"6th of October" "data center"`, `"مدينة السادس من أكتوبر" "مركز بيانات"`, `site:newcities.gov.eg "السادس من أكتوبر" "مركز بيانات"`.
- **Alexandria**: Search Alexandria Governorate, Borg El Arab/New Borg El Arab, free zones, cable/network routes, Orange/Vodafone/Telecom Egypt exchanges, and disaster-recovery/enterprise datacenters. Queries: `"Alexandria" "data center" Egypt`, `"برج العرب" "مركز بيانات"`, `"New Borg El Arab" "data center"`, `"محافظة الإسكندرية" "مركز بيانات"`.
- **Red Sea**: Prioritize renewable-energy and cable/landing/tourism-resort infrastructure around Hurghada, Gouna, Safaga, Marsa Alam, and Ras Ghareb. Search NREA, EETC, red-sea governorate, and investor announcements for green datacenter projects. Queries: `"Red Sea" Egypt "data center"`, `"الغردقة" "مركز بيانات"`, `"Ras Ghareb" "data center" "renewable"`, `"البحر الأحمر" "محطة محولات" "مركز بيانات"`.
- **Suez**: High-priority for Suez Canal corridor, submarine-cable routes, Ain Sokhna, Suez Canal Economic Zone (SCZone), industrial zones, and renewable/hydrogen-linked projects. Queries: `site:sczone.eg "data center" OR "مركز بيانات"`, `"Ain Sokhna" "data center"`, `"Suez Canal Economic Zone" "data center"`, `"السويس" "مركز بيانات" "محطة محولات"`.
- **Port Said**: Search East Port Said/new city/free zone/SCZone and West Port Said Free Zone digital-infrastructure projects. Existing leads include West Port Said Free Zone datacenter management. Queries: `"Port Said Free Zone" "data center"`, `"East Port Said" "data center"`, `"بورسعيد" "مركز بيانات"`, `site:sczone.eg "Port Said" "data center"`.
- **South Sinai**: Search El Tor, Sharm El Sheikh, Ras Sudr, green-energy/hydrogen projects, and Renergy/renewable-data-center leads. Queries: `"El Tor" "hyperscale" "data center"`, `"South Sinai" "green data center"`, `"الطور" "مركز بيانات"`, `"جنوب سيناء" "مركز بيانات" "طاقة متجددة"`.
- **Matrouh**: Search Marsa Matrouh, New Alamein, Ras El Hekma, smart-government services complex, NUCA/New Alamein, and digital/spatial-data center components. Queries: `"Matrouh" "data center"`, `"Marsa Matrouh" "smart government services complex" "data center"`, `"New Alamein" "data center"`, `"مطروح" "مركز بيانات"`.
- **Qalyubia**: Search Shubra Al Khayma, Obour, Qalyubia governorate, Telecom Egypt exchange/core sites, industrial zones, and CAIX/Ramses/Manti references. Queries: `"Qalyubia" "data center"`, `"Shubra Al Khayma" "data center"`, `"القليوبية" "مركز بيانات"`, `"العبور" "مركز بيانات"`.
- **Qena**: Search government/Telecom Egypt regional exchange/datacenter claims, New Qena, Qena governorate, and upper-Egypt digital transformation projects. Queries: `"Qena" "data center" "Telecom Egypt"`, `"قنا" "مركز بيانات"`, `"New Qena" "data center"`.

### 6.3 Medium-yield governorates

- **Ismailia**: Suez Canal corridor, technology/investment zones, cable/fibre routes, and SCZone/Canal projects. Search `الإسماعيلية`, `Ismailia`, `SCZone`, `Qantara`, `data center`, `مركز بيانات`.
- **Damietta**: New Damietta/NUCA, port/logistics and free-zone context, but expect low datacenter density. Search `دمياط الجديدة`, `New Damietta`, `مركز بيانات`, `محطة محولات`.
- **Dakahlia**: New Mansoura/NUCA and Mansoura government/ICT services. Search `New Mansoura`, `المنصورة الجديدة`, `مركز بيانات`.
- **Al Sharqia**: 10th of Ramadan, Obour/industrial spillover, Belbeis, and manufacturing/industrial-zone utility leads. Search `10th of Ramadan data center`, `العاشر من رمضان مركز بيانات`.
- **Beheira**: Nubariya/New Nubariya and Alexandria/Cairo corridor infrastructure. Search `البحيرة`, `النوبارية`, `مركز بيانات`.
- **Beni Suef, Minya, Asyut, Sohag, Aswan, Luxor**: Search new-city authorities, Telecom Egypt/government datacenter components, upper-Egypt digital transformation, and power/renewable corridors. Use Arabic governorate names and new-city names.
- **Faiyum, Monufia, Gharbia, Kafr el-Sheikh**: Mostly negative sweeps unless a government service complex, Telecom Egypt exchange, university/health datacenter, or local operator/cloud service appears.
- **North Sinai and New Valley**: Low probability for commercial colo; search renewable/strategic/government infrastructure, telecom resilience, and official digital-service projects.

---

## 7. Status and evidence rules

- `operational`: official operator page, Uptime record, government/operator completion announcement, or current service page identifies a live facility. Directory-only entries are **C** unless corroborated.
- `construction`: official permit, contractor page, operator announcement, Uptime design certification with build timeline, or government announcement says construction/execution is underway.
- `planned`: MoU, licence, investment announcement, land allocation, power-study MoU, or strategy names a datacenter but no construction evidence is found.
- `candidate`: cloud POP, NTRA cloud licence, technology-park datacenter wording, exchange/telecom building, or market-report lead without facility proof.

Minimum record fields to capture: governorate, city/district/new city, site/park/free zone, operator/developer/legal entity, facility name and aliases, status, source grade, source URLs, evidence date, capacity MW/MVA/racks/sqm when directly supported, NTRA licence relation, planning authority, power source, environmental source, and notes distinguishing commercial colo/cloud from internal/government/telecom exchange infrastructure.
