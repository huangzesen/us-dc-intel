# UZ · Country Anatomy

Datacenter-country knowledge layer for Uzbekistan (UZ).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / energy pipeline | `explorer-official.md` | present |
| Industry / vendor discovery | `explorer-industry.md` | present |
| Division layer | `divisions/` — 14 first-level divisions (12 regions + Karakalpakstan + Tashkent City), run in Uzbek/Russian/English | to be added later |

## Source hierarchy

1. **lex.uz / president.uz / gov.uz (Digital Technologies ministry)** — legal anchors (DP-6079, DP-25, LRU-1015, ZRU-547, RP-358) and ministry announcements (DataVolt phases), Grade A.
2. **Ministry of Energy / grid (minenergy.uz)** — power-led verification for every MW-scale project; separate IT load vs facility load vs grid capacity.
3. **IT Park Uzbekistan / hokimiyat / my.gov.uz / cadastre / construction supervision** — branch/campus and land/permit verification channels.
4. **Uptime Institute country page** — certification baseline; design-document awards are design-stage only.
5. **Operators and lenders** — UzCloud/UZINFOCOM, Uzbektelecom/Uztelecom cloud hubs, DataVolt/Beeline releases; official region lists for negative hyperscale checks.
6. **Trade press / directories** — DCD, UzDaily, Gazeta.uz, Kun.uz, Daryo, Spot, TimesCA, UzA as B; Data Center Map, Datacenters.com, Cloudscene, Baxtel, 2GIS as C seeds.

## Official vs industry pipeline

- Official decides **countability**: ministry/lex.uz groundings, groundbreaking/commissioning announcements, energy MoUs (as planned leads), and Uptime certification type.
- Industry discovers **leads**: operator pages, developer/finance releases (DataVolt, LinkWise, Muroosystems/Uzatom), trade press, catalogs; capacity hierarchy operator/lender official IT MW > Uptime/operator spec > ministry > trade press > directory.
- Division anatomy: 14 divisions, three-language queries per division; Tashkent City vs Tashkent Region and Kokand/Fergana are the classic mis-bucket traps; Bukhara carries three distinct leads (Uztelecom Uptime hub, DataVolt phase, LinkWise MoU).

## Cross-references

- `SKILL.md` — merged playbook (query templates, grades, lifecycle verbs, 14-division matrix).
- `explorer-official.md` §6 — 14-division official strategy table; §5 Uptime baseline; §7 status/evidence rules.
- `explorer-industry.md` §4 — facility seed baseline; §5 14-division industry strategy; §7 verification/deduplication rules.
- Watchlist (quarterly): DataVolt phase statuses, LinkWise MoU -> A upgrade, Jizzakh SMR, Karakalpakstan named operator, UzCloud vs Uzbektelecom dedupe, hyperscaler region pages.
