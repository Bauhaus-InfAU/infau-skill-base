#!/usr/bin/env python3
"""
Convert PDF to Markdown using Docling

Usage:
    python pdf_to_markdown.py <input_path> [output_path]

Arguments:
    input_path   Path to a PDF file or directory containing PDFs
    output_path  (Optional) Output path for markdown file or directory

Examples:
    python pdf_to_markdown.py report.pdf
    python pdf_to_markdown.py report.pdf output.md
    python pdf_to_markdown.py ./papers/
    python pdf_to_markdown.py ./papers/ ./converted/
"""

import os
import sys
import warnings
from pathlib import Path

# Disable HuggingFace hub symlink warnings on Windows
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'
warnings.filterwarnings('ignore')


def convert_pdf_to_markdown(pdf_path, output_path=None):
    """Convert a single PDF file to Markdown using Docling.

    Args:
        pdf_path: Path to the input PDF file.
        output_path: Path for the output Markdown file.
                     Defaults to same name with .md extension.

    Returns:
        Output path on success, None on failure.
    """
    from docling.document_converter import DocumentConverter

    pdf_path = Path(pdf_path)
    if output_path is None:
        output_path = pdf_path.with_suffix('.md')
    else:
        output_path = Path(output_path)

    print(f"Converting {pdf_path.name}...")
    converter = DocumentConverter()
    result = converter.convert(str(pdf_path))
    markdown_content = result.document.export_to_markdown()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown_content, encoding='utf-8')

    print(f"  -> {output_path} ({len(result.document.pages)} pages)")
    return str(output_path)


def convert_directory(input_dir, output_dir=None):
    """Convert all PDFs in a directory to Markdown.

    Args:
        input_dir: Directory containing PDF files.
        output_dir: Output directory for markdown files.
                    Defaults to input_dir/markdown_outputs/.

    Returns:
        Tuple of (successful, failed) file name lists.
    """
    input_dir = Path(input_dir)
    if output_dir is None:
        output_dir = input_dir / 'markdown_outputs'
    else:
        output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_files = sorted(input_dir.glob('*.pdf'))
    if not pdf_files:
        print(f"No PDF files found in {input_dir}")
        return [], []

    print(f"Found {len(pdf_files)} PDF(s) in {input_dir}\n")

    successful, failed = [], []
    for pdf_file in pdf_files:
        output_path = output_dir / f"{pdf_file.stem}.md"
        try:
            convert_pdf_to_markdown(pdf_file, output_path)
            successful.append(pdf_file.name)
        except Exception as e:
            print(f"  FAILED: {e}")
            failed.append(pdf_file.name)

    print(f"\nDone: {len(successful)} converted, {len(failed)} failed")
    if failed:
        for name in failed:
            print(f"  FAILED: {name}")
    return successful, failed


def main():
    if len(sys.argv) < 2:
        print("Usage: pdf_to_markdown.py <input_path> [output_path]")
        print("  input_path   PDF file or directory of PDFs")
        print("  output_path  (Optional) output .md file or directory")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    if not input_path.exists():
        print(f"Error: {input_path} not found")
        sys.exit(1)

    try:
        if input_path.is_dir():
            convert_directory(input_path, output_path)
        elif input_path.suffix.lower() == '.pdf':
            convert_pdf_to_markdown(input_path, output_path)
        else:
            print(f"Error: {input_path} is not a PDF file or directory")
            sys.exit(1)
    except ImportError:
        print("Error: Docling is not installed. Run: pip install docling")
        sys.exit(1)


if __name__ == "__main__":
    main()
