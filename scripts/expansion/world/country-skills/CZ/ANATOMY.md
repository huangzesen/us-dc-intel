# CZ · Country Anatomy

Datacenter-country knowledge layer for Czechia (CZ).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / records pipeline | `explorer-official.md` | present |
| Industry / operator / association discovery | `explorer-industry.md` | present |
| Division layer | `divisions/` — 14 manifest divisions (Prague; Central Bohemia; South Bohemia; Plzen; Karlovy Vary; Usti nad Labem; Liberec; Hradec Kralove; Pardubice; Vysocina; South Moravia; Olomouc; Zlin; Moravia-Silesia) | to be added later |

## Source hierarchy

1. **CENIA EIA/SEA + IPPC** — environmental records (portal.cenia.cz/eiasea, ippc.mzp.cz), Grade A; documents often avoid `datové centrum` and use technologická budova/serverovna/trafostanice terms.
2. **Municipal/city-district úřední deska + builder's portal** — building-permit lifecycle (stavební povolení, územní rozhodnutí, kolaudační souhlas); no single national permit registry.
3. **CUZK cadastre + ARES/justice.cz** — parcel/ownership normalization and legal entities (IČO).
4. **ČEPS / ERÚ / DSO (ČEZ Distribuce, EG.D, PREdistribuce)** — grid/connection context; grid requests are not facilities.
5. **ČTÚ + NEN** — telecom operator records and public procurement (government/university/server-room projects).
6. **Official operator/cloud/association pages** — OVHcloud Prague, O2, CETIN, TTC TELEPORT, SafeDX, T-Mobile, ASCDC/CSDIA/NIX.CZ; AWS/Azure/GCP/OCI official region pages (no CZ region/local zone).
7. **Press / directories** — Lupa.cz, iDNES, HN, Forbes, E15, CzechCrunch, oEnergetice.cz, DCD (B); DataCenterMap, Baxtel, datacenters.com, PeeringDB, Inflect (C seeds).

## Official vs industry pipeline

- Official decides **countability**: CENIA/IPPC records, notice-board permit lifecycle, CUZK parcels, DSO/ČEPS connection terms, ČTÚ/NEN records; statuses: operational / under construction / planned / lead / do-not-count.
- Industry discovers **leads**: operator pages, association member lists, press (MasterDC Kanice AI DC, Chomutov data hub, Monaco/SYNOT), directories; every lead pairs with official evidence before final counts.
- Division anatomy: Prague is the high-density colo/interconnection hub (T-Mobile DC7, TTC TELEPORT, CE Colo, OVHcloud, SafeDX, O2/CETIN, NIX.CZ); South Moravia (Brno: MasterDC/Kanice, Coolhousing, O2, CERIT) and Moravia-Silesia (Ostrava: IT4Innovations VLQ/EuroHPC public HPC) are secondary; low-density divisions run notice-board/procurement sweeps; public/HPC assets stay separate from commercial colo.

## Cross-references

- `SKILL.md` — merged playbook (query templates, vocabulary, counting rules, division matrix).
- `explorer-official.md` §5 — per-division official strategy; §6 official cloud/operator pivots; §7 trapdoors and quality controls; §8 minimal official workflow.
- `explorer-industry.md` §3 — operator/facility seed list; §5 per-division industry strategy; §8 open items to track honestly.
- Watchlist (quarterly): T-Mobile DC7 official archive, MasterDC Kanice permit/EIA, Chomutov data hub, Monaco/SYNOT confirmation, Equinix Prague evidence, OVHcloud Prague product/address, cloud-region pages (incl. eu-prague-1 claims).
