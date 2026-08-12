# BE · Country Anatomy

Datacenter-country knowledge layer for Belgium (BE).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / permits / energy / registries / cloud / procurement pipeline | `explorer-official.md` | present |
| Industry / operators / IXP / subsea adjacency / directories | `explorer-industry.md` | present |
| Region division layer | `divisions/` — 3 regions (Brussels-Capital, Flanders, Wallonia; municipality-level assignment) | to be added later |

## Division layer (future)

- Belgium enumerates region-first, assigning every facility by municipality: Brussels-Capital (KevlinX BRU01, DCU Evere, government/IXP PoPs) vs Flanders (largest colo count: Digital Realty Zaventem, LCL Diegem/Aalst/Huizingen/Antwerp, DCU Antwerp/Machelen/Ghent/Mechelen/Hasselt/Oostkamp, Penta Asse/Zellik, Combell Ghent, Cegeka Hasselt) vs Wallonia (hyperscale-heavy: Google St. Ghislain + Farciennes, LCL Gembloux, Etix Villers-le-Bouillet, DCU Mouscron).
- Planned: per-region skill files covering each permitting surface (urban.brussels/Brussels Environment; Omgevingsloket/Inzageloket + Fluvius; SPW/TWICE/Wallex + ORES/RESA), Elia connection-queue joins, KBO-BCE entity resolution, and Dutch/French query sets per region.
