---
description: Generate architecture-focused images using Google Gemini with structured prompts and style references
argument-hint: "[prompt-id] [--list] [new]"
---

# /monet - AI Image Generation for Architecture

Generate architectural visualizations using Google Gemini. Works with structured projects containing context, style references, and markdown prompts (JSON or narrative).

## Usage

```
/monet                    Open existing monet/ project or scaffold a new one
/monet new                Force-create a new monet/ directory in the current project
/monet <prompt-id>        Generate a specific prompt
/monet --list             List prompts and version counts
```

**Arguments:**
- `new` - Scaffold a new `monet/` directory with standard structure
- `<prompt-id>` - Generate images for a specific prompt file
- `--list` - Show all discovered prompts and their version counts

## Workflow

Invoke the `monet` skill to process `$ARGUMENTS`.

The skill works in phases:
1. **Understand** — Read project context, view references, understand the aesthetic
2. **Scaffold** (if needed) — Create `monet/` directory with standard structure
3. **Author** — Draft prompts as JSON scene descriptions or narrative text
4. **Generate & Iterate** — Run generation, review results, refine prompts

## Prerequisites

- Python 3.7+ with `google-genai`, `Pillow`, `python-dotenv`
- `.env` file with `GOOGLE_API_KEY` or `GEMINI_API_KEY` (get one at https://aistudio.google.com/apikey)

## Examples

**Start a new image project:**
```
/monet new
```
Creates `monet/` in the current directory with context/, references/, prompts/, results/

**Work with an existing project:**
```
/monet
```
Reads monet/context/, views references, enters prompt authoring workflow

**Generate a specific prompt:**
```
/monet facade_study
```
Runs generation for `monet/prompts/facade_study.md`

**Check what's available:**
```
/monet --list
```

## Tips

- JSON prompts are preferred for precise iteration — each field can be independently modified
- The `_design_concept.md` in context/ is auto-prepended to all prompts as a style guide
- Style references in `references/styles/` are sent to Gemini as visual anchors
- Type references in `references/types/` are for Claude's understanding only (not sent to Gemini)
- Results auto-version: `facade_study_v1.png`, `v2.png`, etc.
