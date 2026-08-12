---
name: tj-datacenter-methodology
location: scripts/expansion/world/country-skills/TJ/SKILL.md
description: 塔吉克斯坦数据中心查询方法论（Tajikistan datacenter discovery & audit methodology）——双线来源（官方/监管/电力/采购/云管线 + 行业/厂商发现）与五行政单元模型下的设施枚举规则。
---

# TJ · 塔吉克斯坦数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：面向塔吉克斯坦（Tajikistan / Ҷумҳурии Тоҷикистон, TJ）数据中心、AI/HPC 设施、政府/运营商机房、IXP 与云区域的官方口径与行业/厂商发现。双线方法论：`explorer-official.md`（官方/监管/电力/采购/云管线）与 `explorer-industry.md`（行业/厂商发现），均为 codex 审核定稿。划分模型（per manifest）：**capital territory/autonomous region/region/districts under republic administration** — 5 个覆盖单元：**Dushanbe、Gorno-Badakhshan、Khatlon、districts under government jurisdiction、Sughd**。最后核验（Live pass）：2026-08-12。

## 入口

| 入口 | 管线 | 内容 |
|---|---|---|
| `explorer-official.md` | 官方/监管/电力/采购/云管线 | 结构事实（行政区/俄语塔语拼写/登记/法律）、已验证官方门户与制度面、法律/政策核验清单、搜索词汇（俄语优先）、官方/监管管线（通信监管/总统政府数字技术投资/电力电网/政府采购/云区域官方页）、查询模板、按行政区枚举方法、已核验项目/线索与证据状态、可靠性与覆盖规则、更新/复检节奏 |
| `explorer-industry.md` | 行业/厂商发现 | 行业框架与现实预期、权威与强来源（运营商/IXP/认证/目录/媒体/项目库）、查询模板（全国/IXP CDN 网络/状态容量认证）、关键厂商与项目族（Dushanbe Smart City/Tojiktelecom/TJ-IX、Darvoz darya/Yotta、运营商移动网络机房、公共云与本地主机商）、按行政区行业枚举矩阵、行业媒体与观察名单、验证与分级规则、更新节奏 |

## 核心结构事实

1. **行政区划模型**：5 个覆盖单元（manifest 精确值）：Dushanbe（首都、共和国直辖市，不归入任何州，与周边 Rudaki/Hisor 等 RRP 区分）、Gorno-Badakhshan（ГБАО/自治州，中心 Хорог/Хоруғ；Pamir Energy 供电区；**Darvoz 不在 GBAO，勿误归类**）、Khatlon（州，中心 Бохтар，另含 Куляб；Danghara/Kulob/Panj SEZ 与边境贸易线索）、districts under government jurisdiction（РРП/中央直辖区，含 Hisor、Tursunzoda、Vahdat、Yavan、Rudaki、Rasht、Darvoz 等；杜尚别近郊、能源敏感型项目、Darvoz AI DC 均优先检查本单元）、Sughd（州，中心 Худжанд/Хуҷанд；Khujand、Buston/SEZ Sughd、北部矿区/电信局房线索）。塔吉克斯坦为内陆国，**无海底光缆登陆站**——任何 `landing station` 条目均应作为错误或跨境陆缆节点重查。行政边界不要按营销口径的「大杜尚别」自动归并。
2. **注册库现状**：无公开集中登记册；官方枚举采用证据链（设施/运营者名称 -> 政府或运营方页面 -> 监管许可/决定 -> 建设或环评许可 -> 电力接入 -> 海缆/互联 -> 采购/融资记录）。许可证不能证明某公司拥有商业数据中心，仅证明其具备相应通信服务资格。
3. **法律与监管**：通信监管为 Government of RT Communications Service（当前官网 cs.gov.tj，egov 目录仍列 http://khadamotialoqa.tj/；旧草稿 `sps.tj` 不作主入口除非后续重定向或恢复）。法律库 mmk.tj 核验：《О связи》通信法（运营商许可、互联互通、监管执法背景）、《О защите персональных данных》个人数据保护法 No.1537/2018（数据托管、政府云和跨境处理合规背景）、《О государственных закупках товаров, работ и услуг》政府采购法（采购公告/合同作 A 级证据的法律基础）。数字资产、AI、数字经济、电子政务相关法令与战略先查 president.tj、egov.tj、mmk.tj；2025-2030 被官方口径表述为数字经济与创新发展周期，需用具体法令/计划文本支撑。采购主管机构页面在 egov.tj；可检索采购公告的实际门户为 https://eprocurement.gov.tj/（可能响应慢，须并用 `site:eprocurement.gov.tj`），旧/登录系统 `zakupki.gov.tj` 与 `cabinet.zakupki.gov.tj` 仍作交叉入口。投资委员会 https://investcom.tj/（证书主机名不匹配，用无 www 版本）。
4. **互联与云**：**TJ-IX Dushanbe** 是塔吉克斯坦最强的互联基础设施事实之一——PeeringDB ix/4728 显示 16 peers/610G/Tojiktelecom 组织/Dushanbe/2026-01-25 更新（A）；Tojiktelecom 官方 TJ-IX 页称其为国内中心互联网流量交换点，列出 10G/40G/100G、面向运营商/企业/政府，以及在 Tojiktelecom 技术站点放置设备（colocation）的能力。CDN/cache（Meta/F-root 等内容网络可能出现在 TJ-IX）= 网络互联/缓存或远程参与，不自动代表独立数据中心。官方云区域页在 2026-08-12 live pass 复查：AWS/Azure/Google Cloud/Oracle Cloud 官方全球区域页均未显示 Tajikistan/TJ 公共云区域；任何「塔吉克斯坦 AWS/Azure/GCP/OCI region」主张必须以厂商官方区域页为准；邻近区域或合作伙伴云可记录为服务可用性，不计为 TJ 本土 hyperscale region。Yandex Cloud/Huawei Cloud/Alibaba Cloud 使用厂商官方 regions/locations 页，本地代理商营销页只能作 C。
5. **设施/项目种子**（已核验项目/线索与证据状态）：**Dushanbe State Unitary Enterprise Smart City Data Center**（Dushanbe，Uptime Institute 已列项目，至少 Tier III Certification of Design Documents 线索——Uptime client/country page = A（认证/项目名/地点/认证类型），不要把 Design Documents 认证等同于 constructed facility，建成/投运需另证）；**TJ-IX Dushanbe**（运营中 IXP，PeeringDB = A，Tojiktelecom TJ-IX 服务页 = A）；**Tojiktelecom colocation / technology sites**（Dushanbe + 全国局房，服务存在 = A；设施级地址/规格未公开 = U/C）；**darya.ai / Yotta Darvoz green AI data center**（districts under government jurisdiction / Darvoz，2025-10-25 战略合作/计划，darya 页面称当前项目、2 MW 起步、最高 100 MW 路线图——Yotta 官方新闻稿 = A（合作签署/意向）、darya.ai 官网 = A（公司自述路线图）、DCD/Developing Telecoms = B、Baxtel = C；未见政府供电/施工/验收前不要计为 fully operational）；**Darya AI center (Zev)**（待定位，目录线索 C，不得单独计数除非确认不是 Darvoz 同一项目/阶段）；**国家 ЦОД / 统一数据处理中心**（Dushanbe 待确认，政策/电子政务线索，需采购、Uptime、验收或运营页确认，无直接来源时 U）；**加密矿场 / mining-HPC**（Sughd、Khatlon、RRP 最可能，独立类别不默认商业 DC，除非有第三方托管/云客户，标 `mining/HPC`）；**公共云区域**（AWS/Azure/GCP/OCI 官方页无 TJ 区域 = A 负向）。
6. **语言与词汇**：俄语优先，塔吉克语补充，英语用于国际厂商/投资。英语：`data center`, `AI data center`, `green AI data center`, `HPC`, `GPU cluster`, `colocation`, `hosting`, `cloud`, `cloud region`, `internet exchange`, `IXP`, `CDN`, `digital public infrastructure`, `sovereign cloud`, `Smart City Data Center`。俄语：`дата-центр`, `датацентр`, `центр обработки данных`, `ЦОД`, `серверная`, `серверное оборудование`, `колокация`, `размещение оборудования`, `хостинг`, `облачные услуги`, `облачная инфраструктура`, `точка обмена трафиком`, `пиринг`, `майнинг`, `майнинг-ферма`, `высокопроизводительные вычисления`, `искусственный интеллект`, `графический процессор`, `введён в эксплуатацию`, `строительство`, `меморандум`, `электроснабжение`, `технические условия`。塔吉克语：`маркази додаҳо`, `маркази коркарди додаҳо`, `сервер`, `таҷҳизоти серверӣ`, `хостинг`, `абрӣ`, `интернет`, `табодули трафик`, `зеҳни сунъӣ`, `рақамикунонӣ`, `иқтисодиёти рақамӣ`, `хариди давлатӣ`, `сохтмон`, `ба истифода дода шуд`。
7. **可靠性分级**：A=官方/一手来源（政府/监管/采购/电力/运营商官方、Uptime Institute、云厂商官方、PeeringDB 自述数据）；B=可信行业媒体、国家通讯社、开发银行/国际组织、监管邻近来源；C=目录、地图、聚合器、营销页；U=无法核实或来源不支持的主张。**A 级只覆盖来源实际陈述的事实**：例如 MOU 页面只证明「协议已签」，不能证明「设施已建成」。状态词必须精确：`signed`/`меморандум` = 意向；`construction began`/`началось строительство` = 建设；`commissioned`/`введён в эксплуатацию`/`ба истифода дода шуд` = 投产；Uptime `Design Documents` = 设计认证，不是建成认证。
8. **计数与去重规则**：物理设施与服务商分开——IXP、运营商、云服务、租户和物理机房分别建关系，避免 Tojiktelecom/TJ-IX/hoster 重复计数。容量必须分层：已投产 IT MW > 已签供电/并网 MW > 路线图/远期 MW（darya 2 MW/100 MW 目前按公司自述路线图处理）。大功率判定规则：任何 MW 级数据中心、AI/HPC 或矿场声明至少交叉检查电源位置、并网/供电协议、电价类别、季节性限电影响；无电力证据时不得把远期 MW 路线图记为已投产容量。覆盖必须包含 manifest 五单元，即使预期为零也要记录已跑查询、无强证据、主要排除理由。来源拆分：地址来自 2GIS = C；认证来自 Uptime = A；容量来自公司路线图 = A（自述规划）或 C（目录）；状态来自媒体 = B；最终条目可有多个事实等级。行政边界：Dushanbe 与 RRP/Rudaki/Hisor/Darvoz 分开；GBAO 只含自治州，Darvoz 不在 GBAO；所有记录必须映射到 manifest 五单元之一。

## 常用查询模板

```text
site:president.tj "центр обработки данных"
site:president.tj "дата-центр"
site:president.tj "искусственный интеллект" "центр"
site:president.tj "Darya" "Yotta"
site:president.tj "Smart City Data Center"
site:egov.tj "центр обработки данных"
site:cs.gov.tj "лиценз" "оператор"
site:mmk.tj "О связи"
site:mmk.tj "персональных данных"
site:khovar.tj "центр обработки данных"
site:investcom.tj "data center"
site:eprocurement.gov.tj "ЦОД"
site:eprocurement.gov.tj "серверное оборудование"
site:barqitojik.tj "майнинг"
site:minenergo.tj "майнинг" "электроэнергия"
site:tojiktelecom.tj "TJ-IX"
site:tojiktelecom.tj "colocation"
site:tojiktelecom.tj "размещение оборудования"
"Таджикистан" "центр обработки данных" "введён в эксплуатацию"
"Таджикистан" "дата-центр" "меморандум"
"Dushanbe State Unitary Enterprise Smart City Data Center"
"Darvoz" "AI data center" "Tajikistan"
"Darya.ai" "Yotta" "Darvoz"
Tajikistan "data center" "Dushanbe"
"Республика Таджикистан" "Uptime Institute" "Data Center"
"Тоҷикистон" "маркази коркарди додаҳо"
site:peeringdb.com "TJ-IX"
site:tj-ix.tj "participants"
"TJ-IX" "Meta"
"Tajikistan Internet Exchange"
"Точикителеком" "колокация"
"Tcell" "data center" "Dushanbe"
"Мегафон" "Таджикистан" "дата-центр"
"Билайн" "Таджикистан" "серверная"
site:baxtel.com "Tajikistan"
site:datacenterdynamics.com Tajikistan "Darvoz" OR "Yotta"
site:developingtelecoms.com Tajikistan
```

行政区模板：`"{division_ru}" "{city_ru}" "центр обработки данных"`；`"{division_ru}" "{city_ru}" "дата-центр"`；`"{division_tg}" "{city_tg}" "маркази коркарди додаҳо"`；`"{city_ru}" "майнинг" "электроэнергия"`；`site:eprocurement.gov.tj "{city_ru}" "сервер"`。状态/容量/认证模板：`"{project}" "MW"` / `"{project}" "МВт"` / `"{project}" "GPU cluster"` / `"{project}" "Tier III"` / `"{project}" "Certification of Design Documents"` / `"{project}" "введён в эксплуатацию"` / `"{project}" "construction began"` / `"{project}" "hydropower"`。

## 官方/监管管线要点（详见 explorer-official.md）

- **核心官方源**：总统 president.tj、电子政务/机构目录 egov.tj、通信监管 cs.gov.tj（旧/目录域 khadamotialoqa.tj）、法律库 mmk.tj、采购 eprocurement.gov.tj / zakupki.gov.tj / cabinet.zakupki.gov.tj、投资委 investcom.tj、创新与数字技术署（egov.tj/site/innovation，uidt.tj 使用前确认页面主体）、电力 Barqi Tojik（barqitojik.tj，HTTPS 证书可能过期用 HTTP）/ 能源与水资源部 minenergo.tj、Pamir Energy（GBAO 供电特例，IEA/OECD 确认 Barki Tojik 供电范围不含 GBAO）、Tojiktelecom tojiktelecom.tj、TJ-IX tj-ix.tj。
- **电力/电网管线**：Barqi Tojik 核验供电可靠性、限电、大用户接入、发电/配电项目；能源部核验电价、能源密集型负载、矿场限制和大负荷政策；GBAO 项目须使用 Pamir Energy、AKDN/IFC/World Bank 或地方政府交叉确认。
- **政府采购管线**：eprocurement.gov.tj/ru/searchanno 主入口；检索 `ЦОД`、`центр обработки данных`、`дата-центр`、`серверное оборудование`、`система хранения данных`、`облачные услуги`、`хостинг`、`таҷҳизоти серверӣ`。采购记录 = A 级采购事实，但只覆盖标段/中标/采购人/日期/金额/技术要求；若标的是服务器或存储设备，除非出现建设、机房、ЦОД、托管、运维合同等字段，不自动计为数据中心设施。
- **已核验项目/线索证据状态**：Smart City Data Center（Uptime 已列，Tier III Design Documents 线索，建成/投运待证）；TJ-IX（运营中，PeeringDB/Tojiktelecom A）；Tojiktelecom colocation（服务能力 A，设施级 U/C）；darya/Yotta Darvoz（2025-10-25 战略合作，2 MW/100 MW 路线图按公司自述，投产/建设状态需电力和现场证据）；Darya AI center Zev（C 目录线索，去重待证）；国家 ЦОД（U 待确认）；矿场（独立标 `mining/HPC`）；公共云区域（A 负向）。
- **更新/复检节奏**：月度——TJ-IX PeeringDB、Tojiktelecom TJ-IX/colocation 页、president.tj/khovar.tj/egov.tj 的 AI/DC/数字基础设施检索、eprocurement 新公告；季度——Uptime Tajikistan 页、darya/Yotta Darvoz 状态、电力/供电证据、云厂商官方区域页；半年——Communications Service 入口域名与许可统计、投资委/SEZ 项目、Barqi Tojik 与 GBAO/Pamir Energy 供电背景；事件驱动——总统出席 AI/数据中心活动、签供电协议、开工/竣工/验收、冬季限电或矿场执法。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **市场结构**：1) 运营商与电信局房——Tojiktelecom、Tcell、Babilon-M、Megafon TJ、Beeline TJ、区域 ISP，多数是自用交换/核心机房或技术站点，只有官方明确对外托管/colocation 时才记商业服务；2) IXP/互联互通——TJ-IX Dushanbe 已核验，是塔吉克斯坦最强的互联基础设施事实之一；3) 政府/Smart City 设施——Uptime 已列 Dushanbe Smart City Data Center，需用认证类型和政府/采购/验收材料区分设计认证、建设和投运；4) AI/HPC/绿色算力——darya.ai/Yotta Darvoz 为 2025 年后新重点，当前强证据支持合作和路线图，投产/建设状态需继续验证；5) 加密矿场——高功率设施可能被目录称为 data center，除非有第三方托管/云客户，一律独立标 `mining/HPC`；6) 公共云区域——AWS/Azure/GCP/OCI 官方区域页无 TJ，本地「cloud」多为运营商/主机商服务，不等于 hyperscale cloud region。地理优先级：Dushanbe > districts under government jurisdiction（Darvoz/杜尚别近郊）> Sughd > Khatlon > Gorno-Badakhshan。
- **权威与强来源**：Tojiktelecom（A 服务/自述）、TJ-IX tj-ix.tj/PeeringDB ix/4728（A）、Tcell（A 服务自述，设施推断 C）、Babilon-M/Megafon TJ/Beeline TJ（A-/C）、Uptime Institute TJ 页（A 认证事实）、RIPE NCC TJ members（A 成员事实）、PeeringDB（A 自报数据需时间戳）、DCD/Developing Telecoms（B）、Baxtel/Data Center Map/Cloudscene/datacenters.com/hostings.info/2GIS（C，仅发现与别名）、Khovar/Asia-Plus/Avesta/Sputnik TJ/Ozodi（B；Khovar 引官方决定时可 A-）、Yotta/darya.ai（A 合作/路线图自述，建设状态需另证）。
- **关键提醒**：塔吉克斯坦市场小，单一项目会被多个目录重复收录。必须先归并同名、同地区、同业主、同电源的条目，再决定是否是一个物理设施、多个阶段，或目录重复。运营商自用机房与商业 DC 分开；ASN/peering 单独出现不计为 DC；CDN/cache 参与者不代表独立数据中心；本地主机商需公司官网、业务条款、地址、电力/运营商或客户证据才能进入设施表。
- **验证与分级规则**：1) 先判物理设施——项目名、地点、业主、设施类型、状态、容量、电力来源分别取证；不要把 IXP、租户、云服务、运营商技术站点重复计为多座 DC；2) 状态严控——Design Documents、MOU、strategic collaboration、roadmap、directory listing 都不是运营证据；3) Darvoz 专项——记录为 RRP，优先找供电/水电站、建设许可、采购、现场照片、服务上线页，2 MW 起步和 100 MW 扩展按公司自述路线图保留，未交叉验证前不进已投产容量；4) Smart City 专项——Uptime entry 是强线索，必须补查 Dushanbe municipality、Smart City SUE、采购/验收和 Uptime award type，避免把设计认证误写为建成 Tier III；5) 矿场/HPC 分离——若客户只做自用挖矿或算力，不提供第三方托管/云服务，类型标 `mining/HPC`，电力 MW 不等于 IT load；6) 云区域——只接受厂商官方 global infrastructure/regions 页面，合作伙伴云、本地 reseller、edge/cache 另列服务可用性；7) 行政边界——Dushanbe 与 RRP/Rudaki/Hisor/Darvoz 分开，GBAO 只含自治州，Darvoz 不在 GBAO；8) 来源拆分——地址 2GIS=C、认证 Uptime=A、容量公司路线图=A 或 C、状态媒体=B。推荐输出备注：`operator official`, `Uptime design certification`, `IXP`, `colocation service`, `government agreement`, `company roadmap`, `trade press`, `directory only`, `mining/HPC`, `tenant/PoP`, `MOU only`。

## 维护注意（更新纪律）

- 不删除/移动任何既有文件；双 explorer 文件是 codex 审核定稿，SKILL.md 忠实提炼其内容，细则差异以 explorer 原文件为准。
- A 级只覆盖来源实际陈述的事实（MOU ≠ 设施建成；Design Documents 认证 ≠ 建成认证）；状态词精确分层，容量分层记录（投产 IT MW > 已签供电 MW > 路线图 MW）。
- 每次枚举复核官方云区域页（AWS/Azure/GCP/OCI/Yandex/Huawei/Alibaba）；目录和媒体不得把计划、MOU、路线图直接升级为运营设施。
- 覆盖必须包含 manifest 五单元并记录负向结论；Darvoz 属 RRP 不属 GBAO；任何 landing station 条目均按错误或跨境陆缆节点重查。
