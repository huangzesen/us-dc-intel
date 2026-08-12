---
name: cc-datacenter-methodology
location: scripts/expansion/world/country-skills/CC/SKILL.md
description: 科科斯（基林）群岛数据中心发现与审计方法论（bilingual）。Cocos (Keeling) Islands datacenter discovery & audit methodology: enumerate the official/regulatory/cloud pipeline (Australian Department of Infrastructure IOT, Shire of Cocos (Keeling) Islands, ABS, nbn Sky Muster, Telstra, ACMA, AusTender, ARENA, official cloud-region absence checks) plus industry/trade-press discovery (SUBCO OAC cable, Oman Observer/iTnews/DCD/SubTel, IOTT/MultiWave/local ISPs, directories). Division model: country with 1 division (Cocos (Keeling) Islands); sub-locations West/Home/Direction Island + Unknown CC. Read before running CC exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# CC · 科科斯（基林）群岛数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：科科斯（基林）群岛（CC）为澳大利亚海外领地，人口约 593（ABS 2021），孤岛小型电力系统；截至 2026-08-12，公开官方来源未发现可验证的商业托管、云区域、超大规模、AI/HPC 或 carrier hotel 市场。**关键修正**：CC 并非无海缆领地——**Oman Australia Cable (OAC) 已投入服务**，行业及运营商来源确认其登陆点包括 **West Island, Cocos (Keeling) Islands**；这应记录为电信基础设施/cable landing station lead，不应自动计为商业数据中心。本方法论通过**官方/监管/云管线（explorer-official.md）**与**行业/媒体/厂商发现（explorer-industry.md）**双轨三角验证，以官方/运营商一手证据定稿；本 skill 汇总两份最终审定报告，作为 CC 探索/审计批次的入口。

## 入口

| 文件 | 管线 | 内容 |
| --- | --- | --- |
| explorer-official.md | 官方/监管/云管线 | Infrastructure IOT 门户与治理页、Shire of Cocos (shire.cc)、ABS QuickStats、DFAT、nbn Sky Muster（官方确认 CC 接入）、Telstra/ACMA（运营商/许可）、SUBCO OAC 官方、AusTender（电力/采购记录）、ARENA、四大云区域缺失检查 |
| explorer-industry.md | 行业/媒体/厂商发现 | 海缆（SUBCO、Oman Observer、DCD/Reuters/iTnews/SubTel、Submarine Cable Map）、卫星/移动/本地 ISP（nbn、Telstra、IOTT、MultiWave、Cocos Communications and IT）、电力与市政（AusTender、CER、Home Island 电站）、目录（DCD、DataCenterMap、CloudInfrastructureMap、Corning/IRM/Equinix 全球页）、中文传阅监控 |

## 核心结构事实

1. **行政区划模型**：manifest 为 **country**，恰好 **1 个 division：`Cocos (Keeling) Islands`**；细化地点只作证据落位：**West Island**（首府、机场、政府集中区、OAC 登陆点——高优先）、**Home Island**（社区、Shire seat/服务、电力站历史线索——中）、**Direction Island**（历史电报站误报防护——低）、**Unknown CC**（来源确认存在设施但不给具体岛屿时使用，不强行落到 West/Home）。
2. **注册库现状**：无公开全国数据中心注册库；商用 DC 判断（2026-08-12）= verified negative；nbn 官方确认 Sky Muster 卫星接入（证明接入服务，不证明本地 DC）；OAC 为国际海缆登陆线索；Telstra/IOTT 相关线索须用官方覆盖、ACMA、AusTender 或运营商页面交叉验证。
3. **法律与监管**：澳大利亚政府负责 Christmas Island 与 Cocos (Keeling) Islands 两个 Indian Ocean Territories（Infrastructure 部页面确认，经部门、WA 服务安排或合同交付州级服务）；电信监管经 ACMA（频谱/广播/无线许可、carrier 记录）；采购经 AusTender（tenders.gov.au）与 Shire tender/EOI 页。
4. **互联与云（负向+例外）**：**OAC**（SUBCO）已 ready for service，登陆点含 Perth、West Island (CC)、Muscat——B+ 佐证（SUBCO 官方项目源 + Oman Observer RFS 报道），记 `cable landing station` lead 非商用 DC；nbn Sky Muster 用户侧碟形天线/modem 与澳大利亚本土 ground station 不算 CC 设施；官方 AWS/Azure/GCP/OCI 清单无 CC region（国家下拉框出现 "Cocos (Keeling) Islands" ≠ cloud region）；Google Australia Connect/Bosun/Dhivaru 指向 Christmas Island/Mandurah/Maldives 等，不得外推到 CC。
5. **电力基线**：Home Island 有小规模柴油/风电历史项目（四个 320 kW 柴油发电机 + 80 kW 风电，worldofrenewables B 级）；AusTender 存在 CC 电力发电、配电、电缆、控制系统和燃油采购记录（如 `CKI HV 10032223`、`Generator Control System`、`Diesel fuel for power generation`、`Power Infrastructure Structural Inspections`）；**任何 MW 级数据中心主张必须匹配联邦采购、电力接入和建设批准证据**。
6. **语言与词汇**：英文为主；中文传阅监控词：科科斯（基林）群岛/科科斯群岛/科科斯 + 数据中心/云区域/海缆/算力/服务器/托管/电力；设施词：cable landing station、satellite access service/ground station、telecom exchange、government server room、colocation、cloud region、AI/HPC、power station。
7. **可靠性分级**：A = 官方/一手/运营商（Infrastructure IOT、Shire、ABS、DFAT、nbn、Telstra 官方页、ACMA、AusTender、ARENA、官方云区域清单、运营商正式新闻稿如 SUBCO）；B = 强二手（ABC News、Reuters、Oman Observer、iTnews、DCD、SubTel Forum、Capacity Media、TeleGeography/Submarine Cable Map、APH/ANAO 文件；若直接引用一手文件或运营商声明可作 A 级结论佐证，单独使用时仍为 B）；C = 弱/聚合（数据中心目录、SEO 市场报告、供应商国家下拉页、社交媒体、无引用中英文文章、BGP/故障监控页）——只能生成线索，不能计数。
8. **计数与去重规则**：只有命名设施/项目且功能明确（cable landing station、satellite ground station、telecom exchange、government server room、colocation、cloud region、AI/HPC）时才计候选，否则记录 verified-negative；OAC landing 可计 telecom facility lead，机场普通通信机房不计 DC；电力站不计 DC；政府/Shire server room 被采购/审计/资产计划/官方公告命名才计 lead（非商业设施）；普通 IT 服务或电力工程不计为数据中心；普通机场/学校/诊所/酒店/Shire 办公室 IT 设备不计设施；最低计数标准：一个 A 级设施/项目来源，或运营商官方来源 + 一个独立 A/B 级佐证；细化地点必须有来源明确命名、地址、坐标或可复核的地理编码过程。

## 常用查询模板

```text
# 官方/治理
site:infrastructure.gov.au ("Cocos (Keeling) Islands" OR "Indian Ocean Territories") (ICT OR digital OR connectivity OR "data centre" OR "data center" OR server OR cloud OR cybersecurity)
site:infrastructure.gov.au "Cocos (Keeling) Islands" ("cable landing" OR submarine OR OAC OR "Oman Australia Cable" OR satellite OR power)
site:shire.cc ("Cocos" OR "Keeling") (tender OR EOI OR ICT OR server OR power OR procurement OR "data centre" OR "data center")
site:dfat.gov.au "Cocos (Keeling) Islands" (governance OR connectivity OR digital OR cable)
# 电信
site:nbnco.com.au (Cocos OR "Cocos (Keeling) Islands" OR "Indian Ocean Territories") ("Sky Muster" OR satellite OR gateway OR "ground station" OR PoP)
site:telstra.com.au (Cocos OR "Keeling" OR "Indian Ocean Territories") (mobile OR coverage OR satellite OR exchange OR "data centre" OR "data center")
site:acma.gov.au (Cocos OR "Keeling") (carrier OR licence OR radiocommunications OR satellite OR spectrum)
site:sub.co ("Cocos" OR "West Island" OR "Oman Australia Cable" OR OAC)
"Oman Australia Cable" "West Island" "Cocos (Keeling) Islands" ; "Cocos (Keeling) Islands" "cable landing station"
"Indian Ocean Territories Telecom" OR IOTT (Cocos OR "Cocos 4G" OR "Sky Muster" OR nbn OR hosting OR colocation)
# 电力与采购
site:tenders.gov.au ("Cocos (Keeling) Islands" OR "Cocos/Keeling" OR "Indian Ocean Territories") (ICT OR server OR "data centre" OR power OR generator OR electricity OR "control system" OR fibre OR cable)
site:arena.gov.au (Cocos OR "Cocos (Keeling) Islands") (solar OR battery OR renewable OR microgrid OR storage)
"Cocos (Keeling) Islands" "power station" (diesel OR MW OR generator OR "Home Island") ; "Cocos Keeling Islands - Home Island Generation"
# 云/托管/AI 负面检查
"Cocos (Keeling) Islands" ("cloud region" OR "edge location" OR AWS OR Azure OR "Google Cloud" OR Oracle OR OCI)
"Cocos (Keeling) Islands" ("data centre" OR "data center" OR datacenter OR colocation OR "rack space" OR "carrier hotel") -tourism -diving
"Cocos (Keeling) Islands" (AI OR GPU OR supercomputer OR "high performance computing") (facility OR investment OR campus)
# 行业媒体
site:abc.net.au "Cocos (Keeling) Islands" (cable OR satellite OR internet OR Telstra OR nbn OR digital OR "data centre")
site:reuters.com ("Cocos" OR "Oman Australia Cable" OR "Indian Ocean Territories")
site:itnews.com.au ("Oman Australia Cable" OR "Cocos") ; site:capacitymedia.com ("Cocos" OR "OAC")
site:datacenterdynamics.com ("Cocos" OR "Keeling" OR "Indian Ocean Territories")
# 目录（C，仅发现）
site:datacentermap.com (Cocos OR Keeling) ; site:cloudinfrastructuremap.com (Cocos OR Keeling)
# 中文传阅监控
("科科斯（基林）群岛" OR "科科斯群岛" OR "科科斯") ("数据中心" OR "云区域" OR "海缆" OR "算力" OR "服务器" OR "托管" OR "电力")
```

## 官方/监管管线要点（详见 explorer-official.md）

- **Infrastructure IOT 门户**：确认澳政府对两领地负责及服务交付方式；治理页查治理结构、法律适用、Administrator/地方政府线索。
- **Shire of Cocos (shire.cc)**：官网有效，菜单含 Tender、Council documents、Major Projects、Home Island/West Island 联系页。
- **ABS 2021 QuickStats**：人口/住户/小市场规模基线（约 593）。
- **nbn/Telstra/ACMA**：nbn 官方列出 CC 可经 Sky Muster 获 nbn-powered plans（接入服务非设施）；nbn 卫星地面设备新闻确认体系由澳大利亚境内多个 ground station 支撑（用户侧碟形天线不算设施）；Telstra satellite-to-mobile FAQ 明确不覆盖澳大利亚领地岛屿（该 LEO 手机短信产品不适用，不等同于 Telstra 无任何 CC 业务）；ACMA 查 Register of Radiocommunications Licences。
- **SUBCO/OAC**：官方项目新闻有效但主要确认 Perth landfall 与项目背景；需配合 OAC ready-for-service 来源（Oman Observer 引用 SUBCO：landing points 含 Perth、West Island CC、Muscat）确认 West Island landing——B+ 处理，支撑 cable landing station lead。
- **电力与采购**：AusTender 可检索到 CC 电力相关记录（电缆安装、发电机控制系统、发电柴油、电力基础设施结构检查）；Home Island 电站/风电为 B 级历史容量源（四个 320 kW 柴油 + 80 kW 风电）；CER 生成设施数据可查 `Cocos Keeling Islands - Home Island Generation`。
- **云区域负面**：仅用官方清单确认 "无本地云区域"；国家下拉框出现 ≠ cloud region。
- 首轮工作流：治理/规模基线（Infrastructure/Shire/ABS）→ 连接（nbn/Telstra/ACMA/SUBCO，OAC West Island 单独记 telecom lead）→ AusTender 采购扫描（Cocos/Cocos/Keeling/IOT/OAC/Generator Control System/ICT/server/data centre）→ 电力容量过滤（Home Island/CER/AusTender）→ 官方云区域清单（记 CC cloud-region negative）→ West/Home/Direction 细化扫描（无来源用 Unknown CC）→ 每条候选保留 URL、notice ID、来源等级、摘录日期和「不计数原因」。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 海缆：SUBCO（A）、Oman Observer（B+，引用 SUBCO 确认 OAC live/RFS 与 West Island landing）、DCD/Reuters/iTnews/SubTel Forum/Submarine Networks（B，用于 OAC、Diego Garcia spur、Salalah spur 与未来印度洋路由变化）、Submarine Cable Map（C）。
- 卫星/移动/本地 ISP：nbn Sky Muster（A，服务可用性非设施定位）、nbn ground equipment（A，架构/地面站背景）、Telstra（A，直接声明；查覆盖/USO/移动/卫星-to-移动限制/企业公告）、IOTT（B/C 商业目录线索，除非有 IOTT 自有页面或政府/ACMA/AusTender 证据）、MultiWave（B/C，nbn Sky Muster 转售线索，非设施证据）、Cocos Communications and IT（用 ABN Lookup/AusTender/Shire 文档验证，社交页仅 C）。
- 电力/市政：AusTender（A）、Home Island 电站/风电（B，容量 sanity check）、CER（A/B，发电机名称与年发电量）。
- 目录：DCD（B 真实文章，本轮未发现 CC 商用 DC）、DataCenterMap/CloudInfrastructureMap/DataCenters.com/Corning/Iron Mountain/Equinix 全球页（C，除非命名 CC 地址+运营商+设施并有佐证；国家选择器命中为假阳性）。
- 升级矩阵：OAC/CLS（高优先，明确命名 West Island/CC landing station+operator+status 时计 telecom lead 非 commercial DC）；nbn Sky Muster（高，仅当 nbn/ACMA 命名本地 PoP/gateway/shelter/exchange 时计设施候选）；Telstra/IOTT（高，命名本地交换/hub/shelter/backhaul 设施或 hosting 产品时计）；政府/Shire server room（中，采购或审计命名才计 lead）；本地 ISP/reseller hosting（中，明确提供 CC 本地 rack/hosting/colocation 且地址/设施证据）；商用 colocation/cloud/AI-HPC（低，需一手运营商或官方区域/设施公告，目录站永不单独计数）；电力设施（过滤用，不计 DC）。
- 诚实结论（2026-08）：商业 colocation 无；云区域无；OAC/CLS West Island 为电信设施线索；Google Christmas Island hubs 不外推；卫星服务为连接上下文；电力项目为容量过滤；Direction Island 历史电报站不计现代设施；SEO/目录伪影默认 C。

## 维护注意（更新纪律）

- **更新节奏**：每季度——OAC/SUBCO 状态与任何 colocation/caching/hosting 产品、nbn/Telstra/IOTT 服务与设施命名、AusTender/ACMA 扫描（telecom/ICT/generator/fibre/cable landing/server/data centre，记录 notice ID）、官方云区域清单复检、DCD/DataCenterMap/CloudInfrastructureMap/中文搜索；事件驱动——任何 CC 云区域/colo/AI-HPC 公告为最大变化信号，立即核对一手运营商或官方区域/设施公告。
- **来源核验**：逐一点击 A 级 URL；OAC 以 SUBCO 官方 + RFS 佐证为准；Google 海缆项目（Bosun/Dhivaru/Australia Connect）须明确命名 Cocos (Keeling) Islands 才涉 CC；运营商服务（IOTT/MultiWave/Sky Muster）与设施证据分开记录。
- **不删除纪律（no-deletion）**：已核实记录不得删除；状态变化改标（planned → under construction → ready-for-service → operational）并保留原始证据链；无支撑条目降级为 C 保留而非移除；负向检索（verified-negative）须如实记录而非跳过。
