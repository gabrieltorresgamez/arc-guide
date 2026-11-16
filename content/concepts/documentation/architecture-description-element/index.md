---
title: Architecture Description Element
slug: architecture-description-element
order: 110
category: documentation
kind: concept
summary: An architecture description element is a named part of an architecture description, such as a
  stakeholder, concern, viewpoint, view, correspondence or rationale. Naming each part lets readers find
  it, check it and refer to it.
arc42:
- 3
- 5
- 9
- 12
step: s10-document
related:
- iso-iec-ieee-42010-architecture-description-model
- iso-iec-ieee-42010-architecture-description-standard
- architecture-viewpoint
- architecture-view
- concern
- stakeholder
- traceability
- architecture-decision-rationale
checks:
- Stakeholders, concerns and viewpoints are each named and listed, and each concern is covered by a viewpoint.
- Each viewpoint states its concerns, its stakeholders, and the notations or methods used for its views.
- Correspondences between views or models are recorded in some stated format, such as a table.
- Correspondence rules are stated, and it is clear whether each applies to this AD only or to the whole
  framework.
- Rationale is recorded as a separate, identifiable part of the AD.
sources:
- url: https://www.mit.edu/~richh/writings/emery-hilliard2009.pdf
  title: 'Every Architecture Description Needs a Framework: Expressing Architecture'
  site: mit.edu
  accessed: '2026-11-10'
- url: https://www.evs.ee/en/iso-iec-ieee-42010-2022
  title: ISO/IEC/IEEE 42010:2022 - EVS standard evs.ee | en
  site: evs.ee
  accessed: '2026-11-10'
diagrams:
- file: diagram-1.mmd
  caption: Parts of an architecture description and how they nest.
review:
  status: generated
  flags: []
---

## Explanation

An architecture description (AD) is the document that describes a system's architecture. The 2022 edition of ISO/IEC/IEEE 42010 separates two things: the architecture of the thing you care about, and the AD that expresses it.

**What the parts are**



See *Stakeholder*.
See *Concern*.
See *Architecture Viewpoint*.

See *Architecture View*.

See *Architecture Decision Rationale*.




**Viewpoints and models**

The standard also specifies conformance for viewpoints and model kinds.

**Correspondences and rules**





## Example

A team documents an online shop. They name a stakeholder "operations team" and a concern "recovering from a server failure". They name a viewpoint "deployment" that covers that concern and says to use a box-and-line notation with a legend. The view built from it is "Deployment view, production". A rule says every service in the component view must appear in the deployment view. A small table records which service runs on which server. A short note explains why they chose two servers instead of one.

## Trade-offs


