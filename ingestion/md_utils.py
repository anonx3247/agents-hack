from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from markitdown import MarkItDown
from pathlib import Path

class PDFLoader:
    def __init__(self, pdf_dir: str):
        self.pdf_dir = Path(pdf_dir)

    def load_pdfs(self) -> List[str]:
        pdf_files = [str(f) for f in self.pdf_dir.glob("*.pdf")]
        print(f"Found {len(pdf_files)} PDF(s) in {self.pdf_dir}")
        return pdf_files


class MarkdownConverter:
    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.md_converter = MarkItDown()

    def convert_pdf_to_markdown(self, pdf_path: str) -> str:
        print(f"Converting to markdown: {pdf_path}")
        output_path = self.output_dir / (Path(pdf_path).stem + ".md")
        with open(pdf_path, "rb") as f_pdf:
            result = self.md_converter.convert(f_pdf)
        with open(output_path, "w", encoding="utf-8") as f_out:
            f_out.write(result.text_content)
        print(f"Markdown saved to: {output_path}")
        return str(output_path)


class Chunker:
    def __init__(self, chunk_size=512, chunk_overlap=50):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def chunk_markdown(self, md_path: str):
        print(f"Splitting markdown into chunks: {md_path}")
        with open(md_path, "r", encoding="utf-8") as f:
            text = f.read()
        chunks = self.splitter.split_text(text)
        print(f"Generated {len(chunks)} chunk(s)")
        return chunks