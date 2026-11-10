---
title: 'UML Perspectives: Conceptual, Specification, Implementation'
slug: uml-views-conceptual-specification-implementation
category: modeling-uml
kind: practice
summary: UML diagrams can be read at three levels. Conceptual diagrams describe the real-world domain.
  Specification diagrams describe software through interfaces. Implementation diagrams describe code in
  a specific technology.
arc42:
- 5
- 8
- 12
step: s10-document
related:
- uml-unified-modeling-language
- ubiquitous-language
- domain-model
- c4-model
- uml-interface
- class-diagram
- domain-driven-design
- uml-modeling-best-practice
checks:
- Each diagram states whether it shows the domain, the software specification, or the implementation.
- Specification diagrams describe interfaces without naming a particular implementation technology.
- Implementation diagrams name the specific technology they describe.
sources:
- url: https://www.informit.com/articles/article.aspx?p=360440&seqNum=6
  title: What is the UML? | Object-Oriented Analysis and Design | InformIT
  site: informit.com
  accessed: '2026-11-09'
- url: https://c2wiki.gothdyke.mom/SyntropyMethodology.html
  title: ''
  site: c2wiki.gothdyke.mom
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/cs-cz/archive/blogs/stevecook/syntropy-book-available-online
  title: Syntropy book available online | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/bliki/UbiquitousLanguage.html
  title: Ubiquitous Language
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://c4model.com/
  title: Home | C4 model
  site: c4model.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

The same UML notation can mean different things depending on how you read it. Three perspectives make that explicit.

**Conceptual perspective.** The diagram describes things in the real world or the domain of interest. It is not about software.

**Specification perspective.** The diagram describes software abstractions or components. It uses specifications and interfaces. It does not commit to a particular implementation technology.

**Implementation perspective.** The diagram describes how software is built in a specific technology, such as Java.

**Earlier roots.** The Syntropy method used a similar split into three models. Its essential model describes the world or domain in terms of event broadcasting. Its specification model describes the software, or at least the system boundary. Its implementation model describes the software using the conventional message-passing paradigm. The 1994 Syntropy book also influenced the Object Constraint Language, which became part of UML.

**Links to other ideas.** The ubiquitous language (see the article Ubiquitous Language) should follow the domain model that the software uses. The C4 model splits a system differently. It uses software systems, containers, components and code.

## Example

A team models an online library.

- Conceptual: a diagram shows "Member", "Book" and "Loan". It uses only words the librarians use.
- Specification: a diagram shows a lending component with an interface for borrowing a book. It says nothing about the programming language or database.
- Implementation: a diagram shows the Java classes that realize that interface.

All three diagrams describe the same library, but each reads at a different level.
