#!/usr/bin/env python3
"""Generate PNG charts for the US DC intel repo (Jason 3164: PNG via matplotlib).

Reusable: reads scratch/fix/centers-summary.json and writes PNGs to visualization/.

Usage: scratch/vizenv/bin/python scripts/make_dc_charts.py
"""
import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
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


def save(fig, name):
    p = os.path.join(OUT, name)
    fig.savefig(p, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"wrote {p} ({os.path.getsize(p)} bytes)")

# 1. total planned power by year
by_year = defaultdict(float)
cnt_year = defaultdict(int)
unknown_mw = 0.0
unknown_n = 0
for c in centers:
    cap = c.get("capacity_mw")
    if cap is None:
        continue
    y = c.get("completion_year")
    if y:
        by_year[y] += cap
        cnt_year[y] += 1
    else:
        unknown_mw += cap
        unknown_n += 1

years = sorted(by_year)
vals = [by_year[y] / 1000.0 for y in years]
fig, ax = plt.subplots(figsize=(11, 6))
bars = ax.bar([str(y) for y in years], vals, color="#1f77b4", width=0.6)
for b, y in zip(bars, years):
    ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.3,
            f"{by_year[y]:.0f} MW\n({cnt_year[y]} centers)", ha="center", fontsize=9)
if unknown_mw:
    ax.axhline(unknown_mw / 1000.0, color="#d62728", ls="--", lw=1.2)
    ax.text(len(years) - 0.4, unknown_mw / 1000.0 + 0.4,
            f"年份未定 ~{unknown_mw:.0f} MW\n({unknown_n} centers)", color="#d62728", fontsize=9, ha="right")
total = sum(vals)
ax.set_title(f"US 规划数据中心总功耗（按计划投运/在建年份）\nTotal Planned Data Center Power by Year — 共 {total:.1f} GW 含年份 + {unknown_mw/1000:.1f} GW 年份未定", fontsize=12)
ax.set_ylabel("GW")
ax.set_xlabel("计划投运 / 目标年份")
ax.grid(axis="y", alpha=0.3)
save(fig, "dc_total_power_by_year.png")

# 2. status tier distribution

def tier(status):
    s = (status or "").lower()
    if any(w in s for w in ["operational", "live", "energized", "commissioned", "partial live"]):
        return "运营/已带电"
    if any(w in s for w in ["construction", "site work", "under construction", "groundbreak", "building"]):
        return "在建/场地施工"
    if any(w in s for w in ["approved", "permitted", "rezoning", "plat", "permit"]):
        return "已批准/已许可"
    if any(w in s for w in ["proposed", "planned", "proposal", "announced", "potential", "pre-application", "siting", "provisional"]):
        return "提议/规划中"
    return "未知/其他"


tiers = defaultdict(int)
for c in centers:
    tiers[tier(c.get("status", ""))] += 1
order = ["运营/已带电", "在建/场地施工", "已批准/已许可", "提议/规划中", "未知/其他"]
ts = [tiers.get(k, 0) for k in order]
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(order, ts, color=["#2ca02c", "#1f77b4", "#ff7f0e", "#9467bd", "#7f7f7f"])
for i, v in enumerate(ts):
    ax.text(i, v + 1, str(v), ha="center", fontsize=11)
ax.set_title("数据中心状态分布（由 status 文本粗分类）", fontsize=12)
ax.set_ylabel("中心数")
ax.tick_params(axis="x", rotation=15)
save(fig, "dc_status_distribution.png")

# 3. state aggregation
state_cnt = defaultdict(int)
state_mw = defaultdict(float)
for c in centers:
    st = c.get("state") or "未知"
    state_cnt[st] += 1
    cap = c.get("capacity_mw")
    if cap is not None:
        state_mw[st] += cap

top = sorted(state_mw.items(), key=lambda x: -x[1])[:15]
names = [s for s, _ in top][::-1]
mws = [m / 1000.0 for s, m in top][::-1]
fig, ax = plt.subplots(figsize=(9, 7))
ax.barh(names, mws, color="#17becf")
for i, v in enumerate(mws):
    ax.text(v + 0.2, i, f"{v:.1f} GW ({state_cnt[names[i]]})", va="center", fontsize=9)
ax.set_title("州级规划容量 TOP 15（含年份信号聚合）", fontsize=12)
ax.set_xlabel("GW")
save(fig, "dc_state_top15.png")

# 4. owner breakdown

def owner_label(o):
    if isinstance(o, dict):
        o = str(o.get("name") or o.get("company") or o)
    if not isinstance(o, str):
        o = str(o)
    return o.split(",")[0].split("/")[0].strip() or "未知"


own_cnt = defaultdict(int)
own_mw = defaultdict(float)
for c in centers:
    o = owner_label(c.get("owner"))
    own_cnt[o] += 1
    cap = c.get("capacity_mw")
    if cap is not None:
        own_mw[o] += cap

top = sorted(own_mw.items(), key=lambda x: -x[1])[:12]
names = [s for s, _ in top][::-1]
mws = [m / 1000.0 for s, m in top][::-1]
fig, ax = plt.subplots(figsize=(9, 6))
ax.barh(names, mws, color="#ff9896")
for i, v in enumerate(mws):
    ax.text(v + 0.2, i, f"{v:.1f} GW ({own_cnt[names[i]]})", va="center", fontsize=9)
ax.set_title("所有者/运营商规划容量 TOP 12（按首位归属粗聚合）", fontsize=12)
ax.set_xlabel("GW")
save(fig, "dc_owner_top12.png")

print("done")
