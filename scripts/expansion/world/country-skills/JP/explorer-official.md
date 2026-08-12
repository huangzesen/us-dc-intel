# JP Explorer — Official / Regulatory / Cloud Pipeline for Japan Datacenter Enumeration

Date: 2026-08-12. Country: **JP Japan**. Division model for world expansion: **47 prefectures + municipalities / wards / cities**. Scope: methodology to enumerate datacenter projects through Japanese official planning and building channels, power and energy-efficiency evidence, subsidy / industrial-policy lists, official cloud-region pages, and primary operator facility pages. Reliability grades: **A** = official / primary / legally accountable source, **B** = strong secondary or industry association source, **C** = weak lead only.

---

## 0. Japan-Specific Structure Facts

- Japan has **no single datacenter operating license** and no national searchable planning-permit portal equivalent to US county permit data or China investment filings. A datacenter usually appears as a building / telecommunications / warehouse / office / industrial facility depending on local zoning and filing style.
- Enumeration should be **municipality-first inside prefectures** for planning/building evidence, then bucket results to prefectures. Important public records sit with city/ward governments, prefectural governments, designated building-confirmation inspection bodies, environmental-plan systems, city-planning councils, and local assemblies.
- Power is a major siting constraint. In Greater Tokyo, the high-yield trail is **TEPCO Power Grid / transmission-substation context + Inzai / Shiroi / Chiba municipal planning records + operator announcements**. In Kansai, use Kansai Transmission and Distribution / Osaka municipal records / Keihanna and Sakai official announcements. Hokkaido, Fukushima, Kyushu, and other regions require regional utility and subsidy joins.
- National industrial policy encourages regional dispersal. METI subsidy programs and GX / Watt-Bit policy documents are useful top-down seed lists, but they are not complete registries and often describe infrastructure support rather than a building permit.
- Official cloud pages prove operational **region / metro** presence: AWS Tokyo and Osaka, Azure Japan East and West, Google Cloud Tokyo and Osaka, OCI Tokyo and Osaka. They do not disclose exact campuses; join to operator, building, and utility evidence.

---

## 1. Japanese + English Query Patterns

Use Japanese first for permits and local-government records; English works best for hyperscale / global colo announcements.

### 1.1 Planning / Building / Local Government

```
"{市区町村}" "データセンター" "建築確認"
"{市区町村}" "データセンター" "建築計画"
"{市区町村}" "データセンター" "開発行為"
"{市区町村}" "データセンター" "景観審議会"
"{市区町村}" "データセンター" "都市計画審議会"
"{市区町村}" "データセンター" "地区計画"
"{市区町村}" "データセンター" "住民説明会"
"{市区町村}" "データセンター" "議事録"
site:{municipality-domain}.lg.jp データセンター 建築確認
site:{prefecture-domain}.lg.jp データセンター 開発許可
```

English variants:

```
"{city}" "data center" "building permit" Japan
"{city}" "data centre" "planning" Japan
"{operator}" "{city}" "data center" Japan
"{operator}" "{prefecture}" "data center" "MW"
```

### 1.2 Energy / Grid / Utility

```
"データセンター" "特別高圧" "{市区町村}"
"データセンター" "変電所" "{市区町村}"
"データセンター" "系統接続" "{電力会社}"
"データセンター" "受電" "MW" "{市区町村}"
"データセンター" "省エネ法" "PUE"
"データセンター" "ベンチマーク制度"
site:tepco.co.jp/pg データセンター
site:kepco.co.jp データセンター 変電所
site:enecho.meti.go.jp データセンター 省エネ
site:meti.go.jp データセンター 電力系統
```

### 1.3 MIC / Telecom / JDCC

```
site:soumu.go.jp データセンター 電気通信事業
site:soumu.go.jp 電気通信事業者 届出 一覧 "{operator}"
site:soumu.go.jp 登録電気通信事業者 一覧 "{operator}"
site:jdcc.or.jp "{operator}"
site:jdcc.or.jp "会員一覧"
```

### 1.4 Operator / Cloud

```
AWS 東京 リージョン ap-northeast-1
AWS 大阪 リージョン ap-northeast-3
Azure Japan East Japan West Tokyo Saitama Osaka
Google Cloud 東京 大阪 asia-northeast1 asia-northeast2
Oracle Cloud Japan East Tokyo Japan Central Osaka
Equinix TY 東京 データセンター
NTT Global Data Centers Japan Tokyo Osaka Shiroi Keihanna
KDDI Telehouse Osaka Sakai data center
IDC Frontier 東京府中 北九州 白河 データセンター
SoftBank 苫小牧 AI データセンター 堺 データセンター
さくらインターネット 石狩 データセンター
```

---

## 2. Grade-A Planning / Building-Permit Sources

### 2.1 Building Standards Act / Building Confirmation

- Legal framework: Building Standards Act (建築基準法) building confirmation (建築確認), inspected either by the local building official (建築主事 / 建築確認担当) or by a designated confirmation inspection body (指定確認検査機関).
- MLIT reference: https://www.mlit.go.jp/jutakukentiku/house/jutakukentiku_house_tk_000019.html lists Minister-designated confirmation inspection bodies. MLIT also published technical advice on container-type datacenters under Building Standards Act treatment: https://www.mlit.go.jp/report/press/house05_hh_000234.html
- Grade: **A** when a confirmation / public local-government record names the project, building owner, parcel, building use, floor area, construction period, or council review item.
- Caveat: many private building-confirmation certificates are not publicly searchable. Public visibility often comes indirectly via city planning committees, landscape review, district-plan amendments, environmental-building-plan systems, local assembly minutes, lawsuits, or resident-explanation materials.

Query procedure:

1. Start with the municipality and ward (市区町村) that hosts the suspected facility.
2. Search the municipality site for `データセンター`, `建築確認`, `開発行為`, `景観`, `地区計画`, `都市計画審議会`, `住民説明会`, and `議会 会議録`.
3. Search the prefecture site for development permission / environmental systems.
4. If an address is known, query public building / real-estate registry and local land-use maps manually; Japan's public web surfaces rarely support bulk scraping for private building-confirmation records.

### 2.2 Tokyo Metropolitan Government

- Tokyo datacenter urban-planning guideline page: https://www.toshiseibi.metro.tokyo.lg.jp/machizukuri/smarttokyo/datacenter
- The page publishes **Guidelines for Data Centers Harmonized with Urban Development** and a list of municipal information contacts for datacenter construction. Use this as a current **A-grade process source** for Tokyo, especially Koto, Shinagawa, Minato, Chuo, Otemachi / Chiyoda, Tama, Fuchu, and waterfront sites.
- Tokyo Building Environmental Plan System: https://green-building-pgm.metro.tokyo.lg.jp/KSA00101
- Tokyo environment / CO2 systems can surface large new buildings and facility energy attributes. Search building names, owner names, and `データセンター`; Grade **A** for the submitted building environmental plan metadata.

Tokyo query examples:

```
site:toshiseibi.metro.tokyo.lg.jp データセンター
site:green-building-pgm.metro.tokyo.lg.jp データセンター
site:kankyo.metro.tokyo.lg.jp データセンター 環境計画書
site:city.koto.lg.jp データセンター 建築計画
site:city.shinagawa.tokyo.jp データセンター 建築
site:city.fuchu.tokyo.jp データセンター
```

### 2.3 Chiba / Inzai / Shiroi

- Inzai is Japan's most important hyperscale cluster. Public evidence is often city-planning and council material rather than a simple permit table.
- Inzai example source: city press conference page discussing datacenter building confirmation and district-plan changes: https://www.city.inzai.lg.jp/0000021271.html
- Inzai district-plan materials can explicitly state whether datacenter construction is allowed or restricted in specific zones, e.g. Inzai Makinohara East district plan material: https://www.city.inzai.lg.jp/cmsfiles/contents/0000021/21322/kaigiroku.pdf
- Use Shiroi City and Chiba Prefecture searches for the NTT / TEPCO Shiroi project and Inzai-Shiroi cluster expansion.

Chiba query examples:

```
site:city.inzai.lg.jp データセンター
site:city.inzai.lg.jp データセンター 建築確認
site:city.inzai.lg.jp データセンター 地区計画
site:city.shiroi.chiba.jp データセンター
site:pref.chiba.lg.jp データセンター 印西
site:pref.chiba.lg.jp データセンター 白井
```

### 2.4 Osaka / Kansai / Keihanna

- Osaka City publishes building environmental plan summaries for large buildings; example list page: https://www.city.osaka.lg.jp/toshikeikaku/page/0000665562.html
- Osaka City building confirmation procedure page: https://www.city.osaka.lg.jp/toshikeikaku/page/0000032271.html
- Keihanna projects may sit in Kyoto / Nara / Osaka border municipalities and national research-city planning contexts. Search Kyoto Prefecture, Seika Town, Kizugawa, Nara, and NTT releases.
- Sakai and former industrial/factory conversions need municipal planning, fire, hazardous-material, and building-conversion checks; do not assume a conversion is live until occupancy / operator start evidence appears.

Kansai query examples:

```
site:city.osaka.lg.jp データセンター 建築物環境計画書
site:city.sakai.lg.jp データセンター
site:pref.osaka.lg.jp データセンター
site:pref.kyoto.jp データセンター けいはんな
site:town.seika.kyoto.jp データセンター
site:city.kizugawa.lg.jp データセンター
```

---

## 3. Energy, Grid, and Environmental Pipeline

### 3.1 METI / Agency for Natural Resources and Energy

- Agency for Natural Resources and Energy datacenter energy page: https://www.enecho.meti.go.jp/about/special/johoteikyo/data_center2026.html
- Data-center benchmark / guidance PDF under the Energy Conservation Act framework: https://www.enecho.meti.go.jp/category/saving_and_new/saving/enterprise/factory/support-tools/data/dc_guideline.pdf?update=260603
- Benchmark system overview page includes datacenter PUE as a benchmark field: https://www.enecho.meti.go.jp/category/saving_and_new/saving/enterprise/overview/institution/
- Energy White Paper 2025 discusses datacenter concentration, grid infrastructure, and Watt-Bit coordination: https://www.enecho.meti.go.jp/about/whitepaper/2025/html/1-2-2.html and https://www.enecho.meti.go.jp/about/whitepaper/2025/html/2-6-1.html
- Grade: **A** for national rules, targets, policy constraints, and official lists of companies / subsidy recipients; **B** for project inference where a policy document names only a region or infrastructure class.

Extraction value:

- PUE / energy-efficiency target and reporting context.
- Operators subject to public disclosure or benchmark classification if named in policy systems.
- Grid-siting signals and regions encouraged for distributed AI / datacenter siting.

### 3.2 TEPCO Power Grid and Regional Utilities

- TEPCO PG + NTT Global Data Centers Japan joint development release: https://www.tepco.co.jp/pg/company/press-information/press/2023/1666668_8618.html
- Same NTT English release: https://services.global.ntt/en-us/newsroom/ntt-gdc-japan-and-tepco-power-grid-to-establish-a-new-company
- The NTT / TEPCO source is high-value because it explicitly links datacenter development to the **Inzai-Shiroi area**, power and connectivity, and planned service timing. Grade **A** as primary operator / utility evidence.
- For other regions, use the relevant general transmission and distribution utility: Kansai TD, Chubu PG, Tohoku Electric Power Network, Hokkaido Electric Power Network, Kyushu Electric Power TD, Chugoku, Shikoku, Hokuriku, and Okinawa.

Utility query templates:

```
site:tepco.co.jp/pg データセンター 印西 OR 白井
site:tepco.co.jp/pg データセンター 特別高圧
site:kansai-td.co.jp データセンター
site:chuden.co.jp データセンター 変電所
site:hepco.co.jp データセンター 苫小牧
site:tohoku-epco.co.jp データセンター 福島
site:kyuden.co.jp データセンター 北九州
```

Reliability:

- **A**: utility or government document names the operator / project / substation / supply arrangement.
- **B**: credible press reports a named power request or substation upgrade tied to a known campus.
- **C**: generic "power secured" or "low-cost power" marketing copy.

### 3.3 Environmental Assessment and Building Environmental Plans

- National environmental assessment support network: https://assess.env.go.jp/
- EADAS GIS database: https://eadas.env.go.jp/
- Statutory national EIA categories are mostly roads, dams, railways, airports, power plants, and similar large infrastructure, not ordinary datacenters. Therefore national EIA is **high precision but low recall** for datacenter enumeration.
- The better DC channel is prefectural / municipal **building environmental plan** and large-building energy systems, e.g. Tokyo and Osaka pages above.

Query examples:

```
site:assess.env.go.jp データセンター
site:eadas.env.go.jp データセンター
site:{prefecture-domain}.lg.jp データセンター 環境影響評価
site:{city-domain}.lg.jp データセンター 建築物環境計画書
site:{city-domain}.lg.jp データセンター CASBEE
```

What to extract: owner, project name, building name, floor area, energy systems, planned completion, environmental score, district / parcel, and whether the filing is new construction, expansion, or conversion.

---

## 4. METI Subsidy / Industrial-Policy Sources

### 4.1 Datacenter Regional Base Development Subsidy

- METI public call page for FY2023 "Data Center Regional Base Development Project Subsidy": https://www.meti.go.jp/information/publicoffer/kobo/2023/k230922001.html
- METI adoption result page: https://www.meti.go.jp/information/publicoffer/saitaku/2023/s231107001.html
- Budget materials also describe datacenter regional-base infrastructure support, including power supply and telecom line work: https://www.meti.go.jp/main/yosan/yosan_fy2025/hosei/pdf/r7_gaiyo.pdf
- Grade: **A** for award recipient / subsidy scope; **B** for inferred eventual facility if the subsidy supports enabling infrastructure but no building permit or operator page is found.

Use:

1. Pull all subsidy recipient names and project labels.
2. Search each legal name plus `データセンター`, `所在地`, `整備`, `採択`, `開所`, `竣工`.
3. Join to municipal building / utility / operator evidence before counting as live.

### 4.2 GX Strategy Regions / Watt-Bit Coordination

- METI GX strategy region proposal page mentions GX-type datacenter siting with grid infrastructure consideration: https://www.meti.go.jp/press/2025/08/20250826003/20250826003.html
- METI selected first-screening regions page says datacenter-cluster type is selected at candidate-area / municipality granularity: https://www.meti.go.jp/press/2026/04/20260424007/20260424007.html
- METI / Watt-Bit working group materials are useful for identifying emerging suitable areas and anti-speculation rules around grid reservation; example search target: https://www.meti.go.jp/shingikai/economy/watt_bit/watt_bit_wg/
- Grade: **A** for policy and official candidate-region status; **C/B** as facility evidence until a project/operator is named.

---

## 5. MIC / Regulator and JDCC Sources

### 5.1 MIC Telecommunications Business Act

- Japanese Law Translation, Telecommunications Business Act: https://www.japaneselawtranslation.go.jp/en/laws/view/3648/en
- Article 9 registration and Article 16 notification apply to telecommunications businesses. Colo real-estate operation alone is not a universal datacenter license, but many cloud / hosting / connectivity providers will appear as registered or notified telecommunications carriers.
- MIC / regional telecom bureaus publish lists and manuals; search `登録電気通信事業者一覧`, `届出電気通信事業者一覧`, and `電気通信事業参入マニュアル`.
- Grade: **A** for operator legal status / telecom-business evidence; not a facility registry.

Use:

- Search operator names: Equinix Japan, NTT, KDDI, IDC Frontier, Sakura Internet, SoftBank, BBIX, Internet Initiative Japan, KVH / Colt, MC Digital Realty, AT TOKYO, OPTAGE, QTnet, BroadBand Tower, GMO, NEC, Fujitsu, Hitachi Systems.
- Join telecom registration to facility pages and municipal records; do not count facilities solely from MIC telecom status.

### 5.2 Japan Data Center Council (JDCC)

- JDCC main: https://www.jdcc.or.jp/
- JDCC English overview: https://www.jdcc.or.jp/english/
- JDCC official member list: https://www.jdcc.or.jp/english/menbers.html
- Grade: **B** for industry-member universe and operator discovery; **A** only for JDCC's own statements about standards / council identity. JDCC does not provide a complete facility registry.

Use JDCC to seed operators, constructors, facility managers, network providers, and consultants, then pivot to official operator / government evidence.

---

## 6. Official Cloud Provider Region Pages

Cloud pages are **A-grade evidence for operational cloud region / metro presence**, but only metro-level evidence unless paired with facility filings.

| Provider | Official source | Japan regions / locations | Enumeration value |
|---|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | Asia Pacific (Tokyo) `ap-northeast-1` with 4 AZs; Asia Pacific (Osaka) `ap-northeast-3` with 3 AZs | Search Amazon Data Services Japan / AWS operator and colo partners in Greater Tokyo / Chiba and Osaka / Kansai; official page does not reveal campuses. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | Japan East `japaneast` in Tokyo / Saitama; Japan West `japanwest` in Osaka | Search Microsoft Japan / Azure / partner operators in Tokyo, Saitama, Chiba, Osaka. |
| Google Cloud | https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones | Tokyo `asia-northeast1`; Osaka `asia-northeast2` | Search Google / partner colos and interconnect locations around Tokyo / Osaka; official docs confirm region names. |
| Oracle Cloud Infrastructure | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm and https://www.oracle.com/cloud/public-cloud-regions/ | Japan East (Tokyo) `ap-tokyo-1`; Japan Central (Osaka) `ap-osaka-1` | Search Oracle / OCI Japan East / Japan Central plus colo partners and peering facilities. |

Cloud-region query templates:

```
"Amazon Data Services Japan" "データセンター" "印西"
"AWS" "ap-northeast-1" "data center" Japan
"Microsoft" "Japan East" "Tokyo" "Saitama" "data center"
"Google Cloud" "asia-northeast1" "Tokyo" "data center"
"Google Cloud" "asia-northeast2" "Osaka" "data center"
"Oracle" "ap-tokyo-1" "data center" Japan
"Oracle" "ap-osaka-1" "data center" Japan
```

---

## 7. Official / Primary Operator Facility Pages

Operator facility pages are primary statements by the owner. Use as **A** for marketed existence / city / facility specs and **B** for future capacity unless backed by permit, utility, or official opening evidence.

| Operator | Official source | Japan footprint signals | Follow-up joins |
|---|---|---|---|
| Equinix | Japan overview: https://www.equinix.com/data-centers/asia-pacific-colocation/japan-colocation ; Tokyo: https://www.equinix.com/data-centers/asia-pacific-colocation/japan-colocation/tokyo-data-centers ; Osaka: https://www.equinix.com/data-centers/asia-pacific-colocation/japan-colocation/osaka-data-centers | Equinix says it operates in Tokyo and Osaka, with multiple TY and OS facilities; Tokyo page lists TY1, TY2, TY3, TY11, TY12x, TY13x, TY15 and states 14 Tokyo data centers. | Join TY facility names to Koto, Shinagawa, Minato, Chiba, and Osaka municipal records; xScale sites are strong leads for hyperscale capacity. |
| NTT Global Data Centers / NTT DATA | Global locations: https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/asia-pacific ; Osaka OSK12: https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/asia-pacific/osaka-osk12-data-center ; Keihanna opening: https://www.nttdata.com/global/en/news/press-release/2026/april/040900 | Tokyo, Osaka, Shiroi / Inzai-Shiroi, Keihanna. OSK12 page states 18MW IT load as first building on 36MW campus. | Join to TEPCO / Chiba sources for Shiroi and to Kyoto / Keihanna municipality records for Keihanna. |
| NTT DOCOMO Business / Nexcenter | https://www.ntt.com/en/services/data-center/nexcenter/data-center/tokyo5.html | Tokyo 5, Osaka 5, and broader Nexcenter footprint. | Join to ward / city building and environmental plan data. |
| KDDI / Telehouse | KDDI service: https://biz.kddi.com/english/service/data-center/ ; Telehouse Japan: https://www.telehouse.net/data-centre-services/japan/ ; Telehouse Japan data centers: https://www.telehouse.com/global-data-centers/asia/japan-data-centers/ ; KDDI Osaka Sakai opening: https://newsroom.kddi.com/english/news/detail/kddi_nr-916_4323.html | Telehouse / KDDI cites 9 strategic Japan locations; Tokyo, Osaka, Nagoya, Fukuoka; KDDI announced Osaka Sakai Data Center operation on 2026-01-22. | Join to Otemachi / Tama / Osaka / Sakai municipal records, power, and interconnect pages. |
| IDC Frontier / IDCF | Overview: https://www.idcf.jp/en/datacenter/ ; locations: https://www.idcf.jp/en/datacenter/location/ ; Kitakyushu: https://www.idcf.jp/en/datacenter/location/asianfrontier/ | Tokyo Fuchu, Fukuoka Kitakyushu / Asian Frontier, Fukushima Shirakawa and other sites. | Join to Fuchu, Kitakyushu, Shirakawa municipal records; also SoftBank / BBIX releases where relevant. |
| SoftBank | Tomakomai AI DC article: https://www.softbank.jp/en/sbnews/entry/20260225_01 | Hokkaido Tomakomai AI Data Center; SoftBank / IDC Frontier regional AI infrastructure. | Join to Tomakomai / Hokkaido permits, utility evidence, METI subsidy / regional-base records. |
| Sakura Internet | Ishikari container DC announcement: https://www.sakura.ad.jp/corporate/en/information/2025/08/14/1968220602/ ; additional Ishikari investment PDF: https://www.sakura.ad.jp/corporate/wp-content/uploads/2025/03/en-250321-ir_1.pdf | Ishikari Data Center in Hokkaido; container-type DC at Ishikari completed May 2025 with approx. 3.5MVA and 40 racks. | Join to Ishikari / Hokkaido records and METI cloud / AI subsidy context. |
| AT TOKYO | https://www.attokyo.com/ | Major Tokyo colo operator; official pages and news can confirm facility / interconnect relationships. | Join to Tokyo building environmental plans and ward records. |
| MC Digital Realty / Digital Realty | https://www.mcdigitalrealty.com/ and Digital Realty official pages | Osaka and Tokyo campuses / KIX naming, often with high MW-class specs. | Join to Osaka / Inzai / Chiba / Tokyo municipal records and energy evidence. |
| Colt DCS / KVH, OPTAGE, QTnet, BBIX, IIJ, BroadBand Tower, GMO, NEC, Fujitsu, Hitachi Systems | Official operator facility pages / securities filings | Regional and carrier / enterprise DCs; especially Kansai, Kyushu, Tokyo, and disaster-recovery sites. | Use operator pages as seed, then verify with local planning, telecom registration, power, and building-environment records. |

---

## 8. Systematic Prefecture / Municipality Enumeration Method

Run this for each prefecture, but prioritize high-density municipalities first.

1. **Top-down seed list**: cloud regions (§6), official operator pages (§7), METI subsidy / GX / Watt-Bit sources (§4), JDCC member list (§5), and known clusters: Tokyo wards, Chiba Inzai / Shiroi, Osaka / Sakai, Keihanna, Hokkaido Ishikari / Tomakomai, Fukushima Shirakawa, Fukuoka Kitakyushu.
2. **Municipality sweep**: for each candidate city/ward, search local site and council minutes for `データセンター`, `建築確認`, `建築計画`, `開発行為`, `地区計画`, `景観`, `都市計画審議会`, `住民説明会`, `議事録`.
3. **Prefecture sweep**: search prefectural site for development permission, environmental assessment, industrial land, subsidy, regional strategy, and disaster-resilience programs.
4. **Building environmental plan / large-building systems**: Tokyo, Osaka, and many large cities expose environmental plans or CASBEE-style summaries. Search operator names and generic `データセンター`.
5. **Power join**: search regional utility and METI / ANRE materials for substation, grid connection, special high-voltage, utility partnerships, and electricity-demand discussions. Treat power reservation without a named project as a lead only.
6. **Telecom / corporate join**: query MIC telecom registration / notification lists for operator legal status; use corporate filings and annual reports for listed operators such as NTT, KDDI, SoftBank, Sakura Internet, OPTAGE / Kansai Electric group, and real-estate owners.
7. **Operator confirmation**: attach official facility page / press release. Extract facility name, city, planned opening, MW / racks / floor area if available, certifications, and cloud on-ramp functions.
8. **Status resolution**: distinguish planned / subsidy-awarded / building-confirmed / under construction / completed / operational. Japan has many conversion and AI-campus announcements; do not count live capacity without opening, service-start, customer-availability, or occupancy evidence.

High-priority search matrix:

| Region | Municipal targets | Primary source types |
|---|---|---|
| Tokyo | Koto, Shinagawa, Minato, Chiyoda / Otemachi, Chuo, Fuchu, Tama, Hino, Akishima, waterfront wards | Tokyo datacenter guideline, green-building plan system, ward planning records, Equinix / AT TOKYO / NTT / KDDI pages |
| Chiba | Inzai, Shiroi, Chiba City, Sakura, Narita-adjacent areas | Inzai / Shiroi city records, Chiba Prefecture, TEPCO PG, NTT / Equinix xScale / hyperscaler clues |
| Saitama / Kanagawa | Saitama, Toda, Kawaguchi, Yokohama, Kawasaki, Sagamihara | municipal planning, Azure Japan East clue, operator pages, utility records |
| Osaka | Osaka City, Sakai, Ibaraki, Minoh, Suita, Kadoma, Nakanoshima / OBP | Osaka building environmental plans, KDDI Sakai, Equinix OS, NTT OSK, MC Digital Realty |
| Kyoto / Nara / Keihanna | Seika, Kizugawa, Kyotanabe, Nara border | NTT Keihanna, Kyoto / local planning, research-city materials |
| Hokkaido | Ishikari, Tomakomai, Sapporo | Sakura Ishikari, SoftBank Tomakomai, Hokkaido utility, METI subsidies |
| Fukushima / Tohoku | Shirakawa, Fukushima Hamadori, Sendai | IDC Frontier Shirakawa, AI Fukushima / METI regional policy, Tohoku utility |
| Kyushu | Kitakyushu, Fukuoka, Kumamoto, Okinawa edge | IDC Frontier Kitakyushu, QTnet, BBIX / SoftBank, Kyushu utility, local industrial land |
| Chubu | Nagoya, Toyota, Gifu / Mie, Shizuoka | KDDI / carrier facilities, Chubu utility, local enterprise DCs |

---

## 9. Evidence-Grade Mapping for Japan

| Grade | Definition | Japan sources |
|---|---|---|
| **A** | Official or primary source with legal / operator accountability | Building confirmation or local-government planning record; city / prefecture council minutes naming project; building environmental plan; METI / ANRE subsidy result or energy-policy list; utility release naming project; MIC telecom registration / notification for operator status; official cloud region page; official operator facility page / press release; listed-company securities filing |
| **B** | Strong secondary or corroborated industry evidence | JDCC member list for operator universe; respected trade press (DCD, Nikkei, Impress, Data Center Cafe) when it names owner/site/MW; real-estate filings; contractor project pages; Baxtel / Data Center Map when corroborated |
| **C** | Weak lead | Consultant market maps, unsourced AI-campus claims, marketing decks without address, social media, stale aggregator records |

Caveats to encode:

- **No national DC registry**: absence from MIC / METI / JDCC does not mean absence of a facility.
- **Building-use ambiguity**: datacenters may be filed as office, warehouse, telecom facility, industrial building, or conversion of factory/office space.
- **Private confirmation inspection**: a valid building confirmation may be issued by a private inspection body and not appear in a simple city search. Use council, landscape, environmental, and resident-explanation records to recover the public trail.
- **Power reservation risk**: grid-connection interest and substation discussions can be speculative. Require building, operator, or subsidy evidence before counting a project.
- **Cloud regions are logical**: AWS/Azure/GCP/OCI official pages prove metro/regional presence, not exact physical addresses.
- **Japanese terms vary**: search both `データセンター` and `データセンタ`, plus `IDC`, `クラウド基盤`, `計算基盤`, `AIデータセンター`, `サーバールーム`, `サーバ棟`.

---

## Quick-Reference URL Index

- MLIT designated confirmation inspection bodies: https://www.mlit.go.jp/jutakukentiku/house/jutakukentiku_house_tk_000019.html
- MLIT container-type datacenter Building Standards Act technical advice: https://www.mlit.go.jp/report/press/house05_hh_000234.html
- Tokyo datacenter urban-development guideline: https://www.toshiseibi.metro.tokyo.lg.jp/machizukuri/smarttokyo/datacenter
- Tokyo Building Environmental Plan System: https://green-building-pgm.metro.tokyo.lg.jp/KSA00101
- Osaka building environmental plan public list example: https://www.city.osaka.lg.jp/toshikeikaku/page/0000665562.html
- Osaka building confirmation procedure: https://www.city.osaka.lg.jp/toshikeikaku/page/0000032271.html
- Inzai datacenter / district-plan public record example: https://www.city.inzai.lg.jp/0000021271.html
- METI datacenter regional-base subsidy call: https://www.meti.go.jp/information/publicoffer/kobo/2023/k230922001.html
- METI datacenter subsidy adoption result: https://www.meti.go.jp/information/publicoffer/saitaku/2023/s231107001.html
- METI GX strategy regions: https://www.meti.go.jp/press/2026/04/20260424007/20260424007.html
- ANRE datacenter energy-efficiency article: https://www.enecho.meti.go.jp/about/special/johoteikyo/data_center2026.html
- ANRE datacenter energy guidance PDF: https://www.enecho.meti.go.jp/category/saving_and_new/saving/enterprise/factory/support-tools/data/dc_guideline.pdf?update=260603
- ANRE benchmark overview: https://www.enecho.meti.go.jp/category/saving_and_new/saving/enterprise/overview/institution/
- TEPCO PG / NTT Inzai-Shiroi release: https://www.tepco.co.jp/pg/company/press-information/press/2023/1666668_8618.html
- Telecommunications Business Act translation: https://www.japaneselawtranslation.go.jp/en/laws/view/3648/en
- JDCC: https://www.jdcc.or.jp/ ; members: https://www.jdcc.or.jp/english/menbers.html
- AWS regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations ; Compute regions: https://docs.cloud.google.com/compute/docs/regions-zones
- OCI regions: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm
- Equinix Japan / Tokyo / Osaka: https://www.equinix.com/data-centers/asia-pacific-colocation/japan-colocation
- NTT Global Data Centers APAC: https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/asia-pacific
- KDDI / Telehouse Japan: https://biz.kddi.com/english/service/data-center/ ; https://www.telehouse.net/data-centre-services/japan/
- IDC Frontier datacenters: https://www.idcf.jp/en/datacenter/
- SoftBank Tomakomai AI DC: https://www.softbank.jp/en/sbnews/entry/20260225_01
- Sakura Internet Ishikari container DC: https://www.sakura.ad.jp/corporate/en/information/2025/08/14/1968220602/

*Compiled for the country-skills JP official/regulatory/cloud explorer. Archive government and operator pages at capture time because Japanese municipal pages and PDF lists move frequently.*
