---
title: Stakeholder Questions Addressed in Views
slug: stakeholder-questions-addressed-in-views
category: documentation
kind: concept
summary: Stakeholders ask recurring questions about a system. Each question points to a view that should
  answer it. Picking views from these questions keeps documentation useful for its audience.
arc42:
- 1
- 3
- 5
- 10
step: s10-document
related:
- stakeholder-concern
- architecture-viewpoint
- architecture-view
- stakeholder-identification
- context-view
- arc42-introduction-and-goals
- iso-iec-ieee-42010-architecture-description-standard
- view-creation-method
checks:
- The documentation lists its stakeholders, including those who need it for their work.
- Each view or viewpoint states which stakeholders' concerns it serves.
- Questions about external systems and users are answered in a context view.
- The most important quality goals are stated and tied to the major stakeholders.
- The building block view explains the static decomposition without implementation detail.
sources:
- url: https://www.viewpoints-and-perspectives.info/home/viewpoints/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-1/
  title: 1 - Introduction and Goals | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Stakeholder questions point to the views that answer them
review:
  status: generated
  flags: []
---

## Explanation

A single large model of a system serves individual stakeholders poorly. Each person struggles to find the part that interests them. Splitting the description into separate views is the only successful approach the source authors have found. Together, the views describe the whole system.

A viewpoint is a set of conventions for building one type of view. It also states whose concerns it reflects. The article "Stakeholder Concern" covers concerns in more detail.

Some examples of how questions map to views:

- **"Who and what does the system talk to?"** The Context viewpoint answers this. It shows how the system relates to its environment, meaning external systems and users.
- **"What are the main parts, and how are they split up?"** The arc42 building block view answers this. It shows the static decomposition. Architects can discuss it with stakeholders at an abstract level, without exposing implementation details.
- **"Which quality goals matter most?"** arc42 quality goals are the ones of highest importance to the major stakeholders. They influence fundamental architectural decisions.

arc42 asks architects to identify all stakeholders, including people who need the documentation to do their work.

## Example

A team builds an order-handling system. The project sponsor asks which quality goals matter most. A partner company asks which systems exchange data with it. A new developer asks how the system is split into parts.

The team does not write one giant document. It writes a short quality goals list for the sponsor. It draws a context view for the partner. It draws a building block view for the developer. Each reader finds an answer to their own question.

## Trade-offs

Choosing views by questions depends on knowing your stakeholders. arc42 warns that if you overlook parties involved in or affected by the system, you may get nasty surprises later in development.
