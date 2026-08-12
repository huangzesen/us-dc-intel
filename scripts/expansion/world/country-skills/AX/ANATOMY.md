# AX · Country Anatomy

Datacenter-country knowledge layer for Åland Islands (AX).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present — Ålands landskapsregering & Lagtinget, Traficom, 16 municipal planning/bygglov, Kraftnät Åland/el.ax/energi.ax/Fingrid power, ÅMHM environmental permits, EU TED/Hilma procurement, PRH/YTJ registry, ÅSUB statistics, submarine cables, cloud-region absence checks |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present — Nya Åland, Ålandstidningen, Ålands Radio, HBL/Yle/Kauppalehti/DI, DCD/Capacity/DCK, FDCA/TIVIA/Ålands Näringsliv, Ålcom/Elisa/Telia/Tietoevry, PeeringDB/Baxtel/DataCenterMap/Cloudscene |
| Division layer | `divisions/` — country model with exactly 1 division (Aland Islands); 16 municipalities are search buckets only | to be added later |

## Division layer (future)

- Åland enumerates at territory level; per world-manifest.jsonl, AX is modeled as `subnational_type="country"` with exactly **1 division: `Aland Islands`** — every confirmed record uses `division: Aland Islands`.
- Planned: create `divisions/Aland_Islands/` when the division layer is built; keep the 16 municipalities (Mariehamn, Jomala, Finström, Sund, Saltvik, Hammarland, Eckerö, Lemland, Lumparland, Vårdö, Geta, Föglö, Kökar, Sottunga, Kumlinge, Brändö) as second-level search buckets and candidate positioning only, never as manifest divisions; high priority Mariehamn/Jomala/Finström, mid priority Sund/Saltvik/Hammarland/Eckerö/Lemland, low density for the island municipalities.
