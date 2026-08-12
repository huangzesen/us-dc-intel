# VU Explorer Official — 瓦努阿图数据中心枚举 · 官方/监管来源

日期: 2026-08-12。范围: 瓦努阿图共和国 (Vanuatu, VU)，全国 6 省 (provinces): Malampa、Penama、Sanma、Shefa、Tafea、Torba（已按 `world-manifest.jsonl` 核对）。角度: 通过官方、监管、公用事业与多边机构来源发现运营中、建设中、规划中和误报的数据中心候选设施。

可靠性分级 (Reliability grades): **A** = 政府、监管机构、国企/法定机构、公用事业监管、官方公司页、官方云区域页、立法文本、多边机构项目文件；**B** = 具名来源与日期的可靠本地/区域/行业媒体、承包商案例、运营商访谈、多边项目页面；**C** = 目录站、海缆追踪器、PeeringDB/ASN 聚合、社交页面、SEO/转售页面、无出处聚合。C 级仅作线索或负控，不得用于确立设施。

## 0. 已验证国家基线 (Verified Country Baseline)

- 未发现瓦努阿图有公开的数据中心登记册或数据中心专属牌照类别；设施枚举必须交叉使用 DCDT/PMO、TRBR、采购、海缆、电力和媒体来源。
- 官方已确认的设施级数据中心信号集中在 **Shefa 省 / 维拉港 (Port Vila, Efate)**: DCDT 的 `Vanuatu Government Data Center` 官方资料、PMO 关于 Tamtam submarine cable / data centres / government broadband network 的 COM 公告、以及 DCDT 页面说明 Vanuatu Internet Exchange (VIX) housed at the Vanuatu Government Data Centre in Port Vila。
- 官方连接性资产包括 ICN1 维拉港国际海缆、VIX、Tamtam 第二国际海缆项目，以及运营商/ISP 网络。海缆登陆站、IXP、NOC、交换机房默认不是商业数据中心；只有来源明确点名 data centre / colocation / racks / hosting facility 时才升级。
- 非维拉港省份的设施级信号主要是连接性: Sanma/Santo、Malampa/Malekula、Tafea/Tanna 受 Tamtam 海缆覆盖；Torba、Penama 主要是通用接入、移动覆盖、卫星/政府 ICT 线索。不要从覆盖或海缆节点自动推断商业 DC。
- 官方云区域缺失: AWS、Azure、Google Cloud、Oracle OCI 官方区域清单未列 VU。不要将 VPS、Starlink、Kacific/SES/O3b、云转售或托管广告提升为本地设施。
- 检索语言: 英语优先，辅以法语和 Bislama。地名归一化: Efate/Efate Island、Port Vila/Vila、Espiritu Santo/Santo、Luganville、Malekula/Lakatoro、Tanna/Lenakel/Isangel、Ambae/Saratamata、Vanua Lava/Sola。

## 1. 优先核对的官方来源 (Official Sources To Check First)

### 1.1 DCDT / PMO — 政府数字化与政府数据中心

一手来源:

- DCDT: https://dcdt.gov.vu/ 和镜像/旧路径 https://digital.gov.vu/ 。DCDT 页脚地址为 Port Vila, Efate。
- DCDT brochures: https://dcdt.gov.vu/index.php/media-files/brochures 。已验证页面列出 `Vanuatu Government Data Center`，PDF 路径为 `https://dcdt.gov.vu/images/brochures/VGDC.pdf`；同页还列出 `Vanuatu Internet Exchange Point`，PDF 路径为 `https://dcdt.gov.vu/images/brochures/VIX.pdf`。
- DCDT events: https://digital.gov.vu/index.php/media-files/events 。已验证 VIX 页面说明 VIX 于 2012 年由政府和五家网络运营商 MOU 建立，并 housed at the Vanuatu Government Data Centre in Port Vila。
- PMO press release: https://pmo.gov.vu/en/public-information/press-release/1145-council-of-ministers-approves-key-recommendation-on-the-tamtam-submarine-cable%2C-data-centre-and-government-broadband-network.html 。已验证该 COM 公告提及 Tamtam cable、new data centres、government broadband network，并指示 DCDT complete implementation of the Vanuatu Government Data Centre project（Australian Government support），还说明 Data Centres and Cloud Pilot Project remain State property。

用法:

- DCDT/PMO 是政府数据中心的 A 级锚点。`Vanuatu Government Data Centre, Port Vila` 可登记为 `government_dc` / `operational_or_implementation`，但机架数、冗余站点、精确地址和状态细节需从 VGDC PDF、采购文件或后续官方公告复核。
- PMO 的 `data centres` 和 `Cloud Pilot Project` 是项目/所有权证据；未披露地点的 data centres 不可自动扩展到 Santo 或其他省份。
- VIX 是互联设施信号；只在同一来源点名 Government Data Centre 时支撑 Port Vila 政府 DC，不把 VIX 自身计为商业 colo。

查询 (Queries):

```text
site:dcdt.gov.vu ("Government Data Center" OR "Government Data Centre" OR VGDC OR "data centre" OR "data center" OR VIX)
site:digital.gov.vu ("Government Data Center" OR "Government Data Centre" OR VIX OR "Data Centre" OR "Port Vila")
site:pmo.gov.vu ("data centre" OR "data centres" OR "data center" OR Tamtam OR "Cloud Pilot" OR "Government Broadband Network")
"Vanuatu Government Data Centre" OR "Vanuatu Government Data Center" "Port Vila"
"Vanuatu Internet Exchange" "Government Data Centre" "Port Vila"
```

### 1.2 TRBR Vanuatu — 电信监管机构

一手来源:

- 官网: https://www.trbr.vu/ 。已验证 active site；使用 TRBR 当前主域核查监管资料。
- 联系页: https://www.trbr.vu/contact-us ，列出 PO Box 3547, Port Vila, Efate, Vanuatu。
- Public Register / publications 路径: `https://www.trbr.vu/public-register/...`；站内有 latest news、reports、consultations、notices、regulations。
- Universal Access Policy 页面: https://www.trbr.vu/telecom-industry/universal-access/universal-access-policy 。已验证页面点名 Telecom Vanuatu Ltd、Telsat Broadband Ltd、Digicel Vanuatu Ltd 为 UAP players。

用法:

- TRBR 牌照、RIO、年度报告是运营商存在和监管状态的 A 级证据，但不是数据中心证据。
- 用 TRBR 先列出电信/ISP 参与者，再回到 DCDT、运营商官方页、采购和媒体核实是否有 data centre / colocation / server room / gateway facility。

查询:

```text
site:trbr.vu ("data center" OR "data centre" OR datacenter OR "server room" OR IXP OR hosting OR colocation OR gateway)
site:trbr.vu (licensee OR licence OR license OR "public register") (TVL OR Vodafone OR Digicel OR Telsat OR WanTok OR Interchange)
site:trbr.vu RIO OR "Reference Interconnection Offer" OR interconnection OR gateway
site:trbr.vu "annual report" OR "telecommunications sector report"
site:trbr.vu "Universal Access Policy" (Tanna OR Malekula OR Santo OR Maewo OR Ambae OR Torres OR Efate)
```

### 1.3 政府门户、MIPU、采购与多边项目

一手来源:

- Government portal: https://www.gov.vu/ 及部委子域；PMO: https://pmo.gov.vu/。
- Ministry of Infrastructure and Public Utilities: https://mipu.gov.vu/ 。已验证为 MIPU 官方网站。
- Department of Finance and Treasury: https://doft.gov.vu/；MFEM/财政资料和预算、招标痕迹优先从此处或 `gov.vu` 站内检索。
- ADB Tamtam Submarine Cable Project: https://www.adb.org/projects/59142-005/main ，项目号 `59142-005`；IEE PDF: https://www.adb.org/sites/default/files/project-documents/59142/59142-005-iee-en.pdf 。

用法:

- 政府数据中心建设、云试点、Tamtam、政府宽带网、采购和预算以 PMO/DCDT/DOFT/ADB 为 A 级。
- ADB 项目证实 Tamtam 是第二国际海缆项目；节点/登陆站可作为 `telecom_cable_station_project`，但不等于数据中心。
- 采购、合同授予、EIA 和预算可验证状态（planned / procurement / under_construction / operational）。没有状态证据时不要写作运营中。

查询:

```text
site:gov.vu ("data centre" OR "data center" OR "Government Data Centre" OR "Cloud Pilot" OR "Digital Transformation")
site:pmo.gov.vu (Tamtam OR "submarine cable" OR "data centre" OR "government broadband")
site:doft.gov.vu (tender OR procurement OR contract OR budget) ("data centre" OR ICT OR server OR Tamtam OR broadband)
site:mipu.gov.vu (telecommunications OR broadband OR "submarine cable" OR Tamtam OR ICT)
site:adb.org Vanuatu 59142-005 OR Tamtam OR "submarine cable"
```

### 1.4 海缆、登陆站与互联: ICN1 / Tamtam / VIX

一手/高可信来源:

- Interchange: https://interchange.vu/subsea-cables/ 。已验证官方页面说明 ICN1 于 2014 年完成，连接 Port Vila 和 Suva, Fiji，并接入 Southern Cross；还描述 ICN2/ICN3 计划、Santo 和 New Caledonia/Solomon Islands 方向。
- PMO Tamtam 公告见 §1.1；已验证 Tamtam 将连接 Lifou, New Caledonia 与 Vanuatu，并提升 Santo、Malekula、Efate、Tanna 连接。
- ADB Tamtam 项目见 §1.3；ADB 新闻/项目页是项目融资和状态的 A/B 锚点。
- DCDT VIX 页面见 §1.1；VIX housed at Government Data Centre in Port Vila。

用法:

- ICN1 维拉港登陆站/电缆站: `telecom_cable_station`，省份 Shefa；若仅来源于海缆图/追踪器则降为 C。
- Tamtam 节点: `telecom_cable_station_project` 或 `connectivity_project`，覆盖 Santo/Sanma、Malekula/Malampa、Efate/Shefa、Tanna/Tafea；不要计为 DC。
- VIX: `ixp_inside_government_dc`，只支撑 Port Vila 政府 DC 和互联属性。

查询:

```text
site:interchange.vu (ICN1 OR ICN2 OR ICN3 OR "Port Vila" OR Suva OR Santo OR Tanna OR "Subsea Cables")
"ICN1" "Port Vila" "Suva" "Interchange"
site:pmo.gov.vu Tamtam "data centre" "government broadband"
site:adb.org "Tamtam Submarine Cable Project" "59142-005"
"Vanuatu Internet Exchange" OR VIX "Government Data Centre" "Port Vila"
```

### 1.5 电力、公用事业与大负荷约束

一手来源:

- Utilities Regulatory Authority (URA): https://ura.gov.vu/ 。
- URA on UNELCO: https://ura.gov.vu/en/electricity/whom-do-we-regulate/unelco 。已验证 UNELCO 继续运营 Port Vila electricity concession，期限至 2031-12-31。
- URA on VUI: https://ura.gov.vu/en/electricity/whom-do-we-regulate/vanuatu-utilities-infrastructure-limited 。已验证 VUI 自 2010 年起为 Santo electricity service provider。
- Department of Energy: https://doe.gov.vu/ 。已验证 DOE 新闻页涉及 VUI、UNELCO、能源项目。

用法:

- 任何 MW 级数据中心在瓦努阿图小电网中都必须有电力证据。没有 UNELCO/VUI/URA/DOE 证据的 MW、hyperscale、AI DC 主张应按 C 级或误报处理。
- Port Vila 归 UNELCO/URA 电力背景；Luganville/Santo 归 VUI/URA 背景；Tanna/Malekula 外岛电网仅能支撑小型设施或通信节点，不能支撑未经证实的大型 DC。

查询:

```text
site:ura.gov.vu UNELCO "Port Vila" electricity concession
site:ura.gov.vu VUI Santo Luganville electricity
site:doe.gov.vu (UNELCO OR VUI OR electricity OR "large customer" OR substation) ("data centre" OR "data center" OR ICT OR server)
"Vanuatu" ("data centre" OR "data center" OR "large load" OR MW) (UNELCO OR VUI OR electricity OR grid)
```

### 1.6 规划、建筑、环评、公司注册

一手来源:

- Port Vila Municipal Council / Luganville Municipal Council: 在线许可检索未发现；用 `site:gov.vu`、市政公告和媒体兜底。
- DEPC / environment: 通过 `environment.gov.vu`、`gov.vu`、ADB/World Bank E&S 文件核查海缆和大型建设 EIA。
- VFSC: https://www.vfsc.vu/；VIPA/Investment: 已验证活跃域为 https://investvanuatu.vu/。
- VNSO: https://vnso.gov.vu/，仅作统计背景。

查询:

```text
"Port Vila" "building permit" ("data centre" OR "data center" OR telecommunications OR server)
"Luganville" "building permit" ("data centre" OR "data center" OR telecommunications OR server)
"Vanuatu" DEPC OR EIA ("data centre" OR "data center" OR telecommunications OR "submarine cable")
site:vfsc.vu ("Telecom Vanuatu" OR Digicel OR Telsat OR WanTok OR Interchange OR "data centre")
site:investvanuatu.vu (telecommunications OR ICT OR "data centre" OR "data center" OR Interchange)
```

### 1.7 官方云区域缺失检查

仅使用官方页面做 A 级存在/缺失判断:

| 提供商 | 官方页面 | VU 信号 |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | 未列 VU Region / Local Zone。 |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | 未列 VU 公共区域。 |
| Google Cloud | https://cloud.google.com/about/locations | 未列 VU region。 |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | 未列 VU public cloud region。 |

查询:

```text
"Vanuatu" ("AWS Region" OR "AWS Local Zone" OR "Azure region" OR "Google Cloud region" OR "OCI region")
"Vanuatu" ("cloud region" OR hyperscale OR "data residency" OR "sovereign cloud")
site:cert.gov.vu "Data Protection" Vanuatu
site:dcdt.gov.vu "Data Protection" Vanuatu
```

## 2. 当前官方设施/项目种子清单 (Current Official Facility / Project Seed List)

| 候选 | 省份 | 状态 | 来源等级 | 登记方式 |
|---|---:|---|---|---|
| Vanuatu Government Data Centre, Port Vila | Shefa | 官方确认存在；DCDT 页面列 VGDC brochure，DCDT VIX 页面说明 VIX housed at VGDC in Port Vila；PMO 2025-11-26 COM 指示 complete implementation | A | `government_dc`。地址细节、机架数、冗余站点用 VGDC PDF/采购/后续公告复核；不登记为商业 colo。 |
| Data Centres / Cloud Pilot Project（State property） | 未披露；行政上优先查 Shefa | PMO 确认项目和国家所有权；状态为 implementation / project unless completion evidence found | A | `government_dc_project`。未披露地点不可分配到 Santo 或其他省份。 |
| Vanuatu Internet Exchange (VIX) at VGDC | Shefa | DCDT 确认 VIX housed at Government Data Centre in Port Vila | A | `ixp_inside_government_dc` / `colo_adjacent_interconnection` 属性；VIX 本身非商业 DC。 |
| ICN1 Port Vila landing station / cable station | Shefa | 运营中海缆；Interchange 官方证实 Port Vila-Suva; 2014 完成 | A | `telecom_cable_station`，非 DC。若有 RIO/设备接入证据，可加 `colo_adjacent_telecom`。 |
| Tamtam Submarine Cable nodes / landing sites | Sanma、Malampa、Shefa、Tafea | ADB/PMO 项目；连接 Lifou, New Caledonia 与 Vanuatu，服务 Santo、Malekula、Efate、Tanna；状态按最新 ADB/PMO 文件更新 | A | `telecom_cable_station_project` / `connectivity_project`，非 DC。 |
| TVL/Vodafone, Digicel, Telsat/WanTok network facilities | Shefa 为主；Luganville/Santo 可能有网络节点 | TRBR/运营商可证实服务商存在；设施功能需另证 | A（牌照/存在）；C/B（设施推断） | `telecom_core_lead`，不得无证升级为 DC。 |

## 3. 各省官方枚举策略 (Per-Province Official Enumeration Strategy)

通用清扫 (Generic sweep):

```text
"{Province}" Vanuatu ("data center" OR "data centre" OR datacenter OR colocation OR "server room" OR "Government Data Centre" OR "cable station" OR "landing station" OR ICT)
site:dcdt.gov.vu "{Province}" ("data centre" OR "data center" OR VIX OR broadband OR Tamtam)
site:pmo.gov.vu "{Province}" (Tamtam OR "data centre" OR "data center" OR broadband OR digital)
site:trbr.vu "{Province}" (telecommunications OR internet OR broadband OR cable OR "Universal Access")
site:ura.gov.vu "{Province}" (UNELCO OR VUI OR electricity OR concession)
```

| 省份 | 预期产出 | 官方优先路线 | 说明/归属规则 |
|---|---|---|---|
| Shefa | 最高 | DCDT/PMO、TRBR、Interchange/ICN1、URA/UNELCO、采购、VFSC | Port Vila / Efate 是 VGDC、VIX、ICN1 和多数运营商/政府 ICT 的默认归属。政府数据中心、VIX 和 ICN1 可登记；运营商核心仍需设施证据。 |
| Sanma | 中 | PMO/ADB Tamtam、TRBR、URA/VUI、MIPU、Luganville 检索 | Santo/Luganville 是 Tamtam 覆盖节点和可能网络节点；除非来源点名 data centre / DC project，不登记为 DC。 |
| Malampa | 低-中 | PMO/ADB Tamtam、TRBR UAP、MIPU、DOE/URA | Malekula 是 Tamtam 覆盖节点；作为 `connectivity_project`，不推断 DC。 |
| Tafea | 低-中 | PMO/ADB Tamtam、TRBR UAP、DOE/URA | Tanna 是 Tamtam 覆盖节点；旅游/卫星/小电网 ICT 仅作连接性线索。 |
| Penama | 很低 | TRBR UAP、DCDT/PMO 通用清扫、灾后/教育 ICT | Ambae/Pentecost/Maewo 的 ICT 多为接入、学校、灾后恢复；无命名设施则 `no_projects`。 |
| Torba | 很低 | TRBR UAP、DCDT/PMO 通用清扫、外岛通信项目 | Torres/Vanua Lava/Sola 主要为移动/卫星/政府服务接入；无命名设施则 `no_projects`。 |

覆盖检查: 上表恰好覆盖全部 6 省各一次。

## 4. 负控与升级规则 (Negative Controls And Promotion Rules)

- `government_dc`: 必须有 DCDT/PMO/采购/项目文件点名政府数据中心和地点或清楚归属。
- `commercial_colo`: 必须有运营商官方产品页、合同、资费或设施页明示在瓦努阿图提供 colocation、rack、data centre hosting、disaster recovery site。
- `telecom_cable_station`: 海缆登陆站/节点可登记为电信设施，但非 DC。
- `connectivity_only`: Starlink、Kacific、SES/O3b、移动塔、VSAT、Wi-Fi、学校 ICT、社区互联网、海缆覆盖。
- `false_positive`: 泛 SEO 的 “Port Vila data center services / VPS / dedicated server” 页面，无本地设施、运营商、地址或监管锚点。
