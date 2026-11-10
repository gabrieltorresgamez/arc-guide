---
title: Story Mapping
slug: story-mapping
category: functional-requirements
kind: method
summary: A story map shows how users reach a goal as a picture. Activities form a backbone from left to
  right. Stories hang below, higher when more necessary. Horizontal lines slice the map into releases.
arc42:
- 1
- 3
step: s03-functional-requirements
related:
- user-story
- story-splitting
- epic
- use-case
- use-case-goal-levels
- user-story-vs-use-case
- domain-storytelling
- method-phase-working-with-functional-requirements
checks:
- The map's cards are short verb phrases, each describing one user step.
- Steps are ordered left to right, and vertical placement shows priority.
- Releases are marked as horizontal slices, starting from one objective or MVP.
- A thin end-to-end walking skeleton is identified as the first slice.
sources:
- url: https://jpattonassociates.com/the-new-backlog/
  title: The New User Story Backlog is a Map – Product thinking made fun, practical, & profitable
  site: jpattonassociates.com
  accessed: '2026-11-09'
- url: https://jpattonassociates.com/5-story-mapping-mistakes/
  title: Five common story mapping mistakes – Product thinking made fun, practical, & profitable
  site: jpattonassociates.com
  accessed: '2026-11-09'
- url: https://www.mountaingoatsoftware.com/agile/user-stories/story-mapping
  title: 'Story Mapping: How to Create Story Maps for User Stories - Mountain Goat Software'
  site: mountaingoatsoftware.com
  accessed: '2026-11-09'
- url: https://www.humanizingwork.com/alistair-cockburn-on-use-cases-user-stories/
  title: Alistair Cockburn on Use Cases & User Stories - Humanizing Work
  site: humanizingwork.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Backbone of activities left to right, with ribs below; lower ribs are less necessary.
review:
  status: generated
  flags: []
---

## Explanation

A story map organizes what users do with a system. A flat backlog (one ordered list of work) hides how items relate. A story map shows how the stories fit together. Its purpose is to tell one big story about the system.

**Building blocks**

- A *task* is something a person does to reach a goal.
- An *activity* is a bigger thing people do. Tasks are the smaller steps arranged under activities.
- In a story map, cards are often short phrases, with each card describing a step.

**Backbone and ribs**

The top-level items form the *backbone*. They hold the essential capabilities of the system, and they are not prioritized.

The *ribs* are the stories hanging below the backbone. Height signals priority. High placement means absolutely necessary. Lower placement means less necessary. You build across the backbone first, then down each rib by priority.

**Slicing releases**

The thinnest end-to-end slice is called the walking skeleton. It is built first. Once the map is full of options and details, you slice it into small, successful releases. Horizontal lines can be added to the map to mark planned releases.

**Building it together**

Teams build maps with sticky notes and paper on a wall. Remote teams use a virtual whiteboard.

**What a map is not**

A story map is not a precise tool like a flow chart. It relies on storytelling to convey the varied ways users use a product. One practitioner describes the macro process across users in kite-level use cases as being like the backbone of a story map. He also says story maps lack a discipline for finding holes. See *Use Case Goal Level*.

## Example

A team builds an online bookshop map. The backbone reads, left to right: "Find a book", "Choose a book", "Pay", "Receive order". Under "Pay", the card "Enter card details" sits high because it is necessary. "Save card for later" sits lower. The team draws a line below the top cards. Everything above it becomes the first release, a thin path from search to delivery.

## Trade-offs

A story map is imprecise by design. It is not a precise communication tool like a flow chart, and it communicates through storytelling. The backbone is left unprioritized. Priority is judged only on the ribs below it. Cockburn's view is that story maps are only halfway there on a discipline for finding holes.
