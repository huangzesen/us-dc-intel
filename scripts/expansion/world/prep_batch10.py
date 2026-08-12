import json, os, time

base = 'country-skills'
batch9 = ['AL','BJ','CG','GE','JO','LU','MA','MU','AM','LI','ML','OM','WS','CM','LS','LT','MZ','SB','SS','ZM']
print('=== batch9 review progress (mtime >= 2026-08-12 03:33Z = reviewed) ===')
done, todo = [], []
for c in sorted(batch9):
    p = os.path.join(base, c)
    files = ['explorer-official.md', 'explorer-industry.md']
    ok = all(os.path.exists(os.path.join(p, f)) for f in files)
    if not ok:
        todo.append((c, 'MISSING FILE'))
        continue
    mt = max(os.path.getmtime(os.path.join(p, f)) for f in files)
    reviewed = mt >= time.mktime((2026,8,12,3,33,0,0,0,0))
    (done if reviewed else todo).append((c, time.strftime('%H:%M', time.localtime(mt))))
print('REVIEWED (%d):' % len(done), ', '.join('%s@%s' % x for x in sorted(done)))
print('NOT REVIEWED (%d):' % len(todo), ', '.join('%s(%s)' % x for x in sorted(todo)))

print()
print('=== batch10 draft task generation ===')
manifest = [json.loads(l) for l in open('world-manifest.jsonl') if l.strip()]
batch10_codes = ['AT','BE','BD','PK','SG','QA','ZW','DK','IE','LK','KW','LB','CY','IS','BY','KG','MG','NE','SK','UG']
by_code = {m['country_code']: m for m in manifest}
tasks = []
for code in batch10_codes:
    m = by_code[code]
    tasks.append({
        'code': code,
        'name': m['country_name'],
        'subnational_type': m.get('subnational_type', ''),
        'divisions': m.get('divisions', []),
    })
with open('batch10_tasks.json', 'w') as f:
    json.dump(tasks, f, ensure_ascii=False, indent=1)
for t in tasks:
    print(t['code'], t['name'], '|', t['subnational_type'], '|', len(t['divisions']), 'divs')
