---
name: gw-datacenter-methodology
location: scripts/expansion/world/country-skills/GW/SKILL.md
description: 几内亚比绍（GW）数据中心发现与审计方法论：官方/监管/云管线以联合国/捐助方采购（UNGM/UNDP 国家技术数据中心园区）、ARN-TIC 监管、MTTED/WARDIP 数字整合项目、MENER 能源许可与 EIA/EIASS 文件为主，行业侧以运营商（Telecel/Orange/Guine-Telecom）、ACE 海缆与 GwIX 线索、行业媒体与目录交叉验证；无公共注册库，按 manifest 的 4 个 division（Bissau、East、North、South）组织结果。运行 GW exploration/audit 批次前必读，详细来源与查询模板路由至 explorer-official.md 和 explorer-industry.md。Guinea-Bissau (GW) datacenter discovery & audit methodology: official/regulatory/cloud pipeline (UNGM/UNDP National DC Park, ARN-TIC, MTTED/WARDIP, MENER, EIA/EIASS) + industry/trade-press discovery, organized by the manifest's 4 divisions (Bissau, East, North, South); no national registry exists.
---

# GW · 几内亚比绍数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> **目的**：几内亚比绍无国家数据中心注册库、无公开建筑许可数据库、无中央环境许可门户，市场处于萌芽期且由政府/捐助方主导（无已验证的商业托管商、无 Uptime 记录）。本 skill 汇总两份已评审探索报告的发现与纪律：官方证据链必须由项目名/SPV -> 联合国/捐助方采购通知（UNGM/UNDP）或部委项目页（WARDIP/WARCIP、MTTED）-> 项目级环境/社会文件（EIA/EIASS/ESMP、安置计划）-> ARN 许可/咨询 -> MENER/EAGB 电力证据 -> 运营商/政府官方页逐级拼接；预期每轮全境扫描仅 0-2 条已验证设施记录。

## 入口

| 文件 | 管线 | 用途 |
|---|---|---|
| `explorer-official.md` | 官方/监管/云管线 | ARN-TIC 监管、MENER/EAGB 电力、项目级 EIA/EIASS、市政/规划许可、ITMA/WARDIP/ENTD.GW 公共部门 ICT、UNGM/UNDP 采购、官方云区域否定控制 |
| `explorer-industry.md` | 行业/厂商发现 | 运营商与设施普查、超大规模云状态、ACE/GwIX 连通性、行业媒体与事件、目录使用规则、分 division 行业发现图 |

## 核心结构事实

1. **Division 模型**：manifest 规定 4 个 division（`subnational_type = autonomous sector/province`）：**Bissau**（Sector Autonomo de Bissau）、**North**（Cacheu、Oio、Biombo）、**East**（Bafata、Gabu）、**South**（Quinara、Tombali、Bolama-Bijagos）。行政上为 8 大区 + Bissau 自治部门；仅当每个 division 均被搜索或显式标记 `no_projects: true`（含日期与查询记录）才视为覆盖完整。
2. **语言与拼写**：葡语为政府与媒体工作语言，查询必须用葡语词：`centro de dados`、`data center`、`centro de processamento de dados`、`sala de servidores`、`colocation`/`colo`、`fibra optica`、`backbone`、`licenca`、`autorizacao`、`concurso publico`、`contrato`、`gerador`、`energia`、`EIA`/`EIASS`/`estudo de impacto ambiental`、`parecer ambiental`。
3. **唯一已确认设施**：UNDP/日本资助的 **National Technology Data Center Park / Centro Nacional de Dados**（Alto Bandim，Bissau）：UNDP 招标 UNDP-GNB-00270（UNGM 通知 278362，2025-09-12 发布、2025-10-08 截止），2026-03 开工、地方报道称 2026-07 计划完工，容量未披露；包含国家数据中心、ITMA 新总部及数据保护/网络安全机构设施。别名去重：National Technology Data Center Park = Centro Nacional de Dados = "Data Center" da Guine-Bissau（同一 Bissau 项目，ITMA 总部是其一部分）。
4. **关键机构**：ARN/ARN-TIC（电子通信监管机构，arn.gw，依 Lei n. 5/2010 设立并继承 ICGB；**不是数据中心许可机构**，用于运营商牌照/咨询/市场观察/.gw 域）；MTTED（运输、电信与数字经济部）/WARDIP（世界银行资助的西非区域数字整合项目，wardip.gw，含国家骨干 Espinha Dorsal 与网络空间/数据保护改革）；ITMA（政府 ICT 学院，日本资助新总部约 EUR 193 万，2024-03-29 宣布，总理称建筑将容纳国家数据中心）；MENER（能源政策与关税监管，有能源许可板块）；EAGB（国有电力公司，无官方网站）；ARSECO 仅监管燃料，勿混淆为电力监管。
5. **无注册库纪律**：无电力许可登记册、无数据保护法/机构登记册（DPA）、无集中环境许可门户；不得针对不发布登记册的机构虚构查询，改用 MENER 许可、WARDIP/ITMA 文件与项目级 EIA。
6. **容量语义**：容量声明稀少；建筑/建设通知不得直接换算为 IT 负荷。宣布容量与已投运容量分开记录（GW 目前预期 `capacity_mw=null`）。状态梯子：rumour < MoU < announced < land acquired < permit/procurement applied < permit/procurement granted < construction started < commissioned/inaugurated < operational；无证据不得跳级。
7. **可靠性分级规则**：A = 主要/官方（ARN 通知/许可、MTTED/政府门户、WARDIP/WARCIP 官方文件、UNDP/UNGM 采购通知与国别报告、MENER/EAGB 官方文件、ENTD.GW、官方云区域页）；A- = 官方运营商/新闻稿证明具名场地/状态（设计容量谨慎使用）；B = 强二级（ANG、O Democrata GB、Lusa、RFI、DW 等引述官员的地方/区域媒体）；C = 仅线索（博客、目录、市场报告、SEO 页）。分级作用于具体声明：同一设施可存在性 A、宣布 MW B、投运状态 C。
8. **云/IXP/连通性否定与邻接**：AWS/Azure/GCP/Oracle 均无 GW 公共区域（官方页 A 级否定，每批必查）；ACE 是唯一国际海缆（登陆点 Suro/Suru、Cacheu 区 = North division，经 30 km 陆路延伸至 Bissau 郊区 Antula 电厂，2023-03-28 完成）；GwIX 协会 2024-08-23 成立、官网为占位页、无运营 IXP 设施/PeeringDB 记录；Starlink 未经授权使用（ARN 公告）非数据中心记录；登陆站与骨干是 DC 邻接线索而非设施。
9. **运营商状态**：Telecel Guinea-Bissau（原 MTN/原 Spacetel，2024-08-07 完成转让）、Orange Guinea-Bissau（官方站点或需企业页回退）、Guine-Telecom/Guinetel（国有固网运营商，2013 破产，2021 获牌照，2024 政府招标出售 Guinetel 80%）——均无公开零售托管服务，网络机房为未验证房间。
10. **状态明确性**：国家 DC 园区为在建（construction）而非运营；2026-03 报道称 2026-07 完工但容量不披露，官方启用来源出现前保持 `status=construction`、`capacity_mw=null`；完成日期（地方报道 B/C 级）需官方确认。

## 常用查询模板

官方/监管管线（ARN、MENER、WARDIP/ITMA、UNDP、云否定控制）：

```text
site:arn.gw ("centro de dados" OR "data center" OR datacentre)
site:arn.gw ("licenca" OR "licenciamento" OR "autorizacao") ("{operador}" OR "{SPV}")
site:arn.gw ("EIASS" OR "Estudo de Impacto Ambiental" OR "Espinha Dorsal")
site:ministeriodaenergia.gw ("licenciamento" OR "licenca" OR "autorizacao") "{empresa}"
site:ministeriodaenergia.gw ("centro de dados" OR "data center" OR "servidores")
site:wardip.gw ("centro de dados" OR "data center" OR backbone OR "fibra optica")
"ITMA" "Guine-Bissau" ("data center" OR "centro de dados" OR modernizacao)
site:ungm.org "Guinea-Bissau" ("data center" OR "centro de dados" OR "national technology")
UNDP-GNB ("data center" OR "centro de dados" OR ITMA)
("Alto Bandim" OR Bissau) construcao ("data center" OR "centro nacional de dados")
site:aws.amazon.com "Guinea-Bissau" "Region"
```

行业/厂商发现（运营商、连通性、目录）：

```text
("Guine-Bissau" OR Bissau) ("data center" OR "centro de dados" OR "centro nacional de dados") (launch OR construcao OR inaugurado OR operacional)
(Telecel OR MTN OR Orange) "Guine-Bissau" "centro de dados"
"Guine-Bissau" "ACE" "cabo submarino" (Suro OR Suru OR Bissau)
(GwIX OR "Guinea-Bissau Internet Exchange" OR "PIT Guine-Bissau")
site:datacenterdynamics.com ("Guinea-Bissau" OR "Guine-Bissau")
site:ang.gw ("data center" OR "centro de dados" OR digital OR fibra)
site:baxtel.com ("Guinea-Bissau" OR Bissau) "data center"
site:uptimeinstitute.com ("Guinea-Bissau" OR Bissau) "Data Center"
("{division}" OR "{region}") "Guine-Bissau" ("data center" OR "data centre" OR "centro de dados" OR "sala de servidores")
```

推荐输出结构（每设施一条）：

```json
{
  "country_code": "GW",
  "division": "Bissau",
  "name": "...",
  "status": "construction",
  "operator": "...",
  "capacity_mw": null,
  "announced_capacity_mw": null,
  "racks": null,
  "source_urls": [...],
  "evidence_date": "...",
  "evidence_grade": "A",
  "notes": "..."
}
```

## 官方/监管管线要点（详见 explorer-official.md）

- **ARN**：Lei de Base das TIC Lei n. 5/2010 下电子通信监管；发布 Espinha Dorsal 国家骨干 EIASS（WARDIP 页面链接已验证 PDF）；发布市场观察报告（A 级用于运营商数量，不用于设施）；曾就电子交易法草案咨询、对未授权 Starlink 服务发布公告。
- **MENER**：能源许可（licenciamento energetico）为发电/自发电（柴油机组或太阳能）最接近的许可面；EAGB 为垄断国有电力公司，Karpower 浮动电厂合同已终止，OMVG 互联自 2025 年 8 月下旬供电（B 级）；电网可靠性差，数据中心级负荷预期依赖现场柴油/太阳能。
- **项目级 EIA/EIASS**：EIASS Espinha Dorsal（ARN 站）、WARCIP ACE 安置计划（2019，Plano de acao para reinstalacao）、WARDIP QPR 框架（ibapgbissau.org）；UNDP 采购通知可能内嵌环境要求。
- **市政许可**：Bissau 市场地经 Camara Municipal de Bissau；无全国/公开许可数据库，报刊或官方纪要中的许可引用仅为 B/C 级线索。
- **UNDP 采购**：UNDP-GNB-00270 "Construction of National Technology Data Center Park"（UNGM 278362，2025-09-12 发布/2025-10-08 截止）为 A 级设施证据；UNDP/PNUD 简报与通讯是实施状态最佳官方来源。
- **云区域否定控制**：AWS/Azure/GCP/Oracle 官方页均无 GW（每批重跑）；云办公室/合作伙伴节点/缓存/CDN PoP/卫星宽带/边缘节点均为生态系统记录而非设施。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **设施普查**：唯一记录 = 国家技术数据中心园区（Bissau/Alto Bandim，在建，A/A- 证据链）；ITMA 归属园区内，不作独立商业设施。
- **连通性**：ACE 唯一国际海缆（Suro/Suru，Cacheu）；国家骨干 Espinha Dorsal 经 PPP 模式国际招标（WARDIP）；GwIX 为协会线索（占位官网、LinkedIn、ISOC Peering Roadshow 2025），无运营设施。
- **行业来源**：ANG（B）、O Democrata GB（B）、Lusa/RFI/DW（B）、DCD（B+，GW 报道稀少）、Developing Telecoms/Ecofin/Connecting Africa（B）、ISOC/PCH/TeleGeography（A-/B）、UNGM/UNDP/World Bank（A）、目录（C，GW 基本为噪音）。
- **目录纪律**：无目录条目不得仅凭目录建设施；MW/机柜目录值记为 `claimed_capacity`；别名防重：Telecel vs MTN vs Spacetel、Centro Nacional de Dados vs ITMA 建筑、Suro vs Suru。
- **常见假阳性**：ACE 登陆站（Suro）与 Antula 电厂（30 km 陆路连接）非数据中心；运营商"data center"（网络机房）无托管服务/设施级来源；ITMA 建筑与国家 DC 双计；Starlink/VSAT 卫星互联网；骨干/数字化转型公告；目录国家列表噪音；无 UNGM/UNDP 通知支撑的"PNUD 开工"博客（博客 C、UNGM A）。

## 维护注意（更新纪律）

- **更新节奏**：每批重跑官方云区域否定控制与 Uptime 检查；追踪国家 DC 园区开工/完工/启用官方来源（UNDP/PNUD 简报）、WARDIP/ARN 骨干与 IXP 采购页、Guine-Telecom/Guinetel 80% 出售结果、GwIX 是否出现运营 IXP 记录。
- **来源验证**：官方验证顺序 UNGM/UNDP 通知 -> MTTED/WARDIP 项目页 -> EIA/EIASS/ESMP -> ARN 许可/咨询 -> MENER/EAGB 电力 -> CFE/公司注册 -> 运营商/政府官方页；博客与聚合站除非复制官方通知否则为 C 级；`no_projects: true` 仅在所有 division 模板与官方/全国来源运行后才可用。
- **禁止删除纪律**：本 skill 与两份 explorer 均不删除既有事实；别名合并（Telecel=MTN=Spacetel、Suro=Suru、国家 DC 园区=ITMA 建筑）在记录中保留别名与证据链接，不得静默丢弃旧条目。
