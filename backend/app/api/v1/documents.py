from fastapi import APIRouter, UploadFile, File

from app.services.document_service import DocumentService
from app.services.document_parser_service import DocumentParserService

router = APIRouter()


@router.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()

    file_path = DocumentService.save_file(
        file.filename,
        content
    )

    file_size = DocumentService.get_file_size(file_path)

    extracted_text = ""

    if file.filename.endswith(".docx"):
        extracted_text = DocumentParserService.parse_docx(file_path)

    elif file.filename.endswith(".pdf"):
        extracted_text = DocumentParserService.parse_pdf(file_path)

    return {
        "success": True,
        "filename": file.filename,
        "content_type": file.content_type,
        "saved_to": file_path,
        "file_size_bytes": file_size,
        "preview": extracted_text[:1000]
    }