---
name: sz-datacenter-methodology
location: scripts/expansion/world/country-skills/SZ/SKILL.md
description: 埃斯瓦蒂尼数据中心查询方法论（Eswatini datacenter discovery & audit methodology）——双线来源（官方/监管/云管线 + 行业/厂商/媒体发现）与 region 四区模型下的设施枚举规则。
---

# SZ · 埃斯瓦蒂尼数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：发现并核实埃斯瓦蒂尼（Eswatini, SZ；旧名 Swaziland，2018-04-19 更名）的数据中心、托管/共置设施与灾备中心。双线方法论：`explorer-official.md`（官方/监管/云管线）与 `explorer-industry.md`（行业/媒体/厂商），均为 codex 审核定稿。划分模型（per manifest）：**region** — 4 个一级划分：**Hhohho、Lubombo、Manzini、Shiselweni**。记录和负检索必须覆盖四个 region；不得把自然地理带（Highveld/Lowveld/Lubombo plateau）误作 manifest 行政层级。评审日期：2026-08-12。

## 入口

| 入口 | 管线 | 内容 |
|---|---|---|
| `explorer-official.md` | 官方/监管/云管线 | 可靠性分级与升级规则、已核实事实边界（RSTP National Data Centre/MTN co-location/政府 e-Gov DR 中心/SISPA/超大规模云负向）、官方源与已验证 URL、官方查询模板（含旧名回溯）、设施种子清单、分区官方覆盖策略、记录/去重/容量规则 |
| `explorer-industry.md` | 行业/厂商/媒体发现 | 行业分级、已验证行业/运营商信号、语言与命名矩阵（新旧国名/地名/机构/技术词）、行业与媒体名单、运营商与开发商扫描、可用查询模板、枚举矩阵、分区行业检索指南、负检索协议、去重与容量规则 |

## 核心结构事实

1. **行政区划模型**：region，4 个一级划分：Hhohho（Mbabane, Lobamba, Ezulwini, Pigg's Peak, Bulembu）、Lubombo（Siteki, Big Bend, Simunye, Mhlume, Lavumisa）、Manzini（Manzini, Matsapha, Phocweni, Malkerns, Kwaluseni）、Shiselweni（Nhlangano, Hluti, Mahamba, Hlatikulu）。不能因总部在 Mbabane 就把未定位 data centre 放入 Hhohho。
2. **注册库现状**：埃斯瓦蒂尼**没有公开、集中、可下载的国家级数据中心登记册**。官方枚举先使用一手来源确认设施存在、地点和运营者，再用监管、采购、电力、环境、土地和互联材料补强。只出现「ICT room / server room / connectivity / cloud services」但没有公开托管、共置或数据中心设施描述的条目，保留为线索，不进入已确认设施表。
3. **法律与监管**：ESCCOM（通讯监管，旧 SCC）牌照与咨询、ESPPRA（采购，旧 SPPRA）原始采购记录、EEA（环境，旧 SEA）环境评估记录、EEC/ESERA（电力/能源监管，旧 SEB/SERA/ERA）电力记录、EIPA（投资，旧 SIPA/SIDC）/RSTP/市政土地或园区记录。旧名回溯必须并行跑：Swaziland、SCC/ESCCOM、SEB/EEC、SERA/ESERA、SPPRA/ESPPRA、SIPA/EIPA、SPTC/EPTC、MTN Swaziland/MTN eSwatini。
4. **互联与云**：SISPA / Swaziland Peering Point（NSRC/PeeringDB/Af-IX 生态资料，country SZ，peer 数量很小）是 IXP/peering 线索，不可单列为数据中心，只在托管场地被查明后作为设施互联证据。超大规模公有云区域为 A 级负向：AWS/Azure/Google Cloud/Oracle OCI 官方区域列表无 Eswatini 区域；最近已核实区域在南非（AWS South Africa/Cape Town、Azure South Africa North/West、Google Cloud Johannesburg `africa-south1`、OCI South Africa Central/Johannesburg）。云边缘、CDN、合作伙伴或 Outposts/Local Zones 线索不得记作 SZ hyperscale region。
5. **设施/项目种子**：**RSTP National Data Centre / Royal Science and Technology Park National Data Centre**（Manzini region / Matsapha / Phocweni Site，A——RSTP 官网点名 National Data Centre 并描述 remote hands、colocation、web hosting、secure repositories、national payment gateway；contact 页把 Phocweni Site 标为 IT Park，地址 Royal Science & Technology Park, F8PP+RF4, Matsapha）；**MTN eSwatini Co-Location Hosting Services**（A 服务存在/地点待补强——官方页称是 data centre，提供空间、冷却、电力、物理安全和带宽；未定位前记录为「operator data centre service, location undisclosed」，不默认 Mbabane）；**Government e-Government / Disaster Recovery Centre**（A 项目线索，不等同已运营商业设施——gov.sz 2015-2019 e-Government Operational Framework 含「Disaster Recovery data Centre established」和采购/选址动作；需核对后续建设、投产和地点，优先与 RSTP Phocweni National Data Centre 去重）；**SISPA / Swaziland Peering Point**（B，互联线索）；**EPTC / Eswatini Telecom / Eswatini Mobile**（C/B 线索，官网可达确认 EPTC 为通讯企业，但本轮未找到官方数据中心/共置设施页）；**金融机构灾备机房**（B/C，只记录公开点名的灾备中心，普通 server room 不计）；**Hyperscale cloud region**（A 负向）。
6. **语言与词汇**：英语为主。国名变体：Eswatini; eSwatini; Swaziland; Kingdom of Eswatini/eSwatini/Swaziland; umbuso weSwatini。地名变体：Mbabane/eMbabane、Manzini/eManzini、Siteki/eSiteki 等。机构变体：RSTP / Royal Science and Technology Park、National Data Centre、MICT、ESCCOM/SCC、EEC/SEB、ESERA/SERA/ERA、EEA/SEA、EIPA/SIPA/SIDC、ESPPRA/SPPRA、MTN eSwatini/Eswatini/Swaziland、EPTC/SPTC/Swazi.net。技术词：data centre; data center; datacentre; colocation; co-location; hosting; remote hands; disaster recovery; business continuity; server room; cloud; Tier III; Uptime Institute; UPS; generator; MW; MVA; kVA。
7. **可靠性分级**：A=官方/一手来源直接点名设施、场地或服务（运营商/设施方官网、gov.sz/MICT/RSTP 页面或 PDF、ESCCOM 牌照和公开咨询、ESPPRA 原始采购记录、EEA 环境评估记录、EEC/ESERA 电力记录、EIPA/RSTP/市政土地或园区记录、AWS/Azure/GCP/OCI 官方区域页的负面结论）；B=强二级来源（Times of Eswatini、Eswatini Observer、主流区域 ICT 媒体（DCD、Connecting Africa、ITWeb Africa、Capacity Media、TechAfrica News）、Af-IX/NSRC/PeeringDB、供应商案例、采购聚合站复制的官方招标原文）；C=弱线索（数据中心目录、市场报告摘要、社交媒体、无出处 MoU 转载、泛泛云/托管营销）。升级规则：设施存在可由运营商/设施方官网升为 A；具体 region/城镇/地址只有在同一官方体系或可靠地理证据能定位时才可升为 A；媒体和目录不能单独把设施升为 A；IXP 是互联生态证据，不等于独立数据中心。
8. **计数与去重规则**：Swaziland/Eswatini 新旧国名指同一国家；SCC/ESCCOM、SEB/EEC、SERA/ESERA、SPPRA/ESPPRA、SIPA/EIPA、SPTC/EPTC、MTN Swaziland/MTN eSwatini 按法律实体和地址去重。RSTP、MICT/e-Government、National Contact Centre、National Data Centre 可能在同一个 Phocweni IT Park 生态内重叠；不能把同一楼宇/园区重复记为多座设施。每条设施记录至少包含：operator/legal entity、facility name、region、town/site、address or geocode if public、source URL、source grade、operational status、services、capacity if stated、power/cooling evidence、confidence notes、unresolved checks。容量保守记录：不把 kVA/MVA 自动换算为 MW；发电容量、园区电力、太阳能项目容量不等于 IT load；「Tier III」只在 Uptime Institute 或运营方材料明确说明认证/设计状态时记录原文（区分 certified/designed/marketed）。负向记录必须说明日期、查询语句、覆盖的 source classes；没有命中不等于不存在，尤其是未公开政府/电信灾备设施。

## 常用查询模板

```text
site:esccom.org.sz ("data centre" OR "data center" OR datacentre OR colocation)
site:gov.sz ("data centre" OR "data center" OR "Disaster Recovery Centre" OR "National Data Centre")
site:gov.sz ("e-Government" OR "eGovernment" OR MICT) ("data centre" OR "cloud" OR "business continuity")
site:rstp.org.sz ("National Data Centre" OR "data center" OR colocation OR "remote hands" OR hosting)
site:mtn.co.sz ("co-location" OR colocation OR "data centre" OR "data center" OR hosting)
site:esppra.co.sz ("data centre" OR "data center" OR "server room" OR UPS OR "ICT equipment")
site:eec.co.sz ("data centre" OR "data center" OR "large power" OR substation OR "Matsapha")
site:esera.org.sz ("generation licence" OR "electricity licence" OR IPP OR "backup power")
site:eea.org.sz ("environmental assessment" OR EIA OR "environmental impact") ("data centre" OR generator OR substation)
site:investeswatini.org.sz ("data centre" OR "data center" OR "National Data Centre" OR Matsapha OR Phocweni)
site:centralbank.org.sz ("data centre" OR "data center" OR "disaster recovery" OR "business continuity")
"Royal Science and Technology Park" "National Data Centre"
"RSTP" "National Data Centre" Matsapha OR Phocweni
"MTN eSwatini" "co-location" "data centre"
"Swaziland Peering Point" OR SISPA
"Eswatini" "Internet Exchange" OR IXP
"Angelique International" Eswatini "data center" OR "data centre"
"EPTC" OR "SPTC" "data centre" OR "data center" OR colocation OR hosting
"Swazi.net" hosting "data centre" OR "server"
"Matsapha" "data centre" OR "data center" OR colocation OR hosting
site:times.co.sz ("data centre" OR "data center" OR "National Data Centre" OR RSTP OR colocation)
site:datacenterdynamics.com Eswatini OR Swaziland "data centre"
site:connectingafrica.com Eswatini OR Swaziland ("data centre" OR cloud OR colocation OR IXP)
```

旧名回溯：`"Swaziland" ("data centre" OR "data center" OR datacentre OR colocation)`、`"SPTC" OR "Swaziland Posts and Telecommunications Corporation" ("data centre" OR hosting OR colocation)`、`"MTN Swaziland" ("data centre" OR "data center" OR colocation)`。分区基础模板（每个 region 和 anchor town 都要跑）：`"{region}" "{town}" ("data centre" OR "data center" OR datacentre OR colocation OR hosting) (Eswatini OR Swaziland)`、`"{town}" ("server room" OR "disaster recovery" OR "business continuity") (gov.sz OR MICT OR ESCCOM)`、`"{town}" (EIA OR "environmental assessment" OR generator OR UPS OR substation) ("data centre" OR "data center")`。查询语法需避免裸 `OR` 被搜索引擎误解析；优先使用引号和分组概念拆成多条查询。

## 官方/监管管线要点（详见 explorer-official.md）

- **核心官方源**：ESCCOM（esccom.org.sz，200 OK）、Government portal/MICT（gov.sz，200 OK）、RSTP National Data Centre（rstp.org.sz/national-data-centre/，200 OK）、RSTP contact/Phocweni Site（rstp.org.sz/contact-us/）、RSTP PDF brochure（NATIONAL-DATA-CENTRE.pdf）、MTN co-location（mtn.co.sz/businesssolutions/co-location-hosting-services/，200 OK）、ESPPRA（esppra.co.sz，TLS 本地校验报 issuer 问题，`-k` 后 200，跳转 /sppra/）、EEC（eec.co.sz，200 OK）、ESERA（esera.org.sz，200 OK）、EEA（eea.org.sz，200 OK）、EIPA/Invest Eswatini（investeswatini.org.sz，200 OK）、Central Bank of Eswatini（centralbank.org.sz，200 OK）。
- **分区官方覆盖策略**：Hhohho——重点查政府机关、ESCCOM/EEA/ESERA/EIPA/CBE 地址、MTN/EPTC 总部、银行灾备；Lubombo——重点排除糖业/热电/边境光纤被误记为数据中心，只有 EEA/EEC/ESERA/市政材料点名 data centre、colocation 或灾备中心才记录；Manzini——**最高优先级**，RSTP National Data Centre 已定位到 Matsapha/Phocweni，继续检索 Matsapha 工业区、EIPA/RSTP SEZ、EEC 工业电力、UNESWA 和 ISP 托管线索；Shiselweni——预期负检索，仍须跑 gov.sz/ESCCOM/EEA/EEC/ESERA/媒体组合，记录无命中日期和查询集。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **行业默认输出是 B/C 线索**；只有运营商/设施方或政府一手资料点名设施、场地或服务时，才可在最终设施记录中使用 A。
- **高信号行业源**：RSTP（设施方一手服务页，最终优先引用）、MTN eSwatini（运营商一手共置服务页）、Times of Eswatini、Eswatini Observer（旧域跳转，新域 200 OK，本地 curl 可能需 `-k`）、DCD、Connecting Africa、ITWeb Africa、TechAfrica News、Capacity Media、NSRC IXP Africa（SISPA 线索）、Af-IX（IXP 总表）、PeeringDB（SISPA 条目 ix/262）、DataCenterMap/Data Center Platform/Baxtel/DataCenters.com（目录 C，不可替代一手来源）、设备/承包商（Angelique International、IBM、Schneider Electric、Vertiv、Huawei、ZTE、Caterpillar、本地 UPS/generator 承包商，B/C）。
- **运营商与开发商扫描**：RSTP 已确认 A（查容量、Tier 状态、客户、能源和同址政府项目）；MTN eSwatini 已确认 A 服务（重点补物理地点与容量）；EPTC/Eswatini Telecom/Swazi.net 未确认数据中心（查旧 SPTC 文档、hosting、mail、domain、ESCCOM）；Real Image/本地 ISP（C 线索，需运营商或监管证据）；SISPA（B 互联线索，查托管地点）；Liquid/Africa Data Centres/Teraco/Paratus（南非/区域背景，没有 SZ 专属一手证据不得入库）；银行/CBE/支付运营商（只记录公开数据中心/DR facility，普通 server room 不计）；云供应商（A 负向，SZ 云销售/伙伴不等于本地区域）。
- **负检索协议**（对无设施 seed 的 region，记录「合理否定」前必须覆盖）：1) 本地媒体 Times of Eswatini、Eswatini Observer；2) 行业媒体 DCD、Connecting Africa、ITWeb Africa、TechAfrica News、Capacity Media；3) 官方回查 ESCCOM、gov.sz/MICT/RSTP、ESPPRA、EEA、EEC、ESERA、EIPA；4) 互联 NSRC、Af-IX、PeeringDB、ASN/ISP 名称；5) 运营商 RSTP、MTN eSwatini、EPTC/SPTC/Swazi.net、Real Image、Liquid、Paratus、Teraco、Africa Data Centres；6) 旧名 Swaziland、SPTC、SCC、SEB、SERA、SIPA、SPPRA、MTN Swaziland。负检索条目写明日期、查询语句、source classes 和没有命中的字段；不得把目录无条目当作最终否定。

## 维护注意（更新纪律）

- 不删除/移动任何既有文件；双 explorer 文件是 codex 审核定稿，SKILL.md 忠实提炼其内容，细则差异以 explorer 原文件为准。
- 新证据（RSTP/MTN 容量、政府 DR 中心建设与投产、EPTC 设施页）必须带一手来源、地点与状态后才能升级种子分级。
- 发电容量、园区容量、UPS rating、MVA/kVA 与 IT load 分开记录，不自行换算；Tier III 等级保留原文和来源，区分 certified/designed/marketed。
- 目录条目只作发现，不作最终事实；目录中的 city 可能是 nearest city 或国家级占位。定期复核官方 region pages（AWS/Azure/GCP/OCI）。
