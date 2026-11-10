---
title: Use Case Completeness Check
slug: use-case-completeness-check
category: functional-requirements
kind: practice
summary: A use case set is complete when it is not too small, not too large and not off target. Asking
  people for missing use cases is a start, but it needs a clearer measure.
arc42:
- 1
- 3
step: s03-functional-requirements
related:
- use-case
- use-case-goal-levels
- use-case-template
- use-case-goal-hierarchy-with-include-relationships
- iterative-and-incremental-development
- acceptance-criteria
- stakeholder
- method-phase-working-with-functional-requirements
checks:
- Each use case is marked with its goal level.
- Extensions are listed separately for each use case.
- The use case set was checked against non-functional requirements and domain concepts, not only by asking
  stakeholders.
- The use case set contains no wishful thinking beyond project needs.
sources:
- url: https://ootips.org/use-cases-done.html
  title: (ootips) When Are Use Cases Done?
  site: ootips.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Use_case
  title: Use case - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=26553&seqNum=5
  title: 'Understanding the Hidden Complexity of Requirements | Becoming a Software Developer Part 4:
    Understanding Use Cases and Requirements | InformIT'
  site: informit.com
  accessed: '2026-11-09'
- url: https://www.dsc.ufcg.edu.br/~garcia/cursos/ger_processos/seminarios/Crystal/Use%20Cases,%20Ten%20Years%20Later.htm
  title: Use Cases, Ten Years Later
  site: dsc.ufcg.edu.br
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A use case describes how a user reaches a goal with a system (see Use Case). A completeness check asks whether the set of use cases is good enough to build from.

**The simple test.** The set is complete when users, the sponsor and other stakeholders cannot think of any more use cases. The source calls this answer simplistic.

**Three ways a set can fail.** The set can have too few use cases. It can have too many, for example wishful thinking far beyond what the project needs. Or it can contain the wrong ones.

**Why a measure helps.** Without a measure, judging completeness is subjective and error-prone. One suggestion is to keep a list of ways the system may vary and check the use cases against it.

**Goal levels.** Goals come in different sizes. Levels run from very high summary, through summary, user goal and subfunction, down to too low. The preferred level is user goal, also called "sea level". Mark each use case with its level so readers do not get confused (see Use Case Goal Level).

**Extensions.** An extension is a condition that leads to different interactions than the main success scenario.

**Do not rush.** Users often name use cases they had not thought of before. Give elaboration time, and expect the list to grow.

**Scope by release.** Formal capture of use cases happens later, in increments.

## Example

A team plans an online library system. Users, the sponsor and the stakeholders list their goals: "Borrow a book", "Return a book", "Pay a fine". Nobody can name more, so the simple test passes.

A reviewer then checks levels. "Run the library" is a summary goal. "Check book availability" is a subfunction. Each use case carries its level. The reviewer also checks that each use case lists its extensions, such as a book that is already borrowed. Later, a user mentions "Reserve a book". The team adds it and notes which release will include it.

## Trade-offs

The simple test is simplistic and can miss use cases, since the judgment is subjective and has nothing to measure it against. Taking more time to elaborate finds more use cases.
