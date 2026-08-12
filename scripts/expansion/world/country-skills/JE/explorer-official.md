# JE Explorer Official — 泽西岛数据中心枚举方法论（官方/监管口径）

日期 Date: 2026-08-12。范围 Scope: Jersey (JE)。Manifest 核验结果：`country_code: "JE"`, `subnational_type: "country"`, `divisions: ["Jersey"]`。因此本方法论只需覆盖一个分区 `Jersey`；教区（parish）和工业区只作为岛内定位字段，不作为 manifest 分区。

角度 Angle: **官方/监管方法论**（official/regulatory methodology）——优先用泽西州政府（Government of Jersey / gov.je）、规划审批、州议会记录、JFSC 注册处、JCRA 电信牌照、Jersey Electricity 电网资料、运营商一手设施页面，以及官方云区域页面，确认泽西岛运营中/规划中的数据中心和排除误报。

可靠性分级 Reliability grades:
- **A** = 官方/一手来源：gov.je 规划/采购/政府文件、States Assembly 正式记录、JFSC 注册处、JCRA 牌照清单、Jersey Electricity 官方资料、JT/Sure 等运营商官方设施页或产品说明书、AWS/Azure/GCP/OCI 官方区域列表（用于排除）。
- **B** = 可靠二手来源：Data Center Dynamics、Capacity Media、Computer Weekly、本地信誉媒体（Jersey Evening Post、Bailiwick Express、BBC Jersey）或带具名当事方的公司新闻转载。
- **C** = 目录/聚合/营销来源：DataCenterMap、Cloudscene、Datacenters.com、Data Center Platform、Colomap、Upstack、经销商 VPS/hosting 页面等。

---

## 0. 泽西结构性事实 Jersey Structural Facts

- 泽西是英国王室属地（Crown Dependency），有独立政府、法律和规划体系；不使用英国本土 Planning Portal。官方入口为 https://www.gov.je/ 。
- Manifest 只有一个枚举分区：`Jersey`。岛内定位建议记录 12 个教区：St Helier、St Saviour、St Clement、Grouville、St Martin、Trinity、St John、St Mary、St Ouen、St Peter、St Brelade、St Lawrence。
- 主要高产出地理锚点：St Helier（商业中心、La Collette/South Hill/Queen's Road）、St Saviour（Five Oaks、Rue des Pres/Longueville 一带）、St Peter（机场/工业区）、Grouville（N3 电力登陆）、St Brelade/St Ouen（海岸和潜在海缆线索）。
- 已验证的一手设施信号：JT 官方页面确认其 Channel Islands 数据中心服务，且 JT 产品说明书确认 **Five Oaks Data Centre** 与 **Rue Des Pres Data Centre**；Sure 官方页面确认其 **Jersey Data Centre**，标称 Tier III 和 500 kW IT load。地址仍应在枚举执行轮用运营商资料、规划记录或目录交叉核对到教区。
- JT **First Tower Lane Data Centre** 经目录和 JT 资料上下文核对为 Guernsey/St Peter Port 线索，不属于 JE；必须作为 Jersey/Guernsey 混淆排除项。
- 泽西无官方公有云 hyperscale region。AWS、Azure、Google Cloud、Oracle OCI 的官方区域页面用于排除“Jersey cloud region”误报。
- `JE` 缩写同时可能表示 Jersey Electricity、泽西国家代码和地址邮编片段；搜索时使用 `Jersey`、`Jersey Electricity`、`JT (Jersey) Limited` 等全称消歧。

---

## 1. A 级官方/监管来源 Grade A Official/Regulatory Sources

### 1.1 Government of Jersey / gov.je：规划、政府文件、采购

已验证入口：
- 政府主页：https://www.gov.je/
- Planning and building：https://www.gov.je/PlanningBuilding/pages/default.aspx
- Current planning applications：https://www.gov.je/PlanningBuilding/CurrentPlanningApplications/pages/index.aspx
- Planning application search/register：https://www.gov.je/citizen/Planning/pages/planningapplicationsearch.aspx
- Channel Islands Tenders / Proactis：https://www.tenders.gov.je/
- 当前招标说明页：https://www.gov.je/Government/CommercialServices/SupplyingGoods/pages/registeringtenderopportunities.aspx

用途：
- 数据中心新建、扩建、备用发电机、冷却设备、变电站、大型 ICT 机房改造、Change of Use 等通常会留下规划申请或配套环境/噪声材料。
- 政府采购可能披露政府数据中心迁移、托管、WAN、云服务或机房运维合同。
- gov.je 文件中已能找到历史线索，例如 JT 2010 年报提到 Five Oaks 扩建、Rue des Pres 新数据中心，以及 Channel Islands 数据托管能力；执行轮应保存 PDF URL、页码和摘录。

gov.je 查询模板：
```text
"data centre" site:gov.je
"data center" site:gov.je
datacentre site:gov.je
"server room" site:gov.je "Jersey"
"data centre" "Five Oaks" site:gov.je
"Rue des Pres" "data centre" site:gov.je
"Cyril Le Marquand" "Five Oaks" "data centre" site:gov.je
"planning application" "data centre" "Jersey"
"generator" "data centre" site:gov.je
"cooling" "data centre" site:gov.je
"tender" "data centre" site:gov.je
"WAN" "data centre" site:gov.je
```

规划记录提取字段：
- 申请编号、申请人、业主、SPV、地址、教区、地块编号；
- 描述中的 `data centre`、`server room`、`telecoms exchange`、`generator`、`UPS`、`substation`、`cooling plant`、`change of use`；
- 状态：submitted / approved / refused / withdrawn / superseded；
- 设施属性：面积、机柜/数据大厅、发电机容量、燃油储量、冷却、噪声、运行时间、供电连接。

### 1.2 States Assembly：议会记录和公共公司文件

入口：
- States Assembly：https://statesassembly.je/home
- 旧/兼容域在历史材料中常见为 `statesassembly.gov.je`；新查询优先使用 `statesassembly.je`。

用途：
- 质询、部长决定、Scrutiny 报告和国有/半国有公司材料可能披露 JT、Jersey Electricity、政府 ICT 迁移、海缆、供电和韧性项目。
- 对国有或政府参股主体，States Assembly/gov.je 附件可作为 A 级项目背景；但若只描述服务市场，不自动证明具体物理地址。

查询模板：
```text
"data centre" site:statesassembly.gov.je
"data center" site:statesassembly.gov.je
"JT" "data hosting" site:statesassembly.gov.je
"Five Oaks" "data centre" site:statesassembly.gov.je
"Rue des Pres" "data centre" site:statesassembly.gov.je
"submarine" "JT" site:statesassembly.gov.je
```

### 1.3 JFSC：注册处和实体核验

已验证入口：
- JFSC 官网：https://www.jerseyfsc.org/
- JFSC registry / SIR：https://registry.jfsc.je/ 和 https://sir.jerseyfsc.org/Login.aspx

用途：
- 验证运营商、项目 SPV、托管服务公司、金融服务客户的法律实体名称、注册号和状态。
- JFSC/Jersey registry 是实体证据，不是设施证据；注册地址或持牌地址不得直接当作数据中心地址。

查询模板：
```text
"JT (Jersey) Limited" site:jerseyfsc.org
"Sure (Jersey) Limited" site:jerseyfsc.org
"data centre" site:jerseyfsc.org
"hosting" site:jerseyfsc.org "Jersey"
"{operator}" "registered number" "Jersey"
"{operator}" "JFSC"
```

### 1.4 JCRA：电信牌照和监管边界

已验证入口：
- JCRA 官网：https://www.jcra.je/
- Telecommunications licences in issue：https://www.jcra.je/regulated-sectors/telecommunications/licences-in-issue/
- JT (Jersey) Limited licence page：https://www.jcra.je/cases-documents/licensees-licences/jt-jersey-limited/

已核实要点：
- JCRA 说明在 Jersey 运行全部或部分电信系统需要 JCRA 牌照。
- 牌照清单列出 JT (Jersey) Limited、Sure (Jersey) Limited、Jersey Electricity PLC、BT Jersey Limited、Home Net Limited、Newtel Limited、Starlink Internet Services Limited 等。
- 清单显示 JT (Jersey) Limited 为 Class III Telecoms licensee；Sure (Jersey) Limited 为 Class II Telecoms licensee。牌照证明通信运营资格，不单独证明数据中心设施。

查询模板：
```text
site:jcra.je "licences in issue" "JT (Jersey) Limited"
site:jcra.je "Sure (Jersey) Limited" "Class II"
site:jcra.je "data centre" OR "data center"
site:jcra.je "telecommunications" "licence"
site:jcra.je "Jersey Electricity PLC" "Class I"
site:jcra.je "electricity" "connection"
```

### 1.5 Jersey Electricity：电网、互联和大用户供电

已验证入口：
- Jersey Electricity 官网：https://www.jec.co.uk/ 和 https://www.jerseyelectricity.com/
- Normandie 3 官方项目页：https://www.jec.co.uk/about-us/projects/normandie-3/

已核实要点：
- Normandie 3 页面说明 N3 从法国 Périers/Armanville Beach 到 Grouville Bay，再通过 Jersey 陆缆到 St Helier South Hill Switching Station；这是电网背景和登陆/路由线索。
- 互联容量、La Collette 发电站、South Hill switching/substation、Queen's Road/Rue des Pres 变电站等是供电可行性线索；不得折算为数据中心 IT MW。

查询模板：
```text
site:jec.co.uk "data centre" OR "data center"
site:jerseyelectricity.com "data centre" OR "data center"
"Jersey Electricity" "substation" "data centre"
"Jersey Electricity" "large customer" "data"
"Normandie 3" "Grouville Bay" "South Hill"
"La Collette" "data centre" "Jersey"
"Rue des Pres" "substation" "Jersey Electricity"
```

### 1.6 运营商官方设施页 Operator First-Party Facility Sources

已验证入口：
- JT Data Centre Services：https://business.jtglobal.com/products/cloud/data-centres/
- JT resources page：https://business.jtglobal.com/resources/
- JT Five Oaks Facility Product Description 2025：https://business.jtglobal.com/wp-content/uploads/2025/11/JT-Five-Oaks-Data-Centre-Facility-Product-Description-2025.pdf
- JT Rue Des Pres Facility Product Description 2025：https://business.jtglobal.com/wp-content/uploads/2025/11/JT-RDP-Data-Centre-Facility-Product-Description-2025.pdf
- JT legacy Five Oaks PDF：https://business.jtglobal.com/wp-content/uploads/2020/03/JT-FO-Data-Centre-PD-26-02-2020.pdf
- JT legacy Rue Des Pres PDF：https://business.jtglobal.com/wp-content/uploads/2020/03/JT-RDP-Data-Centre-PD-26-02-2020.pdf
- Sure Jersey Data Centre：https://business.sure.com/products-and-services/offshore-data-centres/jersey-data-centre/

已核实要点：
- JT 页面确认 purpose-built Data Centres 提供 co-location/data hosting，主要站点在 Jersey 和 Guernsey，并列出 SOC/ISO27001 等认证。
- JT Five Oaks 与 Rue Des Pres 产品说明书为 A 级设施存在和技术属性证据；需要从 PDF 中记录 evidence_date、页码、Tier、UPS、generator、cooling、rack power 等。
- Sure 页面确认 Jersey Data Centre 提供 Tier III colocation、24h security、data halls/cages/shared colocation、inter-island connectivity、500 kW IT load。若页面不披露街道地址，地址需用 Sure 联系页、JCRA、目录或规划记录交叉核实后记录。

运营商查询模板：
```text
site:business.jtglobal.com "Five Oaks" "Data Centre"
site:business.jtglobal.com "Rue Des Pres" "Data Centre"
site:business.jtglobal.com "Data Centres" "Product Description"
site:business.sure.com "Jersey Data Centre"
site:business.sure.com "Queens Road" "Jersey Data Centre"
"JT" "Five Oaks" "Data Centre" "Jersey"
"JT" "Rue des Pres" "Data Centre" "Jersey"
"Sure" "Jersey Data Centre" "500kW"
```

### 1.7 官方云区域页面 Official Cloud Region Pages

仅用于排除超大规模云区域误报：

| Provider | Official URL | JE 结论 |
|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html 和 https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | 官方区域列表未列 Jersey。 |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list 和 https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | 官方区域/地理列表未列 Jersey。 |
| Google Cloud | https://cloud.google.com/about/locations | 官方 locations 未列 Jersey。 |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm 和 https://www.oracle.com/cloud/public-cloud-regions/ | 官方区域列表未列 Jersey。 |

规则：本地 MSP、VPS、private cloud、offshore cloud 页面不得升级为 AWS/Azure/GCP/OCI Jersey region；只能作为本地托管/云服务线索。

---

## 2. 全分区覆盖工作流 Per-Division Workflow

Manifest 分区只有 `Jersey`，覆盖要求如下：

1. 对 `Jersey` 做全岛关键词扫描：gov.je、statesassembly.gov.je、JCRA、JFSC、Jersey Electricity、JT、Sure、Digital Jersey。
2. 用 12 个教区作为定位矩阵，而非分区：每条设施记录必须尽量落到 parish、街道/工业区、证据 URL。
3. 先以运营商官方页确认服务/设施存在，再回到 gov.je 规划、JCRA/JFSC、Jersey Electricity 或目录交叉确认地址。
4. 对 JT Five Oaks、JT Rue Des Pres、Sure Jersey Data Centre 进行专项核验；对 JT First Tower Lane、Guernsey Sure/C5 等进行反向排除。
5. 若发现新项目（planning/permit/tender），记录项目状态和审批编号；未开工或仅采购服务的项目不得写作 operating facility。
6. 输出时将 `division` 固定为 `Jersey`；`parish` 作为补充字段。

教区/地点矩阵：

| 教区/地点 | 用途 | 优先来源 |
|---|---|---|
| St Helier（Queen's Road、Minden Place、La Collette、South Hill） | Sure 线索、政府/商业中心、电力/变电、可能的 telecom exchange | Sure 官方、gov.je 规划、JE N3/South Hill、JCRA、目录反查 |
| St Saviour（Five Oaks、Rue des Pres、Longueville） | JT Five Oaks/Rue Des Pres 核心线索 | JT 官方 PDF、gov.je、JCRA、DataCenterMap/Data Center Platform 地址交叉 |
| Grouville | N3 电力海缆登陆背景 | Jersey Electricity N3、gov.je ministerial decisions |
| St Peter | 机场/工业区，潜在灾备/网络设施 | gov.je 规划、Ports/airport、JCRA/JT |
| St Brelade、St Ouen | 海岸/海缆候选区 | JT/Ports/政府海缆资料、规划记录 |
| St Lawrence、Trinity、St John、St Mary、St Martin、St Clement | 低产出区 | 通用 gov.je + parish 扫描；无强证据不记录设施 |

---

## 3. 记录和分级规则 Recording and Grading

- 设施存在性（facility existence）优先级：运营商设施页/PDF、规划许可、政府或监管文件 > 行业媒体 > 目录。
- 地址可信度单独评估：运营商页面不披露地址时，地址即使来自目录也只能标注为目录来源，直到 gov.je/运营商/JFSC/JCRA 或其他一手材料确认。
- 容量字段：只记录披露值。Sure 官方 `500 kW IT load` 可记录为 0.5 MW；JT PDF 的 rack power、generator kVA、cooling kW 只能作为代理指标，不能自行折算成 IT MW。
- 状态字段：`operating` 需要运营商现行页面、最新 PDF、许可或可信媒体确认；旧 PDF/旧目录要用当前页面复核。
- 排除字段：Guernsey 设施、New Jersey（美国）设施、总部/办公室、cloud reseller、VPS、telecom mast、substation-only 均不得计作 JE 数据中心。

---

## 4. 常见陷阱 Common Pitfalls

- `Jersey` 搜索极易混入 **New Jersey, USA**；查询中加入 `Channel Islands`、`site:.je`、`"St Helier"`、`"St Saviour"` 或 `-\"New Jersey\"`。
- `First Tower Lane` 是 Guernsey/St Peter Port 线索；即使由 JT 运营，也不属于 JE。
- `Telephone House, Minden Place`、运营商总部、客服地址或隐私政策地址不能自动当作机房地址。
- `Rue des Pres`、`Longueville Road`、`La Rue des Fonds`、`Five Oaks` 地址在目录间可能写法不一致；最终以一手资料和 gov.je 地址为准。
- Jersey Electricity 的 N3、La Collette、South Hill 是供电/韧性背景；不能把电网 MW 当作数据中心容量。
- Digital Jersey/Jersey Finance 的行业宣传仅说明需求环境，不证明设施。

---

## 5. 最小执行清单 Minimal Execution Checklist

- [ ] 确认 manifest division 仍为 `["Jersey"]`。
- [ ] 保存 gov.je planning register、Channel Islands Tenders、JCRA licences in issue、JFSC registry、JT data centre page、JT Five Oaks/Rue Des Pres PDFs、Sure Jersey Data Centre page。
- [ ] 对 JT Five Oaks、JT Rue Des Pres、Sure Jersey Data Centre 建立候选记录，并分别记录一手证据字段。
- [ ] 用目录只补地址/相邻设施线索，并保留 C 级标签直到一手确认。
- [ ] 对 First Tower Lane、Guernsey、New Jersey USA 误报做排除记录。
- [ ] 对 AWS/Azure/GCP/OCI 官方区域页进行排除性核验。
