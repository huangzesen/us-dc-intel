# TW · Country Anatomy

Datacenter-country knowledge layer for Taiwan (TW).

## Files

| Layer | File | Status |
| --- | --- | --- |
| Country-level skill | `SKILL.md` | present (merged from the two reviewed explorers; luna max review record appended to both explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| County/city division layer | `divisions/` — county/city/special municipality, 20 divisions | to be added later |

## Division layer (future)

Per `world-manifest.jsonl`, TW is modeled as **county/city/special municipality** with exactly **20 divisions**: Changhua, Chiayi, Hsinchu, Hualien, Yilan, Keelung, Kaohsiung, Kinmen, Lienchiang, Miaoli, Nantou, New Taipei, Penghu, Pingtung, Taoyuan, Tainan, Taipei, Taitung, Taichung, Yunlin. Model quirk: **Hsinchu** (新竹市＋新竹縣) and **Chiayi** (嘉義市＋嘉義縣) are each merged into a single division — keep district/second-level names as the search and address-resolution layer. Market concentration: northern Taiwan (Taipei, New Taipei, Taoyuan) plus hyperscaler siting (Changhua, Tainan, Yunlin, Miaoli); eastern counties and outlying islands are predominantly negative results (`no_projects`). When the division layer is built, create per-division files; keep the official cloud-region positive/negative semantics (Azure Taiwan positive; AWS/GCP/OCI absent) and the Google-datacenter ≠ Google-Cloud-region rule intact.
