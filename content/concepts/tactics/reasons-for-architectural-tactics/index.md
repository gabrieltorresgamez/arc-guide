---
title: Reasons for Architectural Tactics
slug: reasons-for-architectural-tactics
category: tactics
kind: concept
summary: Patterns rarely fit a design context perfectly. Tactics are smaller building blocks that help
  architects adapt a pattern and reason about one quality goal at a time.
arc42:
- 4
- 9
step: s07-solution-strategy
related:
- architectural-tactic
- tactics-vs-architectural-styles-and-patterns
- architectural-pattern
- quality-attribute
- tactic-trade-off-balancing
- choosing-and-applying-tactics
- arc42-solution-strategy
- working-with-tactics-and-quality-attributes
checks:
- When a catalog pattern is used, the document shows how it was adapted to the specific problem and design
  context.
- Design decisions are tied to a stated quality attribute objective.
sources:
- url: https://www.informit.com/articles/article.aspx?p=2738304&seqNum=5
  title: '2.5 Design Concepts: The Building Blocks for Creating Structures | Architectural Design | InformIT'
  site: informit.com
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

An architectural tactic is a design decision that affects how a system addresses one quality attribute, such as availability or performance. (See Architectural Tactic and Quality Attribute.) Tactics adjust the parameters of quality attribute models.

**Tactics are smaller than patterns.** A tactic is like an atom and a pattern is like a molecule. So a pattern can be seen as composed of tactics. The SEI report on modifiability tactics follows this idea. It describes standard architectural patterns and their variants in terms of tactics.

**Why use tactics next to patterns?**

- **Top-down reasoning.** Tactics give a way of thinking about design that starts from a quality attribute objective. The architect asks which decisions would serve that goal.

For more on how the two relate, see Relationship between Tactics and Architectural Styles/Patterns.

## Example

A team picks a catalog pattern for its system. The context differs from what the pattern assumes. The team states its main quality goal, for example availability. It then looks at tactics for that goal and adds or changes decisions in the pattern until it fits the situation.

## Trade-offs

This article covers only the reasons for using tactics, not the side effects of individual tactics. For balancing quality attributes, see Tactic Trade-off Balancing.
