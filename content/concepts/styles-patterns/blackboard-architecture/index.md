---
title: Blackboard Pattern
slug: blackboard-architecture
category: styles-patterns
kind: pattern
summary: The blackboard pattern lets independent expert modules build a solution together through one
  shared memory. A control component decides which module runs next. It began in speech recognition and
  is now used for LLM agent teams.
arc42:
- 4
- 5
- 6
- 8
step: s07-solution-strategy
related:
- architectural-pattern
- architectural-style
- publish-subscribe-pattern
- shared-database
- pipe-and-filter-pattern
- microkernel-pattern
- layers-pattern
- broker-pattern
checks:
- The document identifies the blackboard as the shared, structured memory that holds the partial solution.
- Each knowledge source is described as an independent module with a specific expertise.
- The control component is named, and its rule for choosing the next knowledge source is described.
- In an LLM-agent design, agents communicate only through the blackboard, which holds the history.
sources:
- url: https://en.wikipedia.org/wiki/Blackboard_(design_pattern)
  title: Blackboard (design pattern) - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://arxiv.org/html/2507.01701v1
  title: Exploring Advanced LLM Multi-Agent Systems Based on Blackboard Architecture
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://arxiv.org/abs/2507.01701
  title: '[2507.01701] Exploring Advanced LLM Multi-Agent Systems Based on Blackboard Architecture'
  site: arxiv.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Knowledge sources read and write only the shared blackboard. The control component picks which
    one runs next.
review:
  status: generated
  flags: []
---

## Explanation

The blackboard pattern has three kinds of parts.

- **The blackboard.** It is a structured, global memory. It holds objects from the solution space, meaning the partial results of the problem being solved.
- **Knowledge sources.** These are specialized modules. Each has its own representation and contributes a specific piece of expertise. They do not need to know about each other, but they must understand the problem state and the blackboard's representation.
- **The control component.** It decides at runtime which knowledge source runs next. The scheduler applies domain-specific heuristics (practical rules of thumb) to rate which sources to run.

In LbMAS, a recent LLM version of the pattern, agents communicate solely through the blackboard. The blackboard holds all historical context. It acts as public storage and replaces the memory modules that LLM agents usually have individually.

The pattern was identified by the Hearsay-II project and first applied to speech recognition.

LbMAS is an LLM multi-agent system built on a blackboard. Its control unit is itself an LLM agent. It selects the acting agents based on the blackboard's current content. In LbMAS, the cycle ends when the maximum iteration number is reached or the decider agent is selected and gives the solution.

For related ideas, see [Architectural Pattern](architectural-pattern) and [Publish-Subscribe Pattern](publish-subscribe-pattern).

## Example

A team of software agents reviews a contract. One agent extracts clauses and posts them on the blackboard. A second agent reads the clauses and posts a list of risky wording. A third agent drafts a summary from what is on the board. A control component looks at the board after each step and picks the next agent. The agents never call each other. The rounds stop when the agents agree on the result.

## Trade-offs

The pattern is described as providing reusability, changeability and robustness.

The control component generally takes the form of a complex scheduler that uses domain-specific heuristics to rate which sources to run.
