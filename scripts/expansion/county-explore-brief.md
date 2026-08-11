# US DC intel · County 级探索任务

## 背景
Jason 要求最宽口径超集：直接去**每一个 county** 的网站找原始数据（当地新闻/EDA 公告/county 会议记录/许可），避免遗漏。你负责探索 batch 文件里列出的 county。

## 你的任务
1. 读取你的 county 列表：<BATCH_FILE>（TSV：州\t县名，10 行）
2. 对**每个 county**：
   - 直接访问 county 官网（搜索 `<county名> county <state> official website`）
   - 找 EDA / 经济发展 / 规划 / county commission 页面
   - 在该站搜索 data center / server farm / colocation / hyperscale 相关公告、新闻、会议记录、tax abatement、rezoning、building permit
   - 也可以搜 `<county名> county <state> data center` 找当地新闻（当地报纸）
3. 汇总该 county 的数据中心项目（运营/在建/计划/早期公告/被拒都算，**宁多勿漏**）

## 输出 JSONL（每项目一行）
{
  "source": "county-explore",
  "county": "县名",
  "state": "州",
  "project_name": "项目名",
  "aliases": [],
  "city": "城市或 null",
  "developer": "开发商或 null",
  "capacity_mw": 数字或 null,
  "status": "operational|construction|approved|planned|announced|rejected|unknown",
  "status_detail": "细节",
  "year": 年份或 null,
  "source_urls": ["原始 URL"],
  "evidence_date": "2026-08-11",
  "evidence_grade": "official|news|tracker|social|unknown",
  "notes": "备注"
}

没找到项目的 county 也输出一行 {"source":"county-explore","county":"X","state":"Y","project_name":null,"status":"no_projects_found","notes":"..."} 以便追踪覆盖。

## 输出文件
写入 /Users/huangzesen/work/projects/us-dc-intel/scripts/expansion/county-results/<BATCH_NAME>-results.jsonl（如 batch-000-results.jsonl）

## 契约
- 只读探索，不修改 repo 现有文件（dc/ 目录不动）
- NO-DELETION，只写你的输出文件
- 实际访问 county 网站验证，不凭记忆编造；证据等级不实的标 low
- 快速：每个 county 控制在 3-5 分钟以内，找不到就标记 no_projects_found 继续
