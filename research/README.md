# Research Plugin

Research planning and problem selection framework for academic research in computational design, urban planning, and sustainable building. Developed for the InfAU chair (Informatik in der Architektur und Urbanistik) at Bauhaus-Universität Weimar.

## What's Included

### Commands

| Command | Purpose |
|---------|---------|
| `/start` | Begin research planning workflow |
| `/research-question` | Improve research questions using FINER/PICO frameworks |

### Skills (Research Workflows)

#### Research Question Improvement

Helps students transform vague, overly broad, or poorly structured research questions into clear, focused, and answerable questions suitable for academic research.

**Frameworks supported:**
- **FINER** - General academic research (Feasible, Interesting, Novel, Ethical, Relevant)
- **PICO** - Intervention/comparative studies (Population, Intervention, Comparison, Outcome)
- **CDRF** - Computational design research (Data, Model, Evaluation, Generalization, Interpretability)
- **VREF** - VR/AR evaluation studies (Fidelity, Interaction, Measurement, Ecological validity, Accessibility)
- **SSF** - Simulation studies (Calibration, Sensitivity, Uncertainty, Scale, Transferability)

**Usage:**
```
/research-question How can AI generate good floor plans?
```

#### Scientific Problem Selection

A comprehensive framework for research problem selection based on Fischbach & Walsh's "Problem choice and decision trees in science and engineering" (Cell, 2024). Includes 9 interconnected skills:

| Skill | Purpose | Output |
|-------|---------|--------|
| 1. Intuition Pumps | Generate high-quality research ideas | Problem Ideation Document |
| 2. Risk Assessment | Identify and manage project risks | Risk Assessment Matrix |
| 3. Optimization Function | Define success metrics | Impact Assessment Document |
| 4. Parameter Strategy | Decide what to fix vs. keep flexible | Parameter Strategy Document |
| 5. Decision Tree Navigation | Plan decision points | Decision Tree Map |
| 6. Adversity Response | Prepare for crises as opportunities | Adversity Playbook |
| 7. Problem Inversion | Navigate around obstacles | Problem Inversion Analysis |
| 8. Integration & Synthesis | Synthesize into coherent plan | Project Communication Package |
| 9. Meta-Framework | Orchestrate complete workflow | Complete Project Package |

## Getting Started

```bash
# Install the plugin
/install your-org/skill-base research

# Run the start command to begin
/start

# Or jump directly to research question improvement
/research-question [your question here]
```

## Research Areas

This plugin is designed for research in:

- **Computational Design**: AI for floor plans, parametric design, generative methods
- **Urban Planning & Mobility**: Sustainable cities, pedestrian simulation, accessibility
- **Participatory Planning**: VR/AR evaluation, citizen feedback, co-design
- **Sustainable Building**: Timber construction, lifecycle assessment, climate-responsive design

## Common Workflows

**Improving a Research Question**
Start with a rough question and iterate through diagnosis, framework selection, and refinement until you have a clear, answerable research question.

**New Project Planning**
Pitch a research idea and work through ideation, risk assessment, and impact evaluation using the scientific problem selection framework.

**Troubleshooting Stuck Projects**
Navigate decision trees, use problem inversion strategies, and reframe challenges as opportunities.

**Grant/Thesis Planning**
Create comprehensive project documentation with communication materials (presentations, summaries, elevator pitches).

## Who Should Use This

- **Graduate Students**: Choosing thesis projects, committee meetings, qualification exams
- **Postdocs**: Planning independent projects, fellowship applications
- **Principal Investigators**: New directions, mentoring trainees, grant cycles
- **Research Teams**: Collaborative project planning and evaluation

## Literature Integration

The framework supports literature search using:
- Google Scholar / Semantic Scholar for broad academic coverage
- arXiv (cs.CV, cs.AI, cs.GR) for computational methods
- JSTOR / Web of Science for architectural and urban research
- ResearchGate for accessing full-text papers

## License

Skills are licensed under Apache 2.0.
