# GW Explorer Official - Guinea-Bissau Datacenter Enumeration via Regulators, Power, ICT Government, Donor Projects and Investment Records

Date: 2026-08-12. Country: **GW Guinea-Bissau**. Division model verified against `world-manifest.jsonl`: **4 divisions** (`subnational_type = autonomous sector/province`): Bissau, East, North, South. Angle: **official and regulatory evidence** for government, donor-funded, telecom, enterprise and (rare) commercial data-centre facilities.

Reliability grades:
- **A** = primary/official evidence: ARN (ARN-TIC) notices/licences/consultations, MTTED/government portal pages, WARDIP/WARCIP official documents, UNDP/UNGM procurement notices and UNDP country reports, MENER/EAGB official documents, ITMA/government strategy documents (ENTD.GW), official cloud-region pages.
- **A-** = official operator page or official press release proving a named site, location or status, but not a regulator filing or procurement record; use cautiously for design capacity.
- **B** = strong secondary evidence: established local/regional press quoting officials (ANG, O Democrata GB, Lusa, RFI, DW), reputable international trade press with named parties and dates.
- **C** = lead only: blogs, directories, market reports, unsourced capacity tables, SEO pages, or claims that cannot be tied to an official page, procurement notice or operator page.

Use the grade on the *specific claim*. A facility can be **A** for existence, **B** for announced MW (if any), and **C** for commissioning status if those facts come from different evidence chains.

---

## 0. Guinea-Bissau-specific structure facts

- Guinea-Bissau has **no national data-centre register, no public building-permit database and no centralized environmental-permit portal** verified in this pass. The official chain must be built from: project name/SPV -> UN/donor procurement notice or ministry project page (WARDIP/WARCIP, UNDP, MTTED) -> project-level environmental/social documents (EIA/EIASS/ESMP, resettlement plans) -> ARN licence/consultation evidence where telecom is involved -> power evidence from MENER/EAGB -> operator/government official page.
- The country is administratively **8 regions plus the Bissau autonomous sector** (Cacheu, Gabu, Oio, Bafata, Quinara, Tombali, Biombo, Bolama-Bijagos + Bissau). The manifest division model groups them into four: **Bissau** (autonomous sector), **North** (Cacheu, Oio, Biombo), **East** (Bafata, Gabu), **South** (Quinara, Tombali, Bolama-Bijagos). Treat division coverage as complete only when every division below has been searched or explicitly marked `no_projects: true` with date and query notes.
- **Portuguese is the working language** of government and media. Use Portuguese terms in every query: `centro de dados`, `data center`, `data centre`, `centro de processamento de dados`, `sala de servidores`, `servidor`, `colocation`/`colo`, `cloud`, `fibra optica`, `backbone`, `licenca`, `licenciamento`, `autorizacao`, `concurso publico`, `concurso internacional`, `contrato`, `gerador`, `energia`, `subestacao`, `EIA`/`EIASS`/`estudo de impacto ambiental`, `parecer ambiental`.
- **Expected official yield is tiny: 0-2 verified facility records per full sweep.** As of this methodology date the only confirmed facility-level official record is the UNDP/Japan-financed **National Technology Data Center Park / Centro Nacional de Dados** in Alto Bandim, Bissau (construction started March 2026; includes the National Data Center, the new ITMA headquarters and facilities for data-protection and cybersecurity agencies). Everything else is expected to be negative or connectivity/government-room leads.
- **No hyperscaler public cloud region** (AWS/Azure/GCP/Oracle) lists Guinea-Bissau as of this date. Cloud/edge/CDN/satellite presence is ecosystem evidence, not a facility record.
- **No independent electricity-sector regulator register** was verified. MENER (Ministerio da Energia) handles energy policy and tariff regulation, EAGB is the state utility, and ARSECO regulates *fuels*, not electricity. Do not invent an electricity permit register.
- **No dedicated personal-data-protection law/authority register** was verified. Data protection and cybersecurity are part of the WARDIP reform agenda and of the National DC Park programme; ARN has run public consultations on a draft e-transactions law. There is no DPA register to query yet.
- Capacity claims are rare. Do not convert a building/construction notice into an operational IT load without a commissioning, procurement completion, or official status source.

---

## 1. Regulator - Autoridade Reguladora Nacional das Tecnologias de Informacao e Comunicacao (ARN / ARN-TIC)

Official site: https://arn.gw/ (address: Bairro de Enterramento, atras do Hospital Militar, Bissau; phone +245 96 699 31 31).

Verified points:
- ARN is the electronic-communications regulator under the **Lei de Base das Tecnologias de Informacao e Comunicacao, Lei n. 5/2010, de 27 de Maio** (published in the 3rd supplement to Boletim Oficial n. 21), which extinguished the Instituto das Comunicacoes da Guine-Bissau (ICGB); ARN succeeds ICGB's legal personality.
- ARN is **not a data-centre-permit authority**. Use it for connectivity-adjacent evidence: operator licences, spectrum/radioelectric fees consultations, market observatory reports, public consultations, .gw ccTLD (NIC.gw) and any telecom-infrastructure mandate. It is also a useful mirror of sector events (e.g., its notice against unauthorised Starlink service provision; the 2021 delivery of a network-operator licence to Guine-Telecom; consultation on the draft Lei das Transacoes Electronicas).
- ARN and WARDIP publish environmental/social material for the **Espinha Dorsal Nacional (national fibre backbone)**. The verified WARDIP EIASS page links the PDF `WARDIP-Rapport-FINAL-EIESS-PORTUGAISE-MARC-2026-VALIDE.pdf`; use it as the single most relevant official environmental document for backbone-adjacent infrastructure, and continue checking ARN/WARDIP for future backbone/data-centre EIA documents.
- ARN's market observatory (e.g., Observatorio de mercado 3o trimestre 2025) is a Grade-A source for operator counts and sector context, not for facilities.

What to extract: licensee/SPV, licence class, authorisation scope, site wording, dates, consultation notice dates, and related operator names (Spacetel/MTN/Telecel, Orange, Guine-Telecom, Guinetel).

ARN query templates:
```text
site:arn.gw ("centro de dados" OR "data center" OR datacentre)
site:arn.gw ("licenca" OR "licenciamento" OR "autorizacao") ("{operador}" OR "{SPV}")
site:arn.gw ("EIASS" OR "Estudo de Impacto Ambiental" OR "Espinha Dorsal")
site:arn.gw "consulta publica" "transacoes electronicas"
"ARN" "Guine-Bissau" "{operador}" licenca
"ARN-TIC" "Guine-Bissau" "{operador}" licenca
site:nic.gw registo dominio
```

Grade guidance: **A** for ARN pages, notices and official downloads; **B** for press quoting an ARN action; **C** for generic lists of licensees without an ARN page.

---

## 2. Power and energy evidence

### 2.1 Ministerio da Energia (MENER)

Official site: https://ministeriodaenergia.gw/ (also reachable via the government portal https://bissaugov.com/).

Verified points:
- MENER is responsible for electricity policy, electrification, renewables and **tariff regulation**. It hosts a **Licenciamento energetico** (energy licensing) section - the closest thing to a licensing surface for generation/self-generation projects (e.g., diesel gensets or solar for a data centre).
- There is **no independent electricity regulatory agency register** verified in this pass. ARSECO (Autoridade Reguladora do Sector de Combustiveis) regulates fuels only - do not confuse it with an electricity regulator.
- Relevant grid context: EAGB is the monopoly state utility; a Portuguese consortium (EDP/ADP/LCBS) managed EAGB under a World Bank-financed contract from 2019; the Karpower floating plant contract was terminated; Guinea-Bissau has been receiving power from the sub-regional OMVG interconnection project since late August (press, Grade B). Grid reliability is poor; data-centre-class loads are expected to rely on on-site diesel/solar generation, which is exactly what the energy-licensing surface should capture.

MENER templates:
```text
site:ministeriodaenergia.gw ("licenciamento" OR "licenca" OR "autorizacao") "{empresa}"
site:ministeriodaenergia.gw ("centro de dados" OR "data center" OR "servidores")
site:ministeriodaenergia.gw ("gerador" OR "grupo eletrogenio" OR "autoproducao" OR "solar")
"Ministerio da Energia" "Guine-Bissau" "{empresa}" (energia OR gerador OR licenca)
"EAGB" "{localidade}" (subestacao OR "posto de transformacao")
```

### 2.2 Utilities and grid operators

- EAGB - Eletricidade e Aguas da Guine-Bissau: state utility (generation/transmission/distribution of electricity plus water). No functioning official website was verified in this pass (Facebook page and Wikipedia/Wikidata entries only); use official press (ANG, Lusa, ministry communications) for corroboration. EAGB represents Guinea-Bissau in the West African Power Pool (WAPP).
- OMVG interconnection (Gambia river basin energy project): supplies power into Guinea-Bissau; relevant as a power-supply context source, not a facility census.
- Antula thermal power plant (outskirts of Bissau): the ACE terrestrial extension terminates at Antula - a power/landing adjacency fact, not a data centre.

Utility templates:
```text
"EAGB" "{localidade}" ("energia" OR "subestacao" OR "corte")
"{localidade}" "Guine-Bissau" ("gerador" OR "grupo eletrogenio" OR "solar")
("OMVG" OR "interligacao") "Guine-Bissau" energia
"Antula" ("central termica" OR energia) Bissau
```

Grade guidance: **A** for MENER official pages/documents and ministry communications; **B** for utility/donor press releases without documents; **C** for reported MW without a licensing/utility source.

---

## 3. Environment - project-level EIA/EIASS evidence

There is **no central environmental-permit portal** verified for Guinea-Bissau. Environmental review is project-level and donor-driven; look for these document types:
- **EIASS Espinha Dorsal Nacional** (published on ARN's site) - national backbone project.
- **WARCIP ACE resettlement plan** - "Plano de acao para reinstalacao - Projeto de amarracao de cabos submarino ACE, Guine-Bissau, WARCIP" (2019, published via odemocratagb.com) - cable-landing adjacent.
- **WARDIP environmental/social framework documents** (e.g., Quadro de Politica de Reassentamento, QPR, PDF on ibapgbissau.org) - WARDIP components include connectivity infrastructure.
- UNDP procurement notices for the National DC Park (see section 6) may embed environmental requirements even when no separate EIA is public.

Templates:
```text
"Guine-Bissau" ("estudo de impacto ambiental" OR EIA OR EIASS) "{projeto}"
filetype:pdf "Guine-Bissau" ("data center" OR "centro de dados") (ambiente OR EIA OR EIASS)
filetype:pdf (WARCIP OR WARDIP) "Guine-Bissau" (reassentamento OR "impacto ambiental")
site:arn.gw EIASS "Espinha Dorsal"
("{SPV}" OR "{empresa}") "Guine-Bissau" "gerador" (ambiente OR ruido OR combustivel)
```

Grade guidance: **A** for official EIA/EIASS/ESMP documents; **B** for official project pages describing environmental clearance; **C** for claimed environmental compliance with no document. Expect these documents to be scarce and rarely naming a data centre.

---

## 4. Planning and building permits - municipal and sector administrations

No national or public permit database was verified. Permits for Bissau-city sites would flow through the **Camara Municipal de Bissau**; regional sites through regional/sector administrations. Treat any permit reference found in press or official minutes as a lead (Grade B/C) unless the official document is located.

Templates:
```text
"Camara Municipal de Bissau" ("{empresa}" OR "centro de dados" OR "licenca de construcao")
site:bissaugov.com "construcao" ("centro de dados" OR "data center" OR edificio)
"{localidade}" "Guine-Bissau" ("licenca de construcao" OR alvara) "{empresa}"
("Alto Bandim" OR Bissau) construcao ("data center" OR "centro nacional de dados")
```

Extract: authority, plot/parcel, applicant/SPV, use description, permit decision/date, floor area, mechanical/generator references. **A** only when the official document or official permit notice is found.

---

## 5. Data protection, cybersecurity and public-sector ICT

- **No personal-data-protection law/authority register verified** as of this date. WARDIP explicitly includes cybersecurity and data-protection strengthening; the National DC Park programme includes facilities for data-protection and cybersecurity agencies; ARN has consulted on a draft e-transactions law. Use these as forward-looking hooks, not as registers to query.
- **ITMA** - Instituto Tecnologico para a Modernizacao da Administracao (also written Instituto de Tecnologias de Informacao e Modernizacao Administrativa) - is the government ICT institute. Japan finances its purpose-built headquarters (about EUR 1.93 million, announced 2024-03-29 by the UNDP Resident Representative); the Prime Minister (Rui Duarte de Barros) stated the ITMA building will house the "Data Center" da Guine-Bissau. The ITMA building is part of the National Technology Data Center Park at Alto Bandim.
- **ENTD.GW** - Estrategia Nacional de Transformacao Digital - was launched at the Palacio do Governo in Bissau; official strategy documents call for phased construction of a national data centre in-country.
- **WARDIP** (wardip.gw) - West Africa Regional Digital Integration Program (successor of WARCIP), World Bank-financed, executed under MTTED; components: legal/regulatory reform, national and international connectivity (national fibre backbone, PPP), cybersecurity/data protection, digital entrepreneurship, public-service digitalisation. Check its documents page for data-centre-relevant procurement and E&S documents.

Templates:
```text
site:wardip.gw ("centro de dados" OR "data center" OR backbone OR "fibra optica")
site:wardip.gw (ITMA OR ciberseguranca OR "protecao de dados")
"ITMA" "Guine-Bissau" ("data center" OR "centro de dados" OR modernizacao)
("ENTD.GW" OR "Estrategia Nacional de Transformacao Digital") "Guine-Bissau" "centro de dados"
site:bissaugov.com ("transformacao digital" OR "centro de dados" OR ITMA)
"Guine-Bissau" ("lei de protecao de dados" OR "autoridade de protecao de dados")
```

Grade guidance: **A** for ITMA/WARDIP/ministry official pages and strategy documents; **B** for official press; **C** for media summaries without documents.

---

## 6. Donor procurement, UN and investment records

- **UNDP Guinea-Bissau** is the implementation partner for the National Technology Data Center Park: procurement notice **UNDP-GNB-00270 "Construction of National Technology Data Center Park"** (UNGM notice 278362, verified as published **2025-09-12**, deadline **2025-10-08**); UNDP/PNUD Guinea-Bissau reporting and newsletters are the best official sources for launch/implementation status. UNDP tenders are Grade-A facility evidence for reference, title, beneficiary country and procurement dates; use attached procurement documents or official UNDP/PNUD reporting for scope details.
- **Guine-Bissau Investimentos / Agencia de Promocao de Investimentos** - the investment promotion agency (referenced in the official 2021 investment guide); use for foreign-investor announcements and ICT/digital-infrastructure investment leads.
- **CFE - Centro de Formalizacao de Empresas / Guiche Unico de Criacao de Empresas**: https://cfegb.com/ - company incorporation and SPV resolution. The site is indexed as an official creation-of-companies platform but can return intermittent server errors; use the eRegulations company-creation page as fallback confirmation of the CFE procedure.
- **eRegulations Guine-Bissau**: https://guineebissau.eregulations.org/ - official procedures portal (licences, permits); search for data-centre/telecom procedure categories.
- **gov-gb.com** - NIF and company registration services portal; **bissaugov.com/investimento** - government investment page.

Templates:
```text
site:ungm.org "Guinea-Bissau" ("data center" OR "centro de dados" OR "national technology")
UNDP-GNB ("data center" OR "centro de dados" OR ITMA)
(tender OR concurso) "Guine-Bissau" ("data center" OR "centro de dados" OR backbone)
(site:cfegb.com OR site:guineebissau.eregulations.org) (telecomunicacoes OR licenca OR data)
("Guine-Bissau Investimentos" OR "promocao de investimentos") "Guine-Bissau" "{empresa}" (ICT OR digital OR data)
```

Grade guidance: **A** for UNGM/UNDP notices and official agency registrations; **B** for investment-promotion announcements; **C** for investor decks or directories without filings.

---

## 7. Official cloud-region check

Run on every batch. The absence of Guinea-Bissau on an official cloud region list means no Guinea-Bissau cloud-region facility should be created.

Official pages:
- AWS Global Infrastructure / Regions and AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Microsoft Azure geographies and region list: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/ and https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle Cloud regions: https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm

Templates:
```text
site:aws.amazon.com "Guinea-Bissau" "Region"
site:learn.microsoft.com/azure "Guinea-Bissau" "region"
site:cloud.google.com/about/locations "Guinea-Bissau"
site:oracle.com/cloud "Guinea-Bissau" "cloud region"
```

Grade guidance: **A** only for official provider region/location pages. Cloud offices, partner nodes, caches, CDN PoPs, satellite broadband and edge nodes are ecosystem notes, not DC facility records.

---

## 8. Per-division official coverage map

Working region mapping for the 4-division model verified against `world-manifest.jsonl`: Bissau = Sector Autonomo de Bissau; North = Cacheu, Oio, Biombo; East = Bafata, Gabu; South = Quinara, Tombali, Bolama-Bijagos.

| Division | Capitals / hubs and official bodies | Expected official outcome | Core official queries |
|---|---|---|---|
| **Bissau** | Bissau city: Alto Bandim, Antula, Bairro de Enterramento (ARN), Palacio do Governo; MTTED, ITMA, EAGB, Camara Municipal de Bissau, UNDP country office | Positive: **National Technology Data Center Park / Centro Nacional de Dados** (construction, UNDP-GNB-00270); ITMA HQ within the park; ACE terrestrial extension to Antula; GwIX and telco data rooms as leads only | `site:ungm.org "Guinea-Bissau" "data center"`, `"Alto Bandim" "centro nacional de dados"`, `site:wardip.gw "centro de dados"`, `site:bissaugov.com ("data center" OR "centro de dados")`, `"PNUD" "centro nacional de dados"` |
| **North** | Cacheu (incl. Suro/Suru landing area), Oio (Bissora, Mansoa), Biombo (Quinhamel) | ACE landing station lead at **Suro/Suru, Cacheu** (landing point, DC-adjacent, not itself a DC); backbone route; no DC records expected | `("Suro" OR "Suru") "Guine-Bissau" (ACE OR "cabo submarino")`, `site:arn.gw ("Espinha Dorsal" OR EIASS)`, `"Cacheu" ("centro de dados" OR "sala de servidores")`, `("Oio" OR "Biombo") (servidores OR "data center") "Guine-Bissau"` |
| **East** | Bafata, Gabu | Negative for DCs; backbone route and EAGB distribution points only | `("Bafata" OR "Gabu") "Guine-Bissau" ("data center" OR "servidores" OR "fibra")`, `site:ministeriodaenergia.gw (Bafata OR Gabu) energia` |
| **South** | Quinara (Buba), Tombali (Catio), Bolama-Bijagos | Negative for DCs; ITMA programme mentions interior benefits incl. Bijagos; no records expected | `("Quinara" OR "Tombali" OR "Bolama" OR "Bijagos") "Guine-Bissau" ("data center" OR "servidores")`, `("Buba" OR "Catio") "centro de dados"` |

Generic sweep for every division:
```text
("{division}" OR "{region}") "Guine-Bissau" ("data center" OR "data centre" OR "centro de dados" OR "sala de servidores")
(site:*.gov.gw OR site:bissaugov.com) "{region}" ("data center" OR servidores OR "fibra optica")
"{capital}" "Guine-Bissau" (gerador OR energia OR licenca) "{empresa}"
filetype:pdf "{region}" "Guine-Bissau" ("impacto ambiental" OR EIA OR EIASS)
```

---

## 9. Verification recipe

1. Start with the named record: **National Technology Data Center Park / Centro Nacional de Dados, Alto Bandim, Bissau** (UNDP-GNB-00270, UNGM 278362, UNDP/PNUD Guinea-Bissau reporting/newsletters, March 2026 construction coverage). Resolve aliases: "National Technology Data Center Park", "Centro Nacional de Dados", "Centro de Dados da Guine-Bissau", "ITMA building/data centre" are parts of one Bissau programme.
2. Seek permit/procurement evidence in this order: UNGM/UNDP notice -> MTTED/WARDIP project page -> project-level EIA/EIASS/ESMP -> ARN licence/consultation -> MENER/EAGB power evidence -> CFE/company registration -> official operator/government page.
3. For connectivity-adjacent assets (ACE landing at Suro, terrestrial link to Antula; national backbone), record them as DC-adjacent leads with their own status, not as data-centre facilities.
4. Separate facts: `status`, `capacity_mw`, `racks`, `tier`, `address`, `division`, `operator`, `SPV`, `evidence_date`, `source_urls`, `evidence_grade`.
5. For capacity, prefer procurement/EIA/power records over press. Record announced design capacity separately from commissioned/operational capacity (expected: no reliable capacity figures for GW yet).
6. Use `no_projects: true` only after running division templates and checking official/national sources for the relevant capitals/towns.
7. Re-run the official cloud-region check every batch.

Status ladder: rumour < MoU < announced < land acquired < permit/procurement applied < permit/procurement granted < construction started < commissioned/inaugurated < operational. Do not skip ladder stages without evidence.

---

## 10. Pitfalls and corrections from draft verification

- **ARN licence does not equal data-centre facility.** It is a Grade-A connectivity/regulatory lead (operators, backbone, landing station, spectrum).
- **No electricity-permit register and no data-protection register exist yet.** Do not fabricate queries against agencies that do not publish registers; use MENER licensing and WARDIP/ITMA documents instead.
- **The National DC Park is construction-stage, not operational.** March 2026 coverage says completion planned for July 2026; capacity is not disclosed. Keep `status=construction`, `capacity_mw=null` until an official commissioning source appears.
- **ACE landing (Suro) and Antula power plant are DC-adjacent**, not data centres; the terrestrial link is 30 km Suro -> Antula.
- **No hyperscaler region, no Uptime records, no commercial colocation provider** were verified for GW; directories will mostly return noise - treat as leads only.
- **Telecel vs MTN vs Spacetel**: the operator formerly known as Spacetel/MTN Guinea-Bissau transferred to Telecel Group (completed 2024-08-07). Use the current brand for searches and note the aliases.
- **Starlink is being used in GW without authorisation** (ARN notice); satellite internet presence is not a data-centre record.
- Blogs and aggregators (e.g., conosaba, tender-scraper sites) are Grade C unless they reproduce an official notice; verify through UNGM/ARN/WARDIP before upgrading.

## Grade-A backbone URLs

| Source | URL | Use |
|---|---|---|
| ARN (ARN-TIC) | https://arn.gw/ | Telecom licences, consultations, observatory, backbone EIASS, .gw registry |
| ARN/WARDIP EIASS Espinha Dorsal | https://arn.gw/ and https://wardip.gw/estudo-de-impacto-ambiental-e-social-simplificado-eiass-espinha-dorsal-nacional/ | National backbone environmental document; WARDIP page links the verified EIASS PDF |
| Government portal | https://bissaugov.com/ | Ministries, Council of Ministers, strategy documents |
| MTTED/WARDIP | https://wardip.gw/ | Digital-integration programme, backbone, cybersecurity/data-protection reforms |
| MENER | https://ministeriodaenergia.gw/ | Energy licensing, tariff regulation, electrification |
| UNDP GB | https://www.undp.org/guinea-bissau ; UNDP-GNB-00270 on https://www.ungm.org/Public/Notice/278362 | National DC Park procurement and annual reports |
| ENTD.GW / ITMA | https://bissaugov.com/ ; ITMA coverage via https://maisafrika.com/noticias/ultimahora/guine-bissau-japao-financia-construcao-do-itma/ | Digital strategy; ITMA/data-centre building |
| CFE | https://cfegb.com/ | Company incorporation / SPV resolution; intermittently returns server errors, so verify through eRegulations when needed |
| eRegulations GB | https://guineebissau.eregulations.org/ and https://guineebissau.eregulations.org/menu/5?l=pt | Official procedures (licences/permits) and fallback CFE/company-creation procedure |
| Cloud region pages | AWS/Azure/GCP/Oracle URLs in section 7 | Guinea-Bissau cloud-region exclusion check |
