---
name: eh-datacenter-methodology
location: scripts/expansion/world/country-skills/EH/SKILL.md
description: 西撒哈拉数据中心双线查询方法论（官方/监管/云管线 + 行业/厂商/媒体发现），含 division 模型、来源 A/B/C 分级与查询模板；English: dual-line datacenter discovery & audit methodology for Western Sahara (official/regulatory/cloud pipeline + industry/vendor/media discovery), with division model, A/B/C source grading and query templates. 运行 EH 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。
---

# EH · 西撒哈拉数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> **目的**：为西撒哈拉（Western Sahara, EH）的数据中心探索与审计提供统一双线方法论。官方/监管/云管线段负责验证与定稿，行业/厂商/媒体段负责发现与线索，两线互为三角验证。本文件由 codex 审核定稿的两份 explorer 合并而成，细节以 `explorer-official.md`（官方线）与 `explorer-industry.md`（行业线）为准。

## 入口

| 文件 | 职责 | 内容摘要 |
|---|---|---|
| `explorer-official.md` | 官方/监管/云管线：验证与定稿 | 摩方机构（MTNRA/MMSP、ANRT、CRI、AMDIE、ONEE/MASEN、CNDP、采购）、UN/MINURSO、运营商与认证页、海缆路由；分桶官方枚举与验证规则 |
| `explorer-industry.md` | 行业/厂商/媒体发现：线索与预筛 | 行业媒体（DCD、Reuters、Ecofin、Medias24、Le360、TelQuel、Yabiladi、MAP）、目录站、SADR/波利萨里奥侧来源；枚举矩阵与分级规则 |

## 核心结构事实

1. **行政区划模型**：manifest 为单一 division — `["Western Sahara"]`（subnational_type=country）。任何 Laayoune/Dakhla 等标签只是 locality 或内部覆盖桶，禁止作为 division 值入库。
2. **注册库现状**：西撒哈拉没有独立的国家数据中心注册库、规划许可检索门户、电信监管机构或电力监管机构；官方枚举依赖摩洛哥管理的机构（西部/沿海）、UN/MINURSO（任务足迹）与 SADR/波利萨里奥（仅归因声明）。
3. **法律与监管**：摩方行政体系下由 ANRT 管电信许可/频谱/互联（不把数据中心作为独立设施类别发牌）、CNDP 管数据保护（通知不代表设施证明）；采购线含摩方 `marchespublics.gov.ma` 与 UN 的 `ungm.org`/MINURSO。
4. **互联与云**：无已确认的公有云区域；Dakhla 的 Maroc Telecom West Africa 海缆登陆仅为 B/C 级线索（缺 IAM 一手页），WACS 不用于 Dakhla 证据；登陆站不等于数据中心。
5. **设施/项目种子（2026-08 复核基线）**：唯一 A 级官方线索为 **Igoudar Dakhla / Igoudar Numérique 绿色数据中心园区**（Dakhla，状态 `planned / studies launched`，目标容量 500 MW，证据：MTNRA/MMSP 2025-11-14 协议页与 2026-04-14 合作公约页）；未确认任何运营中的商业托管/超大规模设施。
6. **语言与词汇**：法语（centre de données、hébergement、colocation、CRUI/CRI、provinces du Sud、Igoudar 等）、阿拉伯语（مركز البيانات、الاستضافة、الاقاليم الجنوبية、العيون、الداخلة 等）、西班牙语（centro de datos、Sáhara Occidental、El Aaiún、Dajla 等）三语检索。
7. **可靠性分级（A/B/C）**：A=官方或一手证据（部委/监管/CRI/采购/公用事业页、UN/MINURSO 页、运营商自有设施页、Uptime 认证、官方海缆页）；B=强二手（Reuters、DCD、Ecofin、MAP 转载、Medias24、Le360、TelQuel、Yabiladi 等具名有日期媒体）；C=仅线索（目录、市场报告、社媒、截图、无署名声明）。分级按单条事实判定。
8. **计数与去重规则**：MW/MVA/kVA/racks/sqm 仅在来源把它绑定到具名数据中心站点时记录；新能源 MW、海缆容量、电信骨干容量、港口/园区电力计划只是背景；海缆登陆站、电信机房、云服务、培训机构、研究机构、港口、自由区除非来源点名数据中心设施否则不计入。

## 常用查询模板

```text
# 官方线
site:mmsp.gov.ma "Igoudar Dakhla"
site:mmsp.gov.ma "Igoudar numérique" "500 mégawatts"
site:cri-invest.ma "Dakhla" "datacenter"
site:marchespublics.gov.ma "Dakhla" "Igoudar"
site:anrt.ma "centre de données"
site:masen.ma "Laayoune" OR "Boujdour" OR "Dakhla"
site:cndp.ma "hébergement" "Dakhla"
site:ungm.org "MINURSO" "server room"
# 行业线
site:datacenterdynamics.com/en/news/ "Dakhla" "data center"
site:reuters.com "Dakhla" "data center" "Morocco"
site:ecofinagency.com "Dakhla" "data center"
site:medias24.com "Igoudar" OR "Dakhla" "datacenter"
"Dakhla" "500 MW" "data center"
"Maroc Telecom West Africa" "Dakhla" "landing"
"Laayoune" OR "Laâyoune" OR "El Aaiún" "data center"
# 阿语/西语
"الداخلة" "مركز البيانات" "Igoudar"
"العيون" "مركز البيانات"
"Sáhara Occidental" "centro de datos"
"Dajla" "centro de procesamiento de datos"
# 东侧/波利萨里奥侧（仅归因线索）
site:spsrasd.info "data center" OR "centro de datos"
"Polisario" "telecom" "data center"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **MTNRA/MMSP（数字转型部）**：`mmsp.gov.ma/fr` 为 Dakhla 数据中心管线最强官方源；Igoudar 两页为 A 级证据，但只支持 `planned / studies launched`，不得据此标记在建或运营。
- **ANRT**：电信许可/频谱/互联背景（A 可达时）；不为数据中心单设设施牌照。
- **CRI/CRUI**：`cri-invest.ma` 投资批准、土地、许可与区域公告；Laayoune-Sakia El Hamra 地图路径 `/map/my-cri/9`。
- **AMDIE**：投资促进（域可达但本环境 403）；仅 AMDIE 自撰项目细节为 A。
- **ONEE/MASEN**：电网与新能源背景（Noor Laayoune、Noor Boujdour；Tarfaya 风电在 EH 外）；不自动作为 IT 负载证据。
- **CNDP**：数据保护法律背景。
- **采购**：摩方 `marchespublics.gov.ma` 与 UN `ungm.org`/MINURSO；招标/中标只证明采购事件本身。
- **运营商/认证/海缆**：Uptime Institute 摩洛哥列表（`uptimeinstitute.com/.../id/MA`）、IAM（403 需重查）、WACS 官方（仅系统存在性）、ANP/达赫拉大西洋港（背景）、装备部（基础设施背景）。
- **访问纪律**：超时/TLS/403/验证码的 URL 保留并标 `recheck`，不得臆造替代地址。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **高信号源**：DCD、Reuters、Ecofin Agency、Medias24/Le360/TelQuel/Yabiladi/MAP（摩方区域媒体，B）、Uptime 摩洛哥列表（A）、IAM（可达时 A）、UNGM/MINURSO（A 但多为内部 IT 采购）。
- **目录站（DataCenterMap、Datacenters.com、Baxtel、Cloudscene、datacentercatalog 等）仅作 C 级发现**，无 A/B 支撑不得断言状态、容量、认证或精确地址。
- **分级与升级**：Huawei/Reuters/DCD/Ecofin 及区域媒体的 Igoudar 报道为 B，除非运营商自出项目/设施页；Igoudar 进入 `planned` 需 A 级官方证据，措辞用 `500 MW target capacity`。
- **排除项**：卡萨布兰卡/拉巴特/Settat/Benguerir/Nador/Tarfaya 等摩洛哥本土资产、Xlinks 摩英电力项目均不入 EH；WACS/Dakhla 说法视为错误除非新一手证据出现，达赫拉海缆线索查 Maroc Telecom West Africa。
- **诚实结论**：无运营中商业托管/超大规模/公有云区域确认；政治敏感区域用来源归因式中性措辞（"Moroccan-administered source states…" / "SADR/Polisario source states…" / "UN source states…"）。

## 维护注意（更新纪律）

- **更新节奏**：事件驱动 — Igoudar 相关官方公告（合同、采购中标、建筑许可、环评、施工通知、运营商上线页）一出现即核对并升级状态；海缆一手页（IAM/Maroc Telecom West Africa）出现即补。
- **来源核验**：升级任何状态需新的一手证据 URL；500 MW 必须绑定 Igoudar/Igoudar Numérique 并标注为目标容量；每记录必含 operator、facility/project 名、locality、division（`Western Sahara`）、内部桶、状态、证据 URL、来源归属。
- **不删除纪律**：本目录只允许新增/更新文件，禁止删除或移动任何文件；失败 URL 保留原样加 `recheck`。
