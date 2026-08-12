# US data-quality fix plan — GRIDWATCH (read-only investigation + plan)

Generated: 2026-08-12
Scope: read-only. No DB row, code file, or export artifact was modified. This file is the only artifact written.

- DB: `datacenters.db` (SQLite), table `centers`
- Column mapping used below (the DB schema differs from the generic audit wording):
  - "name" = `canonical_project`
  - "developer" = `owner`
  - "subnational" = `subnational`
  - "rowid" = `id` (the table has `id INTEGER PRIMARY KEY AUTOINCREMENT`, so `id` is the SQLite rowid alias)

---

## Finding 1 — US → Puerto Rico mislocation

All facilities coded `country='US'` but actually located in Puerto Rico share one signature: `state='PR'` (and `subnational IS NULL`, `city`/`county` carry Puerto Rico municipality names).

There are **22 rows** (ids 1615–1636). The earlier 30-shard audit (`audit-results/CONSOLIDATED.md` §B) only flagged 12 of these (4 MISLOCATED + 8 UNSURE); this deeper query shows the remaining 10 rows (1615–1621, 1623, 1633, 1636) were missed by that shard sample but have exactly the same defect. All 22 are Puerto Rico and should be recoded to `country='PR'`.

Exact rows (`id | canonical_project | owner | subnational | country` → correct country `PR`):

| id | name (`canonical_project`) | developer (`owner`) | subnational | country | correct |
|---|---|---|---|---|---|
| 1615 | Arecibo Observatory data center | Arecibo Observatory / University of Central Florida consortium | NULL | US | PR |
| 1616 | Engine-4 Data Infrastructure | Engine-4 Foundation | NULL | US | PR |
| 1617 | Puerto Rico AI Research Institute GPU cluster center | Engine-4 Foundation | NULL | US | PR |
| 1618 | Smart Networks Data Center | Smart Networks LLC | NULL | US | PR |
| 1619 | HUB787 Data Center | HUB Advanced Networks LLC | NULL | US | PR |
| 1620 | HRCOM | HRcom Inc. | NULL | US | PR |
| 1621 | FiberX Data Center | FiberX | NULL | US | PR |
| 1622 | Neptuno Data Center | Neptuno Media, Inc. | NULL | US | PR |
| 1623 | Microsoft Guaynabo | Microsoft | NULL | US | PR |
| 1624 | Carter Validus Mission Critical REIT PR Data Center | Digital Realty | NULL | US | PR |
| 1625 | Claro (PR) | Claro | NULL | US | PR |
| 1626 | HUB939 | HUB Advanced Networks | NULL | US | PR |
| 1627 | Data@ccess Ponce secondary colocation site | Data@ccess / Data Access Puerto Rico | NULL | US | PR |
| 1628 | Seabase Puerto Rico subsea AI hub evaluation - Ponce | Seabase | NULL | US | PR |
| 1629 | Data@ccess San Juan / San Juan II / Santurce colocation sites | Data@ccess / Data Access Puerto Rico | NULL | US | PR |
| 1630 | EdgeUno SJU1 San Juan Data Center | EdgeUno, Inc. | NULL | US | PR |
| 1631 | Netwave Data Center | Netwave Equipment Corporation | NULL | US | PR |
| 1632 | Critical Hub DataCenter | Critical Hub Networks / Optico Fiber Business | NULL | US | PR |
| 1633 | Continent 8 Puerto Rico data center / PoP | Continent 8 Technologies | NULL | US | PR |
| 1634 | Municipality of San Juan Health Data Center Project | Municipality of San Juan | NULL | US | PR |
| 1635 | Municipality of San Juan Municipal Tower Data Center Project | Municipality of San Juan | NULL | US | PR |
| 1636 | Seabase Puerto Rico subsea AI hub evaluation - San Juan | Seabase | NULL | US | PR |

Supporting evidence for every row: `state='PR'`, `county` ends in `Municipio` (Arecibo/Bayamón/Caguas/Carolina/Guaynabo/Humacao/Ponce/San Juan), `city` is a PR municipality, and several names/owners mention Puerto Rico (`Puerto Rico AI Research Institute`, `Data Access Puerto Rico`, `Continent 8 Puerto Rico`, `Seabase Puerto Rico`, `Carter Validus ... PR`, `Claro (PR)`).

### US → US-territory mislocation (Guam GU / USVI VI / American Samoa AS / Northern Mariana MP)

**None found.** Checks for `country='US'` with `state IN ('GU','VI','AS','MP')`, with territory city names, with territory county names, and with territory keywords in `canonical_project`/`owner`/`notes` all returned zero true positives. The one candidate hit, id 2331 (`Unnamed St. Croix County / Hammond-area data center concern`, `state='WI'`, `county='St. Croix'`), is St. Croix County, Wisconsin — correctly US, not the US Virgin Islands. The DB already codes those territories separately (`GU`=22 rows, `VI`=1, `AS`=4, `MP`=5), so no US→territory recode is needed.

---

## Finding 2 — US coordinate nulls / (0,0) risk

### What resolves correctly today

- `COUNTRY_COORDS` (`scripts/export_astro_data.py:263-320`) **does** contain `"US"` at line 314 (`[39.8283, -98.5795]`), plus `"PR"` (line 307) and `"VI"` (line 319). So the US country-level marker is not null.
- `STATE_COORDS` (lines 322-375) and `STATE_LAYOUT` (lines 80-133) both cover the same 51 keys: 50 states + DC + PR. `STATE_NAMES` (lines 22-75) has no key missing from `STATE_COORDS`. Therefore the US state cartogram (`states`, built at lines 730-746) and every US state subnational (`subnational_coord` short-circuit at lines 497-505) resolve to a real coordinate.
- A read-only simulation over all 2,731 `country='US'` rows confirms **0** US rows resolve `subnational_coord('US', …)` to null. All 50 states + DC + PR subnational labels hit `STATE_COORDS`.

### What is broken (the US-territory coordinate gaps)

Three US territories are stored as **separate country codes** in the DB and are **missing from `COUNTRY_COORDS`**:

| code | DB rows | `COUNTRY_COORDS[code]` | country-level marker |
|---|---|---|---|
| GU (Guam) | 22 | missing | `[None, None]` → plots at (0,0) |
| AS (American Samoa) | 4 | missing | `[None, None]` → plots at (0,0) |
| MP (Northern Mariana Islands) | 5 | missing | `[None, None]` → plots at (0,0) |
| VI (US Virgin Islands) | 1 | present (line 319) | OK |
| PR (Puerto Rico) | 25 (+22 after Finding 1) | present (line 307) | OK |

Why: `country_coord()` (`export_astro_data.py:428-429`) returns `COUNTRY_COORDS.get(code.upper(), [None, None])`, and the country-level marker in the export uses it directly at line 783 (`lat, lng = country_coord(code)`). The `coord-results/*.jsonl` loader (`load_subnational_coords`, lines 435-458) only supplies **subnational** coordinates and is never consulted for the country-level bubble. It happens to contain exactly one entry per territory (`('GU','Guam')`, `('AS','American Samoa')`, `('MP','Northern Mariana Islands')`), which means the territory *subnational* bubbles resolve fine — but the territory *country* bubble still falls through to `[None, None]`.

Frontend amplification: `astro/src/pages/index.astro:1744` —

```js
const hasCoord = item => Number.isFinite(Number(item?.lat)) && Number.isFinite(Number(item?.lng));
```

`Number(null) === 0`, so a null coordinate passes `hasCoord`, and the marker is placed at `[Number(item.lat), Number(item.lng)]` = `[0, 0]` (lines 1920-1924) — the Gulf of Guinea ("in Africa" symptom), exactly as documented for CN in `audit-results/coordinate-issue.md`.

### Bottom line

- No US **state** (and not PR/VI) plots at (0,0).
- Three US **territories** — **GU, AS, MP** — have a country-level coordinate gap and would plot at (0,0) until their codes are added to `COUNTRY_COORDS`.
- US, PR, and VI are safe today.

---

## Section A — Exact SQL for the PR recode

`id` is the rowid (`INTEGER PRIMARY KEY AUTOINCREMENT`). Required fix — recode the 22 US→PR rows:

```sql
UPDATE centers SET country='PR' WHERE id IN (
  1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624,
  1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634,
  1635, 1636
);
```

No territory recode is needed (no US→GU/VI/AS/MP mislocated rows were found).

Optional harmonization (recommended for consistency with the 25 existing `country='PR'` rows, which store `subnational` = municipality and `state=''`): also set `state=''` and copy the municipality into `subnational` for the 22 rows:

```sql
UPDATE centers SET
  state = '',
  subnational = CASE id
    WHEN 1615 THEN 'Arecibo'
    WHEN 1616 THEN 'Bayamon'
    WHEN 1617 THEN 'Bayamon'
    WHEN 1618 THEN 'Caguas'
    WHEN 1619 THEN 'Carolina'
    WHEN 1620 THEN 'Carolina'
    WHEN 1621 THEN 'Guaynabo'
    WHEN 1622 THEN 'Guaynabo'
    WHEN 1623 THEN 'Guaynabo'
    WHEN 1624 THEN 'Guaynabo'
    WHEN 1625 THEN 'Guaynabo'
    WHEN 1626 THEN 'Humacao'
    WHEN 1627 THEN 'Ponce'
    WHEN 1628 THEN 'Ponce'
    WHEN 1629 THEN 'San Juan'
    WHEN 1630 THEN 'San Juan'
    WHEN 1631 THEN 'San Juan'
    WHEN 1632 THEN 'San Juan'
    WHEN 1633 THEN 'San Juan'
    WHEN 1634 THEN 'San Juan'
    WHEN 1635 THEN 'San Juan'
    WHEN 1636 THEN 'San Juan'
  END
WHERE id BETWEEN 1615 AND 1636;
```

(If only the required country recode is applied, these rows still export safely: `subnational` stays empty, `state='PR'` maps to the `Puerto Rico` label, and `subnational_coord('PR','Puerto Rico')` falls back to `COUNTRY_COORDS['PR']` — no (0,0). The optional step is purely for label/grouping consistency.)

---

## Section B — Code fixes for US coordinates

### B1. Add the missing US-territory country centroids to `COUNTRY_COORDS`

File: `scripts/export_astro_data.py`, dict at lines 263-320 (US already at 314, PR at 307, VI at 319).

Add three entries, reusing the centroids already present in `scripts/expansion/world/coord-results/*.jsonl` so the two sources agree:

```python
    "GU": [13.475, 144.75],       # Guam (matches coord-results 'Guam')
    "AS": [-14.275, -170.702],    # American Samoa (matches coord-results 'American Samoa')
    "MP": [15.213, 145.755],      # Northern Mariana Islands (matches coord-results 'Northern Mariana Islands')
```

Place them alphabetically inside the dict (GU after `"GS"`, AS after `"AR"`, MP after `"MQ"`). This alone fixes the GU/AS/MP country-level (0,0) markers, because `country_coord()` (lines 428-429) and the `countries` build (line 783) will then return real values.

### B2. Subnational-coordinate matching

File: `scripts/export_astro_data.py`, `subnational_coord` at lines 497-505.

No US-state matching change is required: for `country == 'US'`, the function already short-circuits through `state_abbr()` → `STATE_COORDS` (lines 498-501), and `STATE_COORDS` (322-375) covers every `STATE_NAMES` key (all 50 states + DC + PR). US state subnationals never reach `load_subnational_coords()` and never null out.

For the territories, the correct fix is B1 (country-level entries), not a subnational-key change, because the failing lookup is `country_coord()` at line 783 rather than the subnational join. Optional hardening (not US-specific, mirrors the CN fix): in `load_subnational_coords` (lines 435-458), normalize the key to uppercase — `coords[(item.get("country_code") or "").upper(), item.get("division") or ""]` — and in `subnational_coord` (line 502) add a `division.split(" - ")[0]` prefix fallback so province-only labels can still match `Province - City` records. This is relevant for CN, not for US/territories.

### B3. `hasCoord` null-guard

File: `astro/src/pages/index.astro:1744`.

Replace:

```js
const hasCoord = item => Number.isFinite(Number(item?.lat)) && Number.isFinite(Number(item?.lng));
```

with a version that rejects null/undefined before coercion:

```js
const hasCoord = item => item?.lat != null && item?.lng != null && Number.isFinite(Number(item.lat)) && Number.isFinite(Number(item.lng));
```

Optional belt-and-suspenders at the marker site (`index.astro:1919-1920`): skip the item when either coordinate is null, e.g. `if (item.lat == null || item.lng == null) return;` before building `latlng`. The `hasCoord` fix alone is sufficient because every marker source is filtered through `hasCoord` (lines 1866-1882).

---

## Section C — Verification checklist

1. PR recode applied:
   - `SELECT COUNT(*) FROM centers WHERE country='US' AND state='PR';` → **0**
   - `SELECT COUNT(*) FROM centers WHERE country='PR';` → **47** (25 existing + 22 recoded)
   - `SELECT id FROM centers WHERE country='PR' AND id BETWEEN 1615 AND 1636 ORDER BY id;` → returns all 22 ids
2. No US→territory mislocation remains:
   - `SELECT COUNT(*) FROM centers WHERE country='US' AND state IN ('GU','VI','AS','MP');` → **0**
   - `SELECT COUNT(*) FROM centers WHERE country='US' AND county LIKE '%Municipio%';` → **0**
3. Coordinate gap closed (after B1):
   - Confirm `COUNTRY_COORDS` has non-null entries for `US`, `PR`, `VI`, `GU`, `AS`, `MP`.
   - Rerun `LINGTAI_RUNTIME_PYTHON scripts/export_astro_data.py` (this writes the JSON — run only after code/DB changes are approved), then check `astro/src/data/datacenters.json` for `"lat":null` among country-level entries: **none** for US/PR/VI/GU/AS/MP.
4. Frontend null-guard (after B3):
   - Confirm no country/state/subnational marker renders at `[0, 0]`; `hasCoord(null-lat)` must return `false`.
5. Sanity on the 22-row audit gap: the earlier 30-shard audit covered 12 of 22 PR rows; the 10 additional rows (1615-1621, 1623, 1633, 1636) are included in the Section A `WHERE id IN (...)` list above.
