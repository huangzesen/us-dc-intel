# TV Explorer Industry — 图瓦卢行业/媒体/厂商渠道数据中心发现方法
# TV Explorer Industry — Tuvalu Datacenter Discovery via Industry, Trade Press, Vendors, Cables, and Directories

状态：final reviewed。Date: 2026-08-12. Scope: Tuvalu (TV). Manifest divisions: **Funafuti**, **Niutao**, **Nukufetau**, **Nukulaelae**, **Nanumea**, **Nanumaga**, **Nui**, **Vaitupu**。Niulakita 未单列；只作外岛备注，不新增 division。

可靠性分级 / Reliability grades:

- **A**：一手/官方/运营者/公司文件/捐资方文件，例如 TTC、TEC、ICT Department、AIFFP、World Bank、JICA、官方云区域页、PeeringDB/PCH。
- **B**：可信行业媒体或区域媒体，且点名运营者、地点、状态，例如 Submarine Networks、Pacific Island Times、RNZ Pacific、Islands Business、CommsUpdate。
- **C**：目录、市场报告、社交帖、推广文、聚合页；只作线索。
- **U**：无法核验或无独立来源。

核心结论：图瓦卢是微型、几乎零商业数据中心市场。当前行业发现重点不是找 hyperscale/colo，而是避免把 **Vaka 海缆、TTC server room、Starlink gateway、remote-island backhaul、Digital Nation** 误记为商业数据中心。

---

## 0. 行业框架 / Industry frame

- **商业 colocation**：未确认任何图瓦卢境内商业 colocation 数据中心。DataCenterMap Tuvalu URL 本轮返回 429/challenge，不能当作空结果证据；Baxtel `https://www.baxtel.com/data-center/tuvalu` 会跳转到 `https://baxtel.com/data-center/tuvalu` 后返回 404，可记录为 C 级负向目录检查。
- **海缆**：当前锚点是 **Tuvalu Vaka Cable**，不是旧稿中的 “Fiji–Tuvalu 2023 cable”。AIFFP 可验证其连接 Funafuti 与 Bulikula system，项目值约 USD 56m/AUD 80m。Submarine Networks 2024-12-12 报道 Vaka cable lands in Tuvalu。Pacific Island Times 2025-10-27 报道 2025-10-24 Funafuti launch。
- **TTC 设施**：JICA 2026 报告是最重要的行业/一手交叉源，点名 Funafuti TTC single-story building with server room、provisional Vaka operation from October 2025、adjacent micro data center in transit as of September 2025、Starlink ground station gateway on the same premises。这是强设施线索，但资产类别必须精确。
- **电力约束**：TEC/ADB 证实 Funafuti 与部分外岛有 solar/BESS/diesel 组合；这支持小型 telecom/micro-DC 可行性讨论，不支持 MW-scale DC 推断。
- **IXP/cache**：JICA 报告提到 TTC 正与 Google/Akamai 等内容提供商谈 caching servers，最低 1 Gbps 需求是门槛。缓存服务器若未来落地，记录为 `cache-node` 或 `content-cache`，不是 colocation。
- **Starlink/Kacific**：JICA 点名 Funafuti Starlink community/ground station gateway，以及外岛 Starlink/4G/WiFi backhaul。卫星接入不是 DC。
- **Digital Nation**：Tuvalu 的 digital nation / metaverse / digital twin 报道只作为政策和反例背景；不作为数据中心证据。

---

## 1. 高信号行业来源 / High-signal industry sources

| 来源 | URL/检索面 | 用途 | Grade |
|---|---|---|---|
| Submarine Networks | `https://www.submarinenetworks.com/en/systems/trans-pacific/vaka/vaka-cable-lands-in-tuvalu` | Vaka landing, cable system, fiber pairs, partners; B 级行业交叉 | B |
| Pacific Island Times | `https://www.pacificislandtimes.com/post/tuvalu-launches-submarine-cable-government-offers-free-internet-service` | 2025-10-24 Funafuti launch ceremony, minister quote, project partners; B 级媒体状态 | B |
| AIFFP | `https://www.aiffp.gov.au/investments/investment-list/tuvalu-vaka-cable` | official investment, Funafuti location, partners, value | A |
| JICA survey | `https://openjicareport.jica.go.jp/pdf/1000057177.pdf` | TTC facility/server room, micro DC, Starlink gateway, remote-island connectivity, data center design constraints | A |
| TTC | `https://www.tuvalutelecom.tv/about-us` | operator identity, Vaiaku/Funafuti address, services; search internal pages for Vaka/Starlink/business | A |
| TEC | `https://www.tectuvalu.tv/`, `https://www.tectuvalu.tv/adb-article/` | power caveats, Funafuti/outer-island energy background | A |
| CommsUpdate / TeleGeography | `https://www.commsupdate.com/` search Tuvalu | mobile, broadband, market events | B |
| RNZ Pacific / Islands Business / ABC Pacific | search Tuvalu + cable/telecom/data | regional confirmation and dates | B/C |
| DataCenterMap | `https://www.datacentermap.com/tuvalu/` | directory negative check; current review hit 429 challenge | C |
| Baxtel | `https://baxtel.com/data-center/tuvalu` | directory negative check; current review returned 404 | C |
| Cloudscene | `https://cloudscene.com/` | manual directory search only | C |
| PeeringDB / PCH | `https://www.peeringdb.com/`, `https://www.pch.net/ixp/summary` | IX/facility facts if present; no TV IXP expected | A for listed facts |

行业查询包:

```text
site:submarinenetworks.com Tuvalu OR "Vaka Cable" OR "Bulikula" OR "Funafuti"
site:pacificislandtimes.com Tuvalu ("submarine cable" OR "Vaka" OR "internet" OR "Funafuti")
site:commsupdate.com Tuvalu ("4G" OR "broadband" OR "submarine cable" OR "TTC")
site:datacenterdynamics.com Tuvalu ("data center" OR "data centre" OR "cable" OR "cloud")
"Tuvalu" ("data center" OR "data centre" OR datacenter OR colocation OR "server room")
"Tuvalu Vaka Cable" ("ready for service" OR "RFS" OR "launched" OR "landing station")
"TTC" "Funafuti" ("server room" OR "micro data center" OR "Starlink gateway" OR "landing station")
"Tuvalu" ("Google" OR "Akamai") ("cache" OR "caching server" OR "edge")
```

---

## 2. 运营者与厂商种子 / Operator and vendor seeds

| 运营者/厂商 | 图瓦卢信号 | 处理 |
|---|---|---|
| TTC / Tuvalu Telecom | 唯一国家电信运营者；Vaiaku/Funafuti；fixed/mobile/internet；Vaka cable and domestic infrastructure per JICA | A for operator/service;设施细节按 JICA/TTC 原文拆分 |
| SubCom | Vaka cable supplier per Submarine Networks/JICA | cable vendor only, not DC operator |
| Google / Bulikula | Vaka is branch to Bulikula; possible future content cache talks | cable/content ecosystem; no Google cloud region or DC in TV |
| Starlink | Funafuti community/ground station gateway and outer-island backhaul per JICA; official map for availability | satellite-access/gateway only |
| Kacific | older satellite/backhaul search seed | B/C until current role is verified |
| TEC | power utility; Funafuti grid/BESS/diesel/solar | power-background only |
| National Bank of Tuvalu | digital payment/MTUPE linkage, card acceptance context per JICA | bank IT/server-room lead only; no colocation |
| IIJ | JICA reports IIJ approached around government micro DC and hosted Tuvalu officials for DC inspection; project secured by SubCom | vendor/proposal history only |
| Google/Akamai caching | JICA says TTC is negotiating for caching servers | watchlist; cache node if installed |

查询:

```text
"Tuvalu Telecom" OR "Tuvalu Telecommunications Corporation" ("Vaka" OR "Starlink" OR "server room" OR "micro data center")
"SubCom" "Tuvalu Vaka Cable"
"Google" "Tuvalu Vaka Cable" OR "Bulikula" "Tuvalu"
"Starlink" "Tuvalu" ("community gateway" OR "ground station" OR "Funafuti" OR "outer islands")
"Kacific" "Tuvalu" ("gateway" OR "TTC" OR "backhaul")
"National Bank of Tuvalu" ("MTUPE" OR "Mastercard" OR "VISA" OR "server")
"Akamai" OR "Google" "Tuvalu" ("cache" OR "caching")
```

---

## 3. 项目与状态观察清单 / Project and status watchlist

| 项目 | Division | Asset class | 当前状态 | 证据 |
|---|---|---|---|---|
| Tuvalu Vaka Cable / Funafuti landing | Funafuti | cable-landing | landed 2024-12; launch ceremony 2025-10-24; formal CLS/full service needs recheck | AIFFP A; JICA A; Submarine Networks/Pacific Island Times B |
| TTC Funafuti server room / provisional landing production | Funafuti | telco-server-room / provisional-cable-landing | JICA: single-story building with server room; provisional Vaka operation from there from 2025-10 | JICA A |
| Adjacent TTC micro data center | Funafuti | micro-dc / landing-station production | JICA: in transit as of 2025-09; confirm arrival/commissioning | JICA A for plan/status only |
| Starlink ground station/community gateway | Funafuti | satellite-gateway | installed at same premises and operated by TTC per JICA | JICA A |
| Outer-island connectivity | Vaitupu, Niutao, Nanumea, Nukulaelae, Nukufetau, Nui, Nanumaga; Niulakita outside manifest | telecom-access | 4G+Starlink on Vaitupu/Asau, Nanumea/Haumaefa, Niutao; Starlink+WiFi on Niulakita, Nukulaelae, Nukufetau, Nui/Fenua Tapu, Nanumaga/Tonga | JICA A |
| Google/Akamai cache | Funafuti expected | content-cache | negotiation/aspiration only | JICA A for talks; U for installed status |
| Commercial colocation | n/a | commercial-colocation | not found | directory/search negative only |
| Public IXP | n/a | IXP | not found | PeeringDB/PCH manual check |
| Hyperscaler cloud region | n/a | cloud-region | no AWS/Azure/GCP/OCI TV region on official locations | A negative |

状态查询:

```text
"Tuvalu Vaka Cable" ("launched" OR "ready for service" OR "RFS" OR "commercial service" OR "commissioned")
"Vaka Cable" Tuvalu ("landing station" OR "cable landing station" OR "CLS" OR "SLTE")
"TTC" "micro data center" Tuvalu
"Tuvalu" "caching server" ("Google" OR "Akamai" OR "content provider")
"Tuvalu" internet ("outage" OR "fault" OR "restored") ("Vaka" OR "cable" OR "Starlink")
```

---

## 4. Hyperscaler / cloud checks

官方页面只用于负向核验。当前无 TV region/local zone/public cloud region:

- AWS: `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/`
- Azure: `https://learn.microsoft.com/en-us/azure/reliability/regions-list`
- Google Cloud: `https://cloud.google.com/about/locations`
- Oracle OCI: `https://www.oracle.com/cloud/public-cloud-regions/`

不要把以下内容记为 TV 数据中心：SaaS 可用、客户国家支持、partner/reseller coverage、edge cache 谈判、Fiji/Australia/New Zealand hosting for Tuvalu customers。

查询:

```text
"AWS" OR "Amazon Web Services" "Tuvalu" ("region" OR "availability zone" OR "local zone")
"Microsoft Azure" "Tuvalu" ("region" OR "data center")
"Google Cloud" "Tuvalu" ("region" OR "data center")
"Oracle Cloud" "Tuvalu" ("region" OR "data center")
"Tuvalu" ("sovereign cloud" OR "data residency" OR "government cloud")
```

---

## 5. 分区矩阵 / Division matrix

| Division | Priority | Expected assets | Method |
|---|---:|---|---|
| Funafuti | P0 | Vaka landing/provisional production, TTC server room/core, planned/in-transit micro DC, Starlink gateway, possible cache, TEC power background | Run all operator/cable/DC/cache/power queries with Funafuti/Fongafale/Vaiaku |
| Vaitupu | P2 | 4G+Starlink access, school/clinic/server-room leads, solar/microgrid | Record access only; no DC unless source names facility |
| Niutao | P3 | 4G+Starlink access | negative DC check |
| Nanumea | P3 | 4G+Starlink at Haumaefa per JICA | negative DC check |
| Nukulaelae | P3 | Starlink+WiFi backhaul; TEC/ADB solar background | negative DC check |
| Nukufetau | P3 | Starlink+WiFi backhaul; TEC/ADB solar background | negative DC check |
| Nui | P3 | Starlink+WiFi at Fenua Tapu; TEC/ADB solar background | negative DC check |
| Nanumaga | P3 | Starlink+WiFi at Tonga village per JICA spelling `Nanumanga` in report | negative DC check |

Division queries:

```text
"Funafuti" OR "Fongafale" OR "Vaiaku" ("server room" OR "micro data center" OR "landing station" OR "Starlink gateway" OR "cache")
"Vaitupu" OR "Asau" Tuvalu ("4G" OR "Starlink" OR "server" OR "ICT" OR "solar")
"Niutao" Tuvalu ("4G" OR "Starlink" OR "server" OR "ICT" OR "solar")
"Nanumea" OR "Haumaefa" Tuvalu ("4G" OR "Starlink" OR "server" OR "ICT" OR "solar")
"Nukulaelae" OR "Nukufetau" OR "Nui" OR "Fenua Tapu" OR "Nanumaga" OR "Nanumanga" Tuvalu ("Starlink" OR "WiFi" OR "server" OR "ICT" OR "solar")
```

---

## 6. 输出规范 / Output rules

每条候选必须保存:

- `source_status_verb`: landed, launched, in operation, provisional, in transit, planned, negotiating, not confirmed
- `asset_class`: cable-landing, telco-server-room, micro-dc, satellite-gateway, telecom-access, content-cache, power-background, commercial-colocation, IXP, negative-check
- `division`: only one of manifest divisions; Niulakita stays in notes
- `grade_by_field`: source may be A for cable and C/U for data center interpretation
- `not_dc_reason`: required for cable, satellite, cache, telecom access, power, Digital Nation

Do not create records from directory presence alone. For TV, absence of a directory page is weak evidence; positive facility evidence must come from operator/official/JICA/procurement or a named industry report with a verifiable site.

---

## 7. 复检节奏 / Re-check cadence

- **Monthly**：TTC/Vaka news, ICT Department policies and tenders, Finance procurement, AIFFP/World Bank/JICA updates.
- **Quarterly**：Submarine Networks, CommsUpdate, DCD, RNZ Pacific, Islands Business, Pacific Island Times, PeeringDB, PCH, DataCenterMap, Cloudscene, Baxtel, official cloud region pages.
- **Event-driven**：any Vaka RFS/CLS/commissioning notice, micro DC arrival or acceptance, Starlink license change, Google/Akamai cache installation, power outage affecting TTC/landing station, or government cloud/data center tender.
