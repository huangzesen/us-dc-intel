---
name: cz-datacenter-methodology
location: scripts/expansion/world/country-skills/CZ/SKILL.md
description: |
  Czechia (CZ) data-center enumeration methodology. Division model: 14 manifest divisions (Prague; Central Bohemia; South Bohemia; Plzen; Karlovy Vary; Usti nad Labem; Liberec; Hradec Kralove; Pardubice; Vysocina; South Moravia; Olomouc; Zlin; Moravia-Silesia). No single public national building-permit registry; building-office evidence appears on municipal/city-district uredni deska pages, with CENIA EIA/SEA (portal.cenia.cz/eiasea), IPPC (ippc.mzp.cz), CUZK cadastre, ARES/justice.cz entities, CEPS/ERU/DSO (CEZ Distribuce, EG.D, PREdistribuce) grid records, CTU telecom, and NEN procurement as the official backbone. No Czech AWS/Azure/GCP/OCI public-cloud region or Local Zone on official pages (OVHcloud Prague official page exists). Market is Prague-centered colocation/interconnection with Brno and Ostrava secondary. Key seeds: T-Mobile DC7, TTC TELEPORT DC1/DC2, CE Colo, OVHcloud Prague, SafeDX, VSHosting, O2/CETIN, Coolhousing, MasterDC Brno/Kanice AI DC (planned autumn 2026), IT4Innovations VLQ/EuroHPC (public HPC), Datove centrum Monaco/SYNOT (B lead), Chomutov data hub (B lead), Equinix Prague (C lead). Read this before running CZ exploration/audit batches. Routes to explorer-official.md (CENIA/notice-board/grid/entity playbook) and explorer-industry.md (operator/association/press playbook).
---

# CZ · 捷克数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：捷克无单一公共国家建筑许可登记册，建筑许可证据通常出现在市/区级 úřední deska 页面，区域机关负责 EIA、规划、上诉与部分公告。普查以 CENIA EIA/SEA、IPPC、CUZK 地籍、ARES/justice.cz、电网（ČEPS/ERÚ/DSO）、ČTÚ、NEN 采购为官方骨架，与运营商/云/协会/媒体行业线索交叉。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：CENIA EIA、ERÚ/ČEPS/DSO、ČTÚ、NEN、CUZK、ARES/justice.cz、建筑办公室/公告板模板、计数与状态规则、14 分区逐区策略、云/运营商 pivot、陷阱 |
| `explorer-industry.md` | 行业/厂商管线：市场现实与计数姿态、云区域状态、运营商/设施种子表、行业协会（ASCDC/CSDIA/NIX.CZ）、HPC/研究/政府云、媒体与目录用法、待办诚实清单 |

## 核心结构事实（框定每次搜索）

1. 行政划分：**14 个 manifest 分区**：Prague、Central Bohemia、South Bohemia、Plzen、Karlovy Vary、Usti nad Labem、Liberec、Hradec Kralove、Pardubice、Vysocina、South Moravia、Olomouc、Zlin、Moravia-Silesia。分区行是路由指南而非设施计数。
2. **无单一公共国家建筑许可登记册**：建筑办公室证据在市政/城市区 `úřední deska` 页；区域机关用于 EIA、规划、上诉与选定的公告。布拉格须同时搜市与相关城市区（Praha 10、15、4、9 等）；布尔诺搜市政厅与相关城区。
3. **无捷克公共云区域**：官方 AWS/Azure/GCP/Oracle OCI 区域/本地区页均未确认捷克公共云区域（AWS 亦无 Local Zone）。不得把云销售点、CDN 节点、交换端口、网络 PoP 计为 DC 设施。`eu-prague-1` 类声明须对 Oracle 文档重查。OVHcloud Prague 有官方页面（https://www.ovhcloud.com/en/datacenter/europe/czech-republic/prague/）——核验其为完整 DC、Local Zone 还是特定产品地点。
4. 官方骨架：**CENIA EIA**（https://portal.cenia.cz/eiasea/view/eia100_cr，A；搜项目名、投资方 IČO、市镇、EIA 状态、发电机/冷却/电力描述）、**IPPC**（https://ippc.mzp.cz/，A；燃油储存、备用发电、排放/噪声）、**CUZK 地籍**（https://nahlizenidokn.cuzk.cz，A；地块/建筑/所有权/地役权 pivot）、**ARES**（https://ares.gov.cz，A；法人名/IČO/地址）、**justice.cz**（A；商业登记文件）、**ČTÚ**（https://www.ctu.cz，A；电信注册/决定，非 DC 登记册）、**NEN**（https://nen.nipez.cz，A；政府/大学/服务器机房/DC 采购）、**ČEPS/ERÚ**（https://www.ceps.cz、https://eru.gov.cz/plan-rozvoje-ps-cr-2025-2034、连接条例 vyhláška č. 16/2016 Sb.）、**DSO**：ČEZ Distribuce（https://www.cezdistribuce.cz）、EG.D（https://www.egd.cz，403 需浏览器）、PREdistribuce（https://www.predistribuce.cz，布拉格）。
5. 语言：先捷克语，带/不带变音符号都搜（旧 PDF OCR 差或无重音索引）：`datové centrum / datove centrum / datacentrum / datacentra / data centrum / datová centra / serverovna / serverovny / kolokace / housing / serverhousing / cloudové služby / hyperscale / hyperskalní datové centrum / stavba datového centra / úřední deska / verejna vyhlaska / veřejná vyhláška / stavební povolení / územní rozhodnutí / společné povolení / kolaudační souhlas / EIA / posouzení vlivů na životní prostředí / oznámení záměru / integrované povolení / IPPC / připojení k distribuční soustavě / sjednaný příkon / rezervovaný příkon / rozvodna / trafostanice / 110 kV / 400 kV / náhradní zdroj / dieselagregát / záložní zdroj / UPS / chlazení / free cooling / průmyslová zóna / brownfield`。设施文件常避免 `datové centrum`，可能描述为通用 `technologická budova / administrativní objekt / serverovna / trafostanice / strojovna chlazení / náhradní zdroj`。
6. 计数规则：**Operational** = 官方运营商设施页/公共机构页/kolaudační souhlas/绑定捷克地址的当前服务页；**Under construction** = 建筑许可或官方开工通知 + 项目身份；**Planned** = 官方公告 + EIA/规划/电网/土地证据；**Lead** = 媒体/协会/目录/采购意向/分区/电网申请/投资局提及而无足够官方项目证据；**不计** = CDN/边缘 PoP、云销售办公室、网络 PoP、仅互联在场、一般市场在场、投机电网需求、任何不在官方区域列表的 AWS/Azure/GCP/OCI 区域声明。

## 查询模式（复制粘贴模板见 explorer-official.md §3 与 explorer-industry.md §4）

- 建筑办公室/公告板：`"{municipality}" "datové centrum" "stavební povolení"`、`"{municipality}" "datacentrum" "územní rozhodnutí"`、`"{municipality}" "serverovna" "kolaudační souhlas"`、`"{legal_entity}" "kolaudační souhlas"`、`site:{municipality-domain} "datové centrum" "veřejná vyhláška"`、`site:{municipality-domain} "náhradní zdroj" "dieselagregát"`、`filetype:pdf "datové centrum" "stavební povolení" "{municipality}"`、`filetype:pdf "{address}" "stavební povolení"`。
- EIA/IPPC：`site:portal.cenia.cz/eiasea "datové centrum"`、`site:portal.cenia.cz/eiasea "{operator}"`、`site:portal.cenia.cz/eiasea "{municipality}" "datové centrum"`、`"{operator}" "integrované povolení"`、`site:ippc.cz "{operator}" OR "{municipality}" "náhradní zdroj"`。
- 能源/电网：`site:ceps.cz "datové centrum"`、`site:ceps.cz "připojení" "přenosová soustava"`、`site:eru.gov.cz "Plán rozvoje PS" "datové centrum"`、`site:cezdistribuce.cz "datové centrum" "připojení"`、`site:predistribuce.cz "datové centrum" "připojení"`、`"{municipality}" "datové centrum" "rozvodna"`、`"{operator}" "sjednaný příkon" OR "rezervovaný příkon"`、`"{substation}" "datové centrum" "MW" OR "MVA"`。电网事实与设施状态分开：`requested_connection_MW_or_MVA / connection_point / connection_status / permit_status / construction_status / operational_status`。
- 电信/采购/法人：`site:ctu.cz "{operator}" "datové centrum"`、`site:nen.nipez.cz "datové centrum"`、`site:nen.nipez.cz "serverovna"`、`site:nen.nipez.cz "vládní cloud"`、`site:ares.gov.cz "{legal_entity}" "{IČO}"`、`site:justice.cz "{legal_entity}" "datové centrum"`。
- 行业：`"datové centrum" "{city}" "kolokace"`、`"{operator}" "IČO" "datové centrum"`、`"datacentrum" "postaví" "Česko"`、`"AI datacentrum" "Česko"`、`"Chomutov" "datacentrum" OR "datový hub"`、`"Kanice" "MasterDC" "datové centrum"`、`site:ascdc.cz "člen" "datové centrum"`、`site:csdia.online "členové"`、`site:nix.cz "members" "Prague"`、`site:lupa.cz "datacentrum" "Česko"`、`site:oenergetice.cz "datacentra" "příkon"`、`site:datacenterdynamics.com "Czech" "data center"`。

## 官方/监管管线要点（详见 explorer-official.md）

- 提取字段：投资方、IČO、地块、建筑描述、IT 负荷或变压器容量、备用发电机容量、燃油储存、冷却系统、耗水、阶段计划、主管机关、决定/状态日期。
- 状态纪律：每个状态带来源日期或取回日期；2025 年目标开放 ≠ 2026 年运营，除非有启动/当前服务源确认。
- 陷阱：**Equinix Prague**（目录列 PR1/PR2，无官方 Equinix 布拉格地点页——保持 C/B 线索）；**OVHcloud Prague**（官方页存在，核验产品类型/地址）；**Chomutov**（B 线索，除非 EIA/许可/运营商文件确认实际项目、场地与状态）；**Kanice u Brna MasterDC**（官方博客为 B 项目公告，需市政/JMK/EG.D/许可证据确认在建或运营）；**HPC/公共设施**（IT4Innovations、CESNET、CERIT、政府云、医院服务器机房为有效基建记录，但 `facility_type=HPC/public/research/government`，不与商业 colo 混计）；**容量声明**（IT 负荷、总电气容量、申请电网容量、发电机容量、机架数分开，无来源支撑不得互转）。
- 官方流程：ARES/justice.cz 拉法人名与 IČO → CENIA EIA 按 datové centrum/datacentrum/serverovna/运营商/市镇/IČO 搜 → 区与市公告板搜许可生命周期词与地址/地块 pivot → CUZK 规范化地址/地块/所有权/地役权 → ČEPS/ERÚ 与相关 DSO 查连接/负荷语境 → ČTÚ 与 NEN 查电信/公共部门记录 → 按 §4 定状态与分级，未支撑线索进独立线索队列。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场现实：捷克主要是 Prague 中心的 colo 与互联市场，Brno 与 Ostrava 次级，其他地区零散企业/公共设施。官方 AWS/Azure/GCP/OCI 页面未确认捷克公共云区域。目录源（DataCenterMap、Baxtel、datacenters.com、PeeringDB、Inflect）为 C 级种子清单，常重复条目、保留旧品牌、从 PeeringDB 推断地址或混 PoP。
- 设施类别：`commercial_colocation / telecom_colocation / cloud_provider_datacentre_or_local_zone / enterprise_corporate / public_HPC_research / government_or_public_sector / network_pop_or_exchange_only / lead_unconfirmed`——仅前六类在证据充分时计数。
- 运营商/设施种子：**T-Mobile DC7**（Prague，K Pěrovně/Malešice-Hostivař 区；官方 PDF/页捕获才 A）；**O2 Czech Republic**（https://www.o2.cz/firmy-a-organizace/it-reseni/datove-centrum A；目录列 Prague/Brno 但地址需确认）；**CETIN**（https://www.cetin.cz/products-and-services/collocation A；全国网络 colo，仅计站点级记录）；**OVHcloud Prague**（A 种子）；**TTC TELEPORT**（https://ttc-teleport.cz/en/ A；Praha 10-Malešice，Tiskařská 257/10，DC1/DC2）；**CE Colo**（A 运营商存在；目录指向 Nad Elektrárnou 1428/47，地址需 CE Colo 材料或本地记录确认）；**SafeDX**（A；Prague-Vysočany）；**VSHosting**（A 种子）；**Coolhousing**（A；官方页称 Prague/Vinohradská 一个公共 DC + Brno/Cejl 私有 DC）；**MasterDC/Master Internet**（Kanice u Brna AI DC 目标 2026 秋——B 公告，planned/lead）；**IT4Innovations/VLQ/EuroHPC**（Ostrava；VLQ 2025 年安装/启用并入 Karolina——public_HPC_research，非商业 colo）；**CESNET/e-INFRA CZ**（国家研究/e-infra 语境，站点级证据才计数）；**ASCDC**（https://ascdc.cz A 协会事实，会员不证明设施）、**CSDIA**（https://www.csdia.online A/B）、**NIX.CZ**（https://nix.cz A 互联语境，在场非 DC 计数）；**Datové centrum Monaco/SYNOT**（Zlín/Uherské Hradiště；B/C 直到官方 SYNOT 页或许可）；**Equinix Prague**（C）；**Chomutov data hub**（B 线索）。
- 媒体（B）：Lupa.cz、iDNES.cz/ČTK、Hospodářské noviny（hn.cz）、Forbes.cz、Euro.cz、E15、CzechCrunch、oEnergetice.cz、Computerworld/Computertrends、DataCenterDynamics。目录（C）：DataCenterMap、Baxtel、datacenters.com、Data Center Platform、PeeringDB、Inflect。旧品牌（GTS/Telefonica）目录条目须经 ARES/justice.cz 与运营商页对账到现行法人。`will build / plans / is considering / could be` = lead/planned；`autumn 2026` 类目标日期在启动/当前服务源确认前仍是目标。

## 来源分级

- **A**：一手公共机关或官方运营商/云记录——市/区公告板、建筑办公室决定、CENIA EIA/SEA、IPPC、CUZK 地籍、ARES/justice.cz、ČEPS/ERÚ/DSO 文件、ČTÚ/NEN 记录、官方运营商页。
- **B**：强二手线索——成熟捷克或国际贸易媒体、无许可证据的运营商博客、不含许可/设施记录的投资局/新闻稿。
- **C**：弱线索——目录、地图、市场清单、社交、SEO 页、无来源容量声明。多个 C 级目录重复同一条目不得升格。设施仅在 A 级源确认场地、或 B 级运营商/媒体线索与官方许可/EIA/电网/地籍证据配对时才可计数。

## 使用流程（探索/复核批次）

1. 读本 SKILL.md 与两份 explorer 报告，确定目标分区与候选项。
2. 对每个候选：ARES/justice.cz 法人/IČO → CENIA EIA → 区/市公告板 → CUZK → ČEPS/ERÚ/DSO → ČTÚ/NEN。
3. 按计数规则定状态与分级；未支撑线索进线索队列。
4. 14 分区全跑（含低密度分区），HPC/公共设施标记 `public_HPC_research/government` 分开。
5. 云区域每轮重查官方列表（含 AWS Local Zones、`eu-prague-1` 类声明）。
6. 遵守 NO-DELETION；不改写 explorer-*.md。

## 待办（2026-08-12 03:16Z）

- [x] 合并两份探索报告为 SKILL.md + ANATOMY.md。
- [ ] T-Mobile DC7：捕获/归档官方手册页，用 Prague 许可与 PREdistribuce pivot 核验扩张史。
- [ ] MasterDC Kanice：许可/EIA/EG.D 确认（在建或运营前）。
- [ ] Chomutov data hub：CENIA、Chomutov/Ústecký 公告板、CzechInvest/市政、电网确认。
- [ ] 待核实：Datové centrum Monaco/SYNOT 官方确认；Equinix Prague 官方/本地证据；OVHcloud Prague 产品类型与地址。
