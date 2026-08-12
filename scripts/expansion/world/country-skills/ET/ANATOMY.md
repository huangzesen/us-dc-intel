# ET · Country Anatomy

Datacenter-country knowledge layer for Ethiopia (ET).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / power pipeline | `explorer-official.md` | present |
| Industry / operator / trade-press discovery | `explorer-industry.md` | present |
| Division layer | `divisions/` — 13 manifest divisions (Addis Ababa; Afar; Amara/Amhara; Benshangul-Gumaz; Dire Dawa; Gambela Peoples; Harari People; Oromia; Sidama; Somali; Southern Nations/legacy SNNPR; Southwest Ethiopia Peoples; Tigrai/Tigray; search newer South/Central Ethiopia names within the SNNPR bucket) | to be added later |

## Source hierarchy

1. **ECA** — Data Center Service Provider License / Hosting Service Provider License categories (https://www.eca.et/services/), ADDIX, PDPP 1321/2024 registrations; Grade A for licensing/registration.
2. **EIC** — investment permits, SEZ context (https://investethiopia.gov.et/).
3. **IPDC / MinT** — industrial park/SEZ allocation (Bole Lemi, Kilinto, Adama, Hawassa, Dire Dawa, Kombolcha, Debre Birhan, Mekelle, Bahir Dar, Jimma, Semera), Ethio ICT Park, Digital Ethiopia.
4. **EEP / EEU** — hydropower/PPA evidence, MW/MVA, substations, direct-sales customers (critical for colo, telecom, crypto/data-mining).
5. **INSA + Addis Ababa/regional permits** — government cloud/cybersecurity (programme evidence separate from site evidence) and building permits/land leases.
6. **Operator pages / Uptime** — Raxio ET1 (800 racks/3 MW), Wingu Africa (10 MW/800 racks full build), Ethio telecom modular DC/cloud, Safaricom core DC, Redfox, Dashen Bank, ADDIX hosting.
7. **Trade press / vendor cases** — DCD, Shega, Capital, Addis Fortune, Ethiopian Monitor, The Reporter, ENA/FBC (B); Huawei/Schneider/Vertiv (B/C).
8. **Aggregators** — DataCenterMap, Baxtel, Datacenters.com, OCOLO, PeeringDB (C seeds).
9. **Negative evidence** — official hyperscaler region pages (no ET region; Cloud 251/Ethio telecom/Wingu Cloud Exchange are local operators, not hyperscalers).

## Official vs industry pipeline

- Official decides **countability**: ECA licence/registration, EIC permit, IPDC/SEZ record, EEP/EEU power evidence, local permit/land lease, Uptime certification; upgrade to A only when a primary source names the facility/operator and the relevant fact.
- Industry discovers **leads**: operator pages, trade press, vendor cases, crypto/data-mining coverage; lifecycle verbs decide intent vs stronger evidence; crypto/mining needs operator + site + MW to exceed C.
- Division anatomy: Addis Ababa is the high-yield cluster (Ethio ICT Park: Raxio, Wingu, Redfox, crypto-mining; Gola Sefer; Kilinto; Bole Lemi); Oromia (Adama/Dire Dawa-adjacent ring) is low-medium; Amhara/Dire Dawa are expansion leads; Afar/Benshangul-Gumaz/Gambela/Harari/Somali/Sidama/SWEP are negative sweeps; SNNPR bucket must also search South Ethiopia/Central Ethiopia names; Tigray is conflict-affected with stale leads.

## Cross-references

- `SKILL.md` — merged playbook (query templates, confidence rules, division matrix, extraction fields).
- `explorer-official.md` §1 — official sources per pillar; §2 official facility seeds; §4 per-division official strategy; §7 confidence rules.
- `explorer-industry.md` §2 — operator/project sweep; §3 industry-to-official verification pivots; §4 regional search playbook; §7 final evidence rules.
- Watchlist (quarterly): Raxio/Wingu expansions, Safaricom Adama/Dire Dawa, ECA licensing/PDPP portal, IPDC SEZ status, EEP mining-power policy, hyperscaler region pages.
