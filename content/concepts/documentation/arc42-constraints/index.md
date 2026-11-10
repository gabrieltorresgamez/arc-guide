---
title: arc42 Constraints
slug: arc42-constraints
category: documentation
kind: artifact
summary: Chapter 2 of arc42 lists every requirement that limits how architects may design and build a
  system. It shows where the team is free to choose and where it must comply.
arc42:
- 2
step: s05-constraints
related:
- requirements-versus-constraints
- arc42-documentation-template
- arc42-solution-strategy
- arc42-architecture-decisions
- arc42-introduction-and-goals
- operational-constraint
checks:
- The document lists constraints in one place, with an explanation or background for each.
- Constraints are grouped into technical, organizational/political and conventions where the list is long.
- Organizational constraints such as budget, time or processes are recorded.
- Conventions such as programming style and naming rules are recorded.
- Each constraint shows whether it may be negotiated.
sources:
- url: https://docs.arc42.org/section-2/
  title: 2 - Constraints | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/C-2-2/
  title: 'Question C-2-2: What types of constraints exist? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
- url: https://examples.arc42.org/systems/biking/02-architecture-constraints/
  title: Architecture Constraints · arc42 Examples
  site: examples.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A constraint is any requirement that limits the freedom of architects in their design and implementation decisions. Chapter 2 of arc42 (see *arc42 Architecture Documentation Template*) collects them in one place.

The reason is simple. Architects should know exactly where they are free to decide and where they must stick to a given limit.

**Handling constraints.** A team must always deal with a constraint. Some constraints can be negotiated, though.

**Typical groups.** If the list grows long, you can split it into three groups:

- **Technical constraints.** Limits on the technology to use. The biking2 example requires a Java 8 and Spring Boot showcase. It also requires that the application compiles on Mac OS X, Linux and Windows.
- **Organizational and political constraints.** These include standard processes, budget, time and required information flows. The biking2 example requires that source and documentation be published as open source under the Apache 2 License.
- **Conventions.** Rules such as programming style and naming conventions.

**Typical format.** Simple tables of constraints with explanations work well.

## Example

A team builds a small web shop. Its constraints table might read:

| Constraint | Background |
|---|---|
| Must compile on Linux, Windows and macOS | Developers work on all three systems. |
| Source code published as open source | The company wants outside contributors. |
| Variable names follow the company naming rules | Teams share code across projects. |

A reader sees at once which choices are already made for the team.
