---
name: pw-datacenter-methodology
location: scripts/expansion/world/country-skills/PW/SKILL.md
description: |
  Palau (PW) datacenter discovery & audit methodology — how to enumerate, verify, and update Palau datacenter candidates at 16-state granularity. Palau has no public planning-permit portal, no e-permitting database, and no national datacenter association: enumeration starts from PalauGov/OEK law, Foreign Investment Board (FIB) and corporate registry, state governments, the telecom regulator (Bureau of Communications under RPPL 10-17), PPUC/energy approvals, then press. No operational commercial colocation, hyperscale, or cloud-region datacenter was verified: the inventory is telecom/cable-heavy (BSCC PC1/CAP-N at Ngeremlengui, PC2/Echo branch at Ngardmau, CAP-A at Airai, PNCC internal facilities in Koror/Airai), plus one stale commercial proposal (Feb 2022 DC Alliance/Pacific Blockchain non-binding Tier III MOU, 1 MW/200 racks initial, 5 MW/1,000 racks potential — SGX filing). No AWS/Azure/GCP/OCI region. Read this before running PW exploration/audit batches. Routes to explorer-official.md (government/regulator/BSCC/FIB/energy/cloud pipeline) and explorer-industry.md (operator/trade-press/directory/locality recipes).
---

# PW · 帕劳数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：帕劳是**商业前市场**——本轮未验证到任何运营中的第三方托管、超大规模或云区域设施；已验证清单基本是电信/海缆资产：**BSCC PC1/CAP-N**（Ngeremlengui，2017-12 就绪）、**PC2/Echo 支线**（Ngardmau，2026 年中/三季 RFS 预期）、**CAP-A**（Airai 机场接入点）、**PNCC 内部电信设施**（Koror/Airai）。
> 唯一的公共商业 DC 提案是 **2022-02 DC Alliance / Pacific Blockchain 非约束 MoU**（Tier III、初期 1 MW/200 机架、潜力 5 MW/1,000 机架；SGX 申报为 A 级 MoU 条款证据）——无建设/运营跟进，保持 `announced_mou`/`stale_unverified`。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供帕劳探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：PalauGov/州政府/法律门户、BoC/RPPL 10-17 电信监管与 World Bank P160504、BSCC（PC1/PC2/CAP-N/CAP-A 商业计划）、PNCC 与零售 ISP、FIB/企业注册局/商业牌照、PPUC/PEWA 能源与重大负载、云区域缺席核验、16 州覆盖矩阵、设施种子表、分级规则 |
| `explorer-industry.md` | 行业/厂商发现：运营者扫描（BSCC/PNCC/PT Waves/Palau Wifi/DC Alliance/NEC/DXN）、DC Alliance MoU 处理规则、海缆/电信线索、贸易媒体（Island Times/DCD/Submarine Networks/Blue Dot Network/SGX）、目录到一手工作流、区域检索配方、容量提取、预期结果 |

## 核心结构事实（框定每次搜索）

1. **无运营商业 DC**：没有任何第三方 colo/超大规模/云区域验证通过；海缆登陆站/CAP 站点可能含电力、冷却、机架与电信设备，但**不是商业 DC**，除非源称提供 colo/DC 服务。
2. **BSCC 海缆资产（A）**：PC1/BSCCnet（ADB 支持，2017-12 就绪）登陆站/CAP-N 在 **Ngeremlengui**；客户接入点 CAP-N（Ngeremlengui）与 CAP-A（Airai 机场，长期目标）；PC2/Echo Palau 支线（AIFFP 出资）登陆站位于 **Ngardmau**——BSCC 2025-2029 计划预期 PC2 RFS **2026（Q3 前后）**，AIFFP 2026 事实表称 **2026 年中**完成；以 2026 为当前官方预期，除非更新的 BSCC/AIFFP 源取代。
3. **唯一商业提案（A MoU 条款）**：Figtree Holdings（27.5% 关联公司 DC Alliance）与帕劳 Pacific Blockchain 于 2022-02-10 签非约束 MoU，探索 Tier III DC，期限 12 个月，初期 1 MW/200 机架、潜力 5 MW/1,000 机架；至 2026-08-12 无建设/运营跟进——**不得记 `planned`/`under_construction`**，除非出现站点/土地租赁/融资关闭/EPC/建设/电网接入/启用/客户启动的更新 A 或强 B 源。
4. **监管**：RPPL 10-17 建立现代电信监管框架与 **Bureau of Communications（BoC）** 监管者；电信牌照/授权/设备审批是提供网络服务/互联/托管/电信机房的数据中心运营者的相关门槛；World Bank P160504 完结文档提供市场结构语境（非设施证据）。
5. **FIB/注册（外国投资门槛）**：外国 DC 提案需公司注册 + Foreign Investment Approval Certificate——FIB 会议纪要/FIAC 通知是高产核验点；palauregistries.pw 做实体确认（老企业可能不可检索，缺席不假设）。
6. **能源约束**：帕劳柴油依赖极高（PCREEE 评审报告称当时 99.3% 柴油发电，后小幅光伏）；**1-5 MW DC 是重大负载**，应留下 PPUC/PEA/PEWA/IPP/土地租约/新闻痕迹——无此类记录支持保守状态。
7. **云缺席（A 负）**：AWS/Azure/GCP/OCI 官方区域页均无帕劳区域/本地分区/边缘分区；`.pw` 域名、虚拟位置选择器、IP 地理定位、CDN 节点、VPN 端点、托管结账国家列表都不构成设施。
8. **语言**：英语即可；`Palau`/`Belau`/`.pw` + 州名；帕劳语术语无实质增益。
9. **地名防错**：Ngerulmud 在 **Melekeok**；**Ngeremlengui 与 Ngardmau 是两个州**；PC1→Ngeremlengui、PC2/Echo→Ngardmau、CAP-A→Airai——不得因 Koror 是商业中心就改挂。
10. **关岛是区域语境**：GTA TeleGuam/Guam Exchange/Citadel 只作最近商业托管/互联市场解释，**绝不记入帕劳清单**。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§3 / explorer-industry.md §1-§6）

- 政府：`site:palaugov.pw "data center" OR "data centre" OR datacenter`、`site:palaugov.pw "submarine cable" OR "cable landing"`、`site:palaugov.pw "business license" "telecommunications" OR "data"`、`site:palaulaw.gov.pw "telecommunications" OR "Belau Submarine Cable"`。
- 监管：`"Bureau of Communications" Palau telecommunications`、`"Palau" "RPPL No. 10-17"`、`"Palau" "ICT Sector Technical Assistance" P160504`。
- BSCC：`site:belaucable.com "data center" OR colocation`、`site:belaucable.com "CAP-N" OR "CAP-A" OR "Customer Access Point"`、`site:belaucable.com "PC2" OR "Echo" OR "Ngardmau"`、`"BSCC" "Ngeremlengui" "Cable Landing Station"`、`site:belaucable.com "Ready for Service" OR RFS`。
- PNCC/ISP：`site:pnccpalau.com "data center" OR colocation OR NOC`、`"PNCC" Palau "Koror" "server" OR "exchange"`、`"Palau Telecom" OR "PT Waves" "data center" OR "server"`。
- FIB/注册：`site:palaugov.pw/fib "Pacific Blockchain" OR "DC Alliance"`、`site:palauregistries.pw "Pacific Blockchain Corporation"`、`"Foreign Investment Board" Palau "data centre"`。
- 能源：`site:ppuc.com "data center" OR "large customer" OR "MW"`、`site:palaugov.pw "Palau Energy Administration" "tariff" OR "IPP"`、`"Palau" "PPUC" "data center" OR "large load"`。
- 州模板：`"{state}" Palau "data centre" OR "data center" OR datacenter`、`"{state}" Palau "cable landing" OR "submarine cable"`、`site:islandtimes.org "{state}" internet OR cable OR ICT`；高产区变体：`"Koror" OR "Malakal" Palau "PNCC" OR "server room"`、`"Airai" Palau "CAP-A" OR airport`、`"Ngeremlengui" Palau "CAP-N"`、`"Ngardmau" Palau "Echo" OR "PC2" OR "DXN"`、`"Ngerulmud" OR "Melekeok" Palau government ICT`。
- MoU 负控制：`"DC Alliance" "Palau" construction OR commissioned OR operational`、`"Pacific Blockchain Corporation" Palau "data centre" "construction"`、`"Palau" "Tier III" "data centre" -MOU`、`site:links.sgx.com "DC Alliance" "Palau"`。
- 目录/假阳性：`site:datacentermap.com Palau "data center"`、`"Palau" "dedicated server" OR VPS -Guam`、`"Ngerulmud" "dedicated server" OR VPS OR hosting`。

## 官方/监管管线要点（详见 explorer-official.md）

- **PalauGov/州政府/法律（A）**：验证州管辖权、公告、采购、商业牌照、政府 ICT/机房采购；16 州名显式逐一搜索，不凭国家级查询推断缺席。
- **BoC/RPPL 10-17（A 框架）**：电信牌照/授权/设备审批门槛；World Bank P160504 完结文档（A 范围，非设施）。
- **BSCC（A）**：belaucable.com 官方页/About/商业计划（FY2022-2026、FY2025-2029）；PC1/CAP-N、PC2/Echo、CAP-A 状态与 RFS；采购/公告页。
- **PNCC（A 运营者）**：移动/互联网/电话/数字电视在运营；WiFi 材料证明服务分布，不建立 DC 清单。
- **FIB/注册/牌照（A 程序门槛）**：FIB 法律/FIAC 表格/会议纪要/办公地点；State Dept 投资气候声明（外国企业需公司注册+FIAC）。
- **PPUC/PEWA（A 佐证）**：柴油依赖事实、IPP 法规、重大负载/电价/燃料调整程序；**多兆瓦设施应产生官方或新闻可见的电力证据**。
- **云缺席（A）**：四家官方区域页作负控制；转售托管不升超大规模。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **运营者扫描**：BSCC（A，国有批发海缆/光纤，核心 DC 邻近资产）、PNCC（A，固网零售，交换/机房线索）、Palau Telecom/PT Waves（B 除非官方页，零售无线/互联网）、Palau Wifi（B/C，热点不是 DC）、DC Alliance（SGX A MoU 条款/dcalliance.com.au）、Pacific Blockchain（A 若注册/FIB）、NEC（A 厂商稿，海缆供应语境）、DXN（A 官方，PC2 模块化登陆站设备，非商业 DC）、GTA TeleGuam/Guam Exchange（仅关岛语境，排除）。
- **贸易媒体（B）**：Island Times（本地主源：MoU/BSCC 容量/PC2 延迟/能源/网络安全）、DCD、Submarine Networks（PC1/PC2 路由与延迟史）、SubTel Forum、Islands Business、Blue Dot Network（PC2 认证/项目状态，A/B）、Pacific Island Times/RNZ Pacific/PACNEWS/PDN/Marianas Variety；SGX（A 一手申报）。
- **目录（C）**：Baxtel/DataCenterMap/Datacenters.com/Cloudscene 仅负控制/种子；声称帕劳设施的目录条目须运营者官方页/地址/注册/FIB/公用事业许可/具名媒体佐证。
- **假阳性**：`Palau data center`、`Melekeok dedicated servers`、`Ngerulmud VPS` 常为 SEO 位置页——C 级假阳性，除非关联运营者地址/注册/许可/具名设施。
- **容量提取**：商业 DC 容量只有 DC Alliance MoU 数字（1 MW/200 机架→5 MW/1,000 机架，**提案容量**）；海缆容量（波长/支线/RFS/批发带宽）按电信容量不按 `capacity_mw`；PNCC/BSCC 内部机房用 null 除非给出 UPS/发电机/IT 负载/机架数据。

## 来源分级

- **A** = 一手：政府/监管者/州有运营者/公用事业/注册局/云厂商官方页/多边贷款机构项目文件/交易所申报（SGX）。
- **B** = 可信本地/区域/贸易媒体（具名当事方与日期）：Island Times、DCD、Submarine Networks、Islands Business、Pacific Island Times、RNZ Pacific。
- **C** = 目录/市场/SEO 托管页/未验证营销页/无主链转载；只作线索或负控制，不用于建立设施。
- **A 源 ≠ A 设施状态**：SGX 申报对 MoU 存在与条款是 A，但对运营状态只支持 `announced_mou`；海缆登陆站/CAP = 电信基础设施（基础设施注记，不分类为商业 DC）；SEO 假阳性记 `false_positive`/C 并注明缺失证据。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=PW，divisions=16 州）。
2. 全国扫描：PalauGov/法律门户/BoC/FIB/注册局/PPUC/PEWA/BSCC/PNCC。
3. 16 州查询块逐州运行；每州标 `covered`（即使负结果），低产区注明原因。
4. 每个正向线索先分类资产类型：`commercial_datacenter` / `government_server_room` / `telecom_exchange` / `cable_landing_station` / `customer_access_point` / `office_only` / `seo_false_positive`，再定 DC 状态。
5. 运营状态至少一个 A 源；只有贸易媒体则状态封顶 announced/proposed（除非媒体引用/链接主文件）。
6. FIB 会议纪要/注册查外国科技/DC 实体；PPUC/PEA/PEWA 查重大负载/IPP/可再生/电价程序；官方区域页+目录作负控制。
7. 容量只记源明确声明的 IT 负载/机架/建筑面积/电信容量；不把海缆带宽或发电量换算成 DC MW。
8. 输出与 world 探索同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；DC Alliance 状态 `announced_mou`（提案容量入 notes）。
9. 遵守 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：批量复核帕劳数据中心（16 州粒度）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：PC2/Echo RFS（2026 中/Q3 官方更新）、DC Alliance/PBC 是否有终止/续签/绑定协议或新进展、FIB/注册中 Pacific Blockchain 法律状态、PNCC 是否发布机房/NOC 信息、政府 Ngerulmud 服务器机房采购记录、PPUC 是否出现 DC 级负载申请、任何目录条目是否落到关岛/新加坡等区域市场。
