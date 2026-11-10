---
title: Lightweight Approach for Software Reviews (LASR)
slug: lightweight-approach-for-software-reviews-lasr
category: evaluation
kind: method
summary: LASR is a lightweight way to review a software system. A small team runs a short, game-like workshop.
  It checks the system against quantified quality goals and gives first results within hours.
arc42:
- 10
- 11
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- lightweight-atam
- software-architecture-evaluation
- quality-attribute
- risk-storming
- advantages-and-drawbacks-of-atam
- quality-attribute-scenario
checks:
- The review states quantified objectives for the system's top quality attributes.
- The review names the most significant risks against those objectives.
- Controversial gaps between objectives and assessment are analyzed in depth.
sources:
- url: https://www.lasr-reviews.org/
  title: LASR - Lightweight Approach for Software Reviews
  site: lasr-reviews.org
  accessed: '2026-11-09'
- url: https://llm-coding.github.io/Semantic-Anchors/anchor/lasr/
  title: LASR according to Toth/Zörner — Semantic Anchors
  site: llm-coding.github.io
  accessed: '2026-11-09'
- url: https://conf.researchr.org/details/icsa-2026/icsa-2026-software-architecture-in-practice-track/8/Team-Driven-Architecture-Evaluation-with-LASR
  title: Team-Driven Architecture Evaluation with LASR (ICSA 2026 - Software Architecture in Practice)
    - ICSA 2026
  site: conf.researchr.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: The four LASR steps in order.
review:
  status: generated
  flags: []
---

## Explanation

LASR is a review method for software systems. It is lighter than ATAM, a heavier evaluation method (see Architecture Tradeoff Analysis Method (ATAM)). LASR still focuses on the key quality attributes of the system.

**Who runs it.** Two to four developers can run the review themselves. They need no separate evaluation support.

**How it runs.** The review is a short, moderated workshop. The moderation is game-like, so the review becomes a small team event. It works on site or remotely, and a few people are enough. First results appear within a few hours.

**The four steps.**

1. **Lean mission statement.** The team condenses the system's vision into a short statement.
2. **Evaluation criteria.** The team picks the top quality attributes of the system. The quantified objectives form the benchmark for the review.
3. **Risk-based review.** The team identifies the most significant risks against those objectives.
4. **Quality-focused analysis.** The team analyses the controversial gaps in depth. It also looks at cases where such gaps are missing.

**Result diagram.** The result diagram shows the quantified objectives as a benchmark line. This diagram drives the deeper analysis.

**Risk catalogue.** LASR uses a catalogue of standard risks. It comes from more than 100 earlier reviews.

**Evidence of effect.** A short paper in the ICSA 2026 Software Architecture in Practice track reports on 75 independently conducted reviews. Its results indicate that LASR delivers actionable insights with modest effort.

## Example

A team of three developers owns a webshop. They book a half-day workshop and write a short mission statement. They pick two top qualities, such as fast checkout and high availability, and give each a number as its objective. Each person then rates the system against those objectives. The team discusses the biggest gaps in depth and notes the risks it finds.

## Trade-offs

LASR is more streamlined than ATAM. It works with only a few people.
