---
name: la-datacenter-methodology
location: scripts/expansion/world/country-skills/LA/SKILL.md
description: |
  Laos (LA) datacenter discovery & audit methodology — how to enumerate, verify, and update Lao PDR datacenter projects across the 17 manifest provinces plus Vientiane Capital (added manually — nearly all confirmed datacenter/cloud evidence is there). Laos has no public facility-level registry or construction-permit database: enumeration joins MTC/LANIC (regulator, National Data Center unit, government hosting), KPL state news (official announcements/MoUs), Lao Trade Portal laws (Telecom Law 05/NA, Data Protection 25/NA, MTC Decision 3583/MoTC), InvestLaos/MPI/SEZ pages (Savan-Seno, Boten, Golden Triangle, Pakse-Japan, Thakhaek …), EDL/EDL-Gen utility evidence, operator pages (LaoDC, Unitel Cloud, GDMS, Lao Telecom, ETL), the 2016 government eco datacenter precedent (IIJ/Toyota/JCM), hyperscaler region absence checks (no AWS/Azure/GCP/OCI/Alibaba/Tencent/Huawei region), and tri-lingual search (English/Lao/Chinese). Read this before running LA exploration/audit batches. Routes to explorer-official.md (MTC/KPL/law/SEZ/utility/division pipeline) and explorer-industry.md (operator seeds/trade press/project tracker).
---

# LA · 老挝数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：老挝**没有**设施级数据中心注册表、没有公开全国施工许可库；普查靠拼接 MTC/LANIC（监管与政府托管）、KPL 国家通讯社（官方公告）、Lao Trade Portal 法律页、InvestLaos/SEZ 投资页、EDL/EDL-Gen 电力证据、运营者官方页与可信贸易媒体。
> 已确认的设施/云证据几乎全部集中在**万象首都（Vientiane Capital）**：政府节能数据中心（2016）、GDMS 国家云/国家数据中心、Unitel Cloud、LaoDC、LANIC 政府托管；17 个 manifest 省大多应返回**无确认 DC**——把缺席显式记录下来，不要发明省级行。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供老挝探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：MTC/MPT/MOST/LANIC、KPL、Lao Trade Portal 法律（电信法 05/NA、数据保护 25/NA、MTC 决定 3583）、MPI/IPMC/InvestLaos/SEZ（Savan-Seno/Boten/金三角/Pakse-Japan/Thakhaek/VITA/Saysettha 等）、EDL/EDL-Gen、17 省矩阵 + Vientiane Capital 额外单元、分级规则 |
| `explorer-industry.md` | 行业/厂商发现：运营者种子（MTC/LaoDC/Unitel Cloud/GDMS/Lao Telecom/ETL/T-Plus/Best Telecom/Planet Online）、超大规模缺席核验、贸易媒体/聚合器（KPL/Vientiane Times/Xinhua/DataCenterMap）、项目追踪种子行、SEZ 行业扫描、归一化与去重规则 |

## 核心结构事实（框定每次搜索）

1. **行政区**：老挝 17 省 + 万象首都/万象直辖；manifest 只覆盖 17 省（Attapu, Bokeo, Bolikhamxai, Champasak, Houaphan, Khammouan, Louang Namtha, Louangphabang, Oudomxai, Phongsali, Salavan, Savannakhet, Viangchan, Xaignabouli, Xekong, Xiangkhouang, Xaisomboun）——**必须手动加 Vientiane Capital**，因为几乎每条已确认线索都在那里；Viangchan（万象省）与万象首都严格分开。
2. **监管者 MTC**（https://mtc.gov.la/，页脚仍写 MPT；历史别名 MPT/MOST 按时间归一化）：MTC/LANIC（lanic.gov.la）提供 `.la` 域名、服务器租用/托管、ICT 服务许可/设备进口、数字经济战略出版物——是政府托管与 ICT 监管的一手源。
3. **MTC 下辖国家数据中心单元**：KPL 确认 2025-05-30 与 Silicon Tech Park (Lao) 签署 MoU，研究绿色电力 AI 基础设施与万象首都区 >150 ha 的 AI 经济特区（A 级事件，**仅 pipeline**）；Vientiane Times 报道 MTC/Phounphonnakhone（LA Group/Phongsavanh Group 旗下 IT 公司）的国家数据中心+政府数据交换系统可行性研究（B 级）。
4. **政府数据中心先例**：Lao PDR Energy Efficient Datacenter Project——IIJ 称老挝首个政府运营生态数据中心于 2016-11-29 在万象完工，Toyota Tsusho/JCM 确认其为首个老日 JCM 项目、模块化数据中心技术（A 级完成证据；当前运营角色需复查）。
5. **市场极小**：确认的公共设施/云服务证据都在万象首都；省级线索多为 SEZ 机会或电信覆盖；**行类型必须分开**：运营设施 vs 运营者云/托管服务 vs 政府数据中心 vs MoU/可行性研究 vs SEZ 机会 vs 电信/机房线索 vs 加密/诈骗计算线索。
6. **超大规模缺席**：AWS/Azure/GCP/OCI/Alibaba/Tencent/Huawei 均无老挝公共云区域（官方区域页季度核验）；最近区域为泰国/新加坡/马来西亚/香港/中国；转售/合作云/CDN 边缘 ≠ 物理区域。
7. **语言三轨**：英语用于国家媒体/运营者/投资者；老挝语用于部委/省页（ສູນຂໍ້ມູນ 数据中心、ສູນດາຕ້າ、ເຊົ່າ Server、ບໍລິການ Hosting）；中文用于中国关联 SEZ/铁路走廊线索（老挝 数据中心、万象 数据中心、磨丁、金三角经济特区）。
8. **非标准计算排除**：博彩/诈骗园区、加密矿场、铁塔托管、普通企业机房不进入运营 DC 计数（除非单独建 `non_standard_compute`/`telecom_internal` 行）。
9. **容量极少公开**：MW/机架/Tier/面积/冗余很少披露——空着或 n/a，不要从“便宜水电”营销声称推断容量。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§2 / explorer-industry.md §2-§3）

- 官方：`site:mtc.gov.la "data center" OR "ສູນຂໍ້ມູນ"`、`site:mtc.gov.la "ເຊົ່າ Server" OR "Hosting"`、`site:lanic.gov.la "server" OR "hosting" OR "data center"`、`site:kpl.gov.la/En "National Data Center" "Ministry of Technology and Communications"`、`site:kpl.gov.la/En "AI Special Economic Zone" "Vientiane"`、`site:vientianetimes.org.la "National Data Centre" Laos`、`site:investlaos.gov.la "data center" OR "Special Economic Zone"`、`site:laotradeportal.gov.la "Law on Telecommunication" "05/NA"`、`site:edl.com.la OR site:edlgen.com.la "data center" OR "server" OR "cloud"`。
- 老挝语：`"ສູນຂໍ້ມູນແຫ່ງຊາດ" Vientiane`、`"{province}" "ສູນຂໍ້ມູນ"`、`"ຄລາວ" OR "ບໍລິການ Hosting"`。
- 中文：`老挝 数据中心 万象`、`老挝 国家数据中心`、`老挝 人工智能 数据中心`、`磨丁 数据中心`、`金三角经济特区 数据中心`。
- 运营者：`"LaoDC" "Vientiane" colocation`、`"Unitel Cloud" "Nongbone" "Saysettha"`、`"GDMS" "National Cloud" Laos`、`"Silicon Tech Park" Laos "AI" "data center"`、`"Phounphonnakhone" "National Data Centre"`、`"Lao PDR Energy Efficient Datacenter Project"`、`"IIJ" "Lao PDR" "datacenter" Vientiane`。
- 省级：`"{Province}" Laos "data center" OR "cloud" OR "IDC"` + 老挝语对应 + 边境省中文；SEZ 关键 `"Savan-Seno" "data center"`、`"Boten" "data center"`、`"Golden Triangle" "data center"`。
- 贸易/聚合：`site:english.news.cn Laos "national data center"`、`site:laotiantimes.com Laos "data center"`、`site:datacentermap.com/laos/`、`site:developingtelecoms.com Laos data center`。

## 官方/监管管线要点（详见 explorer-official.md）

- **MTC/LANIC（A）**：监管者身份、政府托管服务、国家数据中心单元引用、ICT 服务许可/进口流程、国家数字战略；注意 MTC 页不是设施注册表——策略/服务页不得转成 DC 行，除非指名设施/项目/地点/运营者。
- **KPL（A 事件级）**：确认 MoU/部长级活动的存在、具名政府单元、具名对手方、日期、官方政策声明；MoU/可行性 = pipeline only。
- **Lao Trade Portal（A 法律语境）**：电信法（修订）05/NA、电子数据保护法 25/NA、电信和 ICT 设备管理决定 3583/MoTC、旧 MPT 3201 决定；法律页 ≠ 设施证据。
- **MPI/IPMC/InvestLaos/SEZ（A 区级）**：Savan-Seno（Savannakhet，2003 建区，954 ha，政府开发商，东西经济走廊）、Boten Beautiful Land（Louang Namtha，1640 ha，中国私企开发商，含邮政电信项目类）、Golden Triangle（Bokeo，含邮政/电信/互联网项目类）、VITA Park/Saysettha/Thatluang Lake/Long-Thanh/Dongphosy（首都）、Luangprabang/Thakhaek/Phoukhyo/Champasak（含 Pakse-Japan）；SEZ 页证明潜力，不证明 DC 租户——DC 行需具名租户/项目。
- **电力（A 实用工具）**：EDL/EDL-Gen 公告、SEZ 公用事业分配、电网/变电站工程、土地/许可证据、运营者建设声明五选一才把设施升到企业机房规模以上。
- **云缺席（A）**：七家云厂商官方区域页季度核验；记录 `no_public_region_found` + 最近区域 + 检查日期。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **运营者种子**：GDMS（global-dms.com，主权云/国家数据中心，自称与 MTC 有 10 年战略合作、运营/增强一个国家数据中心并跨两个中心扩展国家云，B+——主源是厂商非部委）；Unitel Cloud（ucloudserver.unitel.com.la，Nongbone Road, Phonxay Village, Saysettha District，万象首都，服务/地址 A、设施规格 C）；LaoDC（laodc.com，自称自有万象首都数据中心，冗余光纤/电力、柴油发电机、光伏；2018 Hatxaykhao 奠基为老挝首个持牌私企 DC——B 级运营者主张，认证/客户待核）；Lao Telecom/ETL/T-Plus（电信内部，C）；Best Telecom（OCK 15 年铁塔租约，连接性非 DC，B 塔交易）；Planet Online（C）。
- **项目追踪种子行**：2016 政府生态 DC（A 完成）、国家云/国家数据中心（B+）、Unitel Cloud（A 服务/C 规格）、LaoDC（A/B）、Silicon Tech Park AI MoU（A 事件）、Phounphonnakhone 可行性（B）、LANIC 托管（A 服务/C 设施）、SEZ 机会行（A 区、无 DC 行）。
- **贸易媒体（B/C）**：KPL（A）、Vientiane Times（B，官方-相邻）、Xinhua 镜像（B，中国向）、Laotian Times/Open Development（B/C）、W.Media/DCD/Capacity/Telecom Review/Developing Telecoms（B/C）、越南媒体（Unitel/Viettel，B）、中文源（B/C）、Facebook（C 除非官方页+文档图+日期+当事方）。
- **归一化**：Vientiane Capital ≠ Viangchan 省；MTC/MPT/MOST 按时点；National Data Center/NDC/ສູນຂໍ້ມູນແຫ່ງຊາດ 归一为 MTC 实体；省名拼写变体表（Louang Namtha/Luang Namtha、Louangphabang/Luang Prabang、Khammouan/Khammouane、Xaignabouli/Xayabury 等）；“LEED Datacenter”在老挝语境可能是节能项目译名而非 USGBC 认证——保留原文措辞。
- **发布规则**：仅当官方/运营者/公用事业/SEZ 源指名地点与 DC/托管/云功能时才发确认设施；MoU/可行性发 `planned`/`feasibility` 并带日期与当事方，绝不记运营 MW/机架；仅目录证据建 `lead` 行。

## 来源分级

- **A** = 一手/法定可问责：MTC/MPT/LANIC 页面、KPL 国家通讯社、Lao Trade Portal 法律/决定页、InvestLaos/MPI/IPMC/SEZ 页面、省级政府/DPI/SEZA 公告、EDL/EDL-Gen 公用事业证据、运营者官方页、云厂商官方区域页（缺席）。
- **B** = 强二级：Vientiane Times、Xinhua、VietnamPlus、Laotian Times、可信律所/监管摘要、上市公司申报、成熟电信/DC 贸易媒体（W.Media/DCD/Capacity/Telecom Review/Developing Telecoms）。
- **C** = 弱线索：DataCenterMap、通用目录、SEO/厂商博客、市场报告片段、社交帖、无佐证的老挝语转贴；仅发现用。
- **状态语义**：MoU/可行性 = pipeline（绝不运营）；SEZ 机会 ≠ 设施；电信内部/加密矿场/诈骗园区/企业机房排除在核心 DC 计数外；GDMS 国家云行不得与 2016 IIJ/Toyota 政府 DC 行重复（除非源显式连接）。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=LA，divisions=17 省；手动追加 Vientiane Capital 为额外高优单元）。
2. 种子：运营者官方页（LaoDC/Unitel Cloud/GDMS/LANIC/Lao Telecom/ETL/T-Plus）+ MTC/KPL + InvestLaos SEZ + 贸易媒体首扫。
3. 万象首都深扫：MTC/LANIC、KPL、Vientiane Times、Unitel Cloud、LaoDC、GDMS、2016 政府生态 DC、首都 SEZ（VITA/Saysettha/Thatluang Lake/Long-Thanh/Dongphosy）、Nongbone Road、Hatxaykhao。
4. 17 省逐一扫描：官方路线（省 DPI/SEZA + MTC/EDL）+ SEZ 关键 + 英/老/中三语模板；无确认 DC 就显式记录 `no confirmed DC found in public sources`。
5. 官方证据链：MTC/LANIC 或 KPL → InvestLaos/MPI/SEZ → 省 DPI/SEZA → EDL/EDL-Gen → 运营者页 → 贸易媒体；只有主张事实的证据为一手时才升 A。
6. 去重/归一：首都与 Viangchan 省分开；部委名按时点；国家数据中心实体归一；省名变体归一；行类型分离（运营/云服务/政府/MoU/SEZ/电信/非标准）。
7. 输出与 world 探索同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；无容量留空/n/a；无项目省写 `no_projects: true`。
8. 遵守 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：批量复核老挝数据中心（17 省 + 万象首都）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Silicon Tech Park AI MoU/Phounphonnakhone 可行性后续、2016 政府生态 DC 当前运营角色与是否即 GDMS 所指国家数据中心之一、LaoDC 当前牌照/认证/客户、Unitel Cloud 物理设施规格、MTC/LANIC 是否有公开 ICT/托管/DC 牌照清单、SEZ 是否出现具名 DC 租户。
