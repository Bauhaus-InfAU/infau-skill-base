<!-- Page 1 -->

Space Syntax Based Agent Simulation  
Alan Penn and Alasdair Turner 
Bartlett School of Graduate Studies, UCL, Gower Street, London, WC1E 6BT, UK. a.penn@ucl.ac.uk; a.turner@ucl.ac.uk; www.vr.ucl.ac.uk; www.spacesyntax.com

Space syntax derives from a set of analytic measures of configuration that have been shown to correlate well with how people move through and use buildings and urban environments. Space syntax represents the open space of an environment in terms of the intervisibility of points in space. The measures are thus purely configurational, and take no account of attractors, nor do they make any assumptions about origins and destinations or path planning.  Space syntax has found that, despite many proposed higher-level cognitive models, there appears to be a fundamental process that informs human and social usage of an environment. In this paper we describe an exosomatic visual architecture, based on space syntax visibility graphs, giving many agents simultaneous access to the same pre-processed information about the configuration of a space layout. Results of experiments in a simulated retail environment show that a surprisingly simple ‘random next step’ based rule outperforms a more complex ‘destination based’ rule in reproducing observed human movement behaviour. We conclude that the effects of spatial configuration on movement patterns that space syntax studies have found are consistent with a model of individual decision behaviour based on the spatial affordances offered by the morphology of the local visual field. 1. Introduction Understanding the way in which pedestrians move around their environment is important for predicting congestion, for evacuation planning, pedestrian traffic and crowd control, as well as assessment of the social and economic function of buildings and urban layouts.  In addition, there has been recent interest generated in the computer graphics community due to the maturing of large-scale visualisation using human avatars. Two main approaches have been developed to address the issue of pedestrian movement analysis, modelling and simulation. These might be defined simply as ‘configurational analysis’ – to cover methods based on representing and quantifying aspects of the spatial configuration or morphology of the environment within which movement takes place, and ‘pedestrian simulation’ – to cover methods that seek to represent the individual pedestrian or the pedestrian population.  

---

<!-- Page 2 -->

Helbing et al. [1] review various methods of pedestrian simulation in detail. They categorise approaches into two broad groups: large-scale urban simulation and low-level building micro-simulation. For urban modelling, pedestrian movement may be incorporated into Land-Use and Transportation Models (LUTMs), the chief example being TRANSIMS [2,3], where tens of thousands of agent journeys may be simulated concurrently, while small-scale urban and building micro-simulation models are constructed for fire evacuation (for example, Drager et al. [4], Galea et al. [5]) and crowding situations (for example, Helbing et al. [6]).  At both levels of resolution, the researcher explicitly chooses the origin-destination pairs for agents, albeit at very different scales. In LUTMs, the movement patterns are calibrated using empirical data, while at the micro-simulation level ideal paths to the destination are generally chosen. Although there are sophisticated methods for determining route choice behaviour (see for example Borgers and Timmermans [7,8] for work in this area), the missing link appears to be an intermediate level of model or simulation where the origin-destination pairs are not pre-programmed, and where there is neither calibration nor a predefined path rationale. There is currently much interest focussed on this aspect of simulation of ‘unprogrammed’ movement, especially for applications where movement is expected to be exploratory rather than purposive, or where the population might be expected to have a wide variety of purposes and data on these are lacking.   These issues are being approached in different ways by researchers spanning computer graphics and planning. Kerridge [9] has proposed agents with limited environmental perception of their immediate vicinity, by superimposing a grid on space and organising obstructions, so that an agent can employ local behaviour rules. For vehicular micro-simulations these rules include minimum car-to-car separations and speed matching in the one-dimensional queue, for pedestrians similar rules control relative positions in two dimensions.  In the field of computer graphics, Thomas and Donikian [10] apply agents that have a ground level knowledge of the environment through a combination of a visibility graph joining sight-lines between key locations and Voronoi diagrams defining routes around the key locations. The agents may then roughly follow the edges of these graphs to provide human-like behaviour. However, the aims of the computer graphics community are somewhat different to those of the simulation and modelling communities in that the requirements for ‘believable’ behaviour simulations are more qualitative than quantitative.    The main methods of configurational analysis are those based on space syntax analysis defined by Hillier and Hanson [11].  These methods differ substantially in both their aims and their methodology from the simulation and modelling approaches outlined above. Initially, space syntax methods were developed in order to allow architectural space to be represented and its pattern properties quantified so that comparisons could be made between differently designed buildings or urban areas. The aim of the research was to develop an understanding of the way that spatial design and social function were related.  It was soon found that a primary effect of spatial configuration on social function resulted from the way that space patterns determined pedestrian movement patterns and so co-presence between people in space [12,13]. These 

---

<!-- Page 3 -->

findings show that between 50 and 80% of the variance in pedestrian flows from location to location in an environment can be explained in terms of variations in configurational properties of those locations in the network. Since co-presence is a prerequisite for both communication and transaction in socio-economic life, space syntax research suggests that spatial configuration itself plays a critical role in determining this, but until recently it has been unclear how mechanisms at the level of the individual might give rise to these population level effects.  With the exception of some previous research by one of us [14] relatively little effort has been made until now to merge syntax analysis with agent simulation, however, in view of the need to investigate individual level mechanisms that might give rise to the observed population level behaviours we have recently returned to simulation methods [15].  In this paper, we describe recent research in which space syntax is being incorporated into agent micro-simulation models for pedestrian movement. In the following section, we discuss the background of space syntax research to date, and contrast it to the assumptions made by current modelling and simulation approaches. We describe a recent study of a department store by way of example of the application of space syntax methods.  Then we turn our attention to how space syntax can be used as the basis for an agent simulation in the form of an exosomatic visual architecture or ‘EVA’. An EVA is a computer architecture that contains pre-processed visual information about the environment which agents access via a lookup table. We discuss the implementation of this architecture in our computer simulation ‘EVAS’ and show how this is being applied to simulate shopper movement patterns. We conclude with a discussion of the way this architecture, on the surface no more than an elegant algorithm to provide agents with elementary vision, takes us back to the principles of space syntax, and possibly offers an insight into the way individual mechanisms give rise to population level effects. 2. Space Syntax analysis Modelling and simulation approaches to human movement have tended to make two main assumptions. First that movement is purposive, and second that humans have a good (often perfect) knowledge of the environment that they are traversing. Purposive movement results in models that explicitly represent the origins and destinations, or the attractors and generators of movement. The assumption of perfect knowledge results in rational choice and assignment models in which agents’ route choice is either predefined, or can be assigned dynamically in order to optimise some measure of cost such as travel time.  The findings of research using space syntax techniques raise doubts about the central role both of these assumptions play in our understanding of pedestrian movement behaviour.    Space syntax methods were first developed to compare the similarities and differences between built environments at both building interior and urban neighbourhood scale.  The plan of an environment is represented as a map in which all longest lines of sight are drawn. This map is then translated into a graph in which a line is represented as a node and intersections between lines are shown as links between nodes. Measures of 

---

<!-- Page 4 -->

the graph are made that can then be assigned back as variables associated with the location of each line in the original map (Fig. 1). Research using these techniques has found that both pedestrian and vehicular movement rates are strongly correlated with certain measures of the graph of the line map (Fig. 2). Since the representation captures nothing except the geometry of the configuration of space in the environment, its ability to predict movement rates brings into question the degree to which the location and strength of attractors or generators of movement are central to observed movement behaviour patterns. Hillier et al. have argued that the logical view is that configuration leads to a pattern of movement or a ‘passing trade’, this then attracts shops to locations where they can take advantage of the passing trade, and the shops then attract additional people [13]. This causal chain involves a feedback loop that Hillier et al. suggest is fundamental to the evolution of urban form and the aggregation of land uses and land values. However it is also clear that the driver for this causal chain is the configuration of space, since countless examples of the failure of shops placed at the heart of modern housing estates in order to ‘enliven’ them show that the attractor effects of specific land uses fail to overcome spatial isolation.   Figure 1: Line map analysis of London, the colours code from red through blue in the spectrum, for shallow to deep mean depth in the graph. 

---

<!-- Page 5 -->

More recently new methods of representation have been developed which replace the ‘line map’ with a grid of points within open space, and build a visibility graph in which points are linked if they are visible to each other  [16]. Measures of the global properties of the graph proceed as before. Visibility Graph Analysis (VGA) of this sort gives a much higher resolution analysis of the configurational properties of open space, and in certain cases has been found to significantly better predict movement patterns than the previous line based analysis.    1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
8
9
1 0
F i t t e d  R A 3  a n d  n e t  C a p a c i t y
S q r t  o f  S q r t  o f  a l l v e h - b u s / p h
y  =  . 9 7 x  -  1 . 0 5 6 ,  R - s q u a r e d :  . 8 2 8
- 1
0
1
2
3
4
5
6
7
8
1 . 2 5
1 . 5
1 . 7 5
2
2 . 2 5
2 . 5
2 . 7 5
3
3 . 2 5
3 . 5
r a 5 p e d L o n d o n
l n ( x )  o f  a d u l t s / p h
y  =  2 . 2 8 6 x  -  . 5 5 9 ,  R - s q u a r e d :  . 5 2 7
Figure 2: (Left) Correlation between vehicular flow rates and a fitted variable consisting of radius 3 mean depth in the graph, and net road width in metres (r2=.83 n=405, p<.0001); (Right) Correlation between radius 5 mean depth and adult pedestrian movement per hour (r2=.53, n=466, p<.0001), both scatters are for all road segments in five study areas in central London.  A specific example of this is given by a recent study of shopper behaviour in a large London department store (Fig. 3). In this study we were asked to investigate the effects of congestion on sales and till receipts. The problem faced by the store owners was simple. The number of shoppers entering the store on a Saturday was double that on a weekday, however the till receipts only increased by 60%.  It was thought that the problem was due to a reduction in ‘passing trade’ within the store caused by congestion reducing movement.  In our study we carried out detailed observations of shopper movement and stopping patterns, stalking individual customers, and observing average movement rates in all parts of the store. We also observed congestion patterns and browsing and shopping behaviour. All of these data were then put together with information on sales and receipts from the Electronic Point of Sale (EPOS) system and with the VGA data on the configuration of the building plan, and analysed statistically.   Our findings were very clear. The measure of mean depth in the VGA is strongly correlated with observed movement flows (Fig. 4 left), however the number of items sold at a till is not directly correlated with movement past the till, but is correlated with static occupancy in the vicinity of the till (Fig. 4 right). Further investigation allowed us to develop a better understanding of what contributed to stopping behaviour, which was the key to selling goods. Static occupancy was found to be associated with two factors, levels of movement and the measure of the linear metres of goods on display in the immediate area. 

---

<!-- Page 6 -->

 Figure 3: VGA analysis of a London department store. Colours signify mean depth in the graph, red is shallow, blue is deep. 0
2 0 0
4 0 0
6 0 0
8 0 0
1 0 0 0
1 2 0 0
T r a n s a c t i o n s  ( S a t u r d a y )
0
4 0
8 0
1 2 0
1 6 0
2 0 0
s t a t i c  p e o p l e  a t  c o u n t e r s
y  =  1 6 6 . 8 8 8  +  3 . 7 1 6  *  x ;  R ^ 2  =  . 5 4 3
0
1 0 0 0
2 0 0 0
3 0 0 0
4 0 0 0
M o v e m e n t  ( S a t u r d a y )
. 2 4
. 2 6
. 2 8
. 3
. 3 2
. 3 4
. 3 6
. 3 8
I s o v i s t  I n t e g r a t i o n
y  =  - 3 3 2 6  +  1 6 7 8 1  *  x   ;  R ^ 2  =  . 5 7 9
Figure 4, Left: Correlation between observed movement mean depth in the VGA (r2=.58, p<.0001); Right: Correlation between number of transactions and numbers of static people within a buffer of the counter (r2=.54, p<.0001).  This was an important finding since there are two camps amongst retailers. The ‘stack it high and sell it cheap’ camp is founded on the notion that the goods and price competition attract shoppers, whilst the ‘passing trade’ camp is founded on the notion that movement, and therefore circulation space, is fundamental. What we found suggests that both camps are in fact correct. A shop needs a constant supply of moving 

---

<!-- Page 7 -->

people past its goods, and the spatial layout of the store is a critical component in achieving this, however movement alone does not make a sale. In order to sell one needs to stop people so that they can browse and select what they want to buy. Stopping people depends on the supply of people in the first place (and so on movement) and on the quantity of goods on display.   These findings allowed us to clarify the nature of the problem faced by the store management. First, they were correct that congestion was having an effect, however, they were wrong about the mechanism involved. It was not that congestion stopped movement and so reduced the passing trade. It was something like the opposite: congestion appeared to be stopping people from stopping – the pressure of congestion kept people moving and so interfered with the conversion of passers -by into shoppers. Thus, determining where crowding will occur is of prime importance in analysis of shopping environments.   It is important to note that these findings are analytic rather than simulation based, and that the analysis of spatial configuration using the VGA method provides a good predictive model for movement. This account of movement incorporates only information on the configuration of space, and has no input on the location of attractors or generators of movement, no representation of individuals and their intentions, or of origins and destinations. However, as soon as one wants to take account of the way that stopping behaviour occurs, or to go a step further and look at the effects of congestion on stopping and shopping behaviour, one needs to simulate individual behaviour and interactions. For this reason we have now gone on to develop micro-simulations of individual movement behaviour specifically aimed at situations, such as shopping, where people browse or have multiple destinations, rather than move on routes with well characterised origins and destinations. 3. Implementation Our simulation approach starts from what we have found in our space syntax based analytic studies. This is that movement patterns are strongly affected by spatial configuration. We have therefore developed an agent simulation architecture based on the visibility graph analysis, in which agents have access to pre-computed information about what is visible from any given location in the map. In addition information can be attached to the nodes of the graph describing attributes of the visible nodes. Amongst these attributes are space syntax measures of the configuration properties of the graph at each node, but we can also attribute information regarding goods on display or other static aspects of the environment. We call this architecture an ‘exosomatic visual architecture’ since it in effect provides agents with a form of exosomatic (outside the body) memory common to all agents in an environment [17].  The idea of pre-computing a look-up table to represent static parts of the environment has been developed by others (see for example Tu [18]). However, the system developed here differs in that it uses the visibility graph as the basis for the look-up table, and for computation of global spatial relations in the environment. The key 

---

<!-- Page 8 -->

factor here is that by using the visibility graph and by computing metrics of that graph (including those used in the space syntax approach), the look-up table encodes not only object locations, but also information about the accessibility structure of the environment. This means that in effect the agents can infer the affordances of the environment, or at least information on the global spatial relations of different locations vis ible from their current position in the environment.   This allows rules governing agent movement not only to read local information from the look-up table, but also to use that to fulfil global intentions. It is this property that converts the look-up table architecture from a method for representing agent perception to one for representing a form of agent memory. Perception is entirely local and a look-up table (such as [18] cited above) that gives information only about what can be seen directly, essentially only replaces perception. However, in this system the visibility graph allows the look-up table to do three additional things.  Firstly, it can store extended local, telling the agent about spaces within their field of view with high potential for further movement.  Secondly, it can store global information – for example, the global mean depth of all locations visible from the agent’s point of view.  Thirdly, it allows the entire graph to be traversed, and so for the computation of rational routes to remote locations.    By giving agents access to the VGA graph and associated attribute data we are effectively giving them a form of vision, but without the computational overhead generally associated with even rudimentary forms of agent perception [19]. However, since the graph captures global information we are also giving them a form of cognition or memory. Our implementation of this architecture uses a ‘bin’ representation of the environment. The visibility graph is used to allocate point values to locations, and also provides a technique to retrieve data quickly for the visual cone of an agent.  For example, for each location (each node in the graph) one stores a set of 'bins', containing the nodes visible in different directions (see Fig 5).  Each bin simply contains a set of reference numbers, indicating other nodes. Our current implementation has 32 bins giving the agents a visual acuity of about 11°.  By selecting the number of bins an agent has access to one can give the agent a variable cone of vision.   As well as a set of bins at each location, a set of attributes is stored for each location, and these attributes may be retrieved with the bin information. One attribute of the visibility graph that appears to be potentially useful is the ‘clustering coefficient’. The clustering coefficient is a simple measure of a graph, first proposed by Watts and Strogatz [20] to measure ‘small world’ social networks.  If one defines the ‘neighbourhood’ of a node in the graph to be the set of nodes immediately connected by a link to the current node, then the clustering coefficient is the number of links between all members of the neighbourhood divided by the total number of links that could possibly exist given that number of nodes.  The clustering coefficient in a visibility graph gives an idea of how much visual information is lost when one moves away from a specific location to any neighbouring location. We have previously 

---

<!-- Page 9 -->

suggested therefore that it gives a measure of ‘junctioness’ of a location [16]. We propose that humans are probably well able to recognise junctions (from years of ‘training’ of what a junction looks like).  We also suspect that humans typically search for promising junctions when seeking out new parts of an environment. Other research in this field by Conroy has found that human subjects in immersive virtual environments pause and scan the environment at junctions, but move more directly on segments of the environment between junctions [21]. Hence, we propose that an agent that searches out junctions is likely to resemble a human moving around a layout in exploratory mode. Figure 5: Using the visibility graph to select possible locations for a next target destination.  Using the clustering coefficient to guide an agent eliminates the need for the agent to have a highly developed cognitive map of an environment — all the agent has to do is be able to recognise junctions and to have a rough map of say, previously visited areas, for it to behave in a sensible exploratory fashion. In fact this seems to provide a system that will achieve globally sensible and rational looking movement patterns while employing minimal rule sets.   Of course, the clustering coefficient is just one measure of a visibility graph, and many other metrics may be used to determine junctioness, or any other feature of the space that might be considered important for agent wayfinding. We make no assertion here that the way that real humans actually wayfind is associated with either clustering coefficients or with the visibility graph. However, first we must investigate whether a 

---

<!-- Page 10 -->

rule as simple as that described above produces agent behaviour that is in any way similar to real observed human movement patterns. 4. Results Figure 6 illustrates the cumulative movement traces for real observed shoppers in the department store described above. These observations, together with sampled shopper flow counts at 49 ‘observation gate’ locations concentrated within the ‘food halls’ area of the store (illustrated in Fig 6.) are used to evaluate agent performance in our simulations. For each ‘gate’ location the flow of shoppers and of agents is compared statistically. Figure 7 shows the correlation between agent movement and observed shopper movement rates, using agents  that headed for areas of low clustering coefficient as described above. Although there is a positive trend, the correlation is disappointing at r2 = .13.   In view of this poor result we decided to try a simpler method similar to that devised by Mottram [15] for animating virtual environments with moving people. In our implementation a node is selected at random from all those within the agent’s 170° view cone. Their next destination is selected at random from all visible nodes within that view cone. A new destination node is selected every few steps giving an opportunity to change direction. Figure 8 shows the rule set in diagrammatic form.  Agents were loaded into the system at the main entrances to the building, using observed flows of people to weight the loading at the different entrances. One agent enters every other iteration of the system. Each agent is removed after 2000 generations. The system was run for 10000 iterations, but the first 2000 iterations were discarded to allow the system to reach a steady state.  The results of this experiment were far more interesting. Figure 9 is a scattergram showing the correlation between agents and observed shoppers at r2 = .56. This is a surprisingly powerful result given that the rule is essentially random, and no account is taken in the simulation of the attractor properties of goods in the store.   Figure 10 shows the cumulative agent traces for the EVAS agents using the random next-step method, and a comparison with Figure 6 shows considerable similarity to the observed real movement patterns. In this illustration the red end of the spectrum denotes high and the blue end low agent flows. At a qualitative level the average flow patterns are highly convincing, and even isolate various local characteristics visible in the observed human behaviour in Figure 6. 

---

<!-- Page 11 -->

 Figure 6: Observed movement trails for shoppers on a Saturday in the ‘food halls’ area of the store. y = 0.9527x
R2 = 0.1309
0
1000
2000
3000
4000
5000
6000
0
1000
2000
3000
4000
5000
Actual movement (gate counts per hour)
Generated movement
 Figure 7: The correlation between agent (generated) movement using agents with the clustering coefficient rule, and observed shopper movement in the department store (r2=.13, n=49, p<.05).  

---

<!-- Page 12 -->

Select a visible destination  Select a new visible destination from the field of view   Take a step towards the destination  Take a side step  Is a step towards the destination possible?  Yes  No  Have less than n-steps been taken?  Yes  No  Is a side step possible?  Yes  No   Figure 8: Flow-chart of the agent decision process for the random next step rule.
 y = 0.9878x
R2 = 0.5599
0
1000
2000
3000
4000
5000
6000
0
1000
2000
3000
4000
5000
Actual movement (gate counts per hour)
Generated movemen
 Figure 9: The correlation between agent (generated) movement and observed shopper movement in the department store (r2=.56, n=49, p<.001). 

---

<!-- Page 13 -->

 Figure 10: Agent movement density after 10 000 agent moves using the random next step rule.  Each grid square is incremented every time an agent steps on it.   5. Discussion These results were simpler than anticipated. Although we expected agents without specific goals to correlate positively with observed human behaviour in an exploratory shopping environment, we were expecting that some form of relatively local forward planning would be taking place. For this reason we chose to test the ‘clustering coefficient’ method as a proxy for detecting junctions, and to use these to provide the immediate ‘next step’ goal for agents. However the finding that a much simpler ‘random’ next step rule significantly outperformed the ‘clustering’ rule, and that it provides a relatively good correlation with observed human movement patterns, is surprising. Initial results of experiments applying agents using the same rules to two different building morphologies and types, an art gallery and a supermarket, have shown similar degrees of correlation to observed human movement flows, and it seems 

---

<!-- Page 14 -->

that approximately 50% of the variance in flows can be accounted for by the dynamics of this agent simulation.  It is clear that the way the random next step rule works is to lead agents to continue moving forwards along linear spaces such as corridors or aisles when the majority of visible nodes within their view cone lie ahead. If an agent comes up against a wall the majority of visible nodes will lie to the right and to the left, and so it is likely that the next step chosen at random will involve a turn one way or the other.  If the agent comes to a cross-road junction, the majority of nodes will lie in three predominant directions, left, right and ahead. Since the view cone is 170° the probability involved in the random selection of visible nodes depends almost entirely on the extent of the view in each of those three directions. Of course, since the selection of the next heading is random, there is a great deal of variation in individual agent behaviour at any step, however, since the selection of the heading is repeated every three steps, the laws of probability smooth out these variations, and what emerges is a pattern of movement very closely related to the linear arrangement of space in the environment, including highest flows on corridors, and lower flows in more broken-up areas.  These findings allow us to draw three tentative conclusions. 1. The affordance offered by an environment for human movement is location and orientation dependent. As an agent moves through an environment their local perception of choices available for movement is directly related to their current location and heading and thus changes at each step. In other words, a fixed environment is objectively different from different points of view; 2. The perceptual range for humans is large scale. By this we mean that, unlike the motion of gas molecules which are more or less locally determined by interaction with their immediate neighbours, humans have long distance vision and make next step decisions based on the longer distance affordances of the environment; this leads to 3. The spatial morphology of the environment acts on human movement mainly through its linear arrangement. Linearly arranged spaces offer more possible ‘next step’ destinations along their length than across their width, and thus they tend to gather and organise linear movement patterns.  This last conclusion brings us back to one of the most surprising findings of space syntax research: the empirical success of the ‘line map’ representation in explaining human movement patterns. One of us has argued elsewhere [22] that human cognition is likely to employ a representation of linear spatial elements since these elements are the least subject to changes during forward movement and so a compressed cognitive representation is likely to store linear spatial elements as single entities. The findings presented here however, suggest a still simpler explanation for the observed linear logic of human movement behaviour. It is possible that the effective space in which agents with long distance vision make immediate ‘next step’ decisions that guide movement is ‘collapsed’ over distance itself: we choose our immediate next destination from the full range of locations that we can currently see, without particular consideration for how far away they are. We then continually review these decisions as we move. When we are moving along a linear corridor space most 

---

<!-- Page 15 -->

opportunities are likely to lie ahead, however when we reach a junction the opportunities are defined by the morphology of the local visual field. Conroy found that it was exactly at these junction locations that people paused and looked around before moving on [21], suggesting that it was at these locations that the cognitive load of decision making required a slower pace of movement and gathering of additional information. Recent work by the authors, currently in preparation, suggests  a mean of three steps before the direction review may be optimal in the EVAS agent simulation.  In conclusion, our discussion suggests that the next steps in the development of the agent simulation could also be simpler than originally anticipated. These next steps address two factors, first the inclusion of stopping and shopping behaviour, and second the inclusion of crowding and congestion effects. We anticipate that, taken together, the feedback effects of stopping and congestion on agent movement flows will further improve the correlation with observed shopper movement patterns.  References 1. D. Helbing, P. Molnár, I. J. Karkas and K. Bolay, Self-organizing pedestrian movement, Environment and Planning B 28, forthcoming (2001). 2. R. J. Beckman, et al. The TRansportation ANalysis SIMulation system (TRANSIMS): The Dallas-Ft. Worth case study.  Los Alamos Unclassified Report LA–UR–97–4502, Los Alamos National Laboratory (1997). 3. J. L. Casti, Would Be Worlds: How Simulation is Changing the Frontiers of Science (John Wiley & Sons Inc., New York, 1997). 4. K. H. Drager, G. Løvås, J. Wiklund, H. Soma, D. Duong, A. Violas and V. Lanères, EVACSIM — a comprehensive evacuation simulation tool, in Proc. 1992 Emergency Mangement and Engineering Conference, 101–108 (1992). 5. E. R. Galea, M. Owen and P. J. Lawrence, Computer modelling of human behaviour in aircraft fire accidents, Toxicology 115, 63–78 (1996). 6. D. Helbing and P. Molnár, Self-organization phenomena in pedestrian crowds, in F. Schweitzer, ed. Self-Organisation of Complex Structures: From Individual to Collective Dynamics (Gordon & Beach, London, UK, 1997) 7. A. Borgers and H. Timmermans, A model of pedestiran route choice and demand for retail facilities within inner-city shopping areas, Geographical Analysis 18, 115–128 (1986). 8. A. Borgers and H. Timmermans, City centre entry points, store location patterns and pedestrian route choice behaviour: a microlevel simulation model, Socio-
Economic Planning Science 20, 25–31 (1986). 9. J. Kerridge and N. McNair, PEDFLOW — a system for modelling pedestrian movement in occam, in B. M. Cook, ed., Architectures, Languages and Techniques (IOS Press, Amsterdam, 1999). 

---

<!-- Page 16 -->

10. G. Thomas and S. Donikian, Modelling virtual cities dedicated to behavioural animation, Computer Graphics Forum 19, C71–C80 (2000). 11. B. Hillier and J. Hanson, The Social Logic of Space (CUP, Cambridge, 1984) 12. B. Hillier, R. Burdett, J. Peponis and A. Penn, Creating life, or, does architecture determine anything? Architecture and Behaviour/Architecture et Comportement, 3(3) 233–250 (1987). 13. B. Hillier, A. Penn, J. Hanson, T. Grajewski and J. Xu, Natural movement; or, configuration and attraction in urban space use, Environment and Planning B: Planning and Design, 20, 29-66 (1993). 14. A. Penn and N. Dalton, The Architecture of Society: stochastic simulation of urban movement, Ch 5, pp85-126, in N. Gilbert and J. Doran, ed.s, Simulating Society: The computer simulation of social phenomena (UCL Press, London, 1994). 15. C. Mottram, A. Penn, R. Conroy and A. Turner,1999, Virtual beings: emergence of population level movement behaviours from individual rulesets, in the Proceedings of the Second International Space Syntax Symposium, Universidad de Brasil, Brazil, 1, 10, (1999). 16. A. Turner, M. Doxa, D. O’Sullivan and A. Penn, From isovists to visibility graphs: a methodology for the analysis of architectural space, Environment and Planning B 28(1), 103–121 (2001). 17. A. Penn and A. Turner, System for the intelligent modelling of public spaces, UK Patent Office, application #0020850.4, 28/8/2000, (2000). 18. X. Tu, Artificial Animals for Computer Animation: Biomechanics, Locomotion, Perception, and Behaviour (LNCS 1635, Springer-Verlag, Berlin, 1999). 19. I. A. Bachelder and A. M. Waxman, Mobile robot visual mapping and localisation: a view-based neurocomputational architecture that emulates hippocampal place learning, Neural Networks 7(6/7), 1083–1099 (1994) 20. D. J. Watts and S. H. Strogatz, Collective dynamics of ‘small-world’ networks.  Nature 393, 440–442 (1998). 21. R. A. Conroy, Spatial Navigation in Immersive Virtual Environments, PhD Thesis, University of London, (2001). 22. A. Penn, Space Syntax and Cognition: or why the axial line?, Proceedings of the Third Space Syntax Symposium, Georgia Tech., Atlanta GA, May 2001, forthcoming (2001). The authors should like to acknowledge funding from the UK’s Office of Science and Technology Foresight Challenge Award VR Centre for the Built Environment and Platform funding from the UK’s Engineering and Physical Sciences Research Council. 