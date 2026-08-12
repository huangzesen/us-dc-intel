# HM · Country Anatomy

Datacenter-country knowledge layer for **Heard Island and McDonald Islands (HM)**.

## Files

| Layer | File | Status | Note |
|---|---|---|---|
| Country-level skill | `SKILL.md` | present | Merged from the two explorers; entry table, division model, verified-negative conclusion, A/B/C grading, query templates. |
| Official/regulatory/cloud pipeline | `explorer-official.md` | present | AAD (antarctica.gov.au), DCCEEW/legislation, AFMA HIMI Fishery, ACMA RRL, IANA `.HM`/registry.hm, UNESCO, official cloud-region lists; no-market rationale, per-round checklist, verified negatives. |
| Industry/trade press/vendor discovery | `explorer-industry.md` | present | Data-center/cloud directory negative checks, network/cable/telecom surfaces (Submarine Cable Map, APNIC, PeeringDB, BGP), fishery/vessel/research exclusions, industry query templates, false-positive list. |
| Division layer | `divisions/` | — | Single division `Heard Island and McDonald Islands`; planned `divisions/Heard Island and McDonald Islands/` creation. |

## Division layer (future)

- World manifest (`world-manifest.jsonl`) models HM as `subnational_type: country` with exactly one division: `Heard Island and McDonald Islands` (Australian external territory, managed by the Australian Antarctic Division, unoccupied by humans, World Heritage and marine reserve).
- All confirmed records (currently none expected) must use `division: Heard Island and McDonald Islands`. Geographic sub-areas (Atlas Cove, Spit Bay, Magnet Point, McDonald Islands/Shag Islet/Morgan Island/Sail Rock, HIMI Marine Reserve) are tagging labels only, never division values.
- Planned: `divisions/Heard Island and McDonald Islands/` with sub-location notes (search buckets only, never divisions), carrying the verified-negative baseline and the upgrade rule (A-grade source naming facility name + function + location + operator, with false-positive exclusions: AADC, AAT stations, Kerguelen, McDonald's brand, vessel systems, temporary research equipment).
