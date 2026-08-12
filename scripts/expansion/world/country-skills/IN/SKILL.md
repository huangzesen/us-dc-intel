---
name: in-datacenter-methodology
location: scripts/expansion/world/country-skills/IN/SKILL.md
description: |
  India (IN) datacenter discovery & audit methodology — how to enumerate, verify, and update India datacenter projects at state/UT + district granularity (763 district-level targets in the current manifest). India has no single planning-permit or facility registry: enumeration triangulates official single-window approvals (NSWS + state portals), environmental/pollution clearances (PARIVESH / SEIAA / SPCB CTE-CTO), power & grid trails, land/SEZ allotments, corporate filings (MCA/NSE/BSE), hyperscaler official region pages, and operator facility pages. Read this before running IN exploration/audit batches. Routes to explorer-official.md (official/regulatory/cloud pipeline) and explorer-industry.md (trade press / vendor discovery).
---

# IN · 印度数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：印度**没有**统一的数据中心设施注册库或全国性规划许可库（无 FOIA、无中国式投资备案平台），不能按美欧方式直接枚举。
> 印度枚举靠**多轨迹交叉三角测量**：工业单窗审批（NSWS + 各邦门户）、环评与排污许可（PARIVESH/SEIAA-SEAC/邦污染委员会 CTE-CTO）、电力与电网批复、土地/产业园区/SEZ 划拨、上市披露（MCA/NSE/BSE）、云厂商官方区域页、运营商官方站点。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供印度探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：NSWS、CPPP/eProcure 招标、PARIVESH 环评、MeitY AMBUD、SEZ、MCA/NSE/BSE 披露、邦级单窗/排污/电力/土地门户（14 邦矩阵）、云区域官方页、运营商官方设施页、763 区县分桶配方 |
| `explorer-industry.md` | 行业/厂商发现：DCD/ET Telecom/DataQuest/Voice&Data/W.Media/Dgtl Infra 贸易媒体、NASSCOM/ASSOCHAM/DCAI 行业协会、运营商与云厂商页面、印地语（天城文）查询模板、邦/区县枚举矩阵、按事实分级规则 |

## 核心结构事实（框定每次搜索）

1. **无全国统一许可库**：数据中心通常按“建筑/建设/IT-ITES/工业基础设施”而非单一“数据中心牌照”审批；单一门户查无 ≠ 项目不存在。
2. **官方管线五条轨迹**：① 单窗审批（NSWS + MAITRI/TG-iPASS/Nivesh Mitra/TN Single Window/GO SWIFT/Silpa Sathi/Invest Karnataka 等）；② 环评排污（PARIVESH、SEIAA/SEAC 纪要、SPCB CTE/CTO）；③ 电力（邦电力公司连接/专用变电站/开放准入/CEIG、SERC 订单）；④ 土地园区（MIDC/SIPCOT/TSIIC/APIIC/UPSIDA/YEIDA/NOIDA-GN/GIDC/KIADB/HSIIDC/WBIDC/IDCO/KINFRA/SEZ BoA）；⑤ 上市披露（MCA/NSE/BSE/SEBI）。
3. **云区域 = 城市级存在证据（A 级），不等于设施地址**：AWS Mumbai `ap-south-1` / Hyderabad `ap-south-2`；Azure Central India (Pune) / South India (Chennai) / West India (Mumbai) / India South Central (Hyderabad)；GCP Mumbai `asia-south1` / Delhi `asia-south2`（AP 在建）；OCI Mumbai / Hyderabad；Jio+Azure 合作区域（Gujarat/Maharashtra，RIL 披露单设施至多 7.5 MW IT 设备）。
4. **容量语义**：优先官方 IT load MW（运营商规格页、电力订单、EC/概念图、年报、交易所披露）；建筑面积/机架数为二级；“园区 MW”常为多年分期规划，必须与 live/已投产 MW 分开存储。
5. **MeitY AMBUD**：云服务商入驻要求印度境内数据中心且至少 100 机架运营或 1 MVA IT load——政府云资格证据，非商业设施注册表。
6. **拼写与语言**：英式 `data centre` 多于美式 `data center`，两者加 `datacenter` 都要搜；印地语（天城文）用于北方/中部区县发现，不作最终证明。
7. 优先级地理：Mumbai/Navi Mumbai/Pune、Hyderabad、Chennai、Delhi NCR/Noida/Greater Noida/Manesar、Bengaluru、Kolkata、Gujarat/GIFT、Visakhapatnam、Bhubaneswar、Kochi。

## 查询模式（复制粘贴模板见 explorer-official.md §2-§4 / explorer-industry.md §5）

- 中央官方：NSWS Know Your Approvals（行业选 `IT/ITES`、`Data Centre`、`Building Construction`、`Industrial Infrastructure`）；CPPP 关键词 `"data centre"` `"data center"` `"state data centre"` `"DR site"` `"GIS substation"` `"DG set"`；环评 `site:parivesh.nic.in "Data Center Construction Project"`；SEZ `site:sezindia.gov.in "data centre"`；披露 `site:bseindia.com "{operator}" "data centre"`、`site:nseindia.com "{operator}" "data center"`。
- 邦级模板：`site:{state-portal} "data centre"`、`site:{spcb} "data centre" "Consent to Establish"`、`site:{utility} "data centre" "substation"`、`site:{serc} "data centre" "open access"`、`site:{land-agency} "data centre" "allotment"`、`site:{fire} "{operator}" "fire NOC"`、`site:{municipal} "data centre" "occupancy certificate"`。
- 行业模板：`site:datacenterdynamics.com/en/news India "{city}" "data center" "MW"`、`site:telecom.economictimes.indiatimes.com "{city}" "data center"`、`site:w.media "{operator}" "{city}"`、`site:dqindia.com "{operator}" "data centre"`。
- 印地语模板：`"डेटा सेंटर" "शिलान्यास" "नोएडा"`、`"{जिला}" "डेटा सेंटर पार्क" "भूमि आवंटन"`、`site:amarujala.com "{जिला}" "डेटा सेंटर"`。
- 云 pivot：`"Amazon Data Services India" "Environmental Clearance"`、`"Microsoft" "India South Central" Hyderabad`、`"Google" "data center" "Mumbai" "environmental clearance"`、`"Jio" "Azure" "Gujarat" "Maharashtra"`。

## 官方/监管管线要点（详见 explorer-official.md）

- 中央：NSWS（KYA 按邦→区县）、CPPP/eProcure（政府/自建设施与 EPC/电气工程招标，A 级）、PARIVESH 2.0/旧 EC 门户（项目按 8(a) 建筑/建设或区域开发申报时出现，**高精度低召回**）、MeitY AMBUD、SEZ Online/sezindia（Chennai/Pune/Navi Mumbai/Noida/Bengaluru/Hyderabad/GIFT/Kochi/Kolkata）、MCA/NSE/BSE/SEBI（SPV 发现、年报、capex 承诺）。
- 邦级四步：Step A 投资/单窗门户扫（优先 Maharashtra、Telangana、Tamil Nadu、UP、Karnataka、Gujarat、Haryana、AP、Odisha、WB、Kerala、MP、Rajasthan、Delhi NCT）；Step B 邦污染委员会 CTE/CTO（常是项目越过 MoU 阶段的最佳证据）；Step C 电力/开放准入（HT/EHT 连接、专用变电站、CEIG）；Step D 土地/规划/消防（MIDC/SIPCOT/TSIIC/…、市政建筑/入住许可、消防 NOC）。
- 实例如：PARIVESH 已见 Amazon Data Services India Telangana Ranga Reddy “Data Center Construction Project” 记录（SIA/TG/INFRA2/503345/2024）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 贸易媒体高信号源：DCD India（B+）、ET Telecom/ET DataCenters（B）、DataQuest（B-/C+）、Voice&Data（B-）、W.Media（B）、Dgtl Infra（B）；对“事件存在”（签约/开工/发布）可靠，容量账须回到一手源。
- 行业协会/政策：NASSCOM、MeitY 数据中心政策草案（2020，NITI for States）、Invest India、DCAI、ASSOCHAM 数据中心委员会、ICRIER Policy Bank；C&W/JLL/CBRE/Colliers 报告仅作城市级聚合上下文。
- 运营商种子（A=官方存在/B=容量）：STT GDC、CtrlS、Nxtra by Airtel、Sify、NTT/Netmagic、Yotta、AdaniConneX、Digital Connexion、Equinix、Web Werks/Iron Mountain、CapitaLand、PDG、Pi/ESDS/NxtGen/E2E/NeevCloud。
- 状态动词必须区分：`announced` / `signed MoU` / `acquired land` / `commenced construction` / `launched` / `operational` / `full build-out`；把“全文园区容量”当当前容量是常见失败模式。

## 来源分级

- **A** = 官方/一手/法律可问责：NSWS 批准证书、邦单窗订单、PARIVESH EC/修正、SEIAA/SEAC 纪要、SPCB CTE/CTO、邦电力/SERC 订单、工业用地划拨、开发局建筑/入住许可、消防 NOC、SEZ BoA 纪要、云区域官方文档、运营商官方设施页、BSE/NSE/MCA/年报披露、CPPP/邦 eProc 招标。
- **B** = 强二级：PIB/邦政府新闻稿、投资促进 MoU 页、成熟贸易媒体（DCD、ET Telecom 数据中心板块）、行业协会报告、与官方源匹配的聚合器（datacenters.com/Baxtel/DataCenterMap）。
- **C** = 弱/未验证：LinkedIn/Facebook、顾问政策摘要、无出处地图、地方 MoU 报道、签约仪式、宣传册；聚合器默认 C，除非官方页/权威记录/披露核实。
- 状态语义：MoU/投资意向=C；土地划拨/建筑许可/CTE=已许可未动工；EC/CTE/电力接入/EPC 招标=强在建前信号；CTO/入住/消防运营 NOC/设施页上线=运营或近运营；云区域上线=城市级云容量（非设施地址）。
- **政策目标 ≠ 项目容量**：邦级 GW 目标、峰会“园区 MW”不得计为管线，须有具名投资者+场地；IT load 与设施功率/MVA 要按原文存单位。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=IN，divisions=邦/UT+区县，763 区县目标）。
2. 建种子：运营商官方位置页（STT/CtrlS/Nxtra/Sify/NTT/Yotta/AdaniConneX/Digital Connexion/Equinix/Web Werks-Iron Mountain/CapitaLand/PDG/Pi/ESDS/NxtGen/E2E/NeevCloud）+ 云区域（AWS/Azure/GCP/OCI/Jio）+ 贸易媒体首扫（DCD/ET/DataQuest/Voice&Data/W.Media/Dgtl Infra）。
3. 对每个 division 按官方管线执行：邦单窗/投资门户 → PARIVESH/SEIAA → SPCB CTE/CTO → 电力/变电站/开放准入 → 土地/规划/消防 → CPPP/招标 → 交易所/年报。
4. 实体解析：品牌→法律 SPV（MCA/披露），按 (母公司, 项目主体/SPV, 园区名, 地块/村庄, 阶段) 去重；注意别名（Netmagic=NTT、GPX Mumbai=Equinix MB1/MB2、Web Werks=Iron Mountain、BAM Digital Realty=Digital Connexion）与拼写（Data Centre/Data Center/Datacenter/IT-ITES/server farm）。
5. 输出与 world 探索同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；无项目 division 写 `no_projects: true`。容量区分 `operational` / `under_construction` / `planned_full_buildout_mw`。
6. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12 02:05Z）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：50× codex terra agent（max thinking）每 agent 分批复核印度数据中心（state-first → district bucketing）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Karnataka 数据中心政策终稿、Gujarat 2026 政策通知、Microsoft Hyderabad（India South Central）2026-08 上线后的设施证据、Visakhapatnam 巨型项目需官方批复才能升级。
