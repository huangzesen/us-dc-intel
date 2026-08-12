---
name: tl-datacenter-methodology
location: scripts/expansion/world/country-skills/TL/SKILL.md
description: |
  Timor-Leste (TL) data-center enumeration methodology. Division model: 13 divisions (Aileu; Ainaro; Baucau; Bobonaro; Cova Lima; Dili; Ermera; Lautem; Liquica; Manatuto; Manufahi; Oe-Cusse Ambeno; Viqueque; Atauro kept as Dili/outer-island variant since 2022 municipality reform). No practical national planning/building-permit portal; official backbone is procurement (CNA + eProcurement), TIC TIMOR/government announcements, Jornal da Republica, ANC regulator records, ADB/World Bank/DFAT donor documents, EDTL power, and connectivity releases. Evidence points to government/telecom data rooms, not hyperscale or multi-MW commercial campuses; default capacity_mw: null. No AWS/Azure/GCP/OCI TL region; resellers are not regions. Key seeds: TIC TIMOR Electronic Government Data Center (Dili/Caicoli), Prime Minister's Office Data Center (Dili), Ministry of Finance Data Center (repeated upgrades via eProcurement 1219650/979880/1133403), Telkomcel Data Center Building (Dili), ADB 55338-001 National Data Center + DR (proposed, USD 50m), TL-IXP (ANC TOR), TLSSC Bebonuk CLS (landed Jun 2024, commercial Aug 2026; 607 km/27 Tbps cable, not DC load), Zchwantech sovereign AI cloud feasibility (B), Atal Networks Dili claim (C). Read this before running TL exploration/audit batches. Routes to explorer-official.md (government/gazette/procurement/regulator/donor/power/cable playbook) and explorer-industry.md (operator/vendor/trade-press playbook).
---

# TL · 东帝汶数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：东帝汶无实用的国家规划/建筑许可门户，官方骨架是「采购（CNA + eProcurement）+ TIC TIMOR/政府公告 + Jornal da Republica + ANC 监管记录 + ADB/世行/DFAT 捐助文件 + EDTL 电力 + 连接/海缆发布」。公开证据指向政府与电信数据机房，而非超大规模或多 MW 商业园区——默认 `capacity_mw: null`，除非一手源给出电气/IT 负荷。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：政府/TIC TIMOR、Jornal da Republica 与法律锚点、采购骨架、ANC、捐助/开发银行、EDTL 电力、TLSSC 连接、超大规模缺失核查、13 分区逐区策略、已知官方设施种子 |
| `explorer-industry.md` | 行业/厂商管线：运营商/厂商扫描、贸易媒体、目录到一手核验流程、13 分区行业配方、种子表、容量与状态规则、陷阱 |

## 核心结构事实（框定每次搜索）

1. 行政划分：**13 个分区**：Aileu、Ainaro、Baucau、Bobonaro、Cova Lima、Dili、Ermera、Lautem、Liquica、Manatuto、Manufahi、Oe-Cusse Ambeno、Viqueque。Atauro 2022 年起为独立市镇——保持为 Dili/外岛搜索变体，除非 repo 分区模型更新。
2. **无实用规划/建筑许可门户**。官方骨架 = 采购（CNA https://www.cna.gov.tl/ 与 eProcurement https://www.eprocurement.gov.tl/）、TIC TIMOR/政府公告、司法部 Jornal da Republica（https://www.mj.gov.tl/jornal/；旧 `jornal.gov.tl` 域为档案）、ANC（https://anc.tl/，注意 ANC = 东帝汶监管机构，不是巴西 ANATEL 或葡萄牙 ANACOM）、ADB/世行/DFAT 项目文件、EDTL 电力、连接/海缆发布。
3. **Dili 是主导搜索目标**：中央政府、TIC TIMOR、财政部 DC 采购、Timor Telecom/ANC Telecom Building（Caicoli）、运营商总部、Bebonuk TLSSC 海缆登陆站均在 Dili。Baucau 因规模与距 Dili 距离是最合理的灾备候选假设，但本次未发现一手源点名 Baucau 为 ADB DR 场地——保持优先搜索假设而非事实。
4. **四语搜索**：英语（data center/data centre/server/ICT）、葡萄牙语（centro de dados/servidores/TIC）、德顿语（sentru dadus/dadus/rede fibra optika/sistema informasaun）、印尼语（pusat data/server/jaringan fiber optik）。本地语言 `dadus/data` 的统计、人口普查、农业、健康数据结果不得成为设施记录。
5. **无超大规模云区域**：AWS/Azure/GCP/Oracle OCI 官方区域页未列 TL（最近实际区域如新加坡/雅加达/悉尼）。在 TL 销售 AWS/Azure/GCP/OCI 的经销商不构成本地区域或本地 DC。
6. 容量与状态规则：所有 TL 种子默认 `capacity_mw: null`；海缆与电网指标分字段——TLSSC `27 Tbps` 是网络容量，Hera/Betano `255 MW` 与世行 `73.7 MWac 太阳能 + 80.2 MWh BESS` 是国家电力语境；采购金额仅作代理（如 eProcurement 1219650 列 USD 884,375、979880 列 USD 191,780）；Tier 声明非认证，除非 Uptime/TIA 文件或运营商证书支撑。状态：`operational`（Telkomcel/TIC/PMO/MoF 锚点有一手证据支持现有设施/功能）、`proposed`（ADB 国家 DC/DR）、`feasibility`（Zchwantech）、`unverified`（目录/经销商）。
7. 陷阱：电信办公室与监管地址不自动是 DC——仅当页面说 data center/datacentre/datacenter、服务器机房、DR 设施、IXP 基建站点或等价物才记录设施；Starlink/VSAT/移动塔仅连接语境；运营商区分：Timor Telecom、Telemor/Viettel Timor、Telkomcel/Telin-Telkom Indonesia 各自独立；MoF 招标链中的 PT NTT Indonesia Technology 供应商 ≠ NTT Global Data Centers；「Tier III Dili」类经销商页为 C 直到 Dili 设施地址与运营商证据出现。

## 查询模式（复制粘贴模板见 explorer-official.md §1 与 explorer-industry.md §1-2）

- 政府/TIC TIMOR：`site:timor-leste.gov.tl "data center" OR "data centre" OR "Data Center"`、`site:timor-leste.gov.tl "centro de dados" OR "sentru dadus"`、`site:tic.gov.tl "Data Center" OR "Datacenter"`、`site:tic.gov.tl "ADB" "Data Center"`、`site:timor-leste.gov.tl "Prime Minister's Office Data Center"`。
- Gazette/法律：`site:mj.gov.tl/jornal "TIC TIMOR" "Data Center"`、`site:mj.gov.tl/jornal "Autoridade Nacional de Comunicações"`、`site:mj.gov.tl/jornal "Decreto-Lei n.o 31/2024"`。法律锚点：DL 29/2017（TIC TIMOR 公共机构）、DL 46/2023（政府机构安置）、DL 15/2012（电信）、DL 31/2024（ANC 章程）、DL 5/2011 与 DL 39/2022（环境许可）。
- 采购：`site:cna.gov.tl "data center" OR "data centre" OR "Data Center"`、`site:eprocurement.gov.tl "Data Centre" OR "data center"`、`site:eprocurement.gov.tl "MdF" "Data Centre"`、`site:eprocurement.gov.tl "disaster recovery" OR "Data Center Recovery"`、`site:eprocurement.gov.tl "{division}" "ICT" OR "servidor"`。提取字段：招标/采购 ID、买方、部门、标题与语言、授标状态、供应商、金额、地点、范围（设施/IT 设备/电力冷却/灾备/网络/托管服务）。
- 监管：`site:anc.tl "IXP" OR "Internet Exchange"`、`site:anc.tl "data center" OR "data centre"`、`site:anc.tl "licence" OR "licensa" OR "licença"`、`site:anc.tl "Starlink"`、`"Autoridade Nacional de Comunicações" "Timor-Leste" "Data Center"`。
- 捐助/开发银行：`site:adb.org "Timor-Leste" "data center" OR "data centre"`、`site:adb.org "55338-001" OR "e-Government Development and Infrastructure Project"`、`site:adb.org "Timor-Leste" "disaster recovery"`、`site:worldbank.org "Timor-Leste" "digital" OR "ICT"`、`site:ungm.org "Timor-Leste" "data center"`。
- 电力：`"EDTL" "Data Center" OR "data centre"`、`"Hera" "Dili" "data center"`、`"Betano" "data center" OR "ICT"`——电力命中仅作选址语境，绑定 ICT 建筑/招标/互联/运营商记录前不证明 DC。
- 连接：`"TLSSC" "data center" OR "data centre"`、`"Bebonuk" "Data Center" OR "Cable Landing Station"`、`"Timor-Leste South Submarine Cable" "DXN" "landing station"`。
- 运营商：`"Timor Telecom" "data center" OR "centro de dados"`、`site:timortelecom.tl "data center" OR "server"`、`"Telkomcel" "Data Center Building" "Timor-Leste"`、`site:telin.net "Telkomcel" "data center"`、`"Telemor" OR "Viettel Timor" "data center" OR "server"`、`"Vanov" "data center" OR "sentru dadus"`、`"Zchwantech" "Timor-Leste" "data centre" OR "sovereign cloud"`。
- 贸易媒体（B）：`site:datacenterdynamics.com "Timor-Leste" "data center" OR "subsea"`、`site:submarinenetworks.com "TLSSC"`、`site:en.tatoli.tl "Data Center" OR "digital"`、`site:thestar.com.my "Timor-Leste" "Zchwantech"`、`site:developingtelecoms.com "Timor-Leste" "data" OR "cable"`。目录/ASN（C）：DataCenterMap、Cloudscene、Datacenters.com、bgp.he.net/country/TL、ipinfo.io/AS136765。

## 官方/监管管线要点（详见 explorer-official.md）

- **TIC TIMOR / Electronic Government Data Center**（A）：TIC TIMOR Data Center 角色页（https://www.tic.gov.tl/en/tic/sentrudadus/）与 2024 ADB 协调文章（https://www.tic.gov.tl/en/tic/shownotisia/115/）点名 Data Center Directorate 与 Electronic Government Data Center（Dili, Caicoli/MTC 区）。政府 DC 职能；物理规格未公开。
- **Prime Minister's Office Data Center**（A）：2018 政府发布称 12 个市政行政经 EDTL 变电站接入总理府数据中心（https://timor-leste.gov.tl/?lang=en&p=19673&print=1）。
- **Ministry of Finance Data Center**（A）：CNA TENDER/13/MOF-2024（https://www.cna.gov.tl/pt/2024/09/02/postqualification-for-the-upgrade-of-equipment-of-/）+ eProcurement 记录 1219650（VISIMITRA UNIPESSOAL LDA，USD 884,375）、979880（BANNILA，USD 191,780）、1133403（ICB/063/MOF-2022 灾备）。逐记录提取供应商/金额；物理机房与 MW 未披露。
- **National Data Center + DR**（A/proposed）：ADB 55338-001（https://www.adb.org/projects/55338-001/main）PDS 状态 Proposed、USD 50m OCR 贷款、执行机构 Council for Administration of the Infrastructure Fund、产出含「National data center and disaster recovery facilities established」——ADB RRP/采购或政府发布确认前不标记在建。
- **TL-IXP**（A/互联锚点）：ANC 技术顾问 TOR（https://anc.tl/media/2025/08/TOR-for-ANC-Technical-Adviser.pdf）覆盖 route server、IXP Manager、DNS、虚拟化与基建设置；本身非 colo 设施。
- **TLSSC Bebonuk CLS**（A 政府发布/B 行业细节）：政府称在 Dili Bebonuk 登陆、607 km、27 Tbps；2024 年 6 月登陆，2026 年 8 月商业运营（DCD）。作为选址语境，非 DC，除非出现 colo/服务证据。
- **Telkomcel Data Center Building**（A 行业文件，官方流程交叉目标）：运营商/母公司官方页确认东帝汶首个 Telkomcel 数据中心建筑（Dili, Timor Plaza 商圈）+ 数据中心/ERP 服务页（https://telkomcel.tl/p/data-center-erp）。
- 可靠性规则：A 级记录仍需状态诚实——ADB 项目产出可为 A/proposed 而非 operational；用 B 级贸易源识别线索与日期，再对官方/采购/运营商页交叉；TLSSC 容量与 DC 容量分开（`27 Tbps` 是海缆容量非 DC IT 负荷）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场形态：市场小而政府/电信主导。强公开证据 = TIC TIMOR/政府 DC 职能、财政部 DC、总理府 DC、Telkomcel DC 建筑。Dili 是唯一证实集群（Caicoli/MTC/政府宫、Telecom Building/ANC/Timor Telecom、Timor Plaza/Comoro 运营商办公室、Taibesi ICT 供应商、Bebonuk 登陆站）。多数其他「云/colo」声明需核验。
- 供应商扫描：**Timor Telecom**（A 运营商身份，C 直到点名 DC——ANC 宿主建筑的重要固定/移动/骨干运营商，仅记录点名 DC/服务器机房证据）；**Telemor/Viettel Timor-Leste**（A 运营商在场，B/C DC 线索——无设施证据不赋 DC）；**Vanov Technology Unipessoal LDA**（B DC 服务线索 + A eProcurement 供应商授标记录 https://www.eprocurement.gov.tl/vendors/show/2922；Dili Aituri-Laran/Taibesi 与 Farol 地址）；**Zchwantech 主权 AI 云/DC 可行性**（B：The Star 2025-12-31 报道与东帝汶达成 AI 伙伴关系、Tier 3+ 国家主权 AI 云与数据中心可行性研究；无官方 gov.tl 页——gov.tl/采购确认前保持 B）；**Atal Networks Dili 声明**（C：目录/SEO 托管线索，无地址与运营商确认不记真实设施）。
- 目录到一手核验流程：目录/ASN/托管页/贸易媒体播种名 → 精确名 + Dili/分区 + 运营商域 → CNA 与 eProcurement 精确名 → timor-leste.gov.tl/tic.gov.tl/anc.tl/mj.gov.tl-jornal → 记录 status/grade/missing_evidence；目录或经销商声明不得升过 C。
- 种子表（industry §5）：TIC TIMOR（A）、PMO DC（A）、MoF DC（A）、Telkomcel DC Building（A）、National DC+DR（A/proposed）、TL-IXP（A）、TLSSC Bebonuk CLS（A/B）、Timor Telecom 骨干/机房（A/C）、Telemor 网络机房（A/C）、Vanov（B/C）、Zchwantech（B）、Atal（C）。

## 来源分级

- **A**：一手/官方——东帝汶政府、TIC TIMOR、司法部 Jornal da Republica、CNA/NPC、eProcurement、ANC、ADB/世行/DFAT 项目文件、EDTL、点名物理设施/项目的运营商自有页。
- **B**：可信贸易或本地/区域媒体（具名当事方）、技术行业数据库（语境用）。
- **C**：目录、经销商页、SEO 落地页、仅社交声明、未核实营销——仅线索。

## 使用流程（探索/复核批次）

1. 读本 SKILL.md 与两份 explorer 报告，确定目标分区与候选项。
2. 对每个候选跑四语通用扫描 + 运营商域 + CNA/eProcurement + 政府/监管域。
3. 按状态与容量规则记录（capacity_mw: null 默认；采购金额作代理；Tier 声明非认证）。
4. 13 分区全跑（含 RAEOA/ZEESM 特殊区采购）。
5. 每轮重查超大规模官方区域页并带日期记录负面。
6. 遵守 NO-DELETION；不改写 explorer-*.md。

## 待办（2026-08-12 03:20Z）

- [x] 合并两份探索报告为 SKILL.md + ANATOMY.md。
- [ ] ADB 55338-001：跟踪 RRP、ADB 商业机会通知、TIC TIMOR/CNA/eProcurement 发布。
- [ ] Telkomcel DC Building：直接核验当前地址/规格。
- [ ] Zchwantech：gov.tl/采购确认（feasibility → proposed）。
- [ ] 待核实：Baucau 是否被官方指定为 ADB DR 场地；Vanov 是否提供公共 colo 服务。
