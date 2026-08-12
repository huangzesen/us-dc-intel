---
name: ao-datacenter-methodology
location: scripts/expansion/world/country-skills/AO/SKILL.md
description: |
  Angola (AO) parent-level methodology for data-center enumeration at province granularity (18 manifest
  provinces; Angola's 2024 reform created 21 official provinces - map Icolo e Bengo/Cuando/Cubango/Moxico
  Leste evidence back to manifest divisions). Angola has no public national data-center register and no
  public planning-permit search engine; enumeration joins government-cloud announcements (MINTTICS/INFOSI),
  telecom/operator official pages (Angola Cables, Raxio, Paratus, Africell, Unitel), public procurement
  (Portal Compras Publicas/SNCP, Diario da Republica), municipal licensing leads, energy/grid context
  (IRSEA/ENDE/RNTEP), and trade press. Market is Luanda-centric: INFOSI Camama government cloud (op 2026-04-28),
  AngoNAP Luanda, Raxio AO1 Cacuaco (3 MW/800+ racks), Paratus DC1/DC2 + planned third DC, Africell Kings
  Tower; only non-Luanda watch is AnyConnect/Visium Lubango DR (planned, Huila). No hyperscaler public
  region. Routes to explorer-official.md (regulator/government/procurement/energy pipeline) and
  explorer-industry.md (press/operator/directory pipeline).
---

# AO · 安哥拉数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：安哥拉没有公开的国家数据中心登记册或类似美国县/英国规划门户的公开规划许可检索引擎；枚举必须拼接政府云公告（MINTTICS/INFOSI）、电信/运营商官方页（Angola Cables、Raxio、Paratus、Africell、Unitel）、公共采购（Compras Publicas/SNCP、《共和国日报》）、市政施工许可线索、能源/电网背景（IRSEA/ENDE/RNTEP）与行业媒体。市场以卢安达（Luanda）为中心：INFOSI Camama 政府云（2026-04-28 启用）、AngoNAP Luanda、Raxio AO1 Cacuaco（3 MW/800+ 机架）、Paratus DC1/DC2 + 规划第三 DC、Africell Kings Tower；非卢安达唯一观察项为 AnyConnect/Visium Lubango DR（规划中，Huila）。**18 省为本仓清单模型**（官方 2024 改革为 21 省：Icolo e Bengo/Cuando/Cubango/Moxico Leste 证据映射回原省）。无超大规模公共区域。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供安哥拉探索与复核批次使用。

## 入口

| 文档 | 用途 |
|---|---|
| `explorer-official.md` | 官方/监管管线：INACOM/Observatorio TIC、MINTTICS、INFOSI、Compras Publicas/SNCP、AIPEX/JUI、IRSEA/ENDE/RNTEP、云区域阴性对照、官方设施观察清单、18 省矩阵 |
| `explorer-industry.md` | 行业管线：行业/本地媒体（Jornal de Angola/Angop/Expansao/DCD 等）、运营商/厂商扫库、目录处理、逐省行业矩阵、置信度规则 |

## 核心结构事实（框定每次搜索）

1. **无登记册**：没有公共国家数据中心登记册，也没有可比的公开规划许可检索引擎；枚举 = 政府云公告 + 运营商官方页 + 公共采购 + 市政施工许可线索 + 能源/电网背景 + 行业媒体。
2. **18 省清单模型**：Bengo, Benguela, Bie, Cabinda, Cuando Cubango, Cunene, North Cuanza, South Cuanza, Huambo, Huila, North Lunda, South Lunda, Luanda, Malanje, Moxico, Namibe, Uige, Zaire；2024 年官方改革为 21 省（Icolo e Bengo 从 Luanda 分出、Cuando/Cubango 从 Cuando Cubango 分出、Moxico Leste 从 Moxico 分出）——新省证据映射回清单省。
3. **卢安达为中心**：已确认设施全部在 Luanda 省：INFOSI 政府数据中心与云（Camama，2026-04-28 启用，MINTTICS 2023 页称 USD 89M、约 5,320 m2 预制两层楼）、INFOSI 备份/遗留 Centro Nacional de Dados（ITEL/Rangel）、Angola Cables AngoNAP Luanda、Raxio AO1（Cacuaco，2025-10-02 启用，USD 30M，3 MW IT、800+ 机架）、Paratus/ITA DC1/DC2（Patriota/Benfica，2017/2019 启用，DCD 称 1,500/7,000 服务器容量）、Africell Kings Tower（2021-10 启用，中心区 HQ）。
4. **Paratus 第三 DC 为 planned**：Paratus 官方 2023 公告称卢安达第三 DC，>10 MW IT、>2,000 机柜、30,000 m2 地块；在施工证据出现前保持 planned。
5. **非卢安达默认阴性**：唯一观察项为 AnyConnect/Visium 2025 年 6,000 万美元数字基础设施框架中规划的 Lubango（Huila）二级 DR 设施——planned/B/C，直到约束性官方/运营商来源确认站点、融资与建设状态。
6. **无超大规模区域**：AWS/Azure/GCP/OCI 官方列表无安哥拉公共区域；`cloud/sovereign cloud/hosted cloud/edge/PoP/Direct Connect/CDN` 语言只是服务/网络证据，除非官方云商页列出安哥拉物理区域。
7. **语言**：葡萄牙语为主（centro de dados、centro de processamento de dados、centro nacional de dados、cloud nacional/do governo/soberana、nuvem、colocation、hospedagem、sala de servidores、licenca de construcao/obras、alvara、concurso publico、decreto presidencial、Diario da Republica）；英文用于 DCD/厂商/云区域。
8. **容量纪律**：容量/机架数字常缺失或冲突；仅用来源支持值——Raxio 官方 2025 启用稿 3 MW/800+ 机架；Paratus 官方 2023 公告 >10 MW/>2,000 机柜；目录/媒体称 INFOSI 208/336 机架与 ~1.04 MW 为 B/C；主源未给出时 `capacity_mw` 留 null。
9. **监管/政府结构**：INACOM（运营商监管 + Observatorio TIC 市场数据）、MINTTICS（国家数字基础设施部委）、INFOSI（国家信息社会促进局，Decreto Presidencial 135/21，运营 Rede Privativa do Estado 与政府 DC/云）、Portal Compras Publicas/SNCP（Lei 41/20 公共合同法）、AIPEX/JUI（Decreto 167/20，投资登记）、IRSEA/ENDE/RNTEP/PRODEL/MINEA（能源）。
10. **排除项**：AngoNAP Fortaleza（巴西）、AngonIX/IXP、PeeringDB、CDN PoP、海缆登陆站、卫星地面站、无安哥拉物理站点的泛云/托管/VPS 页面、省级电信交换/服务器机房（除非来源明确称其为数据中心并给站点）。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§2/§3、explorer-industry.md §1/§2/§5）

```text
site:inacom.gov.ao "data center" OR "centro de dados"
site:inacom.gov.ao "Licenca Multiservicos" "{operator}"
site:observatoriotic.gov.ao "{operator}"
site:minttics.gov.ao "data center" OR "centro de dados" OR "cloud nacional"
site:minttics.gov.ao "Data Center e Cloud do Governo" OR "Camama" OR "Rangel"
site:infosi.gov.ao "data center" OR "centro de dados" OR "Centro Nacional de Dados"
site:infosi.gov.ao "Rede Privativa do Estado" OR "Decreto Presidencial" "135/21"
site:compraspublicas.minfin.gov.ao "data center" OR "centro de dados" OR "INFOSI"
site:sncp.minfin.gov.ao "data center" OR "centro de dados"
"concurso publico" "data center" Angola
site:aipex.co.ao "data center" OR "centro de dados"
site:irsea.gov.ao "data center" OR "grande consumidor"
"ENDE" "subestacao" "Cacuaco" OR "Camama" OR "Talatona"
"Data Center e Cloud do Governo" OR "Data Center e Cloud Nacional" Angola
"INFOSI" "data center" Camama OR Rangel
"Angola Cables" AngoNAP Luanda colocation
"Raxio" Angola AO1 Cacuaco "3MW" OR "800 racks"
"Paratus" Angola "data center" Luanda OR Patriota OR Benfica
"Africell" "data center" "Kings Tower" Angola
"Unitel" "data center" "Luanda Sul"
"AnyConnect" "Lubango" "data center" OR "disaster recovery"
site:jornaldeangola.ao "data center" OR "centro de dados"
site:angop.ao "data center" OR "centro de dados"
site:datacenterdynamics.com/en/news/ Angola "data center"
"{province}" "data center" OR "centro de dados" OR "sala de servidores"
"Icolo e Bengo" "data center" OR "centro de dados"
"Cuando" OR "Cubango" OR "Moxico Leste" "data center"
"Angola" "cloud region" AWS OR Azure OR "Google Cloud" OR Oracle
```

## 官方/监管管线要点（详见 explorer-official.md）

- **INACOM**：电子通信与邮政市场监管/监察机构；Observatorio TIC 市场数据页暴露运营商名（Angola Telecom、Africell、Movicel、Unitel、LMS、MS Telcom、Net One、Multitel、Startel、ITA/Paratus、Infrasat、TV Cabo、DSTV、ZAP）；确认持牌实体，不构成设施证明。
- **MINTTICS**：政府数字基础设施决定性部委来源：2026-04-28 政府 DC 与云启用页（A）、2023-02-16 国家云项目页（USD 89M、Camama 约 5,320 m2 主 DC、Rangel ITEL 旁备份 DC 现代化）、ANGOTIC/华为/Unitel/AI 厂商协议页。
- **INFOSI**：国家云与政府网络运营商（Rede Privativa do Estado、政府 DC/云环境；章程 Decreto Presidencial 135/21）；核实 Camama 主设施与 Rangel 备份设施。
- **采购/公报**：Portal Compras Publicas + SNCP（Lei 41/20）——机构项目早于媒体出现；Diario da Republica 查法令/授权；提取签约实体、供应商、范围、站点/市、日期、价值、物理建设 vs IT 硬件更新。
- **投资/许可**：AIPEX/JUI（Decreto 167/20，私营 DC 投资线索）；SEPE 电子公共服务门户；市政施工许可（licenca de obras/construcao/alvara）无可靠可检索数据库，证据多出现在媒体/AIPEX/市政公告/公司发布中。
- **能源**：IRSEA（水电监管/电价）、MINEA（政策）、ENDE/RNTEP/PRODEL（配电/输电/发电）；安哥拉电网水电占比高但可靠性不一，大型 DC 依赖 UPS 与柴油；电网/变电站新闻可佐证 Camama/Cacuaco/Talatona/Patriota/Benfica/Viana/ZEE 与 Lobito 走廊附近可行性。
- **数据保护**：Lei 22/11（2011-06-17 个人数据保护法）为需求驱动背景；银行（BNA）与政府部门内部 DR/机房仅当具名站点/招标/官方设施主张时计数。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **Angola Cables**（angolacables.co.ao/datacenter）：AngoNAP Luanda 官方服务页（A 存在/服务）；机架/MW 数字 C；不把巴西 Fortaleza 计入。
- **Raxio AO1**：官方 2025 启用稿 = 3 MW IT、800+ 机架、USD 30M、Cacuaco/Luanda（A）；部分目录报 7 MW 为未来/规划扩展。
- **Paratus/ITA**：官方服务页（A 现役 DC1/DC2）；DCD 2017/2019 启用与服务器容量（B）；第三 DC 官方 2023 公告（A planned）。
- **Africell**：2021 官方稿确认 HQ Kings Tower 云化 DC（HP/Nokia/Dell/Oracle 与本地伙伴），支持移动网络与本地企业（A）；容量未公开。
- **Unitel**：Luanda Sul 与 Filda DR 为目录线索（C），需 Unitel 官方/媒体/采购佐证。
- **Movicel/Angola Telecom/MSTelcom/Startel/Infrasat**：核心机房为电信设施线索，不是自动商业 DC。
- **Clouds2Africa**：AngoNAP 支撑的云服务，非独立设施。
- **媒体分级**：Jornal de Angola/Angop（A/B，官方事实引述）、Expansao/Novo Jornal/Verangola/Macauhub（B）、Menos Fios/Primeiro IT（B/C）、Agence Ecofin/We Are Tech/TechAfrica News/DCD/The Tech Capital/Capacity/Developing Telecoms（B）、Engineering News/World Construction Network（B，Paratus 第三 DC 施工）。
- **目录纪律**：DataCenterMap/datacenters.com/Baxtel/OCOLO/Inflect/HostDir/colo.exchange/Cloudscene/DigitalAngola.com 为 C 默认；升级流程 = 精确名称 → 运营商官方域 → MINTTICS/INFOSI/INACOM/compraspublicas → Angop/Jornal de Angola/DCD 等 → Uptime Institute → 无主源保持 C。

## 来源分级

- **A** = 官方/主要：MINTTICS 或 INFOSI 页面、INACOM 或 Observatorio TIC 记录、《共和国日报》法令、运营商官方设施页、Compras Publicas/SNCP 招标或授予、AIPEX/JUI 决定、IRSEA/ENDE/RNTEP/PRODEL/MINEA 页面、官方云区域页、Uptime Institute 认证记录、官方政府新闻（governo.gov.ao、部委页、使领馆页；Angop 携带官方仪式/部长事实时可 A）。
- **B** = 强二级：Jornal de Angola、Expansao、Novo Jornal、Verangola、Macauhub、Agence Ecofin/We Are Tech、TechAfrica News、DCD、The Tech Capital、Capacity、Developing Telecoms、Engineering News、具名客户/站点的厂商案例。
- **C** = 弱线索：DataCenterMap/datacenters.com/Baxtel/OCOLO/Inflect/HostDir/Cloudscene/colo.exchange、DigitalAngola.com 聚合档案、市场报告、LinkedIn/社交帖子、未验证本地博客。
- 状态动词：`memorando de entendimento/protocolo/acordo/parceria/anunciou` = planned；`concurso publico/adjudicacao/contrato` = procurement；`obra/construcao/fase de instalacao` = construction；`inaugurou/abriu/entrou em funcionamento/operacional` = operational；`cloud/hospedagem/VPS/sovereign cloud` = 仅服务证据。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL 中的 AO 记录与种子（INFOSI Camama/Rangel、AngoNAP、Raxio AO1、Paratus DC1/DC2 + 第三 DC、Africell、Unitel 线索、AnyConnect Lubango）。
2. 每次运行重新验证日期敏感状态：INFOSI Camama 2026-04-28 运营；Raxio AO1 2025-10-02 启用；Paratus 第三 DC 保持 planned。
3. 逐省扫描：Luanda 详尽；Huila/Lubango 观察 DR；Benguela（Lobito 走廊）与 Zaire（Soyo）油气/物流二级；Cabinda/Lunda Norte/Lunda Sul/Namibe 采掘/港口内部线索；Huambo/Bie/Malanje 大学/机构；其余省阴性默认，含新省名（Icolo e Bengo/Cuando/Cubango/Moxico Leste）别名。
4. 提升规则：非卢安达线索仅在官方/运营商具名物理站点、具名招标/授予或带可问责来源的强媒体时才成为项目条目，否则 `no_projects: true` 或 notes 中 C 线索。
5. 输出 schema：`{country_code: AO, country_name: Angola, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`（division 用 18 清单省，notes 保留官方地名与 21 省别名）。不动 explorer-*.md，NO-DELETION。

## 待办（2026-08-12）

- [ ] Paratus 第三 Angola DC：追踪施工/启用证据（>10 MW、>2,000 机柜、30,000 m2）。
- [ ] INFOSI Camama 容量：等待 MINTTICS/INFOSI 官方技术文件确认机架/MW。
- [ ] AnyConnect/Visium Lubango DR：寻找约束性官方/运营商来源（站点、融资、建设）。
- [ ] Unitel Luanda Sul/Filda：用 Unitel 官方/媒体/采购佐证目录线索。
- [ ] Uptime 认证核实：Raxio AO1、Paratus、AngoNAP 的认证类型与设施名。
- [ ] 云区域阴性对照：每次运行复查。
