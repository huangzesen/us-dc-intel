---
name: pn-datacenter-methodology
location: scripts/expansion/world/country-skills/PN/SKILL.md
description: 皮特凯恩群岛数据中心发现与审计方法论（bilingual）。Pitcairn datacenter discovery & audit methodology: verified negative market — enumerate the official/regulatory/cloud pipeline (government.pn portal, Island Council Minutes, Laws of Pitcairn, UK FCDO/GOV.UK, IANA .pn delegation, official cloud-region absence checks) plus industry/trade-press discovery (Pitcairn Telecom, Starlink/satellite connectivity, subsea/IXP negatives, Pacific media, directories). Division model: single division Pitcairn. Read before running PN exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# PN · 皮特凯恩群岛数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：皮特凯恩群岛（PN，英国海外领地）是极小型、极偏远、单一定居岛市场——截至 2026-08-12 官方与行业双线结论均为 **verified negative**：未发现商业数据中心、托管/colo、云区域、AI/HPC 园区、IXP、海底光缆或登陆站。本方法论通过**官方/监管/云管线（explorer-official.md）**与**行业/厂商/媒体发现（explorer-industry.md）**双线交叉验证，以 `government.pn`/Island Council Minutes/Laws/FCDO/GOV.UK/IANA 主证，官方云区域清单为负向证据；任何正向候选必须通过 A/B 级证据、PN 内位置、设施功能、供电/连接合理性四重校验。本 skill 汇总两份最终审定的探索报告，作为 PN 探索/审计批次的入口。

## 入口

| 文件 | 管线 | 内容 |
| --- | --- | --- |
| explorer-official.md | 官方/监管/云管线 | `government.pn` 门户（人口/公告/Island Council Minutes/Laws/财务信息）、UK FCDO/GOV.UK（世界页/新闻）、Laws of Pitcairn + legislation.gov.uk（Pitcairn Constitution Order 2010）、IANA `.pn`/nic.pn、电信与 Starlink 背景、电力与物流（无机场/深水港）、官方云区域负向检查 |
| explorer-industry.md | 行业/厂商发现 | Pitcairn Telecom/本地电信、Starlink 与卫星（2022 年 Adamstown 终端）、海底光缆与网络地图（Telegeography/Submarine Networks）、云与边缘负向、目录站 false-positive 处理、太平洋媒体（RNZ/PACNEWS/SubTel Forum/DCD） |

## 核心结构事实

1. **行政区划模型**：manifest 为 `subnational_type: country`，**单一 division `Pitcairn`**；所有官方/行业枚举按全国单市场处理，可归属线索填 `division: Pitcairn`，无法定位但明确属于 PN 的线索填 `Unknown PN`；不做省/市拆分，Adamstown 线索归 `Pitcairn`。
2. **注册库现状**：无公开全国数据中心注册库；最接近普查的是 `government.pn` 门户 + Island Council Minutes + Laws + FCDO 项目文件的组合。主岛约 3.2 km × 1.6 km，人口约 50，首府 Adamstown 位于 Bounty Bay 上方——任何大型设施、土地、电信或公用事业事项都应在政府/法律/会议记录表面留下痕迹。
3. **法律与监管**：Pitcairn 法律由 Governor 制定的 ordinances、适用于 PN 的英国立法/Order in Council（含 **Pitcairn Constitution Order 2010**，legislation.gov.uk/uksi/2010/244）与普通法组成；FCDO 说明英国政府在 PN 的事务由新西兰方向远程治理，岛上有 Governor's Representative，无英国使领馆。
4. **互联与云（负向）**：**Starlink 2022-11 终端运抵 Adamstown 并运行**——连接服务，不是本地 DC；`.pn` ccTLD manager 为 Pitcairn Island Administration，技术/注册由 Nominet 相关联系人与 `nic.pn` 承接——域名注册或 DNS 服务不等于本地数据中心；**无海底光缆/登陆站**（Telegeography/Submarine Cable Map 无 PN landing point）；**无本地 IXP**；**AWS/Azure/Google Cloud/OCI 官方区域清单均无 Pitcairn**（Google Cloud 显示 43 regions/130 zones，AWS/Azure/OCI 表格不含 PN）。
5. **设施/项目种子**：无。卫星终端、VSAT、卫星电话、无线中继、政府网络设备均记 `telecom facility lead` 或 `government ICT lead`；只有公开销售 rack/colo/hosting 且有设施证据时才升级为 DC 候选。
6. **语言与词汇**：英语为主；检索词：data centre/data center/datacenter、colocation、server farm、cable landing、submarine cable、Starlink、satellite internet、IXP、carrier hotel；中文监控：皮特凯恩（数据中心/云区域/算力/托管/机房/海底光缆/卫星互联网）。
7. **可靠性分级**：A = 官方一手（UK FCDO/GOV.UK、`government.pn`、Island Council Minutes、Laws of Pitcairn、legislation.gov.uk、IANA `.pn`、AWS/Azure/GCP/OCI 官方区域清单）；B = 强二级（Pitcairn Islands Tourism、RNZ、PACNEWS、SubTel Forum、Submarine Networks、DCD、Reuters/The Guardian 等引用具名官员或官方文件的报道）；C = 弱信源（数据中心目录站、SEO 云/colo 营销页、无引用中文文章、论坛、社交媒体、BGP/监控页）；**C 级只作线索，不作计数依据**。
8. **计数与去重规则**：只有 A 级来源明确点名本地数据中心、托管设施、云区域或大型 ICT 项目，且说明功能/业主/地点时才计数（或运营商/政府官方页 + 1 个独立 A/B 级信源描述同一设施）；卫星终端、`.pn` 注册、政府电脑房、学校/电信机柜一律不计 DC；对 cloud-region、colo、AI/HPC、IXP、海底登陆的正向判断必须高于一般政府 ICT lead 标准；容量、机架数、MW、坐标不得推断，无来源填 `unknown`。

## 常用查询模板

```text
site:gov.uk Pitcairn ("data centre" OR "data center" OR datacenter OR server OR ICT OR telecom OR Starlink)
site:gov.uk Pitcairn (electricity OR power OR renewable OR solar OR generator)
site:government.pn ("data centre" OR "data center" OR datacenter OR server OR hosting OR ICT OR Starlink OR satellite)
site:government.pn (electricity OR power OR generator OR solar OR battery OR renewable)
site:government.pn ("Pitcairn Telecom" OR telecom OR telephone OR internet)
site:government.pn/laws Pitcairn (telecommunications OR electricity OR "data protection" OR privacy OR land)
site:legislation.gov.uk Pitcairn (telecommunications OR electricity OR "data protection" OR privacy)
site:iana.org/domains/root/db pn ; site:nic.pn Pitcairn
"Pitcairn" ("data centre" OR "data center" OR datacenter OR colocation OR "server farm") -tourism -cruise
"Pitcairn" ("cable landing" OR submarine OR fibre OR fiber OR IXP)
"Pitcairn" (AWS OR Azure OR "Google Cloud" OR Oracle OR OCI OR "cloud region")
"Pitcairn" (AI OR GPU OR supercomputer OR HPC OR bitcoin OR mining)
"皮特凯恩" (数据中心 OR 云 OR 算力 OR 区块链 OR 加密货币 OR 海底光缆 OR 卫星互联网)
"Pitcairn Telecom" ("data centre" OR hosting OR racks OR colocation)
"Pitcairn" Starlink (terminal OR install OR launch OR internet OR service OR coverage)
"Pitcairn" ("submarine cable" OR "landing station" OR fibre) ; "Adamstown" Pitcairn (server OR power)
site:rnz.co.nz Pitcairn (Starlink OR internet OR telecom OR power OR solar)
site:pacnews.com Pitcairn (internet OR telecom OR satellite OR power)
site:datacenterdynamics.com Pitcairn ("data center" OR "data centre" OR cloud)
"Pitcairn" (colocation OR colo OR "rack space" OR hosting OR "server farm") ; "Pitcairn" (GPU OR AI OR HPC OR mining)
"Pitcairn" ("internet exchange" OR IXP OR peering OR "carrier hotel")
```

## 官方/监管管线要点（详见 explorer-official.md）

- **`government.pn`**：PN 官方门户；人口/岛屿基础信息、公告、媒体访问审批（须先向 Mayor and Island Council 提交 request letter）、移民和政府链接。任何 DC 选址、建设、媒体/商业访问或大型基建均应从该表面可追溯。
- **Island Council Minutes / Laws / 财务信息**：Minutes 公开到 2026/2025/2024 等年份，查 `internet`/`Starlink`/`telecom`/`ICT`/`server`/`data centre`/`generator`/`solar`/`power`；Laws 查电信、电力、土地、移民、数据保护/隐私；政府电脑房或电信机柜只记 lead。
- **FCDO/GOV.UK**：`gov.uk/world/pitcairn-island` 与 `/news` 为治理和负向项目搜索入口；说明 Governor's Representative 与无使领馆事实。
- **IANA `.pn` / nic.pn**：确认 ccTLD manager，避免把注册机构、DNS、Nominet 技术联系人误判为 PN 本地 DC。
- **电力与物流**：PN 无公开电力公司表面，供电按村庄级柴油/太阳能微电网处理；无机场或深水货运港，货物依赖补给船和长艇转运——重型发电机、冷却设备、机架批量交付和备件 SLA 均不符合商业 DC 条件；任何 MW 级 IT load 声明必须有 A 级项目文件、供电方案和物流证据。
- **云区域负向**：AWS/Azure/GCP/OCI 官方区域清单逐一检查，无 PN 才可保留 cloud-region verified negative；Starlink 覆盖 ≠ 本地设施。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **Pitcairn Telecom/本地电信**：优先入口为 `government.pn` 的 telecom、notices、Island Council Minutes、Pitcairn Miscellany/旅游站文章及可访问的 Pitcairn Telecom 页面；核验当前电话/互联网服务清单、Starlink/VSAT/卫星链路状态、是否存在 hosting/server/rack/colo 产品；运营商机柜、地面站、电源柜、Starlink terminal = `telecom facility lead`。
- **Starlink 与卫星**：2022 年 Pitcairn Islands Tourism 报道引用 Deputy Governor Alasdair Hamilton，说明此前互联网慢且不稳定，Starlink 是改善连接的步骤；Kacific、O3b/SES、Inmarsat、海事卫星电话只作历史或备援背景。
- **海底光缆/IXP/云**：Telegeography/Submarine Cable Map 核验无 landing station；搜 `Pitcairn IXP`/`Adamstown IXP`/peering/AS，预期无本地 IXP；官方云区域清单是唯一可计数的 cloud-region 依据；Edge/PoP/CDN cache 必须有设施地址或官方 PoP 名称。
- **目录站处理**：Data Center Map/Cloud Infrastructure Map/SEO 目录若只有 "Pitcairn Islands quotes"、国家选择器或空白国家页，标记 `false_positive_directory`；供应商页面含 Pitcairn 多是下拉框/国家码/全球可服务列表，不是设施证据；不得由目录页自动生成设施、容量或城市。
- **诚实结论（2026-08）**：商业 colo、云区域、海底登陆、IXP/carrier hotel 均为 verified negative；旅游、补给船、科研访问设施不是 DC；任何正向候选都回到 `explorer-official.md` 做政府、法律、Island Council、供电与物流交叉验证。

## 维护注意（更新纪律）

- **更新节奏**：每季度——`government.pn` Notices 与 Island Council Minutes 关键词扫描、Starlink/卫星/电信公告；每半年——FCDO/GOV.UK Pitcairn 新闻、Laws/ordinances 更新、云区域清单复核；每年——复查全部 U/C 目录条目与云区域 verified negative；事件驱动——任何太平洋海缆新闻提到 PN、任何 AWS/Azure/GCP/OCI 区域声明为最大变化，立即复核官方区域页。
- **来源核验**：逐一点击 A 级 URL 复核；Starlink/VSAT/卫星报道仅作连接背景，不把 terminal/dish/satellite network 写成 DC；`government.pn` 媒体访问审批要求 request letter，抓取时注意访问限制。
- **不删除纪律（no-deletion）**：已核实记录不得删除；状态变化改标（lead → planned → operational）并保留原始证据链；无支撑条目降级为 U/C 保留而非移除；负向检索（无项目）须如实记录而非跳过。
