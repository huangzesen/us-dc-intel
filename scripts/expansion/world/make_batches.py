#!/usr/bin/env python3
"""Generate world exploration batches from world-manifest.jsonl.

Chunk each country's first-level admin divisions into groups of ~10 divisions.
Tiny countries/territories (<=5 divisions) stay as one whole-country batch.
The Americas coverage is skipped dynamically from the Americas manifest.

Outputs:
  scripts/expansion/world/batches/<batch>.jsonl - one JSON object per batch
"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
EXPANSION_DIR = os.path.dirname(BASE)
MANIFEST = os.path.join(BASE, "world-manifest.jsonl")
AMERICAS_MANIFEST = os.path.join(EXPANSION_DIR, "americas", "americas-manifest.jsonl")
BATCH_DIR = os.path.join(BASE, "batches")
os.makedirs(BATCH_DIR, exist_ok=True)

CHUNK = 10


def read_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


WORLD_SKIP = {row["country_code"] for row in read_jsonl(AMERICAS_MANIFEST)}
SKIP_COUNTRIES = {"US"} | WORLD_SKIP

rows = read_jsonl(MANIFEST)
batches = []
for row in sorted(rows, key=lambda item: item["country_code"]):
    country_code = row["country_code"]
    if country_code in SKIP_COUNTRIES:
        continue
    divisions = row["divisions"]
    if len(divisions) <= 5:
        batches.append(
            {
                "country_code": country_code,
                "country_name": row["country_name"],
                "divisions": divisions,
            }
        )
    else:
        for i in range(0, len(divisions), CHUNK):
            batches.append(
                {
                    "country_code": country_code,
                    "country_name": row["country_name"],
                    "divisions": divisions[i : i + CHUNK],
                }
            )

for i, batch in enumerate(batches):
    with open(os.path.join(BATCH_DIR, f"batch-{i:03d}.jsonl"), "w", encoding="utf-8") as f:
        f.write(json.dumps(batch, ensure_ascii=False, separators=(",", ":")) + "\n")

print(f"batches: {len(batches)}")
print(f"divisions covered: {sum(len(batch['divisions']) for batch in batches)}")
print("batch dir: scripts/expansion/world/batches")
