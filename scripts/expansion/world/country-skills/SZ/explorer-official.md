# SZ Explorer Official — 埃斯瓦蒂尼（Eswatini）数据中心枚举方法（官方信源）

Date: 2026-08-12. Country: SZ - Eswatini（埃斯瓦蒂尼；旧名 Swaziland，2018-04-19 更名）.

Manifest entry (world-manifest.jsonl):

```json
{"country_code":"SZ","country_name":"Eswatini","subnational_type":"region","divisions":["Hhohho","Lubombo","Manzini","Shiselweni"]}
```

Division model: 4 regions — **Hhohho**, **Lubombo**, **Manzini**, **Shiselweni**. 记录和负检索必须覆盖四个 region；不得把自然地理带（Highveld/Lowveld/Lubombo plateau）误作 manifest 行政层级。

**目的 (Purpose)**：埃斯瓦蒂尼没有公开、集中、可下载的国家级数据中心登记册。官方枚举应先使用一手信源确认设施存在、地点和运营者，再用监管、采购、电力、环境、土地和互连材料补强。对只出现「ICT room / server room / connectivity / cloud services」但没有公开托管、共置或数据中心设施描述的条目，保留为线索，不进入已确认设施表。

## 可靠性分级 (Reliability Grades)

- **A**：官方/一手信源直接点名设施、场地或服务。包括运营商/设施方官网；gov.sz / MICT / RSTP 页面或 PDF；ESCCOM 牌照和公开咨询；ESPPRA 原始采购记录；EEA 环境评估记录；EEC/ESERA 电力记录；EIPA/RSTP/市政土地或园区记录；AWS/Azure/GCP/OCI 官方区域页的负面结论。
- **B**：强二级信源。包括 Times of Eswatini、Eswatini Observer、主流区域 ICT 媒体、Af-IX/NSRC/PeeringDB、供应商案例、采购聚合站复制的官方招标原文。
- **C**：弱线索。包括数据中心目录、市场报告摘录、社交媒体、无出处 MoU 转载、泛泛云/托管营销。

**升级规则**：设施存在可由运营商/设施方官网升为 A；具体 region/城镇/地址只有在同一官方体系或可靠地理证据能定位时才可升为 A。媒体和目录不能单独把设施升级为 A。IXP 是互连生态证据，不等于独立数据中心。

## 已核实事实边界 (Verified Frame)

- **RSTP National Data Centre / Royal Science and Technology Park National Data Centre** — A。RSTP 官网点名 National Data Centre，并描述 remote hands、colocation、web hosting、secure repositories、national payment gateway 等服务。RSTP contact 页面把 Phocweni Site 标为 IT Park，并列出 National Data Centre；地址为 Royal Science & Technology Park, F8PP+RF4, Matsapha, Eswatini。因此记录到 **Manzini region / Matsapha / Phocweni Site**。
- **MTN eSwatini Co-Location Hosting Services** — A（服务存在）；地点待补强。MTN 官方页称该服务是 data centre，提供空间、冷却、电力、物理安全和带宽。若最终数据集要求物理场地，必须继续找 MTN 商业合同、ESCCOM 牌照、EEC 连接、地址或采购/建设记录；在未定位前记录为「operator data centre service, location undisclosed」。
- **Government e-Government / Disaster Recovery Centre** — A（政府项目线索，不等同已运营商业设施）。gov.sz 的 2015-2019 e-Government Operational Framework 明确包括「Disaster Recovery data Centre established」和采购/选址动作；gov.sz ICT 新闻页还描述一栋设施将包含 data center、call center、offices、training centre。需核对后续建设、投产和地点，优先与 RSTP Phocweni National Data Centre 去重。
- **Swaziland Peering Point (SISPA)** — B。NSRC/PeeringDB/Af-IX 生态资料列出 SISPA / Swaziland Peering Point，country SZ，peer 数量很小。它是 IXP/peering 线索，不可单列为数据中心；只在托管场地被查明后作为设施互连证据。
- **超大规模公有云区域** — A（负面）。AWS、Azure、Google Cloud、Oracle OCI 官方区域列表无 Eswatini 区域；最近已核实区域在南非（AWS South Africa/Cape Town, Azure South Africa North/West, Google Cloud Johannesburg `africa-south1`, OCI South Africa Central/Johannesburg）。云边缘、CDN、合作伙伴或 Outposts/Local Zones 线索不得记作 SZ hyperscale region。
- **EPTC / Eswatini Telecom / Eswatini Mobile** — C/B 线索。官网可达并确认 EPTC 为通信企业，但本轮未找到官方数据中心/共置设施页。保留为重点扫描对象，不作为已确认设施。

## 官方信源与已验证 URL (Official Sources)

| 类别 | URL | 本轮状态 | 用途 |
|---|---|---:|---|
| ESCCOM（通信监管） | https://esccom.org.sz/ | 200 OK | 牌照、咨询、互连、运营商合法主体 |
| Government portal / MICT | https://www.gov.sz/ | 200 OK | ICT 新闻、e-Government、部委项目与 PDF |
| RSTP National Data Centre | https://rstp.org.sz/national-data-centre/ | 200 OK | National Data Centre、colocation、remote hands、hosting |
| RSTP contact / Phocweni Site | https://rstp.org.sz/contact-us/ | 可检索 | Phocweni IT Park、Matsapha 地址定位 |
| RSTP PDF brochure | https://rstp.org.sz/wp-content/uploads/2024/08/NATIONAL-DATA-CENTRE.pdf | 200 OK | 服务说明与联系方式；用于补容量/服务字段 |
| MTN co-location | https://www.mtn.co.sz/businesssolutions/co-location-hosting-services/ | 200 OK | MTN data centre service 证据 |
| ESPPRA（采购，旧 SPPRA） | https://www.esppra.co.sz/ | 可达；TLS 本地校验报 issuer 问题，`-k` 后 200，跳转 `/sppra/` | 招标/授标 |
| EEC（电力公司，旧 SEB） | https://www.eec.co.sz/ | 200 OK | 大用户接入、变电站、停电/供电可靠性 |
| ESERA（能源监管，旧 ERA/SERA） | https://www.esera.org.sz/ | 200 OK | 发电/供电/燃油许可、电价、IPP |
| EEA（环境） | https://eea.org.sz/ | 200 OK | EA/EIA 记录、环境许可 |
| EIPA / Invest Eswatini | https://investeswatini.org.sz/ | 200 OK | 投资、园区、土地和企业线索 |
| Central Bank of Eswatini | https://www.centralbank.org.sz/ | 200 OK | 金融基础设施、支付系统、灾备线索 |

## 官方查询模板 (Official Query Templates)

查询语法需避免裸 `OR` 被搜索引擎误解析；优先使用引号和分组概念拆成多条查询。

```text
site:esccom.org.sz ("data centre" OR "data center" OR datacentre OR colocation)
site:esccom.org.sz (licence OR license) (ISP OR "network facilities" OR "internet service") Eswatini
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
```

旧名回溯必须并行跑：

```text
"Swaziland" ("data centre" OR "data center" OR datacentre OR colocation)
"Swaziland Communications Commission" ("licence" OR "license") ISP
"Swaziland" "e-Government" "Disaster Recovery" "data Centre"
"SPTC" OR "Swaziland Posts and Telecommunications Corporation" ("data centre" OR hosting OR colocation)
"MTN Swaziland" ("data centre" OR "data center" OR colocation)
```

## 设施种子清单 (Facility Seed List)

| 设施/项目 | Region | 城镇/场地 | 状态 | 最佳证据 | 级别 | 后续动作 |
|---|---|---|---|---|---:|---|
| RSTP National Data Centre | Manzini | Matsapha / Phocweni Site | Operational / service marketed | RSTP official National Data Centre page + RSTP contact page/PDF | A | 抽取地址、服务、联系人；查 EEC/ESERA/EEA 是否有电力/许可；与政府 e-Gov data centre 去重 |
| MTN eSwatini Co-Location Hosting Services | 待定 | 未公开 | Operational service; facility location undisclosed | MTN official co-location page | A for service, B for facility detail until located | 查 ESCCOM 牌照、MTN enterprise docs、发票/合同地址、EEC 连接；不要默认 Mbabane |
| Government Disaster Recovery / e-Government Data Centre | 待定；Manzini/RSTP 候选 | 待定 | Project evidence; operational status to verify | gov.sz e-Government framework and ICT news | A as project clue | 查后续预算、验收、RSTP 归属、采购授标、site handover |
| SISPA / Swaziland Peering Point | 待定 | 待定 | IXP / peering clue | NSRC/PeeringDB/Af-IX | B | 查托管方和物理场地；仅作为互连证据 |
| EPTC / Eswatini Telecom / Eswatini Mobile hosting | Hhohho/Manzini 候选 | 待定 | Unconfirmed | EPTC site and Swazi.net clues only | C/B | 查 EPTC 产品页、ESCCOM licence, `.sz`/mail hosting infrastructure；需明确 data centre/colocation |
| 金融机构灾备机房 | 待定 | 待定 | Unconfirmed | CBE/银行年报线索 | B/C | 只记录公开点名的灾备中心；普通 server room 不计 |
| Hyperscale cloud region | — | — | Negative | AWS/Azure/GCP/OCI region lists | A negative | 定期复核官方 region pages |

## 分地区官方覆盖策略 (Per-Region Official Coverage)

基础模板（每个 region 和 anchor town 都要跑）：

```text
"{region}" "{town}" ("data centre" OR "data center" OR datacentre OR colocation OR hosting) (Eswatini OR Swaziland)
"{town}" ("server room" OR "disaster recovery" OR "business continuity") (gov.sz OR MICT OR ESCCOM)
"{town}" (EIA OR "environmental assessment" OR generator OR UPS OR substation) ("data centre" OR "data center")
"{operator}" "{town}" (licence OR "co-location" OR colocation OR "data centre" OR hosting)
```

- **Hhohho**：Mbabane, Lobamba, Ezulwini, Pigg's Peak, Bulembu。重点查政府机关、ESCCOM/EEA/ESERA/EIPA/CBE 地址、MTN/EPTC 总部、银行灾备。不能因总部在 Mbabane 就把未定位 data centre 放入 Hhohho。
- **Lubombo**：Siteki, Big Bend, Simunye, Mhlume, Lavumisa。重点排除糖业/热电/边境光纤被误记为数据中心；只有 EEA/EEC/ESERA/市政材料点名 data centre、colocation 或灾备中心才记录。
- **Manzini**：Manzini, Matsapha, Phocweni, Malkerns, Kwaluseni。最高优先级。RSTP National Data Centre 已定位到 Matsapha/Phocweni；继续检索 Matsapha 工业区、EIPA/RSTP SEZ、EEC 工业电力、UNESWA 和 ISP 托管线索。
- **Shiselweni**：Nhlangano, Hluti, Mahamba, Hlatikulu。预期负检索；仍需跑 gov.sz/ESCCOM/EEA/EEC/ESERA/媒体组合，记录无命中日期和查询集。

## 记录、去重与容量规则 (Recording Rules)

- Swaziland/Eswatini 新旧国名指同一国家；SCC/ESCCOM、SEB/EEC、SERA/ESERA、SPPRA/ESPPRA、SIPA/EIPA、SPTC/EPTC、MTN Swaziland/MTN eSwatini 要按法律实体和地址去重。
- RSTP、MICT/e-Government、National Contact Centre、National Data Centre 可能在同一 Phocweni IT Park 生态内重叠；不能把同一楼宇/园区重复记为多座设施。
- 每条设施记录至少包含：operator/legal entity, facility name, region, town/site, address or geocode if public, source URL, source grade, operational status, services, capacity if stated, power/cooling evidence, confidence notes, unresolved checks.
- 容量保守记录：不把 kVA/MVA 自动换算为 MW；发电容量、园区电力、太阳能项目容量不等于 IT load；「Tier III」只有在 Uptime Institute 或运营方材料明确说明认证/设计状态时记录原文。
- 负面记录必须说明日期、查询语句、覆盖的 source classes。没有命中不等于不存在，尤其是未公开政府/电信灾备设施。
