---
name: mk-datacenter-methodology
location: scripts/expansion/world/country-skills/MK/SKILL.md
description: |
  North Macedonia (MK) datacenter discovery & audit methodology — how to enumerate, verify, and update North Macedonia datacenter projects at municipality granularity (80 municipalities in the current manifest). North Macedonia has no public national datacenter registry: enumeration joins e-building permits (E-Odobrenie za gradenje / gradezna-dozvola.mk), municipal urban plans, the 2026-06-18 legal change (Official Gazette No. 134 recognizing data centers as a distinct facility type), environmental/procurement records (ESJN e-nabavki, BPN, MDT), AEK telecom-operator evidence, ERC/MEPSO/EVN energy-grid evidence, official cloud-region checks (no hyperscale MK region — negative context), and operator pages (Interspace, Telesmart, Neotel/neoDC/neoCloud, Net.Bit, Data Center DTS, A1, Makedonski Telekom, government BCDR in Prilep). Beware Greek Western Macedonia false positives. Read this before running MK exploration/audit batches. Routes to explorer-official.md (permits/legal/environment/procurement/telecom/energy/cloud) and explorer-industry.md (operators/trade press/aggregators/investment-promotion/local-language sweeps).
---

# MK · 北马其顿数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：北马其顿**没有**公开的全国数据中心注册库，不能按单一门户枚举。
> 枚举靠**多源连接**：e-建筑许可（E-Odobrenie za gradenje）、市政城市规划、2026-06-18 法律修订（官方公报第 134 号，正式承认“数字数据处理设施”为独立设施类型）、环境/采购记录（ESJN/e-nabavki、BPN、数字化部）、AEK 电信监管证据、ERC/MEPSO/EVN 电网证据、云区域官方负面核查与运营商页。
> 小市场、斯科普里主导的 kolokacija/电信市场；目录覆盖弱；先出市场/政策/线索，再以官方页/许可/采购/AEK/电网确认。
> **希腊西马其顿假阳性**：PPC 西马其顿 300 MW 项目在希腊，不属于北马其顿，勿混入。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供北马其顿探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：e-建筑许可系统与市政规划、2026 法律修订（Gazette No. 134 / MIA / SeeNews / BDK Advokati）、环境与空间文件（ENER/portal.mdt.gov.mk/euprojects/IPA）、公共采购（ESJN/BJN/MDT/OP-EU）、AEK 电信监管与 GIS、ERC/MEPSO/EVN 电网、云区域负面核查、官方/运营商种子表（Interspace/Telesmart/Neotel/Net.Bit/DTS/BCDR Prilep/A1/Telekom）、80 市镇分级枚举策略 |
| `explorer-industry.md` | 行业/厂商发现：MIA/SeeNews/CORD/BalkanEngineer/DCD/Balkan Green Energy 媒体、运营商种子扫描（含马其顿语/拉丁转写/阿尔巴尼亚语词表）、DataCenterMap/Inflect/Data Center Platform/Cloudscene/PeeringDB 目录、投资促进（Invest North Macedonia）与政策渠道、云/CDN 负面核查、马其顿语西里尔搜索模式、市镇级行业策略与假阳性清单 |

## 核心结构事实（框定每次搜索）

1. **无全国注册库**：建设许可是市政实务，2026-06 后国家级数据中心政策成型；官方公报第 134 号（2026-06-18）修订《建筑法》与《城市规划法》，明确承认数字数据存储/处理设施为独立设施类型——2026-06-18 之后的项目检索会因此变好；旧设施可能仍按“电信/技术/商业建筑”描述。
2. **e-建筑许可系统为 A 级主干**：https://www.gradezna-dozvola.mk/（E-Odobrenie za gradenje）为账户制，公开枚举常用市政网页收录的决定/许可通知/申请人名；统计署 aggregate 建设许可数据只作总量上下文。
3. **主地理 = 斯科普里**：Aerodrom、Gazi Baba、Centar、Karpos 及周边工业/电信地址；次级官方或可行市镇：Veles（Net.Bit）、Stip（Neotel/neoCloud/Telekabel）、Makedonska Kamenica（Data Center DTS）、Prilep（政府 BCDR 运营）、Kavadarci（BCDR 旧候选/被否）、Kriva Palanka/Deve Bair（弱线索，须一手确认）。
4. **三语搜索**：英语 + 马其顿语西里尔（дата центар、центар за податоци、серверска сала、колокација、облак/клауд、деловен континуитет、обнова од катастрофи、одобрение за градење、урбанистички план、трафостаница、агрегат、јавна набавка）+ 马其顿语拉丁转写（data centar、server sala、gradezna dozvola、urbanisticki plan、trafostanica、priklucok）+ 阿尔巴尼亚语（Tetovo/Gostivar/斯科普里混合区：qender te dhenash、dhoma e servereve、leje ndertimi）。
5. **无超规模云区域（负面上下文）**：AWS/Azure/GCP/OCI 官方列表均无 MK 区域；本地云产品多运行于运营商自有设施或外国区域；CDN/边缘（Cloudflare/Akamai/Google Global Cache）只作互联线索。
6. **官方/运营商种子（A=市场存在，容量/状态须另证）**：Interspace（Skopje，Jane Sandanski/Aerodrom、Pero Nakov/Gazi Baba）、Telesmart Telekom（SET/Skopje Exchange Teleroom，Kiro Gligorov 4 或 Nikola Parapunov 地址歧义）、Neotel/neoDC/neoCloud（Skopje Centar Kuzman Josifovski Pitu + Stip）、Net.Bit（Veles）、Data Center DTS（Makedonska Kamenica，CompuNet 工程引用）、政府 BCDR（Prilep 运营）、A1 Makedonija（内部，C）、Makedonski Telekom（电信核心站点，勿全数）、Akton（SKP02/SKP03，目录证据 C）、Telekabel（Stip 电信）、MARNET（学术网，须物理设施证据）。
7. **2026 政策信号**：MIA 报道新法填补法律空白、政府考虑国有数据中心（计划/政策线索，须采购/许可出现后才算项目）；Invest North Macedonia 市场定位页（B=定位、C=设施枚举，除非点名场地）。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§2 / explorer-industry.md §6）

- 许可/规划：`site:gradezna-dozvola.mk "дата центар"`、`site:gradezna-dozvola.mk "{operator}"`、`"{municipality}" "одобрение за градење" "дата центар"`、`filetype:pdf "дата центар" "одобрение за градење"`、`site:{municipality-domain} "урбанистички план" "дата центар"`、`"Совет на Општина {municipality}" "дата центар"`。
- 法律：`"Службен весник" "134" "2026" "дата центар"`、`"Закон за градење" "дата центар"`、`"data centers" "Official Gazette" "North Macedonia" "134"`、`site:mia.mk "data centers" "urban planning"`、`site:seenews.com "North Macedonia" "data centres"`。
- 采购：`site:e-nabavki.gov.mk "дата центар"`、`site:e-nabavki.gov.mk "серверска сала"`、`site:e-nabavki.gov.mk "disaster recovery"`、`site:bjn.gov.mk "дата центар"`、`site:mdt.gov.mk "data center"`、`site:op.europa.eu "North Macedonia" "Data center IT equipment"`。
- 电信/电网：`site:aek.mk "дата центар"`、`site:aek.mk "notified entities" "Neotel" OR "Telesmart" OR "Interspace"`、`site:mepso.com.mk "{municipality}" "трафостаница"`、`site:evn.mk "дата центар"`、`site:erc.org.mk "data center"`、`"{operator}" "EVN" "data center" "North Macedonia"`、`"{project}" "MVA" "Skopje"`。
- 运营商：`site:interspace.com "data center" "Skopje"`、`site:telesmart.mk "colocation" "Skopje"`、`site:neocloud.mk "data center" OR "Stip"`、`site:neodc.mk "Kuzman Josifovski Pitu"`、`site:netbit.mk "datacentar" OR "Veles"`、`site:datacenterdts.com "Makedonska Kamenica"`、`"Akton Communications" "SKP02" OR "SKP03"`。
- 马其顿语全扫：`"дата центар" "Северна Македонија"`、`"центар за податоци" "Македонија"`、`"серверска сала" "Македонија"`、`"колокација" "Скопје"`、`"деловен континуитет" "дата центар"`、`"обнова од катастрофи" "дата центар"`。
- 阿尔巴尼亚语（Tetovo/Gostivar/斯科普里混合区）：`"{municipality}" "qender te dhenash"`、`"dhoma e servereve"`、`"leje ndertimi" "server"`。
- 行业/投资：`site:mia.mk "дата центри"`、`site:seenews.com "North Macedonia" "data centres"`、`site:balkanengineer.com "North Macedonia" "data centers"`、`site:datacenterdynamics.com "Macedonia" "data center" -"Western Macedonia"`、`site:investnorthmacedonia.gov.mk "Data Centers & Digital Infrastructure"`、`"државен дата центар" "Северна Македонија"`。
- 负面核查：`"Skopje" "cloud region" AWS OR Azure OR Google OR Oracle`、`"North Macedonia" "sovereign cloud" "data center"`（均应无官方区域）。

## 官方/监管管线要点（详见 explorer-official.md）

- 许可/规划：e-Odobrenie za gradenje（A，账户制）+ 市政规划（урбанистички план/деталeн урбанистички план、градежна парцела、Совет на Општина 材料）；提取市镇、地籍市镇、地块、地址、投资人/SPV、设施类别（2026 法下数据中心措辞）、面积、机架数、电力需求、变压器/变电站、发电机/燃料、冷却、用水、许可日期、上诉/使用许可、施工阶段词。
- 法律：官方公报 No. 134（2026-06-18）为 A；MIA/SeeNews/BDK Advokati/BalkanEngineer 为 B 线索，不替代公报；2026-06-18 后的新检索受益于“数据中心”成为法定类型。
- 环境/空间：ENER（ener.gov.mk，政府咨询文件 A）、数字化部文档宿主 portal.mdt.gov.mk（A/B）、euprojects.mk（欧盟资助项目 A/B）、IPA 页面（A）；环境证据主要用于大型绿地园区、变电站、发电机/燃料库、工业区与公共部门项目。
- 采购：ESJN/e-nabavki（A）、BJN（A）、MDT 采购页（A）、OP-EU/TED（A/B）；采购可发现公共部门服务器房、政府 DC、设备更新、设计/监理合同；纯设备招标不作物证，除非点名物理数据中心。
- 电信：AEK（aek.mk，A 监管身份/市场报告）+ AEKGISPortal/e-agencija（电子通信基础设施地籍，WEB GIS Collector 提交新建网络及附属设施）；AEK 证明运营商身份/授权/网络光纤上下文，**不单独证明具体设施或容量**。
- 电网：ERC（监管、许可实体、年报，A）、MEPSO（输电网/变电站/十年发展规划/并网项目，A）、EVN/Elektrodistribucija（配网并网路径，A）、能源部（A）、Invest North Macedonia 能源页（B/A-）；提取 MW/MVA、电压等级、变电站/馈线、配网 vs 输网、备用发电、并网日期；区分外购电力/IT load/营销容量；电网证据对 2026 后超大规模/AI 园区线索尤其关键（投资促进可能先于许可/场地宣布）。
- 云：AWS/Azure/GCP/OCI 均无 MK 区域（负面核查）；若日后宣布区域，作 A 级区域信号但仍须运营商/许可/电力证据定物理设施。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 媒体：MIA（B/A-，政府声明）、SeeNews（B）、CORD（B/C）、BalkanEngineer（B/C）、DCD（B，北马覆盖薄、谨防希腊假阳性）、Balkan Green Energy News（B，电网/大负荷可行性）、ITU/Energy Community/EBRD/WB/EU（A/B）、本地 IT.mk/Faktor/Kapital/Meta/Sloboden Pecat/SDK/Plusinfo（B/C）。
- 目录（C/B- 线索）：DataCenterMap（斯科普里与 Deve Bair 旧条目）、Inflect（Skopje：Akton/Interspace/Neotel/Telesmart 地址别名）、Data Center Platform、Cloudscene、Datacenters.com、Data Center Catalog、PeeringDB（B/C，互联活跃设施如 Telesmart DC Skopje）、LinkedIn 招聘（C，Deve Bair/Kriva Palanka 弱线索）。目录容量字段默认低置信，除非运营商/规格页或强技术来源。
- 状态动词：`plans/contemplating/preparing amendments/legal framework/suitable for investment`=政策意图；`tender/design/supervision/building permit/construction started`=管线（用采购/许可核实）；`opened/operational/offers colocation/hosts/built/address`=较强设施信号（用运营商或公共记录核实）。
- 假阳性清单：希腊西马其顿 PPC 300 MW；政策 vs 项目（Invest NM、2026 法律文章）；电信节点/5G/光纤/交换/POP（非数据中心）；纯服务器招标（可作政府/内部 DC 库存，但按范围单列）；目录 MW（Interspace/Telesmart/Neotel 低置信）；“Skopje 1000”邮编不得推断子市镇；云区域缺失=无官方区域。

## 来源分级

- **A** = 官方/一手：e-建筑许可记录、市政规划文件、官方公报法律文本、部委/政府/EU 项目记录、AEK/AEC 运营商记录、ERC/MEPSO/EVN 电力源、公共采购通知、官方云区域页、运营商自有设施页。
- **B** = 强二级：MIA/SeeNews/CORD/BalkanEngineer 报告、Energy Community/EBRD/WB/ITU 档案、Uptime/PeeringDB/互联记录、可识别地点的厂商案例。
- **C** = 弱线索：聚合目录、社交帖子、招聘广告、市场笔记、投资促进页（未点名设施）、未验证的街道/市镇归派。
- 状态判定：运营商页/许可/规划记录/采购项目记录/AEK 记录/电网记录中至少一条一手源才给 A 级状态；目录证据须核验后才计。
- 去重/归派：斯科普里子市镇须街道/地籍/市政许可/可靠地图证据（Aerodrom/Gazi Baba/Centar/Karpos），不得仅凭“Skopje”；地址变体先调和再归市镇；运营商品牌/法人（Interspace=Интерспејс、Neotel=Неотел、Net.Bit=Нет.Бит）双语记录合并。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=MK，divisions=80 市镇）。
2. 建种子：运营商官方页（Interspace/Telesmart/Neotel-neoDC-neoCloud/Net.Bit/DTS/A1/Telekom/Akton/Telekabel）+ 已知地址（Pero Nakov、Jane Sandanski、Kiro Gligorov、Nikola Parapunov、Kuzman Josifovski Pitu、Nikola Orovcanec、Vasko Karangeleski）+ 政府 BCDR Prilep EU 项目记录。
3. 每个市镇执行统一流程：英/马其顿语词（data center、дата центар、центар за податоци、серверска сала、колокација、облак/клауд、деловен континуитет、обнова од катастрофи）→ 官方域过一遍（gradezna-dozvola.mk、市政站、e-nabavki、bjn、aek、erc、mepso、evn、mdt、portal.mdt、ener、euprojects）→ 运营商名+市镇/街道 → 电网/变电站词。
4. 优先级：斯科普里（Aerodrom/Gazi Baba/Centar/Karpos）→ Veles/Stip/Makedonska Kamenica/Prilep → 主要区域城市/工业市镇 → 其余低概率市镇（一次官方+一次运营商/目录即可，多数为 e-政务/GIS/服务器招标，查全清单后写 `no_projects: true`）。
5. 状态：opened/operational/UD/运营商页活跃=运营；tender/permit/construction started/PG=在建或已许可；plans/policy/投资促进=线索不计数。
6. 输出 world 同 schema；容量字段仅在有来源时填写并标注低置信；每条 A/B 记录附 `why_this_is_a_data_center` 与 `what_is_not_confirmed`。
7. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：codex terra agent（max thinking）每 agent 分批复核北马其顿数据中心（80 市镇粒度）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：官方公报 No. 134 全文与数据中心的法定定义；Interspace/Telesmart/Neotel 各斯科普里地址的市镇归派与许可；Data Center DTS 在 Makedonska Kamenica 的许可/电网连接；政府 BCDR Prilep 的运营状态与二期；政府“国有数据中心”是否进入采购/许可阶段。
