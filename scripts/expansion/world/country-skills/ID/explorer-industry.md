# ID Explorer - Industry, Trade Press, Vendors, and Province Query Patterns

Date: 2026-08-12. Scope: Indonesia datacenter enumeration through industry/trade press, Indonesian search patterns, vendor/operator pages, cloud-region pages, industrial-estate signals, and province-by-province discovery routes. Reliability grades: **A** = primary/operator/government/cloud-region/stock-exchange/permit evidence; **B** = established trade press, Antara, major Indonesian business press, broker report with named projects; **C** = aggregator, directory, social media, unsourced market list, promotional MOU without follow-up.

---

## 0. Indonesia-specific frame

- Indonesia has no single public datacenter facility registry. Enumeration works by triangulating: operator location pages, hyperscaler region pages, DCD/W.Media/Antara/Bisnis/Kontan/CNBC Indonesia/DetikInet/Kompas Tekno articles, industrial-estate pages, PLN or PLN Batam power agreements, APJII/IIX ecosystem announcements, Uptime certificates, OSS/KBLI licensing clues, and local government investment releases.
- The core commercial geography is not "all provinces equally." Prioritize **Jakarta**, **West Java** (Bekasi, Cikarang, Cibitung, Karawang, GIIC, MM2100, Jababeka, Deltamas), **Banten** (South Tangerang, Serpong, BSD, Tangerang), **Riau Islands** (Batam, Nongsa Digital Park, Kabil Industrial Estate, Batamindo), and **East Java** (Surabaya). Secondary hubs: **Bali/Denpasar**, **North Sumatra/Medan**, **South Sulawesi/Makassar**, **Riau/Pekanbaru**, **Lampung/Bandar Lampung**, **Aceh/Banda Aceh**, **Yogyakarta**, **South Kalimantan/Banjarmasin**, **North Sulawesi/Manado**, **Papua/Jayapura**.
- Many "Jakarta" announcements are physically in **Bekasi Regency, West Java** or **South Tangerang, Banten**. Always resolve the municipality/province from the address or industrial estate: Cikarang/Cibitung/Karawang/Purwakarta = West Java; Serpong/BSD/Pondok Aren/South Tangerang = Banten; Kuningan/MT Haryono/TB Simatupang/CBD = Jakarta.
- Indonesian sources use both English **data center** and Indonesian **pusat data**. Also search **data centre**, **datacenter**, **DC**, **kolokasi**, **colocation**, **pusat data nasional**, **PDN**, **hyperscale**, **AI-ready**, **pusat data AI**, **kawasan ekonomi khusus**, **KEK**, **kawasan industri**, **beban IT**, **kapasitas MW**, **MVA**, **PLN**, **PJBTL**, **gardu induk**, **groundbreaking**, **peletakan batu pertama**, **topping out**, **beroperasi**, **diresmikan**, **diluncurkan**.
- Indonesian official/investor language often overstates long-term campus buildout. Record stage verbs exactly: `minat investor`, `MoU`, `kerja sama`, `akuisisi lahan`, `kontrak listrik/PJBTL`, `groundbreaking`, `topping out`, `ready for service`, `launched/opened`, `beroperasi`.

---

## 1. High-signal industry and trade press

Use these sources as the live discovery feed, then verify projects against operator releases, cloud docs, industrial-estate pages, PLN power deals, or local government/permit sources.

| Source | URL / query route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) Indonesia tag/search | `https://www.datacenterdynamics.com/en/news/?tag=indonesia`, `site:datacenterdynamics.com/en/news Indonesia "data center"` | Best English trade feed for DCI, STT GDC, Digital Edge, PDG, BDx, NeutraDC, NTT, Edgnex, Batam/Nongsa, power agreements, construction milestones. | B+ |
| W.Media | `https://w.media/`, `site:w.media Indonesia "data center"` | APAC datacenter news, power deals, capacity shortfall narratives, vendor interviews. Good discovery; verify capacities. | B |
| Antara / Antara Kepri | `https://www.antaranews.com/`, `https://kepri.antaranews.com/` | Strongest public Indonesian wire for Batam, ministries, BP Batam, PLN Batam, provincial government claims. Good for official quotes but still distinguish investor interest from real projects. | B+ |
| Bisnis Indonesia / Bisnis.com | `site:bisnis.com "data center" Indonesia`, `site:teknologi.bisnis.com "pusat data"` | Business/property/investment reporting; good for listed Indonesian developers and industrial estate operators. | B |
| Kontan | `site:kontan.co.id "data center" Telkom Indonesia`, `site:kontan.co.id "pusat data"` | Useful for Telkom/NeutraDC/neuCentrIX rollouts, listed-company capex, operator strategy. | B |
| CNBC Indonesia | `site:cnbcindonesia.com "data center" Indonesia`, `site:cnbcindonesia.com "pusat data"` | Market/investment-policy feed; good for ministerial quotes and large-capacity claims. | B-/C+ |
| DetikInet / DetikFinance | `site:inet.detik.com "data center"`, `site:finance.detik.com "pusat data"` | Good Indonesian tech beat for Telkom launches, PDN incident context, local operator announcements. | B |
| Kompas Tekno / Kompas regional | `site:tekno.kompas.com "data center"`, `site:regional.kompas.com "pusat data" "{province}"` | Useful for national tech/policy and provincial public-sector data center stories. | B |
| Katadata, Tech in Asia ID, DailySocial | `site:katadata.co.id "pusat data"`, `site:dailysocial.id "data center"` | Startup/cloud/economy context, older cloud-region policy reporting. | B-/C+ |
| IDNFinancials / IDX issuer pages | `site:idnfinancials.com "data center" Indonesia`, issuer domains | Helpful for Indonesian-listed operators/developers: DCI, Telkom, Indosat, Puradelta Lestari, Jababeka, Sinar Mas/LG JV. | B unless direct filing |
| Data Center Map / Baxtel / OCOLO / Cloudscene / PeeringDB / Inflect | source sites | Facility address and interconnection cross-checks, especially edge DCs. Never use alone for final MW/status unless no better source exists. | C, sometimes B when sourced |

Trade-press queries:

```text
site:datacenterdynamics.com/en/news Indonesia "{operator}" "data center"
site:datacenterdynamics.com/en/news Indonesia "{city}" ("MW" OR "MVA" OR "IT load")
site:w.media Indonesia "{operator}" ("data center" OR "pusat data")
site:antaranews.com "{province_or_city}" ("data center" OR "pusat data")
site:kepri.antaranews.com Batam ("data center" OR "pusat data" OR "PLN Batam" OR "PJBTL")
site:bisnis.com "{operator}" "data center"
site:kontan.co.id "{operator}" "data center"
site:inet.detik.com "neuCentrIX" "{city}"
site:cnbcindonesia.com "pusat data" Batam
```

Use press as **B** for event discovery. Upgrade only when the article embeds a company release, stock filing, PLN contract, government statement from BP Batam/Kominfo/Coordinating Ministry, or facility spec page.

---

## 2. Indonesian search vocabulary and patterns

Core nouns:

```text
data center
data centre
datacenter
pusat data
pusat data nasional
PDN
kolokasi
colocation
pusat kolokasi
cloud region
region cloud
komputasi awan
pusat data AI
AI data center
server farm
ruang server
fasilitas pusat data
infrastruktur digital
internet exchange
IIX
```

Status/evidence words:

```text
dibangun
membangun
pembangunan
groundbreaking
peletakan batu pertama
topping out
siap beroperasi
ready for service
beroperasi
diresmikan
diluncurkan
komersialisasi
akuisisi lahan
pembebasan lahan
kontrak listrik
PJBTL
perjanjian jual beli tenaga listrik
pasokan listrik
MVA
MW
beban IT
kapasitas
gardu induk
substation
PLN
PLN Batam
AMDAL
Persetujuan Lingkungan
PBG
SLF
OSS
NIB
KBLI
```

National discovery templates:

```text
"{operator}" Indonesia ("data center" OR "pusat data") ("MW" OR "MVA" OR "beban IT")
"{operator}" "{city}" ("data center" OR "pusat data") ("beroperasi" OR "diresmikan" OR "diluncurkan")
"{operator}" "{industrial_estate}" ("data center" OR "pusat data")
"{city}" ("data center" OR "pusat data") ("PLN" OR "PJBTL" OR "MVA" OR "gardu induk")
"{city}" ("data center" OR "pusat data") ("groundbreaking" OR "peletakan batu pertama" OR "topping out")
"{city}" ("data center" OR "pusat data") ("KEK" OR "kawasan ekonomi khusus" OR "kawasan industri")
"{province}" ("data center" OR "pusat data") ("investor" OR "minat" OR "MoU" OR "kerja sama")
```

Operator-domain templates:

```text
site:{operator-domain} Indonesia ("data center" OR "pusat data" OR "locations")
site:{operator-domain} "{city}" ("MW" OR "IT load" OR "rack" OR "sqm")
site:{operator-domain} "{facility}" ("launched" OR "opened" OR "inaugurated" OR "ready for service")
```

Official-ish trail:

```text
site:oss.go.id "63112" "data center"
site:oss.go.id "63122" "data center"
site:amdalnet.menlhk.go.id "pusat data"
site:menlhk.go.id "pusat data" "AMDAL"
site:pln.co.id "{operator}" ("data center" OR "pusat data" OR "MVA")
site:plnbatam.com "{operator}" ("data center" OR "pusat data" OR "PJBTL")
site:bpbatam.go.id "data center" Batam
site:bkpm.go.id "data center" Indonesia
site:investindonesia.go.id "data center" Indonesia
site:idx.co.id "{issuer}" "data center"
site:idxchannel.com "{issuer}" "data center"
```

Stage interpretation:

- `minat investor`, `antre`, `potensi`, `target kapasitas`, `diproyeksikan` = market/pipeline context only, **C**.
- `MoU`, `kerja sama`, `rencana investasi` = intent, **C/B-** depending on counterparty.
- `akuisisi lahan`, `land acquired`, `kawasan industri`, `tenant` = land signal, **B** if from developer/operator, **A-** if from official estate filing.
- `PJBTL`, `PPA`, `pasokan listrik`, `MVA`, `PLN Batam` = strong buildout/power signal, **A-/B+**.
- `groundbreaking`, `peletakan batu pertama`, `topping out` = construction milestone, **B+** if trade press, **A** if operator.
- `diresmikan`, `diluncurkan`, `beroperasi`, `commercialized`, `ready-for-service` = operational signal; verify with operator facility page where possible.

---

## 3. Industry associations, exchanges, events, and market reports

| Body / source | URL | Use | Grade |
|---|---|---|---|
| APJII (Asosiasi Penyelenggara Jasa Internet Indonesia) | `https://apjii.or.id/`, IIX pages/news | Internet exchange ecosystem, IIX nodes in datacenters, ISP demand, partner announcements such as BDx/APJII. Use as connectivity seed. | A-/B |
| Indonesia Internet Exchange / IIX | `https://www.iix.net.id/` | Cross-check exchange nodes and carrier hotels; useful for Jakarta/Bekasi/Batam interconnection. | A-/B |
| IDPRO / Indonesian Data Center Provider Organization | LinkedIn/news/events; search `"IDPRO" "data center" Indonesia` | Association/member ecosystem and regulatory discussions around PP 71/2019 and Personal Data Protection Law. Not a facility registry. | B-/C+ |
| Uptime Institute awards | `https://uptimeinstitute.com/uptime-institute-awards/list` | Certifies named facilities and locations for DCI, NTT, NeutraDC, etc. A for certification existence, not complete capacity. | A |
| DCD>Connect APAC / Data Center Asia Indonesia / Cloud & Datacenter Convention | event pages and exhibitor/speaker lists | Good for active developers/vendors and emerging Batam/Jakarta players. | B-/C+ |
| Mordor, Arizton, Cushman & Wakefield, CBRE, JLL, Knight Frank, Structure Research | site-scoped report queries | Market capacity, city rankings, power constraints, pipeline context. Use facility names only when explicitly stated. | B |

Search templates:

```text
site:apjii.or.id ("data center" OR "pusat data" OR "IIX") "{operator}"
"APJII" "{operator}" "data center"
"IDPRO" "data center" Indonesia
site:uptimeinstitute.com "Indonesia" "{operator}" "Data Center"
"Indonesia data center market" "Jakarta" "Batam" "MW" "Cushman"
"Indonesia data center" "Bekasi" "Cikarang" "JLL"
```

---

## 4. Major operators, developers, and vendor pivots

Official pages are **A** for marketed locations/current claimed presence. Treat rounded campus capacity and long-term GW narratives as **B** unless backed by a named facility, power contract, filing, or certification.

| Operator / developer | Primary URL(s) | Indonesia location signals | Grade notes |
|---|---|---|---|
| DCI Indonesia | `https://dci-indonesia.com/`, news `https://www.dci-indonesia.com/news` | Jakarta E1, Cibitung H1 campus, Karawang H2 campus, Surabaya E2; official news says JK6 is 36 MW and E2 Surabaya is 9 MW. | A for DCI pages and IDX filings; B for trade pipeline. |
| NeutraDC / Telkom Data Ekosistem | `https://www.neutradc.com/`, `https://www.neutradc.com/about-us`, `https://www.neutradc.com/data-center/jakarta-hq`, `https://www.neutradc.com/data-center/batam` | Cikarang hyperscale, Batam with Nxera/Singtel/Medco, enterprise DCs in Sentul/Serpong/Surabaya, 19 neuCentrIX edge locations. | A for own pages; use Telkom annual reports for capex/corporate proof. |
| neuCentrIX / Telkom Indonesia | `https://neucentrix.telkom.co.id/en/location`, Telkom/Telin news | Edge DCs in many provincial capitals: Banda Aceh, Medan, Pekanbaru, Batam, Lampung, Bandung, Semarang/Yogyakarta, Banjarmasin, Makassar, Manado, Jayapura, etc. | A for official location pages and Telkom releases; capacity often only racks or undisclosed. |
| ST Telemedia Global Data Centres Indonesia | `https://www.sttelemediagdc.com/id-en`, locations `https://www.sttelemediagdc.com/id-en/locations` | STT Jakarta campus in GIIC/Cikarang, Bekasi; STT Jakarta 2/3/5/6 expansions reported, 360 MW long-term campus narrative. | A for official pages/factsheets; B for DCD milestones. |
| Princeton Digital Group (PDG) | `https://princetondg.com/locations/indonesia/`, JC3 release `https://princetondg.com/newsroom/princeton-digital-group-breaks-ground-on-milestone-usd-1-billion-120-mw-greater-jakarta-campus/` | JC1/JC2 in MM100 Cibitung; JC3 in GIIC Kota Deltamas; JC4 powered land; legacy XL Axiata portfolio in Pekanbaru, Cibitung, Surabaya, Bintaro, Bandung; Batam/Nongsa campus. | A for own location/release; verify legacy sites and exact province by address. |
| Digital Edge / EDGE DC | `https://www.digitaledgedc.com/`, Indonesia `https://id.digitaledgedc.com/`, CGK campus release `https://www.digitaledgedc.com/resources/newsroom/digital-edge-4-5b-cgk-500mw-ai-ready-hyperscale-campus-indonesia/` | EDGE1/EDGE2 in Jakarta; CGK Campus at GIIC, Bekasi, planned 500 MW full buildout, first phase Q4 2026 target. | A for official facility pages; B for future full-build capacity. |
| BDx Data Centers Indonesia | `https://www.bdxworld.com/locations/cgk3-south-jakarta/`, `https://www.bdxworld.com/locations/cgk4-jatiluhur/` | CGK3 South Jakarta, CGK4 Jatiluhur/Purwakarta area, APJII IIX-JK2 partnership, Indosat/Lintasarta portfolio acquisition. | A for BDx pages; B for BusinessWire/DCD campus scale. |
| DayOne / GDS International | `https://dayonedc.com/market/batam` | 72 MW Nongsa Digital Park campus; Kabil expansion and PLN Batam 511 MVA power deal reported. | A for own Batam page; B for power-deal/trade press unless official PPA release. |
| NTT Global Data Centers Indonesia | `https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/asia-pacific/jakarta-2-data-center`, `.../jakarta-2a-data-center` | Jakarta 2 and Jakarta 2 Annex in Central/South Jakarta; Jakarta 3 in Bekasi; NTT official gives JKT2 9.4 MW and JKT2A 12 MW. | A for NTT pages and Uptime list. |
| Equinix | `https://www.equinix.com/data-centers/asia-pacific-colocation/indonesia-colocation/jakarta-data-center`, JK1 page | JK1 in Jakarta CBD; 550 cabinets phase 1, 1,600 cabinets/5,300 sqm full build in company release. | A for Equinix pages/newsroom. |
| Edgnex / DAMAC | DCD/JLL/company news; search `Edgnex Indonesia Jakarta Cikarang` | Jakarta MT Haryono first site reported; Cikarang/Bekasi 144 MW project with land acquired. | B until official facility page or permit/land record is found. |
| Bitera | `https://bitera.co.id/` and DCD/Baxtel | Jakarta CBD facility often reported as 20 MW / 8,600 sqm. | A if own spec page; B/C via directories. |
| Digital Realty Bersama | `https://digitalrealty-bersama.com/`, Digital Realty JV release | Digital Realty/Bersama Digital Infrastructure Asia JV; APJII interconnection signals; facility list still developing. | A for JV formation; B/C for unnamed pipeline. |
| SM+ Data Centers / LG Sinar Mas | `https://smplus.com/`, Sinar Mas/DSSA release | SMX01 Jakarta CBD under construction; SM+ edge DCs across many provincial cities. | A for company/issuer releases; C for edge location pages if thin. |
| Moratelindo / Nusantara Data Center (NDC) | `https://www.napinfo.co.id/`, `https://www.moratelindo.co.id/` | NDC in Jakarta, Batam, Medan, Palembang, Surabaya, Denpasar/Bali and network-linked facilities. | A if official service page; C via directories. |
| Lintasarta / Indosat Ooredoo Hutchison | `https://www.lintasarta.net/`, `https://ioh.co.id/` | Legacy enterprise DCs; many assets folded into BDx Indonesia JV. | A for company disclosures; be careful not to double-count post-JV assets. |
| Datacomm / Datacomm Diangraha / MettaDC / IDC Indonesia / CenterServ / Mitrakom / Matrix NAP / SEAX / Racks Central / BW Digital / Data Center First / Gaw-Sinar Primera / RangeIDC | own domains plus DCD/Antara/directories | Regional and Batam providers, often with sparse capacity. | A when operator page has address/specs; C for directories/social-only. |

Vendor sweep:

```text
"DCI Indonesia" ("Cibitung" OR "Karawang" OR "Surabaya" OR "JK6") "MW"
"NeutraDC" ("Cikarang" OR "Batam" OR "Serpong" OR "Surabaya" OR "Sentul") "MW"
"neuCentrIX" "{city}" ("diluncurkan" OR "commercialized" OR "rack")
"STT Jakarta" ("GIIC" OR "Cikarang" OR "Bekasi") "MW"
"PDG" ("JC1" OR "JC2" OR "JC3" OR "JC4" OR "Batam") Indonesia
"Digital Edge" ("EDGE2" OR "CGK Campus" OR "Bekasi" OR "GIIC") Indonesia
"BDx" ("CGK3" OR "CGK4" OR "Jatiluhur" OR "APJII") Indonesia
"DayOne" ("Nongsa" OR "Kabil" OR "PLN Batam" OR "511MVA") Batam
"NTT" ("Jakarta 2" OR "Jakarta 2 Annex" OR "Jakarta 3" OR "Bekasi") Indonesia
"Equinix" "JK1" Jakarta Indonesia
```

---

## 5. Hyperscaler official region pages

Cloud-region pages prove operational cloud-region presence at city/region granularity, not physical facility ownership or exact address. Use as **A for cloud region existence**, then pivot to colo/operator/permit/power trails for physical sites.

| Provider | Official URL | Indonesia region signals |
|---|---|---|
| AWS | Launch `https://aws.amazon.com/blogs/aws/now-open-aws-asia-pacific-jakarta-region/`; region docs `https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html` | Asia Pacific (Jakarta), API `ap-southeast-3`, three AZs at launch. Physical CGK sites are not official-address-disclosed; directories and local reporting need verification. |
| Microsoft Azure | Launch `https://news.microsoft.com/id-id/2025/05/27/microsoft-opens-indonesia-central/`; region list `https://learn.microsoft.com/en-us/azure/reliability/regions-list` | Indonesia Central cloud region, Jakarta metro naming, three availability zones. Reporting points to Karawang/GIIC-style West Java builds; verify facility-level claims separately. |
| Google Cloud | Jakarta launch `https://cloud.google.com/blog/products/infrastructure/new-google-cloud-region-in-jakarta-now-open`; locations `https://cloud.google.com/about/locations`; Indonesia update `https://blog.google/intl/id-id/products/cloud/google-cloud-perluas-kapasitas-pusat-data-ai-di-indonesia/` | Jakarta cloud region opened in 2020; later AI-capacity expansion announced. Treat region as A, physical facility/vendor unknown unless sourced. |
| Oracle Cloud | `https://www.oracle.com/cloud/public-cloud-regions/` | Oracle lists Indonesia commercial cloud region(s) in Jakarta/Indonesia. Use official region list for cloud presence, not address. |
| Alibaba Cloud / Tencent Cloud / Huawei Cloud / Akamai / Cloudflare / IBM / SAP | official region/PoP pages | Usually colocated or PoP-based. Use as demand/interconnection signal and pivot to Equinix/NTT/BDx/Digital Edge/DCI/NeutraDC. |

Hyperscaler pivot:

```text
"AWS" Jakarta "data center" ("Cikarang" OR "Bekasi" OR "Karawang" OR "CGK")
"Microsoft" "Indonesia Central" ("Karawang" OR "GIIC" OR "Bekasi" OR "data center")
"Google Cloud" Jakarta "data center" Indonesia "AI"
"Oracle Cloud" Indonesia "Jakarta" "data center"
"{cloud provider}" Indonesia ("Equinix" OR "NTT" OR "DCI" OR "Digital Edge" OR "NeutraDC" OR "BDx")
```

---

## 6. Province enumeration matrix

Workflow for every province:

1. Search English and Indonesian terms with province, capital city, and main industrial estate names.
2. Search operator seeds (`neuCentrIX`, `NeutraDC`, `DCI`, `PDG`, `Digital Edge`, `BDx`, `NDC`, `SM+`, `Mitrakom`, `CenterServ`) plus the city.
3. Search power evidence (`PLN`, `PLN Batam`, `PJBTL`, `MVA`, `gardu induk`) and industrial-estate/SEZ pages.
4. Confirm whether results are commercial colo/hyperscale, telco edge DC, government PDN/provincial data center, or just an office/server room.
5. Grade directories as **C** unless corroborated by operator/press/official records.

### 6.1 Priority provinces and capital-region clusters

| Province / special region | Query localities | Developer/operator seeds | Query notes |
|---|---|---|---|
| Jakarta | Kuningan, CBD, MT Haryono, TB Simatupang, Cyber Building, Mampang, South Jakarta, Central Jakarta | Equinix JK1, NTT JKT2/JKT2A, DCI E1, Digital Edge EDGE1/EDGE2, BDx CGK3, Bitera, Edgnex, Moratelindo/NDC, Lintasarta, APJII/IIX | Query city district names. Do not assign Bekasi/Cikarang sites to Jakarta. Search `Jakarta Selatan pusat data`, `Kuningan data center`, `MT Haryono data center`, `IIX JK2`. |
| West Java | Bekasi, Cikarang, Cibitung, Karawang, Kota Deltamas, GIIC, MM2100, Jababeka, Purwakarta/Jatiluhur, Sentul/Bogor, Bandung | DCI H1/H2/JK6, STT Jakarta campus, PDG JC1/JC2/JC3/JC4, Digital Edge CGK, Microsoft Karawang, NTT JKT3, NeutraDC Cikarang/Sentul, BDx CGK4, Datacomm Cikarang, Edgnex Cikarang | Highest-yield province. Use estate names plus operator names. Search `site:deltamas.id data center`, `GIIC pusat data`, `MM2100 data center`, `Karawang data center Microsoft`, `Jatiluhur BDx`. |
| Banten | South Tangerang, Serpong, BSD, Pondok Aren, Tangerang, Cilegon | NeutraDC Serpong, BDx Technopark/BSD, PDG Bintaro/JB1, EDGE/SM+/NDC smaller sites | "Jakarta" directories may actually be Banten. Search `Serpong data center`, `BSD pusat data`, `Pondok Aren PDG`, `Tangerang Selatan pusat data`. |
| Riau Islands | Batam, Nongsa Digital Park, Kabil Industrial Estate, Batamindo, Tanjung Bemban, Bintan | DayOne/GDS, NeutraDC Nxera Batam, Data Center First, BW Digital, Racks Central, RangeIDC/EGSB, Gaw-Sinar Primera, Matrix NAP, NDC Batam, SEAX, BP Batam, PLN Batam | Batam is the main non-Java hyperscale cluster. Use Antara Kepri, BP Batam, NDP, PLN Batam, `PJBTL`, `MVA`, `KEK Nongsa`. Treat "investor antre" as pipeline only. |
| East Java | Surabaya, Citraland/Lakarsantri, Sidoarjo, Gresik, Malang | DCI E2 Surabaya, NeutraDC Surabaya, NDC Surabaya, PDG legacy Surabaya, IDC/CenterServ | Search `Surabaya data center 9 MW`, `pusat data Surabaya diresmikan`, `Citraland NeutraDC`, `East Java data center`. |
| Bali | Denpasar, Badung, Nusa Dua, Benoa | Moratelindo/NDC Bali, Edge Centres EC71, telco/DR sites | Mostly edge/enterprise. Search `Denpasar data center`, `pusat data Bali`, `NDC Bali`, `EC71 Bali`. |
| North Sumatra | Medan, Deli Serdang, Kualanamu | neuCentrIX Medan, NDC Medan, CenterServ Medan | Regional edge hub. Search `Medan data center`, `neuCentrIX Medan`, `pusat data Sumatera Utara`. |
| South Sulawesi | Makassar, Maros, Gowa | neuCentrIX Makassar, IDC Indonesia Makassar, SM+ Makassar, CenterServ | Eastern Indonesia interconnection hub. Search `Makassar data center`, `Menara Bosowa IDC`, `pusat data Sulawesi Selatan`. |

### 6.2 Other provinces and repeated query route

| Province | Query localities | Likely leads / notes |
|---|---|---|
| Aceh | Banda Aceh, Lhokseumawe | neuCentrIX Banda Aceh launched by Telkom. Search `neuCentrIX Banda Aceh`, `pusat data Aceh`, `data center Banda Aceh`. |
| Bangka Belitung Islands | Pangkalpinang, Tanjung Pandan | Low commercial likelihood; query government/DR and telco edge. `Pangkalpinang pusat data`, `Bangka Belitung data center`. |
| Bengkulu | Bengkulu city | Low likelihood; search Diskominfo/provincial data center and telco edge. |
| Central Java | Semarang, Solo/Surakarta, Kendal Industrial Park | Central Java provincial data center in Semarang; possible enterprise/edge. Search `pusat data Jateng`, `data center Semarang`, `Kendal Industrial Park data center`. |
| Central Kalimantan | Palangka Raya, Sampit | Mostly government/edge. Search `Palangka Raya pusat data`, `Kalimantan Tengah data center`. |
| Central Papua | Nabire, Timika | Very low commercial signal; search government/telecom only. |
| Central Sulawesi | Palu, Morowali | Possible industrial/mining edge, not hyperscale. Search `Palu data center`, `Morowali pusat data`, `kawasan industri Morowali data center`. |
| East Kalimantan | Balikpapan, Samarinda, Sepaku, Nusantara/IKN | neuCentrIX Sepaku/Balikpapan listings; IKN may create government/cloud/edge leads. Search `IKN pusat data`, `Sepaku data center`, `Balikpapan neuCentrIX`, `Nusantara data center`. |
| East Nusa Tenggara | Kupang | Mitrakom/MDC Kupang and telco/government leads. Search `Kupang data center`, `MDC Kupang`, `pusat data NTT Kupang`. |
| Gorontalo | Gorontalo city | Mostly Diskominfo/government data/informatics. Search `Gorontalo pusat data`, `Diskominfo Gorontalo data center`. |
| Highland Papua | Wamena, Jayawijaya | Very low signal; government/telecom only. |
| Jambi | Jambi city | SM+ Jambi/directory leads; verify with operator. Search `Jambi data center`, `pusat data Jambi`, `SM+ Jambi`. |
| Lampung | Bandar Lampung, Tanjung Karang | neuCentrIX Tanjung Karang official/Telkom launch; SM+ Lampung directory. Search `neuCentrIX Tanjung Karang`, `Bandar Lampung data center`. |
| Maluku | Ambon | Mitrakom/MDC Ambon directory lead; government/edge. Search `Ambon data center`, `MDC Ambon`, `pusat data Maluku`. |
| North Kalimantan | Tarakan, Tanjung Selor, Bulungan | Low signal; possible future hydropower/industrial park narrative. Search `Kalimantan Utara pusat data`, `KIPI data center`, `Tanah Kuning data center`. |
| North Maluku | Ternate, Halmahera, Morotai | Low signal; possible Jababeka Morotai SEZ or mining edge. Search `Morotai data center`, `Ternate pusat data`. |
| North Sulawesi | Manado, Bitung | neuCentrIX Manado; possible cable/port edge. Search `neuCentrIX Manado`, `Manado data center`, `Bitung pusat data`. |
| Papua | Jayapura | neuCentrIX Jayapura reported; verify Telkom. Search `neuCentrIX Jayapura`, `Jayapura pusat data`, `Papua data center`. |
| Riau | Pekanbaru, Dumai | neuCentrIX Pekanbaru; PDG legacy Pekanbaru/XL; NDC/edge possible. Search `Pekanbaru data center`, `neuCentrIX Pekanbaru`, `PDG Pekanbaru`. |
| South Kalimantan | Banjarmasin, Banjarbaru | neuCentrIX Banjarmasin-Ulin. Search `Banjarmasin Ulin data center`, `neuCentrIX Banjarmasin`. |
| South Papua | Merauke | Very low signal; government/telecom only. |
| South Sumatra | Palembang | NDC Palembang and government/edge leads. Search `Palembang data center`, `NDC Palembang`, `pusat data Sumatera Selatan`. |
| Southeast Sulawesi | Kendari, Konawe | Low signal; industrial/mining edge only. Search `Kendari pusat data`, `Konawe data center`. |
| Southwest Papua | Sorong | Low signal; government/telecom only. Search `Sorong data center`, `pusat data Papua Barat Daya`. |
| Special Region of Yogyakarta | Yogyakarta, Pugeran, Kotabaru, Sleman | neuCentrIX Pugeran and Kotabaru. Search `neuCentrIX Pugeran`, `Yogyakarta data center`, `pusat data DIY`. |
| West Kalimantan | Pontianak, Singkawang | Possible neuCentrIX/SM+/government edge; verify. Search `Pontianak data center`, `pusat data Kalbar`. |
| West Nusa Tenggara | Mataram, Lombok | Government/telco edge. Search `Mataram data center`, `pusat data NTB`, `Lombok data center`. |
| West Papua | Manokwari, Sorong legacy | Government/telco edge. Search `Manokwari pusat data`, `Papua Barat data center`. |
| West Sulawesi | Mamuju | Very low signal; government/telecom only. |
| West Sumatra | Padang, Bukittinggi | Possible telco/edge and disaster recovery. Search `Padang data center`, `pusat data Sumatera Barat`, `neuCentrIX Padang`. |

Province query template:

```text
"{province}" "{capital_city}" ("data center" OR "pusat data")
"{capital_city}" ("data center" OR "pusat data") ("beroperasi" OR "diresmikan" OR "diluncurkan")
"{capital_city}" ("neuCentrIX" OR "Nusantara Data Center" OR "SM+" OR "Mitrakom" OR "CenterServ")
"{province}" ("Diskominfo" OR "Pemerintah Provinsi") ("pusat data" OR "data center")
"{industrial_estate_or_SEZ}" ("data center" OR "pusat data" OR "AI")
"{province}" ("PLN" OR "PLN Batam") ("data center" OR "pusat data" OR "MVA" OR "PJBTL")
```

---

## 7. Industrial estate and power-source pivots

Industrial-estate and power records are high value because they locate projects better than operator marketing.

Priority estate/SEZ terms:

```text
GIIC / Greenland International Industrial Center
Kota Deltamas
MM2100
Jababeka
Karawang International Industrial City / KIIC
Jatiluhur / Purwakarta
Nongsa Digital Park / NDP
KEK Nongsa
Kabil Industrial Estate / Kabil Integrated Industrial Estate / KIIE
Batamindo Industrial Park
BSD / Digital Hub BSD
Technopark BSD
Kendal Industrial Park
IKN / Nusantara / Sepaku
```

Estate/power queries:

```text
site:deltamas.id ("data center" OR "pusat data" OR "GIIC")
"GIIC" ("data center" OR "pusat data") ("Bekasi" OR "Cikarang")
"Kota Deltamas" "{operator}" "data center"
"MM2100" "{operator}" "data center"
"Jababeka" "data center" "Cikarang"
"Nongsa Digital Park" ("data center" OR "pusat data") ("MW" OR "MVA")
site:bpbatam.go.id ("data center" OR "pusat data" OR "Nongsa" OR "Kabil")
site:plnbatam.com ("data center" OR "pusat data" OR "PJBTL" OR "MVA")
"PLN Batam" "{operator}" ("PJBTL" OR "MVA" OR "pusat data")
"PLN" "{operator}" "{province}" ("data center" OR "pusat data" OR "MVA")
```

Known signal patterns:

- **Bekasi/Cikarang/GIIC**: STT, PDG, Digital Edge, Microsoft-related builds, DCI/NTT nearby. Query by estate plus facility code (`JC3`, `STT Jakarta 2`, `CGK Campus`, `JKT3`) because public articles often say "Jakarta" while addresses say Bekasi.
- **Batam/Nongsa/Kabil**: DayOne, NeutraDC Nxera, Data Center First, BW Digital, RangeIDC/EGSB, Racks Central, Gaw-Sinar Primera, Matrix NAP. Power agreements with PLN Batam are strong pre-construction evidence.
- **Jatiluhur/Purwakarta**: BDx CGK4. Search both `Jatiluhur` and `Purwakarta`; some databases map it to West Java/Bekasi imprecisely.

---

## 8. Reliability and deduplication rules

- Prefer **operator page + exact address/spec** over directories. Use directories only to find aliases and nearby facilities.
- Deduplicate by physical campus: `Jakarta` marketing name can represent Jakarta city, Bekasi/West Java, Banten, or Purwakarta/West Java.
- Separate current facility IT load from full-campus future capacity. Example pattern: a campus may be announced as 500 MW or 1 GW, while only one 20-50 MW building is under construction.
- Separate commercial datacenters from government data centers: `Pusat Data Nasional`, provincial Diskominfo data centers, and enterprise server rooms are valid infrastructure leads but not commercial colo unless evidence says so.
- For Telkom/neuCentrIX, do not infer MW. Many edge sites disclose racks only or no capacity.
- For Batam, treat official BP Batam/Antara statements about "nine projects" or "six investors waiting" as cluster context. Add projects only when a developer, site, and stage are named.
- For hyperscalers, cloud regions are not equivalent to owned facilities. Use cloud-region evidence to seed Jakarta/Bekasi/Karawang searches, then require operator/land/power/permit corroboration for physical enumeration.

