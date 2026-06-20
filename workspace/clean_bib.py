import re

keep_keys = {
    'Liu2022', 'Botelho2022', 'Feng2025', 'Samende2022', 'Ullah2021', 'Feng2022',
    'Patari2021', 'Pareek2020', 'Aboshady2023', 'Helou2021', 'Saidi2021', 'Xu2021',
    'Hashmi2020', 'Amir2023', 'Polat2025', 'Gao2022', 'Roald2022', 'Mahdavi2021',
    'Fobes2020', 'Etedadi2021', 'Srivastava2023', 'Yuan2023', 'Chen2021', 'Liu2025',
    'Zhang2024', 'Riedel2024', 'Zuo2022', 'Yuan2022', 'Zhao2022', 'Sun2024',
    'Chen2025', 'BASARAN2026', 'Ullah2022', 'Nasiri2023', 'Zhang2020', 'Xia2024',
    'Zhu2024', 'Mishra2024', 'Muhtadi2021', 'Dagar2021', 'Ahmad2023', 'She2022',
    'Trivedi2022', 'Choudhury2022', 'Victoria2021', 'Karami2021', 'Ali2022',
    'Park2024', 'Antonopoulos2020', 'Zia2020', 'Gholami2021', 'Mansourlakouraj2021',
    'Najafi2025'
}

with open(r'D:\Latex\DATN\references.bib', 'r', encoding='utf-8') as f:
    content = f.read()

entries = []
current_entry = []
current_key = None
brace_level = 0

for line in content.splitlines():
    match = re.match(r'^@\w+\{([^,]+),', line)
    if match and brace_level == 0:
        current_key = match.group(1).strip()
        current_entry = [line]
        brace_level += line.count('{') - line.count('}')
    elif current_key is not None:
        current_entry.append(line)
        brace_level += line.count('{') - line.count('}')
        if brace_level == 0:
            entries.append((current_key, '\n'.join(current_entry)))
            current_key = None
            current_entry = []

with open(r'D:\Latex\DATN\references.bib', 'w', encoding='utf-8') as f:
    for key, text in entries:
        if key in keep_keys:
            f.write(text + '\n\n')

print(f"Filtered references. Kept {sum(1 for k,t in entries if k in keep_keys)} out of {len(entries)} entries.")
