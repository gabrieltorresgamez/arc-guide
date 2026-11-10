---
title: Architectural View Type
slug: architectural-view-types
category: documentation
kind: concept
summary: An architectural view type is a category of diagram that shows one kind of structure of a system.
  Different view types show different structures of the same system, so each diagram should name its type.
arc42:
- 5
- 7
step: s10-document
related:
- architecture-view
- architecture-viewpoint
- architecture-view-model
- purpose-of-views
- arc42-documentation-template
- distribution-view
- iso-iec-ieee-42010-architecture-description-standard
- matching-diagram-type-to-system-aspect
checks:
- Each diagram is labeled with the type of view it shows, such as building block view or deployment view.
- The document contains a building block view, because arc42 makes it mandatory.
- The building block view starts with the white box of the whole system at level 1, and deeper levels
  zoom into selected blocks.
- The deployment view shows the technical infrastructure and maps building blocks to infrastructure elements.
sources:
- url: https://www.viewpoints-and-perspectives.info/home/viewpoints/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-7/
  title: 7 - Deployment view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: One system, several view types, each showing a different structure
review:
  status: generated
  flags: []
---

## Explanation

A system has more than one structure. You can look at how it divides into parts. You can look at the infrastructure it runs on.

**View and viewpoint.** One catalog of architecture documentation defines a *view* as a representation of structural aspects of an architecture. It defines a *viewpoint* as a collection of patterns, templates and conventions for building one type of view. The viewpoint is the recipe. The view is the result. (See *Architecture View* and *Architecture Viewpoint*.)

**Different views of one system.** That same catalog lists six core viewpoints: Functional, Information, Concurrency, Development, Deployment and Operational. They are not six systems. They are different views of one system.

**Views in arc42.** The arc42 template (see *arc42 Architecture Documentation Template*) also asks for specific views:

- The *building block view* shows how the system is statically split into building blocks. It is mandatory. It is a hierarchy of black boxes and white boxes. Level 1 is the white box of the whole system. Deeper levels zoom into selected blocks.
- The *deployment view* documents the technical infrastructure. It also maps the building blocks to the infrastructure elements.

These two views answer different questions about the same system. One shows the parts. The other shows where the parts sit on the infrastructure.

## Example

A team documents an online shop. One diagram splits the shop into parts and is labeled "Building block view, level 1". A second diagram shows the infrastructure and which parts are mapped to it, and is labeled "Deployment view". Both diagrams describe the same shop. The labels tell the reader which structure each one shows.
