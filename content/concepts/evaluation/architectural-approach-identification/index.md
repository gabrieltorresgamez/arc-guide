---
title: Architectural Approach Identification
slug: architectural-approach-identification
category: evaluation
kind: practice
summary: Architectural approach identification is Step 4 of ATAM. The architect names the approaches used
  in the system. The team only lists them here and analyzes them later.
arc42:
- 4
- 9
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- architectural-style
- architectural-pattern
- architectural-tactic
- sensitivity-point
- trade-off-point
- atam-phase-1-architecture-centric-analysis
- tactics-vs-architectural-styles-and-patterns
checks:
- The evaluation record lists the architectural approaches the architect named.
- The approaches are listed without risk or trade-off findings attached; those appear in the later analysis
  step.
sources:
- url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  title: Architecture Tradeoff Analysis Method® Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method
  title: Architecture tradeoff analysis method - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Step 4 sits between the architecture presentation and the utility tree; analysis comes later
    in Step 6.
review:
  status: generated
  flags: []
---

## Explanation

ATAM is the Architecture Tradeoff Analysis Method. It is a structured way to evaluate an architecture (see the article on ATAM).

Step 4 is where the architectural approaches are named. See the articles on Architecture Style, Architectural Pattern and Architectural Tactic.

**Where it sits.** Step 3 is the architect's presentation of the architecture. Step 4 follows it. Step 5, the utility tree, comes after.

**What happens.** The architect names the approaches.

**What does not happen.** The team does not analyze the approaches in this step. It only identifies them. Risks, sensitivity points and trade-off points are identified later, in Step 6 (and again in Step 8). Step 6 analyzes the approaches. See the articles on Sensitivity Point and Trade-off Point.

## Example

A team evaluates an online shop. In Step 4 the architect says the system uses a layered structure and a message queue between order and shipping. The team writes both down and does not probe them yet. Step 6 examines each one later.


