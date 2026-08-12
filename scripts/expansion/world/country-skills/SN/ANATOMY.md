# SN · Country Anatomy

Datacenter-country knowledge layer for Senegal (SN).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / state-digital pipeline | `explorer-official.md` | present |
| Industry / press / vendor discovery | `explorer-industry.md` | present |
| Region division layer | `divisions/` — 14 regions (Dakar, Diourbel, Fatick, Kaffrine, Kaolack, Kedougou, Kolda, Louga, Matam, Saint-Louis, Sedhiou, Tambacounda, Thies, Ziguinchor) | to be added later |

## Source hierarchy

1. **urbanisme (autorisation de construire) + DEEC/DIREC (EIES / installations classees)** — commune-level permit trail and environmental records; Grade A process sources.
2. **Senelec / CRSE** — utility material, power evidence (raccordement, poste, MW/MVA); Uptime Senelec Datacenter Diamniadio record.
3. **ARTP** — telecom authorization/licence/agrement/sanction; not a facility register.
4. **APIX / Invest in Senegal** — investment promotion PDFs and unnamed-project leads.
5. **Senegal Numerique SA / SENUM** — state operator claim: three operational DCs (Orana, Technopole, Diamniadio); Smart Senegal/cloud national pivots.
6. **Operators / Uptime** — Sonatel Rufisque, Onix, PAIX, Free, StellarIX, Jokko, Douanes BdM, Millicom/Tigo Phase-1A; Uptime country page https://uptimeinstitute.com/uptime-institute-awards/country/id/SN is authoritative for certification/location.
7. **Industry press / aggregators** — DCD, DCmag, Connecting Africa, Ecofin, CIO Mag, RFI, Financial Afrik, Dakaractu, Le Soleil (B); DataCenterMap/Baxtel/Neocloud (C seeds).
8. **Negative evidence** — official hyperscaler region pages (no SN region; AWS Wavelength is an edge lead).

## Official vs industry pipeline

- Official decides **countability**: commune authorization, DEEC/DIREC records, Senelec/CRSE power evidence, ARTP status, APIX investment, SENUM state-program pages, Uptime records.
- Industry discovers **leads and timing**: operator pages (Onix, PAIX, StellarIX, Jokko), press (PAIX ground-breaking, national DC inauguration), vendor pages; status verbs decide planned/under-construction/operational.
- Division anatomy: Dakar region is the yield center (Dakar dept, Rufisque/Diamniadio, Almadies, Les Mamelles, Pikine/Technopole); Diamniadio stays in Rufisque/Dakar (never Thies); Thies watchlist; Kaolack historical C lead; 11 other regions are negative-search territory with logged negatives.

## Cross-references

- `SKILL.md` — merged playbook (query templates, grades, dedup rules, 14-region seeds).
- `explorer-official.md` §3 — source-graded facility seed list; §4 per-region official strategy; §5 dedup/final grading rules.
- `explorer-industry.md` §2 — operator/developer sweep with grades; §5 facility lead sheet; §6 common pitfalls.
- Watchlist (quarterly): PAIX Dakar go-live, SENUM Orana/Technopole function, Free/StellarIX Uptime records, Onix operational status, APIX unnamed project, Kaolack refresh, hyperscaler region pages.
