---
name: mc-datacenter-methodology
location: scripts/expansion/world/country-skills/MC/SKILL.md
description: |
  Monaco (MC) datacenter discovery & audit methodology — how to enumerate, verify, and update Monaco datacentre facilities at 17-quarter granularity. Monaco is a city-state with no provincial planning authorities: building evidence is centralised in the Prince's Government (DEEU/DPUM/Direction des Travaux Publics) and legal notices in the Journal de Monaco (protected-zone arrêtés, tenders). Confirmed evidence is small and sovereignty-driven: Monaco Telecom (3 data centers — certified sites at 4-6 avenue Albert II Zone F / DC3 and 25 boulevard de Suisse Centre de données n°1, ISO/HDS certificate), the Larvotto Supérieur project (Journal 8649 tender, ~1,600 m2 proposed), Telis/MonacoDATACENTER (14 avenue de Grande-Bretagne, since 2013, ISO 27001/HDS, Tier III-designed, thalassothermal cooling), Monaco Cloud (sovereign cloud platform — AMSN-qualified, not a standalone facility), and the DRSI government computer room (23 avenue Albert II, protected zone). No AWS/Azure/GCP/OCI region; watch the France border (Cap-d'Ail, Beausoleil, Nice, Sophia Antipolis must be excluded). Read this before running MC exploration/audit batches. Routes to explorer-official.md (government/gazette/energy/cyber pipeline) and explorer-industry.md (operator/trade-press/directory verification).
---

# MC · 摩纳哥数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：摩纳哥是**单一市镇城邦**，没有省级规划机构——开发证据集中在亲王政府（DEEU/DPUM/公共工程局）与 **Journal de Monaco** 法律公告（保护区法令、招标）；17 个 quarter 为本仓库工作分区，设施按**物理地址**分配，不按总部/销售处/注册处/POP/客户站点。
> 已确认证据小而主权驱动：**Monaco Telecom 三座 DC**（2025 ISO/HDS 证书：`4-6 avenue Albert II - Zone F` 主址/DC3、`25 boulevard de Suisse` Centre de données n°1、`Zone F, 4-6 avenue Albert II` Centre de données n°6）、**Larvotto Supérieur 项目**（Journal 8649 招标，约 1,600 m2，proposed）、**Telis/MonacoDATACENTER**（14 avenue de Grande-Bretagne，2013 起，ISO 27001/HDS、Tier III 设计、海水冷却）、**Monaco Cloud**（主权云平台，非独立设施）、**DRSI 政府机房**（23 avenue Albert II，保护区）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供摩纳哥探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：DEEU/DPUM/公共工程与 Journal de Monaco（保护区/招标）、SMEG 能源与热海网络、AMSN 网络安全/保护区、APDP 数据保护、Extended Monaco/Data Monaco 公共数字设施、17 区工作流、设施分类规则、验证清单 |
| `explorer-industry.md` | 行业/厂商发现：运营者扫描（Monaco Telecom 平台/证书/DC3/Zone J/Larvotto、Telis MonacoDATACENTER、Monaco Cloud、DRSI、银行/赌场/酒店机房）、贸易媒体（DCD/Monaco Life/Monaco Hebdo/Global Security Mag/Monaco Now）、目录到一手工作流、17 区配方、种子清单、容量提取指导 |

## 核心结构事实（框定每次搜索）

1. **Monaco Telecom 是核心运营者**（A）：官方平台页称 3 座 DC、最高 12 kW/机架、2N 供电、ISO 27001:2022/HDS；2025 证书比旧媒体更精确——**优先用证书定站点地址与命名**；历史 2014/2015 报道（DC3 约 1,000 m2/200 机架、EUR 6m 投资）只作历史 B 级上下文，不得假设仍与今天三座认证中心对应。
2. **官方文件锚（A）**：Arrêté Ministériel 2019-452（Journal 8435, 24/05/2019）为 MT DC3 保护区（Zone F 建筑 4 层，`6 avenue Albert II`）；2019-453 为 DRSI 机房保护区（`23 avenue Albert II` 1 层）；Journal 8649（30/06/2023）Larvotto Supérieur 招标含约 1,600 m2 MT 数据中心（R-3/R-4 层，工期最多 36 个月）——**proposed/开发中**，交付验证前不算运营。
3. **Telis/MonacoDATACENTER（A）**：2013 年摩纳哥首个绿色数据中心，`14 avenue de Grande-Bretagne`，ISO 27001/HDS、Tier III 设计、99.997% 声称可用性、海水/自由冷却、24/7/365 值守——用 Telis 官方页核验，不用目录条目。
4. **Monaco Cloud（A 平台，非设施）**：国家主权云，国资控股，官方页称多云站点、数据按摩纳哥法律存储管理、AMSN 认证（PINH Avancé/PSSI-E）、总部 `9 avenue Albert II - Le Copori`；**办公室地址 ≠ DC**——物理足迹只能通过 MT/Telis 托管证据映射；不要数云实例为物理容量。
5. **政府机房（A 公共部门）**：DRSI 机房 `23 avenue Albert II` 是受保护区证明的政府 IT 室，非商业 colo；除非出现公共托管/colo 证据。
6. **超大规模缺席（A）**：AWS/Azure/GCP/OCI 均无摩纳哥区域；“AWS technology/AWS Outposts/云伙伴”措辞 ≠ 摩纳哥区域——始终对照官方区域列表。
7. **能源**：SMEG（smeg.mc）是唯一配电/配气商——连接、变压器、功率、备用馈电、热海网络关键源；Direction de la Transition Énergétique 政策源；2022-11-29 停运报道（Monaco Life B）指出 Fontvieille 购物中心下 Zone J 数据中心、SMEG 电网维护断连、发电机故障——韧性/位置线索，非容量证据。
8. **跨境陷阱**：Cap-d'Ail、Beausoleil、Roquebrune-Cap-Martin、Nice、Sophia Antipolis、CHPG Cap Fleuri 都是**法国**——不得分配给 MC 分区。
9. **容量规则**：摩纳哥极少公布 MW——默认 `capacity_mw: null`，代理指标（12 kW/机架、1.3 kW/m2、2N、N+1 冷却、2020 ISO 公告称三座 DC 共 2,000 m2 IT 机房）按原文存 notes；不得把 kW/机架或面积换算成 MW。
10. **语言**：法语术语——`centre de données`、`datacenter`、`salle informatique`、`salle de serveurs`、`hébergement`、`cloud souverain`、`zone protégée`、`raccordement`、`groupe électrogène`、`thalassothermie`、`SeaWergie`。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§2 / explorer-industry.md §1-§4）

- Gazette：`site:journaldemonaco.gouv.mc "data center" "Monaco Telecom"`、`site:journaldemonaco.gouv.mc "zone protégée" "Data Center"`、`site:journaldemonaco.gouv.mc "Larvotto Supérieur" "data center"`、`site:journaldemonaco.gouv.mc "Monaco Cloud S.A.M."`、`site:journaldemonaco.gouv.mc "boulevard de Suisse" "centre de données"`、`site:journaldemonaco.gouv.mc "avenue de Grande-Bretagne" "datacenter"`。
- 能源：`site:smeg.mc "data center"`、`site:smeg.mc "Monaco Telecom" raccordement`、`site:transition-energetique.gouv.mc thalassothermie Fontvieille`、`"SMEG" "Zone J" "Monaco Telecom"`、`"SeaWergie" "data center" Monaco`。
- 网络安全/数据保护：`site:amsn.gouv.mc "Monaco Cloud" "PINH"`、`site:amsn.gouv.mc "Monaco Telecom" "OIV"`、`site:apdp.mc "Monaco Telecom" hébergement`。
- 公共数字设施：`site:gouv.mc "cloud souverain" Monaco`、`site:gouv.mc "Direction des Réseaux et Systèmes d'Information"`、`site:data.gouvernement.mc antennes Monaco Telecom`、`site:monacocloud.mc "multi-site"`。
- 运营者：`"Monaco Telecom" "Centre de données n°1"`、`"Monaco Telecom" "25 boulevard de Suisse"`、`"Monaco Telecom" "4-6 avenue Albert II"`、`"Monaco Telecom" "Zone J" Fontvieille`、`"Monaco Telecom" "Larvotto Supérieur"`、`"MonacoDATACENTER" "14 avenue de Grande-Bretagne"`、`"Telis" "MonacoDATACENTER" "Tier III"`、`"Monaco Cloud" "PINH Avancé"`。
- 区模板：`"{quarter}" Monaco "data center"`、`"{quarter}" Monaco "salle informatique"`、`"{quarter}" "Monaco Telecom"`、`site:journaldemonaco.gouv.mc "{quarter}" "data center"`。
- 贸易/目录：`site:datacenterdynamics.com Monaco "Monaco Telecom"`、`site:monacolife.net "Monaco Telecom" "data centre"`、`site:monaco-hebdo.com "Monaco Telecom" "data center"`、`site:monaconow.com "Monaco Cloud"`、`site:datacentermap.com/monaco/ "Monaco Telecom"`、`site:baxtel.com "Monaco Telecom" Monaco "Larvotto"`。

## 官方/监管管线要点（详见 explorer-official.md）

- **Journal de Monaco（A）**：已核实高置信记录——2019-452（MT DC3 保护区）、2019-453（DRSI 机房）、Journal 8649（Larvotto Supérieur 招标，含 1,600 m2 DC）、Monaco Cloud S.A.M. 章程公告（法人存在，非设施）；提取文档类型/号/期/日期/URL、申请人/运营者、精确地址/楼层、项目措辞、披露规模/机架/工期/认证、证明的是运营站点/提案/机房还是仅法人。
- **SMEG（A）**：连接/变压器/功率/备用馈电/热海网络；Direction de la Transition Énergétique 政策。
- **AMSN（A）**：合格产品/服务（PINH/PSSI-E）、OIV 语境、CERT-MC、保护区语境；APDP（2024-12-03 Law 1.565 后接替 CCIN）数据保护申报仅作佐证。
- **Extended Monaco / Data Monaco / DSI-DRSI（A/B）**：国家数字战略、开放数据门户（非 DC 普查）、`23 avenue Albert II` 政府 IT 室。
- **云缺席（A）**：四家官方区域页核验；拒绝任何未验证的“hyperscale Monaco”声称。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **运营者扫描**：Monaco Telecom 平台（A 平台：3 DC、colocation/private space、12 kW/rack、2N、N+1）、2025 证书（A 当前认证站点清单）、DC3（A Journal+证书+2015 启动 B 历史）、Zone J 遗留（B，2022 停运）、Larvotto Supérieur（A 项目/B 细节：DCD 称 19 boulevard du Larvotto、1,550 m2、2027 完工）、Telis/MonacoDATACENTER（A）、Monaco Cloud（A 平台）、DRSI（A 机房）、银行/赌场/酒店机房（默认 C/不计数）。
- **连接性语境**：MT 商用产品提供至 10 Gbps 专用光纤与托管/云（连接性语境非设施计数）；Europe India Gateway 海缆声称按 B（除非 MT/海缆所有者确认）；**无公开摩纳哥 IXP**——不要发明交换点/园区/运营商中立生态。
- **贸易媒体（B）**：DCD、Monaco Life（2022 停运）、Monaco Hebdo（2014 扩展历史）、Global Security Mag（2015 DC3 落成）、Univers Freebox、Monaco Now（2021-10 主权云运营）、Cloud Computing News、Le Monde Informatique（AWS Outposts 历史选项——不是 AWS 区域）、Monaco Tribune/Monaco-Matin/Nice-Matin/Gazette de Monaco。
- **目录（C）**：DatacenterMap（MT DC3/MonacoDATACENTER）、Baxtel（Larvotto Supérieur 在建）、Data Center Platform（Telis 14 Av. de Grande-Bretagne）、DC Byte/Cloudscene/DatacenterCatalog——仅种子/候选，字段级分级（同一源可对运营者存在为 A、对目录地址为 C）。
- **容量代理**：MT 平台 12 kW/rack、1.3 kW/m2、2N 链路、N+1 冷却、惰性气体灭火；2020 ISO 公告 3 DC 共 2,000 m2；DC3 历史约 1,000 m2/200 机架（B）；Larvotto 官方 1,600 m2（Journal）vs DCD 1,550 m2——以官方措辞为准；Telis 节能声称不得换算 MW。

## 来源分级

- **A** = 官方/一手：gouv.mc、monservicepublic.gouv.mc、Journal de Monaco、SMEG、AMSN、APDP、运营者证书或运营者官方页。
- **B** = 具名当事方贸易/本地媒体：DCD、Monaco Life、Monaco Hebdo、Global Security Mag、Monaco Now、Cloud Computing News、Monaco Tribune/Monaco-Matin/Nice-Matin/Gazette de Monaco。
- **C** = 目录/市场/SEO/未验证聚合：DatacenterMap、Baxtel、Data Center Platform、Cloudscene、DC Byte、DatacenterCatalog。
- **字段级分级**：证明具体字段的源的等级为准；目录地址不得升 A，除非官方页/证书/Gazette 公告/运营者申报确认。
- **状态语义**：Larvotto Supérieur = proposed/under development（无启用源前）；Monaco Cloud = 主权云平台（只经确认托管 DC 映射）；DRSI = 公共部门机房（非商业 colo）；银行/赌场/酒店自有机房 = C/不计数；Zone J = B 韧性/位置线索。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=MC，divisions=17 quarter）。
2. 种子：Monaco Telecom 官方页 + 2025 ISO/HDS 证书 + Journal 保护区/招标 + Telis 页面 + Monaco Cloud 官方 + DRSI 记录。
3. 17 区逐一扫描（即使预期为零产）：区通用模板 + Gazette/运营者/能源域；Fontvieille 最高产（Avenue Albert II/Zone F、Le Copori、Grande-Bretagne、Terrasses de Fontvieille）。
4. 地址→quarter 映射用地址几何，不用营销区名：`25 boulevard de Suisse`（Monte-Carlo/Sainte-Devote 边界）、Larvotto Supérieur（Larvotto/Saint-Roman 边界）、`4-6/6 avenue Albert II`、`9 avenue Albert II`、`14 avenue de Grande-Bretagne`、`23 avenue Albert II`（均按 repo 几何核验）。
5. 目录到一手：目录种子 → MT 页+证书+Journal 公告 / Telis 页 / Journal 招标 → 地址几何 → 状态证据；仅目录声称存 `candidate_seed`/C，不进最终计数。
6. 分类与状态：运营 colo/托管 DC vs proposed/在建 vs 主权云平台 vs 公共部门机房 vs 仅目录线索；Larvotto 保持 proposed 直到启用/证书/运营者页证明在运。
7. 排除法国站点（Cap-d'Ail、Beausoleil、Nice、Sophia Antipolis、CHPG Cap Fleuri）；核对证书/Gazette/2022 停运来源关系（Zone J 与当前认证中心的关系待 MT/SMEG/JDM 确认）。
8. 输出与 world 探索同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；无 MW 用 null 并把代理值+等级存 notes。
9. 遵守 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：批量复核摩纳哥数据中心（17 quarter 粒度）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Larvotto Supérieur 启用/竣工时间线、Zone J 与当前三座认证中心的关系、Monaco Telecom 三座 DC 在 repo 几何下的精确 quarter 归属、Telis 当前认证/客户、Monaco Cloud 物理托管站点映射、SMEG/Journal 是否出现新设施连接记录。
