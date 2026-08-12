# GRIDWATCH Data-Audit — Consolidated Findings (world expansion)

Generated: 2026-08-12 · Read-only aggregation of `audit-results/shard-*.jsonl` (30 files). No shard file and no DB row was modified.

## 1. Totals

| Metric | Value |
|---|---|---|
| Shard files read (`shard-0..29.jsonl`) | **30** (4 empty: shard-0, shard-23, shard-24, shard-29; 26 non-empty) |
| Finding rows (MISLOCATED + UNSURE lines) | **59** |
| **MISLOCATED** | **14** |
| **UNSURE** | **45** |
| Facilities checked | 409 — the **only** recorded per-shard count (shard-1 trailer `CHECKED=409 MISLOCATED=0 UNSURE=4`). The other 29 shards did not emit a `CHECKED=` trailer, so a total checked number is not derivable from these outputs. |

### Per-shard breakdown

| Shard | Records | MISLOCATED | UNSURE | Trailer |
|---|---|---|---|---|
| shard-0 | 0 | 0 | 0 | — |
| shard-1 | 4 | 0 | 4 | CHECKED=409 MISLOCATED=0 UNSURE=4 |
| shard-2 | 2 | 0 | 2 | — |
| shard-3 | 1 | 0 | 1 | — |
| shard-4 | 3 | 0 | 3 | — |
| shard-5 | 1 | 0 | 1 | — |
| shard-6 | 1 | 1 | 0 | — |
| shard-7 | 2 | 1 | 1 | — |
| shard-8 | 4 | 1 | 3 | — |
| shard-9 | 2 | 1 | 1 | — |
| shard-10 | 1 | 0 | 1 | — |
| shard-11 | 2 | 0 | 2 | — |
| shard-12 | 5 | 2 | 3 | — |
| shard-13 | 2 | 0 | 2 | — |
| shard-14 | 6 | 0 | 6 | — |
| shard-15 | 2 | 1 | 1 | — |
| shard-16 | 2 | 2 | 0 | — |
| shard-17 | 2 | 2 | 0 | — |
| shard-18 | 2 | 1 | 1 | — |
| shard-19 | 2 | 0 | 2 | — |
| shard-20 | 5 | 0 | 5 | — |
| shard-21 | 2 | 1 | 1 | — |
| shard-22 | 2 | 1 | 1 | — |
| shard-23 | 0 | 0 | 0 | — |
| shard-24 | 0 | 0 | 0 | — |
| shard-25 | 1 | 0 | 1 | — |
| shard-26 | 1 | 0 | 1 | — |
| shard-27 | 1 | 0 | 1 | — |
| shard-28 | 1 | 0 | 1 | — |
| shard-29 | 0 | 0 | 0 | — |
| **Total** | **59** | **14** | **45** | |

Field-name notes (defensive read): verdict keys varied (`verdict`, `judgment`, `judgement`, `classification`, `status`); country keys varied (`country_declared`, `declared_country`, `country`); actual-location keys varied (`actual_country`, `correct_country`, `country_should_be`, `real_location`). Records in shard-1/shard-2 carry no verdict key; their notes/trailer identify them as UNSURE.

---

## 2. Findings by issue category

### A. NL vs Dutch Caribbean (Curaçao / Sint Maarten / Aruba) — 7 facilities, ALL MISLOCATED
Declared `NL` (Netherlands proper) but physically in Kingdom-of-the-Netherlands Caribbean constituent countries with their own ISO codes. Root cause: `world:batch:Curaçao` / `world:batch:Sint Maarten` / Aruba batches coded NL.

| Facility | Declared → Actual | Confidence |
|---|---|---|
| SETAR Colocation Datacenter (rowid 12642, shard-12) | NL → **AW** (Oranjestad, Aruba) | high |
| Blue NAP Americas (rowid 12646, shard-16) | NL → **CW** (Willemstad, Curaçao) | high |
| Blue NAP Americas / Willemstad (rowid 22576, shard-16; duplicate of 12646) | NL → **CW** | high |
| CORE Datacenter (rowid 12647, shard-17; twin rowid 3080 already coded CW) | NL → **CW** (Willemstad) | n/a (high per evidence) |
| E-Commerce Park N.V. data center (rowid 12648, shard-18; twin rowid 3079 already coded CW) | NL → **CW** (Willemstad) | n/a |
| OCIX Sint Maarten (rowid 12681, shard-21) | NL → **SX** (Philipsburg, Sint Maarten) | n/a |
| OCIX / Open Caribbean Internet Exchange (rowid 22612, shard-22; duplicate of 12681) | NL → **SX** (Philipsburg) | n/a |

### B. US vs Puerto Rico (PR) — 12 facilities (4 MISLOCATED, 8 UNSURE)
Declared `US` (country DEFAULT artifact of the `county:county-explore` pipeline) while located in Puerto Rico; DB's own convention codes PR facilities as `PR` (25 rows). US is a US territory so US is not geographically absurd → audit split between MISLOCATED (convention violation) and UNSURE.

**MISLOCATED (recommend PR):**
| Facility | Declared → Actual | Confidence |
|---|---|---|
| HUB939 (rowid 1626, shard-6) — Humacao | US → **PR** | n/a (severity low) |
| Seabase Puerto Rico subsea AI hub eval – Ponce (rowid 1628, shard-8) | US → **PR** | n/a |
| Data@ccess San Juan / San Juan II / Santurce (rowid 1629, shard-9; twin 3323 already PR) | US → **PR** | n/a |
| Critical Hub DataCenter (rowid 1632, shard-12; twin 3317 already PR) | US → **PR** | high |

**UNSURE (same pattern, flagged for harmonization):**
| Facility | Declared → Actual | Confidence |
|---|---|---|
| Neptuno Data Center (rowid 1622, shard-2) — Guaynabo | US → PR | high |
| Carter Validus Mission Critical REIT PR (rowid 1624, shard-4; twin 3311 already PR) | US → PR | high |
| Claro (PR) (id 1625, shard-5; twin 3310 already PR) | US → PR | n/a |
| Data@ccess Ponce secondary colocation (id 1627, shard-7) | US → PR | n/a |
| EdgeUno SJU1 San Juan (id 1630, shard-10) | US → PR | n/a |
| Netwave Data Center (rowid 1631, shard-11) — San Juan | US → PR | n/a |
| Municipality of San Juan Health Data Center Project (rowid 1634, shard-14) | US → PR | n/a |
| Municipality of San Juan Municipal Tower DC Project (rowid 1635, shard-15) | US → PR | n/a |

### C. CN vs Hong Kong (HK SAR) — 11 facilities (2 MISLOCATED, 9 UNSURE)
Declared `CN` from the `cn-gov:Hong Kong` batch; physically in Hong Kong SAR. CN is not geographically wrong (SAR of China), but the DB codes Hong Kong as `HK` elsewhere (45 rows HK vs 18 rows CN/Hong Kong).

**MISLOCATED (recommend HK):**
| Facility | Declared → Actual | Confidence |
|---|---|---|
| SUNeVision iAdvantage MEGA Plus (rowid 23625, shard-15; twin 21534 already HK) — Tseung Kwan O | CN → **HK** | n/a |
| AirTrunk HKG2 擴建 35MW (rowid 23627, shard-17; twin 11131 already HK) — Tsuen Wan | CN → **HK** | n/a |

**UNSURE (same pattern, harmonization needed):**
| Facility | Declared → Actual | Confidence |
|---|---|---|
| coverage:香港·監管與行業管線 (rowid 23642, shard-2) — coverage marker, not a physical facility | CN → HK | high |
| Equinix HK6 IBX (rowid 23628, shard-18; twin 11125 already HK) | CN → HK | n/a |
| Equinix HK2 IBX (rowid 23629, shard-19) — Kwai Chung | CN → HK | n/a |
| Global Switch Hong Kong (rowid 23630, shard-20) — Tseung Kwan O | CN → HK | n/a |
| Goodman Group 荃灣數據中心 50MW (rowid 23631, shard-21) | CN → HK | n/a |
| Angelo Gordon 屯門數據中心 20MW (rowid 23632, shard-22; twin 21562 already HK) | CN → HK | n/a |
| GDS Hong Kong #2 葵涌 (id 23636, shard-26) | CN → HK | n/a |
| HKT SkyExchange 數據中心組合 (rowid 23637, shard-27; sister 21544 already HK) | CN → HK | n/a |
| 中國移動 沙田火炭數據中心 Sha Tin Lot 613 (rowid 23638, shard-28) | CN → HK | n/a |

### D. CN vs Macau (MO SAR) — 1 facility, UNSURE
| Facility | Declared → Actual | Confidence |
|---|---|---|
| 澳門電訊 CTM 數據中心 WEST IDC (shard-1) — Macau SAR | CN → CN (ISO code for Macau is **MO**; DB codes HK as HK but stores Macau as CN) | high |

### E. External territory vs sovereign-state coding (Christmas Island CX → AU) — 2 facilities, UNSURE
CX is the correct ISO code for the territory; would be AU if the country field encodes the sovereign state.
| Facility | Declared → Actual | Confidence |
|---|---|---|
| Google Christmas Island connectivity hub / reported AI data centre (shard-1) | CX → **AU** (Christmas Island, Australian external territory) | medium |
| Google AI data centre / data hub, reported lead (shard-1) | CX → AU | low |

### F. Disputed / contested territories — 7 facilities, ALL UNSURE (sovereignty-stance coding)
| Facility | Declared → Actual | Confidence |
|---|---|---|
| Igoudar Dakhla Green Data Center (shard-1) — Dakhla, Western Sahara (ISO EH), Morocco-administered; declared MA matches universal attribution | MA → MA/EH (disputed territory, not a geographic mislocation) | medium |
| Igoudar Numerique / Igoudar Dakhla green campus (id 10405, shard-25) — coded EH/Western Sahara while DB's other Dakhla rows (12361, 22368) are MA/Dakhla-Oued Ed-Dahab | EH → **MA** (per DB convention) | n/a |
| IPKO Data Center (rowid 22954, shard-4) — Fushe Kosove/Pristina | RS → **XK** (de facto Kosovo) | high |
| IPKO Data Center (rowid 13032, shard-12) — Kosovo Polje/Pristina | RS → XK | medium |
| Telecom of Kosovo Core Telecom / IT DC (rowid 13033, shard-13) — Pristina | RS → XK | n/a |
| Miranda-Media telecom infrastructure, Sevastopol (rowid 23381, shard-11) — de jure UA, de facto RU | UA → UA (de jure) / RU (de facto) | n/a |
| Abkhazia cryptocurrency mining technopark (rowid 11044, shard-4) — de jure GE | GE → GE (de jure; no change if convention = international recognition) | medium |

### G. Column-shifted / garbled rows — 2 facilities (1 MISLOCATED, 1 UNSURE)
| Facility | Declared → Actual | Confidence |
|---|---|---|
| KIO XAL (id 3247, shard-7) — country column holds `'1 Xalapa'` (place name); column shift pushed city into country field; real: Xalapa, Veracruz, Mexico | `1 Xalapa` → **MX** (recode country=MX, subnational=Veracruz, owner=KIO Data Centers, city=Xalapa) | n/a |
| Reliance Industries (rowid 1454, shard-14) — contaminated record: canonical name is Indian conglomerate (Mumbai), developer is Pioneer Telephone Coop (Kingfisher, OK); grid operator listed as El Paso Electric (TX); unverifiable without original tracker record | US (OK) → US or IN — **cannot resolve; needs original-record follow-up** | n/a |

### H. Subnational-only issues (country code correct) — 16 facilities, ALL UNSURE
Country field is right; subnational is wrong/mistranslated. No country change needed.
| Facility | Declared → Actual (subnational fix) | Confidence |
|---|---|---|
| KIWI NETWORKS Villa Vicente Guerrero (rowid 3243, shard-3) | MX → MX (Tabasco → **Puebla**) | n/a |
| MTGREEN Zero-Carbon Datacenter, Sabroso de Aguiar (rowid 12938, shard-8) | PT → PT ('Royal Town' → **Vila Real**) | n/a |
| Tus Data Center Mashhad (rowid 11678, shard-8) | IR → IR ('Central Khorasan' → **Razavi Khorasan**) | n/a |
| Asiatech Mashhad IDC (rowid 11679, shard-9) | IR → IR ('Central Khorasan' → **Razavi Khorasan**) | n/a |
| Telecom Egypt Regional Data Hub Smart Village (rowid 10388, shard-8) | EG → EG (Cairo → **Giza**) | n/a |
| Konza National Data Center (rowid 11922, shard-12) | KE → KE (Kajiado boundary caveat → **Machakos/Makueni** optional) | medium |
| Konza National Data Centre (rowid 22064, shard-14) | KE → KE (Kajiado boundary caveat) | n/a |
| Konza National Data Centre (rowid 11930, shard-20) | KE → KE (Makueni → **Machakos**) | n/a |
| Bitfury Norway data center, Mo Industripark (rowid 12703, shard-13) | NO → NO ('Northland' → **Nordland**) | n/a |
| Arctic Circle Data Center, Mo i Rana (rowid 12704, shard-14) | NO → NO ('Northland' → **Nordland**) | n/a |
| atNorth SWE04 Sollefteå (rowid 23114, shard-14) | SE → SE ('Western Northland' → **Västernorrland**) | n/a |
| Covilha Data Center Campus (rowid 12914, shard-14) | PT → PT ('White Castle' → **Castelo Branco**) | n/a |
| Covilha Data Center Campus, Asterion/Altice (rowid 22849, shard-19) | PT → PT ('White Castle' → **Castelo Branco**) | n/a |
| ODATA DC QR04 (rowid 3200, shard-20) | MX → MX (Guanajuato → **Querétaro**) | n/a |
| Kyberna Balzers Data Center (rowid 12260, shard-20) | LI → LI (Vaduz HQ → **Balzers**) | n/a |
| Netia Dzialoszyce data center (rowid 12890, shard-20) | PL → PL ('Holy Cross' → **Świętokrzyskie**) | n/a |

### I. Region-level / multi-country record — 1 facility, UNSURE
| Facility | Declared → Actual | Confidence |
|---|---|---|
| Microsoft Azure East Africa region — Kenya & Tanzania (rowid 13632, shard-12) — announced region spans KE (Nairobi) + TZ (Dar es Salaam); TZ correct only if row = Tanzanian leg | TZ → TZ or region-level KE+TZ (granularity decision) | low |

---

## 3. Recommended fix plan

**No DB write may happen without human/Jason approval.** These are proposals; a reviewer should validate each recode against the evidence URLs in the shard files before applying.

### Root causes to fix at the source (config/pipeline)
1. **`country DEFAULT 'US'`** in the `county:county-explore` (americas) pipeline caused the whole US-vs-PR class (cat. B, 12 rows). Replace the default with an ISO-validated lookup; require state=PR rows to default to country=PR (or add a territory-code mapping US-territories → their ISO codes).
2. **`cn-gov:Hong Kong` batch** hard-codes country=CN for Hong Kong rows (cat. C, 11 rows). Change the batch to emit HK (DB convention), or map subnational='Hong Kong' → country=HK at ingest.
3. **`world:batch:Curaçao` / `Sint Maarten` / Aruba batches** emit NL (cat. A, 7 rows). Map these subnationals to CW/SX/AW.
4. **Macau convention** (cat. D): decide CN vs MO once, consistently with HK=HK (ISO). Currently 1 flagged row; audit the wider Macau set.
5. **Sovereignty policy** (cat. F): document de-jure vs de-facto convention (Kosovo RS-vs-XK, Sevastopol UA-vs-RU, Abkhazia GE, Western Sahara MA-vs-EH) and apply uniformly; today rows disagree with each other (e.g. Dakhla coded both MA and EH).
6. **Validation rule**: country must be a valid ISO 3166-1 alpha-2; subnational must be consistent with country (catches column-shift rows like KIO XAL and the 'Northland'/'White Castle'/etc. translation artifacts, cat. G/H).

### Proposed SQL (illustrative; run only after approval)
```sql
-- A. Dutch Caribbean: NL -> AW/CW/SX
UPDATE centers SET country='AW' WHERE rowid=12642;              -- SETAR (Aruba)
UPDATE centers SET country='CW' WHERE rowid IN (12646,22576,12647,12648); -- Curaçao
UPDATE centers SET country='SX' WHERE rowid IN (12681,22612);  -- Sint Maarten

-- B. Puerto Rico: US -> PR (MISLOCATED set; UNSURE set after review)
UPDATE centers SET country='PR' WHERE rowid IN (1626,1628,1629,1632);
-- review then: 1622,1624,1625,1627,1630,1631,1634,1635

-- C. Hong Kong: CN -> HK (MISLOCATED set; UNSURE set after harmonization decision)
UPDATE centers SET country='HK' WHERE rowid IN (23625,23627);
-- review then (cn-gov batch): 23628,23629,23630,23631,23632,23636,23637,23638,23642

-- G. Garbled: KIO XAL row repair (country, subnational, owner, city)
UPDATE centers SET country='MX', subnational='Veracruz', owner='KIO Data Centers', city='Xalapa' WHERE rowid=3247;
-- rowid 1454 (Reliance Industries): DO NOT change until original tracker record is found

-- H. Subnational-only corrections (no country change) — 16 rows, as listed in section H
-- I. rowid 13632: decide region-vs-country granularity before editing

-- D/F (convention decisions): Macau MO vs CN; Kosovo XK vs RS (22954,13032,13033);
--   Sevastopol UA/RU (23381); Abkhazia GE (11044); Dakhla MA/EH (10405 + shard-1 Igoudar) —
--   require a documented sovereignty-policy decision first; single-row edits are premature.
```

### Duplicate-harmonization note
Several flagged rows duplicate already-correctly-coded rows (twins: 3311/1624, 3310/1625, 3317/1632, 3323/1629, 3080/12647, 3079/12648, 11131/23627, 11125/23628, 21534/23625, 21562/23632, 21544/23637, 12646/22576, 12681/22612). Dedupe policy should be agreed before bulk recoding.

---

*End of consolidated audit report. All source lines retained verbatim in the shard files; this file is the only artifact created by this aggregation.*
