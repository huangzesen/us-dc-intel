---
name: as-datacenter-methodology
location: scripts/expansion/world/country-skills/AS/SKILL.md
description: 美属萨摩亚数据中心发现与审计方法论（bilingual）。American Samoa datacenter discovery & audit methodology: enumerate the official/regulatory/cloud pipeline (FCC cable/licensing records incl. Le Vasa DA-26-578A1, ASTCA state telecom operator & RFPs, ASG portal + procurement.as.gov, NTIA/BEAD, USAC/SAM.gov/USAspending/DOI OIA, ASPA power, cloud-region absence checks) plus industry/trade-press discovery (Samoa News, Talanei/KHJ, Samoa Observer, RNZ Pacific, DCD, cable vendors DXN/SubCom/AP Telecom/Google, directories). Division model: country with 1 division (American Samoa). Read before running AS exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# AS · 美属萨摩亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：美属萨摩亚为美国小型海外领地，无公开数据中心注册库、无已核实的商用托管市场与超大规模云区域（截至 2026-08-12 的工作负基线）；最强官方设施类别为电信海缆登陆/核心网络设施（ASTCA 在 Tafuna/Pago Pago 一带资产），海缆/核心站点非商用 DC，除非主源明确确认托管/机架/云服务。2026 年新增 **Le Vasa** 与 **SAS-2** 海缆工作强化电信设施观察清单，但本身不构成 DC 容量证据。本方法论通过**官方/监管/云管线（explorer-official.md）**与**行业/厂商/媒体发现（explorer-industry.md）**双轨三角验证，以 FCC/ASTCA/ASG/联邦资金记录为主证，目录仅作发现；本 skill 汇总两份最终审定报告，作为 AS 探索/审计批次的入口。

## 入口

| 文件 | 管线 | 内容 |
| --- | --- | --- |
| explorer-official.md | 官方/监管/云管线 | FCC（海缆许可/公告，Le Vasa DA-26-578A1）、ASTCA（州营电信运营商/RFP）、ASG 门户与 procurement.as.gov、NTIA/BEAD（$37.56m）、USAC/SAM.gov/USAspending/DOI OIA、ASPA 电力（aspower.com）、四大云区域缺失检查 |
| explorer-industry.md | 行业/厂商发现 | 本地媒体（Samoa News、Talanei/KHJ）、区域媒体（Samoa Observer、RNZ Pacific、Islands Business）、行业媒体（DCD、Telecompaper/SubTel/SubseaCables）、海缆厂商（DXN、SubCom、AP Telecom、Google/Starfish/Bulikula）、企业机房候选（LBJ、ASCC、港口/机场、银行、罐头厂）、目录（DataCenterMap、Cloudscene、PeeringDB） |

## 核心结构事实

1. **行政区划模型**：manifest 为 **country**，恰好 **1 个 division：American Samoa**（subnational_type="country"，divisions=["American Samoa"]）；所有确认记录必须 division: American Samoa。地理子行（Tutuila：Pago Pago/Fagatogo/Utulei/Tafuna/Nu'uuli/Iliili/Leone/Vaitogi 等；Manu'a：Ta'u/Ofu/Olosega/Fitiuta；Swains Island、Rose Atoll）仅为检索辅助，不是额外 division；Manu'a 与 Swains/Rose 默认 `connectivity_only`/`no_projects`。
2. **注册库现状**：无公开全国数据中心注册库；无已核实的中立商用托管（commercial colo）或超大规模云区域——作为工作负基线而非永久事实；最强官方设施类是电信海缆登陆/核心网络设施（`telecom_cable_station`/`telecom_core`），除非主源明确确认托管/机架/云服务。
3. **法律与监管**：美国领地，电信与海缆许可高度经由 **FCC** 可见；**ASTCA** 为本地州营电信运营商（EO 002-1998 由原 Office of Communications 设立；osas.as 为制度证据）；FCC **DA-26-578A1（2026）**为 A 级证据：ASTCA 将建设 **Tafuna 海缆登陆站与海滩接头井**并拥有运营 Le Vasa；ASG 2026 公告明确 ASTCA 为区域数字基础设施牵头机构（Le Vasa、SAS-2）。
4. **互联与云（负向）**：海缆系统 ASH/SAS、Hawaiki、Manatua、Le Vasa、SAS-2 均为连通性/登陆设施而非 DC；2026-08-12 检查官方 AWS/Azure/GCP/OCI 区域页无 "American Samoa" 条目（A 级缺失证据，不排除私有边缘设备）；Starlink/VSAT/卫星为连通性非 DC 容量；大型负荷（>0.5 MW）声明须 **ASPA** 连接/发电/变电站/资费/公告证据支撑。
5. **设施/项目种子（2026-08 证据状态）**：**Le Vasa**（FCC 公告 + ASG 谷歌项目新闻：规划/在建 Tafuna CLS——非商用 DC）；**SAS-2**（ASG 2026 规划/预算时间表，ASTCA/MCIT——规划中，无站点）；**DXN CLS 合同**（2026-07 行业媒体，B 级：ASTCA 模块化 CLS 合同约 AUD 1m——厂商确认 CLS 而非商用 DC）；**ASTCA 网络/核心/业务**（A 运营商页面：光纤宽带/5G/业务/Hawaiki 电路；无公开托管/colo 产品页）；企业机房候选：LBJ 医疗中心、ASCC、港口/机场、银行（Bank of Hawaii）、罐头厂（StarKist、Chicken of the Sea、Samoa Tuna Processors）——仅 `enterprise_server_room`/`government_dc` 物理站点证据。
6. **语言与词汇**：英文优先；萨摩亚语变体用于双语页面与本地媒体召回：American Samoa、Amerika Samoa、Sāmoa Amelika；设施词：data center/centre、datacenter、colo（colocation/co-location）、hosting、server room、NOC、IXP、cable station、landing station、CLS、core network；状态词：proposed、procurement、under_construction、operational。
7. **可靠性分级**：A = 官方/主源（政府/监管/国企/运营商官方页、FCC/NTIA/USAC/SAM/USAspending/DOI 记录、云官方区域清单、官方项目/合同记录）；B = 强二手（具名行业/本地/区域媒体含日期与主体：Samoa News、Talanei、DCD、RNZ、Islands Business、Telecompaper 等）；C = 目录/地图/社交/SEO/市场报告片段/未核实线索（DataCenterMap、Cloudscene、PeeringDB/ASN 聚合、Submarine Cable Map）。**分级只覆盖该源实际支撑的事实**：A 级运营商服务页不证明物理 colo 站点；B 级厂商公告（DXN CLS）不使设施成为商用 DC。
8. **计数与去重规则**：facility_type 精确（commercial_colo、government_dc、telecom_cable_station、telecom_core、enterprise_server_room、tower_edge、connectivity_only、false_positive）；status 精确（proposed、planned、procurement、under_construction、operational、discontinued、false_positive）；**海缆登陆 ≠ 数据中心**（一律 telecom_cable_station/connectivity_only 起步）；运营商服务/云营销无具名 AS 站点 = 服务线索/connectivity_only；容量字段（MW/机架）无官方/运营商/合同源则保持 null；"data center" 字样在 SAM.gov/联邦奖项中可能指境外托管 IT——须原文复核。

## 常用查询模板

```text
site:astca.as ("data center" OR "data centre" OR datacenter OR colocation OR hosting OR NOC OR "server room" OR "cable landing" OR "landing station")
site:astca.as (Hawaiki OR Manatua OR ASH OR SAS OR "Le Vasa" OR "SAS-2" OR Bulikula OR Google)
site:docs.fcc.gov "American Samoa" ASTCA ("cable landing station" OR "landing station" OR Tafuna OR "Le Vasa")
site:procurement.as.gov ("data center" OR "data centre" OR datacenter OR "server" OR "network" OR "cable landing" OR "generator" OR cooling OR "ICT")
site:americansamoa.gov ("data center" OR "data centre" OR datacenter OR ICT OR broadband OR "digital infrastructure" OR "Le Vasa" OR "SAS-2")
site:asgpressrelease.com ("Le Vasa" OR "SAS-2" OR ASTCA OR "digital infrastructure" OR "data center")
site:ntia.gov "American Samoa" (BEAD OR broadband OR "Digital Equity" OR "middle mile" OR "community anchor")
site:sam.gov "American Samoa" ("data center" OR datacenter OR "IT services" OR broadband OR telecom OR ASTCA)
site:usaspending.gov "American Samoa" (ASTCA OR "American Samoa Telecommunications" OR "Office of Procurement" OR broadband)
site:aspower.com ("data center" OR "data centre" OR "large load" OR substation OR generator OR "power purchase")
("American Samoa" OR "Amerika Samoa" OR "Sāmoa Amelika") ("data center" OR "data centre" OR datacenter OR colocation OR hosting OR "server room" OR "cable station" OR "landing station" OR NOC OR IXP)
"American Samoa" (Hawaiki OR Manatua OR ASH OR SAS OR "SAS-2" OR "Le Vasa") ("landing station" OR "cable station" OR Tafuna OR "Pago Pago")
"DXN" ASTCA "American Samoa" ("cable landing station" OR CLS OR "Le Vasa")
site:samoanews.com ("data center" OR "data centre" OR datacenter OR broadband OR cable OR ASTCA OR "Le Vasa")
site:talanei.com ("data center" OR "data centre" OR broadband OR ASTCA OR fiber OR "Le Vasa" OR "SAS-2")
site:datacenterdynamics.com "American Samoa" ("data center" OR "data centre" OR "cable landing station" OR DXN)
site:datacentermap.com "American Samoa" OR "Pago Pago" ; site:cloudscene.com "American Samoa" ; site:peeringdb.com "American Samoa" OR ASTCA
"American Samoa" ("AWS region" OR "Azure region" OR "Google Cloud region" OR "OCI region" OR "cloud region") - absence check
"American Samoa" (Starlink OR Kacific OR VSAT OR O3b OR satellite) (availability OR coverage OR license OR gateway)
"American Samoa" (edge OR "edge computing" OR cache OR CDN OR IXP)
```

## 官方/监管管线要点（详见 explorer-official.md）

- **FCC**：海缆许可/公告核心；DA-26-578A1（2026）= Le Vasa Tafuna CLS A 级证据；docs.fcc.gov 为文件宿主。
- **ASTCA**：州营电信运营商（astca.as；astca.net 重定向至 .as）；页脚链接当前 RFP；业务页面证明服务存在而非 colo 产品。
- **ASG/采购**：procurement.as.gov 已 curl 验证 HTTP 200；americansamoa.gov/pressreleases 与 asgpressrelease.com 为官方公告；"digital hub/data sovereignty" 等词无物理站点/合同不算设施证据。
- **联邦资金**：NTIA/BEAD（2025-11-21 批准 $37.56m，宽带/社区锚点非 DC）、USAC 高成本/E-rate、SAM.gov/USAspending、DOI OIA、USDA Rural Development/RUS。
- **电力**：ASPA（aspower.com）为大型负荷验证锚点；查询用全称 "American Samoa Power Authority" 避免港口/机场歧义。
- 每轮枚举须覆盖唯一 division（American Samoa 三行地理扫描：Tutuila/Manu'a/Swains+Rose），真无活动则记 `no_projects: true`；来源优先检查表：ASTCA → ASG/采购 → FCC/docs → USAC/SAM/USAspending → NTIA → DOI OIA → ASPA → 云区域清单 → 海缆源（Submarine Networks/Map 作 C 级发现）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 本地/区域媒体：Samoa News（B，ASTCA/DXN/采购/电力）、Talanei/KHJ（B/C；注意 khjnews.com 未解析，用 talanei.com 与 southseasbroadcasting.com/93khj）、Samoa Observer（B，防萨摩亚 WS 污染）、RNZ Pacific（B）、Islands Business（B，Hawaiki/ASTCA 背景）；行业媒体：DCD（B，DXN CLS/太平洋海缆）、Telecompaper/SubTel Forum/subseacables.net（B/C）、PITA/PTC/APNIC/ISOC（B/C 区域上下文）。
- 海缆厂商：DXN（模块化 DC 厂商但 AS 合同为 **CLS**）、SubCom、AP Telecom、Google/Starfish/Bulikula——术语易误导。
- 验证规则：A 运营设施 = 官方/运营商/合同源点名站点+位置+设施功能；B = 强媒体点名；C = 目录/社交/无本地物理证据服务页；**目录缺失为弱证据**（DataCenterMap 可能 429、Cloudscene 需搜索/登录、PeeringDB 仅互联元数据）；大功率声明须 ASPA 或项目文件支撑。
- 诚实结论（2026-08）：无已核实商用 colo、无超大规模云区域；Le Vasa/SAS-2/DXN 为电信/海缆设施观察项；企业/政府机房仅作 enterprise_server_room/government_dc 候选。

## 维护注意（更新纪律）

- **更新节奏**：每季度——ASTCA 站点/RFP、ASG 新闻与采购、Samoa News/Talanei 媒体扫描、DCD/厂商（DXN/SubCom/AP Telecom/Google）海缆报道、FCC 海缆公告；每半年——联邦资金（NTIA/BEAD、USAC、SAM/USAspending、DOI OIA）、ASPA 电力公告、四大云区域清单复检；每年——复核全部 U/C 条目与 no-commercial-colo 基线；事件驱动——任何 AS 云区域/colo 公告为最大变化，监控官方区域页。
- **来源核验**：逐一点击 A 级 URL；FCC 文件以 docs.fcc.gov 为准；厂商/媒体对 DXN 的 "data center" 措辞须对照合同原文核实为 CLS；萨摩亚 WS 记录须明确 AS 侧基础设施才保留。
- **不删除纪律（no-deletion）**：已核实记录不得删除；状态变化改标（proposed → procurement → under_construction → operational）并保留原始证据链；无支撑条目降级为 C/U 保留而非移除；负向检索（无项目）须如实记录而非跳过。
