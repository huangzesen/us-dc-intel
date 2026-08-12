# DZ · Country Anatomy

Datacenter-country knowledge layer for Algeria (DZ).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| Province/state division layer | `divisions/` — 58 wilayas (incl. 2019 split wilayas needing parent-wilaya locality checks) | to be added later |

## Source hierarchy

- **A (official/primary)**: ARPCE authorisation or operator list, ministry / wilaya / commune / university / public-enterprise pages, BOMOP/ANEP tenders, official procurement pages, AAPI/urbanism procedures, Sonelgaz/CREG evidence, official cloud-region pages, official operator facility pages, Uptime certification records.
- **B (strong secondary)**: APS (carried by official agency partners), DCD, Agence Ecofin / We Are Tech, Telecompaper, reputable Algerian national press, vendor/integrator project pages with named client and site.
- **C (weak lead)**: tender aggregators (DZtenders, Algerie Marches…), DataCenterMap / Baxtel / datacenters.com / Cloudscene, social posts, market reports, inaccessible snippets, directory pages, unverified local press.

## Official vs industry pipeline

- **Official pipeline** (explorer-official.md): ARPCE cloud/hosting authorisation → MPT / HCN-Huawei / Algerie Telecom / Algerie Poste ministry & state announcements → BOMOP/ANEP public tenders (ministries, universities, OPGI, wilayas) → AAPI/APC/wilaya urbanism & permits → Sonelgaz/CREG/ELIT power context → official cloud-region negative checks (no DZ hyperscale region).
- **Industry pipeline** (explorer-industry.md): trade press (DCD/APS/Ecofin/Telecompaper/DC Mag) and directory leads → official operator pages / ARPCE authorisation → BOMOP/ministry/urbanism/Uptime verification → Sonelgaz/power corroboration. Every industry lead has a prescribed official verification route (explorer-industry.md §4); directory-only entries stay Grade C.

## Division layer (future)

- Algeria enumerates at wilaya granularity (58 wilayas). Highest priority: Alger (Mohammadia national DC, Sidi Abdellah Cyber Parc, Cheraga, APN), Blida (second national DC), Constantine (Algerie Telecom DC), Oran (MPT AI data center), Ouargla/Hassi Messaoud (Sonatrach industrial compute), Tizi Ouzou (UMMTO HPC/AI), Djelfa (OPGI secondary DC), Tiaret (postal complex), Bejaia (Djezzy Cloud/Amizour lead), Bouira/Lakhdaria (planned), Annaba/Skikda (port/hosting). Medium priority: Batna, Laghouat, Guelma, Khenchela, Medea (university HPC), Setif, Tlemcen, Chlef. All remaining wilayas get negative-search sweeps.
- 2019 split wilayas (Timimoun, Bordj Badji Mokhtar, Ouled Djellal, Beni Abbes, In Salah, In Guezzam, Touggourt, Djanet, El Meghaier, El Meniaa) must be assigned only when the physical commune/locality supports the current wilaya.
- Planned: per-wilaya (or per-cluster) skill files covering ARPCE authorization queries, ministry/university tender pages, AAPI/urbanism routes, and Sonelgaz/CREG grid contacts.

## Cross-references

- `SKILL.md` §查询模式 routes to explorer-official.md §1/§3 and explorer-industry.md §0/§5 for copy-paste templates; the official five-pass wilaya workflow (explorer-official.md §3.1) mirrors the industry wilaya matrix (explorer-industry.md §5); both share the same 58-wilaya manifest and alias conventions.
- Known seeds and calibration examples: explorer-official.md §2/§3.2 and explorer-industry.md §2/§6 (Mohammadia, Blida, Constantine, Oran, OPGI Djelfa, UMMTO, AYRADE, ICOSNET, ISSAL, eBS/WebServices, ADEXCLOUD, Djezzy Cloud, Sonatrach, ELIT).
- Sector manifest: `brief.md` at the country-skills root describes the overall expansion program; this country layer routes DZ batches only.
