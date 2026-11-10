---
title: Architectural Tactic
slug: architectural-tactic
category: tactics
kind: tactic
summary: An architectural tactic is a design decision that changes how well a software architecture meets
  a quality attribute. Tactics work by adjusting parameters of a quality attribute model, and architectural
  patterns are built from them.
arc42:
- 4
- 8
- 9
step: s07-solution-strategy
related:
- quality-attribute
- availability-tactic
- modifiability-tactics
- tactics-vs-architectural-styles-and-patterns
- choosing-and-applying-tactics
- reasons-for-architectural-tactics
- coupling-and-cohesion
- architectural-pattern
checks:
- Each documented tactic names the quality attribute it is meant to improve.
- Each tactic is linked to the model parameters it adjusts, such as coupling, cohesion and cost for modifiability.
- Where a pattern is used, the tactics it is built from are identified.
sources:
- url: https://www.sei.cmu.edu/library/modifiability-tactics/
  title: Modifiability Tactics | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-08'
- url: https://www.sei.cmu.edu/library/realizing-and-refining-architectural-tactics-availability/
  title: 'Realizing and Refining Architectural Tactics: Availability | CMU Software Engineering Institute'
  site: sei.cmu.edu
  accessed: '2026-11-08'
- url: https://arxiv.org/html/2407.16706v1
  title: 'Architectural Tactics to Improve the Environmental Sustainability of Microservices: A Rapid
    Review'
  site: arxiv.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A tactic is a design decision. It changes how well the architecture meets a particular quality attribute.

**Why tactics work.** Tactics rest on the parameters of quality attribute models. A tactic gives you an architectural way to adjust those parameters. That adjustment can improve the attribute-specific behavior of the finished system.

**Example from modifiability.** The modifiability report justifies its tactics using the established concepts of coupling, cohesion and cost motivations as a way to identify the parameters of interest. The tactics are then described by their ability to control those parameters. See Coupling and Cohesion and Modifiability Tactic.

**Catalogs change with practice.** Availability tactics are collected in a catalog. The needs of practice led to updates of that catalog, while its underlying categorization structure stayed stable. A real-world example applies the updated tactics with heuristics and analytic models. See Availability Tactic.

**Tactics and patterns.** The modifiability report describes a standard set of architectural patterns and their variants in terms of the use of tactics. See Relationship between Tactics and Architectural Styles/Patterns.

## Example

A team wants to keep an online shop running. They open the availability tactic catalog and pick a tactic that suits their needs. They write down the choice and the reason in the architecture documentation.
