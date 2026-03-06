---
description: Convert Grasshopper GHX files to LLM-readable markdown and generate RAG summaries
argument-hint: "<ghx-path> [--output <output-path>]"
---

# /ghx-to-llm - Convert GHX to LLM-readable Markdown

Convert Grasshopper `.ghx` files into LLM-readable markdown documentation and semantic summaries.

## Usage

```
/ghx-to-llm <ghx-path> [--output <output-path>]
```

**Arguments:**
- `<ghx-path>` - Path to a `.ghx` file (XML-based Grasshopper definition)
- `--output <output-path>` - (Optional) Custom output path for the conversion file

## Workflow

Invoke the `ghx-to-llm` skill to process `$ARGUMENTS`.

The skill runs in two phases:
1. **Phase 1 (Automated):** Run the Python converter script to produce `{name}_ghx-to-llm.md`
2. **Phase 2 (LLM):** Analyze the conversion output and create `{name}_ghx-summary.md`

Both output files are saved alongside the input `.ghx` file.

## Examples

**Convert a single file:**
```
/ghx-to-llm /path/to/Definition.ghx
```
Creates `Definition_ghx-to-llm.md` and `Definition_ghx-summary.md`

**Convert with custom output:**
```
/ghx-to-llm /path/to/Definition.ghx --output /docs/Definition_ghx-to-llm.md
```

## Tips

- Input must be `.ghx` (XML-based), not binary `.gh` — re-save from Grasshopper if needed
- Python 3.8+ required, uses standard library only (no dependencies)
- Named groups in Grasshopper significantly improve output structure
