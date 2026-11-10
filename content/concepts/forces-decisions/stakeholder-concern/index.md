---
title: Stakeholder Concern
slug: stakeholder-concern
category: forces-decisions
kind: concept
summary: A stakeholder concern is an interest that a person or group has in a system, such as performance,
  security, or maintainability. Concerns shape what the architecture must address and which views describe
  it.
arc42:
- 1
- 10
step: s01-goals-stakeholders
related:
- stakeholder
- concern
- architecture-viewpoint
- architecture-view
- stakeholder-perspective-and-concern
- stakeholder-identification
- iso-iec-ieee-42010-architecture-description-standard
- arc42-introduction-and-goals
checks:
- Stakeholders and their expectations are recorded, for example in a table with roles and expectations.
- Each stakeholder concern is explicitly addressed in the architecture description.
- Each viewpoint names the stakeholders and concerns it reflects.
- Each view states which concerns it addresses.
sources:
- url: https://www.viewpoints-and-perspectives.info/home/viewpoints/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
- url: https://quality.arc42.org/standards/iso-42010
  title: ISO/IEC/IEEE 42010 - Architecture Description | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://www.viewpoints-and-perspectives.info/home/stakeholders/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-1/
  title: 1 - Introduction and Goals | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/1-3/
  title: 'Tip 1-3: Highlight the business goals of the system! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Stakeholders hold concerns. Viewpoints are framed by concerns, and views address them.
review:
  status: generated
  flags: []
---

## Explanation

A **concern** is an interest that a stakeholder has in a system. ISO 42010 gives examples such as performance, security, and maintainability.

A **stakeholder** is a person, team, or organization with an interest in the realization of the system. Stakeholder types include acquirers, who oversee procurement, and developers, who build and deploy the system from specifications. See the article Stakeholder for more.

Each stakeholder group has its own requirements, interests, and needs. The system must meet them. So different groups bring different concerns.

**How concerns connect to other things**

- A view shows how the architecture deals with the concerns of one or more stakeholders.
- A viewpoint defines which stakeholders' concerns it reflects. In ISO 42010, a viewpoint is a specification for building a single view. It names the stakeholders, the concerns, and the modeling techniques. In this way, concerns frame viewpoints. See Architecture Viewpoint and Architecture View.
- The quality goals of the most important stakeholders influence fundamental architectural decisions. arc42 recommends a table with roles, names, contacts, and what each stakeholder expects from the architecture and its documentation.
- Business objectives are often more global and higher-level than detailed system requirements.

**Why it matters for documentation**

ISO 42010 helps ensure completeness by requiring that stakeholder concerns are explicitly addressed in the architecture description.

## Example

A town builds an online permit system. The acquirer, who oversees procurement, cares about what the system will cost to buy. The developers care about building it from clear specifications. Both concerns go into a stakeholder table with each role and its expectations. One view, such as a diagram of the main parts of the system, may address both concerns. The architecture description then shows explicitly how each concern is addressed.

## Trade-offs

Every stakeholder group brings its own needs, and a single model cannot serve all stakeholders. Making stakeholder concerns explicit helps make the description more complete.
