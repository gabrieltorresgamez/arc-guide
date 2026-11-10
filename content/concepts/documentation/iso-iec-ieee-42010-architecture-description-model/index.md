---
title: ISO/IEC/IEEE 42010 Architecture Description Model
slug: iso-iec-ieee-42010-architecture-description-model
category: documentation
kind: standard
summary: The 42010 conceptual model separates a system's architecture from the document that describes
  it. The description is built from views. Each view follows a viewpoint, and each viewpoint frames stakeholder
  concerns.
arc42:
- 1
- 5
- 12
step: s10-document
related:
- iso-iec-ieee-42010-architecture-description-standard
- architecture-view
- architecture-viewpoint
- stakeholder
- concern
- architectural-perspective
- architecture-view-model
- stakeholder-concern
checks:
- The architecture description consists of at least one architecture view.
- Each viewpoint used states which stakeholder concerns it frames.
- The document separates the system's architecture from the description of it.
- Viewpoints are written as conventions for building views, not as vague viewing angles.
sources:
- url: https://trak.sourceforge.io/iso_42010.html
  title: TRAK Architecture Framework - Conformance with International Standard ISO/IEC/IEEE 42010
  site: trak.sourceforge.io
  accessed: '2026-11-09'
- url: https://trakviewpoints.sourceforge.io/what_is_an_architecture_viewpoint.html
  title: What is an Architecture Viewpoint?
  site: trakviewpoints.sourceforge.io
  accessed: '2026-11-09'
- url: https://www.viewpoints-and-perspectives.info/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: How stakeholders, concerns, viewpoints, views and the description relate.
review:
  status: generated
  flags: []
---

## Explanation

The standard rests on a conceptual model. A conceptual model is a small map of ideas and how they connect. This one keeps two things apart: the architecture of a system, and the architecture description that records it. The description is a document. The architecture is what the document talks about.

**The main links**

- An architecture description is formed from one or more architecture views. See *Architecture View*.
- A viewpoint frames one or more stakeholder concerns. A stakeholder is a person or group with an interest in the system. A concern is something they care about. See *Stakeholder*, *Concern* and *Architecture Viewpoint*.

So the chain runs from concerns, to a viewpoint that frames them, to a view, to the description that collects the views.

**What a viewpoint is**

A viewpoint is a set of conventions. It is not a direction from which you look at the system, like a camera angle. It states how to build and read a kind of view.

**Another book's key concepts**

Rozanski and Woods build their book on three key concepts: stakeholders, viewpoints and perspectives. They also provide a template for an architecture description. The *Architectural Perspective* article covers perspectives.

**Why it helps**

The model gives teams shared words. Two people who say "view" or "viewpoint" can mean the same thing.

**Edition note**

The TRAK method was designed to comply with the 2011 edition of the standard. Its authors had not assessed the 2022 edition, though they did not expect the results to differ.

## Example

A team documents an online shop. The operations staff care about where the software runs. The product owner ccares about how an order moves through the system. The team defines one viewpoint for each concern, with its own conventions. They then draw one view per viewpoint. Together, the views form the architecture description of the shop. The shop's architecture exists whether or not this description is written.
