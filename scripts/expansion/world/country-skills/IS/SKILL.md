---
name: is-datacenter-methodology
location: scripts/expansion/world/country-skills/IS/SKILL.md
description: |
  Iceland data-center discovery confirms operator leads through planning/EIA records (Skipulagsgátt, HMS EIA database), municipal permits, Landsvirkjun PPAs and Landsnet grid evidence, company registry, procurement, Fjarskiptastofa/RIX/Farice telecom-cable sources, and cloud-region checks across eight regions, anchored by Verne, atNorth (ICE01-03) and Borealis (Blönduós, Fitjar, Reykjavík).
---

# IS · 冰岛数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为冰岛数据中心/托管设施发现与审计提供可持续、可复现的查询方法论。
> 分区模型：8 个大区（region）：Capital Region；Southern Peninsula；West；Westfjords；Northwest；Northeast；East；South。
> 已知种子：Verne Keflavík/Ásbrú、atNorth ICE01（Hafnarfjörður）/ICE02（Keflavík）/ICE03（Akureyri）、Borealis Blönduós/Fitjar/Reykjavík、RIX/Múli IXP、Farice 海缆（FARICE-1/DANICE/IRIS/AUÐUR）。
> 本 skill 汇总两份探索报告：官方/监管管线（explorer-official.md）与行业/厂商发现（explorer-industry.md），字段级 A/B/C/U 分级。

## 入口

| 文件 | 管线 |
|---|---|
| explorer-official.md | 官方/监管管线：Skipulagsgátt/HMS/Skipulagsstofnun 规划与环评、市镇许可、Landsvirkjun/Landsnet/Orkustofnun、Fyrirtækjaskrá 公司登记、Fjársýslan/utbodvefur 采购、Fjarskiptastofa/RIX/Farice、云区域官方页 |
| explorer-industry.md | 行业/厂商发现：Verne/atNorth/Borealis 运营商页、DCD/DCK/Capacity/RÚV/Vísir/mbl/VB 等媒体、目录聚合器、认证数据库、海缆/IXP 管道 |

## 核心结构事实（框定每次搜索）

1. 冰岛为国家政府 + 市镇两级规划/建筑审批；**8 个大区是统计/区域分组**（Statistics Iceland 用），非独立数据中心许可当局；市镇经合并变动——市镇/大区表以 Statistics Iceland 为刷新源。
2. **无国家数据中心登记册**（不同于挪威 Nkom 式清单）；Fjarskiptastofa 监管电子通信网络/服务，但不维护数据中心专属注册；普查须拼接规划、电网/电力、运营商与地方政府证据。
3. 法律锚点：电子通信 Act No. 70/2022（旧 Act 81/2003 废止）；Fjarskiptastofa 章程 Act 75/2021；电力 Act 65/2003；规划 Act 123/2010；环评 Act 111/2021（HMS 现役服务页）；数据保护 Act 90/2018（Persónuvernd）；采购 Act 120/2016（2024-08-01 起 Fjársýslan 接管 Ríkiskaup 中央采购）。
4. **电力是门槛**：Landsvirkjun 为主要售电商并列出数据中心客户（Verne Global、atNorth 前身 Advania Data Centers、Borealis）；Landsnet 为 TSO 并网来源；Verne 与 Landsnet 2026 年宣布 Keflavík 高容量变电站（240 MW 装机容量变电站 + 120 MW 拟议扩建）。2024 年曾削减对数据中心/加密挖矿售电，2026 PPA 页显示在电网可支持处定向增加 firm power。
5. 云区域（本轮）：AWS/Azure/GCP/Oracle **均无冰岛公共区域**（官方页核验，每轮复查）。
6. 分区预期刻度：**hub**（Southern Peninsula：Verne/ICE02/Fitjar）> **light**（Capital Region：ICE01/Borealis Reykjavík/RIX；Northwest：Borealis Blönduós；Northeast：ICE03）> **none/watch**（West、Westfjords、East、South——无确认商业 DC，记录带日期负面搜索与触发条件）。
7. 认证纪律：atNorth 页称 Tier 3 是运营商营销声称（A 级声称，非 Uptime 认证）；Borealis 页称 ISO 27001（Blönduós/Fitjar）与 Blönduós B5.2/B6.2 OCP Ready；Verne 称一处数据厅 EN 50600 认证；Uptime 认证须单独查 Uptime 数据库。
8. 海缆登陆站（FARICE-1 Seyðisfjörður、DANICE/Greenland Connect/IRIS/AUÐUR 南部登陆语境）为连接性基础设施，非数据中心；AUÐUR（2026 冰岛南部-苏格兰计划电缆）与 Far North Fiber 为未来连接触发条件。

## 查询模式（复制粘贴模板见 explorer-official.md §3-§4 / explorer-industry.md §4-§5）

- 规划/环评：`site:skipulagsgatt.is gagnaver`；`site:skipulagsgatt.is "gagnaver" "matsskylda"`；`site:island.is/s/hms/gagnagrunnur-umhverfismats gagnaver`；`"Nýtt gagnaver" "ákvörðun um matsskyldu"`
- 市镇许可：`site:reykjanesbaer.is gagnaver`；`site:akureyri.is gagnaver`；`site:hunabyggd.is gagnaver OR "Borealis"`；`site:reykjavik.is gagnaver OR "byggingarleyfi"`；`site:hafnarfjordur.is gagnaver OR "Steinhella"`；`site:{municipality-domain} "gagnaver" "deiliskipulag"`
- 电力/电网：`site:landsvirkjun.is gagnaver`；`site:landsvirkjun.com "MW" "data centre" "Iceland"`；`site:landsnet.is "data center" OR "data centre"`；`"gagnaver" "forgangsorka"`；`"gagnaver" "raforkusamningur"`
- 公司登记：`site:skatturinn.is/fyrirtaekjaskra "Verne"`；`site:skatturinn.is/fyrirtaekjaskra "Borealis Data Center"`；`"{operator legal name}" kennitala`
- 采购/政府云：`site:utbodsvefur.is gagnaver OR "skýþjónusta" OR "vistun"`；`site:ted.europa.eu Iceland "data center" OR "cloud"`
- 运营商：`site:verne.co Iceland Keflavik data center`；`site:verne.co "Valhallarbraut" OR "Ásbrú" OR "Landsnet"`；`site:atnorth.com ICE01 OR ICE02 OR ICE03`；`site:bdc.is Blönduós OR Fitjar OR Reykjavík`；`site:bdc.is "Landsvirkjun" OR "OCP Ready"`
- 所有权/融资：`"Verne" "Ardian" "Iceland"`；`"Borealis Data Center" "Reykjavik DC" "Íslandsbanki"`；`"atNorth" "CPP Investments" OR "Equinix" acquisition`
- 电信/IXP/托管：`site:rix.is Reykjavík "POP" OR "connected"`；`"Múli IXP" OR "Muli IXP"`；`site:peeringdb.com "Iceland" "Reykjavik" facility`；`site:mila.is gagnaver OR hýsing`；`site:siminn.is gagnaver OR hýsing`
- 媒体：`site:ruv.is gagnaver`；`site:visir.is gagnaver`；`site:mbl.is gagnaver`；`site:vb.is gagnaver`；`site:akureyri.net gagnaver atNorth`；`site:datacenterdynamics.com Iceland Borealis OR Verne OR atNorth`
- 海缆：`site:farice.is network IRIS DANICE FARICE-1 AUÐUR`；`site:farnorthfiber.com Iceland`
- 云区域（每轮）：`site:aws.amazon.com/about-aws/global-infrastructure Iceland`；`site:azure.microsoft.com Iceland`；`site:cloud.google.com/about/locations Iceland`；`site:oracle.com/cloud/public-cloud-regions Iceland`

## 官方/监管管线要点（详见 explorer-official.md）

- Skipulagsgátt 为规划/环评/施工许可国家咨询门户（JS 重，用搜索片段+浏览器直查）；HMS/island.is 环评数据库有已核验案例：「Nýtt gagnaver Verne við Valhallarbraut, Reykjanesbæ」筛选决定 2026-06-02（A 级）。
- Landsvirkjun 为主要售电证据：Borealis Blönduósi 追加 12 MW firm power（2026-06-23 PPA）；atNorth Akureyri 至多 12 MW 绿色 firm power（2025-09 PPA）——均 A 级。
- Landsnet 为 TSO 并网来源；Verne-Landsnet 高容量变电站以 Verne 页为 A 级运营商事实（TSO 侧事实 B 级，除非 Landsnet 共同发布确认）。
- 市镇站点为建筑许可/会议记录/土地划拨/地方计划/咨询通知所需：已核验 Húnabyggð/Blönduósi 2021 Borealis 扩建通知（A 级地方证据）。
- RIX 官方页列 Reykjavík 三处 POP（Tæknigarður/Dunhagi 5、ISNIC HQ/Katrínartún 2、Múlastöð/Ármúla 25）（A）；PeeringDB 自报 C/B。Farice 为 FARICE-1/DANICE/IRIS 一级来源（A 海缆事实）；海缆登陆站按连接性处理。
- Fyrirtækjaskrá（skatturinn.is）为法人/kennitala/注册地址/活动码 A 级；单独不证明设施位置。
- U.S. trade.gov Iceland Data Centers guide（2026-04-01）为政府市场语境（B/A）；Invest in Iceland/Business Iceland/Data Centers by Iceland 为线索/推广来源。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场小型，集中三家主要运营商：**Verne、atNorth、Borealis**；Landsvirkjun 官方客户页点名三者（A）。
- **Verne Iceland/Keflavík**（Southern Peninsula）：运营商页称 100% 可再生能源、140+ MW 园区容量（A）；2026 高容量变电站 + 120 MW 拟议扩建供应商日（A）；Ardian 2024 年起持股（A 媒体中心页）；Valhallarbraut EIA 筛选（A）。
- **atNorth ICE01**（Hafnarfjörður，Capital Region）：>2,700 sqm 白色技术空间（A）；Landsvirkjun 确认前身 Advania Data Centers（A）。**ICE02**（Keflavík）：9 ha、Tier 3 声称（A 运营商页）；2024 扩张（B Vísir）。**ICE03**（Akureyri）：4.3 ha Tier 3 声称（A）；2025 Landsvirkjun PPA 至多 12 MW（A）；2023-06 首期启用（B/A Akureyri.net）。
- **Borealis Blönduós**（Northwest）：100+ MW 扩建容量、ISO 27001、B5.2/B6.2 OCP Ready（A）；12 MW PPA（A）；2021 扩建施工地方通知（A/B）。**Fitjar**（Reykjanesbær）：10 MW 建成容量、ISO 27001（A）。**Reykjavík Campus**：自 Íslandsbanki 收购 Reykjavik DC，至多 7,000 sqm（A）。融资页确认三处冰岛园区 + Kajaani 芬兰 + $148m 融资（A）。
- **RIX**：互连/共置房间（A 运营商页），非商业 DC 园区；**Múli IXP**：仅线索（C，待运营商自有页）。
- 需谨慎线索：Advania 现役设施（历史相关，无当前一级证据不列）；Opin Kerfi Akureyri（托管线索）；电信机房（Síminn/Míla、Sýn/Vodafone、Nova）；遗留加密挖矿站点（历史/线索，现态需运营商/许可/电力合同/本地报道证明）；聚合器「冰岛数据中心」行（多重复/旧名/托管转售，不直接导入）。

## 已知设施/项目与证据状态

| 设施/项目 | 分区 | 状态与证据 |
|---|---|---|
| Verne Iceland / Keflavík 园区（Ásbrú/Valhallarbraut） | Southern Peninsula | 运营中 + 扩张管线；运营商页 A（140+ MW）、变电站/120 MW A、EIA 案例 A、2010 特别法 A |
| atNorth ICE02 Keflavík | Southern Peninsula | 运营中 + 扩张；运营商页 A（9 ha Tier 3 声称）；2024 扩张 B |
| Borealis Fitjar Campus | Southern Peninsula | 运营中；站点页 A（10 MW、ISO 27001） |
| atNorth ICE01（Steinhella 10, Hafnarfjörður） | Capital Region | 运营中；运营商页 A（>2,700 sqm）；Landsvirkjun 客户/前身 A |
| Borealis Reykjavík Campus / Reykjavik DC | Capital Region | 运营中；sites 页 A + Íslandsbanki 收购 A（至多 7,000 sqm） |
| RIX POPs（三处，Reykjavík） | Capital Region | 互连/IXP 共置（A 运营商页）；非商业 DC 园区 |
| Múli IXP | Capital Region | 线索（C，Pulse 自报） |
| Borealis Blönduós Campus | Northwest | 运营中 + 扩建；站点页 A（100+ MW）、12 MW PPA A、OCP Ready A、2021 施工通知 A/B |
| atNorth ICE03 Akureyri | Northeast | 运营中 + 扩建；运营商页 A（4.3 ha）、PPA A、2023 启用 B/A |
| FARICE-1 登陆（Seyðisfjörður） | East | 海缆登陆站（A Farice）；非 DC |
| DANICE / Greenland Connect / IRIS / AUÐUR 南部语境 | South | 海缆/连接性（A Farice）；非 DC |
| AWS/Azure/GCP/OCI 冰岛公共区域 | n/a | 无（A 级官方页负面核验）；每轮复查 |
| West / Westfjords / East / South 商业 DC | 各省 | 无确认（年度负面搜索 + 触发监控） |

## 更新节奏

- 月度：Skipulagsgátt/HMS `gagnaver` 搜索；Verne/atNorth/Borealis 新闻页；Landsvirkjun/Landsnet 新闻；冰岛媒体 `gagnaver`。
- 季度：Reykjanesbær、Akureyri、Húnabyggð、Reykjavík、Hafnarfjörður 市镇清扫；RIX/PeeringDB/Pulse IXP 变化；Farice 海缆公告。
- 半年：超大规模官方区域页；Uptime/认证数据库；运营商/项目实体公司登记细节。
- 年度：八区全量负面清扫（含 West/Westfjords/East/South）并对账 explorer-industry.md。
- 事件触发：EIA 筛选、建筑许可、PPA、并网/变电站文件、海缆 RFS/新登陆点、收购/品牌变更、新运营商设施页。
- 待办（2026-08-12）：Verne 120 MW 扩建与变电站 Landsnet 共同发布确认；atNorth/Borealis Uptime 认证独立核验；Múli IXP 运营商自有页；Opin Kerfi/电信机房设施证据；AUÐUR 登陆点细节；codex terra agent 分批复核后按本方法论推进。
