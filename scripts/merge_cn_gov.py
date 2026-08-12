#!/usr/bin/env python3
"""Merge CN gov (发改/环保) deep-dive results (cn-gov/*.jsonl) into datacenters.db + dc/<slug>/data.json.

Source: scripts/expansion/cn-gov/<province>.jsonl (31 files)
  Line schema: {name, province, city/subnational, status, capacity_mw, developer,
                source_urls, evidence_date, evidence_grade, notes}
  Or coverage row: name empty / __coverage__ marker.

Behavior (idempotent):
  - Cross-source dedup against existing centers: if a CN center with same
    (country, subnational, canonical_project lower) exists, the row is SKIPPED.
  - cn-gov-owned rows carry source_files='cn-gov:<province>' and are deleted
    before re-insert (re-run safe); existing non-cn-gov rows are never touched.
  - Metadata files use slug prefix 'cngov-{slug}' and carry "cn_gov_batch": true.

NO-DELETION: never deletes unrelated files; only writes its own dc/<slug> dirs
and DB rows marked cn-gov:.
"""

from __future__ import annotations

import json
import os
import glob
import re
import unicodedata
import sqlite3
from pathlib import Path

PROJ = Path(__file__).resolve().parents[1]
CN_DIR = PROJ / "scripts" / "expansion" / "cn-gov"
DC_DIR = PROJ / "dc"
DB_PATH = PROJ / "datacenters.db"
SUMMARY_PATH = PROJ / "merge-output" / "cn-gov-summary.json"

MARKER = "cn_gov_batch"

# Chinese province -> English subnational name (kept consistent with existing DB).
PROVINCE_EN = {
    "北京": "Beijing", "天津": "Tianjin", "上海": "Shanghai", "重庆": "Chongqing",
    "河北": "Hebei", "山西": "Shanxi", "辽宁": "Liaoning", "吉林": "Jilin",
    "黑龙江": "Heilongjiang", "江苏": "Jiangsu", "浙江": "Zhejiang", "安徽": "Anhui",
    "福建": "Fujian", "江西": "Jiangxi", "山东": "Shandong", "河南": "Henan",
    "湖北": "Hubei", "湖南": "Hunan", "广东": "Guangdong", "广西": "Guangxi",
    "海南": "Hainan", "四川": "Sichuan", "贵州": "Guizhou", "云南": "Yunnan",
    "西藏": "Xizang", "陕西": "Shaanxi", "甘肃": "Gansu", "青海": "Qinghai",
    "宁夏": "Ningxia", "新疆": "Xinjiang", "香港": "Hong Kong", "澳门": "Macau",
}


def as_list(x):
    if x is None:
        return []
    if isinstance(x, str):
        return [x]
    return list(x)


def slugify(name):
    s = unicodedata.normalize("NFKD", name or "").encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    s = re.sub(r"-{2,}", "-", s)
    return s[:80] or "unnamed"


def prov_en(prov):
    """Map Chinese province string(s) to English subnational."""
    if not prov:
        return ""
    parts = re.split(r"[/+、和]", str(prov))
    en = []
    for p in parts:
        p = p.strip()
        if p in PROVINCE_EN:
            en.append(PROVINCE_EN[p])
    return "/".join(en) if en else str(prov)


def ensure_columns(cur):
    cols = {row[1] for row in cur.execute("PRAGMA table_info(centers)").fetchall()}
    if "country" not in cols:
        cur.execute("ALTER TABLE centers ADD COLUMN country TEXT DEFAULT 'US'")
    if "subnational" not in cols:
        cur.execute("ALTER TABLE centers ADD COLUMN subnational TEXT")


def main():
    files = sorted(glob.glob(str(CN_DIR / "*.jsonl")))
    print(f"=== Merge CN-gov ({len(files)} province files) ===")

    rows = []
    bad = 0
    for path in files:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    bad += 1
    print(f"  loaded rows: {len(rows)} (bad json: {bad})")

    projects = [r for r in rows if (r.get("name") or "").strip()]
    coverage = [r for r in rows if not (r.get("name") or "").strip()]
    print(f"  project rows: {len(projects)}, coverage rows: {len(coverage)}")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    ensure_columns(cur)

    # Cross-source dedup against existing DB, excluding previous cn-gov rows
    # (they are deleted and re-inserted below on a re-run).
    existing = set()
    for row in cur.execute("SELECT canonical_project, country, subnational, source_files FROM centers"):
        if row["source_files"] and str(row["source_files"]).startswith("cn-gov:"):
            continue
        existing.add((row["country"] or "", row["subnational"] or "", (row["canonical_project"] or "").lower()))

    fresh = []
    already = 0
    seen = set()
    dup = 0
    for r in projects:
        name = (r.get("name") or "").strip()
        prov = prov_en(r.get("province") or "")
        key = ("CN", prov, name.lower())
        if key in seen:
            dup += 1
            continue
        seen.add(key)
        if key in existing:
            already += 1
            continue
        fresh.append((r, prov))
    print(f"  after dedup: {len(fresh)} new (in-file dup: {dup}, already in DB: {already})")

    # ---- metadata files dc/<slug>/data.json (cn-gov-marked, idempotent) ----
    removed = 0
    for d in glob.glob(str(DC_DIR / "*") + "/data.json"):
        try:
            j = json.load(open(d))
        except Exception:
            continue
        if j.get(MARKER):
            p = Path(d).parent
            for f in p.iterdir():
                f.unlink()
            p.rmdir()
            removed += 1
    print(f"  removed previous cn-gov metadata dirs: {removed}")

    written = 0
    for r, prov in fresh:
        slug = f"cngov-{slugify(r.get('name'))}"
        meta = {
            "slug": slug,
            "canonical_project": r.get("name"),
            "owner": r.get("developer") or "",
            "location": {
                "city": r.get("city") or r.get("city/subnational") or "",
                "subnational": prov,
                "country": "China",
                "country_code": "CN",
            },
            "capacity_mw": r.get("capacity_mw"),
            "status": r.get("status") or "unknown",
            "evidence_date": r.get("evidence_date") or "2026-08-12",
            "evidence_grade": r.get("evidence_grade") or "U",
            "sources": as_list(r.get("source_urls")),
            "notes": (r.get("notes") or "") + (f" [province={r.get('province')}]" if r.get("province") else ""),
            MARKER: True,
        }
        out = DC_DIR / slug / "data.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
        written += 1
    print(f"  wrote {written} dc/<slug>/data.json metadata files")

    # ---- DB merge (delete previous cn-gov rows, insert fresh) ----
    cur.execute("DELETE FROM centers WHERE source_files LIKE 'cn-gov:%'")

    inserted = 0
    for r, prov in fresh:
        name = (r.get("name") or "").strip()
        city = r.get("city") or r.get("city/subnational") or ""
        src_files = "cn-gov:" + (prov or "unknown")
        cur.execute(
            """INSERT INTO centers
               (canonical_project, owner, city, county, state, capacity_mw, status,
                status_detail, year, evidence_date, evidence_grade, notes,
                existing_slug, source_files, country, subnational)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                name,
                r.get("developer") or "",
                city,
                "",
                "",
                r.get("capacity_mw"),
                r.get("status") or "unknown",
                "",
                None,
                r.get("evidence_date") or "2026-08-12",
                r.get("evidence_grade") or "U",
                (r.get("notes") or "")[:500],
                None,
                src_files,
                "CN",
                prov,
            )
        )
        inserted += 1

    conn.commit()
    total = cur.execute("SELECT COUNT(*) FROM centers").fetchone()[0]
    cn_total = cur.execute("SELECT COUNT(*) FROM centers WHERE country='CN'").fetchone()[0]
    conn.close()

    summary = {
        "files": len(files),
        "loaded_rows": len(rows),
        "project_rows": len(projects),
        "coverage_rows": len(coverage),
        "new_inserted": inserted,
        "already_in_db": already,
        "in_file_dup": dup,
        "metadata_written": written,
        "db_total_centers": total,
        "db_cn_centers": cn_total,
    }
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  INSERTED {inserted} rows")
    print(f"  DB total: {total} centers (CN: {cn_total})")
    print(f"  summary -> {SUMMARY_PATH}")


if __name__ == "__main__":
    main()
