---
name: ne-datacenter-methodology
location: scripts/expansion/world/country-skills/NE/SKILL.md
description: |
  Niger（NE）数据中心发现以官方/监管管线（MCNTI 数字部、ARCEP 电信监管、ANSI 国家数字机构、HAPDP 个人数据保护、NIGELEC/ARSE 电力、marchespublics.ne 公共采购门户、ARMP/JMP、AfDB DTS 项目 P-Z1-GB0-024、PCH IXP 记录、公有云区域官方页）和行业/厂商发现（ANP/Le Sahel/Ecofin 等新闻、运营商页、目录聚合器、Uptime 认证核对）为主线，按 8 个区（Niamey; Agadez; Diffa; Dosso; Maradi; Tahoua; Tillabéri; Zinder）逐区枚举。
  市场处于萌芽期且 Niamey 中心化：唯一可信的设施级公开证据是国家数据中心/DTS 数据中心（AfDB 支持，PK5/Niamey V 区，Tier III 营销语未获 Uptime 认证）与财政部数据中心采购线索；尼日尔为内陆国，无海缆登陆站，法语为官方与商业主力语言，检索须用 -Nigeria 过滤假阳性。
---

# NE · 尼日尔数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：按 8 个区（Niamey; Agadez; Diffa; Dosso; Maradi; Tahoua; Tillabéri; Zinder）枚举尼日尔数据中心设施与项目。
> 分区模型：一级覆盖为 8 分区——首都城市共同体 Niamey 加 Agadez、Diffa、Dosso、Maradi、Tahoua、Tillabéri、Zinder 七区；gouv.ne 与 ANP 区菜单均确认此覆盖集；不要只搜 Niamey，但预期真实证据以 Niamey 为中心。
> 已知种子：国家数据中心/DTS 数据中心（PK5、Niamey V 区）、财政部数据中心采购（DGMG/TR_DGMG_034）、DTS 跨撒哈拉光缆骨干、Niger Telecoms、Airtel Niger、Zamani Telecom、Moov Africa Niger、Niger IXP（PCH 历史记录）、Atal Networks VPS 转售页。
> 本 skill 汇总两份探索报告：官方/监管管线见 explorer-official.md，行业/厂商发现见 explorer-industry.md。

## 入口

| 文件 | 管线 |
|---|---|
| explorer-official.md | 官方/监管管线：结构事实（8 分区、2023-07-26 政变后过渡政权/AES 语境、无公共 DC 登记册/无建设许可库/无 Uptime 认证设施）、检索词（法语优先）、官方/监管源表（MCNTI、ARCEP、ANSI、HAPDP、marchespublics.ne、ARMP/JMP、NIGELEC/ARSE、gouv.ne/ANP/Le Sahel、AfDB DTS、PCH、云区域清单）、官方查询模板、逐区枚举、可靠性分级、已知设施表、逐区状态快照、更新节奏、排除规则 |
| explorer-industry.md | 行业/厂商发现：市场现实（萌芽期、Niamey 中心化、无商业 carrier-neutral 托管设施、勿与 Nigeria 混淆）、检索词与假阳性过滤（-Nigeria -Lagos -Abuja）、行业管线（Agence Ecofin/Ecofin Agency、ANP、Le Sahel、WeAreTech、DCD、Developing Telecoms、本地媒体）、目录/互连/认证（PCH、PeeringDB、DataCenterMap、Baxtel、Uptime、海缆图负向检查）、行业查询模板、云/CDN/边缘处理规则、分级、已知设施表、逐区行业状态、更新节奏、陷阱 |

## 核心结构事实（框定每次搜索）

1. 尼日尔数据中心市场处于萌芽期且 Niamey 中心化：唯一可信的设施级公开证据来自政府/公共部门——AfDB 支持的国家数据中心/DTS 数据中心项目（ANP 2025-02-27 报道部长宣布 AfDB 支持 90 亿+ FCFA、执行 13%、计划 2025-09-30 接收；AfDB E&S 文件将 EIES 子项目定位于 PK5、Arrondissement Communal Niamey V）与财政部数据中心采购线索（marchespublics.ne 计划 P_MF_2022_5 与临时授予 TR_DGMG_034，中标 Groupe BASSID SERVICES）。
2. 无公共数据中心登记册、无适用设施枚举的公共建设许可库、无 Uptime Institute 认证的尼日尔设施（2026-08-12 核对）；「Tier III」营销/部级用语在认证目录点名该设施前保持 C/U。
3. 尼日尔为内陆国：不接收任何国内海缆登陆站；连通性为陆路（往贝宁/布基纳/尼日利亚的老出口，以及 AfDB 资助的 DTS 往阿尔及利亚与乍得方向）；AfDB 2025-11-14 报告 DTS 光缆超 1000 公里临时移交，但数据中心组件仍需独立投运/认证证据。
4. 政治语境：2023-07-26 政变后处于过渡政权，属 AES（与马里、布基纳法索）；部委名称与官员常变，2026 年检查用 MCNTI 为现行部名并先核实现任部长。
5. 法语主导行政与技术出版物（datacenter / centre de données / salle serveur / hébergement / colocation / cloud souverain / dorsale / fibre optique）；英语用于区域贸易媒体与厂商营销；注意重音变体 Tillabéri/Tillaberi、Niamey/Niame。
6. 目录搜索常返回尼日利亚结果：检索尼日尔专属设施须过滤 `-Nigeria -Lagos -Abuja -Kano`；Airtel Africa/Nxtra 数据中心证据指向尼日利亚 Lagos，不得导入集团或尼日利亚资产入 NE。
7. 分级按字段：A 官方/运营商一手记录（政府公报、部委页、ARCEP 报告/决定、HAPDP 法律文本、ARMP/JMP/门户招标或授予、NIGELEC/ARSE 文件、AfDB 项目/采购/E&S 文件、运营商官方设施页、云官方区域页、PCH/PeeringDB 网络记录）；B 强二级（ANP/Le Sahel 转述具名官员、Ecofin、DCD、Connecting Africa、Developing Telecoms、WeAreTech）；C 仅发现线索（目录、市场、社媒、付费报告预告、VPS 转售、旧 MOU、无站点/电力/运营商证据的发布声明）；U 无可用来源。

## 查询模式（复制粘贴模板见 explorer-official.md §3 / explorer-industry.md §3）

- 官方（分开跑，勿合并为单块）：`site:gouv.ne Niger "centre de données"`、`site:gouv.ne Niger datacenter`、`site:mcnti.gouv.ne "centre de données"`、`site:mcnti.gouv.ne "data center national"`、`site:mcnti.gouv.ne "Dorsale Transsaharienne"`、`site:ansi.ne Niger "centre de données"`、`site:ansi.ne Niger "cloud gouvernemental"`、`site:arcep.ne Niger "rapport annuel" opérateurs`、`site:arcep.ne Niger licence "Niger Telecoms"`、`site:hapdp.ne "Loi-N°2022-59"`、`site:marchespublics.ne "data center"`、`site:marchespublics.ne "centre de données"`、`site:marchespublics.ne "salle pilote"`、`site:armp-niger.org "data center" Niger`、`site:nigelec.ne datacenter Niamey`、`site:nigelec.ne "poste de transformation" Niamey`、`site:arse.ne NIGELEC Niamey MW`、`site:afdb.org Niger DTS "data centre"`、`site:afdb.org "P-Z1-GB0-024" datacenter`。
- 每项目/运营商：`"{operator}" Niger "centre de données"`、`"{operator}" Niger datacenter`、`"{operator}" Niger hébergement colocation cloud`、`"{operator}" Niamey NIGELEC`、`"{operator}" Niger site:marchespublics.ne`。
- 8 分区快速扫掠（官方 §4）：`Niamey Niger "centre de données"`、`Niamey Niger colocation`、`Agadez Niger "centre de données"`、`Diffa Niger datacenter`、`Dosso Niger "centre de données"`、`Maradi Niger datacenter`、`Tahoua Niger "centre de données"`、`Tillabéri Niger datacenter`（及 Tillaberi 变体）、`Zinder Niger "centre de données"`，配 `site:anp.ne "{division}" datacenter`、`site:marchespublics.ne "{division}" "fibre optique"`。
- 行业新闻：`site:agenceecofin.com Niger datacenter`、`site:agenceecofin.com Niger "dorsale transsaharienne"`、`site:ecofinagency.com Niger "data center"`、`site:lesahel.org Niger "centre de données"`、`site:anp.ne Niger "data center"`、`site:wearetech.africa Niger "data center"`、`site:datacenterdynamics.com/en/news/ "Zamani" Niger`。
- 运营商种子：`"Niger Telecoms" datacenter`、`"Niger Telecoms" hébergement colocation cloud`、`"Zamani Telecom" Niger "centre de données"`、`"Orange Niger" "centre de données"`、`"Airtel Niger" datacenter`、`"Moov Africa Niger" datacenter`、`"AFR-IX" Niger Niamey datacenter`、`"Starlink" Niger "data center"`。
- 目录/互连/认证：`site:peeringdb.com Niger Niamey`、`site:pch.net Niger IXP Niamey`、`site:datacentermap.com Niger Niamey datacenter -Nigeria`、`site:uptimeinstitute.com/tier-certification Niger Niamey`、`"Niger" "IXP" Niamey`。
- 云区域负向：`site:aws.amazon.com/about-aws/global-infrastructure Niger`、`site:learn.microsoft.com/en-us/azure/reliability/regions-list Niger`、`site:cloud.google.com/about/locations Niger`、`"Niger" "AWS Local Zone"`。
- 假阳性过滤：`"Niger" "data center" Niamey -Nigeria -Lagos -Abuja`、`"Niger" "centre de données" -Nigeria`、`"Niger Republic" datacenter`。

## 官方/监管管线要点（详见 explorer-official.md）

- MCNTI（mcnti.gouv.ne）为现行数字部：数字政策、国家数据中心计划、DTS 接收、电子政务、AES 数字合作；引用前先核实现任部长（2026 页为 Adji Ali Salatou；旧 2025 国家 DC 文章用 Sidi Mohamed Raliou 旧职务措辞）。
- ARCEP（arcep.ne）为电子通信与邮政监管：2024 年报页列出 CELTEL/Airtel、MOOV、ZAMANI COM、NIGER TELECOMS 等运营商；A 证许可/监管事实，许可证不等于 DC 记录。
- ANSI（ansi.ne）为国家数字机构种子源：Niger 2.0、电子政务、政府云线索；除非命名物理设施，否则仅作官方计划证据。
- HAPDP（hapdp.ne）为数据保护机构：2022-12-16 第 2022-59 号法及 2023-31 修正与 2024 法令构成个人数据框架；支持主权数据需求但不证设施。
- NIGELEC（nigelec.ne）生产/输配/分销、总部 Avenue du Général De Gaulle, Plateau I, Niamey；ARSE 电力页称 NIGELEC 在八区均有存在；电力文件 A 证公用事业事实，须查任何 DC 级负载声明。
- 采购：marchespublics.ne 为最佳官方来源（招标计划与授予）；ARMP/JMP（armp-niger.org）为采购期刊与佐证（本轮 curl 返回 Cloudflare 522）。
- AfDB DTS（P-Z1-GB0-024）：项目页、2024-10 EER、简化采购计划、E&S 文件；A 证 AfDB 文件；包含国家数据中心范围与 EIES/PAR 文件。
- PCH IXP 目录（pch.net/ixp/details/1921）：Niamey 的 Niger IXP 状态，历史/搁置记录削弱商业托管声明。
- 云区域：AWS/Azure/GCP/OCI 官方清单 2026-08-12 均无尼日尔公有云区域（A 级负向检查）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 无商业 carrier-neutral 托管设施页；目录搜索多返回尼日利亚结果，NE（Niger）与 NG（Nigeria）不可混淆。
- DTS 项目已越过旧草案目标日期表述：AfDB 2025-11-14 报告超 1000 公里光缆临时移交，数据中心组件仍需独立投运/认证证据。
- 无活跃 IXP 证据：PCH 历史记录非运营互连设施证明。
- 电力是主要可行性约束：任何设施级负载声明都必须以 NIGELEC/ARSE 核对（nigelec.ne、arse.ne/electricite）。
- 运营商：Niger Telecoms（A 证运营商存在，U 证 DC 服务，无公开托管/云设施页，Facebook/社媒声明保持 C/U）；Zamani Telecom/前 Orange Niger（并购新闻不是 DC 线索，除非资产转移文件点名设施）；Airtel Niger（集团 DC 资产在 Lagos/Nigeria，不计入 NE）；Moov Africa Niger（Maroc Telecom 集团资产在别处，需尼日尔特定证明）；AFR-IX 无设施证据。
- 新闻源：ANP（具名官方声明 B+）、Le Sahel（部长访谈，例：正在建设 data center 访谈）、Agence Ecofin（DTS 执行 97% 报道）、Ecofin Agency（英文佐证）、WeAreTech（13% 完成度/9 月完工目标报道）、DCD（Zamani/Niger Telecoms 并购）、本地媒体（ActuNiger、Journal du Niger、Echos du Niger、Air Info Agadez）。
- 云/CDN/边缘规则：超大规模客户、市场伙伴、CDN 缓存、Starlink 许可、边缘 PoP 都不是数据中心园区；从法国/Abidjan/Dakar/Lagos 向尼日尔营销的本地托管不是尼日尔设施，除非提供商点名物理场地且获佐证。

## 已知设施/项目与证据状态

| 设施/项目 | 分区 | 状态与证据 |
|---|---|---|
| 国家数据中心 / DTS 数据中心 | Niamey（PK5、Arrondissement Communal Niamey V） | 建设/接收中；A（AfDB 项目范围 P-Z1-GB0-024 与 E&S 文件）；B+（ANP 2025-02-27 部长宣布 90 亿+ FCFA、13% 执行、计划 2025-09-30 接收）；C/U（Tier III 认证与最终投运，需官方验收/认证文件）；与所有「national DC」「DTS Niamey DC」「ANSI/政府云」引用去重为同一物理项目 |
| 财政部数据中心 / DGMG 采购 | 大概率 Niamey（中央采购） | 采购存在 A（计划 P_MF_2022_5 含机房外壳/内部布线/IT 设备/试点室；临时授予 TR_DGMG_034、2021-07-27、Groupe BASSID SERVICES）；运营状态/精确地址/托管角色 U；作为政府内部 DC 线索单独保留，非商业托管 |
| DTS 光缆骨干 | 全国/跨境（阿尔及利亚、乍得、贝宁、布基纳、马里方向） | A/B（骨干项目 1031 公里/97% 执行、2025-11-14 超 1000 公里临时移交）；非数据中心，仅连通性语境 |
| Niger Telecoms | Niamey HQ 加区域交换局/骨干 | A（运营商存在/许可）；C/U（DC 分类）；交换局/铁塔/骨干 PoP 不计数 |
| Airtel Niger | Niamey 移动/核心网络 | A（运营商/许可）；U（尼日尔 DC）；Airtel Africa 官方 DC 活动在 Lagos, Nigeria，不计入 |
| Zamani Telecom | Niamey 加全国移动网 | A（持牌运营商，ARCEP 来源）；U（设施） |
| Moov Africa Niger | Niamey | A（运营商）；U（尼日尔 DC）；需尼日尔特定证明 |
| Niger IXP | Niamey | A（PCH 记录）；历史/搁置互连线索，非活跃托管设施 |
| Atal Networks「Niamey VPS」 | Niamey 声称 | C/U；转售营销，除非点名尼日尔实体设施并获佐证 |
| AWS/Azure/GCP/OCI 公有云区域 | 无 | A（官方清单负向检查）；边缘/CDN/客户在场不是 DC 记录 |

## 更新节奏

- 月度：MCNTI、gouv.ne 内阁公报、ANP、Le Sahel、marchespublics.ne、ARMP/JMP、ARCEP 通知、AfDB P-Z1-GB0-024 项目/采购页。
- 季度：NIGELEC/ARSE、HAPDP 清单、PCH 与 PeeringDB、DataCenterMap/Baxtel/DataCenterPlatform/Inflect、DCD、Agence Ecofin、WeAreTech、Connecting Africa、TechAfrica News、Telecom Review Africa。
- 半年：AWS/Azure/GCP/OCI 区域清单、Uptime 认证目录、海缆图（内陆负向检查）。
- 触发事件：国家 DC 接收/启用、EIES/验收证书发布、Zamani/Niger Telecoms 合并行动、AES 区域数字基础设施公告、ARCEP 许可变更、Niamey 重大电网/变电站事件。
- 待办（2026-08-12）：NE 属 batch-10 已复核国家；后续按本方法论推进 8 分区枚举，codex terra agent 分批复核后更新证据分级。
