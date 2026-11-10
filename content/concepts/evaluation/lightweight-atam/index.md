---
title: Lightweight ATAM
slug: lightweight-atam
category: evaluation
kind: method
summary: A lightweight ATAM is a shortened form of the full Architecture Tradeoff Analysis Method. It
  uses fewer people and simpler steps to deliver results in about a day, but it finds fewer risks.
arc42:
- 10
- 11
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- advantages-and-drawbacks-of-atam
- lightweight-approach-for-software-reviews-lasr
- atam-findings-risks-non-risks-sensitivity-points-and-trade-offs
- software-architecture-evaluation
- sensitivity-point
- trade-off-point
- atam-non-risk
checks:
- The document states whether the architecture review was a full ATAM or a lightweight variant.
- 'The document records who ran the lightweight review: external parties, the team, or both.'
- The document admits that a lightweight review may not have uncovered all risks.
- The review results list trade-offs, sensitivity points, and risks or non-risks.
sources:
- url: https://www.heise.de/en/background/Risk-analysis-with-lightweight-architecture-reviews-10355745.html
  title: Risk analysis with lightweight architecture reviews | heise online
  site: heise.de
  accessed: '2026-11-09'
- url: https://dmccreary.github.io/atam/faq/
  title: FAQ - Architecture Tradeoff Analysis Method
  site: dmccreary.github.io
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method
  title: Architecture tradeoff analysis method - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A full ATAM review (see Architecture Tradeoff Analysis Method (ATAM)) uses moderated workshops. It takes anywhere from two days to several weeks. One source describes the typical SEI-specified evaluation as two to three days of facilitated workshops.

Lightweight variants, sometimes called mini-ATAM or ATAM-lite, squeeze the method into one day, or even half a day. They are common in agile settings, where a formal two-day workshop is impractical.

**How the effort shrinks**

Lightweight methods save effort in several ways, including:

- Fewer people take part.
- The analysis steps are simpler.
- Results arrive faster.

The main cost drivers of ATAM are the number of stakeholders and the number of scenarios. A scenario is a concrete, measurable description of how the system should respond to a specific stimulus. Trimming either one cuts the cost.

**What you still get**

ATAM scenario analysis produces trade-offs, sensitivity points, and risks or non-risks. See ATAM Findings: Risks, Non-Risks, Sensitivity Points and Trade-off Points.

**Who runs it**

A lightweight review can be done by outside reviewers, by the team on its own, or by both together.

## Example

A small team is halfway through building a booking system. They want a quick check of the design before the next phase. They pick a few important scenarios, such as "the system stays responsive during a sales peak". They invite only the architect and a few key people. In one day they walk through the scenarios against the design. They leave with a short list of risks and trade-offs to follow up.

## Trade-offs

Speed comes at a price.

- **Less complete.** Lightweight reviews may not find all risks. The authors of one lightweight method, PBAR, do not claim to uncover all risks, but aim to find at least some of them in a very short time.
- **Depends on people.** Some methods lean on the reviewers' expertise: PBAR needs reviewers who know suitable patterns and their effects, and TARA relies even more on the reviewers' knowledge and experience. The pre-mortem method instead depends on the group's understanding of the system, its context, and its creativity.

Choose a lightweight review when speed and low effort matter more than full coverage.
