# SZ Explorer Industry — 埃斯瓦蒂尼（Eswatini）数据中心发现方法（行业/媒体/厂商）

Date: 2026-08-12. Scope: Eswatini (SZ) 数据中心发现。行业文件用于扩展线索；所有可入库设施仍须回到 `explorer-official.md` 的官方/运营商一手信源流程验证。

Manifest entry confirmed from `world-manifest.jsonl`:

```json
{"country_code":"SZ","country_name":"Eswatini","subnational_type":"region","divisions":["Hhohho","Lubombo","Manzini","Shiselweni"]}
```

Division model: **region** — Hhohho; Lubombo; Manzini; Shiselweni. 城镇锚点：Mbabane, Lobamba, Ezulwini, Pigg's Peak, Bulembu（Hhohho）；Siteki, Big Bend, Simunye, Mhlume, Lavumisa（Lubombo）；Manzini, Matsapha, Phocweni, Malkerns, Kwaluseni（Manzini）；Nhlangano, Hluti, Mahamba, Hlatikulu（Shiselweni）。

## 可靠性分级 (Reliability Grades)

- **A**：官方/一手信源。包括设施方或运营商官网、gov.sz/MICT/RSTP、ESCCOM、ESPPRA、EEC/ESERA、EEA、EIPA/市政、AWS/Azure/GCP/OCI 官方区域列表。
- **B**：强二级信源。包括本地主流媒体、Data Center Dynamics、Connecting Africa、ITWeb Africa、Capacity Media、TechAfrica News、Af-IX、NSRC、PeeringDB、供应商案例研究、保留原文的采购转载。
- **C**：弱线索。包括 DataCenterMap、DataCenters.com、Baxtel、市场报告、社媒、SEO 云主机页面、无出处新闻转载。

行业发现的默认输出是 B/C 线索；只有运营商/设施方或政府一手资料点名设施、场地或服务时，才可在最终设施记录中使用 A。

## 已核实行业/运营商信号 (Verified Industry and Operator Signals)

- **RSTP National Data Centre**：一手官网已核实。RSTP 页面描述 National Data Centre、colocation、remote hands、web hosting、secure repositories 和 national payment gateway 等服务；contact 页面把 National Data Centre 放在 Phocweni IT Park，地址为 Matsapha。DataCenterMap、Data Center Platform 等目录可辅助发现，但最终引用应优先使用 RSTP URL。
- **MTN eSwatini co-location**：一手官网已核实。MTN 官方页直接描述 co-location hosting as a data centre，并列出 physical security、space、cooling、power、bandwidth。行业侧任务是找物理位置、机房名称、容量、客户/互连证据；不要默认其位于 Mbabane。
- **Government e-Government / Disaster Recovery Centre**：gov.sz PDF 和 ICT 新闻已核实为项目线索。行业侧要查媒体是否报道 RSTP/政府楼宇验收、启用、承包商 Angelique International、IBM 培训中心、National Contact Centre 同址等。
- **SISPA / Swaziland Peering Point**：NSRC/PeeringDB/Af-IX 生态资料存在。它是互连线索，不是数据中心记录；查找托管地点、成员 ASN、是否与 RSTP/MTN/EPTC 机房关联。
- **EPTC / Eswatini Telecom / Swazi.net**：公司官网可达，但本轮未核实到数据中心/共置服务页。行业目录、邮件/hosting、旧 SPTC/Swazi.net 资料只能作为发现线索。
- **Hyperscale clouds**：官方区域页无 Eswatini region；行业新闻如写「cloud in Eswatini」通常指 South Africa regions、reseller、sovereign hosting、edge/CDN 或 local partner。

## 语言与命名矩阵 (Language / Naming Matrix)

| 类别 | 变体 |
|---|---|
| 国名 | Eswatini; eSwatini; Swaziland; Kingdom of Eswatini; Kingdom of eSwatini; Kingdom of Swaziland; umbuso weSwatini |
| 地名 | Mbabane; eMbabane; Lobamba; Ezulwini; Manzini; eManzini; Matsapha; Phocweni; Malkerns; Kwaluseni; Siteki; eSiteki; Big Bend; Simunye; Mhlume; Lavumisa; Nhlangano; Hluti; Hlatikulu; Pigg's Peak; Bulembu |
| 机构 | RSTP / Royal Science and Technology Park; National Data Centre; MICT; ESCCOM / SCC; EEC / SEB; ESERA / SERA / ERA; EEA / SEA; EIPA / SIPA / SIDC; ESPPRA / SPPRA; MTN eSwatini / MTN Eswatini / MTN Swaziland; EPTC / SPTC / Swazi.net |
| 技术词 | data centre; data center; datacentre; colocation; co-location; hosting; remote hands; disaster recovery; business continuity; server room; cloud; Tier III; Uptime Institute; UPS; generator; MW; MVA; kVA |

## 行业与媒体信源 (Industry and Press Sources)

| 信源 | URL / 路径 | 用途 | 级别 |
|---|---|---|---:|
| RSTP | https://rstp.org.sz/national-data-centre/ | 设施方一手服务页；最终优先引用 | A |
| MTN eSwatini | https://www.mtn.co.sz/businesssolutions/co-location-hosting-services/ | 运营商一手共置服务页 | A |
| Times of Eswatini | https://times.co.sz/ | 本地商业/ICT/政府项目报道 | B |
| Eswatini Observer | https://www.observer.org.sz/ -> https://www.eswatiniobserver.com/ | 本地政府/商业报道；旧域跳转，新域 200 OK；本地 curl 可能需 `-k` | B |
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/ | 非洲数据中心市场、区域运营商新闻 | B |
| Connecting Africa | https://www.connectingafrica.com/ | 电信、云、光纤、IXP 新闻 | B |
| ITWeb Africa | https://itweb.africa/ | 南部非洲 ICT 新闻 | B |
| TechAfrica News | https://techafricanews.com/ | 政府数字化、运营商新闻 | B |
| Capacity Media | https://www.capacitymedia.com/ | 互连、海缆、批发网络 | B |
| NSRC IXP Africa | https://nsrc.org/ixp/Africa.html | SISPA / Swaziland Peering Point 线索 | B |
| Af-IX | https://af-ix.org/ixps-list | 非洲 IXP 总表；用作互连交叉检查 | B |
| PeeringDB | https://www.peeringdb.com/ix/262 | SISPA 条目；需登录/动态页时用搜索结果或 API 辅助 | B |
| DataCenterMap | https://www.datacentermap.com/eswatini/ | RSTP 等目录线索；不可替代一手来源 | C |
| Data Center Platform / Baxtel / DataCenters.com | 各目录站 | 名称、地址、别名发现 | C |
| 设备/承包商 | Angelique International, IBM, Schneider Electric, Vertiv, Huawei, ZTE, Caterpillar, local UPS/generator contractors | 建设、供电、冷却、维护线索 | B/C |

## 运营商与开发商扫描 (Operator and Developer Sweep)

| 目标 | 主 URL / 线索 | 当前处理 |
|---|---|---|
| Royal Science and Technology Park (RSTP) | `rstp.org.sz`, National Data Centre, Phocweni Site, Matsapha | 已确认 A；查容量、Tier 状态、客户、能源和同址政府项目 |
| MTN eSwatini | `mtn.co.sz`, co-location hosting | 已确认 A 服务；重点补物理地点与容量 |
| EPTC / Eswatini Telecom / Swazi.net | `eptc.co.sz`, `sptc.co.sz`, `eswatinitelecom.co.sz`, `swazi.net` | 未确认数据中心；查旧 SPTC 文档、hosting、mail、domain、ESCCOM |
| Real Image / local ISPs | ISP 官网、ESCCOM licence、ASN/PeeringDB | C 线索；需要运营商或监管证据 |
| SISPA / Swaziland Peering Point | NSRC, PeeringDB, Af-IX | B 互连线索；查托管地点 |
| Liquid / Africa Data Centres / Teraco / Paratus | 区域运营商官网和新闻 | 南非/区域背景；没有 SZ 专属一手证据不得入库 |
| Banks / CBE / payment operators | CBE、银行年报、payment-system docs | 只记录公开数据中心/DR facility；普通 server room 不计 |
| Cloud providers | AWS, Azure, Google Cloud, OCI region pages | A 负面；SZ 云销售/伙伴不等于本地 region |

## 可用查询模板 (Usable Query Templates)

将复杂 `OR` 拆分为短查询，避免搜索引擎误读。

```text
"Royal Science and Technology Park" "National Data Centre"
"RSTP" "National Data Centre" Matsapha OR Phocweni
"National Data Centre" Eswatini colocation "remote hands"
"MTN eSwatini" "co-location" "data centre"
"MTN Swaziland" colocation OR hosting
"Swaziland Peering Point" OR SISPA
"Eswatini" "Internet Exchange" OR IXP
"Angelique International" Eswatini "data center" OR "data centre"
"IBM" Eswatini "training centre" "data center"
"EPTC" OR "SPTC" "data centre" OR "data center" OR colocation OR hosting
"Swazi.net" hosting "data centre" OR "server"
"Matsapha" "data centre" OR "data center" OR colocation OR hosting
```

Source-scoped searches:

```text
site:times.co.sz ("data centre" OR "data center" OR "National Data Centre" OR RSTP OR colocation)
site:observer.org.sz ("data centre" OR "data center" OR "National Data Centre" OR RSTP OR colocation)
site:datacenterdynamics.com Eswatini OR Swaziland "data centre"
site:connectingafrica.com Eswatini OR Swaziland ("data centre" OR cloud OR colocation OR IXP)
site:itweb.africa Eswatini OR Swaziland ("data centre" OR cloud OR MTN OR RSTP)
site:capacitymedia.com Eswatini OR Swaziland (IXP OR peering OR fibre OR data centre)
site:datacentermap.com/eswatini RSTP OR "National Data Center"
```

## 枚举矩阵 (Enumeration Matrix)

| Region | 城镇/园区锚点 | 最可能信源类型 | 当前预期 |
|---|---|---|---|
| Hhohho | Mbabane, Lobamba, Ezulwini, Pigg's Peak, Bulembu | 政府机关、监管机构、MTN/EPTC 总部、银行灾备、媒体 | 高线索密度，但未定位设施不可自动落 Hhohho |
| Lubombo | Siteki, Big Bend, Simunye, Mhlume, Lavumisa | 工业能源、边境连接、糖业企业、地方政府 | 中低；能源/工业项目多，不等于数据中心 |
| Manzini | Manzini, Matsapha, Phocweni, Malkerns, Kwaluseni | RSTP、工业园区、EIPA、EEC 工业电力、ISP、UNESWA | 最高；RSTP National Data Centre 已确认 |
| Shiselweni | Nhlangano, Hluti, Mahamba, Hlatikulu | 地方媒体、市政、EIA、电力记录 | 低；执行负检索协议 |

## 分地区行业检索指南 (Per-Region Industry Guidance)

基础扫描（每个 region/town 套用）：

```text
"{region}" "{town}" Eswatini "data centre"
"{region}" "{town}" Swaziland "data center"
"{town}" colocation OR "co-location" OR hosting OR "remote hands"
"{town}" "disaster recovery" "business continuity" Eswatini
"{town}" UPS OR generator OR substation "data centre"
site:times.co.sz "{town}" ICT OR "data centre" OR RSTP OR MTN
site:observer.org.sz "{town}" ICT OR "data centre" OR RSTP OR MTN
```

- **Hhohho**：查 Mbabane 与 Ezulwini 的总部型误导。行业报道若只说「company launched cloud service」但没有 facility/site，不入设施；转官方页核验。
- **Lubombo**：查 Big Bend/Simunye/Mhlume 时要排除 sugar estate cogeneration、factory control rooms、border telecom huts。只收「data centre/colocation/DR centre」明确措辞。
- **Manzini**：围绕 Matsapha/Phocweni/RSTP 扩展：目录别名、承包商、IBM/Angelique、National Contact Centre、EIPA/RSTP SEZ、EEC connection。注意 RSTP 和政府 e-Gov 项目可能同址。
- **Shiselweni**：以负检索为主。Nhlangano/Hluti/Hlatikulu/Mahamba 有命中时，先判断是普通 ICT/server room 还是对外服务/灾备设施。

## 负检索协议 (Negative-Search Protocol)

对无设施 seed 的 region，记录「合理否定」前必须覆盖：

1. 本地媒体：Times of Eswatini、Eswatini Observer；
2. 行业媒体：DCD、Connecting Africa、ITWeb Africa、TechAfrica News、Capacity Media；
3. 官方回查：ESCCOM、gov.sz/MICT/RSTP、ESPPRA、EEA、EEC、ESERA、EIPA；
4. 互连：NSRC、Af-IX、PeeringDB、ASN/ISP 名称；
5. 运营商：RSTP、MTN eSwatini、EPTC/SPTC/Swazi.net、Real Image、Liquid、Paratus、Teraco、Africa Data Centres；
6. 旧名：Swaziland、SPTC、SCC、SEB、SERA、SIPA、SPPRA、MTN Swaziland。

负检索条目写明日期、查询语句、source classes 和没有命中的字段。不得把目录无条目当作最终否定。

## 去重与容量规则 (De-Duplication and Capacity Rules)

- RSTP National Data Centre、National Contact Centre、e-Government Centre、Phocweni IT Park 和政府 Disaster Recovery Centre 可能互相重叠；按地址、业主、运营商和功能去重。
- MTN co-location 是运营商服务；未定位前不要与 MTN HQ、交换局或基站机房合并。
- Swaziland/Eswatini 新旧名称统一；SPTC/EPTC/Eswatini Telecom/Swazi.net 需按业务线和法律实体注明。
- 目录条目只作发现，不作最终事实；目录中的 city 可能是 nearest city 或国家级占位。
- 发电容量、园区容量、UPS rating、MVA/kVA 与 IT load 分开；不自行换算。Tier III 等级保留原文和来源，区分 certified、designed、marketed。
