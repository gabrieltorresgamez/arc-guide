---
title: ATAM Risk
slug: architectural-risk
category: evaluation
kind: concept
summary: In ATAM, a risk is an architectural decision that may harm how the system responds to a quality
  scenario. Teams record risks, and the good decisions (non-risks), so they can review and mitigate them.
arc42:
- 11
step: s11-evaluate
related:
- atam-non-risk
- sensitivity-point
- trade-off-point
- architecture-tradeoff-analysis-method-atam
- atam-findings-risks-non-risks-sensitivity-points-and-trade-offs
- battlefield-control-system-atam-case-study
- quality-attribute-scenario
- architectural-decision-record
checks:
- Each recorded risk names the architectural decision, the affected quality attribute response with its
  consequences, and a rationale.
- Non-risks are recorded too, with their assumptions stated.
- Undecided or poorly understood decisions are listed as risks.
- Risks are tied to a scenario and quality attribute.
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

ATAM is the Architecture Tradeoff Analysis Method (see its own article). It sorts architectural decisions into two groups.

- **Risks** are decisions that may cause problems.
- **Non-risks** are good decisions. They rely on assumptions, and those assumptions are often left unwritten.

Teams should record both explicitly.

**What a record contains**

A risk or non-risk record names three things:

- the architectural decision,
- the quality attribute response it affects, with the consequences of the expected level of that response,
- a rationale for why the decision helps or hurts.

**Where risks come from**

A risk is not always a bad decision. It can also be a decision nobody has made yet, such as an undecided scheduling discipline or an unclear portability layer. It can also be a decision made without a full grasp of its consequences.

**Non-risks can turn into risks**

A non-risk stays one only while its assumptions hold. If the message arrival rate, the processing time or the number of higher-priority processes changes, the decision may become a risk. The team must then justify the non-risk label again.

**Related findings**

Particular values of a sensitivity point may become risks. A trade-off point is a parameter that holds more than one sensitivity point and affects the quality attributes differently. For instance, raising the speed of a communication channel might improve throughput but reduce reliability. See Sensitivity Point and Trade-off Point.

## Example

A team decides that one server handles all order processing. The scenario is "the server fails during peak load." The record says: decision, single server. Risk, an outage stops all orders. Impact, availability falls short of the target. Rationale, no backup exists. Later, the team adds a backup. They write down the assumption that the backup can take the full load. If traffic grows, they re-check that assumption.

## Trade-offs

In the reporting step, the ATAM team may write a report that includes any proposed mitigation strategies.
