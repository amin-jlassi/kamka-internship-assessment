import pdfplumber

"""Metadata = """

class PDFParser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_text(self) -> str:
        """Text extraction without page metadata."""
        with pdfplumber.open(self.file_path) as pdf:
            pages = []
            for page in pdf.pages:
                text = page.extract_text()
                if text:  
                    pages.append(text)
        return "\n".join(pages)

    def extract_text_with_metadata(self) -> list[dict]:
        """
        Returns text per page with page number 
        output: [{"text": "...", "page_number": 1}, ...]
        """
        pages = []
        with pdfplumber.open(self.file_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    pages.append({
                        "text": text,
                        "page_number": i + 1
                    })
        return pages