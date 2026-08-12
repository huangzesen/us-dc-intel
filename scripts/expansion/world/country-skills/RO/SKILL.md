---
name: ro-datacenter-methodology
location: scripts/expansion/world/country-skills/RO/SKILL.md
description: |
  Romania (RO) datacenter discovery & audit methodology — how to enumerate, verify, and update Romania datacenter projects at county (judet) + Bucuresti municipality granularity (41 counties + Bucuresti in the current manifest). Romania has no single public national datacenter registry: enumeration joins decentralized local construction permits (municipality/city/commune registers, CU/AC/PUZ/PUD), ANMAP/ANPM county environmental files, SEAP/SICAP (e-licitatie) procurement, Transelectrica/ANRE/DSO connection evidence, ADR/STS government-cloud and regional-program pages (Cloudul Privat Guvernamental — Bucuresti, Timisoara/Giroc, Brasov/Cristian, Sibiu; STS CDS II Sibiu; Centrul de Date Regional Sud-Muntenia), official cloud-region checks (no RO hyperscale region; Google Cloud Interconnect NXDATA-1 Bucharest BU1 is an A-grade seed), and operator pages (NXDATA, GTS, Voxility, Orange/ex-Telekom, Portland Trust, HZone, DataPark, Pidgin Host, INVITE, Digital Cuisine). Romanian terms matter (centru de date, autorizatie de construire, certificat de urbanism, acord de mediu, racordare la RED/RET); CU is not a build right. Watch legacy aliases (Telekom Romania Communications = Orange since 2021) and Bucharest-vs-Ilfov physical assignment. Read this before running RO exploration/audit batches. Routes to explorer-official.md (permits/environment/energy/procurement/regulator/cloud/divisions) and explorer-industry.md (operators/trade press/directories/cloud-edge/county sweeps/upgrade path).
---

# RO · 罗马尼亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：罗马尼亚**没有**统一的全国数据中心注册库；枚举靠**拼接**分散的地方建筑许可、ANMAP/ANPM 县级环境文件、SEAP/SICAP 采购、Transelectrica 与 DSO 并网证据、ADR/STS 政府云与区域项目页、运营商页与贸易媒体。
> 建筑许可分散：记录单位通常是市镇/城市/公社/县议会或布加勒斯特分区；**无波兰式全国建筑检索**。罗马尼亚语先行：`centru de date` `centru de procesare date` `centru de servicii IT&C` `camera servere` `colocare` `cloud` `racordare la RED/RET` `post trafo` `statie 110/20 kV` `grup electrogen` `UPS` `climatizare`。
> `Certificat de urbanism`（CU）只是规划/通知前体，**不是建筑权**；`autorizatie de construire`（AC）、环境决定/`acord de mediu`、采购中标、运营商启用或明确的公共业主公告才算更强。
> 公共部门数据中心重要：STS、ADR、县议会、部委、大学/研究所、BNR、公用事业与政府云项目常产生大型或战略性设施，不出现在商业 colo 目录。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供罗马尼亚探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：分散建筑许可注册（Constanta/Brasov/Sibiu/Alba Iulia 可检索注册表、PMB UrbOnline、Sector 3 CU_02.2025 范例、县议会 HCL/HCJ）、ANMAP/ANPM 县级环境页（Teleorman Class IT Outsourcing 范例）、Transelectrica/ANRE/DSO 电网（ATR、容量分配 ≥5 MW）、SEAP/e-licitatie + TED + ADR 政府云与区域项目（CPG 四节点、STS CDS II Sibiu、Sud-Muntenia 区域 DC）、ANCOM 电信监管、云区域官方核查（Google Interconnect NXDATA-1 为硬种子）、分区枚举法（Bucuresti-Ilfov/Dolj-Valcea/Timis/Brasov-Sibiu/Cluj-Mures/Prahova-South-Muntenia 等）与可靠性计数规则 |
| `explorer-industry.md` | 行业/厂商发现：DataCenter Forum Romania/Data Center Nation/CBRE/Panorama/Business Forum 生态、DCD/Profit.ro/Economica/ZF/Balkan Green Energy News 媒体、目录（Baxtel/Data Center Map/Datacenters.com/Inflect/DC Hub/PeeringDB）、运营商/项目种子表（Bucuresti-Ilfov：NXDATA-3 Tunari BUH3 5 MW/GTS Rahovei 2 MW/Voxility IR2/Orange/Portland Trust Preciziei/Microsoft Otopeni 许可线索/Solidus/Kyndryl；政府云与 STS；Dolj-Valcea ClusterPower 800 MW 与 Fauresti；Timis SANY 70 MW/Giroc；Cluj GTS/DriverAI Luna 80 MW；Mures Vidrasau；Bihor HZone；Iasi DataPark；Giurgiu Pidgin Host；Prahova INVITE；Tulcea DANUBIUS-RO 等）、云/边缘/互联解读（无 RO 区域、Equinix 负面核查）、三遍县扫描、别名与重复控制、线索升级路径 |

## 核心结构事实（框定每次搜索）

1. **许可分散，注册表是 A**：Constanta `Registrul de autorizatii in constructii`、Brasov/Sibiu/Alba Iulia 可检索 AC 注册表、PMB urbanism（urbanism.pmb.ro）、Sector 1-6 门户（Sector 3 见 `racordare la RED centru de date` CU_02.2025.pdf）、县议会 `Monitorul Oficial al Judetului`/HCL/HCJ；从 CU/AC/PUZ/PUD 提取机构/文件号/申请人（titular）/工程标题/地址/地籍号/地块/有效期/功能/层高/面积/电网工程/变压器/发电机/冷却/消防线索；真实项目可写作 `imobil cu destinatie speciala`、`spatiu tehnic`、`modernizare infrastructura IT`、`racordare la RED`、`post trafo`——不要只按 `centru de date` 过滤。
2. **环境是高出产**：数据中心触发柴油备用发电机、燃料库、噪声、空气排放、HVAC、电池/UPS、用水/冷却、电网工程等可发布线索；ANMAP（2025 取代/吸收 ANPM）新旧域名都搜（`djmtr.anmap.gov.ro`、`apmb.anpm.ro`、`apmtm.anpm.ro` 等）；提取 `memoriu de prezentare`、`decizia etapei de incadrare`、`acord de mediu`/`aviz de mediu`、项目标题/受益人/场地/面积/发电机功率/油箱/冷却/噪声缓解/并网工程；范例：Teleorman `SC Class IT Outsourcing SRL` Alexandria（Str. Turnu Magurele nr. 4），县 ANMAP + 市 AC 交叉核验模型。
3. **生命周期词与状态规则**：`PUZ/PUD/PUG/CU` < `solicitare acord de mediu/memoriu` < `decizie etapa de incadrare/acord de mediu` < `autorizatie de construire` < `licitatie proiectare si executie` < `lucrari/receptie` < `punere in functiune/inaugurare/operational`；Planned=CU/融资分配/可研/非约束公告；Approved=环境决定/AC/签署的公共融资或采购合同；Construction=运营商/贸易/地方当局称开工或工程合同已授；Operational=运营商页/STS 公告/Uptime/PeeringDB/互联/公开启用。
4. **政府云与 STS 锚点（A）**：ADR `Cloudul Privat Guvernamental`——Bucuresti、Timisoara/Giroc、Brasov/Cristian、Sibiu 四节点（设计 2×Tier IV + 2×Tier III；Cristian 与 Giroc 已完成，Bucuresti 与 Sibiu 完成中）；STS `CDS II Sibiu`（Uptime 佐证）；ADR Sud-Muntenia 战略项目 `Centrul de Date Regional Sud-Muntenia`（STS 主导、>EUR 47m、七县参与——物理设施可能只在 Ploiesti/Prahova，伙伴县是服务受益方，不得重复计数）。
5. **电网（Transelectrica/ANRE/DSO）**：RET=110 kV 以上国家战略输电网；容量分配流程主要面向 ≥5 MW 新发电/储能站点（DC 捆绑发电/BESS/私营电站时相关）；DSO：Retele Electrice Muntenia/Banat/Dobrogea、DEER、Delgaz Grid、Distributie Oltenia、Premier Energy；字段分开：`requested_connection_MW`、`ATR_status`、`connection_voltage`、`substation`、`DSO/TSO`、`generation_or_BESS_component`；发电/储能拍卖与 ATR 申请**不证明数据中心**（SANY/ClusterPower/VLA Energy/Resita 型线索须单独验证 DC 组件许可）。
6. **云区域（负面核查 + 硬种子）**：AWS/Azure/Oracle 官方列表无 RO 区域（AWS 布加勒斯特办公室、Microsoft/Otopeni 土地=许可线索，不作区域）；Google Cloud 把布加勒斯特列为网络边缘 metro 且 `NXDATA-1 Bucharest Romania (BU1)` 为 Cloud Interconnect 设施（A=互联存在 + NXDATA 硬种子，非 Google 自有区域）；Equinix 官方位置无罗马尼亚——目录/旧页提到 Equinix Romania 多为过时/无关。
7. **运营商种子（A=自我描述存在，B=容量）**：NXDATA（NXDATA-1 BU1 互联；NXDATA-3 BUH3 Tunari 38 Bucharest Ring Road，5 MW 装机/3 MW IT，目标 2026 Q4）、GTS（Bucuresti Electromagnetica Business Park Calea Rahovei 266-268 2 MW/240 racks + Cluj Liberty Technology Park Strada Garii 21 500 kW/60 racks，Tier III/TIA 942）、Voxility（IR2 Dimitrie Pompeiu 1 MW）、Orange/ex-Telekom/NCC Balcan-IX（2021 收购后旧条目=别名历史）、Portland Trust（Bucuresti 三址，DC1/Strada Releului、DC2/Bd. Timisoara/Preciziei，20-30 MW 线索，B 级待官方细节）、Solidus Ai Tech（8 MW Bucharest 目标 2026 Q4，C）、Kyndryl（Soseaua Orhideelor，C）、HZone Oradea（A）、DataPark Miroslava（A）、Pidgin Host Bacu Giurgiu（A）、INVITE Ploiesti backup DC（A）、Digital Cuisine Ramnicu Valcea（A）、ClusterPower（Mischii 2022 启用 + AIC 2025-12 宣布 Mischii/Fauresti 800 MW AI 区域——B 待地方官方记录）、SANY Timis 70 MW DC 组件（B 计划）、DriverAI Luna Cluj 80 MW “quantum AI”（B/C，PressOne 警示诉讼/未签协议）、Vidrasau/Mures 工业园（B）、Tenaris Silcotub Zalau（A/B 企业）、DANUBIUS-RO Murighiol（研究，B/A）、TAZ IT Targu Mures（A 公司声明）、Resita Data（B/C 早期计划，ATR 进行中）。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§4 / explorer-industry.md §1/§2）

- 许可/地方：`"centru de date" "{judet}" "autorizatie de construire"`、`"centru de date" "{municipiu}" "certificat de urbanism"`、`"centru de date" "{comuna}" "PUZ" OR "PUD"`、`site:{primarie-domain} "centru de date" "autorizatie"`、`site:{judet-domain} "centru de date" "parteneriat" "STS"`、`filetype:pdf "centru de date" "certificat de urbanism"`、`site:urbanism.pmb.ro "centru de date"`。
- 环境：`site:anmap.gov.ro "centru de date" "{judet}"`、`site:{county-code}.anmap.gov.ro "centru de date"`、`site:apmb.anpm.ro "centru de date"`、`"centru de date" "decizia etapei de incadrare"`、`"centru de date" "memoriu de prezentare"`、`"centru de date" "Acord de mediu"`。
- 采购/电网：`site:e-licitatie.ro "centru de date" "{judet}"`、`site:e-licitatie.ro "centru de date sustenabil"`、`site:e-licitatie.ro "Centrul de Date Regional"`、`site:transelectrica.ro "centru de date"`、`"centru de date" "Transelectrica" "MW"`、`"centru de date" "racordare la RED" "{municipiu}"`、`"centru de date" "statie 110/20 kV" "{judet}"`。
- 政府云/公共：`site:adr.gov.ro/cpg "centre de date"`、`site:sts.ro "centru de date" Sibiu OR Brasov OR Timisoara`、`"Centrul de Date Regional Sud-Muntenia" STS Ploiesti Prahova`、`site:2021-2027.adrmuntenia.ro "Centrul de Date Regional"`、`site:e-licitatie.ro "Cloud Privat Guvernamental"`、`"BNR" "Targu Jiu" "centru de date"`。
- 运营商（Bucuresti-Ilfov）：`"NXDATA-3" Tunari "Bucharest Ring Road" "5 MW"`、`"NXDATA-1" "Google Cloud Interconnect" "BU1"`、`"GTS Bucuresti" "Calea Rahovei" "2MW"`、`"Voxility IR2" "Dimitrie Pompeiu" "1 MW"`、`"Portland Trust" "Strada Releului" "centru de date"`、`"Microsoft" Otopeni "centru de date" "certificat de urbanism"`。
- 能源园区/区域：`"ClusterPower" Mischii Craiova "centru de date"`、`"ClusterPower" "AIC" "800MW" Romania`、`"ClusterPower" Fauresti Valcea`、`"SANY" Timisoara "70 MW" "data center"`、`"DriverAI" Luna Cluj "80MW"`、`"GTS Cluj-Napoca" "Strada Garii 21" "500kW"`、`"Vidrasau" "Parcul Industrial Mures"`、`"HZone" Oradea "Calea Borsului"`。
- 英文/云：`"Romania" "data center" "building permit"`、`"Bucharest" "data center" "110/20 kV"`、`site:docs.cloud.google.com "NXDATA-1 Bucharest Romania"`、`site:aws.amazon.com "Bucharest" "Local Zone"`、`site:equinix.com "Romania" "Bucharest"`。
- 行业：`site:datacenterdynamics.com Romania data center Bucharest ClusterPower NXDATA SANY Portland`、`site:profit.ro "centru de date" STS Portland Microsoft`、`site:balkangreenenergynews.com Romania data center SANY`、`site:panorama.ro centre-de-date`。

## 官方/监管管线要点（详见 explorer-official.md）

- 许可：市政/城市/公社建筑注册表（A）；布加勒斯特城与分区门户（Sector 3 等）；县议会/地方议会（Monitorul Oficial al Judetului、HCL/HCJ）；ANCPI/eTerra/geoportal 只作候选地址/地块已知后的上下文。
- 环境：ANMAP（新）+ ANPM 旧域名；Atlas Explorer（上下文）；环境部（法律/过程/敏感区）；ANMAP + 市 AC 交叉核验是模型。
- 电网：Transelectrica（RET 地理/变电站邻接 + 容量分配流程）、ANRE（并网规则/ATR/证书）、各 DSO；能源证据找大项目但字段分开；发电/储能拍卖不证明 DC。
- 采购：SEAP/SICAP（e-licitatie，A）、TED（A/B）、ADR（CPG，A）、ADR 区域项目页（Sud-Muntenia，A）、部委/研究项目页；高产量词：`centru de date`、`centru de date sustenabil/container`、`Centrul de Date Regional`、`Cloud Privat Guvernamental`、`proiectare si executie`、`dotare centru de date`、`camera servere climatizare`、`grup electrogen UPS`。
- 电信：ANCOM（市场结构/运营商/网络光纤上下文，非 DC 许可库）；识别 Orange、DIGI、Vodafone、Telekom/Orange 固网资产、GTS、Euroweb、M247、NXDATA 相关网络与 IX/互联设施。
- 云：AWS/Azure/Oracle 负面核查；Google Bucharest 边缘/互联（A）；`NXDATA-1 BU1` 硬种子；Microsoft/Otopeni 许可线索。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 生态/媒体：DataCenter Forum Romania（B，赞助商/讲者表揭示运营/顾问/承包商/能源厂商/公共部门）、DCD（B，Portland Trust/ClusterPower-AIC/SANY/Orange Timisoara solar/Resita）、Profit.ro（B）、Economica/Economedia/ZF/Romania Insider（B）、Balkan Green Energy News（B，能源链接项目）、Panorama（B，调查）、The Tech Capital/Baxtel News（B/C）、本地媒体 radiomures/ramnicuvalceaweek/graiul（B/C）、CBRE（C，市场咨询）。
- 目录（C/C+）：Baxtel（C+，大型项目线索+布加勒斯特地图）、Data Center Map（C+，旧 colo 地址/Orange-Telekom legacy）、Datacenters.com（C）、Inflect（C+，Orange/WhiteHat 地址载波线索）、DC Hub/ColoMap/DataCenterCatalog/DataCenterPlatform（C，区域小 colo 种子）、PeeringDB（B/C，互联信号）。
- 升级路径：每条行业线索争取 ≥2 类独立证据：① 运营商/当前业主页或官方云/互联页；② 本地 AC/CU/PUZ/PUD 或 ANMAP 环境文件；③ SEAP/TED 招标、公共融资合同或县议会决议；④ 电力/电网证据（ATR、DSO/TSO、变电站、请求 MW）；⑤ 贸易媒体仅用于时间/容量/管线上下文。
- 别名与重复控制：Orange/Telekom/Romtelecom/NCC Balcan-IX 归一（2021 收购，同址新旧名不双计）；Bucharest vs Ilfov 按物理地址归派（Tunari/Otopeni/Chiajna/Voluntari/环线市镇）；Sud-Muntenia 区域 DC=宿主县一个物理设施，伙伴县仅受益；政府云四节点与区域 DC 不混；能源园区（ClusterPower/SANY/VLA/Resita）只计被点名且状态可分离的 DC 组件；目录按地址/运营商/IX 合并去重。

## 来源分级

- **A** = 官方/一手：运营商官方设施页、匹配数据中心标题的本地 AC/CU、点名数据中心的 ANMAP 环境决定、SEAP 数据中心建设/设备合同/中标、STS/ADR/政府云官方页、Uptime/官方认证（具名设施）、官方云/互联页（如 Google NXDATA-1 BU1）。
- **B** = 强二级：DCD、Profit.ro、Economica、Balkan Green Energy News、Romania Insider、Business Forum、Panorama、DataCenter Forum、具名官员的本地媒体、厂商案例（Tema Energy、Datanet）。
- **C** = 弱线索：Baxtel、Data Center Map、Datacenters.com、Inflect、DC Hub、ColoMap、DataCenterCatalog、通用市场报告；作地址/运营商种子，用官方/运营商证据升级。
- **不计数**：云销售办公室、软件工程办公室、无设施证据的通用托管公司、未作为数据中心营销的电信 POP、仅参与区域云项目的县（除非宿主物理设施）、DC 组件纯属推测的电网/发电项目。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=RO，divisions=41 县 + Bucuresti 市；manifest 用 ASCII 县名，搜索时加罗马尼亚语变音符变体）。
2. 建种子：运营商页（NXDATA/GTS/Voxility/Orange/Portland Trust/HZone/DataPark/Pidgin Host/INVITE/Digital Cuisine）+ 地址 pivot（Bd. Timisoara、Preciziei、Releului、Dimitrie Pompeiu、Calea Rahovei、Calea Borsului、Strada Garii 21、Tunari ring road）+ 政府云四节点 + 谷歌互联 NXDATA-1。
3. 每县五步：① 县/市镇域名查 `centru de date`+autorizatie/CU/PUZ/PUD/hotarare/registru；② 县 ANMAP/旧 ANPM 域名查 centru de date/grup electrogen/UPS/statie 110-20/racordare；③ SEAP 查县/市/STS/大学/县议会/公用事业；④ DSO 领地与电力线索，≥110 kV 或捆绑能源园区时升级 Transelectrica；⑤ 运营商/贸易线索对照官方记录后再升级置信度。
4. 三遍县扫描：Pass 1 高概率（Bucuresti-Ilfov/Dolj/Valcea/Timis/Brasov/Sibiu/Cluj/Mures/Prahova/Iasi/Bihor/Giurgiu）；Pass 2 公共/研究/企业或目录仅线索（Bacau/Braila/Buzau/Caras-Severin/Constanta/Galati/Gorj/Harghita/Mehedinti/Maramures/Salaj/Tulcea/Teleorman）；Pass 3 负面控制县（Alba/Arges/Bistrita-Nasaud/Botosani/Calarasi/Covasna/Dambovita/Hunedoara/Ialomita/Neamt/Olt/Satu Mare/Suceava/Vaslui/Vrancea 等——不得仅英文/目录搜索后标 no_projects，须罗马尼亚语地方与环境查询）。
5. 状态按规则（Planned/Approved/Construction/Operational），输出 world 同 schema（含 legacy_operator_aliases、power_source_or_grid_connection、needs_official_permit_check）。
6. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：codex terra agent（max thinking）每 agent 分批复核罗马尼亚数据中心（41 县+Bucuresti）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：NXDATA-3 BUH3 Tunari 2026 Q4 启用与许可；Portland Trust 三址的 PMB/分区 AC/CU 记录；ClusterPower/AIC Mischii-Fauresti 800 MW 的地方许可/并网进展；SANY Uivar 70 MW DC 组件的官方文件；DriverAI Luna 诉讼/协议状态（PressOne 警示）；Sud-Muntenia 区域 DC 的物理场地（Ploiesti？）确认；政府云四节点（Bucuresti/Sibiu）完成状态；Microsoft/Otopeni 土地线索的 CU/AC。
