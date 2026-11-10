---
title: arc42 Architecture Decisions
slug: arc42-architecture-decisions
category: documentation
kind: artifact
summary: Section 9 of arc42 records important, expensive, large-scale or risky architecture decisions
  with their reasons. It points back to section 4 for the most fundamental decisions instead of repeating
  them.
arc42:
- 9
- 4
step: s09-decisions
related:
- arc42-solution-strategy
- architectural-decision-record
- arc42-documentation-template
- architectural-decision
- architecture-decision-rationale
- architecturally-significant-decision
- markdown-architectural-decision-records-madr
- documentation-as-code
checks:
- Each entry in section 9 states the decision together with its rationale.
- Section 9 refers to section 4 instead of repeating the fundamental decisions.
- Decisions in section 4 are short but give reasons.
- Where ADRs are used, each ADR covers a single decision.
sources:
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-4/
  title: 4 - Solution strategy | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://adr.github.io/
  title: Architectural Decision Records (ADRs) | Architectural Decision Records
  site: adr.github.io
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Section 9 of the arc42 template (see the article "arc42 Architecture Documentation Template") is the place for architecture decisions. An architecture decision is a choice that shapes how a system is built. You record the choice together with its rationale, meaning the reasons behind it.

**Which decisions belong here**

Section 9 covers decisions that are important, expensive, large in scale or risky. Use judgement about whether a decision belongs in this central section or is better documented locally.

**Relation to section 4**

Section 4, Solution Strategy (see the article "Solution Strategy"), already summarizes the fundamental decisions that shape the architecture. Section 9 does not repeat them. It refers back to section 4 instead.

Strategy decisions are cornerstones. Many more detailed decisions or implementation rules build on them. Section 4 keeps the explanation of these key decisions short, while still motivating what was decided and why.

**Format**

Section 9 can be a list or table of decisions, ordered by importance and consequences. It can also hold one Architectural Decision Record (ADR) per decision. An ADR captures a single decision and its rationale. Michael Nygard's 2011 blog post popularized the idea. See "Architectural Decision Record" for details.

## Example

A team builds an online shop. Section 4 states the fundamental choice: one deployable application, kept simple for a small team, with short reasons.

Later the team makes a more detailed choice: use a managed payment provider instead of building payment handling. This is an important, expensive and risky decision, so section 9 records it. The entry gives the decision and the reasons. It also refers back to section 4 for the overall strategy.

## Trade-offs

Section 9 should avoid redundant text and refer to section 4 instead.
