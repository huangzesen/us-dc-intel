# NG · Country Anatomy

Datacenter-country knowledge layer for Nigeria (NG).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| Province/state division layer | `divisions/` — 36 states + Abuja Federal Capital Territory | to be added later |

## Source hierarchy

- **A (official/primary)**: state/FCT planning or building-control records, Federal Ministry of Environment/EAD EIA disclosures, NERC captive-generation permits or electricity orders, NCC licence/register entries, official cloud-provider pages (AWS Lagos Local Zone af-south-1-los-1a), official operator facility pages, Uptime Institute certification records, official government data-centre/cloud pages (NITDA, Galaxy Backbone).
- **B (strong secondary)**: trade press (DCD, TechCabal, TechAfrica News…), exchange/IXP/subsea operator pages, state investment-promotion releases, reputable local business press, vendor case studies, financing/government MoUs with named site.
- **C (weak lead)**: generic market reports, directory-only facilities, social posts, procurement rumours, unimplemented MoUs, state ICT plans that say “data centre” without site/status.

## Official vs industry pipeline

- **Official pipeline** (explorer-official.md): state/FCT development permit + building control → EAD/EIA disclosure → NCC licence/register → NERC captive-power/MYTO evidence → NITDA/Galaxy Backbone government cloud → official cloud-region/edge pages → Uptime certifications → operator pages. Status is upgraded only with permit/NERC/NCC/Uptime/operator confirmation.
- **Industry pipeline** (explorer-industry.md): trade press / aggregator / IXP-subsea lead → operator official page → state/FCT planning + EAD + NERC/NCC records → Uptime/certification → commissioning page. Press stage language (announces/MoU/groundbreaking) stays lead-only; aggregator MW/status never accepted without corroboration.

## Division layer (future)

- Nigeria enumerates at state + FCT granularity, siting city/locality-first. Priority clusters: Lagos (Lekki, Victoria Island, Eko Atlantic, Ikoyi, Ikeja, Oregun, Ikate Elegushi, Yaba, Apapa, Ojota — Equinix/MainOne/MDXi, Rack Centre, ADC, OADC, Digital Realty/Medallion, Kasi, MTN, Airtel/Nxtra), FCT Abuja (Galaxy Backbone, government cloud, National Shared Services Centre), Kano (Galaxy Backbone Tier IV, MTN switch), Rivers/Port Harcourt (Equinix PR1, 2Africa, oil/gas power), Ogun (Sagamu/Atakobo energy park — old announcements need fresh proof), Akwa Ibom/Eket (Kasi DNEK), Cross River/Calabar (Nugi/9mobile), Benue/Makurdi (UniCloud/Benue Digital Infrastructure Company), Abia (WIOCC/OADC MoU), plus state ICT rooms/telecom switches across remaining states (South East/South South/South West/North Central/North West/North East groups).
- Dedup anchors: Lagos by operator+campus (Lekki/MainOne-Equinix, Oregun/Rack Centre, Eko Atlantic/ADC-Nxtra, Ikate/OADC, Victoria Island/Medallion-Digital Realty, Lekki/Kasi); FCT/Kano Galaxy Backbone hosted-service partnerships are not new facilities in partner states.
- Planned: per-state (or per-cluster) skill files covering state/FCT planning and building-control routes, EAD EIA surfaces, NCC licence categories per operator, NERC CPG lookups, and power/TCN contacts.

## Cross-references

- `SKILL.md` §查询模式 routes to explorer-official.md §1/§3 and explorer-industry.md §1/§4 for copy-paste templates; the official state-by-state strategy (explorer-official.md §3) mirrors the industry state matrix (explorer-industry.md §4); both share operator seeds and locality pivots.
- Known seeds and validation anchors: explorer-official.md §2/§3.1 and explorer-industry.md §2/§4.1 (Equinix/MainOne/MDXi LG1-LG3 + PR1, Rack Centre LGS2 + NERC/CPG/165, OADC CPG/177 + Equiano, ADC LOS1, Digital Realty/Medallion, Galaxy Backbone Abuja/Kano, Kasi LOS/DNEK, MTN switches, Airtel/Nxtra, NITDA/Galaxy Backbone government sources).
- Sector manifest: `brief.md` at the country-skills root describes the overall expansion program; this country layer routes NG batches only.
