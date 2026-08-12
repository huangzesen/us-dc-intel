# TD · Country Anatomy

Datacenter-country knowledge layer for Chad (TD).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| Province division layer | `divisions/` — 23 provinces (2024 administrative structure) | to be added later |

## Division layer (future)

- Enumeration granularity: 23 provinces. Priority: N'Djamena (critical — PMICE National DC, ADETIC backup site, TCHADIX host, 2016 Tigo/Moov DC, SOTEL/Airtel/Moov cores, ISP hosting), Moyen-Chari/Sarh (high — PMICE ceremony/reception searches, route endpoint), Ouaddai/Abeche (medium-high — PMICE route includes Abeche, eastern corridor), Logone Oriental/Doba, Mandoul/Koumra, Salamat/Am Timan (medium — PMICE route localities, fiber/transmission sweeps), Ennedi Est/Guera/Mayo-Kebbi Est/Wadi Fira (medium — ADETIC telecentre precedent, institutional ICT rooms; Wadi Fira route localities Am Zoer/Guereda/Iriba), remaining provinces (low — telecom/power/institutional rooms only, expect no commercial DC).
- Provincial records must separate `micro data center`, `institutional server room`, and `telecom transmission site`; do not merge into one DC category.
- Planned per-division files: `divisions/{province}.md` with French query pivots (centre de données / salle serveurs / hébergement / site technique), PMICE route localities, ADETIC telecentre checks, and sweep status.

## Cross-references

- Parent country folder: `country-skills/TD/` (SKILL.md, ANATOMY.md, explorer-official.md, explorer-industry.md).
- World manifest division names: N'Djamena, Barh El Gazel, Batha, Borkou, Chari-Baguirmi, Ennedi Est, Ennedi Ouest, Guera, Hadjer-Lamis, Kanem, Lac, Logone Occidental, Logone Oriental, Mandoul, Mayo-Kebbi Est, Mayo-Kebbi Ouest, Moyen-Chari, Ouaddai, Salamat, Sila, Tandjile, Tibesti, Wadi Fira.
