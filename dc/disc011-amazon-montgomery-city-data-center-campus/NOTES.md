# disc011 — 更新记录

## 2026-08-11（discovery 并入）
- 由 codex discovery daemon 发现（candidates-hyperscaler.jsonl），人类审批后并入（Jason “开始做吧”, 2026-08-11）。
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- 状态从 `announced/planned` 更新为 `approved-permitted`。县官网项目页列出 Project Green (Amazon Web Services) 及县级 Project Green Resolution Plan、Chapter 100 Bond Order、Plan Cost Benefit Analysis、site plan、development/funding agreement 等材料；搜索索引可见县托管 PDF，包括 infrastructure agreement、NorthPoint site plan、Chapter 100 bond order。（来源：https://mcmo.us/amazon/ ；https://mcmo.us/wp-content/uploads/2026/02/Infrastructure-Development-and-Funding-Agreement-Project-Green.pdf ；https://mcmo.us/wp-content/uploads/2026/02/NorthPoint-Project-Green-site-plan.pdf ；https://mcmo.us/wp-content/uploads/2026/02/Chapter-100-Bond-Order-Project-Green.pdf ；检索日期：2026-08-11）
- 官方公告核实投资、业主与地方影响：Missouri Governor 于 2026-06-15 公告 Amazon 计划在 Montgomery City 建设 100 亿美元数据中心园区，预计 400 个直接岗位、数千个建设岗位、25 年内数亿美元新增财产税，并说明 Amazon/Ameren 电力服务成本由项目承担。（来源：https://governor.mo.gov/press-releases/archive/amazon-investing-10-billion-montgomery-county ；日期：2026-06-15）
- Amazon 自身公告核实 Montgomery County 数据中心园区、400+ 全职岗位、道路与水基础设施、$7M+ 社区投入、Ellis Road 桥梁/道路改造、水系统建成后捐给 Montgomery County Public Water Supply District No. 1、雨水回收和水循环设计；Amazon 文章称水冷使用时间预计不超过全年 7%。（来源：https://www.aboutamazon.com/news/company-news/amazon-data-center-missouri-new-jobs ；日期：2026-06）
- Ameren 于 2026-06-26 确认 Amazon 在 Montgomery County 的 100 亿美元数据中心投资将受 Ameren Missouri 大负荷客户方案约束，需预付 100% 并网相关成本，且最低月度需量电费至少为最大申请需量的 80%。（来源：https://www.ameren.com/resource-center/amazon ；日期：2026-06-26）
- 场址细节补充：Data Center Dynamics 于 2026-06-16 报道 Project Green 位于 New Florence、Montgomery County，I-70 与 Highway 19 交叉口东北象限，约 1,000 acres；AWS 计划两期开发，第一期 8 栋、第二期最多 13 栋，并配置雨洪池、3 口井、污水和水处理设施。（来源：https://www.datacenterdynamics.com/en/news/amazon-commits-10bn-to-data-center-campus-in-montgomery-city-missouri/ ；日期：2026-06-16）
- 批准/许可证据补充：The Missouri Times 于 2026-02-04 称 Project Green 为 approved development plan，并列出 minimum phase one 与 maximum full build-out 税收情景；Montgomery Standard 摘要称 Project Green 和 Project Spade 均于 2025-11 获 site plan approval，Project Green 已获得 dirt disturbance permit。（来源：https://themissouritimes.com/aws-new-facilities-near-new-florence-will-double-tax-revenue-for-montgomery-county/ ；日期：2026-02-04；https://www.mystandardnews.com/stories/residents-voice-concerns-about-proposed-data-centers%2C146731 ；日期：2026-05）
- 容量：未发现官方 campus MW。Cleanview 把 AWS Project Green 单体楼列为 75 MW、planned、2027 expected year，但这是行业 tracker 的建筑级数据，本次未据此推导 campus `capacity_mw`。（来源：https://cleanview.co/data-centers/missouri/2124/aws-project-green---building-1 ；检索日期：2026-08-11）
- 冲突/不确定项：官方州长公告写 Montgomery City；县材料、DCD 与本地报道多称 New Florence / I-70 and Highway 19 交叉口附近 Project Green。暂保留 canonical_project，并在 data.json `location.site_area` 与 `contradictions` 中标注。
