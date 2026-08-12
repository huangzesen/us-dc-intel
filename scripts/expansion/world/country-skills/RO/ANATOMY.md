# RO · Country Anatomy

Datacenter-country knowledge layer for Romania (RO).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| Province/state division layer | `divisions/` — 41 counties (judete) + Bucuresti municipality | to be added later |

## Source hierarchy

- **A (official/primary)**: operator official facility pages, local construction-permit records (AC/CU/PUZ/PUD registers), ANMAP/ANPM county environmental decisions, SEAP/SICAP procurement contracts/awards, STS/ADR government-cloud and regional-program pages, Uptime/official certification for named facilities, official cloud/interconnect pages (Google Cloud Interconnect NXDATA-1 Bucharest BU1).
- **B (strong secondary)**: DCD, Profit.ro, Economica, Balkan Green Energy News, Romania Insider, Business Forum, Panorama, DataCenter Forum, local press with named officials, vendor case studies (Tema Energy, Datanet).
- **C (weak lead)**: Baxtel, Data Center Map, Datacenters.com, Inflect, DC Hub, ColoMap, DataCenterCatalog, generic market reports — address/operator seeds only.

## Official vs industry pipeline

- **Official pipeline** (explorer-official.md): local construction permit (CU → AC) + county ANMAP/ANPM environmental file → SEAP/SICAP procurement + ADR/STS government-cloud and regional-program records → Transelectrica/ANRE/DSO grid evidence → ANCOM telecom context → official cloud-region checks (no RO hyperscale region).
- **Industry pipeline** (explorer-industry.md): directory/trade/operator lead → operator page or official cloud/interconnect page → city/county permits → ANMAP environmental record → SEAP/funding record → grid/utility context. Upgrade requires at least two independent evidence types; directories stay C/C+ until confirmed.

## Division layer (future)

- Romania enumerates at county + Bucuresti municipality granularity. Priority clusters: Bucuresti + Ilfov (NXDATA, GTS, Voxility, Orange, Portland Trust, Solidus, Microsoft/Otopeni lead, Google Interconnect NXDATA-1); Dolj + Valcea (ClusterPower Mischii/Fauresti, Digital Cuisine); Timis (Giroc government cloud, SANY/Uivar, Orange Timisoara); Brasov + Sibiu (STS government-cloud nodes, STS CDS II Sibiu, Orange Brasov); Cluj + Mures + Bistrita-Nasaud (GTS Cluj, DriverAI Luna, Vidrasau, regional cloud leads); Prahova + South-Muntenia (regional data center, likely Ploiesti host); Iasi, Bihor (HZone Oradea), Giurgiu (Pidgin Host), Constanta, Galati, Tulcea (DANUBIUS-RO), plus public/research leads (BNR Targu Jiu, university HPC). Remaining counties get Romanian-language negative sweeps.
- Physical assignment: many “Bucharest” listings belong to Ilfov localities (Tunari, Otopeni, Chiajna, Voluntari, ring-road municipalities); South-Muntenia partner counties are beneficiaries, not separate facilities.
- Planned: per-county (or per-cluster) skill files covering local AC/CU registers, ANMAP/ANPM county hosts, SEAP procurement surfaces, and DSO/Transelectrica grid contacts.

## Cross-references

- `SKILL.md` §查询模式 routes to explorer-official.md §1/§4 and explorer-industry.md §1/§2 for copy-paste templates; the official division strategy (explorer-official.md §3) mirrors the industry three-pass county sweep (explorer-industry.md §4); both share the county-level template sets (explorer-official.md §4, explorer-industry.md §2).
- Known seeds and upgrade paths: explorer-official.md §2.4/§3 and explorer-industry.md §2/§6 (NXDATA, GTS, Voxility, Orange/ex-Telekom lineage, Portland Trust, ClusterPower/AIC, SANY, HZone, DataPark, Pidgin Host, INVITE, STS/ADR government cloud).
- Sector manifest: `brief.md` at the country-skills root describes the overall expansion program; this country layer routes RO batches only.
