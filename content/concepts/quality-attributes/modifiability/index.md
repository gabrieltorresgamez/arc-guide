---
title: Modifiability
slug: modifiability
category: quality-attributes
kind: quality-attribute
summary: Modifiability describes how well a system can be changed. Architects steer it by adjusting coupling,
  cohesion, and cost, using architectural tactics.
arc42:
- 4
- 10
step: s04-quality-requirements
related:
- modifiability-tactics
- modifiability-scenario
- coupling-and-cohesion
- maintainability
- architectural-tactic
- iso-iec-25010-quality-model
- tactics-vs-architectural-styles-and-patterns
- reduce-coupling
checks:
- The document names coupling, cohesion, and cost as the parameters it uses to reason about modifiability.
- Each modifiability tactic in the document states which parameter it adjusts.
- Patterns used for modifiability are described in terms of the tactics they apply.
sources:
- url: https://www.sei.cmu.edu/library/modifiability-tactics/
  title: Modifiability Tactics | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-08'
- url: https://www.tmap.net/wiki/quality-characteristics-iso25010/
  title: Quality characteristics ISO25010 - TMAP
  site: tmap.net
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Modifiability is about change. How easily can people alter a system? ISO 25010, a standard quality model, defines the related quality maintainability. It is the degree to which the intended maintainers can modify a product effectively and efficiently. See the article Maintainability for that wider quality.

Architects need a way to reason about this. One well-known report from the Software Engineering Institute (SEI) uses three parameters:

- **Coupling**
- **Cohesion**
- **Cost**

The article Coupling and Cohesion explains the first two in more depth.

Architects can adjust such parameters with **tactics**. A tactic is an architectural means of adjusting them. The article Modifiability Tactic covers the specific tactics. The article Architectural Tactic explains the general idea.

The same report also describes standard architectural patterns and their variants. It does so in terms of modifiability tactics. The article Relationship between Tactics and Architectural Styles/Patterns goes further.

## Example

A team builds an order system. They notice that many parts depend directly on each other, so a small change touches many places. They treat this as high coupling. They pick a tactic that lowers it. They also ask what the change will cost and weigh that against the benefit. Coupling, cohesion, and cost give the team shared words for the discussion.
