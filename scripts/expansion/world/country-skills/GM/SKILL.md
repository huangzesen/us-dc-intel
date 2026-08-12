---
name: gm-datacenter-methodology
location: scripts/expansion/world/country-skills/GM/SKILL.md
description: 冈比亚（Gambia）数据中心发现与审计方法论：官方/监管/云管线（MOCDE/GICTA 政府云、PURA 电信监管、NAWEC 电力、GPPA 招标、GIEPA 投资、World Bank WARDIP、云区域状态）叠加行业/厂商发现（运营商、托管、电信、IXP、供应商、贸易媒体）；以清单中的 6 个城市/分区（Banjul、Lower River、Central River、North Bank、Upper River、Western）为划分粒度，字段级定级。运行 GM 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。Bilingual discovery & audit methodology for The Gambia datacenters: official/regulatory/cloud pipeline + industry/trade-press discovery, at the 6 city/division granularity from the manifest; field-level grading; read before running GM exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# GM · 冈比亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> **目的**：冈比亚没有公开的国家数据中心登记册，也无集中在线规划许可数据库——通过拼接 MOCDE/GICTA 电子政务证据、PURA ICT 牌照、NAWEC 电力证据、GPPA 招标、GIEPA 投资材料、WARDIP 文件、市政记录与运营商页面建记录。市场以 Greater Banjul Area 为中心、非常小且早期；诚实产量预期 **1–3 条可计数/近可计数设施**（Abuko 国家数据中心；具名 GAMTEL 交换局/托管点若有官方站点证据；WARDIP 登陆站/数据中心工程当出现站点级采购/施工）。Lower River、Central River、North Bank、Upper River 通常为 `no confirmed facility found`。运行任何 GM 探索/审计批次前必须阅读本 skill，并按需路由到两份探索报告。

## 入口（Entry points）

| 文件 | 管线 | 内容 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | MOCDE/GICTA 政府云与 NIMS、PURA ICT 牌照、NAWEC 电力、GPPA/GIEPA/世行采购、海缆/登陆站/IXP、市政议会、官方云区域状态、6 分区官方枚举策略 |
| explorer-industry.md | 行业/厂商发现 | 运营商/设施种子表（GICTA/NDC/NIMS、GAMTEL、WARDIP、Margins、SIXP、Kairaba Exchange）、贸易媒体、网络/对等/CDN/目录证据、企业/金融/政府/供应商线索、协会与活动、6 分区行业策略、确认工作流、来源说明 |

## 核心结构事实（框定每次搜索）

1. **划分模型**：清单为 **6 个城市/分区**：**Banjul；Lower River；Central River；North Bank；Upper River；Western**。规范化：Western Region、West Coast Region、WCR、Kanifing、Serekunda、Abuko、Bakau、Brikama、Yundum 归 **Western**（除非来源明确在 Banjul 市/分区）；Greater Banjul Area 横跨 **Banjul** 与 **Western** 两分区，不得合并。
2. **核心设施/项目集**：**Gambia National Data Centre, Abuko, Western**（强媒体/厂商报道：总统 Barrow 于 2026-07-01 与 NIMS 国家身份系统一同启用；**B 级**直至 GICTA/MOCDE/State House 官方页打开；`ISO-certified` 保持 B/C 除非证书/认证条目出现）；**GAMTEL 托管/设施租赁服务**（官方页：客户可租用 GAMTEL 全国 43 个站点/铁塔空间托管电信硬件或服务器——**A 级服务主张**，但不得乘成 43 个数据中心，具名交换局/铁塔在站点级证据前仅为设施线索）；**WARDIP / DTFA P176932**（MOCDE/世行：第二海缆、登陆站、数据基础设施工程，含 GAMTEL 设施与全国数据中心建设/升级——A 级项目范围；逐站点记录需招标/许可/电力/运营商证据）；**SIXP / Serekunda Internet Exchange, Western**（PeeringDB/AfPIF 定位国家 IXP 于 Serekunda——网络存在证据，非数据中心证明）；**Kairaba Exchange**（PeeringDB fac/2287——C/B 网络/目录线索）。
3. **关键机构**：MOCDE（政策所有者；G-Cloud 战略 = 官方需求信号）、GICTA（运营 ICT 机构）、PURA（监管通信与公用事业；四家移动运营商、一家固网、四家持牌 ISP；**无独立公共数据中心执照类别**——设施证据嵌入电信/ISP/网关记录）、NAWEC（电力/水务，门控过滤器：为每个运营主张记录并网、变电站、连接负荷、备电发电机、UPS、燃油、太阳能/自备电力与停电暴露）、GPPA（官方采购面）、GIEPA（投资促进；Data Centre 行业资料非设施证明）、World Bank（WARDIP P176932）、国家议会法案跟踪器（DATA PROTECTION AND PRIVACY BILL 2024 状态 **Assented**，最后更新 2026-07-15）。
4. **查询语言与拼写**：英语为主；"data centre"/"data center"/"server room"/"hosting"/"colocation"/"co-location"；分区名 + Gambia；注意 Banjul 与 Western 分区边界。
5. **容量语义**：状态值分离：`operational`、`under construction`、`approved`、`planned`、`MoU/intent`、`lead only`；不从法律、执照类别、光纤线路、IXP、云转售页、铁塔托管主张或 MoU 单独计数；仅当具名运营商或公共机构绑定物理设施或数据中心服务才计数。NAWEC 单元精确保留，不自行换算 MVA→MW/IT 负荷。
6. **海缆/IXP/网络证据**：ACE 在/近 Banjul 登陆、GAMTEL 为全国固网基础设施锚点；SIXP/Serekunda 为国内交换点与强网络线索，非数据中心证明；PeeringDB 设施条目为 C/B 定位线索，须经运营商/市政/PURA 记录确认。
7. **云区域状态（已核查）**：AWS/Azure/GCP/OCI/Huawei Cloud 官方页面均无冈比亚公共区域；冈比亚云区域主张除非官方页面变化否则按本地/混合/边缘证据处理。
8. **可靠度分级（字段级）**：A = 该字段的一手来源（政府/监管/运营商页、MOCDE/GICTA 文件、GPPA 招标、NAWEC 记录、PURA 执照/法规、GIEPA 文件、市政/建筑记录、官方云区域页、世行/MOCDE WARDIP 文件）；B = 强具名二级（The Standard、The Point、Foroyaa、GRTS、GambiaJ、Biometric Update、ITWeb Africa、Developing Telecoms、Connecting Africa、Capacity、Techpoint Africa、DCD、Cloudflare/Internet Society 分析、PeeringDB/IXP 网络存在）；C = 仅线索（目录、社交、泛市场报告、无支撑地址/容量主张、无站点/电力/许可证据的 MoU、转售/云伙伴主张）。同一设施可有 A 级运营方存在、B 级启用日期、C 级地址/容量，逐字段独立核验。
9. **去重纪律**：GAMTEL 43 站点 ≠ 43 数据中心；Abuko NDC 在官方页打开前不升 A；`inaugurated` 无官方页不升 A；`ISO-certified` 无认证证据不升 A；WARDIP 是 A 级项目范围但逐站点工程无站点级证据不可计数；Kairaba Exchange 在运营方/官方站点证据前为 C/B。

## 常用查询模板（详见 explorer-official.md / explorer-industry.md）

```text
site:gicta.gov.gm "data centre" OR "data center" OR "NIMS" OR "national data centre"
site:mocde.gov.gm "data centre" OR "data center" OR "G-Cloud" OR "cloud"
site:pura.gm "data centre" OR "colocation" OR "GAMTEL" OR "Africell" OR "QCell"
site:nawec.gm "data centre" OR "server" OR "generator" OR "substation"
site:gppa.gm "data centre" OR "ICT infrastructure" OR "landing station"
site:giepa.gm "data centre" OR "data center" OR "ICT"
"Gambia National Data Centre" Abuko GICTA
"National Identity Management System" Gambia "data centre" Margins
"WARDIP" Gambia "data centre" contract OR award
"{division}" "data centre" OR "data center" OR "server room" OR "hosting" Gambia
"{capital}" "GAMTEL" OR "GICTA" OR "WARDIP" Gambia
"{capital}" "substation" OR "generator" "data" Gambia
"SIXP" OR "Serekunda Internet Exchange" members OR peers Gambia
"Kairaba Exchange" Serekunda colocation
"{operator}" "PURA" OR "GPPA" OR "NAWEC" Gambia
site:standard.gm Gambia "data centre" OR GICTA OR WARDIP OR NIMS
site:biometricupdate.com Gambia "data centre" OR NIMS OR "digital ID"
"Gambia" "cloud region" official   # 云区域排除
```

## 官方/监管管线要点（详见 explorer-official.md）

- MOCDE/GICTA：先用此线索查主权系统、G-Cloud、NIMS 与公共数据中心基础设施；核验 Abuko NDC 官方所有权、启用措辞、托管系统、运营方/机构、物理位置、Tier/ISO 主张、电力/设施特征；MoU 保持 `MoU/intent` 除非站点/采购/启用记录存在。
- PURA：A 级来源确定持牌电信与 ISP 市场结构（GAMCEL、AFRICELL、COMIUM、QCELL、GAMTEL + 持牌 ISP）；执照/服务为线索非设施记录。
- NAWEC：电力证据决定运营主张是否可信；公开线索可能稀疏，仍将每个设施的电力字段记录为 `unknown` 直至有来源。
- GPPA/GIEPA/世行：tenders.gm 等聚合器除非复制可验证来源的官方招标否则 C 级。
- 海缆/登陆站/IXP：ACE 登陆、WARDIP 第二海缆与新登陆站工程为官方项目证据；仅当具体站点、招标、施工记录或运营商声明存在才计数登陆站/数据中心设施。
- 市政：Banjul City Council、Kanifing Municipal Council、Brikama/Mansakonko/Kerewan/Basse Area Councils 的土地分配、建筑许可与完工/占用证据。
- 云区域：AWS/Azure/GCP/OCI/Huawei 官方页 + 年度核验查询。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 先运营商/政府页播种（GICTA/政府目录、GAMTEL、MOCDE/WARDIP/G-Cloud/Open Data PDF、GPPA/政府招标、PURA、NAWEC、世行）；媒体/行业来源用于日期、伙伴与容量线索并保持 B 级；目录/PeeringDB 仅作线索。
- 每个候选至少与以下两者交叉核对：运营商页、PURA 执照、GPPA 招标/中标、NAWEC 电力记录、GICTA/MOCDE 文件、市政记录、世行/MOCDE 项目文件。
- 网络证据：Google Global Cache、Meta、Akamai、Netflix OCA、Cloudflare 等缓存仅显示网络/边缘部署；仅当托管设施被具名并佐证才计数 DC。
- 企业/金融/政府/供应商：银行（CBG、Trust Bank、GTBank、Access Bank、Ecobank）、GRA/SSFA/National Assembly、Margins/Huawei/Presight/SYSROAD 集成商——网络升级不是 DC 除非来源说数据中心/设施；UTG 等大学机房仅凭公共设施证据计数。

## 维护注意（更新纪律）

- **更新节奏**：每次批次重查官方云区域页（AWS/Azure/GCP/OCI/Huawei）、MOCDE/GICTA/gambia.gov.gm、PURA、NAWEC、GPPA/政府招标、国家议会法案跟踪器（数据保护法案最终法案文本）、WARDIP 世行项目页、Abuko NDC 官方确认。
- **来源核验**：GICTA 目录页可用；tenders.gm 与聚合器为 C 级；`ISO-certified` 需证书；GAMTEL 43 站点主张为 A 级服务语言而非 43 个数据中心；Kairaba Exchange 为 C/B 网络/目录线索。
- **不删除纪律**：无法核实的旧线索保留为降级线索并注明缺失证据；六分区全部运行并显式记录 `no confirmed facility found`；存储字段级等级与精确来源措辞。
