# MT · Country Anatomy

Datacenter-country knowledge layer for Malta (MT).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| Province/state division layer | `divisions/` — 68 local councils (permits centralized at Planning Authority, not per council) | to be added later |

## Source hierarchy

- **A (official/primary)**: Planning Authority applications/decisions, Government Gazette weekly PA notices, ERA Medium Combustion Plant permits (e.g. Melita Data Centre EP1255/22), MITA official datacentre pages, operator official pages with physical locality, MCA/REWS/Enemalta official records, Malta Stock Exchange/company filings.
- **B (strong secondary)**: DCD, MaltaToday, Times of Malta, TVM/PBS, The Malta Independent, reposted official company announcements.
- **C (weak/unverified)**: DataCenterMap, Datacenters.com, Cloudscene, Data Center Platform, Colomap, Upstack, generic hosting/VPS pages without facility ownership/address.

## Official vs industry pipeline

- **Official pipeline** (explorer-official.md): PA/eApplications + Gazette notices (centralized permit backbone) → ERA MCP generator permits → Enemalta/REWS energy & grid evidence → MCA authorised-undertakings register → MITA government datacentre pages → official cloud-region negative checks (no MT hyperscale region).
- **Industry pipeline** (explorer-industry.md): operator sweep (MITA, BMIT, Melita, GO, Epic, Continent 8, CSL, Heritage Malta) → locality/permit verification pass in PA/Gazette/ERA/MBR → trade press (DCD/Times/MaltaToday/Stock Exchange) for status and history. Directory-only sites stay Grade C until matched to a primary record.

## Division layer (future)

- Malta enumerates at local-council granularity (68 divisions), assigning facilities via the locality field in PA/Gazette/ERA records (not council portals). High-yield clusters: Santa Venera (MITA, Epic, Continent 8), Birkirkara (GO, CSL, Mriehel-CBD), Qormi/Handaq (BMIT Handaq), Kalkara/SmartCity (BMIT, Heritage Malta), Swieqi/Madliena (Melita), Marsa (GO; Streamcast abandoned), Żejtun/Bulebel (BMIT), Gzira (MIDI/SIS DC1), Msida (MIX/University), Rabat Gozo/Victoria (Gozo Data Centre).
- Locality boundary variants to normalize: Mriehel (Birkirkara vs Qormi), Madliena (Naxxar vs Swieqi per ERA), Victoria = Rabat Gozo (vs Rabat, Malta), Ħamrun/Mellieħa/Għajnsielem/Xagħra spellings.
- Planned: per-cluster (or per-council) skill files covering PA/Gazette search per locality, ERA MCP checks, MCA operator context, Enemalta/REWS grid contacts, and MITA procurement surfaces.

## Cross-references

- `SKILL.md` §查询模式 routes to explorer-official.md §1/§2 and explorer-industry.md §4 for copy-paste templates; the locality workflow in explorer-official.md §2 mirrors the locality recipes and seed table in explorer-industry.md §4/§5.
- Known facility seeds and validation paths are in explorer-industry.md §5 (MITA, BMIT Handaq/SmartCity/Żejtun, Melita, GO, Epic, Continent 8, CSL, MIDI/SIS, University/MIX, Heritage Malta, Enemalta/Streamcast).
- Sector manifest: `brief.md` at the country-skills root describes the overall expansion program; this country layer routes MT batches only.
