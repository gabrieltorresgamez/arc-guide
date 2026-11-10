---
title: Twin Peaks Model
slug: twin-peaks-model
category: forces-decisions
kind: concept
summary: The Twin Peaks Model treats requirements and architecture as two bodies of work that grow together.
  Both start rough and become detailed through repeated rounds, each informing the other.
arc42:
- 1
- 4
- 9
step: s07-solution-strategy
related:
- architecturally-significant-requirement
- iterative-and-incremental-development
- architectural-forces
- evolutionary-domain-modeling
- solution-as-moving-target
checks:
- The document shows that requirements and architecture were refined together, in mutual interplay.
- Requirements and architecture are described at a level of detail that grew through iteration, starting
  from a rough version.
- Technical limits or goal conflicts found during architecture work are recorded as feedback to the requirements.
sources:
- url: https://www.microtool.de/en/knowledge-base/what-is-the-twin-peaks-model/
  title: What Is the Twin Peaks Model? | microTOOL
  site: microtool.de
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Requirements and architecture alternate, both gaining detail each round.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

The Twin Peaks Model says teams refine requirements and architecture in parallel, and each one influences the other.

Both start rough and general. Through repeated rounds, both become detailed.

This interplay matters because architecture work can teach something about the requirements. While designing, the team can find technical limits. It can also find goals that conflict with each other. Those findings feed back into the requirements.

See Architecturally Significant Requirement for requirements that shape the architecture most.

## Example

A team sketches the requirements for an online ticket shop. Its first architecture draft shows that two goals pull against each other: instant order confirmation and a slow external check of every order. The team takes this back to the requirements and revises them. Then it refines the architecture again, with more detail on both sides.
