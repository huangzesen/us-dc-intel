---
name: bf-datacenter-methodology
location: scripts/expansion/world/country-skills/BF/SKILL.md
description: |
  Burkina Faso (BF) data-center enumeration methodology. Division model: legacy 13 regions (Boucle du Mouhoun; Cascades; Centre; Centre-Est; Centre-Nord; Centre-Ouest; Centre-Sud; Est; Hauts-Bassins; Nord; Plateau-Central; Sahel; Sud-Ouest) — the Presidency announced 2025-07-02 reorganization to 17 regions/47 provinces with endogenous names (Kadiogo=Centre, Guiriko=Hauts-Bassins, Bankui/Sourou=Boucle du Mouhoun, Goulmou/Sirba/Tapoa=Est, Liptako/Soum=Sahel); use both old and new names. No public national datacenter registry; enumeration joins MTDPCE/ANPTIC government programs, ARCEP licences, ANEVE/SINADEVE environmental records, ARSE/SONABEL power, ARCOP procurement, BFIX/PeeringDB interconnection, and operator pages. Market is small and Ouagadougou-centric. No AWS/Azure/GCP/OCI public cloud region listed. Key seeds: two government modular datacenters (inaugurated 2026-01-23; 3 PB storage/105.6 TB RAM/28,800 CPU cores/7,000+ VMs, ~15.2-16 bn FCFA), ANPTIC/legacy G-Cloud/education DC, Virtix Data Center (Palais des Sports, Ouaga 2000 — best commercial colo seed), IKA Cloud (Avenue de la Dignité, Cissin), Alink Telecom, IPSyS TELECOM (Avenue Kwame Nkrumah), Orange BF telco-core DC + solar, ONATEL/Moov Africa, Telecel Faso, BFIX legacy facilities (Immeuble du Faso, Ministère de l'agriculture), NOC/supervision center (target Oct 2026), Essor Services+Kaia waste-to-energy 12 MW DC (C speculative). Read this before running BF exploration/audit batches. Routes to explorer-official.md (ministry/ARCEP/ANEVE/ARSE/SONABEL/ARCOP playbook) and explorer-industry.md (trade-press/operator/directory playbook).
---

# BF · 布基纳法索数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：布基纳法索无公共国家数据中心登记册，枚举靠拼接「MTDPCE/ANPTIC 政府计划 + ARCEP 牌照 + ANEVE/SINADEVE 环境记录 + ARSE/SONABEL 电力 + ARCOP 采购 + BFIX/PeeringDB 互联 + 运营商页」。市场小而 Ouagadougou 中心；内陆国无本国海缆登陆，国际路由靠经科特迪瓦/加纳/多哥/贝宁的陆缆。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：部委/ANPTIC/总统府-SIG、ARCEP 牌照与运营商名册、ANEVE/SINADEVE、ARSE/SONABEL、ARCOP/采购、BFIX/PeeringDB、云负面核查、官方核实种子表、13 区策略与后 2025 别名、最低记录标准 |
| `explorer-industry.md` | 行业/媒体/厂商管线：市场现实、媒体源分诊、运营商/项目种子、逐区行业策略、云/CDN/边缘处理、证据升级规则、陷阱、发现顺序 |

## 核心结构事实（框定每次搜索）

1. 行政划分：保留请求的**遗留 13 区模型**：Boucle du Mouhoun；Cascades；Centre；Centre-Est；Centre-Nord；Centre-Ouest；Centre-Sud；Est；Hauts-Bassins；Nord；Plateau-Central；Sahel；Sud-Ouest。**边界注意**：总统府 2025-07-02 宣布自 13 区/45 省重组为 **17 区/47 省**、内生名称、六个月过渡（https://www.presidencedufaso.bf/conseil-des-ministres-du-2-juillet-2025/）。新旧名称都搜：Kadiogo=Centre、Guiriko=Hauts-Bassins、Bankui/Sourou=原 Boucle du Mouhoun、Goulmou/Sirba/Tapoa=原 Est、Liptako/Soum=原 Sahel。
2. **无公共国家数据中心登记册**。官方骨架：数字转型部（MTDPCE/MDENP 遗留域 https://www.mdenp.gov.bf/）、ANPTIC（https://anptic.gov.bf/，实施运营国家 ICT 基建）、总统府/SIG、ARCEP（https://www.arcep.bf/，牌照与运营商名册）、ANEVE/SINADEVE（https://sinadeve.envieau.gov.bf/，环评/合规）、ARSE（https://www.arse.bf/，电力监管）、SONABEL（国有电力，独立域 curl 超时需人工核验）、ARCOP（https://www.arcop.bf/，采购）、BFIX（https://www.bfix.bf/，IXP）。
3. **无超大规模云区域**（A 级负面）：AWS/Azure/GCP/Oracle OCI 官方区域页未列 BF。客户/伙伴/CDN 缓存/边缘 PoP ≠ DC 园区；Cloudflare 与 Meta 作为 BFIX 对等方只证明在 BFIX 互联，非其独立 DC；从法国/达喀尔/阿比让等地向 BF 营销的境外托管除非点名 BF 设施否则不是 BF 设施。
4. 市场现实：市场小、Ouagadougou 中心；核心 2026 需求信号 = 国家数据主权计划（两个政府模块化数据中心 2026-01-23 启用、国家数字基建监督/NOC 楼目标 2026 年 10 月、政府云持续扩展）。内陆国无海缆登陆——「低延迟超大规模」声明除非有 BFIX/PeeringDB、运营商骨干或实测延迟支撑否则存疑。电力是主要约束——任何行业声明应与 SONABEL/ARSE、发电机、UPS、太阳能/PPA 或 EIA 证据对账。
5. 语言：法语优先，英文第二；保留带引号法语词：`datacenter / data center / centre de données / cloud gouvernemental / souveraineté numérique / hébergement / colocation / centre de supervision / groupe électrogène / permis de construire / étude d'impact / avis environnemental / poste de transformation / kVA / MVA / NOC / salle serveur / point de présence`。
6. 不得从网吧、普通网页托管经销商、境外托管、大学实验室、市镇 IT 办公室、「数字枢纽」、塔址、光纤路由、NOC/控制室创建 DC 记录，除非来源证明托管/colo/云/算力设施功能。

## 查询模式（复制粘贴模板见 explorer-official.md §2-5 与 explorer-industry.md §2-4）

- 官方站点：`site:mdenp.gov.bf ("datacenter" OR "centre de données" OR "cloud gouvernemental" OR NOC)`、`site:anptic.gov.bf ("datacenter" OR "centre de données" OR hébergement)`、`site:presidencedufaso.bf OR site:sig.gov.bf ("datacenter" OR "infrastructures numériques" OR NOC)`、`site:arcep.bf ("liste des opérateurs" OR licence OR "licence technologiquement neutre")`、`site:sinadeve.envieau.gov.bf ("datacenter" OR "centre de supervision" OR "groupe électrogène")`、`site:arse.bf (tarif OR SONABEL OR "grand client")`、`site:sonabel.bf ("datacenter" OR "poste de transformation" OR MVA)`、`site:arcop.bf ("datacenter" OR "cloud gouvernemental" OR NOC)`。
- 项目/运营商：`"{operator}" Burkina ("datacenter" OR colocation OR hébergement)`、`"{operator}" Burkina (ARCEP OR licence OR ANEVE OR SINADEVE OR SONABEL OR "permis de construire")`、`"{operator}" (BFIX OR PeeringDB OR "Ouaga 2000" OR "Avenue de la Dignité" OR "Avenue Kwame Nkrumah")`。
- 贸易媒体（B）：`site:datacenterdynamics.com/en/news/ "Burkina Faso" ("data center" OR datacenter)`、`site:ecofinagency.com "Burkina Faso" ("data center" OR "centre de supervision" OR towers)`、`site:developingtelecoms.com "Burkina Faso" ("data centre" OR "waste-to-energy")`、`site:lefaso.net Burkina (datacenter OR "cloud gouvernemental")`、`site:aib.media Burkina (datacenter OR "infrastructures numériques")`、`site:burkina24.com Burkina (datacenter OR "découpage administratif")`、`site:wakatsera.com Burkina (datacenter OR "cloud gouvernemental")`。
- 目录/互联（C/A-B）：`site:datacentermap.com/burkina-faso/`、`site:datacenterplatform.com/countries/burkina-faso/`、`site:inflect.com/datacenters/emea/burkina-faso`、`site:peeringdb.com/ix/2729`（BFIX Ouagadougou）、`site:peeringdb.com/org/14212`。
- 13 区快速扫描 + 后 2025 别名：`"{legacy region}" Burkina ("datacenter" OR "centre de données" OR colocation)`、`"{capital}" Burkina ("salle serveur" OR hébergement)`、`Kadiogo Ouagadougou Burkina datacenter`、`Guiriko Bobo-Dioulasso Burkina datacenter`、`Bankui Dedougou Burkina datacenter`、`Goulmou "Fada N'Gourma" Burkina datacenter`、`Liptako Dori Burkina datacenter`。
- 云负面：`site:aws.amazon.com/about-aws/global-infrastructure Burkina Faso`、`site:learn.microsoft.com/en-us/azure/reliability/regions-list Burkina Faso`、`site:cloud.google.com/about/locations Burkina Faso`、`site:docs.oracle.com/iaas/Content/General/Concepts/regions.htm Burkina Faso`。

## 官方/监管管线要点（详见 explorer-official.md）

- MTDPCE（A 部委页；仅 Facebook 可用则 B）：政府云、国家 DC、NOC、「零白色地带」、数字转型计划。
- ANPTIC（https://anptic.gov.bf/ A 实时页；缓存片段 B/C）：实施运营国家 ICT 基建；页面含行政数据中心与 2026 模块化 DC 材料，slug 存活检查偶 404——用站点搜索模板。
- ARCEP（A 牌照/名册事实；本身不证明 DC）：Decret 2010-245/PRES/PM/MPTIC/MEF 规定牌照程序；用 ARCEP 构建运营商全集（ONATEL、Orange Burkina Faso、Telecel Faso、PAV-Burkina 等），再把每个持牌运营商 pivot 到设施/托管/colo/BFIX 搜索。
- ANEVE/SINADEVE（A 官方通知/EIA 时）：新建、重发电机场地、光纤走廊、能源厂、垃圾发电项目；记录 EIA 事实：发起人、地点、备用发电、燃油储存、冷却/水、地块、建设阶段。
- 建筑许可在市镇级，通常在线不可搜：Ouagadougou 搜「mairie de Ouagadougou」与区/部门名，高价值记录联系市镇确认。
- 电力 sanity check 强制：提取 kVA/MVA/MW、电压、变电站、发电机自主时间、UPS 拓扑、燃油储存、太阳能/PPA 证据；电力字段独立于设施字段分级。
- 最低记录标准：规范名与别名；业主/运营商与法人；遗留 13 区归属 + 后 2025 别名；地点/区/街道地标/坐标；状态（announced/procurement/permitted/under construction/inaugurated/operational/inactive）；功能（commercial colo/government cloud/education-government/telco core/IXP/NOC/server room/speculative）；容量带精确单位与字段级分级（racks/sqm/MW-kVA-MVA/storage/CPU cores/RAM/VMs）；证据 URL 逐字段分级；与 ANPTIC/G-Cloud、MDENP 遗留、BFIX 遗留、运营商办公室、电信交换局的去重说明。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 种子表：**政府云模块化数据中心 ×2**（Ouagadougou；MTDPCE 建设进度页 A 项目存在；2026-01-23 启用；DCD/Connecting Africa B 容量/启用细节——3 PB 存储、105.6 TB RAM、28,800 CPU 核、7,000+ VMs、约 15.2-16 bn FCFA；官方页文字先于写 A 容量；两个物理站点分开表示，地址未公开）；**ANPTIC/遗留 G-Cloud/教育 DC**（`site:anptic.gov.bf "DATACENTER DE L'EDUCATION"` B 直到文章可开；重要去重区——仅当场地/功能/状态不同才分开）；**Virtix Data Center / Virtual Technologies and Solutions SA**（Palais des Sports, Ouaga 2000, Ouagadougou；官方站 https://virtix.bf/ A 地点/营销服务；PeeringDB B 互联；目录容量 C——「Tier 3/hyperscale」为自称除非 Uptime 记录；目录 1,200 m2/3 MW 需独立确认；最佳商业 colo 种子）；**IKA Cloud / IKA Solution**（Avenue de la Dignité, Cissin/Secteur 26, Ouagadougou；定价/服务页 A 地址与广告服务；「premier datacenter」声明为营销（Virtix 更早）；核实物理 DC vs 经销商/平台）；**Alink Telecom**（目录 Ouagadougou；域名 HTTP-only B/C；ARCEP/运营商页/BFIX/许可/客户证据前设施状态不超 C）；**IPSyS TELECOM**（Avenue Kwame Nkrumah；官方站 https://ipsys-bf.com/ A 若展示设施服务；核实地址是设施还是办公室）；**Orange Burkina Faso**（A 牌照；B DCD 太阳能/DC 存在；电信核心 DC 线索，无产品/场地页不计公共 colo）；**ONATEL / Moov Africa BF**（A 牌照；B/C DC 声明；在位网络核心，不把交换站点乘成 DC）；**Telecel Faso**（A 牌照；C 推断 DC；点名核心网/MSC/交换/托管前不计数）；**BFIX 遗留设施**（Immeuble du Faso、Ministère de l'agriculture、Virtix——B 网络节点在场，C 商业 DC 解读；核实业主/状态）；**NOC/数字基建监督中心**（Ecofin B：540 万美元；Ouagadougou；NOC/运营楼非默认 DC，作为国家 DC 运营的 join 目标与许可/采购记录）；**Essor Services + Kaia Energy 垃圾发电 DC**（C：公告 12 MW 垃圾发电 + DC，目标 2025 年 11 月——无官方 EIA/许可/建设证据，保持投机线索）。
- 媒体源（B）：DCD、Ecofin Agency、Developing Telecoms、leFaso.net、AIB、Sidwaya、Burkina24、Wakat Sera、TechAfrica News、WeAreTech、Telecom Review Africa。目录（C）：DataCenterPlatform、DataCenterMap、Inflect、Baxtel、DCJournal。PeeringDB/PCH（B/A 互联事实，非商业设施证明）。
- 证据升级：公告→C/B（无地址/许可）；施工→B/A（奠基、采购授标、ANEVE 通知、市镇许可、承包商通知、官方渠道带日期的施工照片）；运营→A/B（官方启用、带地址的运营商服务页、客户就绪 colo 条款、BFIX/PeeringDB 设施连接、公用事业通电、审计文件）；容量字段单独分级；计数前去重（Cloud Gouvernemental/ANPTIC/MDENP/「mini datacenters」/教育 DC/NOC 为相邻政府基建但不自动同一设施；BFIX/Virtix/遗留 Immeuble du Faso/Ministère de l'agriculture 可重叠）。

## 来源分级

- **A**：一手——部委、总统府/SIG、ANPTIC、ARCEP、ANEVE/SINADEVE、市镇许可、ARMP/DGMP 采购、ARSE/SONABEL、官方运营商设施页、官方云区域页、PeeringDB/PCH 互联记录、BRVM/发行人文件。
- **B**：强二手——DCD、Developing Telecoms、Ecofin Agency、AIB、Sidwaya、leFaso.net、Burkina24、Wakat Sera、可信厂商案例、行业协会、转述具名官方事件的本地媒体。
- **C**：弱线索——聚合器目录、市场报告片段、社交、旧 MoU、无场地/电力/许可证据的启动声明、「服务器机房」提及而无托管/colo/云功能。

## 使用流程（探索/复核批次）

1. 从 ANPTIC、Virtix、IKA、BFIX/PeeringDB、Orange、ONATEL/Moov、Telecel、Alink、IPSyS 构建 Ouagadougou 种子表。
2. 每个种子跑 运营商 + 地址 + `ARCEP`/`ANEVE`/`SONABEL`/`BFIX`/`PeeringDB`/`permis de construire`/`rapport annuel`。
3. 扫 DCD、Ecofin、Developing Telecoms、leFaso.net、AIB、Sidwaya、Burkina24、Wakat Sera、WeAreTech 的种子名与法语 DC 词汇。
4. 跑 13 区快速查询，再跑后 2025 别名查询。
5. 对照官方 explorer 源图对账每个候选，字段级分级后创建/更新设施记录。
6. 遵守 NO-DELETION；不改写 explorer-*.md。

## 待办（2026-08-12 03:26Z）

- [x] 合并两份探索报告为 SKILL.md + ANATOMY.md。
- [ ] 政府模块化 DC：ANPTIC 实时文章打开，确认两个物理站点地址与容量官方文字。
- [ ] Virtix：Uptime 记录核验；目录 1,200 m2/3 MW 独立确认。
- [ ] NOC：官方授标/许可记录；Essor/Kaia 垃圾发电 DC：EIA/许可/建设证据。
- [ ] 待核实：IKA 物理 DC vs 经销商；IPSyS 地址设施 vs 办公室；Orange/ONATEL/Telecel 点名核心 DC 场地。
