---
name: de-datacenter-methodology
location: scripts/expansion/world/country-skills/DE/SKILL.md
description: |
  Germany (DE) datacenter discovery & audit methodology — how to enumerate, verify, and update Germany datacenter projects at Land + Kreis/kreisfreie Stadt granularity (403 divisions in the current manifest). Germany has no single national building-permit or facility registry: enumeration pivots on municipal Bauleitplanung (Bebauungsplan / Flächennutzungsplan / Sondergebiet Rechenzentrum), council/RIS documents, UVP/BImSchG environmental files, Bundesnetzagentur & grid-operator Netzanschluss proceedings, the EnEfG energy-efficiency register (RZReg, coming validation channel), cloud-region pages, and operator facility pages. Read this before running DE exploration/audit batches. Routes to explorer-official.md (permits/energy/state portals/cloud) and explorer-industry.md (trade press/vendors/query patterns).
---

# DE · 德国数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：德国**没有**全国统一的数据中心建筑许可库或设施注册库（16 部 Landesbauordnungen，许可由市镇/县 Bauaufsicht 管理），不能按单一门户直接枚举。
> 德国枚举的**官方主线是 Bauleitplanung（土地利用规划）早于 Baugenehmigung（建筑许可）**：找 Bebauungsplan/Flächennutzungsplan 修正、`Sondergebiet Rechenzentrum`、`Netzanschluss`、`Umspannwerk`、`Abwärme`；电网容量是核心瓶颈。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供德国探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：Bauleitplanung/Bauaufsicht 主干、16 州规划门户路由表、UVP-Verbund/UVP 环评、EnEfG RZReg 能效注册、Bundesnetzagentur 电网批复、云区域官方页（AWS/Azure/GCP/OCI）、DE-CIX 互联、运营商官方设施页、403 division 枚举工作流与状态规则 |
| `explorer-industry.md` | 行业/厂商发现：Datacenter-Insider/heise/Golem/Computerwoche/DCD 德英贸易媒体、eco/GDA/Bitkom/Borderstep 协会、Data Center Map/Baxtel/datacenters.com 目录、分区运营商种子清单（Hessen/Berlin-BB/NRW/Bayern/北方等）、德文查询模板、按证据分级 |

## 核心结构事实（框定每次搜索）

1. **无全国建筑许可库**：以每个 Kreis/kreisfreie Stadt 为操作搜索单元；项目常以 Gemeinde 命名而非 Kreis，须按 (Land, Kreis, Gemeinde) 归一化。
2. **先看 Bauleitplanung 而非 Baugenehmigung**：许可文件常不公开，但公众参与文件公开，含地块/SPV/目标 IT load/变电站/备用发电/冷却水/余热承诺。生命周期：`Standortsuche` < `Aufstellungsbeschluss` < `Offenlage/Auslegung` < `Satzungsbeschluss/rechtskräftig` < `Bauantrag` < `Baugenehmigung` < `Baubeginn/Spatenstich` < `Richtfest` < `Inbetriebnahme`。只有 `Baugenehmigung`/`Baubeginn` 及以上算施工证据。
3. **RZReg（EnEfG §14 能效注册）**：全国性运营数据中心报告渠道，未来高价值校验源，但公开数据尚未形成实用普查——现阶段是“将到的 A 级渠道”，不是今日发现底座。
4. **电网是瓶颈**：`Netzanschluss Rechenzentrum` 比 `Baugenehmigung Rechenzentrum` 更易命中；查 Bundesnetzagentur 程序（BK4/BK6 系列、380-kV-Netzanschluss、Investitionsmaßnahme）与 TSO/DSO（50Hertz/TenneT/Amprion/TransnetBW；NRM/Syna/Westnetz/e-netz/Stromnetz Berlin/E.DIS/Bayernwerk 等）。
5. **地理高度聚集**：Frankfurt/Rhein-Main（DE-CIX + 四云区域）→ Berlin-Brandenburg（AWS European Sovereign Cloud 2026 开服、GCP Berlin-Brandenburg 2023、Nauen 等）→ NRW Rheinisches Revier（Microsoft 32 亿欧元）→ 慕尼黑/巴伐利亚 → 汉堡/北方。
6. **云区域=城市级证据（A），非设施地址**：AWS `eu-central-1` (Frankfurt)；Azure Germany West Central (Frankfurt) / Germany North (Berlin)；GCP `europe-west3` (Frankfurt) + Berlin-BB；OCI `eu-frankfurt-1`；IBM `eu-de`。不推断物理设施归属。
7. **容量语义**：区分 `Netzanschlussleistung`、变压器 MVA、楼宇功率、IT load；规划文件/运营商页常写园区最终规模，须按阶段与状态分开记录。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§2 / explorer-industry.md §4）

- 德文核心词：`Rechenzentrum` `Datacenter` `KI-Rechenzentrum` `Colocation` `Bebauungsplan` `B-Plan` `Sondergebiet Rechenzentrum` `Flächennutzungsplan` `Bauantrag` `Baugenehmigung` `Bauaufsicht` `Netzanschluss` `Umspannwerk` `110-kV`/`380-kV` `Abwärme` `Fernwärme` `Notstromaggregate`/`Netzersatzanlage` `UVP` `BImSchG`。
- 规划：`"{stadt}" "Rechenzentrum" "Bebauungsplan"`、`"{kreis}" "Rechenzentrum" "Baugenehmigung"`、`filetype:pdf "Rechenzentrum" "Begründung" "Satzungsbeschluss"`、`site:bb.beteiligung.diplanung.de Rechenzentrum`、`site:rim.ekom21.de Rechenzentrum "{Kommune}"`、`site:ratsinfo.* Rechenzentrum`。
- 电网/环评：`site:bundesnetzagentur.de "Rechenzentrum" "Netzanschluss"`、`site:bundesnetzagentur.de "380-kV-Netzanschluss Rechenzentrum"`、`site:uvp-verbund.de Rechenzentrum`、`site:{grid-operator-domain} Rechenzentrum Umspannwerk`、`"{stadt}" "Rechenzentrum" "Abwärme" "Fernwärme"`。
- 行业：`site:datacenter-insider.de "{operator}" "{Ort}" Rechenzentrum`、`site:datacenterdynamics.com Germany "{Ort}" "data center"`、`site:heise.de "{Ort}" Rechenzentrum`。
- 云 pivot：`"AWS" "Frankfurt" "eu-central-1"`、`"Azure" "Germany West Central" Frankfurt`、`"{provider}" "Brandenburg" "Bebauungsplan" "Rechenzentrum"`、`"Rheinisches Revier" Microsoft Rechenzentrum Baugenehmigung`。
- 取消追踪：`"{operator}" "{Ort}" Rechenzentrum (abgelehnt OR zurückgezogen OR gestoppt)`（如 Vantage Gross-Gerau 2026 被拒、STACK Babenhausen 取消）。

## 官方/监管管线要点（详见 explorer-official.md）

- 主干链：① 市镇 Bauleitplanung（B-Plan/FNP 修正/Sondergebiet/Gewerbegebiet）→ ② 议会信息系统（Ratsinformationssystem/Bürgerinfo/Vorlagen/Drucksache）→ ③ Bauaufsicht/Baugenehmigung → ④ 区域规划（Regionalplan/Zielabweichung/Raumordnungsverfahren，州 Regierungspräsidium）。
- 规划门户：Frankfurt Stadtplanungsamt 数据中心指南（A）、DiPlanung（bb.beteiligung.diplanung.de，Brandenburg Nauen “Sondergebiet Rechenzentrum 2” 为范例）、BayernPortal/Bayern DiPlanung、Hamburg Bauleitplanung Online、he/mv.bauleitplanung-online.de、bob-sh.de、Sachsen/Sachsen-Anhalt/NRW 中央门户。
- 环评：UVP-Verbund（搜索 `Rechenzentrum`/`Notstrom`/`Umspannwerk`/运营商名）、联邦 UVP-Portal；提取柴油发电机 MW/MVA、冷却水、变电站、110/380-kV、Natura 2000。无全量 UVP 的项目常因变电站/备用电源/供热触发文件。
- 电网：Bundesnetzagentur（BK6-24-245 大负荷分配、BK4-20-028 380-kV-Netzanschluss Rechenzentrum Mittenwalde/Thyrow 为范例）；按地理查 TSO/DSO。
- 16 州路由表（Baden-Württemberg/Bayern/Berlin/Brandenburg/Bremen/Hamburg/Hessen/MV/Niedersachsen/NRW/RP/Saarland/Sachsen/ST/SH/Thüringen）：先查州规划门户，再钻 Kreis/市镇。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 贸易媒体：Datacenter-Insider（B，德国 DC 行业最佳）、heise（B）、Golem（B，政策/争议）、Computerwoche（B）、DCD（B，国际交叉验证）；本地报纸 B-/C+（议会投票/冲突好，技术规格差）。
- 协会/市场：eco、German Datacenter Association (GDA)、Bitkom、Borderstep（B+，能源/市场研究）、GTAI/ITA（B-）；JLL/CBRE/DC Byte/Structure Research 报告仅作市场情报。
- 目录：Data Center Map / Datacenters.com / Baxtel / Datacenterplatform = **C+ 线索源**，地址/别名有用，须运营商页或市政文件核实；注意 geoDC 噪音（与 GEODE 混淆）。
- 运营商种子（A=存在/B=容量）：Equinix (FR)、Digital Realty/Interxion (FRA5-32)、NTT (Frankfurt 1-4，Frankfurt 1: 52,200+ sqm/77.4 MW max IT load)、maincubes (FRA01/FRA03/BER01)、Vantage (Frankfurt 112 MW/Berlin 88 MW)、CyrusOne (FRA1/5/6/7)、STACK (Frankfurt/Liederbach)、Iron Mountain、Telehouse、NorthC、Hetzner (Nuremberg/Falkenstein)、Google (Hanau)、AWS/Azure/GCP/Oracle 区域。
- 状态语义：`announced`=不计数；`Bebauungsplan in Aufstellung`=提议；`Satzungsbeschluss`/`Baugenehmigung erteilt`/grid connection signed=已批准未动工；`Spatenstich`/`Baubeginn`/`Richtfest`=在建；`in Betrieb`/`opened`/`GA`=运营（仍区分壳楼/装机 IT load/租赁容量）；`abgelehnt`/`zurückgezogen`/`aufgegeben`=被拒/取消，保留为负面证据。

## 来源分级

- **A** = 官方/一手：市政 B-Plan/FNP 文件、议会决议、Bauaufsicht 通知、Bundesnetzagentur 程序与电网运营商规划文件、RZReg/BfEE/BMWE/EnEfG 资料（公开数据可得时）、UVP-Verbund/UVP 门户文件、运营商官方设施页（存在/位置）、云区域官方文档（城市级）、DE-CIX 官方 enabled-site 页。
- **B** = 强二级：运营商页容量（未独立核实）、DCD/Datacenter-Insider/heise/Golem/Computerwoche、德国数据中心协会/Bitkom/UBA/BMWK 研究、市场顾问报告。
- **C** = 弱/未验证：Data Center Map/Baxtel/PeeringDB/Cloudscene/datacenters.com（字段级 B/C）、本地政治声明、投资 MoU、宣传册；聚合器须核实后才计入。
- 容量规则：优先设施级 IT MW；否则标注为 connection MW/MVA；规划总容量与一期分开；大项目须≥两条证据链（规划/许可+运营商，或规划/许可+电网/UVP，或运营商+RZReg）。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=DE，divisions=Land+Landkreis/kreisfreie Stadt，403 目标）。
2. 归一化 division：确定 Land、Kreis、主要 Gemeinde、产业园区；项目常以 Gemeinde 命名。
3. 官方规划查询：州规划门户（Rechenzentrum/Datacenter/Sondergebiet/Umspannwerk/运营商名）→ 市镇 B-Plan/Baugenehmigung → 议会 RIS/Drucksache。
4. 电网/环评查询：Bundesnetzagentur（Netzanschluss/Investitionsmaßnahme/380-kV）→ TSO/DSO → UVP-Verbund/联邦 UVP（Notstromaggregate/Umspannwerk）。
5. 云/运营商 pivot：Frankfurt/Rhein-Main 与 Berlin-BB 查全部大运营商；其他 division 用 DE-CIX where-to-connect + 云连接页做种子。
6. 去重：同一园区可同时是运营商品牌、德国 SPV（…Germany GmbH）、街道地址、B-Plan 名、园区名；按 (运营商母公司, Gemeinde, 街道/地块, 园区名, 规划号) 聚类。输出 world 同 schema；无项目 division 写 `no_projects: true`。
7. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12 02:07Z）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：50× codex terra agent（max thinking）每 agent 分批复核德国数据中心（Land/Kreis 粒度）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：RZReg 公开数据上线时升级为普查源；AWS European Sovereign Cloud（Brandenburg）具体 Gemeinde；Microsoft Rheinisches Revier 各市镇（Bergheim/Bedburg/Elsdorf/Grevenbroich）许可状态；历史遗留项（2015-2018 Microsoft Magdeburg）不得计入当前容量。
