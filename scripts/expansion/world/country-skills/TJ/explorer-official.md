# TJ Explorer — Official/Regulatory/Cloud Pipeline（塔吉克斯坦数据中心 官方/监管/电力/采购/云区域 枚举方法论）

最后核验（Live pass）：2026-08-12。范围：面向塔吉克斯坦（Tajikistan / Ҷумҳурии Тоҷикистон）数据中心、AI/HPC 设施、政府/运营商机房、IXP 与云区域的官方口径发现方法。优先使用政府、监管、电力、采购、运营商官方、认证机构与云厂商官方页面；行业媒体只作补充线索。

可靠性分级（Reliability grades）：**A** = 官方/一手来源（政府/监管/采购/电力/运营商官方、Uptime Institute、云厂商官方）；**B** = 可信行业媒体、国家通讯社、开发银行/国际组织、监管邻近来源；**C** = 目录、地图、聚合器、营销页；**U** = 无法核实或来源不支持的主张。**A 级只覆盖来源实际陈述的事实**：例如 MOU 页面只证明「协议已签」，不能证明「设施已建成」。

---

## 0. 结构事实（行政区、登记、法律）

### 0.1 行政区划（5 个覆盖单元；已按 world-manifest.jsonl 核对）

Manifest entry：`TJ / Tajikistan / capital territory/autonomous region/region/districts under republic administration`，divisions = `Dushanbe`, `Gorno-Badakhshan`, `Khatlon`, `districts under government jurisdiction`, `Sughd`。

| Division（manifest 精确值） | Русский | Тоҷикӣ | 类型/行政中心 | 枚举注意 |
|---|---|---|---|---|
| Dushanbe | Душанбе | Душанбе | 首都、共和国直辖市 | 不归入任何州；与周边 Rudaki/Hisor 等 RRP 区分 |
| Gorno-Badakhshan | Горно-Бадахшанская автономная область / ГБАО | Вилояти Мухтори Кӯҳистони Бадахшон | 自治州；中心 Хорог / Хоруғ | Pamir Energy 供电区；Darvoz 不在 GBAO，勿误归类 |
| Khatlon | Хатлонская область | Вилояти Хатлон | 州；中心 Бохтар，另含 Куляб | Danghara/Kulob/Panj SEZ 与边境贸易线索 |
| districts under government jurisdiction | Районы республиканского подчинения / РРП | Ноҳияҳои тобеи ҷумҳурӣ | 中央直辖区；含 Hisor、Tursunzoda、Vahdat、Yavan、Rudaki、Rasht、Darvoz 等 | 杜尚别近郊、能源敏感型项目、Darvoz AI DC 均优先检查本单元 |
| Sughd | Согдийская область | Вилояти Суғд | 州；中心 Худжанд / Хуҷанд | Khujand、Buston/SEZ Sughd、北部矿场/电信局房线索 |

塔吉克斯坦为内陆国，无海底光缆登陆站；任何 `landing station` 条目均应作为错误或跨境陆缆节点重查。行政边界不要按营销口径的「大杜尚别」自动归并。

### 0.2 已核验的官方门户与制度面

- **总统**：https://www.president.tj/ 。数字经济、AI、投资签约和基础设施项目的一手新闻源。
- **政府/电子政务目录**：https://egov.tj/ 。已核验可列示机构页面，包括 Communications Service、Public Procurement Agency、Agency of Innovation and Digital Technologies。
- **通信监管机构**：Communications Service under the Government of RT，当前可用官网为 https://cs.gov.tj/ ，egov 目录仍列 http://khadamotialoqa.tj/；旧草稿中的 `sps.tj` 不作为主入口，除非后续重定向或恢复。
- **采购**：采购主管机构页面在 egov.tj；可检索采购公告的实际门户为 https://eprocurement.gov.tj/ ，旧/登录系统 `zakupki.gov.tj` 与 `cabinet.zakupki.gov.tj` 仍作交叉入口。`eprocurement.gov.tj` 可能响应慢，搜索引擎 `site:eprocurement.gov.tj` 必须并用。
- **法律法规库**：https://www.mmk.tj/ 已核验可访问；用于通信法、个人数据法、采购法、数字资产/AI/数字经济政策文本核查。
- **投资委员会**：https://investcom.tj/ 已核验可访问；`https://www.investcom.tj/` 证书主机名不匹配，方法中使用无 `www` 版本。
- **创新与数字技术署**：egov 机构页 https://egov.tj/site/innovation?lang=en 已核验；联系人域显示 `innovation.tj`，部门链接使用 `edavlat.tj`。另有 https://www.uidt.tj/ 页面与数字技术/创新教育机构相关，不能直接替代总统直属署，使用前确认页面主体。
- **电力**：Barqi Tojik 官网 http://www.barqitojik.tj/ 已核验可访问；其 HTTPS 证书可能过期。IEA/OECD 文件确认 Barki Tojik 供电范围不含 GBAO，GBAO 由 Pamir Energy 供电。
- **Tojiktelecom**：https://tojiktelecom.tj/ 已核验；官方 about 页列出互联网、电话、数字电视服务及牌照；TJ-IX 服务页列示 peering 与设备放置/colocation 能力。

### 0.3 法律/政策核查清单

使用 mmk.tj / president.tj / egov.tj 核查现行文本和日期：

- `Закон РТ «О связи»` / Law on Communications：运营商许可、互联互通、监管执法背景。
- `Закон РТ «О защите персональных данных»` / Personal Data Protection Law No.1537, 2018：数据托管、政府云和跨境处理合规背景。
- `Закон РТ «О государственных закупках товаров, работ и услуг»`：采购公告/合同作为 A 级证据的法律基础。
- 数字资产、AI、数字经济、电子政务相关法令与战略：先查 president.tj、egov.tj、mmk.tj；2025-2030 已被官方口径表述为数字经济与创新发展周期，需用具体法令/计划文本支撑。

---

## 1. 搜索词汇（俄语优先，塔吉克语补强，英语用于国际厂商/投资）

- 英语：`data center`, `data centre`, `AI data center`, `green AI data center`, `HPC`, `GPU cluster`, `colocation`, `hosting`, `cloud`, `cloud region`, `internet exchange`, `IXP`, `CDN`, `digital public infrastructure`, `sovereign cloud`, `Smart City Data Center`。
- 俄语：`дата-центр`, `датацентр`, `центр обработки данных`, `ЦОД`, `серверная`, `серверное оборудование`, `колокация`, `размещение оборудования`, `хостинг`, `облачные услуги`, `облачная инфраструктура`, `точка обмена трафиком`, `пиринг`, `майнинг`, `майнинг-ферма`, `высокопроизводительные вычисления`, `искусственный интеллект`, `графический процессор`, `введён в эксплуатацию`, `строительство`, `меморандум`, `электроснабжение`, `технические условия`。
- 塔吉克语：`маркази додаҳо`, `маркази коркарди додаҳо`, `сервер`, `таҷҳизоти серверӣ`, `хостинг`, `абрӣ`, `интернет`, `табодули трафик`, `зеҳни сунъӣ`, `рақамикунонӣ`, `иқтисодиёти рақамӣ`, `хариди давлатӣ`, `сохтмон`, `ба истифода дода шуд`。

---

## 2. 官方/监管管线

### 2.1 通信监管与运营商许可

主入口：https://cs.gov.tj/ 和 egov 机构目录 `site:egov.tj/site/aloka-tj`。用途：

- 许可运营商名单、监管统计、公告 = **A 级公司/许可事实**。
- 许可不能证明某公司拥有商业数据中心；仅证明其具备相应通信服务资格。
- 搜索时保留历史名称：`Служба связи при Правительстве РТ`, `Хадамоти алоқа`, `khadamotialoqa.tj`, `Агентство связи при Правительстве РТ`。

### 2.2 总统、政府、数字技术与投资促进

- `site:president.tj`：国家 AI、数字经济、Smart City、外国 ICT 合作、数据中心投产/开工。
- `site:egov.tj`：机构目录、电子政府、数字公共服务、采购主管机构。
- `site:investcom.tj`：投资协议、自由经济区、项目介绍。MOU/协议只给「意图/合作」A；建设/投产需另证。
- `site:khovar.tj`：国家通讯社。若全文引用官方会议/总统/政府决定，可作 A-；普通报道按 B。
- `site:stat.tj`：统计署和政策转载；可作为数字经济官方政策线索。

### 2.3 电力/电网管线

- **Barqi Tojik**：http://www.barqitojik.tj/ 。核查供电可靠性、限电、大用户接入、发电/配电项目。HTTPS 证书异常时使用 HTTP。
- **能源与水资源部**：http://www.minenergo.tj/ 。核查电价、能源密集型负载、矿场限制和大负荷政策。
- **Pamir Energy / GBAO**：Pamir Energy 为 Gorno-Badakhshan 电力特例；IEA/OECD 已确认 Barki Tojik 供电范围不含 GBAO。GBAO 项目须使用 Pamir Energy、AKDN/IFC/World Bank 或地方政府交叉确认。
- **大功率判定规则**：任何 MW 级数据中心、AI/HPC 或矿场声明，至少交叉检查电源位置、并网/供电协议、电价类别、季节性限电影响。无电力证据时不得把远期 MW 路线图记为已投产容量。

### 2.4 政府采购管线

主入口：https://eprocurement.gov.tj/ru/searchanno；辅助入口：`zakupki.gov.tj`, `cabinet.zakupki.gov.tj/auth`, egov 采购机构页。检索词：

```text
site:eprocurement.gov.tj "ЦОД"
site:eprocurement.gov.tj "центр обработки данных"
site:eprocurement.gov.tj "дата-центр"
site:eprocurement.gov.tj "серверное оборудование"
site:eprocurement.gov.tj "система хранения данных"
site:eprocurement.gov.tj "облачные услуги"
site:eprocurement.gov.tj "хостинг"
site:eprocurement.gov.tj "таҷҳизоти серверӣ"
site:zakupki.gov.tj "ЦОД"
site:zakupki.gov.tj "серверное оборудование"
```

采购记录 = **A 级采购事实**，但只覆盖标段/中标/采购人/日期/金额/技术要求。若标的是服务器或存储设备，除非出现建设、机房、ЦОД、托管、运维合同等字段，不自动计为数据中心设施。

### 2.5 云区域官方页面（每次枚举复检）

官方区域页已在 2026-08-12 live pass 复查：AWS、Azure、Google Cloud、Oracle Cloud 官方全球区域页均未显示 Tajikistan/TJ 公共云区域。任何「塔吉克斯坦 AWS/Azure/GCP/OCI region」主张必须以厂商官方区域页为准。邻近区域或合作伙伴云可记录为服务可用性，不计为 TJ 本土 hyperscale region。

核查入口：

- AWS：https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure：https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies
- Google Cloud：https://cloud.google.com/about/locations
- Oracle Cloud：https://www.oracle.com/cloud/public-cloud-regions/
- Yandex Cloud：https://yandex.cloud/en/docs/overview/concepts/region
- Huawei Cloud / Alibaba Cloud：使用厂商官方 regions/locations 页；本地代理商营销页只能作 C。

---

## 3. 查询模板（官方管线）

```text
site:president.tj "центр обработки данных"
site:president.tj "дата-центр"
site:president.tj "искусственный интеллект" "центр"
site:president.tj "Darya" "Yotta"
site:president.tj "Smart City Data Center"
site:egov.tj "центр обработки данных"
site:egov.tj "цифровая инфраструктура"
site:cs.gov.tj "лиценз" "оператор"
site:cs.gov.tj "центр обработки данных"
site:mmk.tj "О связи"
site:mmk.tj "персональных данных"
site:mmk.tj "цифровых актив"
site:khovar.tj "центр обработки данных"
site:khovar.tj "дата-центр"
site:khovar.tj "зеҳни сунъӣ"
site:investcom.tj "data center"
site:investcom.tj "центр обработки данных"
site:eprocurement.gov.tj "ЦОД"
site:eprocurement.gov.tj "серверное оборудование"
site:barqitojik.tj "майнинг"
site:barqitojik.tj "электроснабжение" "потребитель"
site:minenergo.tj "майнинг" "электроэнергия"
site:tojiktelecom.tj "TJ-IX"
site:tojiktelecom.tj "colocation"
site:tojiktelecom.tj "размещение оборудования"
"Таджикистан" "центр обработки данных" "введён в эксплуатацию"
"Таджикистан" "дата-центр" "меморандум"
"Dushanbe State Unitary Enterprise Smart City Data Center"
"Darvoz" "AI data center" "Tajikistan"
"Darya.ai" "Yotta" "Darvoz"
```

---

## 4. 按行政区枚举方法与现实预期

| Division | 锚点（RU/TJ/EN） | 官方/监管路径 | 现实预期 |
|---|---|---|---|
| Dushanbe | Душанбе / Dushanbe | president.tj、egov.tj、eprocurement、cs.gov.tj、Tojiktelecom、TJ-IX、Uptime、Smart City/municipal sources | 最高：Smart City Data Center、TJ-IX、Tojiktelecom/运营商托管、政府/银行机房 |
| Gorno-Badakhshan | ГБАО, Хорог/Хоруғ | Pamir Energy、AKDN/World Bank/IEA、GBAO/Хорог 地方政府、对华口岸数字化 | 很低：边缘/灾备/政务机房；注意 Darvoz 不属于 GBAO |
| Khatlon | Хатлон, Бохтар, Куляб/Кӯлоб, Данғара | 州政府、SEZ Danghara/Kulob/Panj、eprocurement、Barqi Tojik/能源部 | 低：区域电信局房、政府机房、矿场/工业负载 |
| districts under government jurisdiction | РРП, Дарвоз, Гиссар/Ҳисор, Турсунзода, Яван/Ёвон, Вахдат, Рудаки | 区政府、Barqi Tojik、investcom、president.tj、darya/Yotta 项目线索 | 低-中：杜尚别近郊与 Darvoz AI/HPC 项目；高功率项目需严查供电 |
| Sughd | Сугд, Худжанд/Хуҷанд, Бустон, Истаравшан, Исфара | 州政府、SEZ Sughd、eprocurement、能源部/Barqi Tojik、运营商区域节点 | 低-中：Khujand 电信局房、SEZ IT、矿场/能源密集型项目 |

行政区模板：

```text
"{division_ru}" "{city_ru}" "центр обработки данных"
"{division_ru}" "{city_ru}" "дата-центр"
"{division_ru}" "{city_ru}" "серверная"
"{division_ru}" "{city_ru}" "хостинг"
"{division_tg}" "{city_tg}" "маркази коркарди додаҳо"
"{city_ru}" "майнинг" "электроэнергия"
"{city_ru}" "ферма" "электроэнергия"
site:eprocurement.gov.tj "{city_ru}" "сервер"
site:khovar.tj "{city_ru}" "рақамикунонӣ"
```

---

## 5. 已核验项目/线索与证据状态

| # | 名称/项目 | 行政区 | 当前状态 | 证据与分级 |
|---|---|---|---|---|
| 1 | **Dushanbe State Unitary Enterprise Smart City Data Center** | Dushanbe | Uptime Institute 已列项目；至少有 Tier III Certification of Design Documents 线索，是否建成/投运需另证 | Uptime Institute client/country page = A（认证/项目名/地点/认证类型）；不要把 Design Documents 认证等同于 constructed facility |
| 2 | **TJ-IX Dushanbe** | Dushanbe | 运营中 IXP | PeeringDB ix/4728 显示 TJ-IX、Dushanbe、Tojiktelecom、16 peers/610G、2026-01-25 更新 = A；Tojiktelecom TJ-IX 服务页 = A（服务与设备放置/colocation 能力） |
| 3 | **Tojiktelecom colocation / technology sites** | Dushanbe + 全国局房 | 服务存在；设施级地址/规格需另证 | Tojiktelecom TJ-IX 页面提到在 Tojiktelecom 技术站点放置设备（colocation）= A（服务能力）；具体物理 DC/机架/MW 未公开 = U/C |
| 4 | **darya.ai / Yotta Darvoz green AI data center** | districts under government jurisdiction（Darvoz） | 2025-10-25 战略合作/计划；darya 页面称当前项目、2 MW 起步、最高 100 MW 路线图；投产/建设状态需电力和现场证据 | Yotta 官方新闻稿 = A（合作签署/意向）； darya.ai 官网 = A（公司自述路线图）；DCD/Developing Telecoms = B；Baxtel = C。未见政府供电/施工/验收前不要计为 fully operational |
| 5 | **Darya AI center (Zev)** | 待定位，可能 Darvoz/水电点 | 目录线索；需官方或现场佐证 | Baxtel 列 2 个 darya.ai 条目 = C；不得单独计数，除非确认不是 Darvoz 同一项目/阶段 |
| 6 | **国家 ЦОД / 统一数据处理中心** | Dushanbe 待确认 | 政策/电子政务线索；需采购、Uptime、验收或运营页确认 | president.tj、egov.tj、eprocurement、Uptime Smart City 项目交叉核查；无直接来源时 U |
| 7 | **加密矿场 / mining-HPC** | Sughd、Khatlon、RRP 最可能 | 独立类别，不默认商业 DC | 能源部、Barqi Tojik、执法/媒体可支持监管或用电事实；除非有第三方托管/云客户，标 `mining/HPC` |
| 8 | **公共云区域** | — | AWS/Azure/GCP/OCI 官方页无 TJ 区域 | 云厂商官方区域页 = A（无 TJ 区域）；本地经销/伙伴云只作服务线索 |

---

## 6. 可靠性与覆盖规则

- 官方/认证来源优先：Uptime、PeeringDB、Tojiktelecom、cs.gov.tj、eprocurement、president.tj、egov.tj、mmk.tj、Barqi Tojik/Pamir Energy。
- 状态词必须精确：`signed`/`меморандум` = 意向；`construction began`/`началось строительство` = 建设；`commissioned`/`введён в эксплуатацию` = 投产；Uptime `Design Documents` = 设计认证，不是建成认证。
- 容量必须分层：已投产 IT MW > 已签供电/并网 MW > 路线图/远期 MW。darya 2 MW/100 MW 目前按公司自述路线图处理。
- 物理设施与服务商分开：IXP、运营商、云服务、租户和物理机房分别建关系，避免 Tojiktelecom/TJ-IX/hoster 重复计数。
- 覆盖必须包含 manifest 五单元；即使预期为零，也要记录已跑查询、无强证据、主要排除理由。

---

## 7. 更新/复检节奏

- **月度**：TJ-IX PeeringDB、Tojiktelecom TJ-IX/colocation 页面、president.tj / khovar.tj / egov.tj 的 AI/DC/数字基础设施检索、eprocurement 新公告。
- **季度**：Uptime Tajikistan country/client page、darya/Yotta Darvoz 状态、电力/供电证据、云厂商官方区域页。
- **半年度**：Communications Service 入口域名与许可统计、投资委/SEZ 项目、Barqi Tojik 与 GBAO/Pamir Energy 供电背景。
- **事件驱动**：总统出席 AI/数据中心活动、签供电协议、开工/竣工/验收、冬季限电或矿场执法。

## 快速 URL 索引

- 总统：https://www.president.tj/ ｜ 电子政务/机构目录：https://egov.tj/
- 通信监管：https://cs.gov.tj/ ｜ 旧/目录域：http://khadamotialoqa.tj/
- 法律法规库：https://www.mmk.tj/
- 采购：https://eprocurement.gov.tj/ ｜ https://zakupki.gov.tj/ ｜ https://cabinet.zakupki.gov.tj/
- 投资委：https://investcom.tj/
- 创新与数字技术署目录：https://egov.tj/site/innovation?lang=en
- 电力：http://www.barqitojik.tj/ ｜ http://www.minenergo.tj/ ｜ Pamir Energy/AKDN/IEA 资料
- Tojiktelecom：https://tojiktelecom.tj/ ｜ TJ-IX：https://tj-ix.tj/ ｜ PeeringDB TJ-IX：https://www.peeringdb.com/ix/4728
- Uptime Tajikistan：https://uptimeinstitute.com/uptime-institute-awards/country/id/TJ
- darya.ai：https://www.greendarya.ai/ ｜ Yotta Darvoz announcement：https://yotta.com/press-releases/darya-ai-and-yotta-data-services-sign-strategic-collaboration-agreement-to-develop-tajikistans-first-green-ai-data-center/
- 云区域：AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ｜ Azure https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies ｜ GCP https://cloud.google.com/about/locations ｜ OCI https://www.oracle.com/cloud/public-cloud-regions/
- 交叉参考：同目录 explorer-industry.md（行业/厂商口径）。
