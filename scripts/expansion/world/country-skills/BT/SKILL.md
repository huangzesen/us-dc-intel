---
name: bt-datacenter-methodology
location: scripts/expansion/world/country-skills/BT/SKILL.md
description: |
  Bhutan (BT) parent-level methodology for data-center enumeration at dzongkhag granularity (20 dzongkhags).
  Bhutan has no public national datacenter register or searchable planning-permit database; enumeration joins
  GovTech/GDC, DCS/Thimphu TechPark, DHI/Bitdeer official material, Gelephu Mindfulness City Authority
  announcements, BICMA licensing, BPC/DGPC/BEA energy records, cloud-region pages, and local/trade press.
  Confirmed anchors: GDC/Neyduetewa, DCS, btIX (Thimphu), Bitdeer Gedu (Chhukha, 100 MW online crypto),
  Bitdeer Jigmeling (Sarpang, 500 MW online crypto). Planned: national 40-50 MW datacenter roadmap (2027
  target), DHI AI proposal, SATO-GMCA AI compute campus (LOI). Four asset classes must not be merged:
  government hosting, commercial colo, crypto-mining, planned AI/GPU. No hyperscaler public region.
  Routes to explorer-official.md (government/regulator/utility pipeline) and explorer-industry.md
  (press/operator/mining-disclosure pipeline).
---

# BT · 不丹数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：不丹没有公开的国家数据中心登记册或可检索的规划许可数据库；枚举必须拼接 GovTech/GDC、DCS/廷布科技园、DHI/Bitdeer 官方材料、Gelephu 正念城管理局（GMCA）公告、BICMA 许可、BPC/DGPC/BEA 能源记录、云区域页面与本地/行业媒体。已确认锚点：GDC/Neyduetewa、DCS、btIX（廷布）、Bitdeer Gedu（Chhukha，100 MW 在线加密矿）、Bitdeer Jigmeling（Sarpang，500 MW 在线加密矿）；规划中：国家 40-50 MW 数据中心路线图（2027 建设目标）、DHI AI 提案、SATO-GMCA AI 计算园区（LOI）。**四类资产不得混并**：政府托管、商业 colo、加密货币矿场、规划 AI/GPU。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供不丹探索与复核批次使用。

## 入口

| 文档 | 用途 |
|---|---|
| `explorer-official.md` | 官方/监管管线：GovTech/GDC、DCS、DHI、BICMA、BPC/DGPC/BEA、MoIT/BCTA、GMCA、规划/土地、云区域阴性对照、20 区工作流 |
| `explorer-industry.md` | 行业管线：DCD/The Bhutanese/Kuensel/BBS、Bitdeer IR/SEC 披露、SATO/GMCA、目录处理、状态观察清单、逐区模板 |

## 核心结构事实（框定每次搜索）

1. **无登记册**：不丹没有公开的国家数据中心登记册或可检索的国家规划许可数据库；枚举 = 政府/监管/公用事业/运营商官方材料 + 行业/本地媒体 + 能源记录 + 云区域阴性对照。
2. **20 个宗（dzongkhag）**：Paro, Chhukha, Haa, Samtse, Thimphu, Tsirang, Dagana, Punakha, Wangdue Phodrang, Sarpang, Trongsa, Bumthang, Zhemgang, Trashigang, Monggar, Pema Gatshel, Lhuentse, Samdrup Jongkhar, Gasa, Trashi Yangtse。
3. **四类资产不混并**：政府托管（GDC）、商业 colo（DCS）、加密货币矿场（Bitdeer）、规划 AI/GPU（SATO/DHI/国家路线图）——即使共用同一水电叙事，也是独立记录。
4. **廷布科技园（Thimphu TechPark）是核心**：GDC/Neyduetewa（2017 年运营，2023 年托管 200+ 政府系统，A）、DCS Tier 2/3 IDC（双馈线来自 Olakha/Semtokha 变电站，ABB 变压器，A）、btIX（PeeringDB ix/2355，IX 不是 DC）。
5. **Bitdeer 状态已更新**：2026 年 Bitdeer 公开材料列 **Gedu（Chhukha）100 MW 在线加密矿** 与 **Jigmeling（Sarpang）500 MW 在线加密矿**；不要再用旧材料把 Jigmeling 描述为仅规划；资产类别记为 `crypto/mining`，非商业 colo。
6. **规划管线三件套**：①国家 40-50 MW / USD 450M 数据中心（21 世纪经济路线图，当地报道建设目标 2027，B 至官方选址/许可）；②DHI AI 数据中心提案（2026 Invest Bhutan 峰会，A 战略/B 设施细节）；③SATO-GMCA AI 计算园区（LOI 于 2026-06-20 生效、2026-07-06 公告；初始 5 MW、目标 100 MW 坚实水电、可能 500 MW 路径——均为 planned，不得计入运营容量）。
7. **电力是门控信号**：不丹水电使该国具吸引力，但冬季从印度进口与径流式季节性是需要记录的实质限制；保持 `gross electrical capacity`、`IT load`、`mining load`、`substation/feed`、`planned scale` 分字段；水电厂/变电站不是数据中心。
8. **无超大规模区域**：官方 AWS/Azure/GCP/OCI 列表无不丹区域；"不丹云" 声明 = GDC 政府托管、DCS 商业服务、电信托管、境外区域服务或未建成的规划 AI 设施。
9. **语言**：英文是实用检索语言（政府/监管/电信/能源/ICT 材料通常为英文）；宗卡语（Dzongkha）低产。
10. **状态动词必须精确**：`LOI`、`proposal`、`feasibility study`、`roadmap target`、`under construction`、`energized`、`online`、`operational` 在不丹语境含义不同。

## 查询模式（复制粘贴模板见 explorer-official.md §2/§3/§4/§5/§6、explorer-industry.md §1/§2/§5/§6）

```text
site:tech.gov.bt ("Government Data Centre" OR "GDC" OR "cloud" OR "GovNet")
site:support.neyduetewa.gov.bt ("server request" OR "Government Data Center")
site:dcs.bt ("data centre" OR "colocation" OR "Tier" OR "Olakha" OR "Semtokha")
site:thimphutechpark.bt ("data centre" OR "DCS" OR "btIX")
site:btix.bt ("launch" OR "Thimphu TechPark")
site:ir.bitdeer.com Bhutan ("Gedu" OR "Jigmeling" OR "MW" OR "Online")
site:dhi.bt ("Bitdeer" OR "Green Digital" OR "AI Data Centers")
site:gmc.bt ("SATO" OR "AI data center" OR "Green Technology Valley")
site:bysato.com Bhutan ("AI data centre" OR "Gelephu" OR "100 MW" OR "500 MW")
site:bicma.gov.bt ("ISP License" OR "online licensing" OR "cloud")
site:bpc.bt ("data center" OR "substation" OR "Olakha" OR "Semtokha")
site:drukgreen.bt ("data center" OR "AI" OR "mining")
site:moenr.gov.bt ("data center" OR "AI" OR "National Energy Policy")
site:moit.gov.bt ("data center" OR "server room")
site:thimphucity.bt ("construction approval" OR "building permit")
site:nlc.gov.bt ("Gelephu" OR "Jigmeling" OR "Gedu" OR "TechPark") ("lease" OR "land")
site:datacenterdynamics.com/en/news/ Bhutan ("data center" OR "AI" OR "Bitdeer" OR "SATO")
site:thebhutanese.bt ("data center" OR "AI" OR "Jigmeling" OR "Gedu")
site:kuenselonline.com ("data center" OR "GMC" OR "Bitdeer" OR "SATO")
"Government Data Centre" OR "Neyduetewa" Thimphu
"Bitdeer" ("Gedu" OR "Jigmeling") ("MW" OR "online" OR "crypto")
"SATO" "Bhutan" ("AI data center" OR "Gelephu" OR "100 MW")
"21st Century Economic Roadmap" "data center" Bhutan
"{dzongkhag}" ("data center" OR "data centre" OR "server room" OR cloud)
"AWS" "Bhutan" ("region" OR "availability zone" OR "local zone")
```

## 官方/监管管线要点（详见 explorer-official.md）

- **GovTech 机构**（tech.gov.bt，DITT 继任者）：GDC、GovNet、云服务、政府托管、AI 政策锚点；ITU 2023 演示称 GDC 于 2017 年运营、与 DCS 并置（GDC 1,000 sq ft + DCS 租赁 2,500 sq ft）、当时托管 200+ 政府系统。
- **DCS**：廷布科技园内 Tier 2/3 互联网数据中心，商业 colo/托管/备份/连接；双馈线（Olakha/Semtokha 经独立路由）。
- **DHI**：国家持股/投资公司；Green Digital/Bitdeer 伙伴关系、科技园生态、AI 数据中心投资框架（10X 路线图是战略意图，不是站点记录）。
- **BICMA**：电信/ICT/媒体监管机构；2023 在线许可公告（A 流程）；2024 Starlink ISP 许可是连通性许可示例，不是 DC 证据。
- **电力（BPC/DGPC/BEA/MoENR）**：BPC 配电/输电/变电站/OPGW；DGPC 发电/水电官方来源；BEA 电力许可/电价监管；MoENR 2025 国家能源政策目标 2040 年 25,000 MW（水电 20,000 + 太阳能 5,000）——只作市场背景。
- **规划/土地**：MoIT/BCTA（建筑许可流程 A，非项目登记册）、Thimphu Thromde 施工批准（GDC/DCS/TechPark 背景）、NLC 地块/Thram、GMCA（gmc.bt，A 区/投资公告）；SATO 项目在 GMCA 发布土地租赁/施工/电力分配证据前保持 LOI/planned。
- **云区域**：AWS/Azure/GCP/OCI 官方页 = 无不丹公共区域（A 阴性对照）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **Bitdeer IR/SEC**：Gedu/Jigmeling 容量与状态的最高置信来源（A）；把电气容量/加密矿用法与 IT 负载分开。
- **SATO Technologies**（bysato.com）：LOI 一手来源（A 公告）；5/100/500 MW 是规划路径数字，直到电力分配/租赁/施工/通电证据出现。
- **本地媒体**：The Bhutanese（路线图 40-50 MW、DHI 提案、Jigmeling 细节，B+；具名官员引语 A-）、Kuensel/BBS/Business Bhutan（B）；GovInsider（B）；The Block/CoinDesk/Cointelegraph（B/C，公共公司申报摘要强、精确地址弱）。
- **电信**：Bhutan Telecom（DrukNet/光纤骨干）与 Tashi InfoComm/TashiCell 为电信服务 A、设施细节 C（交换/核心网络仅线索）。
- **NewEdge Technologies**：DCS 合资伙伴，C+ 线索。
- **目录纪律**：Baxtel/DataCenterMap/Cloudscene 为 C；用目录找名字后必须用 DCS/Bitdeer/GMCA 官方材料验证。

## 来源分级

- **A** = 官方/主要：政府、监管机构、公用事业、运营商官方页、公司申报（Bitdeer IR/SEC）、官方云区域页、IX 事实用 PeeringDB。
- **B** = 具名运营商/站点/容量的强二级或行业来源：DCD、The Bhutanese、Kuensel、BBS、Business Bhutan、GovInsider、CoinDesk/The Block/Cointelegraph（引述具名矿场申报或官方声明时）。
- **C** = 弱目录、市场报告、社交帖子或推广文章，仅作线索：Baxtel、DataCenterMap、Cloudscene。
- 状态映射：`operational/online` = GDC/DCS/btIX/Bitdeer（当前材料支撑）；`planned/proposal` = DHI AI、国家路线图 DC、SATO/GMC；`lead only` = 电信交换、银行/政府服务器机房、工业园、水电项目、光纤路线、无设施证据的云服务可用性。
- 容量纪律：电气 MW、IT MW、加密矿 MW、坚实电力分配、未来扩展路径分开；水电能力 ≠ DC IT 负载。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL 中的 BT 记录与种子（GDC、DCS、btIX、Bitdeer Gedu/Jigmeling、SATO、DHI 提案、路线图 DC）。
2. 每宗四遍法：①国家种子遍（GovTech/GDC、DCS、DHI/Bitdeer、GMCA/SATO、BICMA、BPC/DGPC/BEA、云区域）②具名站点遍（GDC/Neyduetewa、TechPark、Gedu、Jigmeling、Gelephu、GMC、BITC、Olakha、Semtokha）③区遍（dzongkhag 模板，按城镇/公园/地标映射）④验证遍（分类：政府 DC/商业 colo/加密矿/规划 AI/IX/电信交换/假阳性）。
3. 17 个低概率宗记录阴性扫描而不是跳过；水电项目本身不是数据中心。
4. 输出 schema：`{country_code: BT, country_name: Bhutan, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`（notes 含 asset_class 与容量细分）；阴性宗 `no_projects: true`。
5. 不动 explorer-*.md，NO-DELETION。

## 待办（2026-08-12）

- [ ] SATO-GMCA：寻找 GMCA 土地租赁/施工/电力分配证据以升级 LOI。
- [ ] 国家 40-50 MW 数据中心：追踪官方选址、土地、许可、电力证据（2027 目标）。
- [ ] DHI AI 数据中心提案：从 2026 Invest Bhutan 峰会材料提取商业模式与电力主张。
- [ ] Bitdeer：每季度用 IR 材料刷新 Gedu/Jigmeling 状态与容量。
- [ ] DCS：如需要精确机架/MW 用运营商材料核实。
- [ ] 云区域阴性对照：每次运行复查。
