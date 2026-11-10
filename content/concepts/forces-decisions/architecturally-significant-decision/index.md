---
title: Architecturally Significant Decision
slug: architecturally-significant-decision
category: forces-decisions
kind: concept
summary: An architecturally significant decision is hard or costly to change, or carries high risk or
  cost. These decisions deserve careful review and a written record. Small, local choices do not.
arc42:
- 9
- 4
- 11
step: s09-decisions
related:
- architectural-decision
- architecturally-significant-requirement
- arc42-architecture-decisions
- architectural-decision-record
- architecture-decision-rationale
- integration-pattern
- levels-of-architectural-decisions
- quality-attribute-scenario
checks:
- The architecture decisions section lists only important, expensive, large-scale or risky decisions,
  each with its rationale.
- The decision log is kept small enough to maintain and does not record every decision.
- Hard-to-reverse decisions, such as the integration style, are explicitly identified as significant.
- The reasons a decision was judged significant are stated, for example business risk, quality demands
  or cross-cutting impact.
sources:
- url: https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html
  title: Architectural Decisions — The Making Of
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2023/12/01/ADDefinitionOfReady.html
  title: A Definition of Ready for Architectural Decisions (ADs)
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Architectural_decision
  title: Architectural decision - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2020/09/24/ASRTestECSADecisions.html
  title: Architectural Significance Criteria and Some Core Decisions Required
  site: ozimmer.ch
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

An architectural decision is a conscious choice among several options for a design problem. Teams often make it together. Often no single optimal solution exists for a given set of design problems (see Architectural Decision).

Not every decision matters equally. A significant decision is one that is hard and costly to change once made. Switching from one integration style to another is a typical case. It costs a lot, so the team should make that choice with care. (Integration Style explains the term.)

**Signals of significance**

The ASR test proposes five plus two criteria for judging whether a requirement, or another artifact such as a decision, is architecturally significant. (ASR stands for Architecturally Significant Requirement.) The criteria cover:

- high business value or business risk, and stakeholder concerns;
- demanding quality-of-service needs;
- external dependencies;
- impact across the whole system;
- first-of-a-kind work;
- past trouble with similar work.

The first five criteria are fairly objective. The last two depend more on context.

An (H/H) ranking in a utility tree can also be an indicator.

**Judgment, not arithmetic**

The assessment is qualitative and subjective. It depends on context. The ASR test is not a calculator that produces a score. It makes formerly tacit knowledge somewhat explicit.

**Why it matters for documentation**

Significant decisions are the ones worth recording. Arc42 section 9 holds decisions that are important, expensive, large-scale or risky, together with their rationales. Logging everything backfires. A decision log with more than 100 entries will probably bore readers and be hard to maintain. So focus on the decisions that matter.

## Example

A team must choose how two systems exchange data. Later, switching that approach would mean rewriting both systems. The team treats it as significant. They compare options, discuss it with stakeholders and record the result with its reasons. The same team also picks a name for an internal helper function. Changing that costs minutes and affects nothing else. They do not record it.

## Trade-offs

Recording only significant decisions keeps the log small and useful. The cost is that the call is subjective. Two teams may rate the same decision differently, and a decision judged minor today may prove costly later. Treat the criteria as a qualitative aid, not as a score.
