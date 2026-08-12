# EE · Country Anatomy

Datacenter-country knowledge layer for Estonia (EE).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory pipeline | `explorer-official.md` | present |
| Industry / operator discovery | `explorer-industry.md` | present |
| County division layer | `divisions/` — 15 counties (Harju, Hiiu, Ida-Viru, Jõgeva, Järva, Lääne, Lääne-Viru, Põlva, Pärnu, Rapla, Saare, Tartu, Valga, Viljandi, Võru) | to be added later |

## Source hierarchy

1. **EHR (Ehitisregister)** — public building register (https://ehr.ee), Grade A; data centers may be filed under office/telecom/industrial/storage/technical purposes; search by address/entity/parcel/permit ID, not keyword only.
2. **Municipal planning/permits** — detailplaneering, ehitusluba, kasutusluba via municipal pages and Tallinn Planning Register (https://tpr.tallinn.ee); Ametlikud Teadaanded (https://www.ametlikudteadaanded.ee) for official notices.
3. **Keskkonnaamet / KOTKAS** — environmental permits, generator air permits, EIA/KMH decisions (https://kotkas.envir.ee).
4. **Elering (TSO) / Elektrilevi (DSO)** — grid connections, substation and capacity evidence (https://elering.ee, https://www.elektrilevi.ee).
5. **Äriregister** — legal entity, registry code, EMTAK 6311/63101 pivots (https://ariregister.rik.ee).
6. **Operator pages / trade press / catalogs** — seed and support (Greenergy, Sunly, Telia, Elisa, WaveCom, INFONET; DCD, ERR, Invest Estonia; DataCenterMap/Baxtel as C-grade seeds).

## Official vs industry pipeline

- Official decides **countability**: a facility is countable at Grade A only with EHR use permit/active status, municipal permit, environmental decision, or grid evidence bound to a named developer/site.
- Industry discovers **leads**: operator pages, contractor releases (Caverion, Merko, Siemens, Delta UPS), trade press, and catalogs; catalog totals stay C until matched.
- Division anatomy: counties are enumeration buckets (79 municipalities); Harju and Lääne carry the live/planned leads; low-yield counties use the low-yield sweep template before recording no projects.

## Cross-references

- `SKILL.md` — merged playbook (query templates, grades, lifecycle, county strategy).
- `explorer-official.md` §3 — action table of official facility seeds (Greenergy, Sunly Risti, Telia, Elisa, WaveCom, INFONET, Narva, RIA/Riigipilv, Nebius watchlist).
- `explorer-industry.md` §3 — player/facility lead inventory with source grades and official follow-up.
- Watchlist (quarterly): Sunly Risti milestones, Greenergy/MCF expansion, Nebius confirmation, Harju industrial municipalities, Ida-Viru industrial zones.
