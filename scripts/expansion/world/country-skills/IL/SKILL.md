---
name: il-datacenter-methodology
location: scripts/expansion/world/country-skills/IL/SKILL.md
description: |
  Israel (IL) datacenter discovery & audit methodology. No facility registry; enumeration is a Hebrew-first statutory-plan (Mavat/מידע תכנוני, XPlan) and local-committee exercise joined with electricity gating sources (Electricity Authority decisions incl. 74506 suspension for 8 MVA+ connections and 50 MVA+ transmission hearing, IEC connection-probability map, Noga ISO), Ministry of Communications licenses, TASE/MAYA filings, cloud regions (AWS il-central-1, Google me-west1, Azure Israel Central, Oracle Israel/Bynet Jerusalem underground), and operator pages (MedOne, Bynet, Serverfarm ISR1, Digital Realty Mivne, Mega DC/Mega Or, GTR, NED, Keystone). Division model: 6 districts (HaDarom, Hefa, Yerushalayim, HaMerkaz, Tel Aviv, HaTsafon). Read this before running IL exploration/audit batches. Routes to explorer-official.md (planning/energy/cloud/operator) and explorer-industry.md (press/vendor/district tactics).
---
# IL · 以色列数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为以色列数据中心枚举提供「希伯来语优先的法定规划 + 电力门槛 + 云区域 + 运营商官网 + 证券备案」五线并联的查询框架。以色列通过规划管理局有可用的全国规划主干，但枚举仍是**希伯来语优先的法定规划（statutory plan）与地方委员会作业**：先用国家系统找规划与文件，再转入相关区/地方规划委员会、市政府、工业园区公司与运营商。**电力是门槛性官方源**：2026 年电力局发布临时决定，**暂停 8 MVA 及以上**数据中心连接项目的审查/响应程序，并另开 50 MVA 及以上输电并网消费者标准听证——大型项目的电力状态（secured/requested/suspended/speculative）必须显式记录。云区域只证明区域存在与都会级需求（AWS/Google/Azure/Oracle 均有以色列信号但不公布精确 AZ/建筑）。本 skill 汇总两份探索报告（官方管线 + 行业发现），供以色列探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：Mavat/XPlan/Planning Administration、电力局决定与听证（74506、50 MVA）、IEC/Noga、通信部许可、TASE/MAYA 备案、云区域页、运营商官网 |
| `explorer-industry.md` | 行业/厂商发现：Globes/Calcalist/DCD/Times of Israel 等媒体、运营商/开发商矩阵、希伯来/英语词汇表、逐区枚举战术、已知线索宇宙 |

## 核心结构事实（框定每次搜索）

1. **希伯来语优先 + Mavat 法定记录**：主要公共规划系统是 **Mavat / 规划信息（מידע תכנוני）** 与 **XPlan / 蓝线图（קווים כחולים）**。Mavat（https://mavat.iplan.gov.il/）是规划、申请、上诉、委员会议程、协议与决定的法定记录；XPlan（https://ags.iplan.gov.il/xplan/）是 2011 年起在线提交规划的制图助手，法定/现行数据须回 Mavat 校验。大型项目可能走国家基础设施处理：**政府决定 3907（2026）**（קידום הקמת חוות שרתים מתקדמות לחיזוק ההובלה של ישראל בתחום הבינה המלאכותית，https://www.gov.il/he/pages/dec3907-2026）把先进数据中心框定为战略 AI 基础设施，并参照输电并网时限与候选区域映射。
2. **电力是门槛性官方源（2026 关键）**：电力局决定与听证中心 https://www.gov.il/he/departments/topics/decisions-and-hearings；**决定 74506**（8 MVA+ 数据中心连接临时暂停，https://www.gov.il/he/pages/74506）；**50 MVA+ 输电并网消费者标准听证** https://www.gov.il/he/pages/shimam50hibur（附件 `skira_shim_50.pdf` 含 `תשתיות מחשוב על` 表述）；财政部/能源部临时建议新闻稿（2026-02-19，https://www.gov.il/he/pages/press_190226）：优先以色列中部以外数据中心、缩短优选区规划、防止投机性电网预留。IEC 连接概率图 https://www.iec.co.il/content/renewableenergy/contentpages/probabilitymap；Noga ISO https://www.noga-iso.co.il/。**任何 2026+ 项目公告在出现 secured power/Noga-IEC 连接/自发电/变电站证据前，不算完全验证**（Calcalist 2026-07：Noga 收到大量新申请后电力局冻结 8MW+ 新并网请求 140 天）。
3. **希伯来语核心词**：חוות שרתים（服务器农场=数据中心常用词）、מרכז נתונים、דאטה סנטר、מתקן מחשוב על（先进计算基础设施）、חדרי שרתים（机房）、תשתיות מחשוב（计算基础设施）、תב"ע（法定规划）、תכנית בניין עיר、היתר בנייה（建筑许可）、בקשה להיתר（许可申请）、ועדה מקומית（地方委员会）、ועדה מחוזית（区委员会）、שינוי ייעוד（改用途）、אזור תעשייה（工业区）、תחנת משנה（变电站）、חיבור חשמל/חיבור לרשת（并网）、נגה（Noga）、חברת החשמל（IEC）、רשות החשמל（电力局）、מגה-וואט/MVA、ממוגן（加固）、תת קרקעי（地下）、שרידות（韧性/冗余）。状态词：החלה בנייה（开工）、אבן פינה（奠基）、נחנך（落成）、הושק/נפתח（启动/开放）、יוקם（将建）、מתוכנן（规划中）、בקשה（申请）、הקפאה（冻结）。**只有 `היתר בנייה`、开工、运营商调试或更强才计为施工证据**；宣布拿地/规划申报/电网请求/云区域语言按 planned/lead 处理。
4. **希伯来语+英语双语**：规划/电网/市政/交易所文件用希伯来语优先；超大规模、国际运营商与贸易媒体用英语。希伯来源常称数据中心为「服务器农场」（חוות שרתים），普通 `data center` 搜索会漏；地下/加固设施常见：`underground`/`fortified`/`bunker`/`ממוגן`/`תת קרקעי`/`שרידות` 能找到一般搜索漏掉的以色列 DC 报道。
5. **云区域 = 逻辑区域，非物理设施**：AWS Israel (Tel Aviv) Region `il-central-1` 3 AZ（https://aws.amazon.com/local/israel/ + https://aws.amazon.com/blogs/aws/now-open-aws-israel-tel-aviv-region/）；Google Cloud Tel Aviv `me-west1`（zones a/b/c）；Azure `Israel Central`/`israelcentral`（2020 宣布首个以色列云数据中心区域）；Oracle Israel 区域 https://www.oracle.com/il-en/cloud/cloud-regions/israel/（媒体报道经 Bynet 的地下耶路撒冷设施，设施级为 B）；Project Nimbus（政府云采购，AWS+Google，https://www.gov.il/en/pages/press_01082023_b）作需求/租户语境。精确站点须规划/能源/运营商/备案确认，不从目录复制 AZ 地点。
6. **证券备案与边界注意**：TASE/MAYA https://maya.tase.co.il/ + https://mayafiles.tase.co.il/（搜 חוות שרתים/Data Center/Digital Realty Mivne/מגה אור/מבנה/לוינשטיין/נבידיה/Nebius；例 Digital Realty/Mivne JV PDF P1456371-00）；上市实体：Mivne、Mega Or、Levinstein、Dalia、Electra、Shikun & Binui、Azrieli。**边界注意**：市场材料常把 Central（Herzliya、Petah Tikva、Bnei Zion、Beit Shemesh）宣传为「Tel Aviv」；每个设施按市镇/坐标映射到 repo 区，不按营销都会区。

## 查询模式（复制粘贴模板见 explorer-official.md §1 与 explorer-industry.md §3-4）

- `site:mavat.iplan.gov.il "חוות שרתים"` / `site:iplan.gov.il "מרכז נתונים"` / `site:ags.iplan.gov.il "חוות שרתים"`
- `"{locality Hebrew}" "חוות שרתים" "היתר"` / `"{locality Hebrew}" "מרכז נתונים" "תכנית"` / `"{locality}" "דאטה סנטר" "בקשה להיתר"`
- `"{operator}" "חוות שרתים" "מוא"`（MVA）/ `"{operator}" "תחנת משנה"` / `"{operator}" "רשות החשמל"` / `site:maya.tase.co.il "{operator}" "חוות שרתים"`
- `site:gov.il "חוות שרתים" "רשות החשמל"` / `site:iec.co.il "חוות שרתים" OR "data center"` / `site:noga-iso.co.il "חוות שרתים" OR "data center"`
- `"Israel" "data center" "grid connection"` / `"Tel Aviv" "data center" "MW"` / `"Petah Tikva" "data center" "Digital Realty"` / `"Kfar Yona" "data center" "MedOne"` / `"Ashdod" "data center" "Dalia" "Serverfarm"`
- `"{city}" Israel ("underground data center" OR "fortified data center")` / `"חוות שרתים" ("תת קרקעי" OR "ממוגן" OR "שרידות") "{עיר}"`
- 状态词映射：החלה בנייה/אבן פינה=施工（B/A 依源）；נחנך/הושק/נפתח=运营（A 须运营商页复核）；יוקם/מתוכנן/בקשה=规划/lead；הקפאה=冻结（2026 电力语境）。

## 官方/监管管线要点（详见 explorer-official.md）

- **规划管理局（A 级）**：IPlan https://www.iplan.gov.il/；Mavat https://mavat.iplan.gov.il/SV3?searchEntity=3&searchMethod=2（按希伯来词/运营商/SPV/工业区名/规划号搜；按区过滤：דרום=HaDarom、חיפה=Hefa、ירושלים=Yerushalayim、מרכז=HaMerkaz、תל אביב=Tel Aviv、צפון=HaTsafon；提取规划号、区/地方委员会、地块/宗地、用途、建筑权、委员会决定与附件 PDF：הוראות/תשריט/נספחים/פרוטוקולים/החלטות）；XPlan 蓝线图 https://ags.iplan.gov.il/xplan/；规划地图服务 https://ags.iplan.gov.il/services/；政府决定 3907 https://www.gov.il/he/pages/dec3907-2026。官方规划文档短语：מטרת התכנית、עיקרי הוראות התכנית、שימושים מותרים、זכויות בנייה、קומות תת קרקעיות、תחנת משנה、חדרי חשמל、גנרטורים、מערכות קירור、נספח סביבתי、נספח תנועה、נספח תשתיות、החלטת ועדה、פרוטוקול。用规划号在市政府/地方委员会站再搜——本地页可能暴露 Mavat 不明显的建筑许可（בקשה להיתר）细节。
- **电力局/IEC/Noga（A 级）**：决定/听证中心 + 74506 + 50 MVA 听证 + 财政部/能源部临时建议（2026-02-19）+ IEC 连接概率图 + IEC https://www.iec.co.il/ + https://iec-global.com/ + Noga https://www.noga-iso.co.il/。每个规划/施工项目按项目/运营商搜 `חיבור לרשת`、`מוא"`/MVA、`תחנת משנה`、`רשת ההולכה`、`חברת החשמל`、`נגה`、`רשות החשמל`；记录电力是 secured/requested/suspended/speculative——2026 政策已对 8 MVA+ 数据中心连接改变；贸易声称「secured power」在电力局决定/IEC-Noga 材料/规划文件/证券备案确认前为 B。连接容量与 IT 负载分列（文档可能给 מוא"״/MVA、设施总 MW 或 IT MW，不换算除非注明假设）。
- **通信部（运营商身份，非设施）**：https://www.gov.il/he/departments/ministry_of_communications + 通用/统一许可页 https://www.gov.il/he/pages/lic（Bezeq International 等运营商）；许可不证明具体站点有数据中心。
- **证券备案（A 级，上市公司）**：TASE/MAYA（见核心结构事实 §6）。
- **云区域页**：AWS https://aws.amazon.com/local/israel/ + regions doc（il-central-1）；GCP https://cloud.google.com/about/locations + https://docs.cloud.google.com/compute/docs/regions-zones（me-west1）+ Nimbus https://cloud.google.com/blog/topics/inside-google-cloud/google-cloud-selected-to-provide-cloud-services-to-the-state-of-israel；Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list + https://news.microsoft.com/source/emea/features/microsoft-to-launch-new-cloud-datacenter-region-in-israel/；Oracle https://www.oracle.com/il-en/cloud/cloud-regions/israel/ + https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm。
- **运营商官方页（A 级存在性/容量）**：MedOne https://medone.co.il/（官方称 25,000+ sqm 分布于四个安全地下站点 + 七个在建/开发站点；Kfar Yona/Ramle/Petah Tikva/Tirat HaCarmel/Dimona；扩张路线图超 250 MW IT，注明 secured land/power 的命名站点）；Bynet Data Centers https://bynetdcs.co.il/（Jerusalem of Gold/Silver/Light、TLV A/B、Lod、Ha'horesh Shoham，逐站 rack/MW/sqm）；Bezeq International https://www.bezeqint.net/en（电信/海缆相邻）；Serverfarm ISR1 https://www.serverfarmllc.com/tel-aviv-data-center/（北特拉维夫首个中东设施）+ 阿什杜德 Dalia/IIF 130 MW 项目（B 至运营商页/许可成熟）；Digital Realty/Mivne https://www.digitalrealty.com/about/newsroom/press-releases/122655/...（Petah Tikva 多租户园区最高 20 MW IT，Mivne https://en.mivnegroup.co.il/）；Equinix 无清晰官方特拉维夫设施页——聚合器 `Equinix TL` 声称未证实；Mega Data Centers/Mega Or https://www.megadc.com/our-sites（MATAM Haifa、Beit Shemesh、Idan HaNegev、Masmia/Bnei Re'em、Modi'in、Hadera，AI/HPC 导向）；Global Technical Realty https://globaltechnicalrealty.com/（Petah Tikva IS One 10.5 MW 地下 build-to-suit，须 Mavat/地方委员会许可证明）；NED Data Centers https://www.ned-dc.com/projects/?ContentID=70652（Netanya Alpha Campus 42 MW AI-ready 地下，Globes 报 2027 年初首设施）；IDCA https://idca.org.il/（行业生态源，非设施普查）。
- **B 级项目信号**：Dalia Energy/Serverfarm/IIF Ashdod 130 MW（约 15 亿美元，DCD/Globes）；Keystone Fund/IPM Be'er Tuvia 两数据中心园区 40 MW IT（电站旁）；Nvidia Yokneam/Mevo Carmel 内部 AI/HPC（报道现有 30 MW + 63/64 MW 建设，与 Mega DC 谈判 64 MW，多为内部用途，press-only）；Nebius/Mega Or Modi'in；Mega Or 购入 Hadera Alliance Tire 地块（约 10 亿新谢克尔，市场预期大型 DC，B 至规划/电力文件）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **贸易媒体分级**：Globes EN/HE（B+，最佳商业/地产/基建源：Dalia/Serverfarm Ashdod 130 MW、NED Netanya 42 MW、Nvidia/Mega Or Mevo Carmel、Keystone Be'er Tuvia、Mega Or Hadera）；Calcalist/CTech（B+，电力监管/投资/MedOne/AI 需求与瓶颈，并网受限项目预警）；DCD（B+，国际贸易源：Dalia、MedOne、NED、GTR、Keystone、AWS、Oracle）；Times of Israel/JNS/Jerusalem Post/Ynetnews（B/C+，云区域启动、Oracle/Bynet 耶路撒冷、Nvidia/Yokneam）；Dgtl Infra/The Tech Capital/Data Centre Magazine/Data Center POST（B-/C+）；IDCA（B-/C+）。
- **运营商/开发商矩阵（按区）**：Tel Aviv=Serverfarm ISR1、Bynet TLV A/B、AWS/GCP/Azure 逻辑区域标签；HaMerkaz=GTR Petah Tikva IS One、Bynet Lod/Shoham、MedOne Ramle/Kfar Yona、NED Alpha Netanya、Mega DC Modi'in/Beit Shemesh、Nebius/Mega Or Modi'in、Digital Realty Mivne Petah Tikva；Yerushalayim=Bynet Jerusalem of Gold/Silver/Light、Oracle/Bynet 地下耶路撒冷、Beit Shemesh（按来源市场归类）；Hefa=MedOne Tirat HaCarmel、Mega DC MATAM Haifa、Mega Or/Mega DC Hadera；HaTsafon=Nvidia/Yokneam/Mevo Carmel AI/HPC、Mega DC/Mega Or 北部管线；HaDarom=Dalia/Serverfarm/IIF Ashdod、Mega DC Idan HaNegev + Masmia/Bnei Re'em、Keystone/IPM Be'er Tuvia、MedOne Dimona（聚合器 lead）、Beersheba 边缘/HPC（Gav-Yam Negev 园区多为校园 IT 而非商业托管）。
- **目录来源（C+）**：Data Center Map https://www.datacentermap.com/israel/（快速城市/运营商种子与别名，物理 AZ 地点未经一手证据不算确认）、Datacenters.com、Baxtel（关系图与规划园区线索：MedOne/NED/GTR）、Mordor/ResearchAndMarkets/Arizton（市场规模，不作设施存在证明）。
- **去重与验证**：媒体常说「Tel Aviv」实为 Central 区郊区（Petah Tikva/Shoham/Lod/Ramle/Netanya/Kfar Yona/Modi'in）；`DigiTel` 疑似 Digital Realty 或 דיגיטל ריאלטי 误拼，仅作别名不作设施；Nvidia 园区搜索混入办公室/实验室（仅当文章说 data center/AI processing facility/GPU/MW/חוות שרתים 才计）；大型 AI 园区多为电力预留或拿地故事而非在建设施；2026 电力冻结下高 MW 无并网证据项目保持 planned/speculative；地下/加固设施单独标注。

## 来源分级

- **A** = 官方/一手：Mavat 规划/申请/听证页或附件法定文件、地方/区规划委员会决定/协议/建筑许可/市政府官方发布、电力局决定/听证、IEC/Noga 电网材料或官方并网文件、运营商官方设施页（地点/容量/状态）、云供应商官方区域文档（仅区域/AZ 数）、TASE/MAYA 上市公司备案、通信部许可（仅电信/运营商身份）。
- **B** = 强二级：DatacenterDynamics、Globes、Calcalist、TheMarker、Jerusalem Post、Data Center Frontier、Data Centre Magazine（引用命名运营商/备案/政府决定）；基础设施基金投资方页（点名项目状态与运营商）；供应商/承包商案例（明确站点/运营商）。
- **C** = 仅作线索：DataCenterMap、Baxtel、Datacenters.com、Cloudscene、Ocolo、Newby Ventures、MLQ.ai、LinkedIn/社交、经纪商列表、SEO 设施页、无一手源的聚合容量/地址值。
- 状态语义：planned/permitting/construction/operational/expansion/cancelled-paused 按规划/电力/运营商证据；>8 MVA 或 >50 MVA 项目显式标注 2026 电力局暂停/听证是否影响时序；连接容量与 IT 负载分列。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=IL，divisions=6 districts），按 explorer-industry.md §4 逐区枚举（含希伯来区/地名词）。
2. 种子：运营商种子（MedOne、Bynet、Bezeq International、Serverfarm、Digital Realty Mivne、Mega DC/Mega Or、GTR、NED、Oracle/Bynet、AWS、Google Cloud、Microsoft、Nvidia/Nebius）+ 云区域页 + Project Nimbus 语境。
3. 扫描：Mavat 搜希伯来/英文项目/运营商与通用希伯来词，存规划号与委员会状态 → 电力局/IEC/Noga 搜项目/运营商/地点 + מוא"״/MVA/תחנת משנה/חיבור לרשת → MAYA/TASE 搜上市实体（Mivne、Mega Or、Levinstein、Dalia、Electra、Shikun & Binui、Azrieli）→ 运营商官网核对设施/园区状态与容量（运营商页优先于聚合器）→ 贸易媒体补缺（B 降级除非一手文档已链接并核查）。
4. 验证：以 A 级官方记录落事实；地名/区归一化（营销都会名→市镇/区，用 Mavat/XPlan 或地图）；每个 >8 MVA 或 >50 MVA 项目显式标注 2026 电力局暂停/听证影响；字段含 name/operator-SPV/district-municipality/industrial-zone-campus-parcel/status/planning reference/energy reference（requested-secured MVA、IT MW、总功率 MW、变电站/并网）/building scale（sqm、racks、楼层、地下/加固状态）/tenants-cloud links（AWS/GCP/Azure/Oracle/Nebius/Nvidia）/evidence URLs-date/confidence notes。
5. 输出：按 world schema 写结果，附证据日期与分级。
6. 无项目判定：低密度区（Beersheba 边缘、HaTsafon 大部、HaDarom 内陆）显式负面搜索（运营商+希伯来词+规划/电力兜底），区分校园 IT/机房与商业托管；三面无信号才设 no_projects: true。
7. 遵守 NO-DELETION；本 skill 与两份 explorer 均为只读输入，只新增 SKILL.md 与 ANATOMY.md。

## 待办（2026-08-12 02:31Z）

- [x] explorer-official.md 与 explorer-industry.md 已完成并合并为本 SKILL.md。
- [ ] 下一步：每批 50× codex terra agents，注入本 skill 后按 6 区逐区枚举（优先 HaMerkaz、Tel Aviv、Hefa、Yerushalayim、HaDarom、HaTsafon）。
- [ ] 待核实：Digital Realty Mivne Petah Tikva 20 MW 园区的 Mavat/TASE 现状；MedOne 扩张路线图各站点（Kfar Yona/Ramle/Tirat HaCarmel/Dimona）的规划与电力状态（2026 冻结影响）；Dalia/Serverfarm Ashdod 130 MW 与 Keystone Be'er Tuvia 40 MW 的 Mavat 申请与电力局处理状态；Nvidia Yokneam/Mevo Carmel 设施的官方/Mavat 证据；Oracle 耶路撒冷地下设施经 Bynet 的运营商/规划佐证。
