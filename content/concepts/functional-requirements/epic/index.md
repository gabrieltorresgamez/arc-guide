---
title: Epic
slug: epic
category: functional-requirements
kind: concept
summary: An epic is a large user story that is too big to finish in one iteration. It holds a place for
  a wanted feature until the team splits it into smaller stories.
arc42:
- 1
- 12
step: s03-functional-requirements
related:
- user-story
- story-splitting
- story-mapping
- invest-criteria
- agile-enterprise-backlog-model
- card-conversation-confirmation
- iterative-and-incremental-development
- method-phase-working-with-functional-requirements
checks:
- Stories too large for one iteration are labeled as epics and not scheduled for implementation as they
  are.
- Each epic is split into smaller user stories before implementation starts.
- Epics that are not yet needed stay as placeholders without detailed specification.
- Epics are not confused with themes, which are collections of stories.
sources:
- url: https://www.mountaingoatsoftware.com/agile/stories-epics-and-themes
  title: Epics, Features and User Stories - Mountain Goat Software
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://agilealliance.org/glossary/epic/
  title: What is an Epic User Story? | Agile Alliance
  site: agilealliance.org
  accessed: '2026-11-09'
- url: https://www.humanizingwork.com/the-humanizing-work-guide-to-splitting-user-stories/
  title: The Humanizing Work Guide to Splitting User Stories
  site: humanizingwork.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: An epic is split into smaller stories that fit one iteration.
review:
  status: generated
  flags: []
---

## Explanation

An epic is a large user story (see the article User Story). It is too big to fit into one sprint or iteration, which is a short, fixed work period.

**A placeholder.** An epic keeps a large, loosely defined idea in the backlog as a single item. It stands in for future discussions. Those discussions produce finer-grained backlog items. So the team defers detail until it is needed.

**Splitting.** Before implementation, the team splits the epic into a set of smaller stories. Teams often do this during backlog refinement, the regular session where the team prepares upcoming work.

**Epic and theme.** A theme is a different idea. It is a collection of user stories.

**Ways to split.** The article Story Splitting covers this in depth. Three common cuts:

- *By operation.* The word "manage" often signals several operations, such as create, edit, and delete. Each operation can become its own story.
- *By data variation.* Some complexity comes from handling different kinds of data. Each variation can become a story.
- *By workflow step.* Splitting one step at a time is the obvious cut, but it is the wrong way to go. The biggest value often comes from the beginning and the end of a workflow, though sometimes the whole workflow matters.

**Size target.** After splitting, each story should be small. One guideline says 6 to 10 stories should fit into a sprint (see INVEST Criteria).

## Example

A team lists the epic "Customers can manage their saved addresses." Nobody needs it yet, so it stays a one-line placeholder in the backlog.

Later the team needs the feature. During backlog refinement, it sees that "manage" covers several operations. It splits the epic into smaller stories: add an address, edit an address, and delete an address.

## Trade-offs

Keeping an epic as a placeholder avoids specifying a feature in detail before anyone needs it. The cost is that an epic is too big to deliver in one iteration. It cannot be built as written. The team must split it first.
