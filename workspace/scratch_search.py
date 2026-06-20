import urllib.request, urllib.parse, json

queries = [
    '"stochastic optimization" microgrid inaccurate probability distribution',
    '"robust optimization" microgrid conservative worst-case intractable'
]

results = []
for q in queries:
    url = f'https://api.crossref.org/works?query={urllib.parse.quote(q)}&filter=from-pub-date:2020-01-01,type:journal-article&select=DOI,title,author,published-print,published-online,container-title&rows=5'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'mailto:test@example.com'})
        resp = urllib.request.urlopen(req)
        data = json.loads(resp.read().decode('utf-8'))
        for item in data['message']['items']:
            results.append(item)
    except Exception as e:
        print('Error:', e)

for idx, r in enumerate(results):
    title = r.get('title', [''])[0]
    authors = ' and '.join([a.get('family', '') + ', ' + a.get('given', '') for a in r.get('author', [])])
    year = r.get('published-print', r.get('published-online', {})).get('date-parts', [[None]])[0][0]
    journal = r.get('container-title', [''])[0]
    doi = r.get('DOI', '')
    print(f'[{idx+1}] {title} | {authors} | {year} | {journal} | {doi}')
