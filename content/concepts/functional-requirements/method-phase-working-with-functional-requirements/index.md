---
title: Working with Functional Requirements (Method Phase)
slug: method-phase-working-with-functional-requirements
category: functional-requirements
kind: method
summary: Working with functional requirements means making clear what a system must do. A requirement
  is precise enough when developers have no more questions. Architects separate these from quality requirements,
  split large ones, and add detail iteratively.
arc42:
- 1
- 3
- 10
step: s03-functional-requirements
related:
- smart-requirements
- story-splitting
- story-mapping
- architecturally-significant-requirement
- goal-hierarchy-to-component-mapping
- requirements-versus-constraints
- arc42-introduction-and-goals
- user-story
checks:
- The document briefly describes the functional requirements and refers to existing requirements documents.
- Functional requirements are kept apart from quality requirements and constraints.
- Detailed requirements exist for the subset needed for architectural decisions.
- Large functional requirements are broken into parts that each still offer business value.
sources:
- url: https://public.isaqb.org/curriculum-req4arc/curriculum-req4arc-en.html
  title: Curriculum for Certified Professional for Software Architecture (CPSA)® Advanced LevelREQ4ARC
    – Requirements for Software Architects
  site: public.isaqb.org
  accessed: '2026-11-09'
- url: https://www.humanizingwork.com/the-humanizing-work-guide-to-splitting-user-stories/
  title: The Humanizing Work Guide to Splitting User Stories
  site: humanizingwork.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-1/
  title: 1 - Introduction and Goals | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: From goals to requirements that are precise enough
review:
  status: generated
  flags: []
---

## Explanation

Architects handle functional requirements in a few connected activities.

**Know what you are looking at.** Architects learn to tell functional requirements apart from quality requirements and constraints. A constraint is a requirement that limits the solution space beyond what the functional and quality requirements need. See *Architectural Constraint* and *arc42 Quality Requirements*.

**Make them precise enough, not perfect.** A functional requirement is precise enough once the development team has no more questions about its meaning.

**Split coarse requirements.** Large requirements are broken into smaller parts. Each part should still offer business value. Such a hierarchy can be drawn as a story map (see *Story Mapping*).

When you split a workflow, avoid cutting it one step at a time from beginning to end. Build the simple end-to-end case first. Then add the middle steps. See *Story Splitting*.

**Start from goals.** Visions and business goals are the highest level requirements. Impact Mapping is one named technique for breaking business goals down systematically.

**Go deep only where it matters.** Requirements are gathered iteratively and incrementally. Architects need detail only for the subset that drives architectural decisions. These are the *Architecturally Significant Requirements*. The rest can be gathered later, iteratively and incrementally, just in time for decisions.

**Use tools.** The curriculum lists several kinds of requirements tools, including cards, wikis, modeling tools and issue trackers.

**Document it.** The first arc42 section asks for a short description of the functional requirements. If requirements documents already exist, that overview should refer to them. See *arc42 Introduction and Goals*.

## Example

A team builds an online booking system. The business goal is "more customers book without calling us." The coarse requirement "customers can book an appointment" is too big. The team first builds the simplest complete path: pick a slot, confirm, receive a booking. Later they add the middle steps, such as payment or reminders. Each piece still gives customers something useful. The team stops refining a piece when developers say they have no open questions about it. Only the requirements that shape big technical choices get extra detail early.

## Trade-offs

Architects must pick carefully which requirements are significant enough to detail early. Cutting a workflow step by step is the obvious split, but the Humanizing Work guide calls it the wrong way to go.
