---
name: mu-datacenter-methodology
location: scripts/expansion/world/country-skills/MU/SKILL.md
description: |
  Mauritius (MU) datacenter discovery & audit methodology — how to enumerate, verify, and update Mauritius datacentre projects at division granularity (12 manifest divisions: 9 mainland districts + Agalega, Cargados Carajos Shoals, Rodrigues). Small telecom/conglomerate-led market with real colocation/government-DC density in Port Louis, Ebene/Reduit (Moka), Arsenal/Terre Rouge (Pamplemousses), Rose-Belle (Grand Port), and Plaines Wilhems. Enumeration joins Building and Land Use Permit (BLUP) planning records, ICTA licences (pivots, not facility registers), certification registries (EPI/TIA Emtel Rated 3; Uptime MT Rose Belle Tier IV design+constructed, Bhumishq Tier IV design), MITCI/Government Online Centre (state DC, 80 racks) and sovereign-cloud procurement, CEB/URA energy records, cable/IXP chain (METISS lands at Emtel Arsenal DC), and operator pages. No hyperscaler public cloud region. Read this before running MU exploration/audit batches. Routes to explorer-official.md (planning/regulator/certification/government/energy/cable/cloud) and explorer-industry.md (operator sweep/sources/directory-to-primary workflow/division recipes).
---

# MU · 毛里求斯数据中心查询方法论（Datacentre Discovery & Audit Methodology）

> 目的：毛里求斯市场小且由电信/集团主导；公开数据中心证据集中于 **Port Louis、Ebene/Reduit（Moka）、Arsenal/Terre Rouge（Pamplemousses）、Rose-Belle（Grand Port）与 Plaines Wilhems**；目录的宽泛市场标签不可用于分区归属。
> 分区模型：**12 个 manifest 分区**（9 主岛区 + Agalega、Cargados Carajos Shoals/Saint Brandon、Rodrigues）；本地政府门户仅暴露主岛市镇/区议会。
> 认证基线（已修正草稿错误）：**Uptime 确实列出毛里求斯条目**——MT Rose Belle Tier IV Design+Constructed、Bhumishq Cybercity Tier IV Design；Emtel 为 ANSI/TIA-942-B Facility Rated 3（证书 TIA942MU230924001，2026-09-23 到期）。
> 无 AWS/Azure/GCP/OCI 公共云区域（官方页负面）；海缆登陆点≠数据中心（唯一例外：METISS 经 Emtel Arsenal DC 登陆）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供毛里求斯探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：规划与地方政府（la.govmu.org BLUP/Outline Planning Permission、Gazette/公告）、ICTA 牌照（B.01/B.02/C.02-C.08 清单）、认证注册库（EPI/TIA/Uptime）、MITCI/GOC/主权云 RFI、CEB/URA 能源与环境、海缆/IXP 链（SAFE/LION/MARS/T3/METISS/T4/MIXP）、超规模缺席核查、12 分区官方策略与种子表 |
| `explorer-industry.md` | 行业/厂商发现：优先运营商扫（Emtel/MT RBDC/RHDC/Bhumishq/Rogers/Harel Mallac/BIRGER/Aphelion/GOC）、行业来源表（EPI/TIA/Uptime/运营商页/本地媒体）、目录到一手工作流、12 分区配方、种子记录验证表、容量与可靠性规则 |

## 核心结构事实（框定每次搜索）

1. **认证是骨干且已修正**：Emtel Data Centre（Arsenal，B11 Plaine des Papayes Road，Pamplemousses）EPI/TIA ANSI/TIA-942-B Facility Rated 3、证书 TIA942MU230924001、2026-09-23 到期（A）；MT Rose Belle Data Centre/RBDC（Rose-Belle，Grand Port）Uptime Tier IV Design+Constructed（A），MT 页称 1,500 sq m 安全机架空间/400+ 机架/3 MW；Bhumishq Cybercity DC（Ebene，Moka）Uptime Tier IV Design（A，设计≠建成）。
2. **GOC 是 A 级国家数据中心**：Government Online Centre（Port Louis），MITCI 页称 2005-05 起集中政府 DC、80 机架、g-Cloud、托管与服务器 co-location（A）；主权云 + 灾备站点为采购管线（MITCI/RFI/01/2025-26，A 政策/采购，地点 null）。
3. **分区归属以物理位置为准**：Ebene/Reduit/Cybercity=Moka；Arsenal/Terre Rouge/Riche Terre/JinFei=Pamplemousses；Rose-Belle/Gros Billot=Grand Port；Rose Hill/Candos/Quatre Bornes=Plaines Wilhems；Edith Cavell/Mere Barthelemy/GOC 中心=Port Louis；Baie Jacotet/Bel Ombre 海缆站=Savanne；勿因目录市场标签把 Terre Rouge/Aphelion 归 Port Louis。
4. **ICTA 牌照是 pivot 不是注册库**：Network Infrastructure Provider=MultiCarrier；B.01/B.02/C.02/C.03/C.04/C.08 覆盖 Emtel/MT/Cellplus/Rogers Capital/CEB Fibernet/Kaldera 等；证明电信授权而非设施存在；无专门 DC 牌照类别。
5. **海缆链**：SAFE（MT 传统）、LION/LION2（Emtel 直达声称）、MARS（Baie Jacotet→Grand Baie/Rodrigues）、T3（Baie Jacotet 2023-03-24 登陆）、METISS（Emtel Arsenal DC 登陆点，DC 关联唯一）、T4（MT 计划替代 SAFE，管线）、MIXP（IXP，Ebene DC 托管 + GOC 节点，PeeringDB ix/1508）——除 METISS 外均连接资产。
6. **能源/环境**：CEB、CEB Fibernet、URA、能源部/EEMO、环境部；Emtel 官方页为最强电源细节源（双 1 MW 变压器 + N+1 发电机——是运营商声称，非 IT load）。
7. **容量纪律**：Tier/评级、变压器容量、机架数（无功率声明）、海缆带宽/capex、市场预测、营销词（hyperscale/world-class/sovereign）一律不得推导容量；`capacity_mw: null` 加源标注。
8. **无超规模区域**：转售/伙伴/CDN/本地 zone/edge/VPS/市场页不构成区域证据；每次运行核查官方页。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§2 / explorer-industry.md §1-§4）

- 规划：`site:la.govmu.org "data centre" OR "data center" OR datacentre OR "server room" OR telecom`、`"Building and Land Use Permit" Mauritius "data centre" OR "server room" OR "telecom"`、`"Ebene" OR "Cybercity" OR "Rose-Belle" OR Arsenal OR "Quatre Bornes" "Building and Land Use Permit"`。
- 监管：`site:icta.mu "data centre" OR "data center" OR hosting OR "sovereign cloud"`、`site:icta.mu "Emtel" OR "Mauritius Telecom" OR "Rogers Capital"`、`site:icta.mu "Network Infrastructure Provider" "MultiCarrier"`。
- 认证：`site:epi-certification.com Mauritius`、`site:tiaonline.org/942-datacenter/emtel-data-centre/`、`site:uptimeinstitute.com/uptime-institute-awards/country/id/MU Mauritius`。
- 政府：`site:mitci.govmu.org/mitci "Government Online Centre" "data centre"`、`site:publicprocurement.govmu.org "MITCI/RFI/01/2025-26" OR "Sovereign Cloud"`、`site:edbmauritius.org "data centre" OR ICT`。
- 能源/海缆：`site:ceb.mu "data centre" OR substation OR MVA OR kVA`、`"METISS" Emtel "data centre" Arsenal Mauritius`、`"Baie Jacotet" Mauritius T3 OR SAFE OR MARS "landing"`、`"MIXP" Mauritius Ebene "Government Online Centre"`。
- 运营商：`"Emtel" "data centre" Arsenal "TIA942MU230924001" OR "Rated 3"`、`"Rose Belle Data Centre" OR RBDC Mauritius Telecom "3 MW" OR "400 racks"`、`"Rogers Capital" "data centre" Ebene OR "La Tour Koenig" OR MIXP`、`"Government Online Centre" Mauritius "80-rack"`。
- 分区通用：`"{division}" Mauritius "data centre" OR "data center" OR datacentre OR "server room" OR colocation`、`site:lexpress.mu "{division}" "data centre" OR telecom`、`"{division}" "centre de donnees" OR "salle de serveurs"`。

## 官方/监管管线要点（详见 explorer-official.md）

- 规划：BLUP/Outline Planning Permission 由地方当局按 Local Government Act 2011 裁定；公共访问可能需议会查询/采购记录/Gazette 公告/FOI；提取申请号/法人/地块/分区/用途/面积/发电与冷却/决定状态。
- ICTA：牌照列表作 pivot；无 DC 牌照类别；许可决定规则=证明授权不证明设施。
- 认证注册库：EPI/TIA（Emtel Rated 3）、Uptime（MT Rose Belle 与 Bhumishq）；记录认证机构/类型/Tier/证书 ID/颁发与到期/注册库 URL。
- 政府：MITCI（GOC A + Blueprint 管线）、CIB、NCB、DPO、公共采购门户、EDB ICT 板块。
- 能源：CEB/CEB Fibernet/URA/EEMO/环境部作佐证；纯电力基础设施不建 DC 记录。
- 海缆：按表逐项处理（见核心事实 5）；超规模缺席每批次核查官方页。
- 决策规则：认证类型决定一切（design≠constructed）；未知容量保持 null；线索无法验证时降级保留并注明缺失证据，**不得删除**。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 优先运营商扫：Emtel（A 地址/证书/服务）、MT Rose Belle/RBDC（A 容量页+Uptime）、MT Rose Hill Tier III/RHDC（A MT 声称/C 目录细节）、Bhumishq（A Uptime 设计/C 地址）、Rogers Capital Ebene DC（A/B，MIXP 托管）、La Tour Koenig/Port Louis/Les Cascades（A/C，BLUP 待补）、Harel Mallac/MCS Datacenter 02（B/C）、BIRGER Candos（C/B）、Aphelion DC3（C，勿归 Port Louis）、GOC（A）。
- 媒体：Telecom Review Africa（B）、DCD（B）、Submarine Networks（B/A）、TeleGeography（B）、L'Express/Le Mauricien/Defi Media（B）；目录（C）：DataCenterMap、DataCenterPlatform、ColocationM、UPSTACK、ColoMap、DC Hub、Baxtel、Cloudscene。
- 目录到一手工作流：目录种子→匹配主域（emtel.com/myt.mu/rbdc.mu/technology.rogerscapital.mu/birger.technology/hmtechnologies.mu/icta.mu/mitci.govmu.org/epi-certification.com/tiaonline.org/uptimeinstitute.com）→按物理位置分区→A 级仅当一手证据证明同一设施/主张→未决线索降级保留。
- 容量规则（见核心事实 7）；负面控制查询（`"Mauritius" "AWS region" OR "Azure region"...`、Starlink/2Africa/Equiano/LION3 landing 假阳性）。

## 已知设施/项目与证据状态

| 设施/项目 | 分区 | 状态与证据 |
|---|---|---|
| Emtel Data Centre | Pamplemousses（Arsenal） | 运营（A EPI/TIA Rated 3 + 官方页 + METISS）；双 1 MW 变压器为声称 |
| MT Rose Belle Data Centre / RBDC | Grand Port | 运营（A Uptime Tier IV design+constructed + MT 页 1,500 sq m/400+ 机架/3 MW） |
| MT Rose Hill Tier III / RHDC | Plaines Wilhems | 运营/线索（A MT 声称；C 目录细节） |
| Bhumishq Cybercity Data Centre | Moka（Ebene） | 运营待验（A Uptime Tier IV design；C 地址/500 sq m） |
| Rogers Capital Ebene DC（MIXP 托管） | Moka | 运营（A/B Rogers 官方页+MIXP） |
| Rogers Capital La Tour Koenig / Port Louis / Les Cascades | Port Louis（待验边界） | A 运营商声称/C 目录细节；BLUP 待补 |
| Harel Mallac / MCS Datacenter 02 | Port Louis | B/C（公司身份有源，设施多为目录/媒体） |
| BIRGER Candos Recovery Centre | Plaines Wilhems | C/B；BIRGER 官方页只证公司 |
| Aphelion DC3 | Pamplemousses（Terre Rouge） | C；勿按目录归 Port Louis |
| Government Online Centre | Port Louis | 运营国家 DC（A MITCI，80 机架） |
| 新政府 DC + 主权云 + 灾备站 | 待定 | 计划/采购（A 政策/采购；地点 null） |
| CEB 灾备中心 | 待定 | B 线索（内部需求，非公共 colo） |

## 更新节奏

- 每批次：超规模官方区域核查、Emtel TIA 证书到期（2026-09-23）、GOC/主权云 RFI 进展、MT RBDC/RHDC 官方页、Rogers 各址 BLUP/一手页、Aphelion/BIRGER 设施页。
- 季度：12 分区负面扫回顾、新海缆（T4 替代 SAFE）登陆点、MIXP 节点变化、EDB Blueprint 更新。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（12 分区粒度）；本 skill 作为国家层参考注入。
