---
title: Design for Change
slug: design-for-change
category: principles
kind: principle
summary: Design for change means making the parts of a system that are likely to change easy to modify.
  Apply it only where change is foreseeable, because flexibility costs effort and can make other changes
  harder.
arc42:
- 4
- 8
- 10
- 11
step: s07-solution-strategy
related:
- loose-coupling
- modifiability
- modifiability-scenario
- information-hiding
- flexibility
- refactoring
- architectural-tactic
- technical-debt
checks:
- Likely changes are written down as change scenarios, such as a new external provider.
- At least one change scenario has a measurable limit, such as effort in person-weeks.
- External systems are accessed through a single wrapping interface, not called directly across the code.
- Flexibility is built only for foreseeable changes, not for guessed features.
- Independent change of subsystems is stated as a quality requirement.
sources:
- url: https://martinfowler.com/bliki/Yagni.html
  title: Yagni
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/designDead.html
  title: Is Design Dead?
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/eaaCatalog/gateway.html
  title: Gateway
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/10-6/
  title: 'Tip 10-6: Consider change (quality) scenarios!! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/qualities/extensibility
  title: Extensibility | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
- url: https://quality.arc42.org/requirements/independent-enhancement-of-subsystem
  title: Independent enhancement of subsystem | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Some changes are probable: a new payment provider, a different database, a new external system. Architects can prepare for these ahead of time. The aim is to make the affected part cheap to change when the day comes.

**Prepare, do not build early.** Preparing for a change differs from building the feature now. YAGNI ("you aren't gonna need it") warns against building presumptive features. Such features add complexity, and that complexity makes software harder to modify and debug. YAGNI covers capabilities built for a guessed feature. It does not cover work that makes software easier to change, such as refactoring, tests, and continuous delivery. YAGNI itself only works if the code is easy to change.

**Hide outside systems behind one interface.** The Gateway pattern wraps an external system behind a simple interface. Without it, the external API spreads through the code. Then a change, such as swapping a database for XML, becomes much harder. With a gateway, one place changes.

**Make change scenarios concrete.** arc42 recommends writing change scenarios. They cover maintainability, modifiability, changeability, and flexibility. One example turns a likely change into a measurable requirement: integrating a new external payment provider takes at most two person-weeks.

**Keep parts independent.** Changes to one subsystem should be possible without touching the others. arc42 also treats extensibility, the ability to add features, as a goal. Plugin and event-driven architectures support it.

**Spend flexibility with care.** Flexible frameworks and components cost extra up front, and the payback comes later. XP advises not building them for the first case that needs the functionality.

## Example

A team expects to replace its payment provider someday. It does not build support for three providers now. It puts all provider calls behind one payment interface and writes a scenario: a new provider must be integrable within two person-weeks. Only that one interface would change later.

## Trade-offs

Planned flexibility helps only for anticipated changes. It may hurt for unforeseen ones, because unneeded complexity makes the system harder to change in every direction except the expected one. Guessing future needs often goes wrong, especially without detailed requirements. Working on the wrong flexibility early is even more wasteful than working on the right one early. Keep flexibility to the likely change spots, and keep the code easy to change so you can add the rest later.
