# TL Explorer Industry - Timor-Leste Datacenter Enumeration via Operators, Vendors, Trade Press, Directories, and Local-Language Leads

Date: 2026-08-12. Scope: Timor-Leste (TL), repo/requested 13 divisions: Aileu; Ainaro; Baucau; Bobonaro; Cova Lima; Dili; Ermera; Lautem; Liquica; Manatuto; Manufahi; Oe-Cusse Ambeno; Viqueque. Atauro has been a separate municipality since 2022, but for this methodology keep it as a Dili/outer-island variant unless the repo schema changes.

Reliability grades:

- **A**: operator-owned page, official public-sector page, procurement/award, regulator record, or donor project document naming the facility/project.
- **B**: reputable trade press or named-party local/regional reporting.
- **C**: directory/marketplace/SEO page, hosting reseller page, social-only material, or unverified claim.

## 0. Market Shape

- Timor-Leste's datacenter market is small and government/telecom-led. Strong public evidence exists for TIC TIMOR/government data-center functions, the Ministry of Finance data center, the Prime Minister's Office Data Center, and the Telkomcel Data Center Building. Most other "cloud" or "colo" claims require verification.
- Dili is the only proven cluster: Caicoli/MTC/Government Palace ministries, Telecom Building/ANC/Timor Telecom, Timor Plaza/Comoro operator offices, Taibesi ICT vendors, and Bebonuk cable landing station.
- Baucau is the most plausible disaster-recovery candidate because of its size and distance from Dili, but no primary source found in this pass names Baucau as the ADB DR site. Keep it as a priority search hypothesis, not a fact.
- The TLSSC submarine cable landed at Bebonuk in June 2024 and commercial operation was reported in August 2026; it changes the connectivity case for future Dili facilities but does not itself prove a datacenter.
- Be skeptical of "Tier III Dili" or "Timor-Leste VPS/cloud" pages. Require a named operator, local address, and primary corroboration.

## 1. Operator and Vendor Sweep

| Operator / project | URL | Locality | Grade | How to use |
|---|---|---|---:|---|
| TIC TIMOR / Electronic Government Data Center | https://www.tic.gov.tl/en/tic/sentrudadus/ and https://www.tic.gov.tl/en/tic/shownotisia/115/ | Dili, MTC/Caicoli area | A | TIC TIMOR names a Data Center role and says it has a Data Center Directorate managing the Electronic Government Data Center. Capture as government facility/function; specs not public. |
| Prime Minister's Office Data Center | https://timor-leste.gov.tl/?lang=en&p=19673&print=1 | Dili | A | Government fiber-contract release says municipal administrations connect to the PMO Data Center. Treat as a confirmed government DC anchor. |
| Ministry of Finance Data Center | CNA: https://www.cna.gov.tl/pt/2024/09/02/postqualification-for-the-upgrade-of-equipment-of-/ ; eProcurement: https://www.eprocurement.gov.tl/publishedDocuments/show/1219650 ; https://www.eprocurement.gov.tl/publishedDocuments/show/979880 ; https://www.eprocurement.gov.tl/publishedDocuments/show/1133403 | Dili | A | Multiple procurement records prove an existing MoF DC/DR procurement trail. Extract award/vendor/status from each record; do not infer MW. |
| Telkomcel Data Center Building | https://www.telin.net/en/company/news/telkomcel-inaugurated-the-first-telkomcel-data-center-building-in-timor-leste and https://telkomcel.tl/p/data-center-erp | Dili, Telkomcel/Timor Plaza business area | A | Operator/parent official evidence for Telkomcel's first DC building in Timor-Leste and service page for data-center/ERP services. Verify current address/specs directly from Telkomcel before capacity claims. |
| Timor Telecom | https://www.timortelecom.tl/ | Dili, Telecom Building / national backbone | A for operator identity; C until DC named | Important fixed/mobile/backbone operator and host building for ANC. Record only named data-center/server-room evidence; otherwise use as network lead. |
| Telemor / Viettel Timor-Leste | https://www.telemor.tl/ | Dili, Timor Plaza / nationwide network | A for operator identity; B/C for DC leads | Official site confirms operator presence/address. Use Viettel, QDND, and procurement searches for network-core or government-DC upgrade work; do not assign a DC without facility evidence. |
| Vanov Technology Unipessoal LDA | https://vanov.tl/ and https://vanov.tl/data-center-consultant-and-services/ | Dili, Aituri-Laran, Taibesi; eProcurement vendor address also Farol/Dili | B for DC services; A for eProcurement vendor awards | Local ICT/vendor lead, not proven public colo. eProcurement vendor record shows government awards: https://www.eprocurement.gov.tl/vendors/show/2922 |
| National Data Center + DR, ADB 55338-001 | https://www.adb.org/projects/55338-001/main | Site TBD, nation-wide output | A/proposed | ADB project output, proposed. Track ADB business opportunities, RRP, and TIC TIMOR announcements. |
| TL-IXP | https://anc.tl/media/2025/08/TOR-for-ANC-Technical-Adviser.pdf | Dili likely | A/interconnection | ANC-led IXP deployment is a future interconnection anchor, not a colo facility unless hosted services are separately evidenced. |
| TLSSC / Bebonuk cable landing station | https://timor-leste.gov.tl/?lang=en&p=38073&print=1 and https://www.submarinenetworks.com/en/systems/asia-australia/png-national/tlssc | Dili, Bebonuk | A for official landing; B for industry technical details | Use as a proximity anchor for Dili private-sector DC leads. Cable capacity is not DC capacity. |
| Zchwantech sovereign AI cloud/data-center feasibility | https://www.thestar.com.my/starpicks/2025/12/31/timor-leste-and-zchwantech-enter-landmark-ai-partnership | Site TBD | B/proposed feasibility | Regional press reports feasibility study for a National Sovereign AI Cloud and Data Centre to Tier 3+ standards. No official Timor-Leste government page found in this pass; keep B until confirmed by gov.tl/procurement. |
| Atal Networks Dili claim | https://atalnetworks.com/dili-timor-leste/ | Dili claimed | C | Directory/SEO-style hosting lead. Do not record as a real TL facility without address and operator confirmation. |

Operator query templates:

```text
"Timor Telecom" "data center" OR "data centre" OR "centro de dados"
site:timortelecom.tl "data center" OR "server" OR "fibra"
"Telkomcel" "Data Center Building" "Timor-Leste"
site:telkomcel.tl "Data Center" OR "ERP" OR "cloud"
site:telin.net "Telkomcel" "data center"
"Telemor" OR "Viettel Timor" "data center" OR "server"
site:telemor.tl "data" "center" OR "server"
"Vanov" "data center" OR "datacenter" OR "sentru dadus"
"TIC TIMOR" "Data Center" OR "sentru dadus"
"Zchwantech" "Timor-Leste" "data centre" OR "sovereign cloud"
```

## 2. Trade Press and Secondary Sources

Use trade press to seed leads and event dates, then backfill primary evidence.

| Source | URL | Use | Grade |
|---|---|---|---:|
| Data Center Dynamics | https://www.datacenterdynamics.com/en/tags/timor-leste/ | TLSSC landing/commercial launch and future DC coverage | B |
| DCD TLSSC landing | https://www.datacenterdynamics.com/en/news/timor-leste-south-submarine-cable-system-lands-in-dili/ | June 2024 landing details, DXN landing-station note | B |
| DCD TLSSC commercial launch | https://www.datacenterdynamics.com/en/news/timor-leste-launches-commercial-operations-of-first-international-subsea-cable/ | August 2026 commercial-operation context | B |
| Submarine Networks TLSSC | https://www.submarinenetworks.com/en/systems/asia-australia/png-national/tlssc | Cable-system technical summary and project timeline | B |
| Tatoli English | https://en.tatoli.tl/ | State news agency; official-adjacent government and telecom reporting | A/B depending on underlying source |
| Tatoli TLSSC landing | https://en.tatoli.tl/2024/06/24/timor-leste-begins-installation-of-southern-submarine-cable/19/ | Bebonuk landing-station confirmation | B unless paired with gov.tl |
| The Star Zchwantech article | https://www.thestar.com.my/starpicks/2025/12/31/timor-leste-and-zchwantech-enter-landmark-ai-partnership | Sovereign AI cloud/data-center feasibility lead | B |
| Developing Telecoms | https://developingtelecoms.com/ | Telecom market changes, cable, satellite, operator launches | B |
| Capacity Media | https://www.capacitymedia.com/ | Cable/operator market context | B |
| TeleGeography submarine cable map | https://www.submarinecablemap.com/submarine-cable/timor-leste-south-submarine-cable-tlssc | Cable map/landing context | B/C |
| PeeringDB | https://www.peeringdb.com/ | IXP/member/operator lead generation | C unless matched to operator |
| bgp.he.net / IPinfo | https://bgp.he.net/country/TL and https://ipinfo.io/AS136765 | ASN leads such as Vanov; not facility proof | C |
| DataCenterMap / Cloudscene / Datacenters.com | https://www.datacentermap.com/ ; https://cloudscene.com/ ; https://www.datacenters.com/ | Directory seeds only | C |

Trade query templates:

```text
site:datacenterdynamics.com "Timor-Leste" "data center" OR "subsea"
site:submarinenetworks.com "TLSSC" OR "Timor-Leste South Submarine Cable"
site:en.tatoli.tl "Data Center" OR "data centre" OR "digital"
site:en.tatoli.tl "Bebonuk" "cable"
site:thestar.com.my "Timor-Leste" "Zchwantech"
site:developingtelecoms.com "Timor-Leste" "data" OR "cable"
site:capacitymedia.com "Timor-Leste" "TLSSC" OR "data centre"
```

## 3. Directory-to-Primary Verification Workflow

1. Seed names from directories, ASN databases, hosting pages, and trade press.
2. Search exact name plus Dili/division and the operator domain.
3. Search exact name in CNA and eProcurement.
4. Search `timor-leste.gov.tl`, `tic.gov.tl`, `anc.tl`, and `mj.gov.tl/jornal`.
5. Record `status`, `grade`, and `missing_evidence`. Do not promote a directory-only or reseller claim above C.

Required verification fields:

```text
facility_or_project_name
operator_or_owner
division
locality/address
source_url
source_grade
status: operational | proposed | tender | feasibility | unverified
evidence_type: operator_page | tender | award | regulator | donor_project | trade_press | directory
capacity_mw_or_null
proxy_capacity_or_budget
notes_on_uncertainty
```

## 4. Per-Division Industry Search Recipes

Universal sweep for all 13 divisions:

```text
"{division}" "data center" OR "data centre" OR "centro de dados" OR "sentru dadus"
"{division}" "server" OR "servidor" OR "colo" OR "colocation"
"{division}" "pusat data" OR "jaringan fiber optik"
"{division}" "Timor Telecom" OR "Telemor" OR "Telkomcel"
"{division}" "fibra" OR "fibre" OR "banda larga"
"{division}" "EDTL" "substation" OR "power"
```

| Division | Search variants | Industry strategy |
|---|---|---|
| Aileu | Aileu; Laulara; Remexio; Liquidoe | Search operator backbone, municipal fiber, and government-network contractor posts. Low probability of facility. |
| Ainaro | Ainaro; Maubisse; Hato-Udo; Hatu-Udo | Search telecom shelters/backbone, municipal services, and disaster-resilience ICT; no current DC lead. |
| Baucau | Baucau; Baukau; Venilale; Vemasse; Laga | Search as DR candidate: `"Baucau" "disaster recovery" "data center"`, operator backbone, ADB procurement, local government ICT. |
| Bobonaro | Bobonaro; Maliana; Balibo; Batugade | Border-connectivity lead. Search customs/border digitalization, Telkomcel/Telemor/TT backbone, and government network nodes. |
| Cova Lima | Cova Lima; Covalima; Suai; Zumalai; Tilomar | Search Suai government/enterprise ICT, south-coast fiber, and oil/gas logistics IT. |
| Dili | Dili; Caicoli; Bebonuk; Comoro; Timor Plaza; Bidau; Taibesi; Vila Verde; Fatuhada; Cristo Rei; Metinaro | Main target. Search named operator pages plus MoF, TIC TIMOR, PMO Data Center, Telkomcel DC, TL-IXP, TLSSC, Vanov, and local hosting claims. |
| Ermera | Ermera; Gleno; Atsabe; Letefoho; Railaco | Low. Search municipal-network and operator coverage. Exclude agricultural/statistical "data" results. |
| Lautem | Lautem; Lospalos; Los Palos; Com; Tutuala; Iliomar | Low. Search eastern backbone, municipal ICT, operator facilities; no proven DC lead. |
| Liquica | Liquica; Likisa; Maubara; Bazartete | Dili-adjacent spillover possibility. Search coastal industrial, fiber route, and operator backbone terms. |
| Manatuto | Manatuto; Laclo; Laleia; Soibada; Natarbora | Watch energy and transmission work after the World Bank 2026 solar/BESS announcement, but require ICT/facility evidence. |
| Manufahi | Manufahi; Same; Betano; Alas; Fatuberliu; Turiscai | Betano power station creates power-context leads. Search DR/backup/ICT around Same and Betano. |
| Oe-Cusse Ambeno | Oe-Cusse; Oecusse; Oekusi; Oecussi-Ambeno; RAEOA; ZEESM; Pante Macassar | Special-region sweep. Search RAEOA/ZEESM procurement, local power, border systems, operator nodes, and government digital-service deployments. |
| Viqueque | Viqueque; Vikeke; Ossu; Uatolari; Uatucarbau; Lacluta | Low. Search municipal ICT, operator backbone, and public-service digitalization only. |

## 5. Seed List for Enumeration

| Seed | Division | Status tendency | Grade | Best evidence path |
|---|---|---|---:|---|
| TIC TIMOR / Electronic Government Data Center | Dili | Operational government data-center function | A | TIC TIMOR Data Center page and ADB coordination article. |
| Prime Minister's Office Data Center | Dili | Operational government DC anchor | A | Government fiber-contract release linking 12 municipal administrations to the PMO Data Center. |
| Ministry of Finance Data Center | Dili | Existing, repeatedly upgraded | A | CNA TENDER/13/MOF-2024 and eProcurement records 1219650, 979880, 1133403. |
| Telkomcel Data Center Building | Dili | Operational operator DC | A | Telin/Telkomcel official pages; then verify current address/specs. |
| National Data Center + DR | TBD, likely Dili primary plus DR elsewhere | Proposed | A/proposed | ADB 55338-001; watch RRP, ADB business notices, TIC TIMOR, CNA/eProcurement. |
| TL-IXP | Dili likely | Deployment / interconnection | A | ANC TOR and APNIC/ANC follow-up. |
| TLSSC Bebonuk CLS | Dili, Bebonuk | Operational connectivity anchor | A/B | Government landing release plus Submarine Networks/DCD. |
| Timor Telecom backbone/rooms | Dili + nationwide | Network infrastructure; DC unconfirmed unless named | A/C | Official operator site, government fiber contract, exact DC/server-room searches. |
| Telemor/Viettel network rooms | Dili + nationwide | Network infrastructure; DC unconfirmed unless named | A/C | Telemor official site, Viettel/QDND, procurement searches. |
| Vanov DC services | Dili, Taibesi/Farol | Vendor/service lead, not proven colo | B/C | Vanov site plus eProcurement vendor awards. |
| Zchwantech sovereign AI cloud/data center | Site TBD | Feasibility | B | The Star/Zchwantech leads; upgrade only with gov.tl/procurement. |
| Atal Networks "Tier III Dili" | Dili claimed | Unverified | C | Treat as lead only; require physical address/operator proof. |

## 6. Capacity and Status Rules

- Set `capacity_mw: null` for all Timor-Leste seeds unless the source directly discloses IT/electrical load.
- Keep cable and grid metrics in separate fields: TLSSC `27 Tbps` is network capacity; Hera/Betano `255 MW` and World Bank `73.7 MWac solar + 80.2 MWh BESS` are national power context.
- Use procurement amounts as proxies only: e.g. MoF eProcurement record 1219650 lists USD 884,375; 979880 lists USD 191,780.
- Treat Tier claims as claims, not certifications, unless backed by Uptime Institute/TIA documentation or an operator certificate.
- Status language must be conservative: `operational` for Telkomcel/TIC/PMO/MoF anchors where primary evidence supports existing facilities/functions; `proposed` for ADB national DC/DR; `feasibility` for Zchwantech; `unverified` for directories/resellers.

## 7. Common Traps

- Do not import Brazil ANATEL or Portugal ANACOM records. Timor-Leste's telecom regulator is ANC.
- Do not merge Timor Telecom, Telemor/Viettel, and Telkomcel/Telin/Telkom Indonesia.
- Do not confuse PT NTT Indonesia Technology, a vendor in the MoF tender trail, with NTT Global Data Centers.
- Do not treat Starlink, VSAT gateways, mobile towers, or ordinary operator offices as datacenters.
- Do not let local-language `dadus`/`data` results for statistics, census, agriculture, or health datasets become facility records.
- Do not assign Baucau or Oe-Cusse as DC sites without a site-specific source. They are priority hypotheses because of resilience/special-zone logic, not confirmed locations.
