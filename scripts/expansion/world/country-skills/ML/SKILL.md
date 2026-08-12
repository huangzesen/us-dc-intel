---
name: ml-datacenter-methodology
location: scripts/expansion/world/country-skills/ML/SKILL.md
description: |
  马里（Mali, ML）数据中心发现与审计方法论。采用项目要求的 11 分区工作模型（Bamako District 加 10 个大区），
  并将 2023 年 19 大区改革的新区名（Bougouni、Kita、Nara 等）作为强制搜索别名。核心管线：官方侧
  （MCENMA、SMTD、AMRTP、DGMP/marchespublics、ARMDS、AEDD、EDM/CREE、API-Mali、APDP，法文优先）
  与行业侧（DCD、Ecofin、TechAfrica News、Maliweb/Bamada、Afribone、PeeringDB/MLIX）。主要种子：国家
  Tier III 政府数据中心（Bamako，2026-01-31 启用）、SMTD 互惠托管数据中心（Bamako/Kati）、Afribone 商业
  数据中心（Bamako/Baco Djicoroni）、MLIX 互联点。无 AWS/Azure/GCP/OCI 公有云区域；内陆国、电力为硬约束。
  详见 explorer-official.md（官方/监管管线）与 explorer-industry.md（行业/厂商发现）。
---

# ML · 马里数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：马里没有公开的国家数据中心登记册，枚举需三角化官方机构、采购、电力、环保与互联证据。
> 主簇集中在 Bamako/Kati；非 Bamako 分区以 telco PoP、塔站、光纤再生与行政机房为主。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供后续按 11 分区粒度复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：MCENMA、SMTD、AMRTP、CREE/EDM、AEDD、ARMDS、DGMP/marchespublics、API-Mali、APDP、MLIX 官方路由；11 分区 + 2023 别名扫描模板；官方验证种子表。 |
| `explorer-industry.md` | 行业/厂商发现：DCD、Connecting Africa、Ecofin、TechAfrica News、Maliweb/Bamada 等贸易媒体；Afribone/运营商/PeeringDB 种子与证据升级规则。 |

## 核心结构事实（框定每次搜索）

1. **行政区划双轨**：项目记录用 11 分区模型（Bamako District、Kayes、Koulikoro、Sikasso、Segou、Mopti、Tombouctou、Gao、Kidal、Taoudenit、Menaka）；2023 年 19 大区改革已立法（Loi 2023-006/007），新区名必须作为搜索别名，物理站点尽量回填 11 分区。
2. **无国家 DC 登记册**：官方证据依赖 SGG Journal Officiel、DGMP-DSP/marchespublics.ml 采购、ARMDS、AEDD 环评、EDM/CREE 电力与 AMRTP 牌照。
3. **种子集群**：国家 Tier III 政府 DC（Bamako，2026-01-31 Semaine du Numerique 启用，B 级）、SMTD 托管数据中心（A 级服务存在）、Afribone DC（A 级服务页 + PeeringDB org 23638）、MLIX（互联对象，不计为 DC）。
4. **无 hyperscaler 区域**：AWS/Azure/Google/OCI 官方区域表均无马里（2026-08-12 核查）。AES 数据主权声明是政策信号，不算设施。
5. **电力是门槛**：EDM 电网不稳、频繁停电；任何运营记录需发电机/UPS/电网/太阳能/PPA 证据或显式 unknown。
6. **法文优先**：`centre de données`、`hébergement`、`colocation`、`appel d'offres`、`permis de construire`；英语用于国际媒体。
7. **Tier III 是声明**：除非找到 Uptime 认证/设计文档/采购规格，不得升为已认证。
8. **错误源控制**：cybercafe、境外转售托管、银行 IT 机房、NOC、塔站、光纤路由不构成 DC 记录。

## 查询模式（复制粘贴模板见 explorer-official.md / explorer-industry.md）

```text
site:communication.gouv.ml Mali (datacenter OR "centre de donnees" OR "centre de données" OR cloud OR "souverainete numerique")
site:smtd.ml (datacenter OR "centre de donnees" OR hebergement OR cloud OR "Mali numerique")
site:amrtp.ml (datacenter OR "centre de donnees" OR operateur OR autorisation OR agrement)
site:dgmp.gouv.ml OR site:marchespublics.ml (datacenter OR "centre de donnees" OR "cloud gouvernemental" OR "fibre optique" OR NOC)
site:aedd.gouv.ml (datacenter OR EIES OR "etude d'impact" OR "groupe électrogène")
Afribone Mali (datacenter OR colocation OR MLIX OR "centre de donnees")
"{operator}" Mali (datacenter OR "centre de donnees" OR colocation OR hebergement OR cloud)
"{division}" Mali (datacenter OR "centre de donnees" OR colocation OR PoP)
site:datacenterdynamics.com Mali OR site:agenceecofin.com Mali (datacenter OR "centre de donnees")
```

## 官方/监管管线要点（详见 explorer-official.md）

- **MCENMA**（communication.gouv.ml）：数字政策、Mali Numerique、Semaine du Numerique、政府 DC/云公告。
- **SMTD-SA**（smtd.ml）：国有传输/扩散运营商，centre-de-donnees 页确认互惠托管数据中心服务（A 级服务存在；地址/容量未公开）。
- **AMRTP**：电信/邮政监管，运营商牌照与观测站——牌照不等于 DC。
- **采购管线**：DGMP-DSP、marchespublics.ml、ARMDS 查政府 DC/云/NOC/光纤合同，法文招标词（avis d'appel d'offres、attribution、marché）。
- **电力/环评/投资/数据**：EDM/CREE 电力、AEDD EIES、API-Mali 投资批准、APDP 数据保护（不证明物理设施）。
- **互联**：MLIX（PeeringDB ix/2665, fac/7240）5 个 peer（Afribone、ATEL、PCH、SOTELMA），196.60.46.0/24。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **Afribone**（afribone.com/data-center/ + colocation-housing/）：Bamako Baco Djicoroni 商业 DC，2019 年启用（Bamada B 级）；目录 MW/坐标一律 C 级待核。
- **国家 Tier III DC**：DCD/Ecofin/TechAfrica/Maliweb 报道 2026-02-02 启用（B 级）；Huawei 角色与认证待官方确认；必须与 SMTD 去重。
- **运营商宇宙**：Orange Mali、Moov Africa Malitel/SOTELMA、Telecel/ATEL —— 牌照/peering 是 A/B，设施推断是 C。
- **目录处理**：DataCenterMap/DC Hub/Connectbase 仅作发现触发器，坐标/MW/认证需官方佐证。
- **证据升级**：公告/MoU ≤ B；采购/在建 A；运营需服务页/启用/PeeringDB/供电记录；容量字段独立分级。

## 已知设施/项目与证据状态

| 设施/项目 | 分区/地点 | 状态与证据 |
|---|---|---|
| 国家 Tier III 政府数据中心 | Bamako District（地址/运营方未公开） | B 级启用（2026-01-31/02-02）；Tier III 为声明；需官方页面/采购/运营商规格。 |
| SMTD-SA 互惠托管数据中心 | Bamako/Kati 城区 | A 级服务存在（smtd.ml）；容量/电力/站点未知；不得与国家 Tier III 合并。 |
| Afribone 数据中心/colocation | Bamako, Baco Djicoroni | A 级服务页与联系方式；B 级 2019 启用新闻；容量/电力待核。 |
| MLIX | Bamako | A/B 互联对象（PeeringDB）；不计为独立 DC。 |
| Orange Mali / Moov Malitel-SOTELMA / Telecel-ATEL | 全国，核心 Bamako | A 级运营商地位；设施记录需托管/colo/云证据。 |
| 政府云/e-government 托管 | Bamako 中心 | B/A 视来源；与 SMTD/Tier III 去重。 |

## 更新节奏

- 每批次：重跑官方查询块（MCENMA/SMTD/AMRTP/DGMP/AEDD/EDM）与行业查询块（DCD/Ecofin/TechAfrica/Maliweb），重点盯国家 Tier III DC 的地址/运营商/认证落地。
- 每季度：重核 hyperscaler 官方区域表；复查 2023 年新区别名扫描（Bougouni、Kita、Nara、Koutiala、San 等）。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（11 分区粒度）；本 skill 作为国家层参考注入。
