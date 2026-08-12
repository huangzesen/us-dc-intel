---
name: uz-datacenter-methodology
location: scripts/expansion/world/country-skills/UZ/SKILL.md
description: |
  Uzbekistan (UZ) data-center enumeration methodology. Division model: 14 first-level divisions (12 regions + Republic of Karakalpakstan + Tashkent City), run in Uzbek/Russian/English. No open county-style permit database; verification channels are my.gov.uz, Ministry of Construction supervision, Cadastre Agency, and hokimiyat sections on gov.uz. No AWS/Azure/GCP/Oracle public cloud region listed; Yandex Cloud has a Kazakhstan region only. Enumeration is power-led: separate IT load vs facility load vs grid capacity, and never count MoU/master-plan MW as built. Key seeds: DataVolt TAS-1 (Tashkent City IT Park, 10-12 MW), DataVolt New Tashkent (up to 250 MW planned), DataVolt Bukhara (40->250 MW planned), Uztelecom DC2 Akhangaran / Cloud Hub Kokand 1 / Cloud Hub Bukhara 1 (Uptime design certs), DC E-GOV Solnechniy, UzCloud/UZINFOCOM 5-site cloud (61 modules, 299 racks, 5.1 MW), LinkWise Bukhara 300 MW MoU, Muroosystems/Uzatom Jizzakh SMR DC. Read this before running UZ exploration/audit batches. Routes to explorer-official.md (ministry/lex.uz/energy/regulator/Uptime playbook) and explorer-industry.md (operator/trade-press/catalog seeding).
---

# UZ · 乌兹别克斯坦数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：乌兹别克斯坦无公开的郡级许可数据库，枚举靠「部委/总统令/法律（lex.uz）+ 能源/电网 + 运营商/认证（Uptime）+ 目录种子」多轨交叉。本项目电力驱动，须严格区分 IT 负荷 / 设施总负荷 / 并网容量，MoU 与总体规划兆瓦不得计为已建成。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/能源管线：数字技术部、lex.uz 法律锚点、IT Park、建设/土地/地籍、能源部/电网、监管许可、云区域核查、Uptime 基线、14 分区逐区策略 |
| `explorer-industry.md` | 行业/厂商管线：运营商与认证、外国开发商/融资、贸易媒体/目录、市场桶、查询模板、去重规则 |

## 核心结构事实（框定每次搜索）

1. 行政划分：**14 个一级分区** = 12 州（viloyatlar）+ 卡拉卡尔帕克斯坦共和国 + 塔什干市。每次搜索用乌兹别克语/俄语/英语三语别名；目录与电信页通常按城市索引，务必带首都/主要城市名。
2. **无开放许可门户可比美式 permit 门户**。验证渠道：my.gov.uz（https://my.gov.uz，服务存在为 A，逐项目记录可能需认证）、建设部（https://mc.uz）/监督系统（https://nazorat.mc.uz）、地籍署 gov.uz 栏目（https://gov.uz/en/kadastr）、各区 hokimiyat 的 gov.uz 栏目（旧独立域名可能失效，优先 gov.uz）。
3. **电力驱动**：始终区分 IT 负荷 / 设施总负荷 / 并网容量；区分运营供电 vs 提议的电价/PPA/MoU；区分可再生能源宣传 vs 签约发电或储能。MoU/总体规划 MW 只作 planned 线索。
4. **无超大规模云区域**：AWS/Azure/GCP/Oracle 官方区域页未列 UZ；Yandex Cloud 公开文档只有哈萨克斯坦区域。政府与超大规模厂商会晤只是需求/投资信号，不得据此建设施记录（A 级否定核查，带日期记录）。
5. 法律锚点（lex.uz，A 级）：Digital Uzbekistan 2030 总统令 DP-6079（https://lex.uz/en/docs/7008256）、Enterprise Uzbekistan 国际数字技术中心 DP-25（https://lex.uz/docs/6957961）、电信法 LRU-1015（https://lex.uz/en/docs/7287371）、个人数据法 LRU/ZRU-547（https://lex.uz/docs/4831939，本地化要求是需求侧驱动而非设施证据）、AI 战略至 2030 RP-358（https://lex.uz/en/docs/7159258）。
6. 核心规则：分离**设施存在 / 地点 / 容量 / 认证类型 / 状态**。乌兹别克斯坦公告常混多个阶段与 MoU。
7. 认证：Uptime 国家页 https://uptimeinstitute.com/uptime-institute-awards/country/id/UZ 。若奖项页文字为「Tier III Certification of Design Documents」，只记设计认证，不得据此标记已运营/已建成。
8. 语言：乌兹别克语 `ma'lumotlar markazi / ma'lumotlarni qayta ishlash markazi / server markazi / bulutli infratuzilma / quvvat / qurilish boshlandi / ishga tushirildi`；俄语 `дата-центр / центр обработки данных / ЦОД / серверная / облачная инфраструктура / МВт / началось строительство / введен в эксплуатацию`；英语 `data center / colocation / cloud hub / cloud region / hyperscale / AI-ready / sovereign cloud / MW`。

## 查询模式（复制粘贴模板见 explorer-official.md §1-4 与 explorer-industry.md §3）

- 部委：`site:gov.uz/en/digital "data center"`、`site:gov.uz/en/digital "DataVolt" OR "DATAVOLT"`、`site:digital.uz "data center" OR "дата-центр" OR "ma'lumotlar markazi"`。
- 法律：`site:lex.uz "дата-центр" OR "центр обработки данных" OR "ЦОД"`、`site:lex.uz "IT Park" "дата-центр"`、`site:lex.uz "искусственный интеллект" "вычислительные мощности"`。
- 能源：`site:minenergy.uz "data center" OR "дата-центр"`、`site:minenergy.uz "LinkWise"`、`site:president.uz "data center" OR "дата-центр" OR "ma'lumotlar markazi"`、`"Uzbekistan" "data center" "tariff" OR "electricity" OR "PPA"`。
- 项目验证：`"{project}" "yer ajratish" OR "land allocation"`、`"{project}" "foydalanishga topshirildi" OR "введен в эксплуатацию" OR "commissioned"`、`site:my.gov.uz "{project}"`、`site:nazorat.mc.uz "{project}"`、`site:kadastr.uz "{project}"`。
- 行业/目录/IXP：`site:datacenterdynamics.com/en/tags/uzbekistan/ Uzbekistan`、`site:uzdaily.uz "data center" OR "дата-центр"`、`site:gazeta.uz ...`、`site:kun.uz ...`、`site:daryo.uz ...`、`site:spot.uz ...`、`site:telecompaper.com Uzbektelecom "Tier-3"`、`site:datacentermap.com/uzbekistan "Tashkent"`、`site:cloudscene.com/market/uzbekistan`、`"TAS-IX" "data center" "Uzbekistan"`。
- 状态提取：`"{project}" "MW" OR "МВт" OR "quvvat"`、`"{project}" "IT capacity" OR "IT load"`、`"{project}" "groundbreaking" OR "construction began" OR "qurilish boshlandi"`、`"{project}" "commissioned" OR "launched" OR "ishga tushirildi"`、`"{project}" "MoU" OR "memorandum" OR "kelishuv"`。

## 官方/监管管线要点（详见 explorer-official.md）

- 数字技术部（https://digital.uz / https://gov.uz/en/digital）A 级：DataVolt 公告（https://gov.uz/en/digital/news/view/10951）——一期 10 MW/1.5 亿美元绿色数据中心于 IT Park 塔什干；二期 New Tashkent 25 公顷最高 250 MW；三期 Bukhara 25 公顷 40 MW 可扩至 250 MW；国家计划 2030 年前 50 亿美元。Enterprise Uzbekistan 发布（https://gov.uz/en/digital/news/view/105735）为政策/投资区锚点，非设施。
- IT Park（https://www.it-park.uz/en，基础设施页 https://www.it-park.uz/en/itpark/infrastructure，Bukhara 校区 https://itpark-bukhara.uz）：官方分支/校区源，非数据中心设施证明。DataVolt TAS-1 归塔什干市，不归塔什干州。
- 监管/许可：电信监管署（https://gov.uz/en/ttsa）、部委许可/认证/国家监管页。colo/托管/云运营通常没有独立的公开「数据中心许可证」类别——核实运营商是否另有电信/网络/数据传输许可；有电信许可不得推断有物理 DC。电子政务/国有云交叉核实 UZINFOCOM、数字政府项目管理中心、数字技术部、Uzbektelecom。
- 状态与证据规则：云官方区域页列出 = 记录区域；运营商官方页 = 按页措辞记录；Uptime 设计认证 = 仅设计；Uptime 建成/运营奖 = 强建成/运营证据；总统/部委奠基或开工公告 = 在建；lex.uz 法令/投资协议/MoU/土地划拨 = planned 线索；能源部 MoU/电价/PPA = 能源支撑的 planned 线索（核实赞助方/场地及 MW 是负荷还是并网容量）；仅目录 = C 级发现线索。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场桶：① 国有云/DC（UzCloud/UZINFOCOM、数字政府项目管理中心、电子政务 DC）；② 在位电信（Uzbektelecom/Uztelecom 云枢纽与区域 IDC；Beeline Uzbekistan、Ucell、Mobiuz/UMS 核心网 DC）；③ 外国超大规模/AI 开发商（DataVolt、LinkWise、Muroosystems/Uzatom、可能的湾/沙特/中国投资载体）；④ 政策枢纽（Karakalpakstan AI/DC 激励区，设施证据弱）；⑤ 目录/地图仅作种子。
- 设施种子基线：**DataVolt TAS-1**（塔什干市，部委 A + 运营商/融资 A/B；部委 10 MW、2026 融资报道 12 MW IT 容量，在建/2026 底投运需当期运营商/贷方页佐证）；**DataVolt New Tashkent**（塔什干州，planned 最高 250 MW/25 公顷）；**DataVolt Bukhara**（planned 40->250 MW/25 公顷）；**Uztelecom DC2**（Akhangaran，A Uptime 设计认证）；**Uztelecom Cloud Hub Kokand 1**（费尔干纳州，A Uptime 设计认证）；**Uztelecom Cloud Hub Bukhara 1**（A Uptime 设计认证）；**DC E-GOV Solnechniy**（塔什干市，A Uptime 设计认证/国有设施）；**UzCloud/UZINFOCOM 5 站点云**（Akhangaran/塔什干州、Bukhara、Kokand/费尔干纳等，官方声称 5 DC/4 州/61 模块/299 IT 机架/5.1 MW，需逐站对账物理设施并避免与 Uzbektelecom 云枢纽重复计数）；**LinkWise Bukhara 300 MW**（B MoU/planned）；**LinkWise Surxondaryo 300 MW**（更弱，仅讨论）；**Muroosystems/Uzatom Jizzakh SMR DC**（B/C planned：50 MW DC + 55 MWe RITM-200N SMR，待 Uzatom/官方确认）；**Karakalpakstan AI/DC 枢纽**（B 政策，找 A 级法令/具名运营商）；**Core AI Holdings 等 AI-DC 投资声明**（C，无站点/运营商/贷方/政府佐证不计）。
- 贸易媒体（B）：DCD Uzbekistan 标签页、UzDaily、Gazeta.uz、Kun.uz、Daryo、Spot.uz、Times of Central Asia、UzA（B+）、Telecom Review/Telecompaper。目录（C）：Data Center Map、Datacenters.com、Cloudscene、Baxtel、2GIS/Yandex Maps。

## 来源分级

- **A**：一手源——lex.uz 法律/法令、president.uz、数字技术部/gov.uz、能源部、Uptime 认证、运营商官方基建页、云厂商官方区域页、贷方/投资方官方发布。
- **B**：国家媒体或可信贸易/本地媒体引用具名部委/运营商/贷方/投资方（DCD、UzDaily、Gazeta.uz、Kun.uz、Daryo、Spot、TimesCA、UzA、Trend、Telecom Review/Telecompaper）。计数容量/状态前须回查 A 级源。
- **C**：目录/地图/社交/纯营销或无来源投资声明（Data Center Map、Datacenters.com、Cloudscene、Baxtel、2GIS/Yandex Maps、会议 deck）。仅发现用。
- 容量层级：运营商/贷方官方 IT MW > Uptime/运营商设施规格 > 部委公告 > 贸易媒体 > 目录。状态层级：运营服务页/投运 > 建成/Uptime 运营证据 > 融资+建设 > 奠基 > 土地/许可 > MoU > 政策谈话 > 目录线索。

## 使用流程（探索/复核批次）

1. 读本 SKILL.md 与两份 explorer 报告，确定目标分区与候选项。
2. lex.uz 政策/法律查询找新法令、AI/数据处理基建、电信许可、数据本地化、Enterprise Uzbekistan 更新。
3. 数字技术部/IT Park/president.uz 查具名项目、阶段、仪式、土地、MW、状态动词。
4. 对每个 MW 级项目查能源部与电网/运营商源；记录数字是 IT 负荷/设施负荷/拟议连接。
5. 重扫 Uptime 国家页并精确记录认证类型；重查 AWS/Azure/GCP/OCI/Yandex 官方区域页（未列出需带日期记录）。
6. 14 分区全部跑乌/俄/英三语矩阵：`site:gov.uz/en/{division_slug} "data center" OR "дата-центр" OR "ma'lumotlar markazi"`、`site:president.uz "{division}" ...`、`site:minenergy.uz "{division}" ...`、`site:it-park.uz "{city}" ...`、`"{city}" "data center" "MW" OR "Tier III"`。
7. 按物理站点/园区与发起方/SPV 去重；分开记录运营商、租户、项目阶段与源分级。遵守 NO-DELETION；不改写 explorer-*.md。

## 待办（2026-08-12 03:04Z）

- [x] 合并两份探索报告为 SKILL.md + ANATOMY.md。
- [ ] DataVolt TAS-1：当期运营商/贷方页确认 12 MW 与在建/投运状态；TAS-1/New Tashkent/Bukhara 三个独立记录。
- [ ] LinkWise Bukhara/Surxondaryo：找 minenergy.uz 页面或签约项目公司决议（B 升级 A）。
- [ ] Uzatom/Muroosystems Jizzakh SMR DC：Uzatom/lex.uz/minenergy 确认场地、并网与时间表。
- [ ] 待核实：UzCloud 5 站点与 Uzbektelecom 云枢纽的物理设施对账与去重。
