---
name: mr-datacenter-methodology
location: scripts/expansion/world/country-skills/MR/SKILL.md
description: |
  Mauritania (MR) datacenter discovery & audit methodology — how to enumerate, verify, and update Mauritania datacenter projects at wilaya/region granularity (15 manifest regions). Mauritania has no public national datacenter register and no hyperscaler cloud region; the market is nascent and state-led. Enumeration joins AMI state news, MTNIMA ministry tenders/contracts, ARE regulator publications, ARMP procurement, EIB/EEAS/World Bank donor pages (WARCIP/WARDIP), Uptime Institute certification records, and SDIN/IMT/operator pages. The only A-grade public facility anchor is Nouakchott Data Hub (West Nouakchott, inaugurated 8 May 2025, 1,372 m2, 100 racks expandable, Tier III design + constructed-facility certification, SDIN owner / IMT operator, EUR 15m EIB loan). Read this before running MR exploration/audit batches. Routes to explorer-official.md (AMI/MTNIMA/ARE/EIB/WB/Uptime pipeline) and explorer-industry.md (press/vendor/directory/division matrix).
---

# MR · 毛里塔尼亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：毛里塔尼亚**没有**公开的全国数据中心注册库、**没有**可比美式的可检索规划许可门户，也**没有**任何超大规模云公共区域——市场为**国家主导的新生市场**。
> 枚举靠**官方新闻 + 采购 + 监管 + 捐助方 + Uptime + 运营商**联合：AMI 国家通讯社、MTNIMA 数字部招标/合同、ARE 监管局、ARMP 公共采购、EIB/EEAS/世界银行（WARCIP/WARDIP）、Uptime Institute 认证、SDIN/IMT 与电信运营商页面。
> 唯一 A 级公共设施锚点：**Nouakchott Data Hub**（West Nouakchott，2025-05-08 启用，1,372 m2、100 机架可扩展、Tier III 设计+竣工认证、SDIN 持有/IMT 运营、EIB 1,500 万欧元贷款）。本 skill 汇总两份探索报告（官方管线 + 行业发现），供毛里塔尼亚探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/捐助方管线：AMI、MTNIMA（Government Cloud 合同、EllaLink 登陆、Digital Agenda）、ARE（互联目录、年度报告）、EIB/EEAS/Global Gateway、世界银行 WARCIP/WARDIP、Uptime 认证、SDIN/IMT/运营商、ARMP 采购、云区域缺失核查、15 省映射表与逐省官方工作流 |
| `explorer-industry.md` | 行业/厂商发现：贸易媒体分级（DCD/DCmag/Ecofin/We Are Tech/CIO Mag）、本地媒体、运营商与集成商扫掠（SDIN/IMT/Mauritel/Mattel/Chinguitel/SNIM/BU-WAC）、目录处理（DataCenterMap 等 C 级）、已知线索校准表、逐省行业矩阵、验证路径 |

## 核心结构事实（框定每次搜索）

1. **无全国注册库/无云区域**：AWS/Azure/GCP/OCI 官方区域页均无毛里塔尼亚——只作缺失证据，不排除私有云/政府云/边缘缓存/CDN/合作伙伴托管/企业机房。
2. **唯一 A 级设施锚点 = Nouakchott Data Hub**（West Nouakchott / Nouakchott-Ouest，Tevragh-Zeina 一带）：AMI 确认 1,372 m2、100 机架可扩展、全国托管/云/备份/业务连续性/AI 大数据服务、IMT 运营；EIB 确认 1,500 万欧元贷款覆盖建筑、监理与 Tier III 认证；Uptime 列出 **Tier III Certification of Design Documents + Constructed Facility**（客户 SDIN）。只建**一条**设施记录；`capacity_mw=null`（除非官方公布精确电力）。
3. **SDIN vs IMT 角色分离**：SDIN（Societe pour le Developpement des Infrastructures Numeriques，https://sdin.mr/）是国家基础设施所有者（WARCIP 资产转移公约含国家骨干、Datacenter、IXP）；IMT（International Mauritania Telecom，政府经 Mauripost + 三家电信运营商）负责运营 Data Hub——**不要为 IMT 另建第二条设施记录**，除非来源命名另一物理站点。SDIN 旧文案称"在建"，须与 2025 AMI/EIB/Uptime 启用认证证据对账。
4. **WARDIP Government Cloud ≠ 设施**：MTNIMA 公共合同页列出 WARDIP "Acquisition et mise en place d'un Cloud Gouvernemental"（合同 1320/F/011/CPMP/MTNIMA/WARDIP/2025，中标 HMN SMART CO LTD，2025-06-24 签，MRU 103,611,370，12 个月）——A 级政府云平台采购，**不是** Nouakchott Data Hub 之外的新物理设施，除非来源点名独立站点。
5. **海缆 ≠ 数据中心**：EllaLink 第二条分支 2026-05-05 MTNIMA 确认 Nouadhibou 登陆 + 中立登陆站；BU-WAC/WAC 在 Nouadhibou 终端站登陆（ARE 目录）；ACE 相关连通性——全部只算**电信/连通性上下文**，除非后续来源点名计算/机架/colo。
6. **语言**：法语是官方搜索最高产语言；阿拉伯语用于 MTNIMA/AMI 镜像；英语用于 EIB/EEAS/世界银行/DCD/海缆源。词表：`centre de donnees`、`centre d'hebergement de donnees`、`cloud gouvernemental`、`cloud souverain`、`salle serveur`、`centre de calcul`、`station d'atterrissement`、`point d'echange internet`、`مركز البيانات`、`استضافة البيانات`、`مناقصة`。
7. **四类非 DC 类别**：一切其他线索先归入 telecom/cable landing、IXP/network node、institutional server room/compute center、cloud-service procurement 之一——有具名物理设施（building/centre de calcul/salle serveur/rack hall）才建数据中心记录。

## 查询模式（复制粘贴模板见 explorer-official.md §1 与 explorer-industry.md §0-§5）

- AMI：`site:ami.mr/fr "data center"`、`site:ami.mr/fr "centre d'hebergement de donnees"`、`site:ami.mr/fr "{wilaya_fr}" "numerique"`、`site:ami.mr/ar "مركز البيانات"`。
- MTNIMA：`site:mtnima.gov.mr/fr "Cloud Gouvernemental"`、`site:mtnima.gov.mr/fr "data center" OR "datacenter" OR "centre de donnees"`、`site:mtnima.gov.mr/fr "cable sous-marin" OR "fibre optique"`。
- ARE：`site:are.mr "centre de donnees"`、`site:are.mr "{operator}" "catalogue"`、`site:are.mr "{operator}" "licence"`。
- 采购：`site:armp.mr "data center" OR "datacenter" OR "centre de donnees" OR "cloud"`、`site:armp.mr "salle serveur"`、`site:armp.mr "{buyer}" "{locality}"`。
- 捐助方：`site:projects.worldbank.org Mauritania WARCIP`、`site:projects.worldbank.org Mauritania WARDIP`、`site:eib.org Mauritania data center`、`site:eeas.europa.eu Mauritania datacenter`、`site:international-partnerships.ec.europa.eu Mauritania data center`。
- Uptime：`site:uptimeinstitute.com Mauritania`、`site:uptimeinstitute.com "Nouakchott Data Hub"`。
- 运营商：`site:sdin.mr "Nouakchott Data Hub"`、`"International Mauritania Telecom" "Nouakchott Data Hub"`、`site:mauritel.mr "cloud" OR "hebergement"`、`"SNIM" "centre de donnees" "Zouerate"`。
- 行业：`site:datacenterdynamics.com/en/news/ Mauritania EllaLink`、`site:dcmag.fr "Nouakchott Data Hub"`、`site:agenceecofin.com Mauritanie "centre de donnees"`。
- 通用 division：`"{division}" "data center" Mauritania`、`"{wilaya_fr}" "centre de donnees" Mauritanie`、`"{locality}" "salle serveur"`、`"{wilaya_ar}" "مركز البيانات"`。

## 官方/监管管线要点（详见 explorer-official.md）

- **AMI**（https://ami.mr/fr/，EN 镜像 /en/）：总统就职/奠基/部长视察的权威记录；Data Hub 启用稿 AMI FR 2025-05-08（https://ami.mr/fr/archives/270548）；能确认设施/项目阶段，但**极少给 MW/MVA**。
- **MTNIMA**（https://mtnima.gov.mr/fr/）：政府云采购、EllaLink Nouadhibou、Digital Agenda 2022-2025、WARDIP 云迁移通知；公共合同页 2024-08 至 2025-08。
- **ARE**（https://www.are.mr/）：电信牌照/互联状态与运营商目录（Mattel、Mauritel、Chinguitel、IMT、SNIM、IKASIRA、RIMATEL、SOMELEC）；BU-WAC 目录证明 WAC 分支在 Nouadhibou 终端站登陆；5G 授权（Ecofin：四候选、总报价 2,700 万）。
- **EIB/EEAS/Global Gateway**：EIB 2025-05-09 稿确认 8 May 2025 启用、EUR 15m 贷款、Tier III 认证覆盖、WARCIP 背景、IMT 管理；Global Gateway 页确认"数据中心 + 海缆"配套政策包（含连接、湿站、陆缆段、登陆站）。**不把欧元贷款换算成容量**。
- **世界银行 WARCIP/WARDIP**：WARCIP=国家骨干/ACE 相关连通性/SDIN 资产/Data Hub 背景；WARDIP=政府云、NREN、数字支付、公共服务、跨境集成、新缆容量骨干分发——云组件是服务/平台线索。
- **Uptime**（https://uptimeinstitute.com/uptime-institute-awards/country/id/MR）：Nouakchott Data Hub 两项 Tier III 认证（Design Documents + Constructed Facility），客户 SDIN。
- **ARMP**（https://armp.mr/）：MTNIMA 页未披露时的采购决定；买方含 MTNIMA、内政、财政、卫生、高教、国防、BCM、SNIM、SOMELEC、PANPA、TCN、机场、港务。提取买方/合同号/中标方/日期/阶段/对象/地区/是否点明站点/合同类型（设施建设、设备供应、托管服务、云迁移、维保、网络安全运营）。
- **运营商**：Mauritel/Mattel/Chinguitel/Rimatel/SNIM/IKASIRA/BU-WAC/SOMELEC 是电信/网络种子；目录与服务页**不证明商业数据中心站点**——须点名服务器机房/核心网中心/云平台/设施地址。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **高信号媒体**：DCD（EllaLink/海缆/电信市场，B）、DCmag.fr（Data Hub 启用，B）、Agence Ecofin（Data Hub/IXP/5G 牌照/运营商名单，B）、We Are Tech（B/C）、CIO Mag（EllaLink，B）、世界银行博客（B，正式项目文件才 A）、本地媒体 rapideinfo/ladepeche/cridem/trustmag（B/C，引用具名官员或文件才 B）、Agenzia Nova（奠基线索，B/C，须与 EIB/AMI 对账）。
- **运营商/集成商**：SDIN（A 资产所有者）、IMT（经 AMI/EIB/ARE 确认，无稳定官网）、Mauripost（政府股东通道）、Mauritel（Maroc Telecom 集团云页**不是**毛里塔尼亚设施）、Mattel（2023 华为 5G 试验）、Chinguitel（2026 5G 商用报道，设施证据仍缺）、Rimatel（5G 竞标新进入者）、SNIM（Nouadhibou/Tiris Zemmour 矿业走廊，须显式设施证据）、IKASIRA（监管种子）、BU-WAC（Mauritel 海缆分支单位，电信上下文）、Huawei/HMN SMART（HMN 中标政府云合同——厂商参与≠设施所有）、Schneider/Vertiv/Delta/Rittal/Eaton（案例页 B/C）、本地 IT 商（smpnt/gitss/maurisoft/sysoftdata/saharadev，C 线索）。
- **目录处理**：DataCenterMap/datacenters.com/datacenterslist/thebuildout.ai/neocloud.asia 默认 C；捕获名称/运营商/地址/声称 tier/容量→按精确名称在 AMI/MTNIMA/EIB/Uptime/SDIN/运营商站核验→ARMP/MTNIMA 找合同→DCD/DCmag/Ecofin 确认→有主源则主源进 `source_urls`，目录仅作地址别名。
- **生命周期动词（法语）**：`inaugure`/`mis en service`/`operationnel`/`certifie Tier III`=运营信号（AMI/EIB/Uptime 验证）；`pose de la premiere pierre`/`lancement des travaux`/`en construction`=施工；`appel d'offres`/`attribution`/`contrat signe`=采购；`cloud`/`VPS`/`hebergement`/`bare metal`=仅服务证据；`station d'atterrissement`/`wet station`/`IXP`=电信设施。
- **最高优先级 division**：West Nouakchott（Data Hub/SDIN/IMT/大学计算中心/电信总部/银行/部委/SOC-CSIRT）；Nouadhibou Peninsula（EllaLink/WAC 登陆站、SNIM、港口/自由区 IT——紧盯登陆站旁新增数据大厅）。

## 来源分级

- **A** = 声称事实的一手源：AMI 国家新闻；MTNIMA 招标/合同/新闻页；ARE 监管发布；ARMP 采购通知/决定；EIB、EEAS/EU Global Gateway、世界银行项目页/项目文件；Uptime 认证记录；SDIN/IMT/官方运营商页。分级按声称事实（ARE 确认牌照/互联≠数据中心；MTNIMA 确认采购阶段≠完工；EIB 确认融资范围≠MW；Uptime 确认认证≠运营商/机架数/公共 colo 服务）。
- **B** = 强二级作线索/上下文：DCD、DCmag.fr、Agence Ecofin、We Are Tech、CIO Mag、世界银行博客、引用具名官员或项目文件的可靠毛里塔尼亚媒体。
- **C** = 仅弱线索：目录、泛市场报告、顾问 SEO 页、招标聚合器、社交帖、LinkedIn 声称、不识别物理设施的运营商服务页。
- 状态语义：operational=AMI/EIB/官方启用证据（Data Hub 已满足）；施工=奠基/动工官方证据；采购=合同/中标证据（非设施）；`no_projects=true` 仅当官方新闻+采购+监管+精确地名检索均负且排除泛 Nouakchott/全国性结果后。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=MR，divisions=15 省区）。
2. 建种子：Nouakchott Data Hub（单条记录）、WARDIP 政府云（平台采购）、大学 Centre de Calcul（B）、EllaLink/WAC 登陆站（上下文）。
3. 逐 division 执行官方工作流：锚点精确设施检索（AMI/MTNIMA/EIB/EEAS/Uptime/SDIN/ARMP）→ wilaya 官方新闻过（AMI+MTNIMA，法/阿/英）→ 监管过（ARE）→ 采购过（MTNIMA/ARMP/公企）→ 捐助方过（EIB/EEAS/WB）→ 设施测试（具名物理设施才建记录）。
4. 验证：每条 A 级声称用对应一手源；`capacity_mw=null` 除非精确电力公布；非 MW 细节（1,372 m2、100 racks、Tier III、海缆登陆、IXP、云合同金额）记入 notes。
5. 去重/归属：division 用 manifest 名 + 本地 wilaya 别名进 notes；泛 "Nouakchott" 线索默认 `division_uncertain` 除非 locality 佐证（当前 Data Hub/SDIN/大学证据支持 West Nouakchott）；Nouadhibou 不把登陆站/港口机房当数据中心。
6. 输出 world schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`。
7. 遵守 NO-DELETION；只新增 SKILL.md 与 ANATOMY.md。

## 待办（2026-08-12 02:59Z）

- [x] explorer-official.md 与 explorer-industry.md 已完成并合并为本 SKILL.md。
- [ ] 下一步：50× codex terra agent 按 15 division 逐省枚举（优先 West Nouakchott、Nouadhibou Peninsula、Trarza/Eastern Basin 边境走廊）。
- [ ] 待核实：Data Hub 实际运营租户与电力（MW）证据；SDIN 站点文案更新；Nouadhibou 登陆站旁是否出现计算/colo 设施；Mattel/Chinguitel/Rimatel 5G 核心机房具名设施证据；云区域列表是否新增毛里塔尼亚。
