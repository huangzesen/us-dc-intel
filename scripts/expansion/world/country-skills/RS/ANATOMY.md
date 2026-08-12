# RS · Country Anatomy

Datacenter-country knowledge layer for Serbia (RS).

## Files

| File | Status | Notes |
|---|---|---|
| Country-level skill | SKILL.md | Merged from explorer-official.md + explorer-industry.md (2026-08-12) |
| explorer-official.md | Present (unchanged) | Official/regulatory/cloud pipeline: RATEL list, CEOP/APR permits, environmental records, EMS/EDS/AERS grid, procurement, Oracle Jovanovac region |
| explorer-industry.md | Present (unchanged) | Industry/operator/district patterns: Belgrade/Kragujevac/Vojvodina/Nis/Kosovo-Metohija seeds, cloud rules, Serbian alias table |
| Division layer | `divisions/` | Planned; 20 manifest divisions, added when batch-6 division runs are written |

## Division layer (future)

- Enumeration granularity: 20 divisions (city/district/autonomous province). Tier 1: Belgrade (commercial colo/interconnection), Sumadija (government/cloud hub), Vojvodina (Vrsac/Novi Sad DR+cloud), Nisava (NiNet/Tehnis), Kosovo-Metohija (IPKO, jurisdiction-sensitive). Tier 2: Macva, Kolubara, Podunavlje, Branicevo, Pomoravlje, Bor, Zajecar, Zlatibor, Moravica, Raska, Rasina, Toplica, Pirot, Jablanica, Pcinja (negative-control until named facility).
- Planned per-division files: `divisions/{division}.md` with Latin/Cyrillic locality aliases, operator seeds, and sweep status.

## Cross-references

- Parent country folder: `country-skills/RS/` (SKILL.md, ANATOMY.md, explorer-official.md, explorer-industry.md).
- World manifest division names: `Belgrade`, `Macva`, `Kolubara`, `Podunavlje`, `Branicevo`, `Sumadija`, `Pomoravlje`, `Bor`, `Zajecar`, `Zlatibor`, `Moravica`, `Raska`, `Rasina`, `Nisava`, `Toplica`, `Pirot`, `Jablanica`, `Pcinja`, `Kosovo-Metohija`, `Vojvodina`.
