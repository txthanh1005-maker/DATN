import os
f = r"D:\Latex\DATN\chapters\chapter4.tex"
with open(f, "r", encoding="utf-8") as file:
    content = file.read()
content = content.replace(r"t\=", "t=")
content = content.replace(r"\text{h}\$", r"\text{h}$")
with open(f, "w", encoding="utf-8") as file:
    file.write(content)
print("Fix applied to chapter4.tex")
