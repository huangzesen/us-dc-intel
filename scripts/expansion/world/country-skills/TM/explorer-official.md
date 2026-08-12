# TM（土库曼斯坦）Explorer — 官方 / 监管 / 能源方法学

# TM Explorer — Official / Regulatory / Energy Methodology

- 日期（Date）：2026-08-12
- 国家（Country）：Turkmenistan / Türkmenistan / Туркменистан（TM）
- 清单来源（Manifest）：`world-manifest.jsonl` 第 172 行 — `subnational_type: region/city`，`divisions = ["Ahal","Balkan","Dashoguz","Lebap","Mary","Ashgabat"]`
- 行政区覆盖（Division coverage）：完整覆盖 6 个桶（5 州 + Ashgabat 首都城市桶）：Ahal、Balkan、Dashoguz、Lebap、Mary、Ashgabat
- 语言说明：中文为主、英/俄/土库曼语术语为辅（Chinese-primary bilingual）；查询串保留原始语言。

---

## 0. 数据可用性约束（TM 特有）— Data Availability Constraints

土库曼斯坦的数据中心枚举必须以“少量官方来源 + 严格状态动词”运行，不应套用开放市场国家的方法。

1. **信息环境高度封闭**：Freedom House 2025 将 Turkmenistan 评为 Not Free，国家页显示总分 1/100，互联网自由未单独跟踪；境内外访问政府站、媒体站和搜索结果都可能不稳定。来源：`https://freedomhouse.org/country/turkmenistan`
2. **官方信息集中**：国家门户 `turkmenistan.gov.tm`、TDH 国家通讯社 `tdh.gov.tm`、部委/国企官网是设施证据主线。Turkmenportal、Business Turkmenistan、ORIENT、Arzuw News 多数为国家对齐媒体，只能作为 B 级补充。
3. **无公开设施登记**：未发现公开规划许可库、数据中心许可库、能源接入队列、地籍/土地划拨查询库或统一公共数据中心清单。
4. **采购透明度有限**：公开资料显示财政部/财政经济体系负责采购；第三方采购资料承认 Turkmenistan 没有成熟统一的全国电子采购平台。采购公告可作 B/C 级线索，不等于设施存在。
5. **域名与机构名称会变**：本次核验确认 `mincom.gov.tm`、`telecom.tm`、`minenergo.gov.tm` 可用；旧域名（如 `tmtelecom.tm`、`minenergy.gov.tm`）保留为历史搜索线索，不作为当前官方入口。
6. **状态混报常见**：官方报道常把政策、论坛、MoU、开工、启用放在同一语境。必须单独记录 `planned / signed / under construction / opened / operational`，不能把 MoU 或论坛发言计为建成。
7. **地图证据弱**：Google Maps、OSM、2GIS/Yandex 覆盖和更新频率有限；地图点位最多 C 级，不能单独支持设施入册。
8. **语言要求**：俄语命中率通常最高，土库曼语补充本地实体名，英语用于官方英文页和国际媒体。所有关键查询至少跑 RU + EN，重要项目补 TK。

---

## 1. 官方主干（National Official Backbone）

### 1.1 政府门户与国家通讯社

| 来源 | 已核验 URL | 用途 | 可靠度 |
|---|---|---|---|
| 国家门户 / Golden Age / Altyn Asyr | https://turkmenistan.gov.tm | 总统令、内阁会议、部委政策、官方项目报道 | A |
| TDH 国家通讯社 | https://tdh.gov.tm | 官方新闻、启用/开工/签约仪式、政策报道 | A |
| 阿什哈巴德市政府 | https://ashgabat.gov.tm | 首都公告、城市项目；可达性需每轮复检 | A- |
| Arkadag 市官网 | https://arkadag-shaheri.gov.tm | Ahal/Arkadag 智慧城市、数字服务、城市设施线索 | A- |
| 外交部“政府网站”清单 | https://tmembassy.gov.tm/en/websites | 重新确认部委/机构入口，尤其通信主管部门 | A- |

已核验证据锚点：

- `turkmenistan.gov.tm/en/post/63237/meeting-cabinet-ministers-turkmenistan-28`：内阁会议报道提到创建 single Information Center / Data Center，并称 Türkmenaragatnaşyk agency 为数字经济授权机构。
- `tdh.gov.tm/ru/post/19534/...` 与 `turkmenistan.gov.tm/en/post/13192/...`：均把国家 Data Centre 描述为“计划开设/创建”的存储处理、服务器/网络设备放置和互联网接入中心。
- `turkmenistan.gov.tm/en/post/13270/...`：总统提出需开设 National Data Centre；这是政策/计划证据，不是已建成证据。

官方查询模板：

```text
site:turkmenistan.gov.tm "data center" OR "Data Center" OR "National data centre"
site:turkmenistan.gov.tm "центр обработки данных" OR "Дата-центр" OR "ЦОД"
site:turkmenistan.gov.tm "single Information Center" OR "единый информационный центр"
site:tdh.gov.tm "дата-центр" OR "центр обработки данных" OR "ЦОД"
site:tdh.gov.tm "введён в эксплуатацию" "дата-центр" OR "центр обработки данных"
site:ashgabat.gov.tm "дата-центр" OR "сервер" OR "цифров"
site:arkadag-shaheri.gov.tm "digital" OR "санлы" OR "цифров" OR "сервер"
"Туркменистан" "национальный дата-центр"
"Türkmenistan" "maglumat merkezi" OR "serwer"
```

### 1.2 通信 / ICT 主管部门（Regulator / Ministry）

- 本次核验确认 **Türkmenistanyň Aragatnaşyk ministrligi / Ministry Communications of Turkmenistan** 官网为 `https://mincom.gov.tm/`，页脚列出地址 Ashgabat, Archabil Avenue 88，邮箱 `mincom@sanly.tm`，并列出 `TURKMENTELEKOM`、`Turkmenpochta`、`TMCELL`、`ACTN` 等下属/关联机构。
- 外交部政府网站清单仍列出 `«TÜRKMENARAGATNAŞYK» AGENCY http://www.mincom.gov.tm/ru`，说明机构名/英文译名可能在 Ministry 与 Agency 之间混用。枚举时以页面标题和当日政府网站清单为准。
- 未发现独立电信监管机构或公开许可证数据库；电信牌照、频谱、号码资源不应被推断为数据中心设施。
- `sanly.tm` 出现在官方邮箱中，可作为数字政府相关实体/域名线索，但域名本身不是设施证据。

监管查询模板：

```text
site:mincom.gov.tm "data center" OR "дата-центр" OR "центр обработки данных" OR "ЦОД"
site:mincom.gov.tm "сервер" OR "хостинг" OR "hosting" OR "maglumat merkezi"
site:mincom.gov.tm "TURKMENTELEKOM" OR "Türkmentelekom" OR "Туркментелеком"
site:turkmenistan.gov.tm "Türkmenaragatnaşyk" OR "Туркменарагатнашык" OR "Ministry Communications"
site:turkmenistan.gov.tm "цифровая экономика" "Türkmenaragatnaşyk"
"Туркменистан" "лицензия" "оператор связи" "дата-центр"
"Türkmenistan" "aragatnaşyk" "lisenziýa" "maglumat"
```

### 1.3 Turkmentelekom / 国营电信

- 本次核验确认 **Türkmentelekom / Turkmentelekom** 官方站为 `https://telecom.tm/`。
- 官方 hosting 页 `https://telecom.tm/en/hosting/` 可访问，列出 hosting 服务、Physical Server 产品、价格、技术支持和地址 `Ashgabat c., Archabil pr., 88 h.`；这是运营商官方服务证据（A），但页面没有公开机房名称、Tier、IT MW 或精确设施地址，不能据此生成多个设施。
- 旧查询中的 `tmtelecom.tm` 容易误命中 Malaysia Telekom 等无关 “TM Global”。当前方法学应以 `telecom.tm` 为主，`tmtelecom.tm` 仅作历史域名/误拼排除。
- AS/BGP、IP WHOIS、DNS 记录只能用于运营商归属或网络存在性验证，不是数据中心设施证据。

运营商查询模板：

```text
site:telecom.tm "hosting" OR "Physical Server" OR "Host 1"
site:telecom.tm "data center" OR "дата-центр" OR "колокация" OR "хостинг"
site:telecom.tm "maglumat merkezi" OR "serwer" OR "hyzmat"
"Turkmentelekom" OR "Türkmentelekom" "data center" OR "hosting" OR "colocation"
"Туркментелеком" "дата-центр" OR "ЦОД" OR "хостинг" OR "сервер"
"TM CELL" OR "Altyn Asyr" OR "Алтын Асыр" "сервер" OR "дата-центр" OR "5G"
"MTS Turkmenistan" "data center" OR "дата-центр" OR "сервер"
```

### 1.4 电子政务 / 国家数据中心（E-Government / National DC）

- 国家 Data Centre 目前应记录为**政策/计划级单一设施线索**，优先桶为 Ashgabat，除非后续官方页面明确给出其他地点。
- 2018-2022 官方资料多次使用 “planned / necessary to open / steps are being taken to create/launch” 等措辞；本次未核到官方“已启用/投入运营”的公开页面。
- `e.gov.tm` 可通过 Arkadag 市官网数字服务页发现，说明政府服务门户存在；门户服务存在不等于国家数据中心已建成。
- Arkadag（Ahal）是智慧城市/5G/GPON/数字服务高优先线索，但智慧城市 ICT 不等于独立数据中心；需要找机房、数据处理中心、运营商设施或采购/启用证据。

查询模板：

```text
site:turkmenistan.gov.tm "National data centre" "opened" OR "commissioned"
site:turkmenistan.gov.tm "single Information Center" "Data Center"
site:turkmenistan.gov.tm "центр хранения и обработки данных"
site:tdh.gov.tm "национальный Дата-центр" OR "единый центр обработки данных"
site:e.gov.tm "data center" OR "сервер" OR "maglumat merkezi"
site:arkadag-shaheri.gov.tm "5G" OR "GPON" OR "digital service" OR "цифров"
"Arkadag" OR "Аркадаг" "data center" OR "дата-центр" OR "серверная" OR "smart city"
"akylly şäher" "maglumat" OR "serwer" "Arkadag"
```

### 1.5 采购（Procurement）

- 未发现可核验的、统一的全国电子采购门户。第三方 TurkmenistanTenders 页面称公共采购不由类似成熟 eProcurement 的统一全国平台支持；GPPD 将 PPA 记为 Ministry of Finance，并把 tender surface 指向聚合/目录式页面而非政府 e-procurement 系统。
- 采购公告通常应从 TDH、国家门户、国家报刊转载、Turkmenportal/Business Turkmenistan 线索回查。采购类材料最多 B 级，只有后续验收/启用/运营商服务页才能升级。
- 不要把“采购服务器/网络设备”直接计为数据中心；先归为 `telecom core room`、`server room` 或 `government IT procurement` 线索。

采购查询模板：

```text
site:tdh.gov.tm "тендер" OR "закупка" "сервер" OR "оборудование" OR "дата-центр"
site:turkmenistan.gov.tm "тендер" "сервер" OR "центр обработки данных"
site:turkmenportal.com "тендер" "сервер" OR "дата-центр" OR "ЦОД"
site:business.com.tm "tender" "server" OR "data center"
"Туркменистан" "тендер" "серверное оборудование" OR "ЦОД"
"Türkmenistan" "satyn alyş" "serwer" OR "maglumat"
```

---

## 2. 电力 / 电网管线（Energy / Grid Pipeline）

- 本次核验确认 **Türkmenistanyň Energetika ministrligi / Ministry of Energy** 官方站为 `https://minenergo.gov.tm/`；旧 `minenergy.gov.tm` 不应作为当前主 URL。
- 官网说明能源部包括/管理 `Türkmenenergo` 国家电力公司等机构；电网接入技术条件、工业大用户队列、电价目录未发现公开。
- 土库曼斯坦电力以天然气发电为主；官方报道常披露电站 MW、输电线、变电站、出口线路。**电站 MW 不能换算为 DC IT load**。
- 电力证据仅在明确绑定数据中心/服务器设施/数字园区时升级；否则作为区域可行性或背景线索。

能源查询模板：

```text
site:minenergo.gov.tm "дата-центр" OR "data center" OR "сервер" OR "цифров"
site:minenergo.gov.tm "электроснабжение" OR "подстанция" OR "МВт"
site:turkmenistan.gov.tm "электростанция" "Arkadag" OR "Ашхабад" OR "индустриальный"
site:tdh.gov.tm "электроснабжение" "дата-центр" OR "сервер"
"Turkmenenergo" OR "Туркменэнерго" "data center" OR "цифровой" OR "сервер"
"Туркменистан" "дата-центр" "электроэнергия" OR "подстанция"
"Türkmenistan" "maglumat merkezi" "elektrik" OR "energiýa"
```

---

## 3. 云区域页面（Cloud Region Pages）

每轮枚举必须以官方云页面复检，并把“无 TM 区域”的核验日期写入运行记录。

| 云厂商 | 官方页面 | 本次 TM 结论 |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | 页面列 AWS 全球 Region/AZ；未列 Turkmenistan |
| Microsoft Azure | https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/ | 未列 Turkmenistan geography/region |
| Google Cloud | https://cloud.google.com/about/locations | 未列 Turkmenistan location/region |
| Oracle Cloud | https://www.oracle.com/cloud/public-cloud-regions/ | 未列 Turkmenistan public cloud region |
| Yandex Cloud | https://yandex.cloud/en/docs/overview/concepts/region | 2026-08-05 文档仅列 Russia、Kazakhstan；无 TM |
| Alibaba Cloud | https://www.alibabacloud.com/global-locations | 全球区域清单未列 TM；中东最近为 UAE/SAU，亚洲不含 TM |

规则：云厂商会面、论坛演讲、MoU、CDN 节点或邻国区域不是 TM 云区域或数据中心设施。

云查询模板：

```text
site:aws.amazon.com Turkmenistan "region" OR "Local Zone"
site:azure.microsoft.com Turkmenistan "geography" OR "region"
site:cloud.google.com Turkmenistan "locations" OR "region"
site:oracle.com Turkmenistan "cloud region"
site:yandex.cloud Turkmenistan "region" OR "Ashgabat"
site:alibabacloud.com Turkmenistan "region" OR "data center"
"Turkmenistan" "cloud region" "AWS" OR "Azure" OR "Google" OR "Oracle" OR "Alibaba" OR "Yandex"
```

---

## 4. 可靠度分级（Reliability Grades）

| 级别 | TM 枚举含义 |
|---|---|
| **A** | `turkmenistan.gov.tm`、`tdh.gov.tm`、部委/地方政府/国企官网明确给出的法律、决议、开工/启用、运营服务页；`telecom.tm` hosting/设施页；云厂商官方区域页；Uptime Institute 官方认证页。 |
| **A-** | 官方域名但内容为一般城市/数字服务介绍，或未给出设施名称/状态/地点；可支持背景和实体存在，不能单独支持容量或设施计数。 |
| **B** | Business Turkmenistan、Turkmenportal、ORIENT、Arzuw、Times of Central Asia、Trend.az、Caspian News、DCD 等引用具名政府/运营商/厂商的报道；Bitdeer/华为/ZTE 官方或论坛材料中的探索/MoU。 |
| **C** | 数据中心目录、地图、BGP/WHOIS、社交媒体、会议议程、聚合采购站、营销页面、无来源投资文章。只作发现，不计数。 |

容量与状态规则：

- 设施存在、位置、运营主体、状态、容量、认证分别打分。
- `opened / commissioned / введён в эксплуатацию / işe girizildi` 才能支持 operational 或 commissioned。
- `planned / necessary to open / steps are being taken / MoU / explores` 只支持 planned 或 prospect。
- 电站 MW、建筑总面积、城市 ICT 投资额不得填入 `capacity_value` 的 IT load。

---

## 5. 六大行政区官方策略（Per-Division Official Strategy）

| 行政区 | 别名（TK / RU / EN） | 官方表面 | DC 关注点 | 预期产出 |
|---|---|---|---|---|
| **Ahal** | Ahal welaýaty / Ахалский велаят；Arkadag şäheri / город Аркадаг | `turkmenistan.gov.tm`、TDH、`arkadag-shaheri.gov.tm` | Arkadag 智慧城市、5G/GPON、数字服务、Ahal 首府迁移后的政府 ICT；目前不是独立 DC 证据 | 高 |
| **Balkan** | Balkan welaýaty / Балканский велаят；Türkmenbaşy / Туркменбашы；Balkanabat | 国家门户、TDH、能源/港口报道 | 里海港口、油气、跨里海光纤潜在登陆点；无已核官方 DC | 低—中 |
| **Dashoguz** | Daşoguz welaýaty / Дашогузский велаят；Daşoguz / Дашогуз | 国家门户、TDH、运营商区域服务 | 区域通信机房/移动节点；无已核独立 DC | 低 |
| **Lebap** | Lebap welaýaty / Лебапский велаят；Türkmenabat / Туркменабат | 国家门户、TDH、跨境通信/交通报道 | 乌兹别克/阿富汗方向光纤和口岸 IT；无已核独立 DC | 低—中 |
| **Mary** | Mary welaýaty / Марыйский велаят；Mary / Мары | 国家门户、TDH、能源/气化工报道 | 天然气工业数字化、区域通信机房；无已核独立 DC | 低 |
| **Ashgabat** | Aşgabat / Ашхабад / Ashgabat | `ashgabat.gov.tm`、国家门户、TDH、`mincom.gov.tm`、`telecom.tm` | Turkmentelekom hosting/核心网、国家 Data Centre 计划、移动核心网、政府 IT | 最高 |

每区查询模板（替换 `{div}`、`{div_ru}`、`{city}`、`{city_ru}`）：

```text
site:turkmenistan.gov.tm "{div_ru}" "дата-центр" OR "ЦОД" OR "сервер" OR "цифров"
site:tdh.gov.tm "{div_ru}" "центр обработки данных" OR "дата-центр" OR "сервер"
site:mincom.gov.tm "{city_ru}" "сервер" OR "хостинг" OR "интернет"
"{div_ru}" "центр обработки данных" OR "дата-центр" "МВт"
"{div}" "maglumat merkezi" OR "serwer" OR "sanly"
"{city_ru}" "серверная" OR "телекоммуникационный узел" OR "ЦОД"
```

状态动词（TK/RU/EN）：

- 规划：rejalasdyrylýar / планируется / planned
- 探索/MoU：öwrenýär, memorandum / изучает, меморандум / explores, MoU
- 开工：gurluşyk başlandy / началось строительство / construction began
- 启用：açyldy, işe girizildi / открыт, введён в эксплуатацию / opened, commissioned
- 运营：işleýär / работает, действует / operational

---

## 6. 状态与证据规则（Status and Evidence Rules）

| 证据 | 枚举状态 |
|---|---|
| `telecom.tm` hosting/设施页，仅有服务器/hosting 服务，无机房详情 | 运营商 hosting 服务；不自动拆成设施 |
| 官方门户/TDH 报道“planned / necessary to open / steps are being taken” | planned / policy-backed lead |
| 官方门户/TDH 报道“opened / commissioned / введён в эксплуатацию” | commissioned 或 operational，按原文动词记录 |
| 云厂商官方区域页列出 TM | cloud region exists；当前预期无 |
| Uptime 国家页列出 TM 项目 | certification exists；当前需逐轮检查，未核到具体 TM award 条目 |
| 能源部/电站 MW 报道 | power context；不能填 IT load |
| Bitdeer/华为/ZTE MoU 或论坛发言 | B/C prospect，除非有官方土地、电网、开工或启用证据 |

---

## 7. 本次已核验 URL（Verified Source Set）

```text
https://turkmenistan.gov.tm
https://tdh.gov.tm
https://ashgabat.gov.tm
https://arkadag-shaheri.gov.tm
https://tmembassy.gov.tm/en/websites
https://mincom.gov.tm
https://telecom.tm
https://telecom.tm/en/hosting/
https://minenergo.gov.tm
https://freedomhouse.org/country/turkmenistan
https://uptimeinstitute.com/uptime-institute-awards/country/id/TM
https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/
https://cloud.google.com/about/locations
https://www.oracle.com/cloud/public-cloud-regions/
https://yandex.cloud/en/docs/overview/concepts/region
https://www.alibabacloud.com/global-locations
```
