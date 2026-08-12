# GA · Country Anatomy

Datacenter-country knowledge layer for Gabon (GA).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | Present — merged from the two explorers |
| Official / regulatory / cloud pipeline | `explorer-official.md` | Present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | Present |
| Province division layer | `divisions/` | To be added later |

## Division layer (future)

The manifest (`world-manifest.jsonl`) defines Gabon as **9 provinces**: **Estuary; Upper Ogooue; Middle Ogooue; Ngounie; Nyanga; Ogooue-Ivindo; Ogooue-Lolo; Maritime Ogooue; Woleu-Ntem** (French administrative names: Estuaire; Haut-Ogooue; Moyen-Ogooue; Ngounie; Nyanga; Ogooue-Ivindo; Ogooue-Lolo; Ogooue-Maritime; Woleu-Ntem). A future `divisions/` layer will carry per-province discovery/audit skills; 8 of the 9 provinces are expected to return no public colocation and should be recorded with explicit coverage notes rather than padded with policy statements, landing stations, IXP POPs, or labs.
