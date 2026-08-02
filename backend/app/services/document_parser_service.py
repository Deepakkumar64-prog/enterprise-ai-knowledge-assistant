from docx import Document
from pypdf import PdfReader


class DocumentParserService:

    @staticmethod
    def parse_docx(file_path: str) -> str:
        doc = Document(file_path)

        text = []

        for paragraph in doc.paragraphs:
            text.append(paragraph.text)

        return "\n".join(text)

    @staticmethod
    def parse_pdf(file_path: str) -> str:
        reader = PdfReader(file_path)

        text = []

        for page in reader.pages:
            text.append(page.extract_text() or "")

        return "\n".join(text)