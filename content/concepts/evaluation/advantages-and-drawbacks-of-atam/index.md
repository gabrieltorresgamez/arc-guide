---
title: Advantages and Drawbacks of ATAM
slug: advantages-and-drawbacks-of-atam
category: evaluation
kind: concept
summary: 'ATAM brings early risk detection, clearer quality requirements, better documentation and more
  stakeholder discussion. The price is effort: a full evaluation takes days and many people, so lighter
  variants exist.'
arc42:
- 9
- 10
- 11
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- lightweight-atam
- atam-results
- atam-findings-risks-non-risks-sensitivity-points-and-trade-offs
- software-architecture-evaluation
- insufficient-atam-application
- software-architecture-analysis-method-saam
- risk-storming
checks:
- The architecture evaluation produced a written report or out-brief that lists risks and non-risks.
- The effort for the evaluation (duration, participants) was estimated before it started.
- The team considered reusing recorded scenarios or a lighter method to reduce evaluation cost.
sources:
- url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  title: Architecture Tradeoff Analysis Method® Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://www.heise.de/en/background/Risk-analysis-with-lightweight-architecture-reviews-10355745.html
  title: Risk analysis with lightweight architecture reviews | heise online
  site: heise.de
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=24371&seqNum=9
  title: 8 What Are the Benefits and Costs of Performing an Architecture Evaluation? | Evaluating a Software
    Architecture | InformIT
  site: informit.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

ATAM is the Architecture Tradeoff Analysis Method, a structured way to evaluate a software architecture. The article Architecture Tradeoff Analysis Method (ATAM) covers the method itself. This article covers what it gives you and what it costs.

**Advantages**

- **Risks show up early.** The evaluation finds risks while the project is still young.
- **Quality requirements become clearer.** Quality requirements say how well a system must work, such as how fast or how available it must be. ATAM pushes teams to state them clearly.
- **Documentation improves.** The architecture description gets better. The reasons behind architectural decisions get written down.
- **Stakeholders talk more.** Stakeholders are people with an interest in the system. The evaluation increases communication among them.

**What you get out**

An ATAM produces an out-brief presentation, a written report, or both. The report lists risks and non-risks. It also contains a utility tree of the requirements that drive the architecture. See ATAM Results and ATAM Findings: Risks, Non-Risks, Sensitivity Points and Trade-off Points.

**Cost**

A full ATAM typically takes three to four days. It gathers an evaluation team, the architects and stakeholder representatives. One source puts a medium-size evaluation at about 70 person-days across all participants, and small projects at about 32. Another source gives a wider range: two days to several weeks. The number of stakeholders and scenarios drives that range.

**Ways to reduce the cost**

- Reuse recorded scenarios from earlier evaluations. Over time they work like a checklist.
- On smaller projects, this can halve the effort.
- Use a lighter method. Lightweight alternatives such as DCAR, pre-mortem and PBAR trade thoroughness for speed. See Lightweight ATAM.

## Example

A team plans an evaluation for a mid-size system. They expect to need several days and many people. Before the workshop, they reuse scenarios recorded in an earlier evaluation. The workshop forces them to write precise quality requirements. The final report lists risks and non-risks. The team then updates its decision records.

## Trade-offs

A full ATAM costs a lot of time and many people. Reuse of scenarios and smaller scope lower that cost. Lightweight alternatives are faster but less thorough. PBAR, for example, finds only some risks quickly. DCAR can take as long as ATAM if it evaluates all significant decisions. Choose the depth that fits the project size and the risk you face.
