# KM · Country Anatomy

Datacenter-country knowledge layer for Comoros (Union des Comores) (KM).

## Files

| File | Status | Notes |
| --- | --- | --- |
| Country-level skill `SKILL.md` | Present | Merged from the two reviewed explorers (official/regulatory/cloud pipeline + industry/trade-press discovery) |
| Official / regulatory / cloud pipeline `explorer-official.md` | Present | Final-reviewed: Journal Officiel, ANRTIC, ANADEN, Comores Câbles, AfDB PADEC, IsDB/World Bank, Cour Suprême audits, SONELEC, certification registries, cloud-region absence checks |
| Industry / trade press / vendor discovery `explorer-industry.md` | Present | Final-reviewed: operators (Comores Telecom, Yas Comores/AXIAN), Comores Câbles landing stations, cable systems (EASSy/Avassa/FLY-LION3/2Africa/domestic), trade press, directory-to-primary workflow |
| Island-group division layer `divisions/` | To be added later | KM is manifest type `geographical unit` with 3 divisions (Anjouan, Grande Comore, Moheli) |

## Division layer (future)

Per world-manifest.jsonl, KM is modeled as **geographical unit** with **3 divisions**: **Anjouan** (Ndzuwani/Nzwani; Mutsamudu cable landing and telecom PoPs; no public DC found in review), **Grande Comore** (Ngazidja; the confirmed national/public-administration data centre plus Moroni/Itsandra cable and operator infrastructure), and **Moheli** (Mwali; Fomboni landing and telecom PoPs only). When the division layer is built, create `divisions/Anjouan/`, `divisions/Grande_Comore/`, and `divisions/Moheli/`; keep commune-level locations (e.g., Moroni-Bambao vs Itsandra within Grande Comore) as sub-location notes, not divisions, and keep Mayotte (France) out of scope entirely.
