import urllib.request
import urllib.error
import os

dois = [
    "10.3390/app11020627",
    "10.1109/ias44978.2020.9334785",
    "10.1109/ojpel.2021.3056627",
    "10.35833/mpce.2019.000237",
    "10.1109/tsg.2022.3147370",
    "10.3390/en16134851"
]

bib_entries = []

for doi in dois:
    url = f"https://api.crossref.org/works/{doi}/transform/application/x-bibtex"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            bib_entries.append(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetching {doi}: {e}")

if bib_entries:
    with open(r"D:\Latex\DATN\references.bib", "a", encoding="utf-8") as f:
        f.write("\n\n" + "\n\n".join(bib_entries))
    print("Successfully appended BibTeX entries to references.bib")
else:
    print("No BibTeX entries fetched.")
