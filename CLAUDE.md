# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Claude Code skill repository for the InfAU chair (Informatik in der Architektur und Urbanistik) at Bauhaus-Universität Weimar. It contains domain-specific plugins with custom skills for academic research tasks.

## Repository Structure

```
skill-base/
├── .claude-plugin/              # Root plugin manifest
├── research/                    # Research domain plugin
│   ├── .claude-plugin/
│   ├── commands/
│   │   ├── start.md
│   │   └── research-question.md
│   ├── skills/
│   │   ├── research-question/
│   │   └── scientific-problem-selection/
│   └── README.md
├── data/                        # Data domain plugin
│   ├── .claude-plugin/
│   ├── commands/
│   └── skills/
├── _templates/                  # Templates for creating new skills
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
- `/start` - Begin research planning workflow
- `/research-question [question]` - Improve research questions using FINER/PICO frameworks
