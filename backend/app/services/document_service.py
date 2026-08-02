from pathlib import Path


class DocumentService:

    @staticmethod
    def save_file(file_name: str, content: bytes):
        upload_dir = Path("uploads")
        upload_dir.mkdir(exist_ok=True)

        file_path = upload_dir / file_name

        with open(file_path, "wb") as f:
            f.write(content)

        return str(file_path)

    @staticmethod
    def get_file_size(file_path: str):
        return Path(file_path).stat().st_size