# Research Question Frameworks

## FINER Framework

FINER is a general-purpose framework for evaluating research questions, originally developed for clinical research but widely applicable across disciplines.

### F - Feasible

The question can be answered with available:
- **Time**: Can be completed within thesis/project timeline
- **Resources**: Funding, equipment, software available
- **Expertise**: Researcher has or can acquire necessary skills
- **Data**: Data exists or can be collected ethically and practically

**Red flags:**
- Requires longitudinal data over many years
- Needs access to restricted populations or data
- Requires resources not available to the researcher
- Depends on cooperation from organizations unlikely to participate

**Questions to ask:**
- "What data would you need, and can you access it?"
- "What is your timeline for this research?"
- "What tools or methods do you already know?"

### I - Interesting

The question matters to someone beyond the researcher:
- **Academic interest**: Other researchers would want to know the answer
- **Practical interest**: Practitioners could use the findings
- **Personal interest**: Researcher is genuinely motivated

**Red flags:**
- Answer seems obvious before research begins
- No one has asked this question (and there's a reason why)
- Only interesting as an academic exercise

**Questions to ask:**
- "Who would use these findings?"
- "What would change if we knew the answer?"
- "Why hasn't this been studied before?"

### N - Novel

The question adds something new:
- **New knowledge**: Answers unknown question
- **New context**: Tests known findings in new setting
- **New method**: Approaches known question differently
- **New perspective**: Reframes existing knowledge

**Red flags:**
- Repeating existing research without clear justification
- "Gap" is actually well-covered in literature
- Novelty is purely semantic (same question, different words)

**Questions to ask:**
- "What does the existing literature say about this?"
- "How is your approach different from previous work?"
- "What specifically is unknown that you'll discover?"

### E - Ethical

The question can be investigated ethically:
- **No harm**: Participants/subjects not harmed
- **Consent**: Proper consent procedures possible
- **Privacy**: Data can be collected and stored appropriately
- **Honesty**: No deception required (or justified deception)

**Red flags:**
- Requires deception without justification
- Involves vulnerable populations without protections
- Could produce harmful knowledge if published
- Privacy concerns with data collection

**Questions to ask:**
- "Will you need ethics approval, and is it feasible?"
- "How will you protect participant privacy?"
- "Could the findings be misused?"

### R - Relevant

The question connects to broader concerns:
- **Field relevance**: Advances the discipline
- **Practical relevance**: Informs real-world decisions
- **Societal relevance**: Addresses meaningful problems
- **Timely**: Addresses current concerns

**Red flags:**
- Pure academic exercise with no application
- Addresses problem that no longer exists
- Disconnected from current discourse in the field

**Questions to ask:**
- "How does this connect to current debates in your field?"
- "What practical decisions could this inform?"
- "Why is this important now?"

---

## PICO Framework

PICO is designed for research questions about interventions, comparisons, or evaluations. It's particularly useful when testing whether something "works."

### P - Population

Who or what is being studied:
- **Specificity**: Clearly defined boundaries
- **Accessibility**: Can actually be studied
- **Representativeness**: Findings can generalize appropriately

**Examples in architecture/urban contexts:**
- "Pedestrians in European medium-density neighborhoods"
- "Historic buildings in seismic zones"
- "Urban planners working with participatory processes"

**Questions to ask:**
- "Specifically who or what are you studying?"
- "How will you define the boundaries of this group?"
- "Can you access enough of this population?"

### I - Intervention

What is being tested or examined:
- **Specificity**: Clear enough to replicate
- **Controllability**: Can be implemented consistently
- **Measurability**: Can detect whether it was applied

**Examples:**
- "Agent-based simulation of pedestrian flow"
- "Green facade installation"
- "Participatory design workshop format"

**Questions to ask:**
- "What exactly are you testing?"
- "Can you describe the intervention precisely enough for someone else to replicate?"
- "How will you ensure the intervention is applied consistently?"

### C - Comparison

What is being compared against:
- **Baseline**: Status quo, no intervention
- **Alternative**: Different intervention
- **Control**: Matched comparison without treatment

**Examples:**
- "Compared to standard traffic modeling"
- "Compared to buildings without green facades"
- "Compared to traditional top-down planning"

**Questions to ask:**
- "What are you comparing your intervention to?"
- "Is this a fair comparison?"
- "Can you isolate the effect of your intervention?"

### O - Outcome

What is being measured:
- **Measurability**: Can be observed and quantified
- **Relevance**: Matters to stakeholders
- **Specificity**: Clear what "success" looks like

**Examples:**
- "Pedestrian route choice accuracy within 10%"
- "Building surface temperature reduction"
- "Stakeholder satisfaction with planning process"

**Questions to ask:**
- "How will you know if the intervention worked?"
- "What specific outcome are you measuring?"
- "Is this outcome meaningful to the people who would use your findings?"

---

## Framework Selection Guide

| Question Type | Recommended Framework |
|---------------|----------------------|
| "What is...?" (descriptive) | FINER |
| "How does...?" (explanatory) | FINER |
| "Does X improve Y?" (intervention) | PICO |
| "Which is better, X or Y?" (comparison) | PICO |
| "How can we design...?" (design research) | FINER |
| "What factors influence...?" (exploratory) | FINER |
| "Does method X work for problem Y?" (evaluation) | PICO |

**InfAU-specific additions:**

| Question Type | Recommended Framework |
|---------------|----------------------|
| "Can ML/AI generate/predict...?" | CDRF |
| "How does VR compare to...?" | VREF |
| "How accurate is simulation of...?" | SSF |
| "What is the performance of model X?" | CDRF |
| "How do users respond to VR/AR...?" | VREF |
| "How sensitive is simulation to...?" | SSF |

See `infau-frameworks.md` for detailed CDRF, VREF, and SSF descriptions.

---

## SMART Adaptation (Supplementary)

Some questions benefit from SMART criteria (borrowed from goal-setting):

- **Specific**: Single, clear focus
- **Measurable**: Observable outcomes
- **Achievable**: Within scope of project
- **Relevant**: Connected to field/practice
- **Time-bound**: Can be completed in available time

SMART overlaps with FINER but emphasizes measurability and timeline. Use as a quick check, not a primary framework.

---

## Combining Frameworks

For complex questions, use FINER for overall evaluation and PICO for the intervention component:

**Example:**
> "How effective is agent-based modeling for predicting pedestrian route choice in historic European city centers?"

**FINER check:** Is this feasible, interesting, novel, ethical, relevant? (Overall question quality)

**PICO breakdown:**
- P: Pedestrians in historic European city centers
- I: Agent-based modeling predictions
- C: Actual observed pedestrian behavior
- O: Prediction accuracy (e.g., route choice match rate)

For computational research, layer CDRF on top:
- D: What pedestrian behavior data will train/validate the model?
- M: What agent-based modeling approach?
- E: How is prediction accuracy measured?
- G: Will the model work in other city types?
- I: Can planners understand and use the predictions?
