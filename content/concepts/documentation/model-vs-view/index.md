---
title: Model vs. View
slug: model-vs-view
category: documentation
kind: concept
summary: A model is structured data holding the elements of an architecture and how they relate. A view
  is a diagram built on top of that model. Each view serves the concerns of certain stakeholders.
arc42:
- 5
- 6
- 7
step: s10-document
related:
- architecture-view
- architecture-viewpoint
- c4-model
- 4-1-view-model
- iso-iec-ieee-42010-architecture-description-model
- stakeholder-concern
- modeling-tool-vs-drawing-tool
- architecture-view-model
checks:
- Diagrams are described as views of a model that is kept separate from them.
- Each view states which stakeholders and concerns it addresses.
- The conventions for each view type (viewpoint) are defined apart from the views themselves.
- The documentation includes a building block view showing the static decomposition of the system.
sources:
- url: https://www.viewpoints-and-perspectives.info/home/viewpoints/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
- url: https://c4model.com/tooling
  title: Tooling | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://docs.structurizr.com/as-code
  title: Why “as code”? | Structurizr
  site: docs.structurizr.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/4%2B1_architectural_view_model
  title: 4+1 architectural view model - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: One model, several views for different stakeholders.
review:
  status: generated
  flags: []
---

## Explanation

An architecture has many parts and many readers. No single picture suits everyone. Two ideas help: the model and the view.

**Model.** The model is structured data about the architecture. It is not visual. It exists apart from any picture of it.

**View.** A view presents one or more structural aspects of an architecture. It shows how the architecture addresses stakeholder concerns. In C4 modeling tools, a diagram is a view created on top of the model. The tool renders the view as a diagram.

**Several views, one model.** You can build different views on the same model. Kruchten's 4+1 approach describes an architecture through multiple views. It has four views: logical, development, process and physical. Scenarios are the "plus one". Views show the system from the standpoint of different stakeholders, for example end users, developers, system engineers and project managers.

**Viewpoint versus view.** A viewpoint is a set of conventions for building one type of view. It covers patterns, templates and the stakeholders the view serves. The view is the instance made by following those conventions.

**Tooling.** The Structurizr DSL provides a clean separation between the model (content) and the views (presentation).

**A standard view.** The arc42 building block view shows how the system is statically broken down into building blocks. The arc42 template makes this view mandatory for every architecture documentation made with it.

## Example

A team describes an online shop. The model lists the web shop, the payment service and the order database, and how they connect. One view shows only the web shop and its neighbors, for business readers. Another view shows the internal blocks, for developers. Both views draw on the same model.
