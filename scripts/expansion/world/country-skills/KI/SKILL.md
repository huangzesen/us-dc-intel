---
name: ki-datacenter-methodology
location: scripts/expansion/world/country-skills/KI/SKILL.md
description: 基里巴斯数据中心发现与审计方法学（bilingual）。Kiribati datacenter discovery & audit methodology: enumerate the official/regulatory/cloud pipeline (MICT/CCK, MFED, BNL, World Bank/ADB/JICA project documents, PUB, cloud-region absence checks) plus industry/trade-press discovery (DCD, Submarine Networks, GeoCables, operators, directories). Division model: geographical unit with 3 divisions (Gilbert Islands, Line Islands, Phoenix Islands). Read before running KI exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# KI · 基里巴斯数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：基里巴斯无公开数据中心注册库、无可按项目检索的规划许可/建筑许可数据库，且属**极小（近零）商业数据中心市场**——截至 2026-08 无已确认的商业托管设施、无超大规模云区域、未发现公共 IXP；本方法论通过**官方/监管/云管线（explorer-official.md）**与**行业/媒体/厂商发现（explorer-industry.md）**双轨三角验证（registry-status / triangulation approach），将政府/捐赠方项目文件、监管与电力证据、海缆与运营商线索拼合成诚实的小型清单。本 skill 汇总两份最终审定的探索报告，作为 KI 探索/审计批次的入口。

## 入口

| 文件 | 管线 | 内容 |
| --- | --- | --- |
| explorer-official.md | 官方/监管/云管线 | MICT/数字转型办公室、CCK 监管、MFED、BNL、MLPID、PUB、世界银行/亚行/JICA 项目文件、云区域缺失检查、MTCIC/投资促进 |
| explorer-industry.md | 行业/厂商发现 | DCD、Submarine Networks、GeoCables、commsupdate、NEC 新闻稿、运营商（Vodafone Kiribati、Ocean Link、BNL）、卫星（Kacific/Starlink/Lynk）、目录与 PeeringDB 检查 |

## 核心结构事实

1. **行政区划模型**：manifest 为 **geographical unit**，3 个 division 直接对应三大岛群——**Gilbert Islands**（首都环礁 South Tarawa，人口/政府/互联中心）、**Line Islands**（Kiritimati/圣诞岛为枢纽；Teraina、Tabuaeran 低密度）、**Phoenix Islands**（仅 Kanton/Abariringa 有人定居，其余为凤凰群岛保护区 PIPA）。官方语言英语与吉尔伯特语；政府/监管/电信/捐赠方材料通常以英语发布，**搜索语言为英语**，吉尔伯特语只用于地名。
2. **无公开注册库**：枚举须联合 MICT（ICT 部/数字转型办公室）、MFED（海缆与数字项目执行机构）、BNL（国有海缆/基建公司）、世界银行/ADB/JICA 项目文件、Vodafone Kiribati 与 Ocean Link（电信运营商）、PUB（电力）、云区域页与行业媒体；官方渠道直接产出低，多为项目/政策文件而非设施注册。
3. **监管与法律**：电信牌照由 **Communications Commission of Kiribati (CCK)**（2013 年《通讯法》设立，前身为电信管理局）负责，服务含个人/类别牌照、频谱、编号、型号核准与 `.ki` 域名；MICT 为政策部委与上级监督渠道。**《2025 年数据保护法》（Data Protection Act 2025）**为已生效主要引证，是主权托管需求（国内/集装箱式数据中心与政府云采购）的驱动因素——援引前须复核生效与条例。
4. **互联锚点（海缆≠数据中心）**：**EMCS 东密克罗尼西亚海缆系统**（2,250 km，Tarawa–瑙鲁–科斯雷–波纳佩，延至关岛）——BNL 报告 2025-07-25 Tarawa 登陆、NEC 2026-05-15 宣布建设完成并移交，标记为“运营/在用”前须复核 RFS/零售服务状态；**Southern Cross NEXT Kiritimati 支线**——377 km 单纤对分支至 **Tabwakea（Line Islands）**，2022-07 起在用，登陆站由 BNL 运营。海缆登陆站与骨干网仅作互联证据，不得计为数据中心设施。
5. **电力是硬约束而非设施证明**：South Tarawa 电网为柴油基、由国企 **PUB** 运营；STREP 项目在 Bonriki 增 5 MW 光伏 + 13 MWh 储能（基里巴斯史上最大可再生能源装机，按数据中心标准仍极小）；外岛为小型村庄电网。2026-08 基里巴斯境内任何地点均无商用规模稳定电力支撑大型数据中心——任何 MW 宣称须对照 PUB 接电/馈线证据核验。
6. **当前物理与采购锚点（2026-08）**：(1) 世行资助 **Kiribati Digital Government Project (P176108)** 项下的**计划中/采购阶段国内（集装箱式）政府数据中心 + 政府云设备**——2026-03-13 修订采购计划将二期 `KI-MICTTD-470992-GO-RFQ` 列为 Pending Implementation（预算约 US$900,000），招标镜像显示 2026-03 发布、2026-03-31 截标；(2) EMCS Tarawa/Nanikai 登陆站；(3) SX NEXT Tabwakea 登陆站；(4) Vodafone Kiribati (ATHKL) 与 Ocean Link 电信核心/网络站点。**无任何源证实基里巴斯存在运营中的商业托管设施或超大规模云区域。**
7. **云区域为缺失检查**：AWS/Azure/Google Cloud/Oracle OCI 官方区域页均无基里巴斯区域（AWS 最近实用区域为悉尼/新加坡/东京）。SaaS 可用性、合作伙伴托管、边缘缓存或客户国支持不得生成 KI 设施记录。
8. **资产类别严格分离（不得合并）**：`government-DC | gov-cloud-procurement | cable-landing | telco-core | satellite-gateway | planned-proposal`；现有部委/服务器机房、登陆站、电信交换机房、卫星网关、计划提案各为独立记录。
9. **可靠性分级规则**：A = 官方/主源（MICT/DTO、CCK、MFED、BNL、MLPID、PUB、kiribati.gov.ki/president.gov.ki 官方页与通告、世行项目文件与采购通告、ADB 文件、JICA 报告、NEC 新闻稿、云官方页、EMCS 官方站、Vodafone Kiribati/Ocean Link 官方页、PeeringDB 互联事实）；B = 强二手（DCD、Submarine Networks、GeoCables、TeleGeography（经媒体）、UNCTAD、commsupdate、Islands Business、引用官员的可靠本地媒体）；C = 弱线索（DevelopmentAid/GlobalTenders 镜像、DataCenterMap、Cloudscene、市场报告、社媒、宣传文）；U = 无法二次确认。分级只覆盖该源实际支撑的事实；同一项目可有 A 级存在证据与 B/C 级容量或时间线证据。
10. **状态动词强制**：`landed` / `ready for service` / `construction complete` / `pending implementation` / `RFQ published` / `awarded` / `delivered` / `commissioned` / `in service since` 语义不同；计划/采购类记录必须带确切阶段与文号（如 `KI-MICTTD-470992-GO-RFQ`），未交付/未通电前不得计为已建。
11. **误报陷阱**：澳大利亚 **Christmas Island**（印度洋）不是基里巴斯——Google 2025 年底 AI 数据中心报道涉及澳属圣诞岛；基里巴斯的 Kiritimati 绝不能继承澳属圣诞岛的任何报道，检索须显式加 “Kiribati”。

## 常用查询模板

```text
site:mict.gov.ki ("data center" OR "data centre" OR datacenter OR "server" OR "cloud" OR REOI OR RFQ)
site:mict.gov.ki ("containerized" OR "government cloud" OR "Digital Government" OR "Data Protection Act")
site:cck.ki ("Individual License" OR "Class License" OR "Vodafone" OR "Ocean Link" OR Starlink)
site:mlpid.gov.ki ("data" OR "ICT" OR "cable" OR "Kiritimati" OR "investment")
site:bnl.com.ki ("cable" OR "landing station" OR "EMCS" OR "SX NEXT")
site:eastmicronesiacable.com ("ready for service" OR "Kiribati" OR "Tarawa")
site:pub.com.ki ("solar" OR "diesel" OR "STREP" OR "grid" OR "tariff")
site:vodafone.com.ki ("enterprise" OR "business" OR "hosting" OR "cloud" OR "data")
site:datacenterdynamics.com/en/news/ Kiribati ("data center" OR "data centre" OR "cable" OR "cloud" OR "EMCS")
site:submarinenetworks.com Kiribati OR EMCS OR "Southern Cross NEXT"
site:geocables.com Kiribati OR Tabwakea OR Tarawa
"Kiribati Digital Government Project" ("data center" OR "cloud" OR "procurement" OR "container")
"OP00432633" OR "KI-MICTTD-470992-GO-RFQ"
"EMCS" OR "East Micronesia Cable" ("Tarawa" OR "Nanikai" OR "ready for service")
"Kiritimati" OR "Christmas Island Kiribati" ("data center" OR "data centre" OR "server" OR "cloud" OR "compute")
"Kanton" OR "Abariringa" OR "Phoenix Islands" ("data" OR "server" OR "internet" OR "telecom")
"AWS" OR "Microsoft Azure" OR "Google Cloud" OR "Oracle Cloud" "Kiribati" ("region" OR "data center") - absence check
"Kiribati" ("data center" OR "data centre" OR datacenter OR colocation) -"Christmas Island Australia"
```

## 官方/监管管线要点（详见 explorer-official.md）

- 四遍式分工流程（每 division 均跑）：(1) 全国种子遍——MICT/DTO、MFED、世行通告（P176108、PRCP Phase 4）、JICA 调查、BNL、Vodafone Kiribati、Ocean Link、PUB、MTCIC/IPD、MLPID、云区域页；(2) 具名站点遍——South Tarawa（Betio/Bairiki/Ambo/Nanikai/Bonriki 等）、Kiritimati（Tabwakea/London/Banana）、Kanton；(3) 分区遍——按 division 模板查询并仅在镇/小岛/站点证据落入该 division 时归入；(4) 验证遍——按资产类别与状态分类。
- Gilbert Islands（优先级 South Tarawa）：KDGP 集装箱式 DC/政府云采购、EMCS Nanikai/Tarawa 登陆站、电信核心（Vodafone Kiribati、Ocean Link）基本全在环礁；外环礁为负预期，只留意岛屿议会/卫生/银行服务器机房与卫星/Starlink 网关。
- Line Islands（Kiritimati 战略观察）：SX NEXT Tabwakea 登陆站在用（2022-07 起）、MLPID 将 Kiritimati 打造为“世界级投资枢纽”的愿景、地价低、中太连通性最佳之一——但柴油/光伏电力受限，2026-08 未核实任何数据中心提案；留意任何将 SX NEXT 容量与土地/电力/投资促进挂钩的 MLPID/BNL/政府公告。
- Phoenix Islands：仅 Kanton（Abariringa）有人定居，PIPA 覆盖大部；记录负面检索而非跳过，仅留意政府/海岸警卫队卫星与通讯设备。
- 预期产出（诚实口径）：Gilbert ~2–4 条（KDGP/集装箱式 DC 采购、EMCS 登陆站、电信核心/机房线索），Line ~1–2 条（SX NEXT 登陆站、卫星/电信线索），Phoenix 0 条（负面检索后记 `no_projects`）——**极小市场，不得虚增**。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 高信号媒体/源：DCD（免费行业源最佳：EMCS 登陆、Lynk/Vodafone 星地手机、未来任何 DC/云报道）、Submarine Networks（海缆系统/登陆站/RFS 日期）、GeoCables（海缆地理/状态）、NEC 新闻稿（EMCS 建设完成，主供应商 A 级）、EMCS 官方站与 BNL 页（A 级项目状态）、commsupdate、Islands Business、ZDNET/content-technology（SX NEXT 历史）。
- 运营商/厂商种子：Vodafone Kiribati（ATHKL，2015-05 收购 TSKL 资产，South Tarawa 核心网 + Kiritimati 存在，运营商存在 A 级、设施细节 C 级）；Ocean Link（第二运营商，2018/2019 起运营，官方域名/联系方式为人工复核项）；BNL（国有海缆/基建公司，非数据中心运营商）；小 ISP（Speed Wave、Tentanini、TeniCom，C 级线索）；卫星（Kacific/Starlink/Lynk——接入/回程提供商，网关非数据中心）。
- 目录检查：DataCenterMap/Cloudscene/Baxtel 的 KI 页在复核中返回 429/404，目录缺失本身不是证明（页面能加载才算）；PeeringDB/PCH 常需人工浏览，复核搜索未现 KI 条目。
- 状态观察清单：EMCS RFS/零售服务、KDGP 集装箱式 DC 授标/交付/投产、2025 数据保护法生效/条例、任何将 Kiritimati 连通与土地/电力配对的 MLPID/MTCIC 投资公告、任何海缆中断或 RFS 延期。

## 维护注意（更新纪律）

- **更新节奏**：每月——MICT 新闻/招标（news-page、REOI 节点）、世行 P176108 采购通告（集装箱式 DC 授标/状态）、EMCS 官方站（RFS）、BNL 页（Kiritimati 支线零售推广）、MLPID 新闻、PUB 项目页；每季度——超大规模云区域页（缺失复查）、PeeringDB/PCH 人工检查、DataCenterMap/Cloudscene/Baxtel 目录（C 级线索）、DCD 与 Submarine Networks 关键词清扫；事件驱动——2025 数据保护法生效/条例、电信法合并、海缆 RFS/中断、任何命名 Kiritimati 或 Tarawa 数字基建的投资公告、集装箱式 DC 授标/交付；每遍——复查时效性状态：EMCS RFS/零售服务、`KI-MICTTD-470992-GO-RFQ` 的世行/STEP 授标与完成字段、CCK 牌照清单、Ocean Link 官方域名、PeeringDB 缺失、任何把计划 DC 从采购变为已交付/已投产的 MICT/MFED/BNL 公告。
- **来源核验**：复核层逐个点击 A 级 URL 确认页面实际载明所引事实；被阻断/限速/失效的目录页标为人工复核线索而非设施证据；记录须含 `name/aliases/operator/asset_class/division/islet/status/source_status_verb/capacity/power_sources/connectivity/evidence_grade_by_field/source_urls`。
- **不删除纪律（no-deletion）**：已复核记录不得删除；状态变化改标（如 landed → construction complete → RFS → in service）并保留原文号与日期证据链；无支撑条目标 U 作临时队列，绝不计数。
