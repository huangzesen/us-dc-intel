# PN · Country Anatomy

Datacenter-country knowledge layer for Pitcairn (PN).

## Files

| File | Status | Notes |
| --- | --- | --- |
| Country-level skill `SKILL.md` | Present | Merged from the two reviewed explorers (official/regulatory/cloud pipeline + industry/trade-press discovery); working conclusion 2026-08-12: **verified negative** — no commercial DC, colo, cloud region, AI/HPC, IXP, submarine cable or landing station |
| Official / regulatory / cloud pipeline `explorer-official.md` | Present | Final-reviewed: `government.pn` portal, Island Council Minutes, Laws of Pitcairn + legislation.gov.uk (Constitution Order 2010), UK FCDO/GOV.UK, IANA `.pn`/nic.pn, telecom/Starlink context, power & logistics (no airport/deep-water port), official cloud-region absence checks |
| Industry / trade press / vendor discovery `explorer-industry.md` | Present | Final-reviewed: Pitcairn Telecom/local telecom, Starlink & satellite (2022 Adamstown terminal), subsea maps (Telegeography/Submarine Networks), cloud/edge negatives, directory false-positive handling, Pacific media (RNZ, PACNEWS, SubTel Forum, DCD) |
| Division layer `divisions/` | To be added later | PN is manifest type `country` with a single division `Pitcairn` |

## Division layer (future)

Per world-manifest.jsonl, PN is modeled as a **single division: `Pitcairn`** (`subnational_type: country`, `divisions: ["Pitcairn"]`). All official and industry enumeration is handled as one national market; Adamstown leads map to `Pitcairn` and unlocatable-but-PN leads to `Unknown PN`. When the division layer is built, create `divisions/Pitcairn/`; keep no province/region subdivision — locality work is done by island/settlement labels only if a positive candidate ever appears.
