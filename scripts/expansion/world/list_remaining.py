import json, os
manifest = [json.loads(l) for l in open('world-manifest.jsonl') if l.strip()]
have = set(os.listdir('country-skills/')) - {'brief.md'}
remaining = []
for m in manifest:
    code = m.get('country_code')
    name = m.get('country_name')
    if code and code not in have:
        remaining.append((code, name, m.get('subnational_type'), len(m.get('divisions', []))))
print('manifest total:', len(manifest))
print('have dirs:', len(have))
print('remaining:', len(remaining))
for c, n, t, d in sorted(remaining):
    print(c, n, '|', t, '|', d)
