# DC Discovery Brief — 找「不在 208 baseline 里」的在建/规划数据中心

## 目标

找出美国在建/规划（含已宣布、已批、施工中、即将并网）但**未被 2026-07-16 冻结 baseline（208 masters）包含**的数据中心项目。产出候选清单，供人审后并入 repo。

## 已含项目（避免重复）

208 个 master 的 canonical_project + aliases + location 在：
`/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase4/national_master_inventory.json`（master_records[].canonical_project / aliases / location）。

你的任务**不是**重查这 208 个；而是找它们之外的新项目/被漏项目。开始前先用脚本/命令提取 208 个 canonical_project 名到内存，搜索时避开。

## 搜索方向（按你的焦点）

1. **Hyperscaler / Stargate-class 新公告**：xAI、Meta、Google、OpenAI/Stargate、Amazon、Microsoft 2025-2026 新宣布或新推进的园区（如 Stargate 后续站点、xAI 新 campus、Meta 新数据中心州）
2. **二三线市场 / tracker 覆盖外**：CBRE 14 主要市场、JLL/C&W 覆盖之外的州/县；中型/区域开发商项目；工业园/旧厂改造数据中心
3. **电网 queue / utility 宣布**：ERCOT/PJM/AEP/Dominion/Oncor 等 interconnection queue 新入列的 mega-load 项目；utility 官方公布的数据中心供电协议（2025-08 之后的新公告）

## 交付物

在 `/Users/huangzesen/work/projects/us-dc-intel/scripts/discovery-candidates/` 写一个 JSONL 文件（你自己的焦点命名，如 `candidates-hyperscaler.jsonl`），每行一个候选：
```json
{"name": "项目/园区名", "owner": "运营方/开发商", "location": {"city": "", "county": "", "state": ""}, "capacity_mw": null, "status": "announced|approved|under construction|...", "source_urls": ["..."], "evidence_date": "YYYY-MM-DD", "why_not_in_baseline": "新公告/漏项/覆盖外", "confidence": "high|medium|low"}
```

规则：
- 只收录有真实来源（URL）的项目；无 URL 不写。
- 每候选至少 1 个 source_url；confidence 按证据强度。
- 不与 208 master 重名（用名称/位置判断）。
- **NO DELETION**：不删除任何文件，不 git 操作，不改 baseline；只在上面指定目录新建你自己的 JSONL。
- 完成后调用 daemon finish(status="done", summary="<候选数> candidates written to <path>", artifacts=["<path>"])。

## 范围边界

只搜美国（contiguous US + PR 等领地可备注）。只收在建/规划/已宣布，不收已全面运营多年（full buildout 长期运行）的存量设施，除非是明确扩建/新建。
