---
title: Architecture Description Element
slug: architecture-description-element
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

An architecture description (AD) is the document that describes a system's architecture. The 2022 edition of ISO/IEC/IEEE 42010 separates two things: the architecture of the thing you care about, and the AD that expresses it. AD elements belong to the description, not to the architecture itself.

**What the parts are**

One proposal for the make-up of an AD lists these parts:

- **Stakeholders** are the people or groups with an interest in the system. See *Stakeholder*.
- **Concerns** are the matters those stakeholders care about. See *Concern*.
- **Viewpoints** are templates for building views. See *Architecture Viewpoint*.
- **Correspondence rules** are constraints that link two or more models.
- **Views** are the descriptions that result from applying viewpoints. See *Architecture View*.
- **Correspondences** are the recorded links between models or views.
- **Rationale** explains why choices were made. See *Architecture Decision Rationale*.
- **Administrative information** is the required record keeping.

The first four together form an architecture framework. The views and correspondences must satisfy that framework.

**Viewpoints and models**

A viewpoint states which concerns it covers and which stakeholders care about them. It also names the notations, models and methods used to create, read and analyze a view. A map legend is a good comparison: it explains the symbols and gives the basis for reading the map. Views are made of architecture models, so models are further parts of the description. The standard also specifies conformance for viewpoints and model kinds.

**Correspondences and rules**

The 2000 edition of IEEE 1471 only asked authors to record known inconsistencies between views. A working draft of the revision (ISO/IEC WD4 42010) introduced model correspondences. These relate two or more models to express consistency, traceability, refinement or other dependencies. The draft sets no format for them. Relations, tables or graphics all work, and tables are the traditional choice for traceability.

A correspondence rule is a constraint on two or more models. You can write it inside one AD, where it applies to that AD only. You can also put it in a framework, where it applies to every AD that uses the framework.

## Example

A team documents an online shop. They name a stakeholder "operations team" and a concern "recovering from a server failure". They name a viewpoint "deployment" that covers that concern and says to use a box-and-line notation with a legend. The view built from it is "Deployment view, production". A rule says every service in the component view must appear in the deployment view. A small table records which service runs on which server. A short note explains why they chose two servers instead of one.

## Trade-offs

The draft gives no required format for correspondences, so the team must choose one. Tables are common but are only one option. The standard gave little normative guidance on recording rationale and decisions at the time of the draft, and framework developers can consider ways to capture them.
