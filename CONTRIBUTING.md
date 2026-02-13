# Contributing: How to Create Your Own Skill

This guide is for colleagues who want to add new skills. No programming experience required.

## Quick Start (5 minutes)

1. **Copy the template:**
   - Copy the entire `_templates/skill-template/` folder
   - Paste it into `skills/` with your skill name (e.g., `skills/literature-review/`)

2. **Rename and edit:**
   - Open `SKILL.md` in any text editor
   - Replace the placeholder content with your skill

3. **Create the command:**
   - Copy an existing file from `commands/` (e.g., `research-question.md`)
   - Rename it to match your skill (e.g., `literature-review.md`)
   - Edit the content to describe your skill

4. **Test it:**
   - Open Claude Code in this repository
   - Type `/your-skill-name` and test

## Understanding Skill Structure

A skill has two parts:

### 1. The Command (`commands/your-skill.md`)

This defines the slash command users type. It's a short file that:
- Describes what the skill does
- Tells Claude how to use it
- Points to the full skill definition

### 2. The Skill Definition (`skills/your-skill/SKILL.md`)

This is the main content. It tells Claude:
- What problem it solves
- How to approach the task
- What steps to follow
- What principles to apply

## Writing Your SKILL.md

### The Header

Start with a YAML header that describes your skill:

```yaml
---
name: literature-review
description: Helps students conduct systematic literature reviews
trigger: always  # Options: always, manual
---
```

### The Body

Write clear instructions for Claude. Use sections:

```markdown
# Literature Review Assistant

## Purpose
Help students conduct systematic and thorough literature reviews.

## When to Activate
- User mentions "literature review"
- User asks about finding sources
- User is working on a thesis background section

## Process

### Phase 1: Scope Definition
First, understand what the student is researching...

### Phase 2: Search Strategy
Help them develop search terms...

## Principles
- Ask one question at a time
- Explain your reasoning
- Provide concrete examples
```

### Key Sections to Include

| Section | Purpose |
|---------|---------|
| Purpose | What problem does this skill solve? |
| When to Activate | What triggers should make Claude use this skill? |
| Process | Step-by-step workflow |
| Principles | Guidelines for behavior |
| References | Link to supporting documents (optional) |
| Examples | Show input/output examples (optional) |

## Adding Supporting Files

You can add reference documents that Claude will use:

```
skills/your-skill/
├── SKILL.md
├── references/
│   ├── methodology.md      # Detailed methodology
│   └── common-mistakes.md  # Problems to avoid
└── examples/
    └── good-examples.md    # Sample outputs
```

Reference them in your SKILL.md:
```markdown
## References
See `references/methodology.md` for detailed framework descriptions.
```

## Writing Tips

### Be Specific, Not Vague

**Bad:** "Help the student improve their work"

**Good:** "Identify three specific weaknesses in the student's argument, explain why each is problematic, and suggest concrete improvements"

### Give Examples

**Bad:** "Ask clarifying questions"

**Good:** "Ask clarifying questions like: 'What specific aspect of X are you most interested in?' or 'Are you focusing on theoretical frameworks or practical applications?'"

### Define the Workflow

**Bad:** "Guide the student through the process"

**Good:**
```
1. First, read their current draft
2. Identify the main thesis statement
3. List supporting arguments
4. For each argument, check if evidence is provided
5. Highlight gaps and suggest sources
```

### Set Boundaries

Tell Claude what NOT to do:
```markdown
## Boundaries
- Do not write the paper for them
- Do not provide more than 3 suggestions at once
- Ask permission before making major structural changes
```

## Testing Your Skill

1. Open Claude Code in this repository folder
2. Type your command: `/your-skill-name`
3. Test with various inputs
4. Check that Claude:
   - Follows your defined process
   - Applies your principles
   - Uses your references appropriately

### Test Cases to Try

- Simple input (does it work at all?)
- Complex input (does it handle edge cases?)
- Incomplete input (does it ask for clarification?)
- Wrong input (does it redirect appropriately?)

## Checklist Before Submitting

- [ ] SKILL.md has a clear purpose section
- [ ] Process is defined step-by-step
- [ ] Principles are specific and actionable
- [ ] Command file exists in `commands/`
- [ ] Tested with at least 3 different inputs
- [ ] No spelling errors in key terms
- [ ] Examples are relevant to our research areas

## Common Mistakes

### Too Long
Skills over 2000 words become unfocused. Split into:
- Core skill (SKILL.md)
- Reference documents (references/)

### Too Vague
"Be helpful" means nothing. Be specific:
- What questions to ask
- What format to use
- What to check for

### No Examples
Abstract instructions are hard to follow. Always include:
- Sample inputs
- Expected outputs
- Before/after comparisons

## Getting Help

- Look at existing skills for patterns
- Test incrementally (add one feature, test, repeat)
- Ask colleagues who have created skills

## Example: Minimal Skill

Here's the simplest possible skill:

**`commands/thesis-outline.md`:**
```markdown
# Thesis Outline Helper

Help the student create a thesis outline.

Use the skill defined in `skills/thesis-outline/SKILL.md`.
```

**`skills/thesis-outline/SKILL.md`:**
```markdown
---
name: thesis-outline
description: Creates thesis outlines
---

# Thesis Outline Helper

## Purpose
Help students structure their thesis with a clear outline.

## Process
1. Ask for the thesis topic
2. Ask for the main research question
3. Propose 3-5 main chapters
4. For each chapter, suggest 2-3 subsections
5. Review and refine based on feedback

## Principles
- Keep outlines to 1 page initially
- Use standard academic structure (Intro, Background, Method, Results, Discussion)
- Ask one question at a time
```

This is enough to create a working skill. Start simple, then add complexity as needed.
