# AZ · Country Anatomy

Datacenter-country knowledge layer for Azerbaijan (AZ).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| Province/state division layer | `divisions/` — rayons / municipalities / autonomous republic (Nakhchivan) from world-manifest.jsonl | to be added later |

## Source hierarchy

- **A (official/primary)**: MINCOM/ICTA operator register, Uptime Institute certification lists, AzInTelecom official pages, EIB/IFI financing pages, presidential/cabinet/state-company announcements, State Committee on Urban Planning / e-construction records, e-procurement awards (etender.gov.az), AzerEnergy/Azerishiq/AERA sources, official cloud-region pages, operator-owned facility pages.
- **B (strong secondary)**: AZERTAC, APA, Trend, AzerNews, DCD, Telecompaper, vendor case studies quoting named officials/operators or republishing official project facts.
- **C (weak lead)**: directories (Datacenters.com, DataCenterMap, Data Center Catalog, Cloudscene, Inflect), marketplace pages, PeeringDB/IX-only records, blogs, social posts, market reports without facility-level evidence.

## Official vs industry pipeline

- **Official pipeline** (explorer-official.md): MINCOM/ICTA entity registration → Uptime certification sweep → AzInTelecom/Government Cloud official pipeline (Baku + Yevlakh operating; Absheron/Gobustan + Hajigabul/Pirsaat green DCs via EIB EUR 43m loan) → urban-planning/e-construction permits → e-procurement → AERA/AzerEnergy/Azerishiq energy & sustainability validation → cloud/edge negative checks (no hyperscale AZ region).
- **Industry pipeline** (explorer-industry.md): trade press (DCD/AZERTAC/APA/Trend/AzerNews) and directory/PeeringDB leads → operator official page or Uptime/certification corroboration → MINCOM registration + facility page → state/IFI/procurement/construction source. Directory leads are promoted only after certification, official page, or strong named-operator trade coverage.

## Division layer (future)

- Azerbaijan enumerates at rayon / municipality / autonomous-republic granularity. Tier 1 (exhaustive official sweep): Baku, Yevlakh City, Absheron, Gobustan, Hajigabul, Goychay, Agdash, Sumgayit, Nakhchivan. Tier 2 (state infrastructure / regional validation): Ganja, Mingachevir, Shirvan, Lankaran, Shaki, Naftalan, Khizi, Salyan, Astara, Fuzuli, Shusha, Zangilan, Aghdam and others — expect many no-project outcomes. Tier 3: all remaining rayons, negative-control sweep.
- Locality vs project-region conflicts must be preserved: Absheron project ↔ Uptime locality Gobustan; Hajigabul project ↔ Uptime locality Pirsaat; Yevlakh City vs Yevlakh district.
- Planned: per-division (or per-cluster) skill files covering MINCOM/ICTA registry queries, Uptime checks, AzInTelecom state-cloud pages, arxkom/e-construction permits, etender procurement, and AzerEnergy/Azerishiq grid contacts.

## Cross-references

- `SKILL.md` §查询模式 routes to explorer-official.md §1-§5 and explorer-industry.md §3 for copy-paste templates; the per-division official workflow (explorer-official.md §6) mirrors the per-division industry workflow (explorer-industry.md §4); alias tables in both files (explorer-official.md §6.3, explorer-industry.md §5) are the same mapping from manifest divisions to local spellings.
- Known facility seeds and validation anchors are in explorer-official.md §2/§6 and explorer-industry.md §2 (AzInTelecom MDC/RDC/New DPC/Absheron/Hajigabul, CBAR, DGK, Delta DTMDC, PASHA BMDC/GDRS, Azerconnect Baku/Agdash, STDC Sumgayit, Nakhchivan).
- Sector manifest: `brief.md` at the country-skills root describes the overall expansion program; this country layer routes AZ batches only.
