# MH · Country Anatomy

Datacenter-country knowledge layer for the Republic of the Marshall Islands (MH).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| Municipality division layer | `divisions/` — 24 atoll/single-island municipalities | to be added later |

## Division layer (future)

- Enumeration granularity: 24 municipalities. Priority: Majuro (the only real cluster — NTA HQ/cable landing/earth station/L-root, government data rooms, IOKWE Majuro landing planned), Kwajalein (two tracks: civilian Ebeye NTA landing station + restricted US Army Reagan Test Site IT, IOKWE Ebeye landing planned), Jaluit (low — satellite-fed telecom only), remaining 19 outer atolls (very low — Intelsat/NTA small-cell sites, expect `no_projects: true`).
- Planned per-division files: `divisions/{division}.md` with NTA/Intelsat satellite evidence, HANTRU-1/IOKWE landing-station status, Marshallese name normalization (Ebeye/Uliga-Delap-Rita/Jabor/Enewetak-Ujelang), and sweep status.

## Cross-references

- Parent country folder: `country-skills/MH/` (SKILL.md, ANATOMY.md, explorer-official.md, explorer-industry.md).
- World manifest division names: Majuro, Kwajalein, Ailinglaplap, Ailuk, Arno, Aur, Ebon, Enewetak & Ujelang, Jabat, Jaluit, Bikini & Kili, Lae, Lib, Likiep, Maloelap, Mejit, Mili, Namdrik, Namu, Rongelap, Ujae, Utrik, Wotho, Wotje.
