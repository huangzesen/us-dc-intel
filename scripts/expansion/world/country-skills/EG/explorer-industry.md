# EG Explorer - Industry, Vendor, Cloud, and Governorate Query Methodology

Date: 2026-08-12. Scope: how to enumerate Egypt datacenter projects through Egyptian colo providers, cloud-region evidence, trade press, associations/investment agencies, and repeatable English + Arabic query patterns per governorate. Reliability grades: **A** = primary regulator, government, operator, official cloud-region, contractor, or listed-company source; **B** = established trade press, development-bank/investor source, or strong contractor/customer case study; **C** = directories, social posts, market-report snippets, or unverifiable aggregators used as leads only.

---

## 0. Egypt-specific frame

- Egypt does **not** expose a single public facility registry for datacenters. Enumeration works by triangulating: **NTRA licensees and regulatory framework**, MCIT/ITIDA/government media, operator facility pages, cloud-region pages, Suez Canal Economic Zone and new-city announcements, contractor project pages, telecom/cable landing material, trade press, and directories.
- The commercial market is heavily concentrated in **Greater Cairo**: Cairo, Giza, New Cairo, Maadi, 6th of October / Smart Village, and the New Administrative Capital. Outside Greater Cairo, expect a smaller number of planned hyperscale campuses, telco/edge facilities, government/free-zone datacenters, and unverified directory-only entries.
- Treat **cloud region**, **edge POP**, **public cloud service**, **partner-hosted cloud**, **government datacenter**, and **commercial colocation facility** as separate record types. Egypt has Huawei Cloud Cairo Region evidence; AWS/Azure/GCP/OCI official public-region tables should be checked to avoid false positives.
- Arabic and English searches are both needed. English coverage is strongest for hyperscale, investment, cloud, and international trade press. Arabic coverage is stronger for government media, governorate pages, cabinet/ministerial releases, free-zone announcements, licensing ceremonies, and construction-contract notices.
- Common failure mode: counting a license, MoU, land usufruct agreement, or ministerial discussion as operational capacity. Preserve the exact status verb: `licensed`, `approved`, `MoU`, `land allocation`, `usufruct`, `planned`, `groundbreaking`, `under construction`, `customer-ready`, `inaugurated`, `operational`.

Primary/source examples:

- NTRA regulatory framework for establishing/operating datacenters and hosting/cloud services: https://www.tra.gov.eg/en/regulatory-framework-for-establishing-operating-data-centers-and-providing-hosting-and-cloud-computing-services/
- NTRA telecom-services licensee PDF includes a datacenter/cloud license category and names licensees such as Raya Data Center, EGIT, Cyshield, AWS, Link Data Center, E-finance, Delta Electronic Systems, GPX, and others: https://www.tra.gov.eg/wp-content/uploads/2023/10/Telecommunication-Services-Licensees.pdf
- Huawei official release says Huawei Cloud launched a **Cairo Region** in May 2024: https://www.huawei.com/en/news/2024/5/huawei-cloud-goes-live-in-egypt
- Orange Egypt official release says Orange and Huawei launched Huawei Cloud services in Egypt and ties the service to Orange's data-center/cloud operation: https://www.orange.eg/en/about/media-center/press-kit/orange-and-huawei-partnership-agreement-for-webposting-295-event
- Telecom Egypt official release for the Regional Data Hub in Smart Village / west Cairo: https://ir.te.eg/en/CorporateNews/PressRelease/132/Telecom-Egypt-is-building-Egypt-s-largest-international-data-center
- U.S. International Trade Administration market note gives current market framing, submarine-cable context, and growth estimates: https://www.trade.gov/market-intelligence/egypt-data-centers

---

## 1. Highest-value primary sources

### 1.1 NTRA license and regulatory framework (Grade A)

- **National Telecom Regulatory Authority (NTRA)**: https://www.tra.gov.eg/
- Datacenter/cloud regulatory framework: https://www.tra.gov.eg/en/regulatory-framework-for-establishing-operating-data-centers-and-providing-hosting-and-cloud-computing-services/
- NTRA framework announcement: https://www.tra.gov.eg/en/ntra-approves-a-regulatory-framework-to-establish-data-centers-in-egypts-market/
- Telecom-services licensees PDF: https://www.tra.gov.eg/wp-content/uploads/2023/10/Telecommunication-Services-Licensees.pdf

Use:

- NTRA is the backbone for operator/license enumeration. The licensee PDF names companies under categories such as `Establishing, operating and Provisioning of data center and cloud computing services`, `Provisioning of cloud computing services`, and `Establishing, Operating Data Centers for Provisioning of Collocation Services`.
- The PDF is company-level or service-level evidence, not always facility-level evidence. Pivot every licensee name into official pages, trade press, directories, and Arabic searches to locate facilities.
- Re-check NTRA press releases for new licenses. In 2026, trade press and MCIT/NTRA social channels reported a Hassan Allam Digital Infrastructure / A15 data-center and cloud-services license; verify through NTRA/MCIT primary pages when public HTML/PDF is available.

NTRA query patterns:

```text
site:tra.gov.eg "data center" "cloud computing services" Egypt license
site:tra.gov.eg "Establishing, operating" "data center" "cloud"
site:tra.gov.eg "Telecommunication Services Licensees" "Raya Data Center"
site:tra.gov.eg "GPX" "Collocation Services"
site:tra.gov.eg "Amazon Web Services" "cloud computing services"
site:tra.gov.eg "Hassan Allam" "data center" "license"
site:mcit.gov.eg "data center" "cloud services license"
site:mcit.gov.eg "Hassan Allam" "A15" "data center"
site:tra.gov.eg "مراكز البيانات" "الحوسبة السحابية" "ترخيص"
site:tra.gov.eg "مركز بيانات" "تراخيص"
```

### 1.2 MCIT, ITIDA, Egypt official media, and investment authorities (Grade A/B)

| Source | URL / search route | Use | Grade |
|---|---|---|---|
| MCIT | https://mcit.gov.eg/ | Ministry releases, digital-infrastructure policy, cloud strategy, government-cloud and NTRA license ceremonies. | A |
| ITIDA | https://itida.gov.eg/ | Investor touchpoint for ICT/offshoring; useful for Maadi Technology Park, Smart Village, new-city tech zones, and investor promotion. | A/B |
| State Information Service (SIS) | https://sis.gov.eg/ | Official presidential/prime-minister/government announcements, including Government Data and Cloud Computing Center and governorate smart-service projects. | A |
| Cabinet / Egyptian Government Portal | https://www.cabinet.gov.eg/ | Cabinet meeting statements, land usufruct and SCZONE approvals, national digital projects. | A |
| General Authority for Investment and Free Zones (GAFI) | https://www.gafi.gov.eg/ | Free-zone/investor setup and investment announcements; useful for Port Said and special economic zones. | A/B |
| Suez Canal Economic Zone (SCZONE) | https://sczone.eg/ | Sokhna / East Port Said industrial-zone projects such as Kemet Data Center. | A/B |
| New Urban Communities Authority (NUCA) / new-city authorities | https://www.newcities.gov.eg/ | New Administrative Capital, New Alamein, 6th October, New Cairo and other new-city land/infrastructure leads. | A/B |

Official query patterns:

```text
site:mcit.gov.eg Egypt "data center" OR "data centre" "cloud"
site:mcit.gov.eg "مركز بيانات" OR "مراكز البيانات" "الحوسبة السحابية"
site:itida.gov.eg "data center" "Maadi Technology Park"
site:sis.gov.eg "Government Data and Cloud Computing Center"
site:sis.gov.eg "data center" "governorate"
site:cabinet.gov.eg "data center" "SCZONE" OR "Sokhna" OR "usufruct"
site:sczone.eg "data center" OR "data centre" "Sokhna"
site:sczone.eg "مركز بيانات" "السخنة"
site:gafi.gov.eg "data center" "free zone"
site:newcities.gov.eg "data center" "New Administrative Capital"
```

### 1.3 Contractor and engineering project pages (Grade A/B)

Egyptian datacenter projects often surface through EPC/MEP/consultant pages before operator facility pages. Use these for rack counts, sqm, status, and location, but verify whether a contractor page is current.

Examples:

- Orascom Construction says it is building two datacenters in the New Administrative Capital, including a Tier 3 38k sqm project and 133-rack / 1,088-rack datacenters: https://orascom.com/projects/data-centers-at-the-new-administrative-capital/
- ECG project pages have been useful for Telecom Egypt RDH2 evidence and IT load/rack counts: https://www.ecgsa.com/
- Redcon Group is tied to GPX Cairo expansion reporting; search official Redcon and GPX pages together.
- Raya Network Services / Raya IT appears as contractor/implementer for Telecom Egypt RDH phases and as Raya Data Center's parent ecosystem.

Queries:

```text
site:orascom.com "data center" "Egypt"
site:ecgsa.com "data center" "Telecom Egypt" OR "RDH2"
site:redconcon.com "GPX" "data center" Cairo
site:raya-it.net "data center" "Telecom Egypt"
"{contractor}" "data center" "New Administrative Capital"
"{contractor}" "مركز بيانات" "العاصمة الإدارية"
```

---

## 2. Egyptian colo / cloud / datacenter operator seed list

Operator pages are **A for claimed presence** and **B for capacity** unless supported by formal filings, detailed project pages, or audited disclosures. Directories are useful for aliases and addresses, but grade them **C** unless corroborated.

| Operator / developer | Primary URLs | Egypt location signals | Grade guidance |
|---|---|---|---|
| **Telecom Egypt / Regional Data Hub (RDH)** | https://ir.te.eg/ ; https://www.te.eg/ | Smart Village / west Cairo / 6th of October / Giza; RDH phase 1 launched 2021 and RDH2/Smart Village expansion. Strong cable-landing and international gateway angle. | Official releases **A**; directories for exact building aliases **C**. |
| **Raya Data Center / Raya IT** | https://www.rayadatacenter.com/ ; https://raya-it.net/solution-data-center/ ; https://rayacorp.com/ | Official Raya IT page says three Egypt locations: 6th of October, Maadi, New Cairo. Raya Holding announced Africa50 investment for a new Tier III facility, construction slated early 2025. | Operator/listed-company release **A**; Datacenters.com/DataCenterMap **C** for address leads. |
| **GPX Global Systems** | https://gpxglobal.net/ | Cairo 1 and Cairo 2 / New Cairo. Official GPX release and DCD report a Cairo 2 expansion adding 12MW, 9,000 sqm, and 1,800 racks. | GPX official **A**; DCD **B**; directory addresses **C**. |
| **Orange Egypt / Orange Business** | https://www.orange.eg/ ; https://www.orange-business.com/ | Orange Business Cloud hosted in Egypt; Orange/Huawei Cloud partnership; Orange data-center role in New Administrative Capital and Grifols Egypt project. | Orange official **A** for services/partnership; facility specs often **B/C** unless contractor/customer page confirms. |
| **Huawei Cloud** | https://www.huawei.com/ ; https://www.huaweicloud.com/ | Huawei Cloud Cairo Region launched May 2024; Orange is local services partner. SIS later reported Huawei Cloud Summit Northern Africa 2025 and a new AZ planned for 2026. | Official cloud region **A**; physical facility inference requires Orange/operator evidence. |
| **Link Data Center (LDC)** | https://www.linkdatacenter.net/en/ | NTRA licensee for cloud services; Maadi/Hadayek El Maadi directory leads. Search Arabic/English under `Link Datacenter`, `LINK Development`, and `LDC`. | NTRA/operator **A/B**; directory locations **C**. |
| **e-finance / e-finance Investment Group** | https://www.efinanceinvestment.com/ | NTRA cloud-services licensee; government digital-payment/sovereign workload ecosystem. May have private/government datacenter assets rather than open colo. | NTRA **A**; facility evidence must be verified. |
| **Cyshield** | https://cyshield.com/ | NTRA datacenter/cloud licensee; cybersecurity/cloud platform angle. | NTRA **A**; facility-level unknown until official page/press. |
| **EGIT / Egyptian Group for Integrated Technology** | https://eg4it.com/ | NTRA datacenter/cloud licensee. | NTRA **A**; verify facility before counting. |
| **ECC Solutions** | Search official ECC / directories | Directory evidence around 6th October / Cairo; market reports list ECC Solutions as a local colo investor. | Often **C** unless official source found. |
| **e& Egypt / Etisalat Misr** | https://www.etisalat.eg/ ; e& official pages | Smart Village / Giza and telecom cloud/enterprise facilities; appears in market-report snippets and directories. | Operator/NTRA **A/B**; directory **C**. |
| **Benya Group / Khazna Data Centers** | https://www.benya.com/ ; https://khaznadatacenters.com/ | Khazna-Benya hyperscale facility at Maadi Technology Park; Khazna official release announced USD 250m Egypt entry. | Operator press **A/B**; planned until construction/commissioning proof. |
| **Hassan Allam Digital Infrastructure / A15** | https://www.hassanallam.com/ ; A15 official/trade press | NTRA license reported for a major datacenter/cloud project in 2026; exact governorate and facility details need primary confirmation. | License ceremony **A if NTRA/MCIT**; trade-only details **B**. |
| **INTRO Technology / Intro Group / Oman Data Park / Kemet Data Center** | https://introholding.com/ ; SCZONE/cabinet/BusinessWire/EnterpriseAM | Planned Kemet Data Center in Sokhna Industrial Zone / SCZONE, reported as 80MW in four phases. | SCZONE/cabinet land agreement **A/B**; BusinessWire/company MoU **B**. |
| **Income Egypt / IGI Group** | Search `Income Egypt`, `IGI Group`, `Borg El Arab data center` | Planned Borg El Arab / Alexandria hyperscale campus, trade press reports 100MW initial power and potential later expansion. | Trade press **B** until official operator/utility/permit source. |
| **Renergy Group** | Search official Renergy + Egypt Oil & Gas/DCD | Planned green/hyperscale datacenter around El Tor / South Sinai integrated with renewables/green-hydrogen proposals. | Mostly **B/C** until land/permit/NTRA proof. |
| **Telecom Egypt edge/exchange sites** | Telecom Egypt pages, DT-Holding fire-suppression project page, Datacenters.com/Inflect | October 1/2, Ramses/Manti, Sohag East, West Qena and other protected telecom datacenters appear in directories/contractor pages. | Treat as **C/B** telco/edge leads unless Telecom Egypt source confirms. |

Operator query patterns:

```text
"{operator}" Egypt ("data center" OR "data centre" OR datacenter OR colocation OR "cloud services")
"{operator}" Cairo ("MW" OR "IT load" OR racks OR "Tier III" OR "Rated-4")
"{operator}" "New Cairo" "data center"
"{operator}" "Maadi" "data center"
"{operator}" "6th of October" OR "Smart Village" "data center"
"{operator}" "New Administrative Capital" "data center"
"{operator}" "NTRA" "cloud computing services"
"{operator}" "Uptime Institute" Egypt
"{operator}" "مركز بيانات" "مصر"
"{operator}" "مراكز البيانات" "القاهرة"
```

---

## 3. Cloud-region and public-cloud evidence

Use official cloud pages for region existence and provider language. Do **not** infer a physical facility address from a cloud region unless a local operator, permit, contractor, or government source identifies a site.

| Provider | Official URL | Egypt signal |
|---|---|---|
| **Huawei Cloud** | https://www.huawei.com/en/news/2024/5/huawei-cloud-goes-live-in-egypt ; https://www.huaweicloud.com/intl/en-us/news/20240523155312706.html | Cairo Region went live in May 2024; official Huawei release says it is the first public cloud in Egypt / Northern Africa and had 93 AZs in 33 regions at launch. |
| **Orange + Huawei** | https://www.orange.eg/en/about/media-center/press-kit/orange-and-huawei-partnership-agreement-for-webposting-295-event | Orange Egypt official release says Huawei Cloud services launch in Egypt, Orange will provide and operate integrated cloud/data-center services, and data sovereignty is a driver. |
| **AWS** | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; https://aws.amazon.com/local/africa/ | Official AWS global region table shows Africa/Middle East regions but no Egypt public region in the checked table; NTRA licensee PDF lists AWS under cloud-service provisioning, which is service/license evidence, not a local AWS region. |
| **Microsoft Azure** | https://learn.microsoft.com/en-us/azure/reliability/regions-list ; https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | Official Azure region list/geographies should be checked for Egypt; do not treat Cairo Front Door/edge POPs as Azure regions. Azure Front Door edge docs list Cairo POPs, which are edge presence only. |
| **Google Cloud** | https://cloud.google.com/about/locations ; https://docs.cloud.google.com/compute/docs/regions-zones | Official Google Cloud locations/Compute Engine regions should be checked; no Egypt public Compute Engine region in the checked list. |
| **Oracle Cloud** | https://www.oracle.com/cloud/public-cloud-regions/ ; https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | Official OCI public-region list should be checked; no Egypt public OCI region in the checked list. |

Cloud-to-facility pivot queries:

```text
"Huawei Cloud" "Cairo Region" "data center" Orange Egypt
"Huawei Cloud" "Egypt" "availability zone" "2026"
"Orange Egypt" "Huawei Cloud" "data center" "New Administrative Capital"
"AWS" Egypt "NTRA" "cloud computing services" "license"
"AWS" Egypt "data center" -jobs -training
"Azure" Egypt "data center" "region" -Front -POP
"Azure Front Door" Cairo Egypt POP "not region"
"Google Cloud" Egypt "region" Cairo -jobs
"Oracle Cloud" Egypt "Cairo Region" -jobs
```

---

## 4. Trade press and market sources

Use trade press to discover project names, phases, MW claims, timelines, and local partners; then verify through NTRA, operator, government, utility, contractor, or land/permit sources.

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/ | Best English project feed for Telecom Egypt, GPX, Khazna-Benya, Orange/Huawei, government cloud center, Income Borg El Arab, Renergy, and Egypt market updates. | B |
| W.Media | https://w.media/ | Regional DC trade press; useful for Telecom Egypt business carve-out, RDH utilization/phase context, market strategy. | B |
| Capacity Media / Total Telecom / Developing Telecoms / Telecom Review / Mobile Europe / Connecting Africa | site-scoped searches | Strong for telecom/cloud/operator announcements and NTRA license news. | B |
| EnterpriseAM / Zawya / BusinessWire / Ahram Online / Daily News Egypt / Egypt Today | site-scoped searches | Good for cabinet, SCZONE, investment, MoU, and land-agreement coverage. Often syndicates official statements; verify project stage. | B/C |
| U.S. International Trade Administration | https://www.trade.gov/market-intelligence/egypt-data-centers | Market framing, cable count, competition, and U.S. exporter context. | A-/B+ |
| Uptime Institute certifications | https://uptimeinstitute.com/ | Facility certification search for Tier/Rated claims; use certificate name/location as high-grade evidence. | A for certification only |
| Directories: DataCenterMap, Datacenters.com, Baxtel, Inflect, Cloudscene, PeeringDB, Ocolo, ColoMap | site-specific searches | Useful for aliases, addresses, network ecosystem, and legacy telco/edge sites. Must be cross-checked before final record. | C |

Trade-press queries:

```text
site:datacenterdynamics.com/en/news Egypt "data center" Cairo GPX Telecom Egypt Khazna
site:datacenterdynamics.com/en/news Egypt "MW" "data center"
site:w.media Egypt "data center" "Telecom Egypt" OR "Regional Data Hub"
site:capacitymedia.com Egypt "data centre" "Telecom Egypt" OR "submarine cable"
site:developingtelecoms.com Egypt "data centre" "NTRA" OR "license"
site:mobileeurope.co.uk Egypt "data centre" Huawei OR Khazna
site:enterprise.news Egypt "data center" SCZONE OR Sokhna OR Kemet
site:zawya.com Egypt "data center" "Suez Canal Economic Zone"
site:businesswire.com Egypt "Kemet Data Center" "Oman Data Park"
site:trade.gov "Egypt Data Centers"
```

Status verbs to capture:

- English: `approves`, `licenses`, `signs`, `MoU`, `usufruct`, `land allocation`, `invests`, `breaks ground`, `expands`, `customer-ready`, `completed`, `inaugurated`, `launched`, `operational`.
- Arabic: `وافق`, `منح ترخيص`, `وقع`, `مذكرة تفاهم`, `حق انتفاع`, `تخصيص أرض`, `استثمار`, `بدء الإنشاء`, `توسعة`, `جاهز للعملاء`, `اكتمل`, `افتتاح`, `تدشين`, `تشغيل`.

---

## 5. English and Arabic search vocabulary

### 5.1 English terms

```text
"Egypt" ("data center" OR "data centre" OR datacenter OR datacentre) "{governorate}"
"{governorate}" ("data center" OR "data centre") ("MW" OR "MVA" OR "IT load" OR racks OR sqm)
"{city}" ("colocation" OR "cloud services" OR "hosting" OR "Tier III" OR "Rated-4")
"{city}" ("hyperscale" OR "AI data center" OR "green data center" OR "sovereign cloud")
"{industrial zone}" ("data center" OR "cloud region" OR "digital infrastructure")
"{operator}" "{governorate}" ("NTRA" OR "license" OR "cloud computing services")
"{operator}" "{city}" ("Uptime" OR "Tier III" OR "Rated-3" OR "Rated-4")
```

Named-place expansion:

```text
"Smart Village" "data center" "Telecom Egypt" OR Raya OR Etisalat
"6th of October" "data center" Raya OR "Telecom Egypt" OR ECC
"Maadi Technology Park" "data center" Khazna OR Benya OR Raya
"New Cairo" "data center" GPX OR Raya OR EGID
"New Administrative Capital" "data center" Orange OR Orascom OR Grifols
"Ain Sokhna" "Government Data and Cloud Computing Center"
"Sokhna Industrial Zone" "Kemet Data Center"
"Suez Canal Economic Zone" "data center"
"Borg El Arab" "data center" Income OR IGI
"Mansoura" "EgyptNetwork" "data center"
"Port Said Free Zone" "data center" WAVZ
"El Tor" "green data center" Renergy
```

### 5.2 Arabic terms

Core nouns:

- data center: `مركز بيانات`, `مركز البيانات`, `مراكز بيانات`, `مراكز البيانات`
- cloud computing: `الحوسبة السحابية`, `خدمات سحابية`, `خدمات الحوسبة السحابية`
- colocation / hosting: `استضافة`, `استضافة مشتركة`, `خدمات الاستضافة`
- hyperscale: `فائق النطاق`, `مركز بيانات فائق`, `هايبر سكيل`
- AI datacenter: `مركز بيانات للذكاء الاصطناعي`, `مركز ذكاء اصطناعي`
- digital infrastructure: `البنية التحتية الرقمية`, `البنية الرقمية`
- license: `ترخيص`, `رخصة`, `اعتماد`
- building permit: `رخصة بناء`, `تصريح بناء`
- land allocation / usufruct: `تخصيص أرض`, `حق انتفاع`
- power: `قدرة كهربائية`, `ميغاواط`, `ميجاواط`
- launch/opening: `افتتاح`, `تدشين`, `إطلاق`, `تشغيل`
- construction/expansion: `إنشاء`, `بناء`, `بدء الأعمال`, `توسعة`

Arabic templates:

```text
"مصر" "مركز بيانات" "الحوسبة السحابية"
"{governorate_ar}" "مركز بيانات" "ميغاواط"
"{city_ar}" "مركز بيانات" "ترخيص"
"{city_ar}" "مراكز البيانات" "رخصة بناء"
"{industrial_zone_ar}" "مركز بيانات" "حق انتفاع"
"{operator_ar}" "مركز بيانات" "مصر"
"الجهاز القومي لتنظيم الاتصالات" "مركز بيانات" "ترخيص"
"وزارة الاتصالات" "مركز بيانات" "مصر"
"المنطقة الاقتصادية لقناة السويس" "مركز بيانات"
"العاصمة الإدارية الجديدة" "مركز بيانات"
"مدينة السادات" "مركز بيانات"
```

---

## 6. Governorate-by-governorate enumeration approach

Use these as copy-paste starting points. For every governorate, search English name, common city anchors, and Arabic governorate name. The right source varies by location: Greater Cairo needs operator/NTRA/directories; SCZONE/coastal governorates need economic-zone and cable queries; Upper Egypt mostly needs telco-edge and negative searches.

| Governorate | Arabic / city anchors | Enumeration route |
|---|---|---|
| **Cairo** | `القاهرة`, Maadi, New Cairo, New Administrative Capital, Maadi Technology Park | Highest priority. Search GPX, Raya Maadi/New Cairo, Khazna-Benya Maadi, Orange/NAC, Orascom NAC, EGID, Link Data Center, NTRA licensees, Cairo ICT press. |
| **Giza** | `الجيزة`, 6th of October, Smart Village, Sheikh Zayed | Highest priority. Search Telecom Egypt RDH/Smart Village, Raya 6th October, Etisalat/e& Smart Village, ECC Solutions, October 1/2 telco sites, Uptime/directories. |
| **Alexandria** | `الإسكندرية`, Borg El Arab, برج العرب | Search Income/IGI Borg El Arab, utility/power allocation, Borg El Arab industrial zone, Alexandria cable/telecom facilities, Arab Academy/enterprise datacenters. |
| **Suez** | `السويس`, Ain Sokhna, Sokhna Industrial Zone, SCZONE, `السخنة` | Search Government Data and Cloud Computing Center, Kemet Data Center, SCZONE land agreements, cabinet releases, Intro/Oman Data Park, Suez cable/logistics corridor. |
| **Port Said** | `بورسعيد`, East Port Said, West Port Said Free Zone | Search free-zone digital-infrastructure projects, WAVZ, GAFI, SCZONE East Port Said, port/cable/telecom edge. |
| **Dakahlia** | `الدقهلية`, Mansoura, `المنصورة` | Search EgyptNetwork Mansoura, local ISP/hosting, Telecom Egypt exchange/data rooms, directories for operational small colo. |
| **Qalyubia** | `القليوبية`, Shubra Al Khayma, Manti, Banha | Search Telecom Egypt Manti/Ramses exchange aliases, CAIX/Inflect, telco edge. Verify address because Cairo/Qalyubia boundary aliases are common. |
| **Sohag** | `سوهاج`, Gerga, `جرجا` | Search Telecom Egypt Sohag East and Qareeb Gerga leads; likely edge/telco more than hyperscale. |
| **Qena** | `قنا` | Search Telecom Egypt West Qena contractor/directory leads; mostly edge/telco negative search. |
| **South Sinai** | `جنوب سيناء`, El Tor, Sharm El Sheikh, `الطور`, `شرم الشيخ` | Search Renergy green/hyperscale datacenter, green-hydrogen/renewable projects, tourism/government continuity facilities. |
| **Matrouh** | `مطروح`, Marsa Matrouh, New Alamein, `العلمين الجديدة` | Search SIS/cabinet smart government services complex, New Alamein smart-city infrastructure, coastal cable/telco edge. |
| **Red Sea** | `البحر الأحمر`, Hurghada, Safaga, Ras Ghareb | Search tourism smart-city/renewables, cable/telecom edge, green-energy datacenter proposals; likely negative unless project-specific. |
| **Ismailia** | `الإسماعيلية`, East Ismailia, Suez Canal corridor | Search SCZONE/canal corridor, Telecom Egypt exchanges, government continuity. Avoid double-counting Suez/Port Said SCZONE projects. |
| **Damietta** | `دمياط`, New Damietta | Search port/free-zone digital infrastructure and Telecom Egypt edge; likely negative. |
| **Beheira** | `البحيرة`, Nubaria, Wadi El Natrun, Damanhour | Search industrial/agro zones and cable route proximity; likely negative. |
| **Beni Suef** | `بني سويف` | Search technology park/university/government datacenter; likely negative. |
| **Asyut** | `أسيوط` | Search Assiut tech park/university/Telecom Egypt edge; likely negative. |
| **Aswan** | `أسوان` | Search government/university/tourism and renewable-energy datacenter; likely negative. |
| **Faiyum** | `الفيوم` | Search local government digital-infrastructure only; likely negative. |
| **Gharbia** | `الغربية`, Tanta, `طنطا` | Search local ISP/hosting/telco edge; likely negative. |
| **Kafr el-Sheikh** | `كفر الشيخ` | Search local government/university/telco edge; likely negative. |
| **Luxor** | `الأقصر` | Search tourism/government continuity/Telecom Egypt edge; likely negative. |
| **Minya** | `المنيا` | Search university/government/telco edge; likely negative. |
| **Monufia** | `المنوفية`, Sadat City, `مدينة السادات` | Search Sadat industrial city, local ISP, government datacenter; likely negative but industrial-city search is worthwhile. |
| **Al Sharqia** | `الشرقية`, 10th of Ramadan, `العاشر من رمضان`, Zagazig | Search 10th of Ramadan industrial zone, cloud/colo investors, telco edge; likely negative but industrial searches matter. |
| **North Sinai** | `شمال سيناء`, Arish, `العريش` | Search government/security/telecom edge only; hyperscale unlikely. |
| **New Valley** | `الوادي الجديد`, Kharga, `الخارجة` | Search renewables/desert-land AI datacenter proposals; otherwise negative. |

Per-governorate template:

```text
"{governorate}" Egypt ("data center" OR "data centre" OR datacenter OR colocation OR "cloud computing")
"{governorate}" Egypt ("MW" OR "racks" OR "Tier III" OR "Uptime") "data center"
"{city}" Egypt ("data center" OR "cloud services") "{operator}"
site:tra.gov.eg "{operator}" "{governorate}" "data center"
site:mcit.gov.eg "{governorate}" "data center"
site:sis.gov.eg "{governorate}" "data center"
site:cabinet.gov.eg "{governorate}" "data center"
"{governorate_ar}" "مركز بيانات" "مصر"
"{city_ar}" "مركز بيانات" "ميغاواط" OR "ترخيص" OR "رخصة بناء"
```

Industrial-zone template:

```text
"{industrial_zone}" Egypt ("data center" OR "cloud" OR "digital infrastructure")
"{industrial_zone}" Egypt ("land" OR "usufruct" OR "power" OR "MW") "data center"
"{industrial_zone_ar}" "مركز بيانات" "حق انتفاع" OR "تخصيص أرض"
```

---

## 7. Verification and grading rules

### 7.1 Evidence hierarchy

1. **A - Primary/legal/facility evidence**: NTRA license/framework pages; MCIT/SIS/cabinet/SCZONE releases; operator official facility pages; official cloud-region pages; contractor project pages with scope/location; Uptime Institute certificates; utility/land/permit records if found.
2. **B - Strong secondary evidence**: DCD, W.Media, Capacity Media, Developing Telecoms, Mobile Europe, EnterpriseAM, Zawya, BusinessWire/company PR distribution, development-bank/investor announcements.
3. **C - Lead-only evidence**: DataCenterMap, Datacenters.com, Baxtel, Inflect, Cloudscene, PeeringDB, Ocolo, ColoMap, LinkedIn/Facebook/X posts, market-report snippets, vendor partner pages without facility details.

Grade each data point, not just each project. Example: Huawei Cloud Cairo Region existence is **A** from Huawei; its exact physical host facility is **unknown/C** unless Orange/operator/permit evidence identifies it.

### 7.2 Status verification recipe

- Count **operational** only when official operator/government/cloud launch/customer-ready evidence exists.
- Count **construction** when contractor, operator, or official project pages show construction/expansion work, EPC award, or site work. A MoU alone is not construction.
- Count **planned/approved** for licenses, MoUs, land-usufruct agreements, power allocations, and investment announcements without construction evidence.
- For capacity, distinguish `IT load`, `total power`, `utility allocation`, `future campus capacity`, `phase capacity`, `rack count`, and `sqm`. Do not convert racks to MW unless the source provides kW/rack or total IT load.
- For Greater Cairo aliases, check whether the same facility is being described as Cairo, Giza, 6th of October, Smart Village, New Cairo, or Maadi. Store a normalized campus name and a location note.
- For New Administrative Capital, be careful with governorate assignment. Many sources say "Cairo" commercially, but administrative boundaries and project context may differ. Preserve source wording and assign only after checking the manifest's division convention.
- For government datacenters and ministry/cloud centers, mark facility type clearly as `government/sovereign`, not commercial colo, unless commercial services are explicitly offered.

### 7.3 Anti-false-positive checks

- `Cairo POP`, CDN node, internet exchange, cloud on-ramp, or Azure Front Door edge location is not a cloud region or full datacenter record by itself.
- `NTRA cloud-service license` is not facility evidence unless paired with a location.
- `Orange Business Cloud`, `Huawei Cloud services`, or `AWS service availability` may mean services sold in Egypt; verify whether infrastructure is physically local.
- Directory-only Telecom Egypt exchange sites are useful leads but should not be assigned MW or Tier without primary/contractor evidence.
- Egyptian Arabic/English pages often translate `data center`, `information center`, and `digital center` inconsistently. Reject generic government IT rooms unless the source shows datacenter infrastructure, racks, cloud/hosting, or critical-facility scope.

---

## 8. Recommended discovery pipeline

1. **License seed**: extract all NTRA datacenter/cloud licensees from the latest `Telecommunication Services Licensees` PDF and NTRA press releases. Normalize company names in English and Arabic.
2. **Greater Cairo operator sweep**: Telecom Egypt RDH, Raya, GPX, Orange/Huawei, Link Data Center, EGID, ECC, e&/Etisalat, Cyshield, e-finance, Benya/Khazna, Hassan Allam/A15. Search official pages first, then DCD/W.Media/directories.
3. **Cloud-region check**: verify Huawei Cloud Cairo Region and re-check official AWS/Azure/GCP/OCI region lists. Record edge POPs separately.
4. **Special-zone and new-city sweep**: SCZONE/Sokhna/Kemet, New Administrative Capital/Orascom/Orange/Grifols, Maadi Technology Park/Khazna-Benya, Smart Village/Telecom Egypt, Borg El Arab/Income, Port Said Free Zone/WAVZ.
5. **Governorate sweep**: run the per-governorate templates in Section 6. Expect Cairo/Giza/Suez/Alexandria/Port Said/Dakahlia/Qalyubia/Sohag/Qena/South Sinai/Matrouh to produce the strongest leads; document negative searches for the rest.
6. **Directory reconciliation**: use DataCenterMap, Datacenters.com, Baxtel, Inflect, PeeringDB, and Cloudscene to find aliases and network facilities, then promote records only when primary or strong secondary evidence exists.
7. **Final verification**: dedupe by `(ultimate operator, campus/name, city/governorate, phase)`, assign lifecycle status from verbs, and grade every source URL.

Pitfalls recap: Greater Cairo boundary aliases; license/service evidence without a facility; edge POPs misread as cloud regions; MoUs counted as operational; future campus MW counted as built; government IT centers mixed with commercial colo; Arabic `مركز معلومات` pages that are ordinary information offices, not datacenters.
