# NA · Country Anatomy

Datacenter-country knowledge layer for Namibia (NA).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / municipal pipeline | `explorer-official.md` | present |
| Industry / operator / press discovery | `explorer-industry.md` | present |
| Region division layer | `divisions/` — 14 regions (Erongo, Hardap, //Karas, Kavango East, Kavango West, Khomas, Kunene, Ohangwena, Omaheke, Omusati, Oshana, Oshikoto, Otjozondjupa, Zambezi) | to be added later |

## Source hierarchy

1. **Municipal/local authority planning & building control** — City of Windhoek, Swakopmund, Walvis Bay; Town Planning Ordinance 1954 / Townships Ordinance 1963; Gazette notices; Grade A.
2. **MEFT EIA / Environmental Clearance** — eia.meft.gov.na, Environmental Commissioner decisions; diesel storage, backup generation, substations, cable landing triggers.
3. **Power / grid** — ECB licences, MME, NamPower, Erongo RED, CENORED, NORED, Windhoek City Electricity; MW/MVA evidence.
4. **CRAN** — telecoms licensing (ECS/ECNS/Network Facilities), public hearings, Gazette decisions; not DC proof alone.
5. **Gazette / BIPA / eProcurement / NIPDB** — official names, government ICT/data-centre work, legal entities.
6. **Operators / cloud-region pages** — Paratus (Armada), Telecom Namibia (Infinitum), MTC, Liquid; official AWS/Azure/GCP/Oracle lists (no NA region).
7. **Press / aggregators** — The Namibian, New Era, Economist, Republikein/AZ (data sentrum/Rechenzentrum), DCD tag (B); DataCenterMap/DataCenters.com/GeoCables (C seeds).

## Official vs industry pipeline

- Official decides **countability**: municipal building records, MEFT ECC, ECB/NamPower connection, CRAN licence/Gazette, BIPA entity; Gazette/regulator/municipal facts override press timing.
- Industry discovers **leads and timing**: operator pages (Paratus Armada, Telecom Infinitum), press (launch dates, N$123m, Equiano landing/CLS activation), cable-system pages (2Africa, Submarine Networks); landing stations stay separate from colocation unless service pages say otherwise.
- Division anatomy: Khomas and Erongo are Priority 1 (only confirmed commercial/cable-linked regions); Oshana and Otjozondjupa Priority 2 (corridors); //Karas and Hardap energy/hydrogen watch; remaining regions Priority 4 absence-checks.

## Cross-references

- `SKILL.md` — merged playbook (query templates, grades, region matrix, dedup schema).
- `explorer-official.md` §1 — official source stack per pillar; §3 known facilities/leads to resolve; §4 region-by-region official strategy.
- `explorer-industry.md` §2 — known leads and treatment; §3 query playbook; §4 region matrix — industry angle.
- Watchlist (quarterly): Paratus Armada A-grade records, Telecom Namibia Infinitum facility evidence, Swakopmund CLS status (Equiano/2Africa), National/Government Data Centre procurement, //Karas/Hardap hydrogen-powered compute claims, hyperscaler region pages.
