---
name: sl-datacenter-methodology
location: scripts/expansion/world/country-skills/SL/SKILL.md
description: 塞拉利昂数据中心查询方法论（Sierra Leone datacenter discovery & audit methodology）——双线来源（官方/监管/云管线 + 行业/厂商/媒体发现）与 province/area 五省模型下的设施枚举规则。
---

# SL · 塞拉利昂数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：发现并核实塞拉利昂（Sierra Leone, SL）的商业托管（colocation）、电信数据中心、海缆登陆站、IXP、政府平台机房、金融灾备和机构服务器房。双线方法论：`explorer-official.md`（官方/监管/云管线）与 `explorer-industry.md`（行业/厂商/媒体发现），均为 codex 审核定稿。划分模型（per manifest）：**province/area** — 5 个一级划分：Eastern 东部省、Northern 北部省、North Western 西北省、Southern 南部省、Western Area 西区。评审日期：2026-08-12。

## 入口

| 入口 | 管线 | 内容 |
|---|---|---|
| `explorer-official.md` | 官方/监管/云管线 | 政府门户、部委、监管牌照、电力/环境许可、采购、海缆/IXP、运营商一级来源与官方云/Uptime 缺失检查、官方查询模板、设施/项目种子表、分省策略 |
| `explorer-industry.md` | 行业/厂商/媒体发现 | 运营商页面、行业媒体、本地媒体、海缆/IXP 记录、云/边缘来源、目录聚合器、Krio 变体查询、分级与去重规则 |

## 核心结构事实

1. **行政区划模型**：province/area，5 个一级划分：Eastern（Kenema 等）、Northern（Makeni 等）、North Western（Port Loko 等）、Southern（Bo 等）、Western Area（Freetown、Jui、Waterloo）。最低位置不得低于 `Western Area / Freetown` 或 `Southern / Bo`。Jui 属 Western Area Rural，不归 North Western。
2. **注册库现状**：SL **没有公开国家数据中心登记册**。枚举必须拼接监管牌照（NatCA/NATCOM）、政府数字化文件、采购（NPPA/e-GP）、电力/环境许可（EDSA/EGTC/EPA-SL）、海缆和 IXP 证据、运营商公告及可靠媒体。
3. **法律与监管**：NatCA/NATCOM 牌照名册只证明运营商资质，不证明物理数据中心；NPPA/e-GP 采购门户可挖政府平台机房线索；EPA-SL 环境许可/EIA/ESIA 可证实建设站点。
4. **互联与云**：ACE 海缆在 Freetown 有登陆站，由 Zoodlabs SL Limited 管理（MoCTI National Broadband Strategy 2023-2028），国家光纤骨干由 Leonecom 承包；SLIX/SLIXP 为 Freetown 2010 年启动的互联交换点，Michcom-IX/PeeringDB 显示 Freetown Zoodlabs CLS MMR 与 Jui Leonecom MMR。官方云厂商区域列表与 Uptime 认证列表均未发现 SL 区域或 Tier 记录——任何云区域/Tier/MW/机架主张必须回验一级来源。
5. **设施/项目种子**：Orange Sierra Leone Freetown Data Centre（Western Area / Freetown，A，Orange 官网自 2018）、Orange Sierra Leone Bo Data Centre（Southern / Bo City，A，MoICE 2025-12-01 确认总统启用 €23m、国家灾备枢纽、配合 Freetown 主中心）、Zoodlabs/SALCAB ACE Cable Landing Station（Western Area / Freetown，A/B）、Michcom-IX/SLIX/SLIXP（Freetown 与 Jui，A/B，按 IXP/meet-me 处理不单独计数为数据中心）、MoF/e-GP 数据中心线索（C/B）、政府 National Data Centre/Government Cloud 线索（C，尚无已运营 A 级证据）。
6. **语言与词汇**：英语为主；Krio 仅作补充发现词：`Salone`、`Fritawn`、`data senta`、`kompyuta senta`、`seva`、`netwok`、`intanet`；Krio 命中一律按 C 级线索、须英语官方/运营商/主流媒体佐证。
7. **可靠性分级**：A=一级/官方来源直接证明（gov.sl/State House/MoICE/MoCTI/DSTI、NatCA/NATCOM、EDSA/EGTC/能源部、EPA-SL、NPPA/e-GP、ACE 官方、运营商官网页、Uptime 认证页、银行/机构官网设施页）；B=强二级来源（World Bank/AfDB/UNDP/EU、DCD、Capacity、CommsUpdate/TeleGeography、SubTel Forum、Developing Telecoms、Balancing Act Africa、TechCabal、Techpoint Africa、WeAreTech Africa、TechAfrica News、ITWeb Africa、PCH/PeeringDB，或点名站点/阶段/业主的可靠本地媒体）；C=仅发现线索（目录/聚合器、社交媒体、市场报告摘要、无原始链接的招标转载、无站点/状态的 MoU、仅说 ICT 系统/服务器而未证明物理数据中心的记录）；U=暂不可用/拒绝（无 SL 上下文、无物理站点、通用云营销、地名假阳性如 `Waterloo`/`Bo`/`Kabala`/`Kambia` 未绑定 SL）。
8. **计数与去重规则**：Orange Freetown 与 Orange Bo 两个站点可分别计数（官方将 Bo 描述为 Freetown 主站的灾备/复制站），容量保持 unknown 除非 Orange 一手资料给出；Zoodlabs/SALCAB CLS、Michcom-IX、MoF/e-GP、机构机房仅在证据支持独立物理/运营身份时分别计数；IXP/MMR 关联到承载设施但不作为独立数据中心；目录数字必须回原始来源。

## 常用查询模板

所有查询同时跑 `data centre` 与 `data center`，并补充 `datacentre`、`server room`、`colocation`、`co-location`、`hosting`、`landing station`、`meet-me room`、`IXP`、`SLIX`、`SLIXP`、`disaster recovery`、`government cloud`、`generator`、`substation`、`MW`、`MVA`、`Tier III`、`Uptime`。

```text
site:gov.sl Sierra Leone "data centre" OR "data center" OR "National Data"
site:moice.gov.sl "data centre" OR "data center" OR Orange OR Bo
site:mocti.gov.sl "data centre" OR "data center" OR "Broadband Strategy" OR SLIX OR Zoodlabs
site:natcom.gov.sl "Registry of Operators" OR "data centre" OR SLIX
site:nppa.gov.sl "data centre" OR "data center" OR server OR cloud OR "disaster recovery"
site:egp.nppa.gov.sl "data centre" OR "data center" OR server OR cloud
site:epa.gov.sl "data centre" OR "data center" OR generator OR EIA OR ESIA
Sierra Leone "data centre" OR "data center" Orange OR Zoodlabs OR SALCAB OR Leonecom
Freetown "data centre" OR "data center" OR "meet-me room" OR "landing station"
Bo Sierra Leone "data centre" OR "data center" Orange OR "disaster recovery"
"Zoodlabs" Sierra Leone "data centre" OR "data center" OR "cable landing station" OR CLS
"SALCAB" OR "Sierra Leone Cable" "landing station" OR ACE
"Michcom-IX" OR "SLIX" OR "SLIXP" OR "Sierra Leone Internet Exchange Point"
"Leonecom" Sierra Leone "meet-me room" OR MMR OR backbone OR data
"data senta" Salone OR Fritawn
"kompyuta senta" Salone OR Freetown
site:datacenterdynamics.com/en/news/ Sierra Leone "data center" OR Orange OR Bo
site:commsupdate.com Sierra Leone ACE OR "submarine cable" OR Orange
site:awoko.org Sierra Leone "data centre" OR ICT OR Zoodlabs OR SALCAB
site:politicosl.com Sierra Leone Zoodlabs OR SALCAB OR ICT OR digital
site:worldbank.org Sierra Leone "data centre" OR "data center" OR "digital transformation"
```

分省模板（对每个一级划分）：`"{division}" Sierra Leone "data centre" OR "data center" OR datacentre`；`"{division capital}" Sierra Leone "data centre" OR colocation OR "server room"`；`"{town}" Sierra Leone colocation OR "meet-me room" OR IXP`；`"{division}" Sierra Leone "cloud" OR "e-government" OR "ICT hub" OR broadband`；`"{division}" Sierra Leone "captive power" OR generator OR substation`。阶段词：线索=`plans`/`seeks`/`MoU`/`study`/`strategy`；流水线=`tender`/`RFP`/`NPPA`/`e-GP`/`EIA`/`ESIA`/`construction`/`upgrade`；运营=`commissioned`/`launched`/`opened`/`operational`/`hosting`/`colocation`/`NOC`。

## 官方/监管管线要点（详见 explorer-official.md）

- **核心官方源**：info.gov.sl、statehouse.gov.sl、MoICE（已确认 Orange Bo Data Centre 公告）、MoCTI（National Broadband Strategy）、DSTI、NatCA/NATCOM 名册、NPPA/e-GP、MoF（e-GP 背景）、EDSA、MoE-EGTC、EPA-SL、ACE 官方。
- **分省官方策略**：Southern 重点查 Orange Bo Data Centre（已证实 A 级种子）；Western Area 最高召回（Zoodlabs/SALCAB ACE CLS、Michcom-IX/SLIX、Orange Freetown 主站、MoF/e-GP 线索、BSL/NCRA/Stats SL、运营商机房、银行 DR），过滤 Waterloo 假阳性；Eastern/Northern/North Western 预期商业 DC 阴性——Orange Bo 公告提到 Kono/Kenema、Makeni 受益服务但不代表该省有站点。
- **发展阶段定性**：`plans`/`strategy`/`MoU`/`study` = 线索；`tender`/`EIA`/`construction` = pipeline；`commissioned`/`opened`/`operational` = operating。牌照不是设施；容量/Tier/机架/MW/MVA/市电/自备电源只采信一级来源。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **高信号行业源**：Orange Sierra Leone（一级运营商）、MoICE Orange Bo 公告、DCD、ACE 官方、Zoodlabs、CrossBoundary Energy（Zoodlabs Freetown data centre/CLS 电力系统：0.8 MWp solar、0.7 MW thermal、1.95 MWh storage、Q2 2023）、MoCTI NBS、Michcom-IX、PeeringDB/PCH、CommsUpdate/TeleGeography、SubTel Forum、Developing Telecoms、Capacity、TechAfrica News、Datacentres Africa、Awoko、Politico SL、Sierra Leone Telegraph、Sierraloaded、目录聚合器（datacenters.com、cloudscene.com、colo.exchange、datacentermap.com、fiberatlantic.com 仅线索）。
- **运营/设施种子分级**：Orange Bo 状态可记 `operating / commissioned 2025-11-29`，容量 unknown 除非官方给出；Orange Freetown 面积/机架容量 DCD 为 B 需回验；Zoodlabs CLS 公共 colo 需运营商一手页面或合同；Sierratel/Africell/QCell/Lintel 交换机房仅官方/运营商/EPA/采购点名时升 A；BSL/银行、NCRA/Stats SL/NRA/大学默认 institutional leads，只有点名 data center/server room/DR site 且带位置才计数。
- **云/边缘**：AWS/Azure/GCP/Oracle 区域页与 Uptime 认证列表均无 SL；Google/Microsoft/AWS/Meta cache、CDN 或 on-net service 按 edge/cache/IXP participant 处理，不按云区域计数。

## 维护注意（更新纪律）

- 不删除/移动任何既有文件；双 explorer 文件是 codex 审核定稿，SKILL.md 忠实提炼其内容，细则差异以 explorer 原文件为准。
- 新证据（尤其 Bo/Freetown 容量、第二海缆、government cloud、national data centre）必须带一级来源、站点、阶段与位置后才能更新种子分级。
- 地名假阳性过滤：`Waterloo`、`Bo`、`Kabala`、`Kambia`、`Leone`、`Sierra` 必须绑定 Sierra Leone、`.sl`、Freetown/Bo/Kenema/Makeni、NatCA、MoCTI、Orange SL、Zoodlabs、SALCAB、Leonecom、EDSA、EPA 或本国机构。
