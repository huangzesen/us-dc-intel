---
name: kz-datacenter-methodology
location: scripts/expansion/world/country-skills/KZ/SKILL.md
description: |
  Kazakhstan (KZ) datacenter discovery & audit methodology — how to enumerate, verify, and update Kazakhstan datacenter projects at 17-oblast + 3-city (Astana/Almaty/Shymkent) granularity. Kazakhstan has no single public planning-permit search; the pipeline is national digital-infrastructure policy + regional akimat/government news, construction/eGov systems (egov.kz, elicense.kz, e-Qurylys, Qportal, AIS GGK), KEGOC/grid documents (transmission constraints, substations, 70/30 generation mechanism), operator annual reports (Kazakhtelecom 25-27 DCs / 1,500-1,600+ racks), official cloud-region pages (Yandex Cloud kz1 is the only documented active public cloud region, local DC in Karaganda with Freedom Telecom PoP; no AWS/Azure/GCP/OCI Kazakhstan region), and trade press. Russian + Kazakh are the strongest search languages; English works for flagship projects (Data Center Valley Ekibastuz 300 MW→1 GW master plan, Akashi Astana 100 MW, GK Hyperscale, Beeline Hyper Cloud, Freedom Cloud) and investment promotion. Read this before running KZ exploration/audit batches. Routes to explorer-official.md (MAIDD/construction/KEGOC/cloud/operator/region matrix) and explorer-industry.md (operator/certification/vendor seeds/trilingual templates/grading rules).
---

# KZ · 哈萨克斯坦数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：哈萨克斯坦**没有**可像美国郡门户或英国规划门户那样直接搜索的全国许可库；实用管线是**国家数字基础设施政策 + 州/市（akimat）政府新闻 + 建筑/eGov 系统（egov.kz/elicense.kz/e-Qurylys/Qportal/AIS GGK）+ KEGOC 电网文件 + 运营商年报 + 官方云区域页 + 贸易媒体**。最强搜索语言是俄语与哈萨克语，英语只对旗舰项目与投资促进有效。
> 电力主导规模（KEGOC 输电约束、变电站、70/30 发电扩张机制、2026 电信/数据中心法将 DC 列为战略对象）；俄语 `ЦОД`/`центр обработки данных`/`дата-центр` 与哈语 `деректер орталығы`/`ДӨО` 是核心词；目录常把高功率加密货币矿场标为“data center”，须与企业 colo/云分开。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供哈萨克斯坦探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：MAIDD（AI 与数字发展部）/电信委员会、总理/总统/Kazakh Invest、建筑与许可（eGov/e-License/Qportal/e-Qurylys/AIS GGK/Adilet）、KEGOC/能源部电网、云区域（Yandex `kz1` 唯一活跃公共区域；AWS/Azure/GCP/OCI 均无）、运营商扫描（Kazakhtelecom/Kazteleport/Transtelecom/NIT/Beeline/AKASHI/Enegix/Freedom/PS.kz）、17 州+3 市路由表、证据分级与状态规则、快速 URL 索引 |
| `explorer-industry.md` | 行业/厂商发现：政府/投资/AIFC/Astana Hub/采购（goszakup）/RSP 检查登记、运营商/认证/目录（Uptime/DataCenterMap/Datacenters.com/Cloudscene/Yandex Maps/2GIS）、英俄哈三语查询模板、项目家族种子（Data Center Valley/Akashi/GK Hyperscale/Freedom Cloud Alatau/Enegix/Makat/Digital Silk Route）、逐区枚举法、验证与分级规则 |

## 核心结构事实（框定每次搜索）

1. **国家官方主干（A，政策/项目存在）**：MAIDD（gov.kz/memleket/entities/maidd）是云/AI/电信/DC 政策主导源；2025 商业 DC 市场约 **4,000 机架、91% 利用率**；**Data Center Valley（Ekibastuz）宣称 300 MW 可用电力、分期扩至 1 GW**——是国家基准数字，非设施清单；2026 电信/数据中心法将 DC 列为战略对象并引入 70/30 机制。
2. **总理/总统/Kazakh Invest（A，协议与优先状态）**：Abai 州投资页有 AI HUB/Data Center Valley 项目卡（abai.invest.gov.kz/doing-business-here/invest-projects/40348/）；签署协议/政府优先状态/地区/站点为 A，未来阶段容量无许可/电网/施工证据时 B/C。
3. **建筑与许可渠道（项目验证而非全国公开清单）**：eGov 建筑服务（`архитектурно-планировочное задание`、`технические условия`、建筑许可/验收）、e-License（公司级许可）、Qportal/e-Qurylys（建设信息整合系统）、AIS GGK 城市规划地籍（地块/分区确认，非 DC 关键词库）、Adilet 法律库；州/市当局在 `gov.kz/memleket/entities/<region>-...`。
4. **能源/电网管线**：KEGOC（系统运营商/国家电网）接入与电网容量、南北输电、西部区整合、南部加固；能源部（`гипермасштабных центров обработки данных` 备忘录）；地区能源/自然垄断公用事业；证据规则：KEGOC/部委具名项目/连接/变电站/MW 为 A，贸易媒体转述 B，营销“便宜电”C。
5. **云区域核查**：**Yandex Cloud `kz1`（可用区 `kz1-a`）是唯一经官方文档确认的哈萨克斯坦活跃公有云区域，本地 DC 在 Karaganda，Freedom Telecom 为 PoP**；AWS/Azure/GCP/OCI 官方区域表均无哈萨克斯坦公共区域（检查日）——“有兴趣/预期”只作需求证据。
6. **运营商（A 公司足迹/B 设施归属）**：Kazakhtelecom 2021 年报 25 个 DC/约 1,500 机架/98% 利用率 + Almaty 3.3 MW 模块化 DPC + Kosshi 100 座设施；2022 年报 27 个 DC/1,600+ 机架/95-98% 利用率/54% 商业 DC 份额；Kazteleport（Almaty/Sairam + Ereymentau/Astana，Uptime 认证）；Transtelecom（铁路/电信，多为 C）；NIT（政府 IT/eGov）；Beeline/VEON Hyper Cloud（Almaty 在建，A）。
7. **私有/超大规模/托管**：AKASHI（Astana，官方 4,224 机架/100 MW IT，A-/B+ 设计容量，须 Astana akimat/e-Qurylys/电网/Uptime 核实）；Enegix（Ekibastuz 150+50 MW，偏矿场/HPC）；Freedom Cloud/Freedom Telecom（7 个 Tier III DC，Karaganda PoP，A-）；PS.kz（Almaty，互连/对等细节）；NLS/Megakhost/Qazmin（C 直到官方页/许可）。
8. **四个发现桶**：① 传统电信/colo/主权云（Kazakhtelecom/Kazteleport/Freedom/Transtelecom/PS-NAT-NLS）② 新超大规模/AI（Data Center Valley、Akashi、GK Hyperscale Akmola+Temirtau、Beeline Hyper Cloud、Freedom Alatau）③ 公有云区域/PoP（Yandex kz1）④ 数字挖矿 DC（高功率，目录常误标，单独记录）。
9. **状态映射**：`MOU/меморандум/инвестиционное соглашение`=计划线索；`land allocated/SEZ/Kazakh Invest 项目卡`=计划（须具名站点与赞助方）；`архитектурно-планировочное задание/технические условия/разрешение на строительство/e-Qurylys 记录`=已许可/建设前；`началось строительство/заложили`=在建；`введен в эксплуатацию/запущен/іске қосылды`=运营；`MW available/reserved power/发电机制`≠ IT 容量。
10. **陷阱**：政府超大项目常聚合多期（勿把 1 GW Data Center Valley 全算建成）；云文档中的“Kazakhstan region”可能是计费/控制面区域或单 AZ；Almaty vs Almaty Region、Astana vs Akmola 易混；俄语音译多变（Karaganda/Қарағанды、Ust-Kamenogorsk/Өскемен、Akkol/Aqkol、Kosshi/Qosshy）；国家/政府云设施可能刻意少披露——无公开许可 ≠ 不存在。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§5 / explorer-industry.md §2）

- 俄语核心词：`дата-центр` `центр обработки данных` `ЦОД` `коммерческий ЦОД` `облачная инфраструктура` `суверенное облако` `строительство ЦОД` `стойки` `мегаватт` `подстанция` `технические условия` `архитектурно-планировочное задание` `разрешение на строительство` `ввод в эксплуатацию` `майнинг дата-центр`；哈萨克语：`деректер орталығы` `деректерді өңдеу орталығы` `ДӨО` `бұлттық инфрақұрылым` `құрылыс` `электр қуаты`。
- 官方：`site:gov.kz "{region_ru}" "дата-центр" "строительство"`、`site:gov.kz "{city_ru}" "центр обработки данных" "разрешение"`、`site:gov.kz "{region_ru}" "технические условия" "ЦОД"`、`site:invest.gov.kz "{region_en}" "data center"`、`site:{regional-invest-subdomain}.invest.gov.kz "Data Center Valley"`、`site:primeminister.kz "data center" Kazakhstan`、`site:goszakup.gov.kz "ЦОД" OR "центр обработки данных"`、`site:rsp.gov.kz "центр обработки данных" "{city}"`。
- 能源：`site:kegoc.kz "дата-центр" OR "центр обработки данных"`、`site:kegoc.kz "data center" Kazakhstan`、`site:gov.kz "гипермасштабных центров обработки данных" "Министерство энергетики"`、`"{project}" "МВт" "подстанция" "Экибастуз" OR "Павлодар"`。
- 云：`site:yandex.cloud Kazakhstan "kz1"`、`site:yandex.cloud "Karaganda" "data center"`、`site:cloud.google.com Kazakhstan "region"`、`site:aws.amazon.com Kazakhstan "Local Zone"`、`site:azure.microsoft.com Kazakhstan "region"`、`site:oracle.com Kazakhstan "cloud region"`。
- 运营商：`site:telecom.kz OR site:b2b.telecom.kz "ЦОД" "{city_ru}"`、`site:ar202*.telecom.kz "дата-центров" "стоек"`、`site:kazteleport.kz "Data Center" OR "ЦОД"`、`site:uptimeinstitute.com "Kazakhstan" "Data Center"`、`site:akashi.cloud "MW" "Astana"`、`site:enegix.net "Ekibastuz" "MW"`、`site:veon.com "Beeline Kazakhstan" "data center"`、`site:fch.kz OR site:freedom.kz "data center"`。
- 行业：`site:datacenterdynamics.com Kazakhstan "data center"`、`site:interfax.com Kazakhstan "data center" "MW"`、`site:astanatimes.com Kazakhstan "data center"`、`site:qazinform.com Kazakhstan "data center"`、`site:profit.kz "дата-центр" Казахстан`、`site:kapital.kz "дата-центр"`、`site:astanahub.com "data center"`。
- 状态/容量提取：`"{project}" (MW OR МВт OR қуаты)`、`"{project}" (racks OR стойк OR стоек OR серверлік)`、`"{project}" (Tier III OR Tier IV OR "Uptime Institute")`、`"{project}" ("construction began" OR "началось строительство" OR "құрылысы басталды")`、`"{project}" (commissioned OR launched OR "введен в эксплуатацию" OR "іске қосылды")`。

## 官方/监管管线要点（详见 explorer-official.md）

- **MAIDD/电信委员会（A，政策）**：Data Center Valley/Firebird/NVIDIA 包、Aleria MOU、IDC 市场快照、2026 电信/数据中心法——项目存在与政府目标 A，已建成容量须明确声明。
- **总理/总统/Kazakh Invest（A）**：签署协议/战略对象分类/地区站点/投资条款；Abai 州 Data Center Valley 项目卡为模板。
- **建筑/许可（验证渠道）**：eGov 服务名（`архитектурно-планировочное задание`/`технические условия`/建筑许可/验收）、e-License、Qportal、e-Qurylys、AIS GGK（地块/规划/工程网络）、Adilet（建筑法典/电信法/许可规则）；州当局 `site:gov.kz "{region_ru}" "ЦОД"`。
- **电网（A）**：KEGOC 接入/技术条件/投资与新闻稿（输电约束、变电站、南北/西部/南部区）、能源部（超大规模 DC 电力备忘录与长期消费/发电机制）；州能源部门/自然垄断公用事业。
- **云（A 区域）**：Yandex `kz1`/Karaganda；AWS/Azure/GCP/OCI 官方表为负控制。
- **行业/协会**：Astana Hub（B+，GK Hyperscale 等投资公告）、AIFC（B）、DCD（B）、Interfax（B+/A- 当转述官方声明）、Astana Times（B）、Qazinform（B+）、Kursiv/Kapital/Profit（B/C）、QazProjects（B/C 项目库）、Uptime（A 认证）、Data Center Map/Datacenters.com/Cloudscene/Baxtel/ColoMap/Yandex Maps/2GIS（C 发现面）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **旗舰项目家族（种子）**：Data Center Valley/Ekibastuz（政府/Kazakhtelecom/Firebird/NVIDIA，按阶段计数）、Akashi/Astana（4,224 机架/100 MW，四栋）、GK Hyperscale（Akmola + Temirtau 各 100 MW Tier III，计划）、Freedom Cloud Alatau（480 机架/7.2 MW，开工报道，注意 Almaty City vs Almaty Region 边界）、Beeline/VEON Hyper Cloud（Almaty 在建，主权企业 AI 云）、Enegix（Ekibastuz 150+50 MW，矿场/HPC 标注）、Makat（Atyrau 40 MW 移动燃气电厂，核实运营商与矿场性质）、Digital Silk Route（Aktau SEZ，计划/陈旧）。
- **运营商（A）**：Kazakhtelecom（全国最广区域 IDC 足迹，年报 A）、Kazteleport（Halyk 子公司，Sairam/Ereymentau/Aktau，Uptime）、Freedom Cloud Holding（7 个 Tier III DC；Yandex 文档确认 Karaganda PoP）、Beeline/VEON、Transtelecom（C 待证实）、NAT/PS/NLS/Serverspace 等（多为 Kazteleport/Kazakhtelecom 内租户——物理设施与租户分开记录防重复）。
- **状态动词（三语）**：英 `signed/planned/construction began/breaks ground/launched/commissioned/go live`；俄 `подписали соглашение/меморандум/планируется/началось строительство/заложили/введен в эксплуатацию/запущен`；哈 `келісім/жоспарлануда/құрылысы басталды/іске қосылды/пайдалануға берілді`。

## 来源分级

- **A** = 官方/一手：MAIDD/总理/能源部/KEGOC 具名文件、eGov/e-Qurylys/Qportal 许可输出、akimat 土地/建筑/验收公告、运营商年报、官方云区域文档、Uptime 认证、RSP 检查登记（地址/运营商，无容量）、goszakup 合同。
- **B** = 强二级：DCD、Interfax、Astana Times、Qazinform、Kursiv、Profit/Kapital（点名官员/运营商时）、运营商新闻稿（无许可/电网证明）、Kazakh Invest 项目页、Astana Hub。
- **C** = 弱：DataCenterMap、Datacenters.com、Cloudscene、Baxtel、ColoMap、Yandex Maps、2GIS、营销页、社交、SEO 页；MOU/投资协议文章常见，非施工证据。
- **容量/状态层级**：运营商官方 IT MW/机架 或 Uptime 认证（A）> 上市发行人年报（A）> 政府项目页（A/B 看阶段）> DCD/Interfax/Kursiv（B）> 目录/地图（C）；`planned up to 1 GW` 是总规划容量，只计数具名已建/在建阶段；矿场/HPC 与 enterprise colo/云分开。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=KZ，divisions=17 州 + Astana/Almaty/Shymkent 三市）。
2. 国家官方种子：MAIDD/总理/能源部/Kazakh Invest/Akorda——提取项目名、赞助方、地区、MW/机架、状态动词。
3. 云核查：验证 Yandex `kz1`；扫 AWS/Azure/GCP/OCI 官方区域页；未列出者记录“无官方公共区域”。
4. 在位运营商扫描：Kazakhtelecom 年报 + B2B 页；Kazteleport、Transtelecom、Freedom、Beeline、PS.kz、Akashi、Enegix 官方页。
5. 逐区许可/电网：每个 division 跑俄/哈 `site:gov.kz` 搜索（DC 词 + 建筑/土地/技术条件/变电站/验收词）；>数 MW 的用 KEGOC/能源部/当地公用事业/akimat 能源部门交叉核对。
6. 认证/目录补缺：Uptime 优先，再 Data Center Map/Datacenters.com/Cloudscene/Baxtel/Yandex Maps/2GIS；发现别名与地址后回官方核实。
7. 去重：按物理园区/运营商-SPV/地址/变电站电源/阶段分组；Data Center Valley/Ekibastuz 阶段与既有 Enegix、Kazakhtelecom Pavlodar 设施分开；Yandex Cloud 租用 Freedom Karaganda 时物理 DC 记一次、Yandex 作云租户/区域证据。
8. 输出与 world 探索同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`（notes 保留来源类别：operator official/government agreement/trade press/directory only/mining-HPC/tenant in third-party DC/MOU only）；无项目 division 写 `no_projects: true`；容量区分 `operational` / `under_construction` / `planned_full_buildout_mw`。
9. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：批量复核哈萨克斯坦数据中心（州/市粒度，Pavlodar-Ekibastuz + Astana + Almaty + Karaganda 深扫）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Data Center Valley 各期（125/250/1000 MW）建设与并网证据、Akashi Astana 四栋完工状态、GK Hyperscale Akmola/Temirtau 许可、Beeline Hyper Cloud Almaty 进度、Freedom Cloud Alatau 开工、Enegix/Makat 矿场 vs 企业性质、Yandex kz1 后续 AZ、Kazakhtelecom 年报 2023-2025 最新 DC 数、AWS/Azure/GCP/OCI 是否宣布哈萨克斯坦区域。
