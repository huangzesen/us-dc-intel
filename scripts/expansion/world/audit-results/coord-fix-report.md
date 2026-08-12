# GRIDWATCH coordinate fallback fix report

**Date:** 2026-08-12
**Scope:** local code edit, export, Astro build, and coordinate verification only. No deployment or push was performed.

## Exact source changes

### `scripts/export_astro_data.py`

1. **Country-level fallback (`COUNTRY_COORDS` / `country_coord`)**
   - **Before:** `COUNTRY_COORDS` (old lines 263–320) contained the existing Americas anchors only; `country_coord()` (old line 428–429) returned `COUNTRY_COORDS.get(code.upper(), [None, None])`, so missing countries serialized as null coordinates.
   - **After:** added the required coord-results-aligned explicit territory anchors in `COUNTRY_COORDS`:
     - line 267: `AS: [-14.275, -170.702]`
     - line 293: `GU: [13.475, 144.75]`
     - line 303: `MP: [15.213, 145.755]`
     `country_coord()` is now lines 435–441: it uses an explicit table entry first, then retrieves a data-derived `__country_centroid__` from the coord-results loader, retaining `[None, None]` only when no source coordinate exists.
   - **Derivation:** lines 444–493 now aggregate every valid coord-results record by uppercased country code and compute mean latitude/longitude. The resulting country centroid is cached without hardcoding a large country table.

2. **Subnational coordinate matching (`load_subnational_coords` / `subnational_coord`)**
   - **Before:** old loader lines 435–458 stored only an exact `(country_code, division)` key with the source country code/name unchanged; old `subnational_coord()` lines 497–505 performed only an exact tuple lookup. Province-only DB labels such as `Xinjiang` therefore missed `Xinjiang - Urumqi Shi` records.
   - **After:** loader lines 444–493 normalize country codes to uppercase and division names by trimming, validate numeric coordinates, and add a secondary prefix key at lines 473–477 using the part before `" - "`. Thus `Xinjiang` resolves to the first corresponding `Xinjiang - ...` coordinate. `subnational_coord()` lines 534–544 normalizes its inputs before exact/secondary lookup and falls back to the derived country centroid.

### `astro/src/pages/index.astro`

3. **Frontend null guard (line 1744)**
   - **Before:**
     ```js
     const hasCoord = item => Number.isFinite(Number(item?.lat)) && Number.isFinite(Number(item?.lng));
     ```
     `Number(null)` is `0`, so null values passed the guard and rendered at `(0, 0)`.
   - **After:**
     ```js
     const hasCoord = item => item?.lat != null && item?.lng != null && Number.isFinite(Number(item.lat)) && Number.isFinite(Number(item.lng));
     ```
     Null/undefined values are rejected before numeric coercion.

## Rebuild and verification

Commands run successfully:

```text
python3 scripts/export_astro_data.py
  wrote astro/src/data/datacenters.json (3,928,759 bytes)
  wrote astro/src/data/dc-metadata.json (3,781,820 bytes, 2860 entries)

cd astro && npm run build
  Astro static build completed: 1 page built, `astro/dist/index.html`
```

Post-export assertions:

- 241 country markers: **0** non-finite/null coordinates; **0** exact `(0,0)` pairs.
- 2,869 subnational markers: **0** non-finite/null coordinates; **0** exact `(0,0)` pairs.
- Derived China country centroid: `CN -> [32.677687296416956, 111.81682410423446]`.
- Required territory coordinates: `GU -> [13.475, 144.75]`, `AS -> [-14.275, -170.702]`, `MP -> [15.213, 145.755]`.
- Prefix lookup: `subnational_coord('CN', 'Xinjiang') -> [47.845, 88.14]`.
- Grep over `astro/src/data/datacenters.json` and `astro/dist`: no `"lat":null`/`"lng":null` and no exact `(0,0)` coordinate pair (grep exit 1, meaning no matches). Individual zero longitude values are legitimate coordinates and are not `(0,0)`.
- Built `astro/dist/index.html`: 0 null-coordinate literals and 0 exact `(0,0)` pairs.
- `python3 -m py_compile scripts/export_astro_data.py` passed; `git diff --check` passed for edited source/generated files.

The working tree had pre-existing modifications to `datacenters.db` and other unrelated/untracked paths before this task; none were reset or deleted. The required export regenerated the tracked Astro data artifacts. No deploy, external write, or git push was performed.
