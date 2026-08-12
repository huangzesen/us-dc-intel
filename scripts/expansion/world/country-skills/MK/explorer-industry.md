# MK Explorer Industry - North Macedonia Datacenter Discovery via Operators, Trade Press, Aggregators, Cloud Signals, and Municipality Query Patterns

Date: 2026-08-12. Scope: North Macedonia (MK) datacenter enumeration from industry media, official/operator pages, investment-promotion channels, aggregators, interconnection records, cloud-provider checks, and local-language searches. Reliability grades: **A** = official/operator-owned or primary public-sector source, **B** = strong trade press, MIA/SeeNews/CORD/BalkanEngineer, interconnection record, vendor/project case study, or EU/IFI source, **C** = aggregator, social media, job ad, market snippet, inferred street-to-municipality mapping, or old/unverified directory record.

---

## 0. Industry discovery frame

- North Macedonia is a **small, Skopje-heavy colocation and telecom market** with several smaller official/operator-confirmed facilities and weak aggregator coverage. There are currently no official hyperscale cloud regions in the country in the checked AWS/Azure/GCP/OCI public lists.
- The 2026 legal shift is important for future pipeline discovery. Industry and legal press reported that amendments to the Law on Construction and Law on Urban Planning explicitly recognize data centers and centralize/clarify their construction path. Watch post-2026 trade press for first large foreign-investor or state-owned data-centre filings.
- Use industry sources to discover names, aliases, addresses, and status, then verify with operator pages, `gradezna-dozvola.mk`, municipal planning, AEK, public procurement, and EVN/MEPSO.
- Existing public leads cluster around **Skopje municipalities**: Aerodrom, Gazi Baba, Centar, Karpos; secondary leads include Veles, Stip, Makedonska Kamenica, Prilep, Kavadarci historical candidate, and Kriva Palanka/Deve Bair weak leads.
- Be strict about "Macedonia" ambiguity. Search results for "Macedonia data center" often refer to **Western Macedonia in Greece**, especially PPC's 300 MW former-coal-mine project. Do not assign Greek Western Macedonia facilities to North Macedonia.

---

## 1. Industry and trade-press sources

| Source | URL / query route | Use | Grade |
|---|---|---|---|
| MIA - Macedonian Information Agency | https://mia.mk/ | Primary local news wire for government statements. July 2026 article says new legislation filled a legal gap for data centers and the government is considering a state-owned data center. | B/A- for quoted government statements |
| SeeNews | https://seenews.com/ | Regional business press. Useful for regulatory shift, telecom market entrants, building-permit statistics, and investment leads. | B |
| CORD Magazine | https://cordmagazine.com/ | Regional business press; useful for legislative/data-centre investment summaries. | B/C |
| BalkanEngineer | https://balkanengineer.com/ | Engineering/construction press; useful for data-centre legal-change and construction-market leads. | B/C |
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/news/ | Good for Balkan telecom and hyperscale news, but North Macedonia coverage is thin; beware Greek Western Macedonia false positives. | B |
| Balkan Green Energy News | https://balkangreenenergynews.com/ | Energy-grid and renewable-power context for MEPSO/EVN/large-load feasibility. | B |
| ITU / Energy Community / EBRD / World Bank / EU documents | official institutional sites | Useful for regulator, broadband, energy, ICT, and government-datacenter context. | A/B |
| Local tech/business press | IT.mk, Faktor, Kapital, Meta, Sloboden Pecat, SDK, Plusinfo, local municipal news | Can surface operator launches, tenders, and government digitalization. Verify all facility claims. | B/C |

Trade queries:

```text
site:mia.mk "data centers" "North Macedonia"
site:mia.mk "дата центри"
site:seenews.com "North Macedonia" "data centres"
site:cordmagazine.com "North Macedonia" "data centre"
site:balkanengineer.com "North Macedonia" "data centers"
site:datacenterdynamics.com "North Macedonia" "data center"
site:datacenterdynamics.com "Macedonia" "data center" -"Western Macedonia"
site:balkangreenenergynews.com "North Macedonia" "MEPSO" "grid"
site:it.mk "дата центар" Македонија
site:faktor.mk "дата центар" Македонија
site:kapital.mk "дата центар" Македонија
```

Read press lifecycle verbs carefully:

- `plans`, `contemplating`, `preparing amendments`, `legal framework`, `suitable for investment` = policy/intent, not a facility.
- `tender`, `design`, `supervision`, `building permit`, `construction started` = pipeline; verify with procurement/permit.
- `opened`, `operational`, `offers colocation`, `hosts`, `built`, `address` = stronger facility signal; verify with operator or public record.

---

## 2. Operator and facility seed sweep

Operator pages are **A for their own marketed services**, but address, municipality, and capacity often come from aggregators and should be downgraded until primary-confirmed.

| Operator / project | Official / primary URL | Facility or locality signal | Notes |
|---|---|---|---|
| Interspace | https://interspace.com/en/data-center-colocation | Skopje data-center colocation; third-party records identify Pero Nakov and Jane Sandanski sites | Search both Interspace and `Интерспејс`; verify Aerodrom/Gazi Baba address with municipal records. |
| Telesmart Telekom | https://en.telesmart.mk/colocation/ | SET / Skopje Exchange Teleroom colocation and interconnection | Address appears as Bul. Kiro Gligorov 4 and/or Nikola Parapunov in third-party records; verify municipality before final assignment. |
| Neotel / neoDC / neoCloud | https://neodc.mk/ ; https://neocloud.mk/architecture/ ; https://neotel.com.mk/en/business-users/cloud-services/infrastructure-as-a-service/ | Skopje neoDC and Neotel/neoCloud architecture with Skopje/Stip data centers | Good official source for Neotel-owned cloud/data-centre platform. Capacity often third-party only. |
| Net.Bit | https://netbit.mk/ | Veles official datacenter; older Skopje listings also appear | Net.Bit site is strong for datacenter service and Veles contact/location. Confirm any Skopje listing separately. |
| Data Center DTS | https://www.datacenterdts.com/ | Makedonska Kamenica / independent datacenter service provider | Also search CompuNet Engineering project page for Macedonian `центар за податоци Data Center DTS`. |
| Government BCDR Data Centre | EU project records, IPA documents, 1X2STUDIO project page, EUMiesAwards profile | Prilep operational public-sector BCDR facility; Kavadarci was a candidate scenario | Treat Prilep as confirmed when supported by EU/project/design sources; Kavadarci as rejected/candidate unless new evidence. |
| A1 Makedonija | https://www.a1.mk/ | Internal Skopje telecom data-center lead from directories | Official facility-specific evidence is thin; use A1 as a telecom/core-network search term. |
| Makedonski Telekom | https://www.telekom.mk/ | Telecom cloud/network infrastructure, 5G/core sites | Do not count all telecom facilities. Search annual reports, enterprise cloud, AEK, procurement. |
| Akton Communications | https://www.akton.net/ or local Akton pages if found | Aggregators list SKP02/SKP03 in Skopje | Needs operator/AEK/permit confirmation; directory-only evidence is C. |
| Telekabel | https://telekabel.com.mk/ | Stip telecom operator; potential server/POP infrastructure | Use as a Stip telecom lead, not confirmed commercial DC unless facility evidence appears. |
| MARNET / academic networks | https://marnet.mk/ | Registry/network infrastructure; possible public-sector technical facilities | Count only if a physical data centre/server facility is identified. |

Operator queries:

```text
"Interspace" "Skopje" "data center"
"Интерспејс" "дата центар"
"Telesmart" "Skopje Exchange Teleroom"
"Telesmart" "Kiro Gligorov" OR "Nikola Parapunov"
"Neotel" "neoDC" "Skopje"
"Neotel" "Stip" "data center"
"neoCloud" "two data centers" "Skopje" "Stip"
"Net.Bit" "Datacentar" "Veles"
"Data Center DTS" "Makedonska Kamenica"
"центар за податоци" "Data Center DTS"
"A1 Macedonia" "internal data center"
"Makedonski Telekom" "data center" "North Macedonia"
"Akton Communications" "SKP02" OR "SKP03"
"Telekabel" "серверска сала" OR "data center"
```

---

## 3. Aggregators, interconnection, and directories

Use aggregators for **lead discovery**, especially because North Macedonia operator pages often omit street address and MW. Never rely on an aggregator alone for A-grade status.

| Source | URL | Use | Grade |
|---|---|---|---|
| Data Center Map | https://www.datacentermap.com/macedonia/ | Lists Macedonia markets/facilities; useful for Skopje and Deve Bair leads and older address/capacity snippets. | C/B- when corroborated |
| Inflect | https://inflect.com/datacenters/emea/macedonia/skopje | Lists Skopje facilities including Akton, Interspace, Neotel, Telesmart. Useful for address aliases. | C/B- |
| Data Center Platform | https://datacenterplatform.com/countries/north-macedonia/ | Lists North Macedonia facilities/operators; useful for Telesmart/Interspace/Akton aliases. | C |
| Cloudscene | https://cloudscene.com/market/data-centers-in-macedonia/all | Market overview; useful for service-provider names and interconnection hints. | C |
| Datacenters.com | https://www.datacenters.com/ | May list A1 internal and provider profiles. | C |
| Data Center Catalog | https://datacentercatalog.com/macedonia-rep-of | Lead discovery only. | C |
| PeeringDB | https://www.peeringdb.com/ | Good for interconnection-active facilities such as Telesmart DC Skopje; verifies peering relevance, not construction permits. | B/C |
| Jobs/LinkedIn | LinkedIn data-center jobs in North Macedonia | Weak leads for location such as Deve Bair/Kriva Palanka; must be verified. | C |

Aggregator queries:

```text
site:datacentermap.com/macedonia "Skopje" "data center"
site:datacentermap.com/macedonia "Deve Bair"
site:inflect.com/datacenters/emea/macedonia/skopje
site:datacenterplatform.com "North Macedonia" "data centers"
site:cloudscene.com "Macedonia" "Telesmart"
site:datacenters.com "A1 Macedonia" "data center"
site:peeringdb.com "Telesmart DC Skopje"
"North Macedonia" "data center technician" "Deve Bair"
```

Aggregator handling rules:

- Keep capacity fields null unless the capacity is on an operator/spec page or a strong technical source; directory MW should be marked lower-confidence in notes.
- Reconcile address variants before assigning municipality. Skopje streets can cross or be ambiguously mapped across Aerodrom/Gazi Baba/Centar/Karpos.
- Treat `Macedonia` country pages with caution because some providers use older country names and some search engines mix in Greece.

---

## 4. Investment-promotion and policy channels

Sources:

- Invest North Macedonia data centers page: https://investnorthmacedonia.gov.mk/data-centers/. It says the country is positioning for hyperscale, colocation, and edge infrastructure. Grade **B for market positioning**, **C for facility enumeration** unless a named site is given.
- Invest North Macedonia energy page: https://investnorthmacedonia.gov.mk/invest-energy/. Useful for energy-system summary and MEPSO/EVN roles.
- MIA, SeeNews, CORD, BalkanEngineer legal-change reporting in 2026. Useful for the first wave of post-amendment project leads.

Queries:

```text
site:investnorthmacedonia.gov.mk "Data Centers & Digital Infrastructure"
site:investnorthmacedonia.gov.mk "data centers" "hyperscale"
site:investnorthmacedonia.gov.mk "energy" "MEPSO" "EVN"
"North Macedonia" "data center" "foreign investment"
"North Macedonia" "AI" "data center" "investment"
"North Macedonia" "state-owned data center"
"Северна Македонија" "дата центри" "инвестиции"
"државен дата центар" "Северна Македонија"
```

Use investment promotion to seed municipalities, TIDZ/industrial zones, and power queries. Do not create projects from opportunity language alone.

---

## 5. Cloud and CDN signals

Official public cloud checks should remain a negative-control step.

| Provider | Official source | MK result to check | Use |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No official MK region found in checked list. | Negative cloud-region check; only partner/edge leads if locally evidenced. |
| Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No official MK Azure region found in checked list. | Negative cloud-region check. |
| Google Cloud | https://cloud.google.com/about/locations ; https://datacenters.google/locations | No official MK cloud region or Google-owned data-center country site found. | Negative cloud-region check. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No official MK OCI public cloud region found. | Negative cloud-region check. |
| CDN/edge providers | Cloudflare, Akamai, Google Global Cache, Netflix OCA, ISP caches | May appear in Skopje operator facilities but rarely public. | Use as interconnection lead only; not standalone DC evidence. |

Cloud/edge queries:

```text
"Skopje" "AWS" "Local Zone"
"Skopje" "Azure" "edge" "data center"
"Skopje" "Google Global Cache"
"Skopje" "Cloudflare" "PeeringDB"
"North Macedonia" "cloud region" AWS OR Azure OR Google OR Oracle
"Macedonia" "sovereign cloud" "data center"
```

If a cloud provider later announces an MK region, use it as an **A-grade region signal** but still seek operator/permit/power evidence for physical facility enumeration.

---

## 6. Local-language search patterns

### 6.1 National sweep

```text
"дата центар" "Северна Македонија"
"дата центри" "Северна Македонија"
"центар за податоци" "Македонија"
"серверска сала" "Македонија"
"колокација" "Скопје"
"клауд" "дата центар" "Македонија"
"деловен континуитет" "дата центар"
"обнова од катастрофи" "дата центар"
"складирање и обработка на дигитални податоци"
"изградба на дата центар" "Македонија"
"дата центар" "Службен весник"
```

### 6.2 Operator + locality sweep

```text
"Интерспејс" "дата центар" "Скопје"
"Телесмарт" "колокација" "Скопје"
"Неотел" "дата центар" "Штип"
"неоДЦ" "Скопје"
"Нет.Бит" "датацентар" "Велес"
"Data Center DTS" "Македонска Каменица"
"А1 Македонија" "дата центар"
"Македонски Телеком" "серверска сала"
"Ак Тон" OR "Akton" "Скопје" "дата центар"
```

### 6.3 Permit/procurement/power sweep

```text
"{municipality}" "одобрение за градење" "дата центар"
"{municipality}" "градежна дозвола" "центар за податоци"
"{municipality}" "детален урбанистички план" "серверска сала"
"{municipality}" "јавна набавка" "серверска сала"
"{municipality}" "јавна набавка" "дата центар"
"{municipality}" "трафостаница" "дата центар"
"{operator}" "ЕВН" "приклучок"
"{operator}" "МЕПСО" "MW"
```

### 6.4 Albanian secondary sweep

Use primarily for Tetovo, Gostivar, Vrapciste, Bogovinje, Zelino, Saraj, Cair, Aracinovo, Lipkovo, and mixed-language Skopje-area records.

```text
"{municipality}" "qender te dhenash"
"{municipality}" "qendra e te dhenave"
"{municipality}" "dhoma e servereve"
"{municipality}" "leje ndertimi" "server"
"{municipality}" "plan urbanistik" "data"
```

---

## 7. Municipality-level industry strategy

### 7.1 Skopje metropolitan municipalities

Skopje is the first-pass market. Run operator, address, interconnection, and municipal-boundary checks before final assignment.

| Municipality | Industry/operator leads | Query additions |
|---|---|---|
| Aerodrom | Interspace DC MK-SK-1 / Jane Sandanski; Akton SKP03 / 23-ti Oktomvri | `Jane Sandanski`, `Јане Сандански`, `23-ti Oktomvri`, `23-ти Октомври`, `Aerodrom data center`, `Општина Аеродром дата центар`. |
| Gazi Baba | Interspace Pero Nakov; Telesmart Kiro Gligorov; Akton Belasitsa | `Pero Nakov`, `Перо Наков`, `Kiro Gligorov`, `Киро Глигоров`, `Belasitsa`, `Беласица`, industrial zone, EVN substation. |
| Centar | neoDC/Neotel Kuzman Josifovski Pitu; A1 internal lead | `Kuzman Josifovski Pitu`, `Кузман Јосифовски Питу`, `A1 Internal`, `Plostad Presveta Bogorodica`, `Плоштад Пресвета Богородица`. |
| Karpos | Telesmart Nikola Parapunov ambiguity | `Nikola Parapunov`, `Никола Парапунов`, `Karpos 4`, `Карпош 4`, PeeringDB Telesmart. |
| Butel, Gjorce Petrov, Kisela Voda, Cair, Saraj, Suto Orizari, Sopiste, Studenicani, Zelenikovo, Cucer-Sandevo, Aracinovo, Ilinden, Petrovec | No strong public commercial leads in checked results; possible telecom POPs, airport/industrial/logistics or future sites | Run universal terms plus A1/Telekom/Neotel/EVN/MEPSO, industrial-zone, airport, and public-procurement queries. |

Skopje templates:

```text
"Skopje" ("Interspace" OR Telesmart OR Neotel OR neoDC OR Akton OR A1) "data center"
"Скопје" ("Интерспејс" OR "Телесмарт" OR "Неотел") "дата центар"
"Skopje" "colocation" "Kiro Gligorov" OR "Pero Nakov" OR "Jane Sandanski"
"Скопје" "серверска сала" "јавна набавка"
site:peeringdb.com "Skopje" "data center"
```

### 7.2 Confirmed/strong secondary municipalities outside Skopje

| Municipality | Lead | Query notes |
|---|---|---|
| Veles | Net.Bit Datacentar Veles | Search `Net.Bit Datacentar`, `Нет.Бит`, `Nikola Orovcanec`, `Никола Оровчанец`, Veles permits/procurement. |
| Stip | Neotel/neoCloud Stip; Telekabel telecom context | Search `Neotel Stip data center`, `neoCloud Stip`, `Неотел Штип дата центар`, `Telekabel server room`. |
| Makedonska Kamenica | Data Center DTS | Search `Data Center DTS`, `Македонска Каменица центар за податоци`, `CompuNet Data Center DTS`. |
| Prilep | Government BCDR Data Centre | Search `Business Continuity and Disaster Recovery Data Centre Prilep`, `деловен континуитет Прилеп дата центар`, `Vasko Karangeleski`. |
| Kavadarci | Historical BCDR candidate/rejected scenario | Search only for updated procurement/permit; avoid counting the old candidate as active. |
| Kriva Palanka / Deve Bair | Weak DataCenterMap/job lead | Require primary evidence: operator page, AEK, permit, border/cadastral address, or power connection. |

Templates:

```text
"Veles" "Net.Bit" "datacenter"
"Велес" "Нет.Бит" "датацентар"
"Stip" "Neotel" "data center"
"Штип" "Неотел" "дата центар"
"Makedonska Kamenica" "Data Center DTS"
"Македонска Каменица" "центар за податоци"
"Prilep" "Business Continuity and Disaster Recovery Data Centre"
"Прилеп" "обнова од катастрофи" "дата центар"
"Kavadarci" "Business Continuity" "data centre"
"Deve Bair" "data center" "North Macedonia"
```

### 7.3 Industrial, border, and secondary city sweep

These municipalities have plausible infrastructure reasons but no strong checked lead: Kumanovo, Tetovo, Gostivar, Bitola, Ohrid, Struga, Gevgelija, Kicevo, Strumica, Prilep expansion, Ilinden, Petrovec, Kavadarci, Negotino, Veles expansion.

Use:

```text
"{municipality}" "industrial zone" "data center" "North Macedonia"
"{municipality}" "TIDZ" "data center"
"{municipality}" "free zone" "data center"
"{municipality}" "telecom" "colocation"
"{municipality}" "серверска сала"
"{municipality}" "технолошко индустриска развојна зона" "дата центар"
"{municipality}" "граничен премин" "data center"
"{municipality}" "EVN" "substation" "data center"
```

Treat results as leads unless a named facility/operator/project emerges.

### 7.4 Low-probability municipalities

For the remaining rural/small municipalities, run one official pass and one operator/aggregator pass. Most hits will be e-government systems, GIS/data portals, or server-equipment tenders. Store `no_projects` only after checking:

- English + Macedonian facility terms;
- municipal procurement and planning;
- known operators;
- DataCenterMap/Inflect/Data Center Platform/PeeringDB;
- TIDZ/industrial-zone and power/substation terms where present.

Do not spend equal effort across all 80 municipalities unless a lead appears. The practical high-yield order is Skopje municipalities -> Veles/Stip/Makedonska Kamenica/Prilep -> major regional cities/industrial municipalities -> rest.

---

## 8. Evidence handling and common false positives

- **Greek Western Macedonia false positive**: PPC's Western Macedonia 300 MW data-center project is in Greece, not North Macedonia.
- **Policy vs project**: `Invest North Macedonia` and 2026 legal-change articles are market/policy leads unless they name a parcel, investor, permit, procurement, or facility.
- **Telecom nodes**: AEK/operator telecom infrastructure, 5G, fibre, exchanges, and POPs are not data centres unless they provide compute/hosting/colocation/cloud/disaster-recovery function.
- **Server rooms**: public tenders for servers or a server room can be valid for government/internal data-centre inventory, but classify separately from commercial colocation and record the scope.
- **Capacity**: directory MW values for Interspace/Telesmart/Neotel should be marked lower-confidence unless corroborated by operator, permit, or power source.
- **Municipality assignment**: do not infer Skopje sub-municipality solely from "Skopje 1000"; use street, cadastral, municipal permit, or reliable map evidence.
- **Cloud region**: absence from official AWS/Azure/GCP/OCI lists means no official MK public region; local cloud products usually run on operator-owned infrastructure or foreign regions.

Minimum record standard for an A/B facility entry:

```text
name:
operator/developer:
municipality:
address_or_parcel:
status:
source_urls:
source_grade:
evidence_date:
why_this_is_a_data_center:
what_is_not_confirmed: capacity, permit, power, exact municipality, tenant, etc.
```

