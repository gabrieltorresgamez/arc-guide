---
title: Matching Diagram Type to System Aspect
slug: matching-diagram-type-to-system-aspect
category: modeling-uml
kind: practice
summary: No single diagram shows every aspect of a system. Pick the diagram type that fits the aspect
  you want to show and the audience, then combine a few complementary diagrams.
arc42:
- 5
- 6
- 7
step: s10-document
related:
- uml-diagram-taxonomy
- structure-diagram
- behavior-diagram
- sequence-diagram
- deployment-diagram
- c4-model
- runtime-view
- distribution-view
checks:
- Static structure is shown in the building block view, separate from runtime behavior.
- Runtime scenarios are chosen for architectural relevance, and each uses a notation that fits it, such
  as a sequence diagram.
- The deployment view shows infrastructure nodes and channels, whether in a UML deployment diagram or
  another notation.
- Only diagrams that add value are included, not every possible diagram type or level.
sources:
- url: https://docs.arc42.org/section-5/
  title: 5 - Building block view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-6/
  title: 6 - Runtime view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://c4model.com/diagrams
  title: Diagrams | C4 model
  site: c4model.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-7/
  title: 7 - Deployment view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Each system aspect maps to its own view and a fitting diagram type.
review:
  status: generated
  flags: []
---

## Explanation

A system has several aspects. Its parts and their structure are one aspect. How it behaves at runtime is another. Where it runs is a third.

The arc42 template (see the article "arc42 Architecture Documentation Template") gives each aspect its own view.

- **Static structure.** The building block view shows how the system breaks down into building blocks.
- **Runtime behavior.** arc42 keeps this separate from static structure. Several notations fit: lists, activity diagrams, sequence diagrams, BPMN and state machines. You pick the one that suits the scenario. Choose scenarios by architectural relevance. A representative selection is enough. You do not need to cover everything.
- **Infrastructure.** The deployment view can use UML deployment diagrams. Other notations are also fine if they show the infrastructure nodes and the channels between them.

The C4 model's core diagrams are static structure diagrams at several levels of zoom: context, containers, components and code. The levels let you tell different stories to different audiences. It also adds supporting diagram types: landscape, dynamic and deployment. C4 also says you need not draw every level. Draw only the diagrams that add value.

Before drawing, ask two questions. What aspect do I want to show? Who will read it? Then choose the diagram type that fits both.

## Example

A team documents an online shop. For the parts of the system and how they relate, they draw a diagram of the main building blocks. For the checkout flow, they draw a sequence diagram of which part calls which, and in what order. For the servers and networks, they draw a deployment diagram. Each diagram answers one question, and none tries to answer all three.

## Trade-offs

arc42 asks for representative runtime scenarios, not all of them. C4 asks for only the diagrams that add value. Flexible notation, as in the deployment view, works only if the diagram still shows the required elements, such as nodes and channels.
