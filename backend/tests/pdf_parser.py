import sys
sys.path.append(".")
from app.utils.pdf_parser import PDFParser
text = PDFParser("uploads/liste_chaine.pdf").extract_text()
print(text)