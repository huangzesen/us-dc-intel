---
name: ie-datacenter-methodology
location: scripts/expansion/world/country-skills/IE/SKILL.md
description: |
  Ireland data-center discovery reconciles local-authority planning registers and An Coimisiun Pleanala (ePlan, SID/appeals), EPA IE/IPC licensing (LEAP), CRU/EirGrid grid-connection policy (DCCOPP v3), CSO demand statistics, and IDA announcements with operator/hyperscaler pages and trade press across four provinces (Leinster, Munster, Connacht, Ulster-IE only).
---

# IE · 爱尔兰数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为爱尔兰数据中心/托管设施发现与审计提供可持续、可复现的查询方法论。
> 分区模型：省（province）：Leinster；Munster；Connacht（repo 可拼写 Connaught）；Ulster（仅爱尔兰共和国郡 Cavan、Donegal、Monaghan；北爱六郡属 UK 范围外）。
> 已知种子：AWS eu-west-1（都柏林/德罗赫达等）、Microsoft Azure North Europe/Grange Castle、Google Dublin（2024 新许可被拒）、Meta Clonee、Digital Realty/Equinix/CyrusOne/Pure DC/Echelon/Vantage 都柏林组合、Herbata Naas、Red Admiral Rochfortbridge、Art Data Centres Ennis、CIX Cork、Mayo Killala、Apple Athenry（历史/取消）。
> 本 skill 汇总两份探索报告：官方/监管管线（explorer-official.md）与行业/厂商发现（explorer-industry.md），字段级 A/B/C/U 分级。

## 入口

| 文件 | 管线 |
|---|---|
| explorer-official.md | 官方/监管管线：31 个地方政府规划登记/ePlan、An Coimisiun Pleanala（SID/上诉）、EPA IE/IPC 许可与 LEAP、CRU/EirGrid/ESB Networks 电网、CSO/Oireachtas/gov.ie、IDA、云区域官方页 |
| explorer-industry.md | 行业/厂商发现：运营商页、Digital Infrastructure Ireland/IDCSA/DataCentres Ireland 协会、DCD/RTE/Irish Times/Silicon Republic 等媒体、INEX/CIX、海缆与聚合器 |

## 核心结构事实（框定每次搜索）

1. 爱尔兰**没有单一国家公共数据中心设施登记册**；官方枚举是跨地方规划登记、An Coimisiun Pleanala、EPA 许可、电网政策、政府统计、IDA 公告、云区域页与运营商页的对账任务。
2. 规划以地方政府为基础：**31 个地方政府**（26 郡议会、3 市议会 Dublin/Cork/Galway、2 市郡议会 Limerick/Waterford）；都柏林 4 个规划当局为 Dublin City、Dún Laoghaire-Rathdown、Fingal、South Dublin。大型项目可走 Strategic Infrastructure Development (SID) 或普通申请 + 上诉至 **An Coimisiun Pleanala**（原 An Bord Pleanala，两者名称都要搜；活域 pleanala.ie）。
3. **能源是门槛层**：CRU 2021 框架限制新并网；CRU 于 2025-12-12 发布新数据中心并网政策 **CRU/2025236**；EirGrid 通过 **Data Centre Connection Offer Process and Policy Version 3 (DCCOPP v3)** 实施。CRU/EirGrid 对政策为 A 级，除非公布具名并网记录，否则通常不是设施证据。
4. 大型备用/应急发电的数据中心可能需要 EPA Industrial Emissions/IPC 许可（能源燃烧类别）；EPA/LEAP 是 A 级许可排放基础设施来源，但不是完整数据中心普查。
5. 需求语境：CSO 报告数据中心 2024 年占计量用电 **22%**、2025 年 **23%**（用最新 CSO 发布作背景数字）。
6. 云区域：AWS `eu-west-1` Europe (Ireland)（3 AZ）与 Azure North Europe 为爱尔兰区域（A 级区域存在）；**Google Cloud 与 Oracle OCI 官方公开区域清单中无爱尔兰公共区域**（Google 在爱有自有园区、Oracle Database@AWS Dublin 不等于 OCI 设施）；Meta Clonee 为自有园区而非公共云区域。
7. 验证规则：设施需至少一个 A 来源，或一个点名具体规划决定/参考号并排期 A 来源跟进（可升级计数）的 B 来源；MIC/MVA、合同电网容量、备用发电、IT 负载、营销园区功率**不可互相等同**；按运营商代号去重（Interxion/Digital Realty DUB、Equinix DB、Meta/Facebook、AWS/SPV 别名）；云区域≠设施地址；供应链工厂/海缆/IXP/能源项目≠数据中心；负面省份保留带日期搜索笔记。
8. 监控项（本轮后）：Mayo/Killala 的 ACP 结果、Herbata Naas ACP/JR 状态、Red Admiral Rochfortbridge 上诉状态、Ennis/Naas/Red Admiral 的 EPA 许可、Google Grange Castle 新申请、AWS Drogheda 在建状态、Vantage Dublin 确认位置与规划参考号。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§5 / explorer-industry.md §1-§3）

- 规划登记：`site:eplanning.ie "data centre" "{county}"`；`site:{council-domain} "data centre"`；`site:pleanala.ie "data centre"`；`"An Coimisiun Pleanala" "data centre" "{county}"`
- EPA/LEAP：`site:epa.ie "data centre" "{operator}"`；`site:leap.epa.ie "data centre"`；`"{operator}" "Industrial Emissions" licence Ireland`
- 电网：`site:cru.ie "data centre"`；`site:eirgrid.ie "DCCOPP" "data centre"`；`site:esbnetworks.ie "data centre" connection`
- 政府/统计：`site:gov.ie "data centres" Ireland enterprise strategy`；`site:cso.ie data centres metered electricity consumption`
- 运营商/项目：`"Amazon Data Services Ireland" "Drogheda" planning`；`site:sdcc.ie "data centre" "Grange Castle" OR Google OR Microsoft OR CyrusOne`；`site:meath.ie "data centre" Clonee OR Meta`；`site:kildarecoco.ie "24/60787" OR Herbata`；`site:westmeathcoco.ie "Red Admiral" OR Rochfortbridge`；`site:wicklow.ie Echelon OR Arklow`；`site:clarecoco.ie "Art Data Centres" OR Ennis`；`site:corkcity.ie "data centre" OR colocation`；`site:mayo.ie Killala OR "Mayo Data Hub" OR AVAIO`；`site:donegalcoco.ie "data centre"`
- 贸易媒体/状态：`site:datacenterdynamics.com Ireland data center`；`site:siliconrepublic.com "data centre" Ireland`；`site:rte.ie "data centre" Ireland`；`"{project}" judicial review OR appeal OR refused OR granted`
- 协会/IXP/海缆：`site:digitalinfrastructure.ie data centre`；`site:inex.ie Dublin Cork data centre`；`Ireland submarine cable landing station Dublin Galway`；`"Farice" Galway cable`；`site:peeringdb.com Dublin data center facility`
- 爱尔兰语补充（仅完整性清扫）：`"ionad sonrai" "{county}"`；`cead pleanala`

## 官方/监管管线要点（详见 explorer-official.md）

- 规划登记：国家 ePlan（council 参与度不一，须同时查 council 自有规划页）；An Coimisiun Pleanala 为 SID/上诉/决定 A 级来源。
- 能源：CRU/2025236（2025-12-12）与 CRU/202504 LEU 咨询、EirGrid DCCOPP v3、ESB Networks 配电级材料；政府 enterprise statement 与 Oireachtas 研究为政策语境。
- EPA：IE/IPC 许可搜索 + LEAP 在线登记 + data.gov.ie 开放数据集；EPA 缺失不证明没有数据中心。
- IDA 新闻室对 FDI 公告/就业/资本声称 A 级，物理设施仍须规划/EPA/运营商页交叉核验；ComReg/DPC 仅为电信/数据保护法律语境。
- 已确认官方锚点：AWS 区域文档（A）、Azure North Europe 清单（A）、Meta Clonee 官方位置/信息页（A）、Kildare EIAR 决定清单（A，24/60787，2025-08-20 授予六栋两层数据中心楼）、Lumcloon Red Admiral 项目页（A 级赞助方声称，Westmeath/Rochfortbridge，六单元 + 分布式能源/太阳能）、CIX 官方页（A，Cork/Hollyhill）、IDA Vertiv Letterkenny 发布（A，供应链非数据中心）。
- Apple Athenry 为历史/取消规划标记（B），不计为活跃设施；Cavan/Monaghan/Donegal 无确认大型设施，保留负面搜索笔记。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场结构：大都柏林地区主导（Grange Castle、Clonshaugh/Profile Park、Blanchardstown/Ballycoolin、Citywest/Kilcarbery 及 Meath/Louth/Kildare/Wicklow/Westmeath 溢出）；电网约束把新提案推向都柏林以外。
- 运营商别名规范化：Amazon Data Services Ireland Ltd/AWS、Microsoft/Azure、Facebook/Meta、Interxion/Digital Realty（DUB 代号）、Red Admiral/Lumcloon、Mayo Data Hub/AVAIO。
- 主要信号：Digital Realty 都柏林组合（A 页）、Equinix DB1-DB8（A 页 + DB7x/DB8 规划跟进）、CyrusOne Dublin I（DCD 破土 B 级 74MW）、Pure DC Ballycoolin（A 页）、Echelon DUB20 Arklow（A 公司页 + DCD 破土 B；DUB30/40 观察）、Vantage Dublin（B 级宣布，未确认位置前不计数）、Herbata Naas（A 决定列表 + B 媒体）、Art Ennis（B：2022 授予、2024 ABP/ACP 批准、2026-03 高等法院驳回挑战）、CIX Cork（A）、INEX（A，用其站点种子化设施别名）、Blacknight/Servecentric（小型共置/托管，需设施级核验）。
- 连接性信号不计数：Farice Galway、Aqua Comms/EXA 海缆、MDM Narwhal、INEX/CIX peering。
- 坑：聚合器都柏林设施计数差异大不可比较；云区域是逻辑服务区域非精确设施位置；Google 无 GCP 爱尔兰公共区域；Oracle Database@AWS 不建立 OCI 区域；Ulster 不得纳入 Belfast 等北爱设施。

## 已知设施/项目与证据状态

| 设施/项目 | 分区 | 状态与证据 |
|---|---|---|
| AWS `eu-west-1` 区域 | Leinster（都柏林区） | 运营中；区域文档 A 级（仅区域存在，不用于园区地址） |
| AWS 都柏林区设施（Clonshaugh/Tallaght/Mulhuddart/Ballycoolin） | Leinster | OPER/UC；以 Amazon Data Services Ireland Ltd 规划/EPA 记录为主（A），媒体为 B 线索 |
| AWS Drogheda / Premier Periclase | Leinster（Louth） | PLN/UC；RTE 2020 有条件许可（B）；核验当前 Louth 参考号与上诉状态 |
| Microsoft Azure North Europe / Grange Castle | Leinster（South Dublin） | OPER/扩建；区域清单 A；建筑细节查 South Dublin 规划 |
| Google Dublin / Grange Castle | Leinster（South Dublin） | OPER；2024 新许可被拒（SDCC，B）；无 GCP 爱尔兰公共区域 |
| Meta Clonee | Leinster（Meath） | OPER；Meta 官方位置/info sheet A 级 |
| Digital Realty / Interxion 都柏林组合 | Leinster（Dublin） | OPER/UC；官方页 A；建设时序/发电需规划/EPA |
| Equinix 都柏林组合（DB1-DB8） | Leinster（Dublin） | OPER/UC；官方页 A；DB7x/DB8 状态需规划交叉核验 |
| CyrusOne Dublin I | Leinster（South Dublin） | UC/状态核验；DCD 破土 B（74MW）；SDCC 记录确认 |
| Pure DC Dublin | Leinster（Fingal） | OPER；官方页 A；功率/微电网细节核验 |
| Echelon DUB20 Arklow | Leinster（Wicklow） | UC；官方页 A + DCD 破土 B |
| Vantage Dublin | Leinster（Dublin） | PRO；B 级宣布，位置/规划参考号待确认 |
| Herbata Naas 园区 | Leinster（Kildare） | PLN/上诉中；24/60787 决定 A（2025-08-20，六栋楼）；跟踪 ACP 上诉/JR |
| Red Admiral DC / Rochfortbridge | Leinster（Westmeath） | PLN/上诉中；Lumcloon 项目页 A（赞助方）+ RTE B；核验参考号/条件/上诉 |
| Art Data Centres / Ennis | Munster（Clare） | PLN；2022 授予、2024 ACP 批准、2026 高等法院驳回挑战（B）；核验施工与 EPA 许可 |
| CIX Cork Internet Exchange | Munster（Cork） | OPER；官方页 A；区域共置/IXP 锚点非超大规模 |
| Mayo Data Hub / Killala | Connacht（Mayo） | PLN/上诉中；Western People/Irish Times B（50MW 声称）；核验 Mayo/ACP 决定 |
| Apple Athenry | Connacht（Galway） | HIST；取消/历史标记，不计活跃 |
| Vertiv Letterkenny | Ulster（Donegal） | 供应链（非 DC）；IDA A 级 |
| Cavan/Monaghan/Donegal 清扫 | Ulster（IE） | 无确认大型设施；保留负面搜索笔记 |

## 更新节奏

- 每周：DCD、RTE Business、Irish Times、Business Post、Silicon Republic、The Journal（仅作线索，直到官方记录捕获）。
- 每月：都柏林 x4、Meath、Louth、Kildare、Wicklow、Westmeath、Clare、Mayo、Cork、Offaly 规划登记；运营商页（Digital Realty、Equinix、Pure DC、Echelon、CyrusOne、AWS、Microsoft、Google、Meta、Vantage、Lumcloon）。
- 季度：全部 31 个地方政府、An Coimisiun Pleanala、EPA/LEAP、CRU/EirGrid/ESB Networks、IDA、eTenders；协会/IXP/目录清扫。
- 年度：云区域官方页（AWS/Azure/GCP/OCI/Meta）、CSO 用电统计、Oireachtas 研究、省覆盖审计、过期 B/C 声称。
- 待办（2026-08-12）：Mayo/Killala ACP；Herbata Naas ACP/JR；Red Admiral 上诉；Ennis/Naas/Red Admiral EPA 许可；Google Grange Castle 新申请；AWS Drogheda 在建状态；Vantage Dublin 参考号；codex terra agent 分批复核后按本方法论推进。
