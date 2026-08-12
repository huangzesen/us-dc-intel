---
name: bi-datacenter-methodology
location: scripts/expansion/world/country-skills/BI/SKILL.md
description: |
  Burundi (BI) parent-level methodology for data-center enumeration at province granularity. CRITICAL
  administrative correction: Burundi is NOT a 17-province country; it had 18 provinces from the 2015
  creation of Rumonge until the 2025 reform, and the current model is 5 provinces (Buhumuza, Bujumbura,
  Burunga, Butanyerera, Gitega). Use the 5 current provinces for normalized records and the legacy 18 names
  for search recall. Burundi has no public national datacenter registry and no reliable online
  construction-permit search; enumeration joins ARCT licensing/observatories, SETIC/PAFEN/PDDSP/eNama
  government-digital documents, operator pages/tenders (BBS, ONATEL, Lumitel, Econet Leo, CNI/NIC.BI),
  energy/environment records (REGIDESO/AREEN/OBPE), IXP/interconnection (BDIXP), donor documents (World
  Bank PAFEN USD 92M), and local press. Market is small and telco/government/server-room driven; Bujumbura
  is the only credible commercial cluster. No hyperscaler region. Routes to explorer-official.md
  (regulator/government/energy pipeline) and explorer-industry.md (press/operator/interconnection pipeline).
---

# BI · 布隆迪数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：布隆迪没有公共的国家数据中心登记册，也没有可靠的在线施工许可检索；枚举必须拼接 ARCT 许可/市场观察、SETIC/PAFEN/PDDSP/eNama 政府数字文件、运营商页面与招标（BBS、ONATEL、Lumitel、Econet Leo、CNI/NIC.BI）、能源/环境记录（REGIDESO/AREEN/OBPE）、IXP/互联（BDIXP）、捐助者文件（世行 PAFEN 9,200 万美元）与本地媒体。**行政更正：布隆迪不是 17 省国家**——2015 年设立 Rumonge 后有 18 省，2025 年改革后现行 5 省；归一化记录用 5 省，检索回调用 18 省旧名。市场小且电信/政府/服务器机房驱动；Bujumbura 是唯一可信商业集群。无超大规模区域。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供布隆迪探索与复核批次使用。

## 入口

| 文档 | 用途 |
|---|---|
| `explorer-official.md` | 官方/监管管线：ARCT、SETIC/PAFEN/PDDSP/eNama、BBS、运营商、OBPE/REGIDESO/AREEN、云区域阴性对照、种子清单、省工作流 |
| `explorer-industry.md` | 行业管线：本地媒体（Iwacu/Burundi Eco/ABP）、非洲/国际行业媒体、运营商/托管商/厂商、IXP 与聚合目录、法/英/基隆迪语模板、分级规则 |

## 核心结构事实（框定每次搜索）

1. **省模型（最重要更正）**：2026 年布隆迪**不是** 17 省国家；2015 年创建 Rumonge 后为 18 省，2025 年改革后现行 **5 省**：Buhumuza（Cankuzo 首府）、Bujumbura、Burunga（Makamba）、Butanyerera（Ngozi）、Gitega。归一化用 5 省，检索必须包含全部 18 个旧省名（Bubanza, Bujumbura Mairie, Bujumbura Rural, Bururi, Cankuzo, Cibitoke, Gitega, Karuzi, Kayanza, Kirundo, Makamba, Muramvya, Muyinga, Mwaro, Ngozi, Rumonge, Rutana, Ruyigi）。
2. **无登记册**：没有公共国家数据中心登记册或可靠在线施工许可检索；枚举 = 电信许可 + 政府数字项目文件 + 运营商页面/招标 + 能源/环境证据 + 采购公告 + IXP/互联 + 本地媒体。
3. **市场结构**：小且以电信/政府/服务器机房为主，非超大规模 colo；保守计数：SETIC 政府托管、BBS 托管/服务器托管、Lumitel/ONATEL/Econet 核心或云服务、CNI/NIC.BI 注册局基础设施、PAFEN 资助的大学计算中心、BDIXP、布琼布拉小托管商。
4. **SETIC 政府数据中心**：Iwacu 2021-05 报道 SETIC 管理数据中心并托管国家机构站点/数据（B，需 SETIC 主源配对升 A）；SETIC/PAFEN 中期页点名通过 Data Center 提供国家托管并现代化政府通信网络。
5. **PAFEN（世行 IDA 9,200 万美元）**：数字基础项目；招标含 **5 个大学计算中心（CIU）**——布隆迪大学、ENS、国立公共卫生研究所、Gitega 理工大学、Espoir d'Afrique 大学（A 招标存在，机构计算室非商业 colo）；BERNET 教育与研究网络安全/管理咨询；2026-03-23 财政部中期评估 61% 预算执行。
6. **CDIN（Centre de Donnees Integre National）**：PDDSP 2023-2033 衍生规划项，保持 `planned` 直到官方招标、授予、EIES、施工或启用具名站点。
7. **BBS（Burundi Backbone System）**：官方页列 `Hebergement Web`、`Hebergement Serveur` 与定价（A 营销服务存在）；具体 colo 设施（站点/机房/机架/地址/电力/SLA）为 B/C；国家光纤骨干为 B 背景（Agence Ecofin：PTA Bank 1,150 万美元贷款）。
8. **运营商**：ONATEL（国有在位者，ARCT 确认 2025 移动运营商）、Lumitel/Viettel Burundi（官方页含 Cloud server 标签，Bujumbura 地址）、Econet Leo（ARCT 确认；LinkedIn Data Centre Engineer 职位为 C 线索）；电信许可/市场份额 ≠ 可计数 DC。
9. **BDIXP/IXP**：2014-03-21 在 Bujumbura 启动（Internet Society/非盟公告 B/A）；PeeringDB ix/2552（26G 元数据）；互联基础设施，本身不是 DC。
10. **云区域为阴性证据**：AWS/Azure/GCP/OCI 官方列表无非州以外布隆迪区域（多在南非）；云服务可用性不得转为布隆迪设施记录。

## 查询模式（复制粘贴模板见 explorer-official.md §2/§3/§5、explorer-industry.md §1/§3/§5/§6）

```text
site:arct.gov.bi "centre de donnees" OR "data center" OR hebergement
site:arct.gov.bi observatoire ECONET LEO LUMITEL ONATEL
site:setic.gov.bi "data center" OR "centre de donnees" OR hebergement
site:setic.gov.bi PAFEN OR PDDSP OR BERNET
site:pafen.gov.bi "centre informatique universitaire" OR CIU OR BERNET
site:pafen.gov.bi hebergement OR "data center" OR serveurs
site:finances.gov.bi PAFEN OR numerique
site:primature.gov.bi PDDSP
site:enama.gov.bi PDDSP OR "centre de donnees" OR CDIN
"Centre de Donnees Integre National" Burundi
site:bbs.bi hebergement OR serveur OR data OR colocation
site:lumitel.bi "Cloud server" OR cloud OR entreprise OR data
site:onatel.bi hebergement OR cloud OR data OR "appel d'offres"
site:cni.bi hebergement OR serveur OR data
site:nic.bi serveur OR infrastructure OR hebergement
site:obpe.bi "etude d'impact" fibre OR telecom OR "centre de donnees"
site:regideso.bi "appel d'offres" transformateur OR poste OR Bujumbura
"BDIXP" OR "Burundi Internet Exchange" Bujumbura
site:iwacu-burundi.org SETIC OR "centre de donnees" OR hebergement
site:burundi-eco.com ONATEL OR PAFEN OR "fibre optique"
site:abp.bi PAFEN OR "centre de donnees" OR numerique
"Bujumbura" Burundi ("centre de donnees" OR "data center" OR hebergement OR colocation OR cloud)
"Gitega" Burundi ("centre de donnees" OR PAFEN OR CIU OR BERNET OR CDIN)
"{legacy_province}" Burundi "data center" OR "centre de donnees" OR fibre
"{current_province}" OR {legacy_names} Burundi (fibre OR "data center" OR "centre de donnees")
"Burundi" "cloud region" OR "public cloud" AWS OR Azure OR Google OR Oracle
```

## 官方/监管管线要点（详见 explorer-official.md）

- **ARCT**（arct.gov.bi）：运营商/许可普查与电信市场来源（Q2 2025 观察确认 ECONET LEO、LUMITEL、ONATEL）；2025-11-10 起运行的电子通信设备进出口/放行授权数字平台；许可 ≠ 设施。
- **政府数字部委/SETIC/PAFEN/PDDSP**：MinCom、财政部（预算与数字经济）、SETIC（ICT 促进与政府托管）、PAFEN（世行资助）、eNama、Primature PDDSP 2023-2033（官方公共服务数字化战略，是项目规划来源，非运营站点证据）。
- **BBS**：托管/服务器托管服务 A；骨干/PoP 背景 B；colocation 设施细节 B/C。
- **CNI/NIC.BI**：.bi 注册局与遗留计算机构；注册/托管基础设施可能位于 Bujumbura，但需主源页面具名服务器/托管基础设施。
- **环境/能源**：OBPE EIES/NIE 记录（本轮回合未验证到公共 DC 专属 EIES）；REGIDESO 大客户连接/变压器/变电站招标；AREEN 水电监管背景；世行能源项目（Jiji/Mulembwe、Rusumo）——电力约束是重大筛选条件。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **本地媒体**：Iwacu（最高价值独立来源，2021 SETIC 文章 B）、Burundi Eco（B）、ABP（官方通讯社，PAFEN 启动报道确认世行 9,200 万美元/6 年，B）、Le Renouveau（B/C）、SOS Medias（B/C）、Itara（C/B）、Burundi AG News（C/B）。
- **行业媒体**：Agence Ecofin（BBS 1,150 万美元贷款，B）、WeAreTech Africa（PAFEN 中期审查，B）、CIO Mag（ARCT/Starlink 统计，B）、TechAfricaNews（PAFEN/Lumitel，B/C）、DCD Africa（低召回，B）、非洲数据中心协会（B 报告/C 无源设施主张）。
- **运营商/托管商**：BBS（A 服务）、Lumitel（A 服务页，设施未证明）、ONATEL（A 运营商，B/C 设施）、Econet Leo（C 人员线索，除非官方招聘页/招标捕获）、CNI/NIC.BI（B/C）、Buja Online 等小托管商（C，多为境外转售）、Huawei/ZTE/Ericsson 厂商案例（B/C 佐证电信基础设施）。
- **生命周期动词**：`projet/etude/strategie/MoU` = intent；`appel d'offres/AMI/DAO/marche attribue` = procurement；`construction/travaux/installation` = under construction；`mise en service/operationnel/inaugure/lance` = operational（仍尽量主源验证）。

## 来源分级

- **A** = 官方或主要：ARCT 许可/法令/统计/招标、SETIC/PAFEN/PDDSP/eNama/Primature/财政部文件、运营商服务页或招标、REGIDESO/AREEN/OBPE 记录、世行项目文件、官方云商区域列表。
- **B** = 强二级：引述官方材料的本地/地区媒体、捐助者/项目报道、Internet Society/非盟 IXP 公告、PeeringDB 互联元数据、公认行业媒体。
- **C** = 仅线索：colocation/托管聚合器、社交帖子、LinkedIn 职位、无具名布隆迪站点的厂商营销、旧 MoU、抓取目录条目、无源本地博客。
- 状态：`operational`、`marketed_service`、`procurement`、`planned`、`under_construction`、`unknown`、`negative`；设施类型精确化：`commercial_hosting`、`telco_core`、`ixp`、`government_dc`、`planned_national_dc`、`university_compute_centre`、`registry_infrastructure`、`edge_pop`、`lead_only`；容量通常为 null，不从未订户数/云营销/光纤公里推断。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL 中的 BI 记录与种子（SETIC、CDIN、PAFEN/CIU、BBS、Lumitel、ONATEL、Econet、CNI/NIC.BI、BDIXP）。
2. 每区工作流：①现行 5 省检索 ②扩展到 18 个旧省名与省会/公社名 ③对 ARCT/SETIC/PAFEN/Primature/财政部/BBS/OBPE/REGIDESO/AREEN/运营商域跑 `site:` 搜索 ④运营商+地名 ⑤项目词（PAFEN、PDDSP、CDIN、CIU、BERNET、COMGOV、eNama、fibre optique、point de presence、hebergement）⑥记录阴性（仅网吧/培训室/泛 ICT 办公室/学校实验室/NGO 服务器机房/无基础设施新闻稿）。
3. 高产区映射：Bujumbura（SETIC/BBS/ONATEL/Lumitel/Econet/CNI/BDIXP/银行，唯一商业集群）；Gitega（政治首都，CIU@Gitega 理工大学，CDIN 未来站点）；其余三省以 PoP/电信机房为主。
4. 输出 schema：`{country_code: BI, country_name: Burundi, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`（division 用 5 省归一化并在 notes 保留旧省/原始来源文本；Rumonge 若 schema 固定为 17 省则同时记 Bururi 与 Bujumbura Rural 父省）；阴性区 `no_projects: true`。
5. 去重政府基础设施：SETIC 数据中心/eNama 托管/PAFEN 国家托管/CDIN 可能重叠或未来同址；来源证明同址才合并为一条物理记录，否则分开 `planned/project` 记录并交叉引用。不动 explorer-*.md，NO-DELETION。

## 待办（2026-08-12）

- [ ] SETIC 数据中心：找到 SETIC 主源具名站点/设施，升级 B→A。
- [ ] CDIN：追踪 PDDSP 实施证据（招标/授予/EIES/施工/启用）。
- [ ] PAFEN 5 个 CIU：确认各计算中心部署与位置（UB、ENS、INSP、UPG、UEA）。
- [ ] BBS colocation：寻找站点/机房/机架/电力/SLA 证据。
- [ ] Lumitel/Econet：核实云服务物理基础设施位置。
- [ ] 云区域阴性对照与 OBPE EIES：每次运行复查。
