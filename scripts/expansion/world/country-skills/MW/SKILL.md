---
name: mw-datacenter-methodology
location: scripts/expansion/world/country-skills/MW/SKILL.md
description: 马拉维数据中心发现与审计方法学（bilingual）。Malawi datacenter discovery & audit methodology: enumerate the official/regulatory/cloud pipeline (MACRA/DPA, Ministry of Information e-Government, PPPC/DIGMAP, PPDA/PPPC/RBM procurement, MERA/ESCOM/EGENCO power, MITC/SEZ, council planning, cloud-region absence checks) plus industry/trade-press discovery (operators, colo, telco, IXP, trade press). Division model: region with 3 divisions (Central Region, Northern Region, Southern Region). Read before running MW exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# MW · 马拉维数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：马拉维无公开全国数据中心注册库、无统一全国规划许可数据库，且为小规模、早期、**双极**数据中心市场（政府/托管密度在利隆圭 Central Region，电信/银行/灾备密度在布兰太尔 Southern Region，北部无已核实设施）；本方法论通过**官方/监管/云管线（explorer-official.md）**与**行业/厂商/媒体发现（explorer-industry.md）**双轨三角验证（registry-status / triangulation approach），将牌照与数据保护注册、政府云/采购记录、电力证据、市议会规划与运营商/行业媒体证据拼合成可审计清单。本 skill 汇总两份最终审定的探索报告，作为 MW 探索/审计批次的入口。

## 入口

| 文件 | 管线 | 内容 |
| --- | --- | --- |
| explorer-official.md | 官方/监管/云管线 | MACRA（通信牌照 + 2024 数据保护法下的数据保护署）、信息部/e-Government 司（ict.gov.mw）、PPPC/DIGMAP（世行 Digital Malawi）、PPDA/PPPC/RBM 采购线、MERA/ESCOM/EGENCO 电力线、MITC/经济特区、市议会规划/建筑许可、云区域缺失检查 |
| explorer-industry.md | 行业/厂商发现 | 运营商（Government DC、Huawei NDC、OCL、MTL、TNM、Airtel、CTN、Korena/1nga）、MIX-BT/PeeringDB、行业媒体（DCD、ITWeb Africa、Capacity、Canonical）、目录→主源工作流 |

## 核心结构事实

1. **行政区划模型**：manifest 为 **region**，3 个 division 精确使用 **`Central Region`、`Northern Region`、`Southern Region`**（全国 28 县）；首都 **Lilongwe**（中央区）、商业首都 **Blantyre**（南部区）、北部主要城市 **Mzuzu**。每个 division 都必须覆盖，即使预期产出低。
2. **无公开注册库**：枚举须联合 MACRA（通信牌照**兼**2024 年《数据保护法》下的数据保护署）、信息部/e-Government 司（ict.gov.mw）、PPPC/DIGMAP（世行 Digital Malawi Acceleration Project）、PPDA/PPPC/RBM 采购记录、MERA/ESCOM/EGENCO 电力证据、MITC 投资/经济特区文书、Lilongwe/Blantyre/Mzuzu 市议会规划记录。
3. **双国家数据中心架构**：**Government Data Centre（利隆圭，世行资助，PPPC/DIGMAP 下，设计为 Primary，超融合基础设施 HCI）** + **National Data Centre（布兰太尔，华为承建，2022-07 投运，官方指定 Secondary/Backup）**；两者均为官方/运营商级种子，**均未披露 MW 容量**。
4. **电力是闸门过滤器**：马拉维电网容量受限（EGENCO 2025-08 声明约 500 MW 发电 vs 约 1,000 MW 需求；MERA 2022-26 基础电价申请文件记录每日高达约 10 小时限电）；任何 “云” 声称在具备 备用发电/燃料储存/UPS/光伏自备发电/BESS/供电协议 等决定性证据字段前不得升为设施级。**公开源未披露任何马拉维数据中心的 IT MW 或设施 MW**——`capacity_mw` 预期保持 null；**不得把 kVA/UPS 数值换算为 MW**。
5. **数据保护法律背景**：《2024 年数据保护法第 3 号》（2024-02 宪报，2024-06-03 生效）指定 **MACRA 为数据保护署**，控制器/处理者注册经 dpa.mw 进行；2026-06 MACRA 就重要数据控制器/处理者拟议注册费征求意见。该法是 A 级需求/法律背景，**非设施证明**——注册本身不得推断出数据中心。
6. **云区域为缺失检查（2026-08-12 核对）**：AWS/Azure/Google Cloud/Oracle OCI/华为云**均无马拉维公共区域**；最近的公共区域在南非（约翰内斯堡/开普敦）。任何马拉维 “cloud region” 声称除非官方区域页列名，否则按本地/混合/合作伙伴云处理；华为在马拉维的角色（2022 年布兰太尔国家数据中心）是项目/设备记录，不是公共云区域证明。
7. **关键官方记录（A 级）**：Government Data Centre Lilongwe（DIGMAP 2024-03-01 文章：在建 51%、预计 2024-05 完工、HCI、利隆圭=Primary/布兰太尔=Secondary；世行 2025-06-23 成果简报确认建成）；**National Data Centre 扩建，利隆圭**（PPPC RFB **MW-PPPC-494042-GO-RFB**，项目场地位于利隆圭 Paul Kagame 路沿线，指出现有 Production Site 为 **Tier-III** 设施，披露两台 160 kVA UPS 与 HCI 节点细节但无 MW；状态 planned/procurement）；**Reserve Bank of Malawi Corporate Data Centre（CDC），Blantyre 分行**（ITB **RBM/ICT/BT/01/2025**，2025-11-13 发布、2025-12-03 截标，设计与建造；planned）。
8. **运营商/行业种子（分级）**：**OCL Enterprise Data Center**（Kanengo, Lilongwe；运营商页声称 world-class、99.982% 可用性、冗余电力/制冷/网络，2023-12-01 起企业托管；A 级运营商/设施声称，容量/地址待核实）；**MTL Data Centre/DataCENTRE**（运营商页宣传机架/地板托管、专用互联网/VPN、消防、空调、UPS、生物识别、CCTV；A 级运营商服务声称；2026-08-12 TLS 链未验证需 `curl -k`，记录抓取注意事项而非降级内容）；**Airtel Malawi DC, Blantyre**（2013-12 DCD 报道，B 级、2013 年记录——**核实当前状态**）；**TNM**（两个现有 DC + 2026-03-05 宣布拟建第三个 DC（ITWeb Africa，B 级），Charmed OpenStack 私有云）；**CTN 微数据中心, Lilongwe**（2026-02 ITWeb Africa 宣布，AI 微 DC/GPU-as-a-Service，B 级，无场地/容量）；**Korena/1nga Solutions, Blantyre**（korena.mw 声称 Tier III+ 主权 AI 云/DC 园区、Mawatt 垃圾发电、NVIDIA A100/H100 GPU 云——**页面联系电话为占位式号码、无任何独立第三方确认**：营销声称存在 A 级、物理状态 U/未验证）；**ESCOM 数据中心**（ML.mw 博客，C 级线索）；**Mzuzu 大学数据中心概念**（2021 学术材料，C 级概念非设施）。
9. **区域殖民玩家缺席**：Raxio、Africa Data Centres、Teraco/Digital Realty、Equinix/iColo、Wingu、Paratus、Liquid Intelligent Technologies **在马拉维均无已核实数据中心**（Liquid 有光纤/网络但无确认公共 DC 设施）；“Kukula”（赞比亚投资公司，无关）与 “2090” 无 DC 证据——如实记录已查空线索。
10. **网络证据边界**：马拉维为内陆国，**无海缆登陆**（国际容量经赞比亚/坦桑尼亚/莫桑比克或第三国登陆）；**MIX-BT**（马拉维互联网交换，MISPA 运营，布兰太尔医学院，2008-12-04 起，约 10 个对等方/46G）为网络存在证据（A/B），**非 DC 证明**；国家光纤骨干/MTL 骨干为连通性驱动，非 DC 证明。
11. **可靠性分级（字段级而非记录级）**：A = 该字段的主源（监管/政府/运营商页、MACRA 牌照或咨询、MERA/ESCOM/EGENCO 电力文件、PPPC/DIGMAP 或 PPDA 采购记录、信息部/e-Government 页、RBM 招标/银行记录、MITC/SEZ 文书、市议会规划/建筑记录、官方云区域页、运营商自有设施页）；B = 具名强二手（DCD、ITWeb Africa、Capacity、Developing Telecoms、Connecting Africa、Xinhua、Nyasa Times、The Nation、Maravi Post、Malawi Voice、MANA、厂商案例、PeeringDB/IXP 网络存在页）；C = 仅线索（目录、社媒、泛市场报告、无场地/电力/许可证据的旧 MoU、无支撑容量/地址声称、学术概念论文）。同一设施可存在 A 级运营商存在、B 级 MW/机架数据、C 级地址——逐字段独立分级，**绝不让 A 级存在声称把 C 级地址升为 A**。
12. **状态纪律**：`operational`（已启动且有持续证据）、`under construction`、`planned`（采购/招标）、`announced`（无场地/许可的公开承诺）、`MoU/intent`、`lead only`（无具名设施）、`unverified`（仅营销声称如 Korena）；不得仅凭 法律需求驱动/牌照类别/光纤路线/IXP 成员/云转售/MoU 计数。

## 常用查询模板

```text
site:macra.mw "data centre" OR "data center" OR "cloud" OR "hosting"
site:macra.mw "data controller" OR "data processor" OR "Data Protection Act"
site:dpa.mw "data centre" OR "hosting" OR "registration" OR "cross-border"
site:ict.gov.mw "data centre" OR "National Data Centre" OR "Government Data Centre"
site:digmap.pppc.mw "data centre" OR "data center" OR "cloud"
site:pppc.mw "data centre" OR "National Data Centre"
"MW-PPPC-494042-GO-RFB" "National Data Centre" "Lilongwe"
site:ppda.mw "data centre" OR "server room" OR "ICT infrastructure"
site:rbm.mw "data centre" OR "Corporate Data Centre"
"RBM/ICT/BT/01/2025" "Corporate Data Centre" "Blantyre"
site:mera.mw "data centre" OR "captive power" OR "backup"
site:escom.mw "data centre" OR "substation" OR "BESS" OR "load shedding"
site:egenco.mw "generation" "MW"
site:mitc.mw "data centre" OR "SEZ" OR "ICT"
site:{council-domain} "data centre" OR "building permit" OR "ICT"
site:peeringdb.com/ix "Malawi" OR "Blantyre"
site:datacentermap.com Malawi ; site:datacenters.com "Malawi"
"{operator}" Malawi "data centre" OR "colocation" OR "Tier III"
site:itweb.africa Malawi datacentre ; site:datacenterdynamics.com Malawi
"Malawi" "cloud region" "official" - absence check
"Malawi" "TIA-942" OR "Uptime Institute" OR "Tier IV" - negative control
```

## 官方/监管管线要点（详见 explorer-official.md）

- **MACRA**（1998 年《通信法》Cap. 68:01 设立）：牌照类别（电信服务商、ISP、国际网关、VSAT、广播/内容、邮政/快递）、Malcel 第三移动牌照线索（网络/频谱线索非 DC 证明）、数据保护注册与 2026-06 注册费咨询（云/DC 运营商需求侧信号）。
- **信息部/e-Government 司（ict.gov.mw）**：A 级政府自有数据中心资产表面——National Data Centre（Blantyre）与 Government Data Centre（Lilongwe）官方表述、National Fiber Backbone（连通性非 DC）、e-Government 服务需求证据。
- **PPPC/DIGMAP/世行**：Government Data Centre Lilongwe（Primary）+ NDC 扩建 RFB（MW-PPPC-494042-GO-RFB，Tier-III 措辞、160 kVA UPS、HCI，planned/procurement）。
- **采购线（新/计划设施最高产）**：PPDA/PPPC 电子采购与部门门户（如 dmap.staging.ict.gov.mw、RBM 站内 ITB）发布 ITB/RFP/授标——RBM CDC Blantyre 即例（RBM/ICT/BT/01/2025，2025-11-13 发布、2025-12-03 截标）。
- **电力线**：MERA 牌照/电价文件（A 级电网背景）、ESCOM 配电网/变电站/馈线/限电表/BESS（12 个 BESS 集装箱 2026-01 起交付利隆圭 Kanengo）、EGENCO 发电状况（约 500 MW vs 约 1,000 MW 需求）；**单位原样保留**（IT MW/设施 MW/连接负荷/MVA/发电机 kVA/光伏 MW 分字段，源不换算则绝不换算）。
- **投资线**：MITC 一站式投资促进；《2025 年经济特区法》监管 SEZ 计划；2026-08-12 无任何 SEZ 特定数据中心租户——仅监控。
- **市议会规划**：马拉维市议会发布可检索许可数据极少；优先 Lilongwe（lcc.gov.mw）、Blantyre（bcc.mw）、Mzuzu 市议会与 Zomba，跨查 Ministry of Local Government 目录；首用前核实域名。
- 分 region 诚实产出：Central 4–6 条（A 级：PPPC/DIGMAP/世行/RFB/OCL/MTL）、Southern 3–5 条（NDC Blantyre、RBM CDC、Airtel 2013、Korena 声称、ESCOM 线索）、Northern 0–1 条（大概率无，如实记 `no_projects`）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 高收益行业源：DCD（2022-07-28 马拉维启用国家数据中心；2013-12-03 Airtel Blantyre DC）、ITWeb Africa（TNM 第三个 DC 2026-03-06、CTN 微 DC 2026-02）、Capacity（2022-07-26 华为 NDC）、Xinhua（2022-07-23 投运官方通稿，B+/A）、Canonical（TNM Charmed OpenStack 案例）、ML.mw 博客（Tier 3 by Huawei 措辞与实体清单，B/C）、本地媒体（Nyasa Times、The Nation、Maravi Post、Malawi Voice、MANA）。
- 确认工作流：发现（媒体/目录/采购/营销）→ 锚定（运营商/政府页 A 级存在与角色；传输/TLS 问题单独记抓取注意事项，可用 `curl -k` 复现读取则不降级）→ 独立二次确认（政府/监管/采购/强媒体）→ 逐字段分级 → 状态纪律 → 容量 null 如实 → 三 region 全覆盖、无产出显式说明。
- 诚实记录（2026-08-12 已核实）：ocl.mw/tier3.html、mtl.mw（curl -k）、korena.mw（占位电话）、digmap.pppc.mw、PPPC RFB 页/PDF、ict.gov.mw、rbm.mw ITB PDF 均打开；mtl.mw TLS 链注意事项；Airtel 2013、TNM DC 数量/位置、NDC Blantyre MW/认证为待复核旧记录；无超大规模云区域；区域殖民玩家缺席。

## 维护注意（更新纪律）

- **更新节奏**：每月——MACRA 咨询/牌照新闻、ict.gov.mw、digmap.pppc.mw、PPPC/PPDA/RBM 采购（CDC 授标、NDC 扩建授标）、运营商页（OCL/MTL/TNM/Airtel/CTN）；每季度——云区域页（缺失复查）、认证注册库（TIA-942/Uptime 负向控制）、ESCOM 电力新闻（BESS/连接）、MITC/SEZ 通告、MIX-BT PeeringDB；里程碑事件——RBM CDC 授标/开工、NDC 扩建授标/完工、TNM 第三 DC、任何新政府 DC 采购；每年——云区域年度验证查询、市议会域名与规划记录核实。
- **来源核验**：复核层逐个点击 A 级 URL；字段级分级并独立记录 URL/标题/发布者/访问日期/引用字段；旧记录（Airtel 2013、TNM 数量、NDC Blantyre MW/认证）须复核现状；mca.ac.mw 旧镜像 2026-08-12 返回 404 不得再用（除非重新核实）。
- **不删除纪律（no-deletion）**：已复核记录不得删除；状态变化改标（如 2022 投运 → 后续持续证据）并保留原始证据链；无支撑线索降级保留并注明缺失证据；任何未经官方显式披露的 MW 数字均为红旗。
