---
description: Convert PDF files to Markdown using Docling
argument-hint: "<pdf-path> [--output <output-path>]"
---

# /pdf-to-md - Convert PDF to Markdown

Convert PDF documents to clean Markdown format using the Docling library.

## Usage

```
/pdf-to-md <pdf-path> [--output <output-path>]
```

**Arguments:**
- `<pdf-path>` - Path to a PDF file or directory containing PDFs
- `--output <output-path>` - (Optional) Custom output path for the Markdown file

## Workflow

### 1. Validate Input

- Verify the provided path exists
- Determine if converting a single file or batch (directory)
- Check that Docling is installed

### 2. Check Dependencies

If Docling is not installed, prompt the user:

```bash
pip install docling
```

### 3. Convert

**Single file:**
1. Load the PDF using Docling's DocumentConverter
2. Export to Markdown format
3. Save to output path (default: same name with `.md` extension)

**Directory (batch mode):**
1. Find all `.pdf` files in the directory
2. Create `markdown_outputs/` subdirectory
3. Convert each PDF, saving with matching filename
4. Report successes and failures

### 4. Report Results

- Confirm output location
- Report page count
- For batch: Provide conversion summary

## Examples

**Convert a single PDF:**
```
/pdf-to-md /path/to/report.pdf
```
Creates `/path/to/report.md`

**Convert with custom output:**
```
/pdf-to-md /path/to/report.pdf --output /docs/converted-report.md
```

**Batch convert all PDFs in a folder:**
```
/pdf-to-md /path/to/papers/
```
Creates `/path/to/papers/markdown_outputs/` with all converted files.

## Tips

- Docling preserves document structure (headings, lists, tables) in the output
- First conversion may be slower as Docling loads its ML models
- For large batches, conversions run sequentially to manage memory
- If a file fails in batch mode, other files still process
