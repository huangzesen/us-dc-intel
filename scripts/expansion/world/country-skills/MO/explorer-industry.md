# MO Explorer Industry —— 澳门数据中心行业/媒体/厂商发现
# MO Explorer Industry — Industry / Trade-Press / Vendor Discovery for Macao Datacenters

审阅日期 / Date reviewed: 2026-08-12
国家 / Country: **MO 澳门 Macao**
Manifest / 分区依据: `{"country_code":"MO","country_name":"Macao","subnational_type":"country","divisions":["Macao"]}`

分区模型 / Division model: **country**. All candidates use `division="Macao"`; add `area`, `parish`, and `place_or_address` for local routing. Cross-border Hengqin/Zhuhai leads are retained only as adjacent CN-jurisdiction evidence.

范围 / Scope: operator websites, vendor case studies, trade press, local media, cloud and interconnect sources, aggregator directories, and gaming-industry disclosures used to discover Macao data-centre candidates before upgrading facts to official/operator evidence.

## 可靠性等级 / Reliability Grades

- **A** = operator/vendor/issuer/government source responsible for the exact fact: CTM, CTT/Gazette authorization, SAFP, CEM, DICJ, GPDP, AMCM, cloud-provider official region pages, HKEX/SEC issuer filings.
- **B** = named project facts from reliable media or contractor pages: Macau Business, Macao News, Macau Daily Times, TDM, Plataforma, Hoje Macau, Ponto Final, Macau Post Daily, DCD, Capacity Media, Reuters, Bloomberg, SCMP, reputable integrators.
- **C** = discovery only: DataCenterMap, Baxtel, Cloudscene, datacenters.com, Inflect, broker pages, market reports, job ads, event listings, LinkedIn/social pages.
- **U** = checked and unsupported; never count.

Scoring rule: source grade follows the fact, not the facility. Directory address = C until confirmed. CTM service page = A for CTM service existence. CTT authorization = A for authorization. Casino annual report = A for disclosed property/IT facts, not for an independently countable public colocation facility.

## 0. Market Model

澳门 is a small, land-constrained, high-compliance market. Discovery should use this order:

1. **CTT/Gazette licensing spine:** since Administrative Regulation No. 13/2024 requires authorization to install and operate paid third-party data centres, CTT/Gazette records are the first filter for public/colocation facilities. Verified CTT notice: as of 2024-10-04, only CTM had been issued such authorization; CTT regulations list later shows CTM authorization renewal through 2027-09-30.
2. **Operator pages:** CTM Data Centre, CTM Cloud, CTM Hong Kong Data Centre. Use these to confirm product/service existence, then seek address/status detail.
3. **Government cloud:** SAFP government cloud/data-centre notices and tenders identify government infrastructure, not commercial colocation unless stated.
4. **Gaming demand:** six casino concessionaires drive local IT, surveillance, EGM, cyber, payment, hotel, CRM, and continuity demand. Track casino internal IT rooms separately.
5. **Neighbouring regions:** Hong Kong, Shenzhen, Guangzhou, Heyuan, Hengqin, Zhuhai carry most hyperscale/cloud/disaster-recovery capacity. They are context, not Macao facilities.

## 1. Search Vocabulary

English:

```text
data centre OR data center OR datacenter Macau OR Macao
colocation OR colo Macau
Internet data centre OR IDC Macau
CTM Data Centre Macau
Macau Telecommunications Company Limited data centers authorization
government cloud OR government data centre Macau
casino data centre OR gaming data centre Macau
EGM technical standards Macau data
critical infrastructure cybersecurity Macau gaming
Hengqin OR Zhuhai data centre Macau
```

Traditional Chinese:

```text
數據中心 澳門
資料中心 澳門
數據中心的設立及運作制度
設立及運作數據中心 許可 澳門
澳門電訊 數據中心
雲計算中心 政府數據中心 行政公職局
博彩 數據中心 澳門
娛樂場 資訊科技 數據 澳門
電子博彩機 技術標準 澳門
橫琴 數據中心 澳門
珠海 數據中心 澳門
```

Simplified Chinese:

```text
数据中心 澳门
澳门电讯 数据中心
澳门 政府云 数据中心
澳门 博彩 数据中心
横琴 数据中心 澳门
珠海 数据中心 澳门 灾备
```

Portuguese:

```text
centro de dados Macau
centros de dados Macau
Regime de instalação e funcionamento de centros de dados
Companhia de Telecomunicações de Macau centros de dados
concurso público centro de dados Macau
centro de computação em nuvem Governo Macau
jogos de fortuna ou azar centro de dados Macau
```

Status and facility terms:

```text
authorized / renewed / licensed / opens / operational / in service
concurso público / adjudicação / autorização / renovação
公開招標 / 判給 / 許可 / 續期 / 啟用 / 維護
MW / MVA / racks / Tier III / ISO 27001 / TIA-942 / PUE
```

## 2. Primary Operator / Vendor Pipeline

### CTM

Seed URLs:
- https://www.ctm.net/en-US/business/ctmDataCenter.html
- https://www.ctm.net/en-US/business/cloudService.html
- https://www.ctm.net/zh-TW/business/hkDataCenter.html

CTM is the only verified authorized public data-centre operator lead from the checked CTT notice. CTM's own pages are A-grade for CTM service existence, but may not expose all address/capacity details because the site is JavaScript-heavy.

```text
site:ctm.net "Data Center Services" OR "CTM Data Centre"
site:ctm.net "數據中心" OR "IDC" OR "CTM Cloud"
"澳門電訊" "數據中心" "許可"
"CTM Macau Data Center" "Taipa" OR "Rua do Lago Sai Van"
```

### Other Telecom Operators

Entities to check: MTel, Hutchison Telephone (Macau) / 3 Macau, China Telecom (Macau), SmarTone Macau. The CTT regulations list contains telecom licenses for these operators, but a telecom license is not a data-centre authorization. Upgrade only if a source states data-centre services or an authorization.

```text
"MTel" Macau "data centre" OR "數據中心"
"和記電話" 澳門 "數據中心" OR "IDC"
"中國電信（澳門）" "數據中心" OR "IDC"
"數碼通" 澳門 "數據中心" OR "IDC"
site:telecommunications.ctt.gov.mo "{operator}" "data centers"
```

### Government and Integrators

SAFP tenders for cloud/data-centre operation and maintenance are high-value leads. Vendor case studies from Huawei, HPE, Cisco, Schneider Electric, Vertiv, NTT, ZTE, and local integrators can reveal implementation details, but grade them B unless the operator/government confirms.

```text
site:safp.gov.mo "雲計算中心" "判給" OR "採購"
site:bo.dsaj.gov.mo "雲計算中心" "判給"
"Huawei Cloud Stack" CTM Macao
"澳門" "雲計算中心" "維護服務"
"澳門" "數據中心" "施耐德" OR "維諦" OR "華為" OR "中興"
```

### Casino Concessionaires

Use official filings to identify IT/cyber/capex disclosures and property lists:

```text
site:hkexnews.hk "Macau" "information technology" "casino"
site:hkexnews.hk "數據中心" "澳門" "博彩"
site:sec.gov "Macau" "data center" "Wynn" OR "Melco" OR "Sands"
"Galaxy Macau" "data centre" OR "IT infrastructure"
"MGM Cotai" "data centre" OR "IT infrastructure"
"Wynn Palace" "data centre" OR "cybersecurity"
"Studio City" "data centre" OR "surveillance"
```

Treat results as one of:
- `public_colocation_dc`: authorization/operator evidence required.
- `government_cloud_or_data_centre`: official SAFP/Gazette evidence required.
- `casino_internal_it`: property/system evidence; not counted as public colocation.
- `cross_border_adjacent`: Hengqin/Zhuhai/Hong Kong/Guangdong service context; not Macao count.

## 3. Hyperscaler Presence

Verified result from official region pages checked on 2026-08-12: no AWS, Azure, Google Cloud, Oracle OCI, Alibaba Cloud, Tencent Cloud, or Huawei Cloud public cloud region named Macao/Macau was found.

Important nuance:
- Tencent lists `港澳台地区（中国香港）` / Hong Kong (`ap-hongkong`) on its CVM region page; this is not a Macao region.
- Alibaba lists China (Hong Kong), Shenzhen, Guangzhou, Heyuan and other nearby regions, not Macao.
- Neighbouring cloud regions can explain service paths and disaster-recovery choices, but cannot be counted as Macao physical facilities.

```text
"Macau" OR "Macao" site:docs.aws.amazon.com/global-infrastructure
"Macau" OR "Macao" site:learn.microsoft.com/en-us/azure/reliability/regions-list
"Macau" OR "Macao" site:cloud.google.com/about/locations
"Macau" OR "Macao" site:docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm
"Macau" OR "Macao" site:alibabacloud.com/en/global-locations
"澳门" OR "澳門" site:cloud.tencent.com/document/product/213/6091
"Macau" OR "Macao" site:huaweicloud.com/intl/en-us/about/global-infrastructure
```

## 4. Trade Press and Local Media

Use local media aggressively because English data-centre trade press has sparse Macao coverage.

Local B-grade sources:
- Macau Business: https://www.macaubusiness.com
- Macao News: https://www.macaonews.org
- Macau Daily Times: https://macaudailytimes.com.mo
- TDM: https://www.tdm.com.mo
- Macau Post Daily: https://www.macaupostdaily.com
- Plataforma: https://www.plataformamedia.com
- Hoje Macau: https://hojemacau.com.mo
- Ponto Final: verify current domain before use
- Macau Daily: https://www.macaodaily.com
- Exmoo: https://www.exmoo.com

Regional/international B-grade sources:
- DCD: https://www.datacenterdynamics.com
- Capacity Media, W.Media, SCMP, Reuters, Bloomberg, Mingtiandi

```text
site:macaubusiness.com "data centre" OR "data center" OR "centro de dados"
site:macaonews.org "data centre" OR "government cloud" OR "CTM"
site:macaudailytimes.com.mo "data centre" OR "CTM" "data centers"
site:tdm.com.mo "數據中心" OR "centro de dados"
site:plataformamedia.com "centro de dados" "Macau"
site:macaodaily.com "數據中心" OR "雲計算中心"
site:datacenterdynamics.com Macau OR Macao
"Chief Executive grants CTM rights to install data centers"
```

## 5. Interconnect, IXP, and Subsea

Macao has no verified major public cloud region and no known major public IXP equivalent to HKIX from checked sources. Treat interconnect as a lead layer only.

```text
"Macau" site:peeringdb.com
"Macau Internet Exchange" OR "Macao Internet Exchange" OR "MIX"
"澳門" "互聯網交換" OR "IX"
site:submarinenetworks.com Macau OR Macao
"澳門" "跨境光纜" OR "海纜"
"CTM" "Hong Kong Data Centre" "Macau"
```

Rules:
- IXP, CDN, POP, edge node, and subsea cable landing facts are not data-centre facilities unless separate facility evidence exists.
- Hong Kong or Zhuhai connectivity supports service-path notes only.

## 6. Aggregator Directories

Use only for leads:
- DataCenterMap Macau: https://www.datacentermap.com/macau/
- CTM Taipa directory lead: https://www.datacentermap.com/macau/taipa/ctm-data-center/
- Baxtel: https://baxtel.com
- Cloudscene: https://cloudscene.com
- datacenters.com: https://www.datacenters.com/locations/macau
- Inflect CTM lead: https://inflect.com

Directory workflow:
1. Capture facility name, operator, address, coordinates, aliases.
2. Search CTM/operator, CTT authorization, Gazette, and reliable media for the same name/address.
3. Keep directory-only address/capacity/status as C and exclude from final count until upgraded.

```text
site:datacentermap.com/macau "CTM" OR "Macau"
site:baxtel.com Macau "data center"
site:cloudscene.com Macau "data centre"
site:datacenters.com/locations/macau "Macau"
site:inflect.com "CTM Macau" "data center"
```

## 7. Per-Division Enumeration Matrix

| Area | Expected leads | Best sources | Counting note |
| --- | --- | --- | --- |
| Macau Peninsula | Government data centre/cloud, CTM/corporate telecom, finance IT | SAFP, CTT, CTM, Gazette, media | Count only facility-level evidence; government cloud separate from public colocation |
| Taipa | CTM/data-centre address leads, telecom nodes, hospitality/airport IT | CTM, CTT, DataCenterMap/Inflect leads | Directory addresses remain C until CTM/official corroboration |
| Cotai | Casino-resort internal IT rooms, CCTV/EGM systems | concessionaire filings, DICJ, reliable gaming media | Separate `casino_internal_it`; not public colocation |
| Coloane | Power context, low-density DR/industrial leads | CEM, Gazette, media | CEM power assets are not data centres |
| New Reclamation | future planning/land | Gazette, DSSCU/DSOP | Pipeline only |
| Hengqin/Zhuhai | adjacent DR/colo serving Macao | CN operator/media/directories | Mark CN jurisdiction; exclude from Macao counts |

## 8. Known Industry / Operator Evidence

| Subject | Evidence | Grade | Action |
| --- | --- | --- | --- |
| CTM public data-centre authorization | CTT notice and telecom regulation list | A | Primary public-DC seed |
| CTM Data Centre / Cloud | CTM business pages | A | Confirm services; seek address/capacity/status |
| CTM Hong Kong Data Centre | CTM page | A | Record as HK-adjacent service, not Macao facility |
| SAFP cloud/data centre | SAFP maintenance/procurement pages | A | Track as government infrastructure |
| DICJ EGM standards | DICJ standards and gov.mo machine approval | A | Demand/regulatory evidence |
| Casino concessionaires | HKEX/SEC filings | A | Property/IT/cyber evidence; not public DC by default |
| DataCenterMap CTM Taipa | directory page | C | Address lead to corroborate |
| Hyperscaler Macao absence | official region pages | A | Record absence in checked pages |
| Hengqin/Zhuhai leads | media/directories/operator pages | C/B/A by source | Store cross-border only |

## 9. Re-Check Cadence

- **Monthly:** CTT regulations/news, CTM product/news pages, SAFP tenders, Gazette search, DICJ notices, local media.
- **Quarterly:** cloud-region pages, HKEX/SEC filings, CEM annual/report updates, GPDP/AMCM decisions, directory leads.
- **Event-driven:** data-centre authorization, CTM facility announcement, government cloud expansion, casino IT/cyber disclosure, Hengqin/Zhuhai facility marketed to Macao customers.
- **Annually:** full bilingual/trilingual query rerun, media-domain refresh, entity-name refresh.

## 10. Red Flags

- `Macau` in a sales territory or support page is not a cloud region.
- CTT authorization is necessary evidence for third-party data centres, but not proof of buildout or capacity.
- Casino IT demand is real but must not be inflated into public colocation supply.
- Hong Kong/Hengqin/Zhuhai facilities must not be mixed into `division="Macao"` counts.
- Public tenders and awards are milestone facts, not operational status.
- Aggregator totals are discovery aids, never validated totals.

## 11. Expected Yield

Expected validated public/third-party data-centre supply in Macao is very small. Based on the verified 2024 CTT authorization notice, CTM is the core public-DC seed. Additional findings are more likely to be government cloud infrastructure, casino internal IT rooms, or adjacent Hong Kong/Hengqin/Zhuhai service paths than independent Macao colocation campuses.
