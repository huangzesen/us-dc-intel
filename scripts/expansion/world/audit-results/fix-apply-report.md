# GRIDWATCH SQLite deterministic data-quality fixes

- **Database:** `datacenters.db`
- **Applied:** 2026-08-12 14:03:18 (local time)
- **Transaction:** One `BEGIN IMMEDIATE` / `COMMIT` transaction; committed successfully.

## Backup

- **Backup filename:** `datacenters.db.bak-20260812-140225`
- **Location:** `/Users/huangzesen/work/projects/us-dc-intel/datacenters.db.bak-20260812-140225`
- **Verification:** Exists and is non-zero (`11,190,272` bytes).

## Schema check

`PRAGMA table_info(centers);` succeeded for table `centers`. Required columns are present:

- `country` (`TEXT`)
- `subnational` (`TEXT`)
- `owner` (`TEXT`)
- `city` (`TEXT`)

## Rows changed

| Category | Rows changed | Result |
|---|---:|---|
| A. Dutch Caribbean NL->territory | 7 | Applied |
| B. Puerto Rico US->PR | 12 | Applied |
| C. Hong Kong CN->HK | 11 | Applied |
| G. KIO XAL garbled row repair | 1 | Applied |
| H. Subnational-only translation fixes | 14 | Applied |
| **Total** | **45** | **Committed** |

Every targeted rowid matched exactly one row before its statement, and every statement changed the expected number of rows. No rowid matched 0 or more than 1 rows; therefore no statement required rollback.

## Verification

The requested post-commit `SELECT rowid,country,subnational ...` returned all 45 targeted rows. Assertions passed for every specified country and subnational value. Row `3247` additionally verified as:

- `country = 'MX'`
- `subnational = 'Veracruz'`
- `owner = 'KIO Data Centers'`
- `city = 'Xalapa'`

The category totals above sum to 45 and match the verified target-row count.

## Policy rows / no-change scope

No updates were issued for policy rows `11922`, `22064`, `1454`, or `13632`; they remain **NEEDS DECISION**. No Macau, Christmas Island, or disputed-territory rows were touched. No rows were deleted or reset.
