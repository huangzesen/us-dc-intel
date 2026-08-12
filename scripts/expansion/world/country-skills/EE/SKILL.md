---
name: ee-datacenter-methodology
location: scripts/expansion/world/country-skills/EE/SKILL.md
description: |
  Estonia (EE) data-center enumeration methodology. Division model: 15 counties / 79 municipal units; facility evidence backbone is Ehitisregister (EHR) plus municipal planning/permitting, Keskkonnaamet/KOTKAS, Elering/Elektrilevi, and Äriregister. No hyperscale cloud region is listed for EE by AWS/Azure/GCP/Oracle. Enumeration pipeline joins official (EHR, planning, environment, grid, business register) and industry (operator pages, trade press, catalogs, IXP) sources; catalog totals (~9-10 Tallinn sites) are C-grade until matched to operator and official records. Key seeds: Greenergy/MCF GRE DC1 (Harju/Saue vald, Alajaama tee 1, 14,500 m2 / 31.5 MW), Sunly Risti campus (Lääne/Lääne-Nigula, planned 180 MW, 36 ha, six modules). Read this before running EE exploration/audit batches. Routes to explorer-official.md (EHR/permits/grid/regulator playbook) and explorer-industry.md (operator/catalog/trade-press seeding).
---

# EE · 爱沙尼亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：爱沙尼亚无全国数据中心注册库，枚举靠「建设登记册 EHR + 市政规划/许可 + 环境许可 + 电网连接 + 商事登记」多轨交叉。本 skill 汇总官方与行业两份探索报告，为每次搜索框定范围、模板与分级。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：EHR、Ehitusregister 字段、许可生命周期、Keskkonnaamet/KOTKAS、Elering/Elektrilevi、Äriregister/EMTAK、15 郡逐郡策略 |
| `explorer-industry.md` | 行业/厂商管线：运营商页面、贸易媒体、目录种子、IXP/互联、市场形态与误报规则 |

## 核心结构事实（框定每次搜索）

1. 行政区划：**15 郡（county）79 个地方自治单位**（state portal 口径；2026 年区域部页面称 78，以 EHAK 空间数据为准）。郡是枚举桶，地方事务由市政处理。EHAK：https://geoportaal.maaamet.ee/eng/spatial-data/administrative-and-settlement-division-p312.html 。
2. **无全国数据中心注册库**。EHR（Ehitisregister, https://ehr.ee）是主要官方设施证据源，但不稳定暴露 `andmekeskus` 用途类别——数据中心可能登记为 office/telecom/industrial/storage/technical 等用途，必须按地址、法人、宗地、市政、许可号反查。
3. 生命周期（爱沙尼亚语）：`üldplaneering -> detailplaneering -> projekteerimistingimused / ehitusprojekt -> ehitusluba / ehitusteatis -> ehitamise alustamise teatis -> kasutusluba / kasutusteatis -> kasutusel`。**运营 = kasutusluba/kasutusteatis 或 EHR kasutusel 或厂商明确宣传在用**；**在建 = ehitusluba/开工通知或官方施工合同**；**规划中 = 详规启动/采纳、EIA/KMH 筛查、电网连接证据或开发商申请**。
4. **无超大规模云区域**：AWS/Azure/GCP/Oracle 官方区域页均未列 EE。不得从客户、办公室、招聘、CDN 边缘、Marketplace 或主权云推断超大规模设施（A 级否定核查）。
5. 环境：Keskkonnaamet（https://keskkonnaamet.ee）与 KOTKAS（https://kotkas.envir.ee）为 A 级：环境许可、备用发电机空气排放许可、EIA/KMH 决策。
6. 电网：Elering（TSO, https://elering.ee/en/connecting-electricity-network, 门户 https://egle.ee）与 Elektrilevi（DSO, https://www.elektrilevi.ee）为 A 级；Konkurentsiamet（https://www.konkurentsiamet.ee）为监管语境（2025-02-09 波罗的海与欧洲大陆同步并网）。电网证据本身不构成数据中心记录，须绑定具体开发商/场地。
7. 商事登记：Äriregister（https://ariregister.rik.ee）A 级确认法人/注册码/地址；EMTAK 6311/63101、6312/63120 为有用 pivot 但不证明物理设施。官方公告：https://www.ametlikudteadaanded.ee 。
8. 语言与去重：先爱沙尼亚语后英语；`andmekeskus` 常见误报 = 统计局/市政信息中心、普通办公楼机房、高校 HPC、IX 成员/CDN 缓存节点、目录所列电信局所/PoP、托管公司注册地址。目录总量（约 9-10 个 Tallinn 设施）为 C 级，需逐一匹配运营商与官方记录；目录常混入老式电话交换局、运营商 PoP、办公室与真实机房。

## 查询模式（复制粘贴模板见 explorer-official.md §2 与 explorer-industry.md §1）

- 爱沙尼亚语核心词：`andmekeskus / andmekeskused / serveriruum / serverikeskus / kolokatsioon / veebimajutus / andmetöötlus / pilveteenus`；许可词缀：`ehitusluba / kasutusluba / detailplaneering / projekteerimistingimused / keskkonnamõju hindamine / KMH / keskkonnaluba / välisõhu saasteluba / varugeneraator / alajaam / liitumine / 110 kV / 330 kV / kaugküte / jääksoojus`。
- 官方站点模板：`site:ehr.ee "andmekeskus"`、`site:livekluster.ehr.ee ...`、`site:ametlikudteadaanded.ee ...`、`site:kotkas.envir.ee ...`、`site:keskkonnaamet.ee ...`、`site:elering.ee ...`、`site:elektrilevi.ee ...`、`site:ariregister.rik.ee ...`、`site:tallinn.ee "planeeringute register" "andmekeskus"`；组合：`"{operator}" "ehitusluba" "{vald}"`、`"{parcel}" "detailplaneering"`、`filetype:pdf "andmekeskus" "ehitusluba" "{maakond}"`。
- 商事 pivot：`site:ariregister.rik.ee "6311" "andmetöötlus"`、`site:inforegister.ee "63101" "andmetöötlus" "{maakond}"`、`"{operator} OÜ" "registrikood"`。
- 英文：`"Estonia" "data center" "building permit"`、`"Estonia" "data centre" "environmental impact assessment"`、`"Estonia" "data center" "grid connection"`、`"{county}" "data center" "planning"`。
- 行业/目录/IXP：`site:datacenterdynamics.com Estonia "data center"`、`site:capacitymedia.com ...`、`site:news.err.ee "data center" Estonia`、`site:aripaev.ee andmekeskus`、`site:datacentermap.com estonia tallinn data center`、`site:baxtel.com "Estonia" "data center"`、`site:peeringdb.com Tallinn Estonia`、`"TIX" Tallinn peering members`。

## 官方/监管管线要点（详见 explorer-official.md）

- EHR 提取字段：EHR code、地址、郡/市/聚落、地籍单元、建筑状态、用途与毛面积、许可类型/编号/日期、主管机关、业主/申请人、相关结构（变电站、发电机、油箱、冷却、通信管井）。
- 环境/电网提取字段：许可号、申请人、场地/地籍、备用发电机台数与 MW/kW、燃油储量、UPS/电池、冷却与用水、噪声/空气建模、连接电压与变电站名、连接容量 MW/MVA、热回收/区域供热链接、状态与决策日期。
- 记录规则：记录不得高于其最弱未决依赖——厂商页称在用但无官方地址/许可：`evidence_grade=B, status=operating_by_operator, official_status=unverified`；目录列设施但厂商仅宣传通用托管：`C, candidate, do_not_count=true`；市政公告称已提交详规申请：`A, planned, do_not_count_as_operating=true`；EHR 使用许可或活动建筑状态绑定运营商/地址：A 级可计数；电网/变电站工程未点名数据中心客户：仅语境。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场形态：小型、Tallinn/Harju 中心的 colo 市场；目录种子 DataCenterMap Tallinn（https://www.datacentermap.com/estonia/tallinn/）与 Baxtel Estonia（https://baxtel.com/data-center/estonia）。
- 主要线索：**Greenergy/MCF GRE DC1**（Harju/Saue vald, Hüüru, Alajaama tee 1；A/B：14,500 m2 / 31.5 MW、EN 50600；官方后续 = EHR/Saue 许可/Äriregister 14069314/地籍；扩张线索 = Caverion 2026 主承包商、MCF 近 1 亿欧元 AI 扩张）；**Sunly Risti 园区**（Lääne/Lääne-Nigula；规划 180 MW/184.5 MW、36 ha、六栋数据处理楼、经 Risti 太阳能园区变电站接 Elering；仅 planned，不计数为在用）；**Telia Eesti**（Tallinn，ERR 报 1000 万欧元/Utilitas 旁；目录列 Sõpruse pst/Pärnu mnt/Sõle 等，逐址候选需 Telia/EHR/TPR 确认，去重 PoP 与旧交换局）；**Elisa**（Tallinn, Adala 4 目录地址）、**WaveCom**（Endla 16）、**INFONET DC**（Laevastiku 3r, reg. 12501440）均为候选在用设施；**FairyHosting/Narva Datacenter**（Ida-Viru/Narva, Mihail/Ak. Maslovi 1）仅目录种子，厂商页指 Tallinn Sõpruse，保持候选；**RIA/Riigipilv** 与国家 X-tee/数据大使馆仅为语境不枚举；**Nebius Estonia** 仅 ERR 招聘猜测，观察名单。
- 大学/研究：University of Tartu HPC/EENet 为非商业计算，除非明确宣传 colo 否则不计。

## 来源分级

- **A**：EHR/官方门户、市政规划或许可文件、监管/环境决策、电网文件、地籍记录、官方超大规模区域页；行业文件中 A = 厂商一手页/承包商自有范围发布/官方云区域页/官方 IXP 页。
- **B**：厂商一手页或新闻稿、成熟贸易/本地媒体、投资机构文章、行业协会/IXP 源。
- **C**：目录/聚合器（DataCenterMap、Baxtel、Datacenters.com、ColoMap、Cloudscene、Inflect 等）、搜索摘要、社交媒体、论坛、目录镜像、无来源市场清单。
- 状态语义：`operating`（有使用许可/在用证据）、`under_construction`（有建设许可/开工）、`planned`（详规/EIA/并网证据）、`candidate`（目录或弱证据，默认 `do_not_count=true`）、`context`（电网/国家 ICT，不计）。

## 使用流程（探索/复核批次）

1. 读本 SKILL.md 与两份 explorer 报告，确定目标郡与候选项。
2. 对每个候选：EHR 郡过滤 + 市政详规/许可页 + Ametlikud Teadaanded + Äriregister EMTAK 6311/63101 按注册地址 + KOTKAS/Keskkonnaamet + Elering/Elektrilevi。
3. 优先郡：**Harju**（Greenergy、Telia、Elisa、WaveCom、INFONET 及目录地址 Sõpruse pst 193、Pärnu mnt 158、Sõle tn 14/25、Adala 4、Endla 16、Laevastiku 3R；扫 Rae/Saue/Harku/Lääne-Harju/Maardu 工业市政与 110/330 kV 负荷）、**Lääne**（Sunly Risti 详规/EHR/KMH/Elering 跟踪）。中等：Ida-Viru（Narva 候选、IVIA、工业园）、Tartu（研究/HPC，非商业）。低产郡用低产模板后记录无项目。
4. 低产模板：`"{maakond}" "andmekeskus"`、`"{main town}" "data center" colocation`、`site:{municipality-domain} "detailplaneering" "andmekeskus"`、`site:ametlikudteadaanded.ee "{vald}" "andmekeskus"`。
5. 按记录规则定级并写 world schema 输出（字段含 county/municipality/settlement、cadastral_or_parcel_id、registry_code、em_tak_code、status/status_basis、capacity_mw、white_space_m2、construction/planning/environment/energy/operator/trade_press_evidence_url、evidence_date/grade、do_not_count_reason）。
6. 每季度复核观察名单：Sunly Risti 里程碑、Greenergy/MCF 扩张许可与承包商节点、Nebius 确认、Harju 工业市政高功率详规、Ida-Viru 工业区。
7. 遵守 NO-DELETION；不改写 explorer-*.md。

## 待办（2026-08-12 03:02Z）

- [x] 合并两份探索报告为 SKILL.md + ANATOMY.md。
- [ ] Greenergy Alajaama tee 1 的 EHR/Saue 许可与 Äriregister 14069314 核验（A 级计数）。
- [ ] Sunly Risti：Lääne-Nigula 详规采纳、EHR 许可、KOTKAS/KMH、Elering 连接证据跟踪。
- [ ] 待核实：Telia/Elisa/WaveCom/INFONET 各 Tallinn 地址在 TPR/EHR 的独立物理设施确认。
- [ ] 待核实：Narva DC（FairyHosting）官方/一手设施证据。
