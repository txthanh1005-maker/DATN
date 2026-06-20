import re
import requests
import time
import urllib.parse
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def extract_cites(tex_path):
    with open(tex_path, 'r', encoding='utf-8') as f:
        content = f.read()
    cites = set()
    for match in re.finditer(r'\\cite\{([^}]+)\}', content):
        keys = [k.strip() for k in match.group(1).split(',')]
        cites.update(keys)
    return cites

def parse_bib(bib_path):
    with open(bib_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    entries = {}
    current_key = None
    current_entry = {}
    
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('@'):
            if current_key:
                entries[current_key] = current_entry
            match = re.search(r'@\w+\{([^,]+),', line)
            if match:
                current_key = match.group(1).strip()
                current_entry = {}
        elif current_key and '=' in line:
            parts = line.split('=', 1)
            key = parts[0].strip().lower()
            val = parts[1].strip()
            # Remove brackets and trailing comma
            val = re.sub(r'^[\{"]', '', val)
            val = re.sub(r'[\}",]+$', '', val)
            current_entry[key] = val
            
    if current_key:
        entries[current_key] = current_entry
        
    return entries

def check_openalex(entry):
    doi = entry.get('doi', '')
    title = entry.get('title', '')
    author = entry.get('author', '')
    year = entry.get('year', '')
    
    # Check DOI
    if doi:
        doi_clean = re.sub(r'^https?://(dx\.)?doi\.org/', '', doi)
        try:
            r = requests.get(f"https://api.openalex.org/works/doi:{doi_clean}", timeout=10)
            if r.status_code == 200:
                data = r.json()
                oa_title = data.get('title', '')
                if oa_title and similar(title, oa_title) > 0.7:
                    return {"status": "REAL", "reason": "DOI and title match"}
        except Exception:
            pass
            
    # Check title
    if title:
        try:
            enc_title = urllib.parse.quote(title)
            r = requests.get(f"https://api.openalex.org/works?filter=title.search:{enc_title}", timeout=10)
            if r.status_code == 200:
                data = r.json()
                results = data.get('results', [])
                if results:
                    best_match = results[0]
                    oa_title = best_match.get('title', '')
                    if oa_title and similar(title, oa_title) > 0.7:
                        # Check year roughly
                        oa_year = best_match.get('publication_year')
                        if str(year) == str(oa_year):
                            return {"status": "REAL", "reason": "Title and year match"}
                        else:
                            return {"status": "PARTIAL", "reason": f"Title matches but year differs (Bib: {year}, OA: {oa_year})"}
        except Exception:
            pass

    return {"status": "HALLUCINATION", "reason": "Not found by DOI or Title"}

def main():
    tex_path = r"D:\Latex\DATN\chapters\chapter1.tex"
    bib_path = r"D:\Latex\DATN\references.bib"
    
    cites = extract_cites(tex_path)
    print(f"Found {len(cites)} citations in chapter1.tex")
    
    bib_entries = parse_bib(bib_path)
    
    hallucinations = []
    
    for i, cite_key in enumerate(cites):
        print(f"[{i+1}/{len(cites)}] Checking {cite_key}...", end=" ")
        if cite_key not in bib_entries:
            print("NOT IN BIB!")
            hallucinations.append({"key": cite_key, "entry": {"title": "MISSING IN BIB"}, "reason": "Not found in references.bib"})
            continue
            
        entry = bib_entries[cite_key]
        
        # Fast fail for obvious fakes
        if entry.get('author', '').lower() == 'various':
            print("HALLUCINATION (Author='Various')")
            hallucinations.append({"key": cite_key, "entry": entry, "reason": "Author is listed as 'Various'"})
            continue
            
        res = check_openalex(entry)
        print(res['status'])
        
        if res['status'] == "HALLUCINATION":
            hallucinations.append({"key": cite_key, "entry": entry, "reason": res['reason']})
        elif res['status'] == "PARTIAL":
            hallucinations.append({"key": cite_key, "entry": entry, "reason": res['reason']})
            
        time.sleep(0.1) # rate limit
        
    print("\n--- HALLUCINATIONS / MISMATCHES ---")
    for h in hallucinations:
        print(f"Key: {h['key']}")
        print(f"Title: {h['entry'].get('title', 'N/A')}")
        print(f"Author: {h['entry'].get('author', 'N/A')}")
        print(f"Year: {h['entry'].get('year', 'N/A')}")
        print(f"DOI: {h['entry'].get('doi', 'N/A')}")
        print(f"Reason: {h['reason']}")
        print("-" * 40)

if __name__ == "__main__":
    main()
