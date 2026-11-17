---
title: ISO/IEC/IEEE 42010 Architecture Description Standard
slug: iso-iec-ieee-42010-architecture-description-standard
order: 90
category: documentation
kind: standard
summary: ISO/IEC/IEEE 42010 is an international standard for describing architectures. It separates a
  system's architecture from its description, and it builds the description from views and viewpoints.
arc42:
- 1
- 5
step: s10-document
related:
- architectural-perspective
- enterprise-architecture-framework
- architecture-view
- architecture-viewpoint
- stakeholder
- concern
- architecture-view-model
- arc42-architecture-documentation-template
- c4-model
checks:
- The document describes the architecture through one or more architecture views.
- Each viewpoint used states which stakeholder concerns it frames.
- The description is kept distinct from the architecture of the system it describes.
- Viewpoints are written as conventions for building views, not as vague viewing angles.
- Key decisions are recorded with their rationale and the alternatives that were not chosen.
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
- url: http://www.iso-architecture.org/42010/cm/
  title: 'ISO/IEC/IEEE 42010: Conceptual Model'
  site: iso-architecture.org
  accessed: '2026-11-17'
- url: https://trakviewpoints.sourceforge.io/what_is_an_architecture_viewpoint.html
  title: What is an Architecture Viewpoint?
  site: trakviewpoints.sourceforge.io
  accessed: '2026-11-09'
- url: https://www.viewpoints-and-perspectives.info/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
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

ISO/IEC/IEEE 42010 is a standard about how to describe an architecture. It does not describe one particular architecture. It defines the ideas an architecture description should use, based on a conceptual model of terms [src:4].

**History.** IEEE Standard 1471 was the predecessor. It formalized the view concepts in 2000 [src:3]. The 2011 edition of 42010 was approved by ISO member bodies in July 2011, by a vote of 21 to 0 [src:2]. A new edition, ISO/IEC/IEEE 42010:2022, was released in November 2022 [src:2].

**Architecture versus description.** The standard treats a system's architecture and the description of it as two different things. It defines architecture as the fundamental concepts or properties of a system in its environment, embodied in its elements, its relationships and the principles of its design and evolution [src:4]. So a system has an architecture even if nobody has written it down. The architecture description is the work product that expresses it. It can be a document, a set of models, a model repository or another form, because the standard does not prescribe a format.

**The core terms (2011 edition)**

- *Stakeholder:* an individual, group or organization with concerns for the system, such as a user, owner, maintainer or auditor. See Stakeholder.
- *Concern:* any interest in the system, such as its purpose, cost, safety or interoperability. See Concern.
- *Viewpoint:* a set of conventions for building, interpreting, using and analyzing one type of view. It frames a specific set of concerns and can name notations, model kinds and analysis methods. See Architecture Viewpoint.
- *View:* expresses the architecture for one or more stakeholders and their concerns, following the conventions of its viewpoint. A description consists of one or more views. See Architecture View.
- *Model and model kind:* a view is made of models. A model kind sets the conventions for one type of model.
- *Correspondence:* a relation between elements of a description, such as traceability or consistency. A correspondence rule can enforce it.
- *Decision and rationale:* a decision pertains to one or more concerns and can raise new ones. The rationale records the reasoning behind it and the alternatives that were not chosen.

So the chain runs from concerns, to a viewpoint that frames them, to a view, to the description that collects the views.

**Changes in the 2022 edition.** The subject of a description is now an *entity of interest* instead of a system of interest [src:4]. Architecture models are now called *view components*. Two concepts are new: *stakeholder perspectives* group concerns, and *architecture aspects* are characteristics of the entity that views reflect.

**Frameworks and languages.** An architecture framework sets a common practice for creating and using descriptions within one domain or community. TOGAF, MODAF, Kruchten's 4+1 view model and RM-ODP are examples. An architecture description language (ADL) is any form of expression used in descriptions, for example SysML or ArchiMate.

**Related approaches.** Rozanski and Woods build their book on three key concepts: stakeholders, viewpoints and perspectives (see Architectural Perspective). The TRAK framework was designed to comply with the 2011 edition [src:1]. Its authors had not assessed the 2022 edition, though they did not expect different results [src:1].

## Example

A team builds an online shop. The owner worries about running costs. Operations staff worry about uptime. The team picks one viewpoint for each worry. The cost viewpoint leads to a view of hosting. The uptime viewpoint leads to a view of servers and failover. Together these views form the architecture description. The running shop itself stays separate from those documents.
