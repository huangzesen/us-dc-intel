#!/usr/bin/env python3
"""Merge Americas exploration results into datacenters.db (country + subnational dimension).

Source: scripts/expansion/americas/results/batch-*.jsonl
  Line schema: {country_code, country_name, division, name, status, capacity_mw, developer,
                source_urls, evidence_date, evidence_grade, notes}
  Or coverage row: {country_code, country_name, division, no_projects: true}

Behavior:
  - Adds country/subnational columns to centers (idempotent ALTER).
  - INSERTs project rows (no_projects != true) with country_code/subnational filled.
  - Marks existing US rows country='US'.
  - Adds source URLs into sources table.
  - Writes merge-output/americas-summary.json with counts.

Idempotent: re-running replaces only the americas-derived rows (source_files LIKE 'americas:%').
NO-DELETION: never deletes files; only rewrites DB rows it owns.
"""

from __future__ import annotations

import json
import os
import glob
import sqlite3
from pathlib import Path

PROJ = Path(__file__).resolve().parents[1]
RESULTS_DIR = PROJ / "scripts" / "expansion" / "americas" / "results"
DB_PATH = PROJ / "datacenters.db"
SUMMARY_PATH = PROJ / "merge-output" / "americas-summary.json"


def as_list(x):
    if x is None:
        return []
    if isinstance(x, str):
        return [x]
    return list(x)


def ensure_columns(cur):
    cols = {row[1] for row in cur.execute("PRAGMA table_info(centers)").fetchall()}
    if "country" not in cols:
        cur.execute("ALTER TABLE centers ADD COLUMN country TEXT DEFAULT 'US'")
    if "subnational" not in cols:
        cur.execute("ALTER TABLE centers ADD COLUMN subnational TEXT")


def main():
    files = sorted(glob.glob(str(RESULTS_DIR / "batch-*.jsonl")))
    print(f"=== Merge Americas ({len(files)} result files) ===")

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

    projects = [r for r in rows if not r.get("no_projects")]
    no_proj = [r for r in rows if r.get("no_projects")]
    print(f"  project rows: {len(projects)}, no_project rows: {len(no_proj)}")

    countries = sorted({r.get("country_code") for r in projects})
    print(f"  countries with projects: {len(countries)} {countries}")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    ensure_columns(cur)

    # Mark existing rows as US
    cur.execute("UPDATE centers SET country='US' WHERE country IS NULL OR country=''")

    # Remove previous americas-derived rows (idempotent re-merge)
    cur.execute("DELETE FROM centers WHERE source_files LIKE 'americas:%'")
    cur.execute("DELETE FROM sources WHERE url LIKE '%_am_%'")

    inserted = 0
    seen_names = set()
    for r in projects:
        name = (r.get("name") or "").strip()
        if not name:
            continue
        cc = r.get("country_code") or ""
        div = r.get("division") or ""
        # dedup same (cc, div, name)
        key = (cc, div, name.lower())
        if key in seen_names:
            continue
        seen_names.add(key)

        src_files = "americas:" + (r.get("source_files") or "batch") + ":" + div
        cur.execute(
            """INSERT INTO centers
               (canonical_project, owner, city, county, state, capacity_mw, status,
                status_detail, year, evidence_date, evidence_grade, notes,
                existing_slug, source_files, country, subnational)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                name,
                r.get("developer") or "",
                "",
                "",
                None,
                r.get("capacity_mw"),
                r.get("status") or "unknown",
                "",
                None,
                r.get("evidence_date") or "2026-08-11",
                r.get("evidence_grade") or "",
                r.get("notes") or "",
                None,
                src_files,
                cc,
                div,
            ),
        )
        center_id = cur.lastrowid
        for u in as_list(r.get("source_urls")):
            if not u:
                continue
            cur.execute("INSERT INTO sources (center_id, url) VALUES (?,?)", (center_id, u))
        inserted += 1

    conn.commit()

    # Summary stats
    total = cur.execute("SELECT COUNT(*) FROM centers").fetchone()[0]
    per_country = cur.execute(
        "SELECT country, COUNT(*) n, COALESCE(SUM(capacity_mw),0) mw FROM centers GROUP BY country ORDER BY n DESC"
    ).fetchall()
    summary = {
        "generated_date": "2026-08-11",
        "files": len(files),
        "loaded_rows": len(rows),
        "project_rows": len(projects),
        "no_project_rows": len(no_proj),
        "inserted": inserted,
        "total_centers": total,
        "countries_with_projects": len(countries),
        "per_country": [
            {"country": r["country"], "facilities": r["n"], "capacity_mw": round(r["mw"], 1)}
            for r in per_country
        ],
    }
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  wrote {SUMMARY_PATH}")
    print(f"  total centers in DB: {total}")
    for r in per_country:
        print(f"    {r['country']}: {r['n']} facilities, {round(r['mw'],1)} MW")

    conn.close()


if __name__ == "__main__":
    main()
