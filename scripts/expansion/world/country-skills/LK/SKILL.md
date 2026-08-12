---
name: lk-datacenter-methodology
location: scripts/expansion/world/country-skills/LK/SKILL.md
description: |
  Sri Lanka data-center discovery assembles evidence from telecom regulation (TRCSL), government ICT programs (ICTA/Lanka Government Cloud/LGN), BOI/Port City investment records, planning/energy routes (UDA/OSU/CEB), procurement, cable-landing records, and Uptime certification, then upgrades industry leads (SLT-Mobitel, Dialog, Lankacom, MillenniumIT/LSEG) across nine provinces with EN/Sinhala/Tamil search sets.
---

# LK · 斯里兰卡数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为斯里兰卡数据中心/托管设施发现与审计提供可持续、可复现的查询方法论。
> 分区模型：9 个省（provinces）：Western；Central；Southern；Northern；Eastern；North Western；North Central；Uva；Sabaragamuwa。
> 已知种子：SLT-Mobitel National Data Center（Pitipana-Homagama，Uptime Tier III）、Dialog Malabe Data Center #2、Dialog Piliyandala、Lankacom Colombo 07、MillenniumIT/LSEG Malabe、National Savings Bank Production DC、ICTA/Lanka Government Cloud、五个海缆登陆站。
> 本 skill 汇总两份探索报告：官方/监管管线（explorer-official.md）与行业/厂商发现（explorer-industry.md），字段级 A/B/C/U 分级。

## 入口

| 文件 | 管线 |
|---|---|
| explorer-official.md | 官方/监管管线：TRCSL、ICTA/Ministry of Digital Economy、DPA、BOI/Port City、UDA/OSU/Colombo MC、CEA/CEB/LECO、Treasury/NPC/ePMS 采购、eROC、云区域/Uptime 官方页 |
| explorer-industry.md | 行业/厂商发现：运营商页、DCD/Daily FT/Sunday Times/EconomyNext/Daily Mirror 等媒体、Submarine Networks/TeleGeography、目录聚合器、FITIS/SLASSCOM/LIRNEasia、僧伽罗语/泰米尔语本地搜索 |

## 核心结构事实（框定每次搜索）

1. 斯里兰卡**没有国家公共数据中心登记册**；证据须从电信监管、政府 ICT 计划、运营商页、规划/采购路线、海缆记录、认证登记与投资促进记录拼接。
2. 监管机构 **TRCSL**（Telecommunications Regulatory Commission，A 级运营商/牌照/监管事实，非数据中心登记册）；政府 ICT 顶端机构 **ICTA**（ICT Act No. 27 of 2003，A 级 LGN/Lanka Government Cloud/NDX/政策事实）；部委名称与范围每批次复查（现为 Ministry of Digital Economy）。
3. 数据保护：**DPA**（Personal Data Protection Act No. 9 of 2022 + 2025 修正案，2023-08 成立）——仅合规语境；投资：**BOI**（investsrilanka.com，A 级批准投资/专区公告）；**Port City Colombo** 无经核验的数据中心专属项目，相关声称保持 C/U。
4. 云区域（2026-08-12 检查）：AWS/Azure/Google Cloud/Oracle OCI **官方清单均无斯里兰卡公共区域**（A 级缺席证据仅限所查页面）；本地「cloud」通常指 SLT Akaza、Dialog cloud/colocation、Lankacom hosting 或 ICTA 政府云。
5. 海缆：Submarine Networks 列出**五个海缆登陆站**（SLT Colombo、SLT Mount Lavinia、SLT Matara、Lanka Bell Colombo、Dialog Mount Lavinia），SLT Welikada 为国际回程枢纽；登陆站默认按海缆/关键设施计数，除非另有数据中心功能来源。五个中四个在 Western，Matara CLS 在 Southern。
6. 已核验设施集中在 **Western Province**（Pitipana/Homagama、Malabe、Piliyandala、Colombo 07、Welikada、Mount Lavinia）；其余 8 省无核验商业 DC，负面结果仅在有完整五遍工作流记录时才算证据。
7. 输出规则：不把 ICT 培训中心、呼叫中心、网络实验室、大学 e-learning、普通电信交换局、银行 DR 提及算作数据中心；`capacity_mw` 仅用于点名该设施的 MW/IT 负载来源；聚合器地址为 C 级直到运营商/许可/登记/可信媒体佐证；Dialog Malabe 与 Piliyandala 不得合并；Uptime 认证只按具体条目（不得把 Malabe 认证转嫁 Piliyandala）。
8. 易变事实每批次复查：云区域缺席、Uptime 认证目录、部委名称、海缆状态、BOI/Port City 公告、采购门户、运营商页。

## 查询模式（复制粘贴模板见 explorer-official.md §2-§6 / explorer-industry.md §1-§5）

- TRCSL：`site:trc.gov.lk "data centre"`；`site:trc.gov.lk "IDC"`；`"TRCSL" "data centre" "Sri Lanka"`
- ICTA/政府云：`site:icta.lk "Lanka Government Cloud"`；`site:icta.lk "LGN 2.0"`；`"ICTA" "National Data Exchange" "Sri Lanka"`
- BOI/Port City：`site:investsrilanka.com "data centre"`；`site:portcitycolombo.lk "data centre"`；`"BOI Sri Lanka" "data centre"`
- 规划/环境/能源：`site:osu.uda.lk "data centre"`；`site:cea.lk "data centre" "EIA"`；`site:ceb.lk "data centre"`；`"grid connection" "data centre" "Sri Lanka"`
- 采购/捐助项目：`site:treasury.gov.lk/procurement "data centre"`；`site:epms.nprocom.gov.lk "ICT"`；`site:ungm.org "Sri Lanka" "data centre"`；`site:documents.worldbank.org "Sri Lanka" "digital"`
- 云区域缺席核验：`site:docs.aws.amazon.com/global-infrastructure Sri Lanka`；`site:learn.microsoft.com/azure Sri Lanka region`；`site:cloud.google.com/about/locations Sri Lanka`；`site:docs.oracle.com Sri Lanka region`
- 运营商/设施：`"SLT" "National Data Center" "Pitipana"`；`"Dialog" "Data Centre" "Malabe"`；`"Dialog" "Data Centre" "Piliyandala"`；`"Lankacom" "data center"`；`"MillenniumIT" "Tier 3 data centre"`
- 本地语言（原文 Unicode）：僧伽罗语 `"දත්ත මධ්‍යස්ථානය" "ශ්‍රී ලංකාව"`；泰米尔语 `"தரவு மையம்" "இலங்கை"`；`"கடலடி கேபிள்" "இலங்கை"`
- 媒体/海缆：`site:datacenterdynamics.com "Sri Lanka" "data center"`；`site:ft.lk "Sri Lanka" "data centre"`；`site:economynext.com "data centre" "Sri Lanka"`；`site:submarinenetworks.com Sri Lanka station`；`"Matara" "cable landing station"`
- 省级清扫：`"{province}" OR "{district}" "data centre" Sri Lanka`；`"Hambantota" "data centre"`；`"Kandy" "data centre"`；`site:peeringdb.com Sri Lanka IXP`

## 官方/监管管线要点（详见 explorer-official.md）

- TRCSL 用于牌照/运营商语境、电信基础设施公告、年报与互联政策；不得仅凭电信牌照推断数据中心。
- ICTA 用于 LGN、Lanka Government Cloud、NDX、主权云政策与数字政务基础设施；SLT LGN 2.0 页确认 SLT 为 LGN 2.0 总通信与基础设施供应商，但本身不证明政府全部负载的物理数据厅。
- BOI/Port City 用于新项目发现：公告只有点名数据中心、运营商/开发商、站点与阶段才达设施级。
- 规划来源低发现率但可核验已知项目地址：UDA、OSU（One Stop Unit）、Colombo MC building applications；CEA 用于 EIA/IEE 筛查；CEB/LECO 不发布公开 DC 清单，MW/kVA 仅在有站点名来源时记录。
- 采购对政府云升级/DR/服务器房/网络服务重要：Treasury procurement notices、NPC、ePMS、UNGM、World Bank 文件；`procurement.gov.lk`/`etenders.lk` 未打开原始买方文件前按未核验处理。
- Uptime Institute 国家页（country/id/LK）列出 SLT Pitipana（Tier III Design + Constructed Facility）、Dialog Malabe（Tier III Design + Constructed Facility）、National Savings Bank Production DC（Tier III Design Documents）——A 级认证事实。
- eROC 仅用于法人注册/注册地址，不证明设施；Sri Lanka CERT|CC 为国家 CERT 角色/事件/采购语境。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场集中在 **Western Province**（Colombo District 及郊区）；无 AWS/Azure/GCP/OCI 公共区域，本地云=SLT Akaza/Dialog 云共置/Lankacom hosting/ICTA 政府云。
- **SLT-Mobitel Pitipana**：SLT 官方页 + 2018-01-16 开业（Rs. 2.4bn+、500 racks、距 HQ DC 24 km）+ Uptime 双认证——强设施（A）；DCD 佐证 500 racks（B）。
- **Dialog Malabe Data Center #2**：Uptime Tier III Design + Constructed Facility；Dialog 2017 官方新闻（托管/共置/云 + Media Hub）——强设施（A）。
- **Dialog Piliyandala**：Dialog 2021 官方新闻（全资、托管/共置/云）+ DCD 佐证（A 级启运/位置/服务）；无独立 Uptime 条目，Tier 声称 U/B。
- **Lankacom Colombo 07**：官方页列数据中心/云托管服务与地址 65C Dharmapala Mawatha（A 级服务/地址）；容量/认证 C/U。
- **MillenniumIT/LSEG Malabe**：LSEG 官方页确认 Malabe 园区（A 地址）；Daily FT/Sunday Times 2015 报道首个私有 Tier 3（80 racks、3,000 sq ft 高架地板）（B 容量/Tier）。
- **ICTA/Lanka Government Cloud**：程序 A 级；物理数据厅映射到 SLT Pitipana 合理但须逐条来源（B/U）。
- **National Savings Bank Production DC**：Uptime 设计文档认证（A）；机构/银行设施非公共共置。
- **海缆登陆站**（FALCON Lanka Bell、SMW4/SMW3/SMW5、BBG/MSC Dialog）：按海缆/关键设施计数，非商业 DC；Hambantota/Kandy/Port City 增长声称仅未来市场线索。
- 目录处理：DataCenterMap/datacenters.com/Cloudscene/Baxtel/Inflect 为 C 级线索；PeeringDB 设施推断 C 级；RIPE/APNIC 注册事实 A 级；市场报告（Mordor/6Wresearch）C 级。

## 已知设施/项目与证据状态

| 设施/项目 | 分区 | 状态与证据 |
|---|---|---|
| SLT-Mobitel National Data Center | Western（Pitipana-Homagama） | 运营中；SLT 官方 A + Uptime Tier III 双认证 A；500 racks/Rs.2.4bn 运营商自述 A/B |
| SLT HQ Data Centre / Welikada 回程枢纽 | Western（Colombo） | B 级设施/回程线索；容量 U |
| Dialog Malabe Data Center #2 | Western（Malabe） | 运营中；Uptime Tier III Design+Constructed A；Dialog 2017 官方 A |
| Dialog Data Centre Piliyandala | Western（Piliyandala） | 运营中；Dialog 2021 官方 A + DCD B；Tier 声称 U/B（无独立 Uptime 条目） |
| Lankacom 数据中心/托管服务 | Western（Colombo 07） | 服务/地址 A；容量/认证 C/U |
| MillenniumIT / LSEG Malabe | Western（Malabe） | 园区地址 A；2015 Tier 3/80 racks B |
| National Savings Bank Production DC | Western（Colombo） | Uptime 设计文档认证 A；机构设施 |
| ICTA LGN / Lanka Government Cloud | Western（全国服务） | 程序 A；数据厅位置 B/U |
| 五个海缆登陆站（SLT x3、Lanka Bell、Dialog） | Western x4 + Southern x1 | 海缆/关键设施（B/A）；非商业 DC |
| Port City Colombo 数据中心说法 | Western | U（无官方专属项目） |
| Hambantota 数据中心传闻 | Southern | U（无官方来源） |
| 其余 7 省（Central/Northern/Eastern/NW/NC/Uva/Sabaragamuwa） | 各省 | 无核验商业 DC；保留负面搜索记录 |

## 更新节奏

- 每批次：云区域缺席、Uptime 认证目录、部委名称、海缆状态、BOI/Port City 公告、采购门户、运营商页（SLT/Dialog/Lankacom/LSEG）、DCD/Daily FT/EconomyNext、Submarine Networks/Submarine Cable Map、PeeringDB。
- 省级五遍工作流：EN/SI/TA 查询 → 运营商查询 → 政府/投资/采购 → 海缆/IXP → 规划/能源/环境（UDA/OSU/CEA/CEB/LECO）。
- 待办（2026-08-12）：Dialog Piliyandala 独立 Uptime/Tier 条目；SLT HQ DC 直接页面；ICTA 政府云物理数据厅归属；Lanka Bell FALCON 与 Dialog MSC 运营状态复查；Hambantota/Port City 新项目监视；codex terra agent 分批复核后按本方法论推进。
