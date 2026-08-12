---
name: md-datacenter-methodology
location: scripts/expansion/world/country-skills/MD/SKILL.md
description: |
  Moldova (MD) datacenter discovery & audit methodology — how to enumerate, verify, and update Moldova datacenter facilities and projects across districts, municipalities, Gagauzia, and the left-bank territorial unit. Moldova has no public national datacenter registry: enumeration joins local construction/urbanism permits (construct-permits.gov.md, Chisinau/DGAURF records, certificat de urbanism / autorizatie de construire), ARCOM/ANRCETI provider registers, STISC/MCloud government-cloud records (future national datacenter — Centrul de Date TIER III AI-Ready, site-search in Balti/Ungheni/Falesti), Environmental Agency EIA records, Moldelectrica/ANRE/Premier Energy grid evidence, MTender/tender.gov public procurement, official cloud-region pages (no MD hyperscale region — negative context), and operator pages (Moldtelecom Data City, MoldData Cloud/Host.md, Trabia/KIVIX, AlexHost, IP HOST/Inovare-Prim, AvenaCloud, Cogent, Orange Moldova, StarNet, Mezon; Transnistria Imperial Hosting as weak lead). Romanian is the primary search language, Russian for Transnistria/older material, English for operators. Lifecycle: concept/feasibility < certificat de urbanism < acord de mediu < autorizatie de construire < dare in exploatare < operational colo. Read this before running MD exploration/audit batches. Routes to explorer-official.md (regulator/permits/environment/energy/procurement/cadastre/cloud/divisions) and explorer-industry.md (operators/directories/IXPs/trade press/regional patterns/dedup).
---

# MD · 摩尔多瓦数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：摩尔多瓦**没有**公开的全国数据中心注册库；枚举靠**拼接**地方建筑/城市规划许可、ARCOM/ANRCETI 供应商注册表、STISC/MCloud 政府云记录、电网并网证据、公共采购与运营商设施页。
> 市场高度集中于 **Chisinau 市**；其他区低产，除政府选址线索（**Balti、Ungheni、Falesti**）、边境/互联走廊、工业园与德涅斯特河左岸托管市场。
> 建设许可权属地方公共行政部门；国家统计给数量不给可检索设施注册表——精确项目用地方页与文档库（certificat de urbanism/autorizatie de construire/议会决定/公众咨询）。
> 罗马尼亚语最佳；俄语用于德左与旧电信/托管材料；英语用于运营商与目录页。
> 云区域页=负面证据：AWS/Azure/GCP/OCI 官方列表无 MD 区域——勿把本地 VPS/colo 误分类为超规模云区域。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供摩尔多瓦探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：ARCOM/ANRCETI 通信监管与公共注册表、建设/城市规划许可（construct-permits.gov.md、egov.md 2025-03 四文件线上化、Chisinau/DGAURF、moldova.digital 处理数据）、环境署 EIA（Law 86/2014、anunturi 公告）、能源电网（Moldelectrica 并网/aviz de racordare、ANRE、Premier Energy Distribution/RED Nord）、采购与政府云（MTender/STISC/MCloud/2025 活动报告——Tier III AI-Ready 国家 DC 与选址之旅）、地籍/地址（ASP）、云区域负面核查、分区枚举策略（Chisinau 最深遍/Balti-Ungheni-Falesti 选址遍/北中南区/德左单独置信）与证据分级 |
| `explorer-industry.md` | 行业/厂商发现：目录与市场（DataCenterMap 6 设施/Datacenters.com/Cloudscene/Inflect/ColocationM/DC Hub）、互联与 IX（PeeringDB Data City fac 15521、MD-IX ix 392、PCH、Internet Society Pulse、Trabia KIVIX、Euro-IX）、贸易媒体与市场上下文（gov.md/STISC/eGov/Moldova1/IPN/Logos Press/UNECE/SeeNews）、运营商种子表（Moldtelecom Data City/MoldData-Host.md/Trabia/AlexHost/IP HOST-Inovare-Prim/AvenaCloud/Cogent CNDC/Orange/StarNet/Mezon、公共部门 MCloud/STISC/HiTech Park-Stauceni、德左 Imperial Hosting）、云/CDN/边缘处理、分区查询模式（Chisinau/Balti/Ungheni-Falesti/Ialoveni 溢流/区域自由区/北小区/德左）、去重规则与枚举顺序 |

## 核心结构事实（框定每次搜索）

1. **市场集中于 Chisinau（A 级运营商种子）**：Moldtelecom Data City（官方页 + PeeringDB fac/15521 + DC Hub，Tier 3 标准 colo）、MoldData Cloud/Host.md（Armeneasca 37/1）、Trabia Network（Vlaicu Pircalab St 52，KIVIX=Chisinau 第二大 IX）、AlexHost（自主供电/冷却/视频监控 colo）、IP HOST/Inovare-Prim（Uzinelor 线索）、AvenaCloud/Infotech-Grup（Muncesti 364，C+/B-）、Cogent Moldova/Chisinau CNDC、Orange Moldova（B/C，勿从全球 Orange 页推断）、StarNet（B/C）、Mezon Business Park DC（C）、MivoCloud。
2. **国家数据中心 = 计划/选址（A 级官方源）**：STISC 2025 活动报告提及 `Centrul de Date TIER III, AI-Ready`、可研采购、赴 Ungheni/Falesti/Balti 选址之旅；拉脱维亚提供方法学支持（gov.md）；在最终选地/许可/建设记录出现前按 planned/site-search 存，不按已选设施计。
3. **政府云 ≠ 新物理设施**：MCloud（egov.md）是整合政府数据中心的公共云平台——除非点名场地/建设/设施记录，`MCloud` 现代化不得变成新物理 DC；MCloud 与 STISC 未来国家 DC 是两个工作流，勿自动合并。
4. **许可生命周期**：`concept/strategie/studiu de fezabilitate` < `identificarea terenului` < `certificat de urbanism pentru proiectare` < `acord de mediu/decizie evaluare prealabila` < `autorizatie de construire` < `lucrari de constructie` < `dare in exploatare/punere in functiune` < `servicii de colocare/hosting operational`；许可文件可写作 `cladire tehnica`、`obiectiv de telecomunicatii`、`spatii pentru echipamente IT`、`statie de transformare`、`constructii industriale/de depozitare`——与技术建筑交叉核对运营商地址/PeeringDB/ARCOM 实体。
5. **电网证据**：Moldelectrica（输电网并网流程/aviz de racordare）、ANRE（许可/年报/closed distribution system）、Premier Energy Distribution（中南+Chisinau）与 RED Nord（北部）；严肃新设施应留下 aviz de racordare、变电站工程、发电机/燃料环境材料或公用事业投资引用的某种组合——用于区分小托管房与实质 DC 项目。
6. **云区域负面核查**：AWS/Azure/GCP/OCI 官方列表无 MD 区域；CDN/边缘节点（Cloudflare/Bunny/Akamai/Google cache）经 MD-IX/KIVIX 出现时记 edge_node/network_pop，除非有设施地址与运营商关系；本地 VPS “cloud” 通常运行于本地 colo/托管设施——用法人、设施地址、电力/冷却证据后再加 DC 行。
7. **德左/左岸与 Bender**：官方摩尔多瓦注册表可能不完全覆盖左岸；用独立置信标签（俄/英托管页 B/C，除非有物理地址/电力/许可/独立互联记录）；Imperial Hosting/Tiraspol 为弱线索；区分物理托管/colo/挖矿站点与 VPS 公司地址。
8. **去重**：Moldtelecom=Data City/MD-IX 管理方/COLO-54/电信页（地址或 PeeringDB ID 不同才分设施）；MoldData Cloud/Host.md/MoldData 为同一生态；Chisinau CNDC/Cogent/Trabia DC/载波 PoP 可能重叠（无设施/地址证据不把 PoP 当独立 DC）；Orange/StarNet 网络房仅在有 DC/colo 服务页、设施记录或许可时计数。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§4 / explorer-industry.md §4）

- 官方/许可：`site:chisinau.md "centru de date"`、`site:chisinau.md "autorizatie de construire" "centru de date"`、`site:dgaurf.md "centru de date" OR "autorizatie de construire"`、`site:{site_domain} "certificat de urbanism pentru proiectare" "centru de date"`、`site:chisinau.md "Alba Iulia 77" OR "Moldtelecom"`、`site:chisinau.md "Armeneasca 37/1"`、`site:chisinau.md "Vlaicu Pircalab" "Trabia"`、`site:chisinau.md "Uzinelor" "IP HOST"`、`site:chisinau.md "Muncesti 364" OR "AvenaCloud"`。
- 环境：`site:am.gov.md "centru de date"`、`site:am.gov.md "generator" "centru de date"`、`site:am.gov.md "Chisinau" "generator diesel" "server"`、`"centru de date" "evaluare prealabila"`、`"centru de date" "acord de mediu"`、`"statie de transformare" "centru de date"`。
- 能源/监管：`site:moldelectrica.md "centru de date" OR "aviz de racordare"`、`site:anre.md "centru de date" OR "sistem de distributie inchis"`、`site:anrceti.md "{operator}"`、`site:en.anrceti.md "{operator}" "Public Register"`、`"{operator}" "aviz de racordare" "Chisinau"`。
- 采购/政府云：`site:mtender.gov.md "centru de date" OR "MCloud" OR "colocare"`、`site:tender.gov.md "centru de date" OR "servere" "STISC"`、`site:stisc.gov.md "Centrul de Date TIER III"`、`site:stisc.gov.md "studiu de fezabilitate" "Centrul de Date"`、`site:stisc.gov.md "Ungheni" "Fălești" "Bălți"`、`"MCloud" "centru de date" Moldova`、`site:egov.md "MCloud"`。
- 互联/运营商：`"Moldtelecom" "Data City" "centru de date"`、`"Trabia" "KIVIX" "Chisinau"`、`"AlexHost" "colocation in Moldova"`、`site:peeringdb.com Chisinau Moldova facility`、`site:datacentermap.com/moldova/chisinau "Data Center"`、`"Cogent" "Chisinau" "CNDC"`。
- 俄语（德左）：`"Тирасполь" "дата центр"`、`"Тирасполь" "ЦОД"`、`"Приднестровье" "дата центр"`、`"Бендеры" "дата центр"`、`"Рыбница" "хостинг" "сервер"`、`"Imperial Hosting" "Tiraspol"`。
- 云负面：`site:docs.aws.amazon.com "Moldova" "Local Zone"`、`site:learn.microsoft.com "Azure regions list" "Moldova"`、`site:cloud.google.com/about/locations "Moldova"`、`site:oracle.com/cloud/public-cloud-regions "Moldova"`。

## 官方/监管管线要点（详见 explorer-official.md）

- ARCOM/ANRCETI：公共注册表（A=授权电信/网络供应商身份，非 DC 证明）；验证 Moldtelecom、Orange Moldova、StarNet、Trabia、Inovare-Prim/IP HOST、Infotech-Grup/AvenaCloud、MivoCloud、Cogent Moldova 与政府/STISC 网络实体的法人；2026 机构更名 ANRCETI→ARCOM。
- 建筑/城市规划：construct-permits.gov.md（A 流程源，公开搜索需认证）、egov.md 2025-03 四文件线上化（Chisinau 市府先行）、Chisinau/DGAURF（A）、moldova.digital 处理数据集（B，仅搜索辅助）、统计署元数据（A 总量，非枚举）；提取签发机构、文件类型、受益人/投资人、地址/地籍号/土地类别、对象描述（DC/电信节点/服务器房/技术楼/变电站/备用发电机/冷却厂）、日期/有效期/决定号/技术条件。
- 环境：环境署（am.gov.md）EIA 页与公告（A）；Law 86/2014（A 法律源）；EIA 是设计前早期程序；提取备用发电机数量/容量与燃料库、变压器/变电站容量与并网点、冷却/噪声/用水/废水、电池/UPS 与危废、规划面积/分期/地块、通知类型（screening/预评/EIA 程序/完整报告/环境协议）。
- 能源：Moldelectrica（高压并网流程 A）、ANRE（A）、Premier Energy Distribution（中南+Chisinau）与 RED Nord（北）；用 aviz de racordare/变电站/发电机材料区分小托管房与实质 DC。
- 采购/政府云：MTender（A）、采购局（A）、STISC 采购页与活动报告（A，国家 DC 选址证据）、MCloud 平台页（A 上下文）；公共项目区分运营平台/设备采购/可研/实际建设。
- 地籍：ASP（A 流程）；候选地址已知后查地籍号/业主/工业园/高压走廊关系；不单凭 IP 地理编码或地图 pin。
- 云：四家超规模官方页负面核查（A=缺失证据）；CDN/边缘记 edge/PoP。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 目录（C+/B- 线索）：DataCenterMap Moldova（6 设施 1 市场：Data City/Trabia/MoldData/AlexHost/IP HOST/AvenaCloud）、Datacenters.com（Trabia/Wintek/Moldtelecom/Orange/StarNet/MoldData）、Cloudscene、Inflect（Cogent/Mezon/Trabia）、ColocationM（地址/功率声称 B-/C+）、DC Hub（坐标/功率/状态交叉核验）；目录启动线索不闭合——常列出托管品牌/电信 PoP/reseller 位置。
- 互联（B）：PeeringDB（Data City fac/15521、MD-IX ix/392）、PCH（MD-IX 活跃，Moldtelecom 管理）、Internet Society Pulse（成员/端口容量）、Trabia KIVIX（A/B，Chisinau 第二大 IX）、Euro-IX IXPDB（C+，可能过时）；互联证明活跃网络存在，不证明 DC 所有权。
- 媒体/上下文：gov.md 拉脱维亚支持（A）、STISC 报告（A）、eGov/MCloud（A）、Moldova1（B）、IPN（B）、Logos Press（C+/B-）、UNECE IT 部门审查（B）、SeeNews（B/C，覆盖稀疏）。
- 枚举顺序：① Chisinau 运营商普查（Data City/MoldData/Trabia/AlexHost/IP HOST/AvenaCloud/Cogent/Orange/StarNet/Mezon/MivoCloud + PeeringDB 设施）；② 互联遍（MD-IX/KIVIX/PCH/Pulse）；③ 官方验证（ARCOM、Chisinau/DGAURF 许可、环境署、Moldelectrica/ANRE/Premier）；④ 政府云遍（MCloud/STISC/未来国家 DC/HiTech Park-Stauceni/Balti-Ungheni-Falesti 选址痕迹）；⑤ 区域负面扫描（地方语区模板，仅物理或官方证据出现才升级）；⑥ 德左遍（俄语托管/colo/挖矿，谨慎分级）。
- 每条候选记录最小字段：facility_name、operator_brand、legal_entity、division、city/locality、address_or_cadastral_reference、status、evidence_grade、source_urls、operator_source、interconnection_source、permit_or_environment_source、capacity_mw_or_power_claim、notes_on_duplicate_risk。

## 来源分级

- **A** = 官方/一手：带地址/服务的运营商设施页、官方地方许可/城市规划记录、环境署 EIA/决定、ARCOM 供应商注册（法人身份）、STISC/政府记录（点名政府 DC 工作）、Moldelectrica/ANRE 并网/监管记录。
- **B** = 强二级：PeeringDB 设施/IX 数据、成熟贸易媒体、处理过的官方数据集、可信运营商市场页、含运营商/地址细节的 DataCenterMap 页。
- **C** = 弱：VPS 目录、通用 “cloud in Moldova” SEO 页、IP 地理定位声称、论坛、弱设施市场、无源文档的社交帖。
- **不计数**：MCloud、“Chisinau cloud server”、CDN/缓存节点列表（除非绑定具名设施）；国家 DC 概念在 Balti/Ungheni/Falesti 的最终场地公开前不算项目（存候选/选址证据）；Chisinau 设施须捕获精确地址与法人（多品牌可能指向同一建筑/供应商生态）。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=MD，divisions=区/市/加告兹/左岸）。
2. 建种子：运营商官方页（Moldtelecom/MoldData/Trabia/AlexHost/IP HOST/AvenaCloud/Cogent）+ 地址 pivot（Alba Iulia 77、Armeneasca 37/1、Vlaicu Pircalab 52、Uzinelor、Muncesti 364、Constantin Brancusi）+ IXP（MD-IX/KIVIX）+ STISC 选址清单。
3. Chisinau 最深遍：按运营商/街道/`centru de date`/`cladire tehnica`/`statie de transformare`/`generator` 查 Chisinau/DGAURF → 环境署（备用电源/冷却/环境通知）→ ARCOM（法人）→ PeeringDB/IXP（活跃互联）→ Moldelectrica/Premier/ANRE（大负荷/变电站）。
4. Balti/Ungheni/Falesti/Stauceni：按计划/选址处理（STISC 报告），最终选地/许可/建设记录出现才升级。
5. 北中南区：快速负面筛选（地方域 + MTender + ANRE/Moldelectrica 变电站 + 罗/俄本地媒体）；高产区外：Balti、Ungheni、Falesti、Ialoveni/Straseni（溢流/物流带）、Cahul（区域发展/自由经济区）、Gagauzia（工业园/自由区）、Stinga Nistrului/德左（俄语托管/挖矿/colo）。
6. 德左/Bender：俄语+英语、独立置信标签；捕获来源管辖区、运营商地址、物理证据与来源类型（托管/挖矿/电信设施）。
7. 输出 world 同 schema；遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：codex terra agent（max thinking）每 agent 分批复核摩尔多瓦数据中心（区/市粒度）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：STISC 国家 DC（Tier III AI-Ready）最终选地（Balti/Ungheni/Falesti）与可研采购进展；Moldtelecom Data City 当前容量/状态与扩建；Trabia KIVIX 与 Trabia DC 的官方设施页细节；IP HOST/Inovare-Prim 与 AvenaCloud 的运营商页/ARCOM 确认；德左 Imperial Hosting/Tiraspol 的物理证据；Chisinau 各设施（Alba Iulia 77、Armeneasca 37/1、Muncesti 364 等）的许可与地址核实。
