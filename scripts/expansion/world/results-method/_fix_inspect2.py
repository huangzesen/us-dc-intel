import json
p = '/Users/huangzesen/work/projects/us-dc-intel/scripts/expansion/world/results-method/batch-277.jsonl'
lines = open(p).read().splitlines()
for i in [10, 12, 13, 15]:
    line = lines[i]
    print('=== line', i+1, 'len', len(line))
    try:
        json.loads(line)
        print('  OK')
    except Exception as e:
        print('  ERR:', str(e)[:120])
        col = int(str(e).split('column ')[1].split(' ')[0]) if 'column' in str(e) else 0
        print('  ctx:', repr(line[max(0, col-80):col+40]))
