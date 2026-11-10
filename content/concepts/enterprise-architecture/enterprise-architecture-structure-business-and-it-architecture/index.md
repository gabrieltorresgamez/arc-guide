---
title: Enterprise Architecture Layers
slug: enterprise-architecture-structure-business-and-it-architecture
category: enterprise-architecture
kind: concept
summary: 'Enterprise architecture describes an organization in layers: business, data, application and
  technology. Higher layers use services of lower layers, and lower layers realize higher-layer elements.
  This lets you trace a business need down to its technical basis.'
arc42:
- 3
- 5
- 7
step: s10-document
related:
- togaf
- business-architecture
- data-architecture
- application-architecture
- technology-architecture
- enterprise-architecture-management
- traceability
- relationship-between-enterprise-architecture-and-application-architecture
checks:
- The document names the layers or domains it uses (business, data, application, technology).
- Cross-layer relationships (use/serving and realization) are shown, not just isolated layers.
- Business objects can be traced through data objects to the artifacts that realize them.
- The business layer covers strategy, governance, organization and key business processes.
sources:
- url: https://en.wikipedia.org/wiki/The_Open_Group_Architecture_Framework
  title: TOGAF - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/ArchiMate
  title: ArchiMate - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://archimate.visual-paradigm.com/cross-layer-alignment-a-guide-to-serving-and-realization-relationships/
  title: 'Cross-Layer Alignment: A Guide to Serving and Realization Relationships - Visual Paradigm'
  site: archimate.visual-paradigm.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Three layers with serving and realization links between them.
review:
  status: generated
  flags: []
---

## Explanation

An organization can describe itself in layers. Links between layers keep the whole picture consistent.

**Four domains in TOGAF**

TOGAF (see the article "TOGAF") rests on four related areas called architecture domains: business, data, application and technology.

- **Business architecture** covers strategy, governance, organization and key business processes.
- **Data architecture** describes the structure of the organization's logical and physical data assets.
- **Application architecture** is a blueprint for the individual systems to be deployed.
- **Technology architecture** is the fourth domain. See the article "Technology Architecture".

**Three layers in ArchiMate**

The ArchiMate core framework uses three layers: business, application and technology. Each layer has passive structure, behavior and active structure.

- The application layer supports business components with application services.
- The technology layer provides hardware and communication infrastructure for the application layer.

**How layers connect**

Two kinds of link matter most.

- **Use.** Higher layers use the services of lower layers. This is the most important relation between layers.
- **Realization.** A lower-layer element may realize a comparable higher-layer element. For example, a data object realizes a business object.

Realization can chain through derivation. An artifact realizes a data object. So it also indirectly realizes the business object.

**Why it matters**

Elements and relationships that cross layers make the architecture description coherent.

## Example

A small shop sells goods online. The business layer holds an "Order" business object. The application layer holds an "Order record" data object that realizes it. A file in the system, an artifact, realizes that record. If the shop changes what an order means, the team follows the links down. They see which data and which files are affected.

## Trade-offs

One caution: elements that link layers play a central role in a coherent architecture description.
