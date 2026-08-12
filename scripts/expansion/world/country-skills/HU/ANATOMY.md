# HU · Country Anatomy

Datacenter-country knowledge layer for Hungary (HU).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| Province/state division layer | `divisions/` — counties / cities with county rights / capital city | to be added later |

## Source hierarchy

- **A (official/primary)**: national or local authority records, NMHH telecom-construction notices, official environmental records (OKIR), MAVIR/DSO/MEKH records, EKR / Public Procurement Authority notices, official cloud-provider infrastructure pages, official operator pages (Telekom, 2Connect, VIVAnet, RackForest), CERN/EuroHPC/university primary pages for research/HPC scope.
- **B (strong secondary)**: established trade press (DCD, Portfolio, hwsw, bitport…), operator-linked contractor case studies, HIPA/association material, Uptime/certification records.
- **C (weak lead)**: directories (DataCenterMap, Baxtel, Inflect, Datacenters.com, Cloudscene), marketplace pages, generic hosting pages without facility detail, old press, market-report snippets, unverified capacity claims.

## Official vs industry pipeline

- **Official pipeline** (explorer-official.md): E-epites/OENY/ETDR building-authority workflow (epitesi engedely → hasznalatbaveteli engedely) + local/county government notices → NMHH telecom-construction permits → OKIR environmental records → MAVIR/DSO/MEKH power evidence → EKR/Kozbeszerzes/TED procurement (NISZ/FEAK/IdomSoft) → official cloud-region checks (no public HU hyperscale region; Oracle eu-budapest-1/IdomSoft = sovereign-region lead).
- **Industry pipeline** (explorer-industry.md): trade press/directory/operator lead → operator official page or certification → NMHH permit / EKR procurement / ETDR-local permit / OKIR / MAVIR confirmation. Directory leads stay C/C+ until confirmed by an operator or official source; press leads stay B until operator/official confirmation.

## Division layer (future)

- Hungary enumerates at county / city-with-county-rights / capital-city granularity. Priority divisions: Budapest (districts XIII/VIII/XI/X/XIV/IX), Pest (Budaors, Torokbalint, Dunakeszi/Fot, Vecses, Szigetszentmiklos, Biatorbagy — many “Budapest” listings physically belong here), Debrecen/Hajdu-Bihar (DP Data Center, BMW DC1, Komondor HPC), Gyor (Adatpark, Audi), Szeged (Adatpark, Rackhost, University), Pecs, Nyiregyhaza, Szolnok, Eger, Szombathely, Zalaegerszeg (ZalaZONE EMAK), Tolna/Paks (planned AI/energy campus). Remaining divisions get universal-template negative sweeps plus local industrial/university pivots.
- Facility classes must be separated: commercial colocation/hosting, telecom datacenter, hosting-provider facility, public-sector datacenter, research/HPC, enterprise/campus server room, planned AI/energy campus.
- Planned: per-division (or per-cluster) skill files covering ETDR/E-epites public search routes, kormanyhivatalok/city-portal notice surfaces, NMHH permit pivots, MAVIR/DSO grid contacts, and EKR procurement surfaces.

## Cross-references

- `SKILL.md` §查询模式 routes to explorer-official.md §1/§4 and explorer-industry.md §1/§4 for copy-paste templates; the official four-pass division method (explorer-official.md §4) mirrors the industry county/city patterns (explorer-industry.md §4); both share the same division seeds tables (explorer-official.md §4.1, explorer-industry.md §4).
- Known seeds and verification anchors: explorer-official.md §3 and explorer-industry.md §2 (Telekom Dataplex/Adatpark addresses, 2Connect/Invitech footprint, RackForest/VIVAnet/Servergarden, Datacenter.hu/DP Data Center, Wigner/CERN, NISZ/FEAK/IdomSoft, BMW Debrecen DC1, KBC Torokbalint).
- Sector manifest: `brief.md` at the country-skills root describes the overall expansion program; this country layer routes HU batches only.
