---
name: cm-datacenter-methodology
location: scripts/expansion/world/country-skills/CM/SKILL.md
description: |
  喀麦隆（Cameroon, CM）数据中心发现与审计方法论。10 大区覆盖，市场集中在 Centre（Yaoundé/Zamengoé）与
  Littoral（Douala）。核心种子：Camtel NBN II/Zamengoé 数据中心（Centre/Lékié，Uptime Tier III Design
  Documents，运营/在售）、Camtel Bepanda（Littoral，PeeringDB fac/10585 + CAMIX Douala）、Orange Cameroun
  数据中心（Littoral/Douala 5e/Maképé，2017-05 起运营，340 racks/3×1050 m²）、ST Digital 数据中心（Littoral/
  Douala 港口区/Douala-Bonabéri，MINPOSTEL 2025 官方视察）、CAMPOST 数据中心 Yaoundé（Centre/Mfoundi，CAMIX
  + PeeringDB fac/10586）、MTN Cameroon Yaoundé DC（Centre，仅 Uptime 设计奖，非运营）。法文优先
  （centre de données、hébergement、colocation）。无 AWS/Azure/GCP/OCI/Huawei Cloud 公有云区域。
  详见 explorer-official.md 与 explorer-industry.md。
---

# CM · 喀麦隆数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：喀麦隆是小型但真实的本地托管市场，集中在 Centre（Yaoundé/Zamengoé）与 Littoral（Douala）。
> 分区归属是硬要求：Zamengoé 归 Centre/Lékié（市场常标 Yaoundé）；Orange/ST Digital 归 Littoral/Douala。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供按 10 大区粒度复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：MINPOSTEL、ART、Camtel/hosting、Orange Business、ST Digital、CAMPOST/CAMIX、MTN/Uptime、ANTIC/CENADI、MINEE/ARSEL/ENEO/SONATREL、MINHDU/MINMAP/ARMP 采购；10 区扫描与记录提取清单。 |
| `explorer-industry.md` | 行业/厂商发现：运营商深度档案（Camtel/Orange/ST Digital/CAMPOST/MTN）、Nexttel/银行/ISP leads、海缆与 CAMIX 互联、hyperscaler 追踪、贸易媒体分级表。 |

## 核心结构事实（框定每次搜索）

1. **10 大区模型**：Adamaoua、Centre、Far North、East、Littoral、North、North-West、West、South、South-West；Centre + Littoral 是正产量区，其余 8 区默认负向扫描。
2. **无国家 DC 登记册**：记录由运营商页 + ART + MINPOSTEL/ANTIC/CENADI + MINHDU 许可 + MINEE/ARSEL/ENEO/SONATREL 电力 + MINEPDED 环评 + 采购 + Uptime/PeeringDB 拼接。
3. **法文优先**：`centre de données`、`hébergement`、`colocation`、`baies`、`mise en service`、`inauguration`、`raccordement`、`MVA`；NW/SW 与英文媒体用 `data centre`/`colocation`/`Tier III`。
4. **Uptime 设计奖 ≠ 建成认证**：Camtel NBN II 与 MTN Yaoundé DC 均为 "Tier III Certification of Design Documents"；MTN 不得标运营/商用。
5. **分区归属硬规则**：Zamengoé→Centre/Lékié（Okola 一带）；Orange→Littoral/Douala 5e/Maképé；ST Digital→Littoral/Douala 港口区/Douala-Bonabéri；CAMPOST→Centre/Mfoundi；Camtel Bepanda→Littoral/Wouri。
6. **无 hyperscaler 区域**：AWS/Azure/GCP/OCI/Huawei Cloud 官方页均无喀麦隆（2026-08-12）；CDN/edge/PoP 与云区域记录分开。
7. **泛非进入者 watchlist**：Raxio、Africa Data Centres 无 CM 设施；ST Digital 已是现实运营者（不再是 lead）。
8. **海缆/地球站/交换机房 ≠ DC**：Kribi/Douala 登陆站、Bepanda/Zamengoé/Garoua 地球站、telco 交换、银行 IT 机房需服务证据才能升级。

## 查询模式（复制粘贴模板见 explorer-official.md / explorer-industry.md）

```text
site:minpostel.gov.cm "centre de données" OR "data center" OR "datacenter"
site:art.cm "centre de données" OR "data center" OR "hébergement" OR "{operator}"
site:camtel.cm OR site:hosting.camtel.cm ("Zamengoé" OR "NBN II" OR "colocation" OR "hébergement")
site:business.orange.cm ("data center" OR "tiers III" OR "340 baies" OR "1050 m²")
site:st.digital ("Cameroun" OR "Douala" OR "datacenter" OR "cloud souverain" OR "CloudStore")
site:camix.cm ("CAMPOST" OR "Data Center" OR "Yaoundé")
site:uptimeinstitute.com "MTN Cameroon" OR "Camtel NBN II"
site:armp.cm OR site:marchespublics.cm OR site:minmap.cm ("data center" OR "centre de données" OR "hébergement")
site:minpostel.gov.cm ("NCSCS" OR "câble sous-marin") OR "SAIL" "Kribi"
"Orange Cameroun" "Maképé" OR "Douala 5" "data center"
"ST Digital" "zone portuaire de Douala" OR "Douala-Bonabéri" "data center"
"{region}" OR "{capital}" "centre de données" OR "data center" "Cameroun"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **MINPOSTEL**：数字战略、NCSCS 国家海缆页、ST Digital 数据中心官方视察文章（2025-07-21，A 级认可 Douala 港口区位置）。
- **ART**：运营商/牌照/DAO；牌照不证明设施。
- **Camtel**（camtel.cm + hosting.camtel.cm）：NBN II/Zamengoé 运营在售 + Uptime 设计奖；Bepanda PeeringDB fac/10585。
- **Orange Business Cameroun**（business.orange.cm）：官方页给出 "1 data center tiers III+"、3×1050 m²、340 racks 两白区、双中压馈线、双光纤接入、24/7。
- **ST Digital**：官方站（ISO 27001/TIA-942/HDS 自述）+ MINPOSTEL 视察；"certified" 限定于 ST Digital 自述，不得转成 Uptime Tier。
- **CAMPOST/CAMIX**：CAMIX 官方联系地址 "Immeuble Data Center CAMPOST, BP 788 Yaoundé" + PeeringDB fac/10586；2024 ARMP AMI 提及 EPOST 数据中心改造/扩建与 Douala 二级数据中心计划。
- **MTN**：仅 Uptime 设计奖（Yaoundé DC）；MTN/ART/PeeringDB/采购证明启用前保持 design-awarded。
- **电力/许可/采购**：MINEE/ARSEL/ENEO/SONATREL/EDC、MINHDU 许可、MINMAP/ARMP/COLEPS 采购、MINEPDED EIES；死链注意（cfce.cm、www.marches-publics.cm、www.minepded.gov.cm 本次未通）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **Camtel**：Zamengoé（Centre）运营/在售；Bepanda（Littoral）为互联/telco 设施；Garoua 地球站（North）为 C lead。
- **Orange Cameroun**：Maképé/Douala 5e 运营（2017-05），官方规格 A 级，16 bn FCFA/$27m 用媒体语境；"Tier III+" 按 Orange 措辞记录。
- **ST Digital**：Douala 港口区运营/在售，A 级证据已存在；CloudStore 服务用 Douala Tier 3 机房服务器（blog 转载 B/C+）。
- **CAMPOST**：Yaoundé 互联/机构设施（CAMIX + PeeringDB）；商业 colo 需 CAMPOST 服务页证明。
- **MTN Yaoundé DC**：Uptime 设计奖是重要修正——不要只当普通 telco 内部 lead。
- **Nexttel/Viettel、Yoomee、银行/大学**：C 级 lead，无 A/B 命名设施不建记录。
- **海缆**：SAT-3/WASC、ACE、NCSCS、SAIL；Kribi（South）是最强非 Centre/Littoral 未来 lead。

## 已知设施/项目与证据状态

| 设施/项目 | 大区/分区 | 状态与证据 |
|---|---|---|
| Camtel NBN II / Zamengoé 数据中心 | Centre / Lékié（市场标 Yaoundé） | 运营/在售；Uptime Tier III Design Documents；容量/成本用 B 级媒体限定词。 |
| Camtel Bepanda | Littoral / Wouri / Douala | 运营互联/telco 设施（A-，PeeringDB fac/10585 + CAMIX Douala）。 |
| Orange Cameroun 数据中心 | Littoral / Douala 5e / Maképé | 运营（2017-05 起），A 级官方规格（340 racks、3×1050 m²、双 MV、双光纤）。 |
| ST Digital 数据中心 | Littoral / Douala 港口区 / Douala-Bonabéri | 运营/在售，A 级（官方站 + MINPOSTEL 视察）。 |
| CAMPOST 数据中心 Yaoundé | Centre / Mfoundi / Yaoundé | 运营互联/机构设施（A-，CAMIX + PeeringDB fac/10586）；商业 colo 待服务页。 |
| MTN Cameroon Yaoundé DC | Centre / Yaoundé（站点未知） | 仅 Uptime 设计奖（A），运营/商用未证。 |
| Camtel Garoua 地球站 | North / Benoué / Garoua | Telco 站点 lead（C），非 DC。 |
| Kribi 海缆登陆基础设施 | South / Ocean / Kribi | 登陆站（A 级登陆证据），demand/edge lead 非 DC。 |
| Nexttel/Viettel、银行、大学、ISP | Centre/Littoral 可能 | C 级内部 lead，需命名证据。 |

## 更新节奏

- 每批次：重跑官方（MINPOSTEL/ART/Camtel/Orange/ST Digital/CAMPOST/MTN/Uptime/采购）与行业（DCD/Ecofin/Business in Cameroon/CIO Mag）查询块；盯 MTN Yaoundé DC 启用证据与 ST Digital 精确地址/认证。
- 每季度：重核 hyperscaler + Huawei Cloud 官方页；复查泛非进入者（Raxio、ADC）；重跑 10 区法英双语扫描。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（10 大区粒度）；本 skill 作为国家层参考注入。
