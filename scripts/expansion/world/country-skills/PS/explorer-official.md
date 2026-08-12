# PS Explorer Official - Palestine Datacenter Enumeration

Date: 2026-08-12. Country: **PS Palestine, State of**. Division model: **16 governorates** from `world-manifest.jsonl`: `Bethlehem`, `Deir El Balah`, `Gaza`, `Hebron`, `Jerusalem`, `Jenin`, `Jericho and Al Aghwar`, `Khan Yunis`, `Nablus`, `North Gaza`, `Qalqilya`, `Ramallah`, `Rafah`, `Salfit`, `Tubas`, `Tulkarm`. Angle: **official / regulatory / government-data-center / procurement / listed-operator / energy evidence**.

Reliability grades:
- **A** = primary source: MTDE/PA ministry, WAFA official news agency for government/operator statements, Shiraa public-procurement portal, World Bank/UN/EU project or damage report, PCBS, PEX filing/annual report, Uptime Institute certification, operator official page that names a facility or service.
- **B** = strong corroboration: DCD, Bloomberg/Data Center Knowledge, Telecompaper, Al Jazeera/NYT/Reuters/Access Now/7amleh when citing named operators or published assessments, industry association material.
- **C** = lead only: DataCenterMap, Inflect, Data Center Platform, Datacenter Catalog, broker pages, LinkedIn/social posts, marketing pages that mention cloud/hosting without a physical site, tender mirrors that do not expose the original buyer notice.

Use **A/B/C** in notes, but do not allow a C-only source to create an operational facility unless the output format explicitly supports low-confidence leads.

---

## 0. Palestine-specific facts

- **No hyperscale public-cloud region is in Palestine.** Official AWS, Google Cloud, Microsoft Azure, and Oracle region lists have no Palestine region. Nearby Israeli regions (`AWS il-central-1`, `Google me-west1`, `Azure Israel Central`, `Oracle il-jerusalem-1`) must not be mapped to PS governorates.
- **Known physical facility universe is small.** Verified routes point to Paltel data centers in **Nablus** and **Al-Bireh/Ramallah**, the MTIT/MTDE Government Computer Center / National Data Center in **Ramallah**, and small enterprise/operator/server-room leads. Gaza has historical Paltel main data centers/switches, but current status is damage/recovery, not normal operation.
- **The strongest private facility evidence is Paltel.** Paltel's own Arabic announcement says the Al-Bireh/Ramallah facility was being built after an earlier Paltel data center at the company's general-management headquarters in **Nablus**. DCD and Bloomberg/DCK later reported the 2019 Ramallah/Al-Bireh launch as Paltel Group's second data center: about 65,000 sq ft / 6,000 sq m, Uptime Tier III Design certified, around USD 10 million.
- **The strongest government facility evidence is the MTIT/MTDE Government Computer Center / NDC.** World Bank material says a centralized government data and IT center was created at MTIT, but lacked a disaster recovery site. The current MTDE/NDC page describes collocation, DR-site hosting, government private cloud, DCIM monitoring, PalCERT monitoring, 17 hosted government institutions, 270 virtual servers, and 109 hosted government websites.
- **Gaza must be status-checked every time.** WAFA reported on 2023-11-16 that Paltel's main data centers and switches in Gaza were shutting down from fuel depletion. 7amleh reported in 2024 that 75% of Gaza telecom infrastructure was damaged and at least 50% destroyed, based on Paltel/Ooredoo assessments published by MTDE. PCBS/MTDE/TRA reported in May 2026 that urgent 2025 interventions kept parts of Gaza connected, but this does not prove any Gaza data center is fully operational.
- **No central planning-permit registry exists.** West Bank building permits are municipal; Gaza permitting is not a reliable web route. Enumeration should pivot from official/operator announcements and procurement to municipalities only after a candidate site is identified.
- **Power is a gating fact.** West Bank facilities depend on imported electricity distributed by local utilities and backup systems; Gaza sites rely on constrained fuel, batteries, solar, and repairs. Do not infer MW scale.

Arabic lifecycle vocabulary:

```text
مركز بيانات / مركز البيانات / مراكز البيانات
مركز المعلومات / مركز الحاسوب الحكومي
استضافة / استضافة الخوادم / استضافة المواقع
الحوسبة السحابية / السحابة الخاصة
التعافي من الكوارث / موقع احتياطي / DR site
الخدمات الإلكترونية / الحكومة الإلكترونية / التحول الرقمي
عطاء / مناقصة / دعوة لتقديم عطاءات
خوادم / معدات / أرشفة / أمن معلومات
ترخيص / رخصة / إذن بناء
افتتاح / إطلاق / تدشين / توقيع / تنفيذ
تدمير / تضرر / انقطاع / إعادة إعمار
```

---

## 1. Official query templates

Core bilingual searches:

```text
"فلسطين" "مركز بيانات"
"مركز البيانات الوطني" فلسطين
"مركز الحاسوب الحكومي" فلسطين
"مركز البيانات" "رام الله" OR "البيرة"
"مركز البيانات" "نابلس" "بالتل"
"بالتل" "مركز البيانات" "Tier-3" OR "Uptime"
"بالتل" "استضافة الخوادم" OR "الحوسبة السحابية"
"غزة" "مراكز البيانات" "بالتل" OR "انقطاع"
"مناقصة" "مركز بيانات" فلسطين
"عطاء" "مركز بيانات" OR "خوادم" OR "أرشفة"
"Palestine" "data center" Paltel Ramallah Al-Bireh
"Palestinian Digital Economy Assessment" "data center" MTIT
"Digital West Bank and Gaza" "data infrastructure" "cloud"
```

Official-site scoped searches:

```text
site:mtde.gov.ps "data center" OR "data infrastructure" OR "cloud"
site:mtde.gov.ps "مركز بيانات" OR "الحوسبة السحابية" OR "استضافة"
site:mtde.online "مركز البيانات الوطني" OR "PalCERT"
site:wafa.ps "مركز البيانات" OR "بالتل" OR "التحول الرقمي"
site:english.wafa.ps "Paltel" "data centers" OR "Digital West Bank"
site:shiraa.gov.ps "مركز بيانات" OR "data center" OR "خوادم"
site:pex.ps PALTEL "Annual Report"
site:paltelgroup.ps "مركز البيانات" OR "data center" OR "Uptime"
site:pcbs.gov.ps "telecommunications" "Gaza" "2026"
```

---

## 2. Grade A official routes

### 2.1 MTDE / MTIT

- **Ministry of Telecommunications and Digital Economy (MTDE)**: https://mtde.gov.ps/ . Grade A. Formerly MTIT; official route for telecom policy, digital economy, PA digital transformation, project procurement, and the future Telecommunications Regulatory Authority.
- **Digital West Bank & Gaza Project (DWBG)**: https://mtde.gov.ps/home/ads/23032?culture=en-US . Grade A. The MTDE page states the IDA-funded USD 20 million project includes: legal/regulatory environment, a Palestinian Telecommunications Regulatory Authority, root Certificate Authority, QoS platform, emergency-response/recovery infrastructure, whole-of-government digital-transformation strategy, **data infrastructure**, a digital public platform, e-services, and e-GP.
- **Unified Data Hosting / Cloud Hosting Strategy EOI**: https://mtde.gov.ps/home/ads/23047?culture=ar-SA . Grade A. This 2025 MTDE procurement notice is high-signal: Cloud Center of Excellence, Cloud-First Policy, cloud readiness, data-hosting infrastructure assessment, existing data centers/cloud providers/hosting capacity, and public-private partnerships for cloud adoption and data-center investments.
- **World Bank DWBG restructuring paper**: https://documents1.worldbank.org/curated/en/099121925070028162/pdf/P174355-6255b6cc-7a74-47c6-90c7-e5d7b4e67043.pdf . Grade A. As of the restructuring, activities expected to start in early 2026 include a National Cloud Hosting and Data Center Strategy; indicators include adoption of a National Data Hosting Strategy.

Extraction rule: DWBG and strategy procurements are **pipeline evidence**, not facility evidence. Create a planned/tendered facility only if a later tender, award, or official announcement names a site, owner, and implementation scope.

### 2.2 Government Computer Center / National Data Center

- **World Bank Palestinian Digital Economy Assessment**: https://documents1.worldbank.org/curated/en/472671640152521943/pdf/Palestinian-Digital-Economy-Assessment.pdf . Grade A/B. It states a centralized government data and IT center was created at MTIT, that the Government Computer Center under MTIT is the main e-government infrastructure entity, and that MTIT planned a government-wide cloud at its Ramallah headquarters plus a disaster recovery site.
- **National Data Center page**: https://mtde.online/national-data-center/ . Grade A- (official-looking MTDE/NDC site, but on `mtde.online`; cross-check with `mtde.gov.ps`, World Bank, WAFA, or direct ministry contact for final coordinates). It confirms services for government collocation, DR-site hosting, DCIM monitoring, PalCERT monitoring, government private cloud, 17 hosted government institutions, 270 virtual servers, and 109 hosted government websites.

Enumeration handling:
- Record as **Government Computer Center / National Data Center**, owner/operator **MTDE / General Secretariat of the Council of Ministers** if supported by the source being used.
- Division: **Ramallah** unless a source gives a different public location. The World Bank places MTIT headquarters in Ramallah context; do not publish exact coordinates unless official.
- Status: **operational** for institutional government data-center service; **planned/tendered** only for new cloud/DC strategy components until award/site evidence appears.

### 2.3 PalCERT / Government SOC

- **PalCERT page**: https://mtde.online/palcert/ . Grade A- with the same domain caveat. The page identifies PalCERT as the government cyber/security operations center monitoring government systems, logs, government websites, and cooperation with OIC-CERT.
- **OIC-CERT member route**: https://www.oic-cert.org/en/ . Grade A/B for membership identity when a PalCERT/GOV-SOC listing is visible.

PalCERT is not a separate data center. Use it to corroborate government hosting/security infrastructure and to find NDC/system announcements.

### 2.4 Public procurement

- **Single Procurement Portal / Shiraa**: https://www.shiraa.gov.ps/ . Grade A. The Palestine Cabinet lists the Public Procurement Council with website `https://www.shiraa.gov.ps`; Shiraa exposes `ProcurementView` notices.
- Example high-signal search result: `https://www.shiraa.gov.ps/ProcurementView?refID=12488` surfaced an Arabic tender titled `عطاء شراء وتركيب نظام ارشفة لمركز بيانات لصالح وزارة التربية والتعليم` (purchase and installation of an archiving system for a data center for the Ministry of Education). Use the original notice, not search snippets, before creating a project.
- DWBG e-GP procurement documents also appear under Shiraa, e.g. PDFs that discuss migration from the current Shiraa portal into an e-GP platform.

Procurement search terms:

```text
site:shiraa.gov.ps "مركز بيانات"
site:shiraa.gov.ps "data center"
site:shiraa.gov.ps "خوادم" "وزارة"
site:shiraa.gov.ps "cloud" OR "الحوسبة السحابية"
site:shiraa.gov.ps "Digital West Bank" "Data Center Strategy"
"shiraa.gov.ps" "مركز بيانات" "دعوة لتقديم عطاءات"
```

Treat tender mirrors (`palestinetenders.com`, `globaltenders.com`, `tenderimpulse.com`, `developmentaid.org`) as C until they link to Shiraa/MTDE/World Bank source documents.

### 2.5 PEX and listed operators

- **Palestine Exchange (PEX)**: https://www.pex.ps/ . Grade A for filings.
- Paltel Group is a listed company. Search PEX and Paltel Group annual reports for `data center`, `مركز البيانات`, `Gaza`, `impairment`, `capital expenditure`, `cloud`, `business services`.
- Mubasher mirrors PEX disclosures and reported Paltel 2025 annual-report disclosure in 2026; use it only as a route to the PEX/company filing.

### 2.6 Paltel Group official sources

- **Paltel Group**: https://www.paltelgroup.ps/ ; **Paltel**: https://www.paltel.ps/ ; **Jawwal**: https://www.jawwal.ps/ . Grade A for company/operator claims.
- Paltel Arabic announcement: https://www.paltelgroup.ps/pginfo/?p=58225 . Grade A. It states the new Al-Bireh/Ramallah data-center building was under construction; confirms earlier Paltel data-center work at the company's general-management headquarters in **Nablus**; describes Tier-3 design targets, four fiber paths, three electricity paths, cooling design, and services including colocation, security management, virtual servers, IaaS/PaaS/SaaS, and storage.
- Uptime award page: https://uptimeinstitute.com/uptime-institute-awards/datacenter/paltel-data-center--albireh/1115 . Grade A for certification identity. It lists client **Palestine Telecommunications Company PLC (Paltel)** and project **Paltel Data Center - Al-Bireh**. Note: the Uptime page has a confusing location line ("Nablus West Bank") while the project name and Paltel/DCD sources point to Al-Bireh/Ramallah; preserve the caveat.
- DCD corroboration: https://www.datacenterdynamics.com/en/news/paltel-group-opens-second-palestine-data-center/ . Grade B. Confirms 2019 launch, second Paltel DC, 65,000 sq ft / 6,000 sq m, Ramallah, Uptime Tier III Design, first Uptime award in Palestine.
- Bloomberg/Data Center Knowledge: https://www.datacenterknowledge.com/cloud/palestinian-phone-company-offers-cloud-computing-from-ramallah . Grade B. Confirms USD 10 million Ramallah cloud/data-center story.

Known Paltel handling:
- **Paltel Data Center - Al-Bireh/Ramallah**: operational, division Ramallah, capacity MW unknown, area 6,000 sq m if citing DCD/Bloomberg, Tier III Design if citing Uptime/DCD.
- **Paltel first data center - Nablus HQ**: operational/historical lead. Paltel's announcement confirms a prior Paltel data-center project at the general-management headquarters in Nablus, but public capacity/current-service details remain limited. Keep confidence below the Al-Bireh site unless a current Paltel page or filing confirms specs.
- **Paltel Gaza main data centers/switches**: historical/institutional telecom infrastructure; current status must be **damaged / intermittently restored / unknown**, not normal operational, unless Paltel or an A-grade 2025-2026 source says otherwise.

### 2.7 Ooredoo Palestine

- **Ooredoo Palestine**: https://www.ooredoo.ps/ . Grade A for operator identity and service claims.
- Ooredoo Group data-center expansion and Iron Mountain partnership are regional group-level signals, not Palestine facility evidence unless Palestine is named.
- No A-grade Palestine facility page was verified in this pass. Do not create an Ooredoo Palestine data-center record from generic cloud/business-service pages.

### 2.8 PCBS, TRA, and telecom statistics

- **PCBS**: https://www.pcbs.gov.ps/ . Grade A for official statistics.
- PCBS/MTDE/TRA World Telecommunication Day release, 2026-05-17: https://www.pcbs.gov.ps/en/post-details/?postId=26011 . Grade A. It gives Gaza internet-access conditions, urgent 2025 interventions, 94 telecom-site database updates, 12 emergency points, FTTH subscriber trend, and April 2026 mobile coverage. This is resilience/context evidence, not data-center commissioning evidence.

### 2.9 Industrial zones, investment, and energy

- **PIPA**: https://pipa.ps/ . Grade A for investment-promotion material; zone pages are useful for Bethlehem Industrial Estate, Jericho Agro-Industrial Park, Jenin Free Industrial Zone, and Tarqumiya/Hebron leads.
- **PIEFZA / industrial estates**: use official authority or PIPA pages when available. Future data-center siting leads may appear in Bethlehem, Jericho, Jenin, and Hebron industrial zones, but no verified DC build was found in this pass.
- **PENRA / energy**: verify live official energy routes (`energy.gov.ps`) and distribution-company pages for power context. Record power only when a facility source states grid/feeders/generators/solar/storage.

---

## 3. Cloud-region absence

| Provider | Official source | PS signal | Handling |
|---|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No Palestine region; nearby `il-central-1` is Israel (Tel Aviv). | Do not map to PS. |
| Google Cloud | https://cloud.google.com/about/locations and Compute regions docs | No Palestine region; `me-west1` is Tel Aviv, Israel. | Do not map to PS. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Palestine region; Israel Central is Israel. | Do not map to PS. |
| Oracle Cloud | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No Palestine region; `il-jerusalem-1` is Israel Central (Jerusalem). | Do not map to PS. |

Local "cloud" means Paltel private/cloud services, MTDE/NDC government private cloud, or small local VPS/hosting providers unless a hyperscaler page says otherwise.

---

## 4. Governorate coverage and routing

| Division | Arabic/local anchors | Official route | Facility handling |
|---|---|---|---|
| `Ramallah` | رام الله، البيرة، بيتونيا | MTDE/NDC/PalCERT; Paltel Group; PEX; Shiraa; Ramallah and Al-Bireh municipalities | Main cluster. Paltel Al-Bireh Tier III DC; Government Computer Center/NDC; Zone Technologies C/B lead; operator HQ/server rooms. |
| `Nablus` | نابلس | Paltel Group; Nablus municipality; PEX; local integrator references | Paltel first data-center lead at general-management HQ in Nablus from Paltel announcement. Keep specs null unless primary evidence appears. |
| `Hebron` | الخليل، طرقوميا | Hebron municipality; Shiraa; PIPA/PIEFZA; vendor claims | Vendor-only municipal data-center success stories are C until a municipal/official page confirms. Tarqumiya zone is a future lead only. |
| `Bethlehem` | بيت لحم، هندازة | Bethlehem municipality; PIPA/PIEFZA; Shiraa | Beware C-only "Paltel Bethlehem" directory/news claims; do not count without primary evidence. BMIP is future-siting context only. |
| `Jerusalem` | القدس، أبو ديس، الرام، العيزرية | Governorate/municipal pages; JDECO; WAFA | No confirmed PS data center. Filter out Israeli Jerusalem/Tel Aviv cloud-region and colo results. |
| `Jenin` | جنين | Jenin municipality; PIPA/PIEFZA; Shiraa | Directory-only "Paltel Jenin" claims are C; no confirmed facility in this pass. |
| `Jericho and Al Aghwar` | أريحا والأغوار | Jericho municipality; JAIP/PIPA; energy/solar leads | No confirmed facility. Treat land/solar/industrial-zone stories as future leads. |
| `Tulkarm` | طولكرم | Municipality; Shiraa; NEC | No confirmed facility; university/enterprise server rooms only unless official. |
| `Qalqilya` | قلقيلية | Municipality; Shiraa | No confirmed facility. |
| `Salfit` | سلفيت | Municipality; Shiraa | No confirmed facility. |
| `Tubas` | طوباس | Municipality; Shiraa | No confirmed facility. |
| `Gaza` | غزة، مدينة غزة | WAFA, MTDE, PCBS, World Bank/UN/EU RDNA, Paltel/Ooredoo statements | Historical Paltel main data centers/switches; current status damaged/intermittent. Directory-only Digital Communication/ISP facilities are C. |
| `North Gaza` | شمال غزة، بيت حانون، بيت لاهيا | UN/RDNA/PCBS/MTDE; Paltel/Ooredoo | Damage/reconstruction scope only. Do not count redevelopment concepts as projects without permit/award. |
| `Deir El Balah` | دير البلح، الوسطى | UN/RDNA/PCBS/MTDE | No confirmed data center; telecom emergency/recovery nodes only. |
| `Khan Yunis` | خان يونس | UN/RDNA/PCBS/MTDE; university material | Al-Aqsa University "Gaza Data Centre" academic/NSDI concept is C/planned concept only. |
| `Rafah` | رفح، معبر رفح | UN/RDNA/PCBS/MTDE; Egypt connectivity leads | Connectivity/rebuild lead only; no confirmed data center. |

Boundary rule: market copy may label Al-Bireh, Beitunia, or Nablus-related assets as "Ramallah." Use the municipality/coordinates when available; otherwise record the repo division from the strongest source and leave a caveat.

---

## 5. Extraction and acceptance rules

Extract these fields:

```text
name
operator / owner / government body
division and municipality
site / building / zone if public
status: planned | tendered | permitted | construction | operational | damaged | cancelled | rejected
capacity_mw (usually null)
area_sqm / sqft, racks, VMs, hosted institutions, sites, or service counts
power: grid/distribution company, generator, solar, battery, multiple feeds
cloud/service links: colocation, DR, VPS, IaaS/PaaS/SaaS, government private cloud
primary evidence URL and date
evidence grade
confidence notes
```

Acceptance thresholds:
- **Operational facility**: operator/government opening statement, official facility page, Uptime certification plus operator/trade corroboration, or government/World Bank text naming an existing data center.
- **Tendered/planned facility**: Shiraa/MTDE/World Bank procurement that names data center/cloud/data-hosting implementation; keep as pipeline if no site.
- **Damaged facility**: Paltel/WAFA/UN/World Bank/PCBS/7amleh evidence of outage/damage; never silently leave pre-war Gaza sites as operational.
- **Reject / no-project**: generic cloud, hosting, FTTH, network coverage, tower, ISP ASN, academic concept, real-estate zone, or redevelopment vision without facility evidence.

Known weak records to downgrade if encountered:
- `Paltel Data Center - Bethlehem`: C-only unless primary source found.
- `Paltel Data Center - Jenin`: C-only directory lead unless primary source found.
- `Digital Communication Gaza data center`: C-only directory lead; must be status-checked against war damage.
- `New Gaza redevelopment data centres`: concept/announced only; not permitted or under construction unless a later official award appears.
- `Hebron Municipality data center`: C/B lead from vendor material until Hebron Municipality or a procurement notice confirms.
- `Zone Ramallah Data Center`: C+/B- lead. DataCenterMap lists a Ramallah/Al-Bireh site and Zone's own site markets cloud/VPS/storage from Masrouji Building, but no official capacity, Tier, power, or commissioning evidence was verified.

---

## 6. Source index

Official and primary:
- MTDE: https://mtde.gov.ps/
- DWBG project page: https://mtde.gov.ps/home/ads/23032?culture=en-US
- MTDE Unified Data Hosting / Cloud Hosting Strategy EOI: https://mtde.gov.ps/home/ads/23047?culture=ar-SA
- World Bank DWBG restructuring paper: https://documents1.worldbank.org/curated/en/099121925070028162/pdf/P174355-6255b6cc-7a74-47c6-90c7-e5d7b4e67043.pdf
- World Bank Palestinian Digital Economy Assessment: https://documents1.worldbank.org/curated/en/472671640152521943/pdf/Palestinian-Digital-Economy-Assessment.pdf
- National Data Center: https://mtde.online/national-data-center/
- PalCERT: https://mtde.online/palcert/
- WAFA: https://english.wafa.ps/ and https://www.wafa.ps/
- Shiraa public procurement portal: https://www.shiraa.gov.ps/
- PCBS: https://www.pcbs.gov.ps/ ; 2026 ICT release: https://www.pcbs.gov.ps/en/post-details/?postId=26011
- PEX: https://www.pex.ps/
- Paltel Group: https://www.paltelgroup.ps/ ; Paltel DC announcement: https://www.paltelgroup.ps/pginfo/?p=58225
- Uptime Paltel Al-Bireh award: https://uptimeinstitute.com/uptime-institute-awards/datacenter/paltel-data-center--albireh/1115

Strong secondary / corroborating:
- DCD Paltel second DC: https://www.datacenterdynamics.com/en/news/paltel-group-opens-second-palestine-data-center/
- Bloomberg/Data Center Knowledge: https://www.datacenterknowledge.com/cloud/palestinian-phone-company-offers-cloud-computing-from-ramallah
- 7amleh Gaza telecom damage: https://7amleh.org/post/impact-of-war-on-gaza-s-telecommunications-infrastructure-en
- WAFA Paltel Gaza blackout: https://english.wafa.ps/Pages/Details/139337
- Al Jazeera Gaza telecom redundancy: https://www.aljazeera.com/news/2023/11/21/keeping-gaza-online-gazas-telecom-heroes-risk-life-and-limb-under-israels-bombs
- World Bank / EU / UN Gaza RDNA 2026: https://thedocs.worldbank.org/en/doc/e539cbf23b348c3d4fc69b8a7e9c9d7d-0280062026/rapid-damage-and-needs-assessment-gaza-strip-april-2026

Cloud-region absence:
- AWS: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Google Cloud: https://cloud.google.com/about/locations
- Azure: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Oracle: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm
