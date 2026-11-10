---
title: ATAM Phase 1 and 2 Activities
slug: atam-phase-1-and-2-activities
category: evaluation
kind: method
summary: An ATAM evaluation is a short series of steps, usually three to four days. Participants present
  the method and the architecture, analyze it against scenarios, and end with a report of findings.
arc42:
- 10
- 11
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- atam-phase-1-architecture-centric-analysis
- atam-roles
- atam-results
- sensitivity-point
- trade-off-point
- quality-attribute-scenario
- atam-findings-risks-non-risks-sensitivity-points-and-trade-offs
checks:
- The evaluation plan allows about three to four days.
- The review team, the project team and stakeholder representatives all take part.
- The utility tree reaches the level of scenarios with stimuli, responses and priorities.
- Risks, sensitivity points and trade-off points are recorded when approaches are analyzed.
- Results are delivered as an out-brief and/or written report, with risks grouped into themes.
sources:
- url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  title: Architecture Tradeoff Analysis Method® Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://cio-wiki.org/wiki/Architecture_Tradeoff_Analysis_Method_(ATAM)
  title: Architecture Tradeoff Analysis Method (ATAM) - CIO Wiki
  site: cio-wiki.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

ATAM is the Architecture Tradeoff Analysis Method (see Architecture Tradeoff Analysis Method (ATAM)). It is a structured review of an architecture. An evaluation typically takes three to four days.

**Who takes part.** ATAM brings together three groups: the review team, the project team and stakeholder representatives. See ATAM Roles for details.

**The steps, in order.**

1. **Present the method.** The evaluation leader explains how the evaluation works to everyone assembled.
2. **Present the architecture.** In step 3 the architect describes the architecture. The focus is on how it meets the business drivers, meaning the business goals behind the system.
3. **Identify architectural approaches.** In step 4 the architect names the approaches used. They are only identified here. They are not analyzed yet.
4. **Build the utility tree.** This tree starts with quality requirements at the top. It is refined down to scenarios. Each scenario has a stimulus (what happens) and a response (what the system should do). The scenarios are then prioritized. A measurement quantifies each response. See Quality Attribute Scenario.
5. **Analyze the approaches.** In step 6 the team examines the approaches. Three kinds of findings appear here: architectural risks, sensitivity points and trade-off points. A sensitivity point is an architecture feature that affects the response to a quality requirement. See Sensitivity Point and Trade-off Point.
6. **Brainstorm scenarios.** In step 7 the entire stakeholder group contributes a larger set of scenarios.
7. **Test the earlier analysis.** In step 8 the prioritized scenarios act as test cases. They confirm the analysis done so far.
8. **Present the results.** In step 9 the ATAM team presents its findings to the stakeholders. The output is an out-brief presentation, a written report, or both.

**What the results contain.** The risks are synthesized into risk themes. These themes show how the risks threaten the business goals of the system. See ATAM Results and ATAM Findings: Risks, Non-Risks, Sensitivity Points and Trade-off Points.

## Example

A team evaluates an online shop. The architect explains how the design supports the goal of handling holiday sales. The group builds a tree with "performance" at the top. One scenario reads: "Under a tenfold traffic spike, checkout answers within two seconds." The team checks the design against it and notes a risk. Later, stakeholders brainstorm more scenarios and vote on them. The team uses the top ones to check its earlier findings. On the last day it presents a report.

## Trade-offs

The method asks for several days from the review team, the project team and stakeholder representatives. See Advantages and Drawbacks of ATAM for a fuller discussion.
