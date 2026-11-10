---
title: Voting
slug: voting
category: tactics
kind: tactic
summary: Voting compares the outputs of several redundant units and uses the majority result. A disagreement
  reveals a fault, and with three units one faulty result is outvoted.
arc42:
- 4
- 8
- 10
- 11
step: s07-solution-strategy
related:
- availability-tactics-fault-detection
- active-redundancy
- availability-tactic
- redundant-spare
- fault
- fault-tolerance
- availability
- reliability
checks:
- The document states how the voter forwards a majority result or flags a mismatch.
- The design says whether the voter is a single point of failure or is triplicated.
- Common-mode faults such as a shared specification, library, or input are discussed as a limit of voting.
- The added compute cost of running replicas (three times for TMR) is acknowledged.
sources:
- url: https://quality.arc42.org/approaches/n-version-redundancy
  title: N-Version Redundancy and Voting | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-08'
- url: https://en.wikipedia.org/wiki/Triple_modular_redundancy
  title: Triple modular redundancy - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: 'Triple modular redundancy: three units get the same input and a voter picks the majority result.'
review:
  status: generated
  flags: []
---

## Explanation

Voting is a way to detect faults. Several redundant units do the same work. A component called the voter compares their outputs. It forwards the majority result, or it flags a mismatch.

**Triple modular redundancy (TMR).** In TMR, three systems perform the same process. A majority-voting system turns their results into one output. With three units, the vote masks one faulty unit.

**The voter.** Everything depends on the voter. If a single voter fails, the whole system goes down. Some designs therefore triplicate the voters.

**Diversity.** Voting works only if the units fail independently. A shared specification error, library, or input makes every unit fail the same way. All outputs then agree, and the vote cannot catch the error. This is called a common-mode fault. N-version design reduces this risk. Independent teams build separate implementations, so a design mistake is less likely to be shared.

For the wider group of techniques, see the Fault Detection Tactic article.

## Example

A pricing service must not return a wrong fee. The team runs the fee calculation on three identical instances with the same input. A voter compares the three results. Two say 12.50 and one says 12.05. The voter forwards 12.50 and flags the odd instance. Later, all three instances share one faulty rounding library and all return 12.05. The voter sees full agreement, so it cannot catch this shared error.

## Trade-offs

- **Cost.** Running N replicas multiplies compute. TMR costs three times as much.
- **Voter risk.** A single voter is a single point of failure. Triplicating voters addresses this.
- **Shared faults.** Identical copies do not protect against a common-mode fault. Independently built versions reduce this risk, at the price of building several implementations, though the Knight & Leveson experiment showed such versions still fail together more often than independence predicts.
