import urllib.request
import json
import urllib.parse

queries = [
    "inverter reactive power compensation microgrid resilience",
    "analytical target cascading hierarchical convergence"
]

for q in queries:
    url = "https://api.openalex.org/works?search=" + urllib.parse.quote(q) + "&sort=relevance_score:desc&per-page=3"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            print(f"--- QUERY: {q} ---")
            for w in data.get('results', []):
                authors = ", ".join([a['author']['display_name'] for a in w.get('authorships', [])])
                print(f"Title: {w.get('title')}")
                print(f"Year: {w.get('publication_year')}")
                print(f"Authors: {authors}")
                print(f"DOI: {w.get('doi')}")
                print("-" * 20)
    except Exception as e:
        print(f"Error: {e}")
