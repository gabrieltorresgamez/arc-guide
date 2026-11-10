---
title: Solution Strategy
slug: arc42-solution-strategy
category: documentation
kind: artifact
summary: The solution strategy is a short chapter of an arc42 document. It lists the fundamental decisions
  that shape the architecture and ties them to the problem, quality goals, and constraints.
arc42:
- 4
step: s07-solution-strategy
related:
- arc42-documentation-template
- arc42-introduction-and-goals
- arc42-constraints
- arc42-architecture-decisions
- architectural-pattern-vs-design-pattern
- architectural-decision
- arc42-quality-chapter
- architectural-tactic
checks:
- The section is short and compact, for example a keyword list, and refers onward instead of giving details.
- The section states the top-level decomposition decision, such as an architectural or design pattern.
- Each key quality goal has a solution approach described in the context of that goal.
- Decisions are justified from the problem statement, quality goals, and key constraints, with links to
  chapters 1 and 2.
- Relevant organizational decisions, such as the development process or work given to third parties, are
  included.
sources:
- url: https://docs.arc42.org/section-4/
  title: 4 - Solution strategy | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

The solution strategy is section 4 of an arc42 document (see arc42 Architecture Documentation Template). It gives a short summary and explanation of the fundamental decisions that shape the architecture.

**What belongs in it**

- Decisions about the top-level decomposition of the system. This means how the system is split at the highest level. An architectural pattern or a design pattern is a typical example (see Architectural Pattern vs. Design Pattern).
- Decisions on how to reach the key quality goals.
- Relevant organizational decisions. Examples are choosing a development process or handing certain tasks to third parties.

**Justify the decisions**

Do not only state what you decided. Explain why. Base the reasoning on the problem statement, the quality goals, and the key constraints. Refer to details in other sections: section 5 for structural details and section 8 for crosscutting concepts.

**Tie approaches to quality**

Describe solution approaches in the context of quality requirements.

**Keep it short**

Keep the explanation of the key decisions short. A compact list of keywords works well. Refer onward to concepts, views, or code instead of detailing them here.

## Example

A small web shop might list its strategy like this:

- Top-level split: a layered structure, chosen so the team can change one part without touching the others.
- Quality goal "easy to change": hide details behind clear interfaces. Details are in the cross-cutting concepts chapter.
- Organizational: an external provider runs payment processing.

Each line is a short keyword phrase, names its reason, and points elsewhere for detail.

## Trade-offs

The section should stay short and motivate the decisions. Refer to details in other sections.
