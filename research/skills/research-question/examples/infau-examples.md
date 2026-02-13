# InfAU-Specific Research Question Examples

These examples demonstrate research question transformation for computational design, VR/AR, simulation, and sustainable building research typical of InfAU work.

---

## Example 1: AI Floor Plan Generation (Neufert 4.0 Style)

### Initial Question
> "How can AI generate good floor plans?"

### Diagnosis

**Problems identified:**

1. **Undefined "good"**: What makes a floor plan "good"? Functional efficiency? Aesthetic quality? Code compliance?

2. **Method embedded in question**: Assumes AI is the right approach without establishing what problem we're solving.

3. **Missing context**: What building type? What standards? What constraints?

4. **No ground truth**: How would we evaluate generated plans?

### Refinement Process

**Q1:** "What specific aspect of floor plan generation interests you?"

**A1:** "I want to see if neural networks can learn the layout rules from architectural standards like Neufert."

**Updated question:**
> "Can neural networks learn floor plan layout rules from Neufert standards?"

---

**Q2:** "What type of floor plans? And what would 'learning the rules' look like in practice?"

**A2:** "Residential floor plans. Learning the rules means generating layouts that comply with the standards."

**Updated question:**
> "Can neural networks generate residential floor plans that comply with Neufert standards?"

---

**Q3:** "How will you measure compliance? And what's your comparison baseline?"

**A3:** "I'll check if room dimensions and relationships meet Neufert guidelines. I want to compare against rule-based generation."

**Updated question:**
> "How does neural network floor plan generation compare to rule-based generation for Neufert compliance?"

---

**Q4:** "What specific architecture? And for which market - Neufert varies by region?"

**A4:** "Graph neural networks for the layout. Focusing on German multi-family housing."

### Final Result

**Before:**
> "How can AI generate good floor plans?"

**After:**
> "How does a graph neural network trained on Neufert standards perform compared to rule-based generation for residential floor plan layout in German multi-family housing?"

### Framework Validation (CDRF)

- **D** (Data): German residential floor plans with Neufert compliance labels
- **M** (Model): Graph neural network for spatial relationship learning
- **E** (Evaluation): Neufert compliance rate, room dimension accuracy
- **G** (Generalization): Limited to German multi-family housing
- **I** (Interpretability): Graph structure allows relationship inspection

---

## Example 2: VR Participatory Planning (OpenVREVAL Style)

### Initial Question
> "Can VR improve public participation?"

### Diagnosis

**Problems identified:**

1. **"Improve" undefined**: Improve what? Attendance? Quality of feedback? Representativeness?

2. **Missing comparison**: Improve compared to what?

3. **Missing population**: Which public? What kind of participation?

4. **Too broad**: "VR" and "public participation" both span many implementations.

### Refinement Process

**Q1:** "What aspect of public participation do you want to improve?"

**A1:** "I'm interested in whether people give better feedback when they can see designs in VR."

**Updated question:**
> "Does VR visualization lead to better feedback in public participation?"

---

**Q2:** "What does 'better feedback' mean? And compared to what?"

**A2:** "More confident, more specific feedback. Compared to looking at 2D drawings and renderings."

**Updated question:**
> "Does VR visualization lead to more confident and specific feedback compared to 2D visualization?"

---

**Q3:** "In what context? And how will you measure confidence?"

**A3:** "Urban planning workshops. I can ask participants to rate their confidence in their feedback."

**Updated question:**
> "How does VR visualization compared to 2D visualization affect stakeholder confidence in design feedback during urban planning workshops?"

### Final Result

**Before:**
> "Can VR improve public participation?"

**After:**
> "How does immersive VR presentation compared to 2D visualization affect stakeholder confidence in their design feedback during urban planning workshops?"

### Framework Validation (VREF)

- **F** (Fidelity): Sufficient for spatial understanding of urban design
- **I** (Interaction): Walkthrough, viewing from multiple angles
- **M** (Measurement): Confidence self-rating, feedback specificity coding
- **E** (Ecological validity): Workshop setting mimics real planning process
- **A** (Accessibility): Accommodations for VR-sensitive participants

---

## Example 3: Pedestrian Simulation Validation (INUMO Style)

### Initial Question
> "How accurate is pedestrian simulation?"

### Diagnosis

**Problems identified:**

1. **Missing context**: Which simulation? What type of environment?

2. **"Accuracy" undefined**: Accuracy of what prediction? Speed? Route? Density?

3. **No comparison baseline**: Accurate compared to what ground truth?

4. **Too general**: Pedestrian simulation encompasses many methods and settings.

### Refinement Process

**Q1:** "What type of pedestrian simulation are you interested in?"

**A1:** "Agent-based models that predict where people walk."

**Updated question:**
> "How accurate are agent-based models at predicting pedestrian routes?"

---

**Q2:** "In what type of environment? Accuracy might differ greatly by context."

**A2:** "Informal settlements - they have irregular street networks that are hard to model."

**Updated question:**
> "How accurate are agent-based models at predicting pedestrian routes in informal settlements?"

---

**Q3:** "What ground truth will you use? And what metric for 'accuracy'?"

**A3:** "GPS tracking data from residents. Accuracy as route overlap or choice prediction."

### Final Result

**Before:**
> "How accurate is pedestrian simulation?"

**After:**
> "What is the prediction accuracy of agent-based pedestrian models for route choice in informal settlements with irregular street networks?"

### Framework Validation (SSF)

- **C** (Calibration): GPS tracking data from settlement residents
- **S** (Sensitivity): Agent speed, route choice parameters
- **U** (Uncertainty): Prediction confidence intervals
- **S** (Scale): Individual agent level, neighborhood scale
- **T** (Transferability): Specific to irregular informal settlement networks

---

## Example 4: Timber Construction Optimization (Spatial Timber Style)

### Initial Question
> "How can we optimize timber structures?"

### Diagnosis

**Problems identified:**

1. **"Optimize" undefined**: Optimize for what? Cost? Material? Strength? Carbon?

2. **Missing structure type**: What timber structures? Frames? Gridshells? CLT panels?

3. **Method assumed**: "Optimize" implies computational optimization but doesn't specify approach.

4. **Missing constraints**: What are the design constraints?

### Refinement Process

**Q1:** "What aspect of timber structures do you want to optimize?"

**A1:** "Material use - I want to minimize the amount of timber while maintaining strength."

**Updated question:**
> "How can we minimize timber material use while maintaining structural strength?"

---

**Q2:** "What type of timber structures? And what optimization method?"

**A2:** "Free-form timber grid shells. Using topology optimization."

**Updated question:**
> "How does topology optimization reduce material use in free-form timber grid shells?"

---

**Q3:** "How will you measure 'maintaining structural strength'? What performance criteria?"

**A3:** "Meeting deflection limits and stress requirements under design loads."

### Final Result

**Before:**
> "How can we optimize timber structures?"

**After:**
> "How does topology optimization reduce material use while maintaining structural performance in free-form timber grid shells?"

### Framework Validation (FINER)

- **F** (Feasible): Topology optimization is established; grid shells are tractable
- **I** (Interesting): Material efficiency is a key concern for sustainable construction
- **N** (Novel): Application to free-form timber gridshells is underexplored
- **E** (Ethical): No human subjects; structural safety must be ensured
- **R** (Relevant): Direct application to sustainable timber construction practice

---

## Example 5: Straw Building Performance (INNOSTROH Style)

### Initial Question
> "Is straw a good building material?"

### Diagnosis

**Problems identified:**

1. **"Good" undefined**: Good for what? Insulation? Structure? Cost? Environment?

2. **Missing comparison**: Good compared to what alternatives?

3. **Missing context**: What climate? What building type? What construction method?

4. **Value judgment framing**: "Good" implies a normative claim.

### Refinement Process

**Q1:** "What aspect of straw as a building material interests you?"

**A1:** "Its thermal and moisture performance - how it handles heat and humidity."

**Updated question:**
> "How does straw perform thermally and hygrothermally as a building material?"

---

**Q2:** "Compared to what? And in what climate?"

**A2:** "Compared to conventional insulation like mineral wool. In Central European climates."

**Updated question:**
> "How does straw compare to mineral wool for thermal and hygrothermal performance in Central European climates?"

---

**Q3:** "What construction system? And how will you measure performance?"

**A3:** "Prefabricated straw panel walls. Long-term monitoring - ideally over several years."

### Final Result

**Before:**
> "Is straw a good building material?"

**After:**
> "How does hygrothermal performance of prefabricated straw panel walls compare to conventional insulation in Central European climates over a 5-year monitoring period?"

### Framework Validation (PICO)

- **P** (Population): Wall assemblies in Central European residential buildings
- **I** (Intervention): Prefabricated straw panel walls
- **C** (Comparison): Conventional mineral wool insulation systems
- **O** (Outcome): Hygrothermal performance (temperature, humidity, moisture content)

---

## Example 6: Urban Mobility Patterns (Ethiopian Mobility Style)

### Initial Question
> "How do people move in African cities?"

### Diagnosis

**Problems identified:**

1. **Too broad**: "African cities" spans enormous diversity
2. **"How" is vague**: Mode choice? Route? Time? Purpose?
3. **Missing population specificity**: Which people? Commuters? All residents?
4. **Overgeneralization risk**: Findings from one city won't represent continent

### Refinement Process

**Q1:** "Which city or cities? And what aspect of movement?"

**A1:** "Addis Ababa. I'm interested in how informal transit routes relate to where people live and work."

**Updated question:**
> "How do informal transit routes relate to residential and employment locations in Addis Ababa?"

---

**Q2:** "Can you be more specific about the relationship you're investigating?"

**A2:** "Whether the routes follow density patterns - do minibus routes serve the highest density areas?"

**Updated question:**
> "What is the relationship between informal transit routes and land use density in Addis Ababa?"

---

**Q3:** "What specific areas? And how will you measure the relationship?"

**A3:** "The expanding peri-urban edges. Looking at route coverage versus residential density."

### Final Result

**Before:**
> "How do people move in African cities?"

**After:**
> "What is the relationship between informal transit route networks and land use density patterns in Addis Ababa's peri-urban areas?"

### Framework Validation (FINER)

- **F** (Feasible): Route mapping and land use data are obtainable
- **I** (Interesting): Informs transit planning in rapidly growing cities
- **N** (Novel): Informal transit in Ethiopian context is understudied
- **E** (Ethical): Uses observational data, no direct human subjects
- **R** (Relevant): Critical for sustainable urban development

---

## Example 7: Parametric Design Evaluation

### Initial Question
> "Can parametric design improve buildings?"

### Diagnosis

**Problems identified:**

1. **"Improve" undefined**: Improve what? Energy? Aesthetics? Cost? Comfort?
2. **Hidden assumption**: Assumes parametric design is better
3. **Missing comparison**: Improve compared to what baseline?
4. **"Buildings" too broad**: What building type? What design aspect?

### Refinement Process

**Q1:** "What aspect of buildings do you want to improve?"

**A1:** "Energy performance and daylight - often there's a trade-off."

**Updated question:**
> "Can parametric design improve the energy-to-daylight trade-off in buildings?"

---

**Q2:** "Improve compared to what? And how will parametric design be used?"

**A2:** "Compared to manual design iterations. Using multi-objective optimization."

**Updated question:**
> "Does multi-objective evolutionary optimization improve the energy-to-daylight trade-off compared to manual design iteration?"

---

**Q3:** "For what building element? And how will you measure the trade-off?"

**A3:** "Office building facades. Energy consumption and daylight autonomy metrics."

### Final Result

**Before:**
> "Can parametric design improve buildings?"

**After:**
> "How does the use of multi-objective evolutionary optimization affect the energy-to-daylight trade-off compared to manual design iteration for office facade configurations?"

### Framework Validation (PICO)

- **P** (Population): Office building facade design options
- **I** (Intervention): Multi-objective evolutionary optimization
- **C** (Comparison): Manual design iteration by trained designers
- **O** (Outcome): Pareto frontier coverage for energy consumption vs. daylight autonomy

---

## Example 8: Lifecycle Assessment Comparison

### Initial Question
> "Which building is more sustainable?"

### Diagnosis

**Problems identified:**

1. **"Sustainable" undefined**: Environmental? Social? Economic?
2. **Comparison undefined**: Which buildings are being compared?
3. **Missing methodology**: How is sustainability measured?
4. **Missing scope**: What life cycle stages? What impact categories?

### Refinement Process

**Q1:** "What aspect of sustainability, and which buildings?"

**A1:** "Carbon emissions. Comparing timber buildings to concrete buildings."

**Updated question:**
> "Do timber buildings have lower carbon emissions than concrete buildings?"

---

**Q2:** "What type of buildings? And what emissions - operational or embodied?"

**A2:** "Mid-rise residential. I want to include both - lifecycle emissions."

**Updated question:**
> "How do lifecycle carbon emissions differ between timber and concrete mid-rise residential buildings?"

---

**Q3:** "What structural systems specifically? And what LCA methodology?"

**A3:** "Cross-laminated timber versus reinforced concrete frames. Using EN 15978 standard."

### Final Result

**Before:**
> "Which building is more sustainable?"

**After:**
> "How do embodied carbon emissions differ between cross-laminated timber and reinforced concrete structural systems for mid-rise residential buildings when assessed using EN 15978 methodology?"

### Framework Validation (FINER)

- **F** (Feasible): EPD data and LCA tools available
- **I** (Interesting): Material choice is a key decision for low-carbon buildings
- **N** (Novel): Specific comparison for mid-rise with EN 15978 adds clarity
- **E** (Ethical): No human subjects; desktop study
- **R** (Relevant): Directly informs sustainable construction practice

---

## Pattern Summary for InfAU Research

| Research Area | Common Initial Problem | Key Refinement Focus |
|---------------|----------------------|----------------------|
| AI/ML Design | "Can AI do X?" | Define evaluation criteria, specify model and data |
| VR Studies | "Is VR better?" | Define "better", establish comparison, specify context |
| Simulation | "How accurate is...?" | Specify ground truth, define accuracy metrics |
| Sustainable Building | "Is X more sustainable?" | Define sustainability dimension, specify LCA methodology |
| Optimization | "Can we optimize...?" | Define objective function, specify constraints |
| Urban Analysis | "How does X affect Y?" | Specify population, setting, measurable outcomes |
