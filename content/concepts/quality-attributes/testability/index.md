---
title: Testability
slug: testability
category: quality-attributes
kind: quality-attribute
summary: Testability is how well a system supports its own testing. High testability makes faults easier
  to find by testing. Low testability means more test effort.
arc42:
- 10
- 1
- 4
step: s04-quality-requirements
related:
- testability-general-scenario
- maintainability
- integrability-deployability-and-testability-tactics
- iso-iec-25010-quality-model
- reliability
- fault
- quality-attribute
- architectural-tactic
checks:
- The document states how testers can observe intermediate and final results of the system.
- Testability is listed as a quality goal where changes to the system are expected, with its link to risk
  reduction.
- Testability is treated under maintainability and also considered under reliability.
sources:
- url: https://arxiv.org/abs/1801.02201
  title: '[1801.02201] A survey on software testability'
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Software_testability
  title: Software testability - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010/57-maintainability
  title: Maintainability
  site: iso25000.com
  accessed: '2026-11-08'
- url: https://quality.arc42.org/articles/iso-25010-shortcomings
  title: Shortcomings of ISO 25010 | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Testability is the degree to which a system, or a part of it under test, supports its own testing. In other words, the system helps you test it.

When testability is high, finding faults by testing is easier. A fault is a defect in the software (see Fault). When testability is low, the team needs more test effort.

**Observability.** Observability is a core part of testability. It means you can see test results, both intermediate and final. If a tester cannot see what the system did, they cannot judge whether it worked.

**Standard definition.** The ISO/IEC 25010 quality model (see ISO/IEC 25010 Product Quality Model) describes testability as how effectively and efficiently you can establish test criteria for a system, product or component.

**Where it sits.** ISO 25010 places testability under maintainability. Maintainability is about how effectively and efficiently you can modify a product. The arc42 quality model notes this placement. It argues that testability also belongs under reliability, so it should appear in both places.

**Why it matters.** When you maintain or change a system, testability reduces risk.

## Example

A team builds an order system. Testers can see the intermediate results of a price calculation, not only the final total. When a total is wrong, they see which step failed. In a system that shows only the final total, the same fault takes longer to find. That system has lower testability and needs more test effort.
