---
name: tv-datacenter-methodology
location: scripts/expansion/world/country-skills/TV/SKILL.md
description: 图瓦卢数据中心查询方法论：官方（ICT 部/TTC/TEC/Vaka 海缆）与行业（海缆媒体/目录/云厂商）双线发现，确认 Funafuti 微设施而商业 colocation 未证实。Tuvalu datacenter discovery methodology: dual official & industry lines, Funafuti micro-facilities confirmed while commercial colocation unconfirmed.
---

# TV · 图瓦卢数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：合并 explorer-official.md 与 explorer-industry.md 双线方法论，指导对图瓦卢（Tuvalu, TV）数据中心与数字基础设施证据的枚举、分级与反例排除。官方线覆盖政府/电信/电力/海缆/采购，行业线覆盖媒体/厂商/目录/云厂商负向核验。核心事实以双语标注，所有条目须按可靠性分级并保留来源状态动词。

## 入口

| 文件 | 管线 | 内容 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | 政府部委（ICT/Finance）、TTC、TEC、立法、AIFFP/World Bank/JICA、官方云区域页负向核验 |
| explorer-industry.md | 行业/厂商/媒体发现 | Submarine Networks、Pacific Island Times、目录负向检查、运营商/厂商种子、项目状态观察、云区域负向核验 |

## 核心结构事实

1. **行政区划模型**：manifest divisions（`subnational_type: town council/island council`）为 **Funafuti**、**Niutao**、**Nukufetau**、**Nukulaelae**、**Nanumea**、**Nanumaga**、**Nui**、**Vaitupu**；Niulakita 为有人岛但未单列，并入外岛负预期组，不新增 division。
2. **注册库现状**：图瓦卢是极小岛国，官方语言 Tuvaluan 与 English，一手 ICT/采购/能源材料基本用英文发布；未确认境内商业 colocation、超大规模云区域或公共 IXP。
3. **法律与监管**：TTC 由 Tuvalu Telecommunications Corporation Act 1993 建立（state-owned enterprise）；立法 PDF 与 WIPO Lex 可作核对入口；主管为 Ministry of Transport, Energy, Communication and Innovation 下属 Department of Information and Communications Technology（`ict.gov.tv`，JICA-cited，本轮访问超时，不标已验证活链）；通讯许可/监管职责仍在制度建设阶段。
4. **互联与云**：当前锚点是 **Tuvalu Vaka Cable**（连接 Funafuti 至 Google Bulikula system，AIFFP Signed and Announced，约 USD 56m/AUD 80m）；Submarine Networks 报 2024-12-12 已 landing，Pacific Island Times 报 2025-10-24 Funafuti launch；AWS/Azure/GCP/OCI 官方区域页均无 TV region（A 级负向）。
5. **设施/项目种子**：Funafuti/Fongafale/Vaiaku 集中数字基础设施——TTC 单层建筑含 server room（Vaka 临时生产环境）、在建/在途 micro data center（landing station 生产用，2025-09 在运输中）、同址 Starlink community gateway、政府/银行（National Bank of Tuvalu）/电力机房线索；资产类别须拆分记录，不合并为 commercial DC。
6. **语言与词汇**：英文为主；查询须加 ICT/DC 限定（Funafuti 为地质/珊瑚礁文献高噪声地名）；状态词：`operational`、`landed`（2024-12）、`launched`（2025-10-24）、`temporary/provisional`（2025-09 起临时接入 TTC）、`in transit/planned`（micro DC）、`not confirmed`（colo/IXP/hyperscaler region）。
7. **可靠性分级**：A=官方/一手/运营商/捐资方文件（TTC、TEC、ICT、legislation、AIFFP、World Bank、JICA、官方云区域页、PeeringDB/PCH）；B=成熟行业或区域媒体且明确点名（Submarine Networks、Pacific Island Times、RNZ Pacific、Islands Business、CommsUpdate）；C=目录/市场报告/社交帖/推广页/聚合页，只作线索；U=打不开、无法复核或只有传言。等级只覆盖来源实际支持的字段。
8. **计数与去重规则**：海缆、Starlink 网关、电信机房、银行/政府机房都不是 colocation/data center，除非来源明确说明托管/机柜/IT load/机房等级或客户服务；境外托管、云可用、国家客户支持、域名/内容分发支持不等于 TV 境内设施；`not_dc_reason` 为必填字段；目录存在不能单独建记录，目录缺失只算弱证据。

## 常用查询模板

```text
site:ict.gov.tv Tuvalu ("data center" OR "data centre" OR "micro data center" OR "landing station" OR "cloud")
site:ict.gov.tv Tuvalu ("National ICT Policy" OR "Broadband Plan" OR "Digital Government Plan" OR "NETP")
site:finance.gov.tv Tuvalu ("tender" OR "procurement" OR "ICT" OR "telecommunications" OR "server" OR "cloud")
site:tuvalutelecom.tv ("data center" OR "data centre" OR "server room" OR "landing station" OR "Vaka" OR "Starlink")
site:tectuvalu.tv ("data center" OR "ICT" OR "BESS" OR "generator" OR "Funafuti")
"Tuvalu Vaka Cable" ("landing station" OR "Funafuti" OR "production environment" OR "ready for service" OR "launched")
"Tuvalu" ("micro data center" OR "micro data centre" OR "containerized data center" OR "government cloud")
"Tuvalu" ("internet exchange" OR IXP OR PeeringDB OR PCH)
site:submarinenetworks.com Tuvalu OR "Vaka Cable" OR "Bulikula" OR "Funafuti"
site:pacificislandtimes.com Tuvalu ("submarine cable" OR "Vaka" OR "internet" OR "Funafuti")
site:commsupdate.com Tuvalu ("4G" OR "broadband" OR "submarine cable" OR "TTC")
"Tuvalu" ("data center" OR "data centre" OR datacenter OR colocation OR "server room")
"Tuvalu Vaka Cable" ("ready for service" OR "RFS" OR "launched" OR "landing station")
"TTC" "Funafuti" ("server room" OR "micro data center" OR "Starlink gateway" OR "landing station")
"Tuvalu" ("Google" OR "Akamai") ("cache" OR "caching server" OR "edge")
"Funafuti" OR "Fongafale" OR "Vaiaku" ("data center" OR "data centre" OR "micro data center" OR "server room" OR "landing station")
"TTC" OR "Tuvalu Telecom" ("Funafuti" OR "Vaiaku") ("server room" OR "core network" OR "Vaka" OR "Starlink gateway")
"Vaitupu" OR "Asau" Tuvalu ("4G" OR "Starlink" OR "server" OR "ICT" OR "telecom" OR "solar")
"Niutao" Tuvalu ("4G" OR "Starlink" OR "server" OR "ICT" OR "telecom" OR "solar")
"Nanumea" OR "Haumaefa" Tuvalu ("4G" OR "Starlink" OR "server" OR "ICT" OR "telecom" OR "solar")
"Nukulaelae" OR "Nukufetau" OR "Nui" OR "Fenua Tapu" OR "Nanumaga" OR "Nanumanga" Tuvalu ("Starlink" OR "WiFi" OR "server" OR "ICT" OR "solar")
"AWS" OR "Amazon Web Services" "Tuvalu" ("region" OR "availability zone" OR "local zone")
"Microsoft Azure" "Tuvalu" ("region" OR "data center")
"Google Cloud" "Tuvalu" ("region" OR "data center")
"Oracle Cloud" "Tuvalu" ("region" OR "data center")
"Tuvalu" ("sovereign cloud" OR "data residency" OR "government cloud")
"SubCom" "Tuvalu Vaka Cable"
"Google" "Tuvalu Vaka Cable" OR "Bulikula" "Tuvalu"
"Starlink" "Tuvalu" ("community gateway" OR "ground station" OR "Funafuti" OR "outer islands")
"National Bank of Tuvalu" ("MTUPE" OR "Mastercard" OR "VISA" OR "server")
"Akamai" OR "Google" "Tuvalu" ("cache" OR "caching")
"Tuvalu Vaka Cable" ("launched" OR "ready for service" OR "RFS" OR "commercial service" OR "commissioned")
"Vaka Cable" Tuvalu ("landing station" OR "cable landing station" OR "CLS" OR "SLTE")
"TTC" "micro data center" Tuvalu
"Tuvalu" "caching server" ("Google" OR "Akamai" OR "content provider")
"Tuvalu" internet ("outage" OR "fault" OR "restored") ("Vaka" OR "cable" OR "Starlink")
```

## 官方/监管管线要点（详见 explorer-official.md）

- 官方来源清单：ICT Department/MTECI（JICA-cited，访问超时，A for JICA facts / U until URL opens）、Finance `finance.gov.tv`（A）、TTC `tuvalutelecom.tv/about-us`（A）、立法 PDF + WIPO Lex（A）、TEC `tectuvalu.tv`（A）、JICA survey 报告（A）、AIFFP Vaka 页（A）、World Bank P159395 PAD（历史背景，旧 RFS 假设不可作当前状态）、官方云区域页（A 负向）。
- 采购字段必留：`notice_url`、`procuring_entity`、`project_id`、`contract/reference_number`、`status_verb`、`status_date`、`delivery_site`、`asset_class`、`evidence_grade_by_field`。
- 最低阳性证据：commercial colocation（未确认）；government DC / sovereign micro DC（JICA 仅支持 TTC adjacent micro DC 为 in transit/planned，2025-09）；cable landing station（Vaka/Funafuti 为强互联证据，非 DC）；telco/server room（TTC/JICA 点名）；satellite gateway（JICA/TTC 点名）；energy support（只作 power caveat）。
- `gov.tv` apex 本轮 DNS 解析失败，用子域发现与缓存页；Facebook 贴文除非账号身份已验证且同事实在 A 级材料中出现，否则保持 B/C。
- 电力：Funafuti 为 diesel base load + grid-tied solar PV + 规划 500 kW solar 与 containerized BESS；Nui/Nukufetau/Nukulaelae 有 solar 增量项目；MW 级 DC 基本负预期。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 行业框架：图瓦卢是微型、几乎零商业数据中心市场；重点是避免把 Vaka 海缆、TTC server room、Starlink gateway、外岛 backhaul、Digital Nation 误记为商业 DC。
- 高信号来源：Submarine Networks（B）、Pacific Island Times（B）、AIFFP（A）、JICA survey（A）、TTC（A）、TEC（A）、CommsUpdate/TeleGeography（B）、RNZ Pacific/Islands Business/ABC Pacific（B/C）、DataCenterMap（C，本轮 429）、Baxtel（C，本轮 404 跳转）、Cloudscene（C）、PeeringDB/PCH（A for listed facts）。
- 运营商/厂商种子：TTC（唯一国家电信运营商，A）、SubCom（Vaka 供应商，非 DC 运营商）、Google/Bulikula（电缆生态，无 TV 云区域）、Starlink（Funafuti gateway + 外岛 backhaul，卫星接入非 DC）、Kacific（B/C 待验证）、TEC（power-background）、National Bank of Tuvalu（银行 IT/server-room 线索）、IIJ（JICA 报告其曾就政府 micro DC 接洽，vendor/proposal 历史）、Google/Akamai caching（TTC 谈判中，watchlist，装设后记 `cache-node`）。
- 输出规则：`source_status_verb` 必填（landed/launched/in operation/provisional/in transit/planned/negotiating/not confirmed）；`division` 只能取 manifest 之一，Niulakita 留在 notes；`grade_by_field` 可能来源 A 而 DC 解释 C/U；`not_dc_reason` 对 cable/satellite/cache/telecom access/power/Digital Nation 必填。
- 云厂商检查：仅用官方区域页做负向核验；SaaS 可用、客户国家支持、partner/reseller 覆盖、edge cache 谈判、境外托管都不算 TV 设施。

## 维护注意（更新纪律）

- 每月：TTC/Vaka 新闻、ICT Department 政策与招标、Finance 采购、AIFFP/World Bank/JICA 更新。
- 每季：Submarine Networks、CommsUpdate、DCD、RNZ Pacific、Islands Business、Pacific Island Times、PeeringDB、PCH、DataCenterMap、Cloudscene、Baxtel、官方云区域页。
- 事件驱动：Vaka RFS/CLS/commissioning 通知、micro DC 到货或验收、Starlink 许可变更、Google/Akamai cache 装设、影响 TTC/landing station 的停电、政府云/数据中心招标；任何 `commissioned`/`RFS`/`ready for service`/`awarded`/`installed`/`accepted` 字样都触发重新分级。
