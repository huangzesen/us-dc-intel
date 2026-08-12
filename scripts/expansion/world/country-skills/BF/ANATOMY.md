# BF · Country Anatomy

Datacenter-country knowledge layer for Burkina Faso (BF).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / procurement pipeline | `explorer-official.md` | present |
| Industry / press / operator discovery | `explorer-industry.md` | present |
| Region division layer | `divisions/` — legacy 13 regions (Boucle du Mouhoun; Cascades; Centre; Centre-Est; Centre-Nord; Centre-Ouest; Centre-Sud; Est; Hauts-Bassins; Nord; Plateau-Central; Sahel; Sud-Ouest) plus post-2025 endogenous aliases (Kadiogo, Guiriko, Bankui/Sourou, Goulmou/Sirba/Tapoa, Liptako/Soum) | to be added later |

## Source hierarchy

1. **MTDPCE / ANPTIC / Presidency-SIG** — government cloud, national datacenters, NOC, digital-transformation programs; Grade A for ministry pages.
2. **ARCEP** — licence facts and operator universe (ONATEL, Orange Burkina Faso, Telecel Faso, PAV-Burkina); not DC proof alone.
3. **ANEVE/SINADEVE** — environmental compliance/EIA for new builds, gensets, fibre corridors, waste-to-energy projects.
4. **ARSE / SONABEL** — electricity regulation and utility power evidence; mandatory power sanity checks (kVA/MVA/MW, substation, generator, solar/PPA).
5. **ARCOP** — tender/award notices for government datacenters, NOC, fibre works.
6. **BFIX / PeeringDB / PCH** — interconnection presence and local facilities (Virtix, Immeuble du Faso, Ministère de l'agriculture); A/B for interconnection, not commercial DC classification alone.
7. **Operator pages** — Virtix (best commercial colo seed), IKA Cloud, Alink, IPSyS, Orange BF, ONATEL/Moov, Telecel; Uptime for certification claims.
8. **Trade press / directories** — DCD, Ecofin, Developing Telecoms, AIB, Sidwaya, leFaso.net, Burkina24, Wakat Sera (B); DataCenterPlatform, DataCenterMap, Inflect, Baxtel (C seeds).
9. **Negative evidence** — official hyperscaler region pages (no BF region; Cloudflare/Meta BFIX peers are not facilities; offshore hosting is not a BF facility).

## Official vs industry pipeline

- Official decides **countability**: ministry/ANPTIC pages, ARCEP licences, ANEVE/EIA, SONABEL/ARSE power, ARCOP awards, commune permits, BFIX/PeeringDB interconnection, operator pages; escalation: announcement C/B -> construction B/A -> operational A/B, with capacity fields graded separately.
- Industry discovers **leads**: trade press (2026 gov mini-DCs, NOC, Orange solar, Essor/Kaia waste-to-energy), operator pages, directories; dedup before counting (Cloud Gouvernemental/ANPTIC/MDENP/mini-DCs/education DC/NOC overlap; BFIX/Virtix/legacy buildings overlap).
- Division anatomy: Centre/Ouagadougou/Kadiogo carries essentially all facility evidence (gov modular DCs, Virtix, IKA, Orange, ONATEL, Telecel, BFIX); Hauts-Bassins/Bobo-Dioulasso is low-medium (telco PoPs, BFIX Bobo-Dioulasso); remaining regions are negative sweeps with post-2025 aliases; Sahel/Nord/Est keep security-context caution.

## Cross-references

- `SKILL.md` — merged playbook (query templates, 13-region + alias sweeps, record standard, escalation rules).
- `explorer-official.md` §1 — official source map; §3 officially verified seeds; §4 regulatory and permitting logic; §5 region coverage strategy; §7 minimum record standard.
- `explorer-industry.md` §3 — operator and project seeds; §4 region-by-region industry strategy; §6 evidence escalation rules; §7 common pitfalls.
- Watchlist (quarterly): ANPTIC modular-DC live pages/site addresses, Virtix Uptime/capacity, NOC award, Essor/Kaia EIA, Orange/ONATEL/Telecel named core sites, hyperscaler region pages.
