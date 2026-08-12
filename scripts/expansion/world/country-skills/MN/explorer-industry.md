# MN Explorer - Industry, Vendor, Cloud, and Province Query Patterns

Date: 2026-08-12. Scope: Mongolia datacenter enumeration from colocation and telecom operators, bank/government/private enterprise facilities, cloud and CDN region signals, trade press, local-language search, and province/capital-city query patterns. Reliability grades: **A** = primary/operator/government/certification/cloud-provider source; **B** = established trade press, local business press, contractor case study, or strong directory with corroboration; **C** = weak directory, social post, lead-generation article, or unverified repost.

---

## 0. Mongolia-specific search model

Mongolia has a small datacenter market. Enumeration should start with **Ulaanbaatar** and then check **Darkhan-Uul** and **Tov** for the two non-capital patterns visible in public sources: Mobinet's geographic-redundancy site in Darkhan and Hunnu City / New Zuunmod investment promotion near the new airport in Tov aimag. Most other aimags are negative-search exercises unless local government, telecom, mining, border-logistics, or renewable-energy press names a new facility.

Use Mongolian and English in every pass. Russian spellings help occasionally because Mongolian ICT pages and older regional directories may use `дата-центр`, but Mongolian Cyrillic is the main local-language path.

Core terms:

```text
data center
datacenter
data centre
colocation
colo
server hosting
cloud service
cloud region
edge data center
internet data center
disaster recovery data center
geographically redundant data center
green data center
renewable powered data center
AI data center
server farm

дата төв
датацентер
дата центр
мэдээлэл боловсруулах төв
мэдээллийн төв
сервер байршуулах
зогсуур түрээс
виртуал сервер
веб хостинг
үүлэн тооцоолол
нөөц дата төв
газарзүйн нөөц дата төв
ногоон дата төв
хиймэл оюун ухаан дата төв
```

Status and capacity terms:

```text
ашиглалтад орсон
ашиглалтад орууллаа
нээгдлээ
байгуулав
барьсан
барих
бүтээн байгуулалт
төсөл
хөрөнгө оруулалт
санамж бичиг
хамтран ажиллах
Tier II
Tier III
TIA-942
Uptime Institute
ISO 27001
ISO 9001
рак
rack
кВт
МВт
MW
PUE
2N
N+1
free-cooling
гал унтраах
дизель генератор
дэд станц
```

Common false positives:

- **Inner Mongolia is China, not Mongolia.** Always exclude `Inner Mongolia`, `Hohhot`, `Ulanqab`, `Horinger`, `Baotou`, and Chinese `内蒙古` results when enumerating country code `MN`.
- **Government digital systems are not always physical data centers.** `E-Mongolia`, `ХУР`, `ДАН`, registry systems, and `Smart Government` procurement are often software/platform workloads hosted by the National Data Center.
- **Bank private data centers are real facilities but not commercial colo.** Uptime Institute lists several bank facilities in Ulaanbaatar; include them if the target database covers enterprise/private data centers, but keep them separate from commercial colocation supply.
- **"Cloud" can mean VPS hosting.** Local operators use cloud/virtual-server marketing for services inside their own data centers. Do not infer a public hyperscale cloud region unless the cloud provider's official region page lists Mongolia.
- **Smart-city and sovereign-wealth-fund announcements are leads.** Hunnu City data-center references should remain `planned` or `announced` until there is land allocation, permit, grid connection, construction, operator, or commissioning evidence.

---

## 1. High-signal sources

| Source | URL / query route | Use | Grade |
|---|---|---|---|
| National Data Center of Mongolia | `https://datacenter.gov.mn/`, `https://datacenter.gov.mn/about-us`, `https://datacenter.gov.mn/contact` | Primary source for the government NDC, services, legal basis, address in Songinokhairkhan district, government cloud, hosting, rack rental, and NDC news. | A |
| LegalInfo.mn | `https://legalinfo.mn/mn/detail?lawId=14146`, `site:legalinfo.mn "Үндэсний дата төв"` | Government resolutions establishing the NDC and mandating government database hosting; useful for official status and public-sector scope. | A |
| Uptime Institute Mongolia awards | `https://uptimeinstitute.com/uptime-institute-awards/country/id/MN` | Best source for certified non-public facilities: Bank of Mongolia NETC, Khan Bank Primary, Khan Bank Seoul, Khan Bank Technical Center-1, XacBank. | A |
| Mobinet / MobiCom official service pages | `https://mobinet.mn/datacenter`, `https://mobinet.mn/service/47`, `https://support.mobicom.mn/115303` | Primary source for Mobinet/MobiCom data-center services, Ulaanbaatar and Darkhan availability, Tier II/Tier III claims, 2N/N+1/free-cooling features. | A |
| Unitel data-center service | `https://www.unitel.mn/business/product/13` | Primary local provider page for Unitel data-center/colocation service; use with directories/trade press for address and facility detail. | A- |
| S Systems / Shunkhlai Holding | `https://www.sg.mn/en/business-sector/technology/0/`, `https://www.ssystems.mn/` | Primary source for S Systems Data Center, launched by Shunkhlai Holding in 2022 and marketed as Mongolia's largest data center. | A |
| Mogul Data Center | `https://moguldc.mn/` | Primary site for Mogul Service/Mogul Data Center; page text may be sparse, so corroborate with directories and partner pages. | A-/B |
| Haskoning ICT Group case study | `https://www.haskoning.com/en/projects/new-certified-tier-iii-data-centre-aims-to-be-the-best-in-mongolia` | Strong contractor evidence for ICT Group JSC's 2022 Tier III-standard data-center project and its prior two data centers. Verify current operating status separately. | B+ |
| Data Center Dynamics Mongolia tag | `https://www.datacenterdynamics.com/en/news/?tag=mongolia` | Best international trade press for Mongolia market context, Hunnu City/sovereign wealth fund data-center promotion, and operator universe. | B |
| Data Center Knowledge archive | `https://www.datacenterknowledge.com/business/mongolia-wants-data-centers` | Older but useful source for KT Corporation's government Internet data-center project leading to the NDC. | B |
| The Tech Capital | `https://thetechcapital.com/mongolia-lines-up-renewables-powered-data-centres-under-new-sovereign-fund` | Secondary source for Hunnu City / Chinggis Khaan Sovereign Wealth Fund renewables-powered DC ambition. | B |
| World Bank / KGGTF Green Data Center Strategy | `https://www.wbgkggtf.org/node/3293` | Policy context for government green-data-center strategy and private-sector incentives; not facility-level proof. | B |
| Cloudflare Ulaanbaatar blog | `https://blog.cloudflare.com/mongolia/` | Primary CDN/edge evidence: Cloudflare says it deployed a data center in Ulaanbaatar in 2018, but physical host and capacity are undisclosed. | A for edge presence; C for host inference |
| DataCenterMap / Baxtel / Datacenters.com / RackCorp / ColocationM | site-scoped searches | Lead discovery for addresses and smaller providers: S Systems, Mogul, Unitel, Mobinet/MobiCom, Gemnet. Always corroborate. | C, sometimes B with operator/press support |
| Mongolian local press: iKon.mn, GoGo.mn, Montsame, News.mn | site-scoped searches | Useful for Mobinet launches, government digital infrastructure, and investment promotion. Prefer exact Mongolian terms. | B/C depending on article specificity |
| Public procurement | `https://www.tender.gov.mn/`, `https://opendata.tender.gov.mn/` | Search tenders for NDC upgrades, provincial server rooms, disaster recovery, UPS/generator/cooling procurement. Good for government facilities but can overcount IT rooms. | A for tender/award; C for facility classification |
| Communications Regulatory Commission | `https://crc.gov.mn/`, `https://admin.crc.gov.mn/` | Telecom/license context for providers; no complete DC registry found. Search operator license pages and equipment-certification notices. | A for license context |

Useful source-scoped queries:

```text
site:datacenter.gov.mn "дата төв" "Tier"
site:legalinfo.mn "Үндэсний дата төв"
site:uptimeinstitute.com/uptime-institute-awards/country/id/MN "Ulaanbaatar"
site:mobinet.mn "дата төв" "Дархан" OR "Улаанбаатар"
site:mobicom.mn "дата төв" "Tier III"
site:unitel.mn "Дата төв" "сервер"
site:sg.mn "S Systems" "data center"
site:haskoning.com Mongolia "data centre" "ICT Group"
site:datacenterdynamics.com Mongolia "data center"
site:ikon.mn "дата төв" "Мобинет" OR "Дархан"
site:montsame.mn "дата төв" "Хүннү" OR "ногоон"
site:tender.gov.mn "дата төв" OR "серверийн өрөө"
site:opendata.tender.gov.mn "дата төв"
```

---

## 2. Operator and project seed list

Operator pages are A for the provider's claimed service presence. Facility count, capacity, exact address, and Tier status need separate evidence unless the official source states them clearly.

| Operator / project | Primary URLs / evidence route | Search pivots | Notes |
|---|---|---|---|
| National Data Center of Mongolia / `Үндэсний Дата Төв` | `https://datacenter.gov.mn/`, `https://datacenter.gov.mn/about-us`, `https://datacenter.gov.mn/contact`, LegalInfo establishment resolution | `Үндэсний Дата Төв`, `National Data Center Mongolia`, `NDC Mongolia`, `Сонгинохайрхан 34 дата төв` | Government facility in Ulaanbaatar. Track separately from commercial colo; services include gov.mn domain, hosting, virtual server, rack rental, and government cloud/system operations. |
| Mobinet / MobiCom / Newcom Group | `https://mobinet.mn/datacenter`, `https://mobinet.mn/service/47`, `https://support.mobicom.mn/115303`, `https://ikon.mn/n/1s54` | `Мобинет дата төв`, `Мобиком дата төв`, `Mobicom data center Mongolia`, `Mobinet Darkhan`, `газарзүйн нөөц дата төв` | Key commercial seed. Official support page says service is available from Ulaanbaatar and Darkhan data centers; local press says Mobinet had three own data centers and built bank DC projects. |
| Unitel Group | `https://www.unitel.mn/business/product/13`, DataCenterMap Unitel Ulaanbaatar, DCD Mongolia article | `Unitel Data Center`, `Юнител дата төв`, `Unitel colocation Ulaanbaatar`, `Viva City data center Unitel` | Commercial telco colo/VPS lead in Ulaanbaatar. Use official service page for existence, directories for address. |
| S Systems LLC / Shunkhlai Holding | `https://www.sg.mn/en/business-sector/technology/0/`, `https://www.ssystems.mn/`, Baxtel/DataCenterMap | `S Systems Data Center`, `S-Systems Ulaanbaatar`, `Shunkhlai data center`, `Си Системс дата төв` | Shunkhlai official page says project launched in 2022 to build Mongolia's largest data center. Directories give 1,600 sqm / Ulaanbaatar leads; verify specs. |
| Mogul Service LLC / Mogul Data Center | `https://moguldc.mn/`, DataCenterMap, Baxtel, RackCorp | `Mogul Data Center`, `MogulDC`, `Могул дата төв`, `Mogul Service colocation` | Ulaanbaatar commercial colocation lead. Directories report 2021/2022 opening and Tier 3-compliant positioning, but capacity/Tier should be C unless official documentation appears. |
| Gemnet | RackCorp Mongolia pages, provider pages if found | `Gemnet data center`, `Gemnet DC Ulaanbaatar`, `Жемнет дата төв`, `Gemnet colocation` | Network/backbone/colo lead in Ulaanbaatar. Treat as C until direct operator page or PeeringDB evidence confirms address/facility. |
| ICT Group JSC | Haskoning case study, DCD Mongolia article, local ICT Group pages/jobs | `ICT Group Mongolia data center`, `ICT Group JSC дата төв`, `Ай Си Ти Групп дата төв`, `Haskoning ICT Group Mongolia Tier III` | Contractor page says ICT Group was opening a Tier III-standard facility in 2022 and already operated two data centers. Current operator, city, and facility name require verification. |
| Bank of Mongolia / NETC | `https://www.mongolbank.mn/en/r/5188`, Uptime Institute Mongolia awards | `Bank of Mongolia NETC data center`, `National Electronic Transaction Center data center`, `Монголбанк дата төв` | Certified financial-sector facility in Ulaanbaatar. Include if enterprise/private DCs are in scope; not commercial colo. |
| Khan Bank | Uptime Institute Mongolia awards | `Khan Bank Primary Data Center`, `Khan Bank Seoul Data Center`, `Khan Bank Technical Center-1`, `Хаан банк дата төв` | Multiple certified facilities in Ulaanbaatar, including Tier III Technical Center-1. Private bank infrastructure. |
| XacBank | Uptime Institute Mongolia awards | `XacBank Data Center`, `ХасБанк дата төв`, `XacBank Uptime Institute` | Certified private bank data center in Ulaanbaatar. |
| Cloudflare edge | `https://blog.cloudflare.com/mongolia/` | `Cloudflare Ulaanbaatar data center`, `Cloudflare Mongolia data center`, `Cloudflare UB POP` | Edge/PoP evidence only. Record Cloudflare as tenant/edge deployment, not as owning a standalone commercial DC unless host is disclosed. |
| Hunnu City / New Zuunmod data-center development | DCD Mongolia 2025 article, The Tech Capital 2025 article, Hunnu/New Zuunmod master-plan sources | `Hunnu City data center`, `Хүннү хот дата төв`, `New Zuunmod data center`, `Sergelen Altanbulag data center`, `Chinggis Khaan Sovereign Wealth Fund data center` | Planned investment lead in Tov aimag south of Ulaanbaatar. Keep `planned/announced` until facility developer, power, land/permit, construction, or MW evidence appears. |

---

## 3. Cloud and network-region checks

Cloud-provider location pages are A for cloud service availability and C for physical-site inference. Mongolia has CDN/edge presence and local VPS/cloud services, but no official AWS/Azure/GCP/OCI public cloud region found in the official lists reviewed for this methodology date.

| Provider | Official source | Mongolia signal |
|---|---|---|
| AWS | `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/`, `https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/` | No Mongolia public region or Local Zone identified on official AWS infrastructure pages. Search Direct Connect separately, but treat any partner/on-ramp as network evidence only. |
| Microsoft Azure | `https://learn.microsoft.com/en-us/azure/reliability/regions-list`, `https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies` | No Mongolia Azure public region on official region list. |
| Google Cloud | `https://cloud.google.com/about/locations` | No Mongolia Google Cloud region in official locations. Do not confuse China Inner Mongolia/Hohhot references with Mongolia. |
| Oracle Cloud | `https://www.oracle.com/cloud/public-cloud-regions/`, `https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm` | No Mongolia OCI public region on official region pages. |
| Yandex Cloud | `https://yandex.cloud/en/docs/overview/concepts/region` | No Mongolia region found in official Yandex Cloud region documentation. |
| Cloudflare | `https://blog.cloudflare.com/mongolia/`, Cloudflare network pages | Official 2018 Ulaanbaatar data-center/edge deployment. Host facility undisclosed. |
| Akamai / Google Global Cache / Meta / Netflix / Apple / Alibaba/Tencent peers | provider network maps, PeeringDB, Mobinet press | Use only as interconnection/CDN lead. Mobinet local press mentions direct/peering connectivity to major networks; do not count peer caches as standalone DCs. |

Cloud pivot queries:

```text
"AWS" "Mongolia" "data center" OR "Direct Connect" OR "Local Zone"
"Azure" "Mongolia" "region" OR "ExpressRoute"
"Google Cloud" "Mongolia" "region" OR "data center"
"Oracle Cloud" "Mongolia" "region"
"Yandex Cloud" "Mongolia" "region"
"Cloudflare" "Ulaanbaatar" "data center"
site:peeringdb.com Mongolia Ulaanbaatar "Data Center"
site:peeringdb.com "Mobinet" OR "Mobicom" OR "Unitel" OR "Gemnet"
```

---

## 4. Province/capital-city enumeration approach

For each division, search the English name, common alternate romanizations, Mongolian Cyrillic, and capital/sum names. Use `дата төв`, `сервер байршуулах`, `үүлэн тооцоолол`, `нөөц дата төв`, `Tier`, `МВт`, and operator names. For most aimags, the expected result is `no_projects` unless a specific government/procurement, telco, mining, or renewable-energy project appears.

Baseline template:

```text
"{division}" "data center" Mongolia
"{division}" "datacenter" OR "colocation" OR "server farm"
"{division}" "cloud" "Mongolia" "MW" OR "Tier"
"{division_cyrillic}" "дата төв"
"{division_cyrillic}" "сервер байршуулах"
"{division_cyrillic}" "нөөц дата төв"
"{division_cyrillic}" "үүлэн тооцоолол" "төсөл"
site:{province_gov_domain_if_known} "дата төв" OR "сервер"
site:tender.gov.mn "{division_cyrillic}" "дата төв"
site:tender.gov.mn "{division_cyrillic}" "серверийн өрөө"
```

| Division | Local anchors | Industry/vendor approach |
|---|---|---|
| Ulaanbaatar | `Улаанбаатар`, `UB`, districts: `Songinokhairkhan`, `Bayanzurkh`, `Sukhbaatar`, `Khan-Uul`, `Баянгол` | Highest priority. Sweep all operator names: NDC, Mobinet/MobiCom, Unitel, S Systems, Mogul, Gemnet, ICT Group, Bank of Mongolia, Khan Bank, XacBank, Cloudflare. Also search by districts and addresses from directories/certifications. |
| Darhan uul | `Дархан-Уул`, `Darkhan`, `Дархан хот` | Priority non-capital. Search `Mobinet Darkhan`, `Мобинет Дархан дата төв`, `газарзүйн нөөц дата төв Дархан`, plus NDC disaster-recovery procurement. DataCenterMap and MobiCom support pages corroborate Ulaanbaatar/Darkhan service availability. |
| Tov | `Төв`, `Tuv`, `Төв аймаг`, `Sergelen`, `Сэргэлэн`, `Altanbulag`, `Алтанбулаг`, `Zuunmod`, `Зуунмод`, `New Zuunmod`, `Хүннү хот` | Priority planned-project search. Hunnu City/New Zuunmod near Chinggis Khaan airport is the key lead. Query sovereign wealth fund, geothermal, renewables, airport logistics, and smart city terms. Keep as planned unless construction/operator evidence appears. |
| Orhon | `Орхон`, `Erdenet`, `Эрдэнэт` | Search mining/Erdenet enterprise IT and telecom nodes: `Эрдэнэт дата төв`, `Орхон серверийн өрөө`, `Erdenet data center`. Likely no public commercial DC; watch industrial cloud/mining false positives. |
| Selenge | `Сэлэнгэ`, `Sukhbaatar city`, `Сүхбаатар хот`, `Altanbulag` | Border/logistics and rail/fiber corridor lead only. Query `Сэлэнгэ дата төв`, `Алтанбулаг дата төв`, but avoid confusion with Sukhbaatar aimag. |
| Dornogovi | `Дорноговь`, `Sainshand`, `Сайншанд`, `Zamiin-Uud`, `Замын-Үүд` | Border logistics and rail/energy corridor. Search `Замын-Үүд дата төв`, `Сайншанд дата төв`, `Dornogovi data center`, plus mining/renewable power terms. |
| Omnogovi | `Өмнөговь`, `Dalanzadgad`, `Даланзадгад`, `Tsogttsetsii`, `Tavan Tolgoi`, `Oyu Tolgoi` | High-power mining region. Query enterprise/mining private data rooms separately: `Оюу Толгой дата төв`, `Таван Толгой дата төв`, `Өмнөговь сервер`. Treat mine IT/server rooms as private enterprise, not colo. |
| Dornod | `Дорнод`, `Choibalsan`, `Чойбалсан` | Low expected yield. Search provincial e-government and energy projects: `Чойбалсан дата төв`, `Дорнод серверийн өрөө`. |
| Hentiy | `Хэнтий`, `Chinggis`, `Чингис хот`, `Undurkhaan`, `Өндөрхаан` | Low expected yield. Search government procurement and telecom: `Хэнтий дата төв`, `Чингис хот сервер`. |
| Suhbaatar | `Сүхбаатар аймаг`, `Baruun-Urt`, `Баруун-Урт` | Low expected yield. Always include `аймаг` to avoid Ulaanbaatar Sukhbaatar district and Selenge Sukhbaatar city. |
| Hovd | `Ховд`, `Khovd city`, `Жаргалант` | Western regional hub. Search `Ховд дата төв`, `Khovd colocation`, university/government server-room tenders, and telecom PoPs. |
| Bayan-Olgiy | `Баян-Өлгий`, `Ölgii`, `Өлгий` | Low expected yield; search Kazakh/Mongolian variants if needed. Watch border/logistics or government server-room tenders. |
| Uvs | `Увс`, `Ulaangom`, `Улаангом` | Low expected yield. Query provincial government and telecom backup systems. |
| Hovsgol | `Хөвсгөл`, `Murun`, `Мөрөн` | Low expected yield. Search local e-government/procurement; do not count tourism web-hosting providers. |
| Dzavhan | `Завхан`, `Uliastai`, `Улиастай` | Low expected yield. Search `Завхан дата төв`, `Улиастай серверийн өрөө`. |
| Govi-Altay | `Говь-Алтай`, `Altai city`, `Алтай хот` | Low expected yield. Search government/telecom server procurement only. |
| Bayanhongor | `Баянхонгор`, `Bayankhongor` | Low expected yield. Include spelling variants: `Bayanhongor`, `Bayankhongor`, `Баянхонгор дата төв`. |
| Ovorhangay | `Өвөрхангай`, `Arvaikheer`, `Арвайхээр` | Low expected yield. Search provincial server-room tenders and e-government nodes. |
| Arhangay | `Архангай`, `Arkhangai`, `Tsetserleg`, `Цэцэрлэг` | Low expected yield; prior targeted searches found no verified projects. Use as negative-search documentation. |
| Bulgan | `Булган` | Low expected yield; ambiguity with `Bulgan` sums in other aimags. Combine with `аймаг` and `дата төв`. |
| Dundgovi | `Дундговь`, `Mandalgovi`, `Мандалговь` | Low expected yield. Search local government procurement and renewable-power claims only. |
| Govi-Sumber | `Говьсүмбэр`, `Govisumber`, `Choir`, `Чойр` | Low expected yield but rail/energy corridor. Search `Чойр дата төв`, `Говьсүмбэр сервер`. |

---

## 5. Verification and grading rules

1. **Separate facility class.** Use `commercial_colocation`, `government`, `bank_private`, `enterprise_private`, `cdn_edge`, `planned_smart_city`, or `procurement/server_room` in notes when possible.
2. **Do not double count tenants and hosts.** Cloudflare Ulaanbaatar is an edge deployment inside an undisclosed secure data center; count it as CDN/edge evidence unless the host facility is identified.
3. **Use Uptime as facility proof, not market proof.** Uptime Institute awards prove named facilities and certification level, especially for banks, but do not mean those facilities offer colocation.
4. **Treat Hunnu City conservatively.** DCD/The Tech Capital sovereign-fund stories are strong leads, but not enough for an operational or under-construction data center.
5. **Capacity hierarchy:** operator/owner official MW/rack/sqm disclosure > Uptime/certification docs > contractor case study > trade press > directories. Many Mongolian sources do not publish MW; leave `capacity_mw` null rather than inferring from floor area or rack count.
6. **Status hierarchy:** operator service page or certification/commissioning > local launch article > contractor case study > procurement award > MOU/investment promotion > directory-only.
7. **Province assignment:** assign by physical city/district. Ulaanbaatar district names matter for bank/NDC facilities; Hunnu/New Zuunmod should map to Tov if the source places it around Sergelen/Altanbulag/new airport rather than within Ulaanbaatar municipality.
8. **Negative results are useful.** For low-yield aimags, record the exact local-language search terms and date when no projects are found; Mongolia-wide industry evidence is heavily capital-centric.

Recommended evidence labels:

```text
operator official
government official
government legal act
Uptime certification
contractor case study
trade press
local press
directory only
CDN/edge tenant
planned/MOU only
server-room/procurement only
no verified project
```
