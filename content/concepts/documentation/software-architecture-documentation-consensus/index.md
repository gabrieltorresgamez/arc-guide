---
title: Software Architecture Documentation Consensus
slug: software-architecture-documentation-consensus
category: documentation
kind: concept
summary: 'Teams that document software architecture increasingly agree on the basics: split the description
  into views, build views with a small set of diagram types, and write for stakeholders. Approaches like
  arc42 and C4 follow this pattern.'
arc42:
- 5
- 6
step: s10-document
related:
- architecture-view
- c4-model
- arc42-documentation-template
- 4-1-view-model
- iso-iec-ieee-42010-architecture-description-standard
- stakeholder-concern
- documentation-as-code
- architecture-viewpoint
checks:
- The architecture description is split into several interrelated views, not one monolithic document.
- Each view states which stakeholders and concerns it addresses.
- If C4 is used, the diagrams follow the hierarchy of system, container, component and code element.
- If arc42 is used, the Building Block View and Runtime View sections are present.
sources:
- url: https://www.informit.com/articles/article.aspx?p=1766161
  title: 'Software Systems Architecture: Viewpoints and Views | Architectural Views | InformIT'
  site: informit.com
  accessed: '2026-11-09'
- url: https://c4model.com/
  title: Home | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/home/
  title: Home | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://c4model.com/abstractions
  title: Abstractions | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: An architecture description made of several views, each shaped by stakeholder concerns.
review:
  status: generated
  flags: []
---

## Explanation

One approach to documenting architecture is to avoid one large document. The architecture description is split into several separate but interrelated views.

**Views are the central element.** A view shows structural aspects of an architecture. It includes only the elements that matter to stakeholder concerns. (See Architecture View and Concern.)

**Why not one big document?** A single monolithic description is hard to keep sound. Because of its complexity, it tends to be incomplete, wrong or outdated.

**Views serve stakeholders.** A view can target one class of stakeholders, or even one person. It should address the concerns of one or more stakeholders. (See Stakeholder.)

**Diagrams help build views.** C4 is one example. It is a developer-friendly, diagram-oriented approach. It uses a small set of abstractions and diagram types, so it is easy to learn. The abstractions form a hierarchy:

- A system contains containers (applications and data stores).
- Containers contain components.
- Code elements implement the components.

**Templates organize the documentation.** arc42 arranges documentation in twelve sections. These include a Building Block View (section 5) and a Runtime View (section 6). Its documentation also tags some information as essential: despite lean and agile approaches, some information, such as quality goals, should always be documented.

## Example

A team builds an online shop. Instead of one long document, it writes short views. One view is for managers and shows the shop and the systems around it. Another is for developers and shows the parts inside the shop. Each view has a clear audience.

## Trade-offs

Splitting the description into views is presented as a more effective way to describe a complex system than a single overloaded model. C4 is easy to learn because it uses a small set of abstractions and diagram types.
