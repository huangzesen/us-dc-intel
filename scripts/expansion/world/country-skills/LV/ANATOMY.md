# LV · Country Anatomy

Datacenter-country knowledge layer for Latvia (LV).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| Province/state division layer | `divisions/` — 43 municipalities / state cities | to be added later |

## Source hierarchy

- **A (official/primary)**: BIS construction records (bis.gov.lv), municipal council/construction-board/public-utility documents, SPRK/AST/Sadales tikls official pages, VPVB/VVD environmental records, operator facility pages (Delska, Tet, LVRTC, Northern Energy), official cloud-region lists.
- **B (strong secondary)**: DCD, Latvian Public Media/LSM, Labs of Latvia, Baltic Times, Datacenter Forum, contractor pages (Citrus Solutions), PeeringDB for interconnection signal.
- **C (weak/unverified)**: DataCenterMap, Baxtel, Datacenters.com, Cloudscene, ColoMap, Inflect, Lursoft snippets, marketplaces, social media, unsourced market reports.

## Official vs industry pipeline

- **Official pipeline** (explorer-official.md): construction intention in BIS (buvniecibas iecere) → building permit (buvatlauja) → construction start (buvdarbu uzsaksana) → commissioning (nodosana ekspluatacija); pivots through BIS/BVKB, municipal buvvalde/council documents, AST/Sadales tikls/SPRK power evidence, VPVB environmental records, and official cloud-region negative checks (no LV hyperscale region).
- **Industry pipeline** (explorer-industry.md): operator/trade lead → operator page → municipal/BIS construction evidence → power/fiber/heating evidence → directory cross-check. Status resolved only after official or operator-confirmed evidence; large MW developer claims (Northern Energy) stay `planned` until municipal/BIS/AST/commissioning records confirm.

## Division layer (future)

- Latvia enumerates at municipality/state-city granularity (43 divisions). Tier 1: Riga (Delska/DEAC, Tet Dattum/Brivibas/Kleistu/Perses/Atlasa/DC6, LVRTC Riga sites), Salaspils novads (Tet DC7, Krasta iela 2/1 — highest-value municipal-document workflow), Liepaja (Northern Energy SEZ campus), Jekabpils novads (Northern Energy Old Airport), Kekavas novads (C.T.Co Valdlauci), Kurzeme/Ventspils cluster (LVRTC Positron). Tier 2: Daugavpils, Valmiera, Rezekne, Jelgava, Jurmala, Ventspils, Liepaja regional LVRTC/telecom-edge checks. Tier 3: all remaining municipalities — compact negative sweep then `no_projects`.
- LVRTC nationwide colocation nodes (Riga TV Tower, Talejas iela 1, Ventspils RTS, Valmiera RTS, Daugavpils RTS, Liepaja RTS) are captured only when a primary or strong interconnection source names the site and describes colo/data-center/interconnection service.
- Planned: per-division (or per-cluster) skill files covering BIS search routes, municipal buvvalde/council document surfaces, AST/Sadales tikls grid contacts, and Salaspils-style utility-routing PDF patterns.

## Cross-references

- `SKILL.md` §查询模式 routes to explorer-official.md §1/§4 and explorer-industry.md §3/§4 for copy-paste templates; the official per-division workflow (explorer-official.md §4) mirrors the industry tiered division strategy (explorer-industry.md §4); alias tables in explorer-industry.md §5 cover operator and address variants used across both files.
- Known facility seeds and verification anchors: explorer-official.md §3 and explorer-industry.md §2 (Delska LV DC1-DC3, Tet Riga sites + DC7, LVRTC Baltic Data Hub + Positron, Northern Energy Liepaja/Jekabpils, C.T.Co Valdlauci).
- Sector manifest: `brief.md` at the country-skills root describes the overall expansion program; this country layer routes LV batches only.
