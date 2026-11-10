---
title: Usability Tactic
slug: usability-tactics
category: tactics
kind: tactic
summary: Usability tactics are design choices that help users interact with a system well. Features such
  as cancel, undo and progress bars need architectural support, so teams must plan them early.
arc42:
- 4
- 8
- 10
step: s04-quality-requirements
related:
- usability
- usability-scenario
- architectural-tactic
- iso-iec-25010-quality-model
- modifiability-tactics
- separation-of-concerns
- model-view-controller-pattern
- tactic-trade-off-balancing
checks:
- The document names which usability features, such as cancel, undo or progress bars, the architecture
  must support, and plans them early.
- The presentation is separated from the rest of the application so later interface changes stay limited
  in impact.
- Usability goals reference interaction capability, including learnability and user error protection.
sources:
- url: https://ercim.eu/publication/Ercim_News/enw46/bass.html
  title: Supporting Usability through Software Architecture
  site: ercim.eu
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010/61-usability
  title: Interaction Capability
  site: iso25000.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Usability describes how well people can interact with a system. The ISO/IEC 25010 quality model calls this characteristic Interaction Capability. It means how well specified users can exchange information with a product or system. The article on the ISO/IEC 25010 Product Quality Model covers the wider model.

Two sub-characteristics of interaction capability matter here:

- **Learnability:** how well users can learn to use the functions of the system.
- **User error protection:** how well the system keeps users from making operation errors. This covers the error avoidance side of usability.

Some usability features cannot be bolted on easily. Cancellation, undo and progress bars all need support from the software architecture. A team that wants them must plan for them early.

Timing matters because late changes cost more. Time and budget pressure can also cut off rounds of user-interface improvement. The result can be a less usable system. Early architectural attention reduces this risk.

One technique limits the cost of later change. Keep the presentation (what users see) separate from the rest of the application. This limits the impact of modifications. A team can then rework the interface without reworking everything behind it.

## Example

A team builds an online editor. Early on, they plan a cancel button and a progress bar for long exports. They also keep the screen code apart from the export logic. Later, designers rework the screens after user feedback. The export logic stays untouched, and the change stays small.

## Trade-offs

Late changes are more expensive, and schedule pressure may leave no room to improve the interface. Separating the presentation from the rest of the application limits the impact of later modifications.
