---
title: ATAM Application Phases
slug: atam-application-phases
category: evaluation
kind: practice
summary: ATAM works best early, before major implementation spending, because it shows whether an architecture
  can meet its quality goals. It also applies to legacy systems, once their real architecture has been
  recovered.
arc42:
- 10
- 11
- 9
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- software-architecture-evaluation
- lightweight-atam
- software-architecture-analysis-method-saam
- advantages-and-drawbacks-of-atam
- atam-phase-1-architecture-centric-analysis
- technical-debt
- architecture-decay
checks:
- The architecture was evaluated before major investment in implementation.
- For a legacy system, the architecture was recovered before the analysis, and the documentation was not
  simply trusted.
- Conflicting stakeholder quality requirements, such as performance versus security, are named as a reason
  for the evaluation.
sources:
- url: https://c2wiki.gothdyke.mom/ArchitectureTradeoffAnalysisMethod.html
  title: ''
  site: c2wiki.gothdyke.mom
  accessed: '2026-11-09'
- url: https://llm-coding.github.io/Semantic-Anchors/anchor/atam/
  title: ATAM — Semantic Anchors
  site: llm-coding.github.io
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

The Architecture Tradeoff Analysis Method (ATAM) is a method for evaluating a software architecture against its quality goals.

**Early, before the system is built**

Checking an architecture before the system exists is cost-effective. You learn whether the system will reach its desired qualities before you invest in building it. ATAM is positioned as a method that reduces risk and can be applied early in the development life cycle. A common guideline says the same: evaluate the architecture before major investment in implementation.

**When stakeholders disagree**

ATAM is also suggested when stakeholders have conflicting quality requirements, for example performance versus security.

**Legacy systems**

Older systems also need architecture analysis. Their architecture is frequently undocumented, or the documents are inaccurate because of unavoidable architectural drift and erosion, which makes analysis impossible. To address this, the SEI developed Dali, a separate workbench for architecture extraction and reconstruction. It rebuilds architectures from source code and checks whether as-built systems conform to their documented architectures.

## Example

A team plans a new order system. It has written no code yet. Two stakeholders want very fast responses and strict data protection, and those goals pull against each other. The team runs an ATAM evaluation now, while changes are still cheap.

Later, the same company wants to analyze an old billing system. Nobody trusts the old diagrams.


