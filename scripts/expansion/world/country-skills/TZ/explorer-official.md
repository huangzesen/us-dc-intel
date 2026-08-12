# TZ Explorer Official - Tanzania Datacenter Enumeration

Date: 2026-08-12. Country: **TZ Tanzania (United Republic of)**. Division model: **31 regions** (26 mainland regions plus 5 Zanzibar regions). Angle: official, regulatory, planning, power, investment, government-cloud, and operator-primary sources for finding commercial, carrier-neutral, telecom, government, and enterprise data-centre facilities.

Reliability grades:
- **A** = primary/official/legal source: TCRA licence register or public-data-centre specification, NEMC EIA/EA record, EWURA/TANESCO record, TISEZA/SEZ instrument, PDPC/legal text, eGA/government document, LGA/Tausi building-permit record, official cloud-provider location page, official operator facility page, Uptime Institute award record.
- **B** = strong secondary source: DCD, W.Media, Capacity, Connecting Africa, Developing Telecoms, ITWeb Africa, TanzaniaInvest, Daily News/The Citizen/Guardian business reporting, industry association, vendor case study, PeeringDB/TIX/Submarine Cable Map for network-node presence.
- **C** = weak lead: generic market report, aggregator/directory entry, social post, old MoU, unsupported capacity claim, or local article that does not identify a physical compute/hosting facility.

Use grades per data point. A single facility record can contain A-grade operator existence, B-grade press capacity, and C-grade directory address until each field is independently verified.

---

## 0. Tanzania-specific structure facts

- Tanzania does **not** have one complete public datacenter planning registry. Enumeration works by joining: **TCRA** communications licensing and public data-centre technical rules; **NEMC** EIA/environmental-audit records; **local government building permits** through councils and the **Tausi** portal; **EWURA/TANESCO** power evidence; **TISEZA** investment and SEZ records; **PDPC/PDPA** data-protection and cross-border-transfer obligations; **eGA** government data-centre/cloud documents; and official operator pages.
- Datacenter supply is heavily concentrated in **Dar es Salaam**. Confirmed/high-value seeds are Raxio TZ1 (launching 2026), Wingu Africa Tanzania, NIDC/TTCL, Vodacom Business, Tigo/Yas, Airtel, Aptus/ISP hosting, TIX and cable landing infrastructure. Secondary government/pipeline clusters are **Dodoma** (eGA/government systems, national-government ICT) and **Zanzibar Urban/West** (Zanzibar e-government and planned/announced government data-centre initiatives). **Pwani/Coast** is a watch region because of Kwala SEZ/Kibaha and fibre/power corridors, not because a datacenter is yet verified there.
- English is sufficient for most official material, but use Swahili variants in government/local searches: `kituo cha data`, `kituo cha kuhifadhi data`, `hifadhi ya data`, `seva`, `chumba cha seva`, `mkongo wa taifa wa mawasiliano`, `mtandao`, `kituo cha mawasiliano`.
- Treat telco core rooms, IXP/cable landing stations, government server rooms, GIS/statistics centres, cyber cafes, and e-government kiosks as **non-datacenter leads** unless the source identifies a hosted compute/colocation/cloud facility.
- Cloud-region handling: as of 2026-08-12, no AWS, Azure, Google Cloud, or Oracle OCI public cloud region is listed in Tanzania on official provider pages. Tanzanian cloud evidence is local/sovereign: eGA/government cloud, NIDC/TTCL, Raxio, Wingu, and telco/ISP cloud or hosting. Do not infer a hyperscale facility from CDN, PoP, partner, or cable presence.
- International connectivity now includes **EASSy, SEACOM, SEAS, and 2Africa** at/through Dar es Salaam/Tanzania evidence surfaces. 2Africa Tanzania activation was reported by Airtel/Telesonic and industry sources in 2024. **DARE1** is a future lead: Djibouti Telecom announced a southward extension in September 2025, with work targeted from 2026 and ready-for-service around 2028. Cable landing evidence proves network presence, not data-centre capacity.

Primary/official source anchors verified during this rewrite:
- TCRA home and licence search: https://www.tcra.go.tz/ and https://www.tcra.go.tz/services/licenses
- TCRA Telecommunications/ICT framework page: https://www.tcra.go.tz/resources/telecommunications-ict
- TCRA public data-centre technical specification: https://www.tcra.go.tz/tcra-tovuti/2025/mamlaka-website/documents/minimum-technical-specs/en_1748239940_MINIMUM_TECHNICAL_SPECIFICATIONS_FOR_PUBLIC_DATA_CENTER_1_1032107643381814476641029946369102376331747724695814_a576d69b16.pdf
- Tanzanite portal: https://tanzanite.tcra.go.tz/
- NEMC PMS: https://eia.nemc.or.tz/
- EWURA electricity licensing/registration: https://www.ewura.go.tz/pages/licensing-and-registration
- EWURA electricity infrastructure: https://www.ewura.go.tz/pages/electricity-infrastructure
- Tausi portal: https://tausi.tamisemi.go.tz/
- TISEZA: https://www.tiseza.go.tz/
- TISEZA history/new mandate: https://www.tiseza.go.tz/pages/history
- PDPC: https://pdpc.go.tz/
- eGA Data Center Standards and Guidelines for Public Institutions: https://www.ega.go.tz/pdf-viewer?file=https%3A%2F%2Fwww.ega.go.tz%2Fuploads%2Fstandarddocuments%2Fsw-1773257204-FINAL+Reviewed_Data+Center+Standards+and+Guidelines+for+Public+Institutions-18.2.2026.pdf
- NIDC: https://nidc.co.tz/
- Raxio Tanzania: https://www.raxiogroup.com/data-centres/tanzania/
- Wingu Africa: https://www.wingu.africa/

---

## 1. Official regulatory and government sources

### 1.1 TCRA - licensing, public DC technical rules, and licencee register

- **TCRA home**: https://www.tcra.go.tz/
- **Licensed Providers & Certificates database**: https://www.tcra.go.tz/services/licenses
  - Searchable official database of licences/certificates. Use sector filter **Telecommunications & Internet** and search operator/SPV names.
  - Extract licence type/number, issue/expiry date, licensee legal name, address, town/region, and licensed service. Licence evidence proves authority to operate regulated communications infrastructure/services; it does not by itself prove the number, capacity, or exact site of datacenters.
- **Tanzanite portal**: https://tanzanite.tcra.go.tz/
  - Official TCRA service portal for licence applications and stakeholders.
- **Telecommunications/ICT framework**: https://www.tcra.go.tz/resources/telecommunications-ict
  - TCRA describes the Converged Licensing Framework categories: Network Facilities Licence (NFL), Network Service Licence (NSL), Application Services Licence (ASL), and Content Service Licence.
- **Minimum Technical Specifications for Public Data Centers**, Document No. **TCRA/TS013**, Version **2.0**, May 2025:
  - Primary source for Tanzania public-data-centre technical requirements and terminology. Use this to classify public DC operators and expected controls; do not treat the specification as a list of facilities.
  - Practitioner commentary in 2025 says public data centres require an NFL and quarterly hosted-customer reporting. Treat the requirement as A only where visible in TCRA instruments/specifications; treat practitioner summaries as B.

TCRA query templates:
```text
site:tcra.go.tz "public data center"
site:tcra.go.tz "public data centre"
site:tcra.go.tz "Minimum Technical Specifications" "Public Data Centers"
site:tcra.go.tz "Network Facilities Licence" "data center"
site:tcra.go.tz/services/licenses Raxio
site:tcra.go.tz/services/licenses Wingu
site:tcra.go.tz/services/licenses TTCL
site:tanzanite.tcra.go.tz Raxio OR Wingu OR TTCL OR NIDC
"TCRA/TS013" "Public Data Centers"
"TCRA" "Network Facility Licence" "data centre" Tanzania
```

Operator sweep terms for the register: `Raxio`, `Wingu`, `TTCL`, `NIDC`, `Vodacom`, `Tigo`, `Yas`, `Airtel`, `Halotel`, `Zantel`, `Smile`, `CBN`, `Sasatel`, `Aptus`, `Flashnet`, `Simbanet`, `Liquid`, `SEACOM`, `Airtel Telesonic`.

### 1.2 NEMC - EIA and environmental-audit evidence

- **NEMC**: https://www.nemc.or.tz/
- **Projects Management System (PMS)**: https://eia.nemc.or.tz/
  - PMS is the official environmental impact assessment and environmental audit management system. It supports developer and environmental-expert accounts and references the Environmental Management Act 2004, EIA and Audit Regulations 2005, and 2018 amendments.
- Datacenters may be filed as ICT buildings, commercial buildings, industrial/SEZ projects, substations, backup-generator/fuel-storage projects, or as a component of a larger mixed-use or telecom project. NEMC is high precision but incomplete through public search.

NEMC query templates:
```text
site:nemc.or.tz "data centre"
site:nemc.or.tz "data center"
site:eia.nemc.or.tz "data centre"
site:eia.nemc.or.tz "data center"
site:nemc.or.tz Raxio OR Wingu OR TTCL OR Vodacom
"Raxio TZ1" NEMC OR EIA OR ESIA
"Wingu" Tanzania NEMC OR EIA OR ESIA
"National Internet Data Center" NEMC Tanzania
"{project}" "Environmental Impact Assessment" Tanzania
"{operator}" "Environmental Audit" Tanzania
```

Extract: NEMC/EIA reference, proponent, district/ward/plot, project title, EIA category, ESIA consultant, generators/fuel storage, cooling/water, waste handling, public-consultation notice, approval/certificate date, and grid/substation linkage.

### 1.3 EWURA and TANESCO - power trail

- **EWURA**: https://www.ewura.go.tz/
- **EWURA electricity licensing and registration**: https://www.ewura.go.tz/pages/licensing-and-registration
  - Official page states EWURA issues a licence for electricity activities above **1 MW** and registration for activities below **1 MW**.
- **EWURA electricity infrastructure**: https://www.ewura.go.tz/pages/electricity-infrastructure
  - Official page states EWURA regulates Tanzania Mainland's electricity supply industry, dominated by state-owned **TANESCO** as a vertically integrated utility.
- **TANESCO**: https://www.tanesco.co.tz/
  - Search for customer connection, substation, feeder, energisation, procurement, and outage/connection terms. Most DC grid evidence will be buried in TANESCO releases/tenders, EWURA filings, or ESIA documents.

Power query templates:
```text
site:tanesco.co.tz "data centre"
site:tanesco.co.tz "data center"
site:tanesco.co.tz Raxio OR Wingu OR NIDC OR Vodacom
site:tanesco.co.tz "33kV" "Dar es Salaam" "data"
site:ewura.go.tz Raxio OR Wingu OR NIDC OR Vodacom
site:ewura.go.tz "data centre" OR "data center"
"{project}" TANESCO "33kV" OR "33 kV" OR MVA OR MW
"{project}" "substation" Tanzania
"{operator}" "power supply agreement" Tanzania
```

Extract and preserve units exactly: IT MW, total facility MW, utility MVA, voltage, feeder/substation, backup generation rating, on-site solar, PPA status, and evidence date. Do not convert MVA to IT MW without a source.

### 1.4 TISEZA, investment certificates, and SEZ/industrial-park leads

- **TISEZA home**: https://www.tiseza.go.tz/
- **TISEZA history/mandate**: https://www.tiseza.go.tz/pages/history
  - TISEZA was created under the **Investment and Special Economic Zones Act No. 6 of 2025**, merging TIC and EPZA functions. It is the key official surface for investment registration, incentives, SEZ/EPZ instruments, and zone/developer announcements.
- **Kwala SEZ / Kwala Industrial Park**, Kibaha, **Pwani/Coast Region**, is a priority watch area because TISEZA and investment press describe a large SEZ/industrial-logistics hub. As of this methodology, Kwala is a site-selection lead only; do not count it as a datacenter without a named DC tenant/project and permit or operator evidence.

TISEZA query templates:
```text
site:tiseza.go.tz "data centre" OR "data center" OR "ICT"
site:tiseza.go.tz "Kwala" "SEZ"
site:tiseza.go.tz "Kibaha" "Special Economic Zone"
site:tiseza.go.tz Raxio OR Wingu OR "data"
"Kwala SEZ" Tanzania "data centre" OR "ICT"
"{region}" Tanzania "Special Economic Zone" "data centre"
"{operator}" TISEZA Tanzania
```

Extract: certificate/licence number, investor/developer, zone, plot, region/district, sector, project title, investment value, expected power/water/fibre, and whether the source is an investment certificate, press release, or promotional material.

### 1.5 PDPC / PDPA - data-residency demand, not facility proof

- **PDPC**: https://pdpc.go.tz/
- **PDPC About**: https://pdpc.go.tz/about-us/
- **PDPC data-protection system**: https://dataprotection.pdpc.go.tz/
- **Personal Data Protection Act, 2022**: https://pdpc.go.tz/the-personal-data-protection-act-2022/

The PDPA established the Personal Data Protection Commission and governs collection, processing, storage, disclosure, and transfer of personal data. PDPC pages show registration of controllers/processors and cross-border data-transfer permits. Use PDPC/PDPA as A-grade legal/demand context for domestic hosting, especially banking, telecom, health, government, and cloud customers. It is not facility evidence unless a registered operator or hosting arrangement is named.

PDPC query templates:
```text
site:pdpc.go.tz "data centre" OR "data center"
site:pdpc.go.tz "cross-border data transfer"
site:pdpc.go.tz "data controller" "processor" "registration"
"Personal Data Protection Act" Tanzania "data centre"
"Tanzania" "data localization" "data centre" PDPC
"Tanzania" "primary servers" "local" "data centre"
```

### 1.6 eGA, government cloud, and public-institution data centres

- **e-Government Authority (eGA)**: https://www.ega.go.tz/
- **Data Center Standards and Guidelines for Public Institutions**: eGA PDF viewer URL above, reviewed/final document dated 18.2.2026 in the file path.
- **e-Government Authority Strategic Plan**: https://www.ega.go.tz/uploads/publications/en-1625048198-e-Government%20Authority%20Strategic%20Plan.pdf
  - Strategic-plan tables include shared/government data-centre infrastructure and eGA management reporting indicators. Use as A-grade evidence that government data-centre infrastructure exists and is managed/planned, but still seek facility-level documents for exact sites.
- **NIDC**: https://nidc.co.tz/
  - Official NIDC pages state the Government of Tanzania constructed the National Internet Data Center in 2015 and describe it as a modern Tier-III data center in Dar es Salaam operated by/with the state telecom operator. Use NIDC pages as A-grade existence/service evidence.

eGA/government query templates:
```text
site:ega.go.tz "data centre"
site:ega.go.tz "data center"
site:ega.go.tz "Data Center Standards"
site:ega.go.tz "shared data centre"
site:go.tz "national data centre" Dodoma
site:go.tz "data centre" "Zanzibar"
site:nidc.co.tz "Tier" OR "colocation" OR "cloud"
"e-Government Authority" Tanzania "data centre"
"National Internet Data Center" Tanzania "Dar es Salaam"
```

Government/DC press leads to verify: planned/announced modern data centres in **Dodoma** and **Zanzibar**, eGA shared data-centre infrastructure, national information/cybersecurity centres, and Zanzibar ICT Infrastructure Agency systems. Keep `planned`, `budgeted`, `under construction`, and `operational` separate.

### 1.7 Building permits and local government planning

- **Tausi portal**: https://tausi.tamisemi.go.tz/
  - Official PO-RALG/TAMISEMI taxpayer portal shows **Building Permit** and **Certificate of Occupancy** services for LGAs. Deep records may require account access or council follow-up.
- **TISEZA procedures - construction permits**: https://procedures.tiseza.go.tz/procedure/166?l=en
  - Good official route summary for investor-facing construction-permit steps.
- Priority councils for Dar es Salaam: **Kinondoni MC, Ilala MC, Ubungo MC, Temeke MC, Kigamboni MC**. Other high-yield LGAs: Dodoma CC, Kibaha TC/DC (Kwala), Arusha CC, Mwanza CC, Moshi MC, Mbeya CC, Morogoro MC, Tanga CC, Mtwara MC, Zanzibar urban authorities.

Permit query templates:
```text
site:tausi.tamisemi.go.tz "Building Permit"
site:{council-domain} "data centre" OR "data center"
"Kinondoni" "data centre" "building permit"
"Ilala" "data centre" "building permit"
"Ubungo" "data centre" "building permit"
"Temeke" "data centre" "building permit"
"Kigamboni" "data centre" "building permit"
"{operator}" "building permit" "Dar es Salaam"
"{operator}" "certificate of occupancy" Tanzania
"{plot OR road}" "data centre" Tanzania
```

Extract: LGA/council, applicant, plot/block/ward, description, gross floor area, data halls, generators/fuel storage, power load, approval date, occupation certificate, and links to EIA/TANESCO/TCRA records.

---

## 2. Official cloud-region and edge handling

| Provider | Official source | Tanzania signal | How to use |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Tanzania Region listed. Africa has AWS Africa (Cape Town); current official expansion list does not show Tanzania. | Treat AWS mentions as customer/partner/edge leads only. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | No Tanzania public Azure region. Africa entries are South Africa North/West; Microsoft/G42 announced an East Africa Cloud Region in Kenya. | Do not infer a Tanzanian Azure facility from Kenya or South Africa. |
| Google Cloud | https://cloud.google.com/about/locations | No Tanzania region. Africa region: Johannesburg (`africa-south1`). | Tenant/edge/partner lead only. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No Tanzania OCI public region. Africa includes Johannesburg; Kenya/Nairobi is listed/announced as coming. | Tenant/partner lead only; verify Kenya claims against Oracle/iXAfrica sources. |
| Local/sovereign | https://www.ega.go.tz/ , https://nidc.co.tz/ , https://www.raxiogroup.com/data-centres/tanzania/ , https://www.wingu.africa/ | Tanzania-hosted government cloud, colocation, and private/cloud-connect services. | Map cloud services to physical host facility before counting. |

Cloud query templates:
```text
"Tanzania" "cloud region" AWS OR Azure OR "Google Cloud" OR Oracle
"Azure" "Tanzania" "data centre"
"AWS" "Tanzania" "data center"
"Oracle Cloud" Tanzania region
"Google Cloud" Tanzania region
"sovereign cloud" Tanzania "data centre"
"government cloud" Tanzania eGA OR NIDC
```

---

## 3. Official/operator facility seed list

Operator pages are A-grade for what the operator says about its own marketed facility. Confirm status, permits, licensing, and utility interconnection independently before changing a record to `operational` or `under_construction`.

| Operator / project | Primary source | Region / locality signal | Verified use and follow-up |
|---|---|---|---|
| Raxio Tanzania / TZ1 | https://www.raxiogroup.com/data-centres/tanzania/ | Dar es Salaam, outskirts of Dar, roughly 30 minutes from CBD | Official page states launch in 2026, carrier-neutral Tier III DC, 800 racks, 4,000 m2, 6 MW IT power, seven security layers, 33 kV utility supply in downloadable/spec material where available. Follow TCRA, NEMC, LGA permits, TANESCO, Uptime award list, and 2026 launch status. |
| Wingu Africa Tanzania | https://www.wingu.africa/ | Dar es Salaam, Mbezi/industrial-area lead from press/directories | Official page confirms Wingu operates in Tanzania and offers carrier-neutral colocation/interconnection/cloud connectivity. Press says phase 1 live from 2022 and phase 2/3 MW expansion in 2025; verify facility-specific capacity against Wingu news, TCRA, NEMC, permits, power evidence, and Uptime list. |
| NIDC / TTCL | https://nidc.co.tz/ and https://www.ttcl.co.tz/ | Dar es Salaam | NIDC official pages describe the National Internet Data Center, constructed by Government of Tanzania in 2015, Tier-III, Dar es Salaam, with cloud/colocation services. Follow TCRA/TTCL licence, eGA/government use, PeeringDB, NICTBB, and power records. |
| Vodacom Business Tanzania | https://www.vodacom.co.tz/ | Dar es Salaam and Dodoma leads from directories/enterprise pages | Treat as telecom/operator-owned data-centre or hosting lead until official page or TCRA/council evidence confirms facility function. Directories are C for address/capacity. |
| Tigo / Yas Tanzania | https://www.yas.co.tz/ and legacy https://www.tigo.co.tz/ references | Dar es Salaam telco-core lead | Distinguish telco core/network facility from marketed colocation. Search TCRA and operator business pages. |
| Airtel Tanzania / Airtel Telesonic | https://www.airtel.co.tz/ | Dar es Salaam telco/cable/network lead; 2Africa Tanzania activation lead | Airtel is relevant for 2Africa/cable and telco core. Do not infer a commercial DC from cable landing or Nxtra regional announcements. |
| eGA / ministry government DCs | https://www.ega.go.tz/ and `.go.tz` ministry pages | Dodoma and national public-institution infrastructure; Zanzibar planned/announced leads | Use eGA standards/strategic plans as A context. Require facility-level source for site, stage, and capacity. |
| Zanzibar government data-centre initiatives | Zanzibar government/e-government/ZIPA and Union ministry sources | Zanzibar Urban/West primarily; other Zanzibar regions as negative checks | Press/MoUs indicate planned data-centre investments. Keep as planned/lead unless a Zanzibar government or operator source shows procurement, construction, or operation. |
| Aptus / Flashnet / ISP hosting | https://aptus.co.tz/ and operator sites | Dar es Salaam | Hosting/VPS/dedicated-server leads. Count only if a physical datacenter/colocation facility is described or corroborated. |
| Banks/enterprise (BoT, CRDB, NMB, universities, insurers) | annual reports, DSE filings, tender portals | Dar es Salaam, Dodoma, Mwanza, Arusha | Enterprise DC/DR leads are usually private. Record as enterprise-only unless a source shows external hosting/colo service. |

Operator query templates:
```text
"Raxio Tanzania" "TZ1" "Dar es Salaam"
"Raxio TZ1" "6 MW" "800 racks"
"Wingu" "Dar es Salaam" "data centre"
"Wingu Africa" Tanzania "3MW" OR "3 MW" OR expansion
"NIDC" "National Internet Data Center" Tanzania "Tier"
"TTCL" "data centre" OR "data center"
"Vodacom Tanzania" "data centre" Dodoma OR "Dar es Salaam"
"Tigo" OR "Yas" Tanzania "data centre"
"Airtel Tanzania" "2Africa" "Dar es Salaam"
```

---

## 4. Division coverage: exact 31-region workflow

Use the following 31 regions as the required coverage set. The manifest uses simplified English names for Zanzibar; official/NBS/Tanzania names often use **Mjini Magharibi (Zanzibar Urban/West)**, **Kaskazini Unguja (Zanzibar North)**, **Kusini Unguja (Zanzibar South/Central)**, **Kaskazini Pemba**, and **Kusini Pemba**. Search both names.

Mainland regions (26): Arusha, Dar es Salaam, Dodoma, Geita, Iringa, Kagera, Katavi, Kigoma, Kilimanjaro, Lindi, Manyara, Mara, Mbeya, Morogoro, Mtwara, Mwanza, Njombe, Coast/Pwani, Rukwa, Ruvuma, Shinyanga, Simiyu, Singida, Songwe, Tabora, Tanga.

Zanzibar regions (5): Pemba North/Kaskazini Pemba, Pemba South/Kusini Pemba, Zanzibar North/Kaskazini Unguja, Zanzibar South/Kusini Unguja, Zanzibar West/Mjini Magharibi/Zanzibar Urban West.

For every region:
1. Run official-domain searches first: TCRA licencee register, NEMC/PMS, LGA/Tausi building permits, EWURA/TANESCO, eGA/ministry/government sites, TISEZA for SEZ/industrial regions.
2. Run operator seeds with region and main town names.
3. Run English and Swahili generic searches.
4. Run interconnection checks (TIX, PeeringDB, Submarine Cable Map) where relevant.
5. Record a defensible negative when all four passes find only generic ICT offices, telco retail shops, POPs, or non-hosting government systems.

### 4.1 Priority clusters

| Region | Main localities | Current facility/lead posture | Required checks |
|---|---|---|---|
| Dar es Salaam | Kinondoni, Ilala, Ubungo, Temeke, Kigamboni; Old Bagamoyo Rd, Mbezi, Laibon Rd, Posta/City Centre | Highest-probability commercial and telco cluster: Raxio TZ1, Wingu, NIDC/TTCL, Vodacom, Tigo/Yas, Airtel, Aptus/Flashnet, TIX, cable landings. | Operator pages, TCRA licences, NEMC, council/Tausi permits, TANESCO 33 kV/MVA evidence, Uptime, PeeringDB, cable maps. |
| Dodoma | Dodoma City, Mtumba, Nzuguni, Chamwino | Government/eGA and telco/government-hosting leads; possible planned national data centre. | eGA, ministry `.go.tz`, Dodoma CC/Tausi, TCRA, TANESCO, press status. |
| Zanzibar West / Mjini Magharibi | Zanzibar City, Stone Town, Fumba | Zanzibar government planned/announced DC and e-government/ZIPA/Silicon Zanzibar leads; Zantel/telco POPs. | Zanzibar government, ZIPA, e-government agency, TCRA, Zantel, press; classify MoUs as planned. |
| Coast / Pwani | Kibaha, Kwala, Bagamoyo, Mkuranga | Kwala SEZ/industrial-park and fibre/power corridor watch area; no confirmed datacenter from official evidence found in this rewrite. | TISEZA, Kibaha LGA/Tausi, TANESCO, NEMC, investor announcements. |
| Mtwara | Mtwara town | Future DARE1 extension/cable landing lead; no confirmed commercial DC from cable evidence alone. | DARE1, cable landing, TANESCO, TCRA, council, port/SEZ sources. |
| Arusha, Mwanza, Kilimanjaro, Mbeya, Morogoro, Tanga | Regional capitals and business/telco hubs | Mostly telco/enterprise/DR leads; commercial colo not assumed. | Operator+TCRA sweep, council permits, bank/enterprise annual reports, NICTBB/telco. |
| Remaining low-yield regions | Kagera, Kigoma, Lindi, Mara, Rukwa, Ruvuma, Shinyanga, Singida, Tabora, Manyara, Geita, Katavi, Njombe, Simiyu, Songwe, Iringa, Pemba North/South, Zanzibar North/South | Negative searches expected except telco POPs, government ICT/server rooms, banks, and fibre nodes. | Minimum negative sweep: generic terms + operator terms + TCRA town/license + `.go.tz` + Swahili terms. |

### 4.2 Copy/paste 31-region seed queries

```text
Arusha Tanzania "data centre" OR "data center" OR datacentre OR colocation
"Dar es Salaam" Tanzania (Raxio OR Wingu OR NIDC OR TTCL OR Vodacom OR Tigo OR Yas OR Airtel OR Aptus) "data centre"
Dodoma Tanzania (eGA OR "national data centre" OR Vodacom OR "government cloud") "data centre"
Geita Tanzania "data centre" OR "data center" OR datacentre OR "kituo cha data"
Iringa Tanzania "data centre" OR "data center" OR datacentre OR "kituo cha data"
Kagera Tanzania "data centre" OR "data center" OR datacentre OR "kituo cha data"
Katavi Tanzania "data centre" OR "data center" OR datacentre OR "kituo cha data"
Kigoma Tanzania "data centre" OR "data center" OR datacentre OR "kituo cha data"
Kilimanjaro OR Moshi Tanzania "data centre" OR "data center" OR datacentre
Lindi Tanzania "data centre" OR "data center" OR datacentre OR "kituo cha data"
Manyara Tanzania "data centre" OR "data center" OR datacentre OR "kituo cha data"
Mara Tanzania "data centre" OR "data center" OR datacentre OR "kituo cha data"
Mbeya Tanzania "data centre" OR "data center" OR datacentre OR colocation
Morogoro Tanzania "data centre" OR "data center" OR datacentre OR colocation
Mtwara Tanzania "data centre" OR "data center" OR "landing station" OR DARE1
Mwanza Tanzania "data centre" OR "data center" OR datacentre OR colocation
Njombe Tanzania "data centre" OR "data center" OR datacentre OR "kituo cha data"
Coast OR Pwani OR Kibaha OR "Kwala SEZ" Tanzania "data centre" OR "data center"
Rukwa Tanzania "data centre" OR "data center" OR datacentre OR "kituo cha data"
Ruvuma Tanzania "data centre" OR "data center" OR datacentre OR "kituo cha data"
Shinyanga Tanzania "data centre" OR "data center" OR datacentre OR "kituo cha data"
Simiyu Tanzania "data centre" OR "data center" OR datacentre OR "kituo cha data"
Singida Tanzania "data centre" OR "data center" OR datacentre OR "kituo cha data"
Songwe Tanzania "data centre" OR "data center" OR datacentre OR "kituo cha data"
Tabora Tanzania "data centre" OR "data center" OR datacentre OR "kituo cha data"
Tanga Tanzania "data centre" OR "data center" OR datacentre OR colocation
"Pemba North" OR "Kaskazini Pemba" Tanzania "data centre" OR "data center" OR "kituo cha data"
"Pemba South" OR "Kusini Pemba" Tanzania "data centre" OR "data center" OR "kituo cha data"
"Zanzibar North" OR "Kaskazini Unguja" Tanzania "data centre" OR "data center" OR "kituo cha data"
"Zanzibar South" OR "Kusini Unguja" Tanzania "data centre" OR "data center" OR "kituo cha data"
"Zanzibar West" OR "Mjini Magharibi" OR "Zanzibar Urban West" Tanzania "data centre" OR "e-Government"
```

---

## 5. Evidence extraction and acceptance rules

Minimum fields for each candidate:
- facility/campus name and aliases;
- region, district/council, locality/road/plot/SEZ when available;
- owner/operator/developer and local SPV/licensee;
- facility type: carrier-neutral colo, telco core, government cloud/shared DC, enterprise/private, cable landing/IXP, planned SEZ tenant;
- status and status evidence date;
- capacity by unit: IT MW, facility MW, MVA, racks, sqm/white space, data halls, phases;
- primary source URLs and grade per field;
- cross-checks: TCRA, NEMC, LGA/Tausi, EWURA/TANESCO, Uptime, eGA/government, TISEZA, operator page, press.

Promote a lead to a counted datacenter only when at least one A-grade or strong B-grade source identifies a physical facility with compute/hosting/colocation/cloud/server-infrastructure function. Keep the following as leads, not counted facilities, unless corroborated: IXP nodes, subsea cable landing stations, telco BTS/tower sites, retail branches, generic ICT offices, cybersecurity/SOC offices, GIS data portals, government statistics units, and cloud service reseller offices.

Recommended discovery order:
1. Seed Dar es Salaam with Raxio, Wingu, NIDC/TTCL, Vodacom, Tigo/Yas, Airtel, Aptus/Flashnet.
2. Resolve each seed through TCRA, NEMC, council/Tausi, TANESCO/EWURA, Uptime, and official operator pages.
3. Add Dodoma and Zanzibar government leads and classify their stage precisely.
4. Sweep Pwani/Kwala, Mtwara/DARE1, and secondary cities.
5. Run the 31-region negative sweep and record explicit negative evidence for low-yield regions.
