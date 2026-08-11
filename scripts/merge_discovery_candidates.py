#!/usr/bin/env python3
"""Merge discovery-daemon candidates into dc/<slug>/ directories.

Reads scripts/discovery-candidates/candidates-*.jsonl, dedupes across files,
and creates one dc/<disc-id>-<short-name>/ directory per unique candidate with:
  - SKILL.md  : maintenance contract (same structure as 208 baseline centers)
  - NOTES.md  : discovery log entry
  - data.json : candidate fields (name/owner/location/capacity/status/sources/
                evidence_date/confidence/why_not_in_baseline)

Slug = disc<nnn>-<short-project-name>, lowercased, filesystem-safe.
Idempotent: re-run refreshes data.json and SKILL.md without duplicating NOTES.md.
"""
import json, os, re, sys, datetime

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAND_DIR = os.path.join(PROJ, "scripts", "discovery-candidates")
DC_DIR = os.path.join(PROJ, "dc")
BASELINE_SHA = "2113de4b0a3455288dc010fcf731fca2aa127d7faa02cfd7418950716b1d1b9a"
TODAY = "2026-08-11"

# Cross-file duplicate merge: list of (kept_name_norm, drop_name_norm) pairs.
# name_norm is lowercase alnum only. The daemons wrote the same project with
# slightly different owner/location strings, so match on name pattern instead.
DUP_MERGE = [
    ("powerhousepoecompanieslouisvillehyperscalecampus", "powerhousepoelouisvillecampgroundroaddatacentercampus"),
]

SKILL_TEMPLATE = """# {disc_id} — {project}

## 一句话
{status_short}

## 位置
- City: {city}
- County: {county}
- State: {state}

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
- canonical_project / owner / location / capacity_mw / status
- evidence_date / confidence / sources（URL 列表）
- why_not_in_baseline、contradictions（如有多源冲突）

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
5. git add + commit（message 含 disc_id 与变更摘要）

## 来源
- 发现于 2026-08-11 codex discovery daemon（{discovery_file}）
- 与 legacy-baseline-20260716（SHA {baseline_sha_short}）校验：无 canonical 名冲突
- disc_id: {disc_id}
"""

NOTES_INIT = """# {disc_id} — 更新记录

## {today}（discovery 并入）
- 由 codex discovery daemon 发现（{discovery_file}），人类审批后并入（Jason “开始做吧”, 2026-08-11）。
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。
"""


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:60].rstrip("-")


def status_short(c):
    return (c.get("status") or "no status").split(".")[0][:200]


def load_candidates():
    records = []
    for fn in sorted(os.listdir(CAND_DIR)):
        if not fn.startswith("candidates-") or not fn.endswith(".jsonl"):
            continue
        p = os.path.join(CAND_DIR, fn)
        with open(p) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                r = json.loads(line)
                r["_file"] = fn
                records.append(r)
    return records


def dedupe(records):
    drop_ids = set()
    for keep_norm, drop_norm in DUP_MERGE:
        keep = [r for r in records if norm(r.get("name")) == keep_norm]
        drops = [r for r in records if norm(r.get("name")) == drop_norm]
        if keep and drops:
            for r in drops:
                drop_ids.add(id(r))
    return [r for r in records if id(r) not in drop_ids], drop_ids


def main():
    records = load_candidates()
    uniq, dropped = dedupe(records)
    uniq.sort(key=lambda r: (r["_file"], r.get("name") or ""))
    os.makedirs(DC_DIR, exist_ok=True)
    created = []
    for i, r in enumerate(uniq, start=1):
        disc_id = f"disc{i:03d}"
        slug = f"{disc_id}-{slugify(r.get('name') or 'unnamed')}"
        d = os.path.join(DC_DIR, slug)
        os.makedirs(d, exist_ok=True)
        loc = r.get("location") or {}
        st = status_short(r)
        data = {
            "disc_id": disc_id,
            "canonical_project": r.get("name"),
            "owner": r.get("owner"),
            "location": loc,
            "capacity_mw": r.get("capacity_mw"),
            "status": r.get("status"),
            "confidence": r.get("confidence"),
            "evidence_date": r.get("evidence_date"),
            "sources": r.get("source_urls", []),
            "why_not_in_baseline": r.get("why_not_in_baseline"),
            "discovery_file": r["_file"],
            "added_at": TODAY,
            "baseline_sha": BASELINE_SHA,
        }
        with open(os.path.join(d, "data.json"), "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        skill = SKILL_TEMPLATE.format(
            disc_id=disc_id, project=r.get("name") or disc_id, status_short=st,
            city=loc.get("city", ""), county=loc.get("county", ""), state=loc.get("state", ""),
            discovery_file=r["_file"], baseline_sha_short=BASELINE_SHA[:12],
        )
        with open(os.path.join(d, "SKILL.md"), "w") as f:
            f.write(skill)
        notes_p = os.path.join(d, "NOTES.md")
        if not os.path.exists(notes_p):
            with open(notes_p, "w") as f:
                f.write(NOTES_INIT.format(disc_id=disc_id, today=TODAY, discovery_file=r["_file"]))
        created.append((disc_id, r.get("name"), slug))
    print(f"total records: {len(records)}")
    print(f"dropped as cross-file duplicates: {len(dropped)}")
    for r in records:
        if id(r) in dropped:
            print(f"  drop {r.get('name')} ({r['_file']})")
    print(f"unique candidates merged: {len(created)}")
    for disc_id, name, slug in created:
        print(f"  {disc_id} {name} -> dc/{slug}")


if __name__ == "__main__":
    sys.exit(main())
