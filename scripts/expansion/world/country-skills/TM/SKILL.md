---
name: tm-datacenter-methodology
location: scripts/expansion/world/country-skills/TM/SKILL.md
description: 土库曼斯坦数据中心查询方法论（Turkmenistan datacenter discovery & audit methodology）——双线来源（官方/监管/能源管线 + 行业/厂商发现）与 region/city 六桶模型下的设施枚举规则。
---

# TM · 土库曼斯坦数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：在高度封闭的信息环境中枚举土库曼斯坦（Turkmenistan / Türkmenistan / Туркменистан, TM）的数据中心与相关设施。双线方法论：`explorer-official.md`（官方/监管/能源管线）与 `explorer-industry.md`（行业/厂商发现），均为 codex 审核定稿。划分模型（per manifest，world-manifest.jsonl 第 172 行）：**subnational_type: region/city**，divisions = **Ahal、Balkan、Dashoguz、Lebap、Mary、Ashgabat**（5 州 + Ashgabat 首都城市桶，6/6 桶必须逐一跑查询；不要把 Ashgabat 并入 Ahal，也不要把 Arkadag/Ahal 线索误归 Ashgabat）。语言：中文为主、双语（Chinese-primary bilingual），查询串保留 EN/RU/TK 原文。评审日期：2026-08-12。

## 入口

| 入口 | 管线 | 内容 |
|---|---|---|
| `explorer-official.md` | 官方/监管/能源管线 | 数据可用性约束（TM 特有）、官方主干（政府门户/TDH/市政/Arkadag/外交部网站清单）、通信 ICT 主管部门（mincom.gov.tm）、Turkmentelekom（telecom.tm）、电子政务/国家数据中心（政策/计划级单一线索）、采购、电力/电网管线、云区域页面、可靠性分级、六大行政区官方策略、状态与证据规则、已核验 URL |
| `explorer-industry.md` | 行业/厂商发现 | 行业视角数据约束、分级规则（容量/状态层级）、市场分桶、权威行业来源（运营商/认证/云、行业媒体与区域媒体、目录与地图）、国家查询模板（广撒网/源限定扫描/运营商项目扫描/状态容量提取）、枚举矩阵（6 行政区 × 分桶）、当前已知行业信号（不直接计数）、云/超大规模信号、验证与去重规则、输出字段、已核验 URL |

## 核心结构事实

1. **行政区划模型**：region/city，6 个桶：Ahal（别名 Ahal welaýaty/Ахалский велаят；Arkadag şäheri/город Аркадаг）、Balkan（Balkan welaýaty/Балканский велаят；Türkmenbaşy/Туркменбашы；Balkanabat）、Dashoguz（Daşoguz welaýaty/Дашогузский велаят）、Lebap（Lebap welaýaty/Лебапский велаят；Türkmenabat/Туркменабат）、Mary（Mary welaýaty/Марыйский велаят）、Ashgabat（Aşgabat/Ашхабад/Ashgabat）。
2. **数据可用性约束（TM 特有）**：1) 信息环境高度封闭——Freedom House 2025 将 Turkmenistan 评为 Not Free、总分 1/100，境内外交访政府站、媒体站和搜索结果都可能不稳定；2) 官方信息集中——国家门户 `turkmenistan.gov.tm`、TDH 国家通讯社 `tdh.gov.tm`、部委/国企官网是设施证据主线；Turkmenportal、Business Turkmenistan、ORIENT、Arzuw News 多数是国家对齐媒体，只能作 B 级补充；3) 无公开设施登记——未发现公开规划许可库、数据中心许可库、能源接入队列、地籍/土地划拨查询库或统一公共数据中心清单；4) 采购透明度有限——公开资料显示财政部/财政经济体系负责采购，第三方资料承认 TM 没有成熟统一的全囶电子采购平台，采购公告可作 B/C 级线索，不等于设施存在；5) 域名与机构名称会变——本次核验确认 `mincom.gov.tm`、`telecom.tm`、`minenergo.gov.tm` 可用；旧域名（如 `tmtelecom.tm`、`minenergy.gov.tm`）保留为历史检索线索不作当前官方入口；6) 状态混报常见——官方报道常把政策、论坛、MoU、开工、启用放在同一语境，必须单独记录 `planned / signed / under construction / opened / operational`，不能把 MoU 或论坛发言计为建成；7) 地图证据弱——Google Maps、OSM、2GIS/Yandex 覆盖和更新频率有限，地图点位最多 C 级；8) 语言要求——俄语命中率通常最高，土库曼语补充本地实体名，英语用于官方英文页和国际媒体；所有关键查询至少跑 RU + EN，重要项目补 TK。
3. **法律与监管**：**Türkmenistanyň Aragatnaşyk ministrligi / Ministry Communications of Turkmenistan** 官网 `https://mincom.gov.tm/`（页脚地址 Ashgabat, Archabil Avenue 88，邮箱 `mincom@sanly.tm`，列出 TURKMENTELEKOM、Turkmenpochta、TMCELL、ACTN 等下属/关联机构）；外交部政府网站清单仍列出 «TÜRKMENARAGATNAŞYK» AGENCY http://www.mincom.gov.tm/ru——机构名/英文译名可能在 Ministry 与 Agency 之间混用，枚举时以页面标题和当日政府网站清单为准。未发现独立电信监管机构或公开许可证数据库；电信牌照、频谱、号码资源不应被推断为数据中心设施。`sanly.tm` 出现在官方邮箱中可作数字政府相关实体/域名线索，但域名本身不是设施证据。
4. **互联与云**：土库曼斯坦电力以天然气发电为主，官方报道常披露电站 MW、输电线、变电站、出口线路——**电站 MW 不能换算为 DC IT load**；电力证据仅在明确绑定数据中心/服务器设施/数字园区时升级，否则作为区域可行性或背景线索。云区域页面（每轮枚举必须复核，并把「无 TM 区域」的核验日期写入运行记录）：AWS、Microsoft Azure、Google Cloud、Oracle Cloud 均未列 Turkmenistan；Yandex Cloud 2026-08-05 文档仅列 Russia、Kazakhstan，无 TM；Alibaba Cloud 全球区域清单未列 TM（中东最近为 UAE/SAU，亚洲不含 TM）。规则：云厂商会面、论坛演讲、MoU、CDN 节点或邻国区域不是 TM 云区域或数据中心设施。
5. **设施/项目种子**（当前已知行业信号，不直接计数）：**Turkmentelekom hosting**（A-/Ashgabat——官方 hosting 页 `https://telecom.tm/en/hosting/` 列 hosting 服务、Physical Server 产品、价格、技术支持和地址 `Ashgabat c., Archabil pr., 88 h.`，这是运营商官方服务证据 A，但页面没有公开机房名称、Tier、IT MW 或精确设施地址，不能据此生成多个设施；旧查询中的 `tmtelecom.tm` 容易误命中 Malaysia Telekom 等无关 “TM Global”，当前以 `telecom.tm` 为主）；**国家 Data Centre**（A policy lead/Ashgabat——官方 2018-2022 资料多次使用 “planned / necessary to open / steps are being taken to create/launch” 措辞，`turkmenistan.gov.tm/en/post/63237` 提到创建 single Information Center / Data Center 并称 Türkmenaragatnaşyk agency 为数字经济授权机构，`turkmenistan.gov.tm/en/post/13270` 总统提出需开设 National Data Centre——这是政策/计划证据，不是已建成证据；本次未核到官方「已启用/投入运营」的公开页面）；**Arkadag 智慧城市 ICT**（A-/B/Ahal——官方城市站和国家媒体支持 smart/digital city、5G/GPON/数字服务；智慧城市 ICT 不等于独立数据中心，需要找机房、数据处理中心、运营商设施或采购/启用证据）；**Huawei 固网/ICT**（B——DCD TM 标签页列 2023 “Huawei to support Turkmenistan's fixed line telecoms expansion”，作 telecom vendor lead 非 DC）；**Bitdeer / White City Ashgabat**（B/C prospect——Business Turkmenistan 2025 报道 Bitdeer 探索在 TM 建高科技计算中心；News Central Asia 2026 报道 White City Ashgabat 2026 MoU/first data center 说法；除非 Bitdeer IR、政府公告或合同/土地/电力证据确认，不计设施）；**跨里海光纤 / 口岸项目**（Balkan、Lebap 可能受益，除非有登陆站/机房/运营商设施证据，否则只作 connectivity context）。
6. **语言与词汇**：俄语优先、土库曼语补充、英语辅助。核心词：дата-центр、центр обработки данных、ЦОД、серверная、хостинг、облачные услуги、электроэнергия、подстанция、МВт、открыт、введён в эксплуатацию、работает、началось строительство、меморандум；maglumat merkezi、serwer、sanly、hyzmat、açyldy、işe girizildi、işleýär、gurluşyk başlandy、rejalasdyrylýar、öwrenýär；data center、datacenter、hosting、colocation、cloud region、smart city。状态动词语（TK/RU/EN）：规划=rejalasdyrylýar/планируется/planned；探索/MoU=öwrenýär, memorandum/изучает, меморандум/explores, MoU；开工=gurluşyk başlandy/началось строительство/construction began；启用=açyldy, işe girizildi/открыт, введён в эксплуатацию/opened, commissioned；运营=işleýär/работает, действует/operational。
7. **可靠性分级**：A=`turkmenistan.gov.tm`、`tdh.gov.tm`、部委/地方政府/国企官网明确给出的法律、决议、开工/启用、运营服务页；`telecom.tm` hosting/设施页；云厂商官方区域页；Uptime Institute 官方认证页。A-=官方域名但内容为一般城市/数字服务介绍，或未给出设施名称/状态/地点；可支持背景和实体存在，不能单独支持容量或设施计数。B=Business Turkmenistan、Turkmenportal、ORIENT、Arzuw、Times of Central Asia、Trend.az、Caspian News、DCD 等引用具名政府/运营商/厂商的报道；Bitdeer/华为/ZTE 官方或论坛材料中的探索/MoU。C=数据中心目录、地图、BGP/WHOIS、社交媒体、会议议程、聚合采购站、营销页面、无来源投资文章——只作发现，不计数。
8. **计数与去重规则**：设施存在、位置、运营主体、状态、容量、认证分别打分。`opened / commissioned / введён в эксплуатацию / işe girizildi` 才支持 operational 或 commissioned；`planned / necessary to open / steps are being taken / MoU / explores` 只支持 planned 或 prospect；电站 MW、建筑总面积、城市 ICT 投资额不得填入 `capacity_value` 的 IT load。容量字段必须保留容量类型：`it_load`、`facility_power`、`grid_connection`、`generation_capacity`、`unspecified`。不要拆分：1) Turkmentelekom hosting 服务页不得拆成多个设施，没有机房名/地址/容量时只保留一个运营商服务线索；2) 国家 Data Centre 的计划报道、Single Information Center、电子政务平台不得重复计数，除非出现清晰不同物理地点；3) 不要把 Ashgabat 与 Ahal/Arkadag 混桶（Ashgabat 是 manifest 独立 city bucket，Arkadag 属 Ahal）；4) 移动运营商核心网、5G、GPON、卫星、互联网接入升级不是数据中心，除非披露「ЦОД/дата-центр/серверная/центр обработки данных」设施；5) MoU、论坛发言、investment pitch、explores/opportunities 一律按 prospect，升级需要官方土地、电力、合同、开工或启用；6) 目录、地图、SEO 站、采购聚合站不直接计数，必须回运营商、政府、厂商官方或可信媒体；7) 认证字段只接受 Uptime Institute 官方或同等认证机构官方页面；8) 所有记录写 `last_verified_date`，TM 尤其需要保留失败核验（timeout/404/no result）说明。容量层级：官方/运营商 IT MW > Uptime/认证设施规格 > 官方启用报道 > 厂商官方披露 > 行业媒体 > 目录。状态层级：运营服务/启用报道 > 建成/运营认证 > 融资+开工 > 开工仪式 > 土地/许可 > MoU/lease/explores > 政策话语 > 目录。

## 常用查询模板

```text
site:turkmenistan.gov.tm "data center" OR "Data Center" OR "National data centre"
site:turkmenistan.gov.tm "центр обработки данных" OR "Дата-центр" OR "ЦОД"
site:turkmenistan.gov.tm "single Information Center" OR "единый информационный центр"
site:tdh.gov.tm "дата-центр" OR "центр обработки данных" OR "ЦОД"
site:tdh.gov.tm "введён в эксплуатацию" "дата-центр" OR "центр обработки данных"
site:ashgabat.gov.tm "дата-центр" OR "сервер" OR "цифров"
site:arkadag-shaheri.gov.tm "digital" OR "санлы" OR "цифров" OR "сервер"
site:mincom.gov.tm "data center" OR "дата-центр" OR "центр обработки данных" OR "ЦОД"
site:mincom.gov.tm "сервер" OR "хостинг" OR "hosting" OR "maglumat merkezi"
site:telecom.tm "hosting" OR "Physical Server" OR "data center"
site:telecom.tm "дата-центр" OR "колокация" OR "хостинг"
site:minenergo.gov.tm "дата-центр" OR "data center" OR "сервер" OR "цифров"
site:turkmenistan.gov.tm "Национальный дата-центр" OR "единый центр обработки данных"
site:e.gov.tm "data center" OR "сервер" OR "maglumat merkezi"
"Туркменистан" "национальный дата-центр"
"Türkmenistan" "maglumat merkezi" OR "serwer"
"Туркменистан" "дата-центр" "Ашхабад"
"Туркменистан" "серверная" OR "хостинг" "Ашхабад"
"Turkmenistan" "colocation" OR "hosting" "Turkmentelekom"
"Turkmentelekom" OR "Türkmentelekom" OR "Туркментелеком" "дата-центр" OR "ЦОД" OR "хостинг" OR "сервер"
"TM CELL" OR "Altyn Asyr" OR "Алтын Асыр" "сервер" OR "дата-центр" OR "5G"
"Huawei" "Turkmenistan" "fixed line" OR "Arkadag" OR "smart city" OR "data center"
"Bitdeer" "Turkmenistan" "data center" OR "digital infrastructure" OR "White City Ashgabat"
"Транскаспийский" OR "Trans-Caspian" "fiber" OR "оптоволокно" "Turkmenistan"
site:tdh.gov.tm "тендер" OR "закупка" "сервер" OR "оборудование" OR "дата-центр"
site:business.com.tm Turkmenistan "data center" OR "Bitdeer" OR "digital infrastructure"
site:datacenterdynamics.com Turkmenistan "data center" OR "Huawei" OR "telecoms"
site:turkmenportal.com "дата-центр" OR "сервер" OR "ЦОД" OR "Arkadag"
site:orient.tm "дата-центр" OR "цифровизация" OR "сервер"
site:timesca.com Turkmenistan "data center" OR "digital" OR "White City Ashgabat"
site:trend.az Туркменистан "оптоволокно" OR "цифровой" OR "дата-центр"
"умный город" OR "akylly şäher" "Arkadag" "сервер" OR "5G" OR "GPON"
"{project}" "MW" OR "МВт" OR "IT capacity" OR "quwaty"
"{project}" "Tier III" OR "Tier 3" OR "Uptime"
"{project}" "opened" OR "commissioned" OR "введён в эксплуатацию" OR "işe girizildi"
"{project}" "MoU" OR "memorandum" OR "меморандум" OR "explores"
```

每区主查询（替换 `{div}`/`{city}`）：`"{city_ru}" "дата-центр" OR "ЦОД" OR "серверная" OR "телекоммуникационный узел"`；`"{city}" "maglumat merkezi" OR "serwer otagy" OR "aragatnaşyk"`；`"{div_ru}" "цифровизация" OR "информационные технологии" OR "дата-центр"`；`site:turkmenistan.gov.tm "{div_ru}" "дата-центр" OR "ЦОД" OR "сервер" OR "цифров"`。

## 官方/监管管线要点（详见 explorer-official.md）

- **官方主干**：国家门户/Golden Age/Altyn Asyr `turkmenistan.gov.tm`（A——总统令、内阁会议、部委政策、官方项目报道）、TDH 国家通讯社 `tdh.gov.tm`（A——官方新闻、启用/开工/签约仪式、政策报道）、阿什哈巴德市政府 `ashgabat.gov.tm`（A-，可达性需每轮复检）、Arkadag 市官网 `arkadag-shaheri.gov.tm`（A-——Ahal/Arkadag 智慧城市、数字服务、城市设施线索）、外交部「政府网站」清单 `tmembassy.gov.tm/en/websites`（A-——重新确认部委/机构入口，尤其通信主管部门）。
- **通信/ICT 主管部门**：Ministry Communications of Turkmenistan `mincom.gov.tm`（本次核验确认；未发现独立电信监管机构或公开许可证数据库；电信牌照、频谱、号码资源不应被推断为数据中心设施；`sanly.tm` 出现于官方邮箱可作数字政府实体/域名线索，但域名本身不是设施证据）。
- **电子政务/国家数据中心**：国家 Data Centre 目前应记录为**政策/计划级单一设施线索**，优先桶为 Ashgabat，除非后续官方页面明确给出其他地点；`e.gov.tm` 可通过 Arkadag 市官网数字服务页发现，说明政府服务门户存在——门户服务存在不等于国家数据中心已建成；Arkadag（Ahal）是智慧城市/5G/GPON/数字服务高优先级线索，但智慧城市 ICT 不等于独立数据中心。
- **采购**：未发现可核验的统一全国电子采购门户；第三方 TurkmenistanTenders 页面称公共采购不由类似成熟 eProcurement 的统一全国平台支持；GPPD 将 PPA 记为 Ministry of Finance，并把 tender surface 指向聚合/目录式页面。采购公告通常应从 TDH、国家门户、国家报刊转载、Turkmenportal/Business Turkmenistan 线索回查；采购类材料最多 B 级，只有后续验收/启用/运营商服务页才能升级。不要把「采购服务器/网络设备」直接计为数据中心，先归为 `telecom core room`、`server room` 或 `government IT procurement` 线索。
- **电力/电网管线**：Ministry of Energy 官方站 `https://minenergo.gov.tm/`（旧 `minenergy.gov.tm` 不应作当前主 URL）；官网说明能源部包括/管理 `Türkmenenergo` 国家电力公司等机构；电网接入技术条件、工业大用户队列、电价目录未发现公开；电站 MW 不能换算为 DC IT load；电力证据仅在明确绑定数据中心/服务器设施/数字园区时升级。
- **六大行政区官方策略**：Ahal——高（Arkadag 智慧城市、5G/GPON、数字服务、Ahal 首府迁移后的政府 ICT；目前不是独立 DC 证据）；Balkan——低-中（里海港口、油气、跨里海光纤潜在登陆点；无已核官方 DC）；Dashoguz——低（区域通信机房/移动节点；无已核独立 DC）；Lebap——低-中（乌兹别克/阿富汗方向光纤和口岸 IT；无已核独立 DC）；Mary——低（天然气工业数字化、区域通信机房；无已核独立 DC）；Ashgabat——最高（Turkmentelekom hosting/核心网、国家 Data Centre 计划、移动核心网、政府 IT）。
- **状态与证据规则**：`telecom.tm` hosting/设施页仅有服务器/hosting 服务、无机房详情 → 运营商 hosting 服务，不自动拆成设施；官方门户/TDH 报道 “planned / necessary to open / steps are being taken” → planned/policy-backed lead；报道 “opened / commissioned / введён в эксплуатацию” → commissioned 或 operational，按原文动词记录；云厂商官方区域页列出 TM → cloud region exists（当前预期无）；Uptime 国家页列出 TM 项目 → certification exists（当前需逐轮检查，未核到具体 TM award 条目）；能源部/电站 MW 报道 → power context，不能填 IT load；Bitdeer/华为/ZTE MoU 或论坛发言 → B/C prospect，除非有官方土地、电网、开工或启用证据。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **数据可用性约束（行业角度）**：行业媒体稀缺（DCD 的 Turkmenistan 标签页可访问，但本次仅核到一条 2023 Huawei 固网扩容相关报道，没有稳定的 TM 数据中心新闻流）；公开运营商信息有限（`telecom.tm` 有官方 hosting/Physical Server 服务页，支持「国营电信提供 hosting/服务器服务」的 A 级结论，但未公开设施名称、容量、Tier 或机房地址）；目录覆盖弱（Data Center Map、Datacenters.com、Cloudscene、Baxtel 等可作目录入口，但 TM 市场预期为空或噪声大，目录条目一律 C 级）；厂商消息多为 MoU/论坛（Huawei、ZTE、Bitdeer 等公开资料多是会谈、论坛演讲、意向或探索，没有官方开工/启用/电网/土地证据前不计为设施）；采购和地图不可直接计数（采购站、地图点、BGP/WHOIS、社交媒体只提供 seed，不提供设施 existence）；流亡/独立媒体（Chronicles of Turkmenistan、Turkmen.news、Azatlyk 可发现被官方隐藏的线索，但需回官方/运营商/厂商材料复核，默认 B-/C）；容量慎用（任何 MW 必须标注 `IT load / facility load / grid / generation / unspecified`，论坛或投资稿中的「可用能源」不能转成 DC MW）。
- **市场分桶**：1) 国营电信/Hosting——Türkmentelekom/Turkmentelekom（telecom.tm），官方 hosting 页列 Physical Server 产品和 Ashgabat Archabil pr. 88 联系地址，记录为 hosting 服务线索，除非新页面披露机房；2) 通信主管机构——Ministry Communications（mincom.gov.tm），用于确认 Turkmentelekom、TM CELL 等官方关联实体；3) 移动核心网——TM CELL / Altyn Asyr、MTS Turkmenistan，核心网/5G 机房通常未公开，没有设施披露时只作 telecom core room seed；4) 电子政务/国家 Data Centre——官方资料支持计划级线索，重点 Ashgabat，需继续寻找 opened/commissioned 证据；5) Arkadag 智慧城市 ICT——Ahal 桶，5G、GPON、e-government、数字服务是强 ICT 背景但不是 DC 设施；6) Huawei/ZTE 厂商项目——固网扩容、智慧城市、5G、政府数字化，DCD 和国家媒体可作 B 级线索，需回官方；7) Bitdeer/AI-HPC prospect——2025-2026 公开资料显示 Bitdeer 参与官方活动并探索/签署数字基础设施相关 MoU，当前按 B/C prospect 不计设施；8) 跨境光纤/里海项目——Balkan、Lebap 可能受益，除非有登陆站/机房/运营商设施证据，否则只作 connectivity context；9) 目录/地图/SEO——只用于找名称，必须回 A/B 级复核。
- **当前已知行业信号（不要直接计数）**：Turkmentelekom hosting（A-/Ashgabat，支持「运营商提供 hosting/服务器服务」，不支持具体 DC 容量或 Tier）；国家 Data Centre（A policy lead/Ashgabat，官方 2018-2022 资料显示计划/推进创建，本次未核到启用证据）；Arkadag 智慧城市（A-/B/Ahal，官方城市站和国家媒体支持 smart/digital city、5G/GPON/数字服务，不等于独立 DC）；Huawei 固网/ICT（B，telecom vendor lead 非 DC）；Bitdeer（B/C prospect，Business Turkmenistan 2025 报道探索建高科技计算中心；News Central Asia 2026 报道 White City Ashgabat 2026 MoU/first data center 说法；除非 Bitdeer IR、政府公告或合同/土地/电力证据确认不计设施）。
- **云/超大规模信号**：AWS、Azure、Google Cloud、Oracle Cloud、Yandex Cloud、Alibaba Cloud 均无 TM public cloud region（Yandex Cloud 文档明确当前 region 为 Russia、Kazakhstan；Alibaba Global Locations 未列 Turkmenistan）。
- **验证与去重规则**（行业侧 9 条）：见核心结构事实第 8 条；另需输出字段：facility_name、aliases_tk_ru_en、operator、owner_or_sponsor、tenant_anchor_customer、division、city_or_district、address_or_site_description、latitude_longitude_if_verified、status、status_evidence_url、status_evidence_grade、capacity_value、capacity_unit、capacity_type（it_load/facility_load/grid/generation/unspecified）、certification_type、certification_url、power_or_grid_evidence、source_notes、last_verified_date。来源备注标签：`operator official`、`government announcement`、`state media`、`official city digital service`、`regional trade press`、`vendor MoU/prospect`、`exile media seed`、`directory seed`、`map seed`、`telecom core room no public DC evidence`、`hosting service no facility details`、`policy no facility`。

## 维护注意（更新纪律）

- 不删除/移动任何既有文件；双 explorer 文件是 codex 审核定稿，SKILL.md 忠实提炼其内容，细则差异以 explorer 原文件为准。
- 所有关键查询至少跑 RU + EN，重要项目补 TK；每轮枚举复核云区域页（AWS/Azure/GCP/Oracle/Yandex/Alibaba）并记录核验日期与失败核验（timeout/404/no result）。
- 状态动词严格分层（planned/signed/under construction/opened/operational），MoU/论坛发言不得计为建成；容量字段必须保留容量类型，电站 MW/建筑总面积/城市 ICT 投资额不得填 IT load。
- 保持 6/6 division bucket 覆盖并记录负向结论；Ashgabat 与 Ahal/Arkadag 分开；目录/地图/SEO/采购聚合站不直接计数。
