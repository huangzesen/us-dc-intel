# GW · Country Anatomy

Datacenter-country knowledge layer for Guinea-Bissau (GW).

## Files

| File | Status | Note |
|---|---|---|
| Country-level skill `SKILL.md` | Present | Merged from the two final-reviewed explorers (official/regulatory/cloud pipeline + industry/trade-press discovery). |
| Official / regulatory / cloud pipeline `explorer-official.md` | Present | ARN-TIC, MENER/EAGB, EIA/EIASS, municipal permits, ITMA/WARDIP/ENTD.GW, UNGM/UNDP procurement, cloud-region negative controls. |
| Industry / trade press / vendor discovery `explorer-industry.md` | Present | Operator census, hyperscaler status, ACE/GwIX connectivity, trade press & directories, per-division discovery map. |
| Division layer `divisions/` | To be added later | Per-division knowledge files once exploration batches produce stable per-division results. |

## Division layer (future)

The manifest (`world-manifest.jsonl`) defines GW divisions as **4 autonomous sectors/provinces** (`subnational_type = autonomous sector/province`): **Bissau** (Sector Autonomo de Bissau), **North** (Cacheu, Oio, Biombo), **East** (Bafata, Gabu), **South** (Quinara, Tombali, Bolama-Bijagos). Future `divisions/` files should be created per manifest division, keyed to these four groups; division coverage is complete only when every division has been searched or explicitly marked `no_projects: true` with date and query notes.
