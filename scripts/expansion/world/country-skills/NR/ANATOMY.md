# NR · Country Anatomy

Datacenter-country knowledge layer for Nauru (NR).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / government pipeline | `explorer-official.md` | present |
| Industry / cable / operator discovery | `explorer-industry.md` | present |
| District division layer | `divisions/` — 14 districts (Aiwo, Anabar, Anetan, Anibare, Baitsi/Baiti, Boe, Buada, Denigomodu, Ewa, Ijuw, Meneng, Nibok, Uaboe, Yaren; plus Unknown NR) | to be added later |

## Source hierarchy

1. **Government ICT** — nauru.gov.nr (Department of ICT, ICT Center/Yaren, Digital Transformation Strategy, GIO media/gazette), Grade A for government server-room leads.
2. **Law/regulation** — RONLAW; Communications and Broadcasting Act 2018 (current, repealed 2017 Act); Nauru Cable Corporation Act 2017 (NFCC mandate).
3. **Cable project** — eastmicronesiacable.com, naurufibrecable.com, AIFFP, DFAT, ADB/WB documents, nem Australasia (B+), NEC (B+); EMC Nauru CLS landed 2025-08-09, expected RFS Nov 2025.
4. **Power** — NUC (https://www.nuc.com.nr), annual reports (11.6 MW firm / 5.3 MW max demand), tenderlink portal; hard filter for any MW-scale claim.
5. **Operators** — Cenpac Net Inc (Aiwo Civic Centre, .nr registry, ISP since 1998), Digicel Nauru (operator presence only); ITU 2017 country profile for market structure.
6. **Negative evidence** — official hyperscaler region pages (no NR region); Data Center Map country page as negative-check source.

## Official vs industry pipeline

- Official decides **countability**: government ICT pages, RONLAW acts, EMC/NFCC/AIFFP/DFAT project documents, NUC power records; minimum standard is one Grade A facility/project source or operator page plus one independent A/B corroborator; district tagging requires a source address/district or documented geocoding.
- Industry discovers **signals**: cable status (RFS), operator pages (Cenpac/Digicel), trade press, Chinese-language rumor watch (C until corroborated); everything else is a verified-negative sweep.
- Division anatomy: treat Nauru as one market; only Yaren (ICT Center) and Aiwo (Cenpac, NUC Power House) have source-supported district anchors; CLS stays Unknown NR until pinned by source/imagery; remaining 12 districts are keyword-sweep coverage (Baitsi/Baiti both spellings).

## Cross-references

- `SKILL.md` — merged playbook (query templates, grades, candidate schema, false positives).
- `explorer-official.md` §1 — official source register; §3 per-division official strategy; §6 first-pass workflow.
- `explorer-industry.md` §1 — cable industry sources; §2 operator sources; §6 verified negatives; §7 sweep order.
- Watchlist (quarterly): EMC RFS status, CLS district pin, Cenpac hosting evidence, Digicel core location, NUC load growth, donor-funded national hosting projects.
