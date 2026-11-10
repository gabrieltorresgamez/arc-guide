---
title: Accidental Architecture
slug: unsystematic-accidental-architecture
category: fundamentals
kind: concept
summary: Accidental architecture is a structure nobody deliberately chose. It is merely implied, and it
  tends to erode through quick fixes and piecemeal growth until it ends as a Big Ball of Mud.
arc42:
- 4
- 9
- 11
step: s07-solution-strategy
related:
- big-ball-of-mud
- architecture-decay
- architectural-decision-record
- architectural-style
- architecture-facts-and-challenges
- technical-debt
- arc42-architecture-decisions
- arc42-solution-strategy
checks:
- The document names the chosen architecture explicitly and does not leave it implied by the code.
- The team has recorded architectural decisions, so the structure traces back to deliberate choices.
- The document describes how the structure is protected against erosion from quick fixes and piecemeal
  growth.
sources:
- url: https://www.laputan.org/mud/
  title: Big Ball of Mud
  site: laputan.org
  accessed: '2026-11-09'
- url: https://developertoarchitect.com/lessons/lesson132.html
  title: Lesson 132 - Architecture by Implication AntiPattern (February 14, 2022) | Developer to Architect
    | Mark Richards
  site: developertoarchitect.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: How an unchosen architecture tends to drift toward a Big Ball of Mud.
review:
  status: generated
  flags: []
---

## Explanation

Richards describes the Architecture by Implication antipattern, in which a software architecture is just "implied". He notes that this usually results in catastrophic failures.

**Where it leads**

A Big Ball of Mud is a system whose structure grew without care, sometimes almost at random. The article Big Ball of Mud covers it in detail.

Big Ball of Mud systems show signs of unregulated growth and repeated, expedient repair. One pattern behind this is piecemeal growth, which gradually lets elements of a once-tidy system sprawl in an uncontrolled fashion.

**Erosion**

Even systems with well-defined architectures can erode structurally.

## Example

A small team builds an internal booking tool. They start coding right away. Nobody discusses how the parts should fit together. Each new feature goes wherever it is quickest to add. Each bug gets a fast patch. After a year, nobody can describe the structure of the tool. Nobody decided on it, so it is implied by the code alone. The team now finds that each patch makes the next change harder.
