# CK · Country Anatomy

Datacenter-country knowledge layer for Cook Islands (CK).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers; non-zero small market: Vodafone telco hosting, CIG government colocation, Manatua cable landing) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present — PPCI procurement (RFT Data Centre Colocation tender=3374, HCI/ICT upgrade tender=3361), MFEM, OPM (Digital Strategy/ICT policy), CRA telecom regulator, CIIC/ACL (Avaroa Cable/Manatua), TAU power, ADB renewable energy, official cloud-region absence checks |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present — Vodafone Cook Islands (Data Housing & Hosting, Aitutaki upgrade via LinkedIn), APAC Outlook (Avarua/Aroa/Aitutaki), Aiscorp, Submarine Networks/GeoCables/commsupdate/Developing Telecoms/RNZ/Cook Islands News, PeeringDB/PCH, DataCenterMap/Cloudscene/Baxtel |
| Division layer | `divisions/` — country model with exactly 1 division (Cook Islands); site clusters Rarotonga/Aitutaki/Pa Enua as search and evidence placement | to be added later |

## Division layer (future)

- Cook Islands enumerates at territory level; per world-manifest.jsonl, CK is modeled as `subnational_type="country"` with exactly **1 division: `Cook Islands`** — every confirmed record uses `division: Cook Islands` with `island/site` as second-level field.
- Planned: create `divisions/Cook_Islands/` when the division layer is built; keep site clusters as search/evidence layers — **Rarotonga-Avarua/Parekura** (P1: OPM/CIG colocation, Vodafone HQ/Data Housing, CRA, government procurement), **Rarotonga-Aroa/Rutaki/Avatiu** (P1: Vodafone Aroa DC lead, Manatua landfall/CLS, TAU/Avatiu power), **Aitutaki/Arutanga** (P1/P2: Manatua domestic landing, Vodafone Aitutaki DC upgrade), **Southern Group** (Atiu/Mangaia/Mauke/Mitiaro — P2/P3, record negatives), **Northern Group** (Penrhyn/Manihiki/Pukapuka/Rakahanga/Nassau — P2/P3, record negatives), **uninhabited/special** (Takutea/Manuae/Palmerston/Suwarrow — P3, usually no_projects).
