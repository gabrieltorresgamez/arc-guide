---
title: Architectural Decision Management
slug: architectural-decision-management-practices
category: forces-decisions
kind: practice
summary: Architectural decision management is a set of habits for choosing which decisions to record,
  deciding them at the right time, justifying them well, and following through on them.
arc42:
- 9
- 4
- 11
step: s09-decisions
related:
- architectural-decision-management-cycle
- architecturally-significant-decision
- definition-of-ready-for-architectural-decisions
- definition-of-done-for-architectural-decisions
- architectural-decision-record
- last-responsible-moment
- architectural-decision-making-fallacies
- raci-matrix
checks:
- The ADR log contains only architecturally significant decisions, those affecting structure, quality
  characteristics or important dependencies.
- Each ADR justification refers to requirements, gathered information, evidence, criteria and agreement.
- Alternatives listed in an ADR are real options, not filler added to satisfy a template.
- Each ADR lists all consequences, not only the positive ones.
- Stakeholder involvement in decisions is planned ahead.
sources:
- url: https://ozimmer.ch/practices/2023/12/01/ADDefinitionOfReady.html
  title: A Definition of Ready for Architectural Decisions (ADs)
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2020/05/22/ADDefinitionOfDone.html
  title: A Definition of Done for Architectural Decision Making
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2020/09/24/ASRTestECSADecisions.html
  title: Architectural Significance Criteria and Some Core Decisions Required
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://www.ozimmer.ch/practices/2025/09/01/ADMFallacies.html
  title: Seven Architectural Decision Making Fallacies (and Ways Around Them)
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://www.ozimmer.ch/practices/2023/04/21/ADAdoptionModel.html
  title: An Adoption Model for Architectural Decision Making and Capturing
  site: ozimmer.ch
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Architectural decisions are choices that shape a system. Managing them means caring about the whole life of a decision, not only the moment of choosing. See *Architectural Decision Management Cycle* for the cycle itself.

**Select what deserves a record.** Not every decision needs an Architectural Decision Record (ADR). arc42 advises documenting only architecturally significant decisions. These affect structure, quality characteristics and important dependencies, especially external ones. arc42 also points to decisions that are important, expensive, large-scale or risky. A significance test can help prioritize. It is a qualitative judgment, not an exact calculation.

**Decide at the right time.** Each decision has a Most Responsible Moment (MRM). Hitting it matters.

**Check readiness.** START is a definition of ready. It holds five criteria to answer before a decision is made. Each decision is made when these criteria are met, but deciding too early harms flexibility.

**Check completeness.** ecADR names five exit criteria. It works as a quick yes/no test. Five "yes" answers mean the decision is done.

**Justify well.** A good justification refers to the requirements and the information gathered to meet the evidence, criteria and agreement criteria. Do not list fake alternatives just to satisfy a template. arc42 adds that all consequences belong in the record, not only the positive ones.

**Decide with care.** One fallacy is assuming that what worked for others will work for you. The countermeasure is to check whether the requirements are compatible before reusing a solution, and to apply a recognized method or your own heuristics when moving from analysis to design. Some bias is unavoidable in big decisions, so blending in gut feeling is acceptable.

**Involve people.** Plan stakeholder involvement ahead, at least a little. Otherwise it may be forgotten. Benefiting from recording and sharing decisions requires architecting skills and experience.

## Example

A team must pick how its web shop talks to a payment provider. The choice is external and costly to undo, so it passes the significance test and gets an ADR. The team waits until the requirements are clear enough, then checks its readiness criteria. It writes the justification with the requirements, evidence and the agreement of the people involved. It lists the downsides as well as the benefits. A short yes/no check confirms the decision is done. A minor choice, such as a button color, gets no ADR.

## Trade-offs

The significance test is only a rough guide, so judgment stays necessary. Gut feeling is acceptable, but it brings some bias. At the highest adoption level (Level 5), the review process is documented and enforced, taking the decision type into account.
