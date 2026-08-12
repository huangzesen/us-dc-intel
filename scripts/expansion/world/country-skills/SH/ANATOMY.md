# SH · Country Anatomy

Datacenter-country knowledge layer for Saint Helena, Ascension and Tristan da Cunha (SH).

## Files

| File | Status | Notes |
| --- | --- | --- |
| Country-level skill `SKILL.md` | Present | Merged from the two reviewed explorers (official/regulatory/cloud pipeline + industry/trade-press discovery); 2026-08 confirmed: 1 facility (SHG Main Data Centre, Carnarvon Court, Jamestown) + connectivity/satellite/procurement leads + explicit negatives |
| Official / regulatory / cloud pipeline `explorer-official.md` | Present | Final-reviewed: SHG portal/Gazette/legislation/planning/procurement, Sure St Helena, Connect Saint Helena power, Equiano fibre project & MCLS/SLTE landing timeline, AIG Ascension telecom transition, TDG satellite, UK FCDO/NAO/Hansard/Companies House, hyperscaler-absence checks |
| Industry / trade press / vendor discovery `explorer-industry.md` | Present | Final-reviewed: SAMS, St Helena Independent/The Sentinel/The Islander, DCD/Developing Telecoms/Capacity/TechAfrica News/SubTel Forum, Sure/Connect/AIG/TDG operator pages, Submarine Networks/Submarine Cable Map, OneWeb/satellite earth-station lead, directories |
| Division layer `divisions/` | To be added later | SH is manifest type `geographical region` with 3 divisions: Ascension, Saint Helena, Tristan da Cunha |

## Division layer (future)

Per world-manifest.jsonl, SH is modeled as **geographical region with exactly 3 divisions: `Ascension`, `Saint Helena`, `Tristan da Cunha`** (`subnational_type: "geographical region"`). Each facility record must carry both the manifest division and the natural sub-layer. When the division layer is built, create `divisions/Ascension/`, `divisions/Saint_Helena/`, and `divisions/Tristan_da_Cunha/`; keep natural sub-layers as the second-level search and address-resolution layer: Saint Helena / Jamestown (SHG Main Data Centre at Carnarvon Court) or Rupert's (Equiano MCLS/landing station — a different location, never merge); Ascension / Georgetown or Cat Hill (military/BBC communications non-public); Tristan da Cunha / Edinburgh of the Seven Seas (IT Container / Starlink + VSAT — satellite communications, not DC).
