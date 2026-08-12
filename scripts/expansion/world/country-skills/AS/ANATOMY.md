# AS · Country Anatomy

Datacenter-country knowledge layer for American Samoa (AS).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present — FCC cable/licensing records (Le Vasa DA-26-578A1), ASTCA state telecom operator/RFPs, ASG portal & procurement.as.gov, NTIA/BEAD, USAC/SAM.gov/USAspending/DOI OIA, ASPA power, cloud-region absence checks |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present — Samoa News, Talanei/KHJ, Samoa Observer, RNZ Pacific, Islands Business, DCD, Telecompaper/SubTel, cable vendors (DXN, SubCom, AP Telecom, Google/Starfish/Bulikula), enterprise rooms, DataCenterMap/Cloudscene/PeeringDB |
| Division layer | `divisions/` — country model with exactly 1 division (American Samoa) | to be added later |

## Division layer (future)

- American Samoa enumerates at territory level; per world-manifest.jsonl, AS is modeled as `subnational_type="country"` with exactly **1 division: American Samoa** — every confirmed record uses `division: American Samoa`.
- Planned: create `divisions/American_Samoa/` when the division layer is built; keep place-level rows (Tutuila corridor: Pago Pago/Fagatogo/Utulei/Tafuna/Nu'uuli/Iliili/Leone; Manu'a: Ta'u/Ofu/Olosega/Fitiuta; Swains Island; Rose Atoll) as search aids only — Manu'a and Swains/Rose default to `connectivity_only`/`no_projects`.
