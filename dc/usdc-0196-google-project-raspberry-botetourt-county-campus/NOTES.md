# USDC-0196 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: County-approved land-use and performance-agreement framework; Virginia DEQ water and air applications remained under review
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：仍按 `approved-permitted / local process` 处理，不上调到 `site work-construction`。Botetourt County 官方项目页截至本次刷新仍称首批 grading permit applications 于 2026-02 收到，on-site grading expected before the end of 2026；未找到已开工、building permit issued、CO、energized 或 live 的官方记录。来源：https://www.botetourtva.gov/1021/Google-Data-Center
- DEQ 审核状态复核：Virginia Water Protection Permit application（received 2026-01-21，Request 25-1919）和 Minor NSR air permit application（received 2026-05-13，Request 21819-1）仍在 DEQ 项目页标为 under review。DEQ 页面还给出项目范围：343.6-acre parcel 中扰动 240.4 acres，三栋约 300,000 sq ft 数据中心、三座变电站、一栋约 28,000 sq ft 办公楼及配套基础设施。来源：https://www.deq.virginia.gov/news-info/shortcuts/topics-of-interest/google-s-project-raspberry
- 设计/用水事实新增：2026-07-22 Google 宣布第一栋数据中心建筑将使用 air-cooling technology；Botetourt County 转发该更新，Western Virginia Water Authority 同日更新称预计项目整体用水需求将低于原先预测，但尚无更新后的 demand figures。来源：https://www.botetourtva.gov/m/newsflash/home/detail/1160；https://www.westernvawater.org/customers/capital-projects/draft-proposed-data-center-in-botetourt-center-at-greenfield
- 监管/公众审查事实新增：2026-07-28 Botetourt County Board of Supervisors 以 3-1 通过设立五人 independent commission，评估拟建 Google data center campus 对环境、基础设施、utility resources 和生活质量的影响；该行动是独立审查安排，不是 permit approval 或 construction milestone。来源：https://www.botetourtva.gov/m/newsflash/home/detail/1164
- owner 补证：county performance agreement 的公司方为 Helio Capital LLC，county/Google 项目页则将项目公开表述为 Google 的 planned data center campus；因此 `owner` 记为 Google LLC / Helio Capital LLC（项目公司/申请主体）。来源：https://www.botetourtva.gov/DocumentCenter/View/6347/Google-Performance-Agreement；https://www.botetourtcountydatacenter.com/
- capacity_mw：继续保留 `null`。未找到官方披露的 IT load、utility interconnection MW 或 full site energy capacity。媒体提及的 79 MW Rocky Forge PPA 不等于 campus capacity，未写入容量字段。
- contradictions：未发现需要写入 `contradictions` 的事实冲突。当前主要不确定项是未来 grading start、更新后用水 demand figures、DEQ permit final decisions、commission appointments/report。
- verified: true（本次写入事实均来自官方/地方政府/utility/Google 项目站点；容量仍因无官方数值而保持未知）。
