---
name: pk-datacenter-methodology
location: scripts/expansion/world/country-skills/PK/SKILL.md
description: |
  Pakistan (PK) datacenter discovery & audit methodology — how to enumerate, verify, and update Pakistan datacenter projects at first-level-unit + city granularity (7 units: Punjab, Sindh, Khyber Pakhtunkhwa, Balochistan, Islamabad ICT, Gilgit-Baltistan, Azad Kashmir). Pakistan has no public national datacenter registry and no hyperscale cloud region: enumeration joins PTA licensing, MoITT/SIFC/BOI project records, PPRA/e-PADS procurement, NEPRA power sanity checks, Uptime Institute PK awards page (PTCL DC-1/DC-2, SBP MDC, NTC, Sky47, Transworld KR1, Safe City), NTC/NADRA government cloud, operator pages (Jazz Digital Park, Zong CICC, Data Vault, QGDC, Khazana), PKIX/PIE/PeeringDB interconnection, and Karachi cable-landing geography. Read this before running PK exploration/audit batches. Routes to explorer-official.md (regulators/procurement/certification/divisions) and explorer-industry.md (operators/IXP/subsea/directories/Urdu recipes).
---

# PK · 巴基斯坦数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：巴基斯坦**没有**公开的全国数据中心注册库（PTA 发电信牌照、无独立公共 DC 设施类别）；公共建筑许可门户非发现源；**Uptime Institute 巴基斯坦授奖页**（uptimeinstitute.com/.../country/id/PK）是最高效的官方锚点；AWS/Azure/GCP/OCI/Huawei 官方区域页均无巴基斯坦（每季度负向核验）。枚举采用“牌照/部委项目 → 采购 → Uptime 授奖 → 运营商页 → IXP/海缆”多轨。
> 分区模型：**7 个一级单位**（Sindh、Punjab、Islamabad ICT、Khyber Pakhtunkhwa、Balochistan、Gilgit-Baltistan、Azad Kashmir）；Karachi（Sindh）= 商业/国际互联枢纽，Islamabad（ICT）= 联邦/电信/云枢纽，Lahore（Punjab）= 第二商业/政府枢纽，其余以机构/公共设施为主。
> 已知种子：PTCL Commercial DC-1 Lahore / DC-2 Karachi、SBP Main Data Center Karachi（Design+Constructed 双奖）、NTC Main Data Centre/DRC Lahore + 政府云、Data Vault Karachi、QGDC Karachi（Huawei $230m）、Transworld KR1、Sky47 Karakoram 1（Islamabad）、Jazz Digital Park、Zong CICC、NADRA Safe City DC、KP 政府 Tier-III DC（策略声明）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供巴基斯坦探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：PTA/MoITT/SIFC/BOI、PPRA/e-PADS 采购、NEPRA 电力、Uptime PK 授奖页、NTC cloud.gov.pk/NDC、PID、PKIX、7 单位逐区覆盖与官方种子证据表、认证规则、云区域缺席检查 |
| `explorer-industry.md` | 行业/厂商发现：运营商种子表（PTCL/Jazz/Zong/NTC/NADRA/Data Vault/QGDC/Transworld/Sky47/Khazana/Multinet/CubeXS/NOVA 等）、PeeringDB fac/ix 快照（PKIX Lahore、PIE Karachi DE-CIX/PTCL）、Karachi 海缆着陆（SEA-ME-WE 3-6/I-ME-WE/AAE-1/PEACE/2Africa/Africa-1/2）、目录（C）、乌尔都语搜索配方、7 单位策略 |

## 核心结构事实（框定每次搜索）

1. **无全国注册库、无云区域**：设施记录须联合 Uptime 授奖/PTA/MoITT/采购/运营商页/PeeringDB；任何“巴基斯坦云区域”措辞在超大规模官方区域页点名巴基斯坦前一律视为本地/主权/伙伴云。
2. **Uptime PK 授奖页是 A 级锚点**：截至 2026-08-12 列有 8 项——GoS Board of Revenue DC（Karachi）、Islamabad ICT Safe City DC（NADRA）、NTC Main Data Centre（Lahore）、PTCL DC-1（Lahore）、PTCL DC-2（Karachi）、Sky47 Karakoram 1（Islamabad）、SBP MDC（Karachi，Design+Constructed 双奖）、Transworld KR1（Karachi）；**仅 A 于授奖类型/城市/客户**，多数为 Tier III Design Documents 而非建成设施认证。
3. **“Tier III”措辞纪律**：Jazz/Zong/PTCL/Sky47 的 TIA-942/Tier-III 营销按源措辞记录；`designed to Tier III`/`compliant`/`certified` 不自动等于运营韧性；Uptime/TIA 认证记录才升级。
4. **采购/部委记录只在其点名项目时用**：PPRA/e-PADS + 省级采购搜 `data center`/`server room`/`DR site`/`cloud migration`/`UPS`/`generator` + 乌尔都语 `ٹینڈر`；招标仅证意图，跟进授标/合同/完工报告后才入账。
5. **电力仅作可行性核验**：NEPRA/DISCO/NTDC 用于功率可行性；MW/kVA/kW 仅在确切设施源声明时记录，不从公司发电资产或电网连接推断。
6. **互连/海缆是枢轴非设施证据**：PKIX（Islamabad 发源、Lahore/Karachi 节点）、PIE Karachi（DE-CIX/PTCL）、PeeringDB `fac`/`ix` API（每次运行重拉，用户维护易变）；Karachi 为海缆枢纽（SEA-ME-WE 3/4/5/6、I-ME-WE、AAE-1、TW1、PEACE、2Africa、Africa-1/2）；登陆站非商业 DC，除非源声明 DC/colo/云服务。
7. **城市归属严谨**：Islamabad ICT 与 Rawalpindi（Punjab）是不同清单分区；Sky47 等城市声明须按源定位。
8. **语言**：英语优先，乌尔都语 `ڈیٹا سینٹر`/`سرور روم`/`کلاؤڈ`/`ڈیجیٹل انفراسٹرکچر`/`کولوکیشن` 用于本地媒体/采购；域名过滤 `site:` 优先于裸 OR。

## 查询模式（复制粘贴模板见 explorer-official.md / explorer-industry.md）

- 官方：`site:pta.gov.pk ("data center" OR cloud OR hosting OR CVAS)`、`site:moitt.gov.pk ("data center" OR "cloud first" OR "national data centre")`、`site:sifc.gov.pk ("data center" OR AI OR "digital infrastructure")`、`site:eprocure.gov.pk ("data center" OR "server room" OR "disaster recovery")`、`site:ppra.org.pk ("data center" OR server OR "ICT infrastructure")`。
- Uptime/认证：`site:uptimeinstitute.com/uptime-institute-awards/country/id/PK Pakistan`、`site:uptimeinstitute.com/.../PK "{operator}"`。
- 运营商：`"{operator}" Pakistan ("data center" OR colocation OR hosting)`、`"{operator}" ("Tier III" OR "TIA-942" OR Uptime) Pakistan`、`"{operator}" (Karachi OR Lahore OR Islamabad OR Rawalpindi) (racks OR MW OR kVA)`、`site:peeringdb.com "{operator}" Pakistan`。
- 分区/乌尔都语：`"{division}" "data center" Pakistan government`、`"{city}" "ڈیٹا سینٹر" Pakistan`、`"{division}" ("ڈیٹا سینٹر" OR "سرور روم" OR "کلاؤڈ")`。
- 互连/海缆：`site:submarinecablemap.com/landing-point/karachi-pakistan`、`"Transworld" "SEA-ME-WE 6" Karachi "data center"`、`"2Africa" Pakistan Karachi Transworld`、`site:peeringdb.com/api/fac?country=PK`。
- 媒体：`site:datacenterdynamics.com Pakistan ("data center" OR "data centre")`、`site:dawn.com "data center" Pakistan`、`site:brecorder.com Pakistan "data centre" OR QGDC`、`site:propakistani.pk "data center"`。

## 官方/监管管线要点（详见 explorer-official.md）

- 入口：PTA 牌照/公告 → MoITT（Cloud First/数字政策/MoU，意图仅记）→ SIFC（Data Vault 等投资管道）→ BOI → PPRA/e-PADS 采购 → NEPRA 电力核验 → Uptime PK 授奖 → NTC/cloud.gov.pk/PID → PKIX。
- 7 单位姿态：Sindh 主枢纽（Karachi：PTCL DC-2、SBP MDC、Board of Revenue DC、Transworld KR1、Data Vault、QGDC、海缆登陆站）；Punjab 次枢纽（Lahore：PTCL DC-1、NTC MDC/DRC、PSCA、Rawalpindi 小心归位）；Islamabad ICT 联邦集群（Zong CICC、Jazz Digital Park、Sky47、NTC/NITB/NADRA、Safe City DC、PKIX/PERN）；KP（Tier-III 政府 DC 策略声明 + KPITB/STP，无商业 colo 证实）；Balochistan（警察 D3C Quetta、Turbat 大学 DC，机构级）；GB/AJK 负向默认（Cloud First 政策 ≠ 本地 DC）。
- 认证规则：Uptime 授奖仅对展示的授奖事实 A；Design Documents ≠ Constructed Facility（SBP MDC 双奖例外）。
- 证据规则：按字段分级；目录计数非普查；“最大/首个/超大规模/AI-ready”为营销声明；登陆站/IXP/电信交换局/服务器机房不入商业 DC 清单，除非源明确提供 colo/云/托管。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 运营商种子：PTCL（A 服务 + Uptime 双奖）、Jazz Digital Park（A 运营商声明：300+ 机架可扩 450、3 MW、TIA Tier-III；非 Uptime）、Zong CICC（A 开业 + 公司称 Tier-III Certified；Uptime 未列）、NTC/政府云（A/B 官方措辞，容量 U）、NADRA（A 实体/授奖 + B CGD 两 DC 相距 150 英里/第三座计划）、Data Vault（A SIFC 开业声明/公司；GPU/太阳能/最大声明须主源）、QGDC（A 公司/B 项目经济性：Gul Ahmed Energy + Huawei $230m）、Transworld KR1（A 授奖/B 时间表）、Sky47（A 授奖；开业/AI 云声明另证）、NASTP/Khazana（A 运营商内容：PTCL Karachi colo + Lahore NASTP Tier 3）、Multinet（A 运营商/PeeringDB fac 3447）、CubeXS（A PeeringDB fac 6728）、NOVA（A PeeringDB fac 8210）、KK/Infinity/Nexlinx/Logon/Getlinks 等（A 仅 PeeringDB）。
- IXP：PKIX（A）、PIE Karachi（A DE-CIX/PTCL 事实）、MyNet Karachi。
- 媒体：DCD、Developing Telecoms、Capacity、TeleGeography/Submarine Cable Map、APNIC、Dawn、Business Recorder、Express Tribune、ProPakistani、TechJuice（B）。
- 目录（C）：DataCenterMap、DataCenterCatalog、datacenters.com、OCOLO、Cloudscene、社媒转载。

## 已知设施/项目与证据状态

| 设施/项目 | 单位/城市 | 状态与证据 |
|---|---|---|
| PTCL Commercial Data Center-1 | Punjab/Lahore | 运营；A（Uptime Design Documents 授奖 + PTCL 服务页）；容量 U 除非 PTCL 披露 |
| PTCL Commercial Data Center-2 | Sindh/Karachi | 运营；A（Uptime 授奖 + PTCL 服务页） |
| SBP Main Data Center | Sindh/Karachi | 运营机构 DC；A（Uptime Design Documents + Constructed Facility 双奖）；细节 U |
| Board of Revenue Data Center（GoS） | Sindh/Karachi | 政府 DC；A（Uptime 授奖）；规格 U |
| Transworld KR1 / TWA DC | Sindh/Karachi | A（Uptime 授奖）；建设/启用时间 B 待运营商页确认 |
| Data Vault AI 数据中心 | Sindh/Karachi | 已启动（SIFC 声明）；A 官方声明/公司存在；GPU/太阳能/最大等 B/U |
| Quantum Global Data Center (QGDC) | Sindh/Karachi | 宣布/计划，非默认运营；A 公司/B 项目（$230m Huawei 合作） |
| Jazz Digital Park | Islamabad ICT | 运营；A（VEON/Jazz：TIA Tier-III、300+ 机架、3 MW）；非 Uptime |
| Zong CICC | Islamabad ICT | 已启用；A（公司称 Tier-III Certified Data Center）；Uptime 注册表未列 |
| Sky47 Karakoram 1 | Islamabad ICT | A（Uptime Design Documents 授奖）；开业/AI 云声明须另证；最大/Tier IV U |
| Islamabad ICT Safe City DC（NADRA） | Islamabad ICT | A（Uptime 授奖）；运营/规格需当局源 |
| NTC National Data Centre + Lahore DRC | Islamabad ICT/Punjab | 政府云/NDC/DRC；A/B（cloud.gov.pk + PID 新闻稿）；当前容量 U |
| NADRA 数据中心群 | Islamabad ICT + 未公开 DR 址 | 运营机构 DC 群；B（CGD：两 DC 相距 150 英里、第三座计划）；位置 U |
| KP Government Data Centre | Khyber Pakhtunkhwa | A（KPITB/KP 数字转型策略声明 Tier-III）；城市/规格 U |
| Balochistan Police D3C | Balochistan/Quetta | 运营机构指挥/数据中心；A（balochistanpolice.gov.pk/d3c）；非商业 colo |
| University of Turbat DC | Balochistan | 运营机构设施；B（Express Tribune） |
| Multinet Karachi | Sindh/Karachi | 运营候选；A（运营商页 + PeeringDB fac 3447）；规格 U |
| CubeXS Weatherly Karachi | Sindh/Karachi | PeeringDB 设施候选；A（PeeringDB fac 6728）；规格 U |
| NOVA / The Professional Communications | Islamabad ICT | PeeringDB 设施候选；A（fac 8210）；规格 U |
| NASTP / Khazana Cloud | Punjab/Lahore + Sindh/Karachi | A（运营商内容：Karachi PTCL colo、Lahore NASTP Tier 3）；“超大规模”标签 U |
| PKIX / PIE Karachi / MyNet | Islamabad/Lahore/Karachi | IXP 节点；A（官方/PeeringDB 事实）；非 DC 证明 |
| GB Cloud First Policy 2024 | Gilgit-Baltistan | 政策信号；A；无确认本地 DC |
| AJK IT Board | Azad Kashmir | 电子政务信号；A 实体；无 DC 确认 |

## 更新节奏

- 每月（活跃项目）：Data Vault、QGDC、Transworld KR1/TWA DC、Sky47、GO AI Hub、Khazana/NASTP、Zong/Jazz 云产品、SIFC/MoITT 云项目。
- 季度：完整官方源扫描、Uptime PK 授奖页、云区域缺席检查（AWS/Azure/GCP/OCI/Huawei）、PeeringDB PK fac/ix API、PPRA/e-PADS + 省级 PPRAs、目录候选。
- 待办（2026-08-12）：两份 explorer 初稿已完成（codex 复核）；下一步 codex terra agent 分批复核（7 单位粒度，KP/Balochistan/GB/AJK 双语负向扫描）；本 skill 作为国家层参考注入。
