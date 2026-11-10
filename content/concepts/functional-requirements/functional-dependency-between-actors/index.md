---
title: Use Case as Goal-Responsibility Contract between Actors
slug: functional-dependency-between-actors
category: functional-requirements
kind: concept
summary: A use case describes an actor who wants to reach a goal by using a system. The system under design
  is responsible for delivering that goal, which works like a contract between the actor and the system.
arc42:
- 3
- 1
- 6
step: s03-functional-requirements
related:
- use-case
- use-case-goal-levels
- use-case-template
- use-case-diagram
- use-case-completeness-check
- responsibility-allocation
- user-story-vs-use-case
- arc42-context-and-scope
checks:
- Each use case is named after the primary actor's goal, using an active-verb phrase.
- The primary actors, the supporting (secondary) actors and the system under design are identified.
- Scenarios show the system's responsibility next to each actor action.
- Use cases state the goal level, and goals are not set far above the system's behavior.
sources:
- url: https://www.dsc.ufcg.edu.br/~garcia/cursos/ger_processos/seminarios/Crystal/Use%20Cases,%20Ten%20Years%20Later.htm
  title: Use Cases, Ten Years Later
  site: dsc.ufcg.edu.br
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Use_case
  title: Use case - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Goals and responsibilities between a primary actor, the system under design and a secondary
    actor.
review:
  status: generated
  flags: []
---

## Explanation

A use case describes an actor trying to reach a goal by using the system. The actor who wants the goal is the primary actor. The system under design is abbreviated SuD.

**The contract idea.** The computer's actions enforce a contract between the stakeholders (the people with an interest in the system).

**Prose, not code.** A use case is a prose description of how the system behaves toward the outside world. At identification, it is named according to the goal it represents for its primary actor.

**Supporting actors.** To find actors, look among the stakeholders, the primary and supporting (secondary) actors, the SuD itself, and the internal actors (the components of the SuD).

**Goal sizes.** Goals come in different sizes. Writers work at different goal levels. For example, winning a contract is a very high-level goal, "up in the clouds" relative to an ATM's behavior.

**Failure and backups.** A use case can describe achieving a goal. It can also describe failing to achieve it. This lets you write down what happens when a goal is missed.

## Example

An online shop sells goods. A customer (primary actor) wants to pay for an order. The shop is the SuD. To do so, the shop relies on a card service (secondary actor). The card service is outside the shop and supports it.

If the payment fails, the use case can also describe that failure.

## Trade-offs

The stakeholders-and-interests contract explains why a use case records actions that are not externally visible. Writers work at different goal levels, so each use case should mark its goal level to avoid confusing readers.
