#!/usr/bin/env python3
"""Generate per-data-center directory skeleton from the frozen 2026-07-16 baseline.

One directory per master record under dc/<slug>/, each containing:
  - SKILL.md   : maintenance contract (data sources, update cadence, fields, validation)
  - NOTES.md   : update log (initial: baseline extraction note)
  - data.json  : extracted baseline fields from national_master_inventory.json

Slug = <master_id>-<short-project-name>, lowercased, filesystem-safe.
Idempotent: re-run refreshes data.json from the baseline without touching NOTES.md.
"""
import json, os, re, sys, datetime

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASELINE = os.path.join(PROJ, "legacy-baseline-20260716", "national_master_inventory.json")
DC_DIR = os.path.join(PROJ, "dc")

SKILL_TEMPLATE = """# {master_id} — {project}

## 一句话
{status_short}

## 位置
- City: {city}
- County: {county}
- State: {state}
- 地址/地块: {parcel}

## 维护契约（每次更新必读）

### 数据源（按优先级）
1. 官方/地方政府：county/city 规划、permit、site plan、utility service records
2. 业主/开发商公告（company announcement）
3. 区域媒体 / 行业 tracker（CBRE/JLL/C&W/Savills/Cleanview/WoodMac 等）
4. 电网侧：utility interconnection queue / load forecasts

### 更新频率
- 至少每周刷新一次；重大公告（开工/获批/并网/跳票）即时更新
- 每条新事实必须带来源 URL 与日期

### 字段（data.json 保持这些 key）
- status_as_of_cutoff / evidence_grade
- capacity_mw（如可得）、owner、location
- milestones/actions（date, government_body, action_type, result_status）
- sources（URL 列表）、contradictions（如有多源冲突）

### 验证方式
- 已证实事实与推测/projected tails 分开标注
- 多源冲突记入 NOTES.md 并保留来源
- announced ≠ construction：状态分层按 baseline 的
  announced / local process / approved-permitted / site work-construction /
  energized / partial live / full buildout

### 如何更新（给后续 agent 的接手流程）
1. 读本 SKILL.md 与 data.json、NOTES.md
2. 按数据源优先级搜索新事实，优先官方/local-government 来源
3. 更新 data.json（同一 key 覆盖并保留旧值到 history）或追加 NOTES.md 新节
4. 更新 NOTES.md（日期 + 变化 + 来源 URL）
5. git add + commit（message 含 master_id 与变更摘要）

## 相关文件

- `data.json`（结构化数据真源）· `NOTES.md`（历次更新记录）
- 顶层 `SKILL.md`（方法论路由）· `ANATOMY.md`（结构地图）

## 基线来源
- baseline: legacy-baseline-20260716/national_master_inventory.json (SHA 2113de4b…)
- master_id: {master_id}
- phase3 stable_id: {stable_id}
"""

NOTES_INIT = """# {master_id} — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: {status_short}
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。
"""


def slugify(master_id, project):
    s = re.sub(r"[^a-z0-9]+", "-", project.lower()).strip("-")
    return f"{master_id.lower()}-{s[:60]}".rstrip("-")


def status_short(rec):
    p3 = rec.get("phase3_record") or {}
    return (p3.get("status_as_of_cutoff") or "").split(".")[0][:200] or "no status"


def main():
    inv = json.load(open(BASELINE))
    recs = inv["master_records"]
    print(f"records: {len(recs)}")
    os.makedirs(DC_DIR, exist_ok=True)
    count = 0
    for rec in recs:
        mid = rec["master_id"]
        proj = rec.get("canonical_project") or mid
        slug = slugify(mid, proj)
        d = os.path.join(DC_DIR, slug)
        os.makedirs(d, exist_ok=True)
        loc = rec.get("location") or {}
        p3 = rec.get("phase3_record") or {}
        p3loc = p3.get("location") or {}
        st = status_short(rec)
        data = {
            "master_id": mid,
            "canonical_project": proj,
            "aliases": rec.get("aliases", []),
            "location": loc,
            "phase3_stable_id": p3.get("stable_id"),
            "status_as_of_cutoff": p3.get("status_as_of_cutoff"),
            "actions": p3.get("actions", []),
            "capacity_mw": p3.get("capacity_mw"),
            "owner": p3.get("owner"),
            "sources": p3.get("sources", rec.get("provenance", {})),
            "contradictions": p3.get("contradictions", []),
            "seed_only": not rec.get("phase3_record"),
            "baseline_sha": "2113de4b0a3455288dc010fcf731fca2aa127d7faa02cfd7418950716b1d1b9a",
        }
        with open(os.path.join(d, "data.json"), "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        skill = SKILL_TEMPLATE.format(
            master_id=mid, project=proj, status_short=st,
            city=loc.get("city", p3loc.get("city", "")),
            county=loc.get("county", p3loc.get("county", "")),
            state=loc.get("state", p3loc.get("state", "")),
            parcel=p3loc.get("parcel_or_address", ""),
            stable_id=p3.get("stable_id", ""),
        )
        with open(os.path.join(d, "SKILL.md"), "w") as f:
            f.write(skill)
        notes_p = os.path.join(d, "NOTES.md")
        if not os.path.exists(notes_p):
            with open(notes_p, "w") as f:
                f.write(NOTES_INIT.format(master_id=mid, status_short=st))
        count += 1
    print(f"generated dirs: {count}")


if __name__ == "__main__":
    main()
