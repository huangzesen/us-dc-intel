#!/usr/bin/env python3
"""CN energy (capacity) estimation — fill missing capacity_mw for China datacenters.

Jason 3560-3566 (2026-08-12): use TWO methods and fill all missing values.
  Method 1 (physical): parse physical cues from notes/name (racks, PFLOPS, investment,
    floor area, explicit MW) with tiered conversions; fall back to 东数西算 hub/region
    baselines and subnational known means.
  Method 2 (mean fill): fill with the country's existing-capacity centers mean.

Writes two new columns on centers:
  capacity_mw_est_phys  — physical-method estimate (falls back to region baseline)
  capacity_mw_est_mean  — country mean fill
  capacity_est_note     — short provenance tag for the physical estimate

Only touches CN rows that have no capacity. Idempotent. NO-DELETION.
"""

from __future__ import annotations

import json
import re
import sqlite3
import statistics
from pathlib import Path

PROJ = Path(__file__).resolve().parents[1]
DB_PATH = PROJ / "datacenters.db"
SUMMARY_PATH = PROJ / "merge-output" / "cn-energy-estimate.json"

# ---- 东数西算 8 hubs / 10 clusters: province-level baseline (MW) for no-cue projects ----
# Cluster cities get a higher baseline; general tier below.
CLUSTER_CITIES = {
    "Zhangjiakou", "Huailai", "Langfang", "Chengde", "Tianjin", "Wuhu", "Shaoguan",
    "Tianfu", "Chongqing", "Hohhot", "Ulanqab", "Guiyang", "Qingyang", "Zhongwei",
    "Huaian", "Jinan", "Guangzhou", "Shenzhen", "Suzhou", "Hangzhou", "Shanghai",
    "Beijing", "Chengdu", "Gui\u2019an", "Anshun", "Baotou", "Yinchuan", "Wuwei", "Zhangye",
}

# province -> (hub baseline MW, tier) for no-cue fallback
PROVINCE_BASELINE = {
    # East-Data-West-Computing hub provinces: higher typical per-project capacity
    "Inner Mongolia": (60, "hub"), "Gansu": (50, "hub"), "Ningxia": (50, "hub"),
    "Guizhou": (45, "hub"), "Hebei": (45, "hub"), "Beijing": (60, "hub"),
    "Tianjin": (45, "hub"), "Shanghai": (45, "hub"), "Jiangsu": (40, "hub"),
    "Zhejiang": (40, "hub"), "Anhui": (35, "hub"), "Guangdong": (45, "hub"),
    "Sichuan": (40, "hub"), "Chongqing": (40, "hub"),
    # Major economic provinces (general tier)
    "Shandong": (30, "major"), "Fujian": (25, "major"), "Hubei": (25, "major"),
    "Hunan": (22, "major"), "Henan": (22, "major"), "Shaanxi": (20, "major"),
    "Liaoning": (20, "major"), "Jilin": (18, "major"), "Heilongjiang": (18, "major"),
    "Yunnan": (20, "major"), "Guangxi": (18, "major"), "Jiangxi": (18, "major"),
    "Shanxi": (16, "major"), "Xinjiang": (18, "major"), "Qinghai": (15, "major"),
    "Hainan": (15, "major"), "Hong Kong": (25, "major"), "Macau": (15, "major"),
    "Taiwan": (25, "major"),
}

# ---- conversion constants (rough engineering-grade, documented) ----
RACK_KW = 6.0          # typical 6 kW/rack for mixed IDC
RACK_KW_HIGHDENSITY = 12.0  # AI/intelligent computing racks
PFLOP_TO_MW = 0.05     # rough: 1 PFLOPS AI cluster ~ 0.05 MW (incl. cooling) — conservative
INVEST_YI_TO_MW = 2.0  # CNY 100M investment ~ 2 MW IT power (incl. civil works)
SQM_TO_MW = 0.0005     # 0.5 kW per sqm gross floor area
MW_DIRECT_RE = re.compile(r"(\d+(?:\.\d+)?)\s*(?:MW|兆瓦|万千瓦|megawatt)", re.I)
RACK_RE = re.compile(r"(\d+(?:[\d,]*))\s*(?:机架|机柜|racks|standard racks|cabinets)", re.I)
PFLOP_RE = re.compile(r"(\d+(?:\.\d+)?)\s*(?:PFLOPS|PFlops|P FLOPS|P$)", re.I)
INVEST_RE = re.compile(r"(?:投资|invest|CNY|RMB)\s*(\d+(?:\.\d+)?)\s*(?:亿|bn|billion|亿人民币)", re.I)
SQM_RE = re.compile(r"(\d+(?:[\d,]*))\s*(?:sqm|平方米|㎡|sq m|sqm floor|gross floor)", re.I)


def parse_num(s: str) -> float:
    return float(s.replace(",", ""))


def physical_estimate(name: str, notes: str, province: str, subnational: str) -> tuple[float | None, str]:
    text = f"{name} {notes}"
    # 1) explicit MW
    m = MW_DIRECT_RE.search(text)
    if m:
        return parse_num(m.group(1)), "mw-direct"
    # 2) rack count
    m = RACK_RE.search(text)
    if m:
        n = parse_num(m.group(1))
        high = bool(re.search(r"智算|智能计算|AI|intelligent|artificial|high.?perf", text, re.I))
        return n * (RACK_KW_HIGHDENSITY if high else RACK_KW) / 1000.0, "racks"
    # 3) PFLOPS
    m = PFLOP_RE.search(text)
    if m:
        p = parse_num(m.group(1))
        return p * PFLOP_TO_MW, "pflops"
    # 4) investment (CNY 亿)
    m = INVEST_RE.search(text)
    if m:
        return parse_num(m.group(1)) * INVEST_YI_TO_MW, "invest"
    # 5) floor area sqm
    m = SQM_RE.search(text)
    if m:
        return parse_num(m.group(1)) * SQM_TO_MW, "sqm"
    # 6) province baseline
    base = PROVINCE_BASELINE.get(province)
    if base:
        return base[0], f"prov-baseline:{base[1]}"
    # 7) last resort: country median of known capacity
    return None, "none"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cols = {r[1] for r in cur.execute("PRAGMA table_info(centers)").fetchall()}
    if "capacity_mw_est_phys" not in cols:
        cur.execute("ALTER TABLE centers ADD COLUMN capacity_mw_est_phys REAL")
    if "capacity_mw_est_mean" not in cols:
        cur.execute("ALTER TABLE centers ADD COLUMN capacity_mw_est_mean REAL")
    if "capacity_est_note" not in cols:
        cur.execute("ALTER TABLE centers ADD COLUMN capacity_est_note TEXT")

    known = [r["capacity_mw"] for r in cur.execute(
        "SELECT capacity_mw FROM centers WHERE country='CN' AND capacity_mw IS NOT NULL AND capacity_mw > 0")]
    mean_mw = statistics.mean(known)
    median_mw = statistics.median(known)

    rows = cur.execute(
        "SELECT id, canonical_project, subnational, status, notes FROM centers "
        "WHERE country='CN' AND (capacity_mw IS NULL OR capacity_mw <= 0)").fetchall()
    print(f"Known CN capacity centers: {len(known)} (mean {mean_mw:.1f} MW, median {median_mw:.1f} MW)")
    print(f"CN centers missing capacity: {len(rows)}")

    # province known means for better regional fallback (optional enhancement)
    prov_rows = cur.execute(
        "SELECT subnational, capacity_mw FROM centers WHERE country='CN' AND capacity_mw IS NOT NULL AND capacity_mw > 0").fetchall()
    prov_means: dict[str, float] = {}
    prov_counts: dict[str, int] = {}
    for r in prov_rows:
        prov = (r["subnational"] or "").split(" - ")[0]
        prov_means.setdefault(prov, 0.0)
        prov_means[prov] += r["capacity_mw"]
        prov_counts[prov] = prov_counts.get(prov, 0) + 1
    for p in prov_means:
        prov_means[p] /= prov_counts[p]

    counts: dict[str, int] = {}
    total_phys = 0.0
    total_mean = 0.0
    for r in rows:
        sub = r["subnational"] or ""
        prov = sub.split(" - ")[0]
        phys, note = physical_estimate(r["canonical_project"] or "", r["notes"] or "", prov, sub)
        if phys is None:
            # per-province mean if available, else country median
            phys = prov_means.get(prov, median_mw)
            note = "prov-mean-or-median"
        counts[note] = counts.get(note, 0) + 1
        total_phys += phys
        total_mean += mean_mw
        cur.execute(
            "UPDATE centers SET capacity_mw_est_phys=?, capacity_mw_est_mean=?, capacity_est_note=? WHERE id=?",
            (round(phys, 3), round(mean_mw, 3), note, r["id"]))

    conn.commit()
    total_known = sum(known)
    summary = {
        "generated_date": "2026-08-12",
        "method": "Jason 3560-3566 two-method estimate",
        "known_centers": len(known),
        "known_capacity_mw": round(total_known, 1),
        "mean_mw": round(mean_mw, 2),
        "median_mw": round(median_mw, 2),
        "missing_centers": len(rows),
        "physical_estimate_total_mw": round(total_phys, 1),
        "mean_fill_total_mw": round(total_mean, 1),
        "combined_phys_total_mw": round(total_known + total_phys, 1),
        "combined_mean_total_mw": round(total_known + total_mean, 1),
        "cue_breakdown": counts,
    }
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    conn.close()


if __name__ == "__main__":
    main()
