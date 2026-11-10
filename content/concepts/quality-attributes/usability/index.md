---
title: Usability
slug: usability
category: quality-attributes
kind: quality-attribute
summary: Usability describes how easily and efficiently people get tasks done through a system's interface.
  It covers learning, speed, error handling and satisfaction, and it links to how cheaply the interface
  can be changed.
arc42:
- 1
- 10
- 8
step: s04-quality-requirements
related:
- usability-tactics
- usability-scenario
- modifiability
- iso-25010-2023-revision
- quality-attribute
- iso-iec-25010-quality-model
- model-view-controller-pattern
- quality-attribute-scenario
checks:
- The document states which usability aspects matter (for example learnability, efficiency, error minimization)
  for the key user tasks.
- Cancel or undo support is described for actions users may want to abandon.
- The user interface is separated from the application so interface changes have limited impact.
- The document distinguishes interaction capability (product quality) from quality in use.
sources:
- url: https://www.nngroup.com/articles/usability-101-introduction-to-usability/
  title: 'Usability 101: Introduction to Usability - NN/G'
  site: nngroup.com
  accessed: '2026-11-09'
- url: https://ercim.eu/publication/Ercim_News/enw46/bass.html
  title: Supporting Usability through Software Architecture
  site: ercim.eu
  accessed: '2026-11-09'
- url: https://www.sonarsource.com/resources/library/iso-iec-25010-explained/
  title: 'ISO/IEC 25010 Explained: 9 Software Quality Characteristics That Matter | Sonar'
  site: sonarsource.com
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-08'
- url: https://www.nngroup.com/articles/ten-usability-heuristics/
  title: 10 Usability Heuristics for User Interface Design - NN/G
  site: nngroup.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Usability is about how well people can get things done with a system's user interface. Architects care because it ties to how the system is structured.

**Core aspects.** Five aspects are commonly used:

- **Learnability:** how fast people learn to do basic tasks with the design.
- **Efficiency:** how quickly people work once they have learned the design.
- **Memorability:** how easily returning users regain proficiency after time away.
- **Error minimization:** how often errors happen, how severe they are, and how easily people recover.
- **Satisfaction:** how pleasant the design is to use.

**In the ISO quality model.** ISO/IEC 25010:2023 calls this area interaction capability. It evaluates how effectively users can interact with software to reach their goals. It has eight subcharacteristics. Two of them are operability (the product is easy to operate and control) and user error protection (the product prevents operation errors). The article on the ISO/IEC 25010:2023 revision covers the full list.

Interaction capability is a product-quality characteristic. It describes intrinsic properties of the software. Quality in use is different. It evaluates whether users actually achieve their goals when they use the software.

**Undo and cancel.** A well-known heuristic is user control and freedom. Users need a clearly marked emergency exit, so they can leave an unwanted action without a long process. In a design, this means support for cancel and undo.

**Link to modifiability.** Separating the presentation from the rest of the application limits the impact of modifications, which makes user interface changes relatively easy after user testing reveals problems. Some aspects of usability are not affected by this separation.

**Business value.** In one NN/g finding, usability redesigns improved user experience metrics by 75% on average. This is not a direct return-on-investment estimate.

## Example

A team builds an online order form. Testers say new users finish a first order slowly (learnability). Some users enter wrong quantities and cannot correct them (error minimization). The team adds a cancel button and an undo step, and the form rejects impossible quantities. Because the interface code is separate from the order logic, the team changes the form several times without touching the order logic.

## Trade-offs

Note that the 75% figure is an average from redesigns. It does not predict the return on any single project.
