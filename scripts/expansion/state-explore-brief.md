# US DC intel 超集清单 · 州级探索任务

## 背景
Jason 要求维护「最宽口径」超集：每个 county、每个开发商、互联网上所有蛛丝马迹形成的项目清单。你负责探索**一个指定州**，找出该州所有数据中心项目（含早期公告/未证实），产出结构化 JSONL。

## 你的任务
探索州 = <STATE_NAME>（<STATE_ABBR>）

找出该州所有数据中心项目条目（运营/在建/计划/早期公告），包括但不限于：
- 已入册知名项目（如 hyperscaler campus、Stargate 等）
- county EDA（经济发展机构）公告的项目
- 州 utility / 互联队列记录的项目（若有）
- 新闻/公告里出现的新项目（Data Center Dynamics、Utility Dive、当地新闻）
- 许可记录（building permit、rezoning、tax abatement）
- developer 官网/新闻稿

## 对每个项目输出 JSON 行
{
  "source": "state-explore",
  "state": "TX",
  "project_name": "官方/常见名称",
  "aliases": ["其他名字"],
  "county": "县名",
  "city": "城市（如知）",
  "developer": "开发商/运营商（如知）",
  "capacity_mw": 数字或 null,
  "status": "operational|construction|approved|planned|announced|rumor|unknown",
  "status_detail": "状态细节文本",
  "year": 预计投运年份或 null,
  "source_urls": ["证据 URL"],
  "evidence_date": "2026-08-11",
  "evidence_grade": "official|news|tracker|social|unknown",
  "notes": "备注"
}

## 方法
1. 先 web_search 该州 + data center 项目、最新公告
2. 检查该州主要 DC 市场的 county EDA 网站/公告
3. 检查该州 RTO/ISO 互联队列或 utility 公告（如 ERCOT/PJM/MISO/SPP/CAISO 相关）
4. 遍历 Data Center Dynamics 等新闻 archive
5. 汇总去重

目标：找到尽可能多的项目条目，宁多勿漏（证据等级会标注）。至少输出 10 个项目，越多越好。

## 输出
写入 /Users/huangzesen/work/projects/us-dc-intel/scripts/expansion/state-projects/<STATE_ABBR>-projects.jsonl
每条一行 JSON。

## 契约
- 只读探索，不修改 repo 内任何现有文件（dc/ 下已有项目目录不动）
- NO-DELETION
- 只写你的输出文件
- 用 web_search/web/curl 实际查证，不要凭记忆编造；不确定的证据等级标 low
