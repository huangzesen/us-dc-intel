# AD Explorer Industry - Andorra Datacenter Discovery

Date: 2026-08-12. Country: **AD Andorra**. Division model: **7 parishes** per `world-manifest.jsonl`: Canillo, Encamp, La Massana, Ordino, Sant Julia de Loria, Andorra la Vella, Escaldes-Engordany. Companion file: `explorer-official.md` covers official, permitting, energy, and telecom methodology. This file covers industry discovery: operator/facility sweeps, local press, trade press, aggregators, interconnection directories, hosting firms, investment-promotion channels, cloud signals, and parish-by-parish search tactics.

Reliability grades: **A** = primary/operator/official proof; **B** = strong press, vendor, or interconnection evidence; **C** = weak lead or aggregator/marketplace claim; **U** = unverified rumour.

---

## 0. Industry Discovery Frame

- Andorra is a micro-market: about 87,000 residents, one state-owned telecom operator, one state utility, limited industrial land, and few local IT providers. Expected yield is low and confirmation quality matters more than volume.
- The **only A-grade marketed data-centre facility currently verified from an operator page** is Andorra Telecom's Data Centre for businesses in **La Massana**: https://www.andorratelecom.ad/en/business/data-center-new-abc/.
- Andorra Telecom's CEO stated in a 2026-08-05 all-andorra.com interview that the operator has three data centres: **La Massana, La Comella, and Santa Coloma**. Use this as **B-grade** evidence for the three-site claim. Use aggregators only to generate address/name leads.
- Live narratives to monitor:
  - **Domestic data-centre capacity**: Andorra Telecom's three facilities and any expansion for AI, public services, 5G core, or enterprise hosting.
  - **Energy-constrained investor interest**: FEDA/Endesa 2037 supply-agreement reporting discussed a possible Andorra data center, but there is no site or approved project.
  - **Sovereign cloud without local hyperscale**: official Google Cloud and AWS agreements, Andorra Digital homologated services, and encryption/key-control models may drive demand without creating a physical cloud region.
- No parish today has a verified non-Andorra-Telecom commercial colocation data centre. Private banks, hospitals, government, ski operators, and IT firms may have server rooms or DR rooms; keep those at **C** unless public evidence names a facility.

---

## 1. Local Press, Trade Press, and Market Sources

| Source | URL | Language | Use | Grade |
|---|---|---|---|---|
| El Periodic d'Andorra | https://www.elperiodic.ad/ | Catalan | Business/tech reporting, Aitek and energy/DC follow-ups. | B |
| L'Altaveu | https://www.altaveu.com/ | Catalan | National, energy, telecom, outage and policy reporting. | B |
| BonDia | https://www.bondia.ad/ | Catalan | Daily business/tech briefs. | B |
| Diari d'Andorra | https://www.diariandorra.ad/ | Catalan | Telecom, government, business updates. | B |
| Cadena SER Principat d'Andorra | https://cadenaser.com/radio-ser-principat-d-andorra/ | Catalan/Spanish | FEDA/Endesa data-centre discussion source. | B |
| Andorra Difusio / RTVA | https://www.rtva.ad/ | Catalan | Public broadcaster; energy, infrastructure, technology. | B |
| VilaWeb Andorra | https://www.vilaweb.cat/categoria/pais/andorra/ | Catalan | Regional coverage; useful cross-check for cloud agreements. | B |
| all-andorra.com | https://all-andorra.com/ | EN/CA/FR | Named-executive interviews and company profiles. | B |
| Andorra Insiders | https://andorrainsiders.com/ | EN/CA | Expat/business explainers; use cautiously for cloud/data residency. | C |
| DatacenterDynamics | https://www.datacenterdynamics.com/ | English | Global data-centre trade press; likely sparse for Andorra. | B when relevant |
| Capacity Media | https://www.capacitymedia.com/ | English | Connectivity and edge market coverage. | B when relevant |

Usable search templates:

```text
site:elperiodic.ad "centre de dades" Andorra
site:altaveu.com "data center" Andorra
site:bondia.ad "centre de processament de dades"
site:diariandorra.ad "Andorra Telecom" "centre de dades"
site:cadenaser.com/andorra FEDA Endesa "data center"
site:rtva.ad "centre de dades"
site:all-andorra.com "Andorra Telecom" "data centres"
site:all-andorra.com "Aitek Souverain Cloud"
```

---

## 2. Operator, Hosting, and Facility Sweep

| Company / institution | What to look for | Best verification route | Seed grade |
|---|---|---|---|
| Andorra Telecom | La Massana Data Centre, La Comella, Santa Coloma/Nexus, NODE/Annexus CPD, 5G core, cloud/colocation products. | Operator pages first; BOPA/Govern/Comu for works; CEO interview for three-site statement; CATNIX for connectivity. | A/B |
| Diquital | Cybersecurity subsidiary/managed security services, not a DC by default. | Andorra Telecom/Govern press; service pages. | C unless facility evidence appears |
| Tecnoland / Xarxa Soft ecosystem | "DataCenter Andorra" marketed services, remote desktop/server hosting. | https://tecnoland.ad/datacenter-andorra-centre-de-dades/ - verify physical parish, ASN, and whether it uses Andorra Telecom or foreign hosting. | B/C |
| Aitek Souverain Cloud | Andorra-domiciled sovereign-cloud positioning, GITEX Africa 2026 reporting. | Local press, all-andorra.com, registry/NRT, company pages; do not confuse with unrelated `aitek.fr`. | B for company/service, U for facility |
| Banks: MoraBanc, Andbank, Creand, BancSabadell d'Andorra | Internal CPD/DR, outsourcing, cloud-risk statements. | Annual reports, regulator notices, BOPA procurement if public, building permits. | C |
| CASS, SAAS/Hospital, UdA, schools | Public/institutional server rooms and DR services. | BOPA procurement, institutional annual reports, tender awards. | C |
| Grandvalira / Pal Arinsal / ski operators | Ticketing, snowmaking, operations server rooms. | Operator pages, tenders, vendor case studies. | C |
| Local IT/MSP firms: Intecom and similar | Hosting, backup, managed infrastructure claims. | Company pages, ASN/whois, BOPA awards, Comu licences. | C |

Sweep method: search `<company> "centre de dades"`, `<company> CPD`, `<company> "sala de servidors"`, `<company> cloud Andorra`, and `<company> hosting`. Do not count a company as a facility without a physical parish and source-backed operational status.

---

## 3. Aggregators, Interconnection Directories, and Marketplaces

| Source | URL | Use | Grade |
|---|---|---|---|
| Data Center Map - Andorra | https://www.datacentermap.com/andorra/ | Country facility seeds; currently Andorra Telecom-focused. | C |
| Data Center Map - Andorra Telecom | https://www.datacentermap.com/c/andorra-telecom/ | Names/addresses for La Comella, Nexus, La Massana; cross-check required. | C |
| Data Center Map - Andorra la Vella | https://www.datacentermap.com/andorra/andorra-la-vella/ | Capital-area seed list; beware duplication. | C |
| datacenters.com - Andorra Telecom provider | https://www.datacenters.com/providers/andorra-telecom | Provider/facility marketplace lead. | C |
| datacenters.com - La Comella | https://www.datacenters.com/andorra-telecom-de-la-comella | La Comella lead; not primary. | C |
| colocationm.com | https://colocationm.com/andorra/andorra-la-vella | Marketplace listings; likely office/HQ-address reuse. | C |
| PeeringDB - ANDORRA TELECOM SAU | https://www.peeringdb.com/org/18174 | ASN/interconnection and possible facility references. | B/C |
| RIPE Database | https://apps.db.ripe.net/db-web-ui/ | ASN, org, route, and contact records. | B |
| IXPDB | https://ixpdb.euro-ix.net/ | Check for domestic IXP absence/presence. | B |
| Internet Exchange Map | https://www.internetexchangemap.com/ | Regional IXP geography cross-check. | C |

Aggregator discipline: aggregators are discovery tools only. They may copy old names, duplicate the same operator site, reuse HQ addresses, or omit parish context. Do not lift capacity, tier, SLA, address, or status into the inventory above **C** unless an official/operator source confirms it.

---

## 4. Connectivity, Cable, and Edge Signals

- Andorra is landlocked; there are no submarine-cable landing stations. Connectivity depends on cross-border fibre toward Spain and France.
- CATNIX reported that Andorra Telecom upgraded its CATNIX connection from 10 Gbps to 20 Gbps over a 100 Gbps port: https://www.catnix.net/en/operadors-cat-and-andorra-telecom-upgrade-their-connection-to-catnix/. Use this as **B** evidence for international peering, not for a facility count.
- Common public IXP directories do not show an Andorran domestic IXP. Re-check IXPDB and PeeringDB quarterly.
- 5G core, emergency satellite features, and public cloud gateways may imply data-centre workloads, but they are not facilities unless a site is named.

Search templates:

```text
"Andorra Telecom" CATNIX 20 Gbps
"Andorra Telecom" PeeringDB facility
"Andorra Telecom" RIPE AS
"Andorra Telecom" "5G standalone" core
"Andorra Telecom" Nokia Ericsson core
"Andorra" "cross-border fibre"
"Andorra" "data center" connectivity
```

---

## 5. Investment, Cloud, and Economic-Development Channels

| Source | URL | Use | Grade |
|---|---|---|---|
| Andorra Business | https://www.andorrabusiness.com/ | Investment and TIC sector promotion; project leads. | A for own statements, B/C for promoted leads |
| Andorra Digital | https://andorra-digital.com/ | Cloud agreements, homologated cloud services, digital programmes. | A |
| Govern digital announcements | https://www.govern.ad/ | Official Google Cloud and AWS agreements, digital strategy, telecom policy. | A |
| Andorra Digital homologated cloud services | https://andorra-digital.com/serveis-homologats | Cloud providers/partners serving Andorra; check for local/foreign hosting. | A for catalogue |
| CCIS | https://www.ccis.ad/ | Chamber of commerce and business climate; possible TIC event leads. | B |
| GITEX Africa / Aitek reporting | https://all-andorra.com/andorra-enters-the-digital-map-with-aitek-sovereign-cloud-at-gitex-africa/ | Sovereign-cloud positioning lead; facility unproven. | B/C |

Search templates:

```text
site:andorrabusiness.com "data center"
site:andorrabusiness.com TIC cloud Andorra
site:andorra-digital.com "cloud sobira"
site:andorra-digital.com "serveis homologats" cloud
site:govern.ad "Google Cloud" Andorra
site:govern.ad "Amazon Web Services" Andorra
"Andorra" "punt de confianca digital"
"Andorra" "sovereign cloud" "data center"
```

Investment-promotion claims are not facility evidence. A real project should later appear in BOPA, Comu planning, FEDA grid planning, operator press, or a construction/procurement award.

---

## 6. Cloud and Local Hosting Checks

- Hyperscaler regions are **negative** for Andorra as of 2026-08-12. Check AWS, Azure, Google Cloud, and OCI official lists every run.
- Official cloud collaboration is **positive**: Google Cloud agreement on 2025-04-01 and AWS alliance on 2025-07-18. These are strategic/cloud-service signals, not local region proof.
- Andorra Telecom cloud/data-centre services are the strongest local commercial lead. Confirm whether a product is hosted in the La Massana DC, another Andorra Telecom site, or external partner cloud before assigning a facility.
- Local hosting queries should include `hosting Andorra`, `servidor dedicat Andorra`, `VPS Andorra`, `cloud Andorra empresa`, `allotjament web Andorra`, and `CPD Andorra`.
- Resellers often market "Andorra" for legal/tax/data-residency reasons while using French or Spanish infrastructure. Check ASN, IP geolocation, traceroute, whois, service terms, and support addresses before grading above **C**.

---

## 7. Catalan, Spanish, French, and English Query Templates

Run exact phrase and no-accent variants:

```text
"centre de dades" Andorra
"centre de processament de dades" Andorra
"centre de dades" "Andorra Telecom"
"centre de dades" "La Massana"
"centre de dades" "La Comella"
"centre de dades" "Santa Coloma"
"data center" Andorra inversio
"nuvol sobira" Andorra
"cloud sobira" Andorra
Andorra "centre de dades" MW
Andorra licitacio "centre de dades"
Andorra CPD servidors
"sala de servidors" Andorra
Andorra allotjament web empreses
Aitek Andorra cloud
Tecnoland Andorra "centre de dades"
FEDA "centre de dades"
```

Spanish:

```text
"centro de datos" Andorra
Andorra "nube soberana"
Endesa FEDA Andorra "centro de datos"
Andorra "licencia de obras" "centro de datos"
```

French:

```text
Andorre "centre de donnees"
Andorre "cloud souverain"
Andorre "salle de serveurs"
```

English:

```text
Andorra data center investment
Andorra colocation
Andorra sovereign cloud
Andorra Telecom data centre La Massana
```

---

## 8. Parish-Level Industry Strategy

### 8.1 Canillo

No confirmed DC. Likely only ski-resort and municipal server rooms. Search `Canillo centre de dades`, `Canillo CPD`, `Grandvalira Canillo servidors`, and Comu urbanism/activity records. **Expected yield: 0-1 C-grade server rooms.**

### 8.2 Encamp

No confirmed DC. Watch Pas de la Casa/connectivity and power-infrastructure references, but avoid confusing substations with data centres. Search `Encamp centre de dades`, `Encamp CPD`, `Pas de la Casa servidors`, `Encamp ETR`. **Expected yield: 0.**

### 8.3 La Massana

One A-grade operator facility: Andorra Telecom Data Centre in La Massana. Search `Andorra Telecom Data Centre La Massana`, `"La Massana" "centre de dades"`, `Comu La Massana llicencia activitat Andorra Telecom`, and Pal Arinsal IT/server-room leads. **Expected yield: 1 confirmed + 0-1 C-grade rooms.**

### 8.4 Ordino

No confirmed DC and limited industrial fit. Search `Ordino centre de dades`, `Ordino CPD`, and Comu urbanism records. **Expected yield: 0.**

### 8.5 Sant Julia de Loria

No confirmed DC. Watch-list because it is the southern border parish and may have comparatively plausible logistics/land for a future investor project. Search `"Sant Julia de Loria" "centre de dades"`, `Lauredia data center`, `Sant Julia CPD`, `Andorra Spain border data center`, and Comu planning. **Expected yield: 0-1 announced/lead only.**

### 8.6 Andorra la Vella

Core market. Leads: Andorra Telecom La Comella and Santa Coloma/Nexus, NODE/Annexus corporate CPD, government internal CPD, banks, local IT firms, and Tecnoland-type services. Search `"Andorra la Vella" "centre de dades"`, `"La Comella" "data center"`, `"Santa Coloma" "Andorra Telecom" "data center"`, `Annexus CPD`, `NODE Andorra Telecom CPD`, and Comu urbanism. **Expected yield: 2 B-grade operator sites plus several C-grade server-room leads.**

### 8.7 Escaldes-Engordany

No confirmed DC. Financial/professional office density means possible private server rooms or DR rooms. Search `Escaldes-Engordany centre de dades`, `Escaldes CPD`, bank back-office terms, and Comu activity licences. **Expected yield: 0-1 C-grade server rooms.**

---

## 9. Evidence Handling and False Positives

- **Tourism/noise filter:** Ignore results about ski event data, visitor centres, generic digitalisation, or statistics unless a physical IT facility is named.
- **Aggregator duplication:** Deduplicate Data Center Map/datacenters.com/colocationm listings against Andorra Telecom's three named sites and operator evidence.
- **The Cloud/NODE confusion:** Andorra Telecom's "The Cloud" / NODE real-estate project and storefront/corporate office news are not automatically data-centre evidence. Require CPD/data-centre wording or technical documentation.
- **Aitek collision:** Aitek Souverain Cloud in Andorra is distinct from unrelated Aitek entities in France/Africa. Verify legal identity before recording.
- **Reseller geo-claims:** VPS and hosting sellers may geolocate or brand services as Andorra while using infrastructure abroad. Confirm ASN and facility operator.
- **Intent is not a project:** FEDA/Endesa discussion, investor interest, or a 1 MW AI-DC concept should be recorded as dated leads only, with no facility count until a site appears.
- **Quarterly re-check:** local press, BOPA, Comu agendas/minutes, FEDA news, Andorra Telecom pages, PeeringDB, CATNIX, Andorra Digital, and cloud-provider official region lists.
