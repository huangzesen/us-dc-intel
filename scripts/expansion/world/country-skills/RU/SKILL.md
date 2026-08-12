---
name: ru-datacenter-methodology
location: scripts/expansion/world/country-skills/RU/SKILL.md
description: |
  Russia (RU) datacenter discovery & audit methodology — how to enumerate, verify, and update Russian datacenter projects across 83+ federal subjects (republics, krais, oblasts, autonomous okrugs/oblast, federal cities; explorers reference 85 repo divisions). Russia has no complete public building-permit search: enumeration joins regional GISOGD / construction-permit registers, EGRZ (egrz.ru) project-expertise records, Rosseti / regional grid connection signals, the new MinTsifry datacenter register (July 2025 law), Roskomnadzor personal-data / Gosuslugi IT registers, official cloud-zone pages (Yandex ru-central1, VK Cloud, Cloud.ru, Selectel, Rostelecom/RTK-DC), and operator pages (RTK-DC/DataLine, DataPro, Selectel, IXcellerate, Rosatom/Atomdata, Yandex, VK, Sber/Cloud.ru, MWS/MTS, Linx, 3data, Key Point, Oxygen, Stack, DataSpace). Read this before running RU exploration/audit batches. Routes to explorer-official.md (permits/grid/regulators/cloud) and explorer-industry.md (trade press/vendors/Russian-language query patterns).
---

# RU · 俄罗斯数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：俄罗斯**没有**成熟完整的公开建筑许可检索库；枚举需组合 **区域 GISOGD/建设许可注册**、**EGRZ（egrz.ru）项目鉴定记录**、**Rosseti/电网接入信号**、**MinTsifry 数据中心注册**（2025 年 7 月新法，逐步可用）、**Roskomnadzor 个人数据注册与 Gosuslugi IT 注册**、**官方云区域页**、**运营商官方页**与**俄语行业媒体**。
> 市场高度集中在 **Moscow/Moscow Oblast** 与 **Saint Petersburg/Leningrad Oblast**；2025-2028 扩张语言指向电力富余地区：Kaluga、Tver/Udomlya、Sverdlovsk、Novosibirsk、Irkutsk、Krasnoyarsk、Khakassia、Murmansk、Primorye、Tatarstan/Innopolis、Nizhny Novgorod、Samara、Krasnodar、Dagestan。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供俄罗斯探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：EGRZ/Glavgosexpertiza 鉴定、区域 GISOGD 与莫斯科/莫斯科州建设监督许可、Rosreestr 地籍、Zakupki 采购、Rosseti 与电网/电费、MinTsifry 注册与 Gosuslugi/RKN 注册、官方云区域（Yandex/VK/Cloud.ru/Selectel/Rostelecom；AWS/Azure 无俄区域）、运营商官方页、85 division 工作流与状态模型 |
| `explorer-industry.md` | 行业/厂商发现：CNews Analytics/ComNews Vision 排名、iKS-Consulting/TAdviser/DCD 媒体、运营商/开发商区域矩阵（RTK-DC、IXcellerate、DataPro、Selectel、Key Point、Oxygen、Yandex、Wildberries 等）、俄语/Yandex 检索语法与状态词表、84 subject 查询表 |

## 核心结构事实（框定每次搜索）

1. **无完整公共许可库**：建设证据碎片化，最强序列通常是：投资备忘录/土地分配 → **ГПЗУ** → **проектная документация / экспертиза**（EGRZ）→ **разрешение на строительство** → **разрешение на ввод в эксплуатацию** → 运营商上线。投资门户与州长公告在匹配到许可/电网/运营商记录前只按计划计。
2. **俄语词优先**：`ЦОД`、`центр обработки данных`、`дата-центр`、`машинный зал`、`серверная`、`объект ИТ-инфраструктуры`、`облачная платформа`、`модульный ЦОД`、`майнинг`（挖矿，非云/AI/colo 不计数）、`вычислительный центр` 返回不同切片。
3. **电力常是门控约束**：`технологическое присоединение`、`технические условия`、`питающий центр`、`подстанция`、`ПС`、`МВА`、`кВ`、`лимит мощности`、`договор энергоснабжения` 是一级发现词；Rosseti 及其区域子公司为 A 级流程源（110/220/500 kV 大园区线索）。
4. **MinTsifry 数据中心注册是新兴监管主干**：2025 年 7 月法律建立俄罗斯境内数据中心注册（https://digital.gov.ru/activity/gos-uslugi/reestr-czentrov-obrabotki-dannyh-czod ）；记录可检索后为 A 级；当前按官方/贸易确认作线索。Roskomnadzor 个人数据注册只是法人验证，不是设施名单；152-ФЗ/242-ФЗ 本地化合规不证设施位置。
5. **云区域=metro 种子**：Yandex Cloud `ru-central1-a/b/d/e/m`（BareMetal `m`）；VK Cloud 莫斯科区域（GZ1/ME1 标签）；Cloud.ru（前 SberCloud）AZ1/AZ2/AZ3/AZ5；Selectel 官方列出 Moscow/SPb/Leningrad Oblast/伙伴 Novosibirsk；Rostelecom/RTK-DC 莫斯科/圣彼得堡/叶卡捷琳堡/新西伯利亚/海参崴。**AWS/Azure 官方确认无俄罗斯云区域**（2022 起暂停俄罗斯新业务）——不种物理站点。
6. **容量字段分开**：`стойко-места`（机柜位）≠ 服务器机架；`ИТ-мощность`（IT 负载）≠ `подведённая мощность`（受电）≠ `МВА`（变电站/变压器）≠ `мощность ЦОД`（营销口径）≠ `campus plan MW`（长期规划）。
7. **别名/污染**：莫斯科常指 Mytishchi/Dubna/Naro-Fominsk 等州内市镇；西伯利亚/远东大量 `майнинг` 公告需排除（除非明确云/AI/colo）；`ЦОД` 在政府采购中可能指软件/数据处理系统、机房或交控中心——需设施级描述才计数。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§4 与 explorer-industry.md §1/§4）

- 俄语核心词：`ЦОД` `центр обработки данных` `дата-центр` `стойко-места` `мощность МВт` `подведённая мощность` `коммерческий ЦОД` `модульный ЦОД` `облачная зона` `зона доступности` `машинный зал`。
- 发现：`"{регион}" ("ЦОД" | "дата-центр" | "центр обработки данных") ("построит" | "строительство" | "ввод" | "запуск" | "открыл")`、`"{город}" ("ЦОД" | "дата-центр") ("стойк" | "МВт" | "Tier III" | "Tier IV")`。
- 许可/鉴定：`site:egrz.ru ("ЦОД" OR "центр обработки данных" OR "дата-центр")`、`"{регион}" "ГИСОГД" "ЦОД"`、`"{регион}" "реестр разрешений на строительство" "ЦОД"`、`"{город}" "ЦОД" "разрешение на строительство"`、`"{город}" "ЦОД" "ввод в эксплуатацию"`。
- 电力：`site:rosseti.ru ("ЦОД" OR "дата-центр") ("технологическое присоединение" OR "подстанция" OR "МВА")`、`"{проект}" "технологическое присоединение" "МВт"`、`"{город}" "ЦОД" ("подстанция" OR "ПС" OR "110 кВ" OR "220 кВ" OR "500 кВ")`。
- 监管：`site:digital.gov.ru "реестр центров обработки данных"`、`site:gosuslugi.ru/itorgs "{operator}" OR "{ИНН}"`、`site:pd.rkn.gov.ru/operators-registry "{operator}"`、`"{operator}" "152-ФЗ" "ЦОД" "{город}"`。
- 采购/土地：`site:zakupki.gov.ru ("ЦОД" OR "центр обработки данных") "{регион}"`、`site:torgi.gov.ru ("ЦОД" OR "дата-центр")`、`"{регион}" ("ОЭЗ" OR "ТОР" OR "индустриальный парк") "ЦОД"`。
- 媒体：`("ЦОД" | "дата-центр") "{регион}" site:cnews.ru`、`("центр обработки данных" "{operator}") site:comnews.ru`。
- Yandex 过滤：`"{регион}" "ЦОД" lang:ru date:20240101..20261231`、`"{регион}" "центр обработки данных" mime:pdf`、`"{город}" "дата-центр" site:{regional-domain}.ru`。
- 状态词：`построит/планирует/анонсировал/соглашение`=计划（弱）；`приступил к строительству`=在建开始；`получил разрешение`=许可信号；`введён в эксплуатацию/запущен/открыл`=运营；`расширил/ввёл зал`=扩展；`сертифицирован Tier`=认证证据非容量。
- 英文回退：`"{region}" Russia "data center" "MW"`、`"{city}" Russia "data center" "Rostelecom"`、`"{city}" Russia "data center" "Selectel" OR "IXcellerate" OR "DataPro"`。

## 官方/监管管线要点（详见 explorer-official.md）

- EGRZ/Glavgosexpertiza（A）：https://egrz.ru/ ——项目鉴定结论存在性、对象名称、申请人/开发商、鉴定状态；区域 GISOGD/ИСОГД 门户（A，各主体格式不一）；莫斯科 Mosgosstroynadzor 年度许可（https://www.mos.ru/stroinadzor/razresheniia-na-stroitelstvo/ ）与莫斯科州 minzhil.mosreg.ru/gusn.mosreg.ru 许可文件——最高密度市场的高价值许可扫描。
- Rosreestr 地籍（A 地籍事实）、Zakupki.gov.ru（A，44-ФЗ/223-ФЗ 政府采购：政府/区域数据中心、UPS/发电机/冷却招标、含地址合同）、GIS Torgi 与 invest.gov.ru 投资地图（A 官方土地/投资记录，计划级）。
- 电网：Rosseti 及其区域子公司（Moscow Region/Lenenergo/Center/Volga/Ural/Siberia 等，A 流程与部分项目信号）、110/220/500 kV 大园区线索、区域电费委员会个别 TP 收费决议（`индивидуальная плата за технологическое присоединение ЦОД {регион}`）。
- 监管：MinTsifry ЦОД 注册（A，可检索后）、Gosuslugi IT 认证注册（A 法人状态）、Roskomnadzor 个人数据注册（A 法人验证）、FSTEC/FSB 认证引用（验证受监管负载适配，不证位置）。
- 云区域（A=区域/AZ 存在，C=精确建筑）：Yandex `ru-central1-a/b/d/e/m`；VK Cloud（莫斯科，GZ1/ME1）；Cloud.ru AZ1/AZ2/AZ3/AZ5（Skolkovo/Balakovo/Domodedovo 线索）；Selectel（Moscow/SPb/Leningrad Oblast/伙伴 Novosibirsk）；Rostelecom/RTK-DC；AWS/Azure 官方确认无俄区域（A=商业状态，不种站点）。
- 运营商官方页（存在性 A-，容量 B）：Rostelecom/RTK-DC/DataLine（CNews 2025 第 1：39 个 DC/27,823 机柜位）、DataPro（Moscow/Tver 园区，官方 PDF 给地址与机架/电力设计）、Selectel（6 个自有 DC+伙伴站，莫斯科 20 MW 新建）、IXcellerate（莫斯科 3 园区+Veshki，7,500 机柜/130+ MW 计划）、Rosatom/Atomdata（Kalininsky/Xelent/Innopolis/StoreData/Moscow-2）、Yandex（莫斯科/中央区 AZ，Kaluga Grabtsevo 63 MW/3,800 机柜计划）、Sber/Cloud.ru（Skolkovo/Balakovo/Domodedovo）、Key Point（Dubna-M、Vladivostok、Novosibirsk、Yekaterinburg、SPb、Dagestan、Krasnodar、Irkutsk）、Oxygen（MSK-2/EKB-1）、Wildberries（Dubna/Naro-Fominsk）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 媒体/排名：CNews Analytics 年度「Центры обработки данных」综述（B，2025 年前 30 商业容量 73.6k→78.7k 机柜位、40 家运营商）、ComNews 数据中心频道与 Vision 年度包（B，运营商法人/排名/Uptime 认证/地图 PDF）、iKS-Consulting 市场报告（B）、TAdviser（C+/B-，时间线聚合，需交叉验证）、DCD Russia tag（B，英文交叉）、allDC/Telecombloger 地图（C 种子）、2GIS/Yandex Maps（C/B-）、Telegram/VK 运营商频道（C，官方认证账号+佐证可 B-）。
- 区域矩阵要点：**Moscow City/Moscow Oblast**（RTK-DC/DataLine/M9、IXcellerate、DataPro、3data、DataSpace、Oxygen、Stack/M1、DCN1、Yandex、VK、Cloud.ru、Wildberries Dubna/Naro-Fominsk、Key Point Dubna-M、Mytishchi/Veshki）；**SPb/Leningrad**（Selectel、Linx、Xelent/Rosatom、DataHouse、OBIT、NK Park Shushary、Dubrovka）；**Tver/Udomlya**（Rosatom/Atomdata Kalininsky，核电相邻）；**Kaluga**（Yandex Grabtsevo 工业园区）；**Sverdlovsk/EKB**（Key Point、Oxygen EKB-1、RTK、乌拉尔工业园）；**Novosibirsk**（Key Point、Selectel 伙伴、Sibtelco）；**Irkutsk/Krasnoyarsk/Khakassia**（电力富余，Cloud X/Key Point/AI DC，排除挖矿）；**Primorye/Vladivostok**（Key Point）；**Tatarstan/Innopolis**（Atomdata、IT-Park、Stack Kazan）；**Samara**（Digital Region/Zhigulevskaya Dolina）；**Dagestan/Krasnodar/Murmansk/Stavropol/Rostov**（Key Point 路线图提及）。
- 验证规则：每条记录至少 2 个来源（运营商页/CNews/ComNews/政府许可/可信地图/卫星）；运营判定需 `введён в эксплуатацию`/`запущен`/`открыл` 或运营商活跃页；积极存储别名（俄语品牌/英语品牌/法人/园区名/城市/工业园/联邦主体）。

## 来源分级

- **A** = 官方/一手：MinTsifry 注册（可检索后）、EGRZ/Glavgosexpertiza、区域 GISOGD 与官方许可注册、莫斯科/莫斯科州建设监督许可文件、Rosseti/区域电网/电费决议、Zakupki.gov.ru 采购、Roskomnadzor/Gosuslugi（法人状态）、官方云区域页、运营商官方设施页（存在/位置 A-；容量 B）。
- **B** = 强二级：CNews Analytics、ComNews Vision、iKS-Consulting、DCD、TelecomDaily、ServerNews、CNews/ComNews 具名开工/开业文章、RBC/TASS/Interfax。
- **C** = 弱线索：TAdviser、allDC、Telecombloger、Yandex Maps、2GIS、Wikipedia、经销商页、Telegram/VK 帖子（官方账号+佐证可 B-）。
- 状态语义：`rumor/lead` → `announced`（无土地/许可/EGRZ/电网证据）→ `site selection`（投资协议/土地拍卖/ОЭЗ/ТОР/工业园）→ `under review`（EGRZ/许可/电网流程可见未终批）→ `permitted`（разрешение на строительство/阳性鉴定+明确项目身份）→ `under construction` → `commissioning`（ввод/验收/PNR/客户迁移）→ `operational`（运营商页/官方开业/认证/采购证据）→ `expansion`；`mining-only` 排除。
- 去重：莫斯科别名（Mytishchi/Dubna/Naro-Fominsk）、`стойко-места` vs `ИТ-стойки`、`ИТ-мощность` vs `подведённая мощность` vs `МВА` 分别存储；按 `(最终运营商, 园区/设施, 阶段/栋, 市镇/联邦主体)` 归一化。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=RU，divisions=83+ 联邦主体：共和国/边疆区/州/自治州/联邦市）。
2. **CNews/ComNews 排名打底**：拉取最新 CNews Analytics 表与 ComNews Vision 包，归一化运营商名/法人/机柜位/计划上线/设施数。
3. **运营商官方页爬取**：对 top-40 运营商抓 `ЦОД`/`дата-центр`/`стойк`/`МВт`/`в эксплуатацию` 与区域名。
4. **联邦主体矩阵**：对每个 division 跑通用查询束（俄语名+首都/大城市），优先 Moscow City、Moscow Oblast、SPb、Leningrad、Tver、Kaluga、Sverdlovsk、Novosibirsk、Irkutsk、Krasnoyarsk、Khakassia、Primorye、Tatarstan、Nizhny Novgorod、Samara、Krasnodar、Dagestan、Murmansk。
5. **官方轨迹**：区域 GISOGD/许可、EGRZ、Rosseti/电网、Zakupki、投资门户、ОЭЗ/ТОР/工业园 resident 名单、州长新闻。
6. **状态判定与去重**：运营/在建/计划分开；容量字段分开（机柜位/机房 m²/建筑 m²/IT MW/受电 MW/电网 MW·MVA/发电机 MW/园区计划 MW）；排除纯挖矿；输出 world 同 schema，无项目 division 写 `no_projects: true`。
7. 遵守 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12 02:15Z）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：50× codex terra agent（max thinking）每 agent 分批复核俄罗斯数据中心（83+ 联邦主体）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Yandex Kaluga Grabtsevo 63 MW/3,800 机柜当前状态、Key Point 各区域站点（Dagestan/Krasnodar/Novosibirsk/海参崴）阶段、Selectel 莫斯科 20 MW 新建许可/电网、IXcellerate 园区分阶段（Veshki 130+ MW 计划）、Atomdata Arctic（Murmansk）是否运营、Wildberries Dubna/Naro-Fominsk 状态、Cloud.ru（Sber）容量与 AZ5、MinTsifry 注册可检索性。
