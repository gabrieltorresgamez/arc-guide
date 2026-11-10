---
title: Tactics-Based Questionnaire
slug: tactics-based-questionnaire
category: evaluation
kind: method
summary: A tactics-based questionnaire turns the tactics of one quality attribute into questions. An analyst
  asks them and records, per tactic, whether it is used, the risk, where it lives, and why.
arc42:
- 10
- 11
step: s11-evaluate
related:
- architectural-tactic
- scenario-based-questions-from-tactics
- quality-attribute-scenario
- modifiability-tactics
- software-architecture-evaluation
- lightweight-atam
- architectural-risk
- working-with-tactics-and-quality-attributes
checks:
- Each tactic question has a recorded Y/N answer and a High/Medium/Low risk rating.
- For each supported tactic, the design decisions and where they appear (modules, frameworks, packages)
  are named.
- A rationale is recorded for each answer.
- The analysis uses scenarios alongside the questionnaire, not a checklist alone.
sources:
- url: https://www.sei.cmu.edu/documents/1288/2020_005_001_650490.pdf
  title: Maintainability
  site: sei.cmu.edu
  accessed: '2026-11-10'
- url: https://www.sei.cmu.edu/documents/1162/1997_005_001_16511.pdf
  title: Recommended Best Industrial Practice for Software Architecture Evaluation
  site: sei.cmu.edu
  accessed: '2026-11-10'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
  - missing-example
---

## Explanation

Tactics are mechanisms commonly used to satisfy maintainability requirements (see Architectural Tactic).

**Relation to scenarios**

The authors do not advocate a purely checklist-based approach. Scenarios give the context for interpreting a quality attribute. Checklists and questionnaires are used alongside them. Questionnaires reflect more mature practice and are assumed to exist before a project begins. Scenarios are specific to one system. They are developed during evaluation and, over time, generalized into checklists and questionnaires.

## Trade-offs

Questionnaires are general and coarse-grained, while scenarios are system-specific and give the context for interpreting a quality attribute.
