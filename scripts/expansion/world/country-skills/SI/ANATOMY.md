# SI · Country Anatomy

Datacenter-country knowledge layer for Slovenia (SI).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| Province/state division layer | `divisions/` — 212 municipalities, grouped by 12 SURS statistical regions for field work | to be added later |

## Source hierarchy

- **A (official/primary)**: PIS/eGraditev construction acts (`GD`/`PG`/`UD`), GOV.SI/municipal/agency decisions, e-JN/enarocanje/TED procurement, ELES/SODO/AKOS official infrastructure context, operator-owned facility pages, government handover/opening records.
- **B (strong secondary)**: DCD, The Slovenia Times/STA, Finance.si, Monitor, PostEurop, EuroHPC/SLING project pages, association/conference material, contractor case studies.
- **C (weak/unverified)**: DataCenterMap, Cloudscene, Datacenters.com, Inflect, Baxtel, market-research and SEO/directory snippets — leads only until cross-checked.

## Official vs industry pipeline

- **Official pipeline** (explorer-official.md): spatial plan (OPN/OPPN) → building permit (`GD`) → start notification (`PG`) → use permit (`UD`) → official handover/opening; pivots through PIS, municipal portals, GOV.SI/ARSO environment records, ELES/SODO/DSO grid context, AKOS telecom context, and e-JN/enarocanje procurement. No hyperscale SI cloud region exists — cloud pages are negative context only.
- **Industry pipeline** (explorer-industry.md): directory/trade/operator lead → operator page or official government/procurement page → PIS construction act → municipal/environment/energy cross-check → AKOS/fiber context. Status resolved only after official confirmation.

## Division layer (future)

- Slovenia enumerates at municipality (obcina) + administrative unit (upravna enota / UE) granularity; the 12 SURS statistical regions (Osrednjeslovenska, Podravska, Goriska, Obalno-kraska, Gorenjska, Savinjska, Jugovzhodna, Pomurska, Koroska, Posavska, Primorsko-notranjska, Zasavska) are sweep buckets only. Most small municipalities return no project evidence.
- Planned: per-region (or per-municipality-cluster) skill files covering PIS/eGraditev act search, municipal OPN/OPPN portals, ELES/SODO/DSO grid contacts, AKOS operator context, and procurement surfaces per region.

## Cross-references

- `SKILL.md` §查询模式 points to explorer-official.md §1/§2 and explorer-industry.md §3 for copy-paste templates; per-region official sweeps in explorer-official.md §4 mirror the 12-region industry sweeps in explorer-industry.md §4.
- Known-lead validation table (explorer-industry.md §5) ties each lead to its official validation route (PIS/GOV.SI/e-JN/ELES/municipality).
- Sector manifest: `brief.md` at the country-skills root describes the overall expansion program; this country layer routes SI batches only.
