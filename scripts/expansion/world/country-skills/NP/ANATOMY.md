# NP · Country Anatomy

Datacenter-country knowledge layer for Nepal (NP).

## Files

| File | Status | Notes |
| --- | --- | --- |
| Country-level skill `SKILL.md` | Present | Merged from the two reviewed explorers (official/regulatory/cloud pipeline + industry/trade-press discovery) |
| Official / regulatory / cloud pipeline `explorer-official.md` | Present | Final-reviewed: DoIT directive + listed-provider roster, IDMC/GIDC + Hetauda DR, NTA, NTC, MoCIT, MoF/NPC budget, PPMO/e-GP procurement, OCR/IRD, NEA/ERC, IBN/DoI/SEZ, NRB, cloud-region absence checks |
| Industry / trade press / vendor discovery `explorer-industry.md` | Present | Final-reviewed: operator pages (Ncell, DataHub, Cloud Himalaya, NTC, WorldLink, Vianet), DCD/NepaliTelecom/ICT Frame/TechSansar/local press, NPIX/PeeringDB/PCH, directories, multilingual search vocabulary |
| Province division layer `divisions/` | To be added later | NP is manifest type `province` with divisions `["-"]` — a single country-level placeholder; the 7 provinces (Koshi, Madhesh, Bagmati, Gandaki, Lumbini, Karnali, Sudurpashchim) are the internal coverage checklist, not rows |

## Division layer (future)

Per world-manifest.jsonl, NP is modeled as **province** with divisions **`["-"]`** (single country-level division placeholder; no province-level rows). A valid enumeration run must produce one country-level output division `-` while demonstrating that all **7 provinces** were swept: Koshi (Biratnagar, Dharan, Itahari, Birtamod/Jhapa, Damak), Madhesh (Birgunj, Janakpur, Rajbiraj, Gaur), Bagmati (Kathmandu, Lalitpur/Nakkhu, Bhaktapur, Hetauda, Bharatpur/Chitwan, Banepa/Kavre, Chandragiri/Syuchatar), Gandaki (Pokhara, Kaski), Lumbini (Butwal/Tilottama, Bhairahawa/Siddharthanagar, Nepalgunj/Kohalpur, Palpa), Karnali (Birendranagar/Surkhet, Jumla), and Sudurpashchim (Dhangadhi, Mahendranagar, Attariya). When the division layer is built, create a single `divisions/-/` slot (or store `division="-"` plus province/city/address per record) and keep the 7-province sweep as the documented coverage checklist.
