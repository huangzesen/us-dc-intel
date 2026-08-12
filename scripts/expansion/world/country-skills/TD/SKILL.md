---
name: td-datacenter-methodology
location: scripts/expansion/world/country-skills/TD/SKILL.md
description: |
  Chad (TD) datacenter discovery & audit methodology — how to enumerate, verify, and update Chad data-center, telco-core, IXP, government-cloud, and public-sector micro-data-center facilities at 23-province granularity. Chad has no national public registry: enumeration joins PMICE project communications (National Data Center in N'Djamena, 1,200 km fiber, 200 SOTEL sites, micro DCs), ARCEP telecom licensing/ISP lists (operator universe), ADETIC/ANSICE data-governance and certification pages (audit-before-exploitation gate), ARSE/TchadElec power records, donor project files (World Bank P180000), telco/operator pages (SOTEL, Airtel, Moov Africa Chad — successor of Tigo Chad with the 2016 Flexenclosure 374 m2/400 kW modular DC), TCHADIX IXP, and cloud-region absence checks (no AWS/Azure/GCP/OCI region). Read this before running TD exploration/audit batches. Routes to explorer-official.md (PMICE/ARCEP/ADETIC/ANSICE/ARSE/donor/cloud pipeline) and explorer-industry.md (operator/vendor/trade-press/province sweep).
---

# TD · 乍得数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：乍得**没有**全国性公共数据中心注册表；市场是**国家主导、首都恩贾梅纳（N'Djamena）主导**——不要描述为“零设施”，已验证线索包括 **PMICE 国家数据中心**（N'Djamena，2026 建筑完工+设备安装，审计/认证为正式运营前门槛）与 **2016 Tigo/Millicom 模块化通信/托管 DC**（N'Djamena，374 m2、400 kW IT 负载，Flexenclosure 建造，现属 Moov Africa Chad 系）。
> 首都之外期望的是 PMICE 光纤/传输站点、公共机构微数据中心、ADETIC 电信中心和运营商技术机房，而非商业托管。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供乍得探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：PMICE 与通信部、ARCEP（ISP 列表/市场观测）、ADETIC/.td/TCHADIX、ANSICE 网络安全与数据保护、ARSE/TchadElec 电力、World Bank P180000 捐赠与采购、云区域缺席核验、官方种子清单、23 省矩阵、提取与分级清单 |
| `explorer-industry.md` | 行业/厂商发现：高信号媒体（DCD/Ecofin/Digital Business Africa/WeAreTech/Alwihda）、运营者/厂商扫描（ADETIC/ANSICE/Huawei/TECHSO/Flexenclosure/Moov/Airtel/SOTEL/ISP/TCHADIX）、已知线索与分级、云/边缘/目录核验、省级行业枚举矩阵、开放缺口 |

## 核心结构事实（框定每次搜索）

1. **PMICE 是主要官方锚点**（2020 启动）：国家数据中心（规划 2,000 m2 三层面建筑）+ 1,200 km 国家光纤（Doba-Koumra-Sarh-Kyabe-Am Timan-Abeche-Am Zoer-Guereda-Iriba + 首都 50 km GPON）+ 200 个 SOTEL 2G/3G/4G 站点 + 100 万用户容量；2026 状态：**建筑完工、数字设备安装，ADETIC/ANSICE/TECHSO 审计认证与最终配置/互联为正式运营门槛**（Huawei 交付承包商，Gulf/GOLF Consultancy 监理）——ADETIC 说“审计后才能运营”= 在 A 级启用/调试源出现前**不算运营**。
2. **2016 Tigo/Millicom 模块化 DC**（B 级）：Flexenclosure 建造的 N'Djamena 通信/托管 DC，374 m2、400 kW IT 负载；Tigo Chad 2019 卖给 Maroc Telecom、2021 更名 Moov Africa Chad——当前验证走 Moov Africa Chad/Maroc Telecom + ARCEP 记录，确认该设施是否仍在运营、是否公开出售托管。
3. **ADETIC 备份站点**（A 级线索，非独立 DC）：2026-02-12 审计/认证任务中检查，位置/容量/角色未公开——位置、容量、角色公布前只作备份/DR 线索。
4. **PMICE 微数据中心**：WeAreTech/Digital Business Africa 报道 100 个政府机构微 DC 处于 ANSICE/ADETIC/TECHSO 认证计划下，已安装的微 DC 等待最终配置/与主 DC 互联。
5. **TCHADIX**：国家互联网交换点（G.I.E.），ADETIC 推动成立，2026-05-20 召开成立近一年后的普通股东大会；物理主机设施待识别——PeeringDB/PCH/ADETIC 记录出现前保持 B。
6. **监管/机构**：ARCEP（arcep.td）定义运营者宇宙（ISP 列表：Albidey Net、Global Technologies、IlNet、Tchad Broadband、Manano Telecom、Infotel-N'Djamena、Amanet 等——候选 N'Djamena 机房/托管线索，非设施记录）；ADETIC（adetic.td）数字政府/数据治理/国家 DC 审计；ANSICE（ansice.td）网络安全/电子认证/个人数据保护/国家 DC 审计认证；ARSE（arse.td）电力监管。
7. **电力硬约束**：ARSE 称国家用电率极低（农村约 1-2%），TchadElec 于 2025-07 取代 SNE；电网/发电机/光伏自备电源证据是设施验证的核心信号。
8. **捐赠/采购**：World Bank Chad Digital Transformation Project P180000（PATN）是需求侧与连接项目，还不是已核实的 DC 建设记录——A 级范围/采购；搜采购计划中的政府云/数字公共服务平台/网络安全/CERT/PKI/托管/灾备。
9. **云缺席**：AWS/Azure/GCP/OCI 均无乍得区域/本地分区（官方页核验）；“云在乍得可用”按伙伴/客户/服务可用性线索处理，不是物理设施。
10. **语言**：**法语为主**——`centre de données`、`data center`、`datacenter`、`salle serveurs`、`hébergement`、`colocation`、`micro Data Center`、`souveraineté numérique`、`réception provisoire`、`mise en exploitation`、`certification`。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§2 / explorer-industry.md §1-§4）

- PMICE：`site:mpntic.gouv.td PMICE "Data Center"`、`site:mpntic.gouv.td "centre de données" Tchad`、`site:primature.td PMICE "réception" OR "inauguration"`、`"PMICE" "Data Center national" "Huawei" "Tchad"`、`"PMICE" "Gulf Consultancy" OR "GOLF Consulting"`、`"micro data centers" ADETIC ANSICE TECHSO Tchad`。
- ARCEP：`site:arcep.td "data center" OR "centre de données"`、`site:arcep.td "fournisseurs d'accès internet" "{operator}"`、`site:arcep.td "TCHADIX" OR "point d'échange"`。
- ADETIC/ANSICE：`site:adetic.td "Data Center national"`、`site:adetic.td "site de backup"`、`site:adetic.td TECHSO ANSICE certification`、`site:ansice.td "Data Center" OR "centre de données"`、`"TCHADIX" "G.I.E" "ADETIC"`。
- 电力：`site:arse.td "data center" OR "centre de données"`、`"Data Center national" Tchad "groupe électrogène" OR solaire OR "TchadElec"`、`"SOTEL" "coeur du réseau" "énergie" OR "générateur"`。
- 捐赠：`site:documents.worldbank.org Chad "Digital Transformation Project" "data center"`、`"P180000" Chad "procurement plan" "server" OR "hosting"`、`"PATN" Tchad "data center" OR "hébergement" OR "cloud"`。
- 国家集：`Tchad ("data center" OR "centre de données") (PMICE OR Huawei OR TECHSO OR certification OR réception)`、`Chad ("data center") ("N'Djamena" OR "Tigo" OR "Millicom" OR "Moov Africa" OR SOTEL)`、`"Tchad" ("micro Data Center" OR "site de backup") ADETIC ANSICE`。
- 运营者：`"Moov Africa Chad" OR "Tigo Tchad" "data center" OR "centre de données"`、`"Millicom" "Tigo Chad" "Flexenclosure" "400kW"`、`"Airtel Tchad" "data center" OR "coeur du réseau"`、`"SOTEL Tchad" "coeur du réseau" OR "PMICE"`。
- 媒体/目录：`site:datacenterdynamics.com Chad "data center"`、`site:agenceecofin.com Tchad "PMICE" OR "data center"`、`site:digitalbusiness.africa Tchad PMICE OR TCHADIX`、`site:alwihdainfo.com TCHADIX OR TCHADELEC OR PMICE`、`site:peeringdb.com TCHADIX OR "N'Djamena"`、`site:datacentermap.com/datacenters/chad`。

## 官方/监管管线要点（详见 explorer-official.md）

- **PMICE/部委（A）**：2020 启动（Ecofin 镜像）、DCD Phase I 报告（1.75 亿美元投资）、Digital Business Africa 2026-05 验证报告；提取国家 DC/国家光纤/200 SOTEL 站点/100 微 DC/200 传输站点组件与阶段词。
- **ARCEP（A 运营者宇宙）**：ISP 授权列表、市场观测台、牌照页——候选机房线索；牌照不是设施。
- **ADETIC/.td/TCHADIX（A）**：Data Center 类别页、2026-02-12 审计认证文章（ADETIC/ANSICE/TECHSO-GROUP 联合任务，Huawei+PMICE 引导参观，覆盖物理/逻辑安全）、ADETIC 备份站点检查；TCHADIX G.I.E. 大会（Alwihda B）。
- **ANSICE（A）**：国家 DC 审计/认证与上线就绪、国家数据本地化/保护声明、网络事件/韧性声明。
- **电力（A 佐证）**：ARSE 运营者页、牌照/授权页；TchadElec/SNE 电网、发电机、光伏/自备电源、变电站、燃料储存。
- **捐赠（A 范围）**：World Bank P180000 项目文件/新闻稿/ISR；搜索政府云/数字平台/CERT/PKI/托管/灾备采购。
- **云缺席（A）**：四家官方区域页；非洲最近为开普敦 af-south-1。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **高信号媒体（B）**：DCD（2016 Tigo DC、PMICE 2026）、Agence Ecofin（常引部委）、Digital Business Africa（2026-05 PMICE 验证状态、TCHADIX）、WeAreTech.Africa（ANSICE/ADETIC/TECHSO 认证 + 100 微 DC 报道）、TechAfricaNews、Developing Telecoms、Alwihda Info（本地强源：TCHADIX/TchadElec/省级）、CybersecurityMag Africa（引向 ANSICE）。
- **运营者/厂商**：Huawei（PMICE 交付）、Gulf/GOLF Consultancy（监理）、TECHSO-GROUP（审计认证伙伴）、Flexenclosure（2016 DC 建造）、Moov Africa Chad/Maroc Telecom（Tigo 继任，验证 2016 DC 活性）、Airtel Chad（核心/交换机房，非商业 colo）、SOTEL/Salam（国有固网，PMICE 下核心现代化）、ARCEP ISP 列表（物理托管待各自页面验证）、TCHADIX（高价值设施线索）、TIC Tchad（声明托管在全球各地数据中心——本地 colo 稀缺的负证据）。
- **阶段词映射**：`annonce/prévoit/MoU/ambition/plan`=仅线索；`construction/travaux/bâtiment achevé/équipements installés`=建设/安装；`audit/certification/tests/interconnexion/configuration finale`=运营前就绪；`réception provisoire/inauguré/mis en exploitation/opérationnel/héberge`=更强状态，须 A/B 源+精确设施。
- **目录（C）**：DataCenterMap/Baxtel/Cloudscene/datacenters.com 仅种子/查重；拒绝目录 MW/状态/服务类型，除非运营者/官方确认；通用“N'Djamena 数据中心施工管理”页 C/忽略。
- **防重**：PMICE 国家 DC、ADETIC 备份站、微 DC、SOTEL 核心、TCHADIX、Moov/Tigo DC 可能关联——仅当源能区分时建独立记录。

## 来源分级

- **A** = 一手：部委/机构声明、ARCEP/ADETIC/ANSICE/ARSE 页面、运营者官方页、签署法令/合同、捐赠项目文件、采购公告、云厂商官方区域页（缺席）、Uptime 证书。
- **B** = 强二级：Agence Ecofin、Digital Business Africa、DCD、Developing Telecoms、TechAfricaNews、WeAreTech.Africa、Alwihda Info、RFI、TchadInfos（有具名项目/地点/业主/组件/日期或官方引语）。
- **C** = 弱线索：目录、通用厂商 SEO 页、社交帖、市场报告片段、无出处“云在乍得”声称、不披露物理设施的托管页。
- **状态语义**：审计/认证门槛未过 = 不运营；托管服务页 ≠ 物理 DC（除非指名国内站点）；电信核心 = 网络基础设施，非商业 colo（除非运营者公开在该设施卖 colo/hosting）；聚合器仅 C。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=TD，divisions=23 省）。
2. 种子：ADETIC/ANSICE 官方页 + PMICE 报道（DCD/Ecofin/Digital Business Africa）+ 运营者（Moov/Airtel/SOTEL）+ ARCEP ISP 列表 + TCHADIX。
3. N'Djamena 深扫：国家 DC（地址/区/启用日期待 ADETIC/部委/ANSICE 确认）、ADETIC 备份站、TCHADIX 主机、2016 Tigo DC 现状、SOTEL/Airtel/Moov 核心、ISP 托管。
4. 23 省逐一扫描：通用省查询块（英/法）+ 官方域（mpntic/adetic/arcep/arse）；高优先级 Sarh（PMICE 仪式/验收）、Abeche/Am Timan/Doba/Koumra（PMICE 光纤沿线）、ADETIC 电信中心省（Ennedi Est/Guera/Mayo-Kebbi Est/Wadi Fira）；无商业 DC 预期省记 no_projects。
5. 每个线索提取：名称/别名、业主/运营者/机构与项目、类型（国家 DC/备份/微 DC/IXP/电信核心/托管/机构机房/传输站点）、省/市/地址、阶段、物理指标、电力、连接性、承包商/监理/出资方、源 URL/日期/类型/分级。
6. 去重与分类：微 DC vs 机构机房 vs 传输站点不得合并为单一 DC 类；云可用性 ≠ 设施。
7. 输出与 world 探索同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；容量空着除非主源公布。
8. 遵守 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：批量复核乍得数据中心（23 省粒度，N'Djamena 深扫）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：PMICE 国家 DC 精确地址/区与最终启用日期、2016 Tigo/Moov DC 是否仍在运营且是否公开出售托管、TCHADIX 物理主机设施、微 DC 与 200 传输站点清单、ADETIC 备份站位置/容量、World Bank P180000 采购是否含 DC 组件、云区域季度复查。
