# JE Explorer Industry — 泽西岛数据中心行业/运营商/媒体枚举方法论

日期 Date: 2026-08-12。范围 Scope: Jersey (JE)。Manifest 核验结果：单一分区 `Jersey`；行业搜索中的教区、工业区、街道和海缆登陆点只用于岛内定位。

角度 Angle: **行业/运营商/媒体方法论**（industry/operator/media methodology）——用运营商、行业媒体、本地媒体和目录发现线索，再回到官方/一手来源确认设施、地址、状态和容量。目录和营销页只能播种，不能作为最终普查证据。

可靠性分级 Reliability grades:
- **A** = 运营商官方设施/产品页、监管/政府/规划/采购记录、JFSC/JCRA/Jersey Electricity 一手资料、官方云区域页。
- **B** = 行业媒体、本地信誉媒体、带具名当事方的新闻稿或公司报道。
- **C** = 目录、聚合、市场平台、SEO 托管页、只说明云/hosting 服务但未证明自有设施的页面。

---

## 0. 市场形态 Market Shape

- 泽西市场小，数据中心需求主要来自金融服务、信托/基金、政府 ICT、灾备、iGaming/数字业务和本地企业托管。
- 已验证一手市场事实：JT 官方页面确认 Channel Islands 数据中心/co-location/data hosting 服务；JT Five Oaks 和 JT Rue Des Pres 有官方产品说明书；Sure 官方页面确认 Jersey Data Centre、Tier III colocation 和 500 kW IT load。
- 目录显示的 Jersey 设施多集中在 St Saviour 和 St Helier，但地址、设施名和运营商归属必须用一手来源核实。
- 与 Guernsey 的混写是最大风险：JT 在 Channel Islands 多岛运营，`First Tower Lane` 为 Guernsey/St Peter Port 线索，不属于 JE。
- 与美国 New Jersey 的混写也很高频；所有搜索模板应加入 `Channel Islands`、`.je`、`St Helier`、`St Saviour` 或排除 `-"New Jersey"`。

---

## 1. 优先运营商和设施种子 Priority Operators and Facility Seeds

| 运营商/设施线索 | 已验证 URL | 位置核验 | 当前分级 | 用法 |
|---|---|---|---|---|
| JT Data Centre Services | https://business.jtglobal.com/products/cloud/data-centres/ | Jersey + Guernsey 总体服务页；不单独给街道地址 | A（服务存在性） | 确认 JT 提供 purpose-built data centres、co-location/data hosting、SOC/ISO27001 等；具体设施需用 PDF。 |
| JT Five Oaks Data Centre | https://business.jtglobal.com/wp-content/uploads/2025/11/JT-Five-Oaks-Data-Centre-Facility-Product-Description-2025.pdf；旧版 https://business.jtglobal.com/wp-content/uploads/2020/03/JT-FO-Data-Centre-PD-26-02-2020.pdf | Five Oaks / St Saviour，地址需用目录或 gov.je 交叉 | A（设施存在/技术属性）；地址若只来自目录则 C/A-mixed | 记录 Tier、rack power、UPS、generator、cooling、安全认证；不要把 cooling/generator 折算为 MW。 |
| JT Rue Des Pres Data Centre | https://business.jtglobal.com/wp-content/uploads/2025/11/JT-RDP-Data-Centre-Facility-Product-Description-2025.pdf；旧版 https://business.jtglobal.com/wp-content/uploads/2020/03/JT-RDP-Data-Centre-PD-26-02-2020.pdf | Rue des Pres/Longueville area，通常 St Saviour；地址需一手核验 | A（设施存在/技术属性）；地址若只来自目录则 C/A-mixed | 与 Five Oaks 同样处理；注意 Rue des Pres、Longueville Road、La Rue des Fonds 写法差异。 |
| Sure Jersey Data Centre | https://business.sure.com/products-and-services/offshore-data-centres/jersey-data-centre/ | 官方页确认 Jersey Data Centre；街道地址需用 Sure/JCRA/目录交叉 | A（设施存在与 500 kW IT load）；地址需另核 | 官方页面披露 Tier III、24h security、data halls/cages/shared colocation、inter-island connectivity、500 kW IT load。 |
| JCRA 运营商名单 | https://www.jcra.je/regulated-sectors/telecommunications/licences-in-issue/ | 全岛 | A（运营资格） | 确认 JT (Jersey) Limited、Sure (Jersey) Limited 等持牌；牌照不是设施证据。 |
| Digital Jersey | https://www.digital.je/choose-jersey/connectivity-and-network-infrastructure/ | 全岛 | A/B（行业定位） | 说明网络和基础设施环境；不证明具体设施。 |
| Jersey Electricity N3 | https://www.jec.co.uk/about-us/projects/normandie-3/ | Grouville Bay 至 South Hill | A（电网背景） | 供电/登陆路线线索，不作为数据中心容量。 |
| JT First Tower Lane | https://business.jtglobal.com/wp-content/uploads/2020/03/JT-FTL-Data-Centre-PD-26-02-2020.pdf；目录显示 Guernsey | Guernsey / St Peter Port | A/C 排除项 | 由 JT 运营但非 JE；必须从 Jersey 设施清单排除。 |

运营商搜索模板：
```text
"JT" "Five Oaks" "Data Centre" "Jersey"
"JT" "Rue Des Pres" "Data Centre" "Jersey"
site:business.jtglobal.com "Data Centre Facility Product Description"
site:business.jtglobal.com "Five Oaks" "Tier 3"
site:business.jtglobal.com "Rue Des Pres" "Tier 3"
"Sure" "Jersey Data Centre" "500kW"
site:business.sure.com "Jersey Data Centre" "Tier III"
"JT" "First Tower Lane" "Guernsey"
"Jersey" "data centre" "Channel Islands" -"New Jersey"
```

---

## 2. 目录和聚合源 Directory Sources

目录只用于播种名称、地址和相邻设施；不能直接计数。

| 来源 | URL | 已观察用途 | 分级 |
|---|---|---|---|
| DataCenterMap Jersey | https://www.datacentermap.com/jersey/ | JT Five Oaks、JT Rue Des Pres、Sure Jersey、可能的 JT Central/East 等地址线索；页面可能限流 | C |
| DataCenterMap Five Oaks | https://www.datacentermap.com/jersey/st-saviour/five-oaks-data-centre/ | 显示 Five Oaks / St Saviour / La Grande Route De St Martin 线索 | C，地址需一手确认 |
| DataCenterMap Rue Des Pres | https://www.datacentermap.com/jersey/st-saviour/jersey-telcom---new-dc---dec-2010/ | 显示 Rue Des Pres / Longueville Rd 线索 | C，地址需一手确认 |
| DataCenterMap Sure Jersey | https://www.datacentermap.com/jersey/st-helier/foreshore-the-powerhouse/ | 显示 Sure Jersey / Queen's Road / 0.5 MW 线索 | C，容量需 Sure 官方确认 |
| Data Center Platform Jersey | https://datacenterplatform.com/data-centers/states-of-jersey/ | 显示 Five Oaks、Rue Des Pres 地址线索 | C |
| Cloudscene | https://cloudscene.com/market/data-centers-in-jersey/all | 市场/设施交叉核对；注意可混入 USA `Jersey` | C |
| Datacenters.com | https://www.datacenters.com/locations/jersey | 可能作为市场入口；搜索经常转向 New Jersey USA | C |
| Colomap/Upstack/其他目录 | 各页面 | 仅作历史地址和别名线索 | C |

目录到一手验证工作流：
1. 从目录提取设施名、运营商、地址、教区、容量/认证声明。
2. 用 `facility + operator + site:operator-domain` 搜索运营商官方页或 PDF。
3. 用精确地址搜索 gov.je planning/register、Jersey Gazette、States Assembly。
4. 用 JCRA 确认运营商持牌；用 JFSC/registry 确认法律实体。
5. 目录声明若无法被一手证据支持，保留 C 级并写明缺口。

目录查询模板：
```text
site:datacentermap.com/jersey/ "JT" "Five Oaks"
site:datacentermap.com/jersey/ "Rue Des Pres"
site:datacentermap.com/jersey/ "Sure Jersey"
site:datacenterplatform.com "Jersey" "Five Oaks Data Centre"
site:datacenterplatform.com "Jersey" "Rue Des Pres Data Centre"
site:cloudscene.com "Jersey" "JT" "data center"
site:datacenters.com "Jersey" "colocation" -"New Jersey"
"{facility name}" "{street}" "Jersey" "data centre"
```

---

## 3. 行业媒体和本地媒体 Trade and Local Media

| 来源 | URL | 用途 | 分级 |
|---|---|---|---|
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/ | Channel Islands、operator、investment、M&A、colocation 新闻 | B |
| Capacity Media | https://www.capacitymedia.com/ | JT、Sure、海缆、批发网络和 Channel Islands 连接 | B |
| Computer Weekly | https://www.computerweekly.com/ | 政府 ICT、托管、云迁移、灾备 | B |
| Jersey Evening Post | https://jerseyeveningpost.com/ | 本地规划、JT/Sure/Jersey Electricity、政府数据中心迁移 | B |
| Bailiwick Express | https://bailiwickexpress.com/ | 本地商业和媒体发布；已见 JT Five Oaks 投资/SOC 线索 | B |
| BBC Jersey / BBC News search | https://www.bbc.co.uk/search?q=Jersey | 本地公共报道、基础设施争议；BBC 地区 URL 会变化，执行时用搜索页或站内搜索定位具体报道 | B |
| Digital Jersey news | https://www.digital.je/news-events/digital-news/ | 本地技术公司和 managed data centre case studies | B/A-mixed；按作者和事实类型区分 |

媒体查询模板：
```text
site:datacenterdynamics.com/en/news/ "Jersey" "data centre"
site:capacitymedia.com "JT" "Jersey" "data centre"
site:computerweekly.com "Jersey" "data centre"
site:jerseyeveningpost.com "Five Oaks" "data centre"
site:jerseyeveningpost.com "Rue des Pres" "data centre"
site:bailiwickexpress.com "JT" "data centre" "Five Oaks"
site:bailiwickexpress.com "Sure" "Jersey Data Centre"
site:bbc.co.uk "Jersey" "data centre"
site:digital.je "Rue des Pres data centre"
```

媒体使用规则：
- B 级媒体可确认项目名、投资额、历史时间线和当事方声明。
- 若媒体引用运营商原话但没有链接原文件，仍保持 B，直到找到运营商/政府源。
- 本地媒体中 `data centre` 可能指政府办公室机房或迁移项目；需要区分 facility、tenant migration、cloud migration。

---

## 4. 教区搜索矩阵 Parish Search Matrix

虽然 manifest 只有 `Jersey`，执行轮仍应按教区扫描，避免漏掉低调设施。

通用模板：
```text
"{parish}" "Jersey" "data centre" -"New Jersey"
"{parish}" "Jersey" "data center" -"New Jersey"
"{parish}" "Jersey" datacentre
"{parish}" "Jersey" colocation
"{parish}" "Jersey" "server room"
"{parish}" "Jersey" "backup generator" "data"
"{parish}" "Jersey" "substation" "data"
site:gov.je "{parish}" "data centre"
site:gov.je "{parish}" "server room"
site:jerseyeveningpost.com "{parish}" "data centre"
```

重点地名模板：
```text
"Five Oaks" "data centre" "Jersey"
"La Grande Route De St Martin" "data centre"
"Rue des Pres" "data centre" "Jersey"
"Longueville Road" "data centre" "Jersey"
"La Rue des Fonds" "data centre" "Jersey"
"Queen's Road" "Jersey Data Centre" "Sure"
"The Powerhouse" "Queens Road" "data centre" "Jersey"
"Minden Place" "JT" "data centre"
"La Collette" "data centre" "Jersey"
"South Hill" "substation" "Jersey Electricity"
"Grouville Bay" "Normandie 3"
```

枚举矩阵：

| 教区 | 已知/高价值线索 | 搜索重点 | 预期 |
|---|---|---|---|
| St Saviour | JT Five Oaks、JT Rue Des Pres/Rue des Pres area | JT PDF、目录地址、gov.je planning、JCRA/JFSC | 高 |
| St Helier | Sure Jersey Data Centre、可能的 JT Central/Telephone House、Queen's Road、La Collette/South Hill | Sure 官方、目录、gov.je、Jersey Electricity、New Jersey 排除 | 高 |
| Grouville | Normandie 3 landing at Grouville Bay | Jersey Electricity、gov.je ministerial decisions | 低-中，主要电力背景 |
| St Peter | Airport/industrial estate | gov.je planning、Ports/airport、operator POP/DR | 中 |
| St Brelade | Les Quennevais/shoreline | planning、media、network/landing terms | 低-中 |
| St Ouen | shoreline/cable candidates | submarine cable、JT、Ports、planning | 低-中 |
| St Lawrence | substations/industrial pockets | planning、Jersey Electricity | 低 |
| Trinity、St John、St Mary、St Martin、Grouville、St Clement | rural/low density except specific infrastructure | broad scan only; require strong evidence | 低 |

---

## 5. 核心证据链 Colocation Activity Evidence Chain

| # | 证据 | 来源 | 分级 | 枚举处理 |
|---|---|---|---|---|
| 1 | JT 官方页面确认 purpose-built data centres、co-location/data hosting、主要 Jersey/Guernsey 站点认证 | JT Data Centre Services | A | 作为 JT 服务存在性和运营商一手入口。 |
| 2 | JT Five Oaks 产品说明书确认具体 data centre facility 和技术属性 | JT PDF 2025/2020 | A | 建立候选设施；地址需从 PDF、gov.je 或目录交叉确认。 |
| 3 | JT Rue Des Pres 产品说明书确认具体 data centre facility 和技术属性 | JT PDF 2025/2020 | A | 建立候选设施；核验 Rue des Pres/Longueville/La Rue des Fonds 地址写法。 |
| 4 | Sure 官方 Jersey Data Centre 页面确认 Tier III colocation 和 500 kW IT load | Sure Business | A | 建立候选设施；若地址来自 Queen's Road/Powerhouse 目录或隐私页，地址来源单独标注。 |
| 5 | JCRA licences in issue 确认 JT、Sure 等电信运营资格 | JCRA | A | 运营商验证，不是设施验证。 |
| 6 | gov.je/JT 年报材料提及 Five Oaks 扩建、Rue des Pres 新建、700 racks、Project Liberty | gov.je PDF/States public-company material | A | 历史容量/投资背景；需用当前运营商页面确认 operating。 |
| 7 | DataCenterMap/Data Center Platform 显示 Five Oaks、Rue Des Pres、Sure Jersey 地址 | 目录 | C | 只作为地址/别名 seed；不能单独计数。 |
| 8 | Digital Jersey 和本地媒体显示本地 managed data centre 使用案例 | Digital Jersey/media | B 或 A/B | 需求侧和市场背景，不直接新增设施。 |

升级/降级规则：
- 目录独有设施保持 C，不进入最终 operating count，除非一手资料确认。
- 运营商官方页面确认设施但未披露地址时，可记录 `facility_evidence_grade: A`、`address_grade: C/null`。
- 若发现条目实为 Guernsey 或 New Jersey USA，立即排除并记录 `exclusion_reason`。
- 若只发现政府/企业“migrated to a data centre”表述，不新增 facility；仅作为租户/使用案例。

---

## 6. 容量和属性提取 Capacity and Attribute Extraction

泽西容量证据通常以 rack、kW、Tier、UPS/generator/cooling 出现。

可直接记录：
- Sure 官方披露的 `500 kW IT load`：可转换为 `capacity_mw: 0.5`，并保留原文单位和 URL。
- JT PDF 披露的 rack sizes、included rack power、additional power increments、UPS autonomy、generator backup、cooling kW、Tier/ISO/PCI/SOC：作为 `capacity_notes` 或技术属性。
- gov.je/JT 年报中若披露 `700 racks`、投资额、扩建/新建时间线：作为历史规模信号，需注明年份。

不可推算：
- 不用 `rack count x 2 kW` 自行生成 IT MW。
- 不用 cooling kW、generator kVA、Jersey Electricity interconnector MW 推算数据中心容量。
- 不把 `Tier III`、`ISO 27001`、`SOC2/3`、`PCI-DSS` 当作容量。

容量查询模板：
```text
"JT Five Oaks" "rack" "2 KW"
"JT Five Oaks" "generator" "560 KVA"
"JT Rue Des Pres" "rack" "2 KW"
"JT Rue Des Pres" "UPS" "generator"
"Sure Jersey Data Centre" "500kW"
"Jersey" "data centre" "700 racks"
"Jersey" "data centre" "£7m"
```

---

## 7. 最终输出建议 Output Guidance

每条候选设施建议记录：

```text
division: Jersey
parish: <St Helier | St Saviour | ... | null>
operator:
facility_name:
address:
address_source_url:
facility_source_url:
facility_evidence_grade:
address_evidence_grade:
status:
capacity_mw:
capacity_original:
capacity_notes:
exclusion_reason:
last_verified_date:
```

JE 最小候选清单（执行轮起点）：
- JT Five Oaks Data Centre — A 级设施 seed；St Saviour/Five Oaks 地址待一手交叉。
- JT Rue Des Pres Data Centre — A 级设施 seed；St Saviour/Rue des Pres 地址待一手交叉。
- Sure Jersey Data Centre — A 级设施 seed；官方 500 kW IT load；Queen's Road/St Helier 地址需交叉。
- JT First Tower Lane — 排除；Guernsey，不计入 JE。
- 目录中的 JT Central / JT East / Telephone House 等 — C 级 seed；必须确认是否为数据中心、exchange、office 或目录误报。
