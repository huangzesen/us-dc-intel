# GQ · Country Anatomy

Datacenter-country knowledge layer for Equatorial Guinea (GQ).

## Files

| File | Status | Note |
|---|---|---|
| Country-level skill `SKILL.md` | Present | Merged from the two final-reviewed explorers (official/regulatory/cloud pipeline + industry/trade-press discovery). |
| Official / regulatory / cloud pipeline `explorer-official.md` | Present | GITGE, CNIAPGE, PAMFP/Hacienda, SEGESA energy leads, cloud-region / IXP / Uptime negative controls. |
| Industry / trade press / vendor discovery `explorer-industry.md` | Present | Operator & facility seeds, cloud/CDN/on-ramp checks, directory & PeeringDB cross-checks, per-division industry patterns. |
| Division layer `divisions/` | To be added later | Per-division knowledge files once exploration batches produce stable per-division results. |

## Division layer (future)

The manifest (`world-manifest.jsonl`) defines GQ divisions as **2 regions** (`subnational_type = region`): **Continental** (Rio Muni mainland; provinces Litoral, Centro Sur, Kie-Ntem, Wele-Nzas, Djibloho) and **Insular** (Bioko Norte incl. Malabo/Sipopo, Bioko Sur, Annobon, plus Corisco). Future `divisions/` files should be created per manifest division, keyed to these two regions with province/city names (Malabo, Bata, Luba, Ebebiyin, Mongomo, Oyala/Ciudad de la Paz, etc.) used only as search anchors.
