---
name: lv-datacenter-methodology
location: scripts/expansion/world/country-skills/LV/SKILL.md
description: |
  Latvia (LV) datacenter discovery & audit methodology — how to enumerate, verify, and update Latvia datacenter projects at municipality/state-city granularity (43 divisions in the current manifest). Latvia has no single public data-center registry: enumeration joins the national Building Information System (BIS/bis.gov.lv — construction intentions, permits buvatlauja, commissioning nodosana ekspluatacija), municipal construction-board/council/utility documents (Salaspils DC7 Krasta iela 2/1 is the flagship municipal-document case), AST/Sadales tikls/SPRK electricity evidence (110 kV/20 kV), environmental records (VPVB/VVD), official cloud-region pages (no hyperscale LV region — negative context), and operator pages (Delska/DEAC LV DC1-DC3, Tet/Tet Cloud Riga sites + DC7 Salaspils, LVRTC Baltic Data Hub + Positron Kurzeme, Northern Energy Liepaja 120 MW / Jekabpils Old Airport 114 MW planned). Latvian terms matter (datu centrs, buvatlauja, elektroapgade, atlikumsiltums); lifecycle: teritorijas planojums < buvniecibas iecere < buvatlauja < buvdarbi < nodosana ekspluatacija. Read this before running LV exploration/audit batches. Routes to explorer-official.md (BIS/municipal/energy/environment/cloud/seeds) and explorer-industry.md (operators/trade press/directories/division tiers/aliases).
---

# LV · 拉脱维亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：拉脱维亚**没有**单一的公开数据中心注册库；枚举靠**拼接**国家建筑信息系统（BIS）、市政建设委员会/议会/公用事业文件、AST/Sadales tikls/SPRK 电力证据、环境记录、云区域官方负面核查与运营商页。
> 实用许可源 = **BIS（Buvniecibas informacijas sistema, bis.gov.lv）**：公开“计划/在建建筑”列表与地图，A 级建设意向与流程记录；市政 `buvvalde`/BIP/议会纪要/采购页不可或缺（拉脱维亚市政页常发布道路地役权、电缆项目、供热互联、土地租赁与建设委员会决定）。
> 拉脱维亚语重要：`datu centrs` `datucentrs` `serveru telpa` `kolokacija` `buvatlauja` `nodosana ekspluatacija` `elektroapgade` `20 kV` `110 kV` `siltuma atguve` `atlikumsiltums`；文件不写 “data center” 也可作电信/IT/工业/能源/办公楼处理。
> 已确认商业容量集中在 **Riga + 都市区（Salaspils、Kekavas novads）**；强非 Riga 线索：**Liepaja**、**Jekabpils novads**、**Ventspils/Kurzeme**（LVRTC Positron）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供拉脱维亚探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：BIS/BVKB 建设系统（planned constructions 列表+地图）、市政规划/BIP/议会与公用事业文件（Salaspils DC7 范例）、SPRK/AST/Sadales tikls 电力与监管、VPVB/VVD/LVGMC 环评、云区域官方负面核查（无 LV 区域）、一手设施种子（Delska/Tet DC7/LVRTC/Northern Energy/C.T.Co）、43 分区工作流与优先级簇、可靠性规则与字段 |
| `explorer-industry.md` | 行业/厂商发现：DCD/LSM/Labs of Latvia/Baltic Times/Datacenter Forum 媒体、Citrus Solutions 承包商页、目录（DataCenterMap/Baxtel/Datacenters.com/Cloudscene/PeeringDB/ColoMap）、运营商种子（Delska-DEAC/Tet Cloud/LVRTC-Baltic Data Hub-Positron/Northern Energy/Telia/Eway）、全国查询模式（英拉双语）、分区三级策略、实体与地址别名表、证据分级与假阳性 |

## 核心结构事实（框定每次搜索）

1. **BIS 是许可主干（A）**：bis.gov.lv/en、planned/current construction 列表与地图（bismap，JS 重、部分细节需 Latvija.lv 认证）；BVKB 管理、经济部上下文；提取案件号、`buvvalde`、项目名/功能、建筑组别、阶段、申请人/投资人法人、地址/地籍号/地块、决定类型与日期（建设意向/设计条件/许可/开工/投运）、外部工程（20/110 kV 电缆、变电站、光纤、冷热、发电机/燃料库）。
2. **生命周期词**：`teritorijas planojums/lokaplanojums/detaplanojums` < `buvniecibas iecere` < `buvprojekts` < `buvatlauja` < `buvdarbi/buvdarbu uzsaksana` < `nodosana ekspluatacija` < `sviniga atklasana/pirmie klienti`；只有 `buvatlauja`/`buvdarbu uzsaksana`/`nodosana ekspluatacija`/运营商确认启用算强证据；规划/电网容量/地产公告为计划/开发前。
3. **电网证据**：SPRK（单一 TSO=Augstsprieguma tikls/AST；8 个 DSO，Sadales tikls 供 99% 用户）；AST 并网页/发展计划；直接 110 kV 输电连接需求、20 kV 配网/外部供电建设、变电站名（Salaspils、Riga CHP/HPP、Liepaja 工业/SEZ、Jekabpils 110 kV、Kurzeme Ring/Broceni/Ventspils）、余热/冷却与区域供热互联（`Salaspils Siltums`）；**电网接入证据不证明运营**，须绑定 BIS/市政/运营商记录。
4. **云区域：无 LV 超规模区域（负面核查）**：AWS/Azure/GCP/OCI 官方列表均无拉脱维亚区域；不从云客户/办公室/MSP 推断设施；拉脱维亚主要超大规模线索是运营商/开发商/能源，不是云区域页。
5. **一手设施种子（A=运营商页存在/状态，B=容量）**：Delska/DEAC——EU North Riga LV DC1（10 MW/1,000 racks，AI/HPC-ready）、LV DC2（Cuibes iela 17，2 MW/240 racks）、LV DC3（Jana Asara iela 24，1 MW/80 racks，地下）；Tet——Riga Dattum 1.4 MW/Brivibas 0.7 MW/Kleistu 1.2 MW/Perses 0.7 MW/Atlasa 40 cabinets/DC6 Kleistu iela 5 0.3 MW，Salaspils DC7（Krasta iela 2/1，EUR30m+，一期 2026 投运，2028 全建成，液冷/AI 就绪 + Salaspils Siltums 余热）；LVRTC——两个 Riga 站点 + 一个约 150 km 的区域枢纽 + 每 100 km 全国 colo 网络，Positron（Kurzeme 高安全，2027 初投运，位置可能刻意不明确）；Northern Energy——Liepaja SEZ 120 MW（2029，110/33 kV）、Jekabpils Old Airport 114 MW 可用/2030 扩 400 MW（110 kV）——均为计划级直至市政/BIS/AST/投运记录确认；C.T.Co/Valdlauci（2015 完工、20 racks、Meistaru Street 33，B 级承包商）。
6. **假阳性**：政府“data centers”=统计/地理信息中心；`serveru telpa` 在办公室/学校/市政楼（无托管/colo 功能）；电信 POP 无机架/托管证据；云服务商/reseller 无物理设施声明；不披露地点的敏感公共部门/安全站点（保留公开地理、不推断精确市镇）；`datu`+`centrs` 二字组合的统计/地理门户、图书馆/数据库中心、学校 IT 房。
7. **状态规则**：`operational`=运营商 launched/available 或市政投运源；`construction`=施工中（许可/奠基/封顶证据）；`planned`=开发商/市政宣布项目+场地+容量但无公开施工/投运证明；`unknown/historical`=仅目录/注册/旧承包商证据；Liepaja/Jekabpils 大 MW 项目须与 Riga 运营设施分开捕获生命周期阶段。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§4 / explorer-industry.md §3/§4）

- 许可/市政：`site:bis.gov.lv "datu centrs" "{municipality}"`、`site:bis.gov.lv "{operator}" "buvniecibas"`、`"{municipality}" "datu centrs" "buvatlauja"`、`"{municipality}" "datu centra" "nodosana ekspluatacija"`、`site:{municipality-domain} "datu centrs" "lemums"`、`site:{municipality-domain} "datu centram" "20kV"`、`filetype:pdf "datu centrs" "buvatlauja"`。
- 能源/环评：`site:ast.lv "data centre" Latvia "110 kV"`、`site:sadalestikls.lv "datu centrs"`、`site:sprk.gov.lv "datu centrs"`、`site:vpvb.gov.lv "datu centrs"`、`"{operator}" "{municipality}" "atlikumsiltums"`、`"datu centrs" "dizelgeneratori" "ietekmes uz vidi"`。
- 英文：`"Salaspils" "DC7" "data center" "building permit"`、`"Liepaja" "data centre" "120 MW"`、`"Jekabpils Old Airport" "data centre" "114 MW"`、`"Riga" "Delska" "10 MW" "data center"`、`"LVRTC" "Positron" "data center"`。
- 行业：`site:datacenterdynamics.com Latvia Tet Delska DEAC LVRTC data center`、`site:eng.lsm.lv Tet data center Salaspils Latvia`、`site:labsoflatvia.com "data center" Latvia`、`site:baltictimes.com "data center" Latvia`、`site:datacenterdynamics.com Latvia DC7 Salaspils`。
- 拉语：`"datu centrs" Riga Tet Delska DEAC LVRTC`、`"datu centrs" Salaspils Tet DC7`、`"datu centra" "pirma karta" "ekspluatacija"`、`"datu centram" "siltumapgade" OR "atlikumsiltums"`、`"datu centram" "20kV" OR "110kV"`、`"serveru telpa" "kolokacija" Latvija`。
- 地址 pivot：`"Cuibes iela 17" OR "Ķuibes iela 17"`、`"Jana Asara iela 24" OR "Jāņa Asara iela 24"`、`"Kleistu iela 5"`、`"Krasta iela 2/1" "DC7"`、`"Meistaru iela 33" Valdlauci`、`"Talejas iela 1" LVRTC`。

## 官方/监管管线要点（详见 explorer-official.md）

- BIS/BVKB：建设意向与流程 A；公开地图 JS 重；提取建设案件、许可、投运与外部工程；记录不要求写 `datu centrs`——按运营商法人名与地址 pivot。
- 市政：A 级——议会决定、公众咨询材料、建设委员会通知、公用事业线路批准；Salaspils 议会 PDF 找到 DC7 的 Krasta iela 2/1 光学连接（Salaspils 变电站）与外部 20 kV 供电（A 级市政公用事业事实）；Kekavas novads（C.T.Co）、Liepaja（SEZ）、Jekabpils（机场地块）为完整性检查。
- 电网：SPRK/AST/Sadales tikls；110 kV/20 kV/变电站名/请求负载/余热互联；上下文强于公开大负荷清单；电网证据须绑定具名建筑/项目。
- 环评：VPVB（EIA）、VVD（许可/控制）、LVGMC（数据）；大多数拉脱维亚 DC 不太可能触发全量 EIA；环境记录对大型发电机/燃料/冷却或工业场地转换更有用；提取备用发电机/燃料库、电池/UPS 房、冷却塔/冷水机与用水、噪声、热复用/区域供热、施工交通。
- 云：无 LV 超规模区域（负面核查）；官方区域页证明逻辑服务地理而非建筑位置。
- 分区工作流：每 division ① 拉语扫（datu centrs/buvatlauja/serveru telpa/elektroapgade/nodosana ekspluatacija）→ ② BIS 手动（列表+地图）→ ③ 市政文件（lemums/domes sede/20kV/110kV/atlikumsiltums/buvvalde）→ ④ AST/Sadales tikls/SPRK 官方页 → ⑤ 分级存储（operator_status / construction_status / energy_status / confidence）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 媒体：DCD（B，Tet DC7 2026 投运与 DEAC/Delska 发展最佳国际源）、LSM English（B，国家大项目确认）、Labs of Latvia（B/C）、Baltic Times/BNN（B/C）、Datacenter Forum（B/C，转载运营商发布）、Citrus Solutions 承包商页（B，C.T.Co 完工）。
- 目录（C/C+ 线索，须运营商/市政核实）：DataCenterMap（Riga 种子，覆盖滞后）、Baxtel（C+，Delska/Tet/LVRTC/Telia 快速列表）、Datacenters.com（C）、Cloudscene（C）、PeeringDB（B=互联信号，C=完整普查）、ColoMap/Inflect（C，LVRTC/Telia 区域地址）。
- 运营商种子：Delska/DEAC（LV DC1 10 MW/DC2 2 MW/DC3 1 MW）、Tet Cloud（Riga Dattum/Brivibas/Kleistu/Perses/Atlasa/DC6 + Salaspils DC7）、LVRTC（两个 Riga + 区域枢纽 + 全国 colo + Positron）、Northern Energy（Liepaja 120 MW/Jekabpils 114-400 MW，计划）、Telia/Liepaja（聚合器 C）、Eway/Ogre（历史 C）、C.T.Co（B）、本地 ISP/服务器房（边缘/托管普查，勿与物理 DC 混）。
- 别名表：Delska/DEAC/DEAC European Data Center Operator/Data Logistics Center；Tet/Tet Cloud/Lattelecom/SIA Tet/DC7/Dattum；LVRTC/Latvijas Valsts radio un televizijas centrs/Baltic Data Hub/Pozitrons；Northern Energy/Northern Europe Energy Group；C.T.Co/Fraternitas/Citrus Solutions；Telia/Eway；地址别名（Cuibes 17、Jana Asara 24、Kleistu 5、Krasta 2/1、Meistaru 33、Talejas 1、Riga TV Tower）。

## 来源分级

- **A** = 官方/一手：BIS 记录、市政议会/建设委员会/公用事业文件、SPRK/AST/Sadales tikls 官方页、运营商设施页、官方云区域列表、LVRTC/Tet/Delska/Northern Energy 官方页。
- **B** = 强二级：DCD、LSM、Labs of Latvia、Baltic Times、承包商页（Citrus Solutions）、PeeringDB 互联信号。
- **C** = 弱/未验证：DataCenterMap/Baxtel/Datacenters.com/Cloudscene/ColoMap/Inflect、Lursoft 片段、市场页、社交、无源市场报告；聚合目录条目除非运营商/市政/BIS/监管源确认否则不升级。
- 区分商业/区域 colo 与超大规模/AI 园区；区分电信/企业服务器房与 colo。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=LV，divisions=43 市镇/州级市）。
2. 建种子：运营商页（Delska-DEAC/Tet Cloud/LVRTC/Northern Energy）+ 地址 pivot（Cuibes 17、Jana Asara 24、Kleistu 5、Krasta 2/1、Meistaru 33、Talejas 1）+ DCD/LSM 首扫。
3. 分级：Tier 1 高概率（Riga、Salaspils、Liepaja、Jekabpils、Kekavas、Kurzeme/Ventspils 簇）跑全流程；Tier 2 区域城市/LVRTC/电信边缘（Daugavpils、Valmiera、Rezekne、Jelgava、Jurmala、Ventspils、Liepaja——LVRTC RTS 站点仅在明确描述 colo/数据中心/互联服务时捕获）；Tier 3 其余市镇紧凑扫后无信号写 `no_projects: true`。
4. 状态判定（operational/construction/planned/unknown-historical）并把 operator_status 与 construction_status 分开存。
5. 输出 world 同 schema，字段含 name/division/address/cadastral/developer_operator/legal_entity/status/capacity_mw/racks/construction_evidence_url/operator_evidence_url/energy_evidence_url/evidence_date/evidence_grade/notes。
6. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：codex terra agent（max thinking）每 agent 分批复核拉脱维亚数据中心（43 市镇粒度）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Tet DC7 二期/2028 全建成与 Salaspils Siltums 余热细节；Northern Energy Liepaja 120 MW 与 Jekabpils 114 MW 的市政/BIS/AST 证据与生命周期阶段；LVRTC Positron 的精确市镇（若公开）与 2027 投运；Delska LV DC2/DC3 的 BIS 记录；LVRTC 全国 colo 节点（Riga TV Tower/Talejas 1/Ventspils RTS 等）的官方确认。
