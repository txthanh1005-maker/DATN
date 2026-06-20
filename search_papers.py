import subprocess
import json
import urllib.parse
import time

def fetch_json(url):
    res = subprocess.run(["curl.exe", "-s", url], capture_output=True, text=True)
    if res.returncode == 0:
        return json.loads(res.stdout)
    return None

queries = [
    ("SO_HILP", "stochastic optimization microgrid \"extreme events\""),
    ("RO_LIMIT", "robust optimization microgrid conservatism intractable"),
    ("MPC_VOLL", "model predictive control microgrid load shedding voll")
]

for tag, q in queries:
    print(f"--- Searching for {tag} ---")
    query = urllib.parse.quote(q)
    url = f"https://api.openalex.org/works?search={query}&filter=publication_year:>2019&per-page=5"
    data = fetch_json(url)
    if data and data.get("results"):
        for res in data["results"]:
            title = res.get('title')
            year = res.get('publication_year')
            doi = res.get('doi')
            abstract_inv = res.get('abstract_inverted_index')
            has_abstract = "Yes" if abstract_inv else "No"
            print(f"[{year}] {title} | DOI: {doi} | Abstract: {has_abstract}")
    else:
        print("No results found or error.")
    time.sleep(1)
