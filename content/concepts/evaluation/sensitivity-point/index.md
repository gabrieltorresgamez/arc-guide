---
title: Sensitivity Point
slug: sensitivity-point
category: evaluation
kind: concept
summary: A sensitivity point is a property of a system that one quality, such as speed or confidentiality,
  depends on strongly. Teams flag these points during evaluation so they know which decisions carry the
  most leverage.
arc42:
- 9
- 10
- 11
step: s11-evaluate
related:
- trade-off-point
- architecture-tradeoff-analysis-method-atam
- atam-findings-risks-non-risks-sensitivity-points-and-trade-offs
- atam-non-risk
- quality-attribute
- architectural-decision-record
- synchronous-vs-asynchronous-communication
- atam-results
checks:
- The evaluation report lists sensitivity points and states which quality attribute response each one
  affects.
- Each sensitivity point is documented with its rationale, ideally as an architectural decision record.
- Properties that affect more than one quality attribute are identified as trade-off points.
- The risks and technical debts section lists identified risks ordered by priority, with suggested mitigation
  measures.
sources:
- url: https://www.informit.com:443/articles/article.aspx?p=24371&seqNum=8
  title: 7 What Are the Outputs of an Architecture Evaluation? | Evaluating a Software Architecture |
    InformIT
  site: informit.com
  accessed: '2026-11-09'
- url: https://dmccreary.github.io/atam/faq/
  title: FAQ - Architecture Tradeoff Analysis Method
  site: dmccreary.github.io
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  title: Architecture Tradeoff Analysis Method® Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-11/
  title: 11 - Risks and technical debt | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A quality attribute is a measurable property such as performance or security (see the article Quality Attribute). A sensitivity point is a property of one or more components, or of how they connect, that is critical to reaching a given response for that quality.

Think of it as a dial. If a small turn changes the measured result a lot, that dial is a sensitivity point.

**Where it comes from**

Sensitivity points are findings of the Architecture Tradeoff Analysis Method (ATAM). The team analyzes the architectural approaches that address the high-priority quality factors in step 6. Analysis of scenarios and architectural decisions yields four kinds of findings: risks, non-risks, sensitivity points and trade-off points. The team may uncover more of them again in step 8. See ATAM Findings: Risks, Non-Risks, Sensitivity Points and Trade-off Points.

**How it differs from the other findings**

- A risk is a decision that may cause problems.
- A non-risk is a good decision. It rests on assumptions that are often left unstated.
- A trade-off point is a property that affects more than one quality, so it is a sensitivity point for several qualities at once. One description adds that the effects run in opposing directions. See Trade-off Point.

**Examples**

- The confidentiality of a virtual private network depends on the number of encryption bits. Changing the encryption level can affect both security and performance.
- The choice between synchronous and asynchronous communication between services is a sensitivity point for latency. See Synchronous vs. Asynchronous Communication.

**Documenting them**

Flag sensitivity points so stakeholders see which decisions carry the most leverage. Record them with their rationale in the final ATAM report. They are also prime candidates for architectural decision records (see Architectural Decision Record).

In arc42, section 11 lists risks and technical debts, ordered by priority, with suggested mitigation measures. It includes a tip to identify problems and risks by qualitative evaluation.

## Example

A team evaluates an online shop. Checkout speed depends heavily on whether the order service calls the payment service and waits for the answer, or hands the request off and continues. Switching between the two changes the measured checkout time a lot. The team flags this choice as a sensitivity point for latency. They record it in the evaluation report with the reason for the current choice.

## Trade-offs

Flagging a sensitivity point does not mean the decision is wrong. It means the decision has high leverage, so changes to it need care. Some sensitivity points are also trade-off points: improving one quality there, such as confidentiality, may affect another, such as performance.
