# Monet Workflow Reference

## The Golden Rule

The JSON prompt is the single source of truth. All desired changes accumulate in the JSON. Every generation is a fresh pass from clean inputs (original starter + style refs + updated JSON). Never use a previously generated image as input for the next generation.

## Iteration Workflow

1. Generate v1 → review result with user
2. User wants changes → modify specific JSON field(s) in the prompt file
3. Generate v2 → fresh from same clean inputs + updated JSON
4. Repeat — quality stays constant, changes are surgical and trackable

### Edit-Existing Workflow

1. View the generated result
2. Update the JSON prompt to capture all desired changes
3. Regenerate from scratch — never chain through the generated image

## Project Directory Structure

When `/monet` scaffolds a project, it creates:

```
monet/
├── context/                    # Project documentation
│   ├── _design_concept.md     # Visual identity guide (auto-prepended to all prompts)
│   └── *.md                   # Brief, constraints, materials, etc.
├── references/
│   ├── types/                 # WHAT to generate — Claude analyzes, NOT sent to Gemini
│   │   └── *.jpg/png
│   └── styles/                # HOW it looks — ALL sent to Gemini as visual anchors
│       └── *.jpg/png
├── starters/                  # Optional base images (hand drawings, white models)
│   └── *.jpg/png             # Sent to Gemini as transformation base
├── prompts/                   # Prompt .md files (## Prompt marker required)
│   └── *.md
└── results/                   # Generated images (auto-versioned: {id}_v{N}.png)
```

## Type vs Style vs Starter References

| Reference Type | Location | Sent to Gemini? | Purpose |
|---------------|----------|-----------------|---------|
| **Type** | `references/types/` | No | Inform Claude what KIND of image (exterior, model, diagram) |
| **Style** | `references/styles/` | Yes, all of them | Visual anchors for aesthetic (materials, lighting, palette) |
| **Starter** | `starters/` | Yes, first one | Base image for transformation (sketch → styled output) |

## Prompt File Conventions

- Files live in `prompts/` as markdown with a `## Prompt` section (required for discovery)
- The `## Prompt` section can contain **narrative text** or **JSON** — auto-detected by `generate.py`
- Files prefixed with `_` are skipped by the discovery system
- Each prompt file should also have a `## Concept` section explaining the image's purpose
- `context/_design_concept.md` content is auto-prepended to all prompts unless `--no-concept` is used

## CLI Reference

```
python generate.py <project-dir> [prompt_ids...] [options]

Positional:
  project-dir          Path to project directory (must contain prompts/)
  prompt_ids           Specific prompts to generate (default: all)

Options:
  --list               List prompts, version counts, and project stats
  --model MODEL        Override model (default: gemini-3.1-flash-image-preview)
  --aspect-ratio RATIO Override aspect ratio (default: 16:9)
  --image-size SIZE    Override image size (default: 2K)
  --style FILE         Use a specific style reference from references/styles/
  --starter FILE       Use a specific starter image from starters/
  --no-concept         Skip prepending design concept
```

## Generation Rules

- Never run all prompts at once — generate one at a time so the user can review each result
- Show the generated image to the user using the Read tool after each generation
- Results auto-version: `{prompt_id}_v1.png`, `v2.png`, etc. — previous versions are never overwritten
- API key must be set: `GOOGLE_API_KEY` or `GEMINI_API_KEY` in a `.env` file
