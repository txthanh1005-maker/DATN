import sys
try:
    import fitz
    doc = fitz.open('D:/Latex/DATN/DATN.pdf')
    text = chr(10).join([page.get_text() for page in doc])
    print(f"Extracted {len(text)} chars using fitz.")
except Exception as e:
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader('D:/Latex/DATN/DATN.pdf')
        text = chr(10).join([page.extract_text() for page in reader.pages if page.extract_text()])
        print(f"Extracted {len(text)} chars using PyPDF2.")
    except Exception as e2:
        print(f"Error: {e}, {e2}")
        sys.exit(1)
        
with open('D:/Latex/DATN/DATN_text.txt', 'w', encoding='utf-8') as f:
    f.write(text)
