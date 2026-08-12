# BI · Country Anatomy

Datacenter-country knowledge layer for Burundi (BI).

## Files

| Layer | File | Status | Notes |
|---|---|---|---|
| Country-level skill | `SKILL.md` | present-merged | Merged methodology: official (ARCT/SETIC-PAFEN-PDDSP/BBS/operators/energy) + industry (press/operator/interconnection) pipelines; 5-province normalization + 18 legacy names for recall |
| Official pipeline | `explorer-official.md` | present | ARCT, SETIC/PAFEN/PDDSP/eNama, BBS, operators (ONATEL/Lumitel/Econet/CNI-NIC.BI), OBPE/REGIDESO/AREEN, cloud-region negative controls, seed list, province workflow |
| Industry pipeline | `explorer-industry.md` | present | Local press (Iwacu/Burundi Eco/ABP), African/international trade press, operator/hoster/vendor sweep, IXP and aggregator handling, FR/EN/Kirundi templates, grading rules |
| Division layer | `divisions/` | to be added later | 5 current provinces (Buhumuza, Bujumbura, Burunga, Butanyerera, Gitega) with legacy 18-province search mapping; Bujumbura commercial cluster, Gitega government/education leads |

## Division layer (future)

- Enumeration granularity: province. Normalize final records to the current 5-province model (2025 reform); use legacy 18 names for search recall; never state "17 provinces" without noting it is an obsolete pre-Rumonge schema.
- Legacy 18 names: Bubanza, Bujumbura Mairie, Bujumbura Rural, Bururi, Cankuzo, Cibitoke, Gitega, Karuzi, Kayanza, Kirundo, Makamba, Muramvya, Muyinga, Mwaro, Ngozi, Rumonge, Rutana, Ruyigi.
- Priority provinces: Bujumbura (SETIC government hosting, BBS hosting, ONATEL, Lumitel, Econet, CNI/NIC.BI, BDIXP, banks); Gitega (CIU at Universite Polytechnique de Gitega, PAFEN/BERNET, possible CDIN); Butanyerera (Ngozi/Kayanza/Kirundo regional PoPs); Buhumuza and Burunga (backbone/border/power leads, negative commercial expected).
- Planned per-division files: `divisions/{province}.md` with seeds, queries, and status per the two explorers' province tables.

## Cross-references

- Parent folder: `scripts/expansion/world/country-skills/` (per-country SKILL.md/ANATOMY.md conventions mirror IN/DE/GB/FR/KR and batches 2-7).
- Division names (current 5): Buhumuza, Bujumbura, Burunga, Butanyerera, Gitega. Legacy search set (18): as above; note Rumonge (2015-2025) and the obsolete 17-province schema.
