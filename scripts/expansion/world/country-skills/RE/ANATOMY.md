# RE · Country Anatomy

Datacenter-country knowledge layer for Reunion (RE).

## Files

| File | Status | Notes |
| --- | --- | --- |
| Country-level skill `SKILL.md` | Present | Merged from the two reviewed explorers (official/regulatory/cloud pipeline + industry/trade-press discovery); key seed 2026-08: **Omega 1 / Omega One** (Le Port, Oceinde/Zeop ecosystem), SFR Business NETCENTER service, Zeop hosting, Orange Reunion lead |
| Official / regulatory / cloud pipeline `explorer-official.md` | Present | Final-reviewed: prefecture/ICPE & DREAL planning, Region/Departement/TCO/mairie, ARCEP, EDF SEI/CRE power, BOAMP/PLACE procurement, SAFE/LION/LION2/METISS cable-landing context, REUNIX IXP, certification registries, hyperscaler-absence checks |
| Industry / trade press / vendor discovery `explorer-industry.md` | Present | Final-reviewed: Omega 1 operator site, SFR Business Reunion NETCENTER, Zeop/Oceinde, Orange Reunion, local media set (clicanoo/linfo/zinfos974/imazpress/ipreunion/freedom/lequotidien/la1ere), directories (DataCenterMap, Baxtel, Cloudscene), REUNIX/PeeringDB, subsea sources |
| Division layer `divisions/` | To be added later | RE is manifest type `country` with a single division `Reunion`; commune is the second-level layer |

## Division layer (future)

Per world-manifest.jsonl, RE is modeled as a **single division: `Reunion`** (`subnational_type: country`, `divisions: ["Reunion"]`) — do not create province/region subdivisions. Commune is the second-level search and address-resolution layer. When the division layer is built, create `divisions/Reunion/`; keep commune sweep priority: **Le Port** (highest — Omega 1 verified), **Saint-Denis / Sainte-Clotilde / Le Chaudron** (operator offices, possible REUNIX), **Saint-Paul** (SAFE/METISS landing context), **La Possession / Saint-Pierre** (low-medium scans), and Le Tampon, Saint-Louis, Saint-André, Saint-Benoît, Sainte-Marie, Sainte-Suzanne (explicit negative scans).
