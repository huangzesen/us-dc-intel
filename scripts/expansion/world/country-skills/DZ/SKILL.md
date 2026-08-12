---
name: dz-datacenter-methodology
location: scripts/expansion/world/country-skills/DZ/SKILL.md
description: |
  Algeria (DZ) datacenter discovery & audit methodology — how to enumerate, verify, and update Algeria datacenter projects at wilaya granularity (58 wilayas in the current manifest). Algeria has no single public national data-center register and no complete public planning-permit search: enumeration joins ARPCE cloud/hosting authorisations, ministry/public-enterprise announcements (MPT, HCN/Huawei national digital-services centers, Algerie Telecom, Algerie Poste), BOMOP/ANEP public tenders, AAPI/APC/wilaya urbanism routes, Sonelgaz/CREG power context, official cloud-region pages (no hyperscale DZ region — sovereign/hosted-cloud market), and operator pages (Djezzy Cloud, AYRADE, ICOSNET, ISSAL, eBS/WebServices, ADEXCLOUD). French is the primary official language, Arabic secondary, English for trade press. Key anchors: Mohammadia/Alger national DC (Tier III Design), Blida second national DC (planned), Algerie Telecom Constantine DC (inaugurated 2023-02-23), MPT Oran AI data center (foundation stone), OPGI Djelfa secondary DC, UMMTO Tizi Ouzou HPC/AI. Read this before running DZ exploration/audit batches. Routes to explorer-official.md (ARPCE/ministries/tenders/urbanism/energy/cloud) and explorer-industry.md (trade press/operators/directories/wilaya matrix).
---

# DZ · 阿尔及利亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：阿尔及利亚**没有**统一的全国数据中心注册库，也无类美式县级规划的完整公开许可检索；枚举靠**拼接** ARPCE 云/托管授权、部委/国企公告、BOMOP/ANEP 公共招标、AAPI/APC/wilaya 城市规划路由、Sonelgaz/CREG 电力上下文与运营商页。
> 公共数据中心活动**国家主导**：数字化高级委员会/Huawei 国家数字服务中心、邮电部项目、Algerie Telecom 设施、Algerie Poste、部委/OPGI 次级数据中心、大学 HPC/云项目、Sonatrach/Sonelgaz 内部设施；商业 colo 更薄，集中在 Alger/Cheraga/Sidi Abdellah、Oran、Constantine 及 Bejaia/Ouargla 少量线索。
> 法语为主、阿拉伯语为辅、英语用于贸易媒体与云厂商页。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供阿尔及利亚探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/采购管线：ARPCE 云与托管授权（含撤销/制裁）、邮电部 MPT 新闻与项目页（Oran 奠基/Algerie Poste/Tiaret）、数字化高级委员会 HCN-Huawei（Mohammadia 国家 DC + Blida 第二个）、Algerie Telecom 官方公告（Constantine 2023-02-23）、BOMOP/ANEP 招标（OPGI Djelfa/UMMTO/国防部）、AAPI/内政部/住建部城市规划路由、Sonelgaz/CREG/ELIT 电网证据、云区域官方负面核查、58 wilaya 五遍扫描与优先簇、提取规则 |
| `explorer-industry.md` | 行业/厂商发现：DCD/APS-AMan/Ecofin-WeAreTech/Telecompaper/DC Magazine/Maghreb Emergent 媒体、运营商/厂商种子表（Algerie Telecom/HCN-Huawei/Djezzy Cloud/AYRADE/ICOSNET/ISSAL/eBS-WebServices/ADEXCLOUD/Syntys/MAHLIATOV/Sonatrach/Sonelgaz-ELIT/Algerie Poste）、目录处理（DataCenterMap/datacenters.com/Baxtel/Cloudscene/PeeringDB）、官方核验路由表、逐 wilaya 行业搜索矩阵（高/中/低优先级）、候选校准示例与输出纪律 |

## 核心结构事实（框定每次搜索）

1. **ARPCE 是云/托管授权主路由（A=服务/实体证据，非设施证据）**：其 cloud 服务页描述授权技术档案（服务描述、基础设施架构、连接方式、设备类型、存储/备份容量、数据安全系统）；实体可用自有设施、租用空间或伙伴基础设施提供云；注意授权撤销/制裁——被撤销授权需续期后才作当前运营证据。
2. **国家主导锚点（A）**：HCN-Huawei——Mohammadia（Alger）国家数字服务中心获 Uptime Tier III Design 认证（APS/AMan/Uptime/BOMOP 佐证）；第二个国家 DC 在 Blida（HCN-Huawei 协议 + BOMOP “Data Center Facilities” 招标）；可能的国家 DR/业务恢复 DC 招标（未点名 wilaya 时保持国家级线索）。
3. **Algerie Telecom Constantine**：官方 2023-02-23 启用公告（A），云平台收集/处理/存储企业数据；Lakhdaria/Bouira 历史计划（DCD/Ecofin 线索，须新官方确认，视为计划）；模块化/集装箱/托管 DC 帖多为客户产品而非自有站点。
4. **采购是最佳机构设施探测器**：BOMOP/ANEP + 部委/大学/wilaya/市镇招标页；实例：MHUv 官方招标点名 `Data Center secondaire ... OPGI de Djelfa`（A）、UMMTO Tizi Ouzou `Data Center HPC/AI et Cloud Prive`、国防部 `centre de donnees sis a Alger`；聚合器（DZtenders/Algerie Marches 等）为 C 线索但 BOMOP 受限时有用。
5. **城市规划证据通常不可按项目公开检索**：AAPI 许可申请流程/内政部表格只证行政路径；用市镇/wilaya/本地媒体/招标文件找具名项目；提取市镇、wilaya、投资人、地块、cyberpark/工业园、许可/合规证号、面积、发电机/HVAC/消防线索。
6. **电网（Sonelgaz/CREG/ELIT）**：多为上下文与公用事业确认源；Sonelgaz 客户联络中心材料说平台集中在 ELIT 数据中心，呼叫平台在 Alger/Constantine/Blida/Oran（内部企业证据）；全国电力统计**不得换算设施容量**，仅具名站点才记 kVA/MVA/MW。
7. **无超规模云区域（负面核查）**：AWS/Azure/GCP/OCI 官方列表均无 DZ 区域；阿尔及利亚为本地主权/托管云市场；Huawei 是国家项目集成商而非必然华为云区域；勿把边缘/伙伴服务变体为物理云区域。
8. **优先 wilaya**：Alger（Mohammadia/Sidi Abdellah Cyber Parc/Cheraga/APN/部委）、Blida、Constantine、Oran（MPT AI 数据中心奠基）、Bouira-Lakhdaria（计划）、Ouargla-Hassi Messaoud（Sonatrach 工业计算）、Tizi Ouzou（UMMTO）、Djelfa（OPGI 次级）、Tiaret（邮政综合体）、Bejaia（Djezzy Cloud/Amizour 线索）、Annaba/Skikda（港口/MAHLIATOV）、Batna/Laghouat/Guelma/Khenchela/Medea（大学 HPC）。2019 年新 wilaya（Timimoun 等）搜旧父 wilaya，物理市镇支持才归现 wilaya。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§3 / explorer-industry.md §0/§5）

- ARPCE：`site:arpce.dz "Hébergement et Stockage en Cloud Computing"`、`site:arpce.dz "centre de donnees"`、`site:arpce.dz "{operator}" "autorisation"`、`site:arpce.dz "Liste des Operateurs" "cloud"`、`site:arpce.dz "retrait definitif" "cloud computing"`。
- 部委/国家：`site:mpt.gov.dz "centre de donnees"`、`site:mpt.gov.dz "{wilaya}" "fibre optique" "data center"`、`site:algerietelecom.dz "data center"`、`site:algerietelecom.dz "cloud" "Constantine"`、`"Haut-Commissariat a la Numerisation" "centre de donnees"`、`"Mohammadia" "Data Center National 1"`、`"Blida" "centre de donnees national" "Huawei"`、`site:aps.dz "data center national"`。
- 采购：`site:bomop.anep.dz "data center"`、`site:bomop.anep.dz "centre de donnees"`、`site:bomop.anep.dz "{wilaya}" "data center"`、`site:mhuv.gov.dz "OPGI" "Data Center"`、`site:mdn.dz "centre de donnees"`、`site:{university-domain} "HPC" "cloud"`。
- 城市规划：`"{operator}" "{wilaya}" "permis de construire"`、`"{project}" "certificat de conformite"`、`"{project}" "AAPI" "data center"`、`site:{wilaya-domain} "centre de donnees"`。
- 电网：`site:sonelgaz.dz "Data Centers d'ELIT"`、`site:sonelgaz.dz "{wilaya}" "poste electrique" "data center"`、`site:creg.gov.dz "centre de donnees"`、`"{project}" "groupe electrogene" "data center"`、`"{project}" "MVA" "Algerie"`。
- 行业：`site:datacenterdynamics.com/en/news/ Algeria "data center"`、`site:datacenterdynamics.com/en/news/ "Algeria Telecom" "Constantine"`、`site:wearetech.africa Algeria "data center"`、`site:telecompaper.com Algeria "data centre" Huawei`、`site:dcmag.fr Algerie "datacenter" Mohammadia`、`site:elwatan.dz "centre de donnees" "Ouargla"`。
- 阿拉伯语：`"{wilaya_ar}" "مركز البيانات"`、`"الجزائر" "مركز البيانات"`、`"المحمدية" "مركز البيانات الوطني"`、`"وهران" "مركز البيانات" "الذكاء الاصطناعي"`。
- 状态词（法）：`accord/partenariat/protocole/approuve`=线索；`appel d'offres/attribution/signature du contrat`=采购；`pose de la premiere pierre/lancement des travaux`=在建；`inaugure/mis en service/operationnel/obtient la certification`=运营/投运；`solution cloud/hebergement/VPS`=纯服务证据。

## 官方/监管管线要点（详见 explorer-official.md）

- ARPCE：云/托管授权服务（A=授权/实体，C=设施）；FAI 列表、audiotex 列表、news/notices、cahier des charges PDF；提取法人、授权号、服务类别、地址、决定日期、存储/备份/安全/网络架构披露；运营商名搜索：Algerie Telecom、Mobilis、Djezzy、Ooredoo、ICOSNET、AYRADE、ISSAL、eBS、WebServices、ADEXCLOUD、Djezzy Cloud、Beyte Datacenters、Syntys、MAHLIATOV、TDA、Connexis、BringCom Algerie、Airband。
- MPT：新闻与项目页（Oran 奠基“advanced data center and AI computing center”、Algerie Poste 总部 DC、Tiaret 邮政综合体 DC）；A=项目事实与 wilaya；容量通常缺失，`capacity_mw` 置空除非官方给 MW/kVA/MVA。
- HCN/国家数字服务中心：APS/AMan/Uptime/BOMOP/Huawei 覆盖；Mohammadia 计独立国家 DC（官方/APS/Uptime 识别时），Blida 仅当招标/HCN/政府证据点名时计计划/在建；未点名 wilaya 的新 DR 招标保持国家级线索。
- Algerie Telecom：A=官方设施/服务证据；同时是模块化/托管 DC 解决方案的线索源（多为服务而非固定设施）。
- 采购：BOMOP/ANEP、MPT、MHUv、MDN、大学招标页；提取买方、wilaya、`sis a` 地点措辞、标的、标段号、ANEP 号、中标日期、承包商、新建/设备/维护/防火墙-Veeam-UPS 续期/服务器房。
- 城市规划：AAPI 许可文件、内政部表格、住建部服务；私有项目许可通常不可公开检索；用市镇/wilaya/媒体/招标找具名项目。
- 电网：Sonelgaz/CREG/ELIT；内部 DC 与 ELIT 托管平台证据；MW 级项目查变电站/变压器/并网容量/备用发电机/柴油库/可再生。
- 云：无 DZ 超规模区域（负面核查）；Huawei Cloud Stack 作为国家项目集成商核验（HCN/部委/BOMOP/APS）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 媒体：DCD（B，Constantine/Oran AI DC/议会 DC/Oman-Algeria 合作/HCN-Huawei）、APS/AMan（A/B，Mohammadia Tier III 认证）、Agence Ecofin/WeAreTech（B）、Telecompaper（B）、DC Magazine（B）、Maghreb Emergent/Algerie Eco/TSA/El Watan/El Moudjahid（B/C）、厂商案例（Huawei/Schneider/Vertiv/ICE，A=服务，B/C=设施细节）。
- 运营商/厂商种子：Algerie Telecom（Constantine A；Lakhdaria/Bouira 计划）、HCN-Huawei（Mohammadia/Blida）、Djezzy Cloud（主权云服务 A，Bejaia/Amizour 目录 C）、AYRADE（ARPCE 2024 授权 01/RM/ARPCE/2024 A，Sidi Abdellah 设施待证实）、ICOSNET（Cheraga/El-Qods 目录）、ISSAL NET/Flex Cloud（Oran 自营 DC 声称 B/C）、eBS/WebServices（Sidi Abdellah Cyber Parc，85 sqm DC 目录）、ADEXCLOUD（自营托管，地点须 ARPCE/公司核验）、Syntys（Constantine 33 Rue Belouizdad 目录）、MAHLIATOV（Annaba 专用服务器）、Sonatrach（Ouargla/Hassi Messaoud 内部工业计算）、Sonelgaz/ELIT（平台上下文）、Algerie Poste（机构设施）。
- 目录（C，须升级工作流）：DataCenterMap（Algiers/Oran/Cheraga/Constantine 线索，含 Huawei Mohammadia/WebServices/AYRADE DC 1/ICOSNET/APN/ISSAL Oran/Syntys）、datacenters.com、Baxtel（B=有源的新闻摘要）、Cloudscene（C/B-）、PeeringDB（只证网络存在）。升级流程：抓精确名/地址/容量 → 搜精确名+运营商官方域 → ARPCE 查法人/授权 → BOMOP/部委/城市规划/Uptime 查站点 → 无一手支持保持 C 并写备注。
- 校准示例：Constantine=A（官方公告）+B（DCD/Baxtel）；Mohammadia=A（APS/AMan+HCN/Uptime+BOMOP）；Blida=A/B 计划/工程（不标运营）；Oran=施工（MPT 奠基 A + DCD B）直至官方启用；AYRADE/ISSAL/Djezzy Amizour=服务 A、设施 C。

## 来源分级

- **A** = 官方/一手：ARPCE 授权或运营商列表、部委/wilaya/市镇/大学/国企页、BOMOP/ANEP 招标、官方采购页、AAPI/城市规划程序、Sonelgaz/CREG 证据、官方云区域页、官方运营商设施页、Uptime 认证记录。
- **B** = 强二级：APS（官方机构伙伴转载）、DCD、Agence Ecofin/We Are Tech、Telecompaper、声誉良好的阿尔及利亚全国媒体、具名客户与地点的厂商/集成商项目页。
- **C** = 弱线索：招标聚合器、DataCenterMap/Baxtel/datacenters.com、社交、市场报告、不可访问片段、目录页、未验证本地媒体。
- 不得计数：无物理设施证据的通用 cloud 服务页；呼叫中心（除非说明运行于/含数据中心）；ARPCE 办公室地址作数据中心地址；UPS/防火墙/软件续期招标（除非点名 DC 或服务器房）；云区域缺失/存在本身。
- 容量：仅当来源给出该设施的 MW/IT load 时填 `capacity_mw`；kVA/MVA/发电机/面积/机架记 notes；项目名以官方法语为准并附英文别名。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=DZ，divisions=58 wilayas）。
2. 建种子：ARPCE 授权名单 + Algerie Telecom/HCN-Huawei/MPT 官方页 + 采购线索（BOMOP/大学/OPGI）+ 已知地址 pivot（Sidi Abdellah Cyber Parc、Centre commercial El-Qods、Rue Belouizdad Constantine、Cite Jourdain Oran、Amizour、Bekri Bouguerra Mohammadia）。
3. 每个 wilaya 五遍：① ARPCE+Algerie Telecom+MPT+运营商名；② BOMOP/ANEP+部委/大学/wilaya/市镇招标；③ AAPI/APC/wilaya/市镇许可与合规证；④ Sonelgaz/CREG/变电站/发电机/UPS；⑤ 运营商官方页优先，DCD/APS/Ecofin/目录作线索。
4. 阿拉伯语二次核查（高优先级地点至少一遍）；2019 新 wilaya 检查旧父 wilaya 归属。
5. 状态：inaugure/mis en service/operationnel/Uptime 建成=运营；pose de la premiere pierre/lancement=在建；accord/appel d'offres 中标前=计划；无信号 wilaya 跑负面清单后写 `no_projects: true`（排除位于他处的国家项目）。
6. 输出 world 同 schema；记录设施类型（物理 DC/云服务/服务器房/HPC 集群/遥测中心/DR 站/呼叫平台）。
7. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：codex terra agent（max thinking）每 agent 分批复核阿尔及利亚数据中心（58 wilaya 粒度）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Mohammadia 国家 DC 的运营状态与后续（含 Uptime 建成认证）；Blida 第二个国家 DC 与 DR 招标的场地披露；Oran AI 数据中心（MPT 奠基后）启用进展；Algerie Telecom Constantine 容量；OPGI Djelfa 次级 DC 与 UMMTO HPC/AI 采购落定；Djezzy Cloud/ISSAL/AYRADE 设施的官方地址证实。
