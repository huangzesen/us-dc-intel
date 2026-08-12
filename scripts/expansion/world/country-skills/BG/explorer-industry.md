# BG Explorer Industry - Bulgaria Datacenter Enumeration via Operators, Cloud/IX, Trade Press, and District Query Patterns

Date: 2026-08-12. Scope: Bulgaria (BG), 28 districts. Focus angle: industry/vendor/trade-press discovery that feeds official verification. Reliability grades: **A** = official/operator/cloud/IX/public-record source, **B** = established trade press or government/investment-promotion source that should be verified, **C** = directories, aggregators, stale announcements, social posts, or weak secondary leads.

---

## 0. Bulgaria-specific market frame

- Bulgaria has no single public national data-center registry. Enumeration should start from **operator portfolios, Sofia internet-exchange/PeeringDB signals, cloud/edge provider pages, trade press, and directories**, then verify new/large projects through municipality building records, environmental notices, public procurement, grid/utility clues, and cadastral/industrial-zone context.
- Sofia is the dominant cluster. Outside Sofia, expect smaller telco/hosting nodes, Neterra/SDC or Telepoint legacy regional facilities, industrial-zone projects, telecom data centers, and public/HPC facilities.
- Bulgarian-language search is required. Use both Latin and Cyrillic forms: `data center`, `datacenter`, `дейта център`, `дата център`, `център за данни`, `центрове за данни`, `колокация`, `колокационен център`, `сървърно помещение`, `сървърна зала`, `облачен център`, `резервен център за данни`, `суперкомпютър`, `AI фабрика`, `фабрика за изкуствен интелект`, `инвестиционно предложение`, `разрешение за строеж`, `одобрен инвестиционен проект`, `ПУП`, `подробен устройствен план`, `ОВОС`, `преценяване необходимостта от ОВОС`, `РИОСВ`, `трафопост`, `електрозахранване`, `дизел генератор`.
- Bulgaria uses districts (`oblast`) for the manifest, but permitting is usually **municipal**. Query city/municipality pages, municipal council minutes, regional environmental inspectorates (`РИОСВ`), and industrial-zone sites rather than only oblast administration pages.
- Treat old, small, and directory-only listings carefully. DataCenterMap/Datacenters.com/Inflect/Baxtel are useful for address/operator seeds, but many Bulgarian regional listings are unverified telco rooms or legacy POPs.

---

## 1. Source Map

### 1.1 Official/public-record surfaces

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Bulgarian Public Procurement Agency / CAIS EOP | https://www2.aop.bg/ and https://www.eop.bg/ | Public-sector data-center, server-room, cloud, UPS, generator, cooling, and DR-site tenders. Use `център за данни`, `сървърно помещение`, `резервен център`, `колокация`, `доставка и монтаж климатизация`, CPV IT/construction terms. | A |
| Ministry of Environment and Water EIA rules | https://www.moew.government.bg/en/ordinance-for-the-conditions-and-the-order-for-implementing-environmental-impact-assessment/ | Process reference for EIA of investment proposals. For actual projects, search MOEW and the relevant RIEW (`РИОСВ`) pages for investment proposal notices and EIA screening decisions. | A |
| Ministry of Innovation and Growth investor guide | https://www.mi.government.bg/en/general/poluchavane-na-razreshenie-za-stroej/ | Official English process reference: construction projects require Spatial Development Act permitting. Use it to frame municipality building-permit verification. | A |
| Municipal building/urbanism registers | `site:{municipality-domain} "разрешение за строеж" "център за данни"`; Sofia example surfaces include `site:sofproect.com`, `site:sofia-agk.com`, `site:sofia.bg` | Primary evidence for new construction, reconstruction, PUP zoning, design approval, use permits, and council approvals. Coverage varies by municipality. | A |
| Regional Inspectorates for Environment and Water (`РИОСВ`) | Queries like `site:riosv-sofia.org "център за данни"`, `site:riosv-plovdiv.org "инвестиционно предложение" "център за данни"` | Environmental screening for large campuses, generator plants, substations, industrial-zone sites, and energy-heavy projects. | A |
| Cadastre / property context | https://kais.cadastre.bg/ and municipal GIS where public | Parcel/location confirmation after a lead identifies address or plot. | A |
| Communications Regulation Commission (CRC) | https://crc.bg/en/articles/2203/notification-of-public-electronic-communications-networks-and-services | Telecom operator context. CRC is not a data-center registry, but helps validate telecom operators behind colo/IX/edge facilities. | A/B |

### 1.2 Industry, IX, and association-like sources

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| BIX.BG | https://www.bix.bg/ | First Bulgarian IXP; states connectivity across 10+ Sofia data centers and gives active peering ecosystem. Seed Sofia facilities and current network-dense sites. | A/B |
| DE-CIX Sofia / BIX.BG partnership | https://www.de-cix.net/en/locations/sofia and https://www.de-cix.net/en/about-de-cix/media/press-releases/de-cix-solidifies-presence-in-bulgarian-market-through-strengthened-partnership-with-internet-exchange-bix-bg | Confirms Sofia as regional interconnection hub; DE-CIX says BIX.BG has 130+ networks, 11 Tbps connected customer capacity, 1.3 Tbps+ peak traffic, and 10 Sofia metro PoPs. | A/B |
| PeeringDB | https://www.peeringdb.com/ | Active facility/IX evidence for Sofia sites such as Equinix SO1/SO2, Evolink Sofia 1/2, Sofia Data Center, Telepoint Sofia Centre, S3. Not complete for all facilities. | B/C |
| NetIX | https://www.netix.net/ | NetIX/B-IX network and on-net data-center clues, especially Sofia and Plovdiv Teleport/Neterra ecosystem. Verify facility claims separately. | B/C |
| International Data Spaces / GATE | https://internationaldataspaces.org/bulgarian-hub-joins-the-idsa/ | Bulgarian digital/data ecosystem seed, not facility registry. Useful for Sofia Tech Park/GATE/AI research context. | B |

### 1.3 Trade press and directories

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/ ; query `site:datacenterdynamics.com Bulgaria data center Sofia Plovdiv Burgas Brinell VueNow Neterra Telepoint` | Strongest international DC trade source. Use for Digital Realty/Telepoint, Neterra SDC2, Brinell Plovdiv/Maritsa, VueNow, market leads. | B |
| Economic.bg / Capital.bg / TechNews.bg / Computerworld.bg / Investor.bg | Queries: `site:economic.bg "център за данни"`, `site:capital.bg "дейта център"`, `site:technews.bg "дейта център"` | Bulgarian business/technology press. Good for AI factory, operator expansions, government-cloud and market context. Verify through operator or public filings. | B |
| SeeNews / BTA / BalkanEngineer / local newspapers | Queries around operator/project + city in English and Bulgarian | Useful for investment-promotion and regional announcements. Check date and whether a memorandum progressed. | B/C |
| Baxtel Bulgaria | https://baxtel.com/data-center/bulgaria | Facility seed list and project tracker. Useful for Sofia, Burgas Top Systems, Brinell, CETIN, Telepoint, Neterra, but verify. | C+ |
| Data Center Map Bulgaria | https://www.datacentermap.com/bulgaria/ | Broadest Bulgarian city/operator seed list; good for regional Neterra/Telepoint/TSBG/ESCOM entries. Coverage/status may lag. | C+ |
| Datacenters.com Bulgaria | https://www.datacenters.com/locations/bulgaria | Commercial listings, address hints, provider aliases. Treat as lead generation. | C |
| Inflect / Cloudscene / OCOLO / DC Atlas / Data Center Platform | Queries by country, city, IX, and operator | Useful for cross-checking addresses and peering/colo clues; do not use alone for firm count/capacity. | C |

---

## 2. Core Search Patterns

### 2.1 National industry sweep

```text
"център за данни" България "MW" OR "мегават" OR "кв.м"
"дейта център" България София Пловдив Варна Бургас Русе
"data center" Bulgaria Sofia Plovdiv Varna Burgas Ruse Neterra Telepoint Equinix Evolink
"колокация" България "център за данни"
"сървърна зала" България "разрешение за строеж"
site:datacenterdynamics.com Bulgaria "data center"
site:economic.bg ("център за данни" OR "дейта център" OR "AI фабрика")
site:capital.bg ("център за данни" OR "дейта център")
site:technews.bg ("център за данни" OR "дейта център")
site:computerworld.bg ("център за данни" OR "data center")
```

### 2.2 Permit, environment, and procurement vocabulary

```text
"център за данни" "{община}" "разрешение за строеж"
"дейта център" "{община}" "ПУП" OR "подробен устройствен план"
"център за данни" "{община}" "инвестиционно предложение"
"сървърно помещение" "{община}" "обществена поръчка"
"резервен център за данни" "{община}" "обществена поръчка"
"център за данни" "{община}" "ОВОС" OR "РИОСВ"
"център за данни" "{община}" "трафопост" OR "електрозахранване" OR "дизел генератор"
site:eop.bg "център за данни" "{city}"
site:aop.bg "център за данни" "{city}"
site:moew.government.bg "център за данни" OR "дейта център"
site:riosv* "център за данни" "{city}"
```

### 2.3 Operator/name pivots

```text
Neterra SDC Sofia Stolnik Ruse "data center" България
Telepoint Sofia East Sofia Centre Montana Digital Realty Bulgaria
Equinix SO1 SO2 Sofia Bulgaria
Evolink "data centers" Sofia Plovdiv
Daticum "135 Tsarigradsko Shose" "data centre"
A1 "Data Center" София Варна Шумен Пловдив Монтана
CETIN Bulgaria Serdika Trakia data center
Top Systems Burgas data center 2.5 MW
Brinell Compute Rakovski Maritsa Plovdiv data center
VueNow Plovdiv Tech Park Bulgaria edge data centers
```

---

## 3. Operator and Project Seed List

Operator pages are **A for self-described facility existence** and usually **B for capacity**, unless a current spec sheet or certification is published. Trade-press and directory-only entries are leads until verified.

### 3.1 Sofia city and Sofia district anchors

- **Digital Realty / Telepoint** - Digital Realty announced on 2026-03-02 that it entered Bulgaria through the acquisition of Telepoint, including two Sofia data centers and one highly interconnected Southeast Europe facility with 110+ network service providers and multiple cloud on-ramps. Official source: https://www.digitalrealty.com/about/newsroom/press-releases/20096/digital-realty-enters-bulgaria-with-acquisition-of-highly-connected-interconnection-hub-in-sofia . Track aliases `Telepoint Sofia East`, `Telepoint Sofia Centre`, `122 Ovcho Pole`, `8 Asen Yordanov`, `Digital Realty Sofia`. Grade A/B.
- **Equinix Sofia SO1/SO2** - official Equinix Bulgaria pages state two network-dense, carrier-neutral data centers in Sofia with about 35,000 sq ft / 3,215 sq m colocation. Official: https://www.equinix.com/data-centers/europe-colocation/bulgaria-colocation and https://www.equinix.com/data-centers/europe-colocation/bulgaria-colocation/sofia-data-centers . Grade A/B.
- **Neterra / Sofia Data Center (SDC)** - official SDC page says Neterra provides services in four data centers: SDC 1, SDC 2, SDC Stolnik, and SDC Ruse. Official: https://sdc.bg/ ; Neterra colocation page: https://neterra.net/rental-of-resources/collocation . SDC2 opening page/DCD report says SDC2 is next to SDC1 and has about 1,400 sq m and 2 MW installed capacity. Grade A/B.
- **SDC Stolnik / Data Center Park Stolnik** - Neterra official pages list it; operator news describes Stolnik near a major substation and about 20 minutes from Sofia Airport. Assign to **Sofia district**, not Sofia city, unless a source uses city/metropolitan shorthand. Grade A/B.
- **A1 Bulgaria / Lift data center / Exoscale BG-SOF-1** - A1 markets `A1 Data Center` services; Exoscale official Bulgaria page lists Bulgarian cloud zone `BG-SOF-1`, and cloud/directories place it in A1 Lift at 3 Nedelcho Bonchev Street, Sofia. A1 page: https://www.a1.bg/a1-data-center ; Exoscale: https://www.exoscale.com/datacenters/bulgaria/ ; A1 International data-center page: https://internationalbusiness.a1.group/data-center/ . Grade A for Exoscale/A1 services; verify exact facility details with A1/Exoscale/current interconnect records.
- **Daticum / Sirma Group** - official Daticum pages provide cloud, dedicated servers, and colocation from 135 Tsarigradsko Shose Blvd., Sofia. Official: https://daticum.com/en/data-centre/ and https://daticum.com/en/contacts/ . Grade A.
- **Evolink** - official page states Evolink built and operates four data centers in Sofia and Plovdiv, with the newest facility `Evolink Data Center Sofia 2` carrier-neutral. Official: https://www.evolink.com/about/evolink-data-center . PeeringDB lists Evolink Sofia 1 and Sofia 2 as BIX facilities. Grade A/B.
- **CETIN Bulgaria Serdika DC** - CETIN International says CETIN Bulgaria installed PV systems on data centers in Sofia and Plovdiv; Serdika DC is in Sofia. Official: https://www.cetin.international/w/data-centers-serdika-and-trakia-now-fully-equipped-with-solar-systems . Grade A/B for named DC existence, weaker for public colo availability.
- **BRAIN++ / Sofia Tech Park AI Factory** - INSAIT and Sofia Tech Park official/government releases say BRAIN++ will be located at Sofia Tech Park, include Discoverer++ and a modern GPU AI data-center/supercomputer component, with construction beginning 2026 and completion within three years. Official sources: https://insait.ai/bulgaria-will-have-its-own-ai-factory-a-project-for-90m-eur/ and https://www.mig.government.bg/all-news/sofia-tech-park-and-insait-are-selected-for-e90-million-eu-project-bulgaria-will-be-home-to-one-of-six-new-eu-ai-factories/?lang=en . Grade A/B for project; verify construction status through Sofia Tech Park/Sofia municipality/procurement.
- **Sofia directory-only/IX seeds** - S3 Company, ITD Network, Rax.bg, Vivacom, EXA, Novatel, NetIX/B-IX-associated sites, SSDCloud/3DC older entries. Use PeeringDB/BIX/DataCenterMap/Inflect as pivots, then verify operator pages and addresses. Grade C/B depending source.

Sofia templates:

```text
"център за данни" София Equinix Neterra Telepoint Digital Realty Daticum Evolink A1 CETIN
"дейта център" София "разрешение за строеж"
"Telepoint Sofia East" "Digital Realty" "110" "network service providers"
"TELEPOINT Sofia Centre" "Ovcho Pole" OR "Овчо поле"
"Equinix SO1" "Equinix SO2" Sofia
"SDC 2" Neterra Sofia "2 MW"
"SDC Stolnik" "Data Center Park Stolnik"
"A1 Lift" "BG-SOF-1" Exoscale Sofia
"Daticum" "Цариградско шосе" "център за данни"
"Evolink Data Center Sofia 2" "Barzaritsa" OR "Акад. Георги Бончев"
"CETIN" "Serdika DC" София
"BRAIN++" "Sofia Tech Park" "център за данни"
site:sofia.bg "център за данни" OR "дейта център" OR "сървърно помещение"
site:sofia-agk.com "център за данни" OR "разрешение за строеж"
site:sofiatech.bg "BRAIN++" OR "център за данни"
site:riosv-sofia.org "център за данни" OR "дейта център"
```

### 3.2 Plovdiv / Maritsa / Rakovski / Trakia Economic Zone

- **Brinell Compute AI data center / AI factory** - DCD and Bulgarian business press reported a planned EUR 3 billion AI data-center/campus in the Rakovski Industrial Zone/Maritsa area north of Plovdiv, with local reports tied to Council of Ministers memorandum activity. DCD 2026 update: https://www.datacenterdynamics.com/en/news/brinell-compute-prepares-for-construction-of-ai-data-center-in-maritsa-bulgaria/ ; Economic.bg: https://www.economic.bg/en/a/view/german-company-may-build-3-billion-ai-factory-near-plovdiv . Grade B until municipality/RIEW/building filings are captured.
- **CETIN Bulgaria Trakia DC** - official CETIN source names Trakia DC in Plovdiv and PV installation. Grade A/B.
- **Evolink Plovdiv** - official Evolink page states data centers in Sofia and Plovdiv. Grade A for existence, B/C for individual facility details unless local page/spec found.
- **Neterra/NetIX/Plovdiv Teleport / TSBG** - mostly directory and network ecosystem seeds; verify via operator pages, PeeringDB, DataCenterMap, Datacenters.com, and local permits. Grade C/B.
- **VueNow / Plovdiv Tech Park** - DCD and PTI/Times of India reported a 2021 MoU for one 100-rack hub in Plovdiv and six edge data centers across Bulgaria. No obvious later firm buildout in quick checks; treat as stale planned lead unless local filing/operator evidence appears. Grade C/B.

Plovdiv templates:

```text
"център за данни" Пловдив Brinell CETIN Evolink Neterra TSBG
"дейта център" Пловдив "Тракия икономическа зона"
"Brinell Compute" Rakovski Maritsa Plovdiv "data center"
"Brinell Compute" "Раковски" "център за данни" OR "AI фабрика"
"Maritsa" "Rakovski Industrial Zone" "data center"
"CETIN" "Trakia DC" Пловдив
"Evolink" Пловдив "data center"
"VueNow" "Plovdiv Tech Park" Bulgaria
site:plovdiv.bg "център за данни" OR "дейта център"
site:maritsa.bg "център за данни" OR "Brinell"
site:rakovski.bg "Brinell" OR "център за данни" OR "инвестиционно предложение"
site:riosv-pd.org "център за данни" OR "Brinell" OR "Раковски"
```

### 3.3 Varna and Burgas / Black Sea coast

- **Top Systems Burgas / BOJ** - official Top Systems page says a Burgas data-center project is planned to open in 2026, with 2.5 MW, 1,200 sq m, 220 racks, 100% renewable energy, and 10 MW / 5,000 sq m expansion ambition. Official: https://topsystems.bg/ . Grade A/B; verify construction/commissioning through Burgas municipality and Industrial and Logistics Park Burgas.
- **AC DC / AbsCloud Varna** - official AC DC and AbsCloud pages describe a green data center in Varna offering colocation/cloud services. Sources: https://acdcbg.com/en/zelen-data-center and https://www.abscloud.bg/datacenter/ . Grade A.
- **Varna Data Center** - official site https://varnadatacenter.com/ is an operating colocation/data-center seed. Grade A.
- **A1 regional colocation** - Bulgarian press on A1's Sofia modernization states A1 also owns colocation centers in Varna, Shumen, Plovdiv, Montana and other cities; use as lead and verify through A1/operator pages. Grade B.
- **VueNow Varna/Burgas edge sites** - 2021 MoU lead only unless later evidence appears. Grade C/B.

Coast templates:

```text
"Top Systems" Burgas "2.5 MW" "data center"
"Топ Системс" Бургас "център за данни"
"Industrial and Logistics Park Burgas" "data center" OR "център за данни"
"AC DC" Varna "green data center"
"AbsCloud" Варна "център за данни"
"Varna Data Center" colocation
"A1" Варна "Data Center" OR "колокационен център"
site:burgas.bg "център за данни" OR "дейта център" OR "разрешение за строеж"
site:industrialpark-burgas.bg "data center" OR "център за данни"
site:riosvbs.com "център за данни" OR "инвестиционно предложение"
site:varna.bg "център за данни" OR "сървърно помещение"
site:riosv-varna.bg "център за данни"
```

### 3.4 Ruse, Stara Zagora, Montana, and other named regional seeds

- **SDC Ruse** - Neterra/SDC official pages list SDC Ruse as one of four data centers. Grade A.
- **Telepoint Montana** - Telepoint contact/help pages and directories identify Montana alongside Sofia; Digital Realty acquisition mentions two Sofia data centers, so Montana should be treated as Telepoint regional/legacy seed and verified by Telepoint/Digital Realty current materials or local records. Grade B/C unless current official facility page captured.
- **Vivacom / Eutelsat OneWeb Stara Zagora ground station mini data centre** - United Group official release says the Stara Zagora ground station includes 18 antennas and a mini data centre connecting LEO satellites to optical networks and data centers; it was completed/commissioned in 2023. Official: https://united.group/vivacom-and-eutelsat-group-are-launching-in-bulgaria-the-fourth-european-ground-station/ . Grade A, but classify as satellite ground-station data-center infrastructure, not standard colo.
- **Neterra regional listings** - DataCenterMap/Datacenters.com list Neterra or related facilities in Pazardzhik, Pleven, Razgrad, Sliven, Burgas and other cities. Use as search pivots; many lack public operator facility pages. Grade C until confirmed.
- **TSBG / Telecom Service Bulgaria** - directory listings identify Plovdiv and Kapitan Andreevo/Haskovo data-center or colo nodes; verify with operator legal site, PeeringDB, and municipal records. Grade C.
- **ESCOM Haskovo** - directory/Inflect/Data Center Platform seed; official ESCOM website confirms company presence but not necessarily full data-center specs. Grade C.

Regional templates:

```text
"SDC Ruse" Neterra "data center"
"Нетерра" Русе "център за данни"
"Telepoint" Montana "data center" OR "Монтана"
"A1" Монтана "колокационен център" OR "Data Center"
"Vivacom" "Eutelsat" "Stara Zagora" "mini data centre"
"Виваком" "Стара Загора" "мини център за данни"
"TSBG" "Kapitan Andreevo" "data center"
"ESCOM" Haskovo "data center"
"Neterra" Pazardzhik Pleven Razgrad Sliven "data center"
```

---

## 4. Cloud, Edge, and Interconnect Interpretation

- **No major hyperscaler public cloud region should be inferred for Bulgaria without official current confirmation.** As of this methodology pass, official AWS, Azure, Google Cloud, and Oracle global-region pages should be rechecked before every census update; do not count offices, partner programs, cache/edge POPs, or interconnect points as hyperscale owned regions.
- **Google Cloud** - official Google sources have historically identified Sofia as a network PoP/cache/peering location; Google Cloud region/location lists should be used to check for actual public cloud regions. A Sofia network PoP is interconnect/edge evidence, not a Bulgarian Google cloud region.
- **Exoscale** - official Exoscale Bulgaria page is a strong cloud-zone signal for `BG-SOF-1`; other sources place it at A1 Lift. Use Exoscale/A1 as a Sofia commercial cloud/colo lead, not a hyperscale region.
- **BIX.BG / DE-CIX Sofia / NetIX / PeeringDB** - strongest interconnect-discovery surface. A facility appearing as an IX PoP or PeeringDB facility is good evidence of an active interconnection site, but it does not prove wholesale colocation scale or MW capacity.
- **BRAIN++ / Discoverer++ / Sofia Tech Park** - public/HPC/AI-factory infrastructure. Count separately from commercial colo/hyperscale unless the inventory schema includes research/public compute facilities.
- **VueNow edge claims** - keep as historical planned edge lead unless refreshed by official local permits, operator construction evidence, or current Bulgarian press.

Cloud/edge queries:

```text
site:aws.amazon.com Bulgaria Sofia "Local Zone" OR "Wavelength"
site:learn.microsoft.com/azure "Bulgaria" "region"
site:azure.microsoft.com "Bulgaria" "region"
site:cloud.google.com/about/locations Bulgaria Sofia
site:docs.cloud.google.com "Sofia" "Cloud Interconnect" OR "Bulgaria"
site:oracle.com/cloud/public-cloud-regions Bulgaria Sofia
"Exoscale" "BG-SOF-1" "A1 Lift"
"Google" "Sofia" "PoP" "Bulgaria"
"BIX.BG" "data centers" Sofia
site:peeringdb.com/fac Bulgaria Sofia
```

---

## 5. District-by-District Enumeration Approach

For every district, run four passes:

1. **Operator/directory pass**: known operators + city name in English/Bulgarian; DataCenterMap, Baxtel, Datacenters.com, Inflect, PeeringDB.
2. **Municipality pass**: municipal sites for `разрешение за строеж`, `ПУП`, council minutes, `инвестиционно предложение`, and `сървърно помещение`.
3. **Environment/power pass**: relevant RIEW, MOEW, local utility/grid, industrial-zone pages, and generator/substation terms.
4. **Procurement/public-sector pass**: AOP/CAIS EOP plus universities, hospitals, municipalities, regional agencies, and state entities for server-room/data-center tenders.

| Manifest district | Bulgarian/local query names | Priority and query notes |
|---|---|---|
| Blagoevgrad | Благоевград | Low known colo density. Search Blagoevgrad, Sandanski, Petrich, Gotse Delchev for public-sector server rooms, industrial parks, and telecom POPs. Queries: `"център за данни" Благоевград`, `"сървърно помещение" Благоевград`, `site:blagoevgrad.bg "разрешение за строеж" "център за данни"`, `site:riosvbl.org "център за данни"`. |
| Burgas | Бургас | High priority because of Top Systems BOJ and VueNow historical lead. Also check port/logistics/industrial park, A1/Neterra regional claims. Queries: `"Top Systems" Бургас`, `"център за данни" Бургас "Индустриален и логистичен парк"`, `site:burgas.bg`, `site:riosvbs.com`. |
| Varna | Варна | High priority for AC DC/AbsCloud, Varna Data Center, A1 regional colocation, port/telecom edge. Queries: `"AC DC" Варна "зелен data center"`, `"Varna Data Center"`, `"колокация" Варна`, `site:varna.bg "център за данни"`, `site:riosv-varna.bg`. |
| Veliko Tarnovo | Велико Търново | No strong known large seed. Search local hosters, university/public-sector DR, telecom POPs. Queries: `"център за данни" "Велико Търново"`, `"сървърна зала" "Велико Търново"`, `site:veliko-tarnovo.bg "сървърно помещение"`. |
| Vidin | Видин | Low probability; border-connectivity and municipal IT leads only. Queries: `"център за данни" Видин`, `"колокация" Видин`, `site:vidin.bg "сървърно помещение"`, `site:riosv-montana.com Видин "инвестиционно предложение"`. |
| Vratsa | Враца | Low/moderate; search telecom, public institutions, industrial/power corridor. Queries: `"център за данни" Враца`, `"сървърно помещение" Враца "обществена поръчка"`, `site:vratsa.bg`, `site:riosv-vratza.bg`. |
| Gabrovo | Габрово | Low known colo density; university/municipal IT and industrial leads. Queries: `"център за данни" Габрово`, `"сървърна зала" Габрово`, `site:gabrovo.bg "разрешение за строеж"`. |
| Dobrich | Добрич | Low known DC density but check wind/renewable industrial sites and municipal ICT. Queries: `"център за данни" Добрич`, `"data center" Dobrich Bulgaria`, `site:dobrich.bg "сървърно помещение"`, `site:riosv-varna.bg Добрич "център за данни"`. |
| Kardzhali | Кърджали | Low; check public-sector tenders and small ISP rooms. Queries: `"център за данни" Кърджали`, `"сървърно помещение" Кърджали`, `site:kardjali.bg`, `site:riosv-hs.org Кърджали`. |
| Kyustendil | Кюстендил | Historical VueNow "region around Kyustendil" lead; otherwise low. Queries: `"VueNow" Kyustendil`, `"център за данни" Кюстендил`, `site:kn.government.bg "център за данни"`, `site:riosv-pernik.com Кюстендил`. |
| Lovech | Ловеч | Low; search municipal/industrial park and telecom rooms. Queries: `"център за данни" Ловеч`, `"сървърна зала" Ловеч`, `site:lovech.bg "разрешение за строеж"`. |
| Montana | Монтана | Telepoint/A1 regional lead. Verify current status carefully because Digital Realty acquisition is Sofia-specific. Queries: `"Telepoint" Монтана "data center"`, `"A1" Монтана "колокационен център"`, `"център за данни" Монтана`, `site:montana.bg`. |
| Pazardzhik | Пазарджик | Directory-only Neterra seed; verify via operator/local sources. Queries: `"Neterra" Pazardzhik "data center"`, `"Нетера" Пазарджик`, `"център за данни" Пазарджик`, `site:pazardzhik.bg`, `site:riosv-pz.com`. |
| Pernik | Перник | Sofia-adjacent overflow possibility; search industrial land, substations, and DR facilities. Queries: `"център за данни" Перник`, `"дейта център" Перник`, `site:pernik.bg "ПУП" "център за данни"`, `site:riosv-pernik.com "център за данни"`. |
| Pleven | Плевен | Directory-only Neterra seed; public/hospital/university server rooms possible. Queries: `"Neterra" Pleven "data center"`, `"център за данни" Плевен`, `site:pleven.bg "сървърно помещение"`. |
| Plovdiv | Пловдив | Highest non-Sofia priority. Brinell/Rakovski/Maritsa, CETIN Trakia, Evolink, Neterra/TSBG, VueNow historical. Use municipality, Maritsa/Rakovski sites, TEZ, and RIEW Plovdiv. Queries listed in section 3.2. |
| Razgrad | Разград | Directory-only Neterra seed; verify. Queries: `"Neterra" Razgrad "data center"`, `"център за данни" Разград`, `site:razgrad.bg "сървърно помещение"`, `site:riosv-ruse.org Разград`. |
| Ruse | Русе | High priority due official SDC Ruse; also Danube/border interconnect. Queries: `"SDC Ruse"`, `"Нетерра" Русе "център за данни"`, `site:ruse-bg.eu "център за данни"`, `site:riosv-ruse.org "център за данни"`. |
| Silistra | Силистра | Low; check municipal/public-sector and telecom edge. Queries: `"център за данни" Силистра`, `"сървърно помещение" Силистра`, `site:silistra.bg`. |
| Sliven | Сливен | Directory-only Neterra seed; verify. Queries: `"Neterra" Sliven "data center"`, `"център за данни" Сливен`, `site:sliven.bg`, `site:riosv-stz.org Сливен`. |
| Smolyan | Смолян | Low; mountainous connectivity/public-sector leads. Queries: `"център за данни" Смолян`, `"сървърно помещение" Смолян`, `site:smolyan.bg`. |
| Sofia (stolitsa) | София-град / Столична община | Highest priority. Operators: Digital Realty/Telepoint, Equinix, Neterra SDC1/2, A1/Exoscale, Daticum, Evolink, CETIN Serdika, BIX/NetIX, BRAIN++ Sofia Tech Park. Use section 3.1 templates. |
| Sofia | София област | High priority for Stolnik/Neterra and Sofia-adjacent land in Elin Pelin, Bozhurishte, Kostinbrod, Ihtiman, Botevgrad, Samokov. Query SDC Stolnik, industrial parks, substations, and `data center park`. Queries: `"SDC Stolnik"`, `"Data Center Park Stolnik"`, `"център за данни" "Елин Пелин"`, `site:elinpelin.org "център за данни"`, `site:riosv-sofia.org "Столник" "център за данни"`. |
| Stara Zagora | Стара Загора | Vivacom/Eutelsat ground-station mini data-centre lead; also energy-rich Maritsa East region can attract AI/DC rumors. Queries: `"Vivacom" "Eutelsat" "Stara Zagora" "mini data centre"`, `"мини център за данни" "Стара Загора"`, `"център за данни" "Стара Загора"`, `site:starazagora.bg`, `site:riosv-stz.org`. |
| Targovishte | Търговище | Low; check public tenders/local hosters. Queries: `"център за данни" Търговище`, `"сървърно помещение" Търговище`, `site:targovishte.bg`. |
| Haskovo | Хасково | ESCOM Haskovo and TSBG Kapitan Andreevo directory leads; border/interconnect angle. Queries: `"ESCOM" Хасково "data center"`, `"TSBG" "Капитан Андреево" "data center"`, `"център за данни" Хасково`, `site:haskovo.bg`, `site:riosv-hs.org`. |
| Shumen | Шумен | A1 regional colocation lead; otherwise small/telecom/public sector. Queries: `"A1" Шумен "колокационен център"`, `"център за данни" Шумен`, `site:shumen.bg "сървърно помещение"`, `site:riosv-shumen.eu`. |
| Yambol | Ямбол | Low; check public-sector and industrial/power corridor. Queries: `"център за данни" Ямбол`, `"сървърно помещение" Ямбол`, `site:yambol.bg`, `site:riosv-stz.org Ямбол`. |

---

## 6. Verification Rules and Common Pitfalls

### 6.1 Evidence hierarchy

1. **A - primary/official**: operator official facility page, cloud provider official zone/region page, IX official PoP/facility page, municipality building permit/PUP/council record, RIEW/MOEW environmental decision, CAIS EOP/AOP procurement record, official government/EuroHPC/INSAIT/Sofia Tech Park release.
2. **B - strong secondary**: DCD, Economic.bg, Capital.bg, TechNews.bg, BTA, SeeNews, credible local press citing government/operator documents.
3. **C - lead only**: DataCenterMap, Datacenters.com, Baxtel, Inflect, Cloudscene, OCOLO, DC Atlas, social posts, market-report snippets, old MoUs.

### 6.2 Status mapping

- `меморандум`, `намерение`, `планира`, `ще изгради`, `инвестиционно намерение`, `ПУП в процес`, `терен` = planned/proposed.
- `одобрен ПУП`, `одобрен инвестиционен проект`, `разрешение за строеж`, `строителството започва`, `в процес на изграждане` = approved / construction-enabling / under construction.
- `въведен в експлоатация`, `Акт 16`, `откри`, `работи`, `operational`, `opened`, `launched` = operational, but still distinguish facility shell, powered capacity, and IT load.
- Capacity terms: separate `installed capacity`, `dedicated power`, `renewable supply`, `rack capacity`, `future expansion`, and `grid connection`. Bulgarian articles often repeat investment value without MW.

### 6.3 Pitfalls

- Do not double count Telepoint Sofia East/Sofia Centre under Telepoint and Digital Realty after the 2026 acquisition.
- Do not misassign `SDC Stolnik` to Sofia city; it is in Sofia district even when marketed as Sofia metro.
- Do not count Exoscale BG-SOF-1 as a hyperscaler region; it is an Exoscale cloud zone hosted in/with A1 infrastructure.
- Do not count Google/AWS/Azure/Oracle office, cache, network PoP, or interconnect hints as owned cloud regions.
- Do not treat `Cloud Виртуален център за данни` in procurement as a physical facility unless the tender is for construction/fit-out/operation of rooms, power, cooling, racks, or a named site.
- Do not count hospital, university, municipal, or satellite ground-station server rooms as commercial colocation unless the source says they sell/offer colocation or data-center services. Tag them as public/HPC/enterprise/edge infrastructure.
- Treat VueNow 2021 Bulgarian edge sites as stale MoU leads until refreshed by construction/permit/operator evidence.
