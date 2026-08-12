---
name: bj-datacenter-methodology
location: scripts/expansion/world/country-skills/BJ/SKILL.md
description: |
  Benin (BJ) datacenter discovery & audit methodology — how to enumerate, verify, and update Benin datacenter projects at department granularity (12 departments, 77 communes in the current manifest). Benin has no public national datacenter register: enumeration chains name/operator → commune building permit (permis de construire, service PS00141) → ABE environmental authorization/EIES → SBEE/SBPE/CEB/ARE power evidence → ARCEP telecom licences → APDP/company records → ministry/ASIN confirmation, plus French-language trade press (Agence Ecofin, DCD, CIO Mag, La Nation) and connectivity hooks (ACE/SAT-3, BENIN-IX). Verified positives: national data centre at Abomey-Calavi and MTN Bénin Data Center product; WARDIP secondary-DC feasibility is pipeline only. Read this before running BJ exploration/audit batches. Routes to explorer-official.md (regulators/permits/environment/power/digital-government/cloud) and explorer-industry.md (operators/trade press/directories/per-department map).
---

# BJ · 贝宁数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：贝宁**没有**全国数据中心注册库，官方枚举是一条“名称/运营商→市镇建设许可→环评（ABE/EIES）→电力（SBEE/SBPE/CEB/ARE）→电信许可（ARCEP）→数字部/ASIN”的证据链；法语优先（`centre de données`、`datacenter`、`salle de serveurs`、`permis de construire`、`étude d'impact`、`station d'atterrissement`）。
> 分区模型：**12 省（departments）**（Alibori, Atakora, Atlantique, Borgou, Collines, Donga, Kouffo, Littoral, Mono, Ouémé, Plateau, Zou），别名 `Atacora/Couffo/Oueme`；产出集中在 **Atlantique（Abomey-Calavi 国家数据中心）** 与 **Littoral（Cotonou 集群：MTN 产品、ACE/SAT-3、BENIN-IX、Alink/ISOCEL 线索）**。
> 无 AWS/Azure/GCP/OCI 公共云区域（官方页负面核查）；MW 披露罕见，保留 sqm/机架/Tier 原单位。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供贝宁探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：ARCEP 决定、创新部/ASIN 数字政府链、市镇建设许可（PS00141）、ABE 环评/EIES、SBEE/SBPE/CEB/ARE 电力、APIEx/GDIZ/Sèmè City 投资区、ACE/SAT-3/BENIN-IX 连接、云负面核查、12 省覆盖图与记录 schema |
| `explorer-industry.md` | 行业/厂商发现：设施与线索清册（国家 DC、MTN、Alink、ISOCEL、SBIN/Celtiis、Sèmè One、ACE/SAT-3、BENIN-IX、WARDIP）、超规模云状态、子海/IXP 证据、贸易媒体（DCD/Agence Ecofin/CIO Mag/La Nation）、目录使用限制、12 省行业发现图、常见假阳性 |

## 核心结构事实（框定每次搜索）

1. **无注册库，链条式取证**：按“名称→许可→环评→电力→电信→公司/数据保护→部委/运营商确认”建立记录；每条主张单独定级（存在 A / 启动日期 B / 面积 C）。
2. **两个已验证正项**：① 国家数据中心 Abomey-Calavi（Atlantique）——2021-06-01 部委页证明开始技术测试、双光纤/安全供电、Tier 3 ANSI/TIA-942 认证流程（A）；La Nation 2019 报 2 公顷地块 + 500 sqm 技术楼（B+/A-）；运营者归属 ASIN/SBIN 待官方确认，商用 colo 未证实。② MTN Bénin Data Center / Collocation Pro（Cotonou，Littoral）——官方产品页（A）+ CIO Mag 2019-06-14 启动（B）；无公开 MW/机架。
3. **法语术语与别名**：`data center national/datacenter national/centre de données national`=Abomey-Calavi；SBIN 正确（目录里的 `SBIM` 是拼写错误，不静默纠正）；Sèmè City 现官方主校区在 Ouidah/Atlantique，Sèmè-Kpodji 仅为历史/搜索别名。
4. **电力证据**：SBEE（配电）、SBPE（发电/批量）、CEB（贝宁-多哥输电）、ARE（监管）；贝宁资料通常只提“安全供电/UPS/发电机/双光纤”，不给 MW。
5. **连接是资产不是设施**：ACE 在 Cotonou/Fidjrossè 登陆、SAT-3/WASC Cotonou 站、BENIN-IX（PeeringDB ix/1017，B）——除非源点名 colo/机架，不计为 DC。
6. **管线**：WARDIP 二级/冗余国家 DC 仅为可行性研究（世界银行采购 OP00432980，A；DCD 称 2026-03-27 截标），选址未定，不建设施记录。
7. **GDIZ 为观察区**：Glo-Djigbé 工业区（Atlantique）战略观察，区内**未发现**已核实 DC 项目。
8. **无超规模云区域**：CDN/缓存/转售/办公室 ≠ 云区域；官方区域页为唯一真值。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§9 / explorer-industry.md §1-§7）

- ARCEP：`site:arcep.bj "centre de données" OR "data center" OR hébergement OR colocation`、`site:arcep.bj "station d'atterrissement" OR "câble sous-marin" OR "fibre optique"`。
- 部委/数字政府：`site:innovation.gouv.bj datacenter OR "centre de données"`、`site:innovation.gouv.bj "Abomey-Calavi" "datacenter national"`、`site:asin.bj "Abomey-Calavi" OR "datacenter national"`、`site:gouv.bj "cloud souverain"`。
- 许可/环评：`site:service-public.bj "permis de construire" "{commune}"`、`"Mairie de {commune}" "permis de construire" "centre de données"`、`site:abe.bj "certificat de conformité" "{operator}"`、`filetype:pdf EIES Bénin "{commune}" datacenter`。
- 电力：`site:sbee.bj "{operator}" OR raccordement`、`site:sbpe.bj "{operator}" OR "Abomey-Calavi" OR "Cotonou"`、`site:are.bj "{operator}"`、`site:cebnet.org "{site}" poste OR transport OR MVA`。
- 连接：`"ACE" "Cotonou" Bénin station OR atterrissement OR Fidjrossè`、`"BENIN-IX" OR "Bénin Internet Exchange" Cotonou`、`site:peeringdb.com Benin OR Bénin Cotonou`。
- 行业：`site:datacenterdynamics.com Benin "data center"`、`site:agenceecofin.com Bénin "data center" OR "centre de données" OR câble`、`site:cio-mag.com Bénin "data center" OR numérique`、`"Bénin" "data center" OR datacenter annonce OR inauguration OR construction`。
- 各省通用：`"{department}" Bénin "data center" OR datacenter OR "centre de données" OR "salle de serveurs"`、`"{capital_or_hub}" "permis de construire" "{operator}" OR datacenter`、`site:arcep.bj "{capital_or_hub}" fibre OR licence`。

## 官方/监管管线要点（详见 explorer-official.md）

- ARCEP（贝宁电信监管）：网络运营商、光纤授权、卫星/VSAT、SVA、互联与编号；**不是**建设许可机构；决定/执照为 A。
- 数字政府链：创新部（innovation.gouv.bj）+ 政府门户（gouv.bj）+ 法律库（sgg.gouv.bj，Code du numérique 2017-20/2020-35）+ ASIN（国家数字执行机构，ASSI/ADN/ANSSI 延续）；国家 DC 测试里程碑为 A。
- APDP（数据保护）：证明数据处理关系，不证明设施。
- 许可与环评：许可在市镇/市政府（PS00141 服务）；ABE 环评/EIES 可暴露发电机数、kVA/MW、燃油量、站点平面与分期。
- 电力：SBEE/SBPE/CEB/ARE 官方文件为 A；报道 MW 无源为 C。
- 云：无 BJ 区域（A 级负面）；WARDIP 为世界银行采购（A）管线。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 贸易媒体：DCD（B+）、Agence Ecofin（B+）、CIO Mag（B）、La Nation（B+/A-，部委视察报道）、24 Heures au Bénin（B-/C+）、OSIRIS（C+/B-）；目录一律 C 且须官方/运营商印证。
- 运营商/实体种子：MTN Bénin（AS37424）、ISOCEL SA（AS37090）、Alink、SBIN/Celtiis、Bénin Télécoms、Moov Africa Bénin、Open BJ——多数是电信/ISP 身份，须设施语言才计入。
- 对账规则：national DC 300 sqm（DataCenterMap）vs 500 sqm（La Nation）双源标注，以部委/官方技术表为准；Alink Benin 勿与其它国家 Alink 混淆；ISOCEL Telecom/ISOCEL SA 去重。
- 假阳性：目录 4 设施计数、`SBIM`、Sèmè 校区归属混乱、Equiano/2Africa/MainOne 无登陆方证据、电信交换机房/移动核心当 DC、MTN 产品当超大规模设施。

## 已知设施/项目与证据状态

| 设施/项目 | 省/市 | 状态与证据 |
|---|---|---|
| Data centre national（Abomey-Calavi） | Atlantique/Abomey-Calavi | A（存在/地点/2021 测试里程碑；部委页）；500 sqm 技术楼/2 公顷为 B+；商用 colo 未证实；SBIN 运营归属待官方确认 |
| MTN Bénin Data Center / Collocation Pro | Littoral/Cotonou | A（官方产品页）+B（2019 启动）；无 MW/机架公开 |
| Alink Telecom Cotonou Datacenter | Littoral/Cotonou | C（目录）；ISP 存在 B/C；无官方 DC 页 |
| ISOCEL Telecom/SA Cotonou | Littoral/Cotonou | B（运营商/连接）；C（DC）；目录线索 |
| SBIN / Celtiis | 全国/Cotonou | A/B（电信角色）；C（目录 DC 运营归属） |
| Sèmè One / Sèmè City DC 提及 | Atlantique/Ouidah（现主校区） | 仅观察（A 校区 / C DC 提及） |
| ACE / SAT-3 登陆站 | Littoral/Cotonou-Fidjrossè | 连接资产（A 海缆/ B 站细节），非商业 DC |
| BENIN-IX | Littoral/Cotonou | B（PeeringDB ix/1017） |
| WARDIP 二级国家 DC | 选址未定 | 管线（A 采购 OP00432980）；不建设施记录 |

## 更新节奏

- 每批次：云区域负面核查、WARDIP 采购/选址更新、国家 DC 运营状态（ASIN/SBIN 官方页）、MTN 产品技术规格、GDIZ/Sèmè City 新公告。
- 季度：12 省负面扫回顾（保留日期与查询记录）、新海缆（Equiano/2Africa/MainOne/WACS）登陆方证据、ABE/ARCEP 新决定。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（12 省粒度）；本 skill 作为国家层参考注入。
