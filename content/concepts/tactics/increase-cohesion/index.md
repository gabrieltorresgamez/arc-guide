---
title: Increase Cohesion
slug: increase-cohesion
category: tactics
kind: tactic
summary: Increase Cohesion is one of three groups of modifiability tactics. It keeps related responsibilities
  together and separates unrelated ones, so future changes cost less.
arc42:
- 4
- 5
- 9
step: s07-solution-strategy
related:
- split-module
- modifiability-tactics
- reduce-coupling
- coupling-and-cohesion
- high-cohesion
- refactoring
- modifiability
- tactic-trade-off-balancing
checks:
- Modules that mix unrelated responsibilities are identified, and splitting them is considered.
- The document states which modifiability tactic group (cohesion, coupling, binding time) each tactic
  belongs to.
- Runtime overhead from added structure, such as layer crossings, is acknowledged.
sources:
- url: https://www.informit.com/articles/article.aspx?p=3197432&seqNum=5
  title: 3.5 Design Concepts to Support Modifiability | Making Design Decisions | InformIT
  site: informit.com
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/library/modifiability-tactics/
  title: Modifiability Tactics | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-08'
- url: http://bradapp.blogspot.com/2008/03/software-modifiability-tactics.html
  title: 'Brad Appleton''s ACME Blog: Software Modifiability Tactics'
  site: bradapp.blogspot.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Modifiability tactics fall into three groups: Increase Cohesion, Reduce Coupling, and Defer Binding. The SEI report motivates them with the ideas of coupling, cohesion and cost. See Coupling and Cohesion for those terms, and Modifiability Tactic for the full set.

Increase Cohesion targets one problem. A module may hold responsibilities that do not belong together. When that module must change, modification costs will likely be high.

**Split Module** is the tactic for this case. The team refactors the module to separate its responsibilities. The expected result is a lower average cost for future changes. See Split Module and Refactoring.

A practitioner summary of the SEI taxonomy lists five tactics in its cohesion group (Localize Changes): Maintain Semantic Coherence, Anticipate Expected Changes, Generalize the Module, Limit Possible Options, and Abstract Common Services. Abstract Common Services hides similar services behind a common abstraction. Another source files that tactic under Reduce Coupling instead. Check which grouping a document uses.

## Example

A single "order" module handles pricing rules and also prints invoices. Any change to invoice layout risks breaking pricing. The team splits it into a pricing module and an invoicing module. Later invoice changes touch only one of them.

## Trade-offs

Structuring for modifiability can carry a runtime cost. Layered structures show this: every interaction that crosses layers pays a performance penalty. Weigh that cost against the expected drop in the average cost of change. See Tactic Trade-off Balancing.
