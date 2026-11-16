---
title: Big Ball of Mud
slug: big-ball-of-mud
category: fundamentals
kind: concept
summary: A Big Ball of Mud is a system whose structure comes from quick fixes rather than design. It grows
  without control and is repaired again and again with expedient patches.
arc42:
- 11
- 4
step: s12-evolve
related:
- shearing-layers
- refactoring
- technical-debt
- code-smell
checks:
- Throwaway code is either removed or deliberately kept and documented, not left in the system by accident.
- The document states how the team alternates expansion with consolidation, refactoring and repair.
- Blighted areas of code are identified and cordoned off.
sources:
- url: https://www.laputan.org/mud/
  title: Big Ball of Mud
  site: laputan.org
  accessed: '2026-11-09'
- url: https://arxiv.org/abs/2112.10934
  title: '[2112.10934] Understanding Software Architecture Erosion: A Systematic Mapping Study'
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://developertoarchitect.com/lessons/lesson132.html
  title: Lesson 132 - Architecture by Implication AntiPattern (February 14, 2022) | Developer to Architect
    | Mark Richards
  site: developertoarchitect.com
  accessed: '2026-11-09'
- url: https://www.laputan.org/mud/mud.html
  title: Big Ball of Mud
  site: laputan.org
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/StranglerFigApplication.html
  title: Strangler Fig
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://ar5iv.arxiv.org/html/2103.11392
  title: '[2103.11392] Understanding Architecture Erosion:The Practitioners’ Perceptive'
  site: ar5iv.arxiv.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A Big Ball of Mud is a system with a loose, haphazard structure. Its organization, if you can call it that, comes from expediency (doing whatever is fastest) rather than from design.

Such systems show clear signs of unregulated growth. They are repaired again and again with quick fixes. People call the result a spaghetti-code jungle.

**Throwaway code.** Throwaway code is a quick piece of code meant to be discarded. The real problem starts when nobody discards it and it stays in the system.

**Different rates of change.** Systems and their parts evolve at different rates. The Shearing Layers pattern builds on this idea (see Shearing Layers).

**Architecture erosion.** A systematic mapping study says architecture erosion harms software development. It also says erosion shows up in more than architectural violations and structural issues. The study asks practitioners to raise awareness of its grave consequences. It also calls for more empirical research on detecting and addressing erosion (see Big Ball of Mud).

**Related patterns.** Two related patterns are covered here:

- *Sweeping It Under the Rug* controls decline by cordoning off the blighted areas of the code.
- *Reconstruction* means tearing everything down and starting over. In advanced cases there may be no alternative.

**More about decay and what to do about it.**

- **Sweeping It Under the Rug:** Sweeping It Under the Rug is a pattern for controlling decline in tangled code. You fence the mess off from the rest of the system and put a clean interface in front of it.
- **Architecture Decay:** Architecture decay is the slow divergence of a built system from its intended design.

## Example

A small team builds a quick demo of an ordering tool. The company then uses it for real work. Nobody discards the demo code, so it stays. Each new request gets another fast patch. Over time, the team cordons off the worst area of code and alternates feature work with cleanup periods.

## Trade-offs

Cordoning off bad code controls decline but does not remove the bad code.
