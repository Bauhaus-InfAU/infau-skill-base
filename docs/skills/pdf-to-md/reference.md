# PDF to Markdown — Advanced Reference

This document covers advanced Docling configuration, export formats, and troubleshooting beyond the basics in SKILL.md.

## Pipeline Architecture

Docling processes PDFs through a multi-stage pipeline:

1. **PDF parsing** — Extracts raw page content (text, images, coordinates)
2. **Layout analysis** — ML model identifies document structure (headings, paragraphs, tables, figures)
3. **Table structure recognition** — Dedicated model reconstructs table rows/columns
4. **OCR** (optional) — Recognizes text in scanned pages or images
5. **Document assembly** — Combines results into a structured document model
6. **Export** — Converts to Markdown, JSON, or other formats

## Pipeline Configuration

### PdfPipelineOptions

The main configuration object for the PDF conversion pipeline:

```python
from docling.datamodel.pipeline_options import PdfPipelineOptions, TableFormerMode
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat

pipeline_options = PdfPipelineOptions()
```

### Table Detection Modes

```python
from docling.datamodel.pipeline_options import TableFormerMode

# Fast mode (default) — good for simple tables
pipeline_options.table_structure_options.mode = TableFormerMode.FAST

# Accurate mode — better for complex/borderless tables, slower
pipeline_options.table_structure_options.mode = TableFormerMode.ACCURATE
```

**When to use ACCURATE:**
- Tables without visible borders
- Merged cells or complex layouts
- Tables spanning multiple columns
- Financial or scientific data tables

### Full Pipeline Example

```python
from docling.datamodel.pipeline_options import PdfPipelineOptions, TableFormerMode
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat

pipeline_options = PdfPipelineOptions()
pipeline_options.table_structure_options.mode = TableFormerMode.ACCURATE
pipeline_options.do_ocr = True
pipeline_options.generate_picture_images = True

converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    }
)
result = converter.convert("document.pdf")
```

## OCR Configuration

### Enabling OCR

```python
pipeline_options = PdfPipelineOptions()
pipeline_options.do_ocr = True
```

### OCR Backends

Docling supports multiple OCR backends:

**EasyOCR** (default when OCR is enabled):
```python
from docling.datamodel.pipeline_options import EasyOcrOptions

pipeline_options.do_ocr = True
pipeline_options.ocr_options = EasyOcrOptions()
```

**Tesseract:**
```python
from docling.datamodel.pipeline_options import TesseractOcrOptions

pipeline_options.do_ocr = True
pipeline_options.ocr_options = TesseractOcrOptions()
```

**Language settings (EasyOCR):**
```python
ocr_options = EasyOcrOptions()
ocr_options.lang = ["en", "de"]  # English and German
pipeline_options.ocr_options = ocr_options
```

### When to Use OCR

| Document Type | OCR Needed? |
|--------------|-------------|
| Digital/native PDF | No — text is already extractable |
| Scanned document | Yes |
| Image-based PDF | Yes |
| Mixed (some pages scanned) | Yes — Docling only OCRs pages without text |

## Export Formats

### Markdown (primary)

```python
md = result.document.export_to_markdown()
```

### Document Tokens

Structured token representation useful for downstream NLP:

```python
tokens = result.document.export_to_document_tokens()
```

### Dictionary / JSON

Full structured representation of the document:

```python
doc_dict = result.document.export_to_dict()

import json
with open("document.json", "w") as f:
    json.dump(doc_dict, f, indent=2)
```

### Iterating Document Elements

Access individual document elements (paragraphs, tables, figures):

```python
for element, level in result.document.iterate_items():
    print(f"Level {level}: {type(element).__name__}")
    if hasattr(element, 'text'):
        print(f"  Text: {element.text[:100]}")
```

## Image Handling

### Extracting Embedded Images

```python
from pathlib import Path

pipeline_options = PdfPipelineOptions()
pipeline_options.generate_picture_images = True

converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    }
)
result = converter.convert("paper.pdf")

image_dir = Path("extracted_images")
image_dir.mkdir(exist_ok=True)

count = 0
for element, _level in result.document.iterate_items():
    if hasattr(element, 'image') and element.image is not None:
        img_path = image_dir / f"image_{count:03d}.png"
        element.image.pil_image.save(str(img_path))
        count += 1

print(f"Extracted {count} images")
```

## Advanced Features

### Converting URLs

Docling can convert web pages and remote PDFs directly:

```python
converter = DocumentConverter()
result = converter.convert("https://arxiv.org/pdf/2408.09869")
md = result.document.export_to_markdown()
```

### Chunking for RAG

Split documents into chunks suitable for retrieval-augmented generation:

```python
from docling.chunking import HybridChunker

converter = DocumentConverter()
result = converter.convert("paper.pdf")

chunker = HybridChunker()
chunks = list(chunker.chunk(result.document))

for i, chunk in enumerate(chunks):
    print(f"Chunk {i}: {chunk.text[:80]}...")
```

### Multiple Input Formats

Docling supports more than just PDF:

```python
from docling.datamodel.base_models import InputFormat

# Supported formats (check Docling docs for current list)
# InputFormat.PDF, InputFormat.DOCX, InputFormat.PPTX,
# InputFormat.HTML, InputFormat.IMAGE
```

### Converting Multiple Files Efficiently

Reuse the converter instance to avoid reloading models:

```python
from pathlib import Path

converter = DocumentConverter()  # Load models once

for pdf in Path("papers/").glob("*.pdf"):
    result = converter.convert(str(pdf))
    md = result.document.export_to_markdown()
    pdf.with_suffix(".md").write_text(md, encoding="utf-8")
```

## Performance Tips

### GPU Acceleration

Docling benefits significantly from GPU for layout analysis and table detection:

```bash
# Install PyTorch with CUDA support
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
pip install docling
```

### Model Caching

Models are downloaded on first use (~500 MB) and cached:
- **Linux/Mac:** `~/.cache/huggingface/hub/`
- **Windows:** `C:\Users\<user>\.cache\huggingface\hub\`

To pre-download models:
```python
from docling.document_converter import DocumentConverter
converter = DocumentConverter()  # Triggers download
```

### Memory Management

For large PDFs or batch operations:
- Process files sequentially (don't parallelize with threads)
- Delete converter and results between large files if memory is tight
- Monitor memory usage for PDFs over 100 pages

```python
import gc

for pdf in pdf_files:
    converter = DocumentConverter()
    result = converter.convert(str(pdf))
    md = result.document.export_to_markdown()
    Path(f"{pdf.stem}.md").write_text(md, encoding="utf-8")
    del result, converter
    gc.collect()
```

### Batch Processing Best Practices

```python
from pathlib import Path
from docling.document_converter import DocumentConverter

converter = DocumentConverter()  # Reuse for small-to-medium files

pdf_files = sorted(Path("input/").glob("*.pdf"))
print(f"Processing {len(pdf_files)} files...")

for i, pdf in enumerate(pdf_files, 1):
    try:
        result = converter.convert(str(pdf))
        md = result.document.export_to_markdown()
        Path(f"output/{pdf.stem}.md").write_text(md, encoding="utf-8")
        print(f"[{i}/{len(pdf_files)}] {pdf.name}")
    except Exception as e:
        print(f"[{i}/{len(pdf_files)}] FAILED {pdf.name}: {e}")
```

## Troubleshooting

### Model Download Issues

**Problem:** First run hangs or fails during model download.

**Solutions:**
- Check internet connection
- Set `HF_HOME` to a path with sufficient space
- Use a VPN if HuggingFace is blocked
- Pre-download: `huggingface-cli download ds4sd/docling-models`

### Out of Memory

**Problem:** `MemoryError` or process killed during conversion.

**Solutions:**
- Close other memory-intensive applications
- Process fewer files at a time
- Use `gc.collect()` between conversions
- For very large PDFs (100+ pages), consider splitting first

### Table Detection Quality

**Problem:** Tables are not properly recognized or structured.

**Solutions:**
- Switch to `TableFormerMode.ACCURATE`
- Ensure the PDF has sufficient resolution
- For borderless tables, ACCURATE mode is strongly recommended
- Check if the table is actually an image (may need OCR)

### OCR Quality Issues

**Problem:** OCR output is garbled or inaccurate.

**Solutions:**
- Use a higher-DPI source document
- Set the correct language: `ocr_options.lang = ["en", "de"]`
- Try a different OCR backend (EasyOCR vs Tesseract)
- For handwritten text, results will be limited

### Windows-Specific Issues

**Symlink warnings:**
```python
import os
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'
```

**Long path issues:** Enable long paths in Windows or use shorter output directories.

**Encoding errors:** Always specify `encoding='utf-8'` when writing files:
```python
Path("output.md").write_text(md, encoding="utf-8")
```

## Docling vs Other PDF Tools

| Feature | Docling | pdfplumber | pypdf | PyMuPDF |
|---------|---------|------------|-------|---------|
| Structured Markdown | Yes | No | No | No |
| Table detection (ML) | Yes | Rule-based | No | No |
| Layout analysis | Yes | No | No | Limited |
| OCR integration | Yes | No | No | Yes |
| Image extraction | Yes | Yes | Yes | Yes |
| Create/edit PDFs | No | No | Yes | Yes |
| Merge/split PDFs | No | No | Yes | Yes |
| License | MIT | MIT | BSD | AGPL |
| GPU acceleration | Yes | No | No | No |

**Use Docling when:** You need structured Markdown output with preserved headings, tables, and document hierarchy.

**Use other tools when:** You need to manipulate PDFs (merge, split, fill forms, create) — see the **pdf** skill.
