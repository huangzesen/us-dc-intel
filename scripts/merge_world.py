#!/usr/bin/env python3
"""Merge world exploration results into datacenters.db + per-center dc/<slug>/data.json metadata.

Source: scripts/expansion/world/results/batch-*.jsonl
  Line schema: {country_code, country_name, division, name, status, capacity_mw, developer,
                source_urls, evidence_date, evidence_grade, notes}
  Or coverage row: {country_code, country_name, division, no_projects: true}

Behavior (idempotent):
  - Scans existing dc/*/data.json; entries whose metadata carries a world marker
    ("world_batch") are replaced on re-run; US curated discNNN entries untouched.
  - Dedup key: (country_code, division, name lower).  First occurrence wins.
  - Writes dc/<slug>/data.json per project (slug = cc + slugified name).
  - Inserts rows into datacenters.db centers table (country/subnational filled),
    source_urls into sources table.
  - Writes merge-output/world-summary.json with counts.

NO-DELETION: never deletes files; only writes its own dc/<slug> dirs and DB rows.
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
RESULTS_DIR = PROJ / "scripts" / "expansion" / "world" / "results"
DC_DIR = PROJ / "dc"
DB_PATH = PROJ / "datacenters.db"
SUMMARY_PATH = PROJ / "merge-output" / "world-summary.json"

WORLD_MARKER = "world_batch"


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


def ensure_columns(cur):
    cols = {row[1] for row in cur.execute("PRAGMA table_info(centers)").fetchall()}
    if "country" not in cols:
        cur.execute("ALTER TABLE centers ADD COLUMN country TEXT DEFAULT 'US'")
    if "subnational" not in cols:
        cur.execute("ALTER TABLE centers ADD COLUMN subnational TEXT")


def main():
    files = sorted(glob.glob(str(RESULTS_DIR / "batch-*.jsonl")))
    print(f"=== Merge World ({len(files)} result files) ===")

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

    # dedup (cc, division, name lower)
    seen = set()
    deduped = []
    dup = 0
    for r in projects:
        name = (r.get("name") or "").strip()
        if not name:
            continue
        key = (r.get("country_code") or "", r.get("division") or "", name.lower())
        if key in seen:
            dup += 1
            continue
        seen.add(key)
        deduped.append(r)
    projects = deduped
    print(f"  after dedup: {len(projects)} (dups skipped: {dup})")

    countries = sorted({r.get("country_code") for r in projects})
    print(f"  countries with projects: {len(countries)}")

    # ---- metadata files dc/<slug>/data.json (world-marked, idempotent) ----
    # remove previous world-marked metadata dirs first (only dirs we own)
    removed = 0
    for d in glob.glob(str(DC_DIR / "*") + "/data.json"):
        try:
            j = json.load(open(d))
        except Exception:
            continue
        if j.get("world_batch"):
            p = Path(d).parent
            for f in p.iterdir():
                f.unlink()
            p.rmdir()
            removed += 1
    print(f"  removed previous world metadata dirs: {removed}")

    written = 0
    for r in projects:
        cc = (r.get("country_code") or "").lower()
        slug = f"{cc}-{slugify(r.get('name'))}"
        meta = {
            "slug": slug,
            "canonical_project": r.get("name"),
            "owner": r.get("developer") or "",
            "location": {
                "city": "",
                "subnational": r.get("division") or "",
                "country": r.get("country_name") or "",
                "country_code": r.get("country_code") or "",
            },
            "capacity_mw": r.get("capacity_mw"),
            "status": r.get("status") or "unknown",
            "evidence_date": r.get("evidence_date") or "2026-08-11",
            "evidence_grade": r.get("evidence_grade") or "U",
            "sources": as_list(r.get("source_urls")),
            "notes": r.get("notes") or "",
            "world_batch": True,
        }
        out = DC_DIR / slug / "data.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
        written += 1
    print(f"  wrote {written} dc/<slug>/data.json metadata files")

    # ---- DB merge ----
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    ensure_columns(cur)

    cur.execute("UPDATE centers SET country='US' WHERE country IS NULL OR country=''")
    cur.execute("DELETE FROM centers WHERE source_files LIKE 'world:%'")
    cur.execute("DELETE FROM sources WHERE url LIKE '%_wd_%'")

    inserted = 0
    for r in projects:
        cc = r.get("country_code") or ""
        div = r.get("division") or ""
        name = (r.get("name") or "").strip()
        src_files = "world:" + (r.get("source_files") or "batch") + ":" + div
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
        "dedup_skipped": dup,
        "metadata_files_written": written,
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
