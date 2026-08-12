---
name: je-datacenter-methodology
location: scripts/expansion/world/country-skills/JE/SKILL.md
description: 泽西岛数据中心双线查询方法论（官方/监管/云管线 + 行业/厂商/媒体发现），含 division 模型、来源分级与查询模板；Jersey datacenter dual-line discovery methodology (official/regulatory/cloud pipeline + industry/vendor/media discovery) with division model, source grading and query templates. 运行 JE 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。
---

# JE · 泽西岛数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为泽西岛（Jersey, JE）数据中心枚举/审计批次提供官方与行业双线发现方法。官方线（explorer-official.md）覆盖泽西州政府、规划审批、议会记录、JFSC 注册处、JCRA 电信牌照、Jersey Electricity 电网与运营商一手设施页；行业线（explorer-industry.md）覆盖运营商、行业媒体、本地媒体与目录发现。两线交叉核验，按 A/B/C 分级入库；目录和营销页只能播撒，不能作为最终普查证据。

## 入口

| 文件 | 职责 | 内容概要 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | Government of Jersey（gov.je 规划/采购/政府文件）、States Assembly 议会记录、JFSC 注册处（jerseyfsc.org/registry.jfsc.je）、JCRA 电信牌照（jcra.je）、Jersey Electricity 电网（N3/变电站/互联）、运营商一手设施页（JT Data Centre Services、JT Five Oaks/Rue Des Pres PDF、Sure Jersey Data Centre）、官方云区域页排除表 |
| explorer-industry.md | 行业/厂商/媒体发现 | 优先运营商/设施种子（JT、Sure、Digital Jersey）、目录/聚合源（DataCenterMap、Data Center Platform、Cloudscene、Datacenters.com、Colomap/Upstack）、行业与本地媒体（DCD、Capacity、Computer Weekly、Jersey Evening Post、Bailiwick Express、BBC Jersey、Digital Jersey news）、教区搜索矩阵、核心证据链、容量提取规则 |

## 核心结构事实

1. **Division 模型**：manifest 已核验 `country_code: "JE"`，`subnational_type: "country"`，`divisions: ["Jersey"]`。唯一枚举分区为 Jersey；教区（parish）和工业区只作岛内定位字段，不作 manifest 分区。
2. **政治与市场形态**：泽西是英国王室属地（Crown Dependency），有独立政府、法律和规划体系，不使用英国本土 Planning Portal；官方入口为 gov.je。市场小，需求主要来自金融服务、信托/基金、政府 ICT、灾备、iGaming/数字业务和本地企业托管。
3. **岛内定位**：建议记录 12 个教区——St Helier、St Saviour、St Clement、Grouville、St Martin、Trinity、St John、St Mary、St Ouen、St Peter、St Brelade、St Lawrence；高产出地理锚点：St Helier（商业中心、La Collette/South Hill/Queen's Road）、St Saviour（Five Oaks、Rue des Pres/Longueville 一带）、St Peter（机场/工业区）、Grouville（N3 电力登陆）、St Brelade/St Ouen（海岸和潜在海缆线索）。
4. **法律与监管**：JCRA（jcra.je）说明在 Jersey 运行全部或部分电信系统需要 JCRA 牌照；牌照清单列 JT (Jersey) Limited（Class III Telecoms licensee）、Sure (Jersey) Limited（Class II）、Jersey Electricity PLC、BT Jersey Limited、Home Net Limited、Newtel Limited、Starlink Internet Services Limited 等；牌照证明通讯运营资格，不单独证明数据中心设施。JFSC 注册处（jerseyfsc.org / registry.jfsc.je / sir.jerseyfsc.org）用于验证运营商、项目 SPV、托管服务公司和金融服务客户的法律实体名称、注册号和状态——实体证据不是设施证据，注册地址/持牌地址不得直接当作数据中心地址。
5. **电力与互联**：Jersey Electricity（jec.co.uk / jerseyelectricity.com）负责电网、互联和大型用户供电；Normandie 3 从法国 Périers/Armanville Beach 到 Grouville Bay，再通过 Jersey 陆缆到 St Helier South Hill Switching Station；互联容量、La Collette 发电站、South Hill switching/substation、Queen's Road/Rue des Pres 变电站是供电可行性线索，不得折算为数据中心 IT MW。
6. **设施/项目种子（2026-08 证据状态）**：JT 官方页确认 Channel Islands 数据中心服务，JT 产品说明书确认 **Five Oaks Data Centre** 与 **Rue Des Pres Data Centre**（A 级设施存在/技术属性）；Sure 官方页确认 **Jersey Data Centre**，标称 Tier III 和 500 kW IT load（A）；JT First Tower Lane Data Centre 经目录和 JT 资料上下文核为 Guernsey/St Peter Port 线索，不属于 JE，必须作为 Jersey/Guernsey 混淆排除项；目录中的 JT Central/JT East/Telephone House 等为 C 级种子，须确认是数据中心、exchange、office 还是目录误报。
7. **语言与词汇**：搜索以英文为主，关键词含 "data centre"/"datacentre"/"data center"、colocation、server room、telecoms exchange、generator、UPS、substation、cooling plant、change of use、planning application、tender、WAN、migration；注意 `Jersey` 极易混入美国 New Jersey——查询加入 `Channel Islands`、`site:.je`、`"St Helier"`、`"St Saviour"` 或排除 `-"New Jersey"`；`JE` 缩写同时可能表示 Jersey Electricity、泽西国家代码和地址邮编片段，搜索使用全称消歧。
8. **可靠性分级**：A = 官方/一手来源（gov.je 规划/采购/政府文件、States Assembly 正式记录、JFSC 注册处、JCRA 牌照清单、Jersey Electricity 官方资料、JT/Sure 等运营商官方设施页或产品说明书、AWS/Azure/GCP/OCI 官方区域列表用于排除）；B = 可靠二手来源（DCD、Capacity Media、Computer Weekly、本地信誉媒体 Jersey Evening Post、Bailiwick Express、BBC Jersey 或带具名当事方的公司新闻转载）；C = 目录/聚合/营销来源（DataCenterMap、Cloudscene、Datacenters.com、Data Center Platform、Colomap、Upstack、经销商 VPS/hosting 页）。
9. **计数与去重规则**：设施存在性优先级——运营商设施页/PDF、规划许可、政府或监管文件 > 行业媒体 > 目录；地址可信度单独评估（运营商页面不披露地址时，地址即使来自目录也只能标注为目录来源，直到 gov.je/运营商/JFSC/JCRA 或其他一手材料确认）；容量字段只记录披露值（Sure 官方 `500 kW IT load` 可记 0.5 MW；JT PDF 的 rack power、generator kVA、cooling kW 只能作代理指标，不能自行折算成 IT MW；不用 rack count × 2 kW 生成 IT MW，不把 Tier III/ISO 27001/SOC/PCI-DSS 当容量）；status `operating` 需要运营商现行页面、最新 PDF、许可或可靠媒体确认，旧 PDF/旧目录用当前页面复核；排除项：Guernsey 设施、New Jersey（美国）设施、总部/办公室、cloud reseller、VPS、telecom mast、substation-only 均不得计作 JE 数据中心。

## 常用查询模板

```text
"data centre" site:gov.je
"planning application" "data centre" "Jersey"
"tender" "data centre" site:gov.je
"data centre" site:statesassembly.gov.je
"Five Oaks" "data centre" site:statesassembly.gov.je
"JT (Jersey) Limited" site:jerseyfsc.org
site:jcra.je "licences in issue" "JT (Jersey) Limited"
site:jcra.je "Sure (Jersey) Limited" "Class II"
site:jec.co.uk "data centre" OR "data center"
"Normandie 3" "Grouville Bay" "South Hill"
site:business.jtglobal.com "Five Oaks" "Data Centre"
site:business.jtglobal.com "Rue Des Pres" "Data Centre"
"Sure" "Jersey Data Centre" "500kW"
site:business.sure.com "Jersey Data Centre"
site:datacenterdynamics.com/en/news/ "Jersey" "data centre"
site:jerseyeveningpost.com "Five Oaks" "data centre"
site:bailiwickexpress.com "JT" "data centre" "Five Oaks"
"{parish}" "Jersey" "data centre" -"New Jersey"
site:gov.je "{parish}" "data centre"
site:datacentermap.com/jersey/ "{operator}"
"JT Five Oaks" "generator" "560 KVA"
"Jersey" "data centre" "700 racks"
"Jersey" "data centre" "Channel Islands" -"New Jersey"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **gov.je 规划/采购/政府文件**：Government of Jersey（gov.je）Planning and building 与 Current planning applications 是规划入口；数据中心新建、扩建、备用发电机、冷却设备、变电站、大型 ICT 机房改造、Change of Use 通常会留规划申请或配套环境/噪音材料；政府采购（tenders.gov.je / Proactis 与 gov.je registering tender opportunities）可能披露政府数据中心迁移、托管、WAN、云服务或机房运维合同；gov.je 文件中已有历史线索（JT 2010 年报提到 Five Oaks 扩建、Rue des Pres 新数据中心、Channel Islands 数据托管能力），执行轮保存 PDF URL、页码和摘录。
- **规划记录提取字段**：申请编号、申请人、业主、SPV、地址、教区、地块编号；描述中的 data centre、server room、telecoms exchange、generator、UPS、substation、cooling plant、change of use；状态 submitted/approved/refused/withdrawn/superseded；设施属性：面积、机柜/数据大厅、发电机容量、燃油储量、冷却、噪音、运行时间、供电连接。
- **States Assembly**：statesassembly.je（旧/兼容域 statesassembly.gov.je 常见于历史材料）——质询、部长决定、Scrutiny 报告和国有/半国有公司材料可能披露 JT、Jersey Electricity、政府 ICT 迁移、海缆、供电和韧性项目；对国有或政府参股主体，States Assembly/gov.je 附件可作 A 级项目背景，但若只描述服务市场，不自动证明具体物理地址。
- **JFSC 注册处**：验证运营商、SPV、托管公司和金融客户的实体；实体证据不是设施证据；注册地址/持牌地址不得直接当数据中心地址。
- **JCRA 电信牌照**：牌照清单（jcra.je/regulated-sectors/telecommunications/licences-in-issue/）列 JT (Jersey) Limited 为 Class III、Sure (Jersey) Limited 为 Class II；牌照证明运营资格不证明设施。
- **Jersey Electricity**：N3 官方项目页（jec.co.uk/about-us/projects/normandie-3/）是电网背景和登陆/路由线索；供电可行性与互联容量不得折算为数据中心容量。
- **运营商一手设施页**：JT Data Centre Services（business.jtglobal.com/products/cloud/data-centres/）、JT Five Oaks/Rue Des Pres 2025 与 2020 产品说明书 PDF、Sure Jersey Data Centre（business.sure.com）为 A 级设施存在和技术属性证据；从 PDF 记录 evidence_date、页码、Tier、UPS、generator、cooling、rack power；Sure 页面不披露街道地址时，地址用 Sure 联系页、JCRA、目录或规划记录交叉核实后记录。
- **官方云区域页排除**：AWS/Azure/GCP/OCI 官方区域/地理列表均未列 Jersey；本地 MSP、VPS、private cloud、offshore cloud 页面不得升级为 AWS/Azure/GCP/OCI Jersey region，只能作本地托管/云服务线索。
- **全分区覆盖流**：对 Jersey 做全岛关键词扫描（gov.je、statesassembly、JCRA、JFSC、Jersey Electricity、JT、Sure、Digital Jersey）；用 12 教区作定位矩阵而非分区；先以运营商官方页确认服务/设施存在，再回到 gov.je 规划、JCRA/JFSC、Jersey Electricity 或目录交叉确认地址；对 JT Five Oaks、JT Rue Des Pres、Sure Jersey Data Centre 专项核验；对 JT First Tower Lane、Guernsey Sure/C5 等反向排除；新项目记录状态和审批编号，未开工或仅采购服务的项目不得写作 operating facility；输出时 division 固定为 Jersey，parish 作补充字段。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **优先运营商与设施种子**：JT Data Centre Services（A 服务存在性，Jersey + Guernsey 总体服务页，不单独给街道地址）→ JT Five Oaks Data Centre（A 设施存在/技术属性，St Saviour/Five Oaks 地址待一手交叉）→ JT Rue Des Pres Data Centre（A 设施存在/技术属性，St Saviour/Rue des Pres 地址待一手核验）→ Sure Jersey Data Centre（A 设施存在与 500 kW IT load，Tier III/24h security/data halls/cages/inter-island connectivity，Queen's Road/St Helier 地址待交叉）→ JCRA 运营商名单（A 运营资格）→ Digital Jersey（A/B 行业定位，说明网络和基础设施环境，不证明具体设施）→ Jersey Electricity N3（A 电网背景）→ JT First Tower Lane（A/C 排除项，Guernsey/St Peter Port，由 JT 运营但非 JE）。
- **目录与聚合源**：DataCenterMap Jersey（JT Five Oaks、JT Rue Des Pres、Sure Jersey 地址线索，页面可能限流）、Data Center Platform、Cloudscene（注意可混入 USA Jersey）、Datacenters.com（搜索经常转向 New Jersey USA）、Colomap/Upstack——只用于播撒名称、地址和相邻设施，不能直接计数。
- **目录到一手验证工作流**：从目录提取设施名/运营商/地址/教区/容量认证声明 → 用 facility + operator + site:operator-domain 搜运营商官方页或 PDF → 用精确地址搜 gov.je planning/register、Jersey Gazette、States Assembly → 用 JCRA 确认持牌、JFSC/registry 确认法律实体 → 目录声明若无法被一手证据支持，保留 C 级并写明缺口。
- **行业与本地媒体**：DCD（Channel Islands/运营商/投资/M&A/colocation）、Capacity Media（JT/Sure/海缆/批发网络）、Computer Weekly（政府 ICT/托管/云迁移/灾备）、Jersey Evening Post（本地规划、JT/Sure/Jersey Electricity、政府数据中心迁移）、Bailiwick Express（本地商业，已见 JT Five Oaks 投资/SOC 线索）、BBC Jersey（本地公共报道；BBC 地区 URL 会变化，执行时用搜索页或站内搜索定位具体报道）、Digital Jersey news（本地技术公司和 managed data centre case studies，B/A-mixed 按作者和事实类型区分）。B 级媒体可确认项目名、投资额、历史时间线和当事方声明；媒体引用运营商原话但没有链接原文时仍保持 B，直到找到运营商/政府源；本地媒体中 data centre 可能指政府办公室机房或迁移项目，需区分 facility、tenant migration、cloud migration。
- **教区搜索矩阵**：manifest 只有 Jersey，执行轮仍按教区扫描避免漏掉低调设施；重点地名模板含 Five Oaks、La Grande Route De St Martin、Rue des Pres、Longueville Road、La Rue des Fonds、Queen's Road、The Powerhouse、Minden Place、La Collette、South Hill、Grouville Bay；矩阵优先级：St Saviour（JT 双设施，高）、St Helier（Sure + 可能的 JT Central/Telephone House/Queen's Road/La Collette/South Hill，高）、St Peter（机场/工业区，中）、St Brelade/St Ouen（海缆候选，低-中）、其余教区 broad scan only，require strong evidence。
- **核心证据链**：①JT 官方页确认 purpose-built data centres/co-location/data hosting（A）②JT Five Oaks 产品说明书确认具体设施和技术属性（A，地址需交叉）③JT Rue Des Pres 产品说明书（A，核验地址写法）④Sure 官方 Jersey Data Centre 页确认 Tier III 与 500 kW IT load（A，Queen's Road/Powerhouse 地址来源单独标注）⑤JCRA licences 确认运营资格（A，不是设施验证）⑥gov.je/JT 年报提及 Five Oaks 扩建、Rue des Pres 新建、700 racks、Project Liberty（A，历史容量/投资背景，需用当前运营商页面确认 operating）⑦目录显示地址（C，只作地址/别名 seed）⑧Digital Jersey 与本地媒体显示 managed data centre 用例（B 或 A/B，需求侧背景不直接新增设施）。
- **容量与属性提取**：可直接记录——Sure `500 kW IT load` → capacity_mw 0.5（保留原文字段和 URL）；JT PDF 的 rack sizes、rack power、power increments、UPS autonomy、generator backup、cooling kW、Tier/ISO/PCI/SOC → capacity_notes 或技术属性；gov.je/JT 年报 `700 racks`、投资额、扩建/新建时间线 → 历史规模信号注明年份。不可推算——rack count × 2 kW、cooling kW、generator kVA、Jersey Electricity interconnector MW、Tier III/认证。
- **最终输出建议**：每条候选设施记录 division: Jersey、parish、operator、facility_name、address、address_source_url、facility_source_url、facility_evidence_grade、address_evidence_grade、status、capacity_mw、capacity_original、capacity_notes、exclusion_reason、last_verified_date；最小候选清单：JT Five Oaks（A seed）、JT Rue Des Pres（A seed）、Sure Jersey Data Centre（A seed）、JT First Tower Lane（排除，Guernsey）、目录中 JT Central/JT East/Telephone House（C seed 须确认类型）。

## 维护注意（更新纪律）

- **更新节奏**：批次运行时以检索当日为准更新证据日期与状态；旧 PDF/旧目录用当前页面复核 status；历史规模信号（700 racks 等）注明年份。
- **来源核验**：每个设施条目保留一手来源 URL 与分级；地址可信度单独评估；目录声明无法被一手证据支持时保留 C 级并写明缺口；新项目记录状态和审批编号，未开工或仅采购服务的项目不得写作 operating facility。
- **不删除纪律**：本目录只新增/更新 SKILL.md、ANATOMY.md 与探索产物，禁止删除/移动任何现有文件（explorer-official.md、explorer-industry.md 与历史证据保留为原始记录）。
