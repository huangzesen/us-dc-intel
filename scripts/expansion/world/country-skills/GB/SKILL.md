---
name: gb-datacenter-methodology
location: scripts/expansion/world/country-skills/GB/SKILL.md
description: |
  United Kingdom (GB/UK) datacenter discovery & audit methodology — how to enumerate, verify, and update UK datacentre projects across 185 repo divisions (nations, regions, counties, boroughs, unitary authorities). The UK has no single national planning-register search for datacentres: enumeration is a local planning authority (LPA) exercise per council, with large projects also surfacing via the NSIP/DCO route (Planning Act 2008 s35 direction), Planning Inspectorate recovered appeals, and grid/power evidence (Ofgem, NESO, DNO open data, substation planning). Datacentres are UK Critical National Infrastructure since Sep 2024 (Ofcom expected as regulator — future operator-registry lead). Read this before running GB exploration/audit batches. Routes to explorer-official.md (planning/grid/cloud/regulator) and explorer-industry.md (trade press/vendor/LPA workflow).
---

# GB · 英国数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：英国**没有**单一全国规划注册搜索库（各议会规划系统不同：Idox/PublicAccess/Civica/Agile 等），设施枚举本质是**地方规划局（LPA）逐议会作业**。
> 大型项目另走 **NSIP/DCO 通道**（2025-10-15 政府书面声明 HCWS966：数据中心可按《2008 规划法》§35 被导向 NSIP 审批），并可通过 **电网/电力证据**（Ofgem/NESO/DNO 开放数据/变电站规划）暴露 MW 与并网时间。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供英国探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：英格兰 LPA 主干（GOV.UK 注册表查询器/Planning Portal/planning.data.gov.uk/GLA Datahub）、Planning Inspectorate NSIP-DCO 与上诉、苏格兰 ePlanning/DPEA、威尔士/北爱门户、Ofgem/NESO/DNO 电网证据、环境许可、云区域官方页（AWS/Azure/GCP/OCI）、运营商官方站点种子、185 division 枚举策略 |
| `explorer-industry.md` | 行业/厂商发现：DCD/The Register/Data Centre Review/techUK/DCA 贸易媒体、运营商扫描（§2 分区域清单）、LPA 工作流与规划文档容量提取、区域开发商地图、按证据分级与状态语义 |

## 核心结构事实（框定每次搜索）

1. **无全国规划注册库**：每个 council 规划注册表各自为政；英格兰有部分中央辅助（planning.data.gov.uk 覆盖不完整，仅作索引）；大型项目走 NSIP/DCO 或国务大臣 recovered appeal（decision letter= A 级）。
2. **2024-09 起数据中心 = 关键国家基础设施（CNI）**：Cyber Security and Resilience Bill 赋予合格运营商通知/安全/韧性义务，Ofcom 预计为运营监管者——未来运营商注册线索，目前不是公开设施普查。
3. **电力是闸门项**：连接队列透明度低于发电注册；查 Ofgem（2024 起打击投机性并网申请）、NESO（TEC register/connections reform）、DNO 开放数据（UKPN/National Grid DSO/SSEN/SPEN/ENWL）、变电站规划申请、环境许可。
4. **云区域=都市级种子（A），非设施证据**：AWS `eu-west-2` London；Azure UK South=London / UK West=Cardiff；GCP `europe-west2` London；OCI UK South (London) / UK West (Newport/Cardiff) + UK 主权区域。种子城市：London/Slough/Hayes/Harlow/Hemel/Cardiff/Newport。
5. **规划用途归类模糊**：数据中心常按 `Use Class B8`（仓储）/`E(g)(ii)`/sui generis 申报；搜 `data centre`/`datacentre`/`data center` + `substation`/`standby generators`/`BESS`/`energy centre` 抓隐藏案例。
6. **容量层级**：IT load MW（规划声明/运营商规格）> 电网 import/MVA（服务上限，非 IT load）> 发电机台数×额定（备用，仅 sanity check）> 建筑面积（无密度假设不可换算，`capacity_mw: null`）。
7. 高密度地理：Greater London+Thames Valley/M4 走廊（Slough/Hayes/Uxbridge/Park Royal/Docklands/Reading/Wokingham/Bracknell）、Hertfordshire/Essex（Harlow/North Weald/South Mimms）、South Wales（Newport/Cardiff/Bridgend）、Northumberland/NE、Yorkshire/Lincs/Humber、Manchester/Stockport、Wiltshire/Corsham、苏格兰中央带。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§4 / explorer-industry.md §3-§5）

- LPA 关键词：`"data centre"` `"datacentre"` `"data center"` `"data hall"` `"hyperscale"` `"substation" "data centre"` `"standby generators" "data centre"` `"Use Class B8"` `"E(g)(ii)"`；状态词：`EIA screening/scoping opinion` `outline/full planning application` `reserved matters` `discharge of conditions` `s73 variation` `prior approval` `committee report` `decision notice`。
- 议会域：`site:{council-domain} "data centre"`、`site:{council-domain} "EIA screening" "data centre"`、`site:{council-domain} "reserved matters" "data centre"`。
- 文档：`filetype:pdf "data centre" ("Design and Access Statement" OR "Planning Statement" OR "Energy Statement" OR "Air Quality Assessment" OR "Environmental Statement") "{division}"`。
- 全国通道：`site:national-infrastructure-consenting.planninginspectorate.gov.uk "data centre"`、`site:gov.uk "section 35" "data centre"`、`site:gov.uk "data centre" "recovered appeal"`。
- 电力：`"{project}" ("MVA" OR "MW" OR "grid connection" OR "substation" OR "132kV")`、`site:ofgem.gov.uk "data centre" "connections queue"`、`site:neso.energy "data centre" "connections"`。
- 行业：`site:datacenterdynamics.com/en/news/ "UK" "data center" "planning"`、`site:theregister.com "UK" "datacenter" "grid"`、`site:datacenterdynamics.com/en/news/ "AI Growth Zone" "data center"`。
- 四国专属：`site:dpea.scotland.gov.uk "Data Centre"`（苏格兰）、`site:gov.wales "data centre" planning`（威尔士）、`site:planningregister.planningsystemni.gov.uk "data centre"`（北爱）、威尔士语 `"canolfan ddata" Newport OR Caerdydd`。

## 官方/监管管线要点（详见 explorer-official.md）

- 英格兰：GOV.UK planning-register finder（邮编→正确议会）、Planning Portal LPA finder（division→council 路由）、planning.data.gov.uk（部分索引）、GLA Planning London Datahub（伦敦全域发现层，再开 borough 注册表）。
- NSIP/DCO：Planning Inspectorate National Infrastructure “Find a project” 搜 `data centre`；HCWS966 §35 方向、DCO 案例、appeal/call-in、国务大臣决定函均为 A 级。
- 苏格兰 ePlanning + DPEA case search；威尔士 Planning Applications Wales + Welsh Government 决定；北爱 central Planning Portal（planningregister.planningsystemni.gov.uk）。
- 电力/环境：Ofgem data-centre connection reforms、NESO Data Portal/TEC register、ENA connections data、DNO 开放数据；大型发电机组群触发环境许可/空气质量/噪音证据（EA/SEPA/NRW/NIEA + 议会文件）。
- 运营商种子（A=存在）：Equinix（Docklands/Slough/Manchester）、Digital Realty（Docklands/Slough/Crawley）、VIRTUS（Slough/Hayes/Stockley Park/Enfield/Park Royal）、Ark（Corsham/Farnborough）、Kao（Harlow/Slough/Northolt）、Telehouse、NTT（Hemel Hempstead）、Colt DCS、Yondr、CyrusOne、Pulsant、iomart、nLighten、Stellium（Cobalt Park/North Tyneside）；Companies House 查 SPV。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 贸易媒体：DCD UK（最佳开放发现流，B→A 仅当链接一手文件）、The Register（B，政策/电网/AI Growth Zone）、Data Centre Review（B）、techUK Data Centres Programme（B）、DCA（B/C）、Data Centre World（C，厂商发现）、Planning Resource（B，上诉/绿带）、本地商业媒体（B/C）。
- 目录：Cloudscene/DataCenterMap/Baxtel/OCOLO/Inflect/Colo-X = C/B（运营型 colo 普查与地址有用，容量须核实）。
- 已知项目参考（示范）：Manor Farm/Tritax 147MW Slough（**P/10076/013**，GOV.UK recovered appeal ref **3366043**）；DC01UK/Equinix South Mimms（Hertsmere **24/1152/OUTEI**，2025-01-23 outline 获批）；Elsham Tech Park（North Lincolnshire **PA/2025/643**，2026-03 outline）；Google North Weald（Epping Forest DC，2025-12-10 outline）；Kao Harlow 园区；Ark Spring Park DC7（Wiltshire **PL/2024/05527**）。
- 状态语义：`announced`（新闻稿/MoU/AI Growth Zone bid，无申请）=不计数；`planned`=已提交申请；`approved`=许可/DCO 获批；`construction`=条件解除/施工管理计划/EPC；`operational`=运营商上线/云服务页/commissioning；`rejected/cancelled`=拒批/撤回/取消/过期。
- AI Growth Zone ≠ 数据中心：是政策/选址赋能 designation；须具名场地+开发商才计 C 以上。

## 来源分级

- **A** = 官方/一手：议会规划注册表申请/委员会报告/决定通知/EIA 筛选-scoping/获批图纸；Planning Inspectorate NSIP-DCO 项目页、国务大臣决定函、上诉监察报告；Ofgem/NESO/政府文件（具名项目时）；云厂商官方区域文档（区域存在）；运营商官方设施页（存在；容量 A-/B 视具体度）；上市公司年报/投资者披露。
- **B** = 强二级：DCD、The Register、Data Centre Review、Computer Weekly、Construction Enquirer、本地商业媒体、规划法律笔记、council news/委员会纪要（A-/B+）；仅当链接并核对一手规划文档时可升级。
- **C** = 弱/未验证：DataCenterMap/Baxtel/DC Atlas/Colo-X/OCOLO（字段级 B/C）、地方活动地图、LinkedIn、纯 PR 公告、顾问博客；无一手链接的目录容量不计。
- 状态与容量规则：全园区远期 MW 仅当源明确为 planned capacity 才计入；否则记分期 MW 并在 notes 标注可能扩展；London 都市营销名（Slough/Harlow/Hemel/Crawley/Newport/Reading）按物理 LPA/division 归桶。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=GB，divisions=185：nation+region+county+borough+unitary）。
2. 将 division 映射到 LPA/注册表：拆分国家前缀，识别 lower-tier LPAs（如 Essex 含 Harlow/Basildon/Chelmsford/Thurrock/Southend）。
3. LPA 注册表关键词扫（data centre/datacentre/data center/data hall/hyperscale/substation/generators）→ 议会域+PDF 模板 → 捕获申请号、申请人/SPV、地址、楼面、IT load MW、import MVA、发电机、变电站、分期、决定日期。
4. 全国通道：Planning Inspectorate §35/DCO、GOV.UK recovered appeals/call-ins（绿带被拒项目可能被国务大臣批准）。
5. 电网/环境：Ofgem/NESO 上下文、DNO 开放数据、能源声明、环境许可。
6. 云+colo 官方页做种子，再把每个运营商/园区名 pivot 回规划记录；贸易媒体/目录仅用于发现与补缺。
7. 去重：按地址/校园+阶段，注意运营商沿革（NGD=Vantage、Telecity=Digital Realty、4D=Redcentric/Stellanor）。输出 world 同 schema；规划参考号记入 notes；无设施级证据输出 `no_projects: true`（普通办公室服务器房/电信机柜/机房翻新不计）。
8. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12 02:08Z）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：50× codex terra agent（max thinking）每 agent 分批复核英国数据中心（division→LPA→规划验证）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：CNI/Cyber Security Bill 监管细则（Ofcom 注册）落地时间；NSIP §35 首批数据中心 DCO 案例；QTS Cambois、Google Thurrock、Microsoft Eggborough 等大型项目的规划/电力进度；NE 部分项目可能暂停或更换赞助方。
