# HR · Country Anatomy

Datacenter-country knowledge layer for Croatia (HR).

## Files

| File | Status | Notes |
|---|---|---|
| Country-level skill | SKILL.md | Merged from explorer-official.md + explorer-industry.md (2026-08-12) |
| explorer-official.md | Present (unchanged) | Official/regulatory/cloud pipeline: eDozvola/ISPU permits, MZOZT EIA, HOPS/HEP/HERA grid, HAKOM e-Operator, EOJN/TED procurement |
| explorer-industry.md | Present (unchanged) | Industry/association/county patterns: HRDCA, trade press, directories, Pantheon/Topusko verification, 21-county recipes |
| Division layer | `divisions/` | Planned; 20 counties + Zagreb City, added when batch-6 division runs are written |

## Division layer (future)

- Enumeration granularity: 21 divisions (20 counties + Zagreb City). Priority: Zagreb City (highest), Zagreb County (DR/industrial-zone belt), Varazdin (DC North/CRATIS), Sisak-Moslavina (Pantheon/Topusko lead), Split-Dalmatia, Primorje-Gorski Kotar, Osijek-Baranja, Istria, Zadar/Sibenik-Knin/Dubrovnik-Neretva (coastal edge/DR), Medimurje (border/interconnect), remaining inland counties low-density.
- Planned per-division files: `divisions/{division}.md` with Croatian county name forms, county seat/city pivots, operator seeds, and sweep status.

## Cross-references

- Parent country folder: `country-skills/HR/` (SKILL.md, ANATOMY.md, explorer-official.md, explorer-industry.md).
- World manifest division names: `Zagreb County`, `Krapina-Zagorje`, `Sisak-Moslavina`, `Karlovac`, `Varazdin`, `Koprivnica-Krizevci`, `Bjelovar-Bilogora`, `Primorje-Gorski Kotar`, `Lika-Senj`, `Virovitica-Podravina`, `Pozega-Slavonia`, `Brod-Posavina`, `Zadar`, `Osijek-Baranja`, `Sibenik-Knin`, `Vukovar-Srijem`, `Split-Dalmatia`, `Istria`, `Dubrovnik-Neretva`, `Medimurje`, `Zagreb City`.
