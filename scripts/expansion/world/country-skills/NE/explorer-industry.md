# NE Explorer Industry - Niger Datacenter Discovery (industry/vendor methodology)

Date verified: 2026-08-12. Scope: industry media, operator pages, vendor pages, directories, IX/peering records, local press, and market context for Niger datacenter enumeration.

Division model: **region / capital urban community**, complete at 8 divisions: Niamey, Agadez, Diffa, Dosso, Maradi, Tahoua, Tillabéri/Tillaberi, and Zinder. Use explorer-official.md for the official structure sources and per-division rules.

## 0. Market Reality

- Niger's datacenter market remains nascent and **Niamey-centric**. The only credible facility-level public evidence found is government/public-sector: the AfDB-supported national Data Center/DTS datacenter program and a Ministry of Finance data-center procurement lead.
- No commercial carrier-neutral colocation facility page in Niger was found on 2026-08-12. Directory searches tend to return **Nigeria** results; do not confuse Niger (NE) with Nigeria (NG).
- Niger is landlocked. There are no in-country submarine cable landings. Connectivity is terrestrial through older exits toward Benin/Burkina/Nigeria and the AfDB-financed DTS routes toward Algeria and Chad.
- The DTS project has now moved beyond the draft's old target-date wording: AfDB reported provisional handover of more than 1,000 km of fibre on 2025-11-14, while the data-center component still needs separate commissioning/certification evidence.
- No active IXP evidence was found. PCH lists Niger IXP in Niamey but the historical record is not proof of an operating interconnection facility: https://www.pch.net/ixp/details/1921 .
- Electricity is the main plausibility constraint. NIGELEC and ARSE are mandatory checks for any claimed facility-scale load: https://www.nigelec.ne/ and https://arse.ne/electricite/ .
- No AWS, Azure, Google Cloud or Oracle public cloud region in Niger was found on official region lists on 2026-08-12.
- No Uptime Institute-certified Niger facility was found. Treat "Tier III" phrases in media/vendor pages as unproven unless a certification record names the facility.

## 1. Search Vocabulary

French dominates the signal. Use English for regional trade press and vendor marketing.

```text
French:
"centre de données" OR datacenter OR "data center" OR "salle serveur" OR "salle informatique"
colocation OR hébergement OR cloud OR "cloud souverain" OR infogérance
"point d'échange" OR IXP OR peering OR "dorsale" OR "fibre optique" OR "très haut débit"
"Tier III" OR "tier 3" OR rack OR MW OR kVA OR onduleur OR "groupe électrogène"

English:
"data center" OR "data centre" OR datacenter OR colocation OR hosting OR cloud
IXP OR peering OR backbone OR "terrestrial fibre" OR "Tier III" OR racks OR MW
```

False-positive filters:

```text
-Nigeria -Lagos -Abuja -Kano when searching for Niger-specific facilities
"Niger" "Niamey" datacenter
"Niger Republic" datacenter
"Niger" "centre de données" -Nigeria
```

## 2. Industry Pipeline

### 2.1 Trade and local press

| Source | URL / route | Good for | Grade |
|---|---|---|---|
| Agence Ecofin | https://www.agenceecofin.com/ | DTS execution, telecom regulation, operator M&A, digital economy coverage. Example DTS execution article: https://www.agenceecofin.com/actualites-numerique/3001-125370-niger-la-dorsale-transsaharienne-a-fibre-optique-atteint-97-de-realisation | B; A-adjacent only when quoting a named official record. |
| Ecofin Agency | https://www.ecofinagency.com/ | English-language corroboration of Niger telecom/digital items. | B. |
| ANP | https://anp.ne/ | State news agency; best media source for official statements, including national DC announcement. | B+ for named official statements; not a substitute for procurement/certification. |
| Le Sahel | https://www.lesahel.org/ | State daily; interviews, DTS reception, ministry activity. Example minister interview on data center target: https://www.lesahel.org/entretien-accorde-a-la-rtn-par-le-ministre-de-la-communication-des-postes-et-de-leconomie-numerique-m-sidi-mohamed-raliou-nous-sommes-en-train-de-construire-un-data-center/ | B. |
| WeAreTech | https://www.wearetech.africa/ | Summaries of public-management digital projects; national DC article mirrors official statement: https://www.wearetech.africa/en/fils-uk/news/public-management/nigers-14-3m-data-center-reaches-13-completion-on-track-for-september-finish | B/C depending on sourcing. |
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/ | Data-center and telecom M&A context; Niger search returned Zamani/Niger Telecom merger coverage but no facility page. | B when present. |
| Developing Telecoms / Connecting Africa / Telecom Review Africa / TechAfrica News | https://developingtelecoms.com/ ; https://www.connectingafrica.com/ ; https://www.telecomreviewafrica.com/ ; https://techafricanews.com/ | Regional telecom context; Niger items are infrequent. | B/C; confirm against official pages. |
| ActuNiger / Journal du Niger / Echos du Niger / Air Info Agadez / Niger Diaspora | https://www.actuniger.com/ ; https://www.journalduniger.com/ ; https://lesechosduniger.com/ ; https://airinfoagadez.com/ ; https://nigerdiaspora.net/ | Local leads, regional corroboration, operator names, power/project stories. | B/C; do not grade facility facts above source detail. |

### 2.2 Directories, interconnection and certifications

| Source | URL / route | Use | Grade |
|---|---|---|---|
| PCH IXP directory | https://www.pch.net/ixp/details/1921 | Niger IXP historical/on-hold status in Niamey. | A for PCH record. |
| PeeringDB | https://www.peeringdb.com/ | NE org/facility/IX search; useful for active interconnection, not facility proof alone. | A/B for network records. |
| DataCenterMap | https://www.datacentermap.com/africa/ and country search | Discovery only. Country-level searches may confuse Niger with Nigeria; DataCenterMap Africa page lists countries and shows Nigeria, but no verified Niger facility was found. | C. |
| Baxtel / Inflect / DataCenterPlatform / DCJournal | Provider/country searches | Discovery only; many hits are Nigeria. | C. |
| Uptime Institute | https://uptimeinstitute.com/tier-certification | Certification check for Tier claims. | A if record exists; negative check found no Niger record. |
| SubmarineCableMap / TeleGeography | https://www.submarinecablemap.com/ | Negative check: no Niger landing station because landlocked. | B/A for map context; not DC evidence. |
| Cloud region lists | AWS/Azure/GCP/OCI official pages in explorer-official.md | Negative check for public cloud regions. | A. |

## 3. Industry Query Templates

Use one line at a time.

```text
site:agenceecofin.com Niger datacenter
site:agenceecofin.com Niger "centre de données"
site:agenceecofin.com Niger "dorsale transsaharienne"
site:ecofinagency.com Niger "data center"
site:ecofinagency.com Niger fibre digital
site:lesahel.org Niger "data center"
site:lesahel.org Niger "centre de données"
site:lesahel.org Niger "dorsale transsaharienne"
site:anp.ne Niger "data center"
site:anp.ne Niger "centre de données"
site:wearetech.africa Niger "data center"
site:datacenterdynamics.com/en/news/ Niger "data center"
site:datacenterdynamics.com/en/news/ "Zamani" Niger
site:developingtelecoms.com Niger "data center"
site:connectingafrica.com Niger "data center"
"Niger Republic" "data center" Niamey
"Niger" "data center" Niamey -Nigeria -Lagos -Abuja
"Niger" "centre de données" Niamey
"Niger" colocation hébergement Niamey
```

Operator-seed block:

```text
"Niger Telecoms" datacenter
"Niger Telecoms" "centre de données"
"Niger Telecoms" hébergement colocation cloud
"SahelCom" Niger datacenter
"Zamani Telecom" Niger datacenter
"Zamani Telecom" Niger "centre de données"
"Orange Niger" "centre de données"
"Airtel Niger" datacenter
"Airtel Niger" "centre de données"
"Moov Africa Niger" datacenter
"Moov Niger" "centre de données"
"AFR-IX" Niger Niamey datacenter
"Starlink" Niger "data center"
"Starlink" Niger datacenter
```

Directory/interconnection block:

```text
site:peeringdb.com Niger Niamey
site:pch.net Niger IXP Niamey
site:datacentermap.com Niger Niamey datacenter -Nigeria
site:baxtel.com Niger Niamey datacenter -Nigeria
site:uptimeinstitute.com/tier-certification Niger Niamey
"Niger" "IXP" Niamey
"Niger" peering Niamey
```

## 4. Cloud, CDN and Edge Handling

Official region checks:

```text
site:aws.amazon.com/about-aws/global-infrastructure Niger
site:learn.microsoft.com/en-us/azure/reliability/regions-list Niger
site:cloud.google.com/about/locations Niger
site:docs.oracle.com/iaas/Content/General/Concepts/regions.htm Niger
"Niger" "AWS Local Zone"
"Niger" "Azure region"
"Niger" "Google Cloud region"
"Niger" "Oracle Cloud region"
```

Rules:

- A hyperscaler customer, marketplace partner, CDN cache, Starlink licence, or edge PoP is not a datacenter campus.
- Local hosting marketed to Niger from France, Abidjan, Dakar, Lagos or elsewhere is not a Niger facility unless the provider names a physical Niger site and the claim is corroborated.
- Airtel Africa/Nxtra data-center evidence currently points to Lagos, Nigeria, not Niger: https://www.airtel.africa/data-centers . Do not import group-level or Nigeria assets into NE.

## 5. Reliability Grades

- **A:** official operator facility page, government/ministry/ARCEP/HAPDP/ARMP/NIGELEC/ARSE record, AfDB project/procurement/E&S document, PeeringDB/PCH record, official cloud-provider region page, audited filing.
- **B:** strong trade or local press: ANP/Le Sahel named-official relay, Agence Ecofin/Ecofin Agency, DCD, Developing Telecoms, Connecting Africa, Telecom Review Africa, TechAfrica News, WeAreTech, credible vendor case study.
- **C:** directory listings, marketplace pages, social posts, paid market-report teasers, VPS-reseller pages, old MoUs, claims lacking address/status/power/operator evidence.
- **U:** no source, dead page, social-only claim, or source does not support the field.

Field-level rule: location, owner/operator, function, status, capacity, power, certification and tenant claims are graded separately. An operator licence is A for operator existence, not for datacenter function.

## 6. Known Facilities / Projects and Evidence Status

| Seed | URLs | Location signal | Grade | Industry handling |
|---|---|---|---|---|
| National Data Center / DTS data center | ANP 2025-02-27: https://anp.ne/le-niger-entend-se-doter-dun-data-center-et-1000-km-de-fibre-optique-sur-axes-et-troncons-du-pays-ministre/ ; AfDB project: https://www.afdb.org/en/projects-and-operations/p-z1-gb0-024 ; AfDB 2025 handover release: https://www.afdb.org/en/news-and-events/press-releases/niger-takes-major-step-towards-high-speed-connectivity-handover-over-1000-km-fibre-optic-cable-88768 | Niamey; AfDB E&S search result indicates PK5 / Arrondissement Communal Niamey V for the EIES subproject. | A for AfDB project scope; B+ for ANP ministerial announcement/status; C/U for Tier III certification and live operational status. | Primary Niger DC record. Keep deduped with DTS/ANSI/government-cloud mentions unless a second site is proven. |
| Ministry of Finance data center lead | Procurement plan: https://www.marchespublics.ne/marches-publics/572 ; provisional awards route: https://www.marchespublics.ne/avis-dattribution-provisoire | Likely Niamey, but visible portal text does not provide full address. | A for procurement; U for operational/facility classification. | Internal government data-center lead. Search awards, final acceptance and current ministry pages before creating a separate facility record. |
| DTS fibre backbone | AfDB/ANP/Ecofin/Le Sahel, especially AfDB 2025 handover release and Agence Ecofin 97% execution article: https://www.agenceecofin.com/actualites-numerique/3001-125370-niger-la-dorsale-transsaharienne-a-fibre-optique-atteint-97-de-realisation | National and cross-border terrestrial fibre. | A/B for network project; not a datacenter. | Use as interconnection context only. |
| Niger Telecoms | https://www.nigertelecoms.ne/ ; ARCEP annual-report pages | Niamey HQ and national backbone/exchanges. | A for operator; U for public DC service. | No public Niger Telecoms colo/cloud facility page found. Facebook/social claims of a Niger Telecoms data center stay C/U until official corroboration. |
| Zamani Telecom / former Orange Niger | Ecofin/DCD M&A coverage and ARCEP seed list. Example: https://www.datacenterdynamics.com/en/news/?tag=zamani-telecom | Niamey plus national mobile network. | A for licensed operator when sourced to ARCEP; U for facility. | Search for hosting/colo every cycle. Merger news is not a DC lead unless asset-transfer documents name facilities. |
| Airtel Niger | ARCEP seed list; group DC page https://www.airtel.africa/data-centers | Niger mobile operator; group DC assets in Nigeria and other markets. | A for operator when sourced to ARCEP; U for Niger DC. | Do not count Nxtra Lagos or Airtel Nigeria pages as Niger. |
| Moov Africa Niger | ARCEP seed list and group/operator pages. | Niger mobile operator. | A for operator when sourced to ARCEP; U for Niger DC. | Maroc Telecom group has DC/network assets elsewhere; require Niger-specific proof. |
| Niger IXP | https://www.pch.net/ixp/details/1921 | Niamey. | A for PCH record. | Historical/on-hold IX lead; no facility/subnet evidence found. |
| Atal Networks VPS Niamey | https://atalnetworks.com/niamey-niger-vps-server/ | Niamey claimed. | C/U. | Reseller-marketing lead only; do not count without named facility/operator. |
| Hyperscaler regions | Official AWS/Azure/GCP/OCI lists | None in Niger. | A negative check. | Record as absence of public region/local zone; ignore partner/customer claims as facility evidence. |

## 7. Per-Division Industry Status

| Division | Industry status | Search posture |
|---|---|---|
| Niamey | Primary market. Government national DC/DTS program and Ministry of Finance internal DC lead; telco cores likely but unpublished as facilities. | Exhaustive operator, procurement, power and press searches. |
| Agadez | No datacenter facility found; mining/security/fibre-corridor context only. | Negative sweep; filter out towers and mine IT rooms. |
| Diffa | No datacenter facility found; security-affected and Chad-route context. | Negative sweep; require official source. |
| Dosso | No datacenter facility found; Benin/Cotonou terrestrial-route context. | Negative sweep and customs/border fibre searches. |
| Maradi | No datacenter facility found; Nigeria corridor and telecom-site expansion context. | Negative sweep; avoid Nigeria false positives. |
| Tahoua | No datacenter facility found. | Negative sweep with power/fibre terms. |
| Tillabéri | No datacenter facility found; border/security corridor. | Negative sweep; require strong evidence. |
| Zinder | No datacenter facility found; possible legacy telecom/bank/university server-room leads. | Search, but only count named hosting/colo/cloud facility proof. |

## 8. Update / Re-check Cadence

- **Monthly:** ANP, Le Sahel, MCNTI, Agence Ecofin, marchespublics.ne, ARCEP, AfDB project P-Z1-GB0-024.
- **Quarterly:** DCD, Developing Telecoms, Connecting Africa, Telecom Review Africa, TechAfrica News, WeAreTech, ActuNiger, Journal du Niger, Echos du Niger, PCH, PeeringDB, DataCenterMap, Baxtel, Inflect, DataCenterPlatform.
- **Semi-annual:** Uptime Institute, hyperscaler region lists, submarine-cable maps, operator product pages for Niger Telecoms/Zamani/Airtel/Moov/AFR-IX.
- **Event-driven:** national data-center commissioning, an AfDB procurement/acceptance update, Zamani/Niger Telecoms merger completion, ARCEP licence changes, AES digital-infrastructure announcements, major grid/substation announcements in Niamey.

## 9. Pitfalls

- Do not promote directories or reseller pages above C without a named physical facility and corroboration.
- Do not count telco exchanges, NOCs, towers, fibre shelters, cybercafes, digital hubs, university labs, bank DR rooms, ministry server rooms or ordinary VPS offers unless the source proves hosting/colo/cloud/compute facility function.
- Do not treat "Tier III" as certified unless Uptime or an equivalent certifier names the facility.
- Do not infer Niger facilities from Nigeria results, especially Lagos/Abuja/Kano pages.
- Assign records by physical site. National articles mentioning all regions do not create regional facility records.
