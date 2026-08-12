# IM Explorer Official — 马恩岛数据中心官方/监管枚举方法

> 日期 Date: 2026-08-12
> 范围 Scope: Isle of Man (IM)。manifest 已核验：`subnational_type: country`，`divisions: ["Isle of Man"]`。这是单分区司法辖区；所有设施记录仍必须落到城镇/教区、地址或园区层级。
> 角度 Angle: 官方/监管与一手来源优先（Isle of Man Government、Planning & Building Control、CURA、Manx Utilities、Companies Registry、GSC、官方云区域页、运营商官方设施页）。
> 可靠度分级 Reliability grades: **A** = 官方/监管/许可/运营商一手来源；**B** = 强二级来源（行业媒体、本地媒体、经纪商技术文章）；**C** = 目录/聚合/SEO/无地址营销页。

---

## 0. 结构性事实（Structural facts）

- 马恩岛是英国王冠属地（Crown Dependency），自治议会为 Tynwald；数据中心枚举应按马恩岛本地政府、监管和许可系统处理，而不是套用英国地方规划或 Ofcom/Companies House 流程。
- manifest 唯一分区是 **Isle of Man**。不要期待下级行政分区清单；执行时以 locality 字段记录 Douglas、Ballasalla、Braddan、Onchan、Ramsey、Peel、Castletown、Port Erin、Port St Mary 等城镇/教区。
- 市场形态是小型离岸托管/colo 与电信/博彩/金融需求驱动。当前可确认的一手设施信号来自 Manx Telecom、Netcetera、Domicilium、Continent 8、Sure；无 AWS/Azure/GCP/OCI 公共云区域或 hyperscale campus 官方信号。
- 规划检索是全岛集中式：官方入口是 Isle of Man Government Online Services planning search 与 Planning & Building Control（pabc.gov.im），不是英国 planningportal.co.uk。
- 通信与公用事业监管机构是 **Communications and Utilities Regulatory Authority (CURA)**；其官网确认负责电信、广播和公用事业监管，并发布 licence information。
- 公司核验使用 **Isle of Man Government Companies Registry**（gov.im / services.gov.im），不是英国 Companies House。
- 博彩监管由 **Isle of Man Gambling Supervision Commission (GSC)** 独立负责；FSA 监管金融服务，spread betting 例外归 FSA。不要写成 GSC 与 FSA 合并或承接。

---

## 1. 已核验官方入口（Verified official entry points）

| 来源 Source | URL | 用途 Use | 分级 |
|---|---|---|---|
| Isle of Man Government | https://www.gov.im/ | 政府新闻、部门、政策、公司注册、采购入口 | A |
| Department for Enterprise | https://www.iomdfenterprise.im/ 与 https://www.gov.im/dfe | 数字产业、招商、Digital Isle of Man 入口 | A |
| Digital Isle of Man | https://www.digitalisleofman.com/ | 数字产业服务商目录、行业上下文 | A（政府机构/官方品牌） |
| Planning Online Services | https://services.gov.im/planning-applications/ | 按地图、规划号、地址、日期搜索规划申请 | A |
| Planning & Building Control | https://pabc.gov.im/ | 规划申请指引、查找申请、Building Control | A |
| CURA | https://www.cura.im/ | 电信/广播/公用事业监管，licence information | A |
| CURA licences | https://www.cura.im/licence-information/licences/ | 电信牌照、许可文件 | A |
| CURA spectrum allocations | https://www.cura.im/spectrum/frequency-allocations/ | 已核验列出 Manx Telecom、Sure、Domicilium、BlueWave 等频谱/运营商信号 | A |
| Manx Utilities | https://www.manxutilities.im/ | 电力连接、用电、网络容量、开发商信息 | A |
| Manx Utilities developer information | https://www.manxutilities.im/energy-transition/information-for-developers/ | 大型负荷、互联电缆、开发商电力咨询上下文 | A |
| Companies Registry | https://www.gov.im/categories/business-and-industries/companies-registry/ 与 https://services.gov.im/companies-registry/ | 法律实体、注册号、注册地址、filings | A |
| GSC | https://www.isleofmangsc.com/ | e-gaming 牌照与 OGRA 监管上下文 | A |
| Online Gambling Regulation Act 2001 | https://legislation.gov.im/ | e-gaming 法律框架；需求方背景 | A |
| Government procurement portal | https://in-tendhost.co.uk/iomg/ | 政府电子招标；可能有 data centre hosting / WAN / DR 合同 | A（入口；文件需逐项核验） |

---

## 2. 官方/监管查询模板（Official query templates）

### 2.1 政府与议会记录（Government and Tynwald）

```text
site:gov.im "data centre" "Isle of Man"
site:gov.im "data center" "Isle of Man"
site:gov.im "Government Data Centre"
site:gov.im "Cabinet Office" "data centre"
site:gov.im "Digital Isle of Man" "data centre"
site:digitalisleofman.com "data centre" OR "datacentre" OR colocation
site:iomdfenterprise.im "data centre" OR datacentre
site:tynwald.org.im "data centre" OR "data center"
site:tynwald.org.im "Manx Telecom" "data centre"
```

提取字段：政府部门、采购/议题日期、设施名、承包商、locality、预算/合同额、服务范围、是否仅为云/托管采购。

### 2.2 规划与建筑控制（Planning and Building Control）

官方入口：

- https://services.gov.im/planning-applications/
- https://pabc.gov.im/planning/finding-applications/
- https://pabc.gov.im/planning/archive-searches/

```text
site:services.gov.im/planning-applications "data centre"
site:pabc.gov.im "data centre" "Douglas"
site:pabc.gov.im "datacentre" OR "data center"
"site:services.gov.im/planning-applications" "standby generator" "Douglas"
"Isle of Man" "planning application" "data centre"
"Isle of Man" "planning application" "generator" "data centre"
"Douglas" "backup generator" "data centre"
"Ballasalla" "data centre" "planning"
"Ronaldsway Industrial Estate" "data centre" "planning"
"Pulrose Road" "data centre" "planning"
"Heywood House" "data centre" "planning"
```

规划记录字段：

- application reference、决定日期、状态、申请人、业主、代理/工程师；
- locality、完整地址、园区/工业区、坐标；
- 用途描述：data hall、server room、telecommunications equipment、UPS、battery room、cooling、fuel storage、standby generator；
- 条件：噪声、排放、消防、交通、运行时段、电力连接；
- 证据评级：规划记录可将设施/扩建/发电机证据提升为 A。

### 2.3 通信监管与运营商（CURA and operator regulation）

```text
site:cura.im "licence" "Manx Telecom"
site:cura.im "licence" "Sure (Isle of Man)"
site:cura.im "licence" "Domicilium"
site:cura.im "licence" "BlueWave"
site:cura.im "frequency allocations" "Manx Telecom"
site:cura.im "telecommunications" "licence" "Isle of Man"
```

CURA 只能证明通信许可/频谱/监管身份；它不能单独证明某地址是数据中心。将 CURA 与运营商官方设施页、规划或目录地址交叉。

### 2.4 电力与公用事业（Manx Utilities）

```text
site:manxutilities.im "data centre" OR "data center"
site:manxutilities.im "large power" OR "large load" OR "substation"
site:manxutilities.im "interconnector" "MW"
"Manx Utilities" "data centre" "Isle of Man"
"Manx Utilities" "{operator}" "substation"
"Manx Utilities" "{operator}" "MVA" OR "MW"
```

电力线索主要用于容量、接入、变电站和大型负荷佐证。Manx Utilities 开发商信息页确认现有 60 MW interconnector 与新互联/开发咨询背景；具体机房用电仍需项目文件或规划附件。

### 2.5 公司与牌照（Companies Registry, FSA, GSC）

```text
site:gov.im/categories/business-and-industries/companies-registry "{operator}"
site:services.gov.im/companies-registry "{operator}"
"{operator} Limited" "registered office" "Isle of Man"
site:iomfsa.im "{operator}" "regulated entity"
site:isleofmangsc.com "{operator}" "licence"
site:isleofmangsc.com "licence holders" "online gambling"
site:legislation.gov.im "Online Gambling Regulation Act 2001"
```

规则：

- Companies Registry = 实体存在、注册名、注册地址、filing。注册地址不是设施地址。
- GSC/e-gaming = 需求方和市场背景；博彩运营商办公室不是数据中心。
- FSA = 金融服务实体核验；除 spread betting 外不要把 online gambling 归入 FSA。

### 2.6 政府采购（Procurement）

官方电子招标入口已核验为 In-Tend IOMG（`https://in-tendhost.co.uk/iomg/`），gov.im Procurement Services 页面说明政府使用 electronic tendering website。

```text
site:gov.im "Procurement Portal" "data centre"
site:gov.im "electronic tendering" "Procurement Portal"
site:in-tendhost.co.uk/iomg "data centre"
site:in-tendhost.co.uk/iomg "hosting"
site:in-tendhost.co.uk/iomg "colocation"
"Isle of Man Government" tender "data centre" hosting
"Cabinet Office" "Isle of Man" "disaster recovery" "hosting"
```

In-Tend 可能出现 bot/登录限制；记录入口可用性、检索日期、是否能打开 tender documents。

---

## 3. 官方云区域缺位确认（Official cloud-region absence checks）

以下仅用于 negative control，确认“无马恩岛公共云区域”：

| Provider | Official page | IM 处理 |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ 与 https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | 无 Isle of Man region；本地 AWS marketing/partner/cloud resale 不能算 AWS region。 |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list 与 https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | 无 Isle of Man public cloud region。 |
| Google Cloud | https://cloud.google.com/about/locations 与 https://docs.cloud.google.com/compute/docs/regions-zones | 无 Isle of Man region/zone。 |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ 与 https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | 无 Isle of Man public region。 |

---

## 4. 单分区覆盖流程（Coverage workflow）

唯一 division = **Isle of Man**。必须做全岛覆盖，但优先级按 locality 分层：

| locality | 覆盖重点 | 官方优先路径 |
|---|---|---|
| Douglas | Manx Telecom、Continent 8、Sure、政府 IT、e-gaming/金融需求方 | 运营商官方页、CURA、规划、Companies Registry、GSC |
| Ballasalla / Ronaldsway / Malew | Netcetera The Dataport、Domicilium、机场/工业区设施 | 运营商官方页、Digital Isle of Man 服务商页、规划、Companies Registry |
| Braddan / Union Mills / Tromode | Douglas 周边工业/通信/电力设施 | 规划、MUA、电信运营商页 |
| Onchan | Douglas 周边备份/通信设施可能性 | 规划、运营商页 |
| Ramsey | 北部通信/备份节点低产出扫描 | 规划、CURA、运营商页 |
| Peel / Castletown / Port Erin / Port St Mary | 低产出负面覆盖 | 规划关键词、运营商覆盖页 |
| St John's / Laxey / Sulby | 极低产出；能源/网络节点需防误判 | 规划、MUA；不要把发电站/水库当机房 |

每个 locality 至少运行：

```text
"{locality}" "Isle of Man" "data centre"
"{locality}" "Isle of Man" datacentre
"{locality}" "Isle of Man" colocation
"{locality}" "Isle of Man" "server room"
"{locality}" "Isle of Man" "standby generator"
site:pabc.gov.im "{locality}" "data centre"
site:services.gov.im/planning-applications "{locality}" "data centre"
```

---

## 5. 官方证据下的已知一手设施线索（A-grade seed leads）

这些是枚举入口，不是最终设施清单；入库仍需地址、状态和证据日期。

| 线索 | locality | 已核验证据 | 注意事项 |
|---|---|---|---|
| Manx Telecom twin datacentres | Isle of Man（Douglas North / Greenhill 需地址核验） | Manx Telecom 官方页称拥有并运营 two Datacentres；isleofmandatacentre.com 为 Manx Telecom 数据中心站点 | 官方页可作 A；DCD 可补面积/机柜数但属 B |
| Netcetera The Dataport | Ballasalla / Malew | Netcetera 官方页称 owns and operates The Dataport；Digital Isle of Man/目录可补地址 | 官方页 A；目录地址需回查 |
| Domicilium (IOM) Limited / The Isle of Man Datacentre | Ballasalla / Ronaldsway Industrial Estate | Domicilium 官方页称提供 datacentres/colo；Digital Isle of Man 服务商页给出 The Isle of Man Datacentre, Ronaldsway Industrial Estate | Digital Isle of Man 是强一手/政府目录；仍建议规划/公司核验 |
| Continent 8 Isle of Man data centre | Douglas / Pulrose Road | Continent 8 官方 location 页称 purpose-built Tier-3 Isle of Man data centre in Douglas；legal page给出 Pulrose Road registered office | 官方页 A；地址与设施边界需确认 |
| Sure Isle of Man data centre services | Isle of Man（具体地址需核验） | Sure Business 官方 offshore data centres 页覆盖 Jersey、Guernsey、Isle of Man；Sure IOM data-centre terms PDF存在 | 服务 A；具体机房地址/开业状态需另证 |

BlueWave 当前处理：官方 `bwc.im` 已核验为马恩岛 BlueWave Communications，但其 off-island wholesale transit 页说明 colocation/data centre services 由 UK sister company aql 提供。因此 BlueWave 是通信运营商/网络线索（CURA A），不是已确认岛内 data-centre operator，除非另有一手设施页或规划记录。

---

## 6. 可靠度规则（Reliability rules）

- **Grade A**：gov.im / pabc.gov.im / services.gov.im / cura.im / manxutilities.im / isleofmangsc.com / legislation.gov.im / 运营商现行官方设施页 / 官方公司注册记录 / 官方云区域页。
- **Grade B**：Data Centre Dynamics、Capacity Media、CommsUpdate、Telecompaper、IOM Today、Manx Radio、BBC Isle of Man、Manx Technology Group 技术市场文章、经纪商文章（含地址但非运营方）。
- **Grade C**：DataCenterMap、Datacenters.com、Cloudscene、Data Center Platform、Colo-X、Colomap、Upstack、社媒、无地址/无所有权声明的 cloud/hosting/SEO 页面。

升级规则：

- 目录地址 + 运营商官方设施页 = 可记录为 A/B 混合，但地址字段需标明来源。
- 运营商官方“services”页无地址 = A 级服务证据，不等于 A 级设施地址证据。
- CURA licence = A 级运营商身份，不等于数据中心设施。
- Government/Digital Isle of Man 服务商目录 = A/B 之间；若页面由官方政府品牌发布，可用于服务商和联系地址，但设施技术规格仍回查运营商/规划。

---

## 7. 常见陷阱（Pitfalls）

- `planning.gov.im` 不是主要当前入口；使用 `services.gov.im/planning-applications/` 和 `pabc.gov.im`。
- `bluewave.im` 不是当前核验到的马恩岛 BlueWave 主站；使用 `https://bwc.im/`。不要与美国 Bluewave Technology Group（bluewave.net）或百慕大 BlueWave（bluewave.bm）混淆。
- Companies Registry 属 gov.im / services.gov.im；不要写成 iomfsa.im 的公司注册处。
- GSC 未与 FSA 合并；e-gaming 由 GSC 监管，spread betting 例外归 FSA。
- 运营商总部/registered office 不是机房地址。Douglas 办公地址尤其容易误标为 data centre。
- “cloud platform”、“managed hosting”、“remote hands”必须确认是否有岛内物理设施；否则只作服务线索。
- 历史政府 data centre、Manx Data Centre、Wi-Manx 数据中心报道需核实现状，不可默认仍运营。
