import os
from pathlib import Path
from dotenv import load_dotenv
from .md_utils import PDFLoader, MarkdownConverter, Chunker
from .db_loader import VectorStoreLoader
import argparse

class Pipeline:
    def __init__(
        self,
        source_type: str,
        source_dir: str,
        md_dir: str,
        db_dir: str,
        embedding_model: str,
        chunk_size: int,
        chunk_overlap: int
    ):
        self.source_type = source_type
        self.source_dir = source_dir
        self.md_dir = md_dir
        self.loader = PDFLoader(source_dir) if source_type == "pdf" else None
        self.converter = MarkdownConverter(md_dir) if source_type == "pdf" else None
        self.chunker = Chunker(chunk_size, chunk_overlap)
        self.vectorstore = VectorStoreLoader(db_dir, embedding_model)

    def run(self):
        print("Starting RAG pipeline...")

        if self.source_type == "pdf":
            pdf_paths = self.loader.load_pdfs()
            md_paths = []
            for pdf_path in pdf_paths:
                md_path = self.converter.convert_pdf_to_markdown(pdf_path)
                md_paths.append(md_path)

            chunks = []
            for md_path in md_paths:
                chunks += self.chunker.chunk_markdown(md_path)
            collection_name = "pdfs"

        elif self.source_type == "class-notes":
            class_notes_dir = Path(self.source_dir) / "class-notes"
            md_paths = list(class_notes_dir.glob("*.md"))
            md_paths = [str(p) for p in md_paths]
            print(f"Found {len(md_paths)} markdown file(s) in {class_notes_dir}")

            chunks = []
            for md_path in md_paths:
                chunks += self.chunker.chunk_markdown_with_headers(md_path)
            collection_name = "class-notes"

        elif self.source_type == "exos":
            exos_md = Path(self.source_dir) / "exos.md"
            if not exos_md.exists():
                raise FileNotFoundError(f"Le fichier exos.md est introuvable dans {self.source_dir}")
            
            chunks = self.chunker.chunk_exercises(exos_md.read_text(encoding="utf-8"))
            collection_name = "exos"
        else:
            raise ValueError(f"Unknown source_type: {self.source_type}")

        self.vectorstore.add_documents(chunks, collection_name=collection_name)

        print("Ingestion completed.")

# python ./ingestion/ingest_pipeline.py --source [pdf|class-notes|exos]
if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(description="Run document ingestion pipeline.")
    parser.add_argument(
        "--source", 
        choices=["pdf", "class-notes", "exos"], 
        required=True, 
        help="Data source type: 'pdf' to extract from PDFs, 'class-notes' or 'exos' to use existing markdown files."
    )
    args = parser.parse_args()

    # Déterminer le dossier source
    source_type = args.source
    source_dir = os.getenv("PDF_DIR") if source_type == "pdf" else os.getenv("MARKDOWN_DIR")

    pipeline = Pipeline(
        source_type=source_type,
        source_dir=source_dir,
        md_dir=os.getenv("MARKDOWN_DIR"),
        db_dir=os.getenv("CHROMA_DB_DIR"),
        embedding_model=os.getenv("EMBEDDING_MODEL"),
        chunk_size=int(os.getenv("CHUNK_SIZE", 512)),
        chunk_overlap=int(os.getenv("CHUNK_OVERLAP", 50))
    )

    pipeline.run()
