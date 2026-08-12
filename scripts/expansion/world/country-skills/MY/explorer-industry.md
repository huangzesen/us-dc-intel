# MY Explorer - Industry / Vendor / Trade-Press Discovery for Malaysia Datacenters

Date: 2026-08-12. Scope: Malaysia (MY) datacenter enumeration through Malaysian colo providers, hyperscaler and cloud-region pages, trade press, industry bodies, and state/federal-territory query patterns. Reliability grades: **A** = primary operator, government, regulator, utility, planning/EIA, exchange/annual-report, official cloud-region, or industrial-park source; **B** = established trade press or Malaysian business press with named project facts; **C** = directories, broker snippets, event pages, social posts, reposted MoUs, or unsourced market lists.

---

## 0. Malaysia-specific search model

Malaysia has no single public datacenter facility registry. Enumeration works by triangulating:

1. **Primary operator/vendor pages** for facility branding, campus names, marketed capacity, phase status, and exact district clues.
2. **MIDA, MDEC, Digital Investment Office (DIO), MITI / Ministry of Digital, state investment agencies, and industrial-park developers** for approved digital investments, incentives, Johor/Selangor policy, and site-development signals.
3. **Local planning, state planning guidelines, OSC 3.0 Plus / Johor Fast Lane, DOE/EIA, water, power, and utility sources** for large greenfield campuses where operator pages hide the exact parcel.
4. **DCD, W.Media, The Edge Malaysia, The Star, Bernama, New Straits Times, BusinessToday, Lowyat, SoyaCincau, and Digital News Asia** for live deal flow, land purchases, groundbreakings, customer/anchor tenant clues, and cloud-region launches.
5. **IXP and interconnect sources** such as MyIX, DE-CIX Malaysia/Kuala Lumpur, Penang IX, PeeringDB, Cloudscene, DataCenterMap, Baxtel, and operator network pages for legacy carrier hotels and smaller colo sites.

The practical geography is concentrated:

- **Johor**: dominant hyperscale expansion zone. Search Kulai/Sedenak, Nusajaya Tech Park, Iskandar Puteri, Gelang Patah, Nusa Cemerlang Industrial Park, Kempas, Plentong, Skudai, Tanjung Kupang, Senai, Johor Bahru, YTL Green Data Center Park, Sedenak Tech Park (STeP), Kidex Sedenak, and Johor-Singapore Special Economic Zone.
- **Selangor / Greater Kuala Lumpur / Cyberjaya**: mature Klang Valley colo and cloud region hub. Search Cyberjaya, Shah Alam/Elmina Business Park, Subang, Petaling Jaya, Klang, Sepang, Puchong, Kajang, Bangi, Bukit Jalil, and Klang Valley Core Data Centre.
- **Wilayah Persekutuan Kuala Lumpur**: carrier hotels, AIMS/Menara AIMS, finance-sector colo, exchange/peering nodes, but many "Kuala Lumpur" announcements are physically in Cyberjaya, Selangor.
- **Pulau Pinang and Kedah**: edge/enterprise colo, semiconductor and industrial demand, Open DC sites, Penang IX, Kulim Hi-Tech Park and Kedah Digital-type leads.
- **Sarawak and Sabah**: state digital-economy, hydro/renewable, government cloud/edge, IX/cable landing, and Kuching/Kota Kinabalu enterprise sites; expect smaller and more government/telco-led records.
- **Melaka, Perak, Negeri Sembilan, Pahang, Terengganu, Kelantan, Perlis, Labuan, Putrajaya**: mostly government, telco, disaster-recovery, industrial park, or speculative pipeline unless a named operator/project emerges.

Always resolve "Kuala Lumpur" and "Johor Bahru" marketing labels to the physical state/district. Cyberjaya is in **Selangor**, not Kuala Lumpur; Nusajaya/Iskandar Puteri/Kulai/Sedenak/Gelang Patah are **Johor**.

## 1. Malay and English query vocabulary

English terms:

```text
data center
data centre
datacenter
colocation
colo
hyperscale
AI data center
AI-ready data centre
cloud region
availability zone
internet data centre
IDC
carrier hotel
interconnection
edge data centre
disaster recovery centre
green data centre
renewable energy data centre
sovereign cloud
data hosting
```

Malay terms and local variants:

```text
pusat data
pusat data raya
pusat data hijau
pusat data AI
pusat data awan
pusat data berskala besar
pusat data hiperskala
pusat kolokasi
pusat pemprosesan data
pusat pemulihan bencana
perkhidmatan awan
pelayan
ladang pelayan
infrastruktur digital
pelaburan digital
kelulusan
permohonan kebenaran merancang
kebenaran merancang
pelan bangunan
kerja tanah
OSC 3.0 Plus
Johor Fast Lane
Penilaian Kesan Alam Sekitar
EIA
bekalan elektrik
pencawang
MVA
MW
bekalan air
air terawat
air kitar semula
industri teknologi
taman teknologi
kawasan perindustrian
```

Status/evidence words:

```text
announces
launches
opens
ready for service
commercial operation
operational
groundbreaking
breaks ground
topped out
land acquisition
acquires land
built-to-suit lease
anchor tenant
power secured
TNB
Tenaga Nasional
PPA
CRESS
Corporate Renewable Energy Supply Scheme
water supply
recycled water
planning approval
stop-work order
approved investment
Malaysia Digital status
Digital Investment Office
MIDA
MDEC
MITI
Ministry of Digital
```

National templates:

```text
"{operator}" Malaysia ("data center" OR "data centre" OR "pusat data") ("MW" OR "IT load" OR "critical IT load")
"{operator}" Malaysia ("Cyberjaya" OR "Johor" OR "Kulai" OR "Sedenak" OR "Nusajaya" OR "Iskandar Puteri")
"{state}" ("data center" OR "data centre" OR "pusat data") ("MIDA" OR "MDEC" OR "DIO" OR "Malaysia Digital")
"{state}" ("data center" OR "data centre" OR "pusat data") ("TNB" OR "pencawang" OR "MVA" OR "power")
"{state}" ("data center" OR "pusat data") ("OSC 3.0 Plus" OR "kebenaran merancang" OR "pelan bangunan")
"{industrial_park}" ("data center" OR "data centre" OR "pusat data" OR "hyperscale")
```

Malay templates:

```text
"{negeri}" ("pusat data" OR "pusat data raya" OR "pusat data AI") ("pelaburan" OR "diluluskan" OR "MIDA" OR "MDEC")
"{negeri}" ("pusat data" OR "data centre") ("kebenaran merancang" OR "OSC" OR "pelan bangunan")
"{negeri}" ("pusat data" OR "data centre") ("bekalan elektrik" OR "TNB" OR "pencawang" OR "MVA")
"{daerah/bandar}" ("pusat data" OR "data centre") ("dibina" OR "dilancarkan" OR "beroperasi" OR "pecah tanah")
"{taman perindustrian}" ("pusat data" OR "data centre") ("Kulai" OR "Cyberjaya" OR "Pulau Pinang")
```

Stage interpretation:

- `Malaysia Digital status`, `approved digital investment`, or MIDA/MDEC aggregate totals = **A for approval/investment context**, not facility proof unless project/entity/site is named.
- `MoU`, `strategic partnership`, `exploring`, `potential`, `expected to attract` = **C** until land, power, planning, construction, or operator page appears.
- `land acquisition`, `built-to-suit lease`, `industrial park tenant`, `power secured`, `water/recycled-water agreement` = **A-/B+** depending on source.
- `groundbreaking`, `construction`, `topped out`, `stop-work order` = strong site evidence; **A** if government/operator/official developer, **B** if trade press.
- `ready for service`, `commercial operation`, `launch`, `opens`, `go-live` = operational evidence; verify with operator page, cloud docs, IX/PeeringDB, or customer connectivity page.

## 2. Primary government, investment, planning, and utility sources

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Digital Investment Office (DIO) | `https://mydigitalinvestment.gov.my/`, `https://mydigitalinvestment.gov.my/data-centre-cloud` | Joint MIDA/MDEC platform for digital investments. Its Data Centre & Cloud page gives Malaysia-wide market counts and confirms DIO's Cloud & Data Centre focus. Good sector frame, not a facility registry. | A for policy/statistics, B for market snippets |
| MDEC releases | `https://www.mdec.my/media-release/` | Approved digital investments, Malaysia Digital status, Data Centre Task Force references, event leads. Example: 2024 digital investments release says data centres and cloud infrastructure were 76.8% of approved digital investments. | A for MDEC statements |
| MIDA releases/news | `https://www.mida.gov.my/` | High-signal investment approvals and operator announcements. Search Bridge MY06, YTL/Sea, Cyberjaya, Equinix, TM, Singtel/Nxera, power/energy context. | A when MIDA release, B when republished press |
| MITI / Ministry of Digital / Data Centre Task Force | MITI, `digital.gov.my`, MDEC/MIDA mirrored releases | National Data Centre Framework, MIDA as principal agency for new/expansion applications, sustainability and coordination policy. | A |
| PLANMalaysia / data centre planning guidelines | Search `GPP Pusat Data`, `Garis Panduan Perancangan Pusat Data`, `PLANMalaysia data centre planning guidelines` | Planning route and standardized siting considerations. Use to understand required local authority approvals; not usually facility-specific. | A |
| Johor State Data Centre Development Planning Guideline | `jpbd.johor.gov.my` PDF, query `GP-DATA-CENTRE-en.pdf` | Very important for Johor. It states applications must go to PBT through OSC 3.0 Plus or Johor Fast Lane and may be referred to the Johor State Data Centre Development Coordinating Committee. | A |
| Local authorities / OSC | `OSC 3.0 Plus`, PBT portals: MBJB, MPKu, MBIP, MBSJ, MBPJ, MPSepang, MBSA, etc. | Planning permission, earthworks, road/drainage, building plans, stop-work notices, meeting minutes. Search by project company and parcel/industrial park. | A if official record |
| Department of Environment / EIA | DOE portals and queries with `EIA`, `Penilaian Kesan Alam Sekitar`, `Environmental Impact Assessment`, project company | Environmental and water/cooling evidence for large campuses. Search exact SPV/operator names, district, and industrial park. | A |
| Tenaga Nasional Berhad (TNB), Energy Commission (Suruhanjaya Tenaga), SEDA, MyPower, CRESS | `tnb.com.my`, `st.gov.my`, `seda.gov.my`, company power/PPA releases | Power connection, substation, MVA/MW, renewable PPA, CRESS, green electricity tariff. Often decisive for hyperscale campus stage. | A/B |
| Water/state utilities | Ranhill SAJ/Johor water, Air Selangor, SPAN, state water agencies | Recycled water and bulk supply agreements; useful where communities raise water concerns. | A/B |
| State investment agencies | Invest Johor, IRDA, Iskandar Regional Development Authority, Cyberview, Invest Selangor, Selangor Industrial Corp, Northern Corridor (NCIA), InvestPenang, Sarawak Digital Economy Corp | Local project leads, parks, data-centre-ready land, state-backed JV announcements. | A-/B |
| Bursa Malaysia filings and annual reports | `https://www.bursamalaysia.com/`, issuer IR pages: YTLPOWER, TM, Axiata/CelcomDigi, TIME/AIMS, Gamuda, Sime Darby Property, Tropicana, Paragon Globe, JLand/JCorp | Land sales, leases, related-party deals, capex, JV ownership, campus development progress. | A |

Official search templates:

```text
site:mida.gov.my "data centre" Malaysia "{operator}"
site:mida.gov.my "data center" "Johor" "MIDA"
site:mdec.my "data centre" "Malaysia Digital"
site:mydigitalinvestment.gov.my "Data Centre & Cloud"
site:digital.gov.my "data centre" "Vantage" OR "Cyberjaya"
site:miti.gov.my "Data Centre Task Force"
site:jpbd.johor.gov.my "data centre" "OSC 3.0 Plus"
site:johor.gov.my "pusat data" "Kulai"
site:investjohor.gov.my "data centre" "Kulai" OR "Sedenak"
site:cyberview.com.my "data centre" Cyberjaya
site:investselangor.my "data centre" Cyberjaya OR Elmina
site:bursamalaysia.com "data centre" "{issuer}"
site:tnb.com.my "{operator}" "data centre" OR "power"
"{project company}" "Suruhanjaya Tenaga" "data centre"
"{project company}" "Penilaian Kesan Alam Sekitar" OR "EIA"
```

## 3. High-signal trade press and Malaysian press

Use press as discovery and event chronology. Verify named sites through operator, MIDA/MDEC, state, Bursa, planning, utility, or industrial-park sources.

| Source | Route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | `site:datacenterdynamics.com Malaysia "data center"` | Best English live feed for Johor/Cyberjaya construction, GDS/DayOne, STT, NTT, Vantage/Yondr, AirTrunk, Bridge, Equinix, Google, TM, Basis Bay, Empyrion, Selangor JV. | B+ |
| W.Media | `site:w.media Malaysia "data center"` | APAC trade feed, Malaysian cloud/datacenter event coverage, YTL/NVIDIA, Cyberjaya/Johor projects. | B |
| The Edge Malaysia | `site:theedgemalaysia.com "data centre" Malaysia` | Strongest Malaysian business press for policy, MDEC/MIDA quotes, Johor/Cyberjaya market structure, listed-company deals, Alibaba/Oracle/Microsoft cloud updates. | B+ |
| Bernama / New Straits Times / The Star / Malay Mail | site-scoped `data centre` and `pusat data` searches | Government-linked announcements, ministries, state leadership, infrastructure, planning and opposition. | B |
| BusinessToday / Digital News Asia / Lowyat / SoyaCincau / TechNode Global | site-scoped searches | Cloud launches, operator openings, local tech interpretation, Google/AWS/Microsoft/Alibaba updates. | B-/C+ |
| Datacenter Knowledge / Dgtl Infra / Capacity Media / Light Reading / CRN Asia / ET Datacenters | site-scoped searches | Secondary regional deal flow; use to catch missed projects and financing. | B-/C+ |
| Arizton, JLL, CBRE, Cushman & Wakefield, Knight Frank, DC Byte, Structure Research, White & Case, S&P, ISEAS/Fulcrum | report snippets and analysis | Market sizing, capacity and pipeline context, power/water constraints. Use named facilities as leads only unless sourced. | B/C |
| Baxtel, DataCenterMap, Datacenters.com, Cloudscene, PeeringDB, Inflect, ColoMap | direct operator/city pages | Facility addresses, nearby-site discovery, IX connectivity, legacy sites. Never use alone for final capacity/status. | C, sometimes B- when sourced |

Press query templates:

```text
site:datacenterdynamics.com Malaysia "{operator}" "data center"
site:datacenterdynamics.com Malaysia "Johor" ("MW" OR "IT load" OR "power")
site:w.media Malaysia "{operator}" ("data centre" OR "data center")
site:theedgemalaysia.com "data centre" "{operator}" OR "{state}"
site:thestar.com.my "data centre" "Johor" OR "Cyberjaya"
site:nst.com.my "pusat data" "Johor" OR "Cyberjaya"
site:bernama.com "pusat data" "Malaysia" "MIDA"
site:digitalnewsasia.com "data centre" Malaysia
site:lowyat.net "cloud region" Malaysia
site:soyacincau.com "data centre" Google Malaysia
```

## 4. Industry associations, IXPs, events, and interconnect sources

| Body / source | URL / route | Use | Grade |
|---|---|---|---|
| Malaysian Data Centre Alliance (MDCA) | Search `Malaysian Data Centre Alliance`, LinkedIn, Outsourcing Malaysia references | Industry-policy body and event/member ecosystem. Not a public facility registry but useful for active operator/vendor names. | B-/C+ |
| MyIX (Malaysia Internet Exchange) | `https://myix.my/`, AIMS MyIX page, PeeringDB | Member and peering-node discovery, especially AIMS Kuala Lumpur, Cyberjaya, and ISP colo locations. | A-/B |
| DE-CIX Malaysia / DE-CIX Kuala Lumpur / Penang IX | DE-CIX pages, ISOC Pulse IXP tracker, PeeringDB | Interconnection nodes in Kuala Lumpur, Cyberjaya, Johor Bahru, and Penang; useful to identify active carrier hotels and edge sites. | A-/B |
| AIMS interconnection pages | `https://www.aims.com.my/`, MyIX page | AIMS is a core Kuala Lumpur carrier hotel/interconnection source; useful for networks and exchange presence. | A for own sites, B for ecosystem |
| DCCI / Malaysia Cloud & Datacenter Convention / W.Media events | `malaysia.dccisummit.com`, `clouddatacenter.events` | Speaker/exhibitor lists reveal new entrants, contractors, utility issues, and MDEC/MIDA policy leads. | C+ lead source |
| Uptime Institute awards/certificates | `https://uptimeinstitute.com/uptime-institute-awards/list` | Certification evidence for named facilities such as TM, NTT, Vantage, AIMS, etc. A for certificate existence, not full inventory. | A |

IX/interconnect templates:

```text
site:peeringdb.com Malaysia "{operator}" "data center"
"MyIX" "{operator}" "Cyberjaya" OR "Kuala Lumpur"
"DE-CIX Malaysia" "{operator}" "Johor" OR "Cyberjaya"
"Penang IX" "data centre" OR "data center"
site:aims.com.my "MyIX" "data centre"
site:cloudscene.com "Malaysia Internet Exchange" "data center"
```

## 5. Operator, developer, and vendor seed list

Official pages are **A** for marketed presence, facility names, and claimed status. Treat full-campus buildout and "powered land" totals as **B** until phase-specific.

| Operator / developer | Primary routes | Malaysia location signals and query pivots | Notes |
|---|---|---|---|
| DayOne / GDS International | `https://dayonedc.com/market/johor`, DCD GDS launch, Nusajaya Tech Park | `DayOne Johor`, `GDS Nusajaya Tech Park`, `NTP1 NTP2 NTP3`, `Nusajaya Tech Park`, `Kempas Tech Park`, `Iskandar Puteri` | Official DayOne page says it operates across Nusajaya Tech Park and Kempas Tech Park. DCD reports GDS launched NTP campus in Johor with Phase 1 capacity. Avoid double-counting GDS legacy name and DayOne rebrand. |
| Princeton Digital Group (PDG) | `https://princetondg.com/locations/malaysia/` | `PDG JH1 Sedenak Tech Park`, `PDG JH2 Johor`, `Kulai`, `370MW`, `Sedenak` | Official PDG page lists JH1 in STeP/Kulai and JH2 16 km away; strong Johor anchor. |
| Vantage Data Centers / Yondr | `https://vantage-dc.com/data-center-locations/apac/johor-malaysia`, Vantage acquisition release | `Vantage JHB1`, `Yondr Johor`, `Sedenak Tech Park`, `300MW`, `JHB1` | Vantage acquired Yondr's Johor campus. Keep historic Yondr and current Vantage identity linked, not separate facilities. |
| Vantage Cyberjaya | `https://vantage-dc.com/data-center-locations/apac/cyberjaya-i-malaysia/`, `.../cyberjaya-ii-malaysia/` | `KUL1 Cyberjaya`, `KUL11 KUL12 KUL13 KUL14`, `KUL2 Cyberjaya`, `436MW` | KUL1 is operational/complete per Vantage release; KUL2 is large adjacent campus/pipeline. Physical state: Selangor. |
| AirTrunk | AirTrunk official pages/releases, DCD `JHB1` tag | `AirTrunk JHB1 Johor`, `AirTrunk JHB2`, `Digital Halo`, `150MW TNB`, `recycled water`, `rooftop solar` | Strong Johor hyperscale operator. Power/water/renewable releases are high-value stage evidence. |
| YTL Data Centers / YTL Power / YTL AI Cloud / Sea / NVIDIA | `https://ytldatacenters.com/locations/malaysia/`, `https://www.ytlpowerinternational.com/our-businesses/data-centers/`, MIDA YTL/Sea release | `YTL Green Data Center Park`, `YTL Johor`, `Kulai`, `Sea`, `NVIDIA`, `YTL AI Cloud`, `500MW solar`, `JDC` | Official YTL pages prove park; MIDA release records YTL/Sea groundbreaking; W.Media/The Edge report NVIDIA AI facility completion. |
| Bridge Data Centres / Chindata / Bain Capital | `https://www.bridgedatacentres.com/locations/malaysia/`, Bridge MY06 release, MIDA | `MY01`, `MY03`, `MY06`, `MY06 Sedenak`, `Kidex Sedenak`, `ByteDance`, `Plentong` | Bridge has Cyberjaya and Johor footprint; MY06 launch with ByteDance is high-signal. Official site may be thin; combine with MIDA/DCD/Baxtel. |
| ST Telemedia Global Data Centres / Basis Bay | STT GDC releases, Basis Bay pages, DCD | `STT Kuala Lumpur 1`, `Basis Bay Cyberjaya DC.1`, `Basis Bay Cyberjaya DC.2`, `Nusa Cemerlang Industrial Park`, `STT Johor 1`, `NCIP` | STT/Basis Bay JV in Cyberjaya and Johor NCIP campus. Basis Bay official page confirms data-centre services; DCD/MIDA provide stage details. |
| NTT Global Data Centers / NTT DATA | NTT Cyberjaya pages and release | `Cyberjaya 1-6`, `CBJ5`, `CBJ6`, `Gelang Patah`, `Johor Bahru`, `290MW` | Official NTT pages list Cyberjaya 5/6, CBJ6 7MW critical IT load; DCD reports Johor land acquisition/pipeline. |
| Equinix | `https://www.equinix.com/data-centers/asia-pacific-colocation/malaysia-colocation`, KL1/JH1 pages | `Equinix KL1 Cyberjaya`, `Equinix JH1 Johor`, `KL2 Cyberjaya`, `JH2` | Official pages prove KL1/JH1. MIDA/DCD/CRN Asia provide expansion/land/topping-out leads. |
| Digital Realty / CSF Advisers | Digital Realty Malaysia release, DCD | `Digital Realty Cyberjaya`, `TelcoHub 1`, `CSF`, `Jalan Teknokrat 8`, `KL11` | Digital Realty entered Malaysia via Cyberjaya acquisition; legacy CSF names and future DLR names can duplicate. |
| EdgeConneX | `https://www.edgeconnex.com/locations/asia-pacific/kl-malaysia/`, MIDA Cyberjaya article | `EdgeConneX Cyberjaya`, `Kuala Lumpur Malaysia data centers` | Official page is broad; verify individual building/status through Cyberview/MIDA/DCD/directories. |
| Telekom Malaysia / TM Global / TM One | `https://tmglobal.com.my/products-and-solutions/data-centre-solutions/data-centre`, `https://www.tmone.com.my/data-centre-services/` | `KVDC Cyberjaya`, `KJDC Klang/Jalan?`, `IPDC Iskandar Puteri`, `Nusajaya Technology Park`, `Twin Core Data Centres` | Official TM pages are primary for KVDC/IPDC; MIDA/DCD reports expansion and commercial operation timing. |
| AIMS Data Centre / TIME / DigitalBridge | `https://www.aims.com.my/` | `Menara AIMS`, `AIMS Kuala Lumpur`, `AIMS Cyberjaya`, `AIMS Johor`, `MyIX`, `carrier hotel` | Core interconnection hub in Kuala Lumpur; use AIMS/MyIX/PeeringDB for network evidence. |
| Open DC / Extreme Broadband | `https://www.opendc.my/`, CJ1 page | `CJ1 Cyberjaya`, `D8-1 Kedah`, `JB1`, `JB2`, `PE1`, `PE2`, `Johor Bahru`, `Penang`, `Kedah` | Useful local multi-state provider. Official page says six data centres across Cyberjaya, Johor Bahru, Kedah, Penang. |
| IP ServerOne | `https://www.ipserverone.com/data-center-malaysia/` | `IP ServerOne CJ1`, `Cyberjaya`, `Tier 3`, `MYIX-CJ1` | Small/enterprise colo; verify exact colocated building if also listed as Open DC/CJ1. |
| Infinaxis | official pages if available, MIDA/Cyberview/DCD/directories | `Infinaxis Cyberjaya 1`, `Infinaxis Cyberjaya 2`, `Cyberjaya data center` | Emerging Cyberjaya operator; many leads are directory/social, so verify through company/Cyberview/MIDA. |
| NEXTDC | `https://www.nextdc.com/data-centres/malaysia-data-centres-colocation` | `NEXTDC KL1`, `Kuala Lumpur`, `65MW`, `Tier IV` | Official page claims Malaysia KL1; verify physical site and whether "Kuala Lumpur" is Cyberjaya/Selangor before mapping. |
| Axiata/CelcomDigi, Maxis, U Mobile, REDtone, TIME, HeiTech, Mesiniaga, VADS, NTT MSC legacy, local banks | telco/issuer pages, PeeringDB, Uptime, directories | `IDC`, `pusat data`, `data hosting`, `disaster recovery`, `Cyberjaya`, `Kuala Lumpur`, `Shah Alam` | Legacy enterprise/telco facilities. Capture if enumeration includes non-hyperscale commercial/government DCs; avoid counting network exchanges/server rooms as full DCs without facility proof. |
| Google / Sime Darby Property | Google Cloud press corner; Sime Darby Property Elmina release | `Google Elmina Business Park`, `Shah Alam`, `Selangor`, `built-to-suit lease`, `Google Cloud region Malaysia` | Official Google investment and Sime Darby groundbreaking establish the first Google data center site in Selangor. |
| Alibaba Cloud, AWS, Microsoft, Oracle, Tencent, Huawei, IBM | official cloud-region pages, DIO/MDEC/The Edge | `Malaysia West`, `Kulai`, `Johor`, `Kuala Lumpur`, `Cyberjaya`, `ap-southeast-5`, `ap-kulai-2`, `Alibaba Cloud Johor` | Cloud region evidence does not automatically reveal owned physical facilities. Use official docs for service region and pivot to operator/permit evidence. |

Operator query templates:

```text
"{operator}" Malaysia ("data center" OR "data centre") ("MW" OR "IT load" OR "critical IT load" OR "ready for service")
"{operator}" ("Cyberjaya" OR "Kulai" OR "Sedenak" OR "Nusajaya" OR "Iskandar Puteri" OR "Elmina") ("data center" OR "data centre")
site:{operator-domain} Malaysia ("data center" OR "data centre" OR "locations")
site:{operator-domain} ("Cyberjaya" OR "Johor" OR "Kulai" OR "Sedenak" OR "Nusajaya")
"{operator}" Malaysia ("TNB" OR "power" OR "PPA" OR "recycled water" OR "groundbreaking" OR "topped out")
```

## 6. Hyperscaler and cloud-region handling

Cloud-region pages prove cloud availability and data-residency region existence; they do **not** prove exact datacenter address unless the source names a physical site.

| Provider | Official route | Malaysia enumeration use |
|---|---|---|
| AWS | AWS News Blog `Now open - AWS Asia Pacific (Malaysia) Region`; AWS region docs | **A** for Region `ap-southeast-5`, three Availability Zones, launched August 2024. Search Cyberjaya/Selangor/Johor/MIDA/OSC/TNB for physical site evidence; do not infer facility addresses from AZ count. |
| Microsoft Azure | Microsoft News Asia Malaysia West GA; Azure region list; Microsoft Johor Bahru expansion article | **A** for Malaysia West in Greater Kuala Lumpur and Southeast Asia 3/Johor Bahru expansion if listed/announced by Microsoft. Map physical DCs only when planning/operator/land evidence names a site. |
| Google Cloud | Google Cloud press corner 2024 investment; Google locations; Sime Darby Property Elmina groundbreaking | **A** for US$2B investment, first Google data center and Google Cloud region in Malaysia; Sime Darby page is **A** for Elmina Business Park/Selangor built-to-suit lease and groundbreaking. |
| Oracle Cloud Infrastructure | Oracle 2024 Malaysia cloud-region investment; Oracle public cloud region list; OCI release note `ap-kulai-2` | **A** for Oracle commitment and OCI `Malaysia West 2 (Kulai)` region available February 2026. Physical mapping should use Oracle docs plus Kulai/Johor planning/utility/operator evidence. |
| Alibaba Cloud | Alibaba official region pages and The Edge Malaysia Johor launch coverage | Search `Alibaba Cloud Malaysia Johor region`, `two data centres`, `five facilities`. Treat official Alibaba pages as A for cloud region; use press as B for local facility counts until official facility detail appears. |
| Tencent Cloud / Huawei Cloud / IBM Cloud / Cloudflare / Akamai / CDN providers | official infrastructure pages, PeeringDB/IX | Usually PoP/edge/interconnect or partner-hosted. Use as demand/interconnect signal and pivot to AIMS, Equinix, TM, NTT, Vantage, Bridge, Open DC, MyIX/DE-CIX. |

Cloud pivot templates:

```text
"AWS Asia Pacific (Malaysia) Region" "ap-southeast-5" "data center"
"AWS" Malaysia ("Cyberjaya" OR "Selangor" OR "Johor" OR "MIDA" OR "OSC")
"Microsoft" "Malaysia West" ("Kuala Lumpur" OR "Cyberjaya" OR "Johor Bahru")
"Microsoft" "Southeast Asia 3" "Johor Bahru"
"Google" "Elmina Business Park" "data center" "Sime Darby"
"Google Cloud region" Malaysia "Selangor"
"Oracle" "ap-kulai-2" "Kulai" "Malaysia West 2"
"Alibaba Cloud" Malaysia Johor "data centre"
"{cloud provider}" Malaysia ("Equinix" OR "AIMS" OR "NTT" OR "TM" OR "Vantage" OR "Bridge")
```

## 7. State and federal-territory enumeration matrix

Workflow for every division:

1. Search English and Malay terms with state name, capital/cities, districts, and industrial parks.
2. Search operator seeds plus local site names.
3. Search MIDA/MDEC/DIO/state investment pages and Bursa filings for the project company or land seller.
4. Search PBT/OSC/planning, EIA/DOE, TNB/power, and water sources for large sites.
5. Cross-check with trade press, IX/PeeringDB, Uptime, and directories; downgrade unsourced directory-only records.

| Division | Priority places / parks | Operator and source pivots | Query pattern |
|---|---|---|---|
| Johor | Kulai, Sedenak, Iskandar Puteri, Nusajaya Tech Park, Gelang Patah, Nusa Cemerlang Industrial Park, Kempas, Plentong, Senai, Skudai, Tanjung Kupang, Johor Bahru, Kidex Sedenak, YTL Green Data Center Park | DayOne/GDS, PDG, Vantage/Yondr, AirTrunk, YTL, Bridge MY06, STT, NTT Johor, Equinix JH1/JH2, TM IPDC, Open DC JB1/JB2, Oracle Kulai, Alibaba Johor | `"Johor" ("data centre" OR "pusat data") ("Kulai" OR "Sedenak" OR "Nusajaya" OR "Gelang Patah")`; `site:jpbd.johor.gov.my "data centre"`; `site:investjohor.gov.my "data centre"`; `"{operator}" "Johor" "MW"` |
| Selangor | Cyberjaya, Shah Alam, Elmina Business Park, Sepang, Petaling Jaya, Subang, Klang, Puchong, Kajang/Bangi | Vantage KUL1/KUL2, NTT Cyberjaya, Equinix KL1/KL2, Digital Realty/CSF, Google Elmina, TM KVDC/KJDC, Open DC CJ1, IP ServerOne, Basis Bay/STT, EdgeConneX, Infinaxis, Selangor Industrial Corp/DC Union | `"Cyberjaya" ("data centre" OR "pusat data") ("MW" OR "critical IT load")`; `"Elmina Business Park" "Google" "data center"`; `site:cyberview.com.my "data centre"`; `site:investselangor.my "data centre"` |
| Wilayah Persekutuan Kuala Lumpur | Menara AIMS, central carrier hotels, financial district, Bukit Jalil, Bangsar, exchange/IX nodes | AIMS, MyIX, DE-CIX, TIME, Maxis, telco/enterprise colo. Beware KL marketing labels for Cyberjaya/Selangor. | `"Kuala Lumpur" ("data centre" OR "carrier hotel" OR "MyIX")`; `"Menara AIMS" "data centre"`; `site:aims.com.my "Kuala Lumpur" "data centre"` |
| Pulau Pinang | Bayan Lepas, George Town, Batu Kawan, Seberang Perai, Penang Science Park, Penang IX | Open DC PE1/PE2, DE-CIX/Penang IX, telcos, semiconductor supply-chain DR sites | `"Penang" OR "Pulau Pinang" ("data centre" OR "pusat data")`; `"Bayan Lepas" "data centre"`; `"Penang IX" "data centre"`; `site:investpenang.gov.my "data centre"` |
| Kedah | Kulim Hi-Tech Park, Kulim, Sungai Petani, Alor Setar | Open DC D8-1, Kulim tech/semiconductor demand, NCIA, possible DR/edge | `"Kedah" OR "Kulim" ("data centre" OR "pusat data")`; `"Kulim Hi-Tech Park" "data centre"`; `"Open DC" "Kedah" "D8-1"` |
| Melaka | Ayer Keroh, Melaka City, industrial parks | Mostly smaller enterprise/telco/DR unless named project emerges; Arizton includes Melaka as coverage lead. | `"Melaka" ("data centre" OR "pusat data") ("MIDA" OR "industrial park" OR "TNB")`; `"Ayer Keroh" "data centre"` |
| Negeri Sembilan | Nilai, Seremban, Enstek, Sendayan TechValley, Malaysia Vision Valley | Search for spillover from Klang Valley and industrial park land/power leads. | `"Negeri Sembilan" ("data centre" OR "pusat data")`; `"Nilai" "data centre"`; `"Sendayan" "data centre"`; `"Enstek" "data centre"` |
| Perak | Ipoh, Batu Gajah, Kamunting, Lumut/Manjung | Edge/DR, state digital projects, industrial park leads; Arizton includes Perak as market coverage lead. | `"Perak" OR "Ipoh" ("data centre" OR "pusat data")`; `site:perak.gov.my "pusat data"` |
| Perlis | Kangar, Padang Besar | Low likelihood for commercial colo; search government/telco edge and DR only. | `"Perlis" OR "Kangar" ("data centre" OR "pusat data" OR "pusat pemulihan bencana")` |
| Kelantan | Kota Bharu, Pengkalan Chepa | Government/telco/edge; beware generic government data-center references. | `"Kelantan" OR "Kota Bharu" ("pusat data" OR "data centre")`; `site:kelantan.gov.my "pusat data"` |
| Terengganu | Kuala Terengganu, Kemaman, Kerteh | Government/telco/energy-sector DR; possible industrial/energy leads. | `"Terengganu" ("pusat data" OR "data centre") ("Kemaman" OR "Kerteh" OR "TNB")` |
| Pahang | Kuantan, Gebeng, Pekan, Bentong, Cameron/telecom sites | Industrial/energy/cable/DR search; no major current hyperscale seed. | `"Pahang" OR "Kuantan" ("pusat data" OR "data centre")`; `"Gebeng" "data centre"` |
| Sabah | Kota Kinabalu, Sepanggar, Cyber City/SICC area, cable landing | Government cloud, telco/edge, IX/cable resilience. Use Sabah digital economy/state portals. | `"Sabah" OR "Kota Kinabalu" ("data centre" OR "pusat data")`; `site:sabah.gov.my "pusat data"`; `"DE-CIX" Sabah OR "MyIX" Sabah` |
| Sarawak | Kuching, Samarahan, Miri, Bintulu, Samalaju, hydro/renewable zones | Sarawak Digital Economy Corp, state cloud, telco/edge, renewable-power pitch, Kuching IX/cables. | `"Sarawak" OR "Kuching" ("data centre" OR "pusat data")`; `site:sarawak.gov.my "pusat data"`; `"Sarawak Digital" "data centre"` |
| Wilayah Persekutuan Putrajaya | Putrajaya, Cyberjaya boundary | Federal government data platforms and DR; commercial records often actually Cyberjaya/Selangor. | `"Putrajaya" ("pusat data" OR "data centre" OR "disaster recovery")`; `"Putrajaya" "Cyberjaya" "data centre"` |
| Wilayah Persekutuan Labuan | Labuan financial centre, offshore finance/DR, cable/telecom | Low likelihood for large DC; search banking/telecom DR and government data rooms. | `"Labuan" ("data centre" OR "pusat data" OR "disaster recovery" OR "colocation")` |

## 8. Reliability and deduplication cautions

- **Johor naming duplicates**: `JHB1` may refer to AirTrunk or Vantage/Yondr depending on source. Always store operator-specific campus code and source date.
- **GDS vs DayOne**: GDS International rebranded to DayOne; do not double-count Nusajaya/Kempas assets under both names.
- **Vantage vs Yondr**: Vantage acquired Yondr's Johor campus; keep historic owner and current operator fields separate.
- **CSF/Digital Realty**: Cyberjaya TelcoHub/CSF pages and Digital Realty Malaysia pages may refer to the same acquired asset.
- **Kuala Lumpur vs Cyberjaya**: Many official international pages call Cyberjaya "Kuala Lumpur"; physical state is Selangor.
- **Cloud regions vs facilities**: AWS/Microsoft/Google/Oracle/Alibaba region names are high-grade cloud-service evidence, but exact buildings require separate planning/operator/land/utility proof.
- **Capacity numbers**: distinguish `critical IT load`, `facility load`, `power supply`, `powered land`, and long-term campus buildout. Store units exactly.
- **Directories**: Baxtel/DataCenterMap/Cloudscene are useful for addresses and nearby facilities, but use as C unless corroborated by operator, exchange, Uptime, planning, or press.
- **Government data centres**: `pusat data nasional`, ministry data hubs, and state integrated data centers may be public-sector IT rooms rather than commercial datacenters. Include only if scope explicitly covers government facilities or if size/operator evidence is meaningful.
- **Social posts**: Facebook/LinkedIn/Instagram can reveal groundbreaking or community opposition leads, but should not be final proof without official/press corroboration.

## 9. Fast enumeration playbook

1. Start with Johor and Selangor/Cyberjaya using operator seeds: DayOne/GDS, PDG, Vantage/Yondr, AirTrunk, YTL, Bridge, STT/Basis Bay, NTT, Equinix, TM, Digital Realty/CSF, Google, Open DC, AIMS.
2. For every large lead, search project/operator + `MIDA`, `MDEC`, `Bursa`, `TNB`, `OSC 3.0 Plus`, `Johor Fast Lane`, `EIA`, `water`, and the industrial park name.
3. Use DCD/W.Media/The Edge to build event timeline: announced, land acquired, groundbreaking, topped out, launch/operational.
4. Use MyIX/DE-CIX/PeeringDB/Uptime/operator connectivity pages to fill legacy carrier hotel and smaller colo sites in Kuala Lumpur, Cyberjaya, Penang, Johor Bahru, Sabah/Sarawak.
5. Sweep each remaining state with Malay terms plus capital city and industrial parks, then downgrade weak state digital-platform results unless they identify a physical datacenter.
