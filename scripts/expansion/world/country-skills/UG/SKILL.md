---
name: ug-datacenter-methodology
location: scripts/expansion/world/country-skills/UG/SKILL.md
description: |
  Uganda（UG）数据中心发现以官方/监管管线（UCC 通信监管与持牌运营商登记、KCCA/Physical Planning Act 2010 规划许可、NEMA/ELMIS 环评、ERA/UETCL/UEDCL 电力（2025-04-01 UEDCL 接管全国配电）、NITA-U/MoICT/PDPO 政府 ICT 与 NDC、UIA 工业园、PPDA/e-GP 采购、URSB 公司登记、公有云区域官方页）和行业/厂商发现（Raxio UG1、MTN Mutundwe/Mbuya、UiXP、Roke/Liquid/Airtel、Seacom/WIOCC/Bayobab 跨境光纤、目录聚合器与贸易媒体）为主线，按 4 个地理大区（Central; Eastern; Northern; Western）逐区枚举。
  公开证据集中于 Central 区 Kampala 都会（Raxio UG1 为 Tier III Design 认证的中立托管锚点、NITA-U 国家数据中心、UiXP 双设施）；乌干达为内陆国无海缆登陆站，英文主导官方记录，超大规模云区域官方清单无 UG 条目。
---

# UG · 乌干达数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：按 4 个地理大区（Central; Eastern; Northern; Western）枚举乌干达数据中心设施与项目。
> 分区模型：135 个区加 Kampala 归入 4 个行政大区（ISO 3166-2:UG 四个地理大区加区/市代码）；精确区清单用 UBOS 出版物。
> 已知种子：Raxio UG1（Namanve/KIBP，Tier III Design 认证）、NITA-U 国家数据中心（NDC）与第三 NDC 市场研究、MTN Mutundwe 交换机与数据中心（2012 年启用）、MTN Mbuya（目录线索）、UiXP（Communications House 与 Raxio 两个 peering 设施）、NBI 国家骨干（Phase V/Moroto）、Roke/Liquid/Airtel 等运营商线索。
> 本 skill 汇总两份探索报告：官方/监管管线见 explorer-official.md，行业/厂商发现见 explorer-industry.md。

## 入口

| 文件 | 管线 |
|---|---|
| explorer-official.md | 官方/监管管线：结构事实（无国家 DC 登记册、4 大区、内陆国、Kampala 都会集中）、检索词、UCC 通信监管、规划与环境（Physical Planning Act 2010、KCCA、NEMA/ELMIS）、能源/电网（ERA、UETCL、UEDCL 2025 接管、Umeme 历史）、NITA-U/MoICT/PDPO（NDC、托管服务、NBI、第三 NDC 研究）、投资与工业园（UIA/KIBP/Namanve）、采购（PPDA/e-GP）、登记（URSB）、云区域官方核对、逐区枚举、已知官方解决设施表、负向与观察清单规则、更新节奏 |
| explorer-industry.md | 行业/厂商发现：行业框架（Kampala 都会市场、东/北/西为观察信号）、检索词、新闻与研究源（DCD、Connecting Africa、Capacity、ITWeb、TechAfrica、African Business、Daily Monitor、New Vision、MIGA、ITU、D4D Hub）、运营商与设施线索（Raxio UG1、Uptime、NITA-U NDC、MTN、UiXP、Roke、Liquid、Airtel、SimbaNET/Zuku、Baasa、Hostalite 等）、互连与运营商语境（UiXP/PeeringDB、Seacom Nairobi-Kampala、WIOCC TEAMS、Bayobab 光缆）、超大规模/云伙伴核对、逐区行业方法、查询模板、已知行业证据汇总、更新节奏 |

## 核心结构事实（框定每次搜索）

1. 乌干达无国家公共数据中心设施登记册、无全国可检索规划登记册：枚举必须联合行业监管（UCC）、区/市规划（KCCA/Physical Planning Act 2010 第 35 条开发许可）、NEMA 环评（ELMIS 门户）、电力记录（ERA/UETCL/UEDCL）、政府 ICT 采购、运营商页与行业证据。
2. 公开证据集中于 Central 区 Kampala 都会（Kampala、Wakiso/Namanve、Mukono 走廊）：Raxio UG1（Namanve/KIBP，2021 年启用，中立/云中立，运营商发布称最高 400 机柜与 1.5 MW IT 功率，Uptime Tier III Design Documents 认证）、MTN Mutundwe（2012 年启用交换机与数据中心）、NITA-U NDC 服务、UiXP 双设施；Eastern/Northern/Western 公开证据多为电信/NBI/边缘或政府服务节点，无已核实商业托管设施。
3. 乌干达为内陆国：无国内海缆登陆站，国际连通经陆路回程到肯尼亚/蒙巴萨与坦桑尼亚/达累斯萨拉姆登陆生态；海缆材料仅作连通性语境，不得在乌干达大区下记录任何海底登陆站。
4. 英文主导官方记录：同时搜 `data centre` 与 `data center`，加 `datacentre`、`colocation`、`carrier neutral`、`cloud`、`DR site`、`National Data Centre`、`NBI`、`Tier III`、`racks`、`MW`、`MVA`、`substation`；斯瓦希里语（kituo cha data/seva/wingu）低收益，仅补充性外展搜索，须用英文/运营商/官方材料确认。
5. NBI 光缆节点、Service Uganda 中心、电信交换局、银行 IT 机房、大学实验室、学校机房与网吧均非数据中心，除非来源明确提供托管/托管/云/实质服务器基础设施；NBI Phase V/Moroto 是已验证连通性证据，非 DC 证据。
6. 超大规模云区域：仅当提供商官方区域清单列出乌干达区域且存在独立本地设施证据才算 UG 设施记录；2026-08-12 核对 AWS/Azure/GCP/OCI 官方清单均无乌干达公有云区域（A 级负向检查）；云伙伴/转售商不暗示超大规模区域或本地设施。
7. 分级按所支持事实：A 一手/官方（监管、法律、政府门户、NITA-U、PDPO、UCC、NEMA、PPDA/e-GP、ERA/UETCL/UEDCL、UIA、云官方区域页、运营商自有设施页、Uptime 奖励页）；B 强二级（成熟贸易/本地媒体、世行/MIGA/ITU 文件、PeeringDB 互连事实、行业协会）；C 弱线索（目录/聚合器、社媒、未佐证市场报告片段）；U 未决线索不作为设施证据。

## 查询模式（复制粘贴模板见 explorer-official.md §2/§3 / explorer-industry.md §7）

- UCC：`site:ucc.co.ug "data centre" OR "data center"`、`site:ucc.co.ug "Infrastructure Provider" "{operator}"`、`"LICENSED TELECOM OPERATORS" Uganda "{operator}"`、`"{operator}" "Uganda Communications Commission" licence`。
- 规划/环境：`site:kcca.go.ug "data centre" OR "data center" OR "server room"`、`"{district}" "physical planning committee" "data centre"`、`site:nema.go.ug "data centre" OR "data center" OR "ICT"`、`"Environmental and Social Impact Assessment" Uganda "data centre"`、`"project brief" NEMA Uganda "{operator OR project}"`、`"{operator}" ESIA Uganda`。
- 能源/电网：`site:era.go.ug "data centre" OR "data center"`、`site:uetcl.go.ug "Namanve" OR "KIBP" OR "substation" OR "MVA"`、`site:uedcl.co.ug "data centre" OR "data center" OR "{operator}"`、`"{project}" "power supply" Uganda "data centre"`、`"{operator}" Uganda "33kV" OR "MVA" OR "substation"`。
- NITA-U/MoICT/PDPO：`site:nita.go.ug "National Data Centre" OR "data centre" OR "DR site" OR "cloud"`、`site:nita.go.ug "Third National Data Centre" OR "Data Center Market Study"`、`site:ict.go.ug "data centre" OR "National Backbone Infrastructure"`、`site:pdpo.go.ug register "{operator OR hosting company}"`、`"National Data Centre" Uganda "{district OR town}"`、`"NITA-U" "disaster recovery" Uganda`。
- 投资/工业园：`site:ugandainvest.go.ug "data centre" OR "data center" OR "ICT"`、`site:ugandainvest.go.ug "Namanve" "{operator}"`、`"Kampala Industrial and Business Park" "data centre"`、`"KIBP" OR "Namanve" "Raxio" OR "cloud"`。
- 采购/登记：`site:ppda.go.ug "data centre" OR "data center" OR "server" OR "cloud"`、`site:egpuganda.go.ug "data centre" OR "data center" OR "NITA-U"`、`site:ursb.go.ug "{operator legal name}"`、`"{operator}" "Uganda Registration Services Bureau"`。
- 云区域负向：`site:aws.amazon.com/about-aws/global-infrastructure Uganda`、`site:learn.microsoft.com/en-us/azure/reliability/regions-list Uganda`、`site:cloud.google.com/about/locations Uganda`、`site:docs.oracle.com/iaas/Content/General/Concepts/regions.htm Uganda`、`"{hyperscaler}" Uganda "cloud region" OR "availability zone" OR "Local Zone"`。
- 行业新闻：`site:datacenterdynamics.com/en/news Uganda "data centre" OR Raxio OR Liquid`、`site:connectingafrica.com Uganda "data centre" OR Bayobab`、`site:techafricanews.com Uganda "NITA-U" OR "National Data Centre"`、`site:monitor.co.ug "data centre" OR "data center" Uganda`、`site:newvision.co.ug "data centre" OR Raxio`、`"Uganda" "data centre" "{operator OR town}" launched OR opened OR commissioned`。
- 运营商：`"{operator}" Uganda "data centre" OR "data center" OR colocation OR hosting`、`site:{operator-domain} Uganda "data centre" OR "data center" OR cloud`、`"{operator}" "Uptime Institute" OR "Tier III" Uganda`、`"{operator}" Namanve OR KIBP OR Kampala OR Mutundwe OR Mbuya`。
- 互连/目录：`site:uixp.co.ug peering OR facility OR members`、`site:peeringdb.com/ix/422 Uganda OR Raxio OR Communications House`、`"UiXP" "Raxio" OR "Communications House"`、`"Uganda" EASSy OR TEAMS OR SEACOM OR 2Africa OR Bayobab`、`site:datacentermap.com/uganda Kampala "data centre"`、`site:inflect.com Kampala Uganda "data center"`。

## 官方/监管管线要点（详见 explorer-official.md）

- UCC（ucc.co.ug）：按 Uganda Communications Act 2013 监管；电信许可页证第 5(1)(b) 条许可职责；eServices 账户门槛；持牌电信运营商登记 PDF（2024-12-30 版，A 证法人/许可类别，非设施证据）；许可类别含 National Telecom Operator、National/Regional Public Infrastructure Provider、National/Regional Public Service Provider。
- 规划与环境：Physical Planning Act 2010 第 35 条要求在规划区开发前取得物理规划委员会开发许可；KCCA（kcca.go.ug）Kampala 规划/建筑控制与 Smart Permit；NEMA（nema.go.ug）ESIA 流程经 ELMIS（eservices.nema.go.ug）提交 Project Brief/ToR/ESIA；从许可/ESIA 提取申请人/SPV、区/市、ward/parish、地块、项目描述、楼面、机柜/IT 负载、变压器/MVA 需求、发电机/燃油存储、水/冷却需求、NEMA 证书/编号、决定日期与地方规划机构。
- 能源/电网：ERA（era.go.ug）电力监管；UETCL（uetcl.go.ug）输电项目/变电站/批发供应；UEDCL（uedcl.co.ug）拥有/运营 33kV 以下配电网络，2025-04-01 从 Umeme 接管并恢复全国配电运营控制（ERA 过渡通知佐证）；Umeme 仅用于 2025-04 前并网历史。
- NITA-U/MoICT/PDPO：NITA-U 国家数据中心页（nita.go.ug/services/technical-services/nita-u-national-data-centre）描述政府托管基础设施，列 IaaS/PaaS/托管服务与 99.98% SLA（A 证存在/服务，精确物理位置未公开）；政府托管服务页（co-location-tx-sites-mancenter）；NBI 项目（Phase 1-4 铺设 4,387 公里光纤连接 53 个区 HQ、11 个边境站、1,480 个 MDA；Phase V Karamoja/Moroto 启动）；2025 数据中心市场研究/第三 NDC 观察清单（研究存在 A，不代表已建成）；PDPO 依 Data Protection and Privacy Act 2019 的登记门户（pdpo.go.ug/register）。
- 投资/工业园：UIA（ugandainvest.go.ug）投资促进与园区材料；KIBP（Namanve）为政府工业园区之一（A 证园区存在/位置，非设施证据）；State House 投资单元 Namanve 投资者活动。
- 采购/登记：PPDA（ppda.go.ug）采购监管（PPDA Act Cap 205）；e-GP 门户（egpuganda.go.ug）；搜服务器机房、NDC 扩展、DR 站点、云托管、ICT 基础设施、UPS/发电机组、NBI 工程；URSB（ursb.go.ug）公司登记/法人名称核对（付费/账户搜索）；OpenCorporates 知识页仅 C 级指针。

## 行业/厂商发现要点（详见 explorer-industry.md）

- Raxio UG1 是乌干达最佳现役商业托管记录：运营商页（raxiogroup.com/data-centres/uganda/）证 Namanve 企业级设施、2021 年启用、中立/云中立、最高 400 机柜与 1.5 MW IT 功率（运营商声明 A/B）；Uptime 国家奖励页证 Raxio Data Centre SMC Limited, Kampala, Raxio UG1, Tier III Certification of Design Documents（A 证认证类型）；250 机柜媒体/目录数字须单独记录为 B/C。
- MTN：官方服务页（mtn.co.ug/businesssolutions/data-centre/）证 DC 服务；MTN 档案称 Mutundwe 交换机与数据中心 2012 年启用并容纳 MTN 数据服务器（A 证存在/功能）；Mbuya 命名设施为目录来源（C/U 待一手确认）。
- UiXP：官方联系页证两个 peering 设施——Communications House, 1 Colville Street, Kampala 与 Raxio Data Center, Plot 781 Block 113, Namanve Industrial Park；PeeringDB IX 422 佐证（peer 数与端口速度为随时间变化 B 级）；IX 非独立托管 DC，除非另有证据。
- 运营商线索：Roke Telkom/Roke Cloud 营销 IT/数据中心/托管/云服务（服务声明 A；目录声称 Kulubya Close 的 Roke DC，运营商页未明确发布该设施记录，C/U）；Liquid Intelligent Technologies Uganda（官方办事处/服务在场 A；DCD 2024 报道 Liquid 在乌干达推出 Microsoft Azure Stack，B 级本地云信号；物理 DC 位置 U）；Airtel Uganda（集团 DC 能力 B/A 于集团级，乌干达设施 U）；SimbaNET/Simba Fiber/Zuku（ISP 在场 B/C，无设施证据）；Baasa Cloud（托管线索 C，1 Water Lane Naguru 社媒地址，设施 U/C）；Hostalite/Computer Point/Datanet/CSG（本地 IT/云/托管线索 U/C）。
- 互连/运营商：Seacom 2026-06-16 发布高容量 Nairobi-Kampala 新路由（A/B 运营商证据，非 DC）；WIOCC TEAMS 连接 Mombasa-Fujairah 并延伸至乌干达（B）；Bayobab Kampala-Tororo-Kenya/Mombasa 光缆（B）；EASSy/SEACOM/TEAMS/2Africa/Equiano 为海缆生态语境。
- 新闻/研究源：DCD（Raxio、Equity Bank 迁移、Liquid Azure Stack）、Connecting Africa、Capacity、ITWeb Africa、TechAfrica News、African Business、Daily Monitor、New Vision、The Independent、CEO East Africa、Techjaja/PC Tech Magazine、MIGA（Raxio 投资者/ESRS 语境 B）、ITU（乌干达国家绿色数据中心战略与指南 B/A 证出版物存在）、D4D Hub 市场简报（B 市场语境）。
- 生命周期分级：`plans`/`MoU` 为意向；`construction` 为管线；`opened`/`operational`/`certified`/`migrated` 更强但仍需运营商/政府/Uptime 确认才达 A 级设施状态。

## 已知设施/项目与证据状态

| 设施/项目 | 分区 | 状态与证据 |
|---|---|---|
| Raxio UG1 数据中心 | Central（Namanve Industrial Park/KIBP，Kampala 都会） | 运营中；A（运营商页证存在/位置/中立/Tier III 声明）；A（Uptime Tier III Design Documents 奖励）；1.5 MW/最高 400 机柜 A/B（运营商声明）；250 机柜媒体数字 B/C 单独记录 |
| NITA-U 国家数据中心（NDC） | Central（乌干达政府 NDC，精确地址未公开） | 运营中政府托管；A（nita.go.ug 证存在/服务，IaaS/PaaS/托管、99.98% SLA）；物理站点/地址 U |
| NITA-U 第三国家数据中心研究 | 位置未决 | 研究/规划信号；A（2025 市场研究页）；已建成设施未确立 |
| MTN Mutundwe 交换机与数据中心 | Central（Mutundwe, Kampala） | 运营中；A（MTN 档案证 2012 年启用/功能）；目录地址 C 除非 MTN/规划记录确认 |
| MTN Mbuya 数据中心 | Central（Mbuya/Kampala） | 服务存在 A（MTN 服务页）；Mbuya 命名设施/地址 C/U（目录来源，待一手确认） |
| UiXP | Central（Communications House, 1 Colville Street, Kampala；第二设施 Raxio, Plot 781 Block 113, Namanve） | 运营中 IX；A/B（UiXP 联系页、PeeringDB IX 422/fac 3962）；非商业托管 DC 除非另有证据 |
| NBI 光纤节点/边境点/区 HQ 连接 | 全区 | A（NITA-U 项目页与 Phase V 启动）；国家光纤/连通性，非 DC 证据 |
| Roke、Liquid、Airtel、Baasa、Hostalite 等本地托管线索 | 主要为 Central | 仅官方公司/服务声明 A；设施存在需一手/运营商设施页或官方记录 |
| AWS/Azure/GCP/OCI 公有云区域 | 无 | 官方区域清单无 UG 区域（A 负向检查）；非洲足迹为南非/Johannesburg 等非 UG 区域 |
| Eastern/Northern/Western 商业托管设施 | Eastern/Northern/Western | 未发现已核实商业托管设施；继续周期负向搜索 |
| 海缆登陆站 | 无 | 乌干达无国内落地；路由证据仅为陆路回程 |

## 更新节奏

- 月度：UCC 许可登记/新闻；NITA-U/MoICT 新闻；PeeringDB UiXP 与 UiXP 联系/设施；DCD/Capacity/Connecting Africa 乌干达搜索；Seacom/WIOCC/Bayobab 路由新闻。
- 季度：NEMA/ELMIS 与 KCCA/区规划搜索；UEDCL/UETCL/ERA 搜索；PPDA/e-GP 采购词；UIA 园区/投资者新闻；运营商扫掠（Raxio、MTN、Roke、Liquid、Airtel、Baasa、Hostalite、Computer Point、Datanet、CSG）。
- 半年：超大规模区域页；Uptime 乌干达奖励；PDPO 登记搜索（托管/云处理者）；URSB 法人名称核对；ITU/D4D/世行市场出版物。
- 年度：刷新 UBOS/ISO 区-大区覆盖；重跑全部模板；重新分级 C/U 线索与负向大区；更新已知设施与负向分区说明。
- 新信号：任何发布/建设/迁移声明立即转向官方文件——UCC、NEMA/ELMIS、KCCA/区规划、ERA/UETCL/UEDCL、UIA、PPDA/e-GP、URSB。
- 待办（2026-08-12）：UG 属 batch-10 已复核国家；后续按本方法论推进 4 大区枚举，codex terra agent 分批复核后更新证据分级。
