---
name: ua-datacenter-methodology
location: scripts/expansion/world/country-skills/UA/SKILL.md
description: |
  Ukraine (UA) datacenter discovery & audit methodology — how to enumerate, verify, and update Ukraine datacenter projects at 24-oblast + Kyiv City/Crimea/Sevastopol granularity. Ukraine has no single public datacenter registry: enumeration joins the Unified State Electronic System in the Construction Sector (ЄДЕССБ, e-construction.gov.ua — permits, MUO urban-planning conditions, acts of readiness, commissioning certificates, open-data ZIPs on data.gov.ua), DIAM construction control, city/oblast council and military-administration records, NERC/NEURC + Ukrenergo + DSO grid-connection evidence (technical conditions, non-standard connection, substations), NCEC/NКЕК telecom-provider registers, SSSCIP cloud/DC provider list (public-sector regime, CMU Resolution 154/2025), Prozorro procurement, EIA registers, cloud-region negative controls (no AWS/Azure/GCP/OCI Ukraine region; Kyiv is a Google edge metro), and operator pages. Read this before running UA exploration/audit batches. Routes to explorer-official.md (ЄДЕССБ/energy/NCEC/cloud/operator/governorate matrix) and explorer-industry.md (IT Ukraine/SSSCIP/trade press/Ukrainian+Russian vocabulary/oblast templates).
---

# UA · 乌克兰数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：乌克兰**没有**全国公开的数据中心设施注册库；普查靠拼接 **ЄДЕССБ 建筑登记（许可/МУО/竣工证书）+ DIAM 建筑管控 + 市/州议会与军事管理局 + NERC/Ukrenergo/DSO 电网证据 + NCEC 电信运营商登记 + SSSCIP 云/DC 服务商清单 + 运营商页**。
> 乌克兰语与俄语变体都是必须（`дата-центр`/`центр обробки даних`/`ЦОД`/`серверна`/`хмарні послуги`…）；乌克兰建筑记录通常不用英文 `data center`；战争/占领状态对 Crimea、Sevastopol、Donetsk、Luhansk、Zaporizhzhia、Kherson 及部分 Kharkiv/Mykolaiv 的验证有实质影响。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供乌克兰探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：ЄДЕССБ 门户与对象页、DIAM、市/州议会与 MUA 规划、NERC/Ukrenergo/各 DSO 连接流程与计算器、NCEC/NКЕК 运营商登记、云区域官方页（负控制：AWS/Azure/GCP/OCI 均无乌克兰区域；国内云 De Novo/GigaCloud/Parkovyi）、运营商种子（De Novo/GigaCloud/Parkovyi/Kyivstar/Datagroup-Volia/Adamant/Cosmonova/UARNet/TENET/RX-NAME 等）、27 division 矩阵、验证与分级规则 |
| `explorer-industry.md` | 行业/厂商发现：IT Ukraine 协会、SSSCIP 云/DC 清单（A）、NCEC/InAU/UA-IX/PeeringDB、DCD/W.Media/Interfax/Ukrinform/Liga/AIN/dev.ua/Forbes 贸易媒体、目录种子（DataCenterMap/Inflect/Datacenters.com/Cloudscene/Baxtel）、按集群运营商种子（Kyiv/Odesa/Kharkiv/Dnipro/Lviv/Poltava/Rivne/Vinnytsia/Zaporizhzhia/Crimea-Sevastopol）、州级快速模板、云区域与边缘核查、证据分级 |

## 核心结构事实（框定每次搜索）

1. **ЄДЕССБ 是 A 级建筑主干**：https://e-construction.gov.ua/ 与 https://e-construction.gov.ua/reestri；对象页形如 `/permits_doc_detail/{id}`、`/document_detail/doc_id%3D{id}`；字段：文档类型（`Містобудівні умови та обмеження`/`дозвіл на виконання будівельних робіт`/`відомості про виконання будівельних робіт`/`акт готовності`/`сертифікат прийняття в експлуатацію`）、状态、登记号、机关（DIAM/前 DABI/市建筑局/hromada）、对象名、客户/投资者、地址、后果等级（СС1/СС2/СС3）、日期与造价；**data.gov.ua 月度 ZIP 是批量搜索最佳路径**。
2. **乌克兰记录不用英文词**：搜乌/俄变体 `дата-центр`、`дата центр`、`центр обробки даних`、`центр обработки данных`、`ЦОД`、`ЦОДД`、`серверна`、`серверний центр`、`хмарний дата-центр`、`обчислювальний центр`、`центр зберігання та обробки даних`。
3. **能源证据关键**：乌克兰设施页很少披露 MW——找非标准连接、变电站、变压器容量、柴油发电机许可、`технічні умови`；NERC/NEURC 连接程序与标准/非标准计算器、Ukrenergo 输电连接程序、区域 DSO（DTEK Kyiv/Dnipro/Odesa、Lvivoblenergo、Kharkivoblenergo、Poltavaoblenergo 等）。能源记录只证明电网状态，不证明数据中心——须同一法律实体/项目同时出现在建筑或运营证据。
4. **NCEC/NКЕК 是电信监管者**：https://nkek.gov.ua/ 提供电子通信网络/服务提供商登记（旧称 NCCIR/НКРЗІ）——运营商/连接性普查，非设施普查；用于归一化法律名称（Kyivstar、Datagroup/Volia、Adamant、Cosmonova/BeMobile、UARNet、TENET、RX-NAME）。
5. **SSSCIP 云/DC 清单（A）**：https://cip.gov.ua/ua/statics/cloud-dc-services 是受规管公共部门使用的云/DC 服务商官方清单（CMU Resolution 154/2025）——运营商/提供者种子渠道，非设施普查。
6. **云区域=负控制**：AWS/Azure/GCP/OCI 官方区域表均无乌克兰公共区域（检查日）；Google 将 Kyiv 列为网络边缘/对等互联 metro（互连信号，非云区域）；Kyivstar-AWS 生成式 AI 实验室合作 ≠ 区域。国内云（De Novo/GigaCloud/Tucha/Volia/Parkovyi）须运营商页+设施地址核实。
7. **市场 Kyiv 重度集中**：De Novo、Parkovyi/DataPark（Uptime/Tier III/CIPS）、GigaCenter/GigaCloud（五家 DC 含乌三/波二）、Kyivstar、Datagroup/Volia、Cosmonova/BeMobile、Lanet、Adamant；次级集群 Odesa（TENET/Arnautsky/HyperHost）、Kharkiv（Ukrnames/ITL/Infiumhost/Layer1）、Dnipro（Datasfera/SerinIX/Omega）、Lviv（UARNet）、Rivne（Campus/Datagroup）、Kremenchuk/Poltava（ColoCall）、Vinnytsia（IP-Connect DC-16）。
8. **战争/占领状态**：Donetsk/Luhansk/Kherson/Zaporizhzhia/Crimea/Sevastopol 及 Kharkiv/Mykolaiv 部分地区——目录与 2022 前页面为状态不确定，须当前运营商页/对等记录/监管申报/2024-2026 本地源确认；记录 de jure 乌克兰归属 + de facto/占领注记 + 来源管辖。
9. **旧大项目须当前复核**：Energoatom/Hotmine Zaporizhzhia（2020 宣布）、TECHIIA/Kherson Ecotechnopark（500 MW/10 亿美元概念）——无新证据前保持 announced/planned，MW 只入 notes。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§4 / explorer-industry.md §2-§3）

- 乌/俄核心词：`дата-центр` `дата центр` `центр обробки даних` `центр обработки данных` `ЦОД` `серверна` `серверний центр` `хмарний дата-центр` `хмарний провайдер` `колокація` `колокейшн` `розміщення серверів` `обчислювальний центр` `суверенний дата-центр` `AI дата-центр`。
- 建筑：`site:e-construction.gov.ua "дата-центр"`、`site:e-construction.gov.ua "центр обробки даних"`、`site:e-construction.gov.ua "{operator}" "дозвіл на виконання будівельних робіт"`、`site:e-construction.gov.ua "{city}" "серверна"`、`"{city}" "дата-центр" "містобудівні умови"`、`"{operator}" "{city}" "сертифікат готовності"`、`site:data.gov.ua "Реєстр будівельної діяльності" "дата-центр"`。
- 能源：`"{operator}" "{city}" "технічні умови" "електропостачання"`、`"{operator}" "{city}" "приєднання до електричних мереж"`、`"дата-центр" "нестандартне приєднання"`、`"центр обробки даних" "трансформаторна підстанція"`、`"ЦОД" "МВт" "Україна"`、`"дата-центр" "дизель-генератор"`、`site:nerc.gov.ua "дата-центр"`、`site:ua.energy "приєднання"`。
- 电信：`site:nkek.gov.ua "Реєстр постачальників" "{operator}"`、`"НКЕК" "{operator}"`、`"НКРЗІ" "{operator}" "дата-центр"`。
- 英文：`"Ukraine" "data center" "building permit"`、`"Kyiv" "data center" "construction permit"`、`"Kyivstar" "AI data center" Ukraine MW`、`"De Novo" "data center" Kyiv`、`"GigaCloud" "data centers" Ukraine Kyiv Lviv Warsaw`。
- 行业：`site:datacenterdynamics.com/en/news/ Ukraine "data center"`、`site:w.media Ukraine "data center" Kyivstar VEON`、`site:interfax.com.ua Ukraine "data center" Energoatom`、`site:ukrinform.net Ukraine "data center"`、`site:ain.ua "дата-центр"`、`site:dev.ua "ЦОД"`、`site:itukraine.org.ua/en "data center"`。
- 云负控制：`"AWS" Ukraine "region" "Availability Zone"`、`"Azure" Ukraine "region"`、`"Google Cloud" Kyiv Ukraine "edge locations"`、`"Oracle Cloud" Ukraine "region"`。

## 官方/监管管线要点（详见 explorer-official.md）

- **ЄДЕССБ/DIAM（A）**：e-construction.gov.ua + data.gov.ua 月度 ZIP（`дата-центр`/`ЦОД`/`центр обробки даних`/运营商名/地址批量搜索）；提取文档类型/状态/登记号/机关/对象名/后果等级/客户/地址/日期/造价；注意战时法令可能限制字段；许多在营设施早于公开覆盖或是电信/办公改造。
- **市/州规划（A/B）**：市议会、州军事管理局、hromada 门户、Prozorro（公共部门服务器机房/设备/发电机/云服务招标，A 但多非商业批发设施）。
- **能源（A）**：NERC/NEURC 连接程序与标准/非标准计算器、Ukrenergo 程序、DSO 连接页；提取标准 vs 非标准、请求/签约 kW/MW 或变压器 MVA、连接点/变电站、线路工程、柴油发电机/电池 UPS、申请/技术条件/并网日期、战时临时连接规则；`requested_connection_mw`/`contracted_power_mw`/`it_load_mw`/`backup_generator_mw`/`substation_mva` 分字段。
- **NCEC（A，支持证据）**：NKЕК 提供商登记与决议，归一化运营商法律名称。
- **云（A 区域/负控制）**：AWS/Azure/GCP/OCI 官方表均无乌克兰公共区域；国内云须设施证据。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **协会/监管清单**：IT Ukraine（B，成员/文章点名 Parkovyi 等）、SSSCIP 云/DC 清单（A 提供商状态）、InAU（B）、UA-IX/PeeringDB（B/C 活跃对等互连证据）、CEE Legal Matters（B，法规语境）。
- **贸易媒体**：DCD Ukraine tag（B，最佳国际流）、W.Media（B，Kyivstar/VEON）、Interfax-Ukraine（B/B+，签约与公司引语）、Ukrinform（B+，官方公告）、Liga/AIN.UA/dev.ua/MC.today/Forbes Ukraine（B/C）、Schneider/Vertiv/ITG 集成商案例（C+/B-）。
- **目录（C+ 种子）**：DataCenterMap（Kyiv 覆盖最全但可能过时）、Inflect、Datacenters.com、Cloudscene、Baxtel（当前弱/空）。
- **运营商种子（A=服务/位置/B=容量认证）**：De Novo（Kyiv，2010 一期/2017 二期，360 机架）、Parkovyi/DataPark（Uptime/Tier III/CIPS/KСЗІ）、GigaCenter/GigaCloud（五 DC：乌三波二）、Kyivstar（现有 colo + 2026 AI DC 计划，B）、Datagroup（自有 Kyiv DC）/Volia、Cosmonova（Hrinchenka 2/1 2013）/BeMobile、Lanet、UARNet（Lviv）、TENET/Arnautsky（Odesa，Velyka Arnautska 2-A）、RX-NAME（Mykolaiv）、HyperHost（B/C）、Ukrnames/ITL/Infiumhost/Layer1（Kharkiv，战时须当前源）、ColoCall（Kremenchuk）、Campus/Datagroup（Rivne）、IP-Connect DC-16（Vinnytsia）；Crimea/Sevastopol：Miranda-Media（俄域，争议/占领注记）。
- **状态映射（乌语）**：`меморандум/намір`=宣布；`містобудівні умови`/`технічні умови`=规划/早期；`дозвіл на виконання будівельних робіт`=已许可；`відомості про виконання будівельних робіт`/`початок`=在建；`акт готовності`/`сертифікат прийняття в експлуатацію`/`введено в експлуатацію`/`запущено`=运营。

## 来源分级

- **A** = 官方/一手：ЄДЕССБ 许可/开工/竣工/认证记录、DIAM 记录、市 MOU（须配许可/土地/电力）、NERC/Ukrenergo/DSO 连接记录与技术条件、NKЕК 提供商登记与决议、SSSCIP 清单、运营商官方设施页（存在/位置）、官方云区域/边缘位置文档、Prozorro 招标、EIA 记录。
- **B** = 强二级：DCD、W.Media、Interfax-Ukraine、Ukrinform、Light Reading、IT Ukraine 文章、可信法规分析、PeeringDB/UA-IX 活跃互连、运营商博客（间接设施语境）。
- **C** = 仅线索：DataCenterMap、Inflect、Datacenters.com、Cloudscene、Baxtel、市场列表、旧论坛/博客、无运营商佐证的第三方地址/规格页。
- **容量规则**：优先电网/公用事业记录的 MW/MVA 或官方项目文件（requested/contracted/IT load 分开）；只有机架数不换算 MW；旧大项目 MW 入 notes，状态保持 announced/planned。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=UA，divisions=24 州 + Kyiv City/Crimea/Sevastopol）。
2. 种子：运营商官方页（De Novo/Parkovyi/GigaCloud/Kyivstar/Datagroup/Volia/Cosmonova/Lanet/Adamant/TENET/UARNet/RX-NAME）+ NKЕК 登记 + SSSCIP 清单 + 目录线索；归一化别名（GigaCloud/GigaCenter/GigaTrans、Parkovyi/Datapark、Datagroup/Volia、Cosmonova/BeMobile、Kyiv/Kiev、Odesa/Odessa、Kharkiv/Kharkov）。
3. ЄДЕССБ 搜索：核心乌/俄术语 + 运营商法律名 + 已知地址；捕获许可/竣工字段与文档 ID；用 data.gov.ua ZIP 批量。
4. 市/州门户搜索：Kyiv、Lviv、Odesa、Kharkiv、Dnipro、Mykolaiv、Poltava/Kremenchuk、Rivne、Vinnytsia、Khmelnytskyi、Zaporizhzhia、Kherson 优先；用 `МУО`/土地/议会/投资项目记录。
5. 电力交叉核对：NERC/Ukrenergo 流程页 + 相关 DSO（`технічні умови`/`нестандартне приєднання`/变电站/发电机许可/变压器容量）。
6. 云验证：AWS/Azure/GCP/OCI 官方表作负控制；国内提供商页核实实体设施 vs 租用 colo vs 境外区域服务。
7. 去重：按 (终极母公司 + 本地法律实体 + 设施品牌 + 地址/hromada + division + 来源管辖 + 许可登记号 + 电网连接 ID/变电站)；注意 Kyiv City vs Kyiv Oblast 分桶错误与占领区目录（国际目录归俄、repo 归 UA）。
8. 输出与 world 探索同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`（含 de facto/占领注记）；无项目 division 写 `no_projects: true`；容量区分 `operational` / `under_construction` / `planned_full_buildout_mw`。
9. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：批量复核乌克兰数据中心（州粒度，Kyiv 深扫）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Kyivstar AI 数据中心（VEON/经济部 MoU → 站点/MW/许可）、De Novo/Parkovyi/GigaCloud 扩建、Energoatom-Hotmine Zaporizhzhia 与 TECHIIA-Kherson 旧概念是否有新许可/电力证据、战时对 Kharkiv/Mykolaiv/Odesa 设施运营的影响、SSSCIP 清单新入选者、Ukrenergo/DSO 队列中的具名大型负荷。
