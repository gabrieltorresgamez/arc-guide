---
title: Self-Documentation
slug: self-documentation
category: documentation
kind: principle
summary: Self-documentation means a system carries the information needed to understand it inside itself,
  mainly in its code. This cuts separate documents that fall out of date, but it cannot capture reasons
  or the full picture.
arc42:
- 5
- 8
- 9
step: s10-document
related:
- documentation-as-code
- traceability
- design-for-change
- architecturally-evident-coding-style
- domain-driven-design
- guidelines-for-documentation
- arc42-documentation-template
- diagrams-as-code
checks:
- Interface or API documentation is generated from the source (for example with Javadoc) instead of written
  separately.
- Architecture documentation is stored as plain text under version control next to the code.
- Documents are built and published by a toolchain, not assembled by hand.
- Rationale for technology choices is written down by humans, because code does not show it.
- The document does not claim that code alone is the full documentation.
sources:
- url: https://martinfowler.com/bliki/CodeAsDocumentation.html
  title: Code As Documentation
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://arc42.org/documentation/
  title: arc42 Documentation - arc42
  site: arc42.org
  accessed: '2026-11-09'
- url: https://www.isaqb.org/blog/will-we-soon-stop-writing-architecture-documentation-ourselves/
  title: Will we soon stop writing architecture documentation ourselves?
  site: isaqb.org
  accessed: '2026-11-09'
- url: https://man.archlinux.org/man/extra/jdk-openjdk/javadoc-openjdk27.1.en
  title: javadoc-openjdk27(1) — Arch manual pages
  site: man.archlinux.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

**Why it matters.** Missing or outdated documentation is a typical failure. Documentation that stays up to date with little effort avoids this problem.

**Code as the main source.** Code is the only artifact detailed and precise enough to be the primary documentation. It is not the only documentation, though. It is also not automatically good documentation. Like any documentation, it can be clear or gibberish. Clarity takes deliberate effort.

**Generated documentation.** Tools can turn information in the source into readable documents:

- Javadoc reads declarations and documentation comments in Java source files. Its standard doclet (the pluggable part that produces the output) creates HTML.
- arc42 documentation (see the arc42 Architecture Documentation Template article) can be built and published by a toolchain such as docToolchain, or by static-site generators.
- Generative AI can extract structured documentation from source code structures, comments, dependencies and build scripts. An arc42 building block view is one example.

**Close to the code.** arc42 works particularly well as docs-as-code, where architecture documentation is treated like source code. That means plain-text formats under version control, next to the code. See the Documentation as Code article.

**Limits.** Source code does not tell the full story. The reason a team chose a technology, for example, is often not visible in code.

## Example

A team writes a payment module in Java. They give classes and methods clear names and add doc comments to the public interfaces. The build runs Javadoc and publishes the HTML on every change, so the interface description is generated from the doc comments. The team also keeps a short text file next to the code. It explains why they chose a particular payment provider, because the code cannot show that.

## Trade-offs

Clear code needs deliberate effort, and code can be gibberish. Generated documents show what is in the source. The reason for a technology choice, for example, is often not visible in the source. Further documentation is usually needed as a supplement to the code.
