---
title: Use Case Goal Level
slug: use-case-goal-levels
category: functional-requirements
kind: concept
summary: Use case goal level describes how high or low a use case sits in a hierarchy of goals. The user-goal
  level, called sea level or blue, is the most important level for writing use cases.
arc42:
- 1
- 3
step: s03-functional-requirements
related:
- use-case
- use-case-template
- use-case-goal-hierarchy-with-include-relationships
- use-case-completeness-check
- use-case-diagram
- goal-hierarchy-to-component-mapping
- user-story-vs-use-case
- method-phase-working-with-functional-requirements
checks:
- Each use case is labeled with its goal level, so readers know what kind of discussion to expect.
- User-goal use cases each have one actor, one sitting and one measurable outcome.
- Subfunction use cases exist only where several user-goal use cases reuse them.
- Steps of summary-level use cases are described by sea-level use cases.
sources:
- url: https://pjhobday.wordpress.com/2010/05/28/setting-use-case-goal-levels/
  title: Setting Use Case Goal Levels | InBetween
  site: pjhobday.wordpress.com
  accessed: '2026-11-09'
- url: https://www.w3computing.com/systemsanalysis/use-case-levels/
  title: Use Case Levels (Use case Modeling)
  site: w3computing.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Use_case
  title: Use case - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.dsc.ufcg.edu.br/~garcia/cursos/ger_processos/seminarios/Crystal/Use%20Cases,%20Ten%20Years%20Later.htm
  title: Use Cases, Ten Years Later
  site: dsc.ufcg.edu.br
  accessed: '2026-11-09'
- url: https://llm-coding.github.io/Semantic-Anchors/anchor/cockburn-use-cases/
  title: Cockburn Use Cases — Semantic Anchors
  site: llm-coding.github.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'Goal levels: a summary goal splits into user goals, which share a subfunction.'
review:
  status: generated
  flags: []
---

## Explanation

A use case describes how a user reaches a goal with a system (see the article "Use Case"). Goals come at different heights. Some are very broad, "up in the clouds". Others are tiny, "down in the mud". Getting a card into an ATM is a "down in the mud" goal.

Cockburn sorts use cases by goal level, using a sea-level metaphor with colors:

- **Summary level (white):** a broad goal. Each of its steps is likely a separate user goal, described in its own sea-level use case. So steps sit one level below.
- **User goal (blue, sea level):** the level Cockburn considers most important.
- **Subfunction (indigo):** writing these is often worthwhile.
- **Too low (black):** writing these is almost never worthwhile.

**How to recognize a user goal**

- The user seeks to complete it in a single sitting.
- It has one actor, one sitting, and one measurable outcome.
- A person should manage one blue activity in roughly 2 to 20 minutes.
- Test question: can the primary actor go away happy after having done this?

**Subfunctions**

Pull out a subfunction only when several user-goal use cases reuse it.

**Marking the level**

Cockburn recommends labeling each use case with its goal level, using a symbol. Readers then know what kind of discussion to expect, because writers work at different levels.

## Example

An online shop has a broad white goal: "Run the shop's sales." Its steps are separate blue goals, each with its own use case: "Place an order", "Track a delivery", "Return an item". Each passes the "go away happy" test.

Several of these need the shopper to find the right product. That shared piece becomes one indigo subfunction use case, reused by the blue ones. Typing a postal code into a form field is too low (black), so it gets no use case.

## Trade-offs

Writing black-level use cases is almost never worth the effort. Indigo ones are often worth writing.
