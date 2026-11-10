---
title: Stakeholder Perspective and Concern
slug: stakeholder-perspective-and-concern
category: documentation
kind: concept
summary: A stakeholder is a person, team or organization with an interest in a system. Their interests
  are called concerns. Architecture documentation must address these concerns, and the concerns decide
  which views you build.
arc42:
- 1
- 10
step: s01-goals-stakeholders
related:
- stakeholder
- concern
- stakeholder-concern
- architecture-view
- architecture-viewpoint
- iso-iec-ieee-42010-architecture-description-model
- arc42-introduction-and-goals
- stakeholder-identification
checks:
- The document contains a stakeholder overview that lists roles and each stakeholder's expectations of
  the architecture and its documentation.
- Each view states which stakeholder concerns it addresses.
- Each viewpoint names the stakeholders whose concerns it reflects.
- The quality goals are the ones most important to the major stakeholders.
sources:
- url: https://quality.arc42.org/standards/iso-42010
  title: ISO/IEC/IEEE 42010 - Architecture Description | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://www.viewpoints-and-perspectives.info/home/viewpoints/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
- url: https://www.viewpoints-and-perspectives.info/home/stakeholders/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-1/
  title: 1 - Introduction and Goals | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Stakeholders hold concerns about the entity of interest. Viewpoints and views address those
    concerns.
review:
  status: generated
  flags: []
---

## Explanation

Start with the thing being described. ISO/IEC/IEEE 42010 calls it the *entity of interest*. It can be a system, software, an enterprise or another thing whose architecture you describe (see ISO/IEC/IEEE 42010 Architecture Description Model).

**Stakeholders** are individuals, teams or organizations with an interest in that entity.

**Concerns** are the interests those stakeholders hold in it. Typical examples are performance, security and maintainability.

Different stakeholder groups have their own requirements, interests and needs. The architect must balance and prioritize them.

**How concerns shape documentation**

- A *view* shows how the architecture deals with the concerns of one or more stakeholders. So concerns drive which views you build. See Architecture View.
- A *viewpoint* names the stakeholders whose concerns it reflects. This links stakeholders and concerns to the choice of viewpoint. See Architecture Viewpoint.
- arc42 asks for an explicit stakeholder overview. For each stakeholder, it lists their expectations of the architecture and its documentation.
- arc42 quality goals are the ones most important to the major stakeholders. They influence fundamental architectural decisions.

## Example

A team documents an online booking system. The operations team cares about maintainability. The security officer cares about security. The business sponsor cares about performance during sales.

The architect lists these three stakeholders and their concerns. Then the architect picks views that address each concern. One view might show deployment for operations. Another might show data protection for the security officer. Each view states which concern it serves.

## Trade-offs

Stakeholder groups have different needs, so their concerns can compete. The architect must balance and prioritize them.
