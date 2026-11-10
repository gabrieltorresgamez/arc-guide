---
title: Quality Attribute Trade-Off
slug: architectural-trade-off-thinking
category: quality-attributes
kind: principle
summary: Improving one quality of a system usually costs another. Architects weigh these conflicts, rank
  what matters most to stakeholders, and improve the design step by step.
arc42:
- 4
- 9
- 10
- 11
step: s07-solution-strategy
related:
- quality-attribute
- architectural-tactic
- trade-off-point
- tactic-trade-off-balancing
- quality-attribute-prioritization
- architecture-tradeoff-analysis-method-atam
- security
- performance-efficiency
checks:
- Quality requirements are ranked by stakeholder importance, with top goals separated from lesser ones.
- Each major decision names the quality it improves and the quality it may harm.
- Performance shortcuts that bypass security steps are backed by a documented risk analysis.
- Caching decisions state how stale data affects security.
- The document shows how the design can be tested and changed over time.
sources:
- url: https://learn.microsoft.com/en-us/azure/well-architected/security/tradeoffs
  title: Security tradeoffs - Microsoft Azure Well-Architected Framework | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html
  title: General design principles - AWS Well-Architected Framework
  site: docs.aws.amazon.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
- url: https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/tradeoffs
  title: Performance Efficiency tradeoffs - Microsoft Azure Well-Architected Framework | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11598420/
  title: Enabling Design of Secure IoT Systems with Trade-Off-Aware Architectural Tactics - PMC
  site: pmc.ncbi.nlm.nih.gov
  accessed: '2026-11-09'
- url: https://martinfowler.com/architecture/
  title: Software Architecture Guide
  site: martinfowler.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A quality attribute is a property such as security, speed, or reliability (see the article Quality Attribute). A trade-off means a design choice helps one quality and hurts another. Security choices, for example, can affect reliability, cost, or performance.

**Common conflicts**

- **Security versus performance.** Inspection, identity checks, and encryption add delay and use computing power.
- **Performance versus security.** Skipping slow steps, such as encryption or scanning, speeds things up but can weaken security. This needs a thorough risk analysis.
- **Caching versus fresh security state.** Caching serves a stored copy instead of checking again. That is faster, but the copy can be stale.
- **Performance versus simplicity.** Denormalizing data means storing it in several shapes for faster access. All copies must then stay in sync. Sharding adds similar complexity.
- **Security versus interaction capability.** A heavy focus on security can compromise Interaction Capability. This is a particular problem in IoT (internet-connected devices), where interoperability is essential.
- **Distribution.** Splitting a system into many services, as in microservices, brings benefits. It also brings costs, such as weaker consistency and a need for operational maturity.

**Tactics help some qualities and hurt others.** A tactic is a small-scale design decision, chosen from alternatives, that serves a specific quality (see Architectural Tactic). Tactics that raise reliability and security can lower performance. Intrusion detection is one example. Architects must balance protection against efficiency.

**How to handle trade-offs**

- Rank quality requirements by importance to stakeholders. Separate the top goals from lesser ones whose partial failure creates no high risk.
- Do not treat decisions as one-time events. If you can test and change a design cheaply, a wrong choice carries less risk.
- Weigh the cost of coordination. Central coordination is worth its cost only in some cases.

## Example

A team builds a patient portal. They encrypt all traffic and check identity on every request. Pages load more slowly. To speed things up, they cache access decisions for a short time. Now a revoked user may keep access briefly. The team writes down both effects, ranks security above speed, and tests the cache duration before settling on it.

## Trade-offs

Few explicit guidelines help architects consider trade-offs when designing secure IoT systems. Trade-off information is crucial for decisions, yet none of the approaches the paper reviewed comprehensively address trade-offs in secure IoT design.
