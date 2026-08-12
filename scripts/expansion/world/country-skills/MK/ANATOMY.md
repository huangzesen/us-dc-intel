# MK · Country Anatomy

Datacenter-country knowledge layer for North Macedonia (MK).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| Province/state division layer | `divisions/` — 80 municipalities (with Skopje sub-municipalities Aerodrom/Gazi Baba/Centar/Karpos as first-pass market) | to be added later |

## Source hierarchy

- **A (official/primary)**: e-building permit records (gradezna-dozvola.mk), municipal urban-planning files, Official Gazette legal text (No. 134 / 2026-06-18), ministry/government/EU project records, AEK/AEC operator records, ERC/MEPSO/EVN power sources, public-procurement notices (e-nabavki/BJN/MDT/OP-EU), official cloud-region pages, operator-owned facility pages.
- **B (strong secondary)**: MIA/SeeNews/CORD/BalkanEngineer reports, Energy Community/EBRD/World Bank/ITU profiles, Uptime/PeeringDB/interconnection records, vendor case studies with identifiable sites.
- **C (weak lead)**: aggregator directories (DataCenterMap, Inflect, Data Center Platform, Cloudscene, Datacenters.com), social/job ads, market notes, investment-promotion pages without a named facility, unverified street-to-municipality mapping.

## Official vs industry pipeline

- **Official pipeline** (explorer-official.md): e-building permit (E-Odobrenie za gradenje) + municipal planning → 2026 legal recognition of data centers (Gazette No. 134) → environment/EU-project records (ENER, euprojects.mk, IPA) → public procurement (ESJN/BJN/MDT) → AEK telecom-operator evidence → ERC/MEPSO/EVN power trail → cloud-region negative check → operator pages. No hyperscale MK cloud region exists; cloud pages are negative context only.
- **Industry pipeline** (explorer-industry.md): trade press / aggregator / interconnection lead → operator official page or investment-promotion/policy signal → permit/municipal/AEK/procurement/power verification. Policy and investment-promotion language is never counted as a facility without a named site.

## Division layer (future)

- North Macedonia enumerates at municipality granularity (80 municipalities). Practical high-yield order: Skopje municipalities (Aerodrom, Gazi Baba, Centar, Karpos — where Interspace, Telesmart, Neotel/neoDC, Akton, A1 leads sit) → Veles (Net.Bit), Stip (Neotel/neoCloud/Telekabel), Makedonska Kamenica (Data Center DTS), Prilep (government BCDR) → major regional/industrial municipalities (Kumanovo, Tetovo, Gostivar, Bitola, Ohrid, Struga, Gevgelija, Ilinden, Petrovec…) → remaining low-probability municipalities.
- Planned: per-municipality (or per-cluster) skill files covering municipal permit/planning portals, AEK operator records, ESJN procurement routes, and EVN/MEPSO grid contacts.

## Cross-references

- `SKILL.md` §查询模式 routes to explorer-official.md §1/§2 and explorer-industry.md §6 for copy-paste templates; municipality tables in explorer-official.md §7 and explorer-industry.md §7 mirror each other (official vs industry angles on the same municipalities).
- Known operator/project seeds and their validation routes are in explorer-official.md §6 and explorer-industry.md §2 (Interspace, Telesmart, Neotel/neoDC/neoCloud, Net.Bit, Data Center DTS, government BCDR Prilep, Akton, A1, Makedonski Telekom, Telekabel, MARNET).
- Sector manifest: `brief.md` at the country-skills root describes the overall expansion program; this country layer routes MK batches only.
