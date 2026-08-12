---
name: mo-datacenter-methodology
location: scripts/expansion/world/country-skills/MO/SKILL.md
description: 澳门数据中心双线查询方法论（官方/监管/云管线 + 行业/厂商/媒体发现），含 division 模型、来源分级、四语检索词与查询模板；Macao datacenter dual-line discovery methodology (official/regulatory/cloud pipeline + industry/vendor/media discovery) with division model, source grading, quadrilingual search vocabulary and query templates. 运行 MO 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。
---

# MO · 澳门数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为澳门（Macao, MO）数据中心枚举/审计批次提供官方与行业双线发现方法。官方线（explorer-official.md）覆盖澳门特别行政区政府门户、CTT 电信监管与数据中心授权、CEM 电力、DICJ 博彩监管、网安/个资/金融监管、公报/采购/工务、官方云区域页与博彩承批公司披露；行业线（explorer-industry.md）覆盖运营商/厂商、贸易媒体与本地媒体、互联/IXP/海缆、聚合目录、博彩行业披露。两线交叉核验，按 A/B/C/U 分级入库；来源等级跟随被支持的事实，而不是跟随设施。

## 入口

| 文件 | 职责 | 内容概要 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | 澳门特区政府门户（gov.mo）/GCS/SAFP 政府云、CTT 电信监管与数据中心授权（Reg. 13/2024、CTM 授权 1/2024 续期）、DSEDT、CTM 澳门电讯、CEM 电力特许、DICJ 博彩、网安法 13/2019/GPDP/AMCM、公报（bo.dsaj.gov.mo）/采购/土地/工务（DSSCU/DSOP）、云厂商官方区域页（AWS/Azure/GCP/OCI/阿里云/腾讯云/华为云）、博彩承批公司披露（HKEX/SEC） |
| explorer-industry.md | 行业/厂商/媒体发现 | 检索词汇四语包（英/繁中/简中/葡）、CTM 主运营商管线、其他电信运营商（MTel、和记电话/3 Macau、中国电信澳门、数码通）、政府与集成商（SAFP 招标、华为/HPE/Cisco/Schneider/Vertiv/NTT/ZTE）、博彩承批公司、超大规模云缺位、贸易与本地媒体（Macau Business、Macao News、TDM、Plataforma、DCD 等）、互联/IXP/海缆、聚合目录（DataCenterMap、Baxtel、Cloudscene、datacenters.com、Inflect）、分区枚举矩阵 |

## 核心结构事实

1. **Division 模型**：manifest 已核验 `country_code:"MO"`、`country_name:"Macao"`、`subnational_type:"country"`、`divisions:["Macao"]`。所有记录必须使用 `division="Macao"`；更精确地理只存辅助字段：`area`（澳门半岛/Taipa/Cotai/Coloane/新填海区）、`parish`（有意义时）、`place_or_address`。
2. **本地路由与语言**：本地路由字段——澳门半岛（Sé、Fátima、Santo António、São Lázaro、São Lourenço）、氹仔（Carmo）、路环（São Francisco Xavier）、路氹填海区、新填海区（A/E 区）；官方语言检索必须覆盖繁体中文、葡文、英文与简体中文：`數據中心`、`資料中心`、`数据中心`、`centro de dados`、`data centre`、`data center`、`datacenter`、`IDC`。
3. **2024 数据中心法律体制（关键核正）**：行政法规第 13/2024 号 `Regime de instalação e funcionamento de centros de dados`（《数据中心的设立及运作制度》）将数据中心定义为向第三方收费、提供设备、电力和互联网接入的实体空间，并须事先取得行政长官授权；CTT 电信页面是主要发牌来源。CTT 于 2024-10-04 公布，在该制度下当时仅有 **澳门电讯有限公司（CTM）** 获发数据中心授权；CTT 电信规管清单显示行政长官批示第 180/2025 号将 CTM 授权 1/2024 自 2025-10-01 续期至 2027-09-30。
4. **法律与监管**：CEM 是澳门电力分配唯一特许经营商（gov.mo 确认），CEM/年报为供电事实 A 级来源；DICJ 负责博彩技术与 EGM 标准（电子博彩机须 DICJ 审批）；网安法第 13/2019 号 2019-06-24 公布、2019-12-22 生效，支撑关键基础设施运营者网安/合规需求；GPDP（个资）、AMCM（金融外包/数据）为需求/监管来源而非设施证据；博彩承批公司（六张牌照，2023-01-01 起 10 年）年报/披露为物业/IT/capex 披露证据。
5. **博彩需求与设施分类**：博彩是本地主导需求驱动，但赌场内部 server room 必须与公共 colocation 数据中心分开跟踪；2024 数据中心制度明确针对付费第三方空间，赌场内部 IT 房除非另行获授权或向第三方提供，否则可能不在公开 DC 发牌计数内。设施分类：`public_colocation_dc`（需授权/运营商证据）、`government_cloud_or_data_centre`（需官方 SAFP/公报证据）、`casino_internal_it`（物业/系统证据，不计公共 colocation）、`cross_border_adjacent`（横琴/珠海/香港/广东服务语境，不计澳门数）。
6. **设施/项目种子（2026-08 证据状态）**：CTM Data Centre / CTM Cloud（A 级 CTM 服务存在性，地址待核验——目录给 Taipa/Rua do Lago Sai Van 线索为 C）；CTM Hong Kong Data Centre（A，记为香港邻近服务，不是澳门设施）；SAFP 政府云/数据中心（A 政府项目事实，与公共 colocation 分开）；DataCenterMap CTM Taipa（C 地址线索待印证）；超大规模云区域均无 Macao 区域（A 级缺位）。
7. **语言与词汇**：四语检索词见 explorer-industry.md §1；状态与设施术语：authorized/renewed/licensed/opens/operational/in service；concurso público/adjudicação/autorização/renovação；公開招標/判給/許可/續期/啟用/維護；MW/MVA/racks/Tier III/ISO 27001/TIA-942/PUE。
8. **可靠性分级**：A = 对所述确切事实负责的一级/责任来源（gov.mo、gcs.gov.mo、bo.dsaj.gov.mo、telecommunications.ctt.gov.mo/ctt.gov.mo、DICJ、GPDP、AMCM、DSEC、SAFP、DSSCU/DSOP、CEM、CTM、云厂商官方区域页、承批公司 HKEX/SEC 披露）；B = 具名事实的可靠二级来源（Macau Business、Macao News、Macau Daily Times、TDM、Plataforma、Hoje Macau、Ponto Final、Macau Post Daily、DCD、Capacity Media、Reuters、Bloomberg、SCMP、信誉工程/厂商案例）；C = 仅线索（DataCenterMap、Baxtel、Cloudscene、datacenters.com、Inflect、经纪页、市场规模报告、招聘广告、活动页、社媒）；U = 已核查但不支持，不计入。只给事实本身评级：云区域页可评“澳门缺席/存在为区域”，不能评地址；公报授权可评“实体获授权设立及经营数据中心”，不能评“设施已建成/运营/有 X MW”；承批公司年报可评“物业/IT/capex 披露”，除非文件明确说明否则不能作为单独可计数的公共 colocation 设施。
9. **计数与去重规则**：不要把 `港澳台地区（中国香港）` 当澳门云区域（那是香港 ap-hongkong）；不要把赌场内部 IT 房当公共数据中心；不要把授权当建成容量；不要用目录计数当已验证设施总数；不要把横琴/珠海设施混入澳门计数；不要只依赖英文，葡文与繁体中文查询必不可少；腾讯 CVM 列表将香港归入港澳台地区，阿里云列香港/深圳/广州/河源等邻近区域，均非澳门区域，只作服务路径语境。

## 常用查询模板

```text
site:gov.mo "數據中心" OR "資料中心" OR "雲計算中心"
site:gcs.gov.mo "數據中心" OR "政府雲" OR "centro de dados"
site:safp.gov.mo "雲計算中心" OR "政府數據中心" OR "7x24"
site:telecommunications.ctt.gov.mo "data centers" OR "centros de dados"
site:bo.dsaj.gov.mo "數據中心的設立及運作制度"
site:bo.dsaj.gov.mo "公開招標" "數據中心"
site:ctm.net "Data Center Services" OR "CTM Data Centre"
site:ctm.net "數據中心" OR "IDC" OR "雲"
"澳門電訊" "數據中心" OR "IDC"
site:cem-macau.com "data centre" OR "數據中心" OR "centro de dados"
site:dicj.gov.mo "EGM" OR "technical standards" OR "gaming machines"
site:gpdp.gov.mo "跨境" OR "個人資料" OR "雲"
site:amcm.gov.mo "外包" OR "數據中心" OR "災備"
site:hkexnews.hk "data centre" OR "數據中心" "Macau"
site:sec.gov "Macau" "data center" "casino"
"Macau" OR "Macao" site:docs.aws.amazon.com/global-infrastructure
"Macau" OR "Macao" site:cloud.google.com/about/locations
"澳門" OR "澳门" site:cloud.tencent.com/document/product/213/6091
site:datacentermap.com/macau "CTM" OR "Macau"
site:macaubusiness.com "data centre" OR "data center" OR "centro de dados"
site:tdm.com.mo "數據中心" OR "centro de dados"
"Hengqin" "data centre" Macau
"珠海" "數據中心" "澳門企業" OR "災備"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **政府门户/GCS/SAFP/政府云**：gov.mo、gcs.gov.mo、safp.gov.mo 用于政府云、政府数据中心、电子政务维护公告、招标与官方新闻；SAFP 页面确认活跃的政府云/数据中心运维与采购，为政府项目事实 A 级，但政府云不自动等于公共 colocation 设施。
- **CTT 电信监管与数据中心授权**：先搜 CTT 规管清单中的 `Regulamento Administrativo n.º 13/2024`、`數據中心的設立及運作制度`、`install and operate data centers` 与授权续期；CTT/公报授权记录为发牌事实 A 级；不得从授权单独推断设施地址、容量、状态或公开可用性——跟随持牌人到运营商页、招标与二级来源。
- **DSEDT**：经济及科技发展局用于经济/科技政策、中小企业数字化与创新语境；电信发牌与 2024 数据中心授权体制应引 CTT/公报，除非具体 DSEDT 页面是实际来源。
- **CTM 澳门电讯**：CTM 是主运营商种子（CTT 记录显示 CTM 获授权设立及经营数据中心）；CTM 页面为 CTM 自身服务与产品标签 A 级；页面 JS 重时保留 URL 并用 CTT/公报与 B/C 目录补地址线索。
- **CEM 电力**：CEM/年报为电网、特许、可靠性、电源结构与澳门供电背景 A 级；没有公开数据中心并网登记册，电力事实必须用具名客户/项目证据关联。
- **DICJ 博彩监管**：用于博彩技术要求、EGM 标准、机器审批、承批框架与赌场监管事实；支撑需求驱动与内部 IT 义务，不单独识别可计数的第三方数据中心。
- **网安/GPDP/AMCM**：Law 13/2019（关键基础设施网安需求）、GPDP（私隐/跨境数据）、AMCM（金融外包）为需求/监管来源。
- **公报/采购/土地/工务**：bo.dsaj.gov.mo 用于公开招标、判给、法律体制、授权、土地批给与公告；DSSOPT 已重组——土地/城建为 DSSCU、工务为 DSOP（按已核验官方页）。
- **云区域官方页**：AWS/Azure/GCP/OCI/阿里云/腾讯云/华为云官方区域列表均未发现名为 Macao/Macau 的官方超大规模云区域；邻近区域只作服务路径语境。
- **博彩承批公司披露**：SJM、Galaxy、Sands China、Wynn Macau、MGM China、Melco 与 HKEXnews/SEC EDGAR 用于官方物业清单、承批/capex/科技披露、网安事件、外包与连续性风险；不得在无设施级证据时把度假村当数据中心。
- **分区枚举**：澳门半岛（政府 DC/云、CTM/企业电信、金融 IT）→ 氹仔（CTM/目录地址线索、电信节点、机场/酒店 IT、灾备候选）→ 路氹（赌场度假村内部 IT 房/CCTV/EGM 需求，与公共 DC 分开计数）→ 路环（低密度，电厂/电气基础设施语境）→ 新填海区（仅规划/土地管线）→ 横琴/珠海（邻接设施，CN 司法辖区，从澳门计数排除）。
- **验证清单**：①确认 division="Macao"，绝不创建 subnational divisions ②候选若为公共/第三方 colocation 先查 CTT 授权记录 ③按事实拆分证据（法律授权/设施存在/地址/状态/业主/容量/认证/电力/客户）④CTM 组合 CTT 授权 + CTM 产品页 + CTM 或 B/C 目录地址级证据，目录地址标 C 直到确认 ⑤政府云按政府基础设施跟踪 ⑥赌场标 `facility_type="casino_internal_it"` 除非来源说明为第三方 colocation 或另行授权 ⑦云提供商只从官方区域页记录澳门缺席/存在，不把香港/深圳/广州区域映射进澳门 ⑧横琴/珠海存澳门计数之外并加司法辖区注记。
- **复查节奏**：月度（CTT 电信规管/新闻、CTM 新闻/产品页、SAFP 招标、公报 I/II 系列、DICJ 通知、CEM 新闻）；季度（云区域页、HKEX/SEC 承批披露、GPDP/AMCM 决定、DSEC/DICJ 背景统计）；事件驱动（新数据中心授权、CTM 牌照续期、政府云采购、赌场网安/IT 披露、土地批给或用途变更通知）；年度（刷新监管名称/域名、教区/区域映射、云区域列表、全部 C 级目录线索）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **市场模型发现顺序**：①CTT/公报发牌主线（Reg. 13/2024 要求授权，CTT/公报记录是公共/colocation 设施的第一过滤器；2024-10-04 核验：仅 CTM 获授权）②运营商页（CTM Data Centre、CTM Cloud、CTM Hong Kong Data Centre，确认产品/服务存在后找地址/状态细节）③政府云（SAFP 通知与招标识别政府基础设施）④博彩需求（六家承批公司驱动本地 IT/监控/EGM/网安/支付/酒店/CRM/连续性需求，赌场内部 IT 房分开跟踪）⑤邻近区域（香港/深圳/广州/河源/横琴/珠海承载大部分超大规模/云/灾备容量，是语境不是澳门设施）。
- **CTM 管线**：CTM 是核验 CTT 通知中唯一已获授权的公共数据中心运营商线索；CTM 自身页为服务存在性 A 级，但站点 JS 重可能不暴露全部地址/容量细节；查询 site:ctm.net + "Data Center Services"/"CTM Data Centre"/"數據中心"/IDC/CTM Cloud。
- **其他电信运营商**：检查 MTel、和记电话（澳门）/3 Macau、中国电信（澳门）、数码通；CTT 规管清单含这些运营商的电信牌照，但电信牌照不是数据中心授权——只有来源说明数据中心服务或授权时才升级。
- **政府与集成商**：SAFP 云/数据中心运维招标是高价值线索；华为/HPE/Cisco/Schneider Electric/Vertiv/NTT/ZTE 及本地集成商案例研究可揭示实施细节，但按 B 级直到运营商/政府确认。
- **博彩承批公司**：用官方披露识别 IT/网安/capex 披露与物业清单；结果按 public_colocation_dc / government_cloud_or_data_centre / casino_internal_it / cross_border_adjacent 分类。
- **超大规模云缺位**：2026-08-12 核验官方区域页——AWS/Azure/GCP/OCI/阿里云/腾讯云/华为云均无 Macao/Macau 公共云区域；腾讯列的是香港（ap-hongkong），阿里列香港/深圳/广州/河源等，都不是澳门区域。
- **贸易与本地媒体**：英文数据中心行业媒体对澳门覆盖稀疏，应积极使用本地媒体（B 级）：Macau Business、Macao News、Macau Daily Times、TDM、Macau Post Daily、Plataforma、Hoje Macau、Ponto Final（使用前核验当前域名）、Macau Daily、Exmoo；区域/国际：DCD、Capacity Media、W.Media、SCMP、Reuters、Bloomberg、Mingtiandi。
- **互联/IXP/海缆**：澳门没有已核验的主要公共云区域，也没有已核验的类似 HKIX 的主要公共 IXP；互联只作线索层——IXP/CDN/POP/edge node/海缆登陆事实不是数据中心设施，除非另有设施证据；香港或珠海连接只支持服务路径注记。
- **聚合目录**：DataCenterMap Macau、Baxtel、Cloudscene、datacenters.com、Inflect 只用于线索；目录流程：捕获设施名/运营商/地址/坐标/别名 → 搜 CTM/运营商、CTT 授权、公报与可靠媒体同名/同址 → 目录独有地址/容量/状态保持 C 并从最终计数排除直到升级。
- **分区枚举矩阵**：澳门半岛（只计设施级证据，政府云与公共 colocation 分开）、氹仔（目录地址保持 C 直到 CTM/官方印证）、路氹（casino_internal_it 分开）、路环（CEM 电力资产不是数据中心）、新填海区（仅管线）、横琴/珠海（CN 司法辖区，从澳门计数排除）。
- **已知行业/运营商证据**：CTM 公共数据中心授权（A，主公共 DC 种子）；CTM Data Centre/Cloud（A，确认服务后找地址/容量/状态）；CTM Hong Kong Data Centre（A，记为香港邻近服务）；SAFP 云/数据中心（A，政府基础设施）；DICJ EGM 标准（A，需求/监管证据）；博彩承批公司（A，物业/IT/网安证据，默认不是公共 DC）；DataCenterMap CTM Taipa（C 地址线索）；超大规模云澳门缺位（A）；横琴/珠海线索（按来源 C/B/A，只存跨境）。
- **复查节奏**：月度（CTT 规管/新闻、CTM 产品/新闻页、SAFP 招标、公报检索、DICJ 通知、本地媒体）；季度（云区域页、HKEX/SEC 披露、CEM 年报更新、GPDP/AMCM 决定、目录线索）；事件驱动（数据中心授权、CTM 设施公告、政府云扩展、赌场 IT/网安披露、面向澳门客户的横琴/珠海设施营销）；年度（完整双语/三语查询重跑、媒体域名刷新、实体名称刷新）。
- **红旗**：销售区域或支持页中的 `Macau` 不是云区域；CTT 授权是第三方数据中心必要条件但不是建成/容量证明；赌场 IT 需求真实但不得膨胀为公共 colocation 供给；香港/横琴/珠海设施不得混入 division="Macao" 计数；公开招标与判给是里程碑事实不是运营状态；聚合器总数是发现辅助，永远不是已验证总数。
- **预期产出**：澳门已验证的公共/第三方数据中心供给非常小；基于核验的 2024 CTT 授权通知，CTM 是核心公共 DC 种子；更多发现更可能是政府云基础设施、赌场内部 IT 房或香港/横琴/珠海邻近服务路径，而非独立的澳门 colocation 园区。

## 维护注意（更新纪律）

- **更新节奏**：按月度/季度/事件驱动/年度节奏复查（详见上）；授权与续期、政府云采购、赌场披露是事件驱动触发器。
- **来源核验**：来源等级跟随事实而非设施；目录地址 = C 直到确认；CTM 服务页 = A 仅限 CTM 服务存在性；CTT 授权 = A 仅限授权；承批公司年报 = A 仅限披露的物业/IT 事实，不构成独立可计数的公共 colocation 设施。
- **不删除纪律**：本目录只新增/更新 SKILL.md、ANATOMY.md 与探索产物，禁止删除/移动任何现有文件（explorer-official.md、explorer-industry.md 与历史证据保留为原始记录）。
