---
name: monet
description: Generate architecture-focused images using Google Gemini with structured prompts and style references. Use when users mention image generation, architectural visualization, Gemini images, /monet, or want to create visual content for architecture projects.
trigger: manual
---

# Monet — Architecture Image Generation

Generate architectural visualizations using Google Gemini. Each project has a `monet/` directory with context, style references, structured prompts (JSON or narrative), and auto-versioned results.

## When to Activate

- User invokes `/monet`
- User asks to generate architectural images or visualizations
- User wants to create image prompts for Gemini

## Prerequisites Check

Before any generation, verify:
1. Python 3.7+ available
2. Dependencies installed: `google-genai`, `Pillow`, `python-dotenv`
3. `.env` file exists in the working directory (or parent) with `GOOGLE_API_KEY` or `GEMINI_API_KEY`

If dependencies are missing, run:
```bash
pip install google-genai Pillow python-dotenv
```

If no API key, tell the user:
> You need a Gemini API key. Get one at https://aistudio.google.com/apikey
> Then create a `.env` file with: `GOOGLE_API_KEY=your-key-here`

## Process

### Phase 1: Understand the Project

Check for an existing `monet/` directory in the current working directory.

**If `monet/` exists:**
1. Read all files in `monet/context/` — this is the project's knowledge base. It contains source documents the user has added (architecture specs, research notes, briefs, technical descriptions, visual identity guides) that inform prompt writing.
2. View images in `monet/references/types/` — understand what kind of images this project produces
3. View images in `monet/references/styles/` — understand the target aesthetic
4. Check `monet/starters/` for base images
5. Summarize: *"This project generates [type] images in [style] aesthetic for [purpose]"*
6. Proceed to Phase 3 (Author Prompts) or Phase 4 (Generate) depending on user intent

**If `monet/` does not exist:**
- Proceed to Phase 2 (Scaffold)

### Phase 2: Scaffold New Project

Create the `monet/` directory with standard structure:

```bash
mkdir -p monet/{context,references/types,references/styles,starters,prompts,results}
```

Then help the user set up:

**Context (knowledge base):**
- Tell the user to add any source documents to `monet/context/` — architecture specs, research notes, briefs, technical descriptions, anything Claude should read to write informed prompts
- These files are Claude's reference material, not sent to Gemini

Remind the user to:
- Add source documents to `monet/context/` for Claude to read when writing prompts (specs, briefs, visual identity notes, research)
- Drop style reference images into `monet/references/styles/`
- Drop type reference images into `monet/references/types/` (optional)
- Drop starter images into `monet/starters/` (optional)

### Phase 3: Author Prompts

1. Read all files in `monet/context/` — absorb the source material the user has provided (specs, notes, briefs). Use this knowledge to write accurate, informed prompts.
2. Read 1-2 existing prompts in `monet/prompts/` (if any) for tone and detail calibration
3. Ask the user what they want to visualize — the **image concept**
4. If starters exist in `monet/starters/`, ask if they want to transform one

**Drafting the prompt:**

Load `references/json-schemas.md` for template structures.

- **JSON prompts** (preferred for precise iteration):
  1. Choose the closest JSON template based on image type
  2. Include common fields: `scene_type`, `composition`, `camera`, `lighting`, `constraints`
  3. Add type-specific fields — invent fields that fit the image
  4. Show draft to user for field-level review

- **Narrative prompts** (when user prefers prose):
  - Use photographic/cinematic language (camera angles, lens types, lighting)
  - Include atmosphere cues ("like an architectural magazine editorial")
  - Specify materials and textures precisely
  - Weave constraints into the prose

Save as `monet/prompts/<id>.md` with this structure:
```markdown
# Image Prompt — [Title]

## Concept
[What the image represents and why — 2-3 sentences]

## Prompt
[JSON object or narrative text]
```

Show draft to user for approval before saving.

### Phase 4: Generate & Iterate

**Generate:**
```bash
python <skill-path>/scripts/generate.py <cwd>/monet <prompt_id>
```

Where `<skill-path>` is the skill's installation directory (resolve from the skill's location).

**After generation:**
1. Show the generated image to the user using the Read tool
2. Ask for feedback

**If user wants changes:**
- For JSON prompts: modify specific fields in the prompt file (surgical edits)
- For narrative prompts: rewrite the relevant section
- Regenerate — fresh from clean inputs + updated prompt
- **Never use a generated image as input for the next generation** (Golden Rule)

**Results auto-version:** `{prompt_id}_v1.png`, `v2.png`, etc. Previous versions are never overwritten.

## CLI Script Reference

| Script | Purpose | Location |
|--------|---------|----------|
| `scripts/generate.py` | Image generation via Gemini API | Run with Python 3.7+ |

**Usage:**
```bash
python scripts/generate.py <project-dir> [prompt_ids...] [options]
```

**Options:**
- `--list` — List prompts and version counts
- `--model MODEL` — Override model (default: gemini-3.1-flash-image-preview)
- `--aspect-ratio RATIO` — Override (default: 16:9)
- `--image-size SIZE` — Override (default: 2K)
- `--style FILE` — Use specific style reference from references/styles/
- `--starter FILE` — Use specific starter image from starters/

## Principles

### One Image at a Time
Never generate all prompts at once. Generate one, show to user, get feedback, iterate. Each image deserves attention.

### JSON is the Source of Truth
All changes accumulate in the JSON prompt. Every generation is fresh from clean inputs. Never chain through generated images.

### Ask Before Assuming
When drafting prompts, show the draft and ask for approval. When the user says "change the lighting," confirm which fields before editing.

### Use Context Documents
Read the user's source documents in `context/` before writing prompts. The better you understand the subject, the better the prompt.

## References

- See `references/workflow.md` for iteration methodology, conventions, and CLI details
- See `references/json-schemas.md` for JSON prompt templates (5 scene types)
- See `examples/prompt-examples.md` for JSON and narrative prompt examples

## Boundaries

This skill should NOT:
- Generate all prompts in batch without user review
- Use a previously generated image as input for the next generation
- Modify style/type reference images
- Skip showing generated results to the user
- Write prompts without reading context documents first
- Create prompts without user approval of the draft
