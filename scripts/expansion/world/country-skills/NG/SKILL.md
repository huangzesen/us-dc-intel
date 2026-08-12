---
name: ng-datacenter-methodology
location: scripts/expansion/world/country-skills/NG/SKILL.md
description: |
  Nigeria (NG) datacenter discovery & audit methodology — how to enumerate, verify, and update Nigeria datacenter projects at state + FCT granularity (36 states + Abuja Federal Capital Territory in the current manifest). Nigeria has no single national public datacenter registry: enumeration joins state/FCT development permits and building control (LASPPPA/LASBCA/LASIMRA, FCTA), Federal Ministry of Environment/EAD EIA disclosures, NCC licence/register entries (Collocation/Infrastructure, International Data Access, cable landing, Infraco regions), NERC captive-power permits and MYTO/customer orders (Rack Centre NERC/CPG/165 10 MW Oregun, Open Access Data Centre CPG/177 3.20 MW Ikate Elegushi, MTN switches), official cloud-region/edge pages (AWS Lagos Local Zone af-south-1-los-1a is a strong seed; no NG Region for Azure/GCP/OCI), Uptime certifications, government digital sources (NITDA, Galaxy Backbone Tier III Abuja / Tier IV Kano), and operator pages (Equinix/MainOne/MDXi LG1-LG3 + PR1 Port Harcourt, Rack Centre LGS2, Africa Data Centres LOS1, OADC/WIOCC Lagos 7,200 sqm/24 MW + Equiano landing, Digital Realty/Medallion, Kasi Cloud Lekki + DNEK Eket, MTN, Airtel/Nxtra, 21st Century/ipNX/Cyberspace/inQ/NTT). Lagos-led market; press stage language (announces/MoU/groundbreaking) is lead-only until permit/NERC/NCC/Uptime/operator confirmation. Read this before running NG exploration/audit batches. Routes to explorer-official.md (NCC/planning/EIA/NERC/government-cloud/cloud-edge/Uptime/seeds/states) and explorer-industry.md (trade press/operators/cloud-IXP-subsea/state matrix/aggregators/validation).
---

# NG · 尼日利亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：尼日利亚**没有**统一的全国数据中心注册库；枚举靠**拼接**：州/FCT 开发许可与建筑管控、联邦环境部/EAD 环评披露、NCC 通信牌照、NERC 自备发电许可与 MYTO/客户馈线命令、云区域/边缘官方页、官方运营商页与 Uptime 认证。
> 法定规划单元通常是**州或 FCT**，但实际选址以城市/地方优先：Lagos、Lekki、Victoria Island、Eko Atlantic、Ikoyi、Ikeja、Oregun、Yaba、Abuja、Kano、Port Harcourt、Eket、Sagamu、Atakobo、Calabar、Makurdi、Aba、Umuahia、Enugu、Ibadan、Kaduna、Benin City。
> 市场 **Lagos 主导**；次级：FCT Abuja、Rivers/Port Harcourt、Kano、Ogun/Sagamu-Ijebu East、Akwa Ibom/Eket、Cross River/Calabar、Benue/Makurdi 与若干州政府 ICT/数据中心。
> 拼写双搜 `data centre`/`data center`/`datacentre`；官方记录基本为英语（约鲁巴/豪萨/伊博语只辅助州政府 ICT 宣传，须英语官方文件核实）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供尼日利亚探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：NCC 牌照清单与类别（Collocation/Infrastructure、International Data Access、电缆登陆、Infraco 区域）、州/FCT 规划与建筑管控（LASPPPA/LASBCA/LASIMRA、FCTA development control、各州规划部）、EAD/联邦环境部 EIA 披露、NERC 自备发电 CSV 与 MYTO 命令、NITDA/联邦数字政府/Galaxy Backbone 政府云、云区域与边缘信号（AWS Lagos Local Zone af-south-1-los-1a）、Uptime 国家清单、官方/运营商设施种子表、逐州枚举策略与优先级簇、证据提取清单 |
| `explorer-industry.md` | 行业/厂商发现：DCD/TechCabal/Technext/TechAfrica News/BusinessDay-Guardian-Punch-ThisDay-Vanguard/Capacity Media/Africa DCA 媒体、IXPN/PeeringDB/PCH/海缆（MainOne/Equiano/2Africa/Glo1/ACE/WACS/SAT-3）互联、运营商/开发商种子表（Equinix-MainOne-MDXi/Rack Centre/ADC/OADC-WIOCC/Digital Realty-Medallion/Galaxy Backbone/Kasi Cloud/MTN/Airtel-Nxtra/21st Century/ipNX/Cyberspace-inQ-NTT/Tetracore-Huawei/UniCloud-Benue/Nugi-9mobile）、云/边缘/IXP/海缆发现、州级行业矩阵（优先州/次州组）、聚合器规则与父/子公司变更、最终验证清单 |

## 核心结构事实（框定每次搜索）

1. **NCC = 运营商/服务证据（A），非设施注册表**：牌照类别含 Collocation/Infrastructure、Infrastructure Sharing and Co-location、International Data Access、International Cable Infrastructure & Landing Station、ISP、Interconnect Exchange、NLD、Unified Access、区域 Open Access Fibre Infraco；高产量名字：MainOne、Equinix、MDXi、MainData、Teleafrica/Medallion、Digital Realty、Rack Centre、OADC、WIOCC、ADC、MTN、Airtel、Nxtra、Galaxy Backbone、21st Century、ipNX、Cyberspace、inQ.Digital、NTT、Broadbased、Zinox、Fleek、Raeanna、Oodua Infraco；Infraco 牌照地理（Lagos、FCT、North West/East/South East/South South/South West）提供州级光纤与边缘 DC 线索。
2. **NERC 自备发电（A=电力许可/客户证据，B/A-=设施推断）**：公共 CSV 有 `Rack Centre Limited`（NERC/CPG/165，10.00 MW，18 Jagal Close，Oregun，Lagos）、`Open Access Data Centre Limited`（NERC/CPG/177，3.20 MW，Plot 99/100 Silverbird Road，Ikate Elegushi，Lagos，2023-12-04）、多个 MTN switch/DC 相关许可（Ojota/Ibadan/Enugu/Abuja/Apapa/Kano/Kaduna/Uselu）；捕获 MW 是发电容量/站点负荷/承诺电力/IT load。
3. **EIA（EAD）**：大 DC 可能经土地开发、柴油/燃料库、燃气电站、变电站、冷却/取水、电信/安全基础设施、工业园/能源园出现而非 “data centre” 类别；EAD 上传含 TCN、Medallion DC、MainOne、WIOCC、MTN、Airtel、GBB、Meta 与光纤/电力参与者；提取 EIA 登记号、proponent、坐标/地块、LGA/州、组件、柴油/燃气/储存、电站/变电站链接、披露日期、批准状态。
4. **州/FCT 规划**：无全国规划许可门户；经州/FCT 物理规划当局与建筑管控机构；Lagos 用 LASPPPA/LASBCA/LASIMRA（电信管道/桅杆/光纤）、FCT 用 Department of Development Control/AMMC/FCTA；提取州/LGA/镇、地块、街道/工业园/SEZ、申请人/SPV、开发描述、面积/层数/机房数、进口 MVA/MW、发电机/燃料库、水/冷却需求、批准/检查/入住状态。
5. **政府数字源**：NITDA（国家数据战略、云优先、IT 服务商清单）、联邦通信部、Galaxy Backbone（官方 FAQ：Abuja Tier III + Kano Tier IV 数据中心）；州政府数据中心采购与共享服务；`National Shared Services Centre`/`Government Cloud` 线索。
6. **云/边缘（负面核查 + 强种子）**：AWS 官方 Local Zones 文档列出 `Nigeria (Lagos)` Local Zone `af-south-1-los-1a`（父区域 af-south-1）——强 Lagos 种子，是 Local Zone/边缘而非完整 AWS 区域；Azure/GCP/Oracle 官方列表无 NG 区域（NCC 敦促 Microsoft 深化=政策/需求线索；Google Equiano 海缆=边缘/海缆种子）。
7. **Uptime（A=认证存在/设施名/运营商）**：国家清单含 Galaxy Backbone Abuja/Kano、GTBank Lagos、Lagos State Data Centre、MainOne Lekki/LG02、MTN Ojota 等；设计级认证不证明运营状态。
8. **运营商种子（A=官方存在/当前足迹，状态须加入州/FCT 规划、EIA、NCC、NERC、Uptime 联合确认）**：Equinix/MainOne/MDXi（Lagos/Lekki LG1-LG3，Equinix 页说 Lagos 三个 IBX；2025-04 PR1 Port Harcourt + 2Africa）、Rack Centre（LGS2 页：12 MW IT power、25 MVA utility、六个 2 MW 机房；NERC CPG 18 Jagal Close Oregun）、ADC（LOS1 Eko Atlantic）、OADC/WIOCC（官方页 7,200 sqm 技术空间、24 MW 站点负荷、Equiano 登陆站角色）、Digital Realty/Medallion（Victoria Island/Lekki）、Galaxy Backbone（Abuja Tier III/Kano Tier IV）、Kasi Cloud（Lekki LOS + Eket DNEK，NSIA 动土）、MTN（电信 switch/DC 多处）、Airtel/Nxtra（Eko Atlantic 线索）、21st Century/ipNX/Cyberspace/inQ/NTT（较小企业/边缘）。
9. **状态词**：`announces/signs MoU/plans/proposes/groundbreaking`=线索；`land acquired/tender/EIA disclosure/NERC-CPG/building permit`=场地/采购；`commissioned/launched/opened/Uptime constructed facility/customer live`=投运；MoU/新闻线索至少一条一手源（运营商页/Uptime/许可/NERC/NCC/投运页）才升级；州 ICT 房、统计数据中心、指挥中心、银行 DC、电信 switch 无托管/colo 服务证据不得升为商业 colo。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§3 / explorer-industry.md §1/§4）

- NCC：`site:ncc.gov.ng "data centre" Nigeria`、`site:ncc.gov.ng "Collocation/Infrastructure" "{operator}"`、`site:ncc.gov.ng "International Data Access" "{operator}"`、`site:ncc.gov.ng "Open Access Fibre Infrastructure Network" "{state}"`、`site:ncc.gov.ng "Galaxy Backbone" "data centre"`。
- 规划：`site:lagosstate.gov.ng "data centre" "planning permit"`、`site:lasbca.lagosstate.gov.ng "data centre"`、`site:fcta.gov.ng "data centre" Abuja`、`site:{state-domain} "physical planning" "data centre"`、`site:lagosstate.gov.ng "Kasi Cloud" "groundbreaking"`。
- EIA：`site:ead.gov.ng/wp-content/uploads "data centre"`、`site:ead.gov.ng/wp-content/uploads "{operator}" "Environmental Impact Assessment"`、`"{project}" "EIA" Nigeria "data centre"`。
- NERC/电网：`site:nerc.gov.ng "Rack Centre"`、`site:nerc.gov.ng "Open Access data centre"`、`site:nerc.gov.ng "MTN Nigeria" "Switch"`、`"{operator}" "captive power" "data centre" Nigeria`、`"{project}" "33kV" "data centre" Nigeria`。
- 政府云：`site:nitda.gov.ng "Galaxy Backbone" "data centre"`、`site:galaxybackbone.com.ng "Abuja" "Kano" "Tier"`、`site:{state-domain} "state data centre"`。
- 云/边缘：`"AWS Local Zone" Lagos Nigeria "af-south-1-los-1a"`、`site:docs.aws.amazon.com "Nigeria (Lagos)" "Local Zone"`、`site:learn.microsoft.com Azure Nigeria "region"`、`site:oracle.com Nigeria "cloud region"`。
- Uptime：`site:uptimeinstitute.com/uptime-institute-awards/country/id/NG "{operator}"`、`site:uptimeinstitute.com "Kano" "Galaxy Backbone"`、`site:uptimeinstitute.com "Lagos State Data Centre"`。
- 行业：`site:datacenterdynamics.com/en/news/ Nigeria "data center" "MW"`、`site:techcabal.com Nigeria "data centre" Lagos`、`site:techafricanews.com Nigeria "data centre" "{state}"`、`site:businessday.ng Nigeria "data centre" Lagos`、`site:guardian.ng Nigeria "data centre" "{state}"`。
- 互联/海缆：`site:ixp.net.ng "data centre"`、`"IXPN" "Rack Centre" OR "MainOne" OR "OADC" OR "Medallion"`、`"Equiano" "OADC Lagos" "data centre"`、`"2Africa" "Port Harcourt" "data center" Equinix`、`"MainOne cable landing station" "Lekki"`。
- 优先簇：`"Lekki" Nigeria ("MainOne" OR Equinix OR OADC OR Kasi) "data centre"`、`"Oregun" Lagos "Rack Centre" "NERC/CPG"`、`"Eko Atlantic" Lagos ("Africa Data Centres" OR Nxtra)`、`"Port Harcourt" Nigeria Equinix PR1`、`"Kano" "Galaxy Backbone" "Tier IV"`、`"Eket" "Kasi Cloud"`、`"Makurdi" Benue UniCloud`、`"Calabar" "Nugi" OR "9mobile"`。
- 通用州块：`"{state}" Nigeria ("data centre" OR "data center" OR datacentre) ("MW" OR MVA OR racks)`、`"{state capital}" Nigeria "data centre" ("opened" OR launched OR commissioned)`、`"{state}" Nigeria ("Tier III" OR "Tier IV" OR "Uptime Institute")`、`"{state}" Nigeria ("captive power" OR substation) "data centre"`。

## 官方/监管管线要点（详见 explorer-official.md）

- NCC：牌照页类别驱动发现（运营商名+类别）；提取法人、牌照类别、地址、发/到期日、覆盖州、电缆登陆/互联角色；区分“仅证明电信服务能力”与“具名物理 DC”。
- 州/FCT 规划：LASPPPA/LASBCA/LASIMRA（Lagos）、FCTA development control（Abuja）、各州规划/城建/土地部（Ogun/Rivers/Akwa Ibom/Cross River/Kano/Benue/Kaduna/Oyo/Edo/Enugu 等）；无全国门户，按地块所在州/FCT 路由。
- EIA：环境部/EAD 公开披露与上传 PDF；大型 DC 常以支撑基础设施类别出现；与 TCN/运营商/能源参与者交叉。
- NERC：自备发电 CSV 与年报、MYTO 订单、配电商订单；A=电力许可/客户证据；区分发电/站点负荷/承诺电力/IT load。
- 政府数字：NITDA（政策/IT 服务商清单）、Galaxy Backbone（Abuja Tier III/Kano Tier IV）、州政府数据中心采购；政府云与共享服务。
- 云/边缘：AWS Lagos Local Zone 硬种子；Azure/GCP/OCI 负面核查；NCC-Microsoft 政策线索。
- Uptime：认证身份/城市/州/设计-建成-运营；设计级不证运营。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 媒体：DCD（B，Rack Centre LGS2/MainOne-Equinix Lekki-PH/Medallion-Digital Realty/OADC/Kasi/Galaxy/BeBenue/Cross River）、TechCabal/TechCabal Insights（B）、Technext（B/C，汇总混合 A/B/C）、TechAfrica News（B，官方公告复述）、BusinessDay/Guardian/Punch/ThisDay/Premium Times/Vanguard（B/C）、Capacity Media/DC Magazine/Dgtl Infra/W.Media（B/C）、Africa DCA（B）。
- 互联/海缆（A/B 视源）：IXPN、PeeringDB、PCH、MainOne/Equiano/2Africa/Glo1/ACE/WACS/SAT-3 页；互联证明生态系统与活跃 DC 位置，不证明 MW/容量；`meet-me room`/`carrier neutral`/`cross-connect`/`interconnect exchange` 高产量。
- 聚合器（C/B-，规则）：Baxtel/DataCenterMap/OCOLO/Datacenters.com/Cloudscene 找别名/地址/坐标/旧运营商；MW/状态绝不单凭聚合器；注意父/子公司变更：MDXi→MainOne→Equinix、Medallion→Digital Realty/Teleafrica、WIOCC→OADC、Dimension Data/Internet Solutions→NTT/inQ/OADC；园区与单体建筑不双计（除非 schema 要设施级）。
- 验证清单：物理位置至少州+城市/地方？是真 DC/colo/云设施还是统计数据库/呼叫中心/培训中心/电信桅杆/办公室服务器房/光纤路由？状态有阶段语言+日期？容量字段分开（IT load/站点负荷/MVA 进口/自备发电 MW/机架/白空间）？A 级需一手源，仅 DCD/本地媒体=B，仅聚合器/社交=C 或 U。
- 去重：Lagos 按运营商+园区——Lekki/MainOne-Equinix、Oregun/Rack Centre、Eko Atlantic/ADC-Nxtra、Ikate/OADC、Victoria Island/Medallion-Digital Realty、Lekki/Kasi；FCT/Kano 不把 Galaxy Backbone 托管服务伙伴关系复制为伙伴州的新设施。

## 来源分级

- **A** = 官方/一手：州/FCT 规划或建筑管控记录、联邦环境部/EAD EIA 披露、NERC 自备发电许可或电力命令、NCC 牌照/注册条目、官方云厂商页、官方运营商设施页、Uptime 认证记录、官方政府 DC/云页。
- **B** = 强二级：贸易媒体、交易所/IXP/海缆运营商页、州投资促进发布、声誉良好的本地商业媒体、厂商案例、具名场地的融资/政府 MoU。
- **C** = 弱线索：通用市场报告、仅目录设施、社交帖、采购传言、未实施 MoU、只说 “data centre” 无场地/状态的州 ICT 计划。
- 状态语义：announced/MoU=线索；land acquired/groundbreaking/tender/EIA/NERC-CPG/许可=场地/在建；commissioned/launched/opened/Uptime constructed/customer live=运营；云 Local Zone≠云 Region；旧未建项目（Sagamu）须新证据。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=NG，divisions=36 州 + FCT）。
2. 建种子：运营商官方页（Equinix-MainOne-MDXi/Rack Centre/ADC/OADC/Digital Realty-Medallion/Galaxy Backbone/Kasi/MTN/Airtel-Nxtra/21st Century/ipNX/Cyberspace-inQ-NTT）+ 地址 pivot（Lekki/Oregun 18 Jagal Close/Ikate Elegushi Plot 99-100/Eko Atlantic/Victoria Island/Ojota/Port Harcourt）+ NERC CPG CSV + AWS Lagos Local Zone + Uptime 清单。
3. 每州/FCT：① 官方域过一遍（州/FCT 站、物理规划/建筑管控、EAD/环境部、NCC、NERC、NITDA/Galaxy Backbone、Uptime）；② 城镇/地方搜英文变体（data centre/center/datacentre、server room/farm、colocation、cloud、Tier III/IV、MW/MVA、captive power、building permit、EIA）；③ 运营商名过一遍；④ MoU/新闻线索至少一条一手源，否则 B/C 计划/宣布。
4. 优先级：Lagos 最深（按运营商+地方，避免仅 Lagos 重复记录）→ FCT/Abuja（Galaxy/政府云）→ Kano（GBB Tier IV/MTN switch）→ Rivers/PH（Equinix PR1/2Africa）→ Ogun（Sagamu/Atakobo 能源园，旧公告须新证据）→ Akwa Ibom/Eket（Kasi DNEK）→ Cross River/Benue（州/产业 MoU，须采购/场地/施工）→ 其余州组（South East/South South/South West/North Central/North West/North East 加州资本与运营商词；州 ICT 房/统计 DC/电信 switch 按功能核实）。
5. 状态判定（announced/MoU → 场地/在建 → 投运），容量字段分开记录；输出 world 同 schema（含 aliases LG1/LG2/LG3/LGS1/LGS2/LOS1/PR1/DNEK、IT load MW、site load MW/MVA、captive generation MW、utility import MVA）。
6. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：codex terra agent（max thinking）每 agent 分批复核尼日利亚数据中心（36 州+FCT）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Rack Centre LGS2（12 MW/25 MVA）投运状态与二期；Equinix PR1 Port Harcourt（2025-04 宣布）进展；Kasi Cloud Lekki LOS 与 Eket DNEK 的 2026 运营声称（须当前一手源）；OADC Lagos（24 MW）当前状态与 Equiano 登陆；Medallion→Digital Realty 更名后 Lagos 资产；Galaxy Backbone Abuja/Kano 的 Uptime 与容量；Ogun Sagamu 旧公告是否有新证据；州级 MoU（Benue/Cross River/Abia）的采购/场地/施工跟进。
