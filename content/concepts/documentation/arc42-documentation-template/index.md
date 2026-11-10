---
title: arc42 Architecture Documentation Template
slug: arc42-documentation-template
category: documentation
kind: framework
summary: arc42 is a free template that gives architecture information a fixed place across twelve sections.
  Teams tailor it to their needs and use it in agile, lean or formal projects.
arc42:
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
step: s10-document
related:
- c4-model
- documentation-as-code
- runtime-view
- distribution-view
- arc42-introduction-and-goals
- arc42-solution-strategy
- iso-iec-ieee-42010-architecture-description-standard
- agile-architecture
checks:
- The architecture documentation is organized by the twelve arc42 sections, tailored to the project's
  needs.
- The building block view is a hierarchy of black boxes and white boxes, with level 1 as the white box
  of the whole system.
- The runtime view uses scenarios chosen for architectural relevance, not a large number of scenarios.
sources:
- url: https://arc42.org/overview/
  title: arc42 Template Overview - arc42
  site: arc42.org
  accessed: '2026-11-09'
- url: https://arc42.org/method/
  title: arc42 method - arc42
  site: arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/home/
  title: Home | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-6/
  title: 6 - Runtime view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://github.com/arc42/arc42-template
  title: 'GitHub - arc42/arc42-template: arc42 - the template for software architecture documentation
    and communication · GitHub'
  site: github.com
  accessed: '2026-11-09'
- url: https://faq.arc42.org/questions/B-17/
  title: 'Question B-17: What about arc42 and C4? | arc42 FAQ'
  site: faq.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

arc42 is a template for documenting software architecture. It answers two questions: what to document and communicate about an architecture, and how. The template says where information belongs, and the arc42 method describes how to work through six activities. The method fits agile, lean or formal projects. Its activities have no fixed order.

**Twelve sections.** The template has twelve sections. Each has a clear purpose, and teams can tailor them to their needs. The official documentation site follows the same twelve sections. It offers keyword paths for lean documentation in agile environments and for thorough documentation in formal or audited settings.

The sections are:

1. Introduction and Goals
2. Architecture Constraints
3. Context and Scope
4. Solution Strategy
5. Building Block View
6. Runtime View
7. Deployment View
8. Cross-cutting Concepts
9. Architecture Decisions
10. Quality Requirements
11. Risks and Technical Debts
12. Glossary

**Building block view.** This section is a hierarchy of black boxes and white boxes. A black box shows what a part does without showing its inside. A white box opens it up. Level 1 is the white box of the whole system. The view abstracts the structure of the source code. Stakeholders can then discuss that structure without implementation details.

**Runtime view.** This section shows how building blocks do their job and communicate while the system runs. It uses scenarios. Authors choose scenarios for their architectural relevance. A large number is not needed.

**Open source.** arc42 is free, including for commercial use. A GitHub repository holds the AsciiDoc source of the template. Releases include all languages, styles and formats, plus a manifest of checksums. The founders maintain the English and German versions.

**Relation to C4.** The arc42 FAQ says the C4 model overlaps with some arc42 sections. It also omits parts such as quality requirements, crosscutting concepts and risks. See the article on the C4 Model.

## Example

A small team starts a new product. They create one document from the template. They describe the system as one white box with three black boxes inside. They add two runtime scenarios for the most important workflows. They tailor the template by leaving out what nobody needs. Later, a new colleague reads the document and finds each topic in the expected section.

## Trade-offs

The template says where information belongs, while the arc42 method describes how to work. The method fixes six activities and some stances, such as clarifying the most important quality requirements first, but leaves the order of the activities open. The C4 model is not a full replacement. According to the FAQ, it omits parts that arc42 covers.
