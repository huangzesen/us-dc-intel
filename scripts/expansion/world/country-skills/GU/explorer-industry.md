# GU · 关岛数据中心探索方法（行业/厂商线路）

范围：`GU = Guam`，manifest 已核实为 `subnational_type: country`、`divisions: ["Guam"]`。行业线路按全岛市场枚举，并用 19 个 villages 做覆盖性搜索；Tumon、Harmon 是 Tamuning 内的高价值子地名，不是额外 division。

本文件是行业/厂商/媒体线路（industry pass）。与 `explorer-official.md`（官方/监管线路）对读后再创建或拒绝设施记录。

## 行业结论（Industry Conclusion）

关岛存在真实商业托管、海缆登陆站 + 数据中心组合设施、以及国防通信/数据中心项目。行业线路的核心不是“是否有 DC”，而是避免把不同类型混在一起：

- **Commercial colo / carrier-neutral DC**：GTA、GNC、Guam Exchange、DOCOMO Pacific、IT&E 是重点；官方产品页可给 A 级服务证据，目录只作补充。
- **Cable landing station / subsea hub**：Piti、Tanguisson、Tumon Bay、Alupang/Agat 等是海缆地名；landing station 只有在来源明确写 data center / colocation 时才升级。
- **Defense / federal**：NAVFAC/SAM.gov/DoD 合同是第一来源；DCD、本地媒体可做线索。
- **Cloud/CDN**：AWS/Azure/GCP/OCI 无 Guam region；Google subsea cables 与 Cloudflare edge 不等同云区域或可枚举 DC。

## 分级规则（Industry Grading）

- **A**：运营商/设施运营方官网（GTA、DOCOMO Pacific、IT&E、Guam Exchange、GNC/RTI 若有官方页）、海缆公司官方页、FCC、SAM.gov、Defense.gov、NAVFAC、DISA、GPA/PUC、官方云区域页。
- **B**：Data Center Dynamics、Submarine Networks、TeleGeography Submarine Cable Map、Pacific Island Times、Pacific Daily News、Guam Daily Post、Marianas Business Journal、Guam Business Magazine、PNC、KUAM、PR Newswire 等具名新闻稿转载。
- **C**：DataCenterMap、Cloudscene、Baxtel、Inflect、Datacenters.com、WHTop、PeeringDB、LinkedIn、招聘帖、社交媒体、SEO 主机目录。

降级规则：`communications facility`、`gateway`、`central office`、`earth station`、`edge server` 不是 data center。除非证据写明 colocation、hosting、data center、racks、第三方机柜、电力/冷却/安全与运营状态，否则只作通信设施线索。

## 1. 运营商与设施运营方（Operators）

### GTA

已核实官方页：

- Data Center: https://www.gta.net/data-center
- Cable Landing Station: https://www.gta.net/cable-landing-station
- Business services: https://www.gta.net/business
- GTA data center news: https://news.gta.net/218940-gta-breaks-ground-on-alupang-data-center/

可确认内容：

- GTA 官方 data center 页列出 GU1/GU2、GU3、HMB IX，并把 GU1/GU2 描述为 Tier 3-designed data centers and cable landing stations；GU1/GU2 约 11,800 sq ft、2 MW；GU3 约 32,000+ sq ft、4 MW，ready for equipment in Q3 2025。
- GTA cable landing station 页明确提供 cable station colocation、power services、到 major data centers / cable landing stations 的光纤。
- 2022 GTA 新闻稿确认 Alupang data center 破土，约 31,000 sq ft，目标为 colocation、稳定电力与 on-island fiber connectivity。

行业模板：

```text
site:gta.net "GU1" OR "GU2" OR "GU3" OR "HMB IX"
site:gta.net "data center" OR "colocation" OR "Tier 3" OR "cable landing"
site:news.gta.net "Alupang Data Center" OR "data center"
"GTA" Guam "GU3" OR "Alupang" OR "Piti-I" OR "GNC"
```

### GNC / RTI / Gateway Network Connections

已核实来源：

- Submarine Networks GNC iX station: https://www.submarinenetworks.com/en/stations/north-america/usa-guam/gnc-cable-landing-station
- RTI/GTA JV article: https://www.submarinenetworks.com/en/stations/north-america/usa-guam/rti-and-gta-to-construct-neutral-cable-landing-station-and-data-center-in-guam
- PR Newswire release: https://www.prnewswire.com/news-releases/gta-and-rti-are-constructing-guams-first-neutral-cable-landing-station-and-data-center-300874340.html

可确认内容：

- GNC iX 被描述为 Guam first combined neutral Cable Landing Station and Data Center，位于 Piti，owned by Gateway Network Connections, LLC。
- JV 新闻稿/转载写明约 11,800 sq ft、250 racks、2 MW、Type 3 designed，计划 Q1 2020 完成。因为当前核实到的是行业/转载页，容量与完成日期按 B/C 处理；设施存在可由 GTA 官方 GU1/GU2 页面交叉确认。

模板：

```text
"Gateway Network Connections" Guam "data center" OR "cable landing"
"GNC iX" Guam "Piti" OR "JGA North" OR "JGA South"
"RTI" "GTA" Guam "neutral cable landing station" "data center"
site:submarinenetworks.com "GNC" "Guam" "data center"
```

### Guam Exchange

已核实官方页：

- Colocation Services: https://guamexchange.com/colocation-services
- Contact/official address appears on the same site: `122 West Harmon Industrial Park Rd Ste. 103, Tamuning, 96913, Guam`

行业补充来源：

- Pacific Island Times launch article: https://www.pacificislandtimes.com/post/citadel-launches-guam-exchange
- Inflect building page: https://inflect.com/building/122-harmon-industrial-park-road-tamuning/guam-exchange/datacenter/guam-exchange-tamuning
- DC Byte facility page: https://www.dcbyte.com/facility/guam-exchange/

可确认内容：

- Guam Exchange 官方页提供 colocation services，称其 state-of-the-art data centers 可承载客户 mission-critical equipment；地址在 Harmon/Tamuning。
- Pacific Island Times 报道 Citadel launches Guam Exchange，并称 Harmon 1 为 open-access, Tier III compliant data center。媒体为 B。
- 面积、电力、容量若只来自 Inflect/DC Byte/Baxtel，按 C 或 B/C 处理，除非 Guam Exchange/Citadel 官方材料确认。

模板：

```text
site:guamexchange.com "colocation" OR "data center" OR "Harmon"
"Guam Exchange" "Harmon 1" OR "Tier III" OR "open access"
"122 West Harmon Industrial Park" "data center" OR "colocation"
site:pacificislandtimes.com "Guam Exchange" "data center"
```

### DOCOMO Pacific

已核实官方页：

- Data Center Colocation: https://business.docomopacific.com/data-center-colocation
- Carrier Services: https://business.docomopacific.com/carrier-services
- About / network: https://www.docomopacific.com/about-us/network
- ATISA FCC announcement: https://aboutus.docomopacific.com/144040-docomo-pacific-announces-grant-of-fcc-license-for-atisa-cable-system/

可确认内容：

- 官方 colocation 页点名 Agana、Harmon、Piti 三个 secure off-site colocation facilities。
- Carrier services 页写明 power、cooling、security、connectivity 与 99.99% SLA。
- DOCOMO Pacific 官方 about 页仍描述其为 NTT DOCOMO wholly owned subsidiary；不要沿用未核实“资产剥离”推测。
- ATISA 官方新闻页确认 FCC 批准 ATISA cable landing license。

模板：

```text
site:business.docomopacific.com "Data Center Colocation" OR Agana OR Harmon OR Piti
site:business.docomopacific.com "carrier services" "data center"
site:docomopacific.com "ATISA" OR "submarine fiber" OR "network"
"DOCOMO PACIFIC" Guam "colocation" OR "data center"
```

### IT&E

已核实官方页：

- Data Services: https://shop.ite.net/business/data-services/
- Managed IT Services: https://shop.ite.net/business/managed-it-services/
- IT&E newsroom: https://ite.pr.co/

可确认内容：

- IT&E data services 页写明 co-location and hosting services，适合作为 A 级服务证据。
- Managed IT services 页提供网络/transport 语境；meet-me points、fiber、transport 不能单独计为 DC。
- 地址、容量和单一设施规格常来自 Inflect/Baxtel/Datacenters.com 等目录，需回填官方或一手证据后再升级。

模板：

```text
site:shop.ite.net/business/data-services "co-location" OR hosting OR facility
site:shop.ite.net/business "data center" OR colocation OR "managed IT"
"IT&E" Guam "colocation" OR "data center" OR "122 Harmon"
"PTI Pacifica" Guam "data center" OR "central office"
```

### NetLabs / local hosting

当前修正：`netlabsguam.com` 未能作为可靠、可复核的 Guam 官方托管源确认。搜索结果更容易命中 unrelated `netlabsglobal.com`。NetLabs 只保留为弱线索，不列入 A 级运营商清单。

模板：

```text
"NetLabs" Guam "hosting" OR "colocation" OR "data center"
"Guam" "server hosting" OR "managed hosting" -GTA -DOCOMO -IT&E
site:whtop.com/directory/country/gu Guam hosting
```

## 2. 海缆与登陆站（Subsea / Landing Stations）

高价值来源：

- TeleGeography Guam page: https://www.submarinecablemap.com/country/guam
- Submarine Networks USA-Guam: https://www.submarinenetworks.com/en/stations/north-america/usa-guam
- Tanguisson station: https://www.submarinenetworks.com/en/stations/north-america/usa-guam/tanguisson
- Tumon Bay station: https://www.submarinenetworks.com/en/stations/north-america/usa-guam/tumon-bay
- AJC Guam landing points: https://ajcable.com/ajc-network/landing-points/guam-landing-points/
- GTA CLS: https://www.gta.net/cable-landing-station
- Google Pacific Connect / Proa / Taihei: https://cloud.google.com/blog/products/infrastructure/pacific-connect-initiative-to-expand
- Google Bulikula / Halaihai: https://cloud.google.com/blog/products/infrastructure/introducing-bulikula-and-halaihai-subsea-cables-to-connect-the-central-pacific

行业解读：

- TeleGeography/Submarine Networks 用于系统名、登陆点、RFS/状态、运营方线索；FCC 或运营方材料用于 A 级确认。
- Piti 和 GNC/GTA 设施有 DC/colo 语言，是 DC 候选重点。
- Tanguisson、Tumon Bay、Tata Piti 等若只有 landing station 语言，默认 `telecom/landing`。
- Google Proa/Taihei/Bulikula/Halaihai 只作为 future/active cable landing 与 connectivity 线索；不要记录为 Google data center。

模板：

```text
"Guam" "landing station" "Piti" OR "Tanguisson" OR "Tumon Bay" OR "Alupang"
"Guam" "GNC iX" OR "Gateway Network Connections" OR "Piti-I"
"AJC" OR "AAG" OR "SEA-US" OR "JGA North" OR "JGA South" "Guam" "landing"
"Proa" OR "Taihei" OR "Bulikula" OR "Halaihai" "Guam" "cable"
site:fcc.gov "Guam" "cable landing"
site:docs.fcc.gov "Guam" "cable landing"
```

## 3. 国防、联邦与承包商（Defense / Federal Vendors）

高价值来源：

- SAM.gov: https://sam.gov/
- Defense.gov contracts: https://www.defense.gov/News/Contracts/
- NAVFAC: https://www.navfac.navy.mil/
- NAVFAC Pacific: https://pacific.navfac.navy.mil/
- Andersen AFB: https://www.andersen.af.mil/
- MCB Camp Blaz: https://www.mcbblaz.marines.mil/
- DISA: https://www.disa.mil/
- Data Center Dynamics Guam search/article: https://www.datacenterdynamics.com/

已核实行业线索：

- NAVFAC Pacific 2025 官方公告授出 Guam communications center upgrades，工程包括 consolidated communications center facility 与 fiber communications cable；这是国防通信设施 A 级线索。
- DCD 2025 报道称 US Navy intends to build data center at Andersen AFB，引用 NAVFAC tender；DCD 作为 B 级线索，必须回到 SAM.gov/NAVFAC 原 tender 验证。
- Camp Blaz / Finegayan / former Naval Base Guam Telecommunications Site 需要用 NAVFAC PA memo、SAM.gov 和 Defense.gov 分辨是普通营建、telecommunications、还是可计 data center。

模板：

```text
site:datacenterdynamics.com Guam "data center" OR "Andersen"
site:sam.gov "Guam" "communications center" OR "data center" OR "teleport"
site:defense.gov/News/Contracts "Guam" "communications center" OR "fiber communications"
site:navfac.navy.mil Guam "communications center" OR "data center"
"Camp Blaz" Guam "communications" OR "telecommunications" OR "data center"
"Andersen Air Force Base" "data center" OR "36th Communications Squadron"
"NCTS Guam" OR "Naval Computer and Telecommunications Station" "Guam" "network"
```

## 4. 媒体与目录（Media / Directories）

媒体：

- Data Center Dynamics: https://www.datacenterdynamics.com/
- Submarine Networks: https://www.submarinenetworks.com/
- Pacific Island Times: https://www.pacificislandtimes.com/
- Pacific Daily News: https://www.guampdn.com/
- Guam Daily Post: https://www.postguam.com/
- Marianas Business Journal: https://www.mbjguam.com/
- Guam Business Magazine: https://www.guambusinessmagazine.com/
- PNC: https://www.pncguam.com/
- KUAM: https://www.kuam.com/

目录：

- DataCenterMap Guam: https://www.datacentermap.com/guam/
- Baxtel Guam: https://baxtel.com/data-center/guam
- Datacenters.com Guam: https://www.datacenters.com/locations/guam
- Inflect Guam: https://inflect.com/datacenters/apac/guam/guam
- Cloudscene: https://cloudscene.com/
- WHTop GU: https://www.whtop.com/directory/country/gu
- PeeringDB: https://www.peeringdb.com/

用法：

- 媒体用于时间线、项目名、承包商和容量线索；必须回填一手来源。
- 目录常把市场统一标为 Hagatna/Guam，地址和 village 可能错误；不要直接采用目录地名。
- PeeringDB 用于网络/ASN/IX 上下文，不作为设施存在证据。

模板：

```text
site:datacenterdynamics.com Guam "data center"
site:pacificislandtimes.com "Guam Exchange" OR "data center" OR "submarine cable"
site:guampdn.com "data center" OR "colocation" OR "GPA" OR "teleport"
site:postguam.com "data center" OR "colocation" OR "GPA" OR "teleport"
site:mbjguam.com "data center" OR "ICT" OR "submarine cable"
site:guambusinessmagazine.com "data center" OR "ICT" OR "submarine cable"
site:datacentermap.com/guam Guam "data center"
site:baxtel.com/data-center/guam Guam
site:inflect.com/datacenters/apac/guam Guam
```

## 5. 查询模板（Island + Villages）

全岛：

```text
"Guam" "data center" OR "datacenter" OR "colocation" OR "server hosting" -Guamá -ship -registry
"Guam" "cable landing station" OR "neutral cable landing" OR "international gateway"
"Guam" "teleport" OR "satellite earth station" OR "communications center"
"Guam" "AWS" OR "Azure" OR "Google Cloud" OR "Oracle" "region" OR "edge"
```

19 villages：

```text
Agana Heights
Agat / Hågat
Asan-Maina
Barrigada
Chalan Pago-Ordot
Dededo
Hagåtña / Hagatna / Agana
Inalåhan / Inarajan
Malesso' / Merizo
Mangilao
Mongmong-Toto-Maite
Piti
Sånta Rita-Sumai / Santa Rita
Sinajana
Talo'fo'fo / Talofofo
Tamuning / Tamuning-Tumon-Harmon / Tumon / Harmon
Humåtak / Umatac
Yigo
Yona
```

Village query pattern:

```text
"{village}" "Guam" "data center" OR "datacenter" OR "colocation" OR "server room"
"{village}" "Guam" "landing station" OR "central office" OR "exchange" OR "gateway"
"{village}" "Guam" "communications center" OR "teleport" OR "fiber"
"{village}" "Guam" "GPA" "substation" OR "large load"
```

Expected yield:

| Village | Focus | Expected yield |
|---|---|---|
| Piti | GNC/GTA, Tata Piti, SEA-US/JGA, power | High |
| Tamuning / Harmon / Tumon | Guam Exchange, carrier offices, Tanguisson/Tumon Bay context | High |
| Hagåtña / Agana | Government ICT, DOCOMO location label | Medium |
| Yigo | Andersen AFB | Medium-High |
| Dededo / Finegayan | Camp Blaz, telecommunications site | Medium-High |
| Santa Rita / Agat | Naval Base Guam, cable landing context | Medium |
| Barrigada / Mangilao | Carrier/government/education ICT | Medium |
| Remaining villages | Negative coverage | Low |

## 6. 枚举矩阵（Enumeration Matrix）

| Facility class | Lead sources | Evidence needed | Default grade | Counting rule |
|---|---|---|---|---|
| Commercial colo | GTA, Guam Exchange, DOCOMO, IT&E official pages | Facility/operator + colo/DC language + location/status | A if official | Count if physical site or explicitly named facility/location exists |
| Combined CLS + DC | GTA/GNC, FCC, Submarine Networks, PR | Landing station + data center/colo/rack/power language | A/B depending source | Count as DC candidate; also tag telecom |
| Landing station only | FCC, TeleGeography, Submarine Networks, cable owners | System + landing point + landing party | A/B | Telecom only unless colo/DC is explicit |
| Defense DC/comms | SAM.gov, NAVFAC, Defense.gov, DCD | Award/tender + project scope + base/location | A if official, B if media | Separate defense/telecom class |
| Government DC | GovGuam, DOA/GSA, notices, BSP | Named location + project phase + operator/agency | A | Generic ICT/cloud language not counted |
| Cloud region | AWS/Azure/GCP/OCI official pages | Guam listed as region/local zone | A | Current official negative evidence: no Guam region |
| CDN/edge | Cloudflare/Akamai official network pages | Guam listed as edge deployment | A/B | Edge only; not DC unless facility evidence exists |
| Directory-only data center | DataCenterMap/Baxtel/Inflect/etc. | Directory entry | C | Lead only; verify elsewhere |

## 7. 去重与验证规则（Dedup / Verification）

1. Normalize village names: `Hagatna/Agana/Hagåtña`, `Agat/Hågat`, `Inarajan/Inalåhan`, `Merizo/Malesso'`, `Umatac/Humåtak`, `Santa Rita/Sånta Rita-Sumai`, `Talofofo/Talo'fo'fo`.
2. Treat `Harmon`, `Tumon`, `Upper Tumon`, `Alupang` as subareas; map to the correct village after address confirmation.
3. Do not merge GTA GU1/GU2/GU3/GNC/Guam Exchange unless a source proves they are the same physical site.
4. Keep cable system, landing station, and data center records linked but distinct.
5. Capacity fields preserve original units and source grade: sq ft, racks, MW, kW, MVA are not interchangeable.
6. If a source says “ready for equipment” or “planned,” status is not operational unless a later official page confirms operations.

## 8. 观察清单（Watch List）

```text
site:gta.net "GU3" OR "ready for equipment" OR "Alupang Data Center"
site:guamexchange.com "Harmon 1" OR "data center" OR "colocation"
site:business.docomopacific.com "Agana" "Harmon" "Piti" "colocation"
site:shop.ite.net/business/data-services "co-location" OR "hosting"
site:fcc.gov Guam "Bulikula" OR "Proa" OR "Taihei" OR "Halaihai"
site:docs.fcc.gov Guam "Bulikula" OR "Proa" OR "Taihei" OR "Halaihai"
site:sam.gov "Guam" "data center" OR "communications center"
site:defense.gov/News/Contracts "Guam" "data center" OR "communications center"
"Guam" "data center" "opened" OR "commissioned" OR "ribbon cutting" OR "Tier III"
```
