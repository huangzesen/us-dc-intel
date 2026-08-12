# ID Explorer — Official / Regulatory / Cloud Pipeline for Indonesia Datacenter Enumeration

Date: 2026-08-12. Country: **ID Indonesia**. Division model for world expansion: **38 provinces / special regions / capital district**. Focus: official and legally accountable evidence for datacenter enumeration: OSS/RBA business licensing and KBLI classification, spatial and building permits, environmental approvals, PLN power trail, Komdigi PSE registration, official cloud-region pages, and official colo/operator disclosures.

Reliability grades used here:
- **A** = primary / official / legally accountable source: Indonesian government portal, PLN / PLN Batam release or power contract disclosure, official cloud-region page, official operator facility page, public-company filing, official industrial-estate / SEZ page.
- **B** = strong secondary source: Antara, major Indonesian business press, Data Center Dynamics, operator partner release, credible engineering / real-estate source that names the project.
- **C** = weak lead: aggregator directory, social media, consultant summary, stale marketing page, project rumor, or MOU-only investment article.

---

## 1. Indonesia-Specific Structure Facts

Indonesia does **not** have a complete public national registry of commercial datacenters. Treat the enumeration problem as a join across five official trails:

1. **Business licensing / OSS-RBA**: datacenter operators register business activities through OSS under KBLI, especially **KBLI 63102 Aktivitas Penyediaan Infrastruktur Komputasi, Hosting, dan Aktivitas Terkait**, whose OSS description explicitly includes cloud infrastructure, server-room rental, network rental in a data center, data-center colocation, and electronic storage. OSS pages: https://oss.go.id/en and KBLI 63102 page https://oss.go.id/kbli/detail/4be9f0ac-583b-5323-9839-7372e1708032. Grade **A** for legal-activity classification / NIB facts, but OSS is not a facility registry.
2. **Spatial and building permission**: large campuses need spatial suitability through RDTR / KKPR and building approval through **SIMBG** for **PBG** and later **SLF**. OSS RDTR Interaktif: https://oss.go.id/en/rdtr-interaktif. SIMBG: https://simbg.pu.go.id/. Grade **A** when a PBG, SLF, RDTR/KKPR, local DPMPTSP, or industrial-estate record names the project or land parcel.
3. **Environmental approval**: large buildings / industrial campuses may need AMDAL or UKL-UPL processed through KLHK / AMDALNET. AMDALNET is the key search concept; portal: https://amdalnet.menlhk.go.id/. Grade **A** for AMDAL/UKL-UPL/PKPLH documents and environmental approval decisions. Absence is not negative evidence because many smaller colocation or retrofit facilities will not surface publicly.
4. **Power trail**: hyperscale projects leave strong evidence through PLN / PLN Batam power-sale agreements (**PJBTL**), connection capacity in MVA, REC procurement, substation works, and PLN e-procurement. PLN customer / REC portal: https://layanan.pln.co.id/; PLN e-procurement: https://eproc.pln.co.id/. Grade **A** when PLN or PLN Batam names the customer, project, and MVA/MW.
5. **Cloud / colo operator trail**: official cloud regions and colo facility pages prove operating markets and narrow the geography, but usually hide exact hyperscaler sites. Grade **A** for market/city/province and disclosed IT load; exact coordinates remain **B/C** unless corroborated by permits, PLN, filings, or industrial-estate pages.

Important caveat: Indonesian datacenters are usually permitted as **computing infrastructure, hosting, office/commercial building, industrial estate, telecommunication facility, warehouse/utility building, or digital infrastructure**, not always under "pusat data" as a unique project category. Use Indonesian terms first.

---

## 2. Indonesian + English Query Patterns

Use Bahasa Indonesia first, then English for hyperscalers, foreign colos, REIT/investor pages, and trade press.

### 2.1 Core Datacenter Terms

```
"pusat data" "{operator}" "{province_or_city}"
"data center" "{operator}" "{province_or_city}"
"data centre" "{operator}" "{province_or_city}"
"datacenter" "{operator}" "{province_or_city}"
"colocation" "{operator}" Indonesia
"infrastruktur komputasi" "{operator}"
"penyediaan infrastruktur komputasi" "{operator}"
"cloud region" Jakarta Indonesia
"Availability Zone" Jakarta Indonesia
```

### 2.2 Permit / Planning / Building

```
site:oss.go.id "63102" "pusat data"
site:oss.go.id "data center" "KBLI"
site:oss.go.id "RDTR Interaktif" "{city}"
site:simbg.pu.go.id "PBG" "pusat data"
"PBG" "pusat data" "{city}"
"Persetujuan Bangunan Gedung" "data center" "{city}"
"Sertifikat Laik Fungsi" "data center" "{operator}"
"SLF" "pusat data" "{operator}"
"KKPR" "data center" "{city}"
"kesesuaian kegiatan pemanfaatan ruang" "pusat data"
site:{province_or_city_dpmptsp_domain} "pusat data"
site:{province_or_city_domain}.go.id "data center" "PBG"
```

### 2.3 Environmental

```
site:amdalnet.menlhk.go.id "pusat data"
site:amdalnet.menlhk.go.id "data center"
site:menlhk.go.id "pusat data" "AMDAL"
"AMDAL" "data center" "{operator}"
"UKL-UPL" "pusat data" "{operator}"
"Persetujuan Lingkungan" "data center" "{city}"
```

### 2.4 Power / PLN

```
site:pln.co.id "data center" "MVA"
site:web.pln.co.id "data center" "MVA"
site:plnbatam.com "data center" "PJBTL"
"PJBTL" "data center" "{operator}"
"Perjanjian Jual Beli Tenaga Listrik" "pusat data"
"PLN" "pasok listrik" "data center" "{city}"
"Renewable Energy Certificate" "data center" "PLN"
site:eproc.pln.co.id "data center"
site:eproc.pln.co.id "pusat data"
```

### 2.5 Government Procurement

Indonesia's public-sector data-center trail is mostly government procurement rather than private hyperscale siting.

```
site:spse.inaproc.id "pusat data"
site:spse.inaproc.id "data center"
site:sirup.lkpp.go.id "pusat data"
site:data.inaproc.id "data center"
"LPSE" "pengembangan data center" "{ministry_or_province}"
"Pusat Data Nasional" "tender"
"data recovery center" "LPSE"
```

Portals: LKPP https://www.lkpp.go.id/, eProc LKPP https://eproc.lkpp.go.id/, SPSE / Inaproc https://spse.inaproc.id/, SIRUP https://sirup.lkpp.go.id/, Data Inaproc https://data.inaproc.id/.

---

## 3. Official Regulatory Sources

### 3.1 OSS-RBA / KBLI / NIB

- OSS: https://oss.go.id/en
- KBLI 63102 official page: https://oss.go.id/kbli/detail/4be9f0ac-583b-5323-9839-7372e1708032
- KBLI 63101 data processing page: https://oss.go.id/kbli/detail/cb1de852-fa0f-4ef2-adce-a001ad258d0d
- Industrial-estate business-location page: https://oss.go.id/id/lokasi-usaha
- RDTR Interaktif: https://oss.go.id/en/rdtr-interaktif

Method:
1. Start with legal entity names from operator pages and filings: `PT Amazon Data Services Indonesia`, `PT Microsoft Indonesia`, `PT Google Cloud Indonesia`, `PT Alibaba Cloud Indonesia`, `PT DCI Indonesia Tbk`, `PT Telkom Data Ekosistem / NeutraDC`, `PT Sigma Cipta Caraka`, `PT NTT Global Data Centers Indonesia`, `PT Equinix Indonesia`, `PT Graha Teknologi Nusantara`, `PT STT GDC Indonesia`, `PT Princeton Digital Group Data Centres`, `PT Digital Edge DC`, `PT BDx Data Centers`, `PT DayOne Data Centers`, `PT Equator Gate System Batam`.
2. Use OSS/NIB facts to confirm the entity's licensed business activities and KBLI, not to count facility capacity.
3. For site candidates, use RDTR Interaktif / RTR map to test whether the parcel is in an industrial, commercial, telecommunication, office, or special economic zone compatible with datacenter use.

Grade: **A** for NIB / KBLI / RDTR / KKPR facts; **B** for facility inference unless project name or parcel is visible.

### 3.2 SIMBG / PBG / SLF Building Trail

- SIMBG: https://simbg.pu.go.id/
- Purpose: **Persetujuan Bangunan Gedung (PBG)** before construction and **Sertifikat Laik Fungsi (SLF)** before/for use.

Method:
1. For every candidate project, search the city/regency DPMPTSP and public-works pages before SIMBG because many SIMBG records are not easily indexed.
2. Query by operator, project code, estate, and exact address: `JK1`, `JK6`, `H1`, `H2`, `JKT3`, `JKT2A`, `CGK`, `Nongsa Digital Park`, `GIIC`, `MM2100`, `Kabil`, `Ariobimo`, `Kuningan Barat`.
3. Extract owner, building function, address, floor area, permit date, construction/operation status, and SLF status.

Grade: **A** for PBG/SLF or local DPMPTSP permit publications; **B/C** for unverified building photos or contractor portfolio pages.

### 3.3 AMDALNET / Environmental Approval

- AMDALNET: https://amdalnet.menlhk.go.id/
- Ministry context: KLHK / Ministry of Environment and Forestry. Search terms: `AMDAL`, `UKL-UPL`, `Persetujuan Lingkungan`, `PKPLH`, `RKL-RPL`.

Method:
1. Search for `pusat data`, `data center`, `infrastruktur komputasi`, operator legal names, industrial estate names, and power-substation names.
2. Where AMDALNET search is weak, web-search indexed PDFs and local DLH / provincial environment pages.
3. Capture project proponent, activity type, location, land area, gross floor area, power / generator capacity, water use, wastewater, hazardous waste, consultation dates, and approval status.

Grade: **A** for environmental documents and approvals; **B** when a credible news source reports environmental approval without a document.

### 3.4 Komdigi / Kominfo PSE Trail

- Komdigi services page: https://www.komdigi.go.id/layanan
- PSE Lingkup Privat: https://pse.komdigi.go.id/
- PSE search: https://pse.komdigi.go.id/pse
- PSE Lingkup Publik: https://pse.layanan.go.id/beranda
- Komdigi data portal: https://data.komdigi.go.id/

Use:
1. Search the PSE private registry for cloud, hosting, SaaS, marketplace, CDN, and enterprise-cloud entities. This confirms regulated electronic-system-provider presence in Indonesia.
2. Search PSE public registry and LKPP for government data centers, disaster-recovery sites, and cloud migrations.
3. Do **not** treat PSE registration as a physical datacenter record. It is best for legal-entity discovery and regulated service status.

Grade: **A** for PSE registration / legal entity facts; **B/C** for facility inference unless joined to permits, PLN, or official facility pages.

---

## 4. PLN / Power Enumeration

Power is one of the strongest Indonesia filters because commercial hyperscale sites usually need large PLN/PLN Batam supply.

Primary sources:
- PLN main / media pages: https://web.pln.co.id/
- PLN customer services / REC: https://layanan.pln.co.id/
- PLN e-procurement: https://eproc.pln.co.id/
- PLN Batam / Batam utility trail: search `site:plnbatam.com data center PJBTL` and official PLN Batam social / press posts.

High-value evidence types:
- **PJBTL**: Perjanjian Jual Beli Tenaga Listrik / electricity sale-purchase agreement.
- Large-load connection in **MVA** and phased energization dates.
- Substation / feeder / transformer / GIS works tied to an operator or industrial estate.
- Renewable Energy Certificate procurement or green-power PPA naming the data-center customer.

Known official / strong examples to seed:
- PLN / PLN Batam + DayOne: public reporting and DayOne official page describe a landmark **511 MVA / about 450 MW** Batam power agreement with PT PLN Batam for DayOne's Batam expansion. DayOne official source: https://dayonedc.com/markets/dayone-signs-indonesias-largest-511mva-450mw-ppa-to-expand-hyperscale-data-center-platform-in-batam. Treat DayOne as **A** for operator disclosure; require PLN/PLN Batam source for fully official utility grade.
- Batam / Nongsa and Kabil are high priority because PLN Batam agreements are being disclosed with customer names and MVA.
- West Java / Bekasi / Cikarang / Karawang are high priority because GIIC, MM2100, KIIC, and Karawang industrial estates concentrate hyperscale loads.

Query workflow:
1. For each candidate operator, search `"{operator}" "PJBTL"`, `"{operator}" "MVA"`, `"{operator}" "PLN"`, and `"{operator}" "pasok listrik"`.
2. Search by industrial estate: `"GIIC" "data center" "PLN"`, `"MM2100" "data center" "PLN"`, `"Nongsa" "data center" "PLN Batam"`, `"Kabil" "data center" "PLN Batam"`.
3. Use PLN e-procurement for substation / feeder works; grade **B** unless the tender names the datacenter customer.

---

## 5. Official Cloud Provider Region Pages

Cloud regions prove operational market presence and focus the search on Greater Jakarta / West Java / Banten and sometimes Batam. They do not reveal all physical sites.

| Provider | Official URL | Indonesia footprint | Enumeration value |
|---|---|---|---|
| AWS | https://aws.amazon.com/local/jakarta/ and region table https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | Asia Pacific (Jakarta), `ap-southeast-3`, **3 AZs** | Grade **A** for Jakarta region / AZ count. Search Amazon Data Services Indonesia, `ap-southeast-3`, `CGK`, Bekasi, Karawang, Cikarang, PLN, PBG, AMDAL. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and launch https://news.microsoft.com/id-id/2025/05/27/microsoft-opens-indonesia-central/ | **Indonesia Central**, Jakarta, region code `indonesiacentral`, 3 availability zones at GA | Grade **A** for Indonesia Central cloud region. Search Microsoft Indonesia, Karawang / GIIC / KIIC / `JKT09`, PLN, PBG, AMDAL. |
| Google Cloud | https://cloud.google.com/blog/products/infrastructure/new-google-cloud-region-in-jakarta-now-open and Indonesia update https://blog.google/intl/id-id/products/cloud/google-cloud-perluas-kapasitas-pusat-data-ai-di-indonesia/ | Jakarta cloud region, first Google Cloud region in Indonesia; later capacity expansion for AI-ready services | Grade **A** for Jakarta region / capacity expansion statement. Search PT Google Cloud Indonesia, Jakarta / West Java, PLN, permits. |
| Alibaba Cloud | https://www.alibabacloud.com/en/global-locations and region docs https://www.alibabacloud.com/help/en/cloud-migration-guide-for-beginners/latest/regions-and-zones | Indonesia (Jakarta), `ap-southeast-5`, 3 zones listed in current docs | Grade **A** for region/zone metadata. Search Alibaba Cloud Indonesia, Jakarta, DCI / local colo partners, PSE, PLN. |

Other providers to track from official pages when expanding beyond the brief: Huawei Cloud Indonesia, Tencent Cloud, Oracle Cloud, local CSPs (Telkom / NeutraDC, Lintasarta, Biznet Gio, Moratelindo / NDC, Indonet, IDC Indonesia).

---

## 6. Official Colo / Operator Sources to Seed

Use operator facility pages as **A** for named facilities, city/province, disclosed IT load, and operational status. Use them as seeds for permit / PLN searches.

### 6.1 NTT DATA / NTT Global Data Centers Indonesia

- Jakarta overview: https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/asia-pacific/jakarta-data-centers
- Jakarta 2: https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/asia-pacific/jakarta-2-data-center
- Jakarta 2 Annex: https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/asia-pacific/jakarta-2a-data-center
- Jakarta 3: https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/asia-pacific/jakarta-3-data-center
- Uptime awards page: https://uptimeinstitute.com/uptime-institute-awards/client/pt-ntt-global-data-centers-indonesia-/900

Seed facts: Jakarta 2 in central Jakarta; Jakarta 2A in central Jakarta with disclosed critical IT load / IT space; Jakarta 3 in Bekasi with up to **45 MW IT load** and 18,000 m2 IT space. Search terms: `JKT2`, `JKT2A`, `JKT3`, `PT NTT Global Data Centers Indonesia`, `MM2100`, `Bekasi`, `Kuningan Barat`.

### 6.2 Telkom Sigma / Telkom / NeutraDC / neuCentrIX

- Telkomsigma: https://www.telkomsigma.co.id/
- NeutraDC locations / facilities: https://www.neutradc.com/
- neuCentrIX locations: https://neucentrix.telkom.co.id/en/location
- Example Telkom official launch pages are often under Telkom / mycarrier / neuCentrIX domains; search exact city names.

Seed facts: Telkom group is the main national edge and enterprise datacenter source. It has hyperscale NeutraDC campuses and many neuCentrIX city facilities. Use official pages for locations and rack counts where disclosed; use PLN / PBG for MW and status.

High-priority terms: `NeutraDC Cikarang`, `NeutraDC Serpong`, `NeutraDC Surabaya`, `NeutraDC Batam`, `neuCentrIX Tanjung Karang`, `neuCentrIX Pugeran`, `neuCentrIX Pekanbaru`, `neuCentrIX Banjarmasin`, `neuCentrIX Medan`, `neuCentrIX Manado`, `neuCentrIX Makassar`, `neuCentrIX Jayapura`.

### 6.3 DCI Indonesia

- Main: https://dci-indonesia.com/
- Data centers: https://www.dci-indonesia.com/data-centers
- News: https://www.dci-indonesia.com/news
- Karawang H2 official release: https://www.dci-indonesia.com/news/dci-indonesia-and-salim-group-inaugurate-second-data-center-in-karawang-pioneering-the-first-solar-powered-data-center-in-indonesia

Seed facts: DCI officially lists / announces a platform across Jakarta, Cibitung, Karawang, and Surabaya. Public pages identify **E1 downtown Jakarta 19 MW**, **E2 Surabaya 9 MW**, H1 Cibitung facilities including JK6, and H2 Karawang campus. Search `PT DCI Indonesia Tbk`, `H1`, `H2`, `JK6`, `Ariobimo`, `MM2100`, `Karawang`, `Surabaya`, `PLN`.

### 6.4 Equinix

- Indonesia overview: https://www.equinix.com/data-centers/asia-pacific-colocation/indonesia-colocation
- Jakarta overview: https://www.equinix.com/data-centers/asia-pacific-colocation/indonesia-colocation/jakarta-data-center
- JK1 facility: https://www.equinix.com/data-centers/asia-pacific-colocation/indonesia-colocation/jakarta-data-center/jk1
- JK1 launch / newsroom: https://newsroom.equinix.com/2025-05-15-Equinix-Unveils-Its-First-AI-Ready-Data-Center-with-Dense-Ecosystem-in-Jakarta

Seed facts: Equinix JK1 is in Jakarta's CBD / Kuningan Barat and opened in 2024/2025 materials; official specs disclose colocation area and building details, while newsroom discloses phase cabinets and full buildout cabinets/sqm. Search `PT Equinix Indonesia`, `JK1`, `Kuningan Barat`, `PBG`, `SLF`, `PLN`.

---

## 7. Province-First Enumeration Approach

Run provinces in tiers. Within each province, bucket to city/regency because Indonesian permits are often city/regency/DPMPTSP or industrial-estate based.

### Tier 1 — Hyperscale / Cloud / Colo Core

| Province / region | Why high priority | Official-first workflow |
|---|---|---|
| **Jakarta** | Cloud-region market label; NTT JKT2/JKT2A, Equinix JK1, DCI E1, Digital Edge, SM+ and enterprise colos | Search DKI DPMPTSP/JAKI/Jakarta building permits, SIMBG/PBG/SLF, Komdigi PSE, PLN UID Jakarta, operator facility pages. Query `Kuningan Barat`, `Ariobimo`, `Karet Tengsin`, `CBD`, `Jakarta Selatan`. |
| **West Java** | Bekasi/Cikarang/Karawang hyperscale belt: DCI H1/H2, NTT JKT3, STT, PDG, Digital Edge, Microsoft/AWS candidate campuses | Search Bekasi/Karawang DPMPTSP, GIIC/MM2100/KIIC/Jababeka estate pages, PLN UID Jawa Barat, AMDALNET, SIMBG. Query `GIIC`, `MM2100`, `Cibitung`, `Cikarang`, `Karawang`, `Kutanegara`. |
| **Banten** | South Tangerang / Serpong / BSD enterprise and colo cluster | Search Tangerang Selatan / Kabupaten Tangerang / Banten DPMPTSP, BSD / Technopark estate pages, PLN Banten, SIMBG. Query `Serpong`, `BSD`, `Pondok Aren`, `Technopark`, `NeutraDC`. |
| **Riau Islands** | Batam / Nongsa / Kabil hyperscale and Singapore-adjacent grid/fiber market | Search BP Batam, Nongsa Digital Park, Kabil Industrial Estate, PLN Batam PJBTL, OSS SEZ / industrial-location pages, AMDALNET. Query `Nongsa`, `Kabil`, `DayOne`, `NeutraDC Nxera`, `Equator Gate System`, `Altiva`, `PLN Batam`. |
| **East Java** | Surabaya as eastern Indonesia interconnection hub; DCI E2, Telkom/NeutraDC, NDC | Search Surabaya / East Java DPMPTSP, PLN UID Jawa Timur, local building permits, DCI and Telkom pages. Query `Surabaya`, `Citraland`, `Lakarsantri`, `E2`, `pusat data`. |

### Tier 2 — Edge / Government / Regional Hub Provinces

Prioritize provinces with official Telkom/neuCentrIX, NDC, government data-center, or strong procurement evidence:

- **North Sumatra**: Medan; search `neuCentrIX Medan`, `NDC Medan`, `Pusat Data Sumut`, PLN Sumut.
- **South Sulawesi**: Makassar; search `neuCentrIX Makassar`, `IDC Makassar`, `Menara Bosowa`, provincial LPSE.
- **Lampung**: Telkom official neuCentrIX Tanjung Karang launch; search Telkom, DPMPTSP Bandar Lampung, PLN Lampung.
- **Special Region of Yogyakarta**: neuCentrIX Pugeran / Kotabaru; search Telkom official pages and DIY LPSE.
- **Riau**: neuCentrIX Pekanbaru; search Telkom launch pages and PLN Riau.
- **South Kalimantan**: neuCentrIX Banjarmasin-Ulin; search Telkom pages and Kalimantan LPSE.
- **Bali**: NDC / edge colos and government systems; search Denpasar DPMPTSP, Bali LPSE, Moratelindo/NDC.
- **Central Java**: provincial government data center and Semarang edge facilities; search Jatengprov, Semarang DPMPTSP, LPSE.
- **East Kalimantan**: IKN / Sepaku / Balikpapan digital infrastructure; search OIKN, Kominfo/Komdigi, Telkom, PLN Kaltim.

### Tier 3 — Low-Recall Provinces

For provinces with no known commercial hyperscale footprint, run a government/edge sweep:

```
"{province}" "pusat data" "Diskominfo"
"{province}" "data center" "LPSE"
"{province}" "pusat data" "provinsi"
"{capital_city}" "neuCentrIX"
"{capital_city}" "Nusantara Data Center"
"{capital_city}" "PBG" "pusat data"
site:{province_go_id_domain} "pusat data"
site:spse.inaproc.id "{province}" "pusat data"
```

Treat "no projects" only after checking: official provincial/city government, LPSE/SPSE/SIRUP, Telkom/neuCentrIX location page, DataCenterMap/Baxtel as weak leads, and local news.

---

## 8. Evidence Extraction Rules

For each candidate record, extract:

- Legal entity / project proponent and brand/operator.
- Facility name/code: e.g. `JK1`, `JKT3`, `JKT2A`, `H1-JK6`, `H2-02`, `E1`, `E2`, `CGK1`, `Indonesia Central`.
- Province, city/regency, district, industrial estate / SEZ / building name, address or coordinates.
- Status: planned, permitting, construction, operational, expansion, cancelled/paused.
- Capacity: IT load MW, utility MVA, racks/cabinets, colocation area, land area, gross floor area. Keep units separate; do not convert MVA to MW unless source does.
- Official evidence: OSS/KBI/NIB, RDTR/KKPR, PBG/SLF, AMDAL/UKL-UPL, PLN PJBTL, cloud-region page, operator facility page, public-company filing.
- Evidence date and confidence grade.

Do not count cloud availability zones as individual facilities unless a source identifies physical campuses. Do not count PSE registration as a datacenter. Do not count government "Pusat Data Nasional" / ministry data-center procurements as commercial colocation unless the facility is externally serviceable.

---

## 9. Practical Validation Stack

Use this order for each candidate:

1. **Operator official page or cloud-region page**: establishes existence and market/province. Grade **A** for disclosed facts.
2. **PLN / PLN Batam**: confirms large-load seriousness and power scale. Grade **A** when named.
3. **SIMBG / DPMPTSP / PBG / SLF / RDTR / KKPR**: confirms construction and lawful building use. Grade **A**.
4. **AMDALNET / environmental approval**: confirms siting, project proponent, and physical characteristics. Grade **A**.
5. **Komdigi PSE and OSS KBLI**: confirms legal entity / regulated service activity. Grade **A** for registry facts only.
6. **Trade press / Antara / DCD**: use as **B** bridge when official pages are silent, then pivot to official evidence.
7. **Aggregators**: use as **C** only, mainly to discover addresses and alternate facility names.

---

## 10. High-Value Source List

Government / regulator:
- OSS-RBA: https://oss.go.id/en
- OSS KBLI 63102: https://oss.go.id/kbli/detail/4be9f0ac-583b-5323-9839-7372e1708032
- OSS RDTR Interaktif: https://oss.go.id/en/rdtr-interaktif
- SIMBG / PBG / SLF: https://simbg.pu.go.id/
- AMDALNET: https://amdalnet.menlhk.go.id/
- Komdigi: https://www.komdigi.go.id/
- PSE Privat: https://pse.komdigi.go.id/
- PSE Publik: https://pse.layanan.go.id/beranda
- LKPP: https://www.lkpp.go.id/
- SPSE / Inaproc: https://spse.inaproc.id/
- SIRUP: https://sirup.lkpp.go.id/
- PLN: https://web.pln.co.id/
- PLN e-procurement: https://eproc.pln.co.id/
- PLN services / REC: https://layanan.pln.co.id/

Cloud / operator:
- AWS Jakarta: https://aws.amazon.com/local/jakarta/
- AWS region table: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Microsoft Indonesia Central launch: https://news.microsoft.com/id-id/2025/05/27/microsoft-opens-indonesia-central/
- Google Cloud Jakarta launch: https://cloud.google.com/blog/products/infrastructure/new-google-cloud-region-in-jakarta-now-open
- Google Indonesia capacity update: https://blog.google/intl/id-id/products/cloud/google-cloud-perluas-kapasitas-pusat-data-ai-di-indonesia/
- Alibaba global locations: https://www.alibabacloud.com/en/global-locations
- Alibaba regions/zones docs: https://www.alibabacloud.com/help/en/cloud-migration-guide-for-beginners/latest/regions-and-zones
- NTT Jakarta data centers: https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/asia-pacific/jakarta-data-centers
- Telkomsigma: https://www.telkomsigma.co.id/
- NeutraDC: https://www.neutradc.com/
- neuCentrIX: https://neucentrix.telkom.co.id/en/location
- DCI Indonesia: https://www.dci-indonesia.com/data-centers
- Equinix Indonesia: https://www.equinix.com/data-centers/asia-pacific-colocation/indonesia-colocation
- Equinix JK1: https://www.equinix.com/data-centers/asia-pacific-colocation/indonesia-colocation/jakarta-data-center/jk1
