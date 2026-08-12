# MP Explorer Industry — 北马里亚纳群岛数据中心盘点行业/供应商通道方法论

Date verified: 2026-08-12 ｜ Scope: Commonwealth of the Northern Mariana Islands (CNMI / MP, 北马里亚纳群岛联邦)

Manifest coverage: MP has one required division, **Northern Mariana Islands**. Saipan, Tinian, and Rota are municipality search buckets only. Industry findings must be normalized back to `division = "Northern Mariana Islands"`.

本文件用于 industry/vendor pass：运营商产品页、海缆/电信行业媒体、数据中心目录、建设商/供应商线索、云/CDN 官方缺席核查。行业线索必须回连到官方/一手证据后才能建档。

## 1. 行业结论 Industry Conclusion

截至 2026-08-12，CNMI 的可验证行业图景是 **telecom-first, data-center-light**：

- **DoCoMo Pacific** 有真实官方 `Data Center Colocation` 产品页（Grade A product evidence），并有 CNMI business support / Saipan office 信息；但该 colocation 页面未在可见文本中给出 CNMI facility address。不能仅凭产品页把 “DoCoMo Saipan data center” 升级为已验证设施。
- **IT&E / Micronesian Telecommunications Corp.** 是 CNMI BEAD subgrant 的官方受约方（BPD 页面显示 2026-05-13 agreement），也是 CNMI/Guam 运营商。公开搜索出现 Saipan data center 目录线索，但未发现足够的一手地址/设施页；按 C 级线索处理。
- **PTI Pacifica** / MICS 是已验证海缆/电信设施相关主体。FCC 2022 notice 说明 MICS 与 Atisa 覆盖 Saipan、Tinian、Rota、Guam；这证明 telecom infrastructure，不证明 commercial data center。
- **Atisa / MICS / Google Proa-TPU-Interlink** 是 CNMI 最重要的 digital infrastructure leads。它们应作为 cable landing / telecom gateway 处理，除非后续有 rack/power/colo/hosting 证据。
- 数据中心目录（Baxtel、Datacenters.com、ColoMap 等）列出 Saipan / DoCoMo / IT&E 相关设施，价值是 lead discovery；没有一手来源前只能 Grade C，不应直接计入 definitive inventory。
- 未发现 AWS/Azure/Google Cloud/Oracle OCI 在 CNMI 的 official region/local zone；Google 在 CNMI 的公开基础设施动作是 subsea cable connectivity，而非 cloud region。

## 2. 行业分级规则 Grading Rules

- **Grade A**：运营商官方设施/产品页、FCC/ICFS、BPD/BEAD、CUC、SAM/FPDS/USASpending、云服务商官方基础设施页、供应商正式新闻稿/PDF。
- **Grade B**：具名日期的本地/行业媒体，如 Marianas Variety、Saipan Tribune、Guam Daily Post、Pacific Daily News、KUAM、Pacific Island Times、RNZ Pacific、Submarine Networks、TeleGeography、Data Center Dynamics、Capacity Media。
- **Grade C**：Baxtel、Datacenters.com、DataCenterMap、Cloudscene、ColoMap、WHTop、PeeringDB/BGP 目录、LinkedIn、社交媒体、招聘、论坛、SEO 主机目录。

降级规则：`communications facility`、`gateway`、`central office`、`landing station`、`server room`、`IT room`、`fiber internet`、`5G`、`business support office` 都不是数据中心语言。只有 `colocation`、`hosting`、`data center/datacenter`、`racks/cabinets`、`power/cooling/security for customer equipment` 等可触发数据中心候选。

## 3. 运营商与供应商线索 Operator & Vendor Leads

### 3.1 DoCoMo Pacific

Verified URLs:

- Main site: `https://www.docomopacific.com/`
- Business colocation product: `https://business.docomopacific.com/data-center-colocation`
- Business support / CNMI contact: `https://business.docomopacific.com/support`
- Atisa FCC-license release: `https://aboutus.docomopacific.com/144040-docomo-pacific-announces-grant-of-fcc-license-for-atisa-cable-system/`
- CNMI expansion context: `https://aboutus.docomopacific.com/248902-docomo-pacific-celebrates-its-expansion-of-cnmi-call-center/`

处理原则：

- DoCoMo colocation product is Grade A that the company offers colocation, with security language such as 24/7 staffing, fencing, mantrap, cameras, and keycard scanners.
- The same page does not prove a CNMI facility location. The support page lists Guam and Saipan business-service locations, but an office/contact location is not a data center.
- Any `DoCoMo Saipan` directory listing must be treated as Grade C until matched to a DoCoMo official address, FCC/ICFS filing, local permit, contract, or credible dated media report.

查询模板：

```text
site:business.docomopacific.com "Saipan" "data center" OR colocation OR cabinets OR racks
site:docomopacific.com "Saipan" "colocation" OR "data center"
"DoCoMo Saipan" "data center" OR colocation -Baxtel -Datacenters.com
"DOCOMO PACIFIC" "Middle Road" "data center" OR colocation
"DOCOMO PACIFIC" "ATISA" "Rota" "Tinian" "landing station"
```

### 3.2 IT&E / Micronesian Telecommunications Corp.

Verified URLs / leads:

- IT&E online shop: `https://shop.ite.net/`（search-verified; direct fetch may time out; retail/service presence only, not DC evidence）
- IT&E newsroom: `https://ite.pr.co/`（verified; confirms Guam/Northern Mariana Islands service footprint and current telecom announcements）
- IT&E managed IT services page: `https://shop.ite.net/business/managed-it-services/`（search-verified; useful lead for meet-me / transport language, but not standalone DC evidence）
- Customer portal / support references under `ite.net` and `itehq.net`（operational presence only）
- CNMI BPD BEAD documents: `https://bpd.cnmi.gov/about-us/b-e-a-d-documents/`（BPD states BEAD Subgrant Agreement with Micronesian Telecommunications Corp. dba IT&E executed 2026-05-13）

处理原则：

- IT&E is a high-priority lead because BPD names it in the BEAD subgrant and because directories claim Saipan data-center/colo presence.
- Do not classify IT&E Saipan as `commercial_colocation` unless an IT&E official page, contract, permit, or strong local reporting confirms facility address and colocation/hosting/rack service.
- BEAD fiber deployment may create central offices, splice huts, cabinets, and network rooms; these remain telecom/FTTP assets unless customer colocation or data-center use is explicit.

查询模板：

```text
site:ite.net OR site:shop.ite.net "data center" OR colocation OR hosting OR cloud
"IT&E" "Saipan" "data center" OR colocation OR cabinets OR racks
"Micronesian Telecommunications Corp" "BEAD" "CNMI" "subgrant"
site:bpd.cnmi.gov "IT&E" "Subgrant Agreement"
"IT&E" "Tekken Street" "Susupe" "data center" -Datacenters.com -Inflect
```

### 3.3 PTI Pacifica / MICS

Verified URLs / leads:

- FCC DA-22-762 MICS regulatory classification notice: `https://docs.fcc.gov/public/attachments/DA-22-762A1.pdf`
- FCC DA-97-522 Mariana-Guam Cable landing license: `https://docs.fcc.gov/public/attachments/DA-97-522A1.pdf`

处理原则：

- PTI/MICS is a confirmed cable/telecom infrastructure lead across Saipan, Tinian, Rota, Guam.
- A Guam-side PTI/affiliate data center or cable landing station is upstream context only and must not be counted in MP.
- Treat enterprise/government/private-carrier services over MICS as telecom services unless a facility is named with data center/colo language.

查询模板：

```text
"PTI Pacifica" CNMI OR Saipan OR Tinian OR Rota "data center" OR colocation
"PTI Pacifica" "MICS" "Saipan" "Tinian" "Rota"
site:fcc.gov "PTI Pacifica" "MICS" "Northern Mariana Islands"
"Mariana-Guam Cable" "data center" OR "landing station"
```

### 3.4 Subsea Cable Vendors / Future Connectivity

Verified URLs:

- NEC ATISA completion: `https://www.nec.com/en/press/201706/global_20170622_01.html`
- Google Cloud Pacific Connect / Proa / TPU: `https://cloud.google.com/blog/products/infrastructure/pacific-connect-initiative-to-expand`
- Governor coverage of Google fiber-optic cable: `https://governor.cnmi.gov/news/stronggoogles-fiber-optic-cable-will-help-attract-new-investments-industries-strong/`
- CNMI BPD Google Pacific Connect page: `https://bpd.cnmi.gov/google-pacific-connect-initiative-proa-tpu-interlink/`

处理原则：

- Atisa/MICS are operational telecom cable systems; Proa/TPU/Interlink are planned or in-progress international cable leads and must be rechecked in FCC/ICFS before final facility status.
- Cable landing does not equal data center. Classify as `operational_telecom` or `planned_telecom` unless sources explicitly describe customer colocation/hosting at the landing station.

查询模板：

```text
site:cloud.google.com/blog "Proa" "CNMI" "TPU" "Interlink"
site:governor.cnmi.gov "Google" "Proa" OR "Pacific Connect"
site:bpd.cnmi.gov "Proa" OR "TPU" OR "Interlink"
site:fcc.gov "Proa" "Northern Mariana Islands" "cable landing"
site:nec.com ATISA CNMI Guam "completed"
```

### 3.5 Satellite / Wireless Access

Starlink, Viasat, Kacific, fixed wireless, mobile broadband, BRS/PCS/LTE/5G towers, and microwave sites are connectivity infrastructure only. Use FCC ULS/ASR and provider availability pages to understand coverage, but do not count them as data centers.

```text
"Starlink" "Northern Mariana Islands" OR Saipan
"Viasat" CNMI OR Saipan
site:fcc.gov "Northern Mariana Islands" "earth station" OR "microwave"
```

## 4. Cloud / CDN Absence Check

Official pages to recheck before each extraction:

- AWS: `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/`
- AWS docs: `https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html`
- Azure: `https://learn.microsoft.com/en-us/azure/reliability/regions-list`
- Google Cloud: `https://cloud.google.com/about/locations`
- Oracle OCI: `https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm`
- Cloudflare: `https://www.cloudflare.com/network/`
- Akamai: `https://www.akamai.com/locations`

当前结论：无 CNMI official cloud region/local zone/edge PoP。Oracle hospitality/service-region style pages may map Northern Mariana Islands to an existing foreign region for application hosting; that is not evidence of an OCI region in MP.

## 5. Trade Press & Directories

Useful Grade B sources:

- Marianas Variety: `https://www.mvariety.com/`
- Saipan Tribune: `https://www.saipantribune.com/`
- Pacific Daily News: `https://www.guampdn.com/`
- Guam Daily Post: `https://www.postguam.com/`
- KUAM: `https://www.kuam.com/`
- Pacific Island Times: `https://www.pacificislandtimes.com/`
- RNZ Pacific: `https://www.rnz.co.nz/international/pacific-news`
- Submarine Networks: `https://www.submarinenetworks.com/`
- TeleGeography: `https://www2.telegeography.com/`
- Data Center Dynamics: `https://www.datacenterdynamics.com/`
- Capacity Media: `https://www.capacitymedia.com/`

Useful Grade C lead sources:

- Baxtel: `https://baxtel.com/data-center/saipan`
- Datacenters.com: `https://www.datacenters.com/locations/northern-mariana-islands`
- DataCenterMap: `https://www.datacentermap.com/`
- Cloudscene: `https://cloudscene.com/`
- ColoMap: `https://colomap.com/datacenters/country/mp/`
- WHTop country directory: `https://www.whtop.com/directory/country/mp`
- PeeringDB: `https://www.peeringdb.com/`
- ARIN: `https://www.arin.net/`

目录处理：

- Baxtel lists `DoCoMo Saipan` and `IT&E Saipan`; Datacenters.com / ColoMap surface similar market entries. These are leads, not final proof.
- If a directory gives a street address, power, racks, square footage, or operator, verify against official operator pages, FCC filings, building permits, procurement records, or direct local media before using.
- Absence from directories is only a weak negative signal.

行业查询模板：

```text
"Northern Mariana Islands" "data center" OR datacenter OR colocation -casino -hotel
"Saipan" "data center" OR colocation OR "server hosting" -casino -hotel
site:mvariety.com "data center" OR "colocation" OR "server room" OR "broadband"
site:saipantribune.com "data center" OR "colocation" OR "IT&E" OR "DOCOMO"
site:kuam.com CNMI "data center" OR "submarine cable" OR "Google"
site:pacificislandtimes.com CNMI "data center" OR "subsea cable" OR "Proa"
site:datacenterdynamics.com "Northern Mariana Islands" OR Saipan OR CNMI
site:capacitymedia.com CNMI OR Saipan OR "Proa"
```

## 6. Enumeration Matrix

| Candidate type | Source path | Minimum evidence | Classification |
|---|---|---|---|
| Commercial colocation | Operator official page -> local permit/contract/media -> directory | Facility address plus colocation/rack/power/cooling/customer equipment language | `commercial_colocation` only after A/B corroboration |
| Operator data center product | DoCoMo/IT&E/PTI official product pages | Product language alone proves product, not CNMI facility | `planned_telecom_colocation` or lead until address proven |
| Cable landing station | FCC/ICFS, operator release, NEC/Google official, Submarine Networks | Landing point on Saipan/Tinian/Rota and operator/licensee | `operational_telecom` or `planned_telecom` |
| Central office / POP | FCC ULS/BDC, operator pages, local reports | Site or service area evidence | `operational_telecom`; not DC |
| Government/institutional DC | BPD/gov/RFP/OPA/SAM/FPDS | Explicit data center/server room/DR/hosting plus location | `government_related_dc` |
| Cloud region / CDN PoP | AWS/Azure/GCP/OCI/Cloudflare/Akamai official network pages | Official region/PoP listing naming CNMI | `hyperscale_region` / `cdn_edge` if present; currently absent |
| Satellite gateway | FCC ULS/earth-station filings, provider official pages | Earth station/gateway location | `operational_telecom`; not DC |

## 7. Per-Municipality Workflow

| Municipality bucket | Industry expectation | Search path | Record guidance |
|---|---|---|---|
| Saipan 塞班 | Highest likelihood: operator offices/POP, cable landing/gateway, possible directory-listed colo leads | DoCoMo/IT&E pages; FCC cable/ULS; BPD/BEAD; local media; CUC Saipan power | Keep as single manifest division. Record Saipan in notes/location fields. Upgrade only with A/B location evidence. |
| Tinian 天宁 | Cable/telecom access; possible landing station; very low DC probability | FCC cable/ULS; DoCoMo Atisa; CUC Tinian; SAM/FPDS Tinian | Default `telecom_only` / `no_projects` unless explicit facility evidence appears. |
| Rota 罗塔 | Cable/telecom access; very low DC probability | FCC cable/ULS; DoCoMo Atisa; CUC Rota; SAM/FPDS Rota | Default `telecom_only` / `no_projects` unless explicit facility evidence appears. |

市镇扫描模板：

```text
"{Municipality}" "Northern Mariana Islands" "data center" OR datacenter OR colocation OR "server hosting" -casino -hotel
"{Municipality}" "IT&E" OR "DoCoMo Pacific" OR "PTI Pacifica" "landing station" OR "central office"
"{Municipality}" "Atisa" OR "MICS" OR "submarine cable"
"{Municipality}" RFP OR tender OR procurement "server room" OR "data center"
```

## 8. Watch List

Rerun before final extraction:

```text
"Saipan" "data center" OR colocation OR "first data center" -casino
"DoCoMo Saipan" "data center" OR colocation
"IT&E Saipan" "data center" OR colocation
site:business.docomopacific.com "Saipan" colocation OR "data center"
site:ite.net "Saipan" colocation OR "data center"
site:bpd.cnmi.gov "IT&E" "subgrant" "middle mile"
site:fcc.gov "Proa" "CNMI" "cable landing"
site:governor.cnmi.gov "Google" "cable landing" "Saipan"
```

If a future source names a facility, require: operator, exact island/municipality, facility type, operational/planned status, and at least one A/B corroborating source before counting.
