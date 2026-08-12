---
name: tz-datacenter-methodology
location: scripts/expansion/world/country-skills/TZ/SKILL.md
description: |
  Tanzania (TZ) parent-level methodology for data-center enumeration at region granularity (31 regions: 26
  mainland + 5 Zanzibar). Tanzania has no single public datacenter planning registry; enumeration joins TCRA
  licensing and TCRA/TS013 public-DC technical rules, NEMC EIA/EA records, LGA/Tausi building permits,
  EWURA/TANESCO power evidence, TISEZA investment/SEZ instruments, PDPC/PDPA data-residency demand, eGA
  government-DC documents, and operator pages. Supply concentrates in Dar es Salaam (Raxio TZ1, Wingu Africa,
  NIDC/TTCL, Vodacom, Tigo/Yas, Airtel); secondary government clusters are Dodoma (eGA) and Zanzibar Urban/West
  (planned/MoU leads); Pwani/Kwala SEZ and Mtwara/DARE1 are watch areas. No hyperscaler public region exists.
  Routes to explorer-official.md (regulator/power/permits pipeline) and explorer-industry.md (press/operator/cable
  pipeline).
---

# TZ · 坦桑尼亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：坦桑尼亚没有一个完整的公开数据中心规划登记册，枚举必须拼接 TCRA 许可与公共数据中心技术规则（TCRA/TS013）、NEMC 环评/审计、地方政府（Tausi 门户）建筑许可、EWURA/TANESCO 电力证据、TISEZA 投资/经济特区文书、PDPC/PDPA 数据留存义务、eGA 政府数据中心文件与运营商官方页面。供给高度集中于达累斯萨拉姆（Dar es Salaam），Dodoma 与 Zanzibar Urban/West 为政府/规划次集群。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供坦桑尼亚探索与复核批次使用。

## 入口

| 文档 | 用途 |
|---|---|
| `explorer-official.md` | 官方/监管管线：TCRA 许可与 TS013 规范、NEMC 环评、EWURA/TANESCO 电力、TISEZA/SEZ、PDPC、eGA/NIDC、建筑许可、云区域阴性对照、31 区工作流 |
| `explorer-industry.md` | 行业管线：DCD/W.Media/Developing Telecoms 等行业媒体、运营商/开发商扫库、电缆/IXP 线索、斯瓦希里语检索、31 区四遍法 |

## 核心结构事实（框定每次搜索）

1. **无单一登记册**：坦桑尼亚没有完整的公共数据中心规划登记册；枚举 = TCRA 许可 + NEMC 环评 + 地方政府建筑许可（Tausi）+ EWURA/TANESCO 电力 + TISEZA + PDPC + eGA + 运营商页面 的拼接。
2. **达累斯萨拉姆集中**：确认/高值种子为 Raxio TZ1（2026 年启用，载波中立 Tier III，800 机架 / 4,000 m2 / 6 MW IT）、Wingu Africa Tanzania（2022 年一期启用，2025 年扩至 ~3 MW）、NIDC/TTCL（2015 年建成，政府 Tier-III）、Vodacom Business、Tigo/Yas、Airtel、Aptus/Flashnet。
3. **TCRA 双重作用**：TCRA 许可数据库（Telecommunications & Internet 过滤）证明受监管实体与许可类型（NFL/NSL/ASL）；TCRA/TS013《公共数据中心最低技术要求》v2.0（2025-05）是公共 DC 技术制度定义，不是设施清单；公共 DC 需 NFL 与季度托管客户报告（A 仅当见于 TCRA 文书）。
4. **NEMC/PMS**：EIA/环境审计系统（eia.nemc.or.tz）高精度但不完整；DC 可能作为 ICT 建筑、商业/工业/SEZ 项目、变电站、备用发电机/储油或综合电信项目的一部分申报。
5. **电力分级**：EWURA 对 >1 MW 活动发许可证、<1 MW 注册；TANESCO 为国有垂直一体化公用事业；保留单位（IT MW / 设施 MW / 公用事业 MVA / 电压 / 馈线），不得把 MVA 换算为 IT MW。
6. **Dodoma 政府集群**：eGA《公共机构数据中心标准与指南》（2026-02-18 定稿）与战略计划为 A 级上下文；国家数据中心/政府云项目需设施级来源才定站点与阶段；Zanzibar Urban/West 有政府规划与 Oman Data Park MoU（2022）计划线索。
7. **无超大规模区域**：官方 AWS/Azure/GCP/OCI 列表均无坦桑尼亚公共区域；肯尼亚/南非区域仅作需求/时延上下文；本地/主权云（eGA、NIDC、Raxio、Wingu）需先映射到物理主机设施再计数。
8. **海底电缆是网络证据**：Dar es Salaam 有 EASSy、SEACOM、SEAS、2Africa（2024 激活）登陆证据；DARE1 南延（约 2028 年 RFS）为未来线索；登陆站/IXP 是网络节点，不是 DC。
9. **31 区双名制**：官方/NBS 用 Mjini Magharibi（Urban/West）、Kaskazini Unguja、Kusini Unguja、Kaskazini Pemba、Kusini Pemba；检索两个名称；Pwani/Kibaha/Kwala SEZ 是选址观察区而非已核实 DC。
10. **语言**：官方材料以英文为主；政府/本地检索用斯瓦希里语：`kituo cha data`、`kituo cha kuhifadhi data`、`hifadhi ya data`、`seva`、`chumba cha seva`、`mkongo wa taifa wa mawasiliano`。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§3/§4、explorer-industry.md §1/§4/§5）

```text
site:tcra.go.tz "public data center" OR "Minimum Technical Specifications"
site:tcra.go.tz/services/licenses Raxio OR Wingu OR TTCL OR NIDC
"TCRA/TS013" "Public Data Centers"
site:eia.nemc.or.tz Raxio OR Wingu OR TTCL OR Vodacom
"Raxio TZ1" NEMC OR EIA OR ESIA
site:tanesco.co.tz Raxio OR Wingu OR NIDC OR Vodacom
site:ewura.go.tz "data centre" OR "data center"
site:tiseza.go.tz "data centre" OR "Kwala" OR "Kibaha"
site:ega.go.tz "data centre" OR "Data Center Standards"
site:nidc.co.tz "Tier" OR "colocation" OR "cloud"
site:go.tz "data centre" "Zanzibar" OR Dodoma
site:pdpc.go.tz "data centre" OR "cross-border data transfer"
site:datacenterdynamics.com/en/news/ Tanzania "data center"
site:w.media/ "Raxio" "TZ1" Tanzania
site:developingtelecoms.com Wingu Tanzania "data centre"
"Raxio Tanzania" "6 MW" "800 racks" "4,000"
"Wingu Africa" Tanzania "Dar es Salaam"
"NIDC" OR "National Internet Data Center" Tanzania colocation OR cloud
"Zanzibar" "Oman Data Park" "data center"
"{region}" Tanzania ("data centre" OR "data center") ("MW" OR MVA OR racks)
"{region}" "kituo cha data"
"{region}" "kituo cha kuhifadhi data" OR "chumba cha seva"
"Tanzania" "cloud region" AWS OR Azure OR "Google Cloud" OR Oracle
"{operator}" "building permit" "{council}"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **TCRA**：许可数据库（sector 过滤 Telecommunications & Internet）提取被许可人法定名称/许可类型/号码/日期/地址；NFL/NSL/ASL/Content 融合许可框架；TS013 定义公共 DC 技术要求与术语。
- **NEMC/PMS**：EIA/EA 官方系统，提取 NEMC/EIA 编号、主张者、区/选区/地块、项目标题、ESIA 顾问、发电机/储油、冷却/水、公众咨询、批准日期、电网/变电站关联。
- **EWURA/TANESCO**：>1 MW 许可、<1 MW 注册；电网证据多在 TANESCO 发布/招标、EWURA 申报或 ESIA 中。
- **TISEZA**：2025 年第 6 号《投资与经济特区法》创设（合并 TIC+EPZA 职能）；Kwala SEZ（Kibaha, Pwani）为选址线索，无具名 DC 租户/许可不得计数。
- **PDPC/PDPA（2022）**：数据控制者/处理者注册与跨境传输许可 = A 级法律/需求上下文（银行、电信、医疗、政府、云客户），不是设施证据。
- **eGA/NIDC**：eGA 标准与战略计划证明政府 DC 基础设施存在并被管理（A）；NIDC 官方页称 2015 年由坦桑尼亚政府建造、Tier-III、Dar es Salaam（A 存在/服务证据）。
- **建筑许可**：Tausi 门户（tausi.tamisemi.go.tz）提供 LGA 建筑许可与占有证书服务；优先议会：Kinondoni/Ilala/Ubungo/Temeke/Kigamboni MC。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **Raxio TZ1**：官方页 2026 年启用、Dar 郊区、载波中立 Tier III、800 机架、4,000 m2、6 MW IT、33 kV 供电（A 存在/容量声明；W.Media/DCD 为 B）；核实 TCRA/NEMC/LGA/TANESCO/Uptime。
- **Wingu Africa Tanzania**：官方页确认坦桑尼亚运营与载波中立 colo/互联/云连接（A）；Mbezi/工业区地址与 3 MW/二期为媒体/目录线索（B/C）。
- **NIDC/TTCL**：A 存在/历史；DCD 2016 使用率报道为 B 历史背景。
- **Vodacom Business**：目录列 Laibon Rd / Lusinde Rd 为 C 线索；Tigo/Yas/Airtel/Halotel/Zantel 设施是电信核心而非商业 colo，除非官方页/TCRA/议会证据确认。
- **状态动词纪律**：`announces/plans/MoU/expected` = planned；`land acquired/breaks ground/financing secured` = under construction；`opened/launched/operational/ready for service` = operational 候选；`Tier III designed/standard` ≠ Uptime 认证。
- **电缆**：2Africa 坦桑尼亚段 2024 激活（Airtel/Telesonic 报道）；DARE1 南延 2025-09 宣布、约 2028 RFS，保持未来线索。

## 来源分级

- **A** = 主要/官方/法律来源：TCRA 许可注册或公共 DC 技术规范、NEMC EIA/EA、EWURA/TANESCO、TISEZA/SEZ 文书、PDPC/法律文本、eGA/政府文件、LGA/Tausi 许可记录、官方云商位置页、运营商官方设施页、Uptime Institute 奖项记录。
- **B** = 强二级：DCD、W.Media、Capacity、Connecting Africa、Developing Telecoms、ITWeb Africa、TanzaniaInvest、Daily News/The Citizen/Guardian 商业报道、行业协会、厂商案例、PeeringDB/TIX/Submarine Cable Map 网络节点存在。
- **C** = 弱线索：市场报告、聚合器/目录条目、社交帖子、旧 MoU、无支撑容量声明、未指明物理计算/托管设施的本地文章。
- 分级到每个数据点：同一设施可含 A 级运营商存在、B 级媒体容量、C 级目录地址；只有至少一个 A 或强 B 来源指明具备计算/托管/colo/云/服务器基础设施功能的物理设施时才提升为计数设施。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL 中的 TZ 记录与种子（Raxio、Wingu、NIDC/TTCL、Vodacom、Tigo/Yas、Airtel、Aptus/Flashnet、eGA/Dodoma、Zanzibar 政府）。
2. 对每个种子解析：运营商页面 → TCRA、NEMC、议会/Tausi、TANESCO/EWURA、Uptime、eGA、TISEZA 验证。
3. 依次扫描 Dar es Salaam（详尽）、Dodoma、Zanzibar Urban/West、Pwani/Kwala、Mtwara/DARE1、次线城市，然后按精确 31 区模板执行阴性扫描并记录低产区显式阴性证据。
4. 输出 schema：`{country_code: TZ, country_name: Tanzania, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；无项目区域 `no_projects: true`。
5. 不动 explorer-*.md，NO-DELETION。

## 待办（2026-08-12）

- [ ] Raxio TZ1：追踪 2026 启用状态、TCRA NFL、NEMC、LGA 许可、TANESCO 33 kV、Uptime 奖项。
- [ ] Wingu：用 Wingu 一手材料核实 3 MW/二期/地址。
- [ ] Dodoma 国家数据中心与 eGA 共享设施：寻找设施级站点/阶段/容量证据。
- [ ] Zanzibar Oman Data Park / 政府 DC：核实采购/施工/运营证据，区分 planned。
- [ ] Kwala SEZ：监控 TISEZA/NEMC/TANESCO/议会中的具名 DC 租户。
- [ ] DARE1 南延：作为 ~2028 未来线索跟踪。
- [ ] 云区域阴性对照与 2Africa/DARE1 电缆状态：每次运行复查。
