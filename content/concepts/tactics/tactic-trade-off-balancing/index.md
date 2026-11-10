---
title: Tactic Trade-Off Balancing
slug: tactic-trade-off-balancing
category: tactics
kind: practice
summary: Tactics serve quality goals, and those goals can conflict. Balancing means ranking the goals,
  finding where they collide, and recording each choice with all its consequences.
arc42:
- 4
- 9
- 10
- 11
step: s07-solution-strategy
related:
- architectural-tactic
- architectural-trade-off-thinking
- trade-off-point
- sensitivity-point
- architecture-tradeoff-analysis-method-atam
- quality-attribute-prioritization
- arc42-solution-strategy
- choosing-and-applying-tactics
checks:
- Quality goals are ranked, for example in a utility tree, so conflicts can be settled by priority.
- Trade-off points and sensitivity points found in the analysis are identified.
- The solution strategy ties each key quality goal to the decisions made for it, ideally in one table.
- Each important decision states its rationale, so stakeholders can retrace it.
- Decision records list all consequences, including the negative ones.
sources:
- url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  title: Architecture Tradeoff Analysis Method® Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-4/
  title: 4 - Solution strategy | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/1-17/
  title: 'Tip 1-17: Combine quality goals with the action points of the ‘solutions strategy’ section!
    | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://arxiv.org/abs/1802.03178
  title: '[1802.03178] Architectural Tactics for Big Data Cybersecurity Analytic Systems: A Review'
  site: arxiv.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'Balancing tactics: rank goals, choose, analyze, record, and adjust.'
review:
  status: generated
  flags: []
---

## Explanation

Quality goals often pull against each other. A choice that helps one goal can cost another. Tactic trade-off balancing is the work of handling that conflict on purpose. (See Architectural Tactic and Quality Attribute Trade-off for the basics.)

**Rank the goals first.** The ATAM method (Architecture Tradeoff Analysis Method) evaluates an architecture against its quality goals. It also shows how those goals interact and conflict. ATAM uses a utility tree for ranking. This is a tree of the requirements that drive the architecture, and it helps the team prioritize quality goals.

**Find the collision points.** In its analysis step, ATAM names three things: architectural risks, sensitivity points and trade-off points. Sensitivity Point and Trade-off Point have their own articles.

**Expect surprises.** A review of tactics for big data security calls for more research on trade-offs and dependencies among tactics.

**Write the choice down.** arc42 is a documentation template. Its solution strategy section holds the core decisions, including how the key quality goals are achieved. arc42 asks you to explain why you decided that way. When decisions rest on specific quality requirements, it suggests a consolidated table of those goals and the resulting decisions in this section. Section 9 asks for important decisions with their rationale, so stakeholders can retrace them. It also asks you to list all consequences, not only the positive ones.

## Example

A team ranks its quality goals and puts one goal at the top. It picks a tactic for that goal. In review, the team marks a trade-off point where the choice affects a lower-ranked goal. It then adds a row to its quality goal table. The row names the goal, the decision and the cost. It also lists that cost among the consequences in its decision record.

## Trade-offs

Writing down all consequences, including the negative ones, gives stakeholders a fuller record of the decision to retrace.
