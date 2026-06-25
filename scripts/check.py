import re

with open('D:/Latex/DATN/chapters/chapter2.tex', 'r', encoding='utf-8') as f:
    text = f.read()

quotes = re.findall(r'["“”\']', text)
non_ascii = set(re.findall(r'[^\x00-\x7F]', text))

print("Quotes:", set(quotes))
print("Non-ASCII:", non_ascii)

# also check for textbf mid-sentence
lines = text.split('\n')
for i, line in enumerate(lines):
    if r'\textbf' in line:
        print(f"Line {i+1}: {line.strip()}")
