---
name: so-datacenter-methodology
location: scripts/expansion/world/country-skills/SO/SKILL.md
description: |
  Somalia (SO) parent-level methodology for data-center enumeration at region granularity (18 regions;
  Northwest = Woqooyi Galbeed incl. Sahil/Berbera note). Somalia has no public data-centre planning
  register, no functional planning-permit database, and no unified national grid; enumeration joins NCA
  licensing (Communications Act 2017, SOMCERT, SoIXP), MOCT federal announcements, NIRA identity
  infrastructure, SOMINVEST studies, World Bank/UNDP/IFC/TaiwanICDF documents, operator official pages
  (Hormuud, Somtel, Telesom, Golis, NationLink, Wingu, SomaliREN), landing stations (DARE1, Somcable
  2Africa), and aggregators. Market is tiny and telecom-led; only confirmed commercial carrier-neutral colo
  is Wingu Berbera SL01. Federal NDC (Mogadishu) under construction→near completion; Somaliland NDC
  (Hargeisa) ground broken Sep 2025. Admin attribution (federal/Somaliland/Puntland) mandatory. No
  hyperscaler region. Routes to explorer-official.md (regulator/government/donor pipeline) and
  explorer-industry.md (press/operator/interconnection pipeline).
---

# SO · 索马里数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：索马里没有公共数据中心规划登记册、功能性规划许可数据库或统一国家电网；枚举必须拼接 NCA 许可（2017 通信法、SOMCERT、SoIXP）、MOCT 联邦公告、NIRA 身份基础设施、SOMINVEST 研究、世行/UNDP/IFC/TaiwanICDF 文件、运营商官方页（Hormuud、Somtel、Telesom、Golis、NationLink、Wingu、SomaliREN）、登陆站（DARE1、Somcable 2Africa）与聚合目录。市场极小且电信主导；唯一确认的商业载波中立 colo 为 Wingu Berbera SL01。联邦国家数据中心（摩加迪沙）在建→接近完工；索马里兰 NDC（哈尔格萨）2025-09-22 破土。**行政归属（联邦/索马里兰/邦特兰）必填**。无超大规模区域。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供索马里探索与复核批次使用。

## 入口

| 文档 | 用途 |
|---|---|
| `explorer-official.md` | 官方/监管管线：NCA、MOCT、NIRA、SOMINVEST、世行/UNDP/IFC/TaiwanICDF、电力（BECO/SESRP）、云区域阴性对照、官方/运营商种子、18 区策略 |
| `explorer-industry.md` | 行业管线：行业媒体（DCD/Bloomberg/Techpoint）、本地媒体（SONNA/Goobjoog/Garowe）、运营商扫库、目录/IXP/海缆、索马里语/阿拉伯语检索、18 区四遍法 |

## 核心结构事实（框定每次搜索）

1. **无登记册/无统一电网**：没有公共国家数据中心规划登记册、功能性的国家规划许可数据库或统一国家电网（电力按城市由私有 ESP 提供）；没有可在线检索的 NEMA/NCA 式国家建筑/环评批准登记册。
2. **18 区 + 行政三重结构**：`Northwest` = Woqooyi Galbeed（索马里兰自分为 Maroodi Jeex/哈尔格萨 与 Sahil/柏培拉；Wingu Berbera SL01 物理上在 Sahil，归 Northwest 并加 Sahil 注释）；Togdheer/Awdal 归索马里兰；Sanaag/Sool 争议（索马里兰/邦特兰/SSC-Khatumo）；Bari/Nugaal/Mudug 归邦特兰。**必须声明搜索的是哪套行政记录且不混并**。
3. **市场极小且电信主导**：唯一确认的商业载波中立 colo 是 **Wingu Berbera SL01**（一期 2021-02-13 投运，2022-02 公告 ready for service；Batalaale Beach Zone 20/Beach Road；PeeringDB fac/13450；Somcable ASN 37425）——但 Wingu 当前主页未把索马里兰列入活跃市场，须直接向 Wingu 复核当前状态/容量。
4. **联邦国家数据中心（摩加迪沙/Banaadir）**：SCALED-UP（世行 P168115）采购（RFB SO-MOF-374369-GO-RFB，2023/24）、2024-04 部长巡视在建、2025-05 接近完工、2025-04 设施工程师 REOI（SO-MOF-425074-CS-INDV）；容量未公开；2026-08-07 的 "plans" 声明与前期记录冲突，按下一阶段/并行规划处理（B/C），勿降级物理站点证据。
5. **索马里兰政府数据中心与网络安全中心/NDC（哈尔格萨/Northwest）**：2025-09-22 在 MICT 破土（TaiwanICDF 主源 A；AllAfrica/Horn Diplomat B）；索马里兰首个政府数据中心，含服务器设施、网络安全管理系统、S-Road/e-治理联动；报道约 USD 1M。
6. **组合声明 ≠ 设施记录**：Hormuud "11 个数据中心 / ~10 MW 合计"（CEO 经 Bloomberg/DCD，B）与 Somtel "3 Data Centers" 只证明组合/服务类别；逐站点记录需要逐站证据（地址/MW/机架）。Hormuud 95% 白天太阳能、10 MW 均为组合级/能源结构主张。
7. **登陆站/IXP 不是 DC**：DARE1 登陆站（摩加迪沙，Hormuud 2022-11 完工）、Somcable 2Africa（柏培拉，2022-05）、SoIXP/MogIX（PCH 2072，2018-11-20 建立，NCA 管理）仅作互联锚点；5G 启用（Hormuud 2024-03、Somtel 2024-01、Telesom 2024-01）不是设施。
8. **无超大规模区域**：AWS/Azure/GCP/OCI 官方列表无索马里区域；联邦数据主权推动（NDC）是激励信号，不是设施记录。
9. **语言**：英文为主；索马里语（xarunta xogta=数据中心、kaydinta xogta=数据存储、seefar=服务器、qolka seefaraha=服务器机房、xog-ballaarinta=数字化、wasaaradda isgaarsiinta=通信部、maamulka isgaarsiinta=通信管理局）与阿拉伯语（مركز البيانات）用于政府站与本地媒体二线检索。
10. **安全背景**：Al-Shabab 袭击电信基础设施（Hormuud 2024 年有员工遇害）；未验证的容量/状态主张须谨慎并做日期检查。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§2/§4/§5、explorer-industry.md §1/§2/§4/§5）

```text
site:nca.gov.so "data centre" OR "data center" OR datacentre
site:nca.gov.so licence "{operator}"
site:moct.gov.so "National Data Center" OR "data centre" OR "cloud"
site:sominvest.gov.so "data centre" OR ICT
site:worldbank.org Somalia "data centre" OR "digital ID" OR ABIS
"SO-MOF-374369-GO-RFB" OR "SO-MOF-425074-CS-INDV" OR "P168115" "Data Centre" Somalia
site:govsomaliland.org "data centre" OR "National Data Center"
site:moiid.govsomaliland.org "data centre" OR Wingu
site:mof.pl.so "data" OR ICT tender
"Somaliland" "Government Data and Cybersecurity Center" MICT
site:beco.so "data centre" OR "large customer"
site:sesrp.moewr.gov.so tender "power plant"
"{operator}" Somalia "data centre" OR "data center" MW
"Hormuud" "data centre" OR "11 data centres"
"Somtel" "3 Data Centers" colocation
"Wingu" Berbera "data centre" OR "carrier-neutral"
site:peeringdb.com/fac/13450 Wingu
site:somaliren.org "Data Center"
site:datacenterdynamics.com/en/news/ Somalia "data center"
"{region}" Somalia "data centre" OR "data center" OR datacentre
"{city}" "xarunta xogta" OR "kaydinta xogta"
"{city}" "مركز البيانات" الصومال
"Somalia" "cloud region" OR "public cloud" AWS OR Azure OR Google OR Oracle
```

## 官方/监管管线要点（详见 explorer-official.md）

- **NCA**（nca.gov.so，2017 通信法）：频谱/运营商许可（Hormuud 2022-11 首个国家频谱许可）、SOMCERT、IXP 促成、海缆监管（NCA-IFC 框架 2024-09、海缆登陆条例咨询 2025）；SoIXP 是互联锚点。
- **MOCT**（moct.gov.so）：联邦 ICT 部，国家数据中心项目业主；2024-04 巡视（在建）、2025-05 接近完工、2025-04 设施工程师 REOI（运营准备信号）；2026-08 "plans" 声明按扩张/下一阶段处理。
- **NIRA**（nira.gov.so）：HUBIYE/eAqoonsi/CDS 国家数字身份基础设施（世行 Scaled-UP 支持；2025-08-18 摩加迪沙 Shangani/Boondheer 试点）；ABIS 为独立执法生物识别线索（FBI RFI：Aden Adde 国际机场安全设施，2,000,000 十指记录 + 50,000 潜在记录 + 二级备份服务器，B/C）——身份数据中心归政府/身份类别，不得转为商业 DC 记录。
- **SOMINVEST**：ICT 部门研究（A 研究本身，市场框架而非设施清单）；世行 2022 数字经济诊断（A）；UNDP 数字转型（B/A）；索马里国家转型计划/数字经济战略搜索可点名规划 DC/政府云投资。
- **电力**：碎片化电网/私有 ESP 模式；BECO（摩加迪沙，8 MWp 太阳能）；SESRP（Daynile/Jazeera 55 MWp AC 太阳能 + 160 MWh BESS；GECO 加尔卡约 3.5 MWp + 7 MWh）——功率基础设施不是 DC 容量；MWp/MWh 与 IT 负载区分。
- **云区域**：AWS/Azure/GCP/OCI 无索马里区域（A 阴性对照）；主权/政府云（联邦 NDC、索马里兰 e-治理、运营商企业云）另记。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **Hormuud**：摩加迪沙核心（Banaadir）；组合 11 DC/~10 MW、95% 白天太阳能（CEO 引语 B/A-）；DARE1 登陆站（互联锚点）；首个频谱许可；5G 2024-03；勿从组合主张铸造 11 条记录。
- **Somtel FGC / Somtel（Dahabshiil 集团）**：总部哈尔格萨；FGC 页提供 colocation；网络页称 "3 Data Centers" 与登陆点（摩加迪沙、博萨索、Wajaale、吉布提、蒙巴萨 + 规划柏培拉 2025）；首个 5G 2024-01；逐站验证 3 个 DC。
- **Telesom**：哈尔格萨（Northwest）；2024-01-01 索马里兰首个 5G；集团含 Somgas/TEC/Dara Salaam Bank；e-治理服务伙伴；DC 专用证据薄。
- **Golis Telecom**：博萨索 HQ（Bari），加尔罗韦（Nugaal）、加尔卡约（Mudug）、Qardho、Erigavo（Sanaag）；博萨索-加尔卡约 ~750 km 骨干；DC 专用证据薄。
- **NationLink**：摩加迪沙（1997 年创立，2022 约 16% 份额），南部至 Kismayo；DC 证据薄。
- **SomaliREN**：摩加迪沙 Hodan 区 Taleh 路 TCC 大楼（Banaadir）；教育/科研网络 DC（AS327764，2026 年 33 成员），记教育网络类别非商业 colo。
- **Wingu Berbera SL01**：唯一确认商业载波中立 colo；2021-02-13 一期投运；与 Somcable 2Africa 登陆和柏培拉港/SEZ 联动；当前状态/容量须直接复核。
- **目录纪律**：datacentermap/Baxtel/OCOLO/DataCenterPlanet/datacenters.com 为 C；PeeringDB 仅作地址/互联佐证；聚合器常错置城市与过期容量。

## 来源分级

- **A** = 主要/官方/法律：NCA 许可/监管、MOCT 部委公告或招标、NIRA/身份计划页面、SOMINVEST 部门研究、世行/UNDP/IFC 项目文件、TaiwanICDF 项目页（索马里兰政府工程）、运营商官方页或新闻稿（Hormuud/Somtel/Telesom/Golis/Wingu/SomaliREN）、官方云商区域列表。
- **B** = 强二级：引述官方公告的行业媒体（DCD、SONNA、Goobjoog、Garowe Online、AllAfrica/Horn Diplomat 转载）、可信厂商/发展伙伴新闻稿、仅用于互联/地址佐证的 PeeringDB/IXP 记录。
- **C** = 弱线索：无支撑聚合条目、社交帖子、旧 MoU、市场报告片段、抓取目录、无设施/所有者/物理位置/状态证据的本地报道。
- 容量：索马里设施无公开设施级 IT 负载数字；记录任何 MW/MVA/MWh 需带单位与来源；区分 MW 总功率、MWp 发电、MWh 储能、IT 负载。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL 中的 SO 记录与种子（联邦 NDC、索马里兰 NDC、Wingu SL01、Hormuud/Somtel 组合主张、SomaliREN、NIRA、ABIS）。
2. 每区四遍法：①行业媒体/厂商遍 ②运营商遍（Hormuud/Somtel/Telesom/Golis/NationLink/Wingu/SomaliREN/Somcable/NIRA）③官方遍（NCA/MOCT 联邦；govsomaliland/moiid 索马里兰；mof.pl.so/Garowe Online 邦特兰；捐助者文件）④互联/聚合遍（SoIXP、DARE1/2Africa、PeeringDB、Baxtel 等）。
3. 高价值项（联邦 NDC、索马里兰 NDC、Wingu SL01、Hormuud 组合、Somtel 3-DC）须经官方/运营商一手来源验证；解析行政归属（联邦 vs 索马里兰 vs 邦特兰；Northwest/Sahil 细节）后再去重。
4. 输出 schema：`{country_code: SO, country_name: Somalia, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`（notes 必含行政归属与单位）；阴性区完成四遍法后 `no_projects: true`。
5. 不动 explorer-*.md，NO-DELETION。

## 待办（2026-08-12）

- [ ] Wingu Berbera SL01：直接向 Wingu 复核当前运营状态与容量。
- [ ] 联邦 NDC：从 MoF/世行一手采购与合同授予记录确认完成/投运日期；厘清 2026-08 "plans" 声明。
- [ ] 索马里兰 NDC：跟踪 MICT/TaiwanICDF 施工与 ISO/IEC 27001 支持进展。
- [ ] Hormuud 11-DC 组合：逐站寻找地址/MW/机架证据。
- [ ] Somtel "3 Data Centers"：逐站验证物理站点。
- [ ] NIRA/ABIS：寻找 SAM.gov 主源通知；确认身份设施细节。
- [ ] 云区域阴性对照与 Uptime 记录：每次运行复查。
