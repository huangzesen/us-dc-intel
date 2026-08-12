---
name: kw-datacenter-methodology
location: scripts/expansion/world/country-skills/KW/SKILL.md
description: |
  Kuwait data-center discovery routes CITRA regulation, Kuwait Municipality permits, MEW power, CAPT/e.gov.kw tenders, KDIPA investment, KUNA news, and official cloud-region checks into operator-primary leads (Syntys/Ooredoo Kuwait City + Shuaiba, Zain Business DC, stc DC1/DC2, Zajil/Kalaam) across six governorates with mandatory Arabic search and per-governorate positive-seed-or-negative-sweep discipline.
---

# KW · 科威特数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为科威特数据中心/托管设施发现与审计提供可持续、可复现的查询方法论。
> 分区模型：6 个省（governorates）：Capital；Hawalli；Farwaniya；Ahmadi；Jahra；Mubarak Al-Kabeer（保留阿拉伯别名于备注）。
> 已知种子：Syntys Kuwait City + Syntys Shuaiba（Iron Mountain 点名）、Ooredoo Kuwait AI DC、Zain Business Data Center、stc Data Center 1/2、Zajil/Kalaam、ix.kw/TEC、Microsoft Azure Region 意向、Google Cloud 意向。
> 本 skill 汇总两份探索报告：官方/监管管线（explorer-official.md）与行业/厂商发现（explorer-industry.md），字段级 A/B/C/U 分级。

## 入口

| 文件 | 管线 |
|---|---|
| explorer-official.md | 官方/监管管线：CITRA、Kuwait Municipality（baladia）、MEW、CAPT/e.gov.kw、KDIPA、KUNA、官方云区域清单、运营商一级来源（Syntys/Iron Mountain/Ooredoo 平台文件） |
| explorer-industry.md | 行业/厂商发现：Syntys/Ooredoo/Iron Mountain 新闻室、DCD/Reuters/Kuwait Times/Arab Times/Al Qabas 等媒体、Submarine Networks/海缆、目录聚合器与市场报告 |

## 核心结构事实（框定每次搜索）

1. 科威特**没有公共国家数据中心登记册**；CITRA 监管电信/ICT 牌照与服务，但其公共服务菜单不暴露数据中心登记；Kuwait Municipality 为建筑许可路线、MEW 为电力路线、CAPT/e.gov.kw 为采购路线。
2. 商业数据中心证据集中在 **Kuwait City/Capital** 与电信关联平台；Capital 之外视为 Syntys/Ooredoo 线索、企业/政府站点或负面清扫，直到一级来源点名设施。
3. 超大规模公告保持 **`planned_or_mou`** 直到官方位置清单或运营商/政府启用/施工来源另有说明；2026-08-12 核验 Azure/Google Cloud/AWS/Oracle 官方区域页均无科威特条目。**Microsoft Azure Region 意向（2025-03-06，Microsoft/CAIT/CITRA 三方）**与 **Google Cloud 公告（2023-01）**均为意向级。
4. **Syntys** 是主要一级来源路线：2025-03 自 Ooredoo 分拆；Iron Mountain 列出科威特位置 Kuwait City 与 Shuaiba；Ooredoo 托管的 Syntys deck 显示科威特 2 个活跃 DC、约 2.2 MW 活跃 IT 负载 + 2 MW 当前容量——A 级平台/国家级容量语境，站点级 MW 不得推断。
5. **ix.kw**（2019-10-20 CITRA 宣布的运营商中立 IXP，TEC Building 联系点）与海缆登陆（FALCON、FOG、GBI、Kuwait-Iran、MEETS/EIG）为 `connectivity_only`，除非同一来源明确说明该站点有数据中心服务。
6. **阿拉伯语搜索强制**：数据中心术语 + 阶段动词（افتتاح 开业、تدشين 启用、إطلاق 发布、وضع حجر الأساس 奠基、تخصيص أرض 划地、دخول الخدمة 投运）。
7. 状态纪律：`operational` / `under_construction` / `land_or_permit` / `planned_or_mou` / `cloud_edge_or_dedicated_region` / `connectivity_only` / `negative_sweep`；容量字段分离（it_mw / facility_power_mw / grid_connection_mva / racks / white_space_sqm / land_area_sqm / announced_campus_mw），不得把 GPU/云区域语言并入共置 MW。
8. 覆盖规则：每次运行六省都必须产出正面种子或带查询日志的负面清扫；国家云 MoU 不覆盖任何省。`Tier III-designed`/`built to Tier III standards` 是设计声称，不是 Uptime 认证；无 Uptime 清单确认不得记录科威特认证设施。

## 查询模式（复制粘贴模板见 explorer-official.md §2 / explorer-industry.md §3-§5）

- 监管/IXP：`site:citra.gov.kw ("data center" OR "مركز بيانات" OR "cloud" OR "سحابية")`；`site:ix.kw ("TEC" OR "landing station" OR "members")`；`site:kuna.net.kw ("مركز بيانات" OR "الحوسبة السحابية") الكويت`
- 许可/采购/投资/电力：`site:baladia.gov.kw ("مركز بيانات" OR "رخصة بناء")`；`site:capt.gov.kw ("data center" OR "cloud" OR "استضافة")`；`site:kdipa.gov.kw ("data center" OR "ICT")`；`site:mew.gov.kw ("مركز بيانات" OR "محطة تحويل")`
- 云区域状态：`site:learn.microsoft.com/en-us/azure/reliability/regions-list Kuwait`；`site:cloud.google.com/about/locations Kuwait`；`site:aws.amazon.com/about-aws/global-infrastructure/regions_az/ Kuwait`；`site:oracle.com/cloud/data-regions Kuwait`；`site:news.microsoft.com/en-xm Kuwait "AI powered Azure Region"`
- 运营商一级：`site:syntys.com Kuwait ("Kuwait City" OR Shuaiba)`；`site:ironmountain.com/data-centers/locations/syntys-data-center Kuwait`；`site:kw.zain.com ("Zain Business Data Center" OR ZBDC)`；`site:stc.com.kw ("Data Center 1" OR "Data Center 2")`；`("Zajil" OR "Kalaam") Kuwait ("data center" OR "Tier III")`；`site:ooredoo.com Kuwait (NVIDIA OR H200 OR Syntys)`
- 媒体：`site:datacenterdynamics.com/en Kuwait (Microsoft OR Azure OR Google OR Syntys OR Ooredoo)`；`site:kuwaittimes.com Kuwait ("data center" OR ZBDC)`；`site:alqabas.com الكويت ("مركز بيانات" OR "سحابة" OR "ذكاء اصطناعي")`
- 阿拉伯语启动/许可：`("افتتاح" OR "تدشين" OR "إطلاق" OR "وضع حجر الأساس") ("مركز بيانات") الكويت`；`("تخصيص أرض" OR "ترخيص بناء") "مركز بيانات" الكويت`
- 省级清扫：`"{district}" "data center" Kuwait`；`Mishref OR Salmiya OR Hawalli "data center"`；`Shuaiba OR "Mina Abdullah" OR "Al Zour" "data center"`；`Jahra OR Sulaibiya OR Subiya "data center"`；`"Mubarak Al-Kabeer" OR "Sabah Al-Salem" "data center"`
- 认证核验：`site:uptimeinstitute.com Kuwait ("Zain" OR Ooredoo OR Syntys OR Zajil OR stc)`

## 官方/监管管线要点（详见 explorer-official.md）

- CITRA 为监管表面：服务含 ISP/SubISP、Licensing、Tenders、.kw 域名；新闻含 2026-07-13 华为数字化转型 MoU；ix.kw 由 CITRA 于 2019-10-20 宣布（A 级 IXP 启用与角色）。
- CITRA Data Privacy Protection Regulation（Resolution No. 42）为隐私合规语境；不是设施来源。
- KDIPA 为 FDI 许可/激励路线（税收/关税豁免、土地/不动产划拨可能）；MEW 为电力机构路线（无公开 DC 负载登记）；Kuwait Municipality 为建筑/许可路线（无公开可搜索 DC 许可登记）。
- CAPT 与 e.gov.kw 为高价值国家采购路线；KUNA 为官方国家新闻（搜索阿/英启运、MoU、部委数据中心声明）。
- 验证工作流：URL 解析且仍支持精确声称；省名归一为六个 repo 分区（区/阿拉伯别名另记）；每个候选一个状态；云意向不得升级为运营；Syntys/Ooredoo 区分国家/平台容量与站点级容量；每次运行查官方云区域清单；Uptime 单独核验后才记录认证等级。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 科威特仍是小型、电信主导市场；Ooredoo/Syntys 分拆显著改善来源质量。Syntys 于 2025-03 成立，Iron Mountain 少数股权/合资，位置 Kuwait City 与 Shuaiba，服务含共置、AI 部署、运营商中立连接、Tier III 设计。
- **Syntys Kuwait City**（Capital）：Iron Mountain 点名 A 级位置；Al-Soor St 等目录地址 C 级。**Syntys Shuaiba**（Ahmadi）：A 级位置，Capital 外最强公共共置线索。
- **Ooredoo Kuwait 主权 AI 数据中心**：媒体称 NVIDIA H200 GPU/本地 DC（B 级启运新闻）；Ooredoo 集团 NVIDIA 区域计划（含科威特）A 级区域计划；需 Ooredoo Kuwait/Syntys 页面才升 A。
- **Zain Business Data Center / ZBDC**：Zain 商务菜单与本地媒体命名（A/B 服务存在）；设施地址/规格需当前运营商页或合同来源（目录 C）。
- **stc Data Center 1 / Data Center 2**：stc 2024 可持续发展报告在评估关键地点点名（A 级存在）；公共商业名与地址需佐证。
- **Zajil/Kalaam**：DCD/Submarine Networks 报道 Kalaam 收购 Zajil 并点名科威特 DC（B）；Tier III 为设计声称。
- **Microsoft/Zain/ZainTech 国家云**（2023-02）：用 Zain 私有云基础设施的国家云计划，支持数据驻留框架（A 级计划）。
- 历史线索不计活跃：Omniva/Moneta Sea City（Al Khiran）GPU/加密计划（C 级分析）；PACI/Mishref（Hawalli）C/U；KOC/KNPC/KIPIC 石油部门 IT 为企业线索（C/U）。

## 已知设施/项目与证据状态

| 设施/项目 | 分区 | 状态与证据 |
|---|---|---|
| Syntys Kuwait City | Capital | operational；Iron Mountain/Syntys A 级位置；地址细节 C |
| Syntys Shuaiba | Ahmadi | operational；Iron Mountain A 级位置 |
| Syntys/Ooredoo 科威特平台容量 | Capital + Ahmadi（国家级） | operational 平台语境；2 活跃 DC、~2.2 MW IT 负载（Ooredoo deck A）；不按站点分配 |
| Ooredoo Kuwait 主权 AI DC | 未披露（可能在 Syntys/Ooredoo 足迹内） | operational（媒体）或 operator_lead；H200/本地 DC 为 B；区域计划 A |
| Zain Business Data Center / ZBDC | Capital（可能） | operational；服务 A/B；地址 C |
| stc Data Center 1 / Data Center 2 | Capital（可能，站点未知） | operational；stc 可持续报告 A 级存在 |
| Zajil / Kalaam 科威特 DC | Capital（可能） | operational；DCD/Submarine Networks B；Tier III 设计声称 |
| Microsoft AI-powered Azure Region | 未披露 | planned_or_mou；Microsoft/CAIT/CITRA 意向 A 级（2025-03-06） |
| Google Cloud 科威特区域 | 未披露 | planned_or_mou；2023-01 协议 B/A（报道）；官方位置清单无条目 |
| ix.kw / TEC Building | Capital | connectivity_only；IXP A 级，非共置 |
| 海缆登陆 FALCON/FOG/GBI/Kuwait-Iran、MEETS/EIG | Capital/连接性 | connectivity_only（B/C）；仅网络邻近性 |
| Omniva/Moneta Sea City GPU/加密计划 | Ahmadi（Al Khiran） | 历史 planned_or_mou（C）；不计活跃 |
| PACI / Mishref 系统 | Hawalli | 企业/政府线索或负面清扫（C/U） |
| Hawalli/Farwaniya/Jahra/Mubarak Al-Kabeer 清扫 | 各省 | 无公共共置则记录 negative_sweep（带查询日志） |

## 更新节奏

- 月度：Azure/GCP/AWS/Oracle 区域清单；Microsoft Kuwait 新闻室；Google Cloud 科威特搜索；CITRA 新闻；KUNA 阿语搜索；Syntys/Iron Mountain/Ooredoo 新闻室；DCD Kuwait tag。
- 季度：Zain、ZainTech、stc Kuwait、Kalaam/Zajil 运营商页；CAPT/e.gov.kw 招标扫描；KDIPA/KAPP/baladia/MEW 搜索。
- 半年：目录对账（DataCenterMap/datacenters.com/Baxtel/datacenterHawk/PeeringDB）、Uptime 认证清单、六省全量负面清扫。
- 事件触发：超大规模区域启用、Syntys 扩张、政府云授予、土地/电力招标、新海缆登陆、公共 AI/GPU 基础设施公告。
- 待办（2026-08-12）：Ooredoo Kuwait AI DC 官方页面确认；Syntys 站点级页面/地址；ZBDC 与 stc DC 地址与规格；Azure/Google 科威特区域状态月度跟踪；codex terra agent 分批复核后按本方法论推进。
