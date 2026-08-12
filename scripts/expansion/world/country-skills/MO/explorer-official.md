# MO Explorer Official —— 澳门数据中心枚举方法（官方来源）
# MO Explorer Official — Macao Datacenter Enumeration Methodology (Official Sources)

审阅日期 / Date reviewed: 2026-08-12
国家 / Country: **MO 澳门 Macao**
Manifest / 分区依据: `/scripts/expansion/world/world-manifest.jsonl` entry:
`{"country_code":"MO","country_name":"Macao","subnational_type":"country","divisions":["Macao"]}`

分区模型 / Division model: **country**. Every record must use `division="Macao"`. More precise geography is stored only in auxiliary fields: `area` (澳门半岛/Taipa/Cotai/Coloane/new reclamation), `parish` when meaningful, and `place_or_address`.

范围 / Scope: official law, regulator, licensing, government procurement, public works, power utility, telecom operator, gaming regulator, data protection, finance regulator, official cloud-region pages, and statutory issuer disclosures used to enumerate Macao data-centre facilities.

## 可靠性等级 / Reliability Grades

- **A** = 一级/责任来源 for the exact fact cited: Macao SAR Government Portal (`gov.mo`), Government Information Bureau/GCS (`gcs.gov.mo`), Official Gazette/Boletim Oficial (`bo.dsaj.gov.mo`, legacy `bo.io.gov.mo` links may redirect), Macao Post and Telecommunications Bureau/CTT telecom site (`telecommunications.ctt.gov.mo`, `ctt.gov.mo`), DICJ, GPDP, AMCM, DSEC, SAFP, DSSCU/DSOP, CEM, CTM, cloud-provider official region pages, HKEX/SEC filings from concessionaires.
- **B** = reliable secondary source for named facts: Macau Business, Macao News, Macau Daily Times, TDM, Plataforma, Hoje Macau, Ponto Final, Macau Post Daily, DCD, Capacity Media, Reuters, Bloomberg, SCMP, reputable engineering/vendor case studies.
- **C** = lead only: DataCenterMap, Baxtel, Cloudscene, datacenters.com, Inflect, brokerage pages, market-size reports, job ads, event pages, social posts.
- **U** = checked and unsupported. Do not count.

Grade only the fact actually supported. A cloud-region page can grade "Macao is absent/present as a region", not an address. A Gazette authorization can grade "entity authorized to install and operate data centres", not "facility is built, live, or has X MW". A casino concessionaire annual report can grade "property/IT/capex disclosure", not a separately countable public colocation facility unless the filing says that.

## 0. 澳门结构事实 / Macao-Specific Structure

- 澳门 is a Special Administrative Region with no province/state layer in this manifest. The only valid division is **Macao**.
- Local routing fields: Macau Peninsula (Sé, Fátima, Santo António, São Lázaro, São Lourenço), Taipa (Carmo), Coloane (São Francisco Xavier), Cotai reclamation, and new reclamation zones such as Zone A/E.
- Official-language searching must cover Traditional Chinese, Portuguese, English, and Simplified Chinese: `數據中心`, `資料中心`, `数据中心`, `centro de dados`, `data centre`, `data center`, `datacenter`, `IDC`.
- **Key verified correction:** Macao has a 2024 legal regime for data centres. Administrative Regulation No. 13/2024, `Regime de instalação e funcionamento de centros de dados` / `數據中心的設立及運作制度`, defines a data centre as paid third-party physical space with equipment, electricity and Internet access for data storage/processing, and requires prior Chief Executive authorization.
- CTT telecom pages are therefore a primary licensing source. CTT published on 2024-10-04 that, under Reg. 13/2024, only **Macau Telecommunications Company Limited (CTM)** had been issued a data-centre authorization at that time. CTT's telecom regulation list also shows Chief Executive Dispatch No. 180/2025 renewing CTM authorization No. 1/2024 from 2025-10-01 to 2027-09-30.
- CEM is the sole concessionaire for electric power distribution in Macao per the Macao SAR Government portal; CEM/CEM annual reports are A-grade for power-supply facts.
- Gaming is the dominant local demand driver, but casino internal server rooms must be tracked separately from public colocation data centres. The 2024 data-centre regime is explicitly about paid third-party space; internal casino IT rooms may fall outside the enumerated public-DC licensing count unless separately authorized or offered to third parties.

## 1. Official / Regulatory Pipeline

### 1.1 Government Portal, GCS, SAFP, Government Cloud

Verified sources:
- Macao SAR Government Portal: https://www.gov.mo
- Government Information Bureau / GCS: https://www.gcs.gov.mo
- Public Administration and Civil Service Bureau / SAFP: https://www.safp.gov.mo
- SAFP procurement example: https://www.safp.gov.mo/zh-hant/news/tender/202102/20448659482736153533003969988285

Use these for government cloud, government data centre, e-government maintenance notices, tenders, and official news. SAFP pages confirm active government cloud/data-centre operations and maintenance; they are A-grade for government project facts, but a government cloud is not automatically a public colocation facility.

```text
site:gov.mo "數據中心" OR "資料中心" OR "雲計算中心"
site:gcs.gov.mo "數據中心" OR "政府雲" OR "centro de dados"
site:safp.gov.mo "雲計算中心" OR "政府數據中心" OR "7x24"
site:safp.gov.mo "採購" "雲計算中心"
"government cloud" OR "government data centre" Macao OR Macau
```

### 1.2 CTT Telecom Regulator and Data-Centre Authorization

Verified sources:
- Macao Post and Telecommunications Bureau entity page: https://www.gov.mo/en/entity-page/entity-4928/
- CTT telecom law/regulation list: https://telecommunications.ctt.gov.mo/en/Laws/Details?alias=allreg
- Reg. 13/2024 in the Official Gazette: https://bo.dsaj.gov.mo/bo/i/2024/13/regadm13.asp and Chinese version https://bo.dsaj.gov.mo/bo/i/2024/13/regadm13_cn.asp
- CTT 2024 notice on issuance of one authorization: https://telecommunications.ctt.gov.mo/zh/News/Details/4107

Method:
1. Search CTT regulations first for `Regulamento Administrativo n.º 13/2024`, `數據中心的設立及運作制度`, `install and operate data centers`, and authorization renewals.
2. Treat CTT/Gazette authorization records as A-grade for the licensing fact.
3. Do not infer facility address, capacity, status, or public availability from authorization alone. Follow the license holder to operator pages, tenders, and secondary sources.

```text
site:telecommunications.ctt.gov.mo "data centers" OR "centros de dados"
site:telecommunications.ctt.gov.mo "數據中心" "許可"
site:bo.dsaj.gov.mo "數據中心的設立及運作制度"
site:bo.dsaj.gov.mo "centros de dados" "Companhia de Telecomunicações de Macau"
site:bo.dsaj.gov.mo "install and operate data centers" Macau
```

### 1.3 DSEDT, Innovation Policy, and Telecom-Adjacent Context

Verified source:
- Economic and Technological Development Bureau / DSEDT entity page: https://www.gov.mo/en/entity-page/entity-7809/
- DSEDT site: https://www.dsedt.gov.mo

DSEDT is useful for economic/technology policy, SME digitalization, and innovation context. Telecom licensing and the 2024 data-centre authorization regime should be sourced to CTT/Gazette unless a specific DSEDT page is the actual source.

```text
site:dsedt.gov.mo "數據中心" OR "雲" OR "科技"
site:dsedt.gov.mo "人工智能" OR "智慧城市"
site:gov.mo "經濟及科技發展局" "數據中心"
```

### 1.4 CTM Macau Telecommunications

Verified sources:
- CTM business cloud page: https://www.ctm.net/en-US/business/cloudService.html
- CTM data-centre services page: https://www.ctm.net/en-US/business/ctmDataCenter.html
- CTM Hong Kong data-centre service page: https://www.ctm.net/zh-TW/business/hkDataCenter.html

CTM is the primary operator seed because CTT records show CTM is authorized to install and operate data centres. CTM pages are A-grade for CTM's own services and product labels. If the page is JavaScript-heavy, preserve the URL and corroborate with CTT/Gazette and B/C directories for address leads.

```text
site:ctm.net "Data Center Services" OR "CTM Data Centre"
site:ctm.net "數據中心" OR "IDC" OR "雲"
"澳門電訊" "數據中心" OR "IDC"
"Macau Telecommunications Company Limited" "data centers" "authorization"
```

### 1.5 CEM Power

Verified sources:
- CEM: https://www.cem-macau.com
- CEM annual reports: https://www.cem-macau.com/en/media-centre/publications/annual-report/
- Macao SAR Government statement identifying CEM as sole electric-power concessionaire: https://www.gov.mo/en/news/100243/

CEM/CEM annual reports are A-grade for grid, concession, reliability, power mix, and Macao electricity-supply background. There is no public data-centre grid-connection register; power facts must be linked by named customer/project evidence.

```text
site:cem-macau.com "data centre" OR "數據中心" OR "centro de dados"
site:cem-macau.com "annual report" "imported electricity"
"CEM" "Macau" "data centre" OR "green power"
"澳門電力" "數據中心" OR "供電"
```

### 1.6 DICJ Gaming Regulator and Casino IT Requirements

Verified sources:
- DICJ: https://www.dicj.gov.mo
- DICJ entity page: https://www.gov.mo/en/entity-page/entity-322/
- DICJ EGM technical standards: https://www.dicj.gov.mo/web/en/egm/standards/index.html
- Government concession-signing news: https://www.gov.mo/en/news/289189/
- Gaming machine approval service: https://www.gov.mo/en/services/ps-1409/ps-1409a/

Use DICJ and Gazette records for gaming technology requirements, EGM standards, machine approval, concession framework, and casino regulatory facts. These sources support demand drivers and internal IT obligations; they do not by themselves identify a countable third-party data centre.

```text
site:dicj.gov.mo "EGM" OR "technical standards" OR "gaming machines"
site:dicj.gov.mo "數據" OR "資訊科技" OR "監控"
site:gov.mo "gaming concession contracts" "1 January 2023"
site:gov.mo "gaming machines" "DICJ" "Macau EGM Technical Standards"
"博彩監察協調局" "電子博彩機" "技術標準"
```

### 1.7 Cybersecurity, GPDP, AMCM

Verified sources:
- Cybersecurity law official explanation by Judiciary Police: https://www.pj.gov.mo/Web/Policia/CyberSafe/?lang=en
- Cybersecurity Law No. 13/2019 Gazette link: https://bo.io.gov.mo/bo/i/2019/25/lei13_cn.asp
- GPDP: https://www.gpdp.gov.mo
- AMCM: https://www.amcm.gov.mo

Law No. 13/2019 was published on 2019-06-24 and came into effect on 2019-12-22. It supports cybersecurity/compliance demand for critical infrastructure operators. GPDP and AMCM support privacy, cross-border data, and financial-outsourcing evidence. These are demand/regulatory sources, not facility evidence unless a named data-centre project is stated.

```text
site:pj.gov.mo "Cybersecurity Law No. 13/2019"
site:gpdp.gov.mo "跨境" OR "個人資料" OR "雲"
site:amcm.gov.mo "外包" OR "數據中心" OR "災備"
"網絡安全法" "博彩" "澳門" "關鍵基礎設施"
```

### 1.8 Official Gazette, Procurement, Land, and Public Works

Verified sources:
- Official Gazette current domain: https://bo.dsaj.gov.mo
- DSOP entity page: https://www.gov.mo/en/entity-page/entity-8042/
- DSSCU history page: https://www.dsscu.gov.mo/en/aboutus/history

Use `bo.dsaj.gov.mo` for public tenders, awards, legal regimes, authorizations, land grants, and notices. DSSOPT was restructured; as of the verified official pages, land/urban construction is DSSCU and public works is DSOP.

```text
site:bo.dsaj.gov.mo "數據中心" OR "雲計算中心" OR "資訊科技"
site:bo.dsaj.gov.mo "centro de dados" OR "centros de dados" OR "informática"
site:bo.dsaj.gov.mo "公開招標" "數據中心"
site:bo.dsaj.gov.mo "判給" "雲計算中心"
site:dsscu.gov.mo "數據中心" OR "centro de dados"
site:dsop.gov.mo "數據中心" OR "centro de dados"
```

### 1.9 Cloud-Region Official Pages

Verified official pages checked:
- AWS: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Azure: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud: https://cloud.google.com/about/locations
- Oracle OCI: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm
- Alibaba Cloud: https://www.alibabacloud.com/en/global-locations
- Tencent Cloud: https://www.tencentcloud.com/global-infrastructure and CVM region list https://cloud.tencent.com/document/product/213/6091
- Huawei Cloud: https://www.huaweicloud.com/intl/en-us/about/global-infrastructure.html

Review result: no official hyperscale cloud region named Macao/Macau was found in the checked region lists. Tencent's China CVM list groups Hong Kong under `港澳台地区（中国香港）`; that is a Hong Kong region (`ap-hongkong`), not a Macao region. Alibaba lists China (Hong Kong), Shenzhen, Guangzhou, Heyuan, etc., but not Macao. Treat all neighbouring regions as service-path context only.

```text
"Macau" OR "Macao" site:docs.aws.amazon.com/global-infrastructure
"Macau" OR "Macao" site:learn.microsoft.com/en-us/azure/reliability/regions-list
"Macau" OR "Macao" site:cloud.google.com/about/locations
"Macau" OR "Macao" site:docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm
"Macau" OR "Macao" site:alibabacloud.com/en/global-locations
"澳门" OR "澳門" site:cloud.tencent.com/document/product/213/6091
"Macau" OR "Macao" site:huaweicloud.com/intl/en-us/about/global-infrastructure
```

### 1.10 Gaming Concessionaire Disclosures

Primary issuer sources:
- SJM Resorts: https://www.sjmresorts.com
- Galaxy Entertainment: https://www.galaxyentertainment.com
- Sands China: https://www.sandschina.com
- Wynn Macau: https://www.wynnmacaulimited.com
- MGM China: https://www.mgmchinaholdings.com
- Melco Resorts: https://www.melco-resorts.com
- HKEXnews: https://www.hkexnews.hk
- SEC EDGAR for US-listed Melco/Wynn/Las Vegas Sands disclosures: https://www.sec.gov/edgar/search/

Use these for official property lists, concession/capex/technology disclosures, cyber incidents, outsourcing, and continuity risk. Do not count a resort as a data centre without facility-level evidence.

```text
site:hkexnews.hk "data centre" OR "數據中心" "Macau"
site:hkexnews.hk "information technology" "Macau" "casino"
site:sec.gov "Macau" "data center" "casino"
site:galaxyentertainment.com "data centre" OR "IT infrastructure"
site:sandschina.com "data centre" OR "information technology"
site:wynnmacaulimited.com "data centre" OR "cybersecurity"
site:mgmchinaholdings.com "data centre" OR "IT"
site:melco-resorts.com "data centre" OR "cybersecurity"
```

## 2. Per-Division Enumeration

Manifest division: **Macao** only. Store every candidate as:

```json
{
  "division": "Macao",
  "area": "Macau Peninsula | Taipa | Cotai | Coloane | New Reclamation | Hengqin/Zhuhai (cross-border, CN jurisdiction)",
  "parish": "...",
  "place_or_address": "...",
  "source_grade_by_fact": {}
}
```

### Macau Peninsula

Expected: government data centre/cloud operations, CTM/business telecom facilities, financial IT, corporate headquarters.

```text
"澳門半島" OR "新口岸" OR "皇朝區" "數據中心"
"Macau Peninsula" OR "NAPE" "data centre"
site:bo.dsaj.gov.mo "數據中心" "澳門"
site:safp.gov.mo "政府數據中心"
```

### Taipa

Expected: CTM/data-centre directory leads, telecom nodes, airport/hospitality IT, disaster-recovery candidates.

```text
"氹仔" "數據中心" OR "資料中心"
"Taipa" "data centre" Macau
"CTM Data Centre" Taipa OR "Rua do Lago Sai Van"
site:ctm.net "Taipa" "Data Centre"
```

### Cotai

Expected: casino-resort internal IT rooms and surveillance/EGM infrastructure demand. Count separately from public data centres.

```text
"路氹" "數據中心" OR "資訊科技"
"Cotai" "data centre" OR "casino IT"
"威尼斯人" OR "倫敦人" OR "巴黎人" "數據中心"
"Galaxy Macau" OR "Wynn Palace" OR "MGM Cotai" "data centre"
"Studio City" OR "City of Dreams" OR "Grand Lisboa Palace" "data centre"
```

### Coloane

Expected: low density; power-plant/electrical infrastructure context, possible industrial/disaster-recovery leads.

```text
"路環" "數據中心" OR "災備"
"Coloane" "data centre" Macau
site:cem-macau.com "Coloane" "power station"
```

### New Reclamation Zones

Expected: planning/land pipeline only unless a named authorized facility appears.

```text
"新城填海區" "數據中心"
"Zona de Aterro" "centro de dados" Macau
site:bo.dsaj.gov.mo "新城填海區" "數據中心" OR "批給"
```

### Hengqin / Zhuhai Cross-Border

Expected: neighbour facilities serving Macao disaster recovery or cloud access. Always store as CN jurisdiction and exclude from Macao counts.

```text
"橫琴" OR "横琴" "數據中心" "澳門"
"珠海" "數據中心" "澳門企業" OR "災備"
"Hengqin" "data centre" Macau
"Zhuhai" "data center" Macau
```

## 3. Known Official Leads

| Subject | Area | Supported fact | Primary evidence | Grade |
| --- | --- | --- | --- | --- |
| Reg. 13/2024 data-centre regime | All Macao | Paid third-party data centres require prior Chief Executive authorization; decisions published in Gazette | `bo.dsaj.gov.mo` Reg. 13/2024 | A |
| CTT data-centre authorization notice | All Macao | As of 2024-10-04, only CTM had received an authorization under Reg. 13/2024 | CTT news `telecommunications.ctt.gov.mo/zh/News/Details/4107` | A |
| CTM authorization renewal | All Macao | CTM authorization No. 1/2024 renewed 2025-10-01 through 2027-09-30 | CTT regulations list / Gazette Dispatch No. 180/2025 | A |
| CTM Data Centre / CTM Cloud | Address to verify | CTM markets data-centre and cloud services | CTM business pages | A for CTM service existence |
| SAFP government cloud/data centre | Government systems | Government cloud/data centre operations, maintenance and procurement | SAFP notices/tenders | A for government project facts |
| CEM power concession | All Macao | CEM is sole electric-power concessionaire; power supply background | `gov.mo`, CEM reports | A |
| DICJ EGM standards | Casinos | Gaming machines require DICJ approval and EGM standards | DICJ/gov.mo | A |
| Six gaming concessions | Casinos | Contracts effective 2023-01-01 for 10 years | `gov.mo` concession-signing news and Gazette/contracts | A |
| Hyperscale cloud regions | n/a | No official Macao region found in checked region lists | AWS/Azure/GCP/OCI/Alibaba/Tencent/Huawei pages | A for absence in checked pages |

## 4. Validation Checklist

For each candidate:

1. Confirm `division="Macao"`; never create subnational divisions.
2. If the candidate is public/third-party colocation, check CTT authorization records first.
3. Split evidence by fact: legal authorization, facility existence, address, status, owner, capacity, certification, power, customers.
4. For CTM, combine CTT authorization + CTM product page + address-level evidence from CTM or B/C directories; mark directory address as C until confirmed.
5. For government cloud, track as government infrastructure unless a public third-party data-centre service is stated.
6. For casinos, tag `facility_type="casino_internal_it"` unless a source says it is third-party colocation or separately authorized.
7. For cloud providers, record Macao absence/presence only from official region pages; do not map Hong Kong/Shenzhen/Guangzhou regions into Macao.
8. For Hengqin/Zhuhai, store outside Macao counts with jurisdiction note.

## 5. Re-Check Cadence

- **Monthly:** CTT telecom regulations/news, CTM news/product pages, SAFP tenders, Gazette Série I/II, DICJ notices, CEM news.
- **Quarterly:** cloud-region pages, HKEX/SEC concessionaire filings, GPDP/AMCM decisions, DSEC/DICJ background statistics.
- **Event-driven:** new data-centre authorization, CTM license renewal, government cloud procurement, casino cyber/IT disclosure, land grant or change-of-use notice.
- **Annually:** refresh regulator names/domains, parish/area mapping, cloud-region list, and all C-grade directory leads.

## 6. Red Flags

- Do not count `港澳台地区（中国香港）` as a Macao cloud region; it is Hong Kong.
- Do not count internal casino IT rooms as public data centres.
- Do not treat authorization as built capacity.
- Do not use directory counts as validated facility totals.
- Do not mix Hengqin/Zhuhai facilities into Macao counts.
- Do not rely on English only; Portuguese and Traditional Chinese queries are essential.
