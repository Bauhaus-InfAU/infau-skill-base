Hi Nourhan,

Following our discussion, here's a possible direction for your thesis that i came up with:

Focus on public spaces (playgrounds, plazas, parks) rather than errands. Apparent problem is that caregivers need to supervise children while resting or doing tasks. Poor spatial configuration forces them to reposition to maintain visual contact. This could be called something like "supervision friction" and it's determined by how the space is designed.

So the question could be: Which visibility graph metrics best predict caregiver-child supervision friction in public spaces, and what thresholds distinguish low-friction from high-friction configurations?

For computational approach could be tricky but potentially you would have to use visibility graph analysis (space syntax) combined with agent-based simulation, where:

- Child agent: Exploratory movement - moves toward visible open space (Penn & Turner's "random next step within view cone")
- Caregiver agent: Wants to stay stationary, but must reposition when child moves out of sight
- Friction metric: How often caregiver must move, how far they travel, how often visual contact breaks

You can read this paper to understand visibility graph analysis + agent-based simulation better:
https://discovery.ucl.ac.uk/id/eprint/2027/1/penn.pdf

Whole thing is quite interesting because usually agent based models focus on single entities.

If we try to imagine potential insight - simple answer is that open spaces are better (obviously).
What could be more interesting is which specific metric matters most, and what thresholds separate good from bad.
For example:
- Is isovist area more predictive than integration?
- Is there a minimum threshold, or is the relationship linear?
- Do metrics interact (e.g., high area but low integration still produces friction)?

This could result in catalog of principles of design for public spaces to minimize this friction, and potentially some draft designs that will be driven by maximizing metrics that are most important (but this is extra)

Just an idea, I would recommend you to run it by your future supervisor if you chose to go that route:)
