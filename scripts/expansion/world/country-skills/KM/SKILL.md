---
name: km-datacenter-methodology
location: scripts/expansion/world/country-skills/KM/SKILL.md
description: 科摩罗数据中心发现与审计方法学（bilingual）。Comoros datacenter discovery & audit methodology: enumerate the official/regulatory/cloud pipeline (Journal Officiel, ANRTIC, ANADEN, Comores Câbles, AfDB PADEC, Cour Suprême audits, certification registries, cloud-region absence checks) plus industry/trade-press discovery (operators Comores Telecom/Yas, cable systems, trade press). Division model: geographical unit with 3 divisions (Anjouan, Grande Comore, Moheli). Read before running KM exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# KM · 科摩罗数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：科摩罗（Union des Comores）为极小、国家主导、年轻的电信/政府导向岛市市场（三岛约 90 万人），无公开数据中心注册库、无在线规划许可门户；本方法论通过**官方/监管/云管线（explorer-official.md）**与**行业/厂商/媒体发现（explorer-industry.md）**双轨三角验证（registry-status / triangulation approach），将政府公报、监管决定、国企审计、多边融资项目文件与海缆/运营商证据拼合成诚实的小型清单。本 skill 汇总两份最终审定的探索报告，作为 KM 探索/审计批次的入口。

## 入口

| 文件 | 管线 | 内容 |
| --- | --- | --- |
| explorer-official.md | 官方/监管/云管线 | Journal Officiel、ANRTIC（TIC 监管）、ANADEN（国家数字署）、Comores Câbles（国企海缆公司）、AfDB PADEC、IsDB/World Bank、Cour Suprême 审计、SONELEC（电力）、认证注册库（TIA-942/EPI/Uptime）、云区域缺失检查 |
| explorer-industry.md | 行业/厂商发现 | 运营商（Comores Telecom、Yas Comores/AXIAN）、Comores Câbles 登陆站、海缆（EASSy/Avassa/FLY-LION3/2Africa/国内骨干）、行业媒体（Agence Ecofin、Data Centres Africa、Techpoint、DCD 等）、目录→主源工作流 |

## 核心结构事实

1. **行政区划模型**：manifest 为 **geographical unit**，3 个 division：**Grande Comore**（Ngazidja；全国数字相关设施集中于 Moroni/Itsandra 一带）、**Anjouan**（Ndzuwani/Nzwani；Mutsamudu 有海缆登陆与电信 PoP，无公开 DC）、**Moheli**（Mwali；仅 Fomboni 登陆/电信 PoP）。commune（如 Grande Comore 内 Moroni-Bambao vs Itsandra）只是子位置备注，不得发明 division 级精度。**Mayotte（法国海外省）明确排除在范围外**，即使 Avassa/FLY-LION3 海缆跨入 Kaweni/Mamoudzou。
2. **唯一已确认设施**：**Data Center de l'Administration Publique（国家/公共行政部门数据中心）**，由 **ANADEN** 与 **Comores Câbles** 共管，ANADEN 官方页确认 **2025-05-19** 揭牌；媒体/行业源另称 **Tier 3** 与 **44.4 Tb 托管容量**（单位有歧义，按原文记录）。**地址/地块未公开**，暂归 Grande Comore（Moroni 一带，须经 ANADEN/Comores Câbles/Journal Officiel 核实具体 commune）。
3. **认证与容量纪律**：“Tier 3”为**自称**——本遍在 TIA-942/EPI/Uptime 注册库中**未发现任何科摩罗设施**，记录为 `claimed Tier 3 (certification not found)`；任何设施**无公开 MW/机架/平方米容量**，`capacity_mw: null`，不得从 Tier、44.4 Tb、预算（PADEC €9.51M / 210 亿 KMF / US$47.8M）、海缆带宽或运营商投资推算容量。
4. **融资管线**：**AfDB PADEC**（P-KM-G00-001，2024 年批准，“Projet d'Appui à la Digitalisation de l'Économie Comorienne”）为 A 级设施管线：主数据中心 + 数字孵化器 + **二级数据中心升级**（“mise à niveau du secondaire”，2025-07-02 PPM 采购措辞）；二级设施身份未核实（候选：Comores Telecom 服务器设施或政府 IT 设施），按线索处理直至主源点名。
5. **监管与法律**：**ANRTIC**（Agence Nationale de Régulation des TIC，anrtic.km）为电信监管机构（牌照、频谱、编号、服务质量、个人数据监管）；2025-05-27 向 Yas Comores 与 Comores Telecom 授予 5G 频段；框架法文号本遍未确认，须经 ANRTIC “Textes de référence”/Journal Officiel 核实。数据保护法（loi portant protection des données à caractère personnel）官方文号/日期未确认；PADEC 含设立国家个人数据保护与信息获取管理局（跟踪其处理登记册/通知/许可）。
6. **运营商双寡头（无公开 DC 服务）**：**Comores Telecom**（历史国有运营商，Huri 品牌，总部 Place Volo-volo, BP 7000, Moroni；20 年运营；5G 频段 2025-05-27）与 **Yas Comores**（原 **Telma Comores**，属 **AXIAN Telecom**，2016 年起第二持牌人，2025-05-16 首发 5G，2025 年中宣布约 €25M 网络投资）；其 HQ/NOC/核心站点仅为线索。**Comores Câbles S.A.**（约 2016 年于 RCIP4/世行互联计划下设立，2023-11 启用 Moroni 新总部）运营海缆登陆与全国骨干并共管国家 DC；Cour Suprême 2023-01-05 审计报告（ROD）为其资产官方主证。
7. **海缆=互联非设施**：登陆点（GeoCables）：**Moroni（4 条）**、**Chindini（2）**、**Mutsamudu/Anjouan（2）**、**Fomboni/Moheli（1）**；系统：EASSy（Moroni，约 2012）、Avassa（2016，科摩罗–Mayotte；Chindini/Moroni/Mutsamudu/Mamoudzou）、FLY-LION3（Moroni–Kaweni 400 km，经 **Itsandra** 登陆站，Comores Câbles/Orange/SRR 联合体）、2Africa 科摩罗支线（2023-01-12 Itsandra 海滩登陆）、科摩罗国内海缆/骨干（命名待核实）。登陆站只有在出现服务器/托管/云证据时才升格为设施记录。
8. **云区域为缺失检查**：AWS/Azure/Google Cloud/OCI 官方区域页均无科摩罗区域/本地区；本地 VPS/转售/云页面仅作服务证据。
9. **可靠性分级规则**：A = 官方/主源直接证明所录事实（Journal Officiel 文本/决定、ANRTIC 决定/公报、ANADEN 或 Comores Câbles 官方页/声明、AfDB/世行/IsDB 项目文件、Cour Suprême 审计、运营商官方页、海缆系统/联合体官方页、云官方区域页、TIA-942/EPI/Uptime 注册库条目）；B = 具名当事人/日期/地点的可靠媒体或行业源（Al-Watwan、La Gazette des Comores、Habari za Comores、Comores Infos、Masiwa Komor、Focus-OI、Agence Ecofin、Data Centres Africa、Techpoint Africa、DCD、Developing Telecoms）；C = 目录/市场/SEO 托管页/社媒/转载（**绝不因报道官方声明而把媒体条目升 A，须单独引用底层官方源**）；U = 未验证。分级只覆盖该源实际支撑的事实。
10. **语言与拼写**：科摩罗官方与媒体材料以法语为主——搜 “centre de données”“salle de serveurs”“hébergement”“station d'atterrissement”“câble sous-marin”“économie numérique” 并配英文；检索必须含 “Comores”/“Comoros” 或运营商/地名，避免 `.km`/KM 歧义与 SEO 噪音。
11. **电网背景**：SONELEC（2018 年法令合并 MAMWE/EDA 成立）供电频繁断电，任何 ICT 机房几乎必有发电机/UPS——**发电机存在绝不等于数据中心**；能源记录仅作大负荷/变电站/备用发电的佐证。

## 常用查询模板

```text
site:journalofficiel-km.com (ANADEN OR numérique OR "data center" OR "centre de données")
site:journalofficiel-km.com ("Comores Câbles" OR "câbles sous-marins" OR backbone OR 5G OR ANRTIC)
site:anrtic.km (5G OR "attribution de fréquence" OR licence OR "données à caractère personnel")
site:anrtic.km ("data center" OR "centre de données" OR hébergement)
site:anaden.org ("data center" OR "centre de données" OR "19 mai" OR "Comores Numérique 2028")
site:comorescables.km ("data center" OR cloud OR "station d'atterrissement")
site:afdb.org PADEC Comores
site:coursupremecomores.km ("Comores Câbles" OR SONELEC OR "data center")
site:egouv.km (numérique OR "économie numérique" OR "data center")
site:alwatwan.net Comores ("centre de données" OR "data center" OR câble)
site:agenceecofin.com Comores ("centre de données" OR numérique)
("Grande Comore" OR Ngazidja OR Moroni OR Itsandra OR Chindini) ("centre de données" OR "data center" OR "station d'atterrissement" OR ANADEN)
(Anjouan OR Ndzuwani OR Nzwani OR Mutsamudu) (câble OR station OR télégraphe OR serveur OR "centre de données")
(Moheli OR Mohéli OR Mwali OR Fomboni) (câble OR station OR serveur OR "centre de données")
"Comoros" "TIA-942" OR "Uptime Institute" OR "Tier IV" OR "Tier 3" - negative control
"Comoros" "AWS" OR Azure OR "Google Cloud" OR OCI region - absence check
"FLY-LION3" Comores Itsandra OR Moroni station ; "2Africa" Comores Itsandra atterrissage
"Comores Telecom" ("data center" OR "centre de données" OR "salle de serveurs" OR NOC)
("Yas Comores" OR "Telma Comores") ("data center" OR "centre de données" OR "core network")
PADEC Comores (datacenter OR "centre de données" OR incubateur OR "protection des données")
```

## 官方/监管管线要点（详见 explorer-official.md）

- 官方面：Journal Officiel（1975 年以来唯一官方公报，法律/法令/决定）、ANRTIC（牌照与 5G 决定）、ANADEN（2019-01 法令设立，PADEC 执行机构，驱动 “Comoros Numérique 2028”，共管国家 DC）、Comores Câbles、AfDB PADEC 项目页/评估报告/2025-07-02 PPM、IsDB 2026 年公共行政现代化 GPN（邻近数字平台/AI 实验室需求证据，**非 DC 项目**除非后续采购点名托管/设施工程）、Cour Suprême Section des Comptes 审计（Comores Câbles ROD 2023-01-05、SONELEC）、Comoros Open Data、SONELEC（经审计报告）。
- 认证注册库为**负向控制**：TIA-942/EPI/Uptime 每轮刷新重查，科摩罗预期“无条目”，该无条目本身即发现；国家 DC “Tier 3” 声称未经认证即不可升级。
- 分 division 覆盖检查表：Grande Comore（高优先）——国家 DC 地址核实、Comores Telecom HQ 服务器机房/NOC、Itsandra 登陆站（FLY-LION3+2Africa）、Moroni EASSy 登陆、Chindini 登陆、egouv 部委、PADEC 采购、SONELEC 电力；Anjouan（中）——Mutsamudu 登陆、ED/SONELEC 电力、电信 PoP/交换局、银行（BIC/Exim/BCC）；Moheli（低）——Fomboni 登陆、电信 PoP。每 division 要么有已核实项目/线索，要么显式标记无公开项目。
- 决策规则：在线规划许可检索在科摩罗产出极低（本遍未确认电子规划门户），用 Journal Officiel/egouv.km/commune 记录佐证并如实说明；国企审计报告是被低估的主证（可证实或否决设施线索）；不得删除旧线索——无法核实则降级保留并注明缺失证据。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 目录→主源工作流：仅从目录（DataCenterMap/Baxtel/Cloudscene/datacenters.com/PeeringDB/CDN PoP）播种，预期科摩罗无或近零 DC 条目（记录该发现）；再以精确设施/运营商/地址对主域（anaden.org、comorescables.km、comorestelecom.km、yas.km、axian-telecom.com、anrtic.km、journalofficiel-km.com、afdb.org）检索；division 经岛屿/commune/地址核实；状态仅用 announced/under development/lead（若仅计划或媒体报道）。
- 种子记录：国家 DC（运营/2025-05-19 揭牌，容量 null，Tier-3 未认证）、PADEC 二级 DC 升级（线索）、Comores Telecom HQ 机房/NOC（线索）、Yas 核心站点（线索）、Itsandra/Moroni/Chindini/Mutsamudu/Fomboni 登陆站（A 级海缆事实，非 DC）、PADEC 孵化器（融资 A 级）、政府/部委服务器机房（C）、银行/金融服务器机房（BCC、BIC、Exim、Banque Postale、Mvola，C）。
- 诚实产出预期：Grande Comore 1 个已确认设施 + 2–4 条线索；Anjouan 与 Moheli 0 个已确认 DC（记录海缆登陆与电信 PoP 线索，显式标记无公开 DC）；不得虚增。

## 维护注意（更新纪律）

- **更新节奏**：每月——ANADEN réalisation 页、Comores Câbles、ANRTIC 决定/公报、Journal Officiel、Al-Watwan/Gazette 等媒体；每季度——AfDB PADEC 项目/采购页面与 PPM、认证注册库（TIA-942/EPI/Uptime，负向复核）、云区域官方页（缺失复查）、Cour Suprême 新审计报告；里程碑事件——PADEC 主/二级 DC 采购授标与交付、国家 DC 地址/认证发布、数据保护管理局设立与登记册上线、新海缆 RFS。
- **来源核验**：复核层必须逐个点击 A 级 URL 确认页面实际载明所引事实；直接 curl HEAD 403 不等于死链（ANRTIC 用浏览器/GET）；Comores Telecom TLS 链校验问题记入爬取日志而不降级内容；记录含 认证机构/tier（自称 vs 认证）/证书 ID/授标与到期日期/capex/揭牌日期/地址/division/运营商/客户类型/公共服务/互联海缆邻近。
- **不删除纪律（no-deletion）**：已复核记录不得删除；旧线索无法核实则降级保留并注明缺失证据；Mayotte 设施一律排除；海缆登陆站保持互联记录，不因营销词（“world-class”“souveraineté numérique”“AI-ready”）升格为设施。
