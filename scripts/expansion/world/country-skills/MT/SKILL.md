---
name: mt-datacenter-methodology
location: scripts/expansion/world/country-skills/MT/SKILL.md
description: |
  Malta (MT) datacentre discovery & audit methodology — how to enumerate, verify, and update Malta datacentre projects at local-council granularity (68 divisions in the current manifest). Malta is a compact single-planning-market country: Planning Authority (PA) records and weekly Government Gazette PA notices are the main development-permit backbone (centralized, not per-council), joined by ERA Medium Combustion Plant permits (backup generators — e.g. Melita Data Centre EP1255/22 Swieqi), Enemalta/REWS/Energy & Water Agency grid evidence, MCA authorised-undertakings register, MITA government datacentre pages (Santa Venera; Gozo/Victoria leads), official cloud-region pages (no hyperscale MT region — negative context), and operator pages (MITA, BMIT Handaq/SmartCity/Żejtun, Melita, GO, Epic, Continent 8, CSL, Heritage Malta). Capacity evidence is rarely MW (racks/sqm/generator thermal bands); Enemalta/Streamcast Marsa project is officially launched but later reported abandoned — record conservatively. Beware IXOne/Aria name traps and locality boundary variants (Mriehel, Madliena, Rabat Gozo). Read this before running MT exploration/audit batches. Routes to explorer-official.md (planning/environment/energy/telecom/government/cloud) and explorer-industry.md (operators/trade press/directories/locality recipes).
---

# MT · 马耳他数据中心查询方法论（Datacentre Discovery & Audit Methodology）

> 目的：马耳他**没有**全国数据中心注册库，但规划许可高度集中：**规划局（Planning Authority, PA）记录与政府公报每周 PA 通知是开发许可主干**（按 local council 分区，许可却是中央化的）。
> 枚举组合：PA/eApplications/公报、ERA 中型燃烧装置（MCP）许可（备用发电机）、Enemalta/REWS 电网、MCA 授权运营商注册表、MITA 政府数据中心页、云区域官方负面核查与运营商页。
> 市场小且服务商主导：多为电信/政府/colo 机房，公开 MW 披露罕见——机架数、面积、发电机许可、变电站引用与官方设施页更常见；iGaming/fintech/DR 需求产生大量云/VPS/托管页，**不证明物理设施**。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供马耳他探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：PA/eApplications/PA map server/政府公报 PA 列表/MSDI、ERA（MCP 类别与 Melita EP1255/22 实例、工业许可程序）、Enemalta/REWS/能源水务署（马耳他-西西里互联）、MCA 授权运营商与频谱、MITA 数据中心页与 Gozo 采购线索、云区域官方页（无 MT 区域）、68 地方议会分区枚举工作流与高产区、置信度与陷阱 |
| `explorer-industry.md` | 行业/厂商发现：运营商/厂商种子表（MITA/BMIT Handaq-SmartCity-Żejtun/Melita/GO/Epic/Continent 8/CSL/MIX/Heritage Malta/Enemalta-Streamcast）、IXOne/Aria 名称陷阱负面对照、DCD/Times of Malta/MaltaToday/TVM/独立报/马耳他证交所媒体、目录（DataCenterMap 12 设施 8 市场/Datacenters.com/Cloudscene 等）、目录→一手验证工作流、地方议会搜索配方与拼写陷阱、容量提取指引（机架/面积/发电机热输入，非 MW） |

## 核心结构事实（框定每次搜索）

1. **PA + 政府公报是主干（A）**：eApplications（eapps.pa.org.mt）、PA map server/PlanningMT 应用（地图层）、每周 Gazette PA 列表（gov.mt DOI）、BusinessFirst 许可确认、MSDI 地理门户；关键词集：`data centre/data center/datacentre` `server farm` `server room` `ICT facility` `telecommunications equipment` `hosting facility` `co-location` `backup/standby generators` `substation` `change of use "data centre"` + 地名（Bulebel/SmartCity/Handaq/Madliena/Marsa underground）+ 马耳他语（`ċentru tad-data` `server farm` `permess` `applikazzjoni` `iżvilupp`）。
2. **ERA MCP 许可 = 发电机高产区（A）**：中型燃烧装置新设即需运营许可；实例 `Melita Data Centre`（Swieqi，Triq il-Madliena，EP1255/22，两台柴油机，含坐标与热输入带）；热输入带**不得换算为 IT load**，只作发电机/排放证据。
3. **地理与边界变体**：`Mriehel/Mriehel-CBD` 可能归 Birkirkara 或 Qormi；`Madliena` 二级列表可归 Naxxar，而 ERA 把 Melita DC 记为 Swieqi；`Victoria`=Gozo 的 Rabat（勿与 Malta 岛 Rabat 混淆）；`Ħamrun`、`Mellieħa`、`Għajnsielem` 等拼写需规范；电信总部地址≠数据中心地址（Epic/Luqa、BMIT/Pembroke 是办公室，不作物证）。
4. **云区域：无 MT 区域（负面核查）**：AWS/Azure/GCP/OCI 官方列表均无马耳他区域；本地 reseller 的 cloud/VPS/IaaS 不构成超规模区域。
5. **已知设施种子（A 级官方/运营商页）**：MITA 数据中心（Santa Venera，Old Railway Track）+ Gozo Data Centre（Victoria/Rabat Gozo，采购附录线索）；BMIT Handaq（Qormi，~300 racks 目录）、BMIT SmartCity（Kalkara）、BMIT Żejtun（Bulebel，2019 官方宣布、Tier III 目标、>400 racks、EUR 10m）；Melita Primary DC（Swieqi/Madliena，ERA EP1255/22）+ Mriehel 次级；GO Birkirkara + GO Marsa（目录地址，须 PA/ERA 确认）；Epic（Santa Venera 目录，Luqa 为总部）；Continent 8（Santa Venera + 第二个未披露 Malta 设施）；CSL（Birkirkara/CBD，官方 2,000 sqm 机架空间）；Heritage Malta 数据中心（Kalkara/Bighi，2025 官方新闻，内部/档案）；MIX（Msida/大学，互联线索）。
6. **Enemalta/Streamcast Marsa**：官方 2018 启动证据（地下数据中心试点），但后续贸易/法院报道显示项目未按计划落地——状态保守记 `rejected/abandoned`，除非新的一手运营证据。
7. **容量证据多为非 MW**：机架数（BMIT Żejtun >400、Handaq ~300）、面积（BMIT 1,200 sqm 可用、CSL 2,000 sqm）、发电机热输入带、每机架功率（勿乘全机架数除非源支持）、投资额（Żejtun EUR 10m、SmartCity EUR 3.5m、Streamcast EUR 5m 试点/EUR 75m 提议）只是项目规模信号，不是 MW。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§2 / explorer-industry.md §4）

- PA/公报：`site:pa.org.mt "data centre"`、`"{division}" "data centre" "Planning Authority"`、`site:gov.mt "Planning Authority" "{division}" "data centre"`、`"change of use" "data centre" Malta`、`"Bulebel" "data centre"`、`"SmartCity" "data centre"`。
- ERA：`site:era.org.mt/era_mcp "data centre"`、`site:era.org.mt/era_mcp "BMIT" OR "Melita" OR "GO" OR "Epic" OR "MITA"`、`"EP" "data centre" "Malta" "ERA"`。
- 能源/电网：`site:enemalta.com.mt "data center" OR "data centre"`、`"data centre" "Enemalta" "Marsa"`、`"data centre" "Bulebel" "substation"`、`"{operator}" "{locality}" "MVA"`、`site:rews.org.mt "data centre"`。
- 电信：`site:mca.org.mt "Register of Authorised Undertakings"`、`site:mca.org.mt "GO plc" "Melita" "Epic"`、`site:mix.net.mt "Malta Internet Exchange"`、`"MIX" "University of Malta" "data centre"`。
- MITA：`site:mita.gov.mt "Data Centre" "Santa Venera"`、`site:procurement.mita.gov.mt "Gozo Data Centre"`、`site:mita.gov.mt "Old Railway Track"`。
- 运营商：`"{operator}" "Malta" "data centre"`、`"{operator}" "{locality}" "colocation"`、`"BMIT" "Handaq" "data centre"`、`"BMIT" "Zejtun" "data centre"`、`"Melita" "Madliena" "data centre"`、`"GO" "Marsa" "data centre"`、`"Continent 8" "Malta DC2"`、`"CSL" "Dun Karm Street" "data centre"`。
- 媒体/证交所：`site:datacenterdynamics.com/en/news/ "Malta" "data center"`、`site:timesofmalta.com "data centre" "MITA"`、`site:maltatoday.com.mt "Streamcast" "Enemalta" "data centre"`、`site:borzamalta.com.mt BMIT`。
- 通用分区：`"{division}" "Malta" "data centre"`、`"{division}" "Malta" "server farm"`、`"{division}" "Malta" "backup generator" "data centre"`、`"{division}" "Malta" "substation" "data centre"`；变体：`"Santa Venera" OR "St Venera"`、`"Qormi" OR "Handaq"`、`"Swieqi" OR "Madliena"`、`"Zejtun" OR "Bulebel"`、`"Victoria" "Gozo Data Centre"`。
- 负面对照：`"IXOne" "Malta" "data centre"`、`"Aria" "Malta" colocation`（名称陷阱，保持负日志）、`"Epic" "Luqa" "data centre"`（总部≠设施）。

## 官方/监管管线要点（详见 explorer-official.md）

- PA：申请号、开发类型、申请人/SPV、业主、建筑师/perit、地点、地址、地块/工业园；描述、用途变更措辞、楼层/机房数、面积、披露机架数；电气连接/变电站、发电机数、燃料库、冷却厂、声学/空气质量文件；状态（received/validated/approved/refused/reconsideration/appeal/development notification/enforcement）与条件（运行时段/噪声/排放/消防）。
- ERA：MCP 新设即需许可（A）；设施名/地点/坐标/许可号/燃料/运营日期/热输入带为 A 级；热输入带不作 IT load；ERA 地点与 PA/运营商页边界名差异时交叉核对。
- 能源：Enemalta（电网运营、客户接入程序、主要配电升级）、REWS（许可/监管、可再生能源/CHP/储能单点联系）、能源水务署（供应安全、马耳他-西西里互联）；提取变电站/馈线/MVA/MW 时确认属于 DC 本身。
- 电信：MCA 授权运营商注册表（GO/Melita/Epic/Vanilla 及小 ECS/ISP）、频谱许可（确认授权，非 DC 列表）、市场报告（识别主要基础设施业主）；MIX 为互联证据与 Msida/大学线索。
- MITA：官方数据中心页（Santa Venera SVR9019）+ Gozo Innovation Hub（Xewkija，**无设施证据不计数**）+ 采购附录 WAN/光纤链引用 Gozo Data Centre（Victoria）。
- 云：无 MT 区域（负面核查）；reseller 云不升级。
- 升级规则：PA/Gazette/ERA/MITA/运营商官方页确认物理设施或许可才给 A；贸易媒体为 B 直至一手记录核验。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 媒体：DCD（B，BMIT Żejtun 与 Streamcast/Marsa 历史最佳国际源）、Times of Malta（B）、MaltaToday（B，SmartCity/Streamcast 废弃与法院报道）、TVM/PBS（B）、The Malta Independent（B）、马耳他证交所/Borza Malta（A/B，上市公司披露如 BMIT/MPC 交易与物业细节）。
- 目录（C，须匹配一手）：DataCenterMap（当前 12 设施 8 市场，马耳他最佳开放目录）、Datacenters.com、Cloudscene、Data Center Platform/Catalog/Colomap/Upstack（GO Marsa、BMIT Qormi/SmartCity、Epic St Venera 旧地址）。
- 运营商种子：MITA、BMIT（Handaq/SmartCity/Żejtun）、Melita Business（官方托管/云 + ERA 佐证）、GO（官方 wholesale/hosting）、Epic（官方服务页，地址目录级）、Continent 8（官方“两个多样化 Malta 设施”）、CSL（官方 Tier 3 载波中立 2,000 sqm）、MIX/NIC（互联）、Heritage Malta（2025 内部）、Enemalta/Streamcast（废弃倾向）。
- IXOne/Aria：定向搜索无可验证的马耳他运营商/设施——名称消歧陷阱；无公司注册号/设施地址/运营商页前不得升级；保留负对照查询日志。
- 目录→一手工作流：DataCenterMap/Cloudscene 只作种子 → 精确名+地点+运营商官方域 → PA/eApplications/Gazette 查地址 → ERA MCP 查发电机 → MBR 查法人 + 证交所公告；纯目录记录 C 并注明缺失的一手证据。

## 来源分级

- **A** = 官方/一手：PA 申请/决定、政府公报 PA 通知、ERA MCP 许可、MITA 官方数据中心页、具物理地点的运营商官方页、MCA/REWS/Enemalta 官方记录（电信/能源上下文）、证交所/公司备案。
- **B** = 强二级：DCD/MaltaToday/Times of Malta/TVM/The Malta Independent 具名报道、公司公告转载、证交所新闻。
- **C** = 弱/未验证：DataCenterMap/Datacenters.com/Cloudscene/Data Center Platform/Colomap/Upstack、无设施所有权/地址的通用托管/VPS 页。
- 去重/归派：Mriehel/CBD/Handaq 的 Birkirkara-Qormi 归属不一致须双记录后定；Madliena 按一手（ERA=Swieqi）优先；Rabat Gozo=Victoria；总部≠设施；同一运营商多站点（BMIT 三址、Melita 两址）按地址/许可/官方页合并。
- 容量：无公开 MW 时 `capacity_mw: null`，把披露代理（机架/面积/热输入/投资额）记入 notes，不推导虚假 MW。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=MT，divisions=68 地方议会）。
2. 建种子：运营商官方页（MITA/BMIT/Melita/GO/Epic/Continent 8/CSL/Heritage Malta）+ 高产区清单（Santa Venera/Birkirkara/Qormi-Handaq-Mriehel/Kalkara-SmartCity/Swieqi-Madliena/Marsa/Żejtun-Bulebel/Gzira/Msida/Victoria-Gozo）。
3. 每个分区：PA/eApplications + Gazette 英文/马耳他语词 → ERA MCP（地点+运营商）→ MCA 授权运营商 → Enemalta/REWS 电力/变电站/储能 → 精确设施/运营商名查 MBR（mbr.mt）验证法人/SPV。
4. 状态：PA 决定/ERA 许可/MITA/运营商页=运营或已许可；仅目录/媒体=线索（C/B）；Streamcast/Marsa 按废弃处理除非新证据。
5. 低产区跑通用扫 + 最近工业园词，但需更强证据才记录。
6. 输出 world 同 schema；容量按代理记录；无证据分区写 `no_projects: true`。
7. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：codex terra agent（max thinking）每 agent 分批复核马耳他数据中心（68 地方议会粒度）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：BMIT Żejtun 2019 后的运营/当前状态与 PA 记录；GO Marsa 与 Epic Santa Venera 地址的一手确认；Continent 8 第二个 Malta 设施地点；MITA Gozo Data Centre（Victoria）的运营与采购证据；Enemalta/Streamcast Marsa 最终状态（法院/贸易更新）。
