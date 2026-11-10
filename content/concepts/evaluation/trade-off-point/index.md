---
title: Trade-Off Point
slug: trade-off-point
category: evaluation
kind: concept
summary: A trade-off point is a property of the architecture that affects several quality attributes at
  once. Improving one attribute through it costs another. ATAM reports these points so teams can decide
  on a compromise knowingly.
arc42:
- 9
- 11
step: s11-evaluate
related:
- sensitivity-point
- architecture-tradeoff-analysis-method-atam
- atam-findings-risks-non-risks-sensitivity-points-and-trade-offs
- architectural-trade-off-thinking
- quality-attribute
- atam-non-risk
- arc42-architecture-decisions
- tactic-trade-off-balancing
checks:
- Each trade-off decision is recorded in arc42 section 9 with its rationale.
- The recorded consequences list negative effects as well as positive ones.
- Accepted trade-off consequences are tracked in the prioritized risk and technical debt list in section
  11.
- Each trade-off point names the quality attributes it is sensitive for, at least two.
sources:
- url: https://www.informit.com:443/articles/article.aspx?p=24371&seqNum=8
  title: 7 What Are the Outputs of an Architecture Evaluation? | Evaluating a Software Architecture |
    InformIT
  site: informit.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method
  title: Architecture tradeoff analysis method - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
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

Security and performance are examples of quality attributes (see the article Quality Attribute). A sensitivity point is a property of a component, or of how components relate, that is critical for reaching one quality attribute response.

A trade-off point goes one step further. It is a property that affects more than one attribute. It is a sensitivity point for more than one of them.

The Architecture Tradeoff Analysis Method (ATAM) looks for these points. Its analysis covers trade-offs, sensitivity points, and risks or non-risks. A risk is a potentially problematic decision. A non-risk is a good decision that rests on assumptions, which are often left implicit. ATAM aims to select a suitable architecture by discovering trade-offs and sensitivity points.

One example is a virtual private network (VPN). Its level of confidentiality might be sensitive to the number of bits of encryption. More bits improve security. They also require more processing time, which affects performance.

For documentation, arc42 section 9 records important, expensive, large-scale or risky decisions with their rationale. Its suggested Nygard structure asks for all consequences of a decision, not just the positive ones. Section 11 lists technical risks and technical debts by priority.

## Example

A team sets the encryption strength of a VPN link between two offices. A stronger setting protects data better. It also uses more processing time, so transfers slow down. The setting is a trade-off point for security and performance. The team writes the chosen strength into a decision record. The record names the security gain and the speed cost as consequences. The team also lists the remaining cost in the risk list.
