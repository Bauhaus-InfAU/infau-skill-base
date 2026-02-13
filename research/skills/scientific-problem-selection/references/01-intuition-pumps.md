# SKILL: Intuition Pumps for Scientific Problem Ideation

## Overview
This skill helps researchers generate high-quality research ideas by providing systematic prompts ("intuition pumps") and identifying common ideation traps. Based on the framework that most research projects involve **intervening in a system, measuring outcomes, and analyzing data**, this skill guides users through structured ideation that can significantly impact how they spend years of their career.

## Core Framework

### The Three Pillars of Research Work
Research advances generally fall into one of these categories, each with two dimensions:

**INTERVENTION**
- *Logic*: Novel ways to manipulate systems (e.g., using parametric design to explore form variations systematically)
- *Technology*: New tools for intervention (e.g., developing VR interfaces for participatory planning, creating AI-based layout generators)

**MEASUREMENT**
- *Logic*: Novel applications of existing measurement tools (e.g., using pedestrian simulation to evaluate urban designs)
- *Technology*: New measurement capabilities (e.g., developing real-time occupancy sensors, computer vision for behavior analysis)

**THEORY/COMPUTATION**
- *Logic*: Using computational tools to make discoveries (e.g., applying machine learning to identify patterns in urban mobility)
- *Technology*: Building new algorithms or models (e.g., developing optimization frameworks for sustainable building design)

Understanding which quadrant resonates with the user can help identify their niche and guide ideation.

## The Skill Workflow

### Phase 1: Initial Discovery Questions (5-10 minutes)

Before diving into intuition pumps, Claude should gather context by asking the user:

1. **What is the user's general research area or field?** (e.g., computational design, urban planning, sustainable building, participatory design, BIM)

2. **What excites the user most about research?**
   - Building new tools/technologies?
   - Discovering fundamental principles?
   - Solving practical problems?
   - Understanding dynamic processes?

3. **What are the user's existing strengths?** (Select all that apply)
   - Specific techniques (please list)
   - Computational skills
   - Access to unique systems/models/data
   - Domain expertise in a particular area

4. **Current constraints:**
   - Time horizon for this project? (months/years)
   - Resources available?
   - Must it connect to existing work, or can the user start fresh?

5. **On a scale of 1-5, how would the user rate their current idea?**
   - Likelihood of success: 1 (very risky) to 5 (highly feasible)
   - Potential impact: 1 (incremental) to 5 (transformative)

### Phase 2: Applying Intuition Pumps

Based on the user's responses, Claude should guide them through relevant intuition pumps from this list:

#### Intuition Pump #1: Make It Systematic
**Prompt:** Take any one-off analysis or design exploration and make it systematic.

**Examples:**
- Instead of designing one floor plan variant, generate and evaluate thousands of variations parametrically
- Instead of one case study → cross-city comparative analysis with standardized metrics
- Instead of evaluating one design → high-throughput simulation across parameter space

**Prompt for User:** What one-off study in your field could become a systematic survey?

#### Intuition Pump #2: Identify Technology Limitations
**Prompt:** What are the fundamental limitations of technologies you use? These limitations are opportunities.

**Examples:**
- BIM can't capture informal construction → develop methods for as-built documentation
- Simulation tools can't handle real-time user feedback → develop interactive simulation frameworks
- AI generators produce generic designs → develop culturally-aware generation methods
- We do single-objective optimization but design involves trade-offs → develop multi-objective frameworks

**Prompt for User:** What technology limitation frustrates you most? How might you turn that limitation into an opportunity?

#### Intuition Pump #3: The "I Can't Imagine" Test
**Prompt:** I can't imagine a future in which we don't have ____, but it doesn't exist yet.

**Examples:**
- The ability to automatically generate building designs that satisfy all codes and user preferences
- Real-time simulation of how proposed urban interventions affect pedestrian flow and social interaction
- AI that can translate community feedback directly into design parameters
- Lifecycle assessment tools integrated seamlessly into early-stage design

**Prompt for User:** What capability seems inevitable but doesn't exist yet in your field?

#### Intuition Pump #4: Static vs. Dynamic Understanding
**Prompt:** We understand spatial "parts lists" (rooms, buildings, streets) but rarely understand dynamic processes.

**Key Insight:** Most analyses are single-timepoint, single-condition format. But built environments are dynamic—like people flowing through stations or energy flowing through buildings.

**Examples:**
- Understanding how building occupancy patterns affect energy use throughout the day
- Time-resolved analysis of how neighborhoods evolve over decades
- Tracking how users adapt spaces over time post-occupancy

**Prompt for User:** What dynamic process in your field do we observe as static snapshots? How might you capture the full temporal or spatial dynamics?

#### Intuition Pump #5: Pick a New Axis
**Prompt:** We almost always use time as the x-axis for dynamic processes. What other coordinate could you use?

**Example:** Instead of time, use "distance from city center" or "building age" to analyze urban patterns

**Prompt for User:** What non-temporal coordinate could reveal new insights in your domain?

#### Intuition Pump #6: Create a Technology Platform
**Prompt:** Instead of answering one question, could you build a platform that enables many questions?

**Examples:**
- A parametric framework that generates floor plans for any residential typology
- AI that evaluates designs against multiple sustainability criteria simultaneously
- A VR platform for any type of participatory design workshop

**Prompt for User:** What platform would transform how your field asks questions?

#### Intuition Pump #7: Dogs That Don't Bark
**Prompt:** Why doesn't something exist or occur? Absence can be as informative as presence.

**Examples:**
- Why don't certain building types exist in certain climates?
- Why do some participatory planning methods fail to engage certain communities?
- Why aren't certain sustainable materials more widely adopted?

**Prompt for User:** What absence puzzles you in your field?

### Phase 3: Avoiding Common Traps

After generating ideas, we must evaluate them critically. Here are the most common traps:

#### Trap #1: The Truffle Hound
**Warning:** Don't become so good at one system or technique that you fail to ask questions of broader significance.

**Bad:** "How does algorithm X perform on dataset Y?"
**Better:** "What design principles emerge from applying computational optimization to residential layouts?"

**Self-Check:** Is the question driven by genuine curiosity or by what the user is technically capable of?

#### Trap #2: Applying Existing Tool to New Domain
**Warning:** "Let's apply deep learning to my design problem" can be valuable but risks crowding and incrementalism.

**When It Works:** The user is enabling a field that truly needs this capability
**When It Fails:** The tool is already widely applied; the contribution will be incremental

**Self-Check:** Will this tool application open new research questions, or just extend existing observations? Claude should help the user evaluate this honestly.

#### Trap #3: Jumping on the First Idea
**Warning:** Treating ideas with reverence instead of skepticism. Confirmation bias sets in quickly.

**Better Approach:** Users should treat new ideas like leeches trying to steal their time. Look for the warts. Develop several ideas in parallel and comparison shop.

**Self-Check:** Has the user critically evaluated at least 3-5 alternative approaches?

#### Trap #4: Too Many Fixed Parameters
**Warning:** Fixing too many parameters at the outset creates a poor technique-application match.

**Example of Over-Constraining:** "I will use graph neural networks to optimize timber connections in modular housing."
- This fixes: technique (GNN), material (timber), and typology (modular housing)
- If any assumption fails, the project fails

**Self-Check:** Has the user fixed more than 2 parameters before starting?

#### Trap #5: Too Few Fixed Parameters
**Warning:** "I want to do impactful work in computational design" → paralysis

**Resolution:** Constraints engender creativity. Fix ONE parameter at a time and let creativity flow.

**Self-Check:** Does the user have at least one concrete constraint to work with?

### Phase 4: Literature Integration

To ensure the idea has appropriate scope and hasn't been thoroughly explored, Claude should ask:

1. **What are 2-3 key questions or gaps the idea addresses?**

2. **What should be searched in academic databases to:**
   - Understand the current state of the field?
   - Identify related approaches?
   - Find empirical knowledge from adjacent domains that could inform the approach?

Claude should help search using:
- Google Scholar / Semantic Scholar for broad academic coverage
- arXiv (cs.CV, cs.AI, cs.GR) for computational methods
- JSTOR / Web of Science for architectural and urban research
- ResearchGate for accessing full-text papers

Use these searches to:
- Assess how general/specific the problem is
- Identify relevant methodological advances
- Find analogous systems or approaches in other fields
- Determine the degree of competition

### Phase 5: Idea Refinement and Output

After working through intuition pumps, avoiding traps, and reviewing literature, Claude should help the user:

1. **Crystallize the Idea:**
   - Research question
   - Technical approach (intervention/measurement/theory: logic vs. technology)
   - What's novel about this angle?

2. **Articulate Fixed vs. Floating Parameters:**
   - What MUST remain constant in the approach?
   - What can be flexible if obstacles arise?

3. **Identify Key Assumptions:**
   - What must be true for this to work?
   - Which assumptions are about the domain vs. technology capabilities?

4. **Sketch Alternative Paths:**
   - If the primary approach fails, what's Plan B?
   - Can the project be designed to succeed regardless of outcome?

## Output Deliverable

At the end of this skill, Claude should produce a **2-page Problem Ideation Document** containing:

### Page 1: Core Idea
- **Title:** Concise project name
- **The Question:** What research question is being asked?
- **The Approach:** How will it be answered? (Specify intervention/measurement/computation: logic vs. technology)
- **What's Novel:** The unique angle
- **Why It Matters:** Potential impact (generality × learning, or technology development)
- **Intuition Pump(s) Used:** Which prompted this idea

### Page 2: Critical Analysis
- **Fixed vs. Floating Parameters:**
  - Fixed: What must stay constant
  - Floating: What can adapt

- **Key Assumptions & Risk Assessment:**
  - Domain assumptions (risk level 1-5)
  - Technical assumptions (risk level 1-5)

- **Traps Avoided:** Which pitfalls were navigated around?

- **Alternative Approaches:** Plan B and Plan C

- **Literature Context:**
  - 3-5 key papers that inform or relate to this work
  - Degree of competition (low/medium/high)
  - The user's edge/advantage

- **Next Steps:** First 3 concrete studies or analyses

## Key Principles to Remember

1. **Reversal of Polarity:** Treat ideas with skepticism, not reverence. Look for flaws before falling in love.

2. **Comparison Shopping:** Develop multiple ideas in parallel. The act of comparison improves decision-making.

3. **Fix One Parameter at a Time:** Constraints engender creativity, but too many constraints prevent it.

4. **Think in Ensembles:** The user is picking a family of possible projects, not a singular path. Flexibility is essential.

5. **Balance Logic and Technology:** Novel insights can come from new tools OR clever application of existing tools.

6. **Systematic Over One-Off:** High-throughput and systematic approaches often reveal more than single observations.

7. **Dynamic Over Static:** Built environments are dynamic. How can process be captured rather than snapshot?

## Getting Started

When the user is ready, Claude should guide them through the Phase 1 questions to begin the systematic ideation process. The key message: spending extra time on problem choice is the highest-leverage activity in research. A well-chosen problem executed reasonably well will have more impact than a mediocre problem executed brilliantly.

---

*This skill is based on the problem choice framework developed by Michael A. Fischbach and Christopher T. Walsh, as described in "Problem choice and decision trees in science and engineering" (Cell, 2024).*
