# InfAU Skill-Base

Academic skills for Claude Code at the InfAU chair (Informatik in der Architektur und Urbanistik), Bauhaus-Universität Weimar.

## Installation (Private Repository)

### Prerequisites

Authenticate with GitHub:
```bash
gh auth login
```

### Add the Marketplace

```
/plugin marketplace add Bauhaus-InfAU/infau-skill-base
```

### Install Plugins

```
/plugin install research@infau-skills
/plugin install docs@infau-skills
/plugin install grasshopper@infau-skills
/plugin install monet@infau-skills
```

### For Auto-Updates (Optional)

Set GitHub token in your shell config (`~/.bashrc` or `~/.zshrc`):
```bash
export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx
```

## What is this?

This repository contains domain-specific plugins for Claude Code that help with common academic tasks. Each domain plugin includes skills (reusable prompts) and commands (slash commands) that guide Claude through specific workflows.

## Available Domains

### Research (`research/`)

Research planning and problem selection framework for academic research in computational design, urban planning, and sustainable building.

**Commands:**
- `/research-plan` - Plan research projects using scientific problem selection framework
- `/research-question` - Improve research questions using FINER/PICO frameworks
- `/deep-research` - Conduct comprehensive multi-source research with citation tracking

**Example:**
```
/research-question How can computational simulation evaluate the impact of micro-scale interventions in fostering spatial synchronization?
```

Claude will:
1. Diagnose specific problems with your question
2. Select an appropriate framework (FINER, PICO, or InfAU-specific)
3. Ask clarifying questions one at a time
4. Show before/after comparisons as you improve

### Grasshopper (`grasshopper/`)

Tools for working with Grasshopper (Rhino) parametric definitions.

**Commands:**
- `/ghx-to-llm` - Convert GHX files to LLM-readable markdown with cluster resolution and letter-based cross-referencing

### Monet (`monet/`)

AI image generation for architecture using Google Gemini.

**Commands:**
- `/monet` - Generate architecture-focused images with structured prompts and style references

**Example:**
```
/monet new
```

Claude will:
1. Scaffold a `monet/` directory with context, references, prompts, and results folders
2. Read your project context and style references
3. Author structured prompts (JSON or narrative)
4. Generate images via Gemini and auto-version results

### Docs (`docs/`)

Document processing and conversion workflows.

**Commands:**
- `/pdf-to-md` - Convert PDF files to Markdown using Docling

## Structure

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
├── grasshopper/                      # Grasshopper domain plugin
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
├── docs/                             # Document processing plugin
│   ├── .claude-plugin/
│   ├── commands/
│   │   └── pdf-to-md.md
│   └── skills/
│       ├── pdf/
│       └── pdf-to-md/
├── _templates/                       # Templates for new skills
├── CLAUDE.md
├── CONTRIBUTING.md
└── README.md
```

## Contributing

Want to add your own skill? See [CONTRIBUTING.md](CONTRIBUTING.md) for a step-by-step guide. No programming experience required.

## License

MIT License - see [LICENSE](LICENSE) for details.
