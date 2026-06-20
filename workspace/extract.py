import json
import urllib.request

file_path = r'C:\Users\Admin\.gemini\antigravity-cli\brain\45bd6bf1-9a8c-471e-b11b-3716b752a17c\.system_generated\steps\14\content.md'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

json_str = ''
for line in lines:
    if line.startswith('{'):
        json_str = line
        break

data = json.loads(json_str)
count = 0
for w in data.get('results', []):
    title = w.get('title')
    doi = w.get('doi')
    if doi and count < 3:
        author_str = ' and '.join([a['author']['display_name'] for a in w.get('authorships', [])])
        year = w.get('publication_year', '')
        journal = w.get('primary_location', {}).get('source', {}).get('display_name', '')
        vol = w.get('biblio', {}).get('volume', '')
        issue = w.get('biblio', {}).get('issue', '')
        pages = f"{w.get('biblio', {}).get('first_page', '')}-{w.get('biblio', {}).get('last_page', '')}"
        
        # generate a citation key
        first_author = w.get('authorships', [])[0]['author']['display_name'].split()[-1] if w.get('authorships') else 'Unknown'
        cit_key = f"{first_author}{year}"
        
        print(f'@article{{{cit_key},')
        print(f'  title={{{title}}},')
        print(f'  author={{{author_str}}},')
        print(f'  journal={{{journal}}},')
        print(f'  volume={{{vol}}},')
        if issue:
            print(f'  number={{{issue}}},')
        print(f'  pages={{{pages}}},')
        print(f'  year={{{year}}},')
        print(f'  doi={{{doi.replace("https://doi.org/", "")}}}')
        print('}\n')
        count += 1
