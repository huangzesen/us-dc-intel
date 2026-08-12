---
name: mn-datacenter-methodology
location: scripts/expansion/world/country-skills/MN/SKILL.md
description: |
  Parent-level data-center enumeration methodology for Mongolia (MN). Mongolia has
  no single public datacenter register; enumeration builds records from four
  independent tracks: construction/land/planning permits, electricity/grid/
  renewable-energy approvals, CRC telecom licensing/standards/ISP sources, and
  operator/certification/cloud-CDN footprints, across 21 aimags plus Ulaanbaatar.
  Mongolian Cyrillic plus English search with Inner-Mongolia (China) exclusion.
  Read this before running MN exploration/audit batches. Routes to
  explorer-official.md (official/regulatory/cloud/power pipeline) and
  explorer-industry.md (industry/vendor/cloud/province patterns).
---

# MN · 蒙古数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：Mongolia has no single public datacenter register；枚举必须沿四条独立轨道建记录——(1) 建设/土地/规划许可，(2) 电力/电网/可再生能源审批，(3) CRC 电信牌照、标准、ISP/网络来源，(4) 运营商、认证与云/CDN 足迹来源。
> 多轨三角测量：官方轨道（政府门户/许可/招标）产出 A 级证据，运营商/认证/云轨道产出 A/B 级设施信号，贸易媒体与目录用于回填 B/C 线索。
> 本 skill 汇总两份探索报告（explorer-official.md / explorer-industry.md）为国家层方法论；批次执行前必读。

## 入口

| 文件 | 内容 | 说明 |
|---|---|---|
| explorer-official.md | 官方/监管/云/电力管线：CRC（`crc.gov.mn`）、建设/土地/规划许可（`mcis.gov.mn`/`mcud.gov.mn`/`ulaanbaatar.mn`/LegalInfo）、能源与环境审批（`energy.gov.mn`/`erc.gov.mn`/`tender.gov.mn`）、政府数字基础设施（`datacenter.gov.mn`）、云区域/CDN/认证/运营商、22 分区枚举策略 | A 级主干与查询模板 |
| explorer-industry.md | 行业/厂商/云/省域模式：运营商种子（NDC、Mobinet/MobiCom、Unitel、S Systems、Mogul、ICT Group、银行）、云与网络区域核验（含 Yandex/Cloudflare）、省/首府查询模式、证据标签体系 | A/B/C 全谱系与负向搜索 |

## 核心结构事实（框定每次搜索）

1. **无国家数据中心注册表**：蒙古不存在统一公开的数据中心登记；官方最佳路径不是单一注册表，而是四条独立轨道交叉：建设/土地/规划许可、电力/电网/可再生能源审批、CRC 电信牌照与标准、运营商/认证/云-CDN 足迹。
2. **地理集中**：已知设施证据集中在 **Ulaanbaatar**；次级线索在 **Darkhan-Uul / Darkhan**（Mobinet 地理冗余设施）；政策级线索在 **Tov aimag**（New Zuunmod / Hunnu City 智慧城市、可再生能源供电数据中心，Chinggis Khaan 主权财富基金）。
3. **语言（西里尔蒙古文 + 英语）**：核心词 `дата төв`（数据中心）、`өгөгдлийн төв`、`серверийн өрөө`、`зогсуур түрээс`（机架租赁）、`үүлэн үйлчилгээ`（云服务）、`хостинг`、`колокэйшн`、`барилгын зөвшөөрөл`（施工许可）、`газрын зөвшөөрөл`（土地许可）、`техникийн нөхцөл`（技术条件）、`эрчим хүч`、`дэд станц`（变电站）；俄语拼写 `дата-центр` 偶有帮助。
4. **负向控制（关键）**：Mongolia (MN) ≠ 中国内蒙古；英语搜索必须排除 `Inner Mongolia`、`Hohhot`、`Ulanqab`、`Wulanchabu` 及中文 `内蒙古`；同时排除美国 Minnesota（MN）歧义。
5. **云语义**：AWS/Azure/GCP/OCI/Yandex 官方区域页均无蒙古公有云区域（截至 2026-08-11/12 核验）；Cloudflare 2018 年官方博客宣布 Ulaanbaatar 边缘数据中心（A 级边缘存在、B 级设施推断——宿主未披露）；Akamai/Google Global Cache/Meta 等仅作互连/CDN 线索。
6. **认证**：Uptime Institute 蒙古列表（Bank of Mongolia NETC、Khan Bank Primary/Seoul/Technical Center-1、XacBank）为设施存在与认证级别 A 级证据，但不含 MW 且不等于对外 colo；CRC 2015 年国家标准 MNS 6528（`Дата төвийн цахилгаан холбооны дэд бүтэц`，基于 ANSI/TIA-942 概念）为标准语境。
7. **容量语义**：蒙古来源极少公布 IT MW；不得从 Tier II/III 或机架租赁营销推断 MW；建筑面积记 notes 而非 `capacity_mw`；电网接入/变电站/招标电力记为 notes 中的 utility capacity。
8. **陷阱**：政府文本中的 "data center" 可能是市政信息办公室或呼叫中心，需服务器/机架/电力/冷却/云/托管语境；银行设施是真实设施但不是商业 colo；"cloud" 常指本地 VPS 托管；Hunnu City 相关报道保持 `planned/announced` 直至土地/许可/电网/建设/运营商证据出现。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§3 / explorer-industry.md §1-§4）

- CRC：`site:crc.gov.mn "дата төв"`、`site:crc.gov.mn "MNS 6528" OR "Дата төвийн цахилгаан холбооны дэд бүтэц"`、`site:customer.crc.gov.mn ("интернэт" OR "харилцаа холбоо" OR "тусгай зөвшөөрөл")`。
- 许可/建设：`"дата төв" "барилгын зөвшөөрөл"`、`"дата төв" "газрын зөвшөөрөл"`、`"дата төв" "техникийн нөхцөл"`、`site:ulaanbaatar.mn "дата төв" ("захирамж" OR "барилга" OR "газар")`、`"Mongolia" "data center" "construction permit" -"Inner Mongolia"`。
- 能源/招标：`site:energy.gov.mn "дата төв" "сэргээгдэх эрчим хүч"`、`site:erc.gov.mn "дата төв"`、`site:tender.gov.mn "дата төв" ("цахилгаан" OR "сервер" OR "барилга")`、`site:shilendans.gov.mn "дата төв"`。
- 政府数字基础设施：`site:datacenter.gov.mn ("өргөтгөл" OR "шинэчлэл" OR "зогсуур")`、`"Үндэсний Дата Төв" "өргөтгөл"`、`site:tender.gov.mn "Үндэсний Дата Төв" ("сервер" OR "цахилгаан" OR "өргөтгөл")`。
- 运营商：`"Mobicom" OR "Mobinet" "дата төв"`、`"Unitel" "data center" Mongolia`、`"S Systems" "data center" Mongolia`、`"ICT Group" "Tier III" Mongolia "data centre"`、`"Khan Bank" "data center" "Ulaanbaatar"`、`"XacBank" "data center" "Ulaanbaatar"`。
- 省域模板：`"{division}" "data center" Mongolia`、`"{division_cyrillic}" "дата төв"`、`"{division_cyrillic}" "серверийн өрөө"`、`"{division_cyrillic}" "нөөц дата төв"`、`site:{official-aimag-domain} "дата төв"`、`site:tender.gov.mn "{division_cyrillic}" ("дата төв" OR "сервер")`。

## 官方/监管管线要点（详见 explorer-official.md）

- **CRC / ХХЗХ**（`crc.gov.mn`、`admin.crc.gov.mn`、e-licensing `customer.crc.gov.mn`、统计 `statistic.crc.gov.mn`）：牌照/监管/标准/统计来源；A 级证明监管存在、牌照状态与行业统计；牌照本身仅证明可运营电信/互联网服务，不证明拥有数据中心建筑。
- **建设/土地/规划许可**：Construction Law（LegalInfo 英文版）定义施工许可、电力/通信/公用事业技术条件与图纸公开要求；真实设施应寻找土地决定、技术条件、设计批准、施工许可、验收证书、公用设施连接文件；A 级为政府门户记录，B 级为规划研究/官员讲话。
- **能源/环境审批**：蒙古电网约束显著，大型项目应留下电力证据（新变电站、高压接入、直购可再生 PPA、"green data center" 语言）；Energy Ministry 2026 年关于数据中心作为能源需求/可再生供电主题的帖子为政策线索；A 级为能源牌照、并网批准、PPA/招标、环评批准。
- **MNDC（蒙古国家数据中心）**：`datacenter.gov.mn` 官方页——依 2009-06-24 政府第 183 号决议设立，位于 Ulaanbaatar Songinokhairkhan 区；服务含 web 托管、虚拟服务器、机架租赁（`Зогсуур түрээс`）、`gov.mn` 域与政府信息安全；A 级政府设施，与商业 colo 分开跟踪。
- **云/CDN 核验**：四家超大规模 + Yandex 官方页确认无蒙古公有云区域；Cloudflare Ulaanbaatar 为边缘部署（2018），宿主未披露，记录为 CDN/边缘证据而非批发设施。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **运营商种子（存在性 A / 容量视证据）**：MNDC（A，政府）、Mobinet/MobiCom（A/B，Ulaanbaatar + Darkhan 可用，Tier II/III、2N/N+1/free-cooling 声明）、Unitel（A- 服务页 `unitel.mn/business/product/13`）、S Systems/Shunkhlai（A，2022 年启动"蒙古最大数据中心"，目录 1,600 sqm 为 C）、Mogul Data Center（A-/B，`moguldc.mn`）、ICT Group JSC（B+，Haskoning 案例：2022 年 Tier III 标准新设施 + 已有两处）、Gemnet（C 待运营商页/PeeringDB）、银行（Bank of Mongolia NETC、Khan Bank 多设施、XacBank；Uptime A 级认证、私人设施非 colo）。
- **认证/标准**：Uptime Institute 蒙古国家列表（A）、TIA-942/MNS 6528 查询（`"TIA-942" "Mongolia" "data center"`、`"MNS 6528" "дата төв" "Улаанбаатар"`）。
- **贸易/本地媒体（B）**：DCD（含主权财富基金/Hunnu City 管线报道）、The Tech Capital、MONTsame、ikon.mn、news.mn、gogo.mn、Data Center Map/Datacenters.com/Baxtel/RackCorp/ColocationM（B/C）；本地媒体识别运营商、地点与事件日期时升 B。
- **目录（C）**：DataCenterMap、Datacenters.com、Baxtel、RackCorp；可浮现 S Systems、Mogul、Gemnet、Unitel、Mobinet、MNDC，须运营商/官方页或 Uptime/TIA 证据升级。

## 来源分级

- **A** = 直接官方/一手：施工许可、土地决定、验收证书、环评/能源/并网批准、CRC 牌照持有人记录、MNDC 官方页、Uptime Institute 认证、运营商官方设施页、银行/央行官方公告、云供应商官方区域页。
- **A-/B+** = 强运营商/工程证据：工程咨询案例、具名 Tier/TIA 设计声明、经审计的银行/企业报告。
- **B** = 强二手：DCD、The Tech Capital、MONTsame、ikon.mn、Data Center Map、Datacenters.com、Baxtel、RackCorp（具体且当前时）。
- **C** = 弱：泛"蒙古想要数据中心"文章、社媒帖子、无地块/开发商/电力细节的招商页、SEO colocation 页。
- **状态映射**：`planned`（官方战略/招商/智慧城市计划/MoU/基金推介，无许可无施工）、`permitted`（具名地点/开发商的土地/建设/能源/环评批准）、`construction`（奠基/EPC 中标/施工合同/可见进度）、`operational`（运营商服务页/验收/Uptime Constructed Facility 认证/政府银行启用公告/经另一来源确认的可信设施条目）、`unknown`（有强证据但无当前运行状态）。
- **容量规则**：未声明则 `capacity_mw` 留空；面积入 notes；电网接入记为 notes 中的 utility capacity；政府 IT 机房与银行 DC 除非明确提供公共托管/机架租赁，否则不按商业 colo 计数。
- **去重规则**：Mobicom Networks/Mobinet/Newcom 别名按地址与设施名解析；Unitel/Univision/MCS Group 可能是网络服务而非数据中心；银行主/备/技术中心/NETC 记录仅在 Uptime 或银行列明不同设施名/地点时分开；Cloudflare Ulaanbaatar 不单独建批发设施；排除所有中国内蒙古项目。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL 中 `country_code == "MN"` 的条目，按 division 分组（21 aimags + Ulaanbaatar）。
2. 以本 skill 运营商标记构建种子：MNDC、Uptime 蒙古列表、Mobinet/MobiCom、Unitel、S Systems、Mogul、ICT Group、Cloudflare 博客、银行官方页。
3. CRC 运营商扫描：用牌照/e-licensing/统计枚举 ISP、网络运营商、托管/域名供应商，逐一以 `дата төв`/`сервер`/`зогсуур түрээс`/`байршуулах` 下钻。
4. 建设/土地扫描：Ulaanbaatar 市/土地门户、`mcis.gov.mn`/`mcud.gov.mn` 的许可/设计批准/土地决定/验收；对 Darkhan-Uul、Tov、Orhon、Selenge 重复。
5. 能源扫描：Energy Ministry、ERC、National Dispatching Center、`tender.gov.mn`、`shilendans.gov.mn` 的供电、变电站、UPS/发电/冷却采购与可再生 DC 管线。
6. 云/CDN 确认：AWS/Azure/GCP/OCI/Yandex 官方区域页确认无区域；官方来源单独记录 CDN/边缘 POP。
7. 贸易媒体回填：DCD/The Tech Capital/MONTsame/ikon/Data Center Map 仅作发现；证据经官方/运营商/许可来源升级。
8. 分区完成度：每个 aimag 跑蒙古语 + 英语查询，`no_projects=true` 仅在对官方 aimag 站、`tender.gov.mn`、`energy.gov.mn` 及至少一条 web/新闻查询后标记；按 world schema 输出 `{country_code: "MN", country_name: "Mongolia", division, city, name, operator, status, capacity_mw, source_urls, evidence_date, evidence_grade, notes}`；**NO-DELETION**（不改写 explorer 文件，复核只增补）。

## 待办（2026-08-12 02:38Z）

- 两份探索报告已合并为国家层方法论；下一步以本 skill 为国家层参考运行 MN 探索/复核批次（22 分区）。
- 需验证：ICT Group JSC 2022 Tier III 设施当前运营状态与地点；Mogul 数据中心容量/Tier 官方文档；S Systems 1,600 sqm 规格与地址；Mobinet Darkhan 设施以官方页/CRC/许可升级；Hunnu City/New Zuunmod 是否出现土地/许可/电网/建设证据；Darkhan-Uul 之外的省域负向结果归档。
