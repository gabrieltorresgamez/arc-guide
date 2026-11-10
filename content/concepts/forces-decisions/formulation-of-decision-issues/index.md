---
title: Architectural Design Issue
slug: formulation-of-decision-issues
category: forces-decisions
kind: concept
summary: A design issue is one concern that needs an architectural decision. You phrase it as a short
  question, list the options, and pick one based on criteria. You then record why you chose it.
arc42:
- 9
- 4
step: s09-decisions
related:
- architectural-decision
- architectural-decision-record
- arc42-architecture-decisions
- architectural-forces
- architecture-decision-rationale
- definition-of-done-for-architectural-decisions
- architecture-as-set-of-design-decisions
- markdown-architectural-decision-records-madr
checks:
- Each design issue is phrased as a concise question.
- Each issue lists its criteria (drivers) and its options.
- Rejected options are evaluated too, not only the chosen one.
- The rationale names the price of the choice and lists negative consequences too.
- The criteria are rooted in actual requirements and experience.
sources:
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2023/04/03/ADRCreation.html
  title: How to create Architectural Decision Records (ADRs) — and how not to
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2020/05/22/ADDefinitionOfDone.html
  title: A Definition of Done for Architectural Decision Making
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2022/11/22/MADRTemplatePrimer.html
  title: The Markdown ADR (MADR) Template Explained and Distilled
  site: ozimmer.ch
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: How a design issue is resolved
review:
  status: generated
  flags: []
---

## Explanation

An issue can be articulated as a question. One example is "Which concept is used to decompose the system under construction into logical building blocks?"

A decision means selecting one alternative based on given criteria. So every issue needs two more things next to the question: the criteria, often called drivers, and the options. Criteria should come from real requirements and experience. These are the forces behind the decision. See the article Architectural Force for more.

**How an issue is resolved**

1. State the question.
2. Name the criteria. One example is the ability to exchange system parts without affecting others.
3. List the options. The decomposition example lists three: Layers, Pipes-and-filters and Workflow.
4. Choose one option. The others are rejected, or kept as fallbacks.

You should also evaluate the options you did not choose, not only the winner. Readers can then see why the alternatives lost.

**Recording the issue**

Stakeholders should be able to understand and retrace your decisions. Section 9 of arc42 recommends Architectural Decision Records (ADRs) for this. An ADR captures a single decision and its rationale. See the articles Architectural Decision Record and arc42 Architecture Decisions.

## Example

A team building an online shop asks: "How do we split the system into building blocks?" The criterion is that the team wants to change checkout without touching the catalog. The options are layers, pipes-and-filters and a workflow-based design. The team weighs each option against the criterion and picks layers. It notes why the other two lost and keeps one as a fallback. The ADR holds the question, the criteria, the options and the choice.

## Trade-offs

Every selection brings benefits, but it also comes at a price. The rationale should say what you gain and what you give up. Arc42 asks you to list all consequences of a decision, not only the positive ones.
