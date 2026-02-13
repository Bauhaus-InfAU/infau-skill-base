# InfAU Skill-Base

Academic skills for Claude Code at the InfAU chair (Informatik in der Architektur und Urbanistik), Bauhaus-Universität Weimar.

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

Data management and analysis workflows.

## Installation

### For Claude Code users

1. Clone or download this repository
2. Copy the domain plugin folder (e.g., `research/`) to your Claude plugins directory:
   - Windows: `%USERPROFILE%\.claude\plugins\`
   - macOS/Linux: `~/.claude/plugins/`
3. Restart Claude Code

The commands will be available immediately after installation.

### Alternative: Project-specific installation

To use these skills only in a specific project:

1. Copy the domain plugin folder (e.g., `research/`) to your project root
2. The commands will be available when working in that project

## Structure

```
skill-base/
├── .claude-plugin/                   # Root plugin manifest
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

Internal use at Bauhaus-Universität Weimar.
