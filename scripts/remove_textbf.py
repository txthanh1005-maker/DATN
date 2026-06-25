import re
import os

files_to_check = [f'chapters/chapter{i}.tex' for i in range(1, 6)]

total_replaced = 0

for file in files_to_check:
    filepath = os.path.join(r'D:\Latex\DATN', file)
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    replaced_in_file = 0
    
    for line in lines:
        def replacer(match):
            global total_replaced, replaced_in_file
            full_match = match.group(0)
            inner_text = match.group(1)
            start_pos = match.start()
            prefix = line[:start_pos]
            
            p_strip = prefix.strip()
            if p_strip == '':
                return full_match
            if p_strip.endswith(r'\item') or p_strip.endswith(r'\item['):
                return full_match
            if p_strip.endswith('&') or p_strip.endswith(r'\\'):
                return full_match
            if r'\multicolumn' in prefix or r'\section' in prefix or r'\caption' in prefix or r'\chapter' in prefix:
                return full_match
            if 'Table' in p_strip or 'Figure' in p_strip:
                return full_match
                
            # If we get here, it's likely middle of sentence
            print(f"Removed in {file}: '{full_match}' after '{prefix[-20:]}'")
            return inner_text

        new_line = re.sub(r'\\textbf\{([^{}]+)\}', replacer, line)
        if new_line != line:
            replaced_in_file += line.count(r'\textbf') - new_line.count(r'\textbf')
            total_replaced += line.count(r'\textbf') - new_line.count(r'\textbf')
        new_lines.append(new_line)
        
    if replaced_in_file > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"--- {file}: replaced {replaced_in_file} instances.")

print(f"Total replaced across all chapters: {total_replaced}")
