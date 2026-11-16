---
title: Use Case
slug: use-case
order: 40
category: functional-requirements
kind: artifact
summary: A use case is a structured description of how a system responds to requests from outside actors.
  It organizes requirements around user goals and can be kept brief or written in detail.
arc42:
- 3
- 6
step: s03-functional-requirements
related:
- uml-use-case-diagram
- user-stories-vs-use-cases
- user-story
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
- url: https://socadk.github.io/design-practice-repository/artifact-templates/DPR-UseCase.html
  title: design-practice-repository | Summaries of artifacts, templates, practices, and techniques for
    agile architecting (DPR-mm) and service design (SDPR-nn).
  site: socadk.github.io
  accessed: '2026-11-09'
- url: https://www.martinfowler.com/bliki/IncludeAndExtend.html
  title: Include And Extend
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/UseCase.html
  title: Use Case
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://pjhobday.wordpress.com/2010/05/28/setting-use-case-goal-levels/
  title: Setting Use Case Goal Levels | InBetween
  site: pjhobday.wordpress.com
  accessed: '2026-11-09'
- url: https://www.w3computing.com/systemsanalysis/use-case-levels/
  title: Use Case Levels (Use case Modeling)
  site: w3computing.com
  accessed: '2026-11-09'
- url: https://www.dsc.ufcg.edu.br/~garcia/cursos/ger_processos/seminarios/Crystal/Use%20Cases,%20Ten%20Years%20Later.htm
  title: Use Cases, Ten Years Later
  site: dsc.ufcg.edu.br
  accessed: '2026-11-09'
- url: https://llm-coding.github.io/Semantic-Anchors/anchor/cockburn-use-cases/
  title: Cockburn Use Cases — Semantic Anchors
  site: llm-coding.github.io
  accessed: '2026-11-09'
- url: https://ootips.org/use-cases-done.html
  title: (ootips) When Are Use Cases Done?
  site: ootips.org
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=26553&seqNum=5
  title: 'Understanding the Hidden Complexity of Requirements | Becoming a Software Developer Part 4:
    Understanding Use Cases and Requirements | InformIT'
  site: informit.com
  accessed: '2026-11-09'
- url: https://github.com/socadk/design-practice-repository/blob/master/artifact-templates/DPR-UseCase.md
  title: design-practice-repository/artifact-templates/DPR-UseCase.md at master · socadk/design-practice-repository
    · GitHub
  site: github.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://examples.arc42.org/systems/mama/05-building-block-view/
  title: Building Block View · arc42 Examples
  site: examples.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A use case is a structured description of how a system behaves when an outside party, called an actor, makes a request. An actor can be a person or another system. Use cases organize requirements as a narrative of how users relate to the system and use it to reach their goals.

Jacobson described the technique in a 1987 OOPSLA paper. It was based on work at Ericsson, where it captured and specified a system's requirements. UML is the Unified Modeling Language (see the article UML (Unified Modeling Language)).

**Levels of detail**

Cockburn describes a more detailed structure for a use case. He allows teams to simplify it when less detail is needed. Many teams write use cases from a structured template, though informal writing also works. The article Use Case covers the structure.

Cockburn also suggests marking each use case with a symbol for its goal level. The article Use Case explains this.

**Diagrams**

 See the article UML Use Case Diagram.

**Compared with user stories**

Stories are finer-grained chunks used for planning. The article User Stories vs. Use Cases compares the two.

**More about use cases.**

- **Use Case Template:** A use case template is a fixed form for writing a use case as text. Teams can use a full or a short version.
- **Use Case Goal Level:** Use case goal level describes how high or low a use case sits in a hierarchy of goals. The user-goal level, called sea level or blue, is the most important level for writing use cases.
- **Use Case Completeness Check:** A use case set is complete when it is not too small, not too large and not off target. Asking people for missing use cases is a start, but it needs a clearer measure.
- **Use Case as Goal-Responsibility Contract between Actors:** A use case describes an actor who wants to reach a goal by using a system. It works like a contract between stakeholders, which the system enforces.
- **Goal Hierarchy to Component Mapping:** A use case can carry a goal level, and its scope can range from a whole organization down to one component.

## Example

A bank describes a use case called "Change PIN" for its cash machine. The actor is the customer. The text describes the requests the customer makes and how the system responds. A brief use case of two to four sentences gives the overview. A fuller template adds detail for readers who need it.

## Trade-offs

Use cases are often too large to estimate usefully. Teams that plan work in small chunks may therefore need finer-grained user stories as well. Detailed templates can be simplified when less detail is needed.
