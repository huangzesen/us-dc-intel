# GR · Country Anatomy

Datacenter-country knowledge layer for Greece (GR).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory pipeline | `explorer-official.md` | present |
| Industry / operator / market discovery | `explorer-industry.md` | present |
| Division layer | `divisions/` — 13 regions + Mount Athos exclusion (Eastern Macedonia & Thrace, Central Macedonia, Western Macedonia, Epirus, Thessaly, Ionian Islands, Western Greece, Central Greece, Attica, Peloponnese, North Aegean, South Aegean, Crete; Mount Athos as negative control) | to be added later |

## Source hierarchy

1. **Diavgeia + FEK/et.gr** — mandatory public decisions, environmental approvals, permits, procurement; Grade A.
2. **e-PRM/YPEN + e-adeies/TEE** — environmental records (ΜΠΕ/ΑΕΠΟ/ΠΠΔ) and building permits/pre-approvals; Grade A.
3. **OpenBusiness** — operating-notification framework Law 5069/2023 + JMD 96038/2024 (from 2025-03-01; >=200 kW IT third-party, >=1,000 kW self-use); Grade A.
4. **Strategic investments portal + ΓΕΜΗ** — Microsoft Operations 4733 Hellas three-site Attica record (Spata 19.2 MW; Koropi 9.6 MW x2), SPV resolution; Grade A.
5. **ADMIE / HEDNO / RAEEY / EETT** — grid route/constraints, telecom operator validation; connection requests are not built capacity.
6. **Official operator/cloud pages** — Digital Realty/Lamda Hellix, DATA4, EDGNEX, Grid Telecom/Quadrivium, Lancom, Synapsecom, OTE/Cosmote, Microsoft region pages; Azure Greece Central status must be re-verified every run.
7. **Industry press / directories** — DCD, Kathimerini, Naftemporiki, OT.gr, Business Daily, energypress (B); DataCenterMap, Baxtel, Datacenters.com, Arizton, Mordor (C seeds).

## Official vs industry pipeline

- Official decides **countability**: Diavgeia/e-PRM/e-adeies/OpenBusiness records, strategic-investment approval, ADMIE grid terms, EETT registry; statuses follow Greek lifecycle terms (intent -> ΜΠΕ -> ΑΕΠΟ -> οικοδομική άδεια -> γνωστοποίηση λειτουργίας -> operational).
- Industry discovers **leads and timing**: operator pages, DCD/press (DATA4 groundbreaking, HER1 launch, Dromeus/Apto, Serverfarm/ADMIE), GR-IX/PeeringDB interconnection evidence, cable announcements; every lead back-resolves to official records before counting.
- Division anatomy: Attica is the core hub (Microsoft, Digital Realty, DATA4, EDGNEX, OTE Rentis, Lancom, Synapsecom, GR-IX Athens) with aggressive brand/SPV dedup; Central Macedonia (Thessaloniki) and Crete (HER1, Chania CLS/Quadrivium campus, Tympaki) are secondary; Mount Athos is a negative-control division; island/cable-node regions stay edge/telecom leads.

## Cross-references

- `SKILL.md` — merged playbook (query templates, lifecycle terms, capacity rules, dedup keys).
- `explorer-official.md` §3 — per-division official strategy (13 regions + Mount Athos); §4 reliability rules; §5 recommended official workflow.
- `explorer-industry.md` §2 — operator/project seed list; §4 cloud regions; §5 per-division industry routing; §6 verification and deduplication rules.
- Watchlist (quarterly): Azure Greece Central GA status, Microsoft Attica permit/notification progress, DATA4/Digital Realty HER1 construction status, EDGNEX/Dromeus/Serverfarm licensing, Chania Quadrivium campus, ADMIE grid-connection reporting.
