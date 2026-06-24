import os
import re

files = ["D:/Latex/DATN/chapters/chapter5.tex", "D:/Latex/DATN/chapters/chapter4.tex"]

for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Reverse the corrupted format: $t\=9\text{h}\$ to $t=9\text{h}$
    content = content.replace(r"$t\=", r"$t=")
    content = content.replace(r"\text{h}\$", r"\text{h}$")
    
    # Wait, what if it was $t\=9\text{h}, t\=10\text{h}\$?
    # The script did: r'\$t=\1\\text{h}, t=\2\\text{h}\$'
    # So it probably became $t\=9\text{h}, t\=10\text{h}\$
    
    # Just fix the specific corruptions:
    # \= to =
    content = content.replace(r"\=", "=")
    # \text{h}\$ to \text{h}$
    content = content.replace(r"\text{h}\$", r"\text{h}$")

    # Fix the original things properly if they were missed.
    # Actually, let's just use regex to fix:
    # Any \$ in math mode end should be $
    content = re.sub(r'\\text\{h\}\\\$', r'\\text{h}$', content)
    
    # Wait, earlier script replaced \$t=(\d+)\$ with \$t=\1\\text{h}\$
    # Since $t evaluated to nothing, it was \=(\d+)\$ -> \=\1\\text{h}\$
    # So "$t=9$" became "$t\=9\text{h}\$"
    # We just need to replace "t\=" with "t="
    content = content.replace(r"t\=", "t=")
    # And replace "\text{h}\$" with "\text{h}$"
    content = content.replace(r"\text{h}\$", r"\text{h}$")
    
    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

print("Fix completed.")
