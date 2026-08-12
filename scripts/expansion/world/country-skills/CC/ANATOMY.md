# CC · Country Anatomy

Datacenter-country knowledge layer for Cocos (Keeling) Islands (CC).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers; commercial DC verified-negative, OAC West Island cable landing recorded as telecom lead) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present — Infrastructure IOT portal & governance, Shire of Cocos (shire.cc), ABS QuickStats, DFAT, nbn Sky Muster, Telstra, ACMA, AusTender, ARENA, official cloud-region absence checks |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present — SUBCO/OAC subsea, Oman Observer/iTnews/DCD/SubTel/Capacity, nbn/Telstra/IOTT/MultiWave/Cocos Communications and IT, AusTender/CER power context, DataCenterMap/CloudInfrastructureMap directories, Chinese rumor watch |
| Division layer | `divisions/` — country model with exactly 1 division (Cocos (Keeling) Islands); sub-locations West Island / Home Island / Direction Island / Unknown CC are evidence placement only | to be added later |

## Division layer (future)

- Cocos (Keeling) Islands enumerates at territory level; per world-manifest.jsonl, CC is modeled as `subnational_type="country"` with exactly **1 division: `Cocos (Keeling) Islands`** — every confirmed record uses `division: Cocos (Keeling) Islands`.
- Planned: create `divisions/Cocos_Keeling_Islands/` when the division layer is built; keep sub-locations as evidence placement only, never as divisions — **West Island** (capital, airport, government cluster, OAC landing point; high priority), **Home Island** (community, Shire seat/services, power-station history; medium), **Direction Island** (historical telegraph-station false-positive guard; low), **Unknown CC** (source confirms a facility but names no specific island; do not force West/Home assignment).
