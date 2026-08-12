---
name: ws-datacenter-methodology
location: scripts/expansion/world/country-skills/WS/SKILL.md
description: |
  萨摩亚（Samoa, WS）数据中心发现与审计方法论（微型市场）。11 个 itumalo/district 全覆盖，主搜索地理为
  Apia/Tuamasaga。无公开 DC 登记册、无 DC 专属牌照、无公开商业 colo 市场；设施宇宙很小：SSCC 海底电缆站
  （Apia 与 Tuasivi，RIO 提供 colo-adjacent 接入）、政府 DC 升级/新建（World Bank DCRSP P180807，实施阶段）、
  运营商核心设施（SamoaTel、Vodafone、Digicel、CSL）。官方管线：OOTR、MCIT/MOF/World Bank、SSCC RIO、
  MWTI/PUMA、EPC、公司登记；行业侧注意与美属萨摩亚（American Samoa）资产严格区分。无 hyperscaler 区域。
  详见 explorer-official.md 与 explorer-industry.md。
---

# WS · 萨摩亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：萨摩亚是微型市场——没有商业 colo 市场，只有 SSCC 电缆站（RIO 接入）、政府 DCRSP 数据中心项目与运营商/ISP 机房。
> 一切 >0.5 MW 的大负荷声明需 EPC 或项目文档证据；海缆站、Starlink、塔站、Wi-Fi 一律不算 DC。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供后续复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：OOTR 牌照与命令、MCIT/MOF/World Bank DCRSP、SSCC RIO 2026、MWTI/PUMA 规划许可、EPC 电力、公司登记、云区域缺省核查；11 区策略与误报规则。 |
| `explorer-industry.md` | 行业/厂商发现：SSCC/SamoaTel/Digicel/Vodafone/CSL/BlueWave/Starlink 扫描、本地媒体与目录负向控制、逐区行业枚举。 |

## 核心结构事实（框定每次搜索）

1. **设施宇宙很小**：SSCC Apia 电缆站（Tuamasaga）与 Tuasivi 电缆站（Fa'asaleleaga）为 A 级 telecom 设施（RIO colo-adjacent 接入，非零售 DC）；政府 DCRSP 数据中心为实施阶段项目；其余为运营商/ISP 机房 lead。
2. **Apia/Tuamasaga 优先**，Tuasivi/Fa'asaleleaga 是唯一非 Apia 的 A 级设施 lead；其余 9 区预期只有塔站、机柜与 ICT 机房。
3. **严格区分 WS 与 American Samoa (AS)**：Pago Pago、Tafuna、ASH、Hawaiki、Le Vasa AS 侧资产均为 AS 范围。
4. **无 hyperscaler 区域**：AWS/Azure/GCP/OCI 官方区域表均无 WS（2026-08-12）；Starlink/VPS 转售为连接性，不算 DC。
5. **DCRSP 状态保守**：World Bank 指标（数据中心容量、可再生能源消耗）2026 年 1/7 月快照仍为 0 进度，目标 2029-10；未出现采购/完工记录前不得标运营。
6. **海缆站 ≠ DC**：SSCC Apia/Tuasivi 记为 `telecom_cable_station`；只有出现命名 rack colo/DC 服务的主要来源才能升级。
7. **牌照 ≠ 设施**：OOTR 牌照证明运营商角色；CSL 的托管/managed services 是最佳私有 lead 但需设施级证据。

## 查询模式（复制粘贴模板见 explorer-official.md / explorer-industry.md）

```text
site:regulator.gov.ws ("data center" OR "data centre" OR hosting OR colocation OR IXP OR RIO)
site:mcit.gov.ws OR site:mof.gov.ws ("data center" OR DCRSP OR P180807 OR "Digital Samoa")
site:ssccsamoa.com (RIO OR "Reference Interconnection Offer" OR "Facility Access" OR Apia OR Tuasivi)
site:mwti.gov.ws (PUMA OR "Development Consent" OR "Building Permit") ("data center" OR telecommunications OR ICT)
site:epc.ws ("data center" OR "large customer" OR MW OR substation)
"Samoa" ("data center" OR "data centre" OR colocation OR hosting) -proxy -VPS
"{District}" Samoa ("data center" OR "data centre" OR "cable station" OR hosting OR broadband)
"Apia" ("landing station" OR "cable station" OR server OR hosting)
site:samoaobserver.ws OR site:samoaglobalnews.com ("data centre" OR "data center" OR broadband OR cable OR digital)
"Samoa" ("AWS Region" OR "Azure region" OR "Google Cloud region" OR "OCI region")
```

## 官方/监管管线要点（详见 explorer-official.md）

- **OOTR**（regulator.gov.ws）：电信/广播/邮政/电力监管；牌照 PDF（List of Telecommunications Licensees）与 Telecom Orders 是运营商宇宙起点。
- **MCIT / MyGov / MOF / World Bank**：DCRSP（P180807）为最高置信政府 DC lead——A 级资助项目、实施阶段。
- **SSCC**：RIO 2026 PDF 是 A 级设施证据（Apia、Tuasivi、Suva 三站定义 + 接入指引）；Tui-Samoa 2018-02 启用、Manatua 2019-11 启用。
- **MWTI/PUMA**：Development Consent + Building Permit 流程（无在线数据库，缺失是弱负向信号）；FESA 消防合规。
- **EPC**：8 座水电 + 太阳能/风能/柴油机组；大负荷 DC 应留下 EPC/ADB 痕迹。
- **公司登记**（businessregistries.gov.ws）：核实运营商/转售商/项目载体法律存在。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **SSCC**：Leased Capacity/IRU/FAA + RIO 接入——最强的 colo-adjacent 证据，但仍非中性零售 colo 市场。
- **SamoaTel**：国有主导运营商 lead；站点稀疏，需 OOTR/官方渠道确认交换/网关/NOC/托管设施。
- **Digicel Samoa / Telstra Pacific**（2022-07-14 收购完成）与 **Vodafone Samoa**：移动核心在 Apia，属 B/C 推断；均为 Starlink 授权转售商。
- **CSL**（csl.ws）：本地 ISP，服务含宽带/网站/备份/网络基础设施/.ws 域名/Starlink；物理设施需 C/B 证据。
- **BlueWave / Samoa Broadband / 小型 WISP**：牌照先、媒体后；设备棚与塔站不是 DC。
- **目录**（DataCenterMap/Cloudscene）：缺项仅是弱负向信号；列出 SSCC/SamoaTel/CSL 时回到官方页 + OOTR。

## 已知设施/项目与证据状态

| 设施/项目 | 区/地点 | 状态与证据 |
|---|---|---|
| SSCC Apia 电缆站 | Tuamasaga（Apia） | Operational telecom cable station，A 级 RIO 2026；`telecom_cable_station`。 |
| SSCC Tuasivi 电缆站 | Fa'asaleleaga（Tuasivi） | Operational telecom cable station，A 级 RIO 2026；唯一非 Apia 的 A 级 lead。 |
| 政府数据中心（DCRSP P180807） | 未公开，likely Tuamasaga | Planned/实施阶段，A 级资助证据；指标目标至 2029-10，未标运营。 |
| SamoaTel / Digicel / Vodafone / CSL / BlueWave 核心设施 | Tuamasaga | A 级牌照/服务；B/C 级设施推断；需命名机房才建记录。 |
| Starlink Samoa Ltd | 全国 | 连接性服务（A 级牌照），负向控制。 |

## 更新节奏

- 每批次：重跑 OOTR 牌照/命令、SSCC RIO、DCRSP 采购/ISR、本地媒体与运营商页；重核云区域缺省。
- 每季度：检查 DCRSP 是否出现采购/完工/并网记录；复查 AS/WS 混淆项。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（11 区粒度）；本 skill 作为国家层参考注入。
