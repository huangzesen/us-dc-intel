---
name: sb-datacenter-methodology
location: scripts/expansion/world/country-skills/SB/SKILL.md
description: |
  所罗门群岛（Solomon Islands, SB）数据中心发现与审计方法论（微型市场）。覆盖 9 省 + Honiara Capital
  Territory。无国家 DC 登记册；监管者为 TCSI（Telecommunication Commission Solomon Islands，依据
  Telecommunications Act 2009，非 "TSPL"）。硬设施证据集中在 Honiara；唯一已证的非 Honiara 政府设施为
  Noro Data Centre（Western 省，2025-11 移交，政府 DR/备份）。种子：Our Telekom（Honiara Exchange
  Building/主数据中心机房 + NOC）、SISCC 海缆站（CS²/SIDN，2020-02 起商用，登陆 Honiara/Auki/Noro/Taro）、
  ACS-1 第二条国际海缆（AIFFP 资助，CLS 2027-04 预期）、SATSOL（目录声明 C 级）、国家 DC 管线（Huawei
  讨论，B 级意向）。无 hyperscaler 区域。详见 explorer-official.md 与 explorer-industry.md。
---

# SB · 所罗门群岛数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：SB 是最不发达国家/小岛国，ISOC Pulse 报告仅列 1 个活跃数据中心、9 个活跃网络（B 级市场指标）。
> "data centre" 常指海缆站、telco 核心/运维室、省级机房、渔业 MCS 设施、云产品或捐赠项目机房——须防过度计数。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供按 9 省 + 首都区粒度复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：TCSI/MCA 牌照与政策、Telecommunications Act 2009、Lands/Physical Planning 许可、Solomon Power 电力（Lungga 唯一电网）、SISCC/ACS-1 海缆、政府数字基建记录（Noro DC、国家 DC 管线、SINBIP）、云区域缺省；逐省策略。 |
| `explorer-industry.md` | 行业/厂商发现：运营商/colo 种子（Our Telekom、bmobile、SATSOL、SISCC、Solomon Tower）、云/主权云扫描、互联 pivot（CS²/SIDN/ACS-1/IXP/卫星）、本地媒体与目录、逐区查询模板。 |

## 核心结构事实（框定每次搜索）

1. **监管者修正**：SB 法定电信监管者是 TCSI（依据 Telecommunications Act 2009，隶属 MCA）；无 "TSPL" 官方机构——`TSPL` 仅作搜索词，权威性按实际来源分级。
2. **Honiara 集中**：唯一真实托管/colo 地理是首都区（Capital Territory）；其他一切是海缆、省级机房、telco 核心或捐赠设施。
3. **Noro Data Centre**：Western 省，2025-11-10/13 总理移交（World Bank/FFA/Australia 资助；Reeves International + TCS International 承包商），政府/省级 DR/备份角色（Island Sun B 级功能描述）——A 级移交公告 + 位置，运营/容量细节待补。
4. **国家 DC 管线**：2025-05 Solomon Star 报道总理与华为讨论国家数据中心/数据主权——意向（B），未确认站点，不得计为已建。
5. **海缆站 ≠ DC**：SISCC（CS² + SIDN，2020-02-01 起商用，4 个批发运营商接入）Honiara CLS 与 Auki/Noro/Taro SIDN 登陆为 A 级电信设施；每条 CLS 是潜在 micro-DC/网络节点，需主要证据才记录。
6. **ACS-1 第二条海缆**：AIFFP 资助约 AU$104m；DXN 模块化 CLS 合同 AU$1.2m，设施 2027-04 预期、海缆 2027 底（DCD 2026-08-04，B）；SISCC/AIFFP 完工证据前不计运营。
7. **电力现实**：Honiara/Lungga 是唯一真实电网（Tina River 15 MW 水电 + 66kV 输电约 2028 初完工）；省级为柴油/太阳能混合 outstation——任何大负荷 DC 需电网或专用发电证据。
8. **无 hyperscaler 区域**：AWS/Azure/GCP/OCI 官方表均无 SB；Google 仅经 Bulikula/ACS-1 分支（连接性非云区域）；SINBIP 161 座塔为省级连接设施，仅作 edge-node leads。

## 查询模式（复制粘贴模板见 explorer-official.md / explorer-industry.md）

```text
site:tcsi.org.sb ("data centre" OR "data center" OR "submarine cable" OR IXP)
site:mca.gov.sb ("ICT" OR "digital") ("data centre" OR "national data" OR "e-government")
site:siscc.com.sb ("landing station" OR CLS OR SIDN OR "ACS-1" OR Auki OR Noro OR Taro OR Honiara)
site:solomons.gov.sb ("data centre" OR "Noro" OR "national data" OR SINBIP)
site:solomonpower.com.sb ("data centre" OR "{town}" "powerhouse" OR "grid")
site:lands.gov.sb ("planning" OR "data") OR "Town and Country Planning Board" ("data centre" OR ICT)
"Noro Data Centre" OR "Noro data centre" "Solomon Islands"
"Honiara" ("data centre" OR "data center" OR colocation OR hosting OR "server room")
"Our Telekom" ("data centre" OR "data center" OR "Exchange Building" OR hosting)
"ACS-1" OR "Adamasia" "Solomon Islands" ("landing" OR CLS)
"Solomon Islands" ("AWS region" OR "Azure region" OR "Google Cloud region" OR "OCI region")
site:datacenterdynamics.com "Solomon Islands" OR site:solomonstarnews.com ("data centre" OR "cable")
"{province}" OR "{town}" "Solomon Islands" ("data centre" OR "data center" OR ICT OR broadband)
```

## 官方/监管管线要点（详见 explorer-official.md）

- **MCA/TCSI**：牌照/频谱/竞争/普遍接入；牌照证明授权非设施；`Cable Systems Access, IXP and Caching` 技术报告建议 Honiara IXP（规划中）。
- **Ministry of Lands（Physical Planning）**：Honiara 与省级 Town and Country Planning Boards 审批 Control of Development Areas 内开发；无在线许可库，许可决策只能在当地媒体/议会纪要/捐赠项目文档中找。
- **Solomon Power / MMERE**：Lungga/Honiara 电网、Tina River 输电、省级 powerhouse（Buala、Noro、Fiu 等）；A 级仅在文档点名站点/负荷时。
- **SISCC**：CS²（Sydney–Honiara，2 纤对、最高 20 Tbps）与 SIDN（730 km 国内 Honiara–Auki–Noro–Taro）运营主体（A 级）。
- **政府数字基建**：Noro DC 移交（A）、国家 DC 管线（B 意向）、SINBIP 161 塔（A 级官方塔项目，非 DC）、SiCERT。
- **环评**：MECDM/SPREP 数据门户（Coral Sea Cable PER 等）；Tina River、海缆、省级电厂文档。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **Our Telekom**（Solomon Telekom，ISP 份额约 89%）：运营商文章确认 Honiara 技术场所、数据托管系统、Exchange Building、主数据中心机房与 NOC——A 级机房存在；托管/colo 产品与运营状态待确认。
- **bmobile-Vodafone**（Bemobile，AS132462）：移动运营商，HQ Mendana Ave Honiara；仅网络核心，需托管/colo/DR 证据。
- **SATSOL**：本地 ISP/数字电视/Starlink 转售；DataCenterMap 的 Honiara DC 声明为 C，待 SATSOL 确认。
- **Solomon Tower（STL）**：SINBIP 161 塔组合 + STL-Our Telekom 协议——塔设施非 DC。
- **银行/国企**：CBSI、SINPF/ICSI、商业银行——企业 DR/机房，需媒体/招标证据。
- **现实产出预期**：1–4 个计数设施/lead（Our Telekom 机房、Noro DC、可能的 SATSOL、可能的 Honiara 企业机房）。

## 已知设施/项目与证据状态

| 设施/项目 | 省/地点 | 状态与证据 |
|---|---|---|
| Noro Data Centre | Western（Noro） | 政府/省级 DR 设施，2025-11 移交（A 级公告）；运营/容量待补。 |
| Our Telekom Exchange Building / 主数据中心机房 | Capital Territory（Honiara） | 运营 telco 机房 + NOC（A 级运营商文章）；公共 colo 未确认。 |
| SISCC Honiara CLS | Capital Territory（Lengakiki） | 运营海缆站（A）；`telecom_cable_station`，非零售 DC。 |
| SISCC Auki/Noro/Taro CLS | Malaita / Western / Choiseul | 运营 SIDN 登陆（A）；省际连接节点。 |
| ACS-1 登陆设施 | 站点待定 | 建设中管线（B）：CLS 2027-04、海缆 2027 底预期。 |
| 国家数据中心管线（华为讨论） | 未定 | 意向（B，2025-05）；不计已建。 |
| SATSOL Honiara DC（目录声明） | Honiara | C 级 lead，待 SATSOL 主要证据。 |
| SINBIP 塔站（161） | 全国 | 省级连接设施（A 级官方塔项目）；仅 edge-node leads。 |

## 更新节奏

- 每批次：重跑 TCSI/MCA/SISCC/solomons.gov.sb/Solomon Power 官方面、运营商页（Our Telekom/bmobile/SATSOL）、本地媒体（Solomon Star/Island Sun/Solomon Times/SIBC）与 DCD；盯 ACS-1 站点与 Noro DC 运营细节。
- 每季度：重核云区域缺省；复查国家 DC 管线是否有站点/采购/施工记录。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（9 省 + 首都区粒度）；本 skill 作为国家层参考注入。
