---
name: kg-datacenter-methodology
location: scripts/expansion/world/country-skills/KG/SKILL.md
description: |
  Kyrgyzstan（KG）数据中心发现以官方/监管管线（CBD 法律库与《数字法典》178/179 号法、digital.gov.kg 数字转型部门（2026-04-29 后并入总统事务局）、invest.gov.kg 国家投资署、NESK 国家电网、zakupki.gov.kg/trade.okmot.kg 采购、dpa.gov.kg 个人数据登记、htp.kg 高科技园、record.minjust.gov.kg 法人登记）和行业/厂商发现（Datatime、KyrgyzTelecom DCASA、Aknet/RackCorp、Elcat、Megaline、Saima、KG-IX、目录聚合器）为主线，按 9 个覆盖单元（Bishkek、Osh City 两个共和国级城市＋7 州）逐区枚举。
  市场小而 Bishkek 中心化：商业设施集中在 Bishkek（Datatime 2024 年启用、Uptime Tier III Design 认证），州级数据中心为设计/采购线索，Inspur MOU 仅意向；俄语检索为主，柯尔克孜语为辅，超大规模云区域官方清单无 KG 条目。
---

# KG · 吉尔吉斯斯坦数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：按 9 个覆盖单元（Bishkek、Osh City 两个共和国级城市＋Chuy、Osh、Jalal-Abad、Batken、Naryn、Talas、Issyk-Kul 七州）枚举吉尔吉斯斯坦数据中心设施与项目。
> 分区模型：7 州＋2 个共和国级城市；Bishkek 行政上不属于 Chuy 州、Osh City 行政上不属于 Osh 州，结果 schema 中不得混淆；区/地方政府站点在 okmot.kg 子域下。
> 已知种子：Datatime（Bishkek 商业 ЦОД，2024 年启用，Uptime Tier III Design）、KyrgyzTelecom ЦОД/托管（DCASA）、国家 ЦОД 设计采购（2023）、内务部 DC 采购（2026）、Infocom/Тундук 电子政务、KG-IX、Inspur Yunzhou MOU、加密货币矿场（Chuy/Jalal-Abad/Osh）。
> 本 skill 汇总两份探索报告：官方/监管管线见 explorer-official.md，行业/厂商发现见 explorer-industry.md。

## 入口

| 文件 | 管线 |
|---|---|
| explorer-official.md | 官方/监管管线：行政结构与登记（9 分区、EGR 法人登记 record.minjust.gov.kg、dpa.gov.kg 个人数据登记、data.gov.kg 开放数据、zakupki.gov.kg 采购、无全国统一建设许可库）、法律依据（数字法典 178 号法 2025-07-31、生效 2026-02-05、通信法）、数字转型机构（digital.gov.kg 与 2026-04-29 总统令 154 号重组）、内阁/总统/投资署、能源/电网（NESK、Minenergo、Electric Stations、矿业限电语境）、政府 IT/电子政务（Infocom/Тундук、egov.kg、HTP、国家 ЦОД、内务部 DC 采购）、电子采购管线、公有云区域官方页（AWS/Azure/GCP/OCI/Yandex）、查询模板、逐区枚举、已知设施表、更新节奏 |
| explorer-industry.md | 行业/厂商发现：市场结构四桶（国有/ISP 电信托管、商业托管/云、国家电子政务/主权云、加密矿场）、权威与强来源（Datatime、RackCorp、Uptime、KyrgyzTelecom、Aknet、Megaline、Elcat、Saima、Hoster、IFS、PeeringDB KG-IX、RIPE、Data Center Map、2GIS、kglabs）、查询模板（全国发现/IXP 互连/状态容量抽取、生命周期动词）、关键厂商与项目族（含超大规模与高功率项目、Inspur MOU、矿场）、逐区行业枚举、贸易媒体与协会观察清单、验证与分级规则、更新节奏 |

## 核心结构事实（框定每次搜索）

1. 吉尔吉斯斯坦为内陆国：无海缆登陆站，国际连通经哈萨克斯坦/中国/塔吉克斯坦/乌兹别克斯坦陆路走廊；海缆/登陆站查询为假阳性，互连证据只取 KG-IX/IX.KG（PeeringDB IX 2145，22 peers，约 1 Tbps）与 CDN 节点。
2. 市场小而 Bishkek 中心化：唯一独立核实运营的商业 Tier III 级设施是 Datatime（Bishkek, Koytashsky lane 46/1，2024-06-10/11 启用，500 kW+ 营销容量，双 6 kV 市变电站供电、1 MW 发电机）；Data Center Map 仅列约 3 个设施且全在 Bishkek；Chuy 多为矿场/目录线索，其余州区预期近零。
3. 州级设施多为线索而非实体：国家 ЦОД 为 2023 年设计采购（84.878m KGS、1400 平米、150 机柜，zakupki.gov.kg id=394299634，A 级仅证招标）；2026 年内务部 DC 采购（id=563665919，Bishkek, pr. Ch. Aitmatova 95，127,988,941 KGS）需验收/投运记录才可计为运营设施；两者不得混同。
4. 无全国统一建设许可搜索库：建设/规划证据经 egov.kg 建设部页、minstroy.gov.kg、Bishkek 建筑局 bga.kg/cabinet.bga.gov.kg 与采购/地方政府/运营商/电网/验收证据交叉；MOU/投资协议文章不得计为建设。
5. 俄语为官方文件、采购与新闻主力语言（дата-центр / центр обработки данных / ЦОД / серверная / колокация / хостинг / облачные услуги）；柯尔克孜语（маалымат борбору 等）罕见但出现在共和国门户；英文仅用于旗舰项目与国际新闻。
6. 能源是硬约束：水电为主但冬季缺口与能源密集型负荷限制反复出现；高 MW「数据中心」声明在确认电源、电价类别与接入点前须存疑；>1 MW 设施须与 NESK 并网新闻交叉核对。
7. 分级按所支持事实：A 官方/一手（含运营商自证、Uptime 认证页、采购中标文档、NESK 文件）；B 可靠贸易媒体/监管邻近源；C 目录/地图/聚合器；U 无法证实声明；MOU 只证「协议签署」不证「设施建成」。

## 查询模式（复制粘贴模板见 explorer-official.md §3 / explorer-industry.md §2）

- 官方管线（site 限定）：`site:digital.gov.kg "ЦОД"`、`site:digital.gov.kg "центр обработки данных"`、`site:digital.gov.kg "Inspur"`、`site:president.kg "цифровая трансформация" "Управление делами Президента"`、`site:cbd.minjust.gov.kg "ЦОД"`、`site:cbd.minjust.gov.kg "майнинг" "электроэнергия"`、`site:gov.kg "{division_ru}" "ЦОД" "строительство"`、`site:invest.gov.kg "data center"`、`site:nesk.kg "дата-центр"`、`site:nesk.kg "подстанция" "{city_ru}"`、`site:zakupki.gov.kg "ЦОД"`、`site:zakupki.gov.kg "серверная"`、`site:trade.okmot.kg "ЦОД"`、`site:data.gov.kg "центр обработки данных"`、`site:htp.kg "дата-центр"`。
- 全国俄语发现：`"Кыргызстан" "центр обработки данных" "Бишкек"`、`"Кыргызстан" "ЦОД" "Бишкек"`、`"Кыргызстан" "дата-центр" "Бишкек"`、`"Бишкек" "ЦОД" "конкурс"`、`"{division_ru}" "дата-центр" "технические условия"`、`"{division_ru}" "ЦОД" "{city_ru}" "ввод в эксплуатацию"`、`"Кыргызстан" "майнинг" "электроэнергия" "ограничение"`。
- 英文/行业：`Kyrgyzstan "data center" "Bishkek"`、`"Kyrgyzstan" "colocation"`、`"Кыргызстан" "колокация"`、`"Кыргызстан" "облако" "хостинг"`、`"Kyrgyzstan" "Tier III" "data center"`、`"Кыргызтелеком" "ЦОД"`、`"Datatime" "ЦОД" "Бишкек"`、`"RackCorp" "Kyrgyzstan" "data center"`、`"Saima" "дата-центр" "Бишкек"`。
- IXP/互连：`site:peeringdb.com Kyrgyzstan Bishkek`、`site:peeringdb.com/ix KG-IX`、`"KG-IX" participants Bishkek`、`Kyrgyzstan CDN node Apple "KG-IX"`。
- 状态与容量抽取：`"{project}" "МВт"`、`"{project}" "мощность" "стоек"`、`"{project}" "Tier III" "Uptime"`、`"{project}" "запущен"`、`"{project}" "введен в эксплуатацию"`、`"{project}" "меморандум"`；生命周期动词 planned/signed/MOU/construction began/launched/commissioned 及俄语对应词。
- 逐区模板：`"{city_ru}" "дата-центр"`、`"{city_ru}" "ЦОД"`、`"{city_ru}" "серверная"`、`"{city_ru}" "хостинг"`，矿场分离加 `"{city_ru}" "майнинг" "электроэнергия"`、`"{city_ru}" "ферма" "электроэнергия"`。

## 官方/监管管线要点（详见 explorer-official.md）

- 法律基础：数字法典（2025-07-31 第 178 号法，2026-02-05 生效，CBD 官方文本 cbd.minjust.gov.kg/3-48/edition/35412/ru）；第 179 号法废除 2008 年个人数据法；通信法；采购法经 zakupki.gov.kg 与新版 popp 门户实施。
- 机构：数字转型部门 digital.gov.kg（2026-04-29 总统令 154 号将其并入总统事务局，搜索两个名称）；通信监督无独立可靠门户，用其许可证运营商/编号/互连信号；内阁 gov.kg NPA 检索；总统 president.kg；国家投资署 invest.gov.kg（外国投资者 DC MOU 官方渠道，A 仅证协议）。
- 能源/电网：NESK 国家高压电网（nesk.kg，>1 MW 设施并网交叉核对）；能源部 minenergo.gov.kg；发电公司 Electric Stations（energo-es.kg，勿将发电新闻当并网批准）；矿业电价/分类见 CBD 检索（майнинг/криптовалюта/расчетно-вычислительный центр блочейна）。
- 政府 IT/电子政务：Infocom（ГП «Инфоком»）运营 Тундук 生态与开放数据 data.gov.kg，是国家云/G-Cloud 基础设施的自然运营商线索；egov.kg 服务目录可暴露 DC/托管采购需求；HTP htp.kg 居民清单可浮现云/托管公司。
- 采购：zakupki.gov.kg（2025 试点新门户）、trade.okmot.kg（ЭГЗ 旧表面）、gostender.kg（聚合器）；部委/政府机构托管与 DC 采购是州级 DC 使用的最强 A 级证据；设计/建设标段预示新设施。
- 登记/门户：法人登记 record.minjust.gov.kg（osoo.kg/reestr.kg 等私人镜像仅 C 级发现用）；个人数据 dpa.gov.kg 与 registry.dpa.gov.kg（2026-02-05 起按数字法典新规）；建设许可线索经 egov.kg 建设部页、minstroy.gov.kg、bga.kg/cabinet.bga.gov.kg。
- 公有云：AWS/Azure/GCP/OCI/Yandex 官方区域页每次枚举都复查；2026-08-12 均无 KG 公有云区域，任何超大规模 KG 区域声明须以官方区域清单为证。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场四桶：① 国有/ISP 电信托管（KyrgyzTelecom kt.kg、Elcat、Aknet、Megaline、Saima Telecom、Hoster.kg、IFS，多数在 Bishkek 机房/托管）；② 商业托管/云（Datatime 2024 启用、RackCorp 国际伙伴、IFS 服务页）；③ 国家电子政务/主权云（Infocom/Тундук，细节多不公开）；④ 加密矿场（Chuy/Jalal-Abad/Osh 高功率设施，目录可能标为「data center」，须单独记录为 mining/HPC）。
- 运营商标注：KyrgyzTelecom DCASA 官方页声明在 KyrgyzTelecom 数据中心提供托管（A 证服务提供）；TAdviser/2017 新闻的 Tier III/5 MW 概念仅历史线索；Datatime Uptime Tier III Design 认证不得升级为已建成设施或运营认证；Aknet 托管云（与 RackCorp）A- 证服务、C 证设施；Megaline 官方托管页 A- 证服务；Elcat/Saima 以 PeeringDB 网络在场为 A/B，设施推断为 C。
- 超大规模/高功率：Inspur Yunzhou（中国）2025 MOU 仅意向（A 证 MOU），无用地/电网/建设/容量证据；国家 ЦОД 与内务部 DC 采购按各自状态记录；公有云区域无 KG 条目，本地「云」跑在 KG 运营商/伙伴基础设施上。
- 互连：KG-IX/IX.KG（PeeringDB IX 2145，KG-IX LLC，Razzakova 55 Bishkek，AS61399）；CDN/缓存网络含 Akamai、Cloudflare、Gcore、PCH/RIPE DNS；kglabs.org 提供骨干/IXP 历史叙事（B），不得覆盖 PeeringDB/运营商记录。
- 目录/聚合器仅发现用：Data Center Map（含 Lebedinovka NSP 目录线索）、datacenters.com、Cloudscene、hostings.info、2GIS/Yandex Maps（Bishkek 有「Дата-центры」栏目）、ix.report。
- 防重复计数：运营商 vs 租户分开记录（如 RackCorp/本地 hoster 可能转售 Datatime 机柜）；企业 DC 与矿场/HPC 分开；Bishkek vs Chuy、Osh City vs Osh 按物理市政边界归类。

## 已知设施/项目与证据状态

| 设施/项目 | 分区 | 状态与证据 |
|---|---|---|
| Datatime Bishkek KR Data Center Data 5 | Bishkek | 运营中，2024-06-10/11 启用；A（运营商页 datatime.kg 证存在/地址 Koytashsky lane 46/1/500 kW+ 营销容量/双 6 kV 供电）；Uptime Tier III Design 认证 A（仅设计认证，非已建成/运营认证）；RackCorp 伙伴页 B |
| 国家 ЦОД / 州级数据中心设计项目 | Bishkek 大概率，具体地点未公开 | 设计/采购线索，未确认运营；A（招标记录 zakupki.gov.kg id=394299634）；B（24.kg/Economist.kg 2023-08 报道 84.878m KGS/150 机柜/1400 平米）；需建设/投运证据才计数 |
| 内务部（MIA/GUFHO）DC 采购 | Bishkek | 2026 年采购（安装与调试）；A（zakupki.gov.kg id=563665919：127,988,941 KGS、Bishkek, pr. Ch. Aitmatova 95、120 天交付、DC/模块/UPS/精密空调）；运营状态需验收/投运记录 |
| KyrgyzTelecom ЦОД / 托管服务 | Bishkek 加电信交换局 | 运营中服务；A（kt.kg/ru/dcasa-rus/ 证托管服务）；TAdviser/2017 的 Tier III/5 MW 概念为历史线索 B/C；区域交换局标 telecom exchange/server room |
| Inspur Yunzhou（中国）合作 | 地点未披露 | MOU/计划线索；A（digital.gov.kg 2025 官方帖证 MOU 意向）；无用地/电网/建设/容量证据，不计为设施 |
| Infocom / Тундук / G-Cloud 基础设施 | Bishkek 大概率 | 运营中国家电子政务平台，DC 建筑不公开；A（portal.tunduk.kg、egov.kg、data.gov.kg 证平台运营）；建筑/地点需采购/运营商确认 |
| IFS 数据中心服务 | Bishkek | 服务提供/集成商线索；B/C（ifs.kg 明确服务页，但不足以计独立物理托管设施） |
| KG-IX / IX.KG 互联网交换 | Bishkek | 运营中 IX；A（PeeringDB ix/2145：22 peers、29 连接、1.0T 总容量、KG-IX LLC）；ix.kg/RIPE A/B；Data Center Map/kglabs 为发现/语境 |
| 海缆登陆站 | 无 | 内陆国方法论事实；仅用海缆图确认无错误「登陆站」记录 |
| Uptime 认证 | Bishkek | 仅 1 条 KG 记录：Datatime Tier III Design；未发现独立 Constructed Facility 或 Operations 认证 |
| 加密矿场/区块链计算中心 | Chuy、Jalal-Abad、Osh 大概率 | 单独类别，默认非企业托管；CBD/部委/新闻支持矿业专门监管与电力处理；无第三方托管/云客户证据时标 mining/HPC |
| AWS/Azure/GCP/OCI/Yandex 公有云区域 | 无 | 官方清单无 KG 条目；A（仅证官方清单缺席） |

## 更新节奏

- 月度：总统/内阁/CBD 与旧 digital.gov.kg 新闻中 `ЦОД/дата-центр`；zakupki.gov.kg 新 DC/托管标段；NESK 与 Minenergo 电网/电力新闻；PeeringDB KG-IX 参与方/容量变化；24.kg/Economist.kg/Tazabek 检索。
- 季度：州级 ЦОД 状态动词复查（设计→建设→投运）；AWS/Azure/GCP/OCI/Yandex 云区域页复查；Uptime 奖励清单查 KG；Datatime 是否超出 Design 认证；Data Center Map KG 页新设施。
- 半年：刷新 154 号令后治理路由、独立通信监管站是否存在、法人/开放数据门户、数字法典实施细则中 DC 选址/本地化条款；Elcat/Saima/Megaline 设施证据；Inspur Yunzhou 状态（MOU→用地→建设）。
- 触发事件：总统/内阁法令；invest.gov.kg 公告（中/俄投资者 MOU）；能源危机法规影响矿场/DC 电力；KG-IX/IX.KG 新 IXP 或 CDN 节点公告。
- 待办（2026-08-12）：KG 属 batch-10 已复核国家；后续按本方法论推进 9 分区枚举，codex terra agent 分批复核后更新证据分级。
