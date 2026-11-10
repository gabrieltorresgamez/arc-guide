---
title: Architectural View
slug: purpose-of-views
category: documentation
kind: concept
summary: An architectural view describes a system from the angle of one stakeholder group. Splitting the
  description into views keeps each part understandable and lets each reader find what matters to them.
arc42:
- 5
- 6
- 7
step: s10-document
related:
- architecture-view
- architecture-viewpoint
- separation-of-concerns
- stakeholder
- model-vs-view
- arc42-documentation-template
- characteristics-of-a-good-view
- contemporary-essential-views
checks:
- Each view states which stakeholders' concerns it addresses.
- No single all-in-one model tries to show every aspect of the system.
- The building block view is present and shows the static decomposition of the system.
- The building block view stays abstract and does not expose implementation details.
sources:
- url: https://www.viewpoints-and-perspectives.info/home/viewpoints/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=1766161&seqNum=4
  title: 'The Benefits of Using Viewpoints and Views | Software Systems Architecture: Viewpoints and Views
    | InformIT'
  site: informit.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A software system has many aspects. Describing all of them in one model gives a picture that is hard to understand. Such a model also rarely shows the most important features of the architecture.

An architectural view avoids this. Each view covers one aspect of the system. Together, the views describe the whole architecture.

**View and viewpoint**

A viewpoint is a reusable set of patterns, templates and conventions for building one type of view. Architects do not have to invent the content of every view from scratch. A viewpoint also states whose concerns its views reflect. See Stakeholder.

**Why views help**

- **Separation of concerns.** Packing many aspects into one picture clouds communication. It also lets aspects that should be independent become intertwined. Describing the system through separate models helps design, analysis and communication, because you can focus on each aspect separately. See Separation of Concerns.
- **Communication.** Different stakeholder groups can go straight to the parts of the description that match their concerns.
- **Managing complexity.** The architect treats each significant aspect on its own, one after another.
- **Developer focus.** The architecture description is the foundation of system design. It matters especially to developers.

**Views in arc42**

The arc42 template uses views directly. Its building block view shows the static decomposition of the system. It is mandatory in every architecture documentation. It lets you talk with stakeholders at an abstract level, without revealing implementation details. See arc42 Architecture Documentation Template.

## Example

A team documents an online shop. One view shows the main parts of the system and how they divide the work. A business owner can read it without seeing any implementation details. Other views cover other aspects, such as how the parts are installed. Each reader opens the view that matches their concerns, and no single picture has to show everything.

## Trade-offs

This article does not cover the costs of views, such as keeping several views consistent with each other.
