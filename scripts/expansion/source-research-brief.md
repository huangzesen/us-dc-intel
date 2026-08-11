# US DC intel 超集清单 · 数据源调研任务

## 背景
Jason 要求把 US 数据中心清单维护成「最宽口径」超集：现有 repo 240 中心（baseline 208 + discovery 32），目标是几千个项目级条目（Cleanview 1788 planned / 369.9 GW、ERCOT 互联队列 225-233 GW、各 RTO/ISO 队列、各州公告等）。

## 你的任务（只读调研，不写 repo）
调研以下数据源的可抓取性，产出调研报告 JSONL。**NO-DELETION：不删除/不修改任何现有文件。**

对每个数据源回答：
- name: 数据源名
- url: 主 URL
- accessible: true/false（能否无需登录/付费直接抓取全量或部分）
- auth_required: none/login/paywall
- project_level: true/false（是否项目级条目，非聚合数字）
- has_capacity: true/false（是否含容量 MW）
- has_status: true/false（是否含状态：运营/在建/计划/公告）
- has_year: true/false（是否含年份）
- est_projects: 预估项目数（能估算的话）
- pagination: 分页方式（URL query / 无限滚动 / 登录墙无）
- fetch_method: curl / web_search / browser / api / none
- notes: 简短备注（抓取难点、去重价值、证据质量）
- sample: 1-3 个示例项目（名称/地点/容量/状态）

## 要调研的数据源（按优先级）
1. Cleanview https://www.cleanview.co/data-centers/us （已知：州页只有 top 项目；完整列表需登录，验证有无 workaround）
2. datacenterHawk https://www.datacenterhawk.com/ （商业 tracker，看免费内容有多少）
3. Baxtel https://www.baxtel.com/ （免费 DC tracker，美国项目）
4. Data Center Map https://www.datacentermap.com/ （免费）
5. DC Byte https://www.dcbyte.com/ （商业，看免费公开列表）
6. ERCOT 互联队列（https://www.ercot.com/mp/data-products/data-product-details?id=PG7-200-ER 或同类；GIS 报告 July2026 有 ~225-233 GW）
7. PJM 互联队列 https://www.pjm.com/planning/service-requests/interconnection-queues
8. MISO 互联队列 https://www.misoenergy.org/planning/generator-interconnection/queue/
9. SPP 互联队列 https://www.spp.org/engineering/generator-interconnection/
10. NYISO / ISO-NE / CAISO / SERC 互联队列
11. Wikipedia 美国数据中心列表（如有）
12. Utility/公告聚合：Utility Dive、Data Center Dynamics、Datacenter Dynamics US 新闻 archive
13. 州级 tracker：如 Virginia/Wisconsin/Indiana 的经济发展公告页
14. CBRE/JLL/Cushman 等 broker 报告附带的项目表（免费 PDF 部分）
15. 其他你发现的免费项目级源（如 eia、federal permit trackers）

## 输出
写入 /Users/huangzesen/work/projects/us-dc-intel/scripts/expansion/source-research-<your-name>.jsonl
每条一行 JSON。最后写 /Users/huangzesen/work/projects/us-dc-intel/scripts/expansion/source-research-<your-name>-summary.md 总结：哪些源可直接抓全量、哪些只能部分、建议的抓取优先级。

## 契约
- 只读调研，不修改 repo 内任何文件
- NO-DELETION
- 用 curl/web 工具实际测试 1-2 个源的可访问性，不要只靠推断
- 输出文件放指定路径
