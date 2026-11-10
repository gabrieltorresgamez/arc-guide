---
title: Use Case
slug: use-case
category: functional-requirements
kind: artifact
summary: A use case is a structured description of how a system responds to requests from outside actors.
  It organizes requirements around user goals and can be kept brief or written in detail.
arc42:
- 3
- 6
step: s03-functional-requirements
related:
- use-case-template
- use-case-goal-levels
- use-case-diagram
- user-story-vs-use-case
- user-story
- use-case-completeness-check
- use-case-goal-hierarchy-with-include-relationships
- uml-unified-modeling-language
checks:
- Each use case is written as a structured description of how the system responds to requests from external
  actors.
- The level of detail of each use case fits its audience, and the template is simplified where less detail
  is needed.
- Each use case is marked with its goal level.
sources:
- url: https://martinfowler.com/bliki/UseCasesAndStories.html
  title: Use Cases And Stories
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Use_case
  title: Use case - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/agile/advantages-of-user-stories-for-requirements
  title: Advantages of User Stories over Requirements and Use Cases - Mountain Goat Software
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A use case is a structured description of how a system behaves when an outside party, called an actor, makes a request. An actor can be a person or another system. Use cases organize requirements as a narrative of how users relate to the system and use it to reach their goals.

Jacobson described the technique in a 1987 OOPSLA paper. It was based on work at Ericsson, where it captured and specified a system's requirements. The UML use case diagram comes from his Objectory notation. UML is the Unified Modeling Language (see the article Unified Modeling Language (UML)).

**Levels of detail**

Cockburn describes a more detailed structure for a use case. He allows teams to simplify it when less detail is needed. Many teams write use cases from a structured template, though informal writing also works. The article Use Case Template covers the structure.

Cockburn also suggests marking each use case with a symbol for its goal level. The article Use Case Goal Level explains this.

**Diagrams**

A use case diagram combined with short use case briefs is a handy, lightweight tool. See the article Use Case Diagram.

**Compared with user stories**

Stories are finer-grained chunks used for planning. The article User Stories vs. Use Cases compares the two.

## Example

A bank describes a use case called "Change PIN" for its cash machine. The actor is the customer. The text describes the requests the customer makes and how the system responds. A one-paragraph brief gives the overview. A fuller template adds detail for readers who need it.

## Trade-offs

Use cases are often too large to estimate usefully. Teams that plan work in small chunks may therefore need finer-grained user stories as well. Detailed templates can be simplified when less detail is needed.
