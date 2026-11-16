---
title: Architectural Decision Management
slug: architectural-decision-management
order: 10
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
- architecturally-significant-decision
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
- url: https://ozimmer.ch/practices/2022/11/22/MADRTemplatePrimer.html
  title: The Markdown ADR (MADR) Template Explained and Distilled
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2023/04/03/ADRCreation.html
  title: How to create Architectural Decision Records (ADRs) — and how not to
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2021/04/23/AnyDecisionRecords.html
  title: ADR = Any Decision Record? Architecture, Design and Beyond
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://arxiv.org/abs/1807.02798
  title: '[1807.02798] Formal Semantics of Architectural Decision Models'
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2025/07/17/ArchitectureDecisionGuidanceTool.html
  title: 'ADG: A Light Architectural Decision Guidance and Management Tool'
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://socadk.github.io/design-practice-repository/activities/DPR-ArchitecturalDecisionCapturing.html
  title: design-practice-repository | Summaries of artifacts, templates, practices, and techniques for
    agile architecting (DPR-mm) and service design (SDPR-nn).
  site: socadk.github.io
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Architectural decisions are choices that shape a system. Managing them means caring about the whole life of a decision, not only the moment of choosing. The cycle itself is described below.

**Select what deserves a record.** Not every decision needs an Architectural Decision Record (ADR). arc42 advises documenting only architecturally significant decisions. These affect structure, quality characteristics and important dependencies, especially external ones. arc42 also points to decisions that are important, expensive, large-scale or risky. A significance test can help prioritize. It is a qualitative judgment, not an exact calculation.

**Decide at the right time.** Each decision has a Most Responsible Moment (MRM). Hitting it matters.

**Check readiness.** START is a definition of ready. It holds five criteria to answer before a decision is made. Each decision is made when these criteria are met, but deciding too early harms flexibility.

**Check completeness.** ecADR names five exit criteria. It works as a quick yes/no test. Five "yes" answers mean the decision is done.

**Justify well.** A good justification refers to the requirements and the information gathered to meet the evidence, criteria and agreement criteria. Do not list fake alternatives just to satisfy a template. arc42 adds that all consequences belong in the record, not only the positive ones.

**Decide with care.** One fallacy is assuming that what worked for others will work for you. The countermeasure is to check whether the requirements are compatible before reusing a solution, and to apply a recognized method or your own heuristics when moving from analysis to design. Some bias is unavoidable in big decisions, so blending in gut feeling is acceptable.

**Involve people.** Plan stakeholder involvement ahead, at least a little. Otherwise it may be forgotten. Benefiting from recording and sharing decisions requires architecting skills and experience.

**More about managing decisions.**

- **Architectural Decision Management Cycle:** The cycle has five logical steps for each architectural decision: identify it, evaluate options, decide, record the outcome in an ADR, and check that the problem is solved. Teams may repeat steps for the same decision.
- **Architectural Design Issue:** A design issue is one concern that needs an architectural decision. You phrase it as a short question, list the options, and pick one based on criteria. You then record why you chose it.
- **Decision Dependencies:** Architectural decisions depend on each other. One decision can trigger or split into others. Recording these links helps teams see which decisions to make early and where follow-on work comes from.
- **Architectural Decision Definition of Ready:** The Architectural Decision Definition of Ready is a checklist of five START criteria: stakeholders, time, alternatives, requirements, template. Teams check it before deciding, so they do not decide without the key inputs.
- **Definition of Done for Architectural Decisions:** A Definition of Done for architectural decisions lists the conditions that must hold before a team calls a decision finished. The ecADR proposal uses five: evidence, criteria, agreement, documentation, and realization and review.

## Example

A team must pick how its web shop talks to a payment provider. The choice is external and costly to undo, so it passes the significance test and gets an ADR. The team waits until the requirements are clear enough, then checks its readiness criteria. It writes the justification with the requirements, evidence and the agreement of the people involved. It lists the downsides as well as the benefits. A short yes/no check confirms the decision is done. A minor choice, such as a button color, gets no ADR.

## Trade-offs

The significance test is only a rough guide, so judgment stays necessary. Gut feeling is acceptable, but it brings some bias. At the highest adoption level (Level 5), the review process is documented and enforced, taking the decision type into account.
