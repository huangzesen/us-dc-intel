# CX · Country Anatomy

Datacenter-country knowledge layer for Christmas Island (CX).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers; no confirmed commercial DC, confirmed telecom/cable infrastructure, Google AI data-centre lead monitored) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present — DITRDCA Indian Ocean Territories portal & Service Delivery kit, Shire of Christmas Island/WA planning, Vocus ASC cable landing, Google Bosun/Dhivaru & EPBC referral, Telstra/CiFi/nbn/ACMA, AusTender/budget/Home Affairs, IOT Power Service, official cloud-region absence checks |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present — Reuters/ABC/Guardian/Capital Brief/DCD Google AI data-centre lead, Vocus/CiFi/Telstra operator pages, PRL/CIP & IOT Power Service land/power leads, Serco/Home Affairs restricted ICT, Submarine Networks/TeleGeography, DataCenterMap/datacenters/cloudscene/PeeringDB |
| Division layer | `divisions/` — country model with exactly 1 division (Christmas Island); sub-locations Flying Fish Cove/Settlement, Phosphate Hill, Airport, Kampong, Drumsite, North West Point, Silver City/Poon Saan, PRL/CIP as evidence placement | to be added later |

## Division layer (future)

- Christmas Island enumerates at territory level; per world-manifest.jsonl, CX is modeled as `subnational_type="country"` with exactly **1 division: `Christmas Island`** — every confirmed record uses `division: Christmas Island` with `sub_location` for placement.
- Planned: create `divisions/Christmas_Island/` when the division layer is built; keep sub-locations as evidence placement — **Flying Fish Cove / Settlement** (High: ASC landing station, Google cable landing works, government/port/operator facilities), **Phosphate Hill / Quarry Road** (High: IOT Power Service, CIP/PRL, possible data-hub power/land lead), **Airport / XCH / YPXM** (High for rumors: Google reported land/data hub lead), **Kampong / Jalan Pantai** (Medium: IOT Administration ICT), **Drumsite** (Medium: CiFi office/local network), **North West Point** (Medium/restricted: detention-centre ICT contracts — contract level only), **Silver City / Poon Saan / Kampong residential** (Low: verified-negative), **Phosphate mine / PRL / CIP** (Medium: enterprise IT/power).
