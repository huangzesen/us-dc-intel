# KI · Country Anatomy

Datacenter-country knowledge layer for Kiribati (KI).

## Files

| File | Status | Notes |
| --- | --- | --- |
| Country-level skill `SKILL.md` | Present | Merged from the two reviewed explorers (official/regulatory/cloud pipeline + industry/trade-press discovery) |
| Official / regulatory / cloud pipeline `explorer-official.md` | Present | Final-reviewed: MICT/CCK, MFED, BNL, MLPID, PUB, World Bank/ADB/JICA project documents, cloud-region absence checks, MTCIC/investment promotion |
| Industry / trade press / vendor discovery `explorer-industry.md` | Present | Final-reviewed: DCD, Submarine Networks, GeoCables, NEC press releases, operators (Vodafone Kiribati, Ocean Link, BNL), satellite providers, directories and PeeringDB checks |
| Island-group division layer `divisions/` | To be added later | KI is manifest type `geographical unit` with 3 divisions (Gilbert Islands, Line Islands, Phoenix Islands) |

## Division layer (future)

Per world-manifest.jsonl, KI is modeled as **geographical unit** with **3 divisions**: **Gilbert Islands** (capital atoll South Tarawa; the population, government, and connectivity centre), **Line Islands** (Kiritimati/Christmas Island is the hub; Teraina and Tabuaeran are low-density), and **Phoenix Islands** (Kanton/Abariringa is the only settlement; most of the division is the Phoenix Islands Protected Area). When the division layer is built, create `divisions/Gilbert_Islands/`, `divisions/Line_Islands/`, and `divisions/Phoenix_Islands/`; evidence should be recorded at islet/town/site granularity (e.g., South Tarawa, Betio, Nanikai, Bonriki; Tabwakea, London, Banana; Kanton/Abariringa) and mapped to its division only when site evidence places it there.
