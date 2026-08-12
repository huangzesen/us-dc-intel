import sys, re, urllib.parse, urllib.request, xml.etree.ElementTree as ET
queries = sys.argv[1:]
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'
for q in queries:
    print('=== Q:', q, '===')
    url = 'https://www.bing.com/search?format=rss&count=20&mkt=zh-CN&setlang=zh-hans&ensearch=0&q=' + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    try:
        data = urllib.request.urlopen(req, timeout=20).read().decode('utf-8', 'ignore')
        root = ET.fromstring(data)
        for it in root.findall('.//item')[:20]:
            t = (it.findtext('title') or '').strip()
            l = (it.findtext('link') or '').strip()
            d = (it.findtext('description') or '')
            d = re.sub('<[^>]+>', ' ', d)[:300].strip()
            print('T:', t)
            print('L:', l)
            print('D:', d)
            print('---')
    except Exception as e:
        print('PARSE_FAIL', repr(e))
