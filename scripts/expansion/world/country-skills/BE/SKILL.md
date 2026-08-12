---
name: be-datacenter-methodology
location: scripts/expansion/world/country-skills/BE/SKILL.md
description: |
  Belgium (BE) datacenter discovery & audit methodology — how to enumerate, verify, and update Belgian datacenter projects at region + municipality granularity (3 regions: Brussels-Capital, Flanders, Wallonia in the current manifest). Belgium has no national datacenter register: enumeration joins regional permits (Brussels urbanism/environment, Flanders omgevingsvergunning, Wallonia permis unique/environnement), Elia + DSO grid evidence (Fluvius/Sibelga/ORES/RESA), KBO-BCE company records, official cloud-region pages (Azure Belgium Central; Google St. Ghislain/Farciennes), procurement (BOSA/TED), and operator pages (KevlinX, Datacenter United, LCL, Digital Realty, Penta Infra) plus BDIA. Read this before running BE exploration/audit batches. Routes to explorer-official.md (permits/energy/registries/cloud/procurement) and explorer-industry.md (operators/IXP/cables/directories).
---

# BE · 比利时数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：比利时**没有**全国数据中心注册库；枚举必须联合三大区（Region）许可、区/联邦能源证据、联邦公司法/公报、云区域官方页、运营商页、IXP 与采购信号。按**市镇**归属设施，不用营销性“布鲁塞尔”标签——Zaventem、Diegem/Machelen、Aalst、Huizingen、Asse 均属 **Flanders** 而非 Brussels-Capital。
> 分区模型：**3 个大区**——Brussels-Capital（19 市镇）、Flanders（含机场环带 Zaventem/Machelen/Asse、Antwerp、Ghent、Aalst、Hasselt、Mechelen、Oostkamp/Bruges）、Wallonia（Hainaut/Liege/Namur/Luxembourg/Walloon Brabant；德语区在内）。
> 已知种子：Google St. Ghislain + Farciennes（Wallonia）、Azure Belgium Central（2025-11-18 开放，地址未公开）、KevlinX BRU01（Neder-Over-Heembeek，32 MW+）、Datacenter United 14 座 DC/12 址（含 Evere）、LCL 五座（Diegem/Aalst/Huizingen/Antwerp/Gembloux）、Digital Realty BRU1/BRU3/BRU4（Zaventem）、Penta Infra BRU01（Asse/Zellik）、Etix Liege。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供比利时探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：KBO-BCE/公报/GBA/CCB、BIPT/BELNET/BNIX、Elia/CREG + Fluvius/Sibelga/ORES/RESA + VREG/BRUGEL/CWaPE、三区许可面（urban.brussels/MyPermit、Omgevingsloket/Inzageloket、SPW/TWICE/Wallex）、云区域官方页（Azure/Google/AWS/Oracle/IBM 负向）、BOSA/TED 采购、三区逐区工作流、生命周期计数规则 |
| `explorer-industry.md` | 行业/厂商发现：BDIA 协会/报告、运营商枢纽表（Microsoft/Google/DCU/LCL/Digital Realty/KevlinX/Penta/Combell/Cegeka/Orange/Proximus/Etix）、BNIX/BelgiumIX/AMS-IX/DE-CIX/NL-ix/PeeringDB 互连、目录（C）、Oostende/Zeebrugge 海缆邻接、搜索模板、证据规则 |

## 核心结构事实（框定每次搜索）

1. **三区许可路径是官方主控线**：Brussels 分城市规划许可（urban.brussels/MyPermit，CoBAT）+ 环境许可（Brussels Environment）；Flanders 用一体化 **omgevingsvergunning**（Omgevingsloket/Inzageloket 公开查询）；Wallonia 用 **permis d'environnement / permis d'urbanisme / permis unique**（SPW、twice.spw.wallonie.be、Wallex）。
2. **“布鲁塞尔”市镇陷阱**：运营商/目录的 “Brussels” 常指 Zaventem（Digital Realty BRU1/3/4）、Diegem/Machelen（LCL Brussels-North）、Aalst（LCL Brussels-West）、Huizingen（LCL Brussels-South）、Asse/Zellik（Penta BRU01）——全部按地址归 **Flanders**；仅 KevlinX BRU01 与 DCU Evere 等在 Brussels-Capital。Mouscron/Moeskroen（7700）属 Wallonia（Hainaut）。
3. **电网证据重要但不等同许可**：Elia（高压/超大规模）+ Fluvius（Flanders 拥塞/弹性接入）、Sibelga（Brussels 19 市镇）、ORES/RESA（Wallonia）；提取 `aansluitvermogen`/`puissance de raccordement`、MVA/MW、`hoogspanningsstation`、`flexibele aansluiting`/`raccordement flexible`、拥塞区、备用发电/余热义务。
4. **云区域官方页强种子但非设施**：Azure **Belgium Central**（2025-11-18 开放，物理地址未公开，U 分配）；Google St. Ghislain（europe-west1）+ Farciennes 建设 + 2025 年 EUR 5B 投资声明；AWS/Oracle/IBM 无比利时区域（每批负向核验）。
5. **法人核验走 KBO-BCE**：按法定名与商号搜 `LCL Belgium`、`Datacenter United`、`KevlinX`、`Google Belgium`、`Microsoft`、`Proximus`、`Interxion`、`Digital Realty`；企业事件（收购/出售）用官方公报（ejustice）。
6. **IXP 只证互连**：BNIX（BELNET 运营，1995 年成立，Brussels 周边 5 处 PoP）、BelgiumIX、AMS-IX/DE-CIX where-to-connect、PeeringDB（B/U）；IXP 交换节点 ≠ 数据中心，须映射宿主设施地址到市镇。
7. **所有权变化防重复计数**：Proximus 2024-10 宣布将四座数据中心售予 Datacenter United（2025 Q1 完成）；旧 Proximus 列表可能已由 DCU 运营；DCU 声明 14 座 DC/12 个比利时地点。
8. **语言**：荷兰语 `datacentrum/datacentra/serverruimte/colocatie/omgevingsvergunning/openbaar onderzoek/netaansluiting/netcongestie`、法语 `centre de données/salle de serveurs/permis d'urbanisme/permis d'environnement/permis unique/enquête publique/raccordement`、英语、德语（仅德语区）均需覆盖。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§4 / explorer-industry.md §6）

- Brussels 许可：`site:urbanisme.irisnet.be datacenter OR "centre de données"`、`site:environment.brussels datacenter "permis d'environnement"`、`"KevlinX" "Neder-Over-Heembeek" permis OR vergunning`、`site:{commune}.brussels datacenter permis`。
- Flanders 许可：`site:omgevingsloketinzage.omgeving.vlaanderen.be datacenter OR datacentrum`、`"datacenter" "omgevingsvergunning" "Zaventem" OR "Machelen" OR "Diegem"`、`"Digital Realty" "Zaventem" omgevingsvergunning`、`"LCL" "Aalst" "omgevingsvergunning"`。
- Wallonia 许可：`site:wallonie.be datacenter "permis unique"`、`site:twice.spw.wallonie.be Google Farciennes`、`"Google" "Farciennes" "permis unique" "conditions"`、`"centre de données" "enquête publique" "Farciennes" OR "Saint-Ghislain"`。
- 电网：`"datacenter" "netcongestie" België OR Vlaanderen`、`site:elia.be datacenter`、`site:fluvius.be datacenter OR netcongestie`、`site:sibelga.be datacenter`、`site:ores.be OR site:resa.be datacenter`。
- 采购：`site:publicprocurement.be datacenter OR datacentrum OR "centre de données"`、`site:publicprocurement.be colocation OR colocatie OR hébergement`、`site:ted.europa.eu Belgium datacenter colocation hosting cloud`。
- 云：`site:datacenters.google/locations/belgium`、`"Belgium Central" Azure`、`site:aws.amazon.com Belgium "Region"`、`site:oracle.com Belgium "public cloud region"`。
- 行业/互连：`site:datacenterdynamics.com Belgium data center`、`site:brusselstimes.com "data center" Belgium`、`site:bdia.be datacenter Belgium operator`、`site:bnix.net Brussels PoP datacenter`、`site:peeringdb.com/fac Belgium Brussels Zaventem BNIX`、`"Proximus" "Datacenter United" datacenters sale leaseback`。

## 官方/监管管线要点（详见 explorer-official.md）

- 入口：先区级官方搜索（三区许可面）→ 按市镇钻取公开调查（openbaar onderzoek/enquête publique、市政议程）→ Elia/区 DSO 电网 → KBO-BCE/公报法人 → BNIX/运营商页仅证互连/在售存在。
- 电网：Fluvius 拥塞/Fall-Back Flex、Sibelga 服务 19 市镇、ORES/RESA 分区；Elia 连接队列与高压扩容（Hainaut/Charleroi 周边）为超大规模项目状态过滤器。
- 计数规则：`aanvraag/demande/openbaar onderzoek` = 管线不入账；`vergunning verleend/permis accordé` = 计划/已许可入账；建设中需运营商/承包商公告 + 许可；运营需运营商页/云位置页/IXP PoP/采购授标；扩建按扩建计；拒绝/撤销不计。
- 不计数：云区域本身、边缘 PoP/IXP 交换机（除非指明宿主设施）、仅目录条目、同址多品牌（除非独立建筑）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 运营商枢纽：Microsoft（Azure Belgium Central，A 区域/U 建筑）、Google（St. Ghislain A、Farciennes B、EUR 5B A）、Datacenter United（A，14 DC/12 址）、LCL（A，五座全在比利时）、Digital Realty BRU1/BRU3/BRU4（A，Zaventem 地址）、KevlinX BRU01（A/B，32 MW+、BESIX 2025-12 移交、DCD ready-for-service）、Penta Infra BRU01（A 存在/U 精确市镇）、Combell（A 服务/U 设施）、Cegeka（A/U）、Orange Belgium Hoboken（B/C）、Proximus（B 历史）、Etix Liege/Villers-le-Bouillet（A/C）、Equinix（U，无现行比利时 IBX 页确认）。
- 协会/市场：BDIA（B+，State of Belgian Data Centres 2025、database/map 作种子）、Agoria（B）、Digital Wallonia/ADN（B/A）。
- 媒体：DCD、Brussels Times、L'Echo/De Tijd、DataNews/Le Vif、ITdaily、Computable、TechPulse、RTBF/VRT/Belga（B）。
- 目录（C，仅种子）：DatacenterMap Belgium、Baxtel、datacenters.com、DataCenterPlatform、DataCenterCatalog、Cloudscene/Ocolo/Upstack、市场报告（Arizton 等）。
- 海缆：Oostende/Zeebrugge 着陆点为邻接信号，非数据中心证据（TeleGeography B）。

## 已知设施/项目与证据状态

| 设施/项目 | 大区/市镇 | 状态与证据 |
|---|---|---|
| Google St. Ghislain | Wallonia/Saint-Ghislain | A（Google 官方位置页 + Google Cloud europe-west1）；EUR 5B 扩建声明 A |
| Google Farciennes 园区 | Wallonia/Farciennes | B（DCD/Brussels Times：2024 开工、EUR 1B）；最终许可须 SPW/Wallex 记录（U/A 待证） |
| Microsoft Azure Belgium Central | 大区级（Brussels 官宣） | A（区域 2025-11-18 开放）；物理建筑地址未公开（U） |
| KevlinX BRU01 | Brussels-Capital/Neder-Over-Heembeek | A（运营商页 32 MW+）+ B（BESIX 2025-12 移交、DCD ready-for-service）；许可号待 Brussels 官方查证（U） |
| Datacenter United DC Evere | Brussels-Capital/Evere | A（运营商页存在）；地址/许可待证（U） |
| Digital Realty BRU1 | Flanders/Zaventem | A（运营商页 Wezembeekstraat 2, 1930，5,000 m²） |
| Digital Realty BRU3/BRU4 | Flanders/Zaventem | A（运营商页 Mercuriusstraat 27, 1930；1,470 / 6,700 m²） |
| LCL Brussels-North | Flanders/Diegem | A（LCL FAQ/联系页 Kouterveldstraat 13, 1831） |
| LCL Brussels-West / Brussels-South / Antwerp | Flanders/Aalst、Huizingen、Antwerp | A（LCL FAQ/新闻）；地址与许可分别确认 |
| LCL Wallonia One | Wallonia/Gembloux | A（LCL 收购 ENGIE Solutions 数据中心并更名） |
| Datacenter United Antwerp/Machelen/Ghent/Mechelen/Hasselt/Oostkamp-Bruges | Flanders 各市镇 | A（运营商页）；逐一确认地址/许可（U） |
| Datacenter United Moeskroen/Mouscron | Wallonia/Mouscron（7700） | A/U（运营商页 coming soon；按地址归 Wallonia） |
| Penta Infra BRU01 | Flanders/Asse-Zellik 线索 | A（运营商页确认 Brussels 市场设施）；精确市镇/地址待钉（U） |
| Etix Belgium DC 1 | Wallonia/Liege 市场、Villers-le-Bouillet 地址线索 | A/C（官方页证存在；目录给 Rue de la Science 3, 4530；地址/许可待证） |
| Combell colocation | Flanders/Ghent 线索 | A（服务）/U（设施详情） |
| Cegeka | Flanders/Hasselt 线索 | A/U（企业/云提供商；设施级证明待补） |
| Orange Belgium Hoboken | Flanders/Antwerp-Hoboken | B/C（2019 开业报道）；现行状态待证 |
| Proximus 售予 DCU 的四座 DC | Brussels/Flanders 历史 | B（历史线索，非现行所有者，防重复计数） |
| BNIX / BelgiumIX PoP | Brussels 及周边 | A/B（IXP 页）；计宿主设施而非交换节点 |
| BELNET/Smals/CIRB 等政府设施 | Brussels | U（设施级公开信息稀少） |

## 更新节奏

- 每批次：云区域负向核验（Azure/Google/AWS/Oracle/IBM）、DCU/LCL/Digital Realty/KevlinX/Penta 运营商页、Google Farciennes 许可进展、KevlinX 许可号。
- 月度：publicprocurement.be/TED、三区许可搜索、Elia/DSO 电网与拥塞新闻、DCD/Brussels Times。
- 季度：运营商位置页、BNIX/BelgiumIX/AMS-IX/DE-CIX/NL-ix/PeeringDB、DatacenterMap/Baxtel/datacenters.com、BDIA map/database。
- 待办（2026-08-12）：两份 explorer 初稿已完成（codex 复核）；下一步 codex terra agent 分批复核（3 大区粒度）；本 skill 作为国家层参考注入。
