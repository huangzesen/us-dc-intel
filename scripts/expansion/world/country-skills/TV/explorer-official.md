# TV Explorer Official — 图瓦卢官方渠道数据中心枚举方法（政府 / 电信 / 电力 / 登陆站 / 采购）
# TV Explorer Official — Tuvalu Datacenter Enumeration via Government, Telecom, Power, Landing Station, and Procurement Sources

状态：final reviewed。Date: 2026-08-12. Scope: Tuvalu (TV). Manifest divisions (`subnational_type: town council/island council`): **Funafuti**, **Niutao**, **Nukufetau**, **Nukulaelae**, **Nanumea**, **Nanumaga**, **Nui**, **Vaitupu**。Niulakita 是有人岛但未单列于 manifest；本方法将其并入外岛负预期组，不新增 division。

可靠性分级 / Reliability grades:

- **A**：官方/一手来源，包括 Tuvalu 政府和部委域名、Tuvalu Telecom/TTC、Tuvalu Electricity Corporation/TEC、Tuvalu legislation、World Bank/ADB/AIFFP/JICA/ITU/UNCTAD 等项目文件、官方云区域页、PeeringDB/PCH 互联事实。
- **B**：成熟行业或区域媒体，且明确点名运营者、地点、状态动词的报道，例如 Submarine Networks、Pacific Island Times、RNZ Pacific、Islands Business、CommsUpdate。
- **C**：目录、市场报告、社交帖、推广页、聚合招标页；只作线索或反查入口。
- **U**：打不开、无法复核、或只有传言的内容。

规则：等级只覆盖来源实际支持的字段。海缆、Starlink 网关、电信机房、银行/政府机房都不是 colocation/data center，除非来源明确说明有托管、机柜、IT load、机房等级或客户服务。

---

## 0. 结构性事实 / Structural facts

- 图瓦卢是极小岛国，官方语言为 Tuvaluan 和 English。所有可用的一手 ICT/采购/能源材料基本用英文发布。
- 数据中心市场判断：截至本次复核，未确认图瓦卢境内有商业 colocation 数据中心、超大规模云区域或公共 IXP。可确认的数字基础设施集中在 **Funafuti/Fongafale/Vaiaku**：TTC 办公/核心设施、Vaka 海缆临时登陆/生产环境、Starlink community gateway、政府/银行/电力机房线索。
- **TTC / Tuvalu Telecom**：官网 `https://www.tuvalutelecom.tv/about-us` 可访问；页面列出地址 Vaiaku, Funafuti，并称 TTC 是 state-owned enterprise、由 Tuvalu Telecommunications Corporation Act 1993 建立、提供固定电话、移动与互联网服务。
- **法律来源**：`https://tuvalu-legislation.tv/cms/images/LEGISLATION/PRINCIPAL/1993/1993-0004/1993-0004_2.pdf` 可访问，用于核对 TTC Act；WIPO Lex 页面 `https://www.wipo.int/wipolex/en/legislation/details/7674` 也可作备用入口。
- **主管部门**：JICA 2026 报告点名 **Ministry of Transport, Energy, Communication and Innovation, Department of Information and Communications Technology**，并列出 `https://ict.gov.tv/` 和 `https://ict.gov.tv/policies/`；这两个 ICT 子域 URL 本轮访问超时，作为 JICA-cited official lead 使用，不标成已验证活链。通信许可/监管职责在转移到该部门后仍处制度建设阶段，是否成立独立监管机构须逐轮复核。
- **Vaka 海缆**：不要继续用旧的 “Fiji–Tuvalu cable landed 2023” 作为当前锚点。经核验，当前官方/行业锚点为 **Tuvalu Vaka Cable**，连接 Funafuti 至 Google Bulikula cable system。AIFFP 页面 `https://www.aiffp.gov.au/investments/investment-list/tuvalu-vaka-cable` 可访问，状态为 Signed and Announced，地点 Funafuti，项目值约 USD 56m/AUD 80m，交付伙伴包括 Government of Tuvalu、TTC、Google、日本、新西兰、台湾、美国。Submarine Networks 报道 2024-12-12 称该电缆已在 Tuvalu landing；Pacific Island Times 报道 2025-10-24/27 的 Funafuti launch。JICA 报告称它 2024-12 landed、计划 2025-10 start operations，初始 10 Gbps，临时接入 TTC 设施，完整服务待正式 landing station 建成。
- **TTC Funafuti 设施 / micro data center**：JICA 2026 报告是关键 A 级方法来源。它描述 TTC 在 Funafuti 有一栋含 server room 的单层建筑，Vaka cable 先从该处临时运行；计划在旁边建设 micro data center，设备截至 2025-09 在运输途中，抵达后用于 landing station production environment；同一场地安装 Starlink ground station gateway。记录时资产类别应拆开：`telco-server-room`、`provisional-cable-landing`、`planned/moving micro-dc for landing-station production`、`satellite-gateway`。
- **电力**：TEC 官网 `https://www.tectuvalu.tv/` 可访问；页面称 TEC 是 state-owned enterprise、由 TEC Act 1990 建立，所有岛屿 24/7 power supply，外岛为 hybrid solar PV + standby diesel，Funafuti 为 grid-tied solar PV + diesel base load。TEC 的 ADB article `https://www.tectuvalu.tv/adb-article/` 可访问，称项目将在 Funafuti、Nui、Nukufetau、Nukulaelae 安装 724 kW solar，其中 Funafuti 500 kW，并在 Funafuti 配套 containerized BESS。能源项目不是数据中心证据，只用于可行性和供电约束。
- **政府门户可用性**：`https://www.gov.tv/` 和 `https://gov.tv/` 在本轮 DNS 解析失败；不要把它们列为已验证活链。优先使用可访问的政府子域（例如本轮验证的 `https://finance.gov.tv/`），并通过搜索发现当前部委/采购页面；`ict.gov.tv` 本轮超时但由 JICA 脚注引用。

反例陷阱 / False positives:

- Tuvalu “Digital Nation / metaverse” 是文化、身份、档案和数字政府韧性倡议，不是境内数据中心证据。
- 海缆登陆站、Starlink/community gateway、基站、交换机房、银行/政府 server room 分资产类别记录，不合并为 commercial DC。
- 境外托管、云服务可用、国家客户支持、域名/内容分发支持不等于 TV 境内设施。
- Funafuti 是地质/珊瑚礁文献高噪声地名，检索必须加 ICT/DC 限定。

---

## 1. 官方来源清单 / Official source checklist

| 来源 | URL / access note | 用途 | 等级 |
|---|---|---|---|
| ICT Department / MTECI | `https://ict.gov.tv/`, `https://ict.gov.tv/policies/`（JICA-cited; 本轮访问超时） | ICT 政策、Broadband Plan、Digital Government Plan、NETP、监管制度线索 | A for JICA-cited facts; U until URL opens for page content |
| Ministry of Finance and Economic Development | `https://finance.gov.tv/` | 采购/预算/捐资方项目执行入口 | A |
| Tuvalu Telecom / TTC | `https://www.tuvalutelecom.tv/about-us` | 运营者身份、地址、服务范围；新闻/ESMP/业务页作设施线索 | A |
| Tuvalu legislation | `https://tuvalu-legislation.tv/cms/images/LEGISLATION/PRINCIPAL/1993/1993-0004/1993-0004_2.pdf` | TTC Act、权限、监管变更核验 | A |
| TEC | `https://www.tectuvalu.tv/`, `https://www.tectuvalu.tv/adb-article/` | 电力背景、Funafuti/外岛供电约束、solar/BESS 项目 | A |
| JICA survey | `https://openjicareport.jica.go.jp/pdf/1000057177.pdf` | 2025 field survey；TTC Funafuti server room、temporary landing station、micro DC、Starlink gateway、remote-island connectivity | A |
| AIFFP | `https://www.aiffp.gov.au/investments/investment-list/tuvalu-vaka-cable` | Vaka cable official finance/location/partners | A |
| World Bank P159395 PAD | `https://documents1.worldbank.org/curated/en/771141548558042678/txt/Tuvalu-project-appraisal-document-pad-P159395Dec18-12182018-636841368206528813.txt` | older Tuvalu Telecommunications and ICT Development Project, cable/PPP/CLS context; historical RFS assumptions only | A |
| Official cloud region pages | AWS/Azure/GCP/OCI official location pages | negative check: no TV region/local zone/region equivalent | A |

Source handling:

- `gov.tv` apex was not resolvable in this review. Use subdomain discovery and cached/linked pages; mark apex access failure in notes.
- Facebook posts from government/ministry/TTC are useful for dates and photos, but keep them B/C unless the account identity is verified and the same fact appears in A-grade material.
- World Bank P159395 is historically important but older than Vaka; never use its assumed late-2020 RFS date as current status.

---

## 2. 证据标准 / Evidence standards

最低阳性证据:

1. **commercial colocation / hosting DC**：运营者或客户-facing 页面明确提供 colocation/hosting/racks/floor space，或官方许可/采购点名数据中心服务。当前 TV：未确认。
2. **government DC / sovereign micro DC**：政府、TTC、JICA、World Bank/ADB、招标或交付文件点名数据中心或 micro data center，并保留状态动词。当前 TV：JICA 仅支持 TTC adjacent micro DC as in transit/planned for landing-station production as of 2025-09，不支持“已运营商业 DC”。
3. **cable landing station**：官方/运营者/捐资方文件点名 landing station、landing、CLS、SLTE 或生产环境。当前 TV：Vaka/Funafuti 是强阳性互联证据，不是 DC。
4. **telco/server room**：TTC/JICA 点名 server room、core network、routers/switches/firewalls。作为 `telco-server-room` 或 `network-core`。
5. **satellite gateway**：JICA/TTC/Starlink/Kacific 点名 community gateway/ground station。作为 `satellite-gateway`。
6. **energy support**：TEC/ADB/JICA 点名供电、BESS、generator、solar。作为 power caveat，不单独创建 DC。

状态词映射:

- `operational`: TTC services, 4G/FTTP/core network where source says operating/in operation.
- `landed`: Vaka cable landing in December 2024, B/A depending on source.
- `launched`: Vaka service launch ceremony on October 24, 2025, B/A depending on source.
- `temporary/provisional`: Vaka provisionally connected to TTC facility as of September 2025, per JICA.
- `in transit/planned`: micro DC adjacent to TTC/landing station as of September 2025, per JICA.
- `not confirmed`: commercial colocation, public IXP, hyperscaler region.

---

## 3. 采购、规划与政策检索 / Procurement, planning, and policy queries

优先查询:

```text
site:ict.gov.tv Tuvalu ("data center" OR "data centre" OR "micro data center" OR "landing station" OR "cloud")
site:ict.gov.tv Tuvalu ("National ICT Policy" OR "Broadband Plan" OR "Digital Government Plan" OR "NETP")
site:finance.gov.tv Tuvalu ("tender" OR "procurement" OR "ICT" OR "telecommunications" OR "server" OR "cloud")
site:tuvalutelecom.tv ("data center" OR "data centre" OR "server room" OR "landing station" OR "Vaka" OR "Starlink")
site:tectuvalu.tv ("data center" OR "ICT" OR "BESS" OR "generator" OR "Funafuti")
"Tuvalu Vaka Cable" ("landing station" OR "Funafuti" OR "production environment" OR "ready for service" OR "launched")
"Tuvalu" ("micro data center" OR "micro data centre" OR "containerized data center" OR "government cloud")
"Tuvalu" ("internet exchange" OR IXP OR PeeringDB OR PCH)
```

采购字段必须保留:

- `notice_url`
- `procuring_entity`
- `project_id`
- `contract/reference_number`
- `status_verb`
- `status_date`
- `delivery_site`
- `asset_class`
- `evidence_grade_by_field`

---

## 4. 电力与场址可行性 / Power and site feasibility

图瓦卢电力信息只用于限制/解释 DC 可行性，不自动生成设施:

- Funafuti：TEC grid with diesel base load and grid-tied solar PV；ADB/TEC 页面提到 500 kW Funafuti solar 和 containerized BESS。小型 telecom/micro-DC 需核查 backup generator/solar/BESS；MW 级 DC 基本为负预期，除非 TEC/项目文件给出并网和备用电力方案。
- Nui、Nukufetau、Nukulaelae：ADB/TEC 页面点名 solar 增量项目；这证明能源项目，不证明 ICT 设施。
- Niutao、Nanumea、Nanumaga、Vaitupu、Niulakita：以 JICA/TEC/项目文件核对 Starlink/4G/solar 微网，不作 DC 阳性。

电力查询:

```text
site:tectuvalu.tv Funafuti ("solar" OR "BESS" OR "generator" OR "diesel" OR "power station")
"Tuvalu Electricity Corporation" ("Funafuti" OR "Nui" OR "Nukufetau" OR "Nukulaelae") ("solar" OR "BESS" OR "diesel")
"Vaka Cable" Tuvalu ("generator" OR "solar" OR "backup power" OR "landing station")
"TTC" Tuvalu ("generator" OR "BESS" OR "power" OR "server room")
```

---

## 5. 分区覆盖 / Division coverage

### Funafuti — P0

预期记录：TTC server room/network core、Vaka provisional landing/landing station、planned/in-transit micro DC for landing station production、Starlink community gateway、government/NBT server-room leads、TEC power background。

```text
"Funafuti" OR "Fongafale" OR "Vaiaku" ("data center" OR "data centre" OR "micro data center" OR "server room" OR "landing station")
"TTC" OR "Tuvalu Telecom" ("Funafuti" OR "Vaiaku") ("server room" OR "core network" OR "Vaka" OR "Starlink gateway")
"Tuvalu Vaka Cable" ("Funafuti" OR "landing" OR "launched" OR "production environment")
"National Bank of Tuvalu" ("Funafuti" OR "server" OR "ICT" OR "payment")
```

### Vaitupu — P2

预期：无数据中心。JICA 点名 Vaitupu/Asau 有 4G + Starlink；只记录通信接入或学校/诊所机房线索。

```text
"Vaitupu" OR "Asau" Tuvalu ("4G" OR "Starlink" OR "server" OR "ICT" OR "telecom" OR "solar")
"Motufoua" Tuvalu ("ICT" OR "computer" OR "server" OR "internet" OR "solar")
```

### Niutao / Nanumea — P3

预期：无数据中心。JICA 点名 Niutao 与 Nanumea/Haumaefa 有 4G + Starlink。

```text
"Niutao" Tuvalu ("4G" OR "Starlink" OR "server" OR "ICT" OR "telecom" OR "solar")
"Nanumea" OR "Haumaefa" Tuvalu ("4G" OR "Starlink" OR "server" OR "ICT" OR "telecom" OR "solar")
```

### Nukulaelae / Nukufetau / Nui / Nanumaga — P3

预期：无数据中心。JICA 点名这些岛使用 Starlink + WiFi backhaul；只记录接入线索。

```text
"Nukulaelae" OR "Nukufetau" OR "Nui" OR "Fenua Tapu" OR "Nanumaga" OR "Nanumanga" OR "Tonga" Tuvalu ("Starlink" OR "WiFi" OR "server" OR "ICT" OR "telecom" OR "solar")
"Tuvalu" "outer islands" ("Starlink" OR "4G" OR "WiFi" OR "telecom" OR "solar")
```

### Niulakita — not manifest division

JICA 点名 Niulakita 有 Starlink + WiFi。因 manifest 未列 Niulakita，不作为独立 division；若数据库需保存，归入外岛负预期备注或按上游 schema 的 parent division 规则处理。

---

## 6. 标准化输出 / Output normalization

字段:

- `name`, `aliases`, `operator`, `ultimate_parent`
- `asset_class`: `commercial-colocation`, `government-dc`, `micro-dc`, `cable-landing`, `telco-server-room`, `network-core`, `satellite-gateway`, `power-background`, `negative-check`
- `division`, `islet/town/site`, `address_or_landmark`, `coordinates`
- `status`, `status_date`, `source_status_verb`
- `capacity_it_mw`, `capacity_electrical_mw`, `racks`, `floor_area`
- `power_sources`, `backup_power`, `grid_connection`, `power_caveat`
- `connectivity`
- `evidence_grade_by_field`, `source_urls`

当前已知项目 / Known records:

| 名称 | Division | Asset class | 状态 | Grade |
|---|---|---|---|---|
| Tuvalu Vaka Cable / Funafuti landing | Funafuti | cable-landing | landed 2024-12; launched 2025-10-24; full formal CLS status to recheck | A/B |
| TTC Funafuti server room / provisional Vaka production environment | Funafuti | telco-server-room / provisional-cable-landing | operating/provisional as of JICA fieldwork 2025-09 | A |
| TTC adjacent micro data center for landing-station production | Funafuti | micro-dc | in transit/planned as of 2025-09; confirm arrival/commissioning | A for plan/status in JICA; not operational until new source |
| Starlink community gateway / ground station at TTC premises | Funafuti | satellite-gateway | installed/operated by TTC per JICA | A |
| Remote-island Starlink/4G access | Vaitupu, Niutao, Nanumea, Nukulaelae, Nukufetau, Nui, Nanumaga; Niulakita outside manifest | telecom-access | access/backhaul only; no DC | A |
| TEC Funafuti solar/BESS/diesel and outer-island hybrid systems | Funafuti, Nui, Nukufetau, Nukulaelae, other islands | power-background | operating/projects; no DC | A |
| Commercial colocation | n/a | commercial-colocation | not confirmed | n/a |
| Public IXP | n/a | IXP | not confirmed | n/a |
| AWS/Azure/GCP/OCI TV region | n/a | hyperscaler-region | not present on official region pages | A negative |

复检节奏：每月查 TTC、ICT、Finance、AIFFP/World Bank/JICA；每季查 cloud region pages、PeeringDB/PCH、DCD/Submarine Networks/CommsUpdate、DataCenterMap/Cloudscene/Baxtel。任何 “commissioned”, “RFS”, “ready for service”, “awarded”, “installed”, “accepted” 字样都应触发重新分级。
