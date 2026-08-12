# LA · Country Anatomy

Datacenter-country knowledge layer for Lao PDR (LA).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| Province division layer | `divisions/` — 17 manifest provinces + Vientiane Capital (manual extra unit) | to be added later |

## Division layer (future)

- Enumeration granularity: 17 manifest provinces + Vientiane Capital (add manually — nearly all confirmed evidence is there). Priority: Vientiane Capital (very high — MTC/LANIC, KPL, GDMS National Cloud, Unitel Cloud, LaoDC, 2016 government eco datacenter, capital SEZs), Savannakhet (medium-high — Savan-Seno SEZ, strongest province outside capital, no confirmed tenant yet), Bokeo / Louang Namtha / Champasak / Khammouan / Viangchan (medium — Golden Triangle, Boten, Pakse-Japan, Thakhaek SEZs; China-border/railway pivots for Louang Namtha), Louangphabang (medium-low), remaining provinces (low — one-pass annual sweeps, expect no confirmed DC).
- Language trivium per division: English (state media/operators), Lao (ສູນຂໍ້ມູນ / ສູນດາຕ້າ / ເຊົ່າ Server / ບໍລິການ Hosting), Chinese for China-linked SEZ/railway leads (老挝/万象/磨丁/金三角 + 数据中心).
- Planned per-division files: `divisions/{division}.md` with official-route (DPI/SEZA/MTC/EDL) recipes, SEZ pages, Lao/Chinese query pivots, and sweep status.

## Cross-references

- Parent country folder: `country-skills/LA/` (SKILL.md, ANATOMY.md, explorer-official.md, explorer-industry.md).
- World manifest division names: Attapu, Bokeo, Bolikhamxai, Champasak, Houaphan, Khammouan, Louang Namtha, Louangphabang, Oudomxai, Phongsali, Salavan, Savannakhet, Viangchan, Xaignabouli, Xekong, Xiangkhouang, Xaisomboun (+ Vientiane Capital as extra unit; spellings normalized: Luang Namtha, Luang Prabang, Khammouane, Xayabury/Sainyabuli, Xiengkhouang, Bolikhamsai, Phongsaly, Sekong, Attapeu).
