---
name: fo-datacenter-methodology
location: scripts/expansion/world/country-skills/FO/SKILL.md
description: 法罗群岛数据中心双线查询方法论（官方/监管/云管线 + 行业/厂商/媒体发现），含 division 模型、A/B/C/U 来源分级与查询模板；English: dual-line datacenter discovery & audit methodology for Faroe Islands (official/regulatory/cloud pipeline + industry/vendor/media discovery), with division model, A/B/C/U source grading and query templates. 运行 FO 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。
---

# FO · 法罗群岛数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> **目的**：为法罗群岛（Faroe Islands, FO）的数据中心探索与审计提供统一双线方法论。官方/监管/云管线段负责用 A/B 证据确认设施，行业/厂商/媒体段负责发现候选并回查确认，两线互为三角验证。本文件由 codex 审核定稿的两份 explorer 合并而成，细节以 `explorer-official.md`（官方线）与 `explorer-industry.md`（行业线）为准。

## 入口

| 文件 | 职责 | 内容摘要 |
|---|---|---|
| `explorer-official.md` | 官方/监管/云管线：确认与定稿 | 官方登记（Skráseting、Lógasavn、Fjarskiftiseftirlitið、SEV、Umhvørvisstovan、Dátueftirlitið）、Keypsportal 采购、规划/EIA、政府 IT、超大规模云区域检查；6 覆盖区域分桶枚举、分级与已确认设施表 |
| `explorer-industry.md` | 行业/厂商/媒体发现：线索与预筛 | Elektron/Nema/FT/NET 运营商、Farice/SHEFA 海缆、PeeringDB/Pulse/BGP 网络库、行业媒体（DCD、Capacity、KVF、Portal、Computerworld DK 等）、目录聚合器；枚举矩阵与谨慎规则 |

## 核心结构事实

1. **行政区划模型**：manifest 为单一 division — `["Faroe Islands"]`（subnational_type=country，法罗为丹麦王国下自治地区，1948 年自治，不属欧盟）。扫描时用 6 个传统区域作覆盖清单：Streymoy、Eysturoy、Norðoyar、Vágar、Sandoy、Suðuroy（全国 29 个市镇，Hagstova 统计入口 `hagstova.fo`）；禁止把 6 区域写成 divisions。
2. **注册库现状**：无国家数据中心登记处（不同于挪威 Nkom 式登记）；清点须组合公司登记（Skráseting，A 级公司事实但不单独证明设施）、运营商自述、采购、规划/建筑许可、SEV 电力资料、电信许可、海缆/IXP 资料。
3. **法律与监管**：电信法 `Løgtingslóg nr. 72 frá 22.05.2015 um fjarskifti`（Lógasavn 权威库，2024-05-16 修订）；DC 运营机房不自动成为电信服务商，提供公共通信/频谱/编号服务才入 Fjarskiftiseftirlitið 范围；规划/建筑许可以市镇网站与会纪要为先；EU 规则不直接套用（FO 非欧盟）。
4. **互联与云**：FARICE-1 经 Funningsfjørður branch 接入法罗并服务 Torshavn；SHEFA-2 连接 Torshavn、设得兰/奥克尼和苏格兰；截至 2026-08-12 AWS/Azure/GCP/Oracle 官方区域页无 FO 公有云区域。登陆站/PoP 不等于数据中心。
5. **设施/项目种子（2026-08 复核基线）**：无公开规格的超大规模或独立第三方 colocation campus；已确认的是本地 managed hosting / IT 运营者 — **Elektron**（自页 `Húsing` + 2022 年报管理约 1,500 servers，HPE 2025 案例 B 级佐证）、**Nema Húsing**（DPA 声明物理数据存储于 Føroyar）、政府 `datacenter B` UPS 采购线（Keypsportal 豁免页，B22 建筑待回查）、FT/NET Klingran 3 电信网络设施（仅电信/网络线索）。
6. **语言与词汇**：法罗语优先（data miðstøð、húsing、samhúsing、servarar、byggiloyvi、byggisamtykt、vinnuøki、útboð、undantak、sjókaðal 等），丹麦语/英语补充（datacenter、colocation、submarine cable、EIA、grid connection 等）；自动检索不要把裸 `OR` 混入 `site:` 查询同一行。
7. **可靠性分级（A/B/C/U）**：A=一手/官方直接证明（市政许可/会议纪要、Umhvørvisstovan EIA、SEV 文件、Skráseting、Lógasavn、运营商自有 hosting/facility 页、Keypsportal、Farice/SHEFA 自有页）；B=可信二手或厂商案例（HPE story、DCD、Capacity、KVF、Portal、Dimmalætting、Sosialurin、Norðlýsið、Computerworld DK、Version2、Energiwatch，具名公司/地点/日期/状态）；C=聚合/自报/弱证据（PeeringDB、Pulse、Submarine Cable Map、BGP/IP 库、DataCenterMap、Baxtel、LinkedIn、市场报告摘要）；U=未验证不可用，不进最终设施表。分级只针对具体事实（如 `Elektron DataCenter` BGP 标签仅 C 级网络标签）。
8. **计数与去重规则**：海缆登陆站、PoP、网络节点不是 DC，除非同设施有 hosting/colocation/IT 运营证据；2030 年 100% 可再生目标、风电/储能、凉爽气候叙事只是市场背景；政府机房采购（UPS、Oracle support）证明 IT 需求但不等同商业 DC。

## 常用查询模板

```text
# 法律/监管/EIA
site:logir.fo "datacenter"
site:logir.fo "fjarskifti"
site:us.fo "data miðstøð"
site:us.fo "umhvørvismat"
site:fjarskiftiseftirlitid.fo "fjarskiftisveitarar"
# 采购/政府 IT
site:keypsportal.fo "datacenter"
site:keypsportal.fo "UPS" "datacenter"
site:keypsportal.fo "Talgildu Føroyar" "Oracle"
site:talgildu.fo "húsing"
# 公司/运营商
site:skraseting.fo "Elektron"
site:elektron.fo "húsing"
site:elektron.fo "servarar"
site:nema.fo "Nema Húsing"
site:ft.fo "server"
site:net.fo "Klingran 3"
# 市政规划/建筑许可
site:torshavn.fo "byggiloyvi" "Klingran"
site:klaksvik.fo "datacenter"
site:runavik.fo "datacenter"
# 电力/电网
site:sev.fo "datacenter"
site:sev.fo "stórnýtsla"
"Elektron" "SEV" "húsing"
# 海缆/连接性
site:farice.is "FARICE-1" "Torshavn"
site:shefa.fo "SHEFA-2"
"Faroe Islands" "IXP" "PeeringDB"
# 行业媒体
site:kvf.fo "datacenter"
site:portal.fo "datacenter"
site:datacenterdynamics.com "Faroe Islands"
site:computerworld.dk "Færøerne" "datacenter"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **规划/EIA/市政许可**：Tórshavn（重点 Hoyvík/Klingran、Staravegur）→ Klaksvík/Runavík/Vágar/Tvøroyri 等市镇站；Umhvørvisstovan（`us.fo`）查 EIA/地图/环境许可；EIA screening/decision 可作 A 级项目证据。
- **电力与电网**：SEV（`sev.fo/english/`）年报/新闻/技术资料确认电网、发电结构、大用户与电源改造；Hagstova 电力统计页确认 SEV 为主要供电者（2024 可持续电力生产 271 GWh、占 56.6%）；一般能源转型材料只作背景。
- **电信/海缆/IXP**：Føroya Tele/FT（`ft.fo`，总部 Klingran 3）、NET（`net.fo`，光纤网络）、Fjarskiftiseftirlitið 许可/运营商列表（普查用）、Farice（FARICE-1）、SHEFA（SHEFA-2）；PeeringDB/Pulse 仅 C 级发现。
- **政府 IT/采购**：Talgildu Føroyar（数字法罗，财政部牵头）找政府平台/身份认证/云 hosting 线索；Keypsportalurin（`keypsportal.fo/undantok/`）用 `datacenter`/`UPS`/`Oracle`/`húsing` 查豁免/采购记录；`datacenter B` 采购须回查采购主体、B22 建筑与用途，避免扩大解释为商业 DC。
- **超大规模云区域**：每半年核对 AWS/Azure/GCP/Oracle 官方区域页（2026-08-12 均无 FO）。
- **搜索纪律**：每条查询保持简单，一行内不要混用多个未加括号的 `OR`；法罗语优先、丹麦语/英语补充。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **运营商骨架**：Elektron（当前最强本地 hosting 线索：`Húsing`/`Netloysnir`/`KT-trygd` 自页 + 2022 年报约 1,500 servers + HPE 2025 案例，分类为 confirmed hosting provider，设施地址/规格未公开到可标 DC campus）、Nema Húsing（DPA 声明物理数据在 Føroyar，设施位置/规模待核）、FT/NET（仅电信/网络设施线索，当前公开页未确认商业 colocation 产品）、政府 IT/Talgildu Føroyar（`datacenter B` UPS 采购线待回查）。
- **连接性来源**：Farice（FARICE-1/DANICE/ÍRIS，A 级海缆事实）、SHEFA（A/B 级）、DCD/SubTel/Capacity/TeleGeography 监控海缆故障/升级；海缆韧性报道不得解读为 DC 建设。
- **行业媒体与本地媒体**：KVF、Portal、Dimmalætting、Sosialurin、Norðlýsið、DCD Faroe tag、Computerworld DK/Version2/Ingeniøren/Energiwatch、Nordregio、e-Governance Academy、HPE 案例；无官方/运营商回证时保持 B/lead。
- **聚合器与认证**：DataCenterMap/Baxtel/DataCenters.com/PeeringDB/BGP.HE.net/IP2Location 仅作发现；Uptime/ISO 27001/EN 50600/SOC 认证只在认证库或资产方页面出现时才定级（Elektron 自报 ISO certified 可 A 级记录“公司认证声明”，但不自动推出 facility tier）。
- **谨慎规则**：FT hosting 假设（旧稿误标，当前页未确认商业 colo）；`Elektron DataCenter`/`NEMA Datacenter`/`DCH` 等 IP/BGP 标签不等于实地设施；政府机房、海缆登陆站、可再生电力叙事、LinkedIn 职位均不得直接计为 DC。
- **诚实结论**：无 hyperscale 或大型第三方 colocation campus；行业 leads 一律回 `explorer-official.md` 用 A/B 证据确认后方可入设施表。

## 维护注意（更新纪律）

- **更新节奏**：每月 — Elektron/Nema/FT/NET 新闻、Keypsportal `datacenter`/`húsing`/`UPS`、SEV 新闻、Tórshavn 许可、DCD Faroe tag；每季 — Fjarskiftiseftirlitið 运营商列表、PeeringDB/Pulse、Farice/SHEFA 海缆更新、本地媒体；每半年 — 超大规模云区域页、Skráseting 公司记录、年报/政策 PDF、认证库；年度 — 按 6 覆盖区域完整负向扫描并与 industry 线对账；事件触发 — EIA、建筑许可、UPS/发电机/电力采购、大用户电网接入、新海缆/PoP、hosting 设施页、收购/品牌变更、政府云/身份平台采购。
- **来源核验**：每记录必含 operator、facility/project 名、locality、division（`Faroe Islands`）、覆盖区域、状态、证据 URL、来源归属；B 级只能证明“该来源如此报道”，设施事实尽量回查 A。
- **不删除纪律**：本目录只允许新增/更新文件，禁止删除或移动任何文件；行业 leads 不得直接入设施表，须先经官方线确认。
