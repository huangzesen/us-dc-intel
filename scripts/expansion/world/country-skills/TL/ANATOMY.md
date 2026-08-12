# TL · Country Anatomy

Datacenter-country knowledge layer for Timor-Leste (TL).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / donor pipeline | `explorer-official.md` | present |
| Industry / operator / trade-press discovery | `explorer-industry.md` | present |
| Division layer | `divisions/` — 13 divisions (Aileu; Ainaro; Baucau; Bobonaro; Cova Lima; Dili; Ermera; Lautem; Liquica; Manatuto; Manufahi; Oe-Cusse Ambeno; Viqueque; Atauro as Dili/outer-island variant) | to be added later |

## Source hierarchy

1. **Government / TIC TIMOR** — timor-leste.gov.tl, tic.gov.tl (Electronic Government Data Center, PMO Data Center fiber contract, TLSSC landing), Grade A.
2. **Jornal da Republica / Ministry of Justice** — decree-laws (DL 29/2017, 46/2023, 15/2012, 31/2024, 5/2011, 39/2022), legal anchors.
3. **CNA + eProcurement** — procurement backbone (MoF DC: TENDER/13/MOF-2024, records 1219650/979880/1133403), award/vendor/amount extraction.
4. **ANC (regulator)** — TL-IXP TOR, licences; not ANATEL/ANACOM.
5. **Donor documents** — ADB 55338-001 (National DC + DR, proposed, USD 50m), 49177-002 (power distribution), World Bank 2026 solar/BESS (power context), UNDP context only.
6. **EDTL / power + connectivity** — Hera/Betano 255 MW context, TLSSC Bebonuk CLS (607 km/27 Tbps cable capacity, landed Jun 2024, commercial Aug 2026).
7. **Operators** — Telkomcel DC Building (A), Timor Telecom (identity A, DC C), Telemor/Viettel (identity A), Vanov (vendor awards A / DC services B).
8. **Trade press / directories** — DCD, Submarine Networks, Tatoli, The Star (Zchwantech feasibility B), Developing Telecoms, Capacity (B); DataCenterMap/Cloudscene/Datacenters.com/bgp.he.net (C seeds).
9. **Negative evidence** — official hyperscaler region pages (no TL region).

## Official vs industry pipeline

- Official decides **countability**: government/TIC pages, procurement records, Jornal da Republica, ANC records, donor project documents, operator-owned pages naming a physical facility; statuses: operational / proposed / tender / feasibility / unverified.
- Industry discovers **leads**: trade press (TLSSC timeline, Zchwantech AI partnership), operator pages, ASN/directory seeds; capacity_mw stays null unless disclosed; procurement amounts and cable/Grid MW are proxies/context only.
- Division anatomy: Dili is the only proven cluster (TIC TIMOR, PMO, MoF, Telkomcel, ANC/Timor Telecom building, Bebonuk CLS); Baucau is a DR hypothesis (not confirmed); Oe-Cusse Ambeno has special-region (RAEOA/ZEESM) procurement angles; remaining divisions are low-yield sweeps with municipal fiber/EDTL context only.

## Cross-references

- `SKILL.md` — merged playbook (four-language queries, capacity/status rules, division matrix).
- `explorer-official.md` §2 — per-division official strategy; §3 known official facility/project seeds; §4 reliability rules and pitfalls.
- `explorer-industry.md` §1 — operator/vendor sweep; §5 seed list for enumeration; §6 capacity and status rules; §7 common traps.
- Watchlist (quarterly): ADB 55338-001 RRP/procurement, Telkomcel DC specs, Zchwantech feasibility -> proposed, Baucau DR confirmation, TLSSC colocation/service offers, Vanov public colo, hyperscaler region pages.
