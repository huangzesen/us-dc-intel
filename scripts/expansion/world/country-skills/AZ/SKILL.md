---
name: az-datacenter-methodology
location: scripts/expansion/world/country-skills/AZ/SKILL.md
description: |
  Azerbaijan (AZ) datacenter discovery & audit methodology — how to enumerate, verify, and update Azerbaijan datacenter projects at rayon / municipality / autonomous-republic granularity (from world-manifest.jsonl). Azerbaijan has no public national datacenter permit register: enumeration anchors on ICTA/MINCOM operator registration, Uptime Institute certification lists, state-cloud AzInTelecom pages (Government Cloud; Baku + Yevlakh operating, Absheron/Gobustan and Hajigabul/Pirsaat green DCs under EIB EUR 43m loan), State Committee on Urban Planning / e-construction, e-procurement (etender.gov.az), AzerEnergy/Azerishiq/AERA energy evidence, official cloud-region checks (no hyperscale AZ region — negative context; Cloudflare/Gcore edge leads), and operator pages (Delta Telecom, PASHA Technology, Azerconnect, CBAR, State Customs, STDC Sumgayit, Nakhchivan planned). No conversion of MVA to IT MW without an explicit source; locality vs project-region conflicts (Gobustan vs Absheron, Pirsaat vs Hajigabul) must be recorded both ways. Read this before running AZ exploration/audit batches. Routes to explorer-official.md (regulator/certification/permits/procurement/energy/cloud) and explorer-industry.md (trade press/operators/directories/region query patterns).
---

# AZ · 阿塞拜疆数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：阿塞拜疆**没有**公开的全国数据中心许可注册库；枚举组合 **ICTA 注册、Uptime 认证、国家云/AzInTelecom 页、城市规划许可、电子采购、电网证据与运营商页**。
> 国家云路径异常重要：**AzInTelecom**（国有云与电信基础设施，运营政府云），官方与 IFI 来源点名巴库与叶夫拉赫的现有设施，以及 Absheron 与 Hajigabul 的绿地数据中心（EIB 4300 万欧元贷款，2027 完工）。
> 阿塞拜疆语/英语/俄语（有时土耳其语）都要搜；云区域/AZ 声称只作服务证据；Cloudflare/CDN/IX PoP 只作边缘/网络位置。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供阿塞拜疆探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/认证管线：MINCOM/ICTA 运营商注册表、AzInTelecom 政府云官方页与 EIB 融资页、Uptime Institute 阿塞拜疆国家清单（12 条认证记录）、国家城市规划委员会/e-construction 许可、etender.gov.az 采购、AERA/AzerEnergy/Azerishiq 电网与可持续验证、云/边缘官方核查（无超规模区域）、分层分区枚举（Tier 1/2/3）与别名表、假阳性清单 |
| `explorer-industry.md` | 行业/厂商发现：DCD/Telecompaper/PRNewswire/Lenovo/EIB 国际源、AZERTAC/APA/Trend/AzerNews/Tech.az/Xeberler/FED 本地媒体、目录与网络库（Datacenters.com/DataCenterMap/Cloudscene/Inflect/PeeringDB）、运营商/项目种子表（国家云+商业电信金融）、阿塞拜疆语/俄语查询模式、状态/建设词、逐分区行业工作流、别名表与升级规则 |

## 核心结构事实（框定每次搜索）

1. **Uptime 是最高产的一手邻接源**：阿塞拜疆国家清单含设施名与位置——Azerconnect Baku（Tier IV 设计）、Azerconnect Agdash（Tier III 设计）、AzInTelecom Baku MDC（Tier III 设计+建成）、AzInTelecom Yevlakh RDC（Tier III 设计+建成）、AzInTelecom Baku New Data Protection Center（Tier III 设计+建成）、AzInTelecom Absheron Main DC M1-M5（Uptime 地点写 Gobustan，Tier III 设计）、AzInTelecom Hajigabul Reserve DC M1-M2（Uptime 地点写 Pirsaat，Tier III 设计）、CBAR 巴库主 DC、Delta Telecom DTMDC、PASHA BMDC、PASHA Goychay GDRS、海关委员会 DGK 巴库主 DC（Tier III 设计）。
2. **国家云锚点（A）**：AzInTelecom 在巴库与 Yevlakh 运营政府云设施；EIB Global 4300 万欧元贷款（2027 完工）建两个新绿地 DC——Absheron（主）与 Hajigabul（备用）；AzInTelecom 绿色技术公告确认两个绿地 DC；Sumgayit 化学工业园 STDC/Sumgait Technologies DC（总统/AZERTAC 报道）；Nakhchivan 计划中的自治共和国国有 DC（州计划/招标线索）。
3. **许可地理 = rayon/市镇/自治共和国**：用 e-construction（arxkom.gov.az、e-tikinti.gov.az、birpencere）作验证层；项目事实常先经国家新闻与 IFI 融资浮出，后才有详细许可材料。
4. **四语搜索**：阿塞拜疆语 `data mərkəzi` `verilənlər mərkəzi` `məlumat mərkəzi` `hesablama mərkəzi` `ehtiyat data mərkəzi` `server otağı` `bulud` `Hökumət buludu`；英语 `data center/centre` `colocation` `sovereign cloud` `supercomputer center` `disaster recovery site`；俄语 `дата-центр` `центр обработки данных` `ЦОД` `облачные услуги`；土耳其语拼写变体（data merkezi）。
5. **地点 vs 项目区域冲突**：Absheron 项目（Uptime 地点 Gobustan）、Hajigabul 项目（Uptime 地点 Pirsaat）、Yevlakh 市 vs Yevlakh 区——按来源原话记录并在 notes 中保留两种写法，官方明确归派时才选清单分区。
6. **电网结构**：AERA 垂直一体化；AzerEnergy（国有，110 kV 及以上输电/变电站）；Azerishiq（110 kV 以下配电与供电）；AREA 可再生能源局。容量规则：MVA 不得无源换算 IT MW；两站 4300 万欧元项目融资不得单站独占；LEED/绿色声明只证明可持续意图。
7. **无超规模云区域**：AWS/Azure/GCP/OCI 官方列表无 AZ 区域；云证据多为主权云/政府云/Gcore-AzInCloud 合作/Cloudflare 边缘/CDN/IX/电信托管云；注意 AWS “AZ” 通常指可用区而非阿塞拜疆。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§5 / explorer-industry.md §3）

- 监管注册：`site:mincom.gov.az "{operator}" "hosting provider"`、`site:mincom.gov.az "data mərkəzi"`、`site:mincom.gov.az "Hökumət buludu"`、`site:mincom.gov.az "AzInTelecom" "Yevlakh"`。
- 国家云：`site:azintelecom.az/en "data center" "Baku"`、`site:azintelecom.az/en "Absheron" "data center"`、`site:azintelecom.az/en "Hajigabul" "data center"`、`site:azintelecom.az/en "Government Cloud" "data centers"`、`site:azintelecom.az/en "Pirsaat" OR "Gobustan"`。
- 认证：`site:uptimeinstitute.com/uptime-institute-awards/country/id/AZ Azerbaijan`、`site:uptimeinstitute.com "{operator}" "{division}"`、`site:uptimeinstitute.com "{facility name}"`。
- 许可/采购：`site:arxkom.gov.az "data mərkəzi"`、`site:arxkom.gov.az "AzInTelecom"`、`site:e-tikinti.gov.az "data mərkəzi"`、`"{division}" "data center" "construction permit" Azerbaijan`、`site:etender.gov.az "data mərkəzi"`、`site:etender.gov.az "Naxçıvan" "data mərkəzi"`、`site:etender.gov.az "server otağı"`。
- 电网/可持续：`site:azerenerji.gov.az "data mərkəzi"`、`site:azerishiq.az "AzInTelecom"`、`site:regulator.gov.az "data mərkəzi"`、`site:area.gov.az "AzInTelecom"`、`"{facility}" "MW" Azerbaijan`、`"{division}" "yarımstansiya" "data mərkəzi"`、`"{operator}" "LEED" "data center" Azerbaijan`。
- 云/边缘：`"Azerbaijan" "AWS Region" site:aws.amazon.com`、`"Baku" "Cloudflare" "data center" site:cloudflare.com`、`"AzInTelecom" "Gcore" "sovereign cloud"`、`"Lenovo" "AzInTelecom" "Supercomputer Center"`。
- 行业/状态：`site:azertag.az "data mərkəzi"`、`site:en.apa.az "Azerbaijan" "data center"`、`site:trend.az "AzInTelecom" "data centers"`、`site:datacenterdynamics.com Azerbaijan data center AzInTelecom`、`"{az}" "data mərkəzi" "tikiləcək"`、`"{az}" "data mərkəzi" "istismara verilib"`、`"{az}" "data mərkəzi" "açılış"`、`"{az}" "data mərkəzi" "MW" OR "MVA"`。

## 官方/监管管线要点（详见 explorer-official.md）

- MINCOM/ICTA：注册运营商/提供商列表（A=实体授权，C=设施，除非配设施证据）；运营商类型含 operator/internet provider/hosting provider；把每个法人 pivot 到 Uptime/官方页/采购/建筑门户/本地新闻。
- AzInTelecom 政府云：官方新闻/页面 + EIB 融资页 + 绿色技术公告；提取设施名、分区/聚落、状态、完工年、运营商、认证、可持续属性；无容量披露时不推断 MW。
- Uptime：A=认证存在/设施名/运营商/城市；设计级认证**不证明运营**，须运营方/建成设施证书/新闻/许可/调试源确认；城市/聚落与行政分区命名可能冲突（记录两种）。
- 城市规划与许可：国家城市规划委员会/电子施工门户为验证层；大 DC 同时查区行政当局、工业园页、环境/能源文件。
- 采购：etender.gov.az；中标/招标文件=A 采购事件与买方；单独招标对最终设施存在=B/C，须中标+调试跟进。
- 电网：AERA/AzerEnergy/Azerishiq/AREA；提取合同电力需求、变电站名、MVA/MW、备用发电机数、太阳能/可再生组件、自然冷却/水效措辞；确认证据属于 DC 本身而非附近基础设施项目。
- 云/边缘：无 AWS/Azure/GCP/OCI AZ 区域（负面对照）；Cloudflare 巴库=边缘 PoP（除非已知宿主设施）；Gcore/AzInCloud=主权云服务证据（pivot 到 AzInTelecom 设施）；Lenovo/AzInTelecom 超级计算机中心（官方供应商证据，确认地址后再定是否独立设施）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 国际媒体：DCD（B，EIB 绿地 DC/Gcore 主权云/巴库历史）、Telecompaper（B，Yevlakh 旧闻）、PRNewswire/Gcore（A/B，主权云合作）、Lenovo 新闻室（A）、EIB 新闻（A，融资与时间线）。
- 本地媒体：AZERTAC（B+/A-，总统视察/工业园/AzInTelecom/超级计算机/Sumgayit 官方仪式）、APA（B+，独家建设/时间线：Absheron 2027、Hajigabul 2029）、Trend（B）、AzerNews（B，复述官方）、Tech.az（B/C+）、Xeberler.az/FED.az（B/C+，Nakhchivan 招标线索）。
- 目录/网络库（C/B- 线索）：Datacenters.com、DataCenterMap（巴库）、Data Center Catalog、Cloudscene、Inflect、PeeringDB；注意 Delta Telecom 地址冲突（241 Abbas Mirza Sharifzadeh vs 69 Muzaffar Hasanov）用官方页/Uptime/网络库裁决；PeeringDB 证明互联存在，不证明施工状态/MW/是否专用建筑。
- 运营商/项目种子：AzInTelecom 系列（Baku MDC 700 sqm、Yevlakh RDC、New Data Protection Center、Absheron M1-M5、Hajigabul M1-M2）、CBAR、海关 DGK、Delta DTMDC/DataCenter.az、PASHA BMDC/GDRS、Azerconnect Baku（Tier IV，2000 kW 承包商证据需确认）/Agdash、STDC Sumgayit、AzerTelecom/Azerfon（PeeringDB 线索 C/B）、Aztelekom/Baktelecom（C/B）、Azercell/Bakcell（C/B，多为网络核心）。
- 状态词：`tikiləcək`=将建、`tikintisi`=在建、`istismara verilib`=已投运、`açılış`=开业、`layihə`=项目、`tender`=招标；升级条件：Uptime 认证 / 官方运营商页 / MINCOM 注册+独立设施页 / 国家-IFI-采购-施工源 / 具名运营商-设施-地点-状态的强贸易文章。
- 假阳性：通用开放数据/统计门户；Online Azerbaijan 宽带扩张；解放区智慧村/智慧城市/电信恢复（无物理计算设施）；CDN/Cloudflare/Gcore 边缘服务声称（无宿主设施）；银行/政府 server otağı 现代化（未描述为数据中心）；AWS/Azure 上下文中的 “AZ”（可用区，不是阿塞拜疆）。

## 来源分级

- **A** = 官方/一手：MINCOM/ICTA 注册、Uptime 认证清单、AzInTelecom 官方页、EIB/IFI 融资页、总统/内阁/国有企业公告、城市规划/e-construction 记录、etender 中标、AzerEnergy/Azerishiq/AERA、官方云区域页。
- **B** = 强二级：AZERTAC/APA/Trend/AzerNews/DCD/Telecompaper 引述具名官员/运营商或复述官方项目事实；厂商案例。
- **C** = 弱线索：目录、市场页、仅 PeeringDB/IX、博客、社交、无设施级证据的市场报告。
- 容量规则：MVA→IT MW 无源不换算；两站合并融资不单站独占；LEED/绿色只证可持续意图。
- 去重/归派：Uptime 地点（Gobustan/Pirsaat）与项目区域（Absheron/Hajigabul）冲突时双记录；Yevlakh 市与 Yevlakh 区分开；设施别名（MDC/BMDC/DTMDC/DGK/CBAR/GDRS/RDC）统一到同一 facility id。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=AZ，divisions=rayon/市镇/自治共和国）。
2. 建种子：Uptime 国家清单 12 条 + AzInTelecom 官方设施页 + MINCOM 注册表运营商名 + 已知地址词（Alibey Huseynzadeh、Sharifzadeh、Alatava、Heydar Aliyev ave、Azadlyg Ave、Tbilisi Prospekti）。
3. 分区分层：Tier 1 穷尽扫（Baku、Yevlakh City、Absheron、Gobustan、Hajigabul、Goychay、Agdash、Sumgayit、Nakhchivan）跑 MINCOM/Uptime/AzInTelecom/e-construction/能源/采购/官方运营商；Tier 2 州基础设施/区域验证（Ganja、Mingachevir、Shirvan、Lankaran、Shaki、解放区等，多数无项目）；Tier 3 其余 rayon 负面对照（四语别名 + 国家运营商/认证核查，无信号写 `no_projects: true`）。
4. 每个候选：认证扫 → 监管/实体扫 → 国家云扫 → 许可/采购/能源扫 → 行政归派（地点 vs 项目区域，双记录）。
5. 状态：Uptime 建成设施/istismara verilib/开业=运营；tikintisi/施工=在建；tikiləcək/设计级认证/融资宣布=计划/已批准；目录/媒体仅线索。
6. 输出 world 同 schema；容量按原单位记录；标注设施类型（商业 colo/企业/政府 DC、DR 站、边缘 PoP、HPC/超算中心、服务器房）。
7. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：codex terra agent（max thinking）每 agent 分批复核阿塞拜疆数据中心（rayon/市镇粒度）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Absheron（Gobustan）M1-M5 与 Hajigabul（Pirsaat）M1-M2 的施工/投运进度与 EIB 2027 时间线；Azerconnect Baku Tier IV 与 Agdash Tier III 的运营状态与 2000 kW；STDC Sumgayit 的运营商与设施性质；Nakhchivan 州计划是否进入招标/许可；Delta Telecom 地址裁决（Sharifzadeh vs Hasanov）。
