# SD · Country Anatomy

Datacenter-country knowledge layer for Sudan (SD).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| State division layer | `divisions/` — 18 states | to be added later |

## Division layer (future)

- Enumeration granularity: 18 states. Only Khartoum and Red Sea have countable DC seeds; the other 16 states are negative/marginal unless a named state/NIC/operator facility appears. Priority tiers: 1) Khartoum (highest — Sudatel SDC/Sinkat St, NIC/NDC/state DC, SIXP lead, Canar Al-Mashtal, Zain/MTN core, EBS; war-status terms mandatory: RSF, occupation, Feb 2024 shutdown, rehabilitation, Oct 2025 reactivation); 2) Red Sea (Port Sudan — Sudatel second DC/SAS1, EASSy/SAS1/SAS2 landings, war-time government/telecom relocation hub); 3) Nile corridor (River Nile, Northern, Gezira, White Nile — marginal, state ICT/telecom exchanges); 4) East/Central (Kassala, Gedaref, Sennar, Blue Nile — war-affected/refugee corridors, humanitarian ICT only); 5) Kordofan & Darfur (North/South/West Kordofan; North/South/West/East/Central Darfur — active/legacy conflict zones, defensible negative sweeps only).
- Language pair per state: English (data centre/data center/datacentre) + Arabic (مركز بيانات / مركز البيانات الوطني / استضافة / خوادم / سحابة / التحول الرقمي) + state Arabic names (الخرطوم, بورتسودان, البحر الأحمر, نهر النيل, الجزيرة, النيل الأبيض, كسلا, القضارف, سنار, النيل الأزرق, كردفان, دارفور).
- Planned per-division files: `divisions/{state}.md` with official-route recipes (SUNA/MTDT/NIC/TPRA/state gov), operator sweeps per state capital, Arabic/English pivots, war-status date tracking, and sweep status.

## Cross-references

- Parent country folder: `country-skills/SD/` (SKILL.md, ANATOMY.md, explorer-official.md, explorer-industry.md).
- World manifest division names: Khartoum, Red Sea, River Nile, Northern, Gezira, White Nile, Kassala, Gedaref, Sennar, Blue Nile, North Kordofan, South Kordofan, West Kordofan, North Darfur, South Darfur, West Darfur, East Darfur, Central Darfur.
