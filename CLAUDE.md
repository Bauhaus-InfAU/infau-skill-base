# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Claude Code skill repository for the InfAU chair (Informatik in der Architektur und Urbanistik) at Bauhaus-Universität Weimar. It contains domain-specific plugins with custom skills for academic research tasks.

## Repository Structure

```
skill-base/
├── .claude-plugin/                   # Root plugin manifest + marketplace
│   ├── plugin.json
│   └── marketplace.json
├── research/                         # Research domain plugin
│   ├── .claude-plugin/
│   ├── commands/
│   │   ├── research-plan.md
│   │   ├── research-question.md
│   │   └── deep-research.md
│   └── skills/
│       ├── research-question/
│       ├── scientific-problem-selection/
│       └── deep-research/
├── docs/                             # Document processing plugin
│   ├── .claude-plugin/
│   ├── commands/
│   │   └── pdf-to-md.md
│   └── skills/
│       ├── pdf/
│       └── pdf-to-md/
├── grasshopper/                      # Grasshopper/Rhino plugin
│   ├── .claude-plugin/
│   ├── commands/
│   │   └── ghx-to-llm.md
│   └── skills/
│       └── ghx-to-llm/
├── monet/                            # AI image generation plugin
│   ├── .claude-plugin/
│   ├── commands/
│   │   └── monet.md
│   └── skills/
│       └── monet/
├── _templates/                       # Templates for creating new skills
├── CLAUDE.md
├── CONTRIBUTING.md
└── README.md
```

## Domain Plugin Pattern

Each domain folder is a **plugin** containing:
- `.claude-plugin/plugin.json` - Plugin manifest
- `commands/` - Slash command definitions
- `skills/` - Skill implementations with references and examples

## Adding New Skills

1. Identify the appropriate domain plugin (e.g., `research/`)
2. Create skill folder: `research/skills/your-skill-name/`
3. Add `SKILL.md` with skill logic
4. Add supporting folders (`references/`, `examples/`) as needed
5. Create command: `research/commands/your-skill-name.md`

## Command File Format

Commands in `domain/commands/` are markdown files where:
- The filename becomes the command name (e.g., `research-question.md` → `/research-question`)
- `$ARGUMENTS` captures everything after the command
- Content is injected as instructions when the command runs

## Available Commands

### Research Domain
- `/research-plan [topic]` - Plan research projects using scientific problem selection framework
- `/research-question [question]` - Improve research questions using FINER/PICO frameworks
- `/deep-research [topic]` - Conduct comprehensive multi-source research with citation tracking

### Docs Domain
- `/pdf-to-md [file]` - Convert PDF files to Markdown using Docling

### Grasshopper Domain
- `/ghx-to-llm [file]` - Convert GHX files to LLM-readable markdown with cluster resolution

### Monet Domain
- `/monet [prompt-id|new|--list]` - Generate architecture-focused images using Google Gemini
