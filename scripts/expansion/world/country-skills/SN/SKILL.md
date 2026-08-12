---
name: sn-datacenter-methodology
location: scripts/expansion/world/country-skills/SN/SKILL.md
description: |
  Senegal (SN) data-center enumeration methodology. Division model: 14 regions (Dakar, Diourbel, Fatick, Kaffrine, Kaolack, Kedougou, Kolda, Louga, Matam, Saint-Louis, Sedhiou, Tambacounda, Thies, Ziguinchor); commercial/carrier-neutral activity concentrated in Dakar region (Dakar dept, Rufisque/Diamniadio). No complete national planning register; enumeration joins the approval chain: commune autorisation de construire -> DEEC/DIREC EIES/installations classees -> Senelec/CRSE power -> ARTP authorization -> APIX investment -> Senegal Numerique SA state programs -> operator/Uptime pages. No hyperscaler public cloud region listed for SN (AWS Wavelength with Orange/Sonatel is an edge lead only). Key seeds: Sonatel Rufisque DC (Uptime), SENUM three state DCs (Orana, Technopole, Diamniadio), Senelec Datacenter Diamniadio (Uptime), Douanes BdM (Uptime), Millicom/Tigo Dakar DC Phase-1A (Uptime), Free Senegal Diamniadio Tier III + Avanti HYLAS4 gateway, Onix Dakar (Almadies/2Africa), PAIX Dakar (Les Mamelles, under construction, phase-1 2026), StellarIX Diamniadio, Jokko sovereign cloud. Read this before running SN exploration/audit batches. Routes to explorer-official.md (permits/DEEC/ARTP/Senelec/SENUM/APIX playbook) and explorer-industry.md (press/vendor/catalog seeding).
---

# SN · 塞内加尔数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：塞内加尔无完整国家数据中心规划登记册，枚举靠「许可链」拼接：市镇 autorisation de construire → DEEC/DIREC 环评/分类设施 → Senelec/CRSE 电力 → ARTP 电信授权 → APIX 投资 → Senegal Numerique SA 国家项目 → 运营商/Uptime 页面。按事实而非按设施分级。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：urbanisme 许可、DEEC/DIREC 环评、ARTP、Senelec/CRSE、Senegal Numerique SA/Smart Senegal、APIX/ZES、云区域核查、设施种子表、14 区策略 |
| `explorer-industry.md` | 行业/媒体/厂商管线：DCD/DCmag/Connecting Africa/Ecofin 等、运营商扫描表、云/边缘/海缆/IXP 处理、14 区四遍法、陷阱 |

## 核心结构事实（框定每次搜索）

1. 行政区划：**14 个区（region）**：Dakar、Diourbel、Fatick、Kaffrine、Kaolack、Kedougou、Kolda、Louga、Matam、Saint-Louis、Sedhiou、Tambacounda、Thies、Ziguinchor。商业与中立 colo 集中在 **Dakar 区**（Dakar 省与 Rufisque/Diamniadio）。Thies 仅为相邻机场/经济区观察名单；Kaolack 只有旧政府意向信号（planned/unverified）；其余 11 区按负面搜索跑（电信交换局、政府 ICT 机房、大学机房、能源/矿业 DR 机房）。
2. **无完整国家规划登记册**：许可证据通过市镇授权、DEEC/DIREC 环评、Senelec/CRSE、ARTP、APIX、SENUM、运营商/Uptime 页面交叉。公开网可能只暴露公告、市议会纪要、采购文件或媒体报道。
3. **Diamniadio 归属规则**：Diamniadio 是 Dakar 区 Rufisque 省的市镇。媒体常因机场走廊说「近 Dakar 或近 Thies」——除非来源点名 Thies 区地块，否则归 Dakar/Rufisque/Diamniadio。
4. **无超大规模云区域**：AWS/Azure/GCP/OCI 官方区域页未列 SN（2026-08-12）。AWS Wavelength（Orange/Sonatel）与 Oracle/Orange 规划只是边缘/服务线索；不得计为区域或设施。
5. 语言：法语优先，全拼写：`centre de donnees / datacenter / data center / centre de traitement de donnees / salle de serveurs / hebergement / colocation / cloud souverain / souverainete numerique / station d'atterrissage / cable sous-marin / raccordement / poste / MW / MVA / groupe electrogene / cuve gasoil / installations classees / Tier III / Uptime / Diamniadio / Rufisque / Almadies / Les Mamelles`。
6. 状态动词须逐字捕获：`announces / plans / MoU / will build / purchased land` = planned/早期建设（B/C）；`breaks ground / construction started / extension / phase` = 在建（B）；`inaugurated / operational / go-live / available` + 当前服务页 = 运营信号（与运营商/Uptime 交叉后 A）；`Tier III / certified` = 营销文字保持 A 仅限营销，认证须 Uptime 确认。
7. Uptime 记录权威于认证/地点名称但不证明商业模式（海关或电力 DC 可能仅内部使用）；Dakar 区多设施并存，不得因同说「Diamniadio/近 Dakar」合并。

## 查询模式（复制粘贴模板见 explorer-official.md §1-4 与 explorer-industry.md §1-4）

- 许可/规划：`site:urbanisme.gouv.sn ("centre de donnees" OR datacenter OR "centre de traitement")`、`site:urbanisme.gouv.sn "autorisation de construire" "{operator}"`、`"{commune}" "autorisation de construire" (datacenter OR "centre de donnees")`、`"arrete" "{commune}" (datacenter OR "centre de donnees")`。
- 环境：`site:denv.gouv.sn ("centre de donnees" OR datacenter)`、`site:denv.gouv.sn Diamniadio EIES`、`"{project}" "etude d'impact environnemental" Senegal`、`"{project}" "groupe electrogene" "installations classees" Senegal`。
- 监管：`site:artp.sn ("centre de donnees" OR datacenter)`、`site:artp.sn "{operator}" (licence OR agrement OR autorisation OR sanction)`、`site:artp.sn "reseaux prives independants" "{operator}"`、`"Avanti" "Diamniadio" "autorisation" Senegal`。
- 能源：`site:senelec.sn (datacenter OR "centre de donnees")`、`site:senelec.sn "{operator}" (raccordement OR poste OR MVA OR MW)`、`"{operator}" Senelec (MW OR MVA OR raccordement) Senegal`。
- 国家项目：`site:senegalnumeriquesa.sn (datacenter OR "centre de donnees" OR cloud OR Diamniadio OR Orana OR Technopole)`、`"SENUM" (Orana OR Technopole OR Diamniadio) datacenter`、`"Smart Senegal" (datacenter OR "cloud national")`。
- 投资：`site:investinsenegal.sn (datacenter OR "centre de donnees")`、`"APIX" (datacenter OR "centre de donnees") Senegal`、`"ZES Diamniadio" (datacenter OR cloud)`。
- 行业媒体（B）：`site:datacenterdynamics.com/en/news/ Senegal ("data center" OR "data centre")`、`site:dcmag.fr Senegal (datacenter OR Dakar OR Diamniadio)`、`site:connectingafrica.com Senegal (datacenter OR Avanti OR PAIX OR Sonatel)`、`site:agenceecofin.com Senegal (datacenter OR Sonatel OR ARTP)`、`site:cio-mag.com Senegal (datacenter OR Diamniadio)`、`site:financialafrik.com Senegal datacenter Diamniadio`、`site:dakaractu.com "Datacenter national" Diamniadio`。
- 目录/认证（C/A 核验）：`site:datacentermap.com/senegal`、`site:baxtel.com Senegal`、`site:uptimeinstitute.com/uptime-institute-awards Senegal "{region}"`、`site:uptimeinstitute.com/uptime-institute-awards "{operator}" Senegal`。

## 官方/监管管线要点（详见 explorer-official.md）

- urbanisme（https://www.urbanisme.gouv.sn，授权申请页 A 级流程）：请求递交属地市镇市长，附件含产权证明、信息表、描述/造价估算、建筑图、污水/化粪池图、地籍摘录、城建税、印花税。TeleDAC 为无纸化途径，旧端点 `teledac.sec.gouv.sn` 不可靠；不当作可检索许可库。提取：市镇、省、地块/产权号、申请人、用途描述、毛面积、高度/楼层、发电机/燃油/存储备注、授权日期/文号。
- DEEC/DIREC（https://www.denv.gouv.sn A 级）：DEIE（环评研究处）与 DIC（分类设施处）；环评流程页 https://www.denv.gouv.sn/avis-de-projet/ 与 /division-des-etudes-dimpact-environnemental-deie/；法规文号 Arrete ministeriel n 9471/9472 MJEHP-DEEC。数据中心经建设 EIES、发电机/油箱 ICPE、变电站、冷却/水系统及大型园区 EIES 浮出。提取：项目名、发起人、市镇/省、地块或坐标、电力需求、发电机规模、燃油储量、冷却/水、污水、噪声/空气影响、公众咨询、决策/文号。
- ARTP（https://artp.sn A 级）：非设施登记册；核实电信/运营商地位、ISP agrement、私有独立网络授权、卫星网关授权、制裁、设备型式核准。已验证线索：Avanti/Free——AXIAN 宣布 Free 在其 Diamniadio Tier III 数据中心建设并运营 Avanti 网关（https://www.axian-telecom.com/2022/05/23/...）；Avanti 宣布 HYLAS 4 网关获授权（https://www.avanti.space/news/...）。未取回 ARTP 决定前不得称制裁。
- Senelec/CRSE（https://www.senelec.sn / https://www.crse.sn A 级）：搜索 `raccordement / poste / MVA / MW / HT / MT / alimentation electrique`、招标与变电站工程；捕获电力数字是市电进口、变压器容量、关键功率还是 IT 负荷。Uptime 有独立 **Senelec Datacenter Diamniadio** 记录（https://uptimeinstitute.com/uptime-institute-awards/datacenter/senelec-datacenter-diamniadio-/1245），除非佐证否则不与 SENUM 国家 DC 合并。
- Senegal Numerique SA（https://www.senegalnumeriquesa.sn A 级）：当前页称 SENUM 继承 ADIE，运营公共数字基础设施、>5,000 km 光纤、**三个在用数据中心：Orana、Technopole、Diamniadio**（https://senegalnumeriquesa.sn/fr/senegal-numerique-moteur-de-la-transformation-digitale-de-letat）。2021-06-22 Diamniadio 国家 DC 启用与 500-1,000 m2 技术/托管面积、1.4 MW 等容量数字用 RFI/CIO Mag/Financial Afrik/DCD 作 B 级，容量字段按来源记录。Orana 与 Technopole 需查明是完整托管 DC、政府服务器机房、灾备站点还是园区机房。CDP（https://www.cdp.sn）为合规语境，非设施登记册。
- APIX（https://investinsenegal.sn A 级）：数字经济 PDF 描述一个数据中心项目（2022 年 7 月开工、预计 2024 年 Q2 运营、约 1,200 万美元），作需识别运营商与当前状态的线索（A/B）；投资者指南 2026-01 版提数据中心/AI/云与 Diamniadio Tier III 语境。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场形态：已核实市场 Dakar 集中；实践发现三角 = 运营商/Uptime 页（具名设施）+ 媒体/厂商页（时间与容量）+ 官方文件（许可/环境/电力/监管确认）。
- 设施线索表：**Sonatel Rufisque DC**（Orange Business Senegal 页 https://www.orangebusiness.sn/digitaliser/datacenter + Uptime https://uptimeinstitute.com/.../data-center-sonatel-rufisque/984，A）；**Senegal Numerique Diamniadio**（A SENUM 名称 + B 启用/容量媒体）；**SENUM Orana / Technopole**（A 国家运营商 DC 名称线索，待查明功能与地点）；**Senelec Datacenter Diamniadio**（A Uptime，公用事业/内部设施）；**Douanes BdM Datacenter**（A Uptime，Dakar，政府内部）；**Millicom/Tigo/SenConnect / Yas 旧线索**（A Uptime「Tigo Senegal Dakar DC Phase-1A」+ B DCD 2017 Diamniadio/SenConnect 叙述；Yas 品牌仅目录为 C）；**Free Senegal Diamniadio**（A/B AXIAN 集团稿：Tier III 设施 + 托管 Avanti 网关；核验 Uptime 与现法律实体）；**Avanti HYLAS 4 网关**（租户/网关证据，非独立 DC）；**Onix Data Centres Senegal**（A 运营商声明 Almadies/2Africa 登陆站 Tier 3，2023 Q4 完成目标为旧稿，运营前重查当前状态）；**PAIX Data Centres Dakar**（B/A-：Les Mamelles，约 918-900 m2 可用/colo 空间、1.2 MW IT 负荷/关键功率、330 机柜，一期计划 2026 运营——PAIX 发布 go-live 前保持 under construction）；**StellarIX Senegal**（A 服务/地点声明：Diamniadio colo/云、宣称 Tier III Design & Facility/PCI-DSS/ISO 27001，认证需 Uptime 查证）；**Jokko/Dariss Consulting**（A 提供商声明：Dakar Tier III+ 数据中心托管的塞内加尔主权云；主机设施与认证源待识别，Tier III+ 为 C/B）；**MainOne/Equinix**（B 线索：Dakar 海缆/PoP/办公室，无确认 Equinix colo）；**WIOCC/OADC、Africa Data Centres**（负面观察名单）；**APIX 未具名项目**（A/B 线索）；**Kaolack 计划 DC**（C 旧意向）。
- 云/边缘/海缆处理：AWS Wavelength 与 Orange/Sonatel 是边缘服务线索；Oracle/Orange 2021 西非区域规划不是运营证据；海缆登陆站（ACE、MainOne、SAT-3、SHARE、2Africa）是互联线索，仅当含 colo/DC 设施才计 DC（如 Onix 于 Almadies 2Africa）；SENIX/IXP 与 CDN 节点本身不是 DC。

## 来源分级

- **A** = 特定数据点的一手/官方证据：市镇或 urbanisme 许可流程、DEEC/DIREC 环境记录、ARTP 授权/许可/制裁、Senelec/CRSE 官方材料、Senegal Numerique SA 页、APIX/投资 PDF、Uptime 奖记录、官方运营商或云厂商页。
- **B** = 强二手证据：DCD、DCmag、Agence Ecofin、CIO Mag、RFI、Le Soleil/主流本地媒体、Africa50/项目融资方、经可靠通讯社转载的运营商稿。
- **C** = 弱线索：DataCenterMap/Baxtel/Neocloud/市场报告片段、社交、旧 MoU、无署名博客、SEO 页、容量/地点声明无独立支撑。
- 按事实分级而非按设施分级；聚合器只能开线索，不能把设施升到 C/B- 以上。planned/under construction/operational 跟随来源动词。

## 使用流程（探索/复核批次）

1. 读本 SKILL.md 与两份 explorer 报告，确定目标区与候选项。
2. 对每个候选跑四遍：① 媒体/厂商遍（区+城镇+法/英 DC 词）；② 运营商遍（Sonatel、Free、Expresso、SENUM/ADIE、Senelec、Onix、PAIX、StellarIX、Jokko、Yas/Tigo/Millicom、Avanti、MainOne、WIOCC/OADC、ADC）；③ 认证/目录遍（Uptime、DataCenterMap、Baxtel、Neocloud、datacenters.com、OCOLO）；④ 官方 pivot 遍（urbanisme、DEEC/DIREC、Senelec/CRSE、ARTP、APIX、SENUM）。
3. 14 区全部跑（区域查询块 + 精确复制种子见两份 explorer），低产区保留负面记录日志。
4. 按去重规则：每运营商/场地一个物理设施；Diamniadio 多个设施线索（SENUM、Senelec、Free、StellarIX、Tigo/Yas、Avanti）不得合并；Uptime 不证明商业模式。
5. 状态按动词定级；PAIX 一期 2026 计划运营不等于已运营，须找 2026 go-live/当前服务页。
6. 写 world schema 输出（含 region/department/commune、authorization/environment/power/regulator 证据 URL、capacity_type、certification_type、source_grade、status）。遵守 NO-DELETION；不改写 explorer-*.md。

## 待办（2026-08-12 03:07Z）

- [x] 合并两份探索报告为 SKILL.md + ANATOMY.md。
- [ ] SENUM Orana/Technopole：查明功能（托管 DC vs 服务器机房 vs 灾备）、地点与容量。
- [ ] PAIX Dakar：找 2026 go-live/当前服务页、许可、EIES、Senelec 连接、Les Mamelles 精确地块。
- [ ] Free Senegal Diamniadio：Uptime 记录核验（现法律实体）与精确地址。
- [ ] 待核实：APIX 未具名 DC 项目（运营商/场地/当前状态）；Kaolack 计划 DC 的最新官方证据。
