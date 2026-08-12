---
name: fj-datacenter-methodology
location: scripts/expansion/world/country-skills/FJ/SKILL.md
description: 斐济（Fiji）数据中心发现与审计方法论：官方/监管/云管线（政府/总理府、TAF 电信监管局、TFL/Vodafone Fiji/FINTEL 官方运营商页、ROC 公司注册、EFL 能源、官方云区域排除）叠加行业/厂商发现（运营商、海缆基础设施、贸易媒体、目录、地域模式）；以清单中的 5 个分区/属地（Central、Eastern、Northern、Rotuma、Western）为划分粒度，每个候选先分类再定级。运行 FJ 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。Bilingual discovery & audit methodology for Fiji datacenters: official/regulatory/cloud pipeline + industry/trade-press discovery, at the 5 division/dependency granularity from the manifest; classify every lead before recording; read before running FJ exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# FJ · 斐济数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> **目的**：斐济是较为活跃但规模仍小的太平洋岛国数据中心市场——预期为少量电信/运营商设施与海缆/ICT 项目，而非广泛的运营商中立或超大规模云区域市场。本方法论通过官方/监管/云管线（explorer-official.md）与行业/厂商发现（explorer-industry.md）双通道枚举，规定**每个候选先分类再记录**（commercial_colocation / operator_hosted_cloud / operator_internal_datacentre / hyperscaler_ict_facility / cable_landing_station / leo_ground_station_colocation / government_server_room / telecom_pop / office_only / seo_false_positive），并要求来源与主张精确匹配。运行任何 FJ 探索/审计批次前必须阅读本 skill，并按需路由到两份探索报告。

## 入口（Entry points）

| 文件 | 管线 | 内容 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | 政府/总理府/统计局、TAF 电信监管局、官方运营商（TFL、Vodafone Fiji、Digicel）、FINTEL/Google/海缆登陆、注册/投资/土地（ROC/businessNOW/Investment Fiji）、能源/水务（EFL/WAF）、官方云区域排除、5 分区覆盖矩阵、枚举工作流、设施/项目种子表 |
| explorer-industry.md | 行业/厂商发现 | 运营商/厂商扫描、Google Natadola 项目处理、海缆与电信基础设施线索、贸易媒体、目录到一手验证工作流、地域搜索配方与分区覆盖、容量提取指引、预期枚举结果 |

## 核心结构事实（框定每次搜索）

1. **划分模型**：清单为 **5 个分区/属地**：**Central、Eastern、Northern、Rotuma、Western**。地域注意：Suva/Vatuwaqa = Central；Savusavu/Labasa = Northern；Natadola/Nadi/Lautoka/Sigatoka/Denarau = Western；Rotuma 单独。Eastern 与 Rotuma 必须搜索并记录为已覆盖（负向扫描仅当记录搜索路径时有效）。
2. **核心设施/项目集**：**TFL 数据中心/托管服务**（官方 ICT Solutions 页证实云服务、灾备托管、数据中心、托管 PABX——A 级服务证据，物理站点/容量未披露，目录称 Suva 仅为 C 级线索）；**Vodafone Fiji Hosted Cloud / IaaS**（官方页证实基于斐济的托管云服务、连接 IPVPN——A 级服务证据，站点/容量未披露）；**FINTEL Vatuwaqa Communications Centre (VCC)**（Central；国际网关与海缆登陆站运营商，明确提供 LEO 地面站/卫星接入点托管（含电源/制冷/回程）——记录为 leo_ground_station_colocation 或 colo_adjacent_telecom，非通用商业托管）；**Google Natadola ICT 设施**（Western/Nadroga；新海缆登陆站 + 数据传输服务器/机架 + 发电设备；斐济政府 2024-11-30 发布为 A 级范围证据；状态保守为 under_construction / near_completion_unverified，**非** GCP 区域）；**TFL NextGen 数据中心**（拟议/EOI 阶段，站点/容量未公开；Fiji Times 称 2026 年起约 24 个月建设——B 级）。
3. **关键机构**：Fiji Government/PM Office（fiji.gov.fj、pmoffice.gov.fj）、TAF 电信监管局（taf.org.fj：执照/进口许可/设备型号核准/频谱——**非**数据中心登记册）、TFL（telecom.com.fj + TenderLink）、Vodafone Fiji、FINTEL（fintel.com.fj）、Google 官方博客（Tabua/Bulikula/Honomoana/Halaihai 海缆）、SSCC（Tui-Samoa：Suva 与 Savusavu 登陆点）、Southern Cross、ROC Public（roc.digital.gov.fj）、businessNOW、Investment Fiji、EFL（能源）、Stats Fiji（电力统计）。
4. **查询语言**：英语足以覆盖斐济官方来源发现；斐济语/印地语仅作本地来源地名规范化。
5. **容量语义**：仅从明确 IT 负荷、机架、楼层面积、等级认证或具名设施规格记录容量；**绝不**从海缆带宽、项目投资额（FJ$200M/US$250M 等——保持来源特定、币种特定、不取均值）或电网发电量换算 MW；TFL/Vodafone/FINTEL/Google Natadola/TFL NextGen 的容量字段一律 null 除非一手技术规格出现；Tier III/Tier 3 仅当 Uptime Institute、运营商认证、招标规格或一手技术文档支持。
6. **海缆基础设施 ≠ 数据中心**：Southern Cross/SC NEXT、Tonga Cable、ICN1（Suva–Port Vila）、Tui-Samoa、Gondwana 2、Google Tabua/Bulikula 为海缆资产/登陆站；仅当来源明确支持托管/主机/云/数据中心式设备安置才升级（FINTEL VCC 的 LEO/卫星托管即此类）。RFS 日期冲突按来源记录，不自行裁决。
7. **云区域排除（已核查 2026-08-12）**：AWS/Azure/GCP/OCI 官方区域页均无斐济；Natadola 是海缆/ICT 基础设施而非云区域；经销商、本地主机、海缆、CDN、营销主张不得构造斐济公共云区域。
8. **可靠度分级**：A = 一手政府/监管/国企/公用事业/公司注册/官方页/官方申报/官方招标/官方多边文件（fiji.gov.fj、PM Office、TAF、TFL、Vodafone、FINTEL、Google 博客、ROC、EFL、Stats Fiji）；B = 具名当事方/日期的可靠本地/区域/行业媒体（Fiji Times、FBC、Fiji Sun、fijivillage、Islands Business/PACNEWS、DCD、APNIC 视主张而定）；C = 目录、市场、社交转载、SEO 托管页、海缆地图/数据库、无署名聚合——C 可启动线索或支持负向控制，但不得确立设施。
9. **误报控制**：斐济 VPS/专用服务器/VPN/`.fj` 主机页多为离岸 SEO 库存（C 级误报）；不从 IP 地理定位、CDN 存在、DNS、VPN 端点、国家选择器或 `.fj` 域名注册建设施；Digicel 与政府/机构（USP/FNU）机房为线索级。

## 常用查询模板（详见 explorer-official.md / explorer-industry.md）

```text
site:fiji.gov.fj ("data centre" OR "data center" OR datacenter OR colocation)
site:fiji.gov.fj Google Natadola ("ICT facility" OR "cable landing station")
site:taf.org.fj ("data centre" OR hosting OR colocation OR licensee)
site:telecom.com.fj ("data centre" OR "data center" OR colocation OR "NextGen" OR tender)
site:vodafone.com.fj ("data centre" OR "hosted cloud" OR IaaS)
site:fintel.com.fj (Vatuwaqa OR "cable landing" OR colocation OR LEO OR Tabua)
site:efl.com.fj ("data centre" OR Google OR Natadola OR substation)
"{division}" Fiji ("data centre" OR "data center" OR datacenter)
"{division}" Fiji ("server room" OR hosting OR colocation OR "cable landing")
(Suva OR Vatuwaqa) Fiji FINTEL ("cable landing" OR "data centre" OR colocation)
(Natadola OR Sigatoka OR Nadroga) Fiji Google ("ICT facility" OR "landing station")
Rotuma Fiji (satellite OR internet OR telecom OR backhaul)
Google Natadola Fiji (commissioned OR operational OR RFS)   # 状态负向控制
site:datacenters.google (Fiji OR Natadola)   # 云排除
Fiji "data centre" (MW OR racks OR "Tier III" OR Uptime)   # 容量
"Staghorn Services" Fiji (ROC OR "Registrar of Companies" OR Natadola)
```

## 官方/监管管线要点（详见 explorer-official.md）

- 政府/总理府：2024-11-30 政府发布为 Google Natadola 范围/动工 A 级证据（新登陆站、数据传输服务器/机架、发电设备，Western 分区，Viti Levu 第二个登陆站，补充 Central 登陆）；PM Office 2023-10-27 南太平洋互联计划（美/斐/澳/法波海缆 + 物理多样化斐济登陆站）；Stats Fiji 电力/能源为国家级上下文非设施证据。
- TAF：执照/进口许可/设备型号核准/频谱与网络监管上下文；用 TAF 验证运营商身份与牌照类别，设施证据仍须来自运营商/注册处/公用事业/招标/政府。
- 运营商：TFL ICT Solutions（云/托管/数据中心/托管 PABX）、TFL–Google 2025-06-09 Vatuwaqa–Natadola 陆缆协议（A 级：两端锚点 FINTEL VCC 与 Google Natadola；光纤/海缆基础设施证据，非 Natadola 运营证明）、TFL NextGen EOI（TenderLink/官方社交；招标门户不再列出已关闭 EOI 时记为 closed/unavailable 而非 dead）、Vodafone IaaS 页（斐济托管云，站点/容量未披露）、Digicel 无已核实数据中心页。
- 注册/投资/土地：ROC Public（实体存在/注册/外国公司记录）、businessNOW、Investment Fiji；Staghorn Services/Natadola Bay Resort/FNPF/iTLTB 租赁链报道在 ROC/土地登记/iTLTB/项目文件确认前保持 B 级。
- 能源/水务：EFL 为电网/停电/电力上下文；本趟未核实 Google Natadola 电力/供水的 A 级 EFL/WAF 来源——电源与水为开放核验项。
- 云排除：仅用官方供应商页面判断云区域状态。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 先官方/运营商扫描再目录；目录声称的斐济设施需官方运营商页、设施地址、许可、注册记录、公用事业/互联记录或具名媒体才能建库；TFL 目录条目仅 C 级 Suva 线索。
- Google Natadola 处理：保留一手事实（政府范围、PM Office 倡议、Google 博客系统名与伙伴、TFL 陆缆路线）；DCD 2024-08-16 FJ$200M/约 US$89.4M 报道为 B 级公众报道、不得用于容量；Fiji Times 2025-11-17 NextGen 计划与 Google Natadola 不得混为一谈。
- 海缆/电信：用 FINTEL 作斐济登陆证据、海缆业主作 RFS/技术日期；Savusavu 支线为 Northern 海缆证据。
- 目录/误报：datacentermap/datacenterplanet/baxtel/cloudscene/whtop 仅目录线索与负向控制；检查"斐济"主机是否实为澳/新/新/美或通用 VPS 平台；SEO-only 托管页记为 seo_false_positive 并注明缺失证据。

## 维护注意（更新纪律）

- **更新节奏**：每次刷新重查官方云区域页（AWS/Azure/GCP/OCI）、fiji.gov.fj/PM Office 公告、TFL/Vodafone/FINTEL 官方页、TAF 执照、Google 博客；跟踪 TFL NextGen 站点选择与 Natadola 调试/启用证据。
- **来源核验**：fiji.gov.fj 证明 Natadola 范围/动工而非运营启用；TFL 证明服务存在而非容量；FINTEL VCC 的明确托管证据仅限 LEO 地面站/卫星接入点农场；海缆 RFS 日期冲突按来源与日期记录，不按偏好裁决。
- **不删除纪律**：无法核实的旧线索保留为降级线索并注明缺失证据；投资额（FJ$200M、US$250M 等）保持来源特定、币种特定，不取均值；Eastern 与 Rotuma 标记为已搜索而非跳过。
