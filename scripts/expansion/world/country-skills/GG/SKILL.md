---
name: gg-datacenter-methodology
location: scripts/expansion/world/country-skills/GG/SKILL.md
description: 根西岛数据中心双线查询方法论（官方/监管/云管线 + 行业/厂商/媒体发现），含 division 模型、A/B/C 来源分级与查询模板；English: dual-line datacenter discovery & audit methodology for Guernsey (official/regulatory/cloud pipeline + industry/vendor/media discovery), with division model, A/B/C source grading and query templates. 运行 GG 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。
---

# GG · 根西岛数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> **目的**：为根西岛（Bailiwick of Guernsey, GG）的数据中心探索与审计提供统一双线方法论。官方/监管线负责确认运营中、拟建或已停滞的数据中心/托管设施，行业/厂商线负责先确认服务再验证地址/容量/状态，两线互为三角验证。本文件由 codex 审核定稿的两份 explorer 合并而成，细节以 `explorer-official.md`（官方线）与 `explorer-industry.md`（行业线）为准。

## 入口

| 文件 | 职责 | 内容摘要 |
|---|---|---|
| `explorer-official.md` | 官方/监管/云管线：验证与定稿 | States of Guernsey 规划（Webmap/Websearch）、GCRA 电信监管、JT/Sure 运营商官方页、电力（Guernsey Electricity/Alderney Electricity）、GFSC/ODPA 客户侧监管、采购与政府 IT、Guernsey Registry、Alderney/Sark/Herm 覆盖；A/B/C 分级与陷阱 |
| `explorer-industry.md` | 行业/厂商/媒体发现：线索与预筛 | JT/Sure 一手运营商扫描、MSP（C5/Civica/Logicalis）、贸易媒体（Guernsey Press、Bailiwick Express、BBC CI、DCD、The Register 等）、目录站；目录到一手验证流程、容量提取指引与误报控制 |

## 核心结构事实

1. **行政区划模型**：manifest 为单一 division — `["Guernsey"]`（subnational_type=country；英国王室属地，不属英国本土或欧盟，有独立规划/电信/电力/金融/数据保护体系）。parish（St Peter Port、St Sampson、Vale、Castel、St Saviour、St Andrew、St Martin、St Peter in the Wood、Forest、Torteval）与 Alderney、Sark、Herm 只是 sub_area/覆盖检查字段，不是 division。
2. **注册库现状**：无独立国家数据中心登记处；主体证据用 Guernsey Registry（portal.guernseyregistry.com，A 级公司/SPV/运营商/注册状态与经济活动代码，不是设施证据）+ GCRA licences（运营商名册：JT (Guernsey) Ltd 前身 Wave Telecom、Sure (Guernsey) Limited、Logicalis Guernsey Ltd 等，不是设施目录）。
3. **法律与监管**：规划 — States of Guernsey Planning Webmap（2020 年以来）与 Planning/Building Control Websearch（2009-04-06 以来）查建筑/用途变更/发电机/机房/变电站/冷却与许可条件；电信 — GCRA 管牌照（牌照不等于 DC 设施证据）；金融/数据保护 — GFSC Cyber Risk（受监管机构须按 Cyber Security Rules and Guidance 管理信息安全/隐私/可用性风险）、ODPA（2024-01 欧盟委员会确认充分性地位，提供 cloud-based services/processor 指引）。
4. **互联与云**：无本地 hyperscale public cloud region；AWS/Azure/GCP/OCI 官方区域页仅用于负向确认；本地 cloud/VPS/reseller 页不得视为 hyperscale region。
5. **设施/项目种子（2026-08 复核基线）**：JT 官方页确认 Jersey and Guernsey primary data centre sites（ISO/IEC 27001、PCI-DSS、SOC2、72 小时柴油备份、N+N 空调）→ `operational` 服务证据 A，地址/容量待一手复核；Sure 官方页确认 Guernsey Data Centre（Tier III、24h 安保、数据大厅/笼位/共享托管、岛间连接、**2MW IT load**）→ `operational` A；States of Alderney 2026 官方 data-centre EOI → `planned/exploratory`（不是已建设施）；政府 secure data centre / MyGov 隐私政策 → `internal/government` 线索，不得混为商业 DC；Digital Greenhouse → `not_a_datacenter` 反证。
6. **语言与词汇**：英语为主（data centre、colocation、planning application、standby generator、IT load、Tier III、2MW 等）；品牌陷阱 — JT 跨 Jersey/Guernsey，必须区分 Jersey-only 地址、Channel Islands 总称与 Guernsey site。
7. **可靠性分级（A/B/C）**：A=官方/一手（States of Guernsey 规划、gov.gg、States of Alderney、GCRA、Guernsey Electricity、Alderney Electricity、GFSC、ODPA、Guernsey Registry、JT/Sure 官方数据中心页、AWS/Azure/GCP/OCI 官方区域页）；B=强二级（Guernsey Press、Bailiwick Express、BBC CI、ITV Channel、DCD、The Register、Channel Eye、Island FM、Guernsey Finance — 证明“该来源如此报道”，设施入库存仍需 A 级物理/运营证据）；C=目录/聚合/SEO（DataCenterMap、Datacenters.com、Cloudscene、Data Center Platform、ColocationM、主机商 landing pages、无地址云经销商页 — 只做 seed）。字段级分级优先于记录级分级。
8. **计数与去重规则**：容量 — 官方 IT load/rack 数/sqm/UPS/发电机/冷却冗余可提取，无官方数字保持 null；Sure 2MW IT load 可作 A 级披露，JT 未披露 Guernsey 专属 MW 时不得从第三方目录抄写；岛级供电容量（GEL/Alderney Electricity）是供电上下文，不得反推 IT load；投资额/经济影响/租赁预测不转化为 MW；误报 — Jersey 设施/Jersey IX/Jersey-only JT 设施不得归入 GG、电信机房/移动基站/光纤节点/海缆登陆站/电站/变电站只记网络电力上下文、政府 secure DC 须区分 internal/government 与 commercial colocation。

## 常用查询模板

```text
# 规划/政府
site:gov.gg "data centre" "Guernsey"
site:planningexplorer.gov.gg "data centre"
site:planningexplorer.gov.gg "server room"
site:planningexplorer.gov.gg "standby generator" "St Peter Port"
site:planningexplorer.gov.gg "La Vrangue"
site:planningexplorer.gov.gg "First Tower Lane"
site:gov.gg "data centre services" tender
# 监管/运营商
site:gcra.gg "JT (Guernsey) Ltd"
site:gcra.gg "Sure (Guernsey) Limited"
site:business.jtglobal.com "Guernsey" "Data Centre"
site:business.sure.com "Guernsey Data Centre" "Tier III"
"Sure" "Guernsey Data Centre" "2MW IT load"
# 电力/客户侧监管
site:electricity.gg "large load"
site:alderney-elec.com "data centre"
site:gfsc.gg "Cyber Security Rules and Guidance"
site:odpa.gg "cloud-based services"
# 公司登记/Alderney
site:portal.guernseyregistry.com/search "Alderney" "Data"
site:alderney.gov.gg "Expression of Interest" "data centre"
# 贸易媒体
site:guernseypress.com "data centre" "Guernsey"
site:bailiwickexpress.com "Alderney" "data centre"
site:datacenterdynamics.com "Guernsey" "data centre"
site:theregister.com "Alderney" "data centre"
# 容量
"Sure Guernsey Data Centre" "2MW"
"JT" "Guernsey" "72-hour diesel"
"Alderney" "data centre" "MW" OR "MVA" OR "power"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **States of Guernsey 规划**：先查精确设施地址，再查 parish/road name，再查申请人；提取 application number、site address、parish/island、applicant、proposal、decision/status/date、conditions、generator/UPS/cooling/substation 备注。
- **GCRA**：`gcra.gg/businesses/telecoms/licences` 确认持牌运营商与监管名称；不得把 licence 当设施证据。
- **JT / Sure 官方页**：确认运营中服务、认证、冗余与容量披露；JT 页确认 Guernsey primary sites，Sure 页确认 Guernsey Data Centre 与 2MW IT load；地址仍需产品文档/规划/其他一手材料确认。
- **电力**：Guernsey Electricity / Alderney Electricity 提供供电上下文、进口容量与连接政策；不得用岛级容量反推 IT load。
- **GFSC / ODPA**：解释金融服务、外包、云、处理者和数据保护要求 — “客户为何选择本地托管”的上下文，不能单独证明物理设施。
- **采购/政府 IT**：gov.gg 站内搜 `procurement`/`tender`/`data centre`；“Statement to Press re move of Data Centre”与 MyGov privacy policy 属政府内部 IT/data-centre 线索，不得自动等同商业托管。
- **Guernsey Registry**：确认 SPV/运营商/开发商/注册状态/经济活动代码；主体证据而非设施证据。
- **Alderney/Sark/Herm**：Alderney 单独查 States of Alderney planning/Hansard/committee minutes；2026 EOI 是 pipeline 证据非 operational；Sark/Herm 主要负向控制。
- **官方云区域页**：AWS/Azure/GCP/OCI 区域页确认无 Guernsey region，有则记录 negative evidence。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **优先运营商扫描**：JT（A 级确认 Guernsey 服务；地址/容量待补证）、Sure（A 级 operational；2MW IT load 可记录为官方容量披露）、Sure offshore 组合页（A 级组合页，不能替代本岛设施页）、GCRA 持牌运营商名册、C5 Alliance/Civica/Logicalis/MSP（B/C 线索，必须排除纯转售或 remote cloud）、Digital Greenhouse（反证）。
- **目录到一手流程**：从目录只抽 facility name/operator/address/claimed MW/sqm/racks → 用 `"exact address" "operator" "Guernsey"`、`site:business.{operator-domain}`、`site:planningexplorer.gov.gg` 查一手 → GCRA 确认运营商法定名、Registry 确认 SPV 状态 → 目录容量若官方未披露写 `capacity_mw: null`、目录容量进 notes 标 `source_grade=C` → Alderney EOI 只有规划许可/开发协议/建设公告才能升级为 planned/permitted 或 under_construction。
- **贸易媒体与二级来源**：Guernsey Press、Bailiwick Express（2026 Alderney EOI 有报道）、BBC CI、ITV Channel、DCD、The Register、Channel Eye、Island FM、Guernsey Finance；本地媒体更早报政府 IT/金融 IT/海缆故障/电力项目。
- **诚实结论**：供给以本地/海峡群岛电信运营商（JT、Sure）为核心；无本地 hyperscale region；Alderney 是探索性 pipeline；目录地址（First Tower Lane、La Vrangue）默认 C 级，须 A 级复核。

## 维护注意（更新纪律）

- **更新节奏**：事件驱动 + 定期 — Alderney EOI 后续（EOI PDF、规划路径、开发商响应、committee minutes/Hansard）、JT/Sure 产品文档或官方地址页、规划 Websearch 新增 data centre 申请、GCRA 牌照变更、Alderney Electricity 供电公告；无建成证据前 Alderney 不得标 operational。
- **来源核验**：每记录必含 `division=Guernsey`、`sub_area`、`facility_name`、`operator/developer`、`status`、`source_grade`、`evidence_url`、`evidence_note`、`capacity_mw`（未知设 null）；字段级分级优先；JT/Sure 服务可 A 级入库但街道地址与容量字段必须按证据来源分别分级。
- **不删除纪律**：本目录只允许新增/更新文件，禁止删除或移动任何文件；目录地址不得升级除非被 A 级来源复核；不要沿用未核实的“2014-2015 已许可 £1.4bn 项目”说法。
