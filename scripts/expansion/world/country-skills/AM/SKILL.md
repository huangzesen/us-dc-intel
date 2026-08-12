---
name: am-datacenter-methodology
location: scripts/expansion/world/country-skills/AM/SKILL.md
description: |
  Armenia (AM) datacenter discovery & audit methodology — how to enumerate, verify, and update Armenia datacenter projects at marz granularity (10 marzes + Yerevan city in the current manifest). Primary-source order: government/ministry projects (hightech.gov.am, mineconomy.am, arlis.am), construction/land/permits (urban.e-gov.am, minurban.am, azdarar.am, cadastre.am), PSRC energy/telecom regulator, Uptime Institute, operator pages, and procurement (armeps.am). Armenian-language evidence is mandatory (տվյալների կենտրոն), with Russian pivots (дата-центр/ЦОД). Verified clusters: Kotayk (Firebird AI Factory DC-1 Hrazdan, OVIO/GNC-ALFA Abovyan Tier III design), Gegharkunik (Eleveight AI Factory Gagarin), Yerevan (Viva, TeamCloud, YSU HPC), Aragatsotn (VSData green DC planned). No hyperscaler public cloud region. Read this before running AM exploration/audit batches. Routes to explorer-official.md (anchors/PSRC/permits/environment/procurement/energy/12-division strategy) and explorer-industry.md (market structure/seeds/source list/query patterns/division workflow).
---

# AM · 亚美尼亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：亚美尼亚已从“小型 Yerevan colo 市场”变为**AI 工厂新兴市场**；官方主源顺序：政府/部委项目（hightech.gov.am、mineconomy.am、arlis.am）→ 建设/土地/许可（urban.e-gov.am、minurban.am、azdarar.am、cadastre.am）→ 监管/公用事业（PSRC、ENA、HVEN、MTAI）→ 认证/运营商（Uptime、官方云区域列表）→ 二手确认（ARKA/Armenpress/DCD）。
> 分区模型：**10 marz + Yerevan 市**（Aragatsotn; Ararat; Armavir; Yerevan; Gegharkunik; Kotayk; Lori; Shirak; Syunik; Tavush; Vayots Dzor）；高产出：Kotayk（Firebird Hrazdan + OVIO Abovyan）、Gegharkunik（Eleveight Gagarin）、Yerevan（Viva/TeamCloud/YSU）。
> 亚美尼亚语强制（`տվյալների կենտրոն` 数据中心、`սերվերային` 服务器房、`կոլոկացիա`、`շինարարության թույլտվություն` 建设许可、`շահագործման է հանձնվել` 已投运），俄语 pivot（`дата-центр`、`ЦОД`、`облачные услуги`）。
> 无 AWS/Azure/GCP/OCI 公共云区域（官方页负面）；Cloudflare Yerevan 为边缘 PoP 非 DC。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供亚美尼亚探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：已核实主锚表（Firebird/Eleveight/OVIO/Viva/TeamCloud/YSU/VSData/Cloudflare/云负面）、PSRC 工作流（电力/电价/电信授权注册）、许可与环评（urban.e-gov.am/minurban/azdarar/cadastre/env.am）、采购（armeps.am）、能源电网验证（ENA/HVEN/MTAI/IEA）、11 单元策略与分级规则 |
| `explorer-industry.md` | 行业/厂商发现：市场结构（四集群）、运营商与项目种子表、高信号源（Firebird/NVIDIA/部委/Eleveight/OVIO/Uptime/Viva/TeamCloud/YSU/VSData）、贸易媒体（DCD/Armenpress/ARKA/Developing Telecoms/Telecompaper）、目录（DataCenterMap 等 C）、查询模式（英/阿/俄）、分区工作流与提取规则 |

## 核心结构事实（框定每次搜索）

1. **四大已核实集群**：① Kotayk——Firebird AI Factory DC-1 Hrazdan（运营，官方页 6,144 NVIDIA B200/15 MW，部委页近 Hrazdan、200,000 sq m、2026-07 启用计划、>6,000 Blackwell/18 MW；300 MW/70,000+ GPUs 为路线图）+ OVIO/GNC-ALFA Data Center Abovyan（运营商业 colo/云，Tier III Design 认证，官方页 2 MW/216 机架，2024-05 商用）；② Gegharkunik——Eleveight AI Factory Gagarin（运营，512 NVIDIA B300、一期 $120m、扩展至 40 MW，地址 Gortsaranayin 1）；③ Yerevan——Viva（A colo 设施）、TeamCloud/Team Telecom Armenia（A 服务/Tier III 主张，地址 C/B）、YSU AI 数据中心/超算（A 机构，64 NVIDIA H100）；④ Aragatsotn——VSData 绿色 DC（B+ 计划/在建，2 MW/125 机架、泉水/峡谷冷却、2025 年底目标，无 A 投运证据）。
2. **计数门槛**：设施级证据（名称/运营商 + 地点或地址 + 状态）才算；PSRC 电信授权、云转售、CDN/IX 存在或服务器房招标不足。
3. **PSRC 是监管上下文非注册库**：电力/电价/电信授权注册（A 授权状态；仅注册表=设施存在 C）；能源决定+设施源=电网/公用事业 A。
4. **许可/土地/环评**：urban.e-gov.am（建设许可平台）、minurban.am（城市发展委员会）、azdarar.am（官方公告）、cadastre.am（地籍）、env.am（环境部 EIA）；提取申请人/地块/许可类型/功能/面积/发证机关/日期/投运状态。
5. **能源与电网**：PSRC、ENA（电价）、HVEN、MTAI；MVA 不自动转 MW；IT load/总设施功率/电网连接/路线图容量分开；Firebird 15/18 MW 当前值与 300 MW 路线图分开；OVIO 用当前官方页 2 MW/216 机架（旧 218 机架页为历史）。
6. **无超规模云区域**：官方页负面控制（AWS/Azure/GCP/OCI）；警惕 `AM` 缩写与亚美尼亚无关（美国/其它）。
7. **假阳性抑制**：开放数据门户、学校/TUMO/智慧城市 IT 房、宽带推广、CDN/IX PoP 无寄主设施、银行/部委服务器房改造、无计算设施证据的电厂（Hrazdan TPP/Metsamor NPP/变电站/太阳能）。
8. **目录陷阱**：目录常把非 Yerevan 设施归入 Yerevan 都市标签——Hrazdan=Kotayk、Abovyan=Kotayk、Gagarin=Gegharkunik、VSData=Aragatsotn；PeeringDB 证明网络存在非 MW/状态。

## 查询模式（复制粘贴模板见 explorer-official.md §3-§5 / explorer-industry.md §4）

- PSRC：`site:psrc.am "տվյալների կենտրոն"`、`site:psrc.am "Էլեկտրոնային հաղորդակցություն" "{operator}"`、`site:psrc.am "Հրազդան" "լիցենզիա"`、`site:psrc.am "Աբովյան" "ենթակայան"`。
- 许可/土地：`site:urban.e-gov.am "տվյալների կենտրոն"`、`site:minurban.am "Հրազդան" OR "Գագարին" OR "Աբովյան"`、`site:azdarar.am "շինարարության թույլտվություն" "տվյալների"`、`"{facility}" "շահագործման թույլտվություն"`、`site:yerevan.am "տվյալների կենտրոն"`。
- 环境：`site:env.am "data center" OR "տվյալների կենտրոն"`、`"{operator}" "environmental impact" Armenia data center`。
- 采购：`site:armeps.am "տվյալների կենտրոն"`、`site:armeps.am "սերվերային"`、`site:armeps.am "supercomputer" OR "գերհամակարգիչ"`。
- 能源：`site:ena.am "տվյալների կենտրոն"`、`"{facility}" "MW" Armenia`、`"{facility}" "220 kV" Armenia`、`site:mtad.am "data center"`。
- 运营商：`site:firebird.ai Hrazdan`、`site:eleveight.ai Gagarin`、`site:ovio.am Abovyan data center`、`site:viva.am colocation data center`、`site:teamcloud.am colocation`、`site:ysu.am supercomputer NVIDIA H100`、`site:vsdata.org Armenia data center`。
- 俄语：`"{ru_alias}" "дата-центр"`、`"{ru_alias}" "ЦОД"`、`"{ru_alias}" "центр обработки данных"`。
- 媒体：`site:datacenterdynamics.com Armenia data center`、`site:armenpress.am "data center" Armenia`、`site:arka.am "data center" Armenia`、`site:developingtelecoms.com VSData Armenia`。

## 官方/监管管线要点（详见 explorer-official.md）

- 政府/部委：hightech.gov.am（Firebird/Eleveight/YSU/HPC 政策与 MoU，A）、mineconomy.am（Infrastructure in Exchange for Investment）、arlis.am（法律）。
- 建设/土地：urban.e-gov.am + urban-permits.e-gov.am（备选）、minurban.am、azdarar.am、cadastre.am、e-request.am；Yerevan 市与 marz 政府门户。
- PSRC：电力/电信授权注册（A 状态；C 设施）；e-services.psrc.am。
- 环评：env.am；采购：armeps.am（中标=采购 A；设施存在 B/C 直至投运/运营商证据）。
- 能源：ENA/HVEN/MTAI；IEA/世行背景；规则见核心事实 5。
- 分级：A=至少一个主源点名设施/项目 + 地点/状态/容量之一；Uptime Design 文档=设计奖 A，非 Constructed 认证；B=强媒体具名但无主源；C=纯目录/PeeringDB/市场/社交/泛云托管页。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 主源：Firebird（firebird.ai，A）、NVIDIA blog（A）、部委（A）、Eleveight（A）、OVIO/oviocloud（A）、Uptime Abovyan 记录（A TCDD）、Viva（A）、TeamCloud（A 服务）、YSU（A）、VSData（B+/自述）、云官方页（A 负面）。
- 媒体：DCD（B，Firebird/Eleveight/OVIO/VSData/YSU 最佳英文贸易索引）、Armenpress（B+/A 政府行动直报）、ARKA/ARKATelecom（B）、Legrand/Data Center Frontier（B/A YSU）、Developing Telecoms（B VSData）、Telecompaper（B 旧史）、Kommersant（B 所有权上下文）。
- 目录（C）：DataCenterMap、DataCenterJournal、datacenters.com、Inflect、Cloudscene、PeeringDB、whtop、SPYUR；目录“operational”标签（尤其 VSData）需主源确认。
- 状态/容量提取：`opened/launched/commissioned`=运营；`under construction`=在建；`planned`=规划；GPUs/机架/MW/MVA/sq m 保留原单位与措辞；设施类型分商业 colo/云、AI/GPU 工厂、机构/研究 HPC、企业/政府内部、灾备、边缘/网络 PoP、服务器房。

## 已知设施/项目与证据状态

| 设施/项目 | 分区 | 状态与证据 |
|---|---|---|
| Firebird AI Factory / DC-1 Hrazdan | Kotayk | 运营（A 官方页/部委/NVIDIA）；6,144 B200/15 MW（官方页）或 18 MW（部委）；300 MW/70,000+ GPUs 为路线图 |
| Eleveight AI Factory | Gegharkunik（Gagarin） | 运营（A 运营商/部委/Armenpress）；512 B300、$120m 一期、40 MW 扩展目标 |
| OVIO / GNC-ALFA Data Center Abovyan | Kotayk（Abovyan） | 运营（A 运营商页 + Uptime TCDD Tier III）；2 MW/216 机架（官方页） |
| Viva Data Centers | Yerevan | 运营 colo（A 官方页；2N 供电/冷却、双高压馈线、柴油发电机） |
| TeamCloud / Team Telecom Armenia DC | Yerevan | A 服务/Tier III 主张；设施地址 B/C 待独立源 |
| Yerevan State University AI DC / 超算 | Yerevan | A 机构（64 NVIDIA H100，政府资助）；非商业 colo |
| VSData 绿色 DC | Aragatsotn | B+ 计划/在建（2 MW/125 机架、泉水冷却）；无 A 投运证据 |
| Datacom / ADC Core Network | Yerevan | C/B 线索；运营商页/许可/采购前不升级 |
| Arminco AIC / Ucom / GNC-Alfa Yerevan | Yerevan | C（历史 ISP/目录线索，地址陈旧） |
| Cloudflare Yerevan #103 | Yerevan | A 边缘 PoP；非 DC 计数项 |

## 更新节奏

- 每批次：云区域负面核查、Firebird DC-1 当前值 vs 路线图、Eleveight 扩展（40 MW）、OVIO/VSData 投运与许可、Viva/TeamCloud 官方页变更、Uptime AM 页。
- 季度：11 单元负面扫回顾（Ararat/Armavir/Lori/Shirak/Syunik/Tavush/Vayots Dzor）、PSRC 授权与 ENA 连接、armeps 采购新标、目录别名去重。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（11 单元粒度）；本 skill 作为国家层参考注入。
