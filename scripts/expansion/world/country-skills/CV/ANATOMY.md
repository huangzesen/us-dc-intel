# CV · Country Anatomy

Datacenter-country knowledge layer for Cabo Verde (CV).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | Present — merged from the two explorers |
| Official / regulatory / cloud pipeline | `explorer-official.md` | Present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | Present |
| Geographical-region division layer | `divisions/` | To be added later |

## Division layer (future)

The manifest (`world-manifest.jsonl`) defines Cabo Verde as **2 geographical regions** (`subnational_type = geographical region`, not admin2): **Ilhas de Barlavento** (windward) and **Ilhas de Sotavento** (leeward). A future `divisions/` layer will carry per-region discovery/audit skills; because the manifest layer is not administrative, every facility record must additionally carry the island + concelho (municipality) as the natural sub-layer.
