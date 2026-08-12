# PG · Country Anatomy

Datacenter-country knowledge layer for Papua New Guinea (PG).

## Files

| File | Status | Notes |
|---|---|---|
| Country-level skill | SKILL.md | Merged from explorer-official.md + explorer-industry.md (2026-08-12) |
| explorer-official.md | Present (unchanged) | Official/regulatory/cloud/energy pipeline: NCDC/DLPP/CEPA permits, NICTA, DICT GovCloud, PNG DataCo, PNG Power/KCH grid |
| explorer-industry.md | Present (unchanged) | Industry/vendor/connectivity/province recipes: operators, sovereign cloud, subsea cables, 5-pass province recipes |
| Division layer | `divisions/` | Planned; 22 provinces, added when batch-6 division runs are written |

## Division layer (future)

- Enumeration granularity: 22 divisions. Priority: National Capital District (highest), Madang (cable landing/DR), Morobe/Lae (watch), Western Highlands/Mount Hagen (watch), West Sepik/Vanimo (Puk-Puk 1), Bougainville, East New Britain, Milne Bay, New Ireland, Northern (connectivity watch); Highlands and island provinces mostly negative-search unless cable/telecom/government evidence.
- Planned per-division files: `divisions/{division}.md` with city/town pivots, operator/cable seeds, and sweep status.

## Cross-references

- Parent country folder: `country-skills/PG/` (SKILL.md, ANATOMY.md, explorer-official.md, explorer-industry.md).
- World manifest division names: `National Capital District`, `Central`, `Morobe`, `Madang`, `Eastern Highlands`, `Western Highlands`, `Chimbu`, `Jiwaka`, `Enga`, `Southern Highlands`, `Hela`, `East New Britain`, `West New Britain`, `New Ireland`, `Bougainville`, `East Sepik`, `West Sepik`, `Manus`, `Milne Bay`, `Northern`, `Gulf`, `Western`.
