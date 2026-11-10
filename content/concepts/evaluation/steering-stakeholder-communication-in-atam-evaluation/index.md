---
title: Steering Stakeholder Communication in ATAM Evaluation
slug: steering-stakeholder-communication-in-atam-evaluation
category: evaluation
kind: practice
summary: Stakeholders in an ATAM evaluation each bring their own agenda. The team lead sets expectations
  early, uses templates to keep the schedule, and supports a cooperative, non-adversarial atmosphere so
  discussion stays useful.
arc42:
- 11
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- atam-roles
- atam-application-phases
- architecture-presentation-in-atam
- atam-findings-risks-non-risks-sensitivity-points-and-trade-offs
- atam-results
- atam-evaluation-team-and-stakeholder-selection
- stakeholder-concern
checks:
- Presentation templates were given to presenters, such as the architect, well before the evaluation.
- Step 1 explained the process to stakeholders and set expectations for the later activities.
- Both risks and non-risks are recorded explicitly.
- The final presentation summarizes the evaluation outputs for stakeholders, possibly with a written report.
sources:
- url: https://www.sei.cmu.edu/documents/629/2000_005_001_13706.pdf
  title: 'ATAM: Method for Architecture Evaluation'
  site: sei.cmu.edu
  accessed: '2026-11-10'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

The Architecture Tradeoff Analysis Method (ATAM) is a risk identification method for assessing the consequences of architectural decisions against quality attribute requirements. It involves many stakeholders.

**Set expectations first.** In Step 1 the method is described to the assembled stakeholders.

**Use templates for what is presented.** The report gives example templates for the business case and architecture presentations.

**Involve the whole group.** In the method's brainstorming step, a larger set of scenarios is elicited from the stakeholders and then prioritized through a voting process.

**Keep the vocabulary of findings clear.** The evaluation produces specific kinds of findings, so a concern is easier to handle when you know which kind it is:
- A risk is an important architectural decision that was not yet made, or was made without fully understood consequences.
- A non-risk is a good decision that relies on assumptions, which are often implicit.
- A sensitivity point is a parameter to which a measurable quality response is highly correlated.
- A trade-off point is a parameter that hosts sensitivity points for several quality attributes, which change differently.

Both risks and non-risks should be recorded explicitly. At the end, a final presentation summarizes the outputs for stakeholders. The team may also write a report.

## Example

A team prepares to review a system. Weeks ahead, the architect receives a presentation template. On the first day, the team lead walks everyone through the process and what to expect. During the brainstorming round, stakeholders contribute scenarios. Afterward, the team sorts the concerns into risks, non-risks, sensitivity points and trade-off points.

## Trade-offs


