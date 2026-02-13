# InfAU-Specific Research Question Frameworks

These frameworks are designed for research at the intersection of informatics and architecture/urban planning, addressing the specific methodological challenges of computational design, immersive technologies, and simulation-based research.

---

## CDRF - Computational Design Research Framework

For AI/ML design generation, parametric optimization, and computational simulation studies.

### D - Data

What training and validation data is available?

**Questions to consider:**
- What data will train/validate your model?
- What is the data quality and size?
- Is the data representative of the target domain?
- How was the data collected and labeled?
- Are there biases in the data?

**Red flags:**
- No clear training/test split
- Data from one context expected to generalize to another
- Self-labeled or unlabeled data without acknowledgment
- Dataset too small for the model complexity

**Questions to ask:**
- "What dataset will you use, and how large is it?"
- "How was the data collected and by whom?"
- "What biases might exist in your training data?"

**Example applications:**
- Floor plan datasets (Neufert, RPLAN, etc.)
- Building energy performance databases
- Urban morphology datasets
- Pedestrian tracking data

---

### M - Model

What computational approach is being used?

**Questions to consider:**
- What ML architecture or algorithm?
- Why this approach over alternatives?
- What are the model's assumptions?
- What computational resources are needed?

**Red flags:**
- Complex model for simple problem (overfitting risk)
- No justification for architecture choice
- Black-box model where interpretability matters
- Computational requirements exceed available resources

**Questions to ask:**
- "Why this specific model architecture?"
- "What alternatives did you consider?"
- "What are the model's key assumptions?"

**Example applications:**
- GAN for floor plan generation
- GNN for spatial layout optimization
- Reinforcement learning for design exploration
- Evolutionary algorithms for multi-objective optimization

---

### E - Evaluation

How will success be measured?

**Questions to consider:**
- What metrics define success?
- Is there a ground truth for comparison?
- Who evaluates the outputs (human experts, automated metrics)?
- How do you handle subjective quality?

**Red flags:**
- No ground truth defined
- Only technical metrics (loss, accuracy) without domain relevance
- No human evaluation for design quality
- Success criteria defined post-hoc

**Questions to ask:**
- "How will you know if the generated designs are 'good'?"
- "What ground truth will you compare against?"
- "Who will evaluate the outputs and using what criteria?"

**Example applications:**
- Functional metrics (circulation efficiency, daylight access)
- Expert rating protocols
- Compliance with standards (Neufert, building codes)
- User preference studies

---

### G - Generalization

Will the model work beyond the training domain?

**Questions to consider:**
- What is the intended scope of applicability?
- How do you test generalization?
- What domain shift is expected?
- Are there known limitations?

**Red flags:**
- Training and test from same distribution only
- No discussion of scope boundaries
- Claims of universality without evidence
- Single context evaluation

**Questions to ask:**
- "Will this work on building types not in your training set?"
- "How will you test generalization to new contexts?"
- "What are the boundaries of where this model applies?"

**Example applications:**
- Cross-cultural design transfer
- Different building typologies
- Various climate zones
- Different urban contexts

---

### I - Interpretability

Can designers understand and trust the output?

**Questions to consider:**
- Can the model's decisions be explained?
- Do designers understand why a design was generated?
- Is the output actionable for practitioners?
- What level of trust is appropriate?

**Red flags:**
- Pure black-box output with no explanation
- Designers expected to blindly accept results
- No connection to design rationale
- Unexplainable failures possible

**Questions to ask:**
- "Can you explain why the model produces a particular output?"
- "Would a designer trust this enough to use it?"
- "How do you communicate the model's reasoning?"

**Example applications:**
- Feature attribution for design decisions
- Design rationale generation
- Constraint visualization
- Confidence/uncertainty communication

---

## VREF - VR/AR Evaluation Framework

For participatory planning, design evaluation, and immersive visualization studies.

### F - Fidelity

What level of realism is needed?

**Questions to consider:**
- What visual/audio/haptic fidelity?
- Does higher fidelity improve the study?
- What is the cost-benefit of increased realism?
- What aspects need to be realistic vs. abstracted?

**Red flags:**
- Maximum fidelity assumed without justification
- Fidelity mismatched to research questions
- Important perceptual cues missing
- Over-investment in irrelevant detail

**Questions to ask:**
- "What level of realism does your research question require?"
- "Which sensory aspects matter most for your study?"
- "Have you considered lower-fidelity alternatives?"

**Example applications:**
- Photorealistic vs. schematic visualization
- Spatial audio requirements
- Level of detail for urban models
- Material and lighting quality

---

### I - Interaction

What user actions are supported?

**Questions to consider:**
- What can users do in the environment?
- How does interaction affect the experience?
- Are the interactions natural or learned?
- What interaction modalities are available?

**Red flags:**
- Passive viewing only when interaction matters
- Unnatural interactions that confuse users
- Interaction capabilities not matched to research questions
- Missing key actions that would occur in reality

**Questions to ask:**
- "What can participants do in the VR environment?"
- "How does this compare to what they would do in reality?"
- "Are the interactions intuitive or do they require training?"

**Example applications:**
- Navigation and wayfinding
- Object manipulation
- Social interaction (multi-user)
- Design modification tools

---

### M - Measurement

What behaviors and responses are captured?

**Questions to consider:**
- What data is collected during the experience?
- How are subjective responses measured?
- What behavioral metrics are tracked?
- Is the measurement intrusive?

**Red flags:**
- Only post-hoc questionnaires, no behavioral data
- Measurement interferes with natural behavior
- Key behaviors not captured
- No baseline for comparison

**Questions to ask:**
- "What data will you collect during the VR session?"
- "How will you measure subjective responses?"
- "Will participants behave naturally while being measured?"

**Example applications:**
- Eye tracking and gaze patterns
- Movement and navigation paths
- Physiological responses (heart rate, skin conductance)
- Think-aloud protocols
- Pre/post questionnaires

---

### E - Ecological Validity

How does VR behavior relate to real-world behavior?

**Questions to consider:**
- Do findings transfer to reality?
- What simulator sickness or fatigue effects exist?
- How does VR novelty affect behavior?
- Are the differences between VR and reality addressed?

**Red flags:**
- Assumption that VR = reality
- No acknowledgment of VR limitations
- Simulator sickness not addressed
- Novelty effects not controlled

**Questions to ask:**
- "How confident are you that VR behavior predicts real behavior?"
- "What evidence supports VR validity for your domain?"
- "How will you address VR-specific artifacts?"

**Example applications:**
- Perception studies (scale, distance)
- Decision-making in design review
- Wayfinding and navigation
- Social behavior in shared spaces

---

### A - Accessibility

Can target users actually participate?

**Questions to consider:**
- Who can use the VR system?
- What exclusion criteria exist?
- Are there accommodation needs?
- What training is required?

**Red flags:**
- Exclusion of important user groups
- No consideration of motion sensitivity
- Expensive equipment limits participants
- Long training requirements limit sample

**Questions to ask:**
- "Who might be excluded from your study?"
- "How will you handle participants with motion sensitivity?"
- "What equipment and training does participation require?"

**Example applications:**
- Elderly participants in planning studies
- Users with disabilities
- Children in educational contexts
- Non-technical stakeholders

---

## SSF - Simulation Study Framework

For agent-based modeling, pedestrian simulation, energy modeling, and other predictive simulations.

### C - Calibration

How is the model validated against reality?

**Questions to consider:**
- What real-world data validates the model?
- How are parameters set?
- What is the calibration process?
- How good is good enough?

**Red flags:**
- No validation data
- Parameters chosen arbitrarily
- Calibration on test data (circular validation)
- No quantified calibration quality

**Questions to ask:**
- "What real-world data will validate your simulation?"
- "How are the model parameters determined?"
- "What calibration accuracy is acceptable for your purpose?"

**Example applications:**
- Pedestrian flow counts and trajectories
- Energy consumption measurements
- Traffic volumes and speeds
- Building occupancy patterns

---

### S - Sensitivity

Which parameters matter most?

**Questions to consider:**
- What parameters have the largest effect?
- Which uncertainties propagate most?
- Are default parameters justified?
- What ranges are realistic?

**Red flags:**
- No sensitivity analysis
- Many parameters with unknown influence
- Single parameter values without ranges
- Unrealistic parameter combinations

**Questions to ask:**
- "Which parameters most affect your results?"
- "Have you tested parameter sensitivity?"
- "What realistic ranges do your parameters span?"

**Example applications:**
- Walking speed distributions
- Energy model inputs (occupancy, weather)
- Agent behavior parameters
- Material properties

---

### U - Uncertainty

How confident are the predictions?

**Questions to consider:**
- What is the prediction uncertainty?
- How do errors propagate?
- Are confidence intervals provided?
- What is the precision vs. accuracy?

**Red flags:**
- Point predictions without uncertainty
- Overconfident conclusions
- No error analysis
- Precision implied beyond capability

**Questions to ask:**
- "What is the uncertainty in your predictions?"
- "How do input uncertainties affect outputs?"
- "What confidence intervals can you provide?"

**Example applications:**
- Monte Carlo uncertainty propagation
- Ensemble simulations
- Confidence bounds on predictions
- Scenario analysis

---

### S - Scale

What spatial and temporal resolution?

**Questions to consider:**
- What is the spatial resolution?
- What is the temporal resolution?
- Is the scale appropriate for the question?
- What are the computational limits?

**Red flags:**
- Resolution finer than data supports
- Scale mismatch with research questions
- Computational infeasibility
- Important phenomena below resolution

**Questions to ask:**
- "What spatial and temporal resolution will you use?"
- "Is this resolution appropriate for your research question?"
- "What phenomena might you miss at this scale?"

**Example applications:**
- Individual agent vs. flow-based models
- Hourly vs. annual energy simulation
- Building vs. neighborhood scale
- Real-time vs. accelerated simulation

---

### T - Transferability

Does the model work in other contexts?

**Questions to consider:**
- What contexts has it been validated in?
- What domain transfer is expected?
- Are there known context dependencies?
- How do you test transferability?

**Red flags:**
- Validated in one context, applied to another
- Context dependencies not acknowledged
- Overgeneralized claims
- No discussion of scope limits

**Questions to ask:**
- "In what contexts has this model been validated?"
- "Will it work in different geographic/cultural contexts?"
- "What are the boundaries of where this model applies?"

**Example applications:**
- Cultural differences in pedestrian behavior
- Climate-specific energy models
- Regional building typologies
- Local planning regulations

---

## Framework Selection Guide

| Research Focus | Primary Framework | Secondary Framework |
|----------------|-------------------|---------------------|
| AI-generated floor plans | CDRF | FINER |
| VR design evaluation study | VREF | PICO |
| Pedestrian simulation validation | SSF | PICO |
| ML energy prediction | CDRF | SSF |
| VR participatory planning | VREF | FINER |
| Agent-based urban model | SSF | CDRF |
| Generative design optimization | CDRF | FINER |
| AR wayfinding study | VREF | PICO |

---

## Framework Combination Example

**Research question:** "How accurately can a GNN trained on German housing predict floor plan layouts for French housing standards?"

**CDRF check:**
- **D** (Data): German housing dataset, French housing for testing
- **M** (Model): Graph neural network for layout prediction
- **E** (Evaluation): Compliance with French housing standards, expert rating
- **G** (Generalization): Cross-cultural transfer is the central question
- **I** (Interpretability): Can explain layout decisions to designers?

**PICO check:**
- **P** (Population): Residential floor plan layouts
- **I** (Intervention): GNN prediction model
- **C** (Comparison): French housing standards as ground truth
- **O** (Outcome): Prediction accuracy, standard compliance rate
