---
name: hr-datacenter-methodology
location: scripts/expansion/world/country-skills/HR/SKILL.md
description: |
  Parent-level data-center enumeration methodology for Croatia (HR). Croatia has
  no single public national registry of commercial datacenters; the strongest
  facility evidence is the built-environment trail (location/building/occupancy
  permits via eDozvola/ISPU, environmental PUO/EIA, HOPS/HEP/HERA grid evidence)
  cross-joined with HAKOM e-Operator, EOJN/TED procurement, operator official
  pages, CIX/SRCE interconnection, and trade press across 20 counties plus Zagreb
  City. Read this before running HR exploration/audit batches. Routes to
  explorer-official.md (official/regulatory/cloud pipeline) and
  explorer-industry.md (industry/association/county patterns).
---

# HR · 克罗地亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：Croatia has no single public national registry of commercial datacenters；最强的设施证据不是电信牌照，而是建成环境轨迹：**lokacijska dozvola（选址许可）、građevinska dozvola（施工许可）、uporabna dozvola（使用许可）、空间规划法案、公告板条目、环境筛选/EIA、并网证据**。
> 多轨三角测量：官方许可/环评/电网轨道产出 A 级证据，运营商/认证/IXP 轨道产出 A/B 级设施信号，贸易媒体与目录用于回填 B/C 线索；国家层面先扫，再转向 Zagreb City、Zagreb County、Varazdin/Medimurje、沿海都市郡与项目所在市镇。
> 本 skill 汇总两份探索报告（explorer-official.md / explorer-industry.md）为国家层方法论；批次执行前必读。

## 入口

| 文件 | 内容 | 说明 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线：ISPU/eDozvola/Oglasna ploča 许可链、MZOZT 环评（PUO/SPUO/OPUO）、HOPS/HEP ODS/HERA 电网、HAKOM e-Operator、EOJN/TED 采购、云区域缺失核验、运营商表、逐郡枚举与证据分级 | A 级主干与查询模板 |
| explorer-industry.md | 行业/协会/郡域模式：HRDCA/峰会/协会生态、贸易与本地商业媒体、目录（Baxtel/DataCenterMap 等）、官方核验面（eDozvola/Uptime）、运营商/云/厂商种子、Pantheon/Topusko 核验、21 郡查询配方与负向过滤器 | A/B/C 全谱系 |

## 核心结构事实（框定每次搜索）

1. **无国家数据中心注册表**：克罗地亚不存在统一公开的商业数据中心登记；实用枚举路径为：运营商/目录/贸易线索 → 运营商页或认证 → eDozvola/ISPU/本地许可 → 环评与电网/能源核验 → HAKOM/电子采购/媒体交叉核验。
2. **许可链（A 级核心）**：`lokacijska dozvola` = 强选址/规划证据（建设前）；`građevinska dozvola` = 批准施工（结合签发日期与新闻作 high-confidence planned/under construction）；`izmjena i dopuna građevinske dozvole` = 扩建/设计变更/容量或电力变更；`uporabna dozvola` = 设施/阶段可能运营的最强公开信号；`javni poziv / uvid u spis predmeta` = 待决许可（早期线索，非批准证明）。
3. **官方规划栈**：ISPU / eDozvola（Ministry of Physical Planning, Construction and State Assets，`edozvola.gov.hr`）；Oglasna ploča（`edozvola.gov.hr/notice-board`、`mpgi.gov.hr/oglasna-ploca`）公布已签发许可与公开征集；郡/市政府行政部门按地点负责建设与空间规划（MPGI 发布主管机构地址清单）——均 A 级。
4. **语言（克罗地亚语 + 英语）**：核心词 `podatkovni centar`、`data centar`、`računalni centar`、`kolokacija`、`smještaj opreme`、`serverska soba`、`oblak`、`virtualni podatkovni centar`、`građevinska dozvola`、`uporabna dozvola`、`lokacijska dozvola`、`procjena utjecaja na okoliš / PUO`、`ocjena o potrebi procjene / OPUO`、`priključenje na mrežu`、`trafostanica`、`prijenosna mreža`、`agregat`、`sunčana elektrana`、`baterijski sustav`、`dalekovod`；带变音符与 ASCII 回退拼写同时搜（Varaždin/Varazdin 等）。
5. **地理分布**：商业 colo 高度 Zagreb 集中（Digital Realty/Altus ZAG1、DataBox、A1、Hrvatski Telekom、Croatian Web Hosting、CIX/SRCE）；非 Zagreb 高置信线索：Jastrebarsko/Križ（Zagreb County）、Varazdin（DC North/CRATIS）、Rijeka、Split、Osijek、Pula（须验证）；新大型项目信号为 **Sisak-Moslavina 郡 Topusko 附近 Pantheon AI / Pantheon Atlas**（公告级，待官方许可）。
6. **云语义（含负向控制）**：AWS/Azure/GCP/OCI 官方区域页均无克罗地亚公有云区域（截至 2026-08-12 核验）；AWS 在克罗地亚开设了数据中心设计设施并于 2021-02 启动 Zagreb Edge 位置——**设计设施 ≠ 云区域**；`virtualni podatkovni centar`/云服务页常不指名物理设施。
7. **容量语义**：容量与存在性分离；优先许可/EIA/电网/运营商技术文档而非聚合器 MW；营销设计容量标为 **planned/design**；IT 负载不得从发电机/变电站值推断（除非明确声明为 IT 负载）。
8. **陷阱**：`podatkovni portal`、无物理设施的 `baza podataka`、无地址的 `virtualni podatkovni centar`、仅 `cloud usluge`/`hosting`、`call centar`、产品类目 "data center"、仅 `ured/poslovnica`、无设备机房证据的 "edge" 营销——全部降级或排除；AWS 设计设施、CIX 节点本身、未核验的 AI 超级园区公告均不计数。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§4 / explorer-industry.md §4-§5）

- 许可/公告板：`site:edozvola.gov.hr/notice-board "podatkovni centar"`、`site:edozvola.gov.hr/notice-board "data centar"`、`site:mpgi.gov.hr "podatkovni centar" "građevinska dozvola"`、`site:mpgi.gov.hr "data centar" "lokacijska dozvola"`、`site:portal-ispu.gov.hr "podatkovni centar"`。
- 环评：`site:mzozt.gov.hr "podatkovni centar" (PUO OR OPUO OR "procjena utjecaja")`、`site:mzozt.gov.hr "trafostanica" "podatkovni centar"`、`site:mzozt.gov.hr "{municipality}" "data centar"`。
- 电网：`site:hops.hr "podatkovni centar"`、`site:hep.hr/ods "data centar" OR "podatkovni centar"`、`site:hera.hr "podatkovni centar" OR "data centar"`、`"priključenje na mrežu" "data centar" Hrvatska`。
- 监管/采购：`site:hakom.hr "data centar"`、`site:eoperator.hakom.hr "{operator}"`、`site:eojn.hr "podatkovni centar" OR "serverska soba" OR "kolokacija"`、`site:ted.europa.eu Croatia "data centre" OR "server room"`。
- 云核验：`site:aws.amazon.com Croatia Zagreb "Edge location"`、`site:learn.microsoft.com/azure Croatia "region"`、`site:cloud.google.com Croatia "region"`、`site:oracle.com/cloud Croatia "region"`。
- 郡域通用：`"{county Croatian name}" "podatkovni centar"`、`"{county seat}" "podatkovni centar" OR "data centar"`、`"{county seat}" "građevinska dozvola" "podatkovni centar"`、`site:{county-domain} "podatkovni centar" OR "data centar"`、`site:mzozt.gov.hr "{county seat}" "podatkovni centar"`。
- 状态词：planned/early = `planirano`、`najavljeno`、`namjeravani zahvat`、`investicija`、`uvršten u strateške projekte`；permitting = `zahtjev`、`javni uvid`、`lokacijska dozvola`、`građevinska dozvola`、`rješenje`；construction = `početak radova`、`gradnja`、`izgradnja`、`dovršetak radova`；operational = `otvoren`、`pušten u rad`、`u funkciji`、`uporabna dozvola`、`komercijalni rad`。

## 官方/监管管线要点（详见 explorer-official.md）

- **eDozvola / ISPU / Oglasna ploča**：A 级设施存在、生命周期与法定地点证据；`uporabna dozvola` 比开业新闻更强的运营触发。
- **MZOZT 环评**：PUO 在不需要选址许可时作为其他批准前的评估——可捕获大型园区、发电机、变电站、能源厂与表后项目；提取投资者、地籍市镇、地块、发电机数、冷却系统、变压器/变电站容量、用水、备用燃料、总建筑面积、分期建设。
- **HOPS / HEP ODS / HERA**：约 1-2 MW 以上项目搜索匹配的变电站或并网公告；大型 AI 园区主张须有 HOPS/HEP/HERA 证据或命名专用发电、输电连接、变电站的环评/许可文件；HEP ODS 的 Moja mreža 数字化并网申报。
- **HAKOM e-Operator**：电子通信网络/服务运营商的中央数据库；A 级证明运营商状态（Digital Realty/Altus、DataBox、A1、HT、Telemach、CRATIS/DC North、Akton、Comping/Data Target、CARNET/SRCE），不含设施容量；HAKOM 缺失 ≠ 私有企业数据中心不存在。
- **EOJN RH / Narodne novine EOJN / EU TED**：A 级招标/中标；用于政府/大学/HPC 项目与扩建信号（turnkey AI/HPC、数据中心建设工程、UPS/发电机/冷却合同、colo 服务中标）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **协会（B/C）**：HRDCA（2024 年成立；LinkedIn 引用政府"22 个活跃私有数据中心"说法——设施级主张须另证）、Croatia Data Center Summit（`datacenterevent.eu`，演讲者/赞助商揭示活跃运营商与工程/电网/冷却厂商）、EUDCA（区域语境）。
- **贸易/商业媒体（B）**：DCD（A1 Zagreb 开业、DataBox/Digital Realty 云业务交易、Pantheon/Topusko 跟踪）、Bug/Mreza、Poslovni dnevnik、Forbes Hrvatska/Dnevnik、Hina、Index/Vecernji/Jutarnji/Lider/Telegram（B/C）、Balkan Insight/BusinessWire/WSJ/Enlit/OIE（Topusko 超大规模/能源项目语境，BusinessWire 为发行方控制）。
- **目录（C/C+）**：Baxtel（现示 19 个克罗地亚设施，突出 PCK-DataCross、DC North Varazdin、Croatian Web Hosting、A1）、DataCenterMap、Datacenters.com、Cloudscene、Data Center Catalog、PeeringDB（活跃对等/设施信号 B，完整性 C）；仅作种子，不作记录源。
- **运营商种子（存在性 A / 容量视证据）**：Digital Realty ZAG1 / 前 Altus IT（Selska cesta 93，1,330 sqm，50+ 云/网络服务商，ISO/PCI 认证）、A1 Hrvatska（Avenija Većeslava Holjevca/Nežićeva 交口，EUR 11m、2,000 sqm、Tier III、Vertiv 承建、两条 2 MW 电力分支、300 IT 机柜、Uptime 认证）、PCK-DataCross（Jastrebarsko/Jalševac 工业区 + Križ DR/BC 平台）、DataBox（Zagreb；承接 Digital Realty 克罗地亚云服务业务，地址须验证以区分）、Croatian Web Hosting / CROWEB.HOST（Zagreb，距机场 15 km，Tier 3 设计 N+1）、Hrvatski Telekom / Telemach（电信云枢轴，无具名物理设施不计数）、Plus Hosting Grupa / DHH（Digital Realty 伙伴）、DC North / CRATIS（Varazdin；CIX 第三地点 2025-05 投运；列入克罗地亚战略项目清单）、SRCE / CIX / CARNET（国家 IXP 与学术基础设施，仅明确数据中心服务/站点时计数）。
- **Pantheon AI / Topusko**：公告称 1 GW 总容量、800 MW 可用 IT 负载、500 MW 太阳能、2 GW/8 GWh BESS、2027-2029 时间线（Sisak-Moslavina 郡 Topusko/Banovina/Pecka-Katinovac-Crni Potok 一带）——B/C 线索，待政府许可、环评、电网与土地记录确认前保持 prospective。
- **厂商/承包商**：Vertiv、Schneider、ABB、Siemens、Končar、HEP/HOPS 承包商；`"podatkovni centar" "referenca" "{vendor}"` 可揭示建造伙伴、发电机许可、并网、冷却升级或设施改造。

## 来源分级

- **A** = 官方/一手：eDozvola/MPGI 已签发选址/施工/使用许可、MZOZT/MINGO PUO/OPUO/EIA 文件、HOPS/HEP/HERA 电网文件、HAKOM e-Operator、EOJN/TED 采购公告与中标、运营商官方设施页（存在性 A-）、Uptime/EN 50600 认证、CIX/SRCE 官方 IXP 地点通知（A 级 CIX 事实）。
- **B** = 强二手：DCD/强贸易媒体、承包商案例、交易所/公司披露、权威本地商业媒体（引用官方许可或运营商申报时）、PeeringDB 活跃对等信号。
- **C** = 弱：Baxtel/DataCenterMap/Datacenters.com/Cloudscene/Data Center Catalog（无验证时）、社媒、市场片段、SEO 托管页、地方政府招商文（未链许可或官方决定）、公告驱动新闻。
- **容量规则**：IT 负载 MW/MVA、总功率、机架、白空间 sqm、认证/Tier、技术房间数、投资额——按来源类型记录；不从发电机/变电站值推断 IT 负载；聚合器 MW 需许可/EIA/电网/运营商技术文档复核，营销容量标 planned/design。
- **分类规则**：AWS 克罗地亚设计设施 ≠ 云区域/数据中心区域；无克罗地亚设施证据的云/托管服务页不计数；CIX 节点本身不计商业数据中心（宿主设施具名除外）；AI 超级园区公告在许可/战略项目决定/EIA/电力证据前不计数。
- **郡属规则**：按物理站点而非销售处/总部定郡；Zagreb 市场目录页常把带状设施归"Zagreb"——Jastrebarsko/Križ 归 Zagreb County，Topusko 归 Sisak-Moslavina。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL 中 `country_code == "HR"` 的条目，按 division 分组（20 郡 + Zagreb City）。
2. 国家扫描：eDozvola/Oglasna ploča → ISPU/MPGI 空间规划与许可 → MZOZT/MINGO 环评 → HOPS/HEP/HERA → HAKOM e-Operator → 云官方区域/边缘页 → EOJN/TED → 最后才用贸易/聚合器列表补漏。
3. 最佳首轮顺序：**Zagreb City → Zagreb County → Varazdin → Sisak-Moslavina/Topusko 线索 → Split-Dalmatia → Primorje-Gorski Kotar → Osijek-Baranja → Istria → 沿海郡 → 其余内陆郡**。
4. 规范化项目身份：运营商最终母公司、设施品牌、法人、地址/市镇、郡、阶段；别名归一（Altus IT vs Digital Realty、Vipnet vs A1、PCK vs DataCross）。
5. 每条候选记录要求至少一个 A 级地点/状态来源（许可、使用许可、环评决定、HOPS/HEP 连接或官方运营商页）；容量独立于存在性。
6. 按 world schema 输出：`{country_code: "HR", country_name: "Croatia", division, city, name, operator, status, capacity_mw, source_urls, evidence_date, evidence_grade, notes}`（参考 explorer-official.md §5.3 示例 JSON）；负结果 `no_projects: true` 仅在对 eDozvola、MZOZT、HAKOM/运营商、EOJN、贸易/聚合器全部扫描为负后标记。
7. **NO-DELETION**：不改写 explorer-official.md / explorer-industry.md；复核批次只增补不删行。

## 待办（2026-08-12 02:40Z）

- 两份探索报告已合并为国家层方法论；下一步以本 skill 为国家层参考运行 HR 探索/复核批次（21 分区）。
- 需验证：Digital Realty ZAG1 的 eDozvola 许可/使用记录与当前容量；DataBox 物理地址（区分于 Digital Realty 生态）；PCK-DataCross Jastrebarsko 与 Križ 两址当前足迹；Croatian Web Hosting 地址与认证；Hrvatski Telekom/Telemach 是否有具名物理设施；Pantheon/Topusko 是否出现 eDozvola/环评/电网/土地记录；DC North 容量与 HOPS/HEP 连接；HRDCA "22 个活跃私有数据中心"说法逐设施核验。
