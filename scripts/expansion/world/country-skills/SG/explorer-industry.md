# SG Explorer - Industry / Vendor / Trade-Press Discovery for Singapore Datacenters

Date reviewed: 2026-08-12. Country: **SG Singapore**. Division model: **district** (five Community Development Council districts: **Central Singapore; North East; North West; South East; South West**). Scope: industry, vendor, operator, trade-press, hyperscaler, interconnect, subsea-cable, and aggregator sources for discovering Singapore datacenter projects.

Reliability grades:
- **A** = primary source for the specific fact: operator facility page or press release, official cloud-region page, exchange/IXP operator page, statutory filing, REIT report, government source, utility source, or official cable guidance.
- **B** = reputable trade / business press or contractor source with named project facts: DCD, The Business Times, The Straits Times, CNA, W.Media, The Edge Singapore, Reuters, Bloomberg, FT, credible engineering/contractor releases.
- **C** = lead source only: DataCenterMap, Baxtel, Cloudscene, DataCenterJournal, datacenters.com, Colomap, broker pages, market-research totals, job ads, event pages, social posts.
- **U** = unsupported; do not count until upgraded.

**Grade rule:** grade facts separately. A-grade operator pages can support a facility name, location, marketed capacity, and status when stated. They do not prove unlisted addresses or audited delivered MW. Aggregator pages never become A-grade and should only drive follow-up searches.

---

## 0. Singapore Industry Search Model

Singapore has no public datacenter facility registry. Industry enumeration works best as a funnel:

1. Start with **operator facility pages** and press releases for named sites, addresses/estates, status, marketed MW, and certificates.
2. Use **official cloud-region pages** to confirm hyperscaler service-region presence, but do not infer physical sites.
3. Use **trade press** for groundbreakings, financing, construction, tenant, and land-acquisition leads, then upgrade facts through operator/statutory sources.
4. Use **IXP, PeeringDB, and subsea-cable sources** to locate interconnect-heavy buildings and demand clusters.
5. Use **aggregator directories** only as lead lists; their counts vary widely by scope.

Important market geography: Singapore's strongest physical clusters are South West (Jurong, Tuas, Boon Lay, International Business Park, Jalan Buroh, Tanjong Kling), South East (Tampines, Loyang/Changi, Tai Seng, Kaki Bukit), Central Singapore (Ayer Rajah/one-north, Kallang/Genting Lane, downtown carrier hotels), North West (Woodlands), and selected North East sites (Defu, Serangoon North, Punggol watchlist).

Division mapping rule: geocode to address / URA planning area first, then assign CDC district. Flag boundary-sensitive entries such as Tai Seng, Defu/Hougang, Queenstown, Seletar, and estate-only locations.

---

## 1. Search Vocabulary

English:

```text
data centre
data center
datacenter
colocation OR colo
hyperscale data centre
AI data centre OR AI-ready data centre
cloud region OR availability zone
Internet data centre OR IDC
carrier hotel
interconnection OR peering
edge data centre
disaster recovery centre
sovereign cloud
data hosting OR managed hosting
rack space OR cage
MW OR MVA OR IT load
PUE OR power usage effectiveness
Green Mark for Data Centres
DC-CFA OR Call for Application
groundbreaking OR breaks ground OR topped out
ready for service OR RFS OR commissioned OR opened
land acquisition OR site acquisition OR built-to-suit lease
anchor tenant
cable landing station
submarine cable OR undersea cable
Internet exchange OR IXP
fibre OR dark fibre
```

Malay / Mandarin / Tamil completeness terms:

```text
"pusat data" Singapura
"pusat data raya" Singapura
"kolokasi" Singapura
"kabel dasar laut" Singapura
数据中心 新加坡
数据中心园区 新加坡
云计算 新加坡
服务器托管 新加坡
海底光缆 新加坡
互联网交换中心 新加坡
தரவு மையம் சிங்கப்பூர்
```

Status terms to combine:

```text
announces / launches / opens / operational / commissioned
breaks ground / groundbreaking / topping out / under construction
ready for service / RFS / phased / fit-out
land tender / lease / acquisition / site selected
approved capacity / awarded / CFA / DC-CFA
Green Mark Platinum / PUE / liquid cooling / hydrogen / SOFC
```

---

## 2. Primary Operator Pipeline

High-priority operators with verified Singapore pages or project sources:

- Equinix Singapore: https://www.equinix.com/data-centers/asia-pacific-colocation/singapore-colocation/singapore-data-center
- Equinix SG5: https://www.equinix.com/data-centers/asia-pacific-colocation/singapore-colocation/singapore-data-center/sg5
- Equinix SG6 announcement: https://newsroom.equinix.com/2024-11-19-Equinix-Fosters-AI-Development-by-Building-a-High-Performance-and-Sustainable-Data-Center-in-Singapore
- Digital Realty Singapore: https://www.digitalrealty.com/data-centers/asia-pacific/singapore
- Digital Realty SIN10: https://www.digitalrealty.com/data-centers/asia-pacific/singapore/sin10
- Keppel Data Centres Singapore: https://www.keppeldatacentres.com/locations/asia-pacific/singapore/
- STT GDC Singapore: https://www.sttelemediagdc.com/sg-en/locations/singapore
- Nxera DC Tuas: https://www.nxera-dc.com/our-reach/singapore-dc-tuas
- Singtel / Nxera opening release: https://www.singtel.com/about-us/media-centre/news-releases/nxera-opens-data-centre
- AirTrunk SGP1: https://airtrunk.com/location/sgp1-singapore/
- AirTrunk SGP1 opening / launch release: https://airtrunk.com/airtrunk-unveils-singapores-largest-independent-and-most-efficient-hyperscale-data-centre/
- DayOne Singapore / SG1: https://dayonedc.com/market/singapore
- Global Switch Singapore: https://www.globalswitch.com/data-centres/singapore/
- ST Engineering Data Centre@Boon Lay: https://www.stengg.com/en/newsroom/news-releases/st-engineering-breaks-ground-on-new-data-centre/

Operators to search regularly for confirmed Singapore facilities or absence of a current facility page: StarHub, M1, China Mobile International, Tata Communications, OneAsia, i-Sprint, ViewQwest, Princeton Digital Group, Bridge Data Centres, SpaceDC, Empyrion, CyrusOne, Vantage, NEXTDC. Keep them out of counted A/B inventory until a Singapore facility or statutory/press trail is found.

Operator queries:

```text
site:equinix.com Singapore "SG1" OR "SG2" OR "SG3" OR "SG4" OR "SG5" OR "SG6"
site:digitalrealty.com Singapore "SIN" "data center"
site:keppeldatacentres.com Singapore "Keppel DC Singapore"
site:sttelemediagdc.com Singapore "Defu" OR "STT Singapore"
site:nxera-dc.com Singapore "DC Tuas" OR "DC West" OR "Kim Chuan"
site:airtrunk.com Singapore "SGP1" OR "SGP2"
site:dayonedc.com Singapore "SG1" OR "Jalan Buroh"
site:globalswitch.com Singapore "Tai Seng" OR "Woodlands"
site:stengg.com "Data Centre@Boon Lay" OR "Jalan Boon Lay"
"{operator}" "ready for service" "Singapore" "data centre"
"{operator}" "Green Mark" "data centre" Singapore
```

---

## 3. Hyperscaler Presence

Official sources:
- AWS: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Azure: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud: https://cloud.google.com/about/locations
- Oracle: https://www.oracle.com/asean/cloud/cloud-regions/singapore/
- Alibaba Cloud: https://www.alibabacloud.com/en/global-locations

Use these as A-grade evidence for service regions only:
- AWS Asia Pacific (Singapore), `ap-southeast-1`, 3 AZs.
- Azure Southeast Asia, Singapore, `southeastasia`.
- Google Cloud Singapore, `asia-southeast1`.
- Oracle Cloud Singapore, `ap-singapore-1`.
- Alibaba Cloud Singapore, `ap-southeast-1`, 4 zones.

Do not map cloud AZs to CDC districts or physical addresses.

```text
"AWS" "ap-southeast-1" "Singapore" "Availability Zones"
"Azure" "Southeast Asia" "Singapore" "southeastasia"
"Google Cloud" "asia-southeast1" "Singapore"
"Oracle Cloud" "ap-singapore-1" "Singapore"
"Alibaba Cloud" "Singapore" "ap-southeast-1" "zones"
"{hyperscaler}" Singapore "data centre" "investment" "DC-CFA"
```

---

## 4. Trade Press and Lead Sources

Reliable B-grade press / contractor sources:
- Data Center Dynamics: https://www.datacenterdynamics.com/
- The Business Times: https://www.businesstimes.com.sg/
- The Straits Times: https://www.straitstimes.com/
- CNA: https://www.channelnewsasia.com/
- W.Media: https://w.media/
- The Edge Singapore: https://www.theedgesingapore.com/
- Reuters / Bloomberg / FT for financing, acquisitions, and hyperscaler investments.
- Engineering / contractor pages such as Aurecon, HDR, PM Group, and official vendor releases where they name a built project.

Verified useful examples:
- DCD: STT GDC opened Defu 3 in 2022: https://www.datacenterdynamics.com/en/news/stt-gdc-opens-third-building-at-defu-campus-in-singapore/
- DCD: Nxera DC Tuas opening coverage: https://www.datacenterdynamics.com/en/news/singtels-nxera-opens-singapore-data-center/
- Business Times: DayOne 20 MW Jurong East / hydrogen pilot groundbreaking: https://www.businesstimes.com.sg/companies-markets/dayone-breaks-ground-first-singapore-data-centre-trial-hydrogen-based-power-generation
- Business Times: AirTrunk SGP1 opening: https://www.businesstimes.com.sg/property/airtrunk-opens-its-first-singapore-data-centre
- The Straits Times: ST Engineering Jalan Boon Lay details: https://www.straitstimes.com/business/st-engineering-to-invest-120m-in-new-sustainable-data-centre-at-jalan-boon-lay
- Aurecon Global Switch Woodlands project: https://www.aurecongroup.com/projects/data-and-telecommunications/global-switch-singapore-woodlands
- PM Group Global Switch Woodlands project: https://www.pmgroup-global.com/what-we-do/our-work/woodlands-data-centre-project/
- HDR STT Defu campus project: https://www.hdrinc.com/portfolio/defu-data-centre-campus

Trade queries:

```text
site:datacenterdynamics.com Singapore "data centre" OR "data center"
site:businesstimes.com.sg "data centre" Singapore
site:straitstimes.com "data centre" Singapore
site:channelnewsasia.com "data centre" Singapore
site:w.media Singapore "data centre" OR "data center"
site:theedgesingapore.com "data centre" Singapore
"{operator}" Singapore "data centre" "groundbreaking"
"{operator}" Singapore "data centre" "green loan"
"{operator}" Singapore "data centre" "ready for service"
```

---

## 5. IXPs, Peering, and Subsea Cable Sources

IXP / peering sources:
- SGIX: https://www.sgix.sg/
- SGIX PeeringDB: https://www.peeringdb.com/ix/429
- DE-CIX Singapore: https://www.de-cix.net/en/locations/singapore
- BBIX Singapore No.3 at Global Switch Tai Seng: https://www.bbix.net/en/information/press/2022-10-13/
- PeeringDB search: https://www.peeringdb.com/

Subsea sources:
- IMDA submarine cable deployment/repair page: https://www.imda.gov.sg/regulations-and-licensing-listing/deployment-and-repair-of-submarine-cable-systems
- IMDA submarine-cable landing guidance PDF: https://www.imda.gov.sg/-/media/imda/files/regulation-licensing-and-consultations/codes-of-practice-and-guidelines/subcablelanding.pdf
- Submarine Networks Singapore: https://www.submarinenetworks.com/en/stations/asia/singapore
- TeleGeography map: https://www.submarinecablemap.com/
- Changi landing point: https://www.submarinecablemap.com/landing-point/changi-singapore
- Tanah Merah landing point: https://www.submarinecablemap.com/landing-point/tanah-merah-singapore
- GeoCables Singapore: https://geocables.com/locations/sg

Use IX and cable sources to identify interconnect-rich buildings and demand clusters. Do not count IXP PoPs or cable landing stations as datacenters unless a separate datacenter source supports the facility.

```text
site:sgix.sg "Singapore" "data centre"
site:peeringdb.com "Singapore" "{facility}"
site:de-cix.net "Singapore" "data center"
site:bbix.net "Singapore" "Global Switch" "Tai Seng"
"Changi North" "cable landing station"
"Tanah Merah" "cable landing station"
"Tuas" "cable landing station"
"{cable}" "Singapore" "landing" "Changi" OR "Tuas" OR "Tanah Merah"
```

---

## 6. Aggregator Directories

Lead lists only:
- DataCenterMap Singapore: https://www.datacentermap.com/singapore/singapore/
- Baxtel Singapore: https://baxtel.com/data-center/singapore
- DataCenterJournal Singapore: https://www.datacenterjournal.com/data-centers/singapore/singapore/
- Cloudscene Singapore search: https://cloudscene.com/
- datacenters.com Singapore search: https://www.datacenters.com/
- Colomap exchange/facility leads: https://colomap.com/

Use aggregators to find facility names, street addresses, and aliases, then confirm through operator, REIT, filing, government, or reliable press sources. Treat aggregator facility counts as C-grade market context only because each directory uses different inclusion rules.

```text
site:datacentermap.com/singapore/singapore "{operator}" "Singapore"
site:baxtel.com/data-center "Singapore" "{operator}"
site:datacenterjournal.com "Singapore" "{operator}" "data center"
site:cloudscene.com "Singapore" "{operator}"
site:datacenters.com "Singapore" "{operator}"
```

---

## 7. Per-Division Enumeration

### 7.1 Central Singapore

Expectation: central colocation, carrier hotels, enterprise facilities, and network PoPs. Priority areas: Ayer Rajah / one-north, Alexandra / Bukit Merah, Genting Lane, Kallang, Bendemeer, Toa Payoh, Bishan, Ang Mo Kio, Downtown Core, Tanjong Pagar, Marina Bay, and part of Queenstown.

Known lead examples: Equinix SG1/SG3 around Ayer Rajah / one-north need operator-page facility-level confirmation; Keppel lists Genting Lane among its Singapore locations; carrier-hotel candidates need PeeringDB/operator confirmation.

```text
"Ayer Rajah" OR "one-north" "data centre" Singapore
"Genting Lane" "data centre" Singapore
"Kallang" OR "Bendemeer" "data centre" Singapore
"Alexandra" OR "Bukit Merah" "colocation" Singapore
"Tanjong Pagar" OR "Raffles Place" OR "Marina Bay" "carrier hotel" Singapore
```

### 7.2 North East

Expectation: modest current footprint. Priority areas: Defu, Serangoon North, Hougang, Punggol Digital District, Sengkang, Seletar.

Known lead examples: STT Singapore 1/2/3 in Defu, Keppel DC Singapore 1 in Serangoon North, Punggol Digital District as a future digital-infrastructure watch item. Assign CDC after GIS because Defu/Hougang and Seletar-adjacent records can be boundary-sensitive.

```text
"STT Singapore" "Defu" "data centre"
"STT Defu 3" "opened" Singapore
"Keppel DC Singapore 1" "Serangoon North"
"Punggol Digital District" "data centre" OR "digital infrastructure"
"Hougang" OR "Sengkang" OR "Seletar" "data centre" Singapore
```

### 7.3 North West

Expectation: Woodlands cluster and possible Sungei Kadut / Sembawang industrial leads.

Known lead examples: Global Switch Woodlands at 7 Woodlands Height, 22 MW; Keppel DC1 in Woodlands. Woodlands proximity to Johor is market context only and does not merge Singapore/Johor counts.

```text
"Global Switch" "7 Woodlands Height"
"Global Switch" "Woodlands" "22MW"
"Keppel" "Woodlands" "data centre"
"Sungei Kadut" "data centre" Singapore
"Sembawang" OR "Yishun" OR "Marsiling" "data centre" Singapore
```

### 7.4 South East

Expectation: major hub. Priority areas: Tampines Industrial Park, Loyang/Changi, Tanah Merah, Tai Seng, Kaki Bukit, Chai Chee, Ubi, Paya Lebar.

Known lead examples: AirTrunk SGP1 at Loyang; Keppel DC Singapore 2/3/4 in Tampines Industrial Park; Global Switch Tai Seng at 2 Tai Seng Avenue, 17 MW; Equinix SG2/SG4 and StarHub/CMI Tai Seng entries require source separation; BBIX Singapore No.3 at Global Switch Tai Seng supports interconnect presence.

```text
"AirTrunk" "SGP1" "Loyang"
"Loyang" "Changi North" "data centre"
"Keppel DC Singapore 2" OR "Keppel DC Singapore 3" OR "Keppel DC Singapore 4"
"Tampines Industrial Park" "data centre"
"Global Switch" "2 Tai Seng Avenue"
"Tai Seng" "data centre" "Equinix" OR "StarHub" OR "China Mobile"
"Kaki Bukit" OR "Chai Chee" OR "Ubi" "data centre" Singapore
```

### 7.5 South West

Expectation: largest hyperscale and industrial DC geography. Priority areas: Jurong East/West, International Business Park, Jalan Buroh, Tanjong Kling, Tuas, Boon Lay, Pioneer/Gul, Sunview Drive, Jalan Tukang, West Coast, Clementi.

Known lead examples: Digital Realty SIN10 at 29A International Business Park; DayOne SG1 at 21 Jalan Buroh / Jurong East campus; Nxera DC Tuas; Equinix SG5 at 6 Sunview Drive; Equinix SG6 under construction for Q1 2027 / 20 MW; ST Engineering Data Centre@Boon Lay; Keppel DC Singapore 5 in Jurong.

```text
"Digital Realty" "SIN10" "29A International Business Park"
"DayOne" "21 Jalan Buroh" OR "Jurong East campus"
"Nxera" "DC Tuas" "58MW"
"Equinix" "SG5" "6 Sunview Drive"
"Equinix" "SG6" "Q1 2027" "20MW"
"ST Engineering" "Jalan Boon Lay" "data centre"
"Keppel DC Singapore 5" "Jurong"
"Tanjong Kling" "data centre" Singapore
"Jurong Island" "low-carbon data centre" Singapore
```

---

## 8. Known Industry / Operator Evidence Table

| Facility / project | Division | Status / fact supported | Evidence | Grade |
| --- | --- | --- | --- | --- |
| Equinix Singapore platform | Multiple | Singapore metro operator page; certifications listed | Equinix Singapore page | A |
| Equinix SG5 | South West | 6 Sunview Drive, opened 2021 | Equinix SG5 page | A |
| Equinix SG6 | South West | SG6, 20 MW when fully built, expected Q1 2027, pilot DC-CFA award | Equinix / EDB releases | A |
| Digital Realty SIN10 | South West | 29A International Business Park, Jurong East facility details | Digital Realty SIN10 page | A |
| Keppel DC Singapore 1 | North East, GIS check | Serangoon North Industrial Estate | Keppel Data Centres | A |
| Keppel DC Singapore 2/3/4 | South East | Tampines Industrial Park | Keppel Data Centres | A |
| Keppel DC Singapore 5 | South West | Jurong | Keppel Data Centres | A |
| Keppel DC DC1 | North West | Woodlands | Keppel Data Centres | A |
| Keppel DC Singapore 7/8 | Division requires address/GIS | Keppel Data Centre Campus; KDC SGP 7 Green Mark Platinum stated | Keppel Data Centres | A for stated facts |
| STT Singapore 1 | North East / boundary check | Defu, 13 MW | STT GDC | A |
| STT Singapore 2 | North East / boundary check | Defu, 12 MW | STT GDC | A |
| STT Defu 3 / STT Singapore 3 | North East / boundary check | Defu third building; 15 MW in DCD; opened 2022 | STT GDC / DCD | A/B |
| Nxera DC Tuas | South West | Up to 58 MW IT load; PUE and Green Mark claims; cable-landing integration; opening release 9 Feb 2026 | Nxera / Singtel | A |
| Nxera DC West | South West likely; GIS needed | Nxera lists Singapore DC West; location described as West | Nxera | A for existence; division needs address |
| Nxera DC Kim Chuan 2 | likely South East / Central boundary; GIS needed | Nxera lists Singapore DC Kim Chuan 2 | Nxera | A for existence; division needs address |
| AirTrunk SGP1 | South East | Loyang campus open; AirTrunk markets 60+ MW design; BT confirms 2020 opening | AirTrunk / BT | A/B |
| DayOne SG1 | South West | Jurong East / 21 Jalan Buroh, 39,978 sqm, 20 MW, RFS 2027, hydrogen SOFC pilot | DayOne / BT | A/B |
| Global Switch Tai Seng | South East | 17 MW, 2 Tai Seng Avenue | Global Switch | A |
| Global Switch Woodlands | North West | 22 MW, 7 Woodlands Height | Global Switch | A |
| ST Engineering Data Centre@Boon Lay | South West | Jalan Boon Lay, fourth SG DC, 2026 completion target, $120m capex, PUE 1.25 design | ST Engineering / MTI / ST | A/B |
| StarHub Tai Seng DCs | South East | Candidate facilities | Aggregators / search leads | C until StarHub confirms |
| China Mobile International 15A Tai Seng | South East | Candidate facility | Aggregators / building listings | C until CMI confirms |
| Meta Tanjong Kling / Jurong | South West | Candidate hyperscale campus and capacity claims | Aggregators / market reports | C until Meta/statutory source confirms |
| Punggol Digital District | North East | Digital district; not a datacenter facility by itself | JTC official pages | A for district only |
| SGIX | n/a | Singapore IXP, member/PoP lead source | SGIX / PeeringDB | A for IXP facts |
| DE-CIX Singapore | n/a | Singapore IXP location | DE-CIX | A for IXP facts |
| BBIX Singapore No.3 @ Global Switch Tai Seng | South East | BBIX PoP at Global Switch Tai Seng | BBIX | A for PoP fact |
| Changi North / Tanah Merah / Tuas cable landing sites | South East / South West | Cable landing clusters | IMDA / Submarine Networks / TeleGeography | A/B |

---

## 9. Update / Re-check Cadence

- **Monthly:** operator pages and newsrooms for Equinix, Digital Realty, Keppel, STT GDC, Nxera/Singtel, AirTrunk, DayOne, Global Switch, ST Engineering; DCD, W.Media, BT, ST, CNA, The Edge Singapore.
- **Quarterly:** hyperscaler region pages; PeeringDB/IXP PoPs; Uptime and Green Mark claims; SGX/REIT disclosures; aggregator leads.
- **On DC-CFA events:** immediately re-check IMDA/EDB, then operator announcements, then press and land/address leads.
- **Semi-annually:** re-check every C-grade facility lead and every boundary-sensitive division assignment.
- **Annually:** refresh CDC district mapping and route all known addresses through OneMap / URA SPACE.

---

## 10. Red Flags

- Cloud regions and AZs are not physical site counts.
- Cable landing stations and IXPs are infrastructure leads, not datacenter facilities unless separately supported.
- Operator facility IDs are not addresses.
- Marketed MW, committed MW, IT load, utility MVA, and delivered live capacity are different facts.
- Aggregator counts are not reliable totals for Singapore because they mix live, planned, edge, cloud, and duplicate entries.
- Preserve original place evidence and CDC assignment uncertainty for boundary-sensitive locations.
