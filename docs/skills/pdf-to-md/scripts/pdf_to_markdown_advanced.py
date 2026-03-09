#!/usr/bin/env python3
"""
Advanced PDF to Markdown conversion with Docling pipeline options.

Usage:
    python pdf_to_markdown_advanced.py <input_pdf> <output_md> [options]

Options:
    --with-images <dir>   Export embedded images to directory
    --ocr                 Enable OCR for scanned documents
    --accurate-tables     Use accurate (slower) table detection model

Examples:
    python pdf_to_markdown_advanced.py paper.pdf paper.md
    python pdf_to_markdown_advanced.py paper.pdf paper.md --with-images ./images
    python pdf_to_markdown_advanced.py scanned.pdf output.md --ocr
    python pdf_to_markdown_advanced.py report.pdf report.md --accurate-tables
"""

import os
import sys
import warnings
from pathlib import Path

os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'
warnings.filterwarnings('ignore')


def convert_advanced(input_pdf, output_md, image_dir=None, ocr=False, accurate_tables=False):
    """Convert PDF with advanced Docling pipeline options.

    Args:
        input_pdf: Path to input PDF.
        output_md: Path to output Markdown file.
        image_dir: If set, export images to this directory.
        ocr: Enable OCR pipeline for scanned documents.
        accurate_tables: Use TableFormerMode.ACCURATE (slower but better).
    """
    from docling.datamodel.pipeline_options import PdfPipelineOptions, TableFormerMode
    from docling.document_converter import DocumentConverter, PdfFormatOption
    from docling.datamodel.base_models import InputFormat

    pipeline_options = PdfPipelineOptions()

    # Table detection mode
    if accurate_tables:
        pipeline_options.table_structure_options.mode = TableFormerMode.ACCURATE
        print("Using accurate table detection (slower)")

    # OCR configuration
    if ocr:
        pipeline_options.do_ocr = True
        print("OCR enabled")

    # Image export
    if image_dir:
        from docling.datamodel.pipeline_options import ImageRefMode
        image_dir = Path(image_dir)
        image_dir.mkdir(parents=True, exist_ok=True)
        pipeline_options.generate_picture_images = True
        print(f"Images will be exported to {image_dir}")

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )

    input_pdf = Path(input_pdf)
    output_md = Path(output_md)

    print(f"Converting {input_pdf.name}...")
    result = converter.convert(str(input_pdf))

    # Export markdown
    markdown_content = result.document.export_to_markdown()

    # Export images if requested
    if image_dir:
        for element, _level in result.document.iterate_items():
            if hasattr(element, 'image') and element.image is not None:
                image_path = image_dir / f"{element.self_ref}.png"
                element.image.pil_image.save(str(image_path))

    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_md.write_text(markdown_content, encoding='utf-8')

    print(f"Output: {output_md} ({len(result.document.pages)} pages)")
    return str(output_md)


def main():
    if len(sys.argv) < 3:
        print("Usage: pdf_to_markdown_advanced.py <input_pdf> <output_md> [options]")
        print("Options: --with-images <dir>, --ocr, --accurate-tables")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_md = sys.argv[2]

    args = sys.argv[3:]
    image_dir = None
    ocr = False
    accurate_tables = False

    i = 0
    while i < len(args):
        if args[i] == '--with-images' and i + 1 < len(args):
            image_dir = args[i + 1]
            i += 2
        elif args[i] == '--ocr':
            ocr = True
            i += 1
        elif args[i] == '--accurate-tables':
            accurate_tables = True
            i += 1
        else:
            print(f"Unknown option: {args[i]}")
            sys.exit(1)

    if not Path(input_pdf).exists():
        print(f"Error: {input_pdf} not found")
        sys.exit(1)

    try:
        convert_advanced(input_pdf, output_md, image_dir, ocr, accurate_tables)
    except ImportError as e:
        print(f"Error: Missing dependency. Run: pip install docling")
        print(f"Details: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
