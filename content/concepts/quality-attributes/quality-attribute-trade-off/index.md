---
title: Quality Attribute Trade-Off
slug: quality-attribute-trade-off
order: 70
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
- architecture-tradeoff-analysis-method-atam
- tactic-trade-off-balancing
- quality-attribute-prioritization
- security
- performance-efficiency
checks:
- Quality requirements are ranked by stakeholder importance, with top goals separated from lesser ones.
- Each major decision names the quality it improves and the quality it may harm.
- Performance shortcuts that bypass security steps are backed by a documented risk analysis.
- Caching decisions state how stale data affects security.
- The document shows how the design can be tested and changed over time.
- Open disagreements about priority are recorded with the person who will decide them.
sources:
- url: https://learn.microsoft.com/en-us/azure/well-architected/security/tradeoffs
  title: Security tradeoffs - Microsoft Azure Well-Architected Framework | Microsoft Learn
  site: learn.microsoft.com
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
- url: https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method
  title: Architecture tradeoff analysis method - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-17'
- url: https://dmccreary.github.io/atam/chapters/07-utility-trees-prioritization/
  title: Utility Trees and Prioritization - Architecture Tradeoff Analysis Methodology
  site: dmccreary.github.io
  accessed: '2026-11-17'
- url: https://www.sei.cmu.edu/library/making-architecture-design-decisions-an-economic-approach/
  title: 'Making Architecture Design Decisions: An Economic Approach'
  site: sei.cmu.edu
  accessed: '2026-11-17'
- url: https://file.scirp.org/Html/3-9301368_19838.htm
  title: 'CBAM Assistant: A Tool to Semi-Automate the Cost Benefit Analysis Method'
  site: scirp.org
  accessed: '2026-11-17'
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

A trade-off means a design choice helps one quality and hurts another. Security choices, for example, can affect reliability, cost, or performance.

**Common conflicts**

- **Security versus performance.** Inspection, identity checks, and encryption add delay and use computing power.
- **Performance versus security.** Skipping slow steps, such as encryption or scanning, speeds things up but can weaken security. This needs a thorough risk analysis.
- **Caching versus fresh security state.** Caching serves a stored copy instead of checking again. That is faster, but the copy can be stale.
- **Performance versus simplicity.** Denormalizing data means storing it in several shapes for faster access. All copies must then stay in sync. Sharding adds similar complexity.
- **Security versus interaction capability.** Focusing heavily on security can hurt interaction capability. This is a particular problem in IoT (internet-connected devices), where interoperability is essential.
- **Distribution.** Splitting a system into many services, as in microservices, brings benefits. It also brings costs, such as weaker consistency and a need for operational maturity.

**Tactics help some qualities and hurt others.** A tactic is a small design decision, chosen from alternatives, that serves a specific quality (see Architectural Tactic). Tactics that raise reliability and security can lower performance. Intrusion detection is one example. Architects must balance protection against efficiency.

**How to handle trade-offs**

- Rank quality requirements by importance to stakeholders. Separate the top goals from lesser ones whose partial failure creates no high risk.
- Weigh the cost of coordination. Central coordination is worth its cost only in some cases.
- Find the trade-off points. An ATAM evaluation analyzes scenarios against the architectural approaches and records the trade-offs it finds, so a compromise is made knowingly. See Architecture Tradeoff Analysis Method (ATAM).
- Settle disagreements about priority. When stakeholders rate the same scenario differently, ask each one what failing it would cost the business. Often they assumed different consequences, and agreement follows once those are explicit. If they still disagree, record an open issue for the person with the authority to decide. With many stakeholders, dot voting lets the whole group decide instead of the loudest voice.
- Compare options by cost and benefit. The SEI's Cost Benefit Analysis Method (CBAM) usually follows ATAM. It uses ATAM's scenarios and strategies to estimate the return on investment of each architectural strategy from cost, utility and importance ratings. CBAM does not make the decision. It informs the people who make it.

## Example

A team builds a patient portal. They encrypt all traffic and check identity on every request. Pages load more slowly. To speed things up, they cache access decisions for a short time. Now a revoked user may keep access briefly. The team writes down both effects, ranks security above speed, and tests the cache duration before settling on it.
