---
title: ADR Common Mistakes and Review Checklist
slug: adr-common-mistakes-and-remediations
category: forces-decisions
kind: practice
summary: Weak decision records often hide their criteria, skip alternatives, give no real "why," or leave
  out downsides. A short review checklist helps catch these gaps before the record is accepted.
arc42:
- 9
step: s09-decisions
related:
- architectural-decision-record
- architecture-decision-rationale
- arc42-architecture-decisions
- genai-support-for-architectural-decision-records
- definition-of-done-for-architectural-decisions
- architectural-decision-making-fallacies
- y-statement
- traceability
checks:
- The criteria in the ADR come from the context and requirements, not from the properties of the preferred
  option.
- The ADR lists the considered options and justifies the rejection of each alternative.
- The decision section explains why the option was chosen and does not just repeat the ADR title.
- The ADR documents negative consequences, not only pros or harmless-looking effects.
- The chosen solution is described in an actionable way and can be traced back to requirements.
sources:
- url: https://ozimmer.ch/practices/2026/09/12/ADRMistakes.html
  title: Ten Common Mistakes in Architectural Decision Records (ADRs)
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2023/04/03/ADRCreation.html
  title: How to create Architectural Decision Records (ADRs) — and how not to
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2023/04/05/ADRReview.html
  title: How to review Architectural Decision Records (ADRs) — and how not to
  site: ozimmer.ch
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

An architectural decision record (ADR) logs the outcome of design and decision making. See the article Architectural Decision Record. Records often show the same flaws.

**Common mistakes and remedies**

- **Criteria bent to fit the favorite.** Some records build their criteria only from the properties of the option the author already prefers. Remedy: derive criteria from the context and the requirements, and make them explicit.
- **Missing alternatives.** Some records do not record the options considered. They also reject alternatives without enough justification. Remedy: list the options and say why each rejected one lost.
- **A decision section with no "why."** Some records only repeat the ADR title in the decision section. Remedy: state the rationale, meaning the reasons for the choice.
- **Hidden downsides.** Two named anti-patterns cover this. The "Free Lunch Coupon" documents no consequences, or only harmless-looking ones. The "Fairy Tale" gives pros but no cons. Remedy: state the negative consequences.

**Review checklist**

A reviewer can ask these questions:

1. Does the problem matter enough to be solved and written down as an ADR?
2. Can each option actually solve the problem? Is a good option left out?
3. Are the decision drivers (the criteria) mutually exclusive and collectively exhaustive? Are conflicting criteria prioritized?
4. Does the ADR report the good and bad consequences of each option as fairly as it can?
5. Is the decision rationale sound and convincing?
6. Is the chosen solution clear enough to act on? Does it link back to the requirements? Does the ADR define a validity period or review date?

## Example

A team records "Use a message queue between the order and billing services." The decision section only repeats that title. The criteria listed are "supports queues" and "has a queue library," which describe the chosen option itself. No other option appears. No downside appears either.

A reviewer asks the checklist questions. The team then adds criteria taken from the requirements and lists two other options with reasons for rejecting them. They also add the cons of the queue and a sentence explaining why it wins.

## Trade-offs

In the example, the team must still write the missing context, options, and consequences.
