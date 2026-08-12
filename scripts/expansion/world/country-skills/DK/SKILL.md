---
name: dk-datacenter-methodology
location: scripts/expansion/world/country-skills/DK/SKILL.md
description: |
  Denmark data-center discovery builds a bottom-up facility list from official planning/building/environmental records (Plandata.dk, municipal lokalplan/byggetilladelse/VVM, CVR/Virk, Energinet/Forsyningstilsynet, BBR) and reconciles operator/hyperscaler leads (Microsoft Denmark East/West, Apple Viborg, Meta Odense, Bulk Esbjerg, GlobalConnect, Equinix, Digital Realty) plus DDI/trade press across five regions and 98 municipalities.
---

# DK · 丹麦数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为丹麦数据中心/托管设施发现与审计提供可持续、可复现的查询方法论。
> 分区模型：5 个大区（North Denmark；Central Denmark；South Denmark；Region Zealand；Capital Region），98 个市镇（municipalities 为实际规划/建筑审批主体）。
> 已知种子：Microsoft Denmark East（Høje-Taastrup/Køge/Roskilde）、Microsoft West Denmark（Esbjerg/Varde，计划中）、Apple Viborg/Foulum/Tjele、Meta Odense、Bulk DK01 Esbjerg、GlobalConnect Taastrup、Equinix/Digital Realty Copenhagen。
> 本 skill 汇总两份探索报告：官方/监管管线（explorer-official.md）与行业/厂商发现（explorer-industry.md），字段级 A/B/C/U 分级。

## 入口

| 文件 | 管线 |
|---|---|
| explorer-official.md | 官方/监管管线：CVR/Virk、Plandata.dk、市镇规划/建筑/环境记录（lokalplan/byggetilladelse/VVM/miljøgodkendelse）、BBR、Energinet/Forsyningstilsynet、udbud.dk/TED/SKI/KOMBIT 采购、云区域官方页 |
| explorer-industry.md | 行业/厂商发现：DDI 协会、Green Power Denmark/IT-Branchen/DI、Computerworld/Version2/ITWatch/EnergyWatch/Ingeniøren/Børsen/DCD 等媒体、Data Center Map/Baxtel/DatacenterHawk 目录、IXP/海缆来源 |

## 核心结构事实（框定每次搜索）

1. 丹麦**没有国家数据中心许可登记册或官方数据中心普查**；设施清单必须自下而上拼接（CVR 法人 → 规划/建筑/环境记录 → 电网/采购 → 运营商自有页）。
2. 行政区划为 **5 个大区 + 98 个市镇**；市镇是数据中心枚举的实际规划与建筑审批主体。丹麦已批准 2027 年起 Capital Region 与 Region Zealand 合并，但本 repo 2026 年枚举仍用五区模型。
3. 法律依据：规划 Planloven；建筑 Byggeloven/BR18；环境 Miljøvurderingsloven/Miljøbeskyttelsesloven；电力 Elforsyningsloven（Energinet/DSO/Forsyningstilsynet）；数据保护 GDPR + Databeskyttelsesloven（Datatilsynet）；网络安全 **NIS 2-loven（Lov nr. 434 af 06/05/2025，2025-07-01 生效）**；电信政策属 Digitaliseringsstyrelsen。
4. 关键官方数据面：**CVR/Virk**（法人/CVR 号/生产单元/地址，NACE 63.11.00 候选宇宙）、**Plandata.dk**（全国规划数字登记）、**BBR**（建筑属性）、市镇规划/建筑/环境档案、**Energinet/Forsyningstilsynet**（大用户并网证据，超大规模项目硬约束）。
5. 环境记录是 A 级技术/决策证据：数据中心常触发噪声、备用发电机、燃油储存、冷却、雨水与**余热回收（overskudsvarme/fjernvarme）**文件；VVM/miljøgodkendelse 不证明运营状态。
6. 云区域状态（2026-08-12）：**Microsoft Azure Denmark East 已启用**（2026-03-26，官方点名 Høje-Taastrup、Køge、Roskilde）；**West Denmark 已宣布**（Esbjerg/Varde，按计划处理）；AWS/GCP/Oracle 无丹麦区域——区域名不等于设施，物理设施需微软/市镇级证据。
7. 验证规则：不得仅凭云区域名或目录行计数；多云区域园区仅在来源点名市镇/站点时按市镇拆分；商业共置、超大规模自建、企业/私有 IT、研究 HPC、IXP、海缆登陆资产分开统计；403/JS/付费墙阻断时保留 URL 但降级事实并加访问备注。
8. 丹麦语拼写须同时用带/不带丹麦字符形式搜索（如 Høje-Taastrup/HTK、Køge/Koge、naerhed/nærhed），因为来源规范化不同。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§4 / explorer-industry.md §1-§4）

- 法人（CVR/Virk）：`site:datacvr.virk.dk "{operator}"`；`"{operator}" "CVR" "63.11"`；`"{operator}" "P-nummer" "{kommune}"`
- 规划/建筑（Plandata/市镇）：`site:{kommune}.dk (datacenter OR "data center" OR serverpark)`；`site:{kommune}.dk lokalplan datacenter`；`site:{kommune}.dk byggetilladelse datacenter`；`"lokalplan nr." "{adresse}" datacenter`
- 环境/余热：`site:{kommune}.dk "{operator}" VVM`；`site:{kommune}.dk datacenter noedstroem`；`site:{kommune}.dk datacenter overskudsvarme`；`site:mst.dk datacenter "{kommune}"`
- 电网/能源：`site:energinet.dk datacenter`；`site:forsyningstilsynet.dk datacenter`；`"{operator}" "{kommune}" nettilslutning`；`"{kommune}" datacenter "150 kV"`
- 采购：`site:udbud.dk datacenter`；`site:udbud.dk kolokation`；`site:ted.europa.eu Denmark datacenter hosting`；`site:ski.dk cloud hosting datacenter`
- 云区域（每次运行前核验）：`site:learn.microsoft.com/azure "Denmark East"`；`site:news.microsoft.com Denmark datacenter region Microsoft`；`site:docs.aws.amazon.com/global-infrastructure Denmark Region`；`site:oracle.com/cloud Denmark region`
- 超大规模/运营商：`"Microsoft" "Høje-Taastrup" datacenter`；`"Microsoft" Gadstrup datacenter`；`"Apple" Viborg Foulum datacenter`；`"Meta" Odense data centre`；`"Bulk Infrastructure" Esbjerg DK01`；`"GlobalConnect" Taastrup datacenter`；`"Equinix" Copenhagen CP1 OR CP2`；`"Digital Realty" Copenhagen Denmark`
- 协会/媒体：`site:datacenterindustrien.dk "{operator}"`；`site:computerworld.dk datacenter`；`site:version2.dk datacenter`
- 目录/IXP/海缆：`site:datacentermap.com Denmark data center`；`Denmark submarine cable landing Blaabjerg`；`site:peeringdb.com Copenhagen "CIX"`
- 分大区清扫：`site:aalborg.dk datacenter`；`site:viborg.dk "lokalplan nr. 460"`；`site:odense.dk Meta datacenter`；`site:esbjerg.dk Bulk datacenter`；`site:roskilde.dk Microsoft datacenter`；`site:koge.dk "Lille Skensved" datacenter`；`site:htk.dk "Høje-Taastrup" datacenter`；`site:brk.dk datacenter Bornholm`

## 官方/监管管线要点（详见 explorer-official.md）

- CVR/Virk 是法人/CVR 号/生产单元/地址/活动码的 A 级来源；CVR 单独不证明数据中心建筑。
- Plandata.dk 为全国规划数字登记（A）；市镇 lokalplan/kommuneplan 修正案、建筑许可、公众咨询、VVM/环境决定是具体计划事实的 A 级来源；不存在单一国家建筑许可库。
- 高产出已确认规划锚点：Viborg 市 Apple/Foulum（lokalplan nr. 460、VVM、应急电站环境许可）；Odense Meta/Tietgenbyen（Lokalplan 6-1096）；Roskilde Microsoft/Gadstrup/Finervej 门户。
- Energinet「Net til tiden」材料是语境；具名并网记录更强；电网瓶颈的一般媒体说法为 B 级。
- 采购（udbud.dk/TED/SKI/KOMBIT）可揭示共置/托管/DR 供应商与 DR 站点，但采购裁决为 A 级事实、设施存在仍需设施证据。
- 无丹麦电信监管机构数据中心设施清单；电信来源仅用于连接性与关键基础设施语境。
- 来源访问被 403/JS/付费墙阻断时：保留 URL、降级未证实事实、加访问备注。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **Danish Data Center Industry (DDI)** 是全国主要行业机构：成员页为 A 级成员状态（非设施普查）；knowledge hub 市场报告为 B 级。
- **Microsoft Denmark East**：2026-03-26 启用（A）；Microsoft Local 确认 Høje-Taastrup/Roskilde 已开工（A）；Køge/Lille Skensved 精确站点细节需市镇记录（B/C）。
- **Microsoft West Denmark**：官方宣布覆盖 Esbjerg/Varde（A 级宣布；非运营）。
- **Apple Viborg/Foulum/Tjele**：Apple newsroom 称运营中、45,000 平方米、支撑欧洲 Apple 服务（A）；许可包需 Viborg Kommune 记录。
- **Meta Odense**：Meta 官方 info sheet（A）；2022 扩建取消为 B 级贸易媒体（DCD/DCK）。
- **Bulk DK01 Esbjerg**：Bulk 自有页（A，curl 可能 403 需浏览器验证）；Invest in Denmark 破土叙事（B）。
- **GlobalConnect / Equinix / Digital Realty Copenhagen**：运营商自有营销页（A）；精确地址若仅来自聚合器为 C；Equinix 特定 URL curl 403 需人工核验；Digital Realty 计数前须核对 Interxion/GlobalConnect 交易后的当前所有权。
- **itm8/Sotea Silkeborg**：仅 C/B 线索，需 itm8 或 Silkeborg Kommune 直接确认；`frostcore.net` 本轮不可达，不作 A 级来源。
- **CIX/Copenhagen Internet Exchange**：`copenhagenix.net` 2026-08-12 DNS 失败；PeeringDB 仅作 C 级线索。
- **atNorth Denmark**：仅其自有页营销声明为 A；页面未点名实际站点时不计数。
- 不计数：Atea/One.com/Simply.com/UnoEuro/Fiberby 等托管服务商（除非自有设施）、区域托管、大学研究算力、IXP、海缆登陆（Blaabjerg 为连接性资产 C+/B）、KMD/NEC Ballerup 与 TDC/Nuuday 遗留共置（B/C 线索）。

## 已知设施/项目与证据状态

| 设施/项目 | 分区 | 状态与证据 |
|---|---|---|
| Apple Viborg/Foulum/Tjele | Central Denmark | 运营中；Apple newsroom A 级（45,000 m²）；市镇规划/VVM 待挂接 |
| Meta Odense | South Denmark | 运营中；Meta info sheet A 级；扩建取消 B 级 |
| Microsoft Denmark East | Capital Region + Region Zealand | 云区域已启用（2026-03-26，A）；物理设施按微软/市镇证据逐个计数；Høje-Taastrup/Roskilde 开工声明 A 级 |
| Microsoft West Denmark | South Denmark | 已宣布/计划；Esbjerg/Varde 官方宣布 A 级；许可/施工状态 B/U |
| Bulk DK01 Esbjerg | South Denmark | 运营商营销活跃园区（A）；许可状态需确认 |
| GlobalConnect Taastrup/Copenhagen | Capital Region | 运营商营销共置（A）；地址若仅聚合器为 C |
| Equinix Copenhagen | Capital Region | 需可访问 Equinix 页/人工核验（A 可达时；U 阻断处） |
| Digital Realty Copenhagen | Capital Region | 自有页 A；计数前核验当前设施所有权 |
| itm8/Sotea Silkeborg | Central Denmark | 仅 C/B 线索，待一级确认 |
| CIX/Copenhagen Internet Exchange | Capital Region | 连接性线索（C/U）；域名解析失败 |
| Blaabjerg 海缆登陆 | South Denmark | 连接性资产（C+/B），非数据中心 |
| AWS/GCP/Oracle 丹麦区域 | n/a | 无（A 级官方页）；每次运行前核验 |

## 更新节奏

- 每次运行前：Microsoft/AWS/GCP/Oracle 区域清单；Microsoft Local Denmark；Apple/Meta/Bulk/GlobalConnect/Equinix/Digital Realty 及 Silkeborg 线索运营商页。
- 月度：DDI、Computerworld、Version2、ITWatch、EnergyWatch、Ingeniøren、Børsen、DCD、DataCenterKnowledge。
- 季度：Plandata.dk「datacenter」搜索；五区市镇搜索；Energinet/Forsyningstilsynet 电网状态；CVR 63.11 宇宙；Data Center Map/Baxtel/DatacenterHawk/PeeringDB/Uptime/TeleGeography。
- 半年：已计数站点 BBR/地址核验；采购搜索；Uptime 清单；海缆地图；行业线索对官方记录全量对账。
- 待办（2026-08-12）：微软 West Denmark 许可/施工状态跟进；Equinix/Digital Realty Copenhagen 人工核验与所有权核对；itm8 Silkeborg 一级确认；CIX 现役官方来源；codex terra agent 分批复核后按本方法论推进。
