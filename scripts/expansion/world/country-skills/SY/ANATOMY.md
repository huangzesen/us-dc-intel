# SY · Country Anatomy

Datacenter-country knowledge layer for Syria (SY).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory pipeline | `explorer-official.md` | present |
| Industry / press / vendor discovery | `explorer-industry.md` | present |
| Governorate division layer | `divisions/` — 14 governorates (Damascus, Aleppo, Homs, Hama, Latakia, Tartus, Daraa, Suwayda, Quneitra, Idlib, Raqqa, Deir Ezzor, Hasaka, Damascus Countryside) | to be added later |

## Source hierarchy

1. **MOCT / Digital Syria / SYTPRA / SIA / SANA (AR+EN)** — national official surface: strategic programs (SilkLink, National Data Center), licences, investment one-stop-shop, official announcements; Grade A.
2. **Operators** — Syrian Telecom, Syriatel, MTN Syria, Zain Syria; A for own services, not facility proof for core rooms/PoPs.
3. **Power authorities** — Ministry of Electricity, PEEGT, governorate electricity companies; electricity is a gating condition, checked per candidate.
4. **Industry trade press** — DCD, Capacity Media, Developing Telecoms, Submarine Networks, TeleGeography, Reuters/AP/AFP, Syria Report, Enab Baladi (B); Uptime Institute certification list (A if matched).
5. **Directories** — Data Center Map, Baxtel, Cloudscene, Datacenters.com, PeeringDB (C seeds; negative results recorded with date).
6. **Negative evidence** — official hyperscaler region pages (no SY region listed).

## Official vs industry pipeline

- Official decides **countability**: MOCT/Digital Syria program pages, SYTPRA licences, SIA investment records, SANA named statements, power evidence. Statuses: operational / under_construction / licensed / program-level / MoU / connectivity / negative.
- Industry discovers **leads**: SilkLink STC award, Go/Etihad Atheeb MoU, Medusa/Ugarit/Aletar cable events, Mijad/Sham Cloud, Ministry of Higher Education IT center; leads stay leads until site/owner/type/status/date are named.
- Division anatomy: 14 governorates; Damascus (highest priority) and Aleppo (second) carry the facility-type leads; Tartus is connectivity-heavy (Medusa/Ugarit landings, SilkLink IXP); low-probability governorates get explicit negative documentation.

## Cross-references

- `SKILL.md` — merged playbook (query templates AR/EN, status semantics, grades, 14-governorate strategy).
- `explorer-official.md` §2 — connectivity classification (SilkLink/Medusa/Ugarit); §4 evidence classification; §5 complete 14-governorate official strategy.
- `explorer-industry.md` §2 — verified press anchors; §3 operator/vendor lead list; §7 validation rules.
- Watchlist (quarterly): Mijad/Sham Cloud certification, SilkLink IXP milestones, Go MoU upgrades, Medusa landing station services, hyperscaler region pages.
