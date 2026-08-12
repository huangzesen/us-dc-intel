---
name: hk-datacenter-methodology
location: scripts/expansion/world/country-skills/HK/SKILL.md
description: 香港数据中心发现与审计方法学（bilingual）。Hong Kong datacenter discovery & audit methodology: enumerate the official/regulatory/cloud pipeline (DPO/ITIB, Town Planning Board, LandsD, BD, EMSD, OFCA, CLP/HK Electric, Companies Registry/HKEX, cloud-region pages) plus industry/trade-press discovery (operators, DCD/SCMP, IXP/cable sources, aggregators). Division model: country (single division “Hong Kong” with 18 District Council districts as granular layer). Read before running HK exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# HK · 香港数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：香港无公开数据中心注册库，也没有可按“data centre”端到端检索的公开规划许可数据库；本方法论通过**官方/监管/云管线（explorer-official.md）**与**行业/厂商/媒体发现（explorer-industry.md）**双轨三角验证（registry-status / triangulation approach），将土地出让、规划申请、楼宇记录、电力、电缆登陆、公司注册与运营商官网证据拼合成可审计的设施清单。本 skill 汇总两份最终审定的探索报告，作为 HK 探索/审计批次的入口。

## 入口

| 文件 | 管线 | 内容 |
| --- | --- | --- |
| explorer-official.md | 官方/监管/云管线 | DPO/ITIB、Town Planning Board、PlanD、LandsD、BD、EMSD/BEAM、EPD、OFCA、CLP/HK Electric、Companies Registry/HKEX、GovHK/DATA.GOV.HK/GeoInfo、云区域官方页、InvestHK/HKTDC/HKPC |
| explorer-industry.md | 行业/厂商发现 | 运营商官网（SUNeVision、Equinix、Digital Realty、NTT、Telehouse、AirTrunk、Vantage 等）、云区域、行业媒体（DCD、SCMP、The Standard、Mingtiandi）、IXP/PeeringDB/海缆、聚合目录 |

## 核心结构事实

1. **行政区划模型**：manifest 为 **country**（单一 division “Hong Kong”），无省级层；落地路由用 **18 个区议会选区（District Council districts）**（中西区、湾仔、东区、南区、油尖旺、深水埗、九龙城、黄大仙、观塘、葵青、荃湾、屯门、元朗、北区、大埔、沙田、西贡、离岛），每条记录须存 `division="Hong Kong"` + `district` + `place/estate`。
2. **无全国性数据中心注册库**：枚举必须联合 TPB 规划申请（DATA.GOV.HK 公开 GIS 数据集 + TPB Statutory Planning Portal）、LandsD 土地出让/租约、BD BRAVO 楼宇记录、电力公司公告、OFCA 电缆登陆/电讯牌照、HKEX/公司注册处文件、运营商官网与可靠媒体。
3. **拼写与语言**：港府与本地媒体用英式 **“data centre”**，中文繁体 **數據中心** / 简体 **数据中心**，全球运营商与云页面常用 “data center”——两种拼写与两种中文形式都要搜。
4. **关键机构**：DPO（数据中心促进组 Data Centre Facilitation Unit，datacentre.gov.hk）；ITIB/施政报告/LegCo（政策线）；Town Planning Board/PlanD（分区计划大纲图 OZP + Section 16/12A/17 规划申请）；LandsD（批租土地，leasehold）；BD（BRAVO 楼宇记录）；EMSD/BEAM Society（BEEO、FWCT、BEAM Plus Data Centres）；EPD/消防处（环境与消防许可）；OFCA（电讯牌照与海缆登陆）；Companies Registry/ICRIS + HKEXnews（实体与上市公司披露）；CLP Power 与 HK Electric（电力双寡头）。
5. **电力双寡头固定特许区**：CLP 供九龙与新界（TKO、葵涌、荃湾、沙田、大埔等主要集群所在）；HK Electric 供港岛与南丫岛（MEGA-i 柴湾、Cyberport 数码港）。网格容量、接电与可再生能源（REC）证据链按此分区追踪。
6. **地权为批租制（leasehold）**：DC 建在政府批地（常含 “data centre” 用途条款）、工业大厦活化改建或私人土地上；2013 年首块将军澳 DC 工业地售出；Sandy Ridge 数据中心设施群 2026-03-02 以 50 年批租授予 Hong Kong Range Intelligent Computing Technology，面积超 110,000 平方米、承诺 3 年内投资 HK$23.8bn、2026 年 3 月动工报道——土地批出不等于已运营设施。
7. **云区域事实（A 级仅限区域存在）**：AWS ap-east-1（3 AZ，2019-04-25 上线）、Azure eastasia（香港）、Google Cloud asia-east2、Alibaba Cloud China (Hong Kong)（3 AZ）、Tencent ap-hongkong、Huawei CN-Hong Kong（4 AZ）；**Oracle OCI 无香港区域**。云区域页不证明任何园区/地址/MW，不得将 AZ 映射到物理区。
8. **可靠性分级规则**：A = 对所述事实负法律/主责的源（DPO、TPB、LandsD、BD、EMSD、OFCA、CLP/HK Electric、公司注册处、HKEX 申报、云官方页、运营商自有设施页、info.gov.hk 官方新闻稿）；B = 可靠二手（DCD、SCMP、The Standard、RTHK、Mingtiandi、Reuters、Bloomberg、FT、Structure Research、C&W、JLL 及可靠的承包商/顾问项目页）；C = 仅作线索（DataCenterMap、Baxtel、Cloudscene、datacenters.com、经纪页、市场研究总数、活动页、社媒、招聘广告）；U = 查证后无支撑，只作临时工作队列且绝不计数。分级只针对该源实际支撑的事实：云页对区域存在为 A、对物理地址不是；运营商页对其公布的设施/地址/状态/营销容量为 A、对未披露坐标或已审计交付 MW 不是；聚合目录即使准确仍为 C。
9. **容量语义**：区分营销 MW、承诺 MW、IT load、电网 MVA、已交付可用容量——分字段保存；目录计数（56–120+ 依口径）只作 C 级市场背景，不得引用为已核实总数。
10. **非设施红线**：政策目标、土地批出、云 AZ 数量、IXP PoP、电缆登陆站均不得计为数据中心设施；MEGA Campus 等为营销伞形品牌，逐栋建筑须各自取证。

## 常用查询模板

```text
site:digitalpolicy.gov.hk "data centre" OR "Sandy Ridge"
site:datacentre.gov.hk "data centre" OR "facilitation"
site:itib.gov.hk "data centre"
site:policyaddress.gov.hk "data centre" OR "數據中心"
site:legco.gov.hk "data centre" OR "數據中心"
site:info.gov.hk "Sandy Ridge" OR "data centre" "tender"
site:ozp.tpb.gov.hk "data centre" OR "數據中心"
site:data.gov.hk "planning applications" "data centre"
site:landsd.gov.hk "data centre" OR "數據中心" OR "Sandy Ridge"
site:bd.gov.hk "data centre" OR "gross floor area"
site:emsd.gov.hk "data centre" OR "Fresh Water Cooling Towers"
site:epd.gov.hk "data centre" OR "數據中心"
site:ofca.gov.hk "submarine cable" OR "海纜"
site:cr.gov.hk "{legal_entity}" ; site:icris.cr.gov.hk "{legal_entity}"
site:hkexnews.hk "{operator}" "data centre"
site:clp.com.hk "data centre" OR "{operator}" "renewable"
site:hkelectric.com "data centre" OR "數據中心"
"{address}" site:map.gov.hk ; site:data.gov.hk "data centre" OR "數據中心"
```

```text
"data centre" OR "data center" OR "datacenter" Hong Kong
"colocation" OR "colo" Hong Kong
"Tseung Kwan O" "data centre" ; "Kwai Chung" OR "Tsing Yi" "data centre"
"Tsuen Wan" "data centre" ; "Chai Wan" OR "Cyberport" "data centre"
"Sandy Ridge" OR "Northern Metropolis" "data centre"
數據中心 香港 / 數據中心 將軍澳 / 數據中心 荃灣 / 數據中心 柴灣
数据中心 香港 / 沙嶺 数据中心
"AWS" "ap-east-1" "Hong Kong" ; "Azure" "eastasia" "Hong Kong"
"Google Cloud" "asia-east2" "Hong Kong" ; "Oracle Cloud" "Hong Kong" region - absence check
"BEAM Plus" "Data Centres" "{operator}" Hong Kong
"{operator}" Hong Kong "data centre" "MW" OR "ready for service"
```

## 官方/监管管线要点（详见 explorer-official.md）

- Sandy Ridge 数据中心设施群：2023 施政报告建议改用途 → 2024 意向书/施政报告扩至约 10 公顷 → 2025-03/04 RFI → 2025-10-10 至 12-31 两阶段招标 → 2025-11 改划完成 → **2026-03-02 批出**（50 年批租、>110,000 平方米、HK$23.8bn）→ 2026-03-28 动工报道。按 意向书/招标/批出/改划/动工/通电 里程碑分别跟踪，通电前不得计为运营设施。
- TPB 规划申请数据集：下载后按用途描述过滤 “data centre”/“data center”/“數據中心”/“数据中心”；注意许多 DC 以既有工业用途运营、无 Section 16 申请，故 TPB 记录缺失不等于设施不存在。
- BRAVO（bd.gov.hk）可按地址查已批准建筑图则（建筑面积/层数，A 级楼宇记录事实），但楼宇记录不标注“数据中心”，需与运营商/租约/媒体证据联查。
- 上市公司披露线：SUNeVision (1686，SHKP 科技臂，官网称 280+ MW 功率容量、约 300 万平方呎 GFA)、HKT (6823)、HKBN (1310)、PCCW (0008)、CITIC Telecom International (1883)；年报为组合构成与所有权 A 级。
- 电缆证据：OFCA 宪报海缆安装通告（如 CMI 的 SEA-H2X 从将军澳登陆，2025–2026 宪报）为 A 级互联事实，只是集群提示，非设施。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 主集群预期：**将军澳工业邨**（SUNeVision MEGA Plus/MEGA IDC、Digital Realty HKG10、NTT FDC、HKEX NGDC、中国移动/电信/联通、HKT、海缆登陆走廊）、**葵涌/青衣**（Equinix HK2、Vantage HKG3、CITIC Telecom Tower、ixTech、Digital Realty HKG11）、**荃湾走廊**（Equinix HK1/HK4–HK6、MEGA Gateway、青衣 AirTrunk HKG1）、**柴湾 MEGA-i**（最互联运营商酒店）、**大埔**（NTT TPDC）、**火炭**（MEGA Two）、**数码港**（AISC，一期 2024-12 运营）、新兴 **Sandy Ridge（北区）** 与屯门/元朗。
- 运营商页面为 A 级事实来源：设施名、地址、营销容量、状态、认证（BEAM Plus/TIA-942/LEED）；聚合目录地址（如 AirTrunk HKG1、Equinix HK2、中国移动 3 Chun Cheong St）经常过时或近似，一律回运营商页确认。
- 行业媒体 B 级：DCD、SCMP、The Standard、RTHK、Mingtiandi、W.Media、Capacity Media、Reuters/Bloomberg/FT；承包商项目页（如 JRP 的 HKEX TKO NGDC、Shielder 的 Global Switch TKO）可作 B 级项目证据。
- IXP/海缆：HKIX（CUHK 运营，亚太最大之一）、AMS-IX/BBIX 香港 PoP、DE-CIX 需用实时 where-to-connect 查询；Submarine Networks/TeleGeography 的登陆点（Tong Fuk 大屿山、TKO 12 Chun Kwong Street 等）；海缆站与 IXP PoP 不得计为数据中心。
- 诚实范围预期：最终 A/B 级设施清单约 **60–120 个**（依去重口径），其中 60–70% 集中于四大集群；香港为亚太最密集市场之一，去重务必以 GeoInfo Map 街道地址为准。

## 维护注意（更新纪律）

- **更新节奏**：每月——DPO/ITIB 新闻室、datacentre.gov.hk、info.gov.hk DC 新闻稿、运营商新闻页；每季度——TPB 规划申请数据集重下载过滤、LandsD 招标结果、OFCA 宪报、HKEXnews 申报（1686/6823/1310/0008/1883）、云区域页（含 OCI 缺失复查）；里程碑事件——Sandy Ridge 及新政府地 DC 招标各阶段、重大运营商开业（Equinix/Digital Realty/Vantage/AirTrunk/GDS）；每半年——重跑全部运营商与聚合线索、复查每个 C 级线索与边界敏感区/电力特区归属；每年——刷新 18 区映射、海缆登陆站清单、云区域列表。
- **来源核验**：复核层必须逐个点击 A 级 URL 确认页面实际载明所引事实；事实按 存在/地址/容量/状态/认证/所有权/云区域/区属/电力特区 分列分级；地址统一用 GeoInfo Map (map.gov.hk) 地理编码。
- **不删除纪律（no-deletion）**：已复核记录不得删除；失效证据改标状态（如地址过时→C/待确认）并保留原始地址/区属/电力特区证据链；降级而非移除。
