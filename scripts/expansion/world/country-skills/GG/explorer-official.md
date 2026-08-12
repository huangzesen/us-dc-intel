# GG Explorer Official — 根西岛（Guernsey）数据中心枚举：官方/监管来源方法学

日期 Date: 2026-08-12 · 范围 Scope: 根西岛 GG（Bailiwick of Guernsey，英国王室属地）。Manifest 校验：`world-manifest.jsonl` 中 GG 的 `subnational_type` 为 `country`，`divisions` 精确为 `["Guernsey"]`。本文件按唯一 division `Guernsey` 入库；教区、Alderney、Sark、Herm 只是覆盖检查字段，不是 manifest division。

角度 Angle: **官方/监管方法学**。目标是用政府规划、电信监管、电力、金融服务监管、数据保护、采购、公司登记和运营商官方材料确认根西岛运营中、拟建或已停滞的数据中心/托管设施。

## 0. 已核实结构事实（Verified structural facts）

- 根西岛是英国王室属地，不属于英国本土或欧盟；有自己的规划、电信、电力、金融服务和数据保护体系。
- Manifest 只有一个 division：`Guernsey`。采集字段中可额外记录 parish/island：St Peter Port、St Sampson、Vale、Castel、St Saviour、St Andrew、St Martin、St Peter in the Wood、Forest、Torteval，以及 Alderney、Sark、Herm。
- States of Guernsey 的规划 Webmap 说明：2020 年以来的 Planning and Building Control applications 可通过 Webmap 查询；2009-04-06 以来的信息可通过 Planning Websearch / Building Control Websearch 查询。
- GCRA 官方 licences 页列出 JT (Guernsey) Ltd (formerly Wave Telecom) 和 Sure (Guernsey) Limited 等电信持牌方；这是运营商名册，不是设施名册。
- JT 官方企业页确认其 Jersey 和 Guernsey primary data centre sites，并说明 ISO/IEC 27001、PCI-DSS、SOC2 认证、72 小时柴油发电备份、N+N 空调等服务特征。
- Sure 官方企业页确认 Guernsey Data Centre：Tier III site、24 小时安保、独立数据大厅/笼位/共享托管空间、inter-island connectivity、2MW IT load、remote hands。
- States of Alderney 官方材料在 2026 年发布 data-centre expression of interest；现阶段是探索/EOI，不是已建成设施。
- ODPA 2026 年说明：欧盟委员会在 2024 年 1 月确认 Bailiwick 继续具有充分性地位；ODPA 还提供 cloud-based services / processor guidance。GFSC Cyber Risk 页说明受监管 firms 必须按 Cyber Security Rules and Guidance 管理信息安全、数据隐私和服务可用性风险。

## 1. 可靠性分级（Reliability grades）

- **A = 官方/一手来源**：States of Guernsey 规划 Webmap / Planning Websearch / gov.gg 公告与议会文件、States of Alderney 官方公告与规划材料、GCRA licences/cases、Guernsey Electricity、Alderney Electricity、GFSC、ODPA、Guernsey Registry / portal.guernseyregistry.com、JT/Sure 官方数据中心页、AWS/Azure/GCP/OCI 官方区域页。
- **B = 强二级来源**：Guernsey Press、Bailiwick Express、BBC Channel Islands、ITV Channel、Data Center Dynamics、The Register、Channel Eye、Island FM、Guernsey Finance。B 级可证明报道存在，但设施入库仍需 A 级物理或运营证据。
- **C = 目录/聚合/SEO 来源**：DataCenterMap、Datacenters.com、Cloudscene、Data Center Platform、ColocationM、主机商 landing pages、无地址云经销商页。C 级只做 seed，不单独入库为 confirmed facility。

分级原则：运营商官方页可 A 级确认“该运营商在 Guernsey 提供数据中心/colo 服务”；若需要精确地址、机房数量、面积或电力容量，必须用同一运营商产品文档、规划记录、GCRA/GEL 文件或其他一手材料补强。目录地址不得升级，除非被 A 级来源复核。

## 2. A 级来源与用法（Official sources and workflow）

### 2.1 States of Guernsey 政府与规划

- 主站：https://www.gov.gg/
- Planning Applications & Decisions：https://www.gov.gg/article/163206/Planning-Applications--Decisions
- Planning Webmap：https://digimap-planning.gov.gg/
- Planning Websearch：https://planningexplorer.gov.gg/portal/servlets/ApplicationSearchServlet

用途：确认建筑/用途变更、发电机、机房、变电站、冷却设备和许可条件。先查精确设施地址，再查 parish/road name，再查申请人。

可用查询模板：
```text
site:gov.gg "data centre" "Guernsey"
site:planningexplorer.gov.gg "data centre"
site:planningexplorer.gov.gg "server room"
site:planningexplorer.gov.gg "standby generator" "St Peter Port"
site:planningexplorer.gov.gg "La Vrangue"
site:planningexplorer.gov.gg "First Tower Lane"
```

提取字段：application number、site address、parish/island、applicant、proposal、decision/status、decision date、conditions、generator/UPS/cooling/substation notes。

### 2.2 GCRA 电信监管

- Licences：https://www.gcra.gg/businesses/telecoms/licences
- 主站：https://www.gcra.gg/

用途：确认持牌运营商和监管名称。GCRA 可确认 JT (Guernsey) Ltd (formerly Wave Telecom)、Sure (Guernsey) Limited 等持牌方，但不得把 licence 当作数据中心设施证据。

可用查询模板：
```text
site:gcra.gg "JT (Guernsey) Ltd"
site:gcra.gg "Sure (Guernsey) Limited"
site:gcra.gg "data centre" "Guernsey"
site:gcra.gg "business connectivity market review" "Guernsey"
site:gcra.gg "Guernsey Electricity" "price control"
```

### 2.3 运营商官方页（JT / Sure）

- JT Data Centre Services：https://business.jtglobal.com/products/cloud/data-centres/
- Sure Guernsey Data Centre：https://business.sure.com/products-and-services/offshore-data-centres/guernsey-data-centre/
- Sure Offshore Data Centres：https://business.sure.com/products-and-services/offshore-data-centres/

用途：确认运营中服务、认证、冗余和容量披露。JT 页面确认 Jersey and Guernsey primary data centre sites；Sure 页面确认 Guernsey Data Centre 和 2MW IT load。地址仍需产品文档、规划或其他一手材料确认。

可用查询模板：
```text
site:business.jtglobal.com "Guernsey" "Data Centre"
site:business.jtglobal.com "First Tower Lane" "Data Centre"
site:business.sure.com "Guernsey Data Centre"
site:business.sure.com "La Vrangue" "data centre"
"JT (Guernsey)" "First Tower Lane" "data centre"
"Sure (Guernsey) Limited" "La Vrangue" "data centre"
```

### 2.4 电力与大型负载

- Guernsey Electricity：https://www.electricity.gg/
- Alderney Electricity：https://alderney-elec.com/
- GCRA electricity sector：https://www.gcra.gg/

用途：确认供电上下文、进口容量、连接政策和大型负载影响。Guernsey Electricity / Alderney Electricity 资料是电力上下文，不直接证明数据中心存在。不得用岛级供电容量反推 IT load。

可用查询模板：
```text
site:electricity.gg "data centre"
site:electricity.gg "large load"
site:electricity.gg "annual report" "import"
site:alderney-elec.com "data centre"
site:gcra.gg "Guernsey Electricity" "price control"
```

### 2.5 GFSC / ODPA 客户侧监管

- GFSC Cyber Risk：https://www.gfsc.gg/cyber-risk
- GFSC 主站：https://www.gfsc.gg/
- ODPA Engaging Processors：https://www.odpa.gg/guidance/engaging-processors
- ODPA adequacy note：https://www.odpa.gg/news/data-protection-supporting-trust-innovation-and-economic-growth

用途：这些来源解释金融服务、外包、云、处理者和数据保护要求。它们可作为“客户为何选择本地托管”的上下文，不能单独证明某个物理设施。

可用查询模板：
```text
site:gfsc.gg outsourcing cloud
site:gfsc.gg "Cyber Security Rules and Guidance"
site:gfsc.gg "data centre"
site:odpa.gg "cloud-based services"
site:odpa.gg "adequacy" "Guernsey"
site:odpa.gg "processor" "Bailiwick of Guernsey"
```

### 2.6 采购与政府 IT

- gov.gg procurement/tender 入口从 https://www.gov.gg/ 站内搜索 `procurement`、`tender`、`data centre`。
- 已核实 gov.gg 存在 “Statement to Press re move of Data Centre” 结果，内容指向政府服务器/存储迁移；这属于政府内部 IT/data-centre 线索，不能自动等同商业托管设施。
- MyGov privacy policy 说明数据存储在 Guernsey secure data centre；可作为政府服务数据位置线索，但仍需区分内部/供应商设施。

可用查询模板：
```text
site:gov.gg "data centre" "procurement"
site:gov.gg "data centre services" tender
site:gov.gg "secure data centre in Guernsey"
site:gov.gg "Agilisys Guernsey" "data centre"
site:my.gov.gg "secure data centre" "Guernsey"
```

### 2.7 Guernsey Registry

- Guernsey Registry portal：https://portal.guernseyregistry.com/search
- Company searches guidance：https://www.guernseyregistry.com/Companysearches

用途：确认 SPV、运营商、开发商、注册办公室、注册状态和经济活动代码。Registry 是主体证据，不是设施证据。

可用查询模板：
```text
site:guernseyregistry.com "Company Searches"
site:portal.guernseyregistry.com/search "Alderney" "Data"
"Guernsey Registry" "Sure (Guernsey) Limited"
"Guernsey Registry" "JT (Guernsey) Ltd"
"Alderney Data Centre" "Guernsey Registry"
```

### 2.8 Alderney / Sark / Herm 覆盖

- States of Alderney：https://alderney.gov.gg/
- States of Alderney Planning Office：https://alderney.gov.gg/article/173020/Planning-Office
- Alderney Electricity：https://alderney-elec.com/

Alderney 需单独查 States of Alderney planning / Hansard / committee minutes。2026 年官方 EOI 是 project pipeline 证据，不是 operational facility。Sark/Herm 低概率，主要做负向控制；若发现服务器/通信站/电力项目，先作为 infrastructure lead，不按 commercial DC 入库。

可用查询模板：
```text
site:alderney.gov.gg "data centre"
site:alderney.gov.gg "Expression of Interest" "data centre"
site:alderney.gov.gg "Planning Office" "data centre"
site:alderney.gov.gg "Stronghold Data Centre"
"Sark" "data centre" "Guernsey"
"Herm" "data centre" "Guernsey"
```

## 3. Division 覆盖工作流（Coverage workflow）

唯一入库 division：`Guernsey`。每次枚举必须完成以下覆盖矩阵：

| 子区域 | 覆盖动作 | 期望信号 |
|---|---|---|
| St Peter Port | 查 JT/Sure 地址、规划、政府 IT、Digital Greenhouse 反证 | 高概率运营商/政府机房 |
| St Sampson / Vale | 查工业区、电力、变电站、发电机 | 电力/工业设施上下文 |
| Castel / St Saviour / St Andrew / St Martin / St Peter in the Wood / Forest / Torteval | 跑通用规划和 road-name scan | 低概率，主要排除 |
| Alderney | 查 States of Alderney EOI、planning、Alderney Electricity | pipeline / proposed |
| Sark / Herm | 查官方/本地站点和通用 web | 负向控制 |

每条候选记录至少包含：`division=Guernsey`、`sub_area`、`facility_name`、`operator/developer`、`status`、`source_grade`、`evidence_url`、`evidence_note`、`capacity_mw`（未知设 null）。

## 4. 已验证种子与处理规则（Verified seeds）

| 候选 | 当前证据 | 建议状态 |
|---|---|---|
| JT Guernsey data centre / colocation | JT 官方页确认 Guernsey primary data centre sites、认证和冗余；GCRA 确认 JT (Guernsey) Ltd 持牌 | `operational` 服务证据 A；地址/容量需继续用产品文档或规划确认 |
| Sure Guernsey Data Centre | Sure 官方页确认 Guernsey Data Centre、Tier III、2MW IT load、colo space；GCRA 确认 Sure (Guernsey) Limited 持牌 | `operational` A；地址需一手复核 |
| States of Guernsey secure data centre / government IT | gov.gg / my.gov.gg 线索确认政府数据中心/安全数据存储表述 | `internal/government` 线索；不得混为商业 DC |
| Alderney data-centre EOI | States of Alderney 2026 官方 EOI / minutes / Hansard 线索 | `planned/exploratory` A；不是 operational |
| Digital Greenhouse | 官方数字创新中心/孵化器 | `not_a_datacenter` 反证 |

## 5. 官方云区域页（确认缺席）

必须用官方区域页确认 AWS/Azure/GCP/OCI 无 Guernsey public cloud region；本地 cloud/VPS/reseller 页面不得视为 hyperscale region。

| Provider | Official URL | 处理 |
|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | 查 region 列表，无 Guernsey 则记录 negative evidence |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | 查 region/geography 列表 |
| Google Cloud | https://cloud.google.com/about/locations | 查 cloud locations |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | 查 commercial/government regions |

## 6. 常见陷阱（Pitfalls）

- `Guernsey` 是唯一 manifest division；不要把 Alderney/Sark/Herm 建成独立 division。
- JT 品牌跨 Jersey/Guernsey；必须区分 Jersey-only 地址、Channel Islands 总称和 Guernsey site。
- GCRA licence 是运营商证据，不是数据中心设施证据。
- Sure 官方 “2MW IT load” 可记录为 Sure Guernsey facility 的披露容量；目录页面的 3000 m2 / 1500 m2 等面积仍为 C 级，除非官方材料确认。
- Vale Power Station、substations、电缆登陆站是电力/网络基础设施，不是数据中心。
- Digital Greenhouse、FinTech hub、innovation centre 不是商业托管数据中心。
- 政府 “data centre” 很可能是内部机房或供应商托管合同，需标注 `internal/government`，不要自动并入 commercial colocation 清单。
