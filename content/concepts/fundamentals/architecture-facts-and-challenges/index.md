---
title: Implicit Architecture
slug: architecture-facts-and-challenges
category: fundamentals
kind: concept
summary: Every system has an architecture, even if nobody planned, documented or understood it. An unplanned
  architecture tends to pile up technical debt and makes the system harder to maintain.
arc42:
- 11
- 5
step: s12-evolve
related:
- unsystematic-accidental-architecture
- architecture-decay
- technical-debt
- software-architecture
- big-ball-of-mud
- maintainability
- motivation-for-architecture-documentation
- architecturally-evident-coding-style
checks:
- The document states the intended architecture, so it can be compared with the implemented one.
- The document records known gaps between intended and implemented architecture as risks or technical
  debt.
- There is a process or tool to keep the architecture description in step with code changes.
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
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Every software system has an architecture. This is true whether or not the team thinks about it.

When a team does not choose its architecture on purpose, the result is an *implicit* architecture. It exists, but it is not visible or well communicated to the team. Crisp warns that such a system leaves you knee-deep in technical debt.

**Why it matters**

In an email exchange with Martin Fowler, Ralph Johnson concluded that "Architecture is about the important stuff. Whatever that is." A poor architecture adds to cruft. Cruft is made of elements of the software that impede developers' understanding. It makes software harder to modify. High internal quality, in turn, helps a team deliver faster.

**Intended versus implemented**

Research on architecture erosion finds that it shows up through architectural violations and structural issues, and also through problems in software quality and during software evolution.

As systems evolve, their architectures inevitably change. Architects who track implementation changes and update the architectural documentation find this time-consuming and error-prone.

**Finding the architecture again**

Understanding the architecture is vital for maintaining large systems. Many automatic architecture recovery techniques have been proposed to ease the work of keeping architectural documentation up to date, though existing solutions still have limitations.

## Example

A small team builds an online shop quickly. Nobody draws a design. Over two years, features are added wherever they fit.

A new developer asks how the parts fit together. No document answers it, and the original design was never written down. The shop still has an architecture, but it is implicit. The developer must read the code to find it. Each change is slow because its effects are unclear.

## Trade-offs

Keeping architectural documentation up to date as the system changes is time-consuming and error-prone for architects.
