---
title: Choosing and Applying Tactics
slug: choosing-and-applying-tactics
category: tactics
kind: method
summary: Choosing tactics means picking design decisions that serve quality requirements you already captured.
  You then build patterns from them and handle the side effects each choice has on other qualities.
arc42:
- 4
- 9
- 10
step: s07-solution-strategy
related:
- architectural-tactic
- tactics-vs-architectural-styles-and-patterns
- tactic-trade-off-balancing
- working-with-tactics-and-quality-attributes
- quality-attribute
- reasons-for-architectural-tactics
- arc42-solution-strategy
- architectural-pattern
checks:
- Each chosen tactic traces back to a documented quality requirement.
- Side effects of each tactic on other quality attributes are documented along with the trade-offs accepted.
- Where a pattern is used, the tactics it relies on are named.
sources:
- url: https://dmccreary.github.io/atam/chapters/09-architectural-tactics-principles/
  title: Architectural Tactics and Design Principles - Architecture Tradeoff Analysis Method
  site: dmccreary.github.io
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/library/modifiability-tactics/
  title: Modifiability Tactics | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-08'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A tactic is a design decision that affects how well an architecture meets a particular quality attribute. See Architectural Tactic and Quality Attribute.

**Start from the requirements.** Tactics are how you implement the quality requirements you already captured, for example in a utility tree.

**Patterns are made of tactics.** Patterns are composed of tactics, which are the building blocks. Patterns and their variants can also be described by which tactics they use. See Relationship between Tactics and Architectural Styles/Patterns.

**Expect side effects.** Applying a tactic to improve one quality attribute almost always affects others. In ATAM, evaluators identify these interactions and document the conflicts they find. See Tactic Trade-off Balancing.

## Example

A team has a captured requirement that a service must keep working when one part fails. They pick a tactic aimed at that availability goal. They then note that it may slow responses or raise cost. They record the side effect and the reasoning, so later readers see why the tactic was chosen and what it costs.

## Trade-offs

Tactic interactions are the rule, not the exception: improving one quality attribute almost always has side effects on others.
