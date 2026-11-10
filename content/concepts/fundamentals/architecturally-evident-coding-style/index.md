---
title: Architecturally Evident Coding Style
slug: architecturally-evident-coding-style
category: fundamentals
kind: practice
summary: An architecturally evident coding style shows architecture rules in the code itself, through
  package layout and naming conventions. Automated tests, such as ArchUnit for Java, can then check that
  the code follows those rules.
arc42:
- 5
- 8
step: s12-evolve
related:
- layered-architecture
- layers-pattern
- architecture-decay
- documentation-as-code
- self-documentation
- technical-debt
- modularity
- module
checks:
- Layers are defined as package patterns, and the allowed interactions between them are stated.
- Architecture and coding rules run as automated unit tests in the build.
- Naming conventions, such as the name pattern for methods that return collections, are checked automatically.
- For a legacy code base, existing violations are frozen so that no new ones are added.
sources:
- url: https://www.archunit.org/userguide/html/000_Index.html
  title: ArchUnit User Guide
  site: archunit.org
  accessed: '2026-11-09'
- url: https://waltz.finos.org/blog/waltz/dev/2019/01/20/arch-unit.html
  title: Formalising code architecture using ArchUnit | FINOS - Waltz
  site: waltz.finos.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Some architecture rules live only in documents or in people's heads.

**Layers as packages.** A layered architecture splits a system into layers and states how they may interact (see Layered Architecture). The Waltz project did this. It defined layers simply as matching package patterns.

**Conventions in names.** Names can carry rules too. In Waltz's data-access objects, `findXYZ()` methods are expected to return a collection or map.

**Checking the rules.** Conventions only help if they hold. ArchUnit is a free Java library for checking the architecture of code. It runs architecture and coding rules as ordinary unit tests, so rule violations show up as failing tests at build time. For layers, you define them by package patterns and state which interactions are allowed. Waltz wanted a more concrete way than a style guide to enforce its rules, and used ArchUnit for this. It also checked the naming convention above with the same tool.

**Legacy code.** Old projects may have too many violations to fix at once. ArchUnit can ignore known violations, for example by matching them with regex patterns. The aim is that the code stays covered by architecture tests, so no further violations are added to it.

## Example

A team builds an online shop in Java. They put code in three packages: `web`, `service` and `persistence`. They agree that `web` may call `service`, and `service` may call `persistence`, but never the other way around. They also agree that any method returning a list of orders starts with `find`.

They write these rules as ArchUnit tests. If a developer later makes `persistence` call `web`, the build fails and the team sees the problem at once.
