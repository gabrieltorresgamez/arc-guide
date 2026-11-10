---
title: Working with Tactics and Quality Attributes
slug: working-with-tactics-and-quality-attributes
category: tactics
kind: method
summary: Working with tactics means taking measurable quality scenarios and choosing small design decisions
  (tactics) that meet them. You record each choice with its reasoning and revisit it as knowledge grows.
arc42:
- 1
- 4
- 9
- 10
step: s07-solution-strategy
related:
- architectural-tactic
- choosing-and-applying-tactics
- quality-attribute-scenario
- tactic-trade-off-balancing
- arc42-solution-strategy
- architectural-decision-record
- architecture-tradeoff-analysis-method-atam
- smart-requirements
checks:
- Each quality scenario is specific and has a measurable criterion.
- A table in the solution strategy links each quality goal and scenario to its tactics or approaches.
- Each tactic decision is recorded as an ADR that traces back to a requirement.
- At least two options were considered for each decision issue.
- The impact of chosen tactics on other quality attributes is noted.
sources:
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11598420/
  title: Enabling Design of Secure IoT Systems with Trade-Off-Aware Architectural Tactics - PMC
  site: pmc.ncbi.nlm.nih.gov
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2023/04/03/ADRCreation.html
  title: How to create Architectural Decision Records (ADRs) — and how not to
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/4-2/
  title: 'Tip 4-2: Describe the solution approaches as a table! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/1-17/
  title: 'Tip 1-17: Combine quality goals with the action points of the ‘solutions strategy’ section!
    | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/articles/specify-quality-requirements
  title: How to specify quality requirements | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-08'
- url: https://docs.arc42.org/tips/10-8/
  title: 'Tip 10-8: Use (quality) scenarios for architecture analysis or evaluation! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: The iterative loop from scenarios to recorded tactic decisions.
review:
  status: generated
  flags: []
---

## Explanation

A quality attribute is a property such as speed or security that the system must have. A quality scenario describes one such need in a concrete situation. A tactic is a small design decision that helps meet a specific quality attribute (see Architectural Tactic).

**Start with measurable scenarios.** Scenarios must be specific and measurable. Then the team knows what is good enough and can decide whether the requirements are fulfilled. arc42 separates two kinds. Usage scenarios describe how the running system reacts to a stimulus. Change scenarios describe the effect of a modification or extension.

**Pick tactics from catalogues.** Tactics are grouped into taxonomies. Security tactics, for example, are organized as detect, resist, react and recover. Look in the catalogue for the quality attribute you are working on. Choose tactics that address the scenario.

**Record each decision with its reasoning.** A good architectural decision record (ADR) resolves at least one architecturally significant requirement. Base the rationale on actual requirements and trace it back to them. Consider at least two options per issue.

**Show the link in a table.** arc42 suggests one consolidated table in the solution strategy (section 4). It links quality goal, scenario, solution approach and details. It answers the question: which tactics, approaches or decisions address each scenario? Section 1.2 then only refers to this table.

**Iterate.** Be ready to revise a decision as design work evolves and you learn more about requirements. Where a decision was deliberately split into stages, revisit it at the end of each stage.

**Evaluate.** Quality scenarios can also feed an ATAM review (see Architecture Tradeoff Analysis Method (ATAM)). A table of quality goal, scenario, solution approach and risk supports a qualitative evaluation.

## Example

A team has the scenario: "When 500 users search at once, results appear within 2 seconds." The scenario is measurable. The team looks in a performance tactic catalogue and considers two options. They choose one and write an ADR that names the scenario as the reason. They add a row to the solution-strategy table: goal, scenario, approach, details. After the first release they revisit the decision with what they learned.

## Trade-offs

Tactics interact. Favoring one quality attribute can come at the expense of another. A tactic that helps speed may hurt something else. Tactic catalogues can record these impacts on other attributes, for example using the ISO 25010 quality model. Check the side effects before you commit to a tactic.
