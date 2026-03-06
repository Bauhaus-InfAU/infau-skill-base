---
name: pdf-to-md
description: Converts PDF files to Markdown using the Docling library, supporting single-file and batch conversions
trigger: always
---

# PDF to Markdown Conversion Skill

## Purpose

Convert PDF documents to clean Markdown format using the Docling library. This skill handles both single-file conversions and batch processing of multiple PDFs in a directory.

## When to Activate

Activate this skill when:
- User explicitly invokes `/pdf-to-md`
- User asks to convert a PDF to Markdown
- User needs to extract text content from PDF documents
- User wants to batch convert multiple PDFs
- User mentions Docling or PDF conversion

## Requirements

**Docling library must be installed:**
```bash
pip install docling
```

If Docling is not installed, inform the user and provide installation instructions before proceeding.

## Process

### Phase 1: Input Validation

1. **Verify path exists**
   - Check if the provided path exists
   - Determine if path is a single PDF file or a directory

2. **Check Docling installation**
   - Attempt to import `docling.document_converter`
   - If import fails, provide installation instructions

3. **Identify conversion mode**
   - **Single file**: Path ends with `.pdf` and is a file
   - **Batch mode**: Path is a directory (will process all PDFs within)

### Phase 2: Conversion

**For single file conversion:**

```python
from docling.document_converter import DocumentConverter

converter = DocumentConverter()
result = converter.convert(pdf_path)
markdown_content = result.document.export_to_markdown()
```

**For batch conversion:**

1. Glob all `.pdf` files in the directory
2. Create an output directory (e.g., `markdown_outputs/`)
3. Process each PDF sequentially
4. Track successes and failures

### Phase 3: Output

**Output path determination:**
- If output path specified: Use it directly
- If not specified for single file: Same name with `.md` extension in same directory
- If not specified for batch: Create `markdown_outputs/` subdirectory

**Report results:**
- Confirm successful conversion
- Report page count for each document
- For batch: Provide summary of successes and failures

## Output Format

### Single File Success
```
Converting {filename} to Markdown...
Successfully converted PDF to Markdown: {output_path}
Document has {page_count} pages
```

### Batch Conversion Summary
```
CONVERSION SUMMARY
==================
Successfully converted: {count}
  - file1.pdf
  - file2.pdf

Failed conversions: {count}
  - file3.pdf (reason)

Markdown files saved to: {output_directory}
```

## Example Usage

### Single File
```
/pdf-to-md /path/to/document.pdf
```

Output saved to `/path/to/document.md`

### Single File with Custom Output
```
/pdf-to-md /path/to/document.pdf --output /other/location/output.md
```

### Batch Conversion
```
/pdf-to-md /path/to/pdf-folder/
```

Creates `/path/to/pdf-folder/markdown_outputs/` with converted files.

## Error Handling

| Error | Action |
|-------|--------|
| Docling not installed | Provide `pip install docling` instructions |
| File not found | Report the invalid path |
| Invalid PDF | Skip file in batch mode, report error |
| Write permission error | Suggest alternative output location |
| Conversion failure | Report specific error, continue batch |

## Implementation Notes

### Windows-Specific Handling

The skill suppresses HuggingFace hub symlink warnings on Windows:
```python
import os
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'
```

### Performance Considerations

- Docling loads ML models on first use (may take time)
- Large PDFs may require significant memory
- Batch conversions process sequentially to avoid memory issues

## Reference Implementation

See `scripts/pdf_to_markdown.py` for a complete Python implementation that can be used directly or as a reference for the conversion logic.

## Principles

### Preserve Document Structure
Docling extracts semantic structure (headings, lists, tables). The resulting Markdown should reflect the document's organization.

### Report Progress
For batch operations, show progress to keep users informed during longer operations.

### Handle Failures Gracefully
In batch mode, continue processing remaining files even if one fails. Provide a complete summary at the end.

### Validate Output
After conversion, verify the output file was created and has content.
