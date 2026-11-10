---
title: TOGAF Architecture Development Method
slug: togaf-architecture-development-method
category: enterprise-architecture
kind: method
summary: The TOGAF Architecture Development Method (ADM) is a cyclic, repeatable method for developing
  an enterprise architecture. An organization can tailor it, move between phases, and adapt it to agile
  work with sprints.
arc42:
- 4
- 9
step: s07-solution-strategy
related:
- togaf
- togaf-phase-c-application-architecture
- enterprise-architecture-management
- data-architecture
- application-architecture
- agile-architecture
- iterative-and-incremental-development
- common-features-of-architecture-frameworks
checks:
- The document states how the ADM was tailored to the organization's needs.
- The document shows that data architecture and application architecture are developed together in Phase
  C.
- The document explains whether and how teams return to earlier phases or repeat activities within a phase.
- If sprints are used, the document says how architecture is delivered incrementally.
- The document names how implementation is overseen (Phase G) and how change is managed (Phase H).
sources:
- url: https://en.wikipedia.org/wiki/The_Open_Group_Architecture_Framework
  title: TOGAF - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://togaf.visual-paradigm.com/2025/01/21/comprehensive-guide-to-iterative-development-with-togaf-adm/
  title: Comprehensive Guide to Iterative Development with TOGAF ADM - Visual Paradigm
  site: togaf.visual-paradigm.com
  accessed: '2026-11-09'
- url: https://www.visual-paradigm.com/guide/togaf/togaf-adm-tutorial/
  title: TOGAF ADM Tutorial
  site: visual-paradigm.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

The TOGAF Architecture Development Method (ADM) is a step-by-step way to develop an architecture for a whole organization. For the framework around it, see the article "TOGAF".

**A cycle, not a straight line.** The ADM is iterative and cyclic. Finishing one phase feeds directly into the next phases, so the work forms a continuous loop.

**Tailoring.** An organization does not have to use the ADM exactly as written. It can tailor the method to its own needs and then use it to manage the work.

**Moving back and forth.** Teams can return to an earlier phase. They can also repeat activities inside one phase to flesh out the architecture content.

**Phase C.** In Phase C, the data architecture and the application architecture are developed in combination. See "Data Architecture" and "Application Architecture" for what each covers.

**Phases G and H.** Phase G gives architectural oversight of the implementation. Phase H sets procedures for managing change to the new architecture.

**Agile use.** The ADM can be tailored for agile practice. TOGAF describes using sprints (short, fixed work periods) to deliver architecture in increments.

## Example

A company tailors the ADM to its needs and works in sprints. In one sprint, the team develops data and application architecture together for a new ordering service. A later finding shows that an earlier result was too narrow. The team goes back to that earlier phase, adjusts it, and continues. During implementation, architectural oversight checks the work. Agreed procedures then handle later changes.

## Trade-offs

The ADM gives freedom: tailoring, going back, repeating work, and using sprints. Each organization has to decide how much to tailor and how often to iterate.
