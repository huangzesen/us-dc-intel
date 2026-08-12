# SC · Country Anatomy

Datacenter-country knowledge layer for Seychelles (SC).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| District division layer | `divisions/` — 27 manifest districts | to be added later |

## Division layer (future)

- Enumeration granularity: 27 districts from `world-manifest.jsonl`. Priority: Anse Boileau (CWS Data Center 1 - Bon Espoir per Uptime), Ile Perseverance I/II (Airtel House DC + PEACE landing; parcel check before duplicating I/II), Anse Etoile / Glacis (2Africa North East Point boundary search space), English River (Victoria/New Port/Ile du Port SEAS-CWS legacy), Roche Caiman (Providence Industrial Estate + Intelvision lead), Cascade/Plaisance/Pointe Larue (Providence boundary + airport/industrial telecom), Mont Fleuri (UniSey/ISCEICT historical institutional lead), Saint Louis/Bel Air (Victoria CBD bank/government/CWS), Baie Sainte Anne/Grand Anse Praslin/La Digue (Praslin/La Digue PoPs — no DC without primary proof), Beau Vallon (SEAS shore history — connectivity only); remaining districts low (generic sweeps).
- Language pair per district: English + French terms (centre de données / salle de serveurs / hébergement / générateur de secours); always include `Seychelles` or a Seychelles place name to avoid South Carolina `.sc` false positives.
- Planned per-division files: `divisions/{district}.md` with SPA/ePlanning parcel pivots, certification-registry checks, cable-landing status, and sweep status.

## Cross-references

- Parent country folder: `country-skills/SC/` (SKILL.md, ANATOMY.md, explorer-official.md, explorer-industry.md).
- World manifest division names: Anse aux Pins, Anse Boileau, Anse Etoile, Au Cap, Anse Royale, Baie Lazare, Baie Sainte Anne, Beau Vallon, Bel Air, Bel Ombre, Cascade, Glacis, Grand Anse Mahe, Grand Anse Praslin, La Digue, English River, Mont Buxton, Mont Fleuri, Plaisance, Pointe Larue, Port Glaud, Saint Louis, Takamaka, Les Mamelles, Roche Caiman, Ile Perseverance I, Ile Perseverance II.
