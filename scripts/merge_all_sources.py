#!/usr/bin/env python3
"""Merge all expansion sources into unified center records + SQLite database.

Sources:
  1. scripts/expansion/county-results/batch-*.jsonl  (county-explore, ~2400 project rows)
  2. scripts/expansion/state-projects/*-projects.jsonl (state-explore, ~419 rows)
  3. scripts/discovery-candidates/candidates-*.jsonl  (discovery, 33 rows; 32 already in dc/ as disc001-032)
  4. Existing dc/<slug>/data.json  (240 baseline centers + 32 disc)

Outputs:
  - merge-output/centers.jsonl : unified canonical center records (dedup across sources)
  - datacenters.db : SQLite database with centers + sources tables (Jason 3293 requirement)
  - merge-output/summary.json : counts, dedup stats, source attribution

Idempotent: overwrites outputs on re-run. NO-DELETION: does not modify dc/ tree.
"""
import json, os, re, sys, datetime, sqlite3, glob

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COUNTY_DIR = os.path.join(PROJ, "scripts", "expansion", "county-results")
STATE_DIR = os.path.join(PROJ, "scripts", "expansion", "state-projects")
CAND_DIR = os.path.join(PROJ, "scripts", "discovery-candidates")
DC_DIR = os.path.join(PROJ, "dc")
OUT_DIR = os.path.join(PROJ, "merge-output")
DB_PATH = os.path.join(PROJ, "datacenters.db")
TODAY = "2026-08-11"

os.makedirs(OUT_DIR, exist_ok=True)

def norm(s):
    """Normalize a name for fuzzy dedup: lowercase, alnum only."""
    if not s:
        return ""
    return re.sub(r"[^a-z0-9]+", "", str(s).lower())

def load_jsonl(path):
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"  !! bad json in {path}: {e}")
    return rows

def load_all_jsonl(directory, pattern):
    rows = []
    for path in sorted(glob.glob(os.path.join(directory, pattern))):
        rows.extend(load_jsonl(path))
    return rows

def as_list(x):
    if x is None:
        return []
    if isinstance(x, str):
        return [x]
    return list(x)

def loc_city(loc):
    if isinstance(loc, dict):
        return loc.get("city") or ""
    return ""

def loc_county(loc):
    if isinstance(loc, dict):
        return loc.get("county") or ""
    return ""

def loc_state(loc):
    if isinstance(loc, dict):
        return loc.get("state") or ""
    return ""

def main():
    print(f"=== Merge all sources into unified centers + SQLite ({TODAY}) ===")

    # --- Load sources ---
    print("Loading sources...")
    county_rows = load_all_jsonl(COUNTY_DIR, "batch-*-results.jsonl")
    state_rows = load_all_jsonl(STATE_DIR, "*-projects.jsonl")
    cand_rows = load_all_jsonl(CAND_DIR, "candidates-*.jsonl")
    print(f"  county-explore: {len(county_rows)} rows")
    print(f"  state-explore:  {len(state_rows)} rows")
    print(f"  discovery:      {len(cand_rows)} rows")

    # Existing centers (240 baseline + 32 disc)
    existing = []
    for path in sorted(glob.glob(os.path.join(DC_DIR, "*", "data.json"))):
        try:
            with open(path) as f:
                d = json.load(f)
            slug = os.path.basename(os.path.dirname(path))
            d["_slug"] = slug
            d["_path"] = path
            existing.append(d)
        except Exception as e:
            print(f"  !! cannot read {path}: {e}")
    print(f"  existing dc centers: {len(existing)}")

    # Existing canonical names + norm map for matching
    existing_norm = {}
    for d in existing:
        keys = [norm(d.get("canonical_project") or d.get("project_name") or "")]
        for a in as_list(d.get("aliases")):
            keys.append(norm(a))
        for k in keys:
            if k:
                existing_norm.setdefault(k, d.get("_slug"))

    # --- Normalize county rows (project rows only) ---
    records = []
    seen = set()  # (norm_name, state, county) dedup

    def add_record(rec, src):
        nonlocal records, seen
        name = rec.get("canonical_project") or rec.get("project_name") or ""
        if not name:
            return
        state = rec.get("state") or ""
        county = rec.get("county") or ""
        key = (norm(name), norm(state), norm(county))
        if key in seen:
            # Merge sources into existing record
            for r in records:
                if (norm(r.get("canonical_project") or ""), norm(r.get("state") or ""), norm(r.get("county") or "")) == key:
                    r["sources"].extend(rec.get("sources", []))
                    r["source_files"].append(src)
                    for u in as_list(rec.get("source_urls")):
                        if u not in r["source_urls"]:
                            r["source_urls"].append(u)
                    break
            return
        seen.add(key)
        rec["sources"] = as_list(rec.get("sources"))
        rec["source_urls"] = as_list(rec.get("source_urls"))
        rec["source_files"] = [src]
        records.append(rec)

    # County rows: project_name != null and status != no_projects_found
    n_county_proj = 0
    for r in county_rows:
        if not r.get("project_name"):
            continue
        if r.get("status") == "no_projects_found":
            continue
        rec = {
            "canonical_project": r.get("project_name"),
            "aliases": as_list(r.get("aliases")),
            "owner": r.get("developer"),
            "location": {
                "city": r.get("city") or "",
                "county": (r.get("county") or "").replace(" County", ""),
                "state": r.get("state") or "",
            },
            "capacity_mw": r.get("capacity_mw"),
            "status": r.get("status"),
            "status_detail": r.get("status_detail") or "",
            "year": r.get("year"),
            "evidence_date": r.get("evidence_date") or TODAY,
            "evidence_grade": r.get("evidence_grade") or "news",
            "notes": r.get("notes") or "",
            "source_urls": as_list(r.get("source_urls")),
        }
        add_record(rec, f"county:{r.get('source')}")
        n_county_proj += 1
    print(f"  county project rows: {n_county_proj}")

    # State rows
    n_state_proj = 0
    for r in state_rows:
        if not r.get("project_name"):
            continue
        if r.get("status") == "no_projects_found":
            continue
        rec = {
            "canonical_project": r.get("project_name"),
            "aliases": as_list(r.get("aliases")),
            "owner": r.get("developer"),
            "location": {
                "city": r.get("city") or "",
                "county": (r.get("county") or "").replace(" County", ""),
                "state": r.get("state") or "",
            },
            "capacity_mw": r.get("capacity_mw"),
            "status": r.get("status"),
            "status_detail": r.get("status_detail") or "",
            "year": r.get("year"),
            "evidence_date": r.get("evidence_date") or TODAY,
            "evidence_grade": r.get("evidence_grade") or "news",
            "notes": r.get("notes") or "",
            "source_urls": as_list(r.get("source_urls")),
        }
        add_record(rec, f"state:{r.get('state')}")
        n_state_proj += 1
    print(f"  state project rows: {n_state_proj}")

    # Discovery candidates
    n_cand = 0
    for r in cand_rows:
        if not r.get("name"):
            continue
        rec = {
            "canonical_project": r.get("name"),
            "aliases": [],
            "owner": r.get("owner"),
            "location": {
                "city": loc_city(r.get("location")),
                "county": loc_county(r.get("location")),
                "state": loc_state(r.get("location")),
            },
            "capacity_mw": r.get("capacity_mw"),
            "status": r.get("status"),
            "status_detail": r.get("why_not_in_baseline") or "",
            "year": None,
            "evidence_date": r.get("evidence_date") or TODAY,
            "evidence_grade": "news" if (r.get("confidence") or "").lower() == "high" else "tracker",
            "notes": r.get("why_not_in_baseline") or "",
            "source_urls": as_list(r.get("source_urls")),
        }
        add_record(rec, "discovery")
        n_cand += 1
    print(f"  discovery rows: {n_cand}")

    print(f"\n=== Unified records: {len(records)} ===")

    # --- Match against existing centers ---
    matched = []
    unmatched = []
    for rec in records:
        name = rec.get("canonical_project") or ""
        keys = [norm(name)]
        for a in as_list(rec.get("aliases")):
            keys.append(norm(a))
        # also try owner+county+state match
        owner = norm(rec.get("owner") or "")
        county = norm(rec.get("location", {}).get("county") or "")
        state = norm(rec.get("location", {}).get("state") or "")
        slug = None
        for k in keys:
            if k and k in existing_norm:
                slug = existing_norm[k]
                break
        if not slug and owner and county and state:
            for ex in existing:
                ex_owner = norm(ex.get("owner") or "")
                ex_county = norm((ex.get("location", {}) or {}).get("county") or "")
                ex_state = norm((ex.get("location", {}) or {}).get("state") or "")
                if owner and ex_owner and (owner in ex_owner or ex_owner in owner) and ex_state == state and (not county or not ex_county or ex_county == county):
                    slug = ex.get("_slug")
                    break
        rec["existing_slug"] = slug
        if slug:
            matched.append(rec)
        else:
            unmatched.append(rec)

    print(f"  matched to existing center: {len(matched)}")
    print(f"  NEW candidates: {len(unmatched)}")

    # --- Write centers.jsonl ---
    centers_path = os.path.join(OUT_DIR, "centers.jsonl")
    with open(centers_path, "w") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"  wrote {centers_path} ({len(records)} lines)")

    # --- Build SQLite ---
    print("Building SQLite datacenters.db...")
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE centers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        canonical_project TEXT,
        owner TEXT,
        city TEXT,
        county TEXT,
        state TEXT,
        capacity_mw REAL,
        status TEXT,
        status_detail TEXT,
        year INTEGER,
        evidence_date TEXT,
        evidence_grade TEXT,
        notes TEXT,
        existing_slug TEXT,
        source_files TEXT
    )""")
    cur.execute("""CREATE TABLE sources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        center_id INTEGER,
        url TEXT,
        FOREIGN KEY(center_id) REFERENCES centers(id)
    )""")
    for rec in records:
        cur.execute(
            "INSERT INTO centers (canonical_project, owner, city, county, state, capacity_mw, status, status_detail, year, evidence_date, evidence_grade, notes, existing_slug, source_files) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (rec.get("canonical_project"), rec.get("owner"), (rec.get("location", {}) or {}).get("city"), (rec.get("location", {}) or {}).get("county"), (rec.get("location", {}) or {}).get("state"), rec.get("capacity_mw"), rec.get("status"), rec.get("status_detail"), rec.get("year"), rec.get("evidence_date"), rec.get("evidence_grade"), rec.get("notes"), rec.get("existing_slug"), json.dumps(rec.get("source_files", [])))
        )
        center_id = cur.lastrowid
        for u in as_list(rec.get("source_urls")):
            cur.execute("INSERT INTO sources (center_id, url) VALUES (?,?)", (center_id, u))
    conn.commit()

    # summary
    n_centers = cur.execute("SELECT COUNT(*) FROM centers").fetchone()[0]
    n_sources = cur.execute("SELECT COUNT(*) FROM sources").fetchone()[0]
    conn.close()
    print(f"  datacenters.db: {n_centers} centers, {n_sources} source URLs")

    summary = {
        "generated_at": datetime.datetime.utcnow().isoformat() + "Z",
        "sources": {
            "county_explore_rows": len(county_rows),
            "county_project_rows": n_county_proj,
            "state_explore_rows": len(state_rows),
            "state_project_rows": n_state_proj,
            "discovery_rows": n_cand,
            "existing_centers": len(existing),
        },
        "unified_records": len(records),
        "matched_existing": len(matched),
        "new_candidates": len(unmatched),
        "sqlite": {"centers": n_centers, "sources": n_sources},
        "centers_jsonl": centers_path,
        "db_path": DB_PATH,
    }
    with open(os.path.join(OUT_DIR, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print("\n=== SUMMARY ===")
    print(json.dumps(summary, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
