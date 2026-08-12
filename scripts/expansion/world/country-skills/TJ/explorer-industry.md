# TJ Explorer — Industry/Vendor Discovery（塔吉克斯坦数据中心 行业/厂商发现方法论）

最后核验（Live pass）：2026-08-12。范围：从运营商、托管/云/主机商、IXP、CDN、AI/HPC 厂商、认证、行业媒体和目录角度枚举塔吉克斯坦（Tajikistan / Ҷумҳурии Тоҷикистон）数据中心项目。行政覆盖必须与 manifest 精确一致：`Dushanbe`, `Gorno-Badakhshan`, `Khatlon`, `districts under government jurisdiction`, `Sughd`。

分级：**A** = 官方/一手（运营商、政府、采购、Uptime、云厂商官方、PeeringDB 自述数据）；**B** = 可信行业媒体/开发银行/国家通讯社/监管邻近来源；**C** = 目录、地图、聚合器、营销页；**U** = 无法核实或来源不支持。A 级只覆盖来源实际支持的事实；目录和媒体不得把计划、MOU、路线图直接升级为运营设施。

---

## 0. 行业框架与现实预期

- 搜索语言：俄语优先，英语用于国际厂商/AI/HPC，塔吉克语用于官方与本地页面。核心词见 explorer-official.md；行业侧补充 `колокация`, `размещение оборудования`, `VPS`, `облако`, `пиринг`, `CDN`, `GPU cluster`, `high-density AI compute`, `Tier III`, `стойка`, `майнинг-ферма`。
- 市场结构：
  1. **运营商与电信局房**：Tojiktelecom、Tcell、Babilon-M、Megafon TJ、Beeline TJ、区域 ISP。多数是自用交换/核心机房或技术站点；只有官方明确对外托管/colocation 时才记商业服务。
  2. **IXP/互联互通**：TJ-IX Dushanbe 已在 PeeringDB 和 Tojiktelecom 官方页核验，是塔吉克斯坦最强的互联基础设施事实之一。
  3. **政府/Smart City 设施**：Uptime Institute 已列 `Dushanbe State Unitary Enterprise Smart City Data Center`，需用 Uptime 认证类型和政府/采购/验收材料区分设计认证、建设和投运。
  4. **AI/HPC/绿色算力**：darya.ai / Yotta Darvoz 项目为 2025 年后的新重点。当前强证据支持合作和路线图，投产/建设状态需继续验证。
  5. **加密矿场**：高功率设施可能被目录称为 data center；除非有第三方托管/云客户，一律独立标 `mining/HPC`。
  6. **公共云区域**：AWS/Azure/GCP/OCI 官方区域页无 TJ；本地「cloud」多为运营商/主机商服务，不等于 hyperscale cloud region。
- 地理优先级：Dushanbe > districts under government jurisdiction（Darvoz/杜尚别近郊）> Sughd > Khatlon > Gorno-Badakhshan。

---

## 1. 权威与强来源

### 1.1 运营商、IXP、认证

| 来源 | URL | 用途 | 分级/注意 |
|---|---|---|---|
| Tojiktelecom | https://tojiktelecom.tj/ | 国有通信运营商；互联网、国际通信、TJ-IX、技术站点/colocation | A（服务/自述）；设施规格需另证 |
| TJ-IX | https://tj-ix.tj/；PeeringDB https://www.peeringdb.com/ix/4728 | Dushanbe IXP、参与者、容量、联系方式、统计链接 | A（PeeringDB/运营方自述） |
| Tcell | https://www.tcell.tj/ | 移动/固定接入、企业服务、机房线索 | A（服务自述）；设施推断 C |
| Babilon-M | https://www.babylon.tj/ | 移动/ISP/企业服务 | A-/C |
| Megafon Tajikistan | https://www.megafon.tj/ | 移动/企业连接 | A-/C |
| Beeline Tajikistan | https://www.beeline.tj/ | 移动/企业连接 | A-/C |
| Uptime Institute TJ | https://uptimeinstitute.com/uptime-institute-awards/country/id/TJ | 认证项目核查；已显示 Dushanbe Smart City Data Center | A（认证事实） |
| RIPE NCC TJ members | https://www.ripe.net/membership/member-support/list-of-members/tj/ | 本地 LIR/网络运营者普查 | A（成员事实） |
| PeeringDB country/ASN search | https://www.peeringdb.com/ | CDN/IX 参与者、网络与设施关系 | A（自报数据，需时间戳） |

### 1.2 目录、媒体、项目库

| 来源 | URL | 用途 | 分级/注意 |
|---|---|---|---|
| Data Center Dynamics | https://www.datacenterdynamics.com/ | Darvoz/Yotta 等国际数据中心新闻 | B |
| Developing Telecoms | https://developingtelecoms.com/ | 区域电信/数据中心新闻 | B |
| Baxtel TJ | https://baxtel.com/data-center/tajikistan | darya.ai/Darvoz/Zev 目录线索 | C；目录状态和容量需官方佐证 |
| Data Center Map | https://www.datacentermap.com/ | 商业 DC 目录；DCD 2025 报道称其当时未列 TJ 商业 DC | C |
| Cloudscene / datacenters.com | https://www.cloudscene.com/ 等 | 主机/colo 目录线索 | C |
| hostings.info TJ | https://ru.hostings.info/hostings/country/tajikistan-hosting | 本地主机商发现 | C |
| 2GIS / Yandex Maps | https://2gis.tj/dushanbe | 本地地址、商户、机房名 | C，仅地址线索 |
| Khovar / Asia-Plus / Avesta / Sputnik TJ / Ozodi | khovar.tj、asiaplustj.info、avesta.tj、tj.sputniknews.ru、ozodi.org | 本地新闻、政府口径、矿场/限电报道 | B；Khovar 引官方决定时可 A- |
| Yotta / darya.ai | https://yotta.com/；https://www.greendarya.ai/ | Darvoz AI data center 官方/公司自述 | A（合作/路线图自述），建设状态需另证 |

关键提醒：塔吉克斯坦市场小，单一项目会被多个目录重复收录。必须先归并同名、同地区、同业主、同电源的条目，再决定是否是一个物理设施、多个阶段，或目录重复。

---

## 2. 查询模板

### 2.1 全国发现

```text
Tajikistan "data center" "Dushanbe"
Tajikistan "AI data center" "Darvoz"
"darya.ai" "Darvoz" "data center"
"Yotta" "Tajikistan" "data center"
"Dushanbe State Unitary Enterprise Smart City Data Center"
"Republic of Tajikistan" "Uptime Institute" "Data Center"
"Таджикистан" "ЦОД" "Душанбе"
"Таджикистан" "центр обработки данных" "Душанбе"
"Таджикистан" "дата-центр"
"Таджикистан" "колокация"
"Таджикистан" "размещение оборудования"
"Таджикистан" "облачные услуги"
"Таджикистан" "майнинг-ферма" "электроэнергия"
"Тоҷикистон" "маркази коркарди додаҳо"
"Тоҷикистон" "зеҳни сунъӣ" "марказ"
"Точиктелеком" "TJ-IX"
"Точиктелеком" "колокация"
"Tcell" "data center" "Dushanbe"
"Вавилон" "серверная" "Душанбе"
"Мегафон" "Таджикистан" "дата-центр"
"Билайн" "Таджикистан" "серверная"
```

### 2.2 IXP / CDN / 网络

```text
site:peeringdb.com "TJ-IX"
site:peeringdb.com "Tajikistan" "Dushanbe"
site:tojiktelecom.tj "TJ-IX"
site:tj-ix.tj "participants"
"TJ-IX" "Meta"
"TJ-IX" "Cloudflare"
"TJ-IX" "Akamai"
"Tajikistan Internet Exchange"
Таджикистан "точка обмена трафиком"
Таджикистан "пиринг"
site:ix.report "TJ-IX"
```

### 2.3 状态、容量、认证

```text
"{project}" "MW"
"{project}" "МВт"
"{project}" "2MW"
"{project}" "100MW"
"{project}" "GPU cluster"
"{project}" "NVIDIA H200"
"{project}" "Tier III"
"{project}" "Certification of Design Documents"
"{project}" "введён в эксплуатацию"
"{project}" "ба истифода дода шуд"
"{project}" "construction began"
"{project}" "strategic collaboration agreement"
"{project}" "power purchase"
"{project}" "hydropower"
```

生命周期判定：

- `signed`, `strategic collaboration`, `MOU`, `меморандум` = 意向/合作。
- `planned`, `roadmap`, `expanding up to` = 规划容量。
- `construction began`, `groundbreaking`, `началось строительство` = 建设。
- `commissioned`, `launched`, `operational`, `введён в эксплуатацию`, `ба истифода дода шуд` = 投产，但仍需设施主体与日期。
- Uptime `Tier III Certification of Design Documents` = 设计文件认证；不能代表建成或运营认证。

---

## 3. 关键厂商与项目族（已核验种子）

### 3.1 Dushanbe：Smart City、Tojiktelecom、TJ-IX

- **Dushanbe State Unitary Enterprise Smart City Data Center**：Uptime Institute 已列 Tajikistan/Republic of Tajikistan 项目，地点 Dushanbe，认证类型至少包括 Tier III Design Documents。作为 A 级认证事实保留；建设、投产、业主法人、地址、容量需再查 president.tj、Dushanbe municipality、eprocurement、Uptime award detail。
- **TJ-IX Dushanbe**：PeeringDB ix/4728 显示 16 peers、610G total capacity、Tojiktelecom 组织、Dushanbe、2026-01-25 更新时间；Tojiktelecom 官方 TJ-IX 页面称其为国内中心互联网流量交换点，并列出 10G/40G/100G、面向运营商/企业/政府、以及在 Tojiktelecom 技术站点放置设备（colocation）的能力。
- **Tojiktelecom technology sites / colocation**：可作为 A 级服务能力，但不是自动的设施级记录。若数据集需要物理设施，必须找地址、设备间/机房、供电、客户或采购材料。

### 3.2 RRP：Darvoz darya.ai / Yotta green AI data center

- **项目事实**：Yotta 2025-10-25 官方新闻稿称与 darya.ai 签署战略合作，意图在 Darvoz, Tajikistan 建设绿色 AI data center；darya.ai 官网称 Tajikistan AI Data Center，2 MW 起步、最高 100 MW 路线图。
- **行政归类**：Darvoz 属 `districts under government jurisdiction`（РРП），不要误放入 Gorno-Badakhshan。
- **状态规则**：Yotta/darya = A（合作和公司自述路线图）；DCD/Developing Telecoms = B；Baxtel = C。未发现政府供电、施工、验收或可用服务合同前，状态应为 `planned/prospective` 或 `announced`; 若 darya 官网出现可购买 GPU/AI 服务并给地点，可拆出服务状态但仍需设施投产证据。
- **去重规则**：Baxtel 同时列 `darya.ai: Darvoz` 与 `Darya AI center (Zev)`；除非官方证据证明 Zev 是独立地点/阶段，不要计为第二座设施。

### 3.3 运营商/移动网络机房

- **Tcell / Babilon-M / Megafon TJ / Beeline TJ**：作为网络运营商和企业连接服务来源扫描。默认记录为 `telecom exchange/server room` 线索；只有出现 `colocation`, `data center`, `размещение оборудования`, `ЦОД`, `hosting` 的官方服务页或合同，才升级为商业托管线索。
- **区域 ISP/LIR**：以 RIPE TJ member list、PeeringDB networks、TJ-IX participants 枚举。若只出现 ASN/peering，不计为 DC；若出现设施/colo/PoP，再追到运营商官方页。
- **CDN/cache**：PeeringDB 可能列 Meta/F-root/内容网络在 TJ-IX；这代表网络互联/缓存或远端参与，不自动代表独立数据中心。

### 3.4 公共云与本地主机商

- **AWS/Azure/GCP/OCI**：官方区域页无 TJ；任何 TJ 公共云区域主张降级为 U，直到厂商官方区域页列出。
- **Yandex/Huawei/Alibaba**：核查官方区域或合作伙伴页；邻国 region/edge/cache 只能记为服务路径，不记 TJ 本土 region。
- **本地主机商**：hostings.info、Cloudscene、2GIS、Data Center Map、Baxtel 仅发现线索。需要公司官网、业务条款、地址、电力/运营商或客户证据才能进入设施表。

---

## 4. 按行政区行业枚举矩阵

| Division（manifest） | 行业/厂商路径 | 预期产出与排除规则 |
|---|---|---|
| Dushanbe | Uptime Smart City DC、Tojiktelecom/TJ-IX、移动运营商总部/核心网、hoster 目录、PeeringDB/CDN、政府/银行机房新闻 | 最高。优先找确证设施；运营商自用机房与商业 DC 分开 |
| Gorno-Badakhshan | Khorog/GBAO、Pamir Energy、电信局房、边境/教育/灾备数字项目 | 基本为零。Darvoz 不归这里；Pamir Energy 只提供电力背景 |
| Khatlon | Bokhtar/Kulob/Danghara/Panj、SEZ、区域 ISP、矿场/工业负载 | 低。矿场与企业/云 DC 分离；查 eprocurement 和电力材料 |
| districts under government jurisdiction | Darvoz、Hisor、Tursunzoda、Yavan、Vahdat、Rudaki、Rasht | 低-中。Darvoz darya/Yotta 是重点；杜尚别近郊项目按真实区县归类 |
| Sughd | Khujand、Buston/SEZ Sughd、Istaravshan/Isfara、北部 ISP/矿场 | 低-中。多为电信局房/矿场/SEZ 意向，需强去重 |

行政区模板：

```text
"{city_ru}" "дата-центр"
"{city_ru}" "ЦОД"
"{city_ru}" "серверная"
"{city_ru}" "колокация"
"{city_ru}" "размещение оборудования"
"{city_ru}" "хостинг"
"{city_tg}" "маркази коркарди додаҳо"
"{city_tg}" "хостинг"
"{city_ru}" "майнинг" "электроэнергия"
"{division_ru}" "data center" "investment"
site:baxtel.com "{city_en}" "Tajikistan"
site:peeringdb.com "{city_en}" "TJ"
```

---

## 5. 行业媒体与观察名单

- **强行业媒体**：Data Center Dynamics、Developing Telecoms、Telecom Review、CNews/Tadviser（视具体来源质量 B/C）。用于捕捉 Darvoz、国际厂商、区域电信/云项目。
- **本地媒体**：Khovar、Asia-Plus、Avesta、Sputnik TJ、Ozodi。用于政府活动、矿场执法、限电、运营商公告；数字与容量必须回到官方/运营商/采购核对。
- **目录**：Baxtel、Data Center Map、Cloudscene、datacenters.com、hostings.info、2GIS、Yandex Maps。目录用于发现和别名，不用于最终状态/容量结论。
- **网络社区**：PeeringDB、RIPE NCC、Internet Society Pulse/IXP Tracker、ix.report。PeeringDB 优先；镜像/统计站用于异常核对。

---

## 6. 验证与分级规则

1. **先判物理设施**：项目名、地点、业主、设施类型、状态、容量、电力来源分别取证；不要把 IXP、租户、云服务、运营商技术站点重复计为多座 DC。
2. **状态严控**：Design Documents、MOU、strategic collaboration、roadmap、directory listing 都不是运营证据。
3. **Darvoz 专项**：记录为 RRP；优先找供电/水电站、建设许可、采购、现场照片、服务上线页。2 MW 起步和 100 MW 扩展按公司自述路线图保留，未交叉验证前不进已投产容量。
4. **Smart City 专项**：Uptime entry 是强线索；必须补查 Dushanbe municipality、Smart City SUE、采购/验收和 Uptime award type，避免把设计认证误写为建成 Tier III。
5. **矿场/HPC 分离**：若客户只做自用挖矿或算力，不提供第三方托管/云服务，类型标 `mining/HPC`；电力 MW 不等于 IT load。
6. **云区域**：只接受厂商官方 global infrastructure/regions 页面；合作伙伴云、本地 reseller、edge/cache 另列服务可用性。
7. **行政边界**：Dushanbe 与 RRP/Rudaki/Hisor/Darvoz 分开；GBAO 只含自治州，Darvoz 不在 GBAO；所有记录必须映射到 manifest 五单元之一。
8. **来源拆分**：地址来自 2GIS = C；认证来自 Uptime = A；容量来自公司路线图 = A（自述规划）或 C（目录）；状态来自媒体 = B。最终条目可有多个事实等级。

推荐输出备注：`operator official`, `Uptime design certification`, `IXP`, `colocation service`, `government agreement`, `company roadmap`, `trade press`, `directory only`, `mining/HPC`, `tenant/PoP`, `MOU only`。

---

## 7. 更新/复检节奏

- **月度**：PeeringDB TJ-IX、Tojiktelecom TJ-IX/colocation、darya.ai/Yotta 新闻、DCD/Developing Telecoms、Khovar/Asia-Plus `ЦОД`/`AI data center`。
- **季度**：Uptime Tajikistan 页面、Baxtel/Data Center Map/Cloudscene 去重、AWS/Azure/GCP/OCI/Yandex/Huawei/Alibaba 官方区域页。
- **半年度**：RIPE TJ member list、Communications Service 许可/统计、移动运营商企业服务页、SEZ/investcom 项目。
- **事件驱动**：Darvoz 供电/开工/投产、Smart City DC 认证或验收变化、冬季限电与矿场执法、新 CDN/IX 参与者。

## 快速 URL 索引

- Tojiktelecom：https://tojiktelecom.tj/ ｜ TJ-IX：https://tj-ix.tj/ ｜ PeeringDB TJ-IX：https://www.peeringdb.com/ix/4728
- Uptime TJ：https://uptimeinstitute.com/uptime-institute-awards/country/id/TJ
- darya.ai：https://www.greendarya.ai/ ｜ Yotta Darvoz announcement：https://yotta.com/press-releases/darya-ai-and-yotta-data-services-sign-strategic-collaboration-agreement-to-develop-tajikistans-first-green-ai-data-center/
- Baxtel TJ：https://baxtel.com/data-center/tajikistan ｜ Data Center Map：https://www.datacentermap.com/ ｜ hostings.info TJ：https://ru.hostings.info/hostings/country/tajikistan-hosting
- 运营商：Tcell https://www.tcell.tj/ ｜ Babilon-M https://www.babylon.tj/ ｜ Megafon TJ https://www.megafon.tj/ ｜ Beeline TJ https://www.beeline.tj/
- 网络社区：PeeringDB https://www.peeringdb.com/ ｜ RIPE TJ https://www.ripe.net/membership/member-support/list-of-members/tj/ ｜ ix.report https://ix.report/
- 媒体：Khovar https://khovar.tj/ ｜ Asia-Plus https://asiaplustj.info/ ｜ Avesta https://www.avesta.tj/ ｜ Sputnik TJ https://tj.sputniknews.ru/ ｜ Ozodi https://www.ozodi.org/ ｜ DCD https://www.datacenterdynamics.com/
- 交叉参考官方管线：同目录 explorer-official.md。
