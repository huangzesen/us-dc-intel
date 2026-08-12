# MW · Country Anatomy

Datacenter-country knowledge layer for Malawi (MW).

## Files

| File | Status | Notes |
| --- | --- | --- |
| Country-level skill `SKILL.md` | Present | Merged from the two reviewed explorers (official/regulatory/cloud pipeline + industry/trade-press discovery) |
| Official / regulatory / cloud pipeline `explorer-official.md` | Present | Final-reviewed: MACRA/DPA, Ministry of Information e-Government, PPPC/DIGMAP, PPDA/PPPC/RBM procurement, MERA/ESCOM/EGENCO power, MITC/SEZ, council planning, cloud-region absence checks |
| Industry / trade press / vendor discovery `explorer-industry.md` | Present | Final-reviewed: operators (Government DC, Huawei NDC, OCL, MTL, TNM, Airtel, CTN, Korena/1nga), MIX-BT/PeeringDB, trade press (DCD, ITWeb Africa, Capacity, Canonical), directory-to-primary workflow |
| Region division layer `divisions/` | To be added later | MW is manifest type `region` with 3 divisions (Central Region, Northern Region, Southern Region) |

## Division layer (future)

Per world-manifest.jsonl, MW is modeled as **region** with **3 divisions**: **Central Region** (capital Lilongwe; Government Data Centre primary, National Data Centre expansion, OCL Kanengo, MTL, CTN — highest yield), **Northern Region** (Mzuzu, Karonga, Rumphi, Nkhata Bay; only academic concept leads, expected 0–1 records, record `no_projects` honestly), and **Southern Region** (commercial capital Blantyre, Zomba, Thyolo, Mangochi; National Data Centre Blantyre secondary/backup, RBM Corporate Data Centre tender, Airtel 2013 DC, Korena/1nga claim, ESCOM lead — medium-high yield). When the division layer is built, create `divisions/Central_Region/`, `divisions/Northern_Region/`, and `divisions/Southern_Region/`; keep 28-district and city-level locations (Lilongwe, Blantyre, Mzuzu) as sub-location fields.
