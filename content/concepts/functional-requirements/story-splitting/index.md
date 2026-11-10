---
title: Story Splitting
slug: story-splitting
category: functional-requirements
kind: practice
summary: Story splitting breaks a large or uncertain user story into smaller ones that still deliver value.
  Teams use patterns such as workflow steps, operations, data, interfaces and spikes, then check the result.
arc42:
- 1
- 4
step: s03-functional-requirements
related:
- user-story
- epic
- invest-criteria
- story-mapping
- card-conversation-confirmation
- acceptance-criteria
- agile-enterprise-backlog-model
- method-phase-working-with-functional-requirements
checks:
- Large stories were checked against INVEST (ignoring size), split with named patterns, and the split
  was then evaluated.
- Stories using the word "manage" were examined and split by operation.
- The first story delivers a simple end-to-end case before variations in data or interface are added.
- Spike stories appear only where the implementation is poorly understood and other patterns failed.
sources:
- url: https://www.humanizingwork.com/the-humanizing-work-guide-to-splitting-user-stories/
  title: The Humanizing Work Guide to Splitting User Stories
  site: humanizingwork.com
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/agile/five-simple-but-powerful-ways-to-split-user-stories
  title: 'SPIDR: Five Simple but Powerful Ways to Split User Stories - Mountain Goat Software'
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://xp123.com/twenty-ways-to-split-stories/
  title: Twenty Ways to Split Stories - XP123
  site: xp123.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: The three steps of story splitting.
review:
  status: generated
  flags: []
---

## Explanation

Story splitting turns one big user story into several smaller ones. A user story is a short description of something a user needs (see User Story).

**A three-step process**

1. Prepare the input story. Check it against the INVEST criteria (see INVEST Criteria), but ignore its size for now.
2. Apply splitting patterns.
3. Evaluate the split.

**Common splitting patterns**

- **Workflow steps.** The biggest value often sits at the start and end of a workflow. Build the simple end-to-end case first.
- **Operations.** The word "manage" in a story is a warning sign. It usually covers several operations, such as create, read, update and delete. Each can become its own story.
- **Data variations.** Complexity can come from handling many kinds of data. Handle a simple case first and add variations later.
- **Interface variations.** Sometimes the difficulty lies in the user interface, not the function. Build a simple interface first.
- **Spike.** A spike is a research activity that helps a team learn about a backlog item. It is a last resort. Use it only when the implementation is poorly understood and other patterns fail.

**SPIDR**

Cohn's SPIDR stands for Spikes, Paths, Interfaces, Data and Rules.

- Paths: split by alternate paths through the story.
- Rules: temporarily relax business rules that the story will eventually need. This makes a large story smaller.

**Why it helps**

Splitting separates high-value parts from low-value ones. A minimal end-to-end solution is a good place to start.

**Evaluating a split**

Prefer the split that lets you drop or deprioritize a story. That removes waste.

## Example

A team has the story "As a librarian, I manage books." The word "manage" signals several operations. The team splits it into add a book, find a book, edit a book and remove a book. They build "add a book" first, as a simple case with plain data. Later stories handle special kinds of data. If the team learns that removing books is rarely needed, it drops that story.

## Trade-offs

Each pattern gives a different split, so the team must choose. The evaluation step helps: prefer the split that lets you drop or deprioritize a story. A spike adds research effort without delivering a feature, so use it only when other patterns fail. Relaxing business rules is temporary. The rules still need support in the end.
