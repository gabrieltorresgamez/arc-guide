---
title: Architecture as Set of Design Decisions
slug: architecture-as-set-of-design-decisions
category: forces-decisions
kind: concept
summary: Architecture is the set of important design decisions about a system. These decisions shape quality
  and are costly to change later. Diagrams only show the results of those decisions.
arc42:
- 9
- 4
step: s09-decisions
related:
- architectural-decision
- architecturally-significant-decision
- architecturally-significant-requirement
- architectural-decision-record
- arc42-architecture-decisions
- architecture-decision-rationale
- software-architecture
- architectural-thinking
checks:
- The architecture documentation lists the important, expensive, large-scale or risky decisions together
  with their reasons.
- Only a few important decisions are documented, each with its motivation, instead of every choice.
- Each documented decision is tied to an architecturally significant requirement.
- Decisions that are costly to reverse, such as the integration style, are explicitly identified.
sources:
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://adr.github.io/
  title: Architectural Decision Records (ADRs) | Architectural Decision Records
  site: adr.github.io
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2023/12/01/ADDefinitionOfReady.html
  title: A Definition of Ready for Architectural Decisions (ADs)
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://martinfowler.com/architecture/
  title: Software Architecture Guide
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/ArchitectureDecisionRecord.html
  title: Architecture Decision Record
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/is-quality-worth-cost.html
  title: Is High Quality Software Worth the Cost?
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

One way to see software architecture is as the set of important design decisions about a system. A design decision is a choice about how the system is built. Not every choice counts. Fowler, citing Ralph Johnson, says architecture is about the important stuff.

**What makes a decision important**

- It addresses a requirement with a measurable effect on the architecture and on the quality of the system. The ADR community calls this an architecturally significant requirement (see Architecturally Significant Requirement).
- It is hard to change once made. Integration style is one example: switching from one style to another is costly.
- It is large in scale or risky. What counts as important also depends on the scale you look at. A choice that matters to one team may be minor for a whole organization.

**Architecture is more than a diagram**

One view, cited by Fowler, is that architecture is the shared understanding expert developers have of the system design.

**Why the cost of change matters**

Fowler argues that internal quality, which good architecture provides, lowers the cost of future change. Decisions that are expensive to reverse deserve care up front.

**Recording decisions**

Teams can see a decision in the code. They often cannot see the motivation behind it. So arc42 section 9 asks you to record important, expensive, large-scale or risky decisions with their reasons. It advises documenting only a few important decisions, not all of them. Fowler describes an architecture decision record (see Architectural Decision Record) as a way to let people understand, long afterwards, why the system is built the way it is.

## Example

A team building an order system decides that all services will talk to each other through a message queue instead of direct calls. Switching later would mean rewriting every service, so this is a principal decision. The team records it with its reasons. Choosing the color of a button is also a design decision, but it is cheap to reverse and does not belong in the architecture record.

## Trade-offs

Importance varies with the scale of the context. Teams often see a decision in the code but miss the motivation behind it.
