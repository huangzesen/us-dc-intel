---
name: mg-datacenter-methodology
location: scripts/expansion/world/country-skills/MG/SKILL.md
description: |
  Madagascar（MG）数据中心发现以官方/监管管线（ARTEC 电信监管与许可证、数字部 MNDPT/UGD 与世行 PRODIGY P169413 项目、JIRAMA 电力证据、EDBM/ORINASA 投资促进、ONE 环境审批与 Ivotoro 建设许可流程、ARMP 公共采购、公有云区域官方页）和行业/厂商发现（STELLARIX TNR1/TNR2、MGIX/PeeringDB、Telma/Yas、Orange、Airtel、Gulfsat、Starlink、海缆 LION/LION2/2Africa/METISS、目录聚合器）为主线，按 6 个省（Antananarivo; Antsiranana; Fianarantsoa; Mahajanga; Toamasina; Toliara）逐省枚举。
  商业市场极小且集中在 Antananarivo 省：唯一明确的商业 DC 运营商为 STELLARIX（TNR1 Analakely 与 TNR2 Galaxy Andraharo 两个站点）；法语为官方与商业主力语言；海缆登陆站（Toamasina/Mahajanga/Fort Dauphin）为连通性设施而非数据中心，须有托管/计算证据才计数。
---

# MG · 马达加斯加数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：按 6 个省（Antananarivo; Antsiranana; Fianarantsoa; Mahajanga; Toamasina; Toliara）枚举马达加斯加数据中心设施与项目。
> 分区模型：法理一级单元为 6 省（ISO 3166-2:MG），实际使用 24 大区作搜索辅助；已建省→大区映射表用于搜索，输出分区必须是 6 省之一。
> 已知种子：STELLARIX（TNR1 Analakely、TNR2 Galaxy Andraharo）、MGIX/Bâtiment Sirius、Telma/Yas NOC 与灾备中心（历史）、PRODIGY 政府计算/采购、LION/LION2（Toamasina）、2Africa（Mahajanga）、METISS（Fort Dauphin）、Starlink 卫星 ISP。
> 本 skill 汇总两份探索报告：官方/监管管线见 explorer-official.md，行业/厂商发现见 explorer-industry.md。

## 入口

| 文件 | 管线 |
|---|---|
| explorer-official.md | 官方/监管管线：国家基线（24 大区/6 省映射、无公共 DC 登记册与 DC 专项许可证）、检索词（法语/英语/马拉加斯语）、ARTEC 电信监管、数字部 MNDPT/UGD/PRODIGY（世行 P169413）、数据保护与数据驻留语境（2014-038 法）、JIRAMA 电力证据、EDBM/ORINASA 投资促进、规划/建设许可/环境（ONE、Ivotoro）、公共采购（ARMP）、公有云区域核对、省覆盖工作流、设施/项目种子表、决策规则、刷新节奏 |
| explorer-industry.md | 行业/厂商发现：市场形态与已核实事实（ISOC Pulse 1 DC/1 IXP、STELLARIX 两站点、MGIX、海缆）、检索词（法语优先）、优先运营商扫掠（STELLARIX、Telma/Yas/AXIAN、Orange、Airtel、Gulfsat、Starlink、UGD/PRODIGY、银行/矿业企业 IT）、连通性枢纽（IXP 与 peering、海缆、卫星/LEO/VSAT）、行业/媒体/目录源图（PeeringDB、ISOC、DataCenterMap、Uptime、TIA/EPI、DCD、Connecting Africa、Submarine Networks、GOTICOM、NIC.MG）、省配方、待验证种子记录、容量/认证/状态抽取、陷阱与决策规则、刷新节奏 |

## 核心结构事实（框定每次搜索）

1. 商业市场极小且集中在 Antananarivo 省：ISOC Pulse 报 1 个活跃 DC 与 1 个 IXP（B 级市场指标，非穷尽设施登记册）；STELLARIX 官方页列出两个 Antananarivo 数据中心 TNR1（Analakely, Lalana Paul Dussac, Antananarivo 101）与 TNR2（Galaxy Andraharo, Building KUBE D 2 层, BP 763 Antananarivo 101），A 级仅证运营商设施/地址声明。
2. 无公共国家数据中心登记册、无数据中心专项许可类别：枚举必须三角化电信许可（ARTEC）、运营商页、规划/环境记录（ONE/Ivotoro）、能源接入证据（JIRAMA）、公共采购（ARMP/UGD）、海缆/IXP 记录与认证/目录。
3. 海缆登陆站不是数据中心：LION/LION2 在 Toamasina、2Africa 在 Mahajanga（勿误归 Toamasina）、METISS 在 Fort Dauphin/Taolagnaro，均为连通性设施，除非有托管/机柜/云/数据中心设施证据；Africa-1 无落地证据为 U/C 线索，EASSy/SEACOM 无 MG 落地。
4. 「Tier III ready」仅为运营商声明：STELLARIX 的 Uptime 搜索只命中 Tanzania 站点，TIA/EPI 未发现 MG 证书；认证状态标 U，须以登记册证据为准。
5. 法语是政府、电信与本地新闻的主力语言（centre de données / hébergement / colocation / salle serveur / station d'atterrissement / appel d'offres）；英语用于海缆/云/贸易媒体/国际目录；马拉加斯语（foibe data 等）仅低收益发现层。
6. 能源是主要选址约束：JIRAMA 生产低效、损耗、低于成本电价与低接入率（IMF 佐证）；电力证据仅作大型 DC 负载的佐证（专用馈线、变压器容量、发电机/燃油许可、UPS/冷却采购、命名企业电价），不得仅凭停电文章提升设施。
7. 分级按所支持事实：A 官方/一手（政府/监管/法律、SOE/公用事业、世行项目记录、运营商自有设施页、云官方区域清单、认证登记册）；B 可靠媒体/贸易源；C 目录/市场/自报 PeeringDB/搜索片段；U 未决线索，不得提升为设施记录。

## 查询模式（复制粘贴模板见 explorer-official.md §2/§3 / explorer-industry.md §2/§5）

- 监管（ARTEC）：`site:artec.mg ("centre de données" OR datacenter OR "data center" OR cloud OR hébergement OR IXP)`、`site:artec.mg (Starlink OR satellite OR "licence satellite" OR "régime de déclaration")`、`site:artec.mg (Telma OR Yas OR Orange OR Airtel OR Gulfsat OR STELLARIX)`、`"decision n°2024/02-ARTEC/DG/L" Starlink Madagascar`。
- 数字部/UGD/PRODIGY：`site:digital.gov.mg ("centre de données" OR datacenter OR hébergement OR serveur OR "infrastructure virtuelle")`、`site:mndpt.gov.mg ("centre de données" OR cloud OR souveraineté OR "stratégie numérique")`、`"P169413" Madagascar (server OR cloud OR data center OR infrastructure OR hosting)`、`"Madagascar" "centre de données national" OR "sovereign cloud"`。
- 能源（JIRAMA）：`site:jirama.mg ("centre de données" OR datacenter OR serveur OR "raccordement")`、`site:jirama.mg (STELLARIX OR Telma OR Yas OR Orange OR Galaxy OR Andraharo)`、`"délestage" Madagascar (STELLARIX OR Telma OR "centre de données")`、`"Antananarivo" "groupe électrogène" "data center" OR datacenter`。
- 投资/公司（EDBM/ORINASA）：`site:edbm.mg (datacenter OR "data center" OR cloud OR ICT OR BPO)`、`site:orinasa.edbm.mg (STELLARIX OR "Telma" OR "Yas")`、`"Choose Digital Madagascar" (datacenter OR cloud OR infrastructure OR hébergement)`。
- 规划/环境：`site:pnae.mg ("centre de données" OR datacenter OR télécommunications OR fibre)`、`"permis de construire" Madagascar (datacenter OR "salle serveur")`、`"Galaxy Andraharo" permis construire OR EIE OR JIRAMA`、`"Lalana Paul Dussac" permis construire OR EIE OR STELLARIX`。
- 采购（ARMP/UGD）：`site:armp.mg ("centre de données" OR datacenter OR hébergement OR serveurs OR cloud OR "infrastructure virtuelle")`、`site:digital.gov.mg ("appel d'offres" OR DAOI) (serveur OR cloud OR hébergement)`、`"appel d'offres" Madagascar PRODIGY serveur OR infrastructure OR cloud`。
- 运营商：`site:stellar-ix.com Madagascar TNR1 OR TNR2 OR Analakely OR Galaxy OR Andraharo`、`"TNR1" "Antananarivo" STELLARIX OR Stellar-IX`、`"Bâtiment Sirius" MGIX OR "Zone Galaxy"`、`"Telma" OR "Yas" Madagascar ("disaster recovery" OR NOC OR datacenter)`、`site:orange.mg Madagascar (hébergement OR cloud OR "centre de données")`。
- 海缆：`"LION" "LION2" Madagascar Toamasina "cable landing station"`、`"2Africa" Madagascar Mahajanga Telma Vodafone landing`、`"METISS" Madagascar "Fort Dauphin" OR Taolagnaro`、`"Africa-1" Madagascar "landing station"`。
- 省配方（官方 §3 / 行业 §5）：`"{province}" OR "{anchor city}" Madagascar ("centre de données" OR datacenter OR hébergement OR colocation OR serveur)`、`site:artec.mg "{anchor city}" OR "{operator}"`、`site:armp.mg "{anchor city}" (serveur OR hébergement OR cloud)`、`site:pnae.mg "{anchor city}" (EIE OR fibre OR datacenter)`、`site:jirama.mg "{anchor city}" (raccordement OR délestage)`。
- 认证：`site:uptimeinstitute.com/uptime-institute-awards Madagascar STELLARIX OR Antananarivo`、`site:tiaonline.org/942-datacenter Madagascar OR STELLARIX`、`site:epi-certification.com/sites Madagascar OR STELLARIX`。

## 官方/监管管线要点（详见 explorer-official.md）

- ARTEC 电信与 ICT 监管：官方页 artec.mg、2005-023 法 PDF、声明/许可制度页（régime de déclaration / régime libre / délivrance de licence）；2024 年报确认 2024-04-29 向 Starlink Madagascar 发卫星许可（A 证许可证事实，2424.mg 补五年期与 10 万欧元初始费为 B）；ARTEC 非设施登记册。
- 数字部 MNDPT（mndpt.gov.mg）与数字治理单位 UGD（digital.gov.mg）：世行 PRODIGY/数字治理与身份管理系统项目 P169413（1.4 亿美元 IDA 信贷）；UGD 发布生物识别、虚拟基础设施、服务器、连通性与防断电设备招标（A 证项目/招标存在，不得仅凭招标推断国家政府 DC）。
- 数据保护：2014-038 号个人数据法（digital.gov.mg 托管文本），仅作需求/监管语境；尚未发现运作中的监管机构、登记清单或数据驻留规则，若后续发现再补充。
- JIRAMA 电力：jirama.mg 生产/输配/供水；IMF 指出生产低效、损耗、低于成本电价与低接入率；电力证据作大型负载佐证。
- 投资促进：EDBM（edbm.mg）一站式投资机构、ORINASA 公司设立、2025-02 启动 Choose Digital Madagascar；仅当命名 DC 项目或投资者场地才算设施记录。
- 规划/环境：ONE（pnae.mg）EIE 环境权威；Ivotoro 描述建设许可流程（向市镇申请、SRAT 转介、>1000 平米项目由土地利用/规划主管部委处理）；无全国可检索建设许可库，A 级仅当官方文件命名申请人/地块/项目。
- 采购：ARMP（armp.mg）、UGD 招标、e-GP 平台推广；搜索服务器机房、托管、政府云、虚拟基础设施、身份系统硬件、民改现代化、备用电源套件、部委灾备。
- 公有云：AWS/Azure/GCP/OCI 官方清单 2026-08-12 均无 MG 区域/本地区（A 级仅证清单检查）；每次刷新复查。

## 行业/厂商发现要点（详见 explorer-industry.md）

- STELLARIX 是主要商业目标：官方页自称非洲数据托管与基础设施管理公司，提供托管、云、虚拟化与互连；TNR1/TNR2 两个不同 Antananarivo 地址，无证据证明同一物理站点前保持分开；DataCenterMap 的 TNR01（Immeuble Tanashore/Enceinte Futura）与 PeeringDB 的 Bâtiment Sirius/Zone Galaxy 均为地址线索，需运营商/地块证据调和。
- MGIX（Madagascar Global Internet eXchange）为国家 IXP，位于 Antananarivo Zone Galaxy Andraharo/Bâtiment Sirius（PeeringDB org 14435/fac 2993，C/A-by-source）；ISOC Foundation 2024-07 至 2026-06 向 iRENALA 提供 Restart MGIX 赠款（现代化线索，非 DC 记录）；勿自动与 STELLARIX 合并。
- Telma/Yas（AXIAN 系）：2011 年公司 PDF 声明 Antananarivo NOC 与灾备中心（A 历史声明，当前状态 U）；DCD 报道 Axian 融资为 B；当前设施状态需新运营商证明。
- Orange/Airtel/Gulfsat/Starlink：运营商存在/服务 A，无设施页前 MG DC 为 U；Gulfsat VSAT 头端、Starlink 地面网关均需命名场地/许可/建设/运营商声明。
- 连通性：2Africa 2023-02 在 Mahajanga 由 Telma/Vodafone 团队落地（B），核心系统在多数登陆国就绪（A/B）；LION 2010-03 RFS 连接 MG/Reunion/Mauritius、LION2 延至 Mayotte/Kenya；METISS 2021-03 起服役；非洲-1 无 MG 运营落地证据。
- 目录/市场源仅发现用：DataCenterMap、OCOLO、Inflect、datacenters.com（C）；PeeringDB 自报（C/A-by-source）；ISOC Pulse 为市场基线（B）；Uptime/TIA/EPI 为认证核对（A 当有证书）。
- 企业 IT 需求：银行/矿业（Ambatovy、QMM）机房为需求/企业 IT 线索（C/U），除非提供第三方托管或命名 DR/DC 站点。

## 已知设施/项目与证据状态

| 设施/项目 | 分区 | 状态与证据 |
|---|---|---|
| STELLARIX TNR1 Analakely | Antananarivo（Lalana Paul Dussac, Antananarivo 101） | 运营商确认线索/可能运营中；A（stellar-ix.com about 页证设施/地址）；地块、电力、认证、当前商业可用性需另行核实 |
| STELLARIX TNR2 Galaxy | Antananarivo（Galaxy Andraharo, KUBE D 2 层, BP 763） | 运营商确认线索/可能运营中；A（运营商页）；与 PeeringDB Galaxy/Andraharo、DataCenterMap/OCOLO C 级交叉核对 |
| MGIX / Bâtiment Sirius | Antananarivo（Zone Galaxy Andraharo） | 活跃 IXP/互连设施；B/C（ISOC Pulse、PeeringDB、ISOC Foundation 赠款）；有托管/机柜/数据厅证据才计为 DC |
| Telma/Yas NOC 与灾备中心 | Antananarivo | 历史线索，当前状态未决；A（2011 年 PDF 历史声明），当前 U |
| PRODIGY 政府计算/采购 | Antananarivo 为主，各省试点 | 项目/招标线索；A（digital.gov.mg、世行 P169413）；来源命名托管站点/地址前不建设施记录 |
| LION/LION2 登陆站 | Toamasina | 连通性站点；A/B（海缆事实）；CLS 非 DC |
| 2Africa 登陆站 | Mahajanga（勿归 Toamasina） | 连通性站点；B（MG 落地事实）、A/B（官方系统状态）；CLS 非 DC |
| METISS 登陆站 | Toliara（Fort Dauphin/Taolagnaro） | 连通性站点；B；确认本地 CLS 与运营商 |
| Starlink Madagascar | 全国 | 已许可卫星 ISP；A/B（ARTEC 2024 年报、2424.mg/Ecofin）；无地面网关/DC 证据 |
| Orange/Airtel/Gulfsat 企业/网络站点 | 多为 Antananarivo | 运营商线索；A（运营商存在），U（DC 证据） |
| AWS/Azure/GCP/OCI 公有云区域 | 无 | 官方清单无 MG 区域/本地区；A（仅证清单检查） |

## 更新节奏

- 季度：STELLARIX 站点与招聘、PeeringDB MGIX/设施记录、ISOC Pulse MG 报告与 IXP 追踪、ARTEC 许可/新闻 PDF、UGD/PRODIGY 招标、ARMP 搜索、2Africa/LION/LION2/METISS/Africa-1 海缆状态、本地媒体 JIRAMA 停电（Antananarivo/Mahajanga/Toamasina/Taolagnaro）。
- 半年：AWS/Azure/GCP/OCI 官方区域清单、Uptime 奖励、TIA/EPI 清单、DataCenterMap/OCOLO/Inflect/datacenters.com、EDBM/Choose Digital Madagascar 发布、Yas/Telma/Orange/Airtel/Gulfsat 企业页。
- 年度：电信法与监管变化、数据保护机构状态、美国务院投资气候声明、trade.gov ICT/数字经济指南、省/大区映射更新。
- 待办（2026-08-12）：MG 属 batch-10 已复核国家；后续按本方法论推进 6 省枚举，codex terra agent 分批复核后更新证据分级。
