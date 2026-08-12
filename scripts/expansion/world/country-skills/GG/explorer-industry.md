# GG Explorer Industry — 根西岛（Guernsey）数据中心枚举：行业/运营商/贸易媒体方法学

日期 Date: 2026-08-12 · 范围 Scope: 根西岛 GG（Bailiwick of Guernsey）。Manifest 校验：GG 的唯一 division 是 `Guernsey`；Alderney、Sark、Herm 和各 parish 只作为 `sub_area`/coverage tags。

角度 Angle: **行业/运营商主导发现**。先从运营商官方页和产品文档确认服务，再用监管、规划、公司登记和贸易媒体验证地址、容量、状态和历史。

## 0. 市场形态（Market shape）

- 根西岛是小型离岸市场，数据中心供给以本地/海峡群岛电信运营商为核心：JT 和 Sure 是已核实的一手运营商来源。
- 已核实无本地 hyperscale public cloud region；AWS/Azure/GCP/OCI 官方区域页只用于负向确认。
- 需求侧来自金融服务、政府、灾备、离岸业务和本地 cloud/managed services。云经销商、VPS 和 MSP 页面不能证明本地物理 facility。
- 目录站点对 JT/Sure 提供了地址种子（例如 First Tower Lane、La Vrangue），但目录默认 C 级；地址、面积和 MW 必须用运营商产品文档、规划或监管来源复核。
- Alderney 在 2026 年有官方 data-centre expression-of-interest / feasibility pipeline，应作为 `planned/exploratory` lead；不要沿用未核实的“2014-2015 已许可 £1.4bn 项目”说法，除非找到一手规划许可或可靠档案。

## 1. 优先运营商与行业线索（Operator and vendor sweep）

| 运营商/线索 | 已核实 URL | 设施/服务信号 | 分级与处理 |
|---|---|---|---|
| JT | https://business.jtglobal.com/products/cloud/data-centres/ | 官方称 Jersey and Guernsey primary data centre sites，提供 co-location / hosting，ISO/IEC 27001、PCI-DSS、SOC2，72 小时柴油发电备份，N+N 空调 | A 级确认 Guernsey 服务；地址/容量需补证 |
| Sure | https://business.sure.com/products-and-services/offshore-data-centres/guernsey-data-centre/ | 官方 Guernsey Data Centre，Tier III，24h security，data halls/cages/shared colo，inter-island connectivity，2MW IT load | A 级确认 operational facility/service；2MW IT load 可记录为官方容量披露 |
| Sure offshore portfolio | https://business.sure.com/products-and-services/offshore-data-centres/ | 官方说明 Crown dependency data-centre provider，覆盖 Jersey、Guernsey、Isle of Man | A 级组合页；不能替代本岛设施页 |
| GCRA licensed operators | https://www.gcra.gg/businesses/telecoms/licences | JT (Guernsey) Ltd、Sure (Guernsey) Limited、Logicalis Guernsey Ltd 等名册 | A 级运营商名册；不是设施目录 |
| C5 Alliance / Civica / Logicalis / MSPs | 官方站和本地商业报道 | 可能有 hosting/cloud/managed service | B/C lead；必须排除纯转售或 remote cloud |
| Digital Greenhouse | https://digitalgreenhouse.gg/ | 数字创新/孵化器 | 反证；不是 commercial colocation DC |
| Alderney 2026 EOI | https://alderney.gov.gg/article/208759/Press-Release---States-of-Alderney-Launches-Exploratory-Digital-Infrastructure-Data-Centre-Expression-of-Interest | 官方探索 data centre 开发 | A 级 pipeline；状态 `planned/exploratory` |

运营商查询模板：
```text
"JT" "Guernsey" "data centre"
"JT (Guernsey)" "First Tower Lane" "data centre"
site:business.jtglobal.com "Guernsey" "co-location"
"Sure" "Guernsey Data Centre" "2MW IT load"
site:business.sure.com "Guernsey Data Centre" "Tier III"
"Sure (Guernsey) Limited" "La Vrangue" "data centre"
"Logicalis Guernsey" "data centre" OR "hosting"
"C5 Alliance" "Guernsey" "hosting" OR "cloud"
```

## 2. 已验证 facility / lead 清单（Seed list for validation）

| Seed | Sub-area | 状态 | 当前最佳证据 | 下一步 |
|---|---|---|---|---|
| JT Guernsey data centre / colocation | Guernsey，地址待一手复核；目录常见 First Tower Lane/St Peter Port seed | `operational` | JT 官方 data-centre page + GCRA operator licence | 找 JT product description、planning record 或官方地址页确认地址和容量 |
| Sure Guernsey Data Centre | Guernsey，目录常见 La Vrangue/St Peter Port seed | `operational` | Sure 官方 Guernsey Data Centre page，含 2MW IT load；GCRA operator licence | 用 Sure terms/product docs、规划或监管来源确认地址和面积 |
| States of Guernsey secure data centre / government IT | Guernsey，内部/供应商待定 | `internal/government lead` | gov.gg / my.gov.gg data-centre references | 查 procurement、Agilisys contract、committee papers；不要归为 commercial colo |
| Alderney data-centre EOI | Alderney sub_area | `planned/exploratory` | States of Alderney 2026 EOI、committee minutes/Hansard snippets、Bailiwick/Guernsey Press follow-up | 获取 EOI PDF、planning path、developer responses；无建成证据前不入 operational |
| Digital Greenhouse | St Peter Port | `not_a_datacenter` | 官方创新中心属性 | 作为误报排除项 |

## 3. 贸易媒体与二级来源（Trade press and secondary sources）

| 来源 | URL | 用途 | 分级 |
|---|---|---|---|
| Guernsey Press | https://guernseypress.com/ | 本地规划、政府、Alderney EOI、商业新闻 | B |
| Bailiwick Express | https://bailiwickexpress.com/ | 本地政策与商业新闻；2026 Alderney data-centre EOI 有报道 | B |
| BBC Channel Islands | https://www.bbc.co.uk/news/world/europe/guernsey | 政府/基础设施/历史报道核对 | B |
| ITV Channel | https://www.itv.com/news/channel | 本地电视新闻核对 | B |
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/ | 行业报道；可查 JT/Sure/Channel Islands/Alderney | B |
| The Register | https://www.theregister.com/ | 历史数据中心项目与技术新闻 | B |
| Channel Eye | https://channeleye.media/ | 海峡群岛商业新闻；Alderney EOI 二级报道 | B |
| Island FM | https://www.islandfm.com/ | 本地新闻；Alderney EOI 二级报道 | B |
| Guernsey Finance | https://www.guernseyfinance.com/ | 金融/数字经济推广，不直接证明 facility | B context |
| DataCenterMap | https://www.datacentermap.com/guernsey/ | JT/Sure 地址种子 | C |
| Data Center Platform | https://datacenterplatform.com/ | 地址/容量 seed，需复核 | C |
| Cloudscene | https://cloudscene.com/ | IX/operator 交叉核对 | C |
| Datacenters.com / ColocationM | https://www.datacenters.com/ | 市场页与聚合 | C |

贸易查询模板：
```text
site:guernseypress.com "data centre" "Guernsey"
site:bailiwickexpress.com "Alderney" "data centre"
site:bbc.co.uk "Alderney" "data centre"
site:datacenterdynamics.com "Guernsey" "data centre"
site:theregister.com "Alderney" "data centre"
site:channeleye.media "Alderney" "data centre"
site:islandfm.com "Alderney" "data centre"
```

## 4. 目录到一手验证流程（Directory-to-primary workflow）

1. 从 DataCenterMap / Data Center Platform / ColocationM 只抽取 facility name、operator、address、claimed MW/sqm/racks。
2. 用 `"exact address" "operator" "Guernsey"`、`site:business.{operator-domain}`、`site:planningexplorer.gov.gg` 查一手证据。
3. 在 GCRA licences 确认 operator legal name；在 Registry 确认 SPV/开发商状态。
4. 若目录披露容量但官方没有披露，将容量写为 `capacity_mw: null`，把目录容量放入 notes 并标 `source_grade=C`。
5. 对 JT/Sure，运营商官方“Guernsey data centre”服务可 A 级入库；街道地址和容量字段必须按证据来源分别分级。
6. 对 Alderney，EOI/feasibility 是 pipeline，不是 facility；只有规划许可、开发协议或建设公告才能升级为 `planned/permitted` 或 `under_construction`。

## 5. 枚举矩阵（Fields and grading）

| 字段 | 首选来源 | 备注 |
|---|---|---|
| `division` | manifest | 固定为 `Guernsey` |
| `sub_area` | address/planning/operator page | parish 或 Alderney/Sark/Herm |
| `facility_name` | operator official page / planning | 避免用目录改名 |
| `operator` | operator page + GCRA | 记录 legal name 与 brand |
| `status` | official page / planning / official announcement | operational、planned/exploratory、internal、not_a_datacenter |
| `address` | planning / operator product doc / official contact | 目录地址默认 C |
| `capacity_mw` | operator official page / planning electrical docs | Sure 2MW IT load 可作为 A 级披露；其他目录 MW 不直接采信 |
| `certifications` | operator official page / certificate | JT 页面披露 ISO/IEC 27001、PCI-DSS、SOC2；Sure 披露 Tier III site |
| `power_notes` | operator page / electricity utility / planning | 不从 island peak/import capacity 换算 |
| `evidence_grade` | 本方法学分级 | 字段级分级优先于记录级分级 |

## 6. 容量提取指引（Capacity extraction guidance）

- 官方 IT load、rack count、sqm、UPS/generator、cooling redundancy 可以提取；没有官方数字时保持 null。
- Sure 官方 `2MW IT load` 可作为 Sure Guernsey Data Centre 的 A 级容量线索。
- JT 官方页披露 72-hour diesel generator backup 和 N+N air conditioning，但未在页面主体披露 Guernsey-specific MW；不要从第三方目录的 MW 自动写入。
- GEL/Alderney Electricity 的岛级容量是供电上下文，不是数据中心 IT load。
- 投资额、经济影响、lease/royalty 预测不转化为 MW。

容量查询模板：
```text
"Sure Guernsey Data Centre" "2MW"
"Sure Guernsey Data Centre" "IT load"
"JT" "First Tower Lane" "Product Description" "Data Centre"
"JT" "Guernsey" "72-hour diesel"
"Guernsey Data Centre" "UPS" "generator"
"Alderney" "data centre" "MW" OR "MVA" OR "power"
```

## 7. 误报控制（False positives）

- Jersey data centres、Jersey Internet Exchange、Jersey-only JT facilities 不得归入 GG，除非来源明确说 Guernsey site。
- Telecom exchanges、mobile masts、fibre nodes、submarine cable landing stations、power stations 和 substations 只记录为 network/power context。
- Digital Greenhouse、innovation hubs、FinTech promotion、cloud strategy 文档不是数据中心设施。
- Government secure data centre 需区分 internal/government 与 commercial colocation。
- Alderney 2026 EOI 是探索性项目；没有建成、开工或许可证据时不得标 operational。
