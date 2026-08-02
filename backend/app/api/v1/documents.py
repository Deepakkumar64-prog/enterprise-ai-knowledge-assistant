from fastapi import APIRouter, UploadFile, File

from app.services.document_service import DocumentService
from app.services.document_parser_service import DocumentParserService
from app.services.chunking_service import ChunkingService
from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService

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

    if file.filename.lower().endswith(".docx"):
        extracted_text = DocumentParserService.parse_docx(
            file_path
        )

    elif file.filename.lower().endswith(".pdf"):
        extracted_text = DocumentParserService.parse_pdf(
            file_path
        )

    elif file.filename.lower().endswith(".txt"):
        extracted_text = DocumentParserService.parse_txt(
            file_path
        )

    chunks = ChunkingService.chunk_text(
        extracted_text
    )

    for index, chunk in enumerate(chunks):

        if not chunk.strip():
            continue

        embedding = EmbeddingService.generate_embedding(
            chunk
        )

        VectorService.store_chunk(
            chunk_id=f"{file.filename}_{index}",
            chunk_text=chunk,
            embedding=embedding
        )

    return {
        "success": True,
        "filename": file.filename,
        "content_type": file.content_type,
        "saved_to": file_path,
        "file_size_bytes": file_size,
        "text_length": len(extracted_text),
        "chunk_count": len(chunks),
        "sample_chunks": chunks[:3],
        "preview": extracted_text[:1000]
    }