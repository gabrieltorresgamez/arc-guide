---
title: ISO/IEC/IEEE 42010 Architecture Description Standard
slug: iso-iec-ieee-42010-architecture-description-standard
category: documentation
kind: standard
summary: ISO/IEC/IEEE 42010 is an international standard for describing architectures. It separates a
  system's architecture from its description, and it builds the description from views and viewpoints.
arc42:
- 1
- 5
step: s10-document
related:
- iso-iec-ieee-42010-architecture-description-model
- architecture-view
- architecture-viewpoint
- stakeholder
- concern
- architecture-view-model
- arc42-documentation-template
- c4-model
checks:
- The document describes the architecture through one or more architecture views.
- Each viewpoint used states which stakeholder concerns it frames.
- The description is kept distinct from the architecture of the system it describes.
sources:
- url: https://trak.sourceforge.io/iso_42010.html
  title: TRAK Architecture Framework - Conformance with International Standard ISO/IEC/IEEE 42010
  site: trak.sourceforge.io
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/ISO/IEC_42010
  title: ISO/IEC 42010 - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=1766161
  title: 'Software Systems Architecture: Viewpoints and Views | Architectural Views | InformIT'
  site: informit.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Software_architecture_description
  title: Software architecture description - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: An architecture description is formed from views; a viewpoint frames stakeholder concerns.
review:
  status: generated
  flags: []
---

## Explanation

ISO/IEC/IEEE 42010 is a standard about how to describe an architecture. It does not describe one particular architecture. It defines the ideas an architecture description should use.

**History.** IEEE Standard 1471 was the predecessor. It formalized the view concepts in 2000. The 2011 edition of 42010 was approved by ISO member bodies in July 2011, by a vote of 21 to 0. A new edition, ISO/IEC/IEEE 42010:2022, was released in November 2022.

**Architecture versus description.** The standard treats a system's architecture and the description of it as two different things. The description is what you write down to tell others about the architecture.

**Views and viewpoints.** An architecture description consists of one or more architecture views. A viewpoint frames one or more stakeholder concerns. See the articles Architecture View, Architecture Viewpoint, Stakeholder and Concern.

**Languages.** An architecture description language (ADL) is any form of expression that describes a software architecture.

## Example

A team builds an online shop. The owner worries about running costs. Operations staff worry about uptime. The team picks one viewpoint for each worry. The cost viewpoint leads to a view of hosting. The uptime viewpoint leads to a view of servers and failover. Together these views form the architecture description. The running shop itself stays separate from those documents.
