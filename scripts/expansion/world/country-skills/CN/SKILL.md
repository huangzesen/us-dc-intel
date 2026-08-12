---
name: cn-datacenter-methodology
location: scripts/expansion/world/country-skills/CN/SKILL.md
description: |
  China (CN) datacenter discovery & audit methodology — how to enumerate, verify, and update China datacenter projects at prefecture-level granularity. China needs a different query method from US/EU: official paper trail (发改委备案/节能审查/环评/IDC 许可证 B11), 东数西算 8 hubs / 10 clusters, 智算中心 announcements, and the WeChat private-domain ecosystem. Read this before running CN exploration/audit batches. Routes to explorer-1-web.md (web search), explorer-2-wechat.md (WeChat), explorer-3-pipeline.md (regulatory pipeline).
---

# CN · 中国数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：中国数据中心不能按美欧方式枚举（无统一规划许可库、无 FOIA、超大规模厂商不公布站点清单）。
> 中国有**密集的官方纸面轨迹**：每个达到一定规模的数据中心必须经过发改委备案/核准、节能审查、环评，
> 运营方需要 IDC 增值电信业务许可证（B11 类）。每一步都产生公开**公示/公告**。
> 本 skill 汇总三份探索报告，供中国探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-1-web.md` | 中文 web 搜索策略：引擎、查询模板（发现/备案/容量提取）、权威来源分级、IDC 厂商名录、超大规模云区域 |
| `explorer-2-wechat.md` | 微信私域获取：公众号监控集、weixin.sogou.com 搜索、小程序/视频号、微信群、来源可信度分级 |
| `explorer-3-pipeline.md` | 行政/监管管线：东数西算 8 枢纽/10 集群、发改委项目公示、节能审查、环评、IDC 许可、各省平台 |

## 核心结构事实（框定每次搜索）

1. **东数西算**（2022 年启动）：8 大算力枢纽 = 京津冀、长三角、粤港澳大湾区、成渝、内蒙古、贵州、甘肃、宁夏；10 大数据中心集群 = 张家口、长三角生态绿色一体化示范区、芜湖、韶关、天府、重庆、和林格尔、贵安、庆阳、中卫。大多数 2022 年后大型新建集中在这些集群——按此地理定位搜索。
2. **IDC 运营商需要工信部 B11 增值电信业务许可证**——许可注册表是运营商普查（非设施普查）。
3. 每个较大项目需要**发改委备案/核准**，超过阈值需**节能审查**（2023-06-01 新版《固定资产投资项目节能审查办法》）。这些备案泄漏 MW/机架数/投资额——中国最好的免费容量证据。
4. 2023 年以来热点是**智算中心/算力中心**（AI 算力），常由地方政府而非传统 IDC 厂商宣布。搜索两种词汇：数据中心、智算中心、算力中心、超算中心、云计算中心、大数据中心、IDC、机架/机柜、标准机架、P（算力规模）。

## 查询模式（复制粘贴模板见 explorer-1-web.md §1.2）

- 引擎：百度（gov.cn 最佳）、必应中国（PDF 更好）、360（补充县域 gov 页）、**搜狗微信搜索 weixin.sogou.com**（公众号文章唯一实用路径）、搜狗（知乎兜底）。
- 发现模板：`"{城市}" (数据中心 OR 智算中心 OR 算力中心) (开工 OR 奠基 OR 签约 OR 投产 OR 点亮 OR 封顶 OR 落成)`
- 备案模板：`"{城市}" 数据中心 项目 (备案 OR 核准 OR 节能审查 OR 环评 OR 公示)`
- 容量模板：`"{项目名}" (机架 OR MW OR 亿元 OR P)`
- 政府站：`site:gov.cn "{城市}" (数据中心 OR 算力) 备案`

## 微信私域要点（详见 explorer-2-wechat.md）

- 微信是封闭花园，无公开文章搜索 API。实用栈：浏览器访问 weixin.sogou.com、微信内搜一搜、基于微信读书凭据的 RSS 桥、mp.weixin.qq.com/s/... 永久链接（无需登录可读，务必作为引用捕获）。
- 核心公众号监控集（B+ 级行业媒体）：中国IDC圈（idc-quan，周刊含新项目清单）、云头条（中标/招标价格）、数据中心之家、CDCC、ODCC、半导体行业观察（AI 芯片前导）、DT财经、算力品牌自媒体（C 级线索）、通信产业网/C114。
- 公众号发布的地方发改委/园区管委会/IDC 厂商公告往往从未进入开放 web——微信是发现中国项目的关键补充通道。

## 监管管线要点（详见 explorer-3-pipeline.md）

- 全国投资项目在线审批监管平台（各省发改委）、各地节能审查公示、环评公示、工信部 IDC/ISP 许可名单。
- 各省发改委项目公示是核心"不同查询方式"。
- 来源分级：**A** = 官方/一手（政府备案、许可注册表、运营商官网、上市公司披露）；**B** = 强二级（成熟行业媒体、行业协会）；**C** = 弱/未验证（聚合器、自媒体、论坛）。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=CN，divisions=地级市/州）。
2. 按 explorer-1 查询模板对每个 division 执行 web 搜索（百度/必应/360 + site:gov.cn）。
3. 对重点城市/集群用 weixin.sogou.com 检索公众号公告（explorer-2）。
4. 对每个项目用监管管线核对备案/节能/环评证据（explorer-3），提取 MW/机架/投资额。
5. 输出与 world 探索同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；无项目 division 写 `no_projects: true`。
6. 遵守 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12 01:10Z）

- 方法论三份 explorer 初稿完成（opus 5，em-15a0/em-06c0/em-b60e）。
- 下一步：50× codex terra agent（max thinking）每 agent 20 个分批复核中国数据中心；本 skill 作为每个 daemon 的国家层参考注入。
- 其他大国（IN/DE/FR/GB/JP 等）也按此模式建立 country-skills/<CODE>/SKILL.md。
