# CI · Country Anatomy

Datacenter-country knowledge layer for Côte d'Ivoire (CI).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / primary pipeline | `explorer-official.md` | present |
| Industry / operator / trade-press discovery | `explorer-industry.md` | present |
| District division layer | `divisions/` — 14 districts (Abidjan; Yamoussoukro; Bas-Sassandra; Comoé; Denguélé; Gôh-Djiboua; Lacs; Lagunes; Montagnes; Sassandra-Marahoué; Savanes; Vallée du Bandama; Woroba; Zanzan) | to be added later |

## Source hierarchy

1. **Ministry of Digital Transition / telecom.gouv.ci + EXIM/USG** — Data Center National (Anoumambo/AIGF, Abidjan), A-grade project evidence.
2. **ARTCI + data-protection portal** — licence holders, telecom authorisations, data-protection decisions (Loi 2013-450); not a facility registry.
3. **SIGUPC/GUPC + district portals (abidjan.district.ci, districtyakro.ci, vitib.ci)** — building permits and free-zone records.
4. **ANARE-CI / CI-ENERGIES / CIE** — power evidence (MV supply, transformers, generators, fuel storage).
5. **ANDE/EIES + ANSSI** — environmental disclosures and state-hosting/cybersecurity context.
6. **CEPICI / IDU / e-Licences / public procurement** — company registry (PAIX DATA CENTRES object) and state procurement.
7. **Operator pages / PeeringDB / Uptime** — Raxio CIV1, Equinix/MainOne AB1 & AB1.2, ST Digital CIV01, PAIX ABJ1, Orange, MTN; PeeringDB fac/12168, fac/6246, fac/15646; Uptime country page.
8. **Trade press / aggregators** — DCD, Capacity, Connecting Africa, The Tech Capital, Ecofin, TechAfrica, FratMat, AIP, Abidjan.net (B); Datacenter Map, Baxtel, OCOLO, Datacenters.com, Systalink (C seeds).
9. **Negative evidence** — official hyperscaler region pages (no CI region; re-check every run).

## Official vs industry pipeline

- Official decides **countability**: ministry/EXIM project records, ARTCI licences, SIGUPC permits, VITIB zone records, CIE/CI-ENERGIES power, ANDE/EIES, IDU/CEPICI registry, Uptime certification.
- Industry discovers **leads and timing**: operator deep dives (Raxio launch, ST Digital inauguration 2025-10-02, MainOne/AB1.2, PAIX), trade press, interconnection feeds (MainOne landing, 2Africa/MTN GlobalConnect, CIVIX); capacity numbers need operator/official corroboration.
- Division anatomy: Abidjan (Data Center National, PAIX ABJ1, MTN, local hosters) and Comoé (Raxio CIV1, Equinix/MainOne AB1/AB1.2, ST Digital, Orange Grand-Bassam lead — VITIB records) are the positive districts; the other 12 are negative-sweep districts (Savanes and Vallée du Bandama as future edge/DR candidates).

## Cross-references

- `SKILL.md` — merged playbook (query templates, status normalization, dedup rules, 14-district sweep).
- `explorer-official.md` — verified official sources, facility seeds with correct district attribution, per-district strategy, record extraction checklist, URL validation notes.
- `explorer-industry.md` — operator deep dives, connectivity/interconnection feeds, verification pipeline, common pitfalls.
- Watchlist (quarterly): Data Center National commissioning, Raxio CIV1 Uptime record/rack reconciliation, Equinix AB1 vs AB1.2 identity, Orange CI official page, MTN Business colo evidence, PAIX current facility page, hyperscaler region pages.
