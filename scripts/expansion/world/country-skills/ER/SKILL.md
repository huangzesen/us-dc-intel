---
name: er-datacenter-methodology
location: scripts/expansion/world/country-skills/ER/SKILL.md
description: 厄立特里亚（Eritrea）数据中心发现与审计方法论：官方/监管/云管线（EriTel 官方托管/私有云页面、Shabait 信息部、法律/公报文本、EEC 电力、AfDB、美国国务院 ICS）叠加行业/厂商发现（运营商、卫星/连接性厂商、海缆/能源/矿业媒体、目录）；以清单中的 6 个地区（Anseba、Southern Red Sea、Southern、Gash-Barka、Central、Northern Red Sea）为划分粒度，搜索时须同时使用清单名与本地名。运行 ER 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。Bilingual discovery & audit methodology for Eritrea datacenters: official/regulatory/cloud pipeline + industry/trade-press discovery, at the 6 region division granularity from the manifest (search both manifest and local names); read before running ER exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# ER · 厄立特里亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> **目的**：厄立特里亚没有公开的数据中心登记册、可检索的规划许可/电信执照/投资许可数据库——公开记录缺失是预期状态，不等于不存在州/企业机房。本方法论通过官方/监管/云管线（explorer-official.md）与行业/厂商发现（explorer-industry.md）双通道枚举，并规定诚实产量：全国预计仅 **1 条 A 级运营商/服务种子（EriTel 托管数据中心，具体站点未披露）** 加多数负向地区记录；宁可把地区标记为 `no_projects: true` 也不要用电信/电力上下文凑数。运行任何 ER 探索/审计批次前必须阅读本 skill，并按需路由到两份探索报告。

## 入口（Entry points）

| 文件 | 管线 | 内容 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | EriTel 官方页面、信息部/Shabait、法律/投资/监管（Proclamation 134/2003、142/2004、115/2001）、电力/港口/银行/大学/采购、官方设施种子表、超大规模/认证护栏、6 地区官方策略与查询模板、提取字段与置信规则 |
| explorer-industry.md | 行业/厂商发现 | 高价值行业来源表、运营商/项目扫描（EriTel、海缆改道线索、卫星/LEO、银行、矿业、UN/使馆、大学）、行业到官方验证枢轴、地区搜索手册、聚合器处理、超大规模/认证/连接性检查、最终证据规则 |

## 核心结构事实（框定每次搜索）

1. **划分模型**：清单为 **6 个地区**：**Anseba、Southern Red Sea、Southern、Gash-Barka、Central、Northern Red Sea**。行政注意：搜索须同时使用清单名与本地/通用名——Central = Maekel/Asmara；Southern = Debub/Mendefera；Northern Red Sea = Semienawi Keyih Bahri/Massawa；Southern Red Sea = Debubawi Keyih Bahri/Assab；Gash-Barka = Gash Barka/Barentu；Anseba = Keren。六行全部运行，负向搜索显式记录。
2. **唯一已核实的官方数据中心级信号**：**EriTel**（国家电信运营商，Proclamation No. 134/2003 设立）。其官方 **Private Cloud Services** 页面称 EriTel Nextcloud 托管于 EriTel 数据中心（存储/用户分级、Asmara 直连 10/5 Mbps、远程城市 2/2 Mbps、90% 可用性、最长 6 天 RTO）；官方 **Email Hosting Services** 页面称邮件本地托管于 EriTel 数据中心（Axigen、Barracuda 网关、VM 副本、每周备份、99% 可用性）。官方页面证实数据中心存在与托管服务，但**不公布设施名、地址、坐标、机架、功率、冗余等级或所在城市**；位置按最强推断记为 **Central, Asmara likely / exact site undisclosed**。
3. **关键机构**：EriTel（eritel.com.er）、Ministry of Information/Shabait（shabait.com，国家公告最佳来源）、EEC（厄立特里亚电力公司，Proclamation 142/2004；2023 年约 232 MW 装机/约 122 MW 可用、54.4% 用电普及）、EFZA（自由区，Proclamation 115/2001，Massawa/Assab 上下文）、AfDB（Desert to Power 12 MW 迷你电网：Teseney、Barentu、Kerkebet）、美国国务院 ICS、UNCTAD 投资法。数据保护：Data Protection Africa 称厄立特里亚无数据保护立法。
4. **查询语言与拼写变体**：英语为主 + 提格里尼亚语辅助（不作分级依据）；必用拼写变体：data center/centre/datacentre/datacenter；Asmara/Asmera；Massawa/Mitsiwa；Assab/Aseb；Keren/Cheren；Mendefera；Barentu；Gash-Barka/Gash Barka；Maekel/Debub/Semienawi Keyih Bahri/Debubawi Keyih Bahri；再加 colocation/hosting/server room/private cloud/email hosting/Nextcloud/gateway/earth station/VSAT/fibre/MPLS/direct connect/racks/MW/substation/free zone。
5. **容量语义**：EriTel 页面不给出 MW/机架/楼层面积；托管分级（存储/用户数）是唯一服务指标；`capacity_mw: null` 除非显式一手来源。电力（约 232 MW 装机）与自由区、矿业、银行、大学机房均为上下文，**不**升级为数据中心。
6. **无公共海缆登陆**：Submarine Networks 称厄立特里亚是唯一没有非洲海缆登陆站的沿海非洲国家，Carnegie 2025 分析重复此例外；**不要**用 Wikipedia/EASSy 片段证明 Massawa 登陆（部分搜索片段与更强来源冲突）。红海改道报道（East African Review 2024-06）仅为未来线索，无具名登陆承诺。
7. **云与认证护栏**：AWS/Azure/GCP/Oracle/Uptime Institute 官方页面均无厄立特里亚条目；EriTel 私有云是本地运营商服务而非超大规模区域；GlobalTT/VSAT/Starlink 可用性页面不构成数据中心。
8. **可靠度分级**：A = 一手/官方（EriTel 页面、Shabait、公报/法律文本如 LOC Proclamation、美国国务院 ICS、AfDB/ITU/世行官方数据、具名运营商/厂商页面）；B = 可靠行业/发展/媒体（Submarine Networks、Carnegie、DataReportal、Internet Society Pulse、ICTworks、BuddeComm、East African Review、Developing Telecoms、Connecting Africa、能源/矿业媒体）；C = 弱线索（目录、论坛、社交、个人博客、通用 VSAT 营销页、仅聚合条目、无来源 MoU、从电信/电力/自由区上下文推断设施）。
9. **不升级规则**：光纤骨干、电信交换机、ADSL 镇、MPLS 服务、自由区、电厂、矿山、大学 ICT 机房、港口系统——若无来源点名托管/数据中心/服务器机房设施，一律不计数；海缆改道兴趣 ≠ 登陆站；EriTel 私有云 ≠ 超大规模云区域。

## 常用查询模板（详见 explorer-official.md / explorer-industry.md）

```text
site:eritel.com.er "Datacenters" OR "Data Centers" OR "data center" OR "data centre"
site:eritel.com.er "Private Cloud Services" OR Nextcloud
site:eritel.com.er "Email Hosting Services" OR Axigen OR Barracuda
site:eritel.com.er "Direct Connect" "Asmara" "remote cities"
site:shabait.com "data center" OR "data centre" OR datacenter OR "datacentre"
"EriTel" "datacenters" Eritrea
"{division}" Eritrea "data center" OR "data centre" OR datacenter OR datacentre
"{town}" Eritrea "server room" OR hosting OR colocation
"{town}" Eritrea "private cloud" OR "email hosting" OR Nextcloud
"{town}" Eritrea "VSAT" OR "earth station" OR gateway OR satellite
"Eritrea" "submarine cable landing station" Massawa   # 负向核查
"Eritrea" "no submarine cable landing"
site:uptimeinstitute.com Eritrea OR EriTel   # 认证核查
site:aws.amazon.com/about-aws/global-infrastructure/regions_az Eritrea  # 云排除
"Eritrean Electric Corporation" "data center" OR server OR substation OR MW
"{town}" "ሜራጥ መስመር" OR "ሰርቨር" OR "ኣገልግሎት ኢንተርኔት"   # 提格里尼亚语辅助
```

## 官方/监管管线要点（详见 explorer-official.md）

- EriTel：关于/历史（2003-10 重组并入固话/移动/互联网，Asmara 与 Massawa 端到端光纤骨干）、互联网服务与 2021 推广城镇（Southern：Debaruwa、Adi Quala、Segenetti；Northern Red Sea：Nakfa；Central：Serjeka）、SiteConnect MPLS VPN、邮件托管、私有云；提取 A 级服务事实，交换局/网关/卫星地面站/ASN 足迹（AS30987/PeeringDB）仅作互联上下文。
- Shabait：用于佐证 EriTel 推广、电力项目、港口/自由区活动与任何未来海缆/政府云公告；具名国家公告为 A，背景文章为 B。
- 法律/投资：LOC Proclamation 134/2003（EriTel）、142/2004（EEC）、UNEP LEAP/FAOLEX 115/2001（EFZA）、state.gov 2025 ICS（可能拦截自动化抓取，改浏览器/人工访问并记录日期）、UNCTAD 投资法。法律文件只证明实体/权力存在，不证明数据中心。
- 电力/港口/银行/大学/采购：EEC 法律文本、Africa Energy Portal、AfDB、Shabait；EFZA 无公开租户名单；NBE/CBE/HCB、部委、EIT（Mai Nefhi）机房一般仅 C 级；无公开电子采购门户，ICT 招标无具名站点不算数据中心证据。
- 云/认证护栏：每次刷新重查 AWS/Azure/GCP/Oracle/Uptime 官方页。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 发现工作流：(1) 监控 EriTel 托管服务/MPLS/光纤/推广页；(2) 扫 Shabait 与官方/法律来源；(3) 扫海缆/卫星新闻找未来登陆/网关线索；(4) 测试银行、矿业、UN/使馆、大学 ICT 机房披露；(5) 运行全部 6 分区搜索并记录负向。
- 行业到官方验证枢轴：任何媒体/厂商/聚合线索先对 eritel.com.er、shabait.com、state.gov、afdb.org、peeringdb.com（AS30987）、uptimeinstitute.com 交叉验证。
- 聚合器（datacentermap.com/eritrea、Baxtel、datacenters.com、ocolo.io）预期为零或弱条目，仅作负向检查与拼写发现；聚合器条目 C 级；邻国（吉布提、苏丹、埃塞、肯尼亚、沙特、阿联酋）条目不得导入厄立特里亚。
- 生命周期措辞精确捕获：considering/planned/prospective/feasibility/coverage/available by reseller 非运营设施证据；hosted in datacenters/launched/commissioned/inaugurated/certified/signed power connection/operational 更强，但仍按来源分级。

## 维护注意（更新纪律）

- **更新节奏**：每季度重验——EriTel 邮件/私有云/企业页面、Shabait 电信/电力公告、Submarine Networks/海缆新闻、Starlink/LEO 牌照、EEC/AfDB 电力增量、EFZA 租户证据、超大规模区域页、数据保护/电信立法。
- **来源核验**：state.gov 可能拦截自动化抓取；Wikipedia/EASSy 海缆片段与 Submarine Networks/Carnegie 冲突时以更强来源为准；EriTel 官方页只支持"托管于 EriTel 数据中心"，不支持街道地址/MW/机架/Tier III/公共托管园区。
- **不删除纪律**：无法核实的旧线索保留为降级线索并注明缺失证据；每候选记录捕获 division、city/town、exact locality 或 "undisclosed"、operator/SPV 法定名、来源 URL/日期/等级、精确主张、生命周期阶段、容量字段（null 规则）、负向连接尝试。
