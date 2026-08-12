# Coordinate mapping audit — GRIDWATCH "China data centers plotted in Africa"

**Date:** 2026-08-12
**Scope:** read-only audit of `scripts/expansion/world/coord-results/*.jsonl` and the
coordinate join/render path in `scripts/export_astro_data.py` + `astro/src/pages/index.astro`.

## TL;DR

1. **The coordinate records themselves are clean.** No `coord-results/*.jsonl` record for
   `country_code=CN` resolves outside China. Zero CN divisions have a lat/lng in Africa or on
   any other wrong continent.
2. **The "plotted in Africa" symptom is a null-coordinate fallback, not a bad coordinate.**
   When a facility's subnational string does not exactly match a `coord-results` division (and
   for every non-Americas country marker), `country_coord()` returns `[None, None]` because
   `COUNTRY_COORDS` only contains Americas entries.
3. The export then writes `"lat": null, "lng": null`, and the frontend's `hasCoord()` coerces
   `null -> 0` via `Number(null) === 0`, so the marker is rendered at **(0, 0) — the Gulf of
   Guinea, Atlantic Ocean, immediately off the coast of West Africa** (visually "in Africa").

Blast radius: **186 of 241 countries** have a null country-level coordinate, and **30 China
subnationals** have null coordinates. China is the only country with null *subnational*
coordinates because its DB rows use province-only labels (e.g. `Xinjiang`) that never match the
`Province - City` format used in `coord-results`.

---

## 1. How coordinates are stored and joined

### Coordinate record shape (`scripts/expansion/world/coord-results/batch-*.jsonl`)

10 shards, 2,513 records total, all with `lat` and `lng` present.

```json
{"country_code": "CN", "division": "Anhui - Anqing Shi", "lat": 30.531, "lng": 117.046, "confidence": "high", "note": "Anqing city center (Yingjiang)"}
```

### Loader (`scripts/export_astro_data.py:435-458`)

`load_subnational_coords()` builds a dict keyed on an **exact tuple match**:

```python
coords[(item.get("country_code") or "", item.get("division") or "")] = [float(lat), float(lng)]
```

So the join key is `(country_code.upper(), division)` — exact string equality, no
normalization, no fuzzy fallback.

### Lookup + fallback chain (`scripts/export_astro_data.py:497-505`)

```python
def subnational_coord(country, name):
    if country == "US":
        ...STATE_COORDS...
    coord = load_subnational_coords().get((country.upper(), name))
    if coord:
        return coord
    return country_coord(country)      # <-- fallback
```

`country_coord(code)` (`:428-429`) is `COUNTRY_COORDS.get(code.upper(), [None, None])`.
`COUNTRY_COORDS` (`:263-350`) contains **only Americas country/territory codes** (AI, AG, AR,
AW, …, US, UY, VC, VE, VG, VI). It has **no** CN, IN, GB, DE, JP, etc.

Consequence: for any non-Americas country (and any non-matching subnational), the fallback is
`[None, None]`, and the export writes `lat: null, lng: null` (lines 775-776 and 783-797).

### Frontend (`astro/src/pages/index.astro:1744`)

```js
const hasCoord = item => Number.isFinite(Number(item?.lat)) && Number.isFinite(Number(item?.lng));
```

`Number(null) === 0` and `Number.isFinite(0) === true`, so a `null` coordinate **passes** the
"has a coordinate" test instead of being filtered out. Markers are then placed at
`[Number(item.lat), Number(item.lng)]` = `[0, 0]` (lines 1920-1924).

---

## 2. Coordinate-record audit (the part the task suspected)

Checks run against all 2,513 records in `coord-results/*.jsonl`:

| Check | Result |
|---|---|
| Records with missing `lat`/`lng` | **0** |
| CN records outside China bbox (lat 18–54, lng 73–135) | **0** (of 307 CN records) |
| `(country_code, division)` keys with conflicting lat/lng duplicates | **0** |
| Nearest-neighbor outlier > 2000 km within the same country | 2 (Kiribati only — legitimate antimeridian spread: Gilbert Is. at 173E vs Line Is. at 157W) |

**Conclusion:** there is no CN division (and no other country's division) in `coord-results`
that resolves to a wrong continent. The suspected coordinate mapping is not the direct cause.

---

## 3. The actual bug and where the markers land

### 3a. Country-level markers

`astro/src/data/datacenters.json` currently contains **186 / 241 countries with
`lat: null, lng: null`** (every non-Americas country, since `COUNTRY_COORDS` lacks them).
On the world map view these render at (0, 0).

### 3b. China subnational markers

China has **30 / 337 subnationals with `lat: null, lng: null`**, all because the DB
`subnational` value is a province-only string (or a city stored without the `Province - City`
prefix) and therefore misses the exact-match lookup. These 30 entries, sorted by capacity,
are the "China datacenters in Africa" markers:

| Country | Subnational (DB label) | facilities | capacity_mw | rendered lat/lng |
|---|---|---:|---:|---|
| CN | Xinjiang | 15 | 4050.1 | null → (0, 0) |
| CN | Beijing | 11 | 2187.5 | null → (0, 0) |
| CN | Hong Kong | 18 | 1878.5 | null → (0, 0) |
| CN | Zhejiang | 14 | 1823.0 | null → (0, 0) |
| CN | Heilongjiang | 12 | 1777.5 | null → (0, 0) |
| CN | Guangdong | 6 | 1702.2 | null → (0, 0) |
| CN | Gansu | 9 | 1542.6 | null → (0, 0) |
| CN | Fujian | 9 | 1486.2 | null → (0, 0) |
| CN | Shaanxi | 10 | 1398.3 | null → (0, 0) |
| CN | Tianjin | 8 | 1336.6 | null → (0, 0) |
| CN | Hunan | 10 | 1328.6 | null → (0, 0) |
| CN | Liaoning | 9 | 1313.8 | null → (0, 0) |
| CN | Qinghai | 10 | 1213.0 | null → (0, 0) |
| CN | Hebei | 6 | 1085.6 | null → (0, 0) |
| CN | Sichuan | 8 | 1004.8 | null → (0, 0) |
| CN | Yunnan | 8 | 973.1 | null → (0, 0) |
| CN | Jiangsu | 6 | 897.0 | null → (0, 0) |
| CN | Shandong | 6 | 715.6 | null → (0, 0) |
| CN | Jiangxi | 6 | 698.0 | null → (0, 0) |
| CN | Chongqing | 5 | 690.6 | null → (0, 0) |
| CN | Xizang (Tibet) | 4 | 685.6 | null → (0, 0) |
| CN | Hubei | 9 | 657.2 | null → (0, 0) |
| CN | Hainan | 5 | 655.8 | null → (0, 0) |
| CN | Ningxia | 3 | 514.2 | null → (0, 0) |
| CN | Henan | 5 | 469.2 | null → (0, 0) |
| CN | Shanxi | 5 | 395.4 | null → (0, 0) |
| CN | Guangxi | 3 | 344.9 | null → (0, 0) |
| CN | Macau | 2 | 342.8 | null → (0, 0) |
| CN | Jilin | 2 | 342.8 | null → (0, 0) |
| CN | Shanghai | 3 | 93.2 | null → (0, 0) |

Every one of these is a **real** Chinese subnational whose DB label is `Province`-only and thus
has no `coord-results` key (`coord-results` uses `Province - City`, e.g. `Xinjiang - Urumqi Shi`).
They all resolve through `country_coord("CN") -> [None, None] -> (0, 0)`.

### 3c. Where (0, 0) actually is

- Latitude 0.000°, longitude 0.000° = **Gulf of Guinea, Atlantic Ocean**.
- Nearest land: roughly 600 km south of Accra, Ghana / west of Nigeria's Niger Delta — the
  west coast of Africa. On a world map this cluster appears on the African side of the
  prime-meridian/equator intersection, which is exactly the reported symptom.

---

## 4. Root-cause summary (three stacked defects)

1. **`COUNTRY_COORDS` is Americas-only** (`export_astro_data.py:263-350`). `country_coord()`
   has no entry for CN (or any EMEA/APAC country), so its fallback is `[None, None]` instead
   of a country centroid.
2. **Exact-match subnational join** (`load_subnational_coords` keyed on `(country, division)`)
   has no normalization, so China's province-only DB labels (`Xinjiang`, `Beijing`, …) fail to
   match `coord-results`'s `Province - City` keys and fall through to the null fallback.
3. **Frontend `hasCoord()` coerces `null` to `0`** (`index.astro:1744`), so null-coordinate
   items are plotted at (0, 0) instead of being dropped or snapped to a country centroid.

## 5. Suggested fixes (for the follow-up, not applied here)

- Add country centroids for all non-Americas countries to `COUNTRY_COORDS` (or derive them
  from `coord-results` as a country mean when a code is missing).
- In `subnational_coord`, add a normalized/secondary lookup: strip to the province prefix
  (`division.split(" - ")[0]`) or `startswith(country + " - " + name)` fallback so `Xinjiang`
  matches `Xinjiang - Urumqi Shi`.
- In `index.astro`, make `hasCoord` reject `null`/`undefined` before `Number()`
  (e.g. `item?.lat != null && Number.isFinite(Number(item.lat))`), and drop or re-anchor items
  that lack coordinates.
