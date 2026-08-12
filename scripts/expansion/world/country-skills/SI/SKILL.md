---
name: si-datacenter-methodology
location: scripts/expansion/world/country-skills/SI/SKILL.md
description: |
  Slovenia (SI) datacenter discovery & audit methodology — how to enumerate, verify, and update Slovenia datacenter projects at municipality (obcina) + administrative unit (upravna enota) granularity, grouped into 12 SURS statistical regions for field work (212 municipalities in the current manifest). Slovenia has no public national data-center registry: enumeration joins PIS/eGraditev construction acts (GD/UD/PG), municipal spatial-planning files (OPN/OPPN), environmental-assessment records (ARSO/MOPE/MNVP), ELES/SODO energy-grid evidence, public procurement (e-JN/enarocanje/TED), AKOS telecom-infrastructure context, official cloud-region pages (no hyperscale SI region — used as negative context), and operator pages (ARNES, Posta/Posita, Datacenter.si, T-2, Telekom Slovenije, A1, Telemach, SoftNET, MegaTel). Read this before running SI exploration/audit batches. Routes to explorer-official.md (permits/environment/energy/procurement/cloud) and explorer-industry.md (trade press/operators/directories/statistical-region sweeps).
---

# SI · 斯洛文尼亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：斯洛文尼亚**没有**公开的全国数据中心注册库，不能按单一门户枚举。
> 枚举靠**多源连接**：PIS/eGraditev 建设行政行为（GD建筑许可 / UD使用许可 / PG开工通知）、市政空间规划（OPN/OPPN）、环评与环境许可、ELES/SODO 电网证据、公共采购（e-JN/enarocanje/TED）、AKOS 电信基础设施、云区域官方页与运营商官方页。
> 小市场谱：希望得到的是“很多小型 kolokacija/电信/公共部门/研究-HPC/企业数据室”，而非超大规模云区域管线；必须严格过滤假阳性（统计数据门户、虚拟云服务、办公室等）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供斯洛文尼亚探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：PIS/eGraditev 建设行为库（GD/UD/PG）、市政 OPN/OPPN 与议会材料、GOV.SI/ARSO 环评与环境许可、ELES/SODO/能源监管机构电网证据、AKOS 电信监管与 Geoportal、e-JN/enarocanje/TED 采购、云区域负面上下文与 ARNES/部委/Posta 官方种子、12 统计区域官方枚举方法与证据分级 |
| `explorer-industry.md` | 行业/厂商发现：DCD/Slovenia Times/STA/Finance.si/Monitor 媒体、DATA CENTER by Palsit 会议、PostEurop/EuroHPC/SLING 研究与 AI Factory 上下文、DataCenterMap/Cloudscene/Baxtel/PeeringDB 目录、运营商种子表（ARNES/Posita/Datacenter.si/T-2/Telekom/A1/Telemach/SoftNET/MegaTel/Arctur 等）、12 区域行业扫描、状态语义与负面过滤、已知线索验证表 |

## 核心结构事实（框定每次搜索）

1. **无全国注册库，建设行为是主干**：PIS “Zbirka podatkov o graditvi objektov”（https://pis.eprostor.gov.si/pis-ua-jv）为 A 级建设行政行为元数据；标记 `GD`建筑许可、`UD`使用许可、`PG`开工/拆除通知，记录 `ID akta`、`Upravni organ`、`Naziv`、`Postopek`、地籍市镇、地块、CC-SI 分类、`Povezani akti`（可链 GD→PG→UD）。
2. **许可地理 = 市镇（obcina）+ 行政单位（upravna enota/UE）**：SURS 12 统计区域只是搜索分桶，每个候选项目须解析到市镇、地籍市镇（katastrska obcina）、地块、地址与行政行为。
3. **声明文件很少写 “data center”**：同时搜斯洛文尼亚语与英语：`podatkovni center` `racunalniski center` `strezniski center` `kolokacija` `oblak` `superracunalnik` `tovarna umetne inteligence` + 支撑设施词 `transformatorska postaja` `RTP` `prikljucitev` `agregat` `UPS` `hlajenje` `odvecna toplota`。
4. **无超规模云区域（负面上下文）**：AWS/Azure/GCP/OCI 官方区域列表无 SI 区域/local zone；不从云使用推断物理设施，而是通过 kolokacija/政府/运营商记录枚举。
5. **官方已知种子（A）**：ARNES Maribor 数据中心/斯洛文尼亚 AI Factory（2025-05 动土，约 2026 完工运营，余热再利用，采购 `JN003755/2024-EUe16/01`）；数字化转型部/斯洛文尼亚邮政（Posta/Posita）卢布尔雅邮政物流中心新数据中心 2025-09-30 交付部委；卢布尔雅大学 AI Factory 高密度混合数据中心；Posta/Posita 卢布尔雅 Vic 与 Maribor Tezno/Center 设施。
6. **地理分布**：Osrednjeslovenska/卢布尔雅（SIX/ARNES、电信、kolokacija）最密；Podravska/Maribor（ARNES、Posta/Posita、政府与研究）；Goriska/Nova Gorica（Arctur、跨境的里雅斯特光纤佐邻）；Obalno-kraska/Koper（SoftNET、港口/物流 IT）；Gorenjska/Kranj（企业/工业数据室）；其余区域低概率。
7. **多数小型设施在现有建筑内**：无独立建筑许可的企业/政府服务器房多，必搜 `sprememba namembnosti`（用途变更）、改建、HVAC/UPS/发电机工程与采购记录。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§2 / explorer-industry.md §3）

- 官方建设：`site:pis.eprostor.gov.si/pis-ua-jv "podatkovni center"`、`site:pis.eprostor.gov.si/pis-ua-jv "{operator}" "{municipality}"`、`site:pis.eprostor.gov.si/pis-ua-jv "transformatorska postaja" "{municipality}"`、`site:gov.si "podatkovni center" "gradnja" "{city}"`、`site:{municipality-domain} "podatkovni center" "OPPN" OR "OPN"`。
- 电网/环评：`site:eles.si "podatkovni center" OR "data centre"`、`site:sodo.si "podatkovni center"`、`site:elektro-ljubljana.si "podatkovni center" OR "RTP" "{municipality}"`（同理 elektro-maribor/celje/gorenjska/primorska）、`"podatkovni center" "presoja vplivov na okolje"`、`site:gov.si "podatkovni center" "okolje"`、`"podatkovni center" "odvecna toplota"`。
- 采购：`site:ejn.gov.si "podatkovni center" "Gradnje"`、`site:ejn.gov.si "podatkovni center" "Maribor" OR "Ljubljana"`、`site:enarocanje.si "podatkovni center" "JN"`、`site:ted.europa.eu "Slovenia" "data centre" "construction"`、`"modularni podatkovni center" "Univerza v Ljubljani"`。
- 电信：`site:akos-rs.si "podatkovni center"`、`site:akos-rs.si "Geoportal AKOS" "{municipality}"`、`site:akos-rs.si "{operator}" "vzorcne ponudbe"`。
- 英文：`"Slovenia" "data center" "building permit"`、`"Ljubljana" "data center" "grid connection"`、`"Slovenia" "AI Factory" "data center" "Maribor"`、`"Slovenia" "colocation" Ljubljana Maribor Koper Nova Gorica`。
- 行业：`site:datacenterdynamics.com Slovenia ARNES OR Posta OR Ljubljana OR Maribor`、`site:finance.si "podatkovni center" "Pošta Slovenije" OR Arnes`、`site:sloveniatimes.com "data centre" Slovenia`、`site:posteurop.org "Slovenia" "data centre"`、`"podatkovni center" "referenca" Slovenija`（承包商引用）。
- 负面过滤：`"podatkovni portal"` `"podatkovna baza"` `"virtualni podatkovni center"`（无物理地点） `"cloud partner"`（无地址） `"pisarna" OR "office"`、`"data center services"`（无位置）。

## 官方/监管管线要点（详见 explorer-official.md）

- 建设主干：PIS/eGraditev（A，全国电子化执行至 2026）；生命周期 `OPN/OPPN` < `GD` < `PG` < `UD` < `predaja v uporabo/官方启用`；只有 GD/PG/UD、官方启用/交付、采购中标或运营商设施页算强证据。
- 空间规划：市政 OPN/OPPN、议会材料（obcinski svet/gradivo/sklep/odlok/javna razgrnitev）、土地行动（prodaja zemljisca/stavbna pravica/komunalni prispevek）；规划证据为 A 级用途过程，但除非明名数据中心/运营商/明确支撑设施，否则只作线索。
- 环评：GOV.SI 环评政策页、ARSO/MOPE/MNVP 通知、市政 “okoljevarstveno soglasje/dovoljenje” 公告；某些模块化/现有建筑内项目低于全量 EIA 门槛，但披露柴油发电机/大型冷却/余热再利用时信号最强；提取变压器容量、电网接入点、冷却/噪声/水、余热协议。
- 电网：ELES 传输网发展规划与 RES hosting-capacity 地图（A，作选址/可行性上下文，**不等于设施存在**）；SODO 配网发展、Agencija za energijo 监管、五大 DSO（elektro-ljubljana/maribor/celje/gorenjska/primorska）；优先检查 Ljubljana/Maribor/Koper/Nova Gorica/Kranj/Celje/Novo mesto 变电站周边。
- 电信：AKOS 运营商注册表、Geoportal AKOS（电子通信基础设施/网络接入点）、vzorcne ponudbe 运营商种子表；用于确认电信运营商法人名称以供 PIS/采购检索，非数据中心许可库。
- 采购：e-JN（ejn.gov.si，A）、enarocanje.si（A）、TED（A/B）；对模块化/现有建筑内项目而言采购常比许可更有信号；已见 e-JN 记录 `Podatkovni center Arnes - lokaciji Maribor in Ljubljana`（JN003755/2024-EUe16/01）。
- 云：无 AWS/Azure/GCP/OCI SI 区域（负面上下文）；官方种子为 ARNES Maribor、部委/Posta 卢布尔雅交付、SURS 地理架构（stat.si/obcine）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 媒体：DCD（B，ARNES/Posta/大学模块化 DC 最佳国际供给）、The Slovenia Times/STA（B）、Finance.si（B/C，容量与财务细节）、Monitor.si/Racunalniske novice（B/C）、PostEurop（B，Posta 扩张交叉验证）、EuroHPC/EuroCC/SLING/SLAIF（A/B，AI Factory 上下文）、DATA CENTER by Palsit 会议（B/C）。
- 目录（C/C+线索，必须官方核实）：DataCenterMap Slovenia（卢布尔雅/Maribor/Nova Gorica/Koper 共约 20 条）、Cloudscene、Datacenters.com、Inflect、Baxtel（C+）、PeeringDB（B/C，互联/网络存在）。
- 运营商种子（A=存在、B=容量/服务声明）：ARNES/SIX、Ministry of Digital Transformation/Posta/Posita（卢布尔雅 Vic + Maribor Tezno/Center）、Datacenter.si/RVO（卢布尔雅科技园 18 - SIX + Center）、T-2、Telekom Slovenije（虚拟 DC，纯服务线索）、A1、Telemach（DC1/DC2 目录线索）、SoftNET（卢布尔雅/Koper）、MEGA M/MegaTel（Velenje 总部）、PERFTECH/Akton/Mikrocop/NIL-Conscia/Kontron（整合商 pivot）、Arctur（Nova Gorica）、IZUM/SLING。
- 状态语义：`operational`=官方交付/开业、UD、活跃 kolokacija 页或完工承包商引用；`under_construction`=PG、官方动土、已确认地点的建设采购；`planned/permitted`=GD、明名投资人的 OPN/OPPN、设计/建设采购中标前通知；`lead-only`=目录/贸易文章/云服务页/电信上下文；`no_project`=英斯双语与目录均无证据。
- **不计数**：云 reseller/服务提供商（无物理设施）、总部/分部办公室、统计/数据门户；普通服务器房仅在项目范围含企业/内部房且有物理证据时计入。

## 来源分级

- **A** = 官方/一手：PIS GD/PG/UD 行为、GOV.SI/市政/机构决定、官方采购中标/通知、ELES/SODO/AKOS 官方基础设施上下文、运营商设施页或政府交付/开业。
- **B** = 强二级：DCD/Slovenia Times/STA/Finance/Monitor 媒体、协会/会议材料、工程承包商客户案例、官方供应商服务页（不指明具体设施）、EuroHPC/SLING 项目页。
- **C** = 弱/未验证：DataCenterMap/Cloudscene/Datacenters.com/Inflect/Baxtel、市场研究、目录摘要与 SEO 页；聚合器默认 C，须运营商/PIS/政府/采购或强贸易媒体核实后才计入。
- 去重：法人规范（Posta Slovenije d.o.o.=Posita；Akademska in raziskovalna mreza Slovenije=ARNES；品牌 vs 注册实体 T-2/Telemach/A1/Telekom Slovenije/Softnet/MEGA M）；斯洛文尼亚语变音符与 ASCII 双写（Š/S、Č/C、Ž/Z）；同一园区多行为（新建/电网接入/变电站/冷却厅/发电机/UD）按地址+地块+运营商合并为同一 facility id。
- 不得计数：云服务/reseller 办公室、总部、软件公司、政府“数据门户”（非物理设施）。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=SI，divisions=市镇（212）按 12 SURS 统计区域分组）。
2. 建种子：运营商官方页（ARNES/Posita-Posta/Datacenter.si/T-2/Telekom/A1/Telemach/SoftNET/MegaTel/Arctur）+ PIS 直接词 + e-JN + DCD/Slovenia Times 首扫。
3. 每个区域执行：拉市镇名单（SURS/清单）→ PIS 搜索（数据中心词、运营商名、RTP/变电站、地址）→ 市政域名 OPN/OPPN/议会/采购→ ELES/SODO/DSO 容量与变电站上下文→ AKOS 运营商/Geoportal→ 采购确认。
4. 状态判定：PG/动土/建设采购=在建；UD/交付/开业/运营商页活跃=运营；GD/OPPN=已许可；其余为 lead-only；无证据市镇写 `no_projects: true`。
5. 输出 world 同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；容量仅在有来源时以 kW/kVA/MVA/MW 或机架数记录，标注设施类型（商业 colo/电信/公共部门/研究-HPC/企业内部）。
6. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：codex terra agent（max thinking）每 agent 分批复核斯洛文尼亚数据中心（市镇粒度，12 统计区分组）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：ARNES Maribor 的 PIS GD/PG/UD 与 2026 运营进度；部委/Posta 卢布尔雅交付设施的地址与 PIS 记录；卢布尔雅大学模块化数据中心采购进展；Telemach DC1/DC2 与 SoftNET Koper 线索的官方确认。
