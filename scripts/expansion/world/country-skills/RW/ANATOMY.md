# RW · Country Anatomy

Datacenter-country knowledge layer for Rwanda (RW).

## Files

| File | Status | Notes |
| --- | --- | --- |
| Country-level skill `SKILL.md` | Present | Merged from the two reviewed explorers (official/regulatory/cloud pipeline + industry/trade-press discovery) |
| Official / regulatory / cloud pipeline `explorer-official.md` | Present | Final-reviewed: RURA licensing/statistics/RINEX, MINICT, RISA/RDAP, NCSA, Data Protection Law 058/2021 + DPO, RPPA UMUCYO, RDB/KIC, REG/REMA energy, cloud-region absence checks |
| Industry / trade press / vendor discovery `explorer-industry.md` | Present | Final-reviewed: local press (The New Times, IGIHE, KT Press), African/international trade press (DCD, Connecting Africa, Agence Ecofin, The Stack, Datacentre Magazine), operators/vendors (TrAC, PAIX, ADC, Raxio, MTN, Airtel, Liquid, BSC, Paratus, AOS), RINEX/PeeringDB, aggregators |
| City/province division layer `divisions/` | To be added later | RW is manifest type `city/province` with 5 divisions (City of Kigali, Eastern, Northern, Western, Southern) |

## Division layer (future)

Per world-manifest.jsonl, RW is modeled as **city/province** with exactly **5 divisions**: **City of Kigali** (Gasabo, Kicukiro, Nyarugenge — the only commercial/telecom cluster; Kacyiru hosts Telecom House, RINEX, NCSA, TrAC), **Eastern** (Bugesera, Gatsibo, Kayonza, Kirehe, Ngoma, Nyagatare, Rwamagana — Rwanda Space Agency teleport at Mwulire, Bugesera airport, Tanzania-border fibre corridor), **Northern** (Burera, Gakenke, Gicumbi, Musanze, Rulindo — low datacenter yield), **Western** (Karongi, Ngororero, Nyabihu, Nyamasheke, Rubavu, Rusizi, Rutsiro — Lake Kivu methane-gas power as energy context), and **Southern** (Gisagara, Huye, Kamonyi, Muhanga, Nyamagabe, Nyanza, Nyaruguru, Ruhango — Huye UR campus, Kamonyi MTN 5G sites). When the division layer is built, create `divisions/City_of_Kigali/`, `divisions/Eastern/`, `divisions/Northern/`, `divisions/Western/`, and `divisions/Southern/`; keep district (akarere) names as the second-level search and address-resolution layer.
