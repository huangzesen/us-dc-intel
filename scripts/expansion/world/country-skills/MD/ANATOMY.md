# MD · Country Anatomy

Datacenter-country knowledge layer for the Republic of Moldova (MD).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| Province/state division layer | `divisions/` — districts, municipalities, Gagauzia, and the left-bank territorial unit (Stinga Nistrului / Transnistria) | to be added later |

## Source hierarchy

- **A (official/primary)**: operator-owned facility pages with address/services, local permit/urbanism records (Chisinau/DGAURF, certificat de urbanism / autorizatie de construire), Environmental Agency EIA/decisions, ARCOM/ANRCETI provider register (legal identity), STISC/government records naming government datacenter work, Moldelectrica/ANRE connection/regulatory records.
- **B (strong secondary)**: PeeringDB facility/IX data (Data City fac 15521, MD-IX ix 392), PCH, Internet Society Pulse, established trade press, processed official datasets, credible operator marketplace pages, DataCenterMap pages with operator/address detail.
- **C (weak)**: VPS directories, generic “cloud in Moldova” SEO pages, IP-geolocation claims, forums, weak facility marketplaces, social posts without source documents.

## Official vs industry pipeline

- **Official pipeline** (explorer-official.md): construction/urbanism permit (certificat de urbanism → autorizatie de construire) + Environmental Agency EIA → ARCOM provider register → Moldelectrica/ANRE/Premier Energy grid evidence → MTender/tender.gov procurement + STISC/MCloud government-cloud records → official cloud-region negative checks (no MD hyperscale region).
- **Industry pipeline** (explorer-industry.md): operator/directory/IXP lead → operator-owned page → PeeringDB/IXP/facility confirmation → ARCOM legal-entity check → Chisinau/local permit and environmental searches → grid/utility checks. Interconnection records prove live connectivity, not datacenter ownership; MCloud and STISC’s future national datacenter are separate workstreams.

## Division layer (future)

- Moldova is a Chisinau-centric market. Chisinau gets the deepest pass (Moldtelecom Data City, MoldData/Host.md, Trabia/KIVIX, AlexHost, IP HOST, AvenaCloud, Cogent, Orange, StarNet, Mezon). Government site-search watchlist: Balti, Ungheni, Falesti, Stauceni (STISC Tier III AI-Ready national datacenter — planned until final land selection). Higher-yield non-Chisinau: Ialoveni/Straseni (spillover/logistics belt), Cahul, Gagauzia, left-bank/Transnistria (Russian-language hosting/colo/mining leads with separate confidence grading). All other districts get fast negative screens.
- Planned: per-division (or per-cluster) skill files covering local permit portals, ARCOM register pivots, STISC/MTender surfaces, and Moldelectrica/Premier/RED Nord grid contacts.

## Cross-references

- `SKILL.md` §查询模式 routes to explorer-official.md §1/§4 and explorer-industry.md §4 for copy-paste templates; the official division strategy (explorer-official.md §4) mirrors the industry per-division patterns (explorer-industry.md §4); both share the operator seed tables (explorer-official.md §4.1, explorer-industry.md §2).
- Known seeds and validation routes: explorer-official.md §4 and explorer-industry.md §2/§5 (Moldtelecom Data City, MoldData/Host.md, Trabia, AlexHost, IP HOST, AvenaCloud, Cogent CNDC, MCloud/STISC national datacenter, Imperial Hosting/Transnistria) plus dedup rules in explorer-industry.md §5.
- Sector manifest: `brief.md` at the country-skills root describes the overall expansion program; this country layer routes MD batches only.
