from typing import List, Tuple
from langchain.text_splitter import RecursiveCharacterTextSplitter
from markitdown import MarkItDown
from pathlib import Path
import re

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
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def chunk_markdown(self, md_path: str) -> List[str]:
        """Chunk basique avec découpe uniforme par longueur"""
        print(f"Splitting markdown into chunks: {md_path}")
        with open(md_path, "r", encoding="utf-8") as f:
            text = f.read()
        chunks = self.splitter.split_text(text)
        print(f"{len(chunks)} chunk(s)")
        return chunks

    def chunk_exercises(self, content: str) -> List[str]:
        """Chunk par exercice avec reconnaissance des balises [Exercice n]{.smallcaps}"""
        pattern = r"(\[Exercice\s+\d+\]\{\.smallcaps\}.*?)((?=\[Exercice\s+\d+\]\{\.smallcaps\})|$)"
        matches = re.findall(pattern, content, re.DOTALL)
        return [match[0].strip() for match in matches]

    def _flush_chunk(self, headers: List[Tuple[int, str]], lines: List[str], chunks: List[str]):
        if lines:
            header_prefix = "\n".join(f"{'#' * level} {text}" for level, text in headers)
            body = "\n".join(lines)
            full_text = header_prefix + "\n" + body if header_prefix else body
            chunks.append(full_text.strip())

    def _match_header(self, line: str) -> Tuple[int, str] | None:
        match = re.match(r"^(#{1,6})\s+(.*)", line)
        if match:
            return len(match.group(1)), match.group(2).strip()
        return None

    def chunk_markdown_with_headers(self, md_path: str, max_chars: int = 5000) -> List[str]:
        """Chunk markdown en respectant la hiérarchie des headers pour chaque chunk."""
        print(f"Splitting markdown with header context: {md_path}")
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        lines = content.splitlines()
        chunks = []
        current_headers: List[Tuple[int, str]] = []
        current_chunk_lines: List[str] = []

        for line in lines:
            header = self._match_header(line)
            if header:
                if current_chunk_lines:
                    self._flush_chunk(current_headers, current_chunk_lines, chunks)
                    current_chunk_lines = []
                level, text = header
                current_headers = [(l, t) for l, t in current_headers if l < level]
                current_headers.append((level, text))
                current_chunk_lines.append(line)
            else:
                current_chunk_lines.append(line)
                temp_chunk = "\n".join(f"{'#' * level} {text}" for level, text in current_headers)
                temp_chunk += "\n" + "\n".join(current_chunk_lines)
                if len(temp_chunk) > max_chars:
                    if len(current_chunk_lines) > 1:
                        current_chunk_lines.pop()
                        self._flush_chunk(current_headers, current_chunk_lines, chunks)
                        current_chunk_lines = [line]
                    else:
                        self._flush_chunk(current_headers, current_chunk_lines, chunks)
                        current_chunk_lines = [line]

        self._flush_chunk(current_headers, current_chunk_lines, chunks)
        print(f"{len(chunks)} chunk(s) with header context")
        return chunks