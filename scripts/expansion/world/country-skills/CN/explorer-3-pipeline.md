# CN Explorer 3 — 行政/监管管道 (Administrative & Regulatory Pipeline) for China Datacenter Enumeration

> Purpose: China cannot be enumerated the way US/EU markets are (no unified planning-permit database,
> no FOIA, hyperscalers do not publish site lists). Instead, China has a **dense official paper trail**:
> every datacenter above trivial size must pass 备案/核准 (investment filing), 节能审查 (energy-conservation
> review), 环评 (environmental impact assessment), and the operator needs an IDC 许可证 (B11 telecom license).
> Each step produces a **public announcement (公示/公告)**. This document maps those channels and gives
> concrete query patterns per province / 地级市 (prefecture-level city).
>
> Per Jason 3443: China needs a different query method — this is that method.

---

## 1. 东数西算 ("East Data, West Computing") — 8 National Hubs, 10 Cluster Cities

The national backbone layout. Approved by 国家发改委/中央网信办/工信部/国家能源局 in two waves:
- **2021-12** (发改高技〔2021〕1773号 series): 内蒙古、贵州、甘肃、宁夏 4 western hubs approved first.
- **2022-02**: 京津冀、长三角、粤港澳、成渝 4 eastern hubs approved → "东数西算" officially launched
  (announcement: https://www.ndrc.gov.cn/fzggw/jgsj/gjss/sjdt/202203/t20220321_1319862.html).
- **2023-12**: 《深入实施"东数西算"工程 加快构建全国一体化算力网的实施意见》(发改数据〔2023〕1779号)
  — upgrades the framework to 全国一体化算力网 (national integrated computing-power network).

### 8 hubs (算力枢纽节点) → 10 clusters (数据中心集群) → anchor cities/districts

| # | 枢纽 (Hub) | 集群 (Cluster) | Anchor location (地级市 / district) |
|---|-----------|----------------|--------------------------------------|
| 1 | 京津冀枢纽 | 张家口集群 | 河北省张家口市 (怀来县、张北县、宣化区) |
| 2 | 长三角枢纽 | 长三角生态绿色一体化发展示范区集群 | 上海市青浦区、江苏省苏州市吴江区、浙江省嘉兴市嘉善县 |
| 3 | 长三角枢纽 | 芜湖集群 | 安徽省芜湖市 (鸠江区、弋江区、无为市) |
| 4 | 粤港澳大湾区枢纽 | 韶关集群 | 广东省韶关市 (浈江区、武江区、曲江区) |
| 5 | 成渝枢纽 | 天府集群 | 四川省成都市 (双流区、郫都区、简阳市) |
| 6 | 成渝枢纽 | 重庆集群 | 重庆市 (两江新区水土新城、西部(重庆)科学城璧山片区、重庆经开区) |
| 7 | 内蒙古枢纽 | 和林格尔集群 | 呼和浩特市和林格尔新区 + 乌兰察布市集宁大数据产业园 |
| 8 | 贵州枢纽 | 贵安集群 | 贵阳市/贵安新区 |
| 9 | 甘肃枢纽 | 庆阳集群 | 庆阳市西峰区 (庆阳东数西算产业园) |
| 10 | 宁夏枢纽 | 中卫集群 | 中卫市 (中卫工业园西部云基地) |

Notes for enumeration:
- The 4 western hubs (内蒙古/贵州/甘肃/宁夏) are **whole-province hubs**; the eastern 4 are metro hubs.
  But actual buildout concentrates in the cluster cities above — start prefecture enumeration there.
- Cluster cities publish their own project lists: e.g. 张家口市发改委, 芜湖市数据资源管理局,
  韶关市工信局, 中卫市发改委 regularly announce 数据中心集群重点项目 with rack counts.
- Non-hub provinces still have large DC bases (山西阳泉/百度, 河北廊坊/润泽, 江苏南京/宿迁,
  湖北武汉, 山东青岛/济南, 陕西西安) — 东数西算 is a subset, not the universe.
- Progress stats (rack counts per cluster) appear in NDRC press events and 中国信通院 reports; as of
  late 2023 the 10 clusters exceeded ~1.05M standard racks (search: "十大集群 标准机架 上架率").

---

## 2. Provincial-Level Project Tracking (省级项目公示渠道)

This is the core "different query method" for China. Every fixed-asset investment project — datacenters
included — must go through 审批 (approval, gov-funded) / 核准 (verification, restricted sectors) /
备案 (filing, most private DC projects) and receives a 项目代码 (unified project code). All of it flows
through one national platform plus province mirrors, and generates public announcements.

### 2.1 全国投资项目在线审批监管平台 (National Online Investment Project Approval & Supervision Platform)

- National portal: **https://www.tzxm.gov.cn** (new UI: https://new.tzxm.gov.cn) — operated by 国家信息中心.
- Every province runs its own instance, e.g.:
  - 浙江: https://tzxm.zjzwfw.gov.cn
  - 上海: https://tzxm.fgw.sh.gov.cn
  - 四川: https://tzxm.sczwfw.gov.cn
  - 甘肃: https://tzxm.fzgg.gansu.gov.cn
  - Pattern: search `"<省名> 投资项目在线审批监管平台"` — every province has one, usually under
    the 政务服务网 (zwfw.gov.cn) domain of that province.
- **Query pattern**: the platforms have 公示公告 / 审批结果公示 sections. Search keywords:
  `数据中心`, `智算中心`, `算力中心`, `IDC`, `云计算中心`, `大数据中心`, `灾备中心`.
  Records give: 项目代码 (24-digit), 建设地点 (down to 区/县), 总投资, 建设规模 (often rack counts /
  机柜数 / 万台服务器), 备案机关, 备案日期.
- Caveat: the national portal's public search is limited; the **provincial portals + 省/市发改委
  website 公示 pages are the reliable public surface**.

### 2.2 节能审查公示 (Energy-Conservation Review) — HIGHEST-SIGNAL CHANNEL for DCs

- Legal basis: 《固定资产投资项目节能审查办法》(国家发改委令 2023年第2号). Projects with annual
  energy consumption ≥ 1万吨标准煤 (or electricity ≥ ~5000万kWh, province-dependent) need 省级节能审查.
  **Almost every non-trivial datacenter crosses this threshold**, so 省发改委(或能源局) 节能审查意见
  公示 pages are effectively a **datacenter project registry with design specs**.
- What the 节能审查意见 discloses: project name, owner entity, exact site, 机架数 (rack count),
  设计PUE, annual electricity consumption, sometimes phasing. This is the single best official source
  for capacity numbers.
- Query pattern: on each 省发改委 site search `节能审查 数据中心` in the 政务公开/公示公告 section.
  Examples of active publishers: 河北省发改委, 内蒙古自治区能源局, 宁夏发改委, 甘肃省发改委,
  广东省发改委, 上海市发改委 (上海 additionally caps new DC PUE and runs annual 新建数据中心
  用能指标 allocation — its 批复名单 is a direct list of approved Shanghai DC projects).
- Hub provinces impose PUE gates (typically ≤1.2 in clusters, ≤1.25–1.3 east) — the review docs state them.

### 2.3 环评公示 (Environmental Impact Assessment)

- 建设项目环境影响评价信息公开: 受理公示 → 拟审批公示 → 审批决定, published by 市/省生态环境局.
- National aggregator: 全国建设项目环境影响评价管理信息平台 (https://zwfw.mee.gov.cn 及各省生态环境厅网站).
- Query pattern: `<市>生态环境局 数据中心 环评 受理公示`. EIA docs (报告表/报告书 full PDFs are often
  posted) contain site coordinates, building areas, diesel-generator counts, cooling design.

### 2.4 通信管理局 IDC 许可公示 (Telecom Regulator — IDC License, the operator-side registry)

- IDC 业务 = 增值电信业务分类目录 **B11类 互联网数据中心业务** (includes 互联网资源协作/云).
  Operating any commercial DC requires this license: 跨地区 (multi-province) licenses issued by 工信部,
  single-province licenses by the 省通信管理局.
- **Master query system**: 电信业务市场综合管理信息系统 — **https://dxzhgl.miit.gov.cn**
  (also https://tsm.miit.gov.cn). Left menu 许可业务信息 → search by 企业名称 or 许可证号:
  `https://dxzhgl.miit.gov.cn/dxxzsp/xkz/xkzgl/resource/qiyesearch.jsp?num=<企业名称>&type=xuke`
  Returns: license number, 业务种类 (look for B11), 覆盖范围 (which provinces), validity dates.
- 工信部 publishes batched 许可证发放/注销名单 (e.g. "(2025)第47批") — mirrored by industry trackers
  such as https://expert.aodun.com.cn/industry/notice (convenient for diffing new entrants).
- Each 省通信管理局 site (pattern: `<省份简称>ca.miit.gov.cn`, e.g. 北京 bca.miit.gov.cn,
  江苏 jsca.miit.gov.cn, 广东 gdca.miit.gov.cn) has 行政审批公示 listing newly licensed IDC operators
  in that province — filter by B11.
- Use: license registered address + coverage → maps operators to provinces; cross-join with
  investment filings to attach facilities to operators.

### 2.5 Other provincial channels

- 公共资源交易平台 / 中国土地市场网 (https://www.landchina.com): 数据中心用地 land-auction results
  give exact parcels and buyer entities. Query `数据中心` in 土地出让结果公告 per city.
- 省/市"十四五"及后续数字经济、新基建规划: planning documents enumerate named pipeline projects.
- 重大项目清单 (annual 省级重点建设项目名单, published each Jan–Mar by 省发改委): datacenters appear
  by name with investment amounts — an excellent yearly snapshot per province.

---

## 3. Key National Lists (全国性官方名单)

| List | Issuer | Latest known | Where |
|------|--------|--------------|-------|
| 国家算力枢纽节点批复 (8 hubs / 10 clusters) | 发改委等四部门 | 2021-12 / 2022-02 批复文件 | ndrc.gov.cn 高技术司 pages |
| 国家新型数据中心典型案例名单 | 工信部通信发展司 | 2021年 (44个), 2022年 (33个: 21 大型 + 7 中小型 + 5 边缘) | miit.gov.cn 公示, mirror: https://www.ncsti.gov.cn/kjdt/tzgg/202303/t20230316_110914.html |
| 国家绿色数据中心名单 | 工信部等六部门, 多批次 (2018/2019, 2020, 2021, 2023年度…) | 2023年度 50家, 公告2024年第12号 (2024-06) | https://www.ncsti.gov.cn/kjdt/tzgg/202406/t20240606_159619.html |
| 数据中心绿色低碳发展专项行动计划 | 发改委等 (2024-07) | 政策文件 with PUE targets | https://www.ndrc.gov.cn/xwdt/tzgg/202407/P020240723625616053849.pdf |
| 增值电信业务经营许可证发放名单 (含IDC) | 工信部, rolling batches | ongoing (per-batch 公告) | dxzhgl.miit.gov.cn; mirror expert.aodun.com.cn/industry/notice |

Supporting quasi-official sources:
- 中国信通院 (CAICT, http://www.caict.ac.cn): 《中国数据中心产业发展白皮书》 and 算力发展指数 —
  per-province rack/compute statistics (aggregate, not per-project).
- ODCC 开放数据中心委员会 (https://www.odcc.org.cn): industry standards body; member/project lists.
- CDCC (中国数据中心工作组): annual 数据中心市场 reports with per-region supply data.
- Note: the 新型数据中心 and 绿色数据中心 lists are **selective showcases**, not registries — use them
  as high-grade confirmations of flagship facilities, never as an enumeration base.

---

## 4. Cloud Provider Official Region/Zone Pages (China)

These pages are the ground truth for *operational* hyperscale capacity and reveal host prefectures.

| Provider | Region/AZ doc | China regions (city ↔ region code) |
|----------|---------------|-------------------------------------|
| 阿里云 Alibaba Cloud | https://help.aliyun.com/zh/document_detail/40654.html | 华北1青岛 cn-qingdao, 华北2北京 cn-beijing, 华北3张家口 cn-zhangjiakou, 华北5呼和浩特 cn-huhehaote, 华北6乌兰察布 cn-wulanchabu, 华东1杭州 cn-hangzhou, 华东2上海 cn-shanghai, 华东5南京 cn-nanjing, 华东6福州 cn-fuzhou, 华中1武汉 cn-wuhan-lr, 华南1深圳 cn-shenzhen, 华南2河源 cn-heyuan, 华南3广州 cn-guangzhou, 西南1成都 cn-chengdu |
| 腾讯云 Tencent Cloud | https://cloud.tencent.com/document/product/213/6091 | 北京 ap-beijing, 上海 ap-shanghai, 南京 ap-nanjing, 广州 ap-guangzhou (AZs extend into 清远), 深圳金融 ap-shenzhen-fsi, 成都 ap-chengdu, 重庆 ap-chongqing; self-built campuses: 天津滨海、清远、重庆、贵安七星 |
| 华为云 Huawei Cloud | https://support.huaweicloud.com/en-us endpoint docs / https://developer.huaweicloud.com/endpoint | 华北-北京一/四 cn-north-1/4, 华北-乌兰察布一 cn-north-9, 华东-上海一/二 cn-east-3/2, 华东-青岛 cn-east-5, 华南-广州 cn-south-1, 西南-贵阳一 cn-southwest-2; flagship campuses 贵安、乌兰察布 |
| 火山引擎 Volcano Engine (字节跳动) | https://www.volcengine.com/docs/6261/64926 | 华北2(北京) cn-beijing, 华东2(上海) cn-shanghai, 华南1(广州) cn-guangzhou; ByteDance self-built: 张家口怀来、内蒙古乌兰察布 (via colo partners) |
| 百度智能云 Baidu AI Cloud | https://cloud.baidu.com/doc/Reference/s/2jwvz23xx | 华北-北京 bj, 华北-保定 bd, 华东-苏州 su, 华南-广州 gz, 华中-武汉 fwh; self-built flagship 山西阳泉、河北徐水/定兴 (西部: 阳泉是百度最大自建园区) |
| 京东云 JD Cloud | https://docs.jdcloud.com/cn/common-declaration/regions-and-availability-zones | 华北-北京 cn-north-1, 华东-宿迁 cn-east-1, 华东-上海 cn-east-2, 华南-广州 cn-south-1; self-built 宿迁、廊坊 |
| 移动云 (中国移动) | https://ecloud.10086.cn (节点分布/资源池 pages) | Resource pools across 呼和浩特(和林格尔)、哈尔滨、贵阳 三大跨省中心 + per-province pools; 中国移动 owns the largest carrier DC footprint |
| 天翼云 (中国电信) | https://www.ctyun.cn (资源池列表 in docs) | 2+4+31+X layout: 内蒙古(和林格尔)、贵州(贵安) 2 hubs + 京津冀/长三角/粤港澳/成渝 4 regions + 31 省级资源池 |
| 联通云 (中国联通) | https://www.cucloud.cn | 5+4+31+X layout; mega-campuses 呼和浩特、贵安、廊坊、哈尔滨 |

Enumeration value:
- Region pages give **prefecture presence** but not facility addresses; hyperscalers mostly lease from
  colo operators (万国数据GDS 09698.HK, 世纪互联VNET NASDAQ:VNET, 秦淮数据/Chindata, 润泽科技300442.SZ,
  数据港603881.SH, 光环新网300383.SZ, 奥飞数据300738.SZ, 宝信软件600845.SH). **Listed-company annual
  reports and bond prospectuses of these colos disclose per-campus MW/rack data** — a key secondary channel.
- 三大运营商 (telcos) publish DC footprints in annual reports and 集采公告 (procurement tenders on
  b2b.10086.cn / caigou.chinatelecom.com.cn / 联通采购 sites) — tender documents name specific
  数据中心机楼 per city.

---

## 5. Systematic Per-地级市 (Prefecture) Enumeration Method

Recommended pipeline, per province P and prefecture C (333 prefecture-level divisions; canonical list:
民政部行政区划代码 https://www.mca.gov.cn/mzsj/xzqh/):

1. **Seed from clusters & lists (top-down)**: 东数西算 cluster membership (§1), 新型/绿色数据中心 lists
   (§3), 省级重点项目清单 (§2.5) → initial named-project set per prefecture.
2. **投资备案 sweep (per province)**: provincial 投资项目在线审批监管平台 + 省/市发改委公示 search
   `数据中心 OR 智算 OR 算力 OR IDC` — capture 项目代码, 建设地点(区县), 总投资, 规模. This yields the
   *pipeline* (planned/approved) set.
3. **节能审查 sweep**: 省发改委/能源局 节能审查意见公示 — attach rack counts, PUE, MW (via annual kWh)
   to each project. Best capacity source (§2.2).
4. **环评 sweep**: 市生态环境局 受理/审批公示 — confirms siting to parcel level, adds construction status.
5. **IDC license join**: dxzhgl.miit.gov.cn B11 query per operator; 省通管局 公示 for new provincial
   licensees — maps operators ↔ provinces, catches operators missed by project filings.
6. **Corporate cross-check**: 国家企业信用信息公示系统 (https://www.gsxt.gov.cn) + 企查查/天眼查/爱企查 —
   search 企业名称 contains `数据中心`/`云计算` with 注册地 = C; project SPVs are usually registered in
   the host county. Colo listed-company filings (§4) for MW-grade detail.
7. **Land join**: landchina.com 出让结果 for DC-zoned parcels in C.
8. **Status resolution**: 备案 ≠ 开工 ≠ 投产. Resolve status via: local gov news (`<市>人民政府 数据中心
   开工/投产/点亮`), operator PR, and 运营商集采 (a live tender implies an operating/near-complete hall).
9. **Industry-media backfill**: 中国IDC圈 (http://www.idcquan.com), DTDATA, 数据中心世界 — good for
   deal/opening news; treat as leads to verify against channels 2–5.

Practical notes:
- Provincial portals are Chinese-only, often require slider captchas; static 公示 list pages are
  crawlable, the search APIs generally are not. Prefer **site-restricted web search**
  (`site:fgw.<province>.gov.cn 数据中心 节能审查`) over portal search boxes.
- Do the sweep **province-by-province** (31 provincial units), not prefecture-by-prefecture — 公示
  pages are provincial; then bucket results into prefectures by 建设地点 parsing.
- Expect heavy aliasing: one physical campus = multiple filings (一期/二期/扩建), an SPV name, a brand
  name, and a 集群 marketing name. Dedupe on address + owner-entity graph.

---

## 6. Evidence-Grade Mapping for Chinese Official Sources

Recommended grading for the us-dc-intel evidence model:

| Grade | Definition | Chinese sources in this grade |
|-------|-----------|-------------------------------|
| **A — Official/primary** | Government legal-effect document naming the project | 发改委枢纽批复文件; 节能审查意见 (capacity specs); 环评批复; 投资项目备案/核准公示 (项目代码); 通管局/工信部 IDC 许可记录 (operator-level); 工信部 新型/绿色数据中心名单; cloud provider official region/AZ docs (operational status, prefecture granularity) |
| **B — Semi-official/corroborated** | State-affiliated or legally accountable disclosure | 央企/运营商年报及集采公告; listed colo annual reports & bond prospectuses (audited MW/rack data); 省/市政府工作报告及规划 named projects; landchina.com 出让结果; 政府官网新闻 (开工/投产仪式) |
| **C — Industry/reported** | Credible trade press, unverified | 中国IDC圈, CDCC/信通院市场报告 (aggregates), C114, provider PR without regulatory trail |
| **D — Weak** | Social media, marketing decks, stale aggregator maps | 微信公众号 rumors, sales brochures |

Caveats to encode with any Chinese evidence item:
- **Stage semantics**: 备案 (filed) → 节能审查/环评 (permitted) → 开工 (construction) → 投产/点亮
  (operational). A-grade filings prove *stage*, not existence of live capacity; many 备案'd projects
  (especially 2020–2021 vintage "算力园区") never broke ground.
- **Design vs. actual**: rack counts and PUE in 节能审查 are design values; actual fit-out lags years.
- **Link rot & access**: .gov.cn 公示 pages expire; archive (screenshot + Wayback) at capture time.
  Some MIIT/NDRC pages block non-CN IPs intermittently — mirrors (ncsti.gov.cn, waizi.org.cn,
  provincial reposts) are acceptable A-grade carriers when the issuing document number
  (e.g. 公告2024年第12号, 发改高技〔2022〕207号) is preserved and citable.
- **Military/state-sensitive**: government cloud (政务云) and certain state facilities are deliberately
  under-documented; absence from public channels is not evidence of absence.

---

## Quick-Reference URL Index

- 全国投资项目在线审批监管平台: https://www.tzxm.gov.cn / https://new.tzxm.gov.cn
- 电信业务市场综合管理信息系统 (IDC 许可查询): https://dxzhgl.miit.gov.cn (alias https://tsm.miit.gov.cn)
  - 许可查询 endpoint: `https://dxzhgl.miit.gov.cn/dxxzsp/xkz/xkzgl/resource/qiyesearch.jsp?num=<企业名称>&type=xuke`
- 工信部: https://www.miit.gov.cn (公示公告 → search 数据中心)
- 国家发改委: https://www.ndrc.gov.cn (高技术司 for 东数西算; 政务公开 for 节能审查办法)
- 2023年度国家绿色数据中心名单: https://www.ncsti.gov.cn/kjdt/tzgg/202406/t20240606_159619.html
- 国家新型数据中心典型案例 (2022年): https://www.ncsti.gov.cn/kjdt/tzgg/202303/t20230316_110914.html
- IDC 许可发放批次 mirror: https://expert.aodun.com.cn/industry/notice
- 企业信用: https://www.gsxt.gov.cn; 土地: https://www.landchina.com
- 行政区划 (prefecture list): https://www.mca.gov.cn/mzsj/xzqh/
- 中国信通院: http://www.caict.ac.cn; ODCC: https://www.odcc.org.cn; 中国IDC圈: http://www.idcquan.com
- Cloud regions: 阿里 https://help.aliyun.com/zh/document_detail/40654.html ·
  腾讯 https://cloud.tencent.com/document/product/213/6091 ·
  华为 https://developer.huaweicloud.com/endpoint ·
  火山 https://www.volcengine.com/docs/6261/64926 ·
  百度 https://cloud.baidu.com/doc/Reference/s/2jwvz23xx ·
  京东 https://docs.jdcloud.com/cn/common-declaration/regions-and-availability-zones ·
  移动云 https://ecloud.10086.cn · 天翼云 https://www.ctyun.cn · 联通云 https://www.cucloud.cn

*Compiled 2026-08-11 by explorer-3 (pipeline). Sources verified via web search where marked; .gov.cn
availability from outside CN varies — archive on capture.*
