# MC · Country Anatomy

Datacenter-country knowledge layer for Monaco (MC).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| Quarter division layer | `divisions/` — 17 quarters | to be added later |

## Division layer (future)

- Enumeration granularity: 17 quarters, assigned by physical address (not head office/marketing names). Priority: Fontvieille (highest — Avenue Albert II / Zone F, Le Copori, 14 avenue de Grande-Bretagne, 23 avenue Albert II, DRSI, MT HQ/DC3/DC6, Telis), Monte-Carlo / Sainte-Devote edge (25 boulevard de Suisse — MT Centre de données n°1), Larvotto / Saint-Roman edge (Larvotto Supérieur project — proposed MT DC, 19 boulevard du Larvotto), La Condamine / Port-Hercule (connectivity/business IT only — no public colo), Moulins / Spelugues (in-house hotel/casino/bank IT — no count without facility evidence), remaining quarters (La Colle, La Gare, Jardin Exotique, Malbousquet, Moneghetti, Monaco-Ville, La Source, Vallon de la Rousse — low-yield sweeps with explicit negative notes).
- French query terms per quarter: centre de données / datacenter / salle informatique / salle de serveurs / hébergement / cloud souverain / zone protégée; exclude French cross-border hits (Cap-d'Ail, Beausoleil, Roquebrune-Cap-Martin, Nice, Sophia Antipolis, CHPG Cap Fleuri).
- Planned per-division files: `divisions/{quarter}.md` with Journal de Monaco notice pivots, address-to-quarter geometry checks, SMEG/AMSN checks, and sweep status.

## Cross-references

- Parent country folder: `country-skills/MC/` (SKILL.md, ANATOMY.md, explorer-official.md, explorer-industry.md).
- World manifest division names: La Colle, La Condamine, Fontvieille, La Gare, Jardin Exotique, Larvotto, Malbousquet, Monte-Carlo, Moneghetti, Monaco-Ville, Moulins, Port-Hercule, Sainte-Devote, La Source, Spelugues, Saint-Roman, Vallon de la Rousse.
