---
title: TOGAF
slug: togaf
category: enterprise-architecture
kind: framework
summary: TOGAF is an enterprise architecture framework first presented in 1995, based mainly on a US Department
  of Defense framework. Its core is the Architecture Development Method, supported by a content framework,
  a continuum and reference models.
arc42:
- 4
- 8
- 9
step: s10-document
related:
- togaf-architecture-development-method
- enterprise-architecture-management
- zachman-framework
- business-architecture
- data-architecture
- application-architecture
- technology-architecture
- iso-iec-ieee-42010-architecture-description-standard
checks:
- The document names which of the four domains (Business, Application, Data, Technology) each architecture
  description covers.
- The document states which artifacts from the content framework are used, rather than assuming TOGAF
  prescribes a format.
- Reference models, if used, are named and their constraining role on design is clear.
- Architecture governance roles are described.
sources:
- url: https://en.wikipedia.org/wiki/TOGAF
  title: TOGAF - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.grahamberrisford.com/00EAframeworks/01Fundamentals/Observations%20on%20the%207%20parts.htm
  title: ''
  site: grahamberrisford.com
  accessed: '2026-11-09'
- url: https://www.opengroup.org/togaf
  title: TOGAF | www.opengroup.org
  site: opengroup.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Main parts of TOGAF.
review:
  status: generated
  flags: []
---

## Explanation

TOGAF is a framework for architecture work across a whole organization. Development began in 1995. It drew mainly on TAFIM, a US Department of Defense framework for information management.

**The core: the ADM.** The Architecture Development Method (ADM) is the core of the framework. See the article TOGAF Architecture Development Method.

**Four domains.** TOGAF is based on four architecture domains: Business, Application, Data and Technology. Related articles cover Business Architecture, Application Architecture, Data Architecture and Technology Architecture.

**Content framework.** TOGAF offers a menu of architecture products and a metamodel. A metamodel defines the kinds of things you describe and how they link. TOGAF 9 added a formal content metamodel that links TOGAF's artifacts together. The framework does not prescribe how you document your architectures.

**Enterprise Continuum.** This is a classification structure for building blocks and artifacts. It has two parts: the Architecture Continuum and the Solutions Continuum. The repository is a separate data store that holds the building blocks and artifacts.

**Reference models.** A reference model is a general pattern that constrains and steers system design. TOGAF includes two: the III-RM and the TRM.

**Architecture capability.** Part 7 covers the roles of architects in an enterprise. Its focus is governance.

**Current edition.** The 10th Edition is split into the TOGAF Fundamental Content and the TOGAF Series Guides.

## Example

A company wants to improve its order handling. The architects use the ADM as their working cycle. They describe the business, data, application and technology domains. They pick the artifacts they need from the content framework's menu. They file reusable pieces in the Enterprise Continuum classification. They check designs against a reference model.

## Trade-offs

The content framework gives you a menu and a metamodel, not a fixed documentation method. The Enterprise Continuum only classifies material; the repository is the data store that holds it.
