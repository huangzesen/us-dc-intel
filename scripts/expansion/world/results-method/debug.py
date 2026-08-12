import json
p = 'scripts/expansion/world/results-method/batch-185.jsonl'
raw = open(p, encoding='utf-8').read()
lines = raw.split('\n')
print('total physical lines:', len(lines))
for idx in (9, 10, 11, 12, 13, 14):
    l = lines[idx]
    print('--- physical line', idx + 1, 'len', len(l))
    try:
        json.loads(l)
        print('  OK')
    except Exception as e:
        print('  ERR:', e)
        # find suspicious chars
        for pos, ch in enumerate(l):
            if ord(ch) > 127 or ch in '\r\t':
                print('   char', pos, repr(ch), hex(ord(ch)))
                break
        print('   ctx:', repr(l[max(0, 440):470]))
