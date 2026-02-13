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
/plugin install data@infau-skills
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
- `/start` - Begin research planning workflow
- `/research-question` - Improve research questions using FINER/PICO frameworks

**Example:**
```
/research-question How can computational simulation evaluate the impact of micro-scale interventions in fostering spatial synchronization?
```

Claude will:
1. Diagnose specific problems with your question
2. Select an appropriate framework (FINER, PICO, or InfAU-specific)
3. Ask clarifying questions one at a time
4. Show before/after comparisons as you improve

### Data (`data/`)

Data management and analysis workflows for SQL, visualization, dashboards, and data validation.

**Commands:**
- `/analyze` - Answer data questions
- `/explore-data` - Profile and explore datasets
- `/write-query` - Write optimized SQL
- `/create-viz` - Create publication-quality visualizations
- `/build-dashboard` - Build interactive HTML dashboards
- `/validate` - QA analyses before sharing

## Structure

```
skill-base/
├── .claude-plugin/                   # Root plugin manifest + marketplace
│   ├── plugin.json
│   └── marketplace.json
├── research/                         # Research domain plugin
│   ├── .claude-plugin/
│   ├── commands/
│   │   ├── start.md
│   │   └── research-question.md
│   ├── skills/
│   │   ├── research-question/
│   │   │   ├── SKILL.md
│   │   │   ├── references/
│   │   │   └── examples/
│   │   └── scientific-problem-selection/
│   └── README.md
├── data/                             # Data domain plugin
│   ├── .claude-plugin/
│   ├── commands/
│   └── skills/
├── _templates/                       # Templates for new skills
├── CLAUDE.md
├── CONTRIBUTING.md
└── README.md
```

## Contributing

Want to add your own skill? See [CONTRIBUTING.md](CONTRIBUTING.md) for a step-by-step guide. No programming experience required.

## License

MIT License - see [LICENSE](LICENSE) for details.
