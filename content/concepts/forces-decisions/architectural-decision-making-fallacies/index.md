---
title: Architectural Decision Making Fallacies
slug: architectural-decision-making-fallacies
category: forces-decisions
kind: concept
summary: Architectural decisions often fail through familiar flawed reasoning, such as copying the crowd
  or leaning on one story. Each fallacy has a countermeasure. Naming them helps teams decide consciously
  and record decisions durably.
arc42:
- 9
- 4
step: s09-decisions
related:
- architectural-decision-record
- architectural-decision
- adr-common-mistakes-and-remediations
- smart-requirements
- architectural-decision-management-practices
- arc42-architecture-decisions
- levels-of-architectural-decisions
- decision-dependencies
checks:
- Context and requirements are stated explicitly, so decisions can be compared with earlier projects.
- Decision records justify choices with SMART quality criteria, not single anecdotes.
- Each decision record states its scope and does not mix system-wide and local arguments.
- Pattern choices and technology or product choices are in separate but related records.
- The expected lifecycle of the system, such as disposable or durable, is stated.
sources:
- url: https://ozimmer.ch/practices/2025/09/01/ADMFallacies.html
  title: Seven Architectural Decision Making Fallacies (and Ways Around Them)
  site: ozimmer.ch
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

Several fallacies weaken architectural decisions. Each comes with a countermeasure. Some bias is unavoidable in big decisions. General advice is to identify decisions proactively, make them consciously, and document them durably as Architectural Decision Records (see "Architectural Decision Record").

**Blind flight.** The team skips context modeling and requirements analysis, and does not elicit non-functional requirements or make quality goals specific and measurable. The countermeasure is to make the context explicit and compare it with earlier projects, then use it to elicit specific and measurable non-functional requirements.

**Following the crowd.** The team assumes that what works for others will work for them. The countermeasure is to "beat the street" (when needed). Market or technology community trends alone are bad scouts, and reusing a solution without checking that requirements are compatible is a smell. Apply a recognized method or your own heuristics when moving from analysis to design.

**Anecdotal evidence.** One positive or negative example from tribal knowledge carries the whole argument. The countermeasure is to provide balanced, fair judgments. Use SMART quality requirements as criteria that justify decisions in the records, and make tradeoffs and confidence levels explicit. See "SMART Requirements".

**Blending whole and part.** Someone judges a whole architectural style by one concept with a bad reputation, or assumes the whole style is good because one concept fits. The countermeasure is divide and conquer. Be clear about the scope of each decision. Keep system-wide and local arguments in separate records.

**Abstraction aversion.** The team decides concepts, technologies, and products at the same time in one "mashup" record. The countermeasure is to navigate between abstract and concrete levels. Keep abstract, conceptual arguments and concrete, technological ones in separate but related records. Pattern choices and product choices should go in separate but related records.

**Golden hammer.** The countermeasure is to keep growing the architecture toolbox. Stay curious and try new practices, patterns, and tools.

**Ignoring the time dimension.** This fallacy assumes architectures do not drift or erode. The countermeasure is to make the expected lifecycle explicit, for example disposable or durable. Look back and think ahead.

## Example

A team must pick a messaging approach for a new order system. One member says, "A well-known company uses it, so we should too." That is following the crowd. Another recalls one failed project with a similar tool. That is anecdotal evidence. The architect instead writes down the context and the measurable quality targets, and states whether the system is disposable or durable. She then records the pattern choice in one decision record and the product choice in a second, related record.

## Trade-offs

Writing separate, related records and making context explicit takes effort. Some bias cannot be removed. The goal is conscious, documented decisions, not perfectly neutral ones.
