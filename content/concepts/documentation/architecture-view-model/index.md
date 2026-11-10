---
title: Architecture View Model
slug: architecture-view-model
category: documentation
kind: concept
summary: An architecture view model is a ready-made set of viewpoints that fit together to describe a
  system. Reusing one, such as 4+1, avoids inventing views and avoids one overloaded model.
arc42:
- 5
- 6
- 7
- 8
step: s10-document
related:
- 4-1-view-model
- architecture-viewpoint
- architecture-view
- zachman-framework
- iso-iec-ieee-42010-architecture-description-standard
- c4-model
- arc42-documentation-template
- common-features-of-architecture-frameworks
checks:
- The documentation states which set of viewpoints (view model) it uses, rather than an ad hoc collection
  of diagrams.
- Each view covers one aspect of the architecture and is not an overloaded all-in-one model.
- If 4+1 is used, a small set of scenarios is included to illustrate the architecture.
- The building block view is present, since arc42 requires it in every architecture documentation.
sources:
- url: https://en.wikipedia.org/wiki/4%2B1_architectural_view_model
  title: 4+1 architectural view model - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.viewpoints-and-perspectives.info/home/viewpoints/
  title: Software Systems Architecture
  site: viewpoints-and-perspectives.info
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/RM-ODP
  title: RM-ODP - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://zachman-feac.com/zachman/about-the-zachman-framework
  title: About the Zachman Framework - Zachman International - FEAC Institute
  site: zachman-feac.com
  accessed: '2026-11-09'
- url: https://c4model.com/
  title: Home | C4 model
  site: c4model.com
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

A complex system cannot be captured in one model. Rozanski and Woods warn against a single, overloaded, all-encompassing model. They split the architecture description into separate but related views. Each view describes one aspect of the architecture.

A **viewpoint** is a collection of patterns, templates and conventions for building one type of view. (See *Architecture Viewpoint* and *Architecture View*.) The IEEE standard does not prescribe a fixed set of views. Rozanski and Woods offer a catalog of core viewpoints. (See *ISO/IEC/IEEE 42010 Architecture Description Standard*.)

**Kruchten's 4+1 model** was introduced in a 1995 IEEE Software article, "Architectural Blueprints". It describes software-intensive systems through multiple concurrent views:

- The **logical view** covers the functionality offered to end users.
- The **development view**, also called the implementation view, shows the system from a programmer's perspective.
- The **physical view**, also called the deployment view, shows the system from a system engineer's perspective.
- The **+1** is a small set of scenarios (use cases). They illustrate the architecture and form a fifth view.

(See *4+1 View Model* for the full model.)

**RM-ODP** defines five complementary viewpoints. The enterprise viewpoint covers purpose, scope and policies. The information viewpoint covers what the information means and how it is processed. The technology viewpoint covers the technology choices made for the system.

The **Zachman Framework** is a matrix. Its columns are communication interrogatives and its rows are reification transformations. (See *Zachman Framework*.)

Other approaches are related but differ in kind. **C4** is a diagramming approach with hierarchical diagrams: context, containers, components and code. It does not depend on a notation. **arc42** has a building block view that shows the static decomposition. It is mandatory in every architecture documentation. Runtime views and crosscutting concepts complement it.

## Example

A team building an online shop adopts a 4+1-style set of views. One view lists the features customers use. Another shows how developers organize the code. A third shows the servers the shop runs on. A few scenarios, such as "customer places an order", tie the views together. When a reviewer asks "where do we describe hosting?", the answer is already in the set.

## Trade-offs

Splitting the description into several views helps you avoid the risk of a single overloaded model. Approaches differ in kind: C4 is a diagramming approach, and arc42 pairs a mandatory building block view with other views. Pick the one that fits your system and stakeholders.
