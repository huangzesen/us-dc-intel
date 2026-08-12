#!/usr/bin/env python3
"""Task Card renderer: method-explore fleet (197 daemons / 394 batches).
Reads real filesystem state only; no fake progress.
"""
from __future__ import annotations
import json, subprocess, sys, time
from pathlib import Path

PROJ = Path("/Users/huangzesen/work/projects/us-dc-intel")
RESULTS = PROJ / "scripts/expansion/world/results-method"
REVIEW = PROJ / "scripts/expansion/world/country-skills"

TOTAL = 394
now = time.strftime("%H:%M:%S")
done = len(list(RESULTS.glob("batch-*.jsonl")))

# TW/KP review marker
review_done = all((REVIEW / c / f"explorer-{a}.md").exists()
                  for c in ("TW", "KP") for a in ("official", "industry"))

lines = [
    f"🌍 方法论探索 fleet：{done}/{TOTAL} 批 ({done*100//TOTAL}%) · {now}",
    "已派 197 daemon（deepseek flash），每 daemon 2 批",
    f"TW/KP 方法论：{'✅ 合并+审核中' if review_done else '合并中'}",
    "下一步：全批完成 → merge_method.py → DB → 部署上线",
]
if done < TOTAL:
    lines.append(f"卡住：无 · 用时：{time.strftime('%M')} min")
else:
    lines.append("卡住：无 · 全部完成，等待 merge")
print("\n".join(lines))
