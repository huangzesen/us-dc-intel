---
name: tn-datacenter-methodology
location: scripts/expansion/world/country-skills/TN/SKILL.md
description: |
  Tunisia (TN) parent-level methodology for data-center enumeration at governorate granularity (24
  governorates). Tunisia has no public national data-center register and no complete open planning-permit
  search; enumeration joins telecom/legal status (INTT licences and SVA declarations), ministry cloud policy
  (MTC), public-sector hosting (CNI/ATI), investment files (TIA), cybersecurity/cloud governance (ANCS),
  operator facility pages, certification records (TUV/ISO/PCI), utility context (STEG/ANME), and local press.
  Confirmed anchors concentrate in Tunis / Greater Tunis (Tunisie Telecom Data Center Carthage, Ooredoo La
  Charguia 1, ATI, CNI private cloud) and Sousse governorate (Orange Kalaa Kebira, EO Data Center/Meninx
  Enfidha); Bizerte is a cable-landing/planned-AI-DC corridor (SoleCrypt planned). No hyperscaler public
  region exists. Routes to explorer-official.md (regulator/public-sector/permits/energy pipeline) and
  explorer-industry.md (press/operator/directory pipeline).
---

# TN · 突尼斯数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：突尼斯没有公开的国家数据中心登记册，也没有完整的开放式规划许可检索；枚举必须拼接电信/法律状态（INTT 许可与增值服务声明）、部委云政策（MTC）、公共部门托管（CNI/ATI）、投资文件（TIA）、网络安全云治理（ANCS）、运营商设施页面、认证记录（TUV/ISO/PCI）、公用事业背景（STEG/ANME）与本地媒体。已确认设施集中于突尼斯城/大突尼斯（TT Data Center Carthage、Ooredoo La Charguia 1、ATI、CNI 私有云）与苏塞省（Orange Kalaa Kebira、EO/Meninx Enfidha）；Bizerte 是海缆登陆/规划 AI-DC 走廊（SoleCrypt 为 planned）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供突尼斯探索与复核批次使用。

## 入口

| 文档 | 用途 |
|---|---|
| `explorer-official.md` | 官方/监管管线：INTT、MTC、ANCS、CNI/ATI、INPDP、TIA、城市规划/ANPE、STEG/ANME、云区域阴性对照、运营商设施锚点、24 省矩阵 |
| `explorer-industry.md` | 行业管线：行业媒体（DCD/We Are Tech/Webmanagercenter/ilboursa 等）、运营商/供应商扫库、目录处理、逐省行业矩阵、候选处理范例 |

## 核心结构事实（框定每次搜索）

1. **无登记册**：突尼斯没有公开的国家数据中心登记册，也没有完整的开放式规划许可检索；枚举 = 电信/法律状态 + 部委云政策 + 公共部门托管 + 投资文件 + 运营商页面 + 认证 + 公用事业 + 本地媒体。
2. **24 省**：Ariana, Beja, Ben Arous, Bizerte, Gabes, Gafsa, Jendouba, Kairouan, Kasserine, Kebili, Le Kef, Mahdia, Manouba, Medenine, Monastir, Nabeul, Sfax, Sidi Bouzid, Siliana, Sousse, Tataouine, Tozeur, Tunis, Zaghouan。
3. **市场结构**：电信主导 + 公共部门主导 + 小型私有 colo；已确认锚点：Tunisie Telecom Data Center Carthage（Tunis，A，TUV 认证）、Ooredoo La Charguia 1（Tunis，站点 B/服务 A）、Orange Tunisie Kalaa Kebira（Sousse，A，2025-05 启用，1,000 m2/Tier III-quality 为 B 佐证）、EO Data Center/Meninx（Enfidha，Sousse，A/B，载波中立/主权云）、ATI 数据中心（Tunis，服务 A）、CNI 私有云（Tunisie Digitale 2020，AfDB/MTC 采购 A）。
4. **SoleCrypt Bizerte 为 planned**：2026-02-02 与 Schneider Electric 的 MoU（A 存在），Bizerte/20 MW/Tozeur T60 太阳能为媒体/公司声明（B/C）；除非出现施工、许可、电力或调试证据，不得计为运营设施。
5. **海缆登陆站不是 DC**：Bizerte 因 Orange/Medusa 登陆而有强连通性；登陆站记录为连通性资产。
6. **无超大规模区域**：官方 AWS/Azure/GCP/OCI 列表均无突尼斯公共云区域（2026-08-12）；突尼斯为主权/托管云与电信云市场。
7. **语言**：法语最高产（centre de donnees/centre de calcul/cloud souverain/hebergement/salle serveur/HPC）；阿拉伯语用于公共页面与本地媒体（مركز البيانات/مركز الحساب/الاستضافة/السحابة السيادية/رخصة البناء）；英语用于 DCD/厂商/云区域/国际海缆。
8. **容量纪律**：仅当来源将 MW/MVA/kVA/机架/平方米绑定到具名站点时才记录；不得从国家电力统计或太阳能电站推导 MW（Tozeur 60 MW Scatec 是能源资产，不是 DC 线索）。
9. **ANCS 托管标签**：国家云战略赋予 ANCS 对托管服务提供商进行标签化的角色；ANCS 发布的提供商列表对获批提供商状态为 A，物理设施仍需单独核实。
10. **TIA 投资政策**：2025-10-14 第 22 届战略委员会将数据中心列为战略增长支柱（A 政策状态，不是设施证据）；可用 TIA 发现大型项目申报与投资公约。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§3、explorer-industry.md §1/§2/§5）

```text
site:intt.tn "licence" "{operator}" OR "services a valeur ajoutee"
site:intt.tn "centre de donnees" OR "data center" OR "hebergement"
site:mtc.gov.tn "centre de donnees" OR "data center" OR "cloud prive"
site:ancs.tn "hebergement" OR "labellisation" OR "cloud"
site:cni.tn "cloud" OR "centre de donnees"
site:ati.tn "data centers" OR "housing" OR "hebergement"
site:afdb.org "Centre National de l'Informatique" "Cloud prive"
site:inpdp.tn "cloud" OR "hebergement"
site:tia.gov.tn "data center" OR "centres de donnees"
site:steg.com.tn "data center"
site:anme.tn "autoproduction" "solaire"
"Tunisie Telecom" "Data Center Carthage"
"Ooredoo Tunisie" "La Charguia" "data center"
"Orange Tunisie" "Kalaa Kebira" "data center"
"EO Data Center" Enfidha
"SoleCrypt" Bizerte "data center"
"SoleCrypt" "Tozeur" "60MW" OR "T60"
"Medusa" Bizerte "landing station"
"{governorate}" "centre de donnees" OR "data center"
"{governorate}" "salle serveur" OR "salle informatique"
"{project}" "permis de construire" OR "etude d'impact" OR "ANPE" Tunisie
"{project}" "STEG" "poste electrique" OR "transformateur" OR "groupe electrogene"
site:datacenterdynamics.com/en/news/ Tunisia "data center"
site:webmanagercenter.com "La Charguia" "data center"
site:tekiano.com Tunisie "data center"
site:ilboursa.com "data center" "Sousse"
site:datacentermap.com/tunisia "{operator}"
"تونس" "مركز البيانات"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **INTT**：电信监管机构；运营商/ISP/SVA 状态、年度报告、光纤/批发容量（location de capacites excedentaires）、QoS、决定与法律文本；对法律/电信/SVA 状态为 A，不自动构成设施证据。
- **MTC**：部委数据中心启用、国家云政策、公共数字项目与采购；2015-01-15 TT 突尼斯新数据中心启用页（A）；CNI 私有云招标/延期页（A）。
- **ANCS**：国家网络安全局；云治理与托管提供商标签化；不是设施登记册。
- **CNI/ATI**：CNI（El Omrane, Tunis 地址≠设施地址）私有云平台（AfDB/MTC 采购 A）；ATI 声明产品托管于 ATI 数据中心并提供 housing/colo（服务存在 A，地址/容量未公开）。
- **INPDP/TIA**：INPDP 为合规背景（loi organique 2022-34）；TIA 为投资政策与大型项目发现（2025-10-14 战略委员会，A 政策状态）。
- **城市规划/ANPE**：permis de construire 属地方事务，无全国公开检索；用 `etude d'impact`、`EIE`、`ANPE`、`consultation publique` 找大项目环评；AFI/工业园区与具名园区。
- **STEG/ANME**：电网/变压器/变电站/自发电/可再生能源背景；不把太阳能容量转为 DC 负载。
- **云区域**：AWS/Azure/GCP/OCI 官方页为“无突尼斯公共区域”提供 A 级阴性对照。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **Tunisie Telecom Data Center Carthage**：A（设施+认证，TT/TUV/MTC）；目录地址（Carthage/Rue Tirons/Avenue de Carthage）保持 C。
- **Ooredoo Tunisie**：托管页（host.ooredoo.tn）为服务/存储在突尼斯 DC 的 A 声明；WMC 2016 探访 La Charguia 1 为 B 站点证据；规格/容量未知。
- **Orange Tunisie Kalaa Kebira**：A（Orange 官方 2025 文章，设施/日期/地点，2025-05-05 运营）；DCD/ilboursa/We Are Tech 为 B（1,000 m2、Tier III-quality 措辞）。
- **EO Data Center/Meninx**：A（当前运营商页：Zone Industrielle d'Enfidha、载波中立/主权云）；B（2013 启用、首家私有/中立历史）。
- **ATI/CNI/CCK**：ATI 服务 A；CNI 政府托管平台 A（实施站点需核实）；CCK El-Khawarizmi 为机构 HPC/科研计算，非商业 colo。
- **SoleCrypt**：A MoU；Bizerte/20 MW/Tozeur T60 为 B；阶段 planned。
- **Topnet（Ariana/El Ghazala）、GlobalNet/HexaByte/Tunet、Novahoster、NeoLedge**：提供商线索（B/C），仅当运营商/监管/证书/许可/强媒体具名当前物理设施时才计数。
- **目录纪律**：DataCenterMap/datacenters.com/Baxtel/Cloudscene/WHTop 为 C 默认；升级流程 = 精确名称在运营商域 → INTT/MTC/ANCS/TIA → 认证/许可 → 无主源则保持 C。

## 来源分级

- **A** = 针对特定主张的主要/官方证据：INTT 页面、电信许可或决定、MTC/ANCS/CNI/ATI/INPDP/TIA/部委/省/市页面、官方采购公告、STEG/ANME 来源、运营商设施页、官方 ISO/PCI/Uptime 证书或认证记录、官方公共云区域列表。
- **B** = 强二级：DCD、Agence Ecofin/We Are Tech Africa、Webmanagercenter、THD、Tekiano、ilboursa、African Manager、La Presse、Business News、Leaders、L'Economiste Maghrebin、TAP（非官方宿主转引）或具名厂商/集成商含项目细节的文章。
- **C** = 弱线索：DataCenterMap、Baxtel、datacenters.com、Cloudscene、WHTop、社交帖子、不可访问片段、泛市场报告、仅目录地址。
- 状态语义：planned/MoU/study、tendered/awarded、under construction、inaugurated/operational、maintenance-only、inactive；仅当来源把容量绑定到具名 DC 站点时写 `capacity_mw`。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL 中的 TN 记录与种子（TT Carthage、Ooredoo、Orange Kalaa Kebira、EO/Meninx、ATI、CNI、SoleCrypt）。
2. 逐省五遍法：①监管/法律（INTT/ANCS）②公共部门（MTC/CNI/ATI/CCK/AfDB/世行/AFD）③运营商 ④规划/能源（省/市、工业园区、ANPE、STEG、ANME）⑤二级确认（行业媒体；目录仅线索）。
3. 省归属按物理市镇/地点（Enfidha→Sousse；La Charguia 1→Tunis；核对 Ariana/Tunis 的 Charguia 歧义）。
4. 输出 schema：`{country_code: TN, country_name: Tunisia, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；阴性省在完成标准阴性清单后才写 `no_projects: true`。
5. 不动 explorer-*.md，NO-DELETION。

## 待办（2026-08-12）

- [ ] SoleCrypt Bizerte：核实施工、许可（permis de construire）、电网与环境记录后才升级 planned。
- [ ] TT Data Center Carthage：用主源确认精确地址；核实 TUV 证书详情。
- [ ] Ooredoo La Charguia 1：寻找运营商/INTT/议会证据升级站点 B→A。
- [ ] CNI 私有云实施站点：从 AfDB/MTC 授予文件中找实施地点。
- [ ] ATI 数据中心：寻找具体大厅/机架/电力证据。
- [ ] Sfax 深层扫描：确认是否命名物理设施，否则记录阴性。
- [ ] Medusa/Bizerte 登陆站状态与云区域阴性对照：每次运行复查。
