---
title: Enterprise Architecture Framework
slug: enterprise-architecture-framework
category: enterprise-architecture
kind: framework
summary: An enterprise architecture framework defines how to create and use an enterprise architecture.
  It usually sorts the work into business, data, application, and technology domains. Organizations often
  treat it as a toolbox and combine several frameworks.
arc42:
- 4
- 9
step: s07-solution-strategy
related:
- togaf
- zachman-framework
- enterprise-architecture-management
- togaf-architecture-development-method
- common-features-of-architecture-frameworks
- enterprise-architecture-structure-business-and-it-architecture
checks:
- The document names which framework (or parts of frameworks) the team uses and states that it is used
  selectively or in combination.
- Architecture content is organized by business, data, application, and technology domains, or by a stated
  merged variant.
sources:
- url: https://en.wikipedia.org/wiki/Enterprise_architecture_framework
  title: Enterprise architecture framework - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/The_Open_Group_Architecture_Framework
  title: TOGAF - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://zachman-feac.com/resources/ea-articles-reference/161-understanding-and-leveraging-synergies-among-the-major-ea-frameworks-by-the-open-group
  title: 'Understanding and Leveraging Synergies Among the Major EA Frameworks by: The Open Group - Zachman
    International - FEAC Institute'
  site: zachman-feac.com
  accessed: '2026-11-10'
- url: https://zachman-feac.com/zachman/about-the-zachman-framework
  title: About the Zachman Framework - Zachman International - FEAC Institute
  site: zachman-feac.com
  accessed: '2026-11-09'
- url: https://www.bcs.org/articles-opinion-and-research/enterprise-architecture-frameworks-the-fad-of-the-century/
  title: 'Enterprise Architecture Frameworks: The Fad of the Century | BCS'
  site: bcs.org
  accessed: '2026-11-10'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

An enterprise architecture framework defines how to create and use an enterprise architecture. Enterprise architecture treats the enterprise as a large and complex system and strives to align business information systems technology with a given business strategy (see the article Enterprise Architecture).

**Domains.** Since 1993 it has been normal to divide enterprise architecture into four domains: business, data, applications, and technology, though TOGAF notes that resource and time limits often prevent building all four in full. Many frameworks merge data and applications into one information-system layer. TOGAF is built on the four domains (see the article TOGAF).

**The Zachman Framework.** It crosses stakeholder perspectives with six questions (what, how, where, who, when, and why). Its own site describes a 6 x 6 matrix, with the questions as columns and the reification transformations (Identification, Definition, and so on) as rows. Its own site calls it a structure, not a process. A structure organizes things. A process tells you the steps. The framework does not tell you how to build the result (see the article Zachman Framework).

**A toolbox.** One description calls an architecture framework a set of tools for developing many different architectures.

**Rarely used on its own.** The critic Kotusev argues that successful real-world practice has little to do with popular frameworks. In a presentation and panel discussion, John Zachman said that Zachman and TOGAF can be integrated, and recalled Allen Brown of The Open Group saying at an earlier TOGAF conference that it is "Zachman and TOGAF" rather than one or the other. The event examined how EA frameworks can co-exist well.

## Example

A company wants to document how orders flow through its business and IT. The architects sort their documents into business, data, application, and technology domains.

## Trade-offs

A structure-only framework such as Zachman's does not give you a process, so you must supply one yourself. Critics also doubt that popular frameworks drive successful practice.
