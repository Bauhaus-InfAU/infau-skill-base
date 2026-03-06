# Thesis Proposal: Caregiver-Child Supervision Friction in Public Space

## Title

**Spatial Configuration and Supervision Friction: A Visibility-Based Agent Simulation of Caregiver-Child Dynamics in Public Spaces**

---

## 1. Problem Statement

Public spaces — playgrounds, plazas, parks — are among the few urban environments explicitly designed to include children. Yet even these spaces often fail to support the caregiver-child relationship. Caregivers must maintain visual contact with exploring children while also resting, socializing, or briefly attending to other tasks. When spatial configuration creates poor sightlines, caregivers must constantly reposition to track their child, creating supervision friction.

This friction is a design problem. Some spatial configurations allow caregivers to supervise from a single position; others force continuous movement. Some layouts channel child exploration into visible areas; others create blind spots where children disappear from view. Understanding how spatial configuration affects supervision friction would provide evidence-based guidance for designing public spaces that genuinely support caregiver-child use.

---

## 2. Research Question

> **"How does the spatial configuration of public spaces affect caregiver-child supervision friction, and which visibility characteristics predict low-friction environments?"**

### Sub-questions

1. How can supervision friction be operationalized as a measurable outcome in agent-based simulation?
2. Which visibility graph metrics correlate with friction levels?
3. What spatial configurations allow caregivers to supervise with minimal repositioning?
4. Are there generalizable design principles that predict supervision-friendly layouts?

---

## 3. Theoretical Framework

### 3.1 Space Syntax and Visibility Graph Analysis

This research builds on visibility graph analysis (VGA) developed by Turner et al. (2001) and the agent simulation work of Penn & Turner (2001). Key findings:

- Spatial configuration explains 50-80% of variance in pedestrian movement patterns
- Simple agent rules (random next step within view cone) produce realistic exploratory movement
- Visibility graph metrics predict movement without modeling attractors or destinations

### 3.2 The Caregiver-Child Dyad

The caregiver and child form a coupled system with different behavioral drivers:

| Agent | Behavior | Goal |
|-------|----------|------|
| **Child** | Exploratory | Move toward visible open space, explore environment |
| **Caregiver** | Supervisory | Maintain visual contact with child, minimize own movement |

The **coupling constraint**: Caregiver must keep child within their view cone. When the child moves out of sight, the caregiver must reposition.

### 3.3 Friction as Emergent Property

Supervision friction emerges from the interaction between:
- Spatial configuration (what is visible from where)
- Child behavior (exploratory movement driven by visibility)
- Caregiver behavior (stationary preference with visual tracking requirement)
- Coupling constraint (child must remain in caregiver's view)

Friction is not programmed directly — it emerges when spatial configuration causes frequent coupling violations that require caregiver repositioning.

---

## 4. Methodology

### 4.1 Spatial Representation

Following Penn & Turner (2001):
- **Grid of cells** covering the public space
- **Visibility graph** connecting mutually visible cells
- **Visibility metrics** computed for each cell:
  - Integration (how visually connected to the whole space)
  - Clustering coefficient (junction-ness, visual information change)
  - Mean depth (average visual steps to all other cells)
  - Isovist area (total visible area from that point)

### 4.2 Agent Behavior Rules

**Child Agent (Exploratory)**
- View cone: 170° forward-facing
- Movement rule: Select next destination randomly from visible cells within view cone
- Tendency: Drawn toward high-visibility areas (open space)
- Re-evaluation: New direction selected every N steps

**Caregiver Agent (Supervisory)**
- Preferred behavior: Remain stationary at chosen position
- Constraint: Child must remain within view cone
- Repositioning trigger: When child exits view cone, caregiver moves to re-establish visual contact
- Position selection: When repositioning, select location that maximizes expected visual coverage

### 4.3 Friction Metric

Supervision friction is operationalized as:

```
Friction = Σ (repositioning events) + α(total caregiver distance traveled) + β(visual contact breaks)
```

Where:
- **Repositioning events**: Instances where caregiver must move to maintain visual contact
- **Caregiver distance**: Total distance caregiver travels during observation period
- **Visual contact breaks**: Duration/frequency of child being out of caregiver's view

A **low-friction space** allows the caregiver to remain mostly stationary while the child explores freely within view.

### 4.4 Experimental Design

**Phase 1: Baseline Analysis**
- Create varied spatial configurations (parametric variations):
  - Open plaza vs. segmented space
  - Central vs. distributed obstacles
  - High vs. low visual permeability
  - Convex vs. concave boundaries
- Simulate child exploration and caregiver supervision
- Measure friction for each configuration
- Map friction to visibility graph metrics

**Phase 2: Characteristic Identification**
- Statistical analysis: which visibility metrics predict friction?
- Candidates:
  - Mean isovist area from seating positions
  - Visual integration of play areas
  - Clustering coefficient distribution
  - Visibility graph connectivity

**Phase 3: Configuration Comparison**
- Test real-world public space typologies:
  - Traditional playground (equipment clusters)
  - Open lawn
  - Segmented garden
  - Urban plaza
- Compare friction profiles
- Identify design patterns associated with low friction

**Phase 4: Design Principle Extraction**
- Synthesize findings into generalizable principles
- Example hypotheses:
  - "Spaces with seating positions that have isovist area > X produce low friction"
  - "Central obstacles increase friction more than peripheral obstacles"
  - "Visual integration of play areas should exceed threshold Y"

### 4.5 Simulation Environment

- Grid-based spatial representation
- Visibility graph computed using established VGA methods
- Agent simulation with rules described above
- Software options: Python (Mesa), or custom implementation with visibility analysis (depthmapX/spatial analysis libraries)

---

## 5. Expected Outputs

### 5.1 Academic Contribution

1. **Friction metric**: Operationalized measure of supervision burden based on spatial configuration
2. **Predictive model**: Which visibility metrics predict low-friction supervision
3. **Design principles**: Evidence-based guidelines for supervision-friendly public space design

### 5.2 Design Outputs (Portfolio)

1. **Friction maps**: Visualization of supervision friction across different configurations
2. **Configuration typology**: Classification of public space layouts by friction profile
3. **Design guidelines**: Spatial principles for caregiver-friendly public spaces
4. **Before/after comparisons**: How design modifications change friction

### 5.3 Transferable Knowledge

The output is not "this specific playground is good" but rather:
> "Public spaces with visibility characteristics A, B, C support low-friction supervision"

These principles can be applied by designers to evaluate and improve any public space.

---

## 6. Scope and Limitations

### In Scope
- Agent-based simulation of caregiver-child supervision in public spaces
- Visibility graph analysis of spatial configuration
- Parametric testing of spatial variations
- Extraction of generalizable design principles

### Out of Scope
- Empirical validation with human subjects (simulation only)
- Waiting points and errand-based friction (different problem)
- Multiple children or multiple caregivers (single dyad focus)
- Detailed play equipment design (focus on spatial layout)

### Limitations
- Agent behavior rules are simplified representations
- Friction metric is a proxy for actual supervision burden
- Generalizability requires testing across multiple configurations
- Real public spaces have factors beyond pure spatial configuration (shade, comfort, social presence)

---

## 7. Research Phases

### Phase 1: Foundation
- Literature review (space syntax, playground design, child-friendly cities)
- Define friction metric precisely
- Implement visibility graph analysis
- Build basic agent simulation

### Phase 2: Parametric Testing
- Create varied spatial configurations
- Run simulations, collect friction data
- Identify correlations with visibility metrics

### Phase 3: Typology Testing
- Model real public space typologies
- Compare friction profiles
- Validate parametric findings

### Phase 4: Synthesis
- Extract design principles
- Produce guidelines and portfolio materials
- Document methodology and findings

---

## 8. References

Hillier, B., & Hanson, J. (1984). *The Social Logic of Space*. Cambridge University Press.

Penn, A., & Turner, A. (2001). Space syntax based agent simulation. *Proceedings of the 1st International Conference on Pedestrian and Evacuation Dynamics*.

Turner, A., Doxa, M., O'Sullivan, D., & Penn, A. (2001). From isovists to visibility graphs: a methodology for the analysis of architectural space. *Environment and Planning B: Planning and Design*, 28(1), 103-121.

Benedikt, M. L. (1979). To take hold of space: isovists and isovist fields. *Environment and Planning B: Planning and Design*, 6(1), 47-65.

---

## 9. Fit with InfAU

This thesis combines:
- **Computational methods**: Visibility graph analysis, agent-based simulation
- **Architectural relevance**: Public space design, spatial configuration
- **Social dimension**: Caregiver-child relationship, inclusive design

The research produces both analytical insight (which spatial characteristics matter) and practical design knowledge (how to configure supervision-friendly spaces), suitable for academic contribution and architectural portfolio.
