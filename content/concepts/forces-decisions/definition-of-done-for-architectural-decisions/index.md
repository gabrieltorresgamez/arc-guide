---
title: Definition of Done for Architectural Decisions
slug: definition-of-done-for-architectural-decisions
category: forces-decisions
kind: practice
summary: 'A Definition of Done for architectural decisions lists the conditions that must hold before
  a team calls a decision finished. The ecADR proposal uses five: evidence, criteria, agreement, documentation,
  and realization and review.'
arc42:
- 9
step: s09-decisions
related:
- definition-of-ready-for-architectural-decisions
- last-responsible-moment
- architectural-decision-record
- y-statement
- markdown-architectural-decision-records-madr
- architectural-decision-making-in-project-development
- adr-common-mistakes-and-remediations
- architectural-decision
checks:
- The decision record shows at least two alternatives that were investigated and compared.
- The decision is captured and shared in a lean template.
- The record states who challenged the decision and that the team accepts outcome and rationale.
- The record says when the decision will be realized and reviewed.
- The record gives a reason to believe the chosen design will work.
sources:
- url: https://ozimmer.ch/practices/2023/12/01/ADDefinitionOfReady.html
  title: A Definition of Ready for Architectural Decisions (ADs)
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2020/05/22/ADDefinitionOfDone.html
  title: A Definition of Done for Architectural Decision Making
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

Agile teams use a Definition of Done to avoid misunderstandings and keep everyone focused. The same idea can be applied to architectural decisions. Feature-level Definitions of Done and Ready do not say when technical design work is ready or finished. Decision-specific criteria fill that gap. A separate post, "A Definition of Ready for Architectural Decisions (ADs)", covers the counterpart at the start of a decision.

One proposal abbreviates five exit conditions as **ecADR**:

- **Evidence:** the team has gained reason to believe the chosen design will work.
- **Criteria:** at least two alternatives were identified, investigated, and compared.
- **Agreement:** a mentor or peer, plus the team, challenged the decision. They accept the outcome and the rationale. Agreement can be light. Sometimes nobody objecting in a design workshop or review meeting is enough.
- **Documentation:** the decision is captured and shared, preferably in a lean, light template.
- **Realization and review:** the team knows when to realize the decision, review it, and possibly revise it.

The quick test turns these into five questions. If you can answer "yes" five times, the decision is done.

One design practice collection lists establishing done criteria, such as ecADR, as part of decision capturing. It also suggests lean templates such as MADR or Y-Statements. See "Markdown Architectural Decision Records" and "Y-Statement".

## Example

A team must choose how two services exchange data. They test one option with a small prototype and feel confident it works. They compare it with a second option. In a review meeting, nobody objects. They write a short decision record. They note that they will review the choice after the first release. All five answers are yes, so the decision is done.

## Trade-offs

ecADR is one proposal, not a standard. The author notes that the ecADR checklist has not been applied much in practice as such. Teams may adapt the criteria. How much agreement is needed depends on project context and decision-making culture; sometimes nobody objecting in a review meeting is enough, and sometimes formal sign-offs are required. A stricter check may suit riskier decisions.
