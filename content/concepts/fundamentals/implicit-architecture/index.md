---
title: Implicit Architecture
slug: implicit-architecture
category: fundamentals
kind: concept
summary: Every system has an architecture, even if nobody planned, documented or understood it. An unplanned
  architecture tends to pile up technical debt and makes the system harder to maintain.
arc42:
- 11
- 5
step: s12-evolve
related:
- big-ball-of-mud
- technical-debt
- software-architecture
- maintainability
- motivation-for-architecture-documentation
- architecturally-evident-coding-style
checks:
- The document states the intended architecture, so it can be compared with the implemented one.
- The document records known gaps between intended and implemented architecture as risks or technical
  debt.
- There is a process or tool to keep the architecture description in step with code changes.
- For a system without documentation, a first overview was created in a short timebox and then refined with stakeholder feedback.
sources:
- url: https://blog.crisp.se/2012/12/18/mikaelbrodd/is-your-software-architecture-explicit
  title: Is your software architecture explicit? - Crisp’s Blog
  site: blog.crisp.se
  accessed: '2026-11-09'
- url: https://martinfowler.com/architecture/
  title: Software Architecture Guide
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://arxiv.org/abs/2112.10934
  title: '[2112.10934] Understanding Software Architecture Erosion: A Systematic Mapping Study'
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://arxiv.org/abs/2311.04643
  title: '[2311.04643] Software Architecture Recovery with Information Fusion'
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://aim42.org/patterns/software-archeology/
  title: Software Archeology | aim42
  site: aim42.org
  accessed: '2026-11-17'
- url: https://aim42.org/patterns/static-code-analysis/
  title: Static Code Analysis | aim42
  site: aim42.org
  accessed: '2026-11-17'
- url: https://aim42.org/patterns/runtime-artifact-analysis/
  title: Runtime Artifact Analysis | aim42
  site: aim42.org
  accessed: '2026-11-17'
- url: https://aim42.org/patterns/architectural-understanding/
  title: Architectural Understanding | aim42
  site: aim42.org
  accessed: '2026-11-17'
- url: https://leanpub.com/read/arc42inpractice/chapter-v
  title: 'arc42 in Practice, chapter V: arc42 in Everyday Work'
  site: leanpub.com
  accessed: '2026-11-17'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Every software system has an architecture. This is true whether or not the team thinks about it.

When a team does not choose its architecture on purpose, the result is an *implicit* architecture. It exists, but it is not visible or well communicated to the team. Crisp warns that such a system leaves you knee-deep in technical debt [src:1].

**Why it matters**

In an email exchange with Martin Fowler, Ralph Johnson concluded that "Architecture is about the important stuff. Whatever that is." A poor architecture adds to cruft. Cruft is made of elements of the software that impede developers' understanding. It makes software harder to modify. High internal quality, in turn, helps a team deliver faster.

**Intended versus implemented**

Research on architecture erosion finds that it shows up through architectural violations and structural issues, and also through problems in software quality and during software evolution.

As systems evolve, their architectures inevitably change. Architects who track implementation changes and update the architectural documentation find this time-consuming and error-prone.

**Finding the architecture again**

Understanding the architecture is vital for maintaining large systems. Many automatic architecture recovery techniques have been proposed to ease the work of keeping architectural documentation up to date, though existing solutions still have limitations.

The aim42 improvement method describes practices for the same job:

- *Software archeology.* First make sure you can build the system from scratch. Then get an aerial view of its biggest structures and sketch them. The most frequent terms in the code are a start for a glossary. Commits per developer, for example from `git shortlog -ns`, show parts of the system where knowledge may be lost.
- *Static code analysis.* Tools find the building blocks and their dependencies and measure complexity, coupling and cohesion. This suits medium and large code bases.
- *Runtime artifact analysis.* Log files, stack traces and usage patterns show what the running system really does.
- *Stakeholder interviews.* The solution strategy is often learned from experienced developers of the system.

**Work in short timeboxes.** The arc42 authors suggest writing such hindsight documentation in a small timebox. Three to five knowledgeable people can create an acceptable overview in two to four hours. For each arc42 section they note what stakeholders need and what already exists, and they work on the gaps. The first version aims at important content, not completeness, and is used to collect feedback. For any documentation task they suggest a fixed timebox of at least 15 minutes and rarely more than 4 hours [src:9]. More valuable topics get longer timeboxes.

## Example

A small team builds an online shop quickly. Nobody draws a design. Over two years, features are added wherever they fit.

A new developer asks how the parts fit together. No document answers it, and the original design was never written down. The shop still has an architecture, but it is implicit. The developer must read the code to find it. Each change is slow because its effects are unclear.

## Trade-offs

Keeping architectural documentation up to date as the system changes is time-consuming and error-prone for architects.
