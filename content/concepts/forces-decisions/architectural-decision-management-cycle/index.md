---
title: Architectural Decision Management Cycle
slug: architectural-decision-management-cycle
category: forces-decisions
kind: method
summary: 'The cycle has five logical steps for each architectural decision: identify it, evaluate options,
  decide, record the outcome in an ADR, and check that the problem is solved. Teams may repeat steps for
  the same decision.'
arc42:
- 9
step: s09-decisions
related:
- architectural-decision-record
- architectural-decision
- architecturally-significant-requirement
- markdown-architectural-decision-records-madr
- y-statement
- definition-of-ready-for-architectural-decisions
- last-responsible-moment
- decision-dependencies
checks:
- Each ADR logs the resolution of at least one architecturally significant requirement.
- Each ADR names its decision makers.
- Each decision lists at least two options and the criteria (decision drivers) used to compare them.
- Each ADR records the outcome, its justification and its consequences.
- Outdated ADRs are marked as superseded.
sources:
- url: https://ozimmer.ch/practices/2023/12/01/ADDefinitionOfReady.html
  title: A Definition of Ready for Architectural Decisions (ADs)
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2022/11/22/MADRTemplatePrimer.html
  title: The Markdown ADR (MADR) Template Explained and Distilled
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2023/04/03/ADRCreation.html
  title: How to create Architectural Decision Records (ADRs) — and how not to
  site: ozimmer.ch
  accessed: '2026-11-09'
- url: https://ozimmer.ch/practices/2021/04/23/AnyDecisionRecords.html
  title: ADR = Any Decision Record? Architecture, Design and Beyond
  site: ozimmer.ch
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: The five logical steps of the cycle. Steps can be repeated for the same decision.
review:
  status: generated
  flags:
  - single-domain
---

## Explanation

An architectural decision (see Architectural Decision) is a design choice that shapes a system. The decision management cycle describes how a team works through one such choice. It has five steps. They are logical steps, not a rigid sequence.

**Step 1: Identify.** The team identifies a design issue and the options that address it.

**Step 2: Evaluate options.** The team compares options against a set of criteria. These criteria are also called decision drivers.

**Step 3: Decide.** The team chooses one option. A decision is ready for this step when criteria such as known stakeholders, a pressing time, understood requirements, at least two alternatives and a chosen record template are met. The choice rests on the criteria and analysis from Step 2. Decision making is a team activity. Teams should prepare, make and record decisions at the Most Responsible Moment.

**Step 4: Record.** The team writes down the outcome, the justification and the consequences. It also names the decision makers, so someone is accountable.

**Step 5: Enforce and evaluate.** The team monitors whether the design problem from Step 1 is actually solved. Many decisions never reach this step.

**Links to ADR formats.** The MADR format (see Markdown Architectural Decision Records) has a Decision Drivers section. It holds the desired qualities, forces and constraints behind a decision. Its optional Confirmation section covers Step 5. It describes how the implementation is enforced and evaluated, for example through reviews or tests. MADR's core is close to Nygard's 2011 ADR proposal. MADR evolved from that format and from Y-statements.

**Iteration.** The same decision can run through the steps several times. Teams should also be ready to revise a decision as design work evolves. An outdated record can be marked superseded.

## Example

A team must choose how its web shop sends order data to a billing system. Fast response times rank high, so the team treats this as a priority decision. It lists two options and compares them against criteria such as response time and effort. Two named people choose one option. They record the choice, the reasons and the consequences in an ADR. Later, a review checks whether orders now flow fast enough. If not, the team reopens the decision and may supersede the old record.

## Trade-offs

Many decisions never reach Step 5. The steps are logical, so a team can go back and forth or repeat them.
