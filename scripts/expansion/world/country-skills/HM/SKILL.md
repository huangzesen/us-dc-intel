---
name: hm-datacenter-methodology
location: scripts/expansion/world/country-skills/HM/SKILL.md
description: 赫德岛和麦克唐纳群岛数据中心双线查询方法论（官方/监管/云管线 + 行业/厂商/媒体发现），含 division 模型、verified-negative 结论与查询模板；English: dual-line datacenter discovery & audit methodology for Heard Island and McDonald Islands (official/regulatory/cloud pipeline + industry/vendor/media discovery), with division model, verified-negative conclusion and query templates. 运行 HM 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。
---

# HM · 赫德岛和麦克唐纳群岛数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> **目的**：为赫德岛和麦克唐纳群岛（Heard Island and McDonald Islands, HM）的数据中心探索与审计提供统一双线方法论。官方/监管/政府管线与行业/运营商/基础设施管线互为三角验证，结论为 **verified-negative**：截至 2026-08-12 复核，无可计数商业数据中心、政府数据中心、公有云区域、海缆登陆站、本地电信运营商设施或大型电力基础设施。本文件由 codex 审核定稿的两份 explorer 合并而成，细节以 `explorer-official.md`（官方线）与 `explorer-industry.md`（行业线）为准。

## 入口

| 文件 | 职责 | 内容摘要 |
|---|---|---|
| `explorer-official.md` | 官方/监管/云管线：验证与定稿 | AAD（antarctica.gov.au）、DCCEEW/legislation、AFMA HIMI Fishery、ACMA RRL、IANA `.HM`/registry.hm、UNESCO、官方云区域清单；无市场论证、每轮复核清单、已验证阴性 |
| `explorer-industry.md` | 行业/厂商/媒体发现：线索与预筛 | 数据中心/云目录负向对照、网络/海缆/电信（Submarine Cable Map、APNIC、PeeringDB、BGP）、渔业/船舶/科考排除、行业查询模板、假阳性清单 |

## 核心结构事实

1. **行政区划模型**：manifest 为单一 division — `["Heard Island and McDonald Islands"]`（subnational_type=country，ISO 3166-1: HM/HMD/334）。行业枚举不再拆分岛屿或营地；地理亚区只用于 tagging 不做 division。
2. **治理与现状**：澳大利亚外部领地，由澳大利亚南极局（AAD）管理，享世界遗产和海洋保护区地位，官方明确 “unoccupied by humans”；人类活动受极端隔绝、恶劣天气和海况限制 — 自 1855 年以来 Heard Island 约 240 次 shore-based visits，McDonald Island 仅 1971 与 1980 两次登陆；活动主要是科研、管理、监督和少量受许可访问；ANARE/AAD 曾在 Atlas Cove 运行研究站（1947-1955），属历史设施。
3. **法律与监管**：环境/许可/世界遗产走 DCCEEW 与 `legislation.gov.au`（含 Heard Island and McDonald Islands Act）；主要经济活动是受管制渔业（AFMA HIMI Fishery / CCAMLR，船载设备不计为陆地设施）；ACMA RRL 复核无线电牌照（预期无 HM 商业电信设施）；IANA `.HM` 委托给 HM Domain Registry 且 registry.hm 显示可注册（域名开放注册只说明命名资源存在，不是本地网络/机房/市场证据）。
4. **互联与云**：无已知海床光缆登陆站、无本地 ISP/IXP/移动网络、无 HM 专属 MCC/MNC 或陆地 PLMN（卫星/海事/航空国际 MCC 不代表本地移动网络）；Iridium/Inmarsat/Starlink 等只能作科考/船舶/应急通信背景；AWS/Azure/GCP/OCI 官方区域清单均无 HM region/zone/edge location（澳大利亚本土 Sydney/Melbourne/Canberra 等不得归入 HM）。
5. **设施/项目种子（2026-08 复核基线）**：**无**。有效设施清单预期为空表，输出 verified-negative；任何候选必须满足 — 至少一份 A 级来源点名设施/项目、来源同时给出名称/功能/位置/运营方、能排除 AADC/AAT 南极站/Kerguelen/McDonald's 品牌/船载设备/临时科考仪器等假阳性、MW 级负载声明必须有 A 级电力/许可/采购或运营商证据。
6. **语言与词汇**：英文与中文双语检索；“data centre / data center / 数据中心 / 云 / 海床光缆 / 服务器 / 算力”；中文检索用 `-"麦当劳"` 排除品牌误命。
7. **可靠性分级（A/B/C）**：A=官方/一手（`antarctica.gov.au` AAD、`dcceew.gov.au`、`legislation.gov.au`、`afma.gov.au`、`acma.gov.au`、IANA、ITU、云厂商官方区域清单、具名运营商公告）；B=权威二级（UNESCO、SCAR、CCAMLR、Geoscience Australia、BoM、Submarine Cable Map/TeleGeography、引用官方材料的主流媒体或科学机构、APNIC/PeeringDB/BGP 工具）；C=弱来源（数据中心目录站、SEO 市场报告、社媒、未引用来源的中英文文章、供应商国家选择列表）— 只作线索或假阳性，不计数。
8. **计数与去重规则**：默认 verified-negative；只有 A 级来源点名“设施名称 + 功能 + 位置 + 运营方”才升级；目录站出现 HM 国家页、空列表或表单国家选项记录为 “directory placeholder” 不得计数；科考营地、自动气象站、海平面站、遥测设备、发电机、临时卫星终端可记录为 non-DC infrastructure lead 但默认不计数；AADC（澳大利亚南极数据中心，科学数据仓库/地图数据服务）不是 HM 岛上数据中心；AAT 南极站（Mawson/Davis/Casey/Wilkins）、Mawson Peak（HM 活火山 Big Ben 的山峰）vs Mawson Station、McDonald Islands vs McDonald's 品牌、Kerguelen（法属南方和南极领地）设施、渔业船载系统均须排除。

## 常用查询模板

```text
# 官方线（英文）
site:antarctica.gov.au "Heard Island" (station OR camp OR expedition OR communications OR satellite)
site:antarctica.gov.au "Heard Island" ("data centre" OR "data center" OR datacenter OR server OR hosting)
site:dcceew.gov.au "Heard Island" (permit OR reserve OR "marine park" OR "marine reserve")
site:legislation.gov.au "Heard Island and McDonald Islands Act"
site:afma.gov.au "Heard Island and McDonald Islands Fishery"
site:acma.gov.au "Heard Island" (licence OR radiocommunication OR amateur)
site:iana.org ".hm" delegation
"Heard Island" OR "McDonald Islands" ("data centre" OR "data center" OR datacenter OR colocation OR hosting)
"submarine cable" "Heard Island" OR "McDonald Islands"
# 官方线（中文）
"赫德岛" OR "麦克唐纳群岛" ("数据中心" OR "云" OR "海底光缆" OR "服务器" OR "算力")
"赫德岛" OR "麦克唐纳群岛" 数据中心 -"麦当劳"
# 行业线
"Heard Island and McDonald Islands" (AWS OR Azure OR "Google Cloud" OR Oracle OR "cloud region" OR "edge location")
site:datacenterdynamics.com "Heard Island" OR "McDonald Islands"
site:datacentermap.com "Heard Island" OR "McDonald Islands"
"Heard Island" OR "McDonald Islands" ("submarine cable" OR "cable landing" OR "landing station")
site:peeringdb.com "Heard Island" OR "McDonald Islands"
"Heard Island" ("Atlas Cove" OR "Spit Bay" OR "Magnet Point") (camp OR satellite OR generator OR power OR station)
"Heard Island" (Iridium OR Inmarsat OR Starlink OR VSAT OR HF) (expedition OR camp OR vessel)
"赫德岛" OR "麦克唐纳群岛" ("数据中心" OR "云" OR "算力" OR "海底光缆" OR "AI")
```

## 官方/监管管线要点（详见 explorer-official.md）

- **AAD 主页面**（`antarctica.gov.au/antarctic-operations/stations-and-field-locations/heard-island/`）：确认 AAD 管理、无人居住、最新科考访问；**Human activities** 页确认访问稀少、历史 Atlas Cove 研究站、科研/渔业/监督活动边界；**Location and geography** 页确认位置、距离、HIMI Marine Reserve、AADC 地图链接。
- **DCCEEW / EPBC**（`dcceew.gov.au`、`legislation.gov.au`）：环境保护、许可、世界遗产相关法律。
- **AFMA HIMI Fishery**（`afma.gov.au`）：确认主要经济活动是受管制渔业；船载设备不计为陆地设施。
- **ACMA RRL**（`acma.gov.au/register-radiocommunications-licences-rrl`）：复核澳大利亚无线电牌照；预期无 HM 商业电信设施。
- **IANA `.HM` / registry.hm**：ccTLD 委托与注册状态；域名注册服务不得误判为数据中心。
- **UNESCO World Heritage**（whc.unesco.org/en/list/577/）：世界遗产、strict nature reserve、低人类扰动（B 级）。
- **官方云区域清单**：AWS/Azure/Google Cloud/Oracle OCI 负向对照 — 无 HM region/edge location。
- **每轮复核清单**：读 manifest 确认 division → 复核 AAD 主页面/Human activities → 检 AAD/DCCEEW/legislation/AFMA 是否出现“永久站点、建设许可、机房、通信设施、能源设施”新公告 → ACMA RRL 是否有 HM 商业电信牌照（有则仅作 lead 需确认是否陆地设施）→ IANA/registry.hm 状态 → 官方云区域清单 → 海缆地图无 landing station → 中英文搜索按假阳性清单排除。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **数据中心/云负向对照**：官方区域清单无 HM；目录站（Data Center Map、Cloudscene、Baxtel、datacenters.com）只作 C 级线索，出现 HM 国家页/空列表/表单选项记 “directory placeholder” 不得计数；澳大利亚本土 region 不得归入 HM。
- **网络/海缆/电信**：Submarine Cable Map/TeleGeography/SubTel Forum 预期无 HM landing station；ACMA/APNIC WHOIS/PeeringDB/BGP 预期无 HM 本地 carrier、IXP、ASN 或固定 ISP；卫星终端可用性不是数据中心设施证据。
- **渔业/船舶/科考**：AFMA HIMI Fishery 与 CCAMLR 是行业侧最可能出实体名称的来源；持牌渔船卫星通信/冷藏/加工/导航/船载 IT 均不计为陆地数据中心；AAD 科考营地、自动气象站、海平面站、遥测设备、发电机、临时卫星终端可记录为 non-DC infrastructure lead，默认不计数。
- **假阳性清单**：AADC（科学数据仓库）、`.hm` 域名注册、AAT 南极站、Mawson Peak/Mawson Station 混淆、McDonald's 品牌、Kerguelen 设施、渔业船载设备、卫星通信报道、市场报告国家列表（把 HM 放国家下拉或统计表中不是市场存在证据）。
- **诚实结论**：HM 没有商业数据中心市场，也没有可作为数据中心候选的运营商、园区、电力或网络基础设施；行业侧与官方侧一致输出 verified-negative。

## 维护注意（更新纪律）

- **更新节奏**：每轮复核清单执行（见官方线）；事件驱动 — 若出现“永久站点、建设许可、机房、通信设施、能源设施、海缆”类新公告或 A 级来源点名商业设施/项目，立即核验位置/运营方/功能三要素后决定升级。
- **来源核验**：候选记录模板（country_code: HM、division、facility_or_project_name、operator、consent_or_authorisation、site_address、coordinates、status: verified-negative|lead|rejected_false_positive、facility_type、it_load_mw、power_connection、connectivity、evidence_grade、primary_urls、last_checked: 2026-08-12、notes）；最小计数标准 — A 级来源点名 + 名称/功能/位置/运营方四要素 + 排除假阳性 + MW 级声明有电力/许可/采购/运营商证据。
- **不删除纪律**：本目录只允许新增/更新文件，禁止删除或移动任何文件；目录占位、卫星终端、船载系统、临时科考设备一律不计数；AAD/AAT/Kerguelen/McDonald's 品牌误命中一律排除。
