# BV · Country Anatomy

Datacenter-country knowledge layer for Bouvet Island (BV).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers; verified-negative baseline, expected facility count 0) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present — Norsk Polarinstitutt (npolar.no), regjeringen.no dependency policy, Lovdata nature-reserve regulations, Norid `.bv`/IANA/ITU numbering, Nkom & official cloud-region absence checks |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present — datacenter directories (DataCenterMap/Cloudscene/Baxtel/datacenters.com), DCD/SubTel Forum, cloud/submarine/network maps, satellite/expedition surfaces, `.bv` domain pitfalls, false-positive list |
| Division layer | `divisions/` — country model with exactly 1 division (Bouvet Island); geographic sub-areas (Nyrøysa, nature reserve/territorial waters, Larsøya) are annotations only | to be added later |

## Division layer (future)

- Bouvet Island enumerates at territory level; per world-manifest.jsonl, BV is modeled as `subnational_type="country"` with exactly **1 division: `Bouvet Island`** — every confirmed record uses `division: Bouvet Island` (expected: none).
- Planned: create `divisions/Bouvet_Island/` when the division layer is built; keep geographic sub-areas as annotation only, never as divisions — **Nyrøysa** (only feasible landing zone; possible research/temporary stations/automatic weather equipment; default not counted), **Bouvetøya Nature Reserve / territorial waters** (vessel equipment not counted as on-island facilities), **Larsøya / cliffs / glaciers / Olavtoppen** (geographic background only).
