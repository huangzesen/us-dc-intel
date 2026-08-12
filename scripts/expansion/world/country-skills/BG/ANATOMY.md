# BG · Country Anatomy

Datacenter-country knowledge layer for Bulgaria (BG).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| Province/state division layer | `divisions/` — 28 NUTS3 districts (област) → 265 municipalities (община) | to be added later |

## Division layer (future)

- Bulgaria enumerates at district granularity (28 области) but permitting is municipal: each division resolves to its municipalities (общини) and their building-permit / `чл.149 ЗУТ` notice surfaces, many on `*.egov.bg`; Sofia City uses NAG registers, Sofia Province hosts Stolnik spillover.
- Planned: per-district (or per-municipality) skill files covering municipal building registers, RIEW environmental inspectorates, ESO/distribution grid contacts, and local operator/IX leads.
