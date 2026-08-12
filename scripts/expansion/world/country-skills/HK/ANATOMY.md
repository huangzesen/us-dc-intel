# HK · Country Anatomy

Datacenter-country knowledge layer for Hong Kong (HKSAR) (HK).

## Files

| File | Status | Notes |
| --- | --- | --- |
| Country-level skill `SKILL.md` | Present | Merged from the two reviewed explorers (official/regulatory/cloud pipeline + industry/vendor/trade-press discovery) |
| Official / regulatory / cloud pipeline `explorer-official.md` | Present | Final-reviewed: DPO/ITIB, TPB/PlanD, LandsD, BD, EMSD/BEAM, EPD, OFCA, CLP/HK Electric, Companies Registry/HKEX, GovHK/DATA.GOV.HK/GeoInfo, cloud-region pages, InvestHK/HKTDC/HKPC |
| Industry / trade press / vendor discovery `explorer-industry.md` | Present | Final-reviewed: operator pages, hyperscaler regions, DCD/SCMP/trade press, HKIX/PeeringDB/subsea cables, aggregator directories |
| District division layer `divisions/` | To be added later | HK is manifest type `country` with 1 division (Hong Kong); granular routing uses the 18 District Council districts + street/estate fields |

## Division layer (future)

Per world-manifest.jsonl, HK is modeled as **country** with a single division: **Hong Kong** (no state/province tier; a Special Administrative Region of China). When the division layer is built, create `divisions/Hong_Kong/` (or store `division="Hong Kong"` + `district` + `place/estate` per record) and keep the 18 District Council districts (Central & Western, Wan Chai, Eastern, Southern, Yau Tsim Mong, Sham Shui Po, Kowloon City, Wong Tai Sin, Kwun Tong, Kwai Tsing, Tsuen Wan, Tuen Mun, Yuen Long, North, Tai Po, Sha Tin, Sai Kung, Islands) as the granular layer for routing and deduplication.
