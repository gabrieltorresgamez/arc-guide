---
title: Seven Types of Architectural Decisions
slug: seven-types-of-architectural-decisions
category: forces-decisions
kind: concept
summary: A decision is architectural when its effects reach beyond one place. Technology choice, such
  as buy versus build, is one kind of such decision. Tactics are decisions too, and the reasoning behind
  all of them needs recording.
arc42:
- 4
- 9
step: s09-decisions
related:
- architectural-decision
- architecturally-significant-decision
- architectural-tactic
- architecture-decision-rationale
- architectural-decision-record
- architecture-decay
- arc42-architecture-decisions
- architecture-as-set-of-design-decisions
checks:
- Each decision with far-reaching, hard-to-change effects is recorded as an architectural decision.
- Buy-versus-build decisions state their total-cost-of-ownership consequences.
- The rationale for risky decisions is documented, with effort matched to risk.
sources:
- url: https://www.informit.com/articles/article.aspx?p=2738304&seqNum=5
  title: '2.5 Design Concepts: The Building Blocks for Creating Structures | Architectural Design | InformIT'
  site: informit.com
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=2738304&seqNum=7
  title: 2.7 Summary | Architectural Design | InformIT
  site: informit.com
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=2738304&seqNum=6
  title: 2.6 Architecture Design Decisions | Architectural Design | InformIT
  site: informit.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

A decision counts as architectural when it has nonlocal consequences and those consequences matter to achieving an architectural driver. Such decisions are made early, reach far, and are hard to change later. See Architectural Decision and Architecturally Significant Decision.

Buy versus build is a key decision. The source calls it one of the most important decisions an architect makes. The criteria for selecting externally developed components affect total cost of ownership.

Tactics are design decisions that influence how a system controls its response to a quality concern. A tactic is simpler than a pattern. Think of a tactic as an atom and a pattern as a molecule. See Architectural Tactic and Architectural Pattern vs. Design Pattern.

Documentation matters too. You should record the rationale, meaning the reasons behind a decision. How much you record should depend on risk. If the rationale for layering is not documented, the layering will inevitably break down. See Architecture Decision Rationale and Architecture Decay.

## Example

A team must choose between buying a payment component and building one. The choice is a buy-versus-build decision. The team records why they chose as they did. The record is detailed because the risk is high. Later, a new developer reads it and keeps the layers intact.

## Trade-offs

Documenting rationale costs effort. The source advises basing what, when and how to document on risk. Writing down everything is not the goal. Skipping the record for risky decisions invites erosion.
