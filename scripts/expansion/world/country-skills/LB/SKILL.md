---
name: lb-datacenter-methodology
location: scripts/expansion/world/country-skills/LB/SKILL.md
description: |
  Lebanon data-center discovery routes TRA/MoT/Ogero regulation, PPA/OMSAR e-procurement, World Bank LDAP P506791, EDL power, Uptime certifications, and cloud-region checks into operator/company evidence (Byblos Bank DC, LFAIT, TerraNet, Ogero/Alfa/Touch) across eight governorates with Arabic/French/English vocabulary and conflict/outage status gating outside Beirut/Mount Lebanon.
---

# LB · 黎巴嫩数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为黎巴嫩数据中心/托管设施发现与审计提供可持续、可复现的查询方法论。
> 分区模型：8 个省（governorates）：Akkar；North Lebanon；Beirut；Baalbek-Hermel；Beqaa；South Lebanon；Mount Lebanon；Nabatieh。
> 已知种子：Byblos Bank / Byblos Tower B1 Data Center（Uptime Tier III）、LFAIT Medyar/Ras Beirut、TerraNet NOC 共置、Ogero 机构托管、World Bank LDAP 政府云/数据中心投资（计划）。
> 本 skill 汇总两份探索报告：官方/监管管线（explorer-official.md）与行业/厂商发现（explorer-industry.md），字段级 A/B/C/U 分级。

## 入口

| 文件 | 管线 |
|---|---|
| explorer-official.md | 官方/监管管线：TRA、MoT、Ogero/Alfa/Touch、PPA/OMSAR e-procurement、EDL/CDR/IDAL、World Bank P506791、Uptime、云区域/Cloudflare、NNA |
| explorer-industry.md | 行业/厂商发现：Byblos/LFAIT/TerraNet 运营商页、DCD/Telecom Review/Executive/ITP/Developing Telecoms/Arab News、IXP/海缆/CDN、目录聚合器与本地危机媒体 |

## 核心结构事实（框定每次搜索）

1. 行政覆盖固定为 **8 个省**；Beirut 既是省又是市，许多 ICT 来源说「Beirut」实指 Greater Beirut（跨入 Mount Lebanon 郊区）——先记市/站点再映射省，不得仅凭「Beirut」措辞强行归省。
2. **无公共国家数据中心登记册**；Ministry of Economy and Trade / Commercial Register 仅识别公司（身份证据）；1959 政体确立国家电信垄断，Law 431/2002 引入自由化但固网/移动实际仍国家控制；Ogero 为固网国有运营臂，Alfa/Touch 为代国家/MoT 运营的移动品牌。
3. **TRA 于 2025 年重启**（2025-09 任命、2025-12-15 获总统接见，此前休眠 13 年；MoT 2025-10-06 宣布）；截至本轮未见 TRA 数据中心/云牌照登记——年度通过前复查 TRA 新闻。数据保护 Law No. 81 of 2018 由 OMSAR 托管；无国家数据保护机构（合规语境，非 DC 认证）。
4. 采购路线活跃：**PPA**（tenders 页含八省过滤器）与 **OMSAR e-procurement**（Delta 驱动）；数据中心/服务器/云招标在点名中标/站点前仅作管线证据。**World Bank Lebanon Digital Acceleration Project P506791**（2026-01-26 批准；2026-04-28 ISR：Component 1 Digital Foundations USD 87.5m、政府社区云/数据中心 PUE/数据中心投资带动 USD 11m 私人资本指标）——计划信号，非运营设施。
5. **电力是门槛约束**：EDL 为电网（站点本轮超时）；官方/贸易报道记录影响 Ogero/ISP 的长期缺电/燃料中断；设施记录需明确电力证据，不得推断 MW/冗余。
6. **危机/冲突状态门槛**：Akkar、North Lebanon、Beqaa、Baalbek-Hermel、South Lebanon、Nabatieh 在断言运营状态前必须先查电信恢复/中断状态；禁止静默保留危机前运营状态。
7. 云区域（2026-08-12）：AWS/GCP/Azure/OCI 官方清单**均无黎巴嫩公共区域**；Cloudflare 2021 新闻列 Beirut 为中东网络城市——CDN/边缘 POP，非区域也非独立 DC 记录。
8. 验收阈值：运营设施=运营商/政府启用声明、官方设施页、Uptime 认证+业主/贸易佐证、或点名现有数据中心的官方/采购/世行文本；招标/计划=PPA/OMSAR/MoT/世行文档点名数据中心/云/政府托管/数据中心投资（无站点则保持管线）；拒绝=泛泛 FTTH、ISP 牌照、网络覆盖、海缆登陆、铁塔、ASN、IXP、CDN POP、学术算力、无设施证据的政策愿景。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§4 / explorer-industry.md §1-§4）

- 官方站点：`site:tra.gov.lb "data center" OR "مركز بيانات" OR "السحابة"`；`site:mpt.gov.lb "مركز بيانات" OR "استضافة"`；`site:ogero.gov.lb "data" OR "استضافة"`；`site:ppa.gov.lb "data center" OR "خوادم" OR "cloud"`；`site:omsar.eprocurement.gov.lb "data center" OR "خوادم"`；`site:nna-leb.gov.lb "مركز بيانات" OR "أوجيرو" OR "انقطاع"`；`site:worldbank.org P506791 Lebanon "data center" OR "government community cloud"`
- 阿/英/法生命周期词：`"لبنان" "مركز بيانات"`；`"مركز بيانات" "بيروت" OR "جبل لبنان"`；`"الحوسبة السحابية" "لبنان" "حكومة"`；`"مناقصة" "مركز بيانات" لبنان`；`"Lebanon" "national data center" OR "government cloud"`
- 运营商：`site:lfait.com "Medyar DC" OR "Datacenter" OR "Lebanon/Medyar"`；`site:terra.net.lb "Co-location" OR "Network Operations Center"`；`site:byblosbank.com "data center" OR "Tier III"`；`"Byblos Bank" "Byblos Tower B1" "Uptime"`；`site:alfa.com.lb "مركز بيانات" OR "cloud"`；`site:touch.com.lb "مركز بيانات" OR "استضافة"`
- 媒体/危机：`site:datacenterdynamics.com Lebanon "data center" OR Ogero`；`site:developingtelecoms.com Lebanon Ogero OR outage`；`"Ogero" "data center" OR "cloud" OR "استضافة"`；`site:telecomreview.com Lebanon "data center" OR cloud`
- 云缺席：`"Lebanon" "cloud region" OR "availability zone"`；`site:cloudflare.com Beirut Lebanon network data center`
- 省级清扫：`"{division}" "data center" Lebanon`；`"{Arabic governorate}" "مركز بيانات" OR "خوادم" OR "استضافة"`；`"{division}" "cable landing" OR "landing station"`
- 状态词：`("افتتاح" OR "إطلاق" OR "تدشين") "مركز بيانات" لبنان`；`("انقطاع" OR "تضرر" OR "توقف") "أوجيرو"`；`("مناقصة" OR "عطاء" OR "استدراج عروض") "خوادم" لبنان`

## 官方/监管管线要点（详见 explorer-official.md）

- TRA 声明仅为法律/监管语境，除非点名数据中心/云设施、牌照、业主或站点；MoT ISP/DSP 名单是持牌运营商宇宙证据，非设施证据。
- Ogero 为身份/骨干 A 级；本轮未发现公开 Ogero 商业共置/数据中心规格页；Alfa/Touch 移动核心站点为机构电信基础设施。
- PPA tenders 页含 Beirut/North Lebanon/Mount Lebanon/South Lebanon/Bekaa/Nabatiyeh/Baalbek Hermel/Akaar 过滤器；BDL 通过 PPA 发布招标通知；采购/项目指标（government community cloud、data center investments）在识别合同/站点/运营商/运营启用前为计划/管线。
- EDL 站点超时（每轮验证）；CDR 返回 Cloudflare 挑战/403；IDAL 返回 525；`public-works.gov.lb` 无法解析——无中央在线建筑许可登记，许可研究仅在候选站点已知后有用。
- Uptime 黎巴嫩国家页 + Byblos Tower B1 条目（客户 Byblos Bank s.a.l.）为 A 级认证证据；银行新闻室给出 2019-06-24 启运与位置语境。
- 边界规则：来源只说「Beirut」而地址是 Sinn El Fil/Forn El Chebbak/Jnah/Chouf/Medyar 等郊区时，不得强行归入 Beirut 省；按实际市/区映射。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场小型且无超大规模园区：证据指向银行私有设施、小型 ISP/托管/NOC 共置、Ogero/政府机构托管、移动核心、IXP、海缆登陆与 CDN/边缘 POP。
- **Byblos Bank / Byblos Tower B1**（Beirut/Ashrafieh）：2019-06-24 启运 + Uptime Tier III constructed（A）；银行私有设施，非公共共置。
- **LFAIT**（Shouf/Medyar, Mount Lebanon + Ras Beirut）：运营商门户广告黎巴嫩服务器/跨多数据中心 VMware 集群；公告引用「Lebanon/Medyar DC」（A 级运营商文本）；目录 MW/sqm/Tier/PCI/ISO/SAS70 值 C 级，不得复制入最终记录。
- **TerraNet NOC 共置**：官方产品页列 UPS/自动发电机/温控/安全访问（A 级服务声称）；无公开地址/规格，设施几何低置信。
- **Ogero**：骨干/国际网关/政府企业连接核心；无公开商业 DC 规格页——「Ogero data center」声称 U 级直到有设施点名来源。
- 网络层不是 DC 证据：Beirut-IX、LEB-IX、OpenIX Beirut、Cloudflare Beirut、IMEWE Tripoli、CADMOS-2/Berytar 登陆点（连接锚点/线索）。
- 目录假阳性降级/拒绝：美国叫 Lebanon 的地方（尤其 Meta 2026 Indiana DC）、无运营商支持的 Cloudscene/Inflect/DataCenterMap 计数、Berytech/BDD 办公/孵化器条目、任何 C 级镜像的「15 MW」容量声称。
- 危机语境门控：Beirut/Mount Lebanon 之外任何危机前设施需当前状态检查；偏好 NNA/运营商来源。

## 已知设施/项目与证据状态

| 设施/项目 | 分区 | 状态与证据 |
|---|---|---|
| Byblos Bank Data Center / Byblos Tower B1 | Beirut（Ashrafieh） | 运营中（2019 起）；银行新闻室 A + Uptime Tier III constructed A；私有银行设施非共置；容量 null |
| LFAIT Medyar | Mount Lebanon（Shouf） | 运营线索；运营商 A（Medyar DC 引用）+ 目录 C 规格 |
| LFAIT Ras Beirut | Beirut（Kraitem/Ras Beirut） | 运营线索（C/A）；运营商页无专用 Ras Beirut 设施页 |
| TerraNet NOC 共置 | 未验证（可能 Greater Beirut） | 运营服务声称（A）；地址/规格缺失 |
| Ogero 机构/骨干托管 | 全国 | 运营商角色 A；DC 规格 U；无商业 DC 页 |
| Lebanon Digital Acceleration Project 政府云/DC 投资 | 全国（计划） | World Bank ISR A 级计划/管线；无公开站点/运营商 |
| 政府 e-services/Dawlati/部委系统 | Beirut 语境 | 程序身份 A；设施 U |
| Beirut-IX / LEB-IX / OpenIX Beirut | Beirut | 网络设施/IXP（B/C），非 DC |
| Cloudflare Beirut | Beirut | CDN/边缘 POP（A 网络城市），非区域/独立 DC |
| IMEWE Tripoli 登陆；CADMOS-2/Berytar | North Lebanon/South | 海缆基础设施（B/C），非 DC |
| 其余省（Akkar/North Lebanon/Beqaa/Baalbek-Hermel/South Lebanon/Nabatieh） | 各省 | 无核验 DC；危机/恢复状态检查优先 |

## 更新节奏

- 季度（2026-2027）：World Bank P506791、OMSAR、MoT 政策实施、PPA/e-procurement 招标、TRA 重启后新闻；Ogero 新闻/投标、NNA 电信、DCD/Developing Telecoms/Telecom Review/L'Orient/Arab News。
- 任何非 Beirut 枚举前：Akkar/North Lebanon/Beqaa/Baalbek-Hermel/South Lebanon/Nabatieh 的中断/恢复状态。
- 半年：Uptime 黎巴嫩国家页；DataCenterMap/Cloudscene/Inflect C 级线索；SubmarineCableMap/GeoCables 登陆变化；AWS/GCP/Azure/OCI 区域清单；Cloudflare 网络图/新闻。
- 年度：Law 81/DLA Piper 实施状态；IDAL/CDR/EDL 可达性；银行年报官方 DC 提及。
- 待办（2026-08-12）：LFAIT 设施规格运营商确认；TerraNet 地址；Ogero 设施点名公告；World Bank P506791 合同/站点；TRA 数据中心/云牌照登记；codex terra agent 分批复核后按本方法论推进。
