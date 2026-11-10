---
title: Scenario-Based Questions from Tactics
slug: scenario-based-questions-from-tactics
category: tactics
kind: method
summary: A questionnaire asks general, open questions that fit any architecture. A scenario describes
  a concrete sequence of steps in which the system is used or changed. Scenario-based questions lean on
  the second idea.
arc42:
- 10
- 4
step: s11-evaluate
related:
- quality-attribute-scenario
- architectural-tactic
- architecture-tradeoff-analysis-method-atam
- sensitivity-point
- software-architecture-evaluation
- availability-scenario
- choosing-and-applying-tactics
checks:
- The review separates general questionnaire-style questions from concrete scenarios that describe a sequence
  of steps of using or changing the system.
- Where ATAM is used, each scenario is linked to the design decisions (sensitivity points) that affect
  it.
- The scenario selection records how tradeoffs between competing qualities influenced which scenarios
  were chosen and ranked.
sources:
- url: https://arxiv.org/html/2105.09595
  title: Training Software Engineers for Qualitative Evaluation of Software Architecture
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/
  title: The Architecture Tradeoff Analysis Method | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://arxiv.org/html/2506.00150
  title: Supporting architecture evaluation for ATAM scenarios with LLMs
  site: arxiv.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Architecture reviews use several kinds of input. Each one asks for a different level of detail.

**Questionnaire.** A questionnaire is a list of general, fairly open questions. They apply to all architectures.

**Scenario.** A scenario is different. It is a concrete sequence of steps in which someone uses or modifies the system. A question built on a scenario is tied to one specific situation, not to architectures in general.

**Checklist.** A checklist is more detailed than a questionnaire. Reviewers build it after evaluating a set of systems from one domain.

So the three tools differ in how specific they are. Questionnaires are general and open. Checklists are detailed and domain-specific. Scenarios are concrete and describe one use or change.

**Link to ATAM.** The Architecture Tradeoff Analysis Method (ATAM) is a structured way to understand tradeoffs in the architecture of software-intensive systems. It looks at several quality attributes together. These attributes interact, so improving one can make others worse. A sensitivity point is a design decision that affects how well one quality-attribute scenario is achieved. ATAM works with scenarios. See the articles on ATAM and on sensitivity points.

Turning a general question into a scenario-based one means moving from the questionnaire style to the scenario style. The question stops asking about architectures in general. It asks about one concrete sequence of steps.

## Example

A general questionnaire item might ask, "Does the system handle failures?"

A scenario-style version describes one concrete sequence of steps instead. For example: "A user submits an order, and then one part of the system stops working. What happens next, step by step?" The answer now points to a specific situation that the team can discuss and check.

## Trade-offs

General questionnaire questions apply to every architecture, but they stay open and non-specific. Scenarios are concrete. In ATAM, tradeoffs between competing qualities can complicate the selection and prioritization of scenarios. Checklists give more detail, and they are developed after evaluating a set of systems in one domain.
