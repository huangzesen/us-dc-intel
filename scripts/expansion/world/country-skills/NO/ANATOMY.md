# NO · Country Anatomy

Datacenter-country knowledge layer for Norway (NO).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / register pipeline | `explorer-official.md` | present |
| Industry / operator / association discovery | `explorer-industry.md` | present |
| Division layer | `divisions/` — 13 repo divisions (2020-2023 county labels: Oslo; Rogaland; More and Romsdal; Northland; Svalbard; Jan Mayen; Viken; Inland; Vestfold and Telemark; Agder; Westland; Trondelag; Troms and Finnmark; search current post-2024 county names too) | to be added later |

## Source hierarchy

1. **Nkom (master register)** — datasenterforskriften under ekomloven (from 2025-01-01); verified 2026-08-12: 115 registered data centres, 61 commercial operators; CSV export; Grade A census backbone (internal sites not named).
2. **Municipal planning/building records** — saksinnsyn/planinnsyn/postjournal (Oslo PBE, DiBK, Altinn, Kartverket, eInnsyn); permit lifecycle (reguleringsplan -> rammetillatelse -> igangsettingstillatelse -> ferdigattest).
3. **Statsforvalteren / Miljødirektoratet / Norske utslipp** — pollution permits (forurensningsloven) for generators/noise/cooling; best official proof for operating/near-operating sites.
4. **NVE / RME / Statnett / grid companies** — concessions, connection capacity, substations, northern Svartisen >5 MW restriction; grid evidence is enabling infrastructure, not operation.
5. **Lovdata / government strategy / NSM** — regulations and policy context.
6. **Operator pages** — Green Mountain (4 sites), Bulk (OS-IX, N01), STACK/DigiPlex SPVs, Nscale, atNorth NOR01, WS Computing/Google Gromstul, Lefdal Mine, Datafjellet, Tussa/Tafjord/NEAS, Storespeed, PolarDC, Tydal/Bitdeer, Exanorth, Trollfjord; Nkom operator rows as existence anchors.
7. **Cloud-region facts** — Azure Norway East/West live (metro anchors only); no AWS/Google/Oracle Norway region; Google/WS Computing Skien is a physical DC project, kept separate from cloud-region facts.
8. **Association / trade press / directories** — Norsk Datasenterindustri (B+), Business Norway (B), DCD/Datacenter Forum (B), Baxtel (B-/C+), DataCenterMap (C+).

## Official vs industry pipeline

- Official decides **countability**: at least one Grade A facility source (Nkom registration tied to operator, municipal permit, environmental permit, NVE/Statnett grid record, or operator facility page); land purchase/political support/grid reservation/cloud-region naming/directories are leads.
- Industry discovers **names and marketed capacity**: operator pages, association membership, trade press; Nkom + operator page can prove existence, but status/address/MW need separate source grades.
- Division anatomy: Rogaland (Green Mountain Rennesøy, atNorth, Azure Norway West anchor) and Vestfold and Telemark (Rjukan, Gromstul/Google) plus Viken/Inland (Enebakk, Hamar) carry the large campuses; Agder (Bulk N01), Westland (Lefdal, Datafjellet), Trondelag (Tydal, NTE) and Northland (Nscale, Trollfjord) are medium; Svalbard and Jan Mayen are negative-control Arctic territories; Troms and Finnmark has northern-grid constraints.

## Cross-references

- `SKILL.md` — merged playbook (query templates, lifecycle vocabulary, grid-field separation, division mapping).
- `explorer-official.md` §0.2 — county mapping; §1 official source backbone; §3 per-division official strategy; §2 query patterns with known pivots.
- `explorer-industry.md` §0 — Nkom operator priority list; §2 operator/platform map; §3 cloud-region facts; §4 per-division industry leads; §5 workflow.
- Watchlist (quarterly): Nkom CSV refresh, atNorth NOR01 permits, Tydal/Bitdeer records, Bulk N01 municipality, Storespeed Halden, Gromstul Datasenter 2 decision, Statnett northern restriction updates.
