set PATH=%PATH%;D:\Ungdung\Latex\installed\texlive\2025\bin\windows
bibtex DATN
pdflatex -interaction=nonstopmode DATN.tex
pdflatex -interaction=nonstopmode DATN.tex
