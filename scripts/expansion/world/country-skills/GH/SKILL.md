---
name: gh-datacenter-methodology
location: scripts/expansion/world/country-skills/GH/SKILL.md
description: |
  Ghana (GH) parent-level methodology for data-center enumeration at region granularity (16 regions). Ghana
  has no national data-centre register and no unified public database for local building permits; the
  official chain is operator/SPV name -> MMDA planning/building permit -> EPA environmental permit/EIA ->
  Energy Commission power permit/register -> NCA telecom/submarine/managed-services licence -> DPC
  registration -> NITA/ministry or operator confirmation. Market is commercially Greater Accra-led:
  Equinix AC1/MDXi Appolonia, Onix Accra #1 (Tier IV), PAIX Accra (RackAfrica legacy), Africa Data
  Centres/Onix Accra pipeline (10 MW initial/30 MW expandable, not yet commissioned); Ashanti is not blank
  - Uptime records NITA Ghana E-Gov Cloud Data Center in Kumasi plus Primary Ghana National Data Center
  Accra. NCA lists legacy cables SAT-3/MainOne/WACS/Glo/ACE; Bayobab/MTN announced 2Africa Accra landing;
  Equiano does not land in Ghana. No hyperscaler public cloud region. Announced MW != operational MW.
  Routes to explorer-official.md (regulators/permits/power/government chain) and explorer-industry.md
  (operators/connectivity/press/directory chain).
---

# GH · 加纳数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：加纳没有国家数据中心登记册，也没有统一的本地建筑许可公共数据库；官方证据链为：运营商/SPV 名 → MMDA 规划/建筑许可 → EPA 环境许可/EIA → 能源委员会电力许可/登记 → NCA 电信/海缆/托管服务许可 → DPC 注册 → NITA/部委或运营商确认。市场以商业性大阿克拉（Greater Accra）为主导：Equinix AC1/MDXi Appolonia、Onix Accra #1（Tier IV）、PAIX Accra（RackAfrica 遗留）、Africa Data Centres/Onix Accra 管线（初始 10 MW/可扩 30 MW，未投运）；**Ashanti 并非空白**——Uptime 记录 NITA 库马西（Kumasi）加纳 e-Gov 云数据中心 + 阿克拉主加纳国家数据中心。NCA 列遗留海缆 SAT-3/MainOne/WACS/Glo/ACE；Bayobab/MTN 宣布 2Africa 阿克拉登陆；**Equiano 不在加纳登陆**。无超大规模公共云区域。宣布 MW ≠ 运营 MW。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供加纳探索与复核批次使用。

## 入口

| 文档 | 用途 |
|---|---|
| `explorer-official.md` | 官方/监管管线：NCA、能源委员会/电网、EPA、MMDA 规划许可、DPC/NITA/部委、GIPC/GFZA、云区域阴性对照、16 区官方覆盖图、验证配方 |
| `explorer-industry.md` | 行业管线：运营商/设施普查（Equinix/Onix/PAIX/NITA/ADC）、超大规模状态、海缆/IXP、行业媒体、目录处理、逐区发现图 |

## 核心结构事实（框定每次搜索）

1. **无国家登记册**：没有国家数据中心登记册，也没有统一的本地建筑许可公共数据库；官方链 = 运营商/SPV 名 → MMDA 规划/建筑许可 → EPA 环境许可/EIA → 能源委员会电力许可/登记 → NCA 电信/海缆/托管服务许可 → DPC 注册 → NITA/部委或运营商确认。
2. **16 区**：Ahafo, Ashanti, Bono, Bono East, Central, Eastern, Greater Accra, North East, Northern, Oti, Savannah, Upper East, Upper West, Volta, Western, Western North；仅当每区都已检索或带日期/查询注释显式 `no_projects: true` 时区域覆盖才算完整。
3. **大阿克拉商业集群**：Equinix AC1/MDXi Appolonia（Appolonia 工业园 Benin Boulevard 1 号地块，运营中载波中立 colo/IBX，A 存在/地址）、Onix Accra #1（Amrahia，Tier IV，170 机架可扩 680，部分太阳能，DCD 称启用时 12 MW）、PAIX Accra（Ring Road Central 42 号，RackAfrica 遗留，Africa50 报道扩至 1.2 MW）、Africa Data Centres/Onix Accra 管线（Cassava，初始 10 MW/可扩 30 MW，2024 与 Onix 合作——pipeline/construction/partnered，未经运营商投运源不得记运营容量）。
4. **Ashanti 非空白**：Uptime Institute 记录 NITA **Ghana E-Gov Cloud Data Center（Kumasi）** 与 **Primary Ghana National Data Center Accra**；Ashanti 标记为政府 DC 存在、商业 colo 未确认。
5. **别名去重**：Equinix AC1 = MainOne MDXi Appolonia；Onix Accra #1 = Onix Data Centres Ghana = Ngoya Etix DC (Ghana) Ltd；PAIX Accra = RackAfrica 遗留；NITA Accra = Primary Ghana National Data Center Accra；NITA Kumasi = Ghana E-Gov Cloud Data Center。
6. **NCA 不是 DC 许可机构**：NCA（Act 769/775）用于连通性邻接证据——海缆登陆许可（含登陆站）、公共数据/互联网服务授权、卫星/VSAT、基础设施/塔站许可、频谱、托管服务咨询；NCA 海缆页列 SAT-3/MainOne/WACS/Glo/ACE（2Africa 较新，用 Bayobab/MTN 官方后查 NCA 许可痕迹）。
7. **电力链**：能源委员会（Act 541）Bulk Customer Permit、Siting Permit、Construction Permit 与 Bulk Customer Register（持证人/地址/业务性质/许可号/日期）；ECG（南部分配）、NEDCo（北部）、GRIDCo（输电）、PURC（电价）、VRA（发电）。
8. **EPA 链**：Act 490/LI 1652 制度要求重大影响项目注册并获环境许可/EIA；EPA 许可/EIA 记录是技术容量线索的最佳官方来源（发电机数/MW、储油、冷却、用水、场地平面、阶段）。
9. **无超大规模区域 + Equiano 排除**：官方 AWS/Azure/GCP/Oracle 列表无加纳区域（每次批次复查）；Equiano 路由证据不含加纳，不得创建加纳记录；宣布 MW ≠ 运营 MW（状态梯：rumour < MoU < announced < land acquired < permit applied < permit granted < construction started < commissioned < operational）。
10. **连通性/IXP**：2Africa 阿克拉登陆（Bayobab 官方）；GIX、Accra-IX、LINX Accra（LINX 称跨 Onix/PAIX/Digital Realty——核实 Digital Realty 命名/托管映射再单独建记录）；海缆/IXP 记录是 DC 邻接线索，不自动构成商业 DC 记录。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§8、explorer-industry.md §1/§3/§7）

```text
site:nca.org.gh "Submarine Cable Landing" Ghana
site:nca.org.gh "data centre" OR "data center" OR datacentre
site:nca.org.gh "landing station" Ghana "{operator}"
site:energycom.gov.gh "{operator}" "Bulk Customer" OR "EC_BCP"
site:energycom.gov.gh "{operator}" "Siting Permit" OR "Construction Permit"
"Bulk Customer Register" Ghana "{company}"
site:ecggh.com "{site}" "data centre" OR substation OR "power supply"
site:gridcogh.com "{site}" substation OR transmission OR MVA
site:epa.gov.gh "data centre" OR "data center" OR datacentre
site:client.epa.gov.gh "{operator}" OR "{SPV}"
"EPA Ghana" "environmental permit" "data centre"
site:{assembly-domain} "data centre" OR "building permit" "{operator}"
site:nita.gov.gh "data centre" OR "Kumasi" "cloud"
site:uptimeinstitute.com Ghana NITA "Data Center"
site:moc.gov.gh "data centre" OR "digital centre"
site:gdcl.gov.gh OR site:adc.gov.gh "data centre" OR "server room"
site:dataprotection.org.gh "{operator}"
site:gipcghana.com OR site:gipc.gov.gh "data centre"
site:gfza.gov.gh "data centre" OR "ICT" "enterprise"
"Appolonia" "data centre" Ghana
"Amrahia" "data centre" Ghana
"Ring Road Central" "data centre"
"Ghana" "data centre" "{operator}" launch OR inaugurated OR operational OR "Tier III" OR "Tier IV"
"Ghana" "AWS region" OR "Azure region" OR "Google Cloud region" OR "Oracle Cloud region"
"Equiano" Ghana site:cloud.google.com OR site:submarinenetworks.com
"{region}" Ghana "data centre" OR "data center" OR "server room"
"{region}" Ghana "environmental permit" "data centre" OR "bulk customer" "data centre"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **NCA**（nca.org.gh，Act 769/775）：非 DC 许可机构；海缆登陆页（A 线索源，含登陆站许可范围与遗留提供商）、公共数据服务授权、托管服务咨询、频谱、类型批准（设备级，不证明设施）。
- **能源委员会**（energycom.gov.gh，Act 541）：Bulk Customer/Siting/Construction Permit；Bulk Customer Register 暴露持证人/地址/业务性质/许可号/日期；DC 可能以大宗电力客户、自发电/孤岛发电、可再生能源项目或供电基础设施许可出现；备用柴油与太阳能是最可能的官方钩子。
- **EPA**（epa.gov.gh，Act 490/LI 1652）：环境许可/EIA 记录——技术容量线索最佳官方来源；每次批次检查现行继任文书。
- **MMDA 规划许可**：开发/建筑许可归 Metropolitan/Municipal/District Assemblies（AMA、TMA、KMA、La Dade-Kotopon、Adentan、La Nkwantanang-Madina、Ga East、Ga West、Kpone-Katamanso、Tamale 等）；提取 MMDA、地块/LR/GR 号、申请人/SPV、用途、许可决定/日期、建筑面积、发电机/机械装置。
- **DPC/NITA/部委**：DPC（Act 843 注册，公司级证据）；NITA 数据中心项目页 + Uptime NITA 客户页（阿克拉与库马西两个奖项，A）；MOC（moc.gov.gh）、Ghana Digital Centres Ltd/Accra Digital Centre。
- **GIPC/GFZA/RGD**：外商投资注册、自由区企业许可（Tema Free Zone、Appolonia、Dawa）、SPV 名称/所有权解析。
- **云区域**：官方 AWS/Azure/GCP/Oracle 页 = 无加纳区域（A 阴性对照）；云办公室/伙伴节点/缓存/CDN PoP/边缘节点是生态注释，非 DC 设施。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **Equinix AC1**：官方页给地址/设施空间（A 存在/地址）；Uptime/贸易记录支持 Tier III 历史；机架数等第三方容量 B/C。
- **Onix Accra #1**：Onix 官方称 Tier IV colo（A 存在/层级）；Uptime 记录 ONIX Accra #1；AIIM 案例 170 机架可扩 680 + 部分太阳能；DCD 12 MW——机架/MW 字段按来源标注。
- **PAIX Accra**：官方确认加纳/阿克拉存在（A 运营商）；Africa50 报道扩至 1.2 MW（B 扩张容量）；目录细节 C。
- **Africa Data Centres Accra**：ADC/Cassava 宣布初始 10 MW 可扩 30 MW（A-/B 宣布项目与容量）；2024 DCD 报道 Onix 合作；状态 pipeline/construction/partnered 直到运营商投运源。
- **NITA 阿克拉/库马西**：Uptime 奖项页（A）；政府/非商业（库马西除非 NITA 展示商业 colo）。
- **MTN/Bayobab/Telecel/AT/NGIC**：企业/网络设施，通常非公开零售 colo；逐站经运营商页/NCA/PeeringDB/IXP 验证。
- **媒体分级**：DCD（B+）、Capacity Media（B）、Connecting Africa（B）、tech.africa/TechAfrica News（B）、Telecom Review Africa/Developing Telecoms/ITWeb Africa（B）、Business & Financial Times（B）、Graphic Business（B）、GhanaWeb/MyJoyOnline/Citi/GNA（B-/C）、Africa50/AIIM/Cassava/ADC 投资方站点（A-/B）、Xalam/Arizton/Mordor 市场报告（C）。
- **目录纪律**：Baxtel/DataCenterMap/DataCenters.com/Data Center Platform 为 C；不摄入仅目录设施（需运营商/监管/Uptime/许可/强媒体之一）；警惕别名重复（MDXi vs AC1、RackAfrica vs PAIX、Ngoya Etix vs Onix）；目录 MW/机架记为 claimed_capacity。
- **行业机构**：Uptime 国家/客户检索是核心认证来源；GIX/Accra-IX/LINX Accra 成员表识别网络运营商；未验证到专门加纳 DC 协会，不要虚构。

## 来源分级

- **A** = 主要/官方：NCA 许可/服务页与咨询、能源委员会许可/许可登记、EPA 许可/EIA 记录、MMDA 开发/建筑许可、NITA 或部委记录、DPC 注册、GIPC/GFZA 注册、官方云区域页、Uptime Institute 奖项页。
- **A-** = 证明具名站点/位置/状态的官方运营商页或官方新闻稿（非监管申报）；设计容量谨慎使用。
- **B** = 强二级：成熟行业媒体、投资者/开发商公告、对等/海缆行业机构、可信加纳商业媒体。
- **C** = 仅线索：市场报告、目录、社交帖子、无源容量表、SEO 页、无法绑定许可/官方登记/运营商页的主张。
- 分级到具体主张：同一设施可 A 存在、B 宣布 MW、C 调试状态；状态梯不可跳级。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL 中的 GH 记录与种子（Equinix AC1、Onix Accra #1、PAIX、ADC/Onix 管线、NITA Accra/Kumasi、MTN/Bayobab 2Africa）。
2. 去重别名后再计数设施；按物理位置指派 division（Appolonia/Amrahia/Ring Road/Tema = Greater Accra；NITA Kumasi = Ashanti），不用总部。
3. 每个命名设施按序寻求许可证据：EPA/EIA → MMDA 许可 → 能源委员会 bulk customer/自发电/选址/施工许可 → NCA 电信/登陆站证据 → DPC/公司注册 → 运营商/NITA 官方页 → Uptime。
4. 拆分事实：`status`、`capacity_mw`、`announced_capacity_mw`、`racks`、`tier`、`address`、`region`、`operator`、`SPV`、`evidence_date`、`source_urls`、`evidence_grade`；容量优先许可/发电机组/电力连接记录而非媒体。
5. 逐区扫描全部 16 区（大阿克拉详尽、Ashanti 政府 DC、其余阴性默认），适当输出 `no_projects: true`；每次批次重跑云区域与 Equiano 排除。
6. 输出 schema：`{country_code: GH, country_name: Ghana, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`。不动 explorer-*.md，NO-DELETION。

## 待办（2026-08-12）

- [ ] ADC Accra：每次批次复查施工/投运状态（10 MW/30 MW 为 announced_capacity）。
- [ ] Onix/PAIX/Equinix 精确运营容量：寻找许可或运营商技术规格表。
- [ ] 2Africa 阿克拉登陆：Bayobab/MTN 官方证据 + NCA 许可痕迹。
- [ ] NITA 库马西/阿克拉：确认奖项与设施详情（政府 DC）。
- [ ] LINX Accra 的 "Digital Realty" 命名：核实是否为运营设施、命名/伙伴错误或他人托管接入点。
- [ ] 云区域阴性对照与 Equiano 排除：每次运行复查。
