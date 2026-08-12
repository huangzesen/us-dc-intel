---
name: np-datacenter-methodology
location: scripts/expansion/world/country-skills/NP/SKILL.md
description: 尼泊尔数据中心发现与审计方法学（bilingual）。Nepal datacenter discovery & audit methodology: enumerate the official/regulatory/cloud pipeline (DoIT directive + listed-provider roster, IDMC/GIDC, NTA, NTC, MoCIT, MoF/NPC budget, PPMO/e-GP procurement, OCR/IRD, NEA/ERC, cloud-region absence checks) plus industry/trade-press discovery (operator pages, DCD/NepaliTelecom/ICT Frame/TechSansar, NPIX/PeeringDB, directories). Division model: province with a single country-level division “-” (7 provinces as internal coverage checklist). Read before running NP exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# NP · 尼泊尔数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：尼泊尔无公开全国数据中心注册库（但 **DoIT 已发布数据中心与云服务商注册名册**，为全国 A 级提供商清单）；本方法论通过**官方/监管/云管线（explorer-official.md）**与**行业/厂商/媒体发现（explorer-industry.md）**双轨三角验证（registry-status / triangulation approach），把 DoIT 指令与注册名册、政府 IDMC/GIDC 设施、预算/采购记录、电力与实体证据、运营商页面与媒体证据拼合成可审计清单。本 skill 汇总两份最终审定的探索报告，作为 NP 探索/审计批次的入口。

## 入口

| 文件 | 管线 | 内容 |
| --- | --- | --- |
| explorer-official.md | 官方/监管/云管线 | DoIT 指令文本与注册名册、IDMC/GIDC 与 Hetauda DR、NTA（电信监管）、NTC、MoCIT、MoF/NPC 预算、PPMO/e-GP 采购、OCR/IRD 实体、NEA/ERC 电力、IBN/DoI/SEZ、NRB、云区域缺失检查 |
| explorer-industry.md | 行业/厂商发现 | DoIT 名册逐家解析、运营商主页面（Ncell、DataHub、Cloud Himalaya、NTC、WorldLink、Vianet 等）、DCD/NepaliTelecom/ICT Frame/TechSansar/本地媒体、NPIX/PeeringDB/PCH 互联、目录与多语言检索 |

## 核心结构事实

1. **行政区划模型**：manifest 为 **province**，divisions 为 **`["-"]`（单一国家层占位）**——有效运行必须产出一个国家层输出 division `-`，同时显示 **7 个省全部清扫过**（Koshi、Madhesh、Bagmati、Gandaki、Lumbini、Karnali、Sudurpashchim）。省份仅作覆盖检查表，不得当作数据行。
2. **DoIT 指令与注册名册**：**《数据中心与云服务（运营和管理）指令 2081》**（doit.gov.np）要求 DC/云服务商向 **DoIT 注册**并提供 tier/评级证据，政府数据托管 DC 须达三级（tier 3）或以上。**DoIT 注册名册**（2026-08-12 已核实名单：Ncell Axiata Ltd；Access World Tech Pvt. Ltd；Silver Lining Pvt. Ltd；Data Hub Pvt. Ltd；Dish Media Network Ltd；Digital Network Solution / Everest Cloud（仅云）；Times Global Pvt Ltd）为 A 级提供商证据，但**名册≠设施**——除非另有物理站点证据，不得把注册名册换算为设施数量；Everest Cloud 当前仅云服务，不得计为物理数据中心。
3. **政府数据中心**：**IDMC（Integrated Data Management Center）/ GIDC（政府综合数据中心，加德满都）** 经 https://idmc.gov.np/ 为当前政府 DC 运营路线（A 级当前角色；旧 NITC 路线保留作历史）；**Hetauda 灾备中心（DR）**为 GIDC 备份，媒体报道 2019-05 在 Hetauda 投入使用（A/B：政府/IDMC 上下文 + 媒体细节 B）。
4. **关键机构**：DoIT（指令+名册）、NTA（电信监管，牌照/ISP 上下文）、Nepal Telecom/NTC（国有电信，采购与 DC 项目）、MoCIT（政策）、MoF/NPC（预算演讲/红皮书：综合国家数据中心升级、Hetauda DR 扩建、Kohalpur 政府 DC、中丘陵 DC 可行性、Syuchatar 主权 AI 计算中心等预算行）、PPMO/e-GP（bolpatra.gov.np/egp，招标与授标）、OCR/IRD（实体与税务身份）、NEA/ERC（电力/变电站/电价）、IBN/DoI/SEZ（投资/外资/园区）、NRB（银行 ICT/BCP 需求背景）。
5. **已核实设施/项目证据状态**：Ncell Nakkhu IDC（Lalitpur；运营商页+DoIT 名册 A；ANSI/TIA-942-C Rated 3 认证须捕获认证机构清单为 A，否则媒体/运营商 B）；DataHub（加德满都 + Butwal/Tilottama 双数据中心，Yeti Cloud，Hosted AI 合作——运营商页 A，启动时点 B）；Cloud Himalaya（加德满都托管/云；Tier-4 营销 U/B 直至认证机构证实）；WorldLink/Data World（Chandragiri；DCD 报道 3.5 MW、520 机架，B 级直至运营商主页面捕获；Mata Tirtha 变电站邻近 B/C；Tier/Edge 认证无认证机构则 U/B）；NTC 加德满都/白拉瓦（Bhairahawa）华为 DC 项目（计划/在建，行业媒体 B，须 NTC/PPMO/e-GP 授标文件升级）；**Syuchatar 主权 AI 计算中心**（FY 2083/84 预算宣布，捕获 MoF 预算文本为 A，否则 B——不得标记运营）；**Kohalpur 政府 DC**（Lumbini，FY 2082/83 预算行，宣布/计划）；Vianet Central Business Park DC（火灾/中断事件报道 B 存在，地址/容量 C/U）；Access World/Silver Lining/Dish Media/Times Global（DoIT 名册 A，物理设施 U）；NEA 内部 DC（C/U）。
6. **云区域为缺失检查**：本遍未发现任何官方 AWS/Google Cloud/Azure/Alibaba/OCI/华为云区域或本地区列表点名尼泊尔；每轮重查官方列表后再记录；不得从合作伙伴接入、CDN 缓存或境外 Direct Connect/ExpressRoute/Interconnect 生成尼泊尔超大规模区域记录。本地云/托管单独计数：Ncell Cloudsuite/Nakkhu、DataHub/Yeti Cloud/YetiCloud.ai、IDMC/GIDC 政府云、Cloud Himalaya 及任何有物理证据的 DoIT 名册提供商。
7. **多语言检索**：英语+尼泊尔语为主（डाटा सेन्टर / डेटा सेन्टर / डाटासेन्टर / डाटा केन्द्र / क्लाउड / क्लाउड सेवा / कोलोकेशन / को-लोकेशन / सर्भर / सर्भर रुम / आईडीसी / टियर / र्याक / मेगावाट / विद्युत / भुकम्प，以及 7 省与重点城市拼写）；中文/韩文/印度厂商术语仅用于华为/KOICA/Airtel Nxtra 类线索。
8. **互联证据边界**：NPIX（npIX DH，PeeringDB ix 241）、PCH Putalisadak（pch.net/ixp/details/159）、bgp.he.net 可确认网络/IXP 存在，但 **IXP 节点不是数据中心记录**；尼泊尔为内陆国、无直接海缆登陆，跨境/转接/带宽证据只是连通性上下文。
9. **可靠性分级（字段级）**：A = 官方政府/注册/法律/公用事业/预算/云区域列表、主 IXP/PeeringDB、认证机构或运营商自有源；B = 可靠行业/本地媒体、律所分析或厂商/伙伴源（具名项目事实）；C = 目录、经纪列表、市场报告、社媒或弱转载；U = 本轮查证后未验证。DoIT 名册条目为 A 级提供商证据，但不是地址/容量/认证/可用性证据；运营商页对存在与声称 A，Tier/MW/机架/SLA 声称须认证机构、采购或工程证据才能 A；目录与市场报告仅 C 级线索；预算/MoU/内阁/新闻宣布项在出现采购、建设、投运或服务证据前一律为 planned。
10. **非设施红线**：总部、电信交换局、NOC、CDN/缓存节点、IXP 交换、银行服务器机房、转售页、云品牌——除非源点名物理数据中心/托管/云基础设施设施/政府 DC 场地；`no_projects` 仅在所有 7 省的英语+尼泊尔语 官方/运营商/采购/互联 检索均已记录后使用。

## 常用查询模板

```text
site:doit.gov.np ("data center" OR "डाटा केन्द्र" OR "क्लाउड सेवा" OR "listed")
site:doit.gov.np/pages/details-of-listed-data-center-and-cloud "सूचीकृत डाटा केन्द्र"
"Ncell Axiata Ltd" "Data Center" "DoIT" Nepal
"Access World Tech Pvt. Ltd" Nepal ("data center" OR cloud OR colocation)
"Silver Lining Pvt. Ltd" Nepal ("data center" OR cloud OR colocation)
"Data Hub Pvt. Ltd" Nepal ("data center" OR cloud OR colocation)
"Dish Media Network Ltd" Nepal ("data center" OR cloud OR colocation)
"Digital Network Solution" "Everest Cloud" Nepal ; "Times Global Pvt Ltd" Nepal ("data center" OR cloud)
site:idmc.gov.np ("data" OR VM OR VPS OR colocation OR backup OR replication OR Hetauda)
"Government Integrated Data Center" Nepal (Singha Durbar OR Kathmandu OR Hetauda)
site:www.mocit.gov.np ("data center" OR "डाटा सेन्टर" OR cloud OR AI)
site:nta.gov.np ("data center" OR cloud OR IDC OR ISP OR license)
site:www.ntc.net.np ("data center" OR Bhairahawa OR Kathmandu OR Huawei)
site:ppmo.gov.np ("data center" OR server OR cloud OR DR)
site:bolpatra.gov.np/egp ("data center" OR server OR cloud OR DR)
site:www.mof.gov.np ("data center" OR "AI compute" OR Syuchatar OR Kohalpur OR Hetauda)
site:npc.gov.np ("data center" OR "AI compute" OR cloud)
site:nea.org.np ("data center" OR substation OR load OR Syuchatar)
site:ocr.gov.np "{company}" ; site:ird.gov.np "{company}"
"Nepal Telecom" "Huawei" "data center" Bhairahawa Kathmandu
"Sovereign AI Compute Center" Syuchatar OR "Kohalpur" "data center" Nepal budget
"{province_en}" Nepal ("data center" OR IDC OR colocation OR "server room")
"{province_ne}" ("डाटा सेन्टर" OR "डेटा सेन्टर" OR सर्भर OR क्लाउड OR कोलोकेशन)
site:peeringdb.com Nepal (NPIX OR "Access World" OR DataHub OR Ncell OR WorldLink)
site:datacenterdynamics.com Nepal data center ; site:nepalitelecom.com ("data center" OR "डाटा सेन्टर")
"Nepal" ("ANSI/TIA-942" OR "Uptime Institute" OR "Tier III" OR "Tier 3") - certification check
"Nepal" AWS OR Azure OR "Google Cloud" OR OCI region - absence check
```

## 官方/监管管线要点（详见 explorer-official.md）

- 法律/监管工作流：先取 DoIT 指令页与 PDF（2081 指令要求注册与 tier/评级证据）；拉取当前 DoIT 名册；对每家名册提供商在 OCR/IRD 检索准确法律名称，再找物理设施地址/运营服务页/PeeringDB/采购记录/强媒体；NTA 仅用于电信/ISP 上下文（除非未来 NTA 发布 DC/云名册）。
- 预算与国家计划：FY 2082/83 行——综合国家数据中心升级、Hetauda DR 扩建、Kohalpur 数据中心建设/升级、中丘陵 DC 可行性研究；FY 2083/84 行——Syuchatar 主权 AI 计算中心。全部为 planned/announced 直至招标/建设/投运/服务证据出现。
- 采购：PPMO/e-GP 与机构通告页分别检索（避免畸形 `site:a OR site:b`）；NTC 站点查 Bhairahawa/Kathmandu/华为/授标；“Nepal Telecom Rs 484 数据中心”线索跟踪。
- 省检查表：Bagmati（最高优先：DoIT 名册、IDMC/GIDC、Hetauda DR、MoCIT、MoF/NPC、NTA、PPMO/e-GP、NEA 变电站、Kathmandu/Lalitpur/Chandragiri/Syuchatar 城市许可）；Lumbini（DataHub Butwal、NTC Bhairahawa、Kohalpur 预算行）；Koshi/Madhesh/Gandaki/Karnali/Sudurpashchim——预期低产出，Koshi 的 Ncell/Biratnagar 网络 DC 声称须更强来源，Karnali/Sudurpashchim 负向清扫。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 高信号源图：DoIT 名册（用前于目录）、Ncell（Nakkhu IDC、Cloudsuite、认证）、DataHub（双 DC、Yeti Cloud）、Cloud Himalaya（托管/Tier 营销）、DCD（WorldLink 启动、Ncell 启动、DataHub/Hosted AI）、NepaliTelecom（NTC/华为项目、Nakkhu/Tier-3、Vianet 火灾）、ICT Frame、TechSansar（YetiCloud.ai、AI 计算中心、预算）、NepalNews/The Himalayan Times/Republica/Kantipur（AI 计算审查、Hetauda DRC）、Developing Telecoms/Fast Mode/New Business Age。
- 最小工作流：拉 DoIT 名册与指令 → 逐家精确检索并分类（名册/物理站点/仅云/省）→ 加运营商主页面 → 搜行业媒体（启动/认证/火灾/授标/AI 云宣布）→ 搜 PPMO/e-GP/NTC 建设采购 → NPIX/PeeringDB/PCH 枢纽佐证 → 运行并记录 7 省英语+尼泊尔语清扫 → 字段级分级与状态。
- 陷阱：加德满都/Thapathali/Central Business Park 类线索按 运营商/地址/ASN/服务页/事件报道 去重；`Kathmandu` 营销默认归 Bagmati（除非点名他市）；Tier/MW/机架/可用性/“首个”“最大”“唯一”在无认证机构/官方采购规格/工程文件时一律为声称；谷歌/JV/Bichuten 类社媒与市场报告声称保持 U。

## 维护注意（更新纪律）

- **更新节奏**：每月——DoIT 名册、DoIT 指令更新、IDMC/GIDC 页、NTA 通告、NTC/PPMO/e-GP 招标、NTC 华为项目、Syuchatar AI 计算中心、Kohalpur/Hetauda 预算行；每季度——名册提供商 OCR/IRD 实体刷新、NEA/ERC 电力事实、PeeringDB/NPIX、认证机构、超大规模官方区域/本地区列表；每年或法律变更后——完整 7 省清扫、Digital Nepal/电信法案/数据保护状态复核、空省 `no_projects` 记录复核。
- **来源核验**：复核层逐个点击 A 级 URL；standinglist.nta.gov.np 可能 TLS 证书问题（用浏览器）；non-www mocit.gov.np 可能证书校验失败（用 www 形式）；nitc.gov.np 可能超时（优先 idmc.gov.np）。
- **不删除纪律（no-deletion）**：已复核记录不得删除；状态变化改标并保留原始证据链；无支撑声称降级为 lead/U 而非移除；名册条目仅因注册名册存在不得自动计数为物理设施。
