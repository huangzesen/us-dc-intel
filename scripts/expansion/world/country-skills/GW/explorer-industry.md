# GW Explorer Industry - Guinea-Bissau Datacenter Enumeration via Operators, Connectivity, Donor Projects, Trade Press and Directories

Date: 2026-08-12. Country: **GW Guinea-Bissau**. Division model verified against `world-manifest.jsonl`: **4 divisions** (Bissau, East, North, South). Angle: **industry and market evidence** that complements `explorer-official.md`: operator pages, UNDP/donor project coverage, subsea/IXP sources, local and international trade press, investor announcements and directories.

Reliability grades:
- **A** = official operator facility page, official cloud-region page, Uptime Institute award page, official IXP/subsea/operator page, UNGM/UNDP procurement notice, or regulator record.
- **A-** = official operator/investor press release or UNDP/government press proving a project or capacity claim where no regulator filing is visible; use `announced_capacity_mw` unless commissioning is also proven.
- **B** = established trade press or reputable Guinea-Bissau/pan-African/Portuguese-language press with specific site facts, dates, parties and status.
- **C** = directories, market reports, SEO lists, social posts, blogs and aggregators. Use as discovery leads only.

Grade each claim separately. Example: the National Technology Data Center Park existence/status is **A** from the UNDP/UNGM chain; its completion date from March 2026 local coverage is **B/C** unless confirmed officially.

---

## 0. Guinea-Bissau market facts

- Guinea-Bissau's data-centre market is **nascent and effectively government/donor-led**. As of this methodology date there is **no verified commercial colocation provider and no Uptime Institute record** in the country. The only confirmed facility record is the government/UNDP **National Technology Data Center Park / Centro Nacional de Dados** in Alto Bandim, Bissau (construction started March 2026; includes the National Data Center, the new ITMA headquarters and facilities for data-protection/cybersecurity agencies).
- Telecom operators (Telecel Guinea-Bissau - ex-MTN/ex-Spacatel, Orange Guinea-Bissau) and the state incumbent (Guine-Telecom/Guinetel) operate network/data rooms, but **no public retail colocation service or facility-level source** was verified for any of them. Treat telco "data centres" as unverified rooms until an operator page or official record appears.
- Connectivity is single-cable: **ACE** is the only international submarine cable landing in Guinea-Bissau (landing point **Suro/Suru, Cacheu region** - North division; a 30 km terrestrial extension connects Suro to the Antula power plant on the outskirts of Bissau). The ACE connection was finalized **2023-03-28**; the project began in 2017 under the WARCIP umbrella. No 2Africa, Equiano, MainOne, WACS or SAT-3 landing for Guinea-Bissau.
- **GwIX** (Guinea-Bissau Internet Exchange Point Association) says it was established in Bissau on **2024-08-23** and formalized at the registry office in 2025; the verified gwix.gw page is still a maintenance/placeholder page. GwIX/WARDIP LinkedIn posts and Internet Society event pages are useful IXP leads, but no facility page, peering LAN record or building address was verified.
- **No AWS, Azure, Google Cloud or Oracle public region** in Guinea-Bissau. Treat cloud/edge/CDN/satellite presence (including unauthorised Starlink use flagged by ARN) as ecosystem evidence, not a facility.
- Announced capacity: none disclosed for the National DC Park. Keep `capacity_mw=null` until official figures appear.

---

## 1. Verified operator and facility census

| Operator / facility | Division / location | Status and capacity handling | Primary evidence | Grade |
|---|---|---|---|---|
| **National Technology Data Center Park / Centro Nacional de Dados (incl. ITMA HQ)** | Bissau - Alto Bandim | Construction started March 2026; completion planned July 2026 in local coverage; capacity not disclosed. Japan-financed, UNDP-implemented. Includes National Data Center, new ITMA building, and data-protection/cybersecurity agency facilities per press/UNDP reporting. UNDP tender UNDP-GNB-00270 "Construction of National Technology Data Center Park" is verified on UNGM notice 278362 (published 2025-09-12; deadline 2025-10-08). | https://www.ungm.org/Public/Notice/278362 ; https://www.undp.org/pt/guinea-bissau/publications/boletim-informativo-do-programa-das-nacoes-unidas-para-o-desenvolvimento-pnud-na-guine-bissau-edicao-05-jan-mar-2026 ; https://conosaba.blogspot.com/2026/03/pnud-inicia-construcao-do-centro.html ; https://maisafrika.com/noticias/ultimahora/guine-bissau-japao-financia-construcao-do-itma/ | A for UNGM procurement/existence; A-/B for UNDP/PNUD implementation reporting; C for blog-only completion/scope details unless matched to official reporting |
| **ITMA (Instituto Tecnologico para a Modernizacao da Administracao)** | Bissau (new HQ within the DC Park; previously rented offices) | Government ICT institute; Japan funds the new building (approx. EUR 1.93M, announced 2024-03-29); PM stated the building will house the "Data Center" da Guine-Bissau. Record as part of the National DC Park programme, not as a separate commercial facility. WARDIP verifies ITMA modernization activity but does not by itself prove a separate data-centre facility. | https://maisafrika.com/noticias/ultimahora/guine-bissau-japao-financia-construcao-do-itma/ ; https://wardip.gw/guine-bissau-valida-plano-estrategico-para-modernizacao-da-administracao-publica-atraves-do-itma/ | B for press-reported ITMA/data-centre building details; A for WARDIP's ITMA institutional modernization context only |
| **Telecel Guinea-Bissau (ex-MTN Guinea-Bissau / ex-Spacatel)** | Mainly Bissau; national network | Mobile/network operator. Transfer from MTN to Telecel completed 2024-08-07 (joint statement). Data rooms exist but no public colocation service or facility-level source verified. | https://www.mtn.com/joint-statement-telecel-group-mobile-completed-the-acquisition-of-mtn-guinea-bissau-from-mtn/ ; https://mtngbissau.com/ (legacy) | A for ownership/licence facts; C for any unverified facility/capacity claims |
| **Orange Guinea-Bissau (Orange Bissau)** | Mainly Bissau; national network | Mobile/network operator (4G, Orange Money). The official site is indexed and normally reachable, but direct fetches may fail from some environments; use Orange corporate/jobs pages as fallback for operator presence. No public data-centre/colocation offering verified. | https://www.orange-bissau.com/ ; https://orange.jobs/gb/en/africa-middle-east/guinea-bissau ; https://www.orange.com/en/press-release/orange-bissau-launches-its-program-to-modernize-the-mobile-access-network-and-extend-its-rural-coverage-to-more-than-1000-new-villages-in-guinea-bissau-234698 | A for operator presence; no facility claims |
| **Guine-Telecom / Guinetel** | Bissau | State incumbent fixed operator + Guinetel mobile brand: declared bankrupt 2013; awarded operating licences in 2021 (Guine-Telecom network/fixed licence); government relaunch project; state launched international tender to sell 80% of Guinetel (2024). Guine-Telecom's new mission includes telecom-infrastructure management (relevant to backbone/landing-station roles). No DC facility verified. | https://www.datacenterdynamics.com/en/news/guinea-bissau-government-keen-to-sell-80-percent-of-guine-telecom-and-guinetel/ ; https://eco.sapo.pt/2024/07/19/estado-guineense-lanca-concurso-para-vender-80-da-guinetel-ha-uma-empresa-portuguesa-interessada/ ; https://ang.gw/governo-apresenta-projeto-de-relancamento-das-empresas-guine-telecom-e-guinetel-aos-parceiros/ | A- for licences/official press; B for sale-process coverage |
| **ACE landing station (Suro/Suru)** | North - Cacheu region (Suro/Suru), terrestrial link to Antula/Bissau | Submarine cable landing (only international cable). DC-adjacent lead: record as landing station/connectivity asset, not as a data centre. ACE official page says the system links Suru to the Antula power plant over 30 km and that the connection is Guinea-Bissau's first international submarine-fibre access. | https://ace-submarinecable.com/en/guinea-bissau-connects-to-ace-submarine-cable/ ; https://www.submarinecablemap.com/submarine-cable/africa-coast-to-europe-ace ; https://geocables.com/locations/gw | A- for landing fact from ACE/TeleGeography/GeoCables; no DC facility claim |
| **GwIX (Guinea-Bissau IXP Association)** | Bissau | IXP association lead. The verified gwix.gw page is a placeholder; LinkedIn posts say the association was established in 2024 and that GwIX/WARDIP signed an MoU for the first IXP; Internet Society lists a Bissau Peering Roadshow in 2025. No operational IXP facility, PeeringDB facility or meet-me-room address verified. | https://gwix.gw/ ; https://www.linkedin.com/company/gwix-guinea-bissau-internet-exchange-point-association ; https://www.internetsociety.org/events/peering-roadshows/ | A- for placeholder domain/association identity; B/C for LinkedIn event/MoU details; no facility record |

Operator census queries:
```text
("Guine-Bissau" OR Bissau) ("data center" OR "centro de dados" OR "centro nacional de dados") (launch OR construcao OR inaugurado OR operacional)
"{operador}" "Guine-Bissau" ("sala de servidores" OR "data room" OR colocation OR colo)
(Telecel OR MTN OR Orange) "Guine-Bissau" "centro de dados"
("Guine-Telecom" OR Guinetel) "Guine-Bissau" (licenca OR "gestao de infraestruturas")
(PNUD OR UNDP) "Guine-Bissau" ("data center" OR "centro de dados" OR ITMA)
```

Alias rules:
- National Technology Data Center Park = Centro Nacional de Dados = "Data Center" da Guine-Bissau (one Bissau programme; the ITMA HQ is part of it).
- Telecel Guinea-Bissau = MTN Guinea-Bissau (legacy) = Spacetel Guinea-Bissau (legacy).
- Suro = Suru (ACE landing, Cacheu region).
- MTTED = Ministerio dos Transportes, Telecomunicacoes e Economia Digital; WARDIP = West Africa Regional Digital Integration Program (ex-WARCIP).

---

## 2. Hyperscaler and cloud-provider status

Official pages to check every run:
- AWS: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/ and https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud: https://cloud.google.com/about/locations
- Oracle Cloud: https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm

As of this methodology date, **none** lists a Guinea-Bissau public cloud region. Do not create a Guinea-Bissau hyperscale/cloud-region facility from:
- Starlink/VSAT satellite broadband use (including unauthorised provision flagged by ARN).
- CDN/cache/edge nodes or partner cloud/reseller presence.
- Donor "digital transformation" announcements that do not name a facility.
- Claims that customer data can be served in-country without an official cloud-region page.

Cloud queries:
```text
site:aws.amazon.com "Guinea-Bissau" "Region" "Availability Zone"
site:learn.microsoft.com/azure "Guinea-Bissau" "region"
site:cloud.google.com/about/locations "Guinea-Bissau" "region"
site:oracle.com/cloud "Guinea-Bissau" "cloud region"
"Guinea-Bissau" ("AWS region" OR "Azure region" OR "Google Cloud region" OR "Oracle Cloud region")
```

---

## 3. Connectivity, subsea and IXP evidence

Connectivity records are **DC adjacency leads**. They can identify landing stations, meet-me sites and operator candidates, but they do not automatically create a commercial data-centre record.

Verified sources and facts:
- **ACE (Africa Coast to Europe)**: only international cable landing in Guinea-Bissau. Landing point **Suro/Suru, Cacheu** (11.7741 N, -15.7911 W per GeoCables); 30 km terrestrial connection Suro/Suru -> Antula power plant (Bissau outskirts); ACE official coverage says the connection was Guinea-Bissau's first international submarine-fibre access and the project began in 2017. Official/operator/industry sources: ace-submarinecable.com; TeleGeography submarinecablemap.com; geocables.com/locations/gw.
- **National fibre backbone (Espinha Dorsal Nacional)**: MTTED launched an international selection for the national backbone under a PPP model (WARDIP); the EIASS for the backbone was published via ARN. Backbone is the main domestic infrastructure programme that could later host/connect data centres; watch WARDIP/ARN procurement pages.
- **GwIX**: association lead reportedly established 2024-08-23 in Bissau and formalized at the registry office in 2025; site gwix.gw is a placeholder; LinkedIn posts say it partners with WARDIP; Internet Society lists a Guinea-Bissau Peering Roadshow in Bissau in 2025. Check PCH/Internet Exchange Map and PeeringDB for an operational exchange before creating a facility record.
- **Satellite**: Starlink and VSAT are used; ARN has publicly flagged unauthorised Starlink service provision. Satellite presence is not a DC record.

Connectivity queries:
```text
"Guine-Bissau" "ACE" "cabo submarino" (Suro OR Suru OR Bissau)
"landing station" "Guinea-Bissau" ACE
site:ace-submarinecable.com "Guinea-Bissau"
("Espinha Dorsal Nacional" OR "backbone nacional") "Guine-Bissau" (PPP OR concurso)
(GwIX OR "Guinea-Bissau Internet Exchange" OR "PIT Guine-Bissau")
(site:submarinecablemap.com OR site:geocables.com) "guinea-bissau"
```

---

## 4. Trade press and market-monitoring feeds

Use these to detect new builds, financing, commissioning and operator changes. They are not substitutes for official/operator evidence.

| Source | URL | Use | Grade |
|---|---|---|---|
| Agencia de Noticias da Guine (ANG) | https://ang.gw/ | Government/agency news: EAGB, MTTED, Guine-Telecom, energy, digital projects | B |
| O Democrata GB | https://www.odemocratagb.com/ | Local sector coverage, ARN notices, WARCIP/ACE documents | B |
| Bantumen / Mais Afrika / Ultima Hora GB / Radio TV Bantaba / Conosaba | outlet domains | Local digital-transformation and project coverage (ITMA, PNUD); verify with official sources | B-/C |
| Lusa (via eco.sapo.pt, Observador, Jornal de Negocios), RFI, DW, VOA Portugues | outlet domains | International Lusophone coverage of GW telecom/energy/digital affairs | B |
| DatacenterDynamics (DCD) | https://www.datacenterdynamics.com/ | Operator/licence news (e.g., Guine-Telecom/Guinetel); GW-specific coverage is rare | B+ |
| Developing Telecoms, Ecofin Agency, Connecting Africa, Capacity Media, TechAfrica News | outlet domains | Telecom/connectivity market news for West Africa | B |
| Internet Society, PCH, TeleGeography (submarinecablemap, internetexchangemap) | official/industry domains | IXP and cable metadata | A-/B |
| UNGM, UNDP Guinea-Bissau, World Bank (WARDIP docs) | official domains | Procurement and project documents | A |
| Baxtel, Data Center Map, DataCenters.com, Data Center Platform, PeeringDB | directory/peering domains | Lead discovery; expect zero-to-noise for GW | C except PeeringDB metadata |

Feed queries:
```text
site:datacenterdynamics.com ("Guinea-Bissau" OR "Guine-Bissau")
site:ang.gw ("data center" OR "centro de dados" OR digital OR fibra)
site:odemocratagb.com ("data center" OR "centro de dados" OR ACE OR "fibra optica")
(site:connectingafrica.com OR site:developingtelecoms.com) "Guinea-Bissau" ("data centre" OR cloud)
"Guine-Bissau" ("centro de dados" OR "data center") (construcao OR lancamento OR inauguracao OR concurso)
"Guine-Bissau" (ITMA OR PNUD OR WARDIP) (data OR digital)
```

---

## 5. Directories and how to use them

Directories are useful for alias discovery, but Guinea-Bissau has effectively **no commercial colocation directory entries**; most hits will be country-list noise.

Directory rules:
- Use Baxtel/DataCenterMap/DataCenters.com/Data Center Platform as **C** unless they link to an official operator page, Uptime record or UNGM/UNDP notice.
- Never ingest a directory-only facility without at least one operator, regulator, UN/donor, Uptime, permit or strong press source.
- Watch for alias duplication: Telecel vs MTN vs Spacetel; Centro Nacional de Dados vs ITMA building; Suro vs Suru.
- Treat directory MW/rack values as `claimed_capacity` until official confirmation (expected: none for GW).
- PeeringDB: no verified Guinea-Bissau facilities were found in this pass; re-check as GwIX matures.

Directory queries:
```text
site:baxtel.com ("Guinea-Bissau" OR Bissau) "data center"
site:datacentermap.com ("Guinea-Bissau" OR Bissau)
site:datacenters.com "Bissau" "data center"
site:peeringdb.com/fac (Bissau OR "Guinea-Bissau")
site:datacenterplatform.com "Guinea-Bissau"
```

---

## 6. Industry bodies and events

- **Uptime Institute**: no Guinea-Bissau award/record verified in this pass (nearest country records are Guinea-Conakry ARPT and regional peers). Re-check `site:uptimeinstitute.com "Guinea-Bissau"` each batch.
- **GwIX**: the only local interconnection body; membership and roadshow activity are leads for future meet-me/colo services.
- **ARN / NIC.gw**: regulator and ccTLD registry; also runs sector fora (e.g., 1st Internet Governance Forum, 2024).
- **Internet Society (ISOC)**: hosted the Peering Roadshow in Bissau (2025) with GwIX/WARDIP; watch for IXP build-out announcements.
- **AfPIF/Datacloud Africa**: regional events may mention GW operators; **B/C** unless tied to official facility pages.
- No dedicated Guinea-Bissau Data Centre Association was verified; do not invent one.

Queries:
```text
site:uptimeinstitute.com ("Guinea-Bissau" OR Bissau) "Data Center"
"GwIX" "Guine-Bissau" (membros OR inauguracao OR "ponto de troca")
("Internet Society" OR "Peering Roadshow") Bissau "Guine-Bissau"
"forum de governacao da internet" "Guine-Bissau"
(AfPIF OR "Datacloud Africa") "Guine-Bissau"
```

---

## 7. Per-division industry discovery map

| Division | Industry search set | Expected result / coding guidance |
|---|---|---|
| **Bissau** | `(Bissau OR "Alto Bandim") ("centro nacional de dados" OR "data center")`; `"ITMA" "Guine-Bissau"`; `(PNUD OR UNDP) Bissau "data center"`; `"{operador}" Bissau ("sala de servidores" OR colo)`; `GwIX Bissau`; directory cross-checks | Positive: National Technology Data Center Park (construction, A/A- chain). Telco and bank/BCEAO data rooms are leads only; do not create records without facility-level sources. |
| **North** | `(Suro OR Suru) "Guine-Bissau" (ACE OR "cabo submarino")`; `Cacheu ("data center" OR servidores)`; `(Oio OR Biombo) servidores`; `"Espinha Dorsal Nacional" (Cacheu OR Oio)` | ACE landing at Suro/Suru (Cacheu) recorded as landing-station/connectivity lead, not a DC. No DC records expected. |
| **East** | `(Bafata OR Gabu) ("data center" OR servidores OR "centro de dados")`; `(Bafata OR Gabu) ("fibra optica" OR backbone)` | Expected negative for facilities; backbone route only. |
| **South** | `(Quinara OR Tombali OR Bolama OR Bijagos) ("data center" OR servidores)`; `(Buba OR Catio) "sala de servidores"` | Expected negative; ITMA programme mentions interior/Bijagos digital benefits but no facility evidence. |

For negative divisions, store query/date notes. Do not omit a division from the output just because no facility is found.

---

## 8. Verification workflow

1. Seed from **A/A-** sources: UNGM/UNDP (National DC Park), ARN, WARDIP, operator pages (Telecel, Orange), ACE/subsea sources, GwIX.
2. Dedupe aliases before counting facilities (National DC Park vs ITMA building; Telecel vs MTN vs Spacetel; Suro vs Suru).
3. For each site, assign `division` by physical location: Alto Bandim/Antula/Bissau = Bissau; Suro/Cacheu = North; nothing expected in East/South.
4. Split status and capacity: `operational_capacity_mw`, `announced_capacity_mw`, `racks`, `certification`, `source_date`, `source_grade`. Expect nulls for GW.
5. Escalate each facility to official verification through `explorer-official.md`: UNGM/UNDP, ARN, MTTED/WARDIP, MENER/EAGB, CFE.
6. Re-run cloud-region exclusion and Uptime checks each batch.
7. Sweep all 4 divisions and explicitly output `no_projects: true` where appropriate.

Recommended output schema:
```json
{
  "country_code": "GW",
  "country_name": "Guinea-Bissau",
  "division": "Bissau",
  "name": "National Technology Data Center Park / Centro Nacional de Dados",
  "status": "construction",
  "operator": "Government of Guinea-Bissau / UNDP (implementer); Japan (funder)",
  "developer": "UNDP Guinea-Bissau",
  "capacity_mw": null,
  "announced_capacity_mw": null,
  "racks": null,
  "source_urls": ["https://www.ungm.org/Public/Notice/278362"],
  "evidence_date": "2026-08-12",
  "evidence_grade": "A",
  "notes": "Includes National Data Center + ITMA HQ + data-protection/cybersecurity agency facilities at Alto Bandim, Bissau."
}
```

---

## 9. Common false positives

- **ACE landing (Suro) and Antula power plant treated as data centres**: they are a landing station and a power plant; the 30 km link is terrestrial fibre, not a DC.
- **Telco "data centres"** (Telecel/Orange/Guine-Telecom network rooms) without a colocation service or facility-level source.
- **ITMA building vs National DC**: both belong to one Alto Bandim programme; do not double-count as separate facilities.
- **Starlink/VSAT satellite internet** (including unauthorised provision flagged by ARN) as a DC record.
- **Backbone/"digital transformation" announcements** (Espinha Dorsal Nacional, WARDIP, ENTD.GW) treated as facilities.
- **Directory country-list noise**: most directory hits are dropdown entries, not Guinea-Bissau facilities.
- **"PNUD construction" blog coverage** without the UNGM/UNDP notice behind it (blogs are C; the UNGM notice is A).

## Final confidence notes

- **High confidence**: division model is 4 divisions (Bissau/East/North/South); the only confirmed facility record is the National Technology Data Center Park at Alto Bandim, Bissau (construction); ACE is the only submarine cable (Suro, Cacheu); GwIX exists as an association (no operational IXP record yet); no hyperscaler region; no Uptime records; no verified commercial colocation.
- **Medium confidence**: exact scope/completion date of the National DC Park (local coverage says July 2026; capacity undisclosed); Telecel's post-transfer network/data-room status; Guine-Telecom/Guinetel relaunch and 80% sale outcome.
- **Low confidence**: any directory-listed facility, any telco/enterprise data room, and any interior-region server room; expect zero commercial DC records for the foreseeable future.
