import urllib.request
import urllib.parse
import json

def search(query, limit=5):
    url = f"https://api.crossref.org/works?query={urllib.parse.quote(query)}&filter=from-pub-date:2020&select=DOI,title,author,published-print,published-online,container-title&rows={limit}"
    req = urllib.request.Request(url, headers={'User-Agent': 'mailto:test@example.com'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data['message']['items']
    except Exception as e:
        print(f"Error: {e}")
        return []

print("=== ARGUMENT 1: Failure of Static Optimization ===")
items = search("day-ahead optimization static microgrid extreme events failure resilience", limit=8)
for i in items:
    title = i.get('title', [''])[0]
    authors = ", ".join([a.get('family', '') + " " + a.get('given', '') for a in i.get('author', [])])
    year = i.get('published-print', i.get('published-online', {})).get('date-parts', [[None]])[0][0]
    venue = i.get('container-title', [''])[0]
    print(f"- {title} ({year}) | {venue} | {authors} | DOI: {i.get('DOI')}")

print("\n=== ARGUMENT 2: MPC Rolling Horizon for Resilience ===")
items = search("Model Predictive Control rolling horizon microgrid resilience extreme events", limit=8)
for i in items:
    title = i.get('title', [''])[0]
    authors = ", ".join([a.get('family', '') + " " + a.get('given', '') for a in i.get('author', [])])
    year = i.get('published-print', i.get('published-online', {})).get('date-parts', [[None]])[0][0]
    venue = i.get('container-title', [''])[0]
    print(f"- {title} ({year}) | {venue} | {authors} | DOI: {i.get('DOI')}")
