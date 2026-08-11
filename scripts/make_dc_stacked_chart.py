#!/usr/bin/env python3
"""US DC intel: stacked line chart by status layer (上线/在建/计划) by planned year.
Jason 3177: 像之前那样的线图，上线、在建、计划的叠在一起.
"""
import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# CJK font on macOS
from matplotlib import font_manager
for fp in ["/System/Library/Fonts/PingFang.ttc",
           "/System/Library/Fonts/STHeiti Light.ttc",
           "/System/Library/Fonts/Hiragino Sans GB.ttc"]:
    if os.path.exists(fp):
        try:
            font_manager.fontManager.addfont(fp)
        except Exception:
            pass
for name in ["PingFang SC", "PingFang HK", "Hiragino Sans GB", "STHeiti"]:
    try:
        plt.rcParams["font.family"] = [name, "DejaVu Sans"]
        break
    except Exception:
        continue
plt.rcParams["axes.unicode_minus"] = False

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUMMARY = os.path.join(BASE, "scratch", "fix", "centers-summary.json")
OUT = os.path.join(BASE, "visualization")
os.makedirs(OUT, exist_ok=True)

centers = json.load(open(SUMMARY))


def tier(status):
    s = (status or "").lower()
    if any(w in s for w in ["operational", "live", "energized", "commissioned", "partial live"]):
        return "op"
    if any(w in s for w in ["construction", "site work", "under construction", "groundbreak", "building", "broken ground"]):
        return "uc"
    return "planned"

T_LABEL = {"op": "上线 / 已带电", "uc": "在建 / 场地施工", "planned": "计划 / 已批 / 提议"}
T_COLOR = {"op": "#2ca02c", "uc": "#1f77b4", "planned": "#d62728"}
T_ORDER = ["op", "uc", "planned"]

# Aggregate capacity (MW) by (tier, completion_year)
by = defaultdict(lambda: defaultdict(float))
cnt = defaultdict(lambda: defaultdict(int))
unknown = defaultdict(float)
for c in centers:
    t = tier(c.get("status", ""))
    cap = c.get("capacity_mw")
    if cap is None:
        continue
    y = c.get("completion_year")
    if y:
        by[t][str(y)] += cap
        cnt[t][str(y)] += 1
    else:
        unknown[t] += cap

all_years = sorted({y for t in T_ORDER for y in by[t]})
# pad missing years with 0 per tier
for t in T_ORDER:
    for y in all_years:
        by[t].setdefault(y, 0.0)
        cnt[t].setdefault(y, 0)

layers = [np.array([by[t][y] / 1000.0 for y in all_years]) for t in T_ORDER]
total = np.sum(layers, axis=0)

fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(all_years, layers,
             labels=[T_LABEL[t] for t in T_ORDER],
             colors=[T_COLOR[t] for t in T_ORDER], alpha=0.75)
ax.plot(all_years, total, "ko-", lw=2, ms=7, label="合计 (GW)")
for x, v in zip(all_years, total):
    ax.annotate(f"{v:.1f}", (x, v), textcoords="offset points", xytext=(0, 9),
                ha="center", fontsize=10, fontweight="bold", color="#222222")

# per-layer per-year labels
for t, layer in zip(T_ORDER, layers):
    for x, v, n in zip(all_years, layer, [cnt[t][str(y)] for y in all_years]):
        if v > 0.05:
            ax.annotate(f"{v:.1f}\n({n})", (x, v), textcoords="offset points",
                        xytext=(0, -16 if t != "op" else 8), ha="center",
                        fontsize=7.5, color="#333333")

# unknown-year total
unk_total = sum(unknown.values())
if unk_total > 0:
    ax.axhline(unk_total / 1000.0, color="#7f7f7f", ls="--", lw=1.2)
    ax.text(all_years[-1], unk_total / 1000.0 + 0.6,
            f"年份未定合计 ~{unk_total/1000:.1f} GW", color="#7f7f7f", fontsize=9, ha="right")

known_total = total[-1]
ax.set_title(
    f"US 数据中心容量按状态与计划年份（GW，已披露 capacity_mw 聚合）\n"
    f"上线/在建/计划堆叠 \u2014 含年份 {known_total:.1f} GW，另有年份未定 {unk_total/1000:.1f} GW；240 中心数据截至 2026-08-11 刷新+复核+修复",
    fontsize=12)
ax.set_ylabel("GW")
ax.set_xlabel("计划投运 / 目标年份")
ax.set_ylim(0, max(60, max(total) * 1.25))
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9, loc="upper left")

out = os.path.join(OUT, "dc_stacked_by_status.png")
fig.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
plt.close(fig)
print(f"wrote {out} ({os.path.getsize(out)} bytes)")

# also print numeric table for the message
print("year | op(GW) | uc(GW) | planned(GW) | total(GW)")
for y in all_years:
    print(y, round(by["op"][y]/1000, 1), round(by["uc"][y]/1000, 1), round(by["planned"][y]/1000, 1), round((by["op"][y]+by["uc"][y]+by["planned"][y])/1000, 1))
print("unknown by tier:", {t: round(unknown[t]/1000, 1) for t in T_ORDER})
