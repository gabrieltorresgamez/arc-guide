---
title: Interaction Capability
slug: interaction-capability
order: 40
category: quality-attributes
kind: quality-attribute
summary: Interaction capability is the ISO/IEC 25010:2023 characteristic for how easily and efficiently
  people get tasks done through a system's interface. It covers learning, speed, error handling and satisfaction, and it links to how cheaply the interface
  can be changed.
arc42:
- 1
- 10
- 8
step: s04-quality-requirements
related:
- interaction-capability-tactics
- maintainability
- quality-attribute
- iso-iec-25010-quality-model
- model-view-controller-pattern
- quality-attribute-scenario
checks:
- The document states which usability aspects matter (for example learnability, efficiency, error minimization)
  for the key user tasks.
- Cancel or undo support is described for actions users may want to abandon.
- The user interface is separated from the application so interface changes have limited impact.
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
- url: https://quality.arc42.org/articles/iso-25010-update-2023
  title: Update on ISO 25010, version 2023 | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-08'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=1
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=2
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/appropriateness-recognizability
  title: "Appropriateness recognizability | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/learnability
  title: "Learnability | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/operability
  title: "Operability | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/user-error-protection
  title: "User error protection | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/user-engagement
  title: "User engagement | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/inclusivity
  title: "Inclusivity | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/user-assistance
  title: "User assistance | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/self-descriptiveness
  title: "Self-descriptiveness | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/new-user-completes-core-tasks-without-training
  title: "New user completes core tasks without prior training"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/compliance-to-wcag
  title: "Compliance with WCAG accessibility guidelines"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/requirements/recognize-assistive-technology
  title: "Recognize Assistive Technologies"
  site: quality.arc42.org
  accessed: '2026-11-16'
- url: https://quality.arc42.org/qualities/interaction-capability
  title: "Interaction capability | arc42 Quality Model"
  site: quality.arc42.org
  accessed: '2026-11-16'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Interaction capability is about how well people can get things done with a system's user interface. The ISO model renamed usability to interaction capability. Several sources on this page still use the name usability.

**Core usability aspects.** Nielsen Norman Group describes usability with five components:

- **Learnability:** how fast people learn to do basic tasks with the design.
- **Efficiency:** how quickly people work once they have learned the design.
- **Memorability:** how easily returning users regain proficiency after time away.
- **Errors:** how many errors people make, how severe they are, and how easily they recover.
- **Satisfaction:** how pleasant the design is to use.

**In the ISO quality model.** Interaction capability is one of the nine characteristics of ISO/IEC 25010:2023. It evaluates how effectively users can interact with software to reach their goals. The list of its eight subcharacteristics is below.

**Undo and cancel.** One of Nielsen's ten usability heuristics is user control and freedom. Users need a clearly marked emergency exit, so they can leave an unwanted action without a long process. In a design, this means support for cancel and undo.

**Link to modifiability.** Separating the presentation from the rest of the application limits the impact of modifications, which makes user interface changes relatively easy after user testing reveals problems. Some aspects of usability are not affected by this separation.

**Business value.** In one NN/g finding, usability redesigns improved user experience metrics by 75% on average. This is not a direct return-on-investment estimate.

**Tactics.** See the article Interaction Capability Tactic.

**Subcharacteristics.** The ISO/IEC 25010 model lists these subcharacteristics under this characteristic:

- **Appropriateness recognizability** means that users can tell whether the product or system suits their needs. More: [arc42 quality model](https://quality.arc42.org/qualities/appropriateness-recognizability).
- **Learnability** means that specified users can learn the product's functions within a specified amount of time. More: [arc42 quality model](https://quality.arc42.org/qualities/learnability).
- **Operability** means that the product has attributes that make it easy to operate and control. More: [arc42 quality model](https://quality.arc42.org/qualities/operability).
- **User error protection** means that the system protects users from making operation errors. More: [arc42 quality model](https://quality.arc42.org/qualities/user-error-protection).
- **User engagement** means that the user interface presents functions and information in an inviting and motivating way, which encourages continued interaction. More: [arc42 quality model](https://quality.arc42.org/qualities/user-engagement).
- **Inclusivity** means that people of various backgrounds, such as different ages, abilities, cultures and languages, can use the product or system. More: [arc42 quality model](https://quality.arc42.org/qualities/inclusivity).
- **User assistance** means that people with the widest range of characteristics and capabilities can use the product to reach their goals in a specified context of use. More: [arc42 quality model](https://quality.arc42.org/qualities/user-assistance).
- **Self-descriptiveness** means that the product shows the information users need, where they need it, so its capabilities and use are obvious without extra effort such as reading documentation or asking for help. More: [arc42 quality model](https://quality.arc42.org/qualities/self-descriptiveness).

**In the arc42 quality model.** The arc42 quality model has its own page on [Interaction capability](https://quality.arc42.org/qualities/interaction-capability).

**Example quality requirements.** The arc42 quality model has example quality requirements for this characteristic: [New user completes core tasks without prior training](https://quality.arc42.org/requirements/new-user-completes-core-tasks-without-training), [Compliance with WCAG accessibility guidelines](https://quality.arc42.org/requirements/compliance-to-wcag), [Recognize Assistive Technologies](https://quality.arc42.org/requirements/recognize-assistive-technology).

## Example

A team builds an online order form. Testers say new users finish a first order slowly (learnability). Some users enter wrong quantities and cannot correct them (errors). The team adds a cancel button and an undo step, and the form rejects impossible quantities. Because the interface code is separate from the order logic, the changes to the form have limited impact on the order logic.

## Trade-offs

Note that the 75% figure is an average from redesigns. It does not predict the return on any single project.
