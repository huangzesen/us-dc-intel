# SJ · Country Anatomy

Datacenter-country knowledge layer for Svalbard and Jan Mayen (SJ).

## Files

| File | Status | Notes |
| --- | --- | --- |
| Country-level skill `SKILL.md` | Present | Merged from the two reviewed explorers (official/regulatory/cloud pipeline + industry/trade-press discovery); 2026-08 working conclusion: **commercial_dc: absent** — no verified commercial DC/colo/hyperscale/cloud region; IT-intensive entities are KSAT SvalSat (satellite_ground_station), Space Norway Svalbard fibre (interconnection), research facilities (UNIS/KHO/EISCAT/SIOS), Seed Vault (government_monitoring), Jan Mayen defence/meteorological/navigation station |
| Official / regulatory / cloud pipeline `explorer-official.md` | Present | Final-reviewed: Sysselmesteren, Longyearbyen Lokalstyre, regjeringen.no Svalbard white paper, Lovdata (Svalbard Act/ekomloven/datasenterforskriften), Nkom datacenter register, Space Norway Svalbard fibre, SSB population, Brønnøysund, Statsforvalteren i Nordland/Forsvaret/Met.no (Jan Mayen), hyperscaler-absence checks |
| Industry / trade press / vendor discovery `explorer-industry.md` | Present | Final-reviewed: KSAT SvalSat/Svalbard Ground Station, Space Norway (incl. Nittedal Teleport false-positive rule), Telenor Svalbard, UNIS/KHO/EISCAT/SIOS, Seed Vault, directory/market-report handling, Norwegian/Chinese search templates |
| Division layer `divisions/` | To be added later | SJ is manifest type `country` with a single division `Svalbard and Jan Mayen`; internal sub_areas Svalbard / Jan Mayen |

## Division layer (future)

Per world-manifest.jsonl, SJ is modeled as a **single repo division: `Svalbard and Jan Mayen`** (`subnational_type: country`, `divisions: ["Svalbard and Jan Mayen"]`). Output records must use only this division; the methodology splits it internally into two audit sub-areas: **Svalbard** (expected commercial DC negative; positive classification for ground station/research/government/telecom) and **Jan Mayen** (pure negative control — nature-reserve administration, meteorology, defence/communications/navigation, emergency). When the division layer is built, create `divisions/Svalbard_and_Jan_Mayen/` with `sub_area` and `settlement_or_site` (Longyearbyen, Ny-Alesund, Barentsburg, Plataberget, Olonkinbyen) as the second-level search and address-resolution layer.
