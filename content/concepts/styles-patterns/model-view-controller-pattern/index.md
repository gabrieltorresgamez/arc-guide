---
title: Model-View-Controller Pattern
slug: model-view-controller-pattern
category: styles-patterns
kind: pattern
summary: MVC splits an interactive application into a model (the domain), views (output) and controllers
  (input). Keeping presentation apart from the domain lets several views show the same data.
arc42:
- 4
- 5
- 8
step: s07-solution-strategy
related:
- separation-of-concerns
- model-vs-view
- layered-architecture
- architectural-pattern
- publish-subscribe-pattern
- modifiability
- coupling-and-cohesion
- domain-layer
checks:
- The document keeps presentation (views and controllers) separate from the domain model.
- Controllers and views have distinct, independent input and output responsibilities.
- The model does not depend on its views, and views observe the model so several screens can show the
  same objects.
sources:
- url: https://martinfowler.com/eaaDev/uiArchs.html
  title: GUI Architectures
  site: martinfowler.com
  accessed: '2026-11-08'
- url: https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller
  title: Model–view–controller - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
- url: https://zenodo.org/records/3676092
  title: Models–Views–Controllers | Zenodo
  site: zenodo.org
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: 'Generic MVC interaction: the controller handles input, the model notifies its views, and several
    views can show the same model.'
review:
  status: generated
  flags: []
---

## Explanation

Model-View-Controller (MVC) is a way to organize an application that has a user interface. A 1979 technical note from Xerox PARC first defined model, view and controller for UI design. MVC was one of the first serious attempts at large-scale UI work. It is best seen as a set of principles, not a fixed recipe.

**The core idea.** Make a strong separation between presentation and domain. The domain holds the business data and rules. The presentation is what the user sees and uses. MVC calls the domain part the *model*. It splits the presentation into the *view* and the *controller*.

**Who does what.**
- The model holds the domain data and logic.
- The view produces output for the user.
- The controller handles the user's input.

Controllers and views have independent input and output responsibilities. This is one way of separating concerns. See Separation of Concerns.

**How the parts stay in sync.** Views and controllers observe the model. When the model changes, the views update. This approach is called Observer Synchronization. The model is ignorant of the UI, and a controller does not need to know which other widgets must change. This helps when several screens show the same model objects.

**Variants.**
- Model-View-Presenter (MVP) first appeared at IBM, and more visibly at Taligent, in the 1990s. MVP variants differ in how they update the view, from using Observer Synchronization to having the presenter do all the updates.
- Presentation Model is a model designed for the presentation layer. It is also known as Model-View-ViewModel.
- Web MVC frameworks later let MVC components run partly on the client. They synchronize data via Ajax.

## Example

A shop application shows an order on two screens. One lists the order lines. The other shows the total. Both are views of the same order model. A user edits a quantity on one screen. The controller passes that input to the model. The model changes and notifies its observers. Both views then refresh. The model never needed to know that two screens existed.

## Trade-offs

MVC is a set of principles, so teams must decide how to apply them. Several variants exist, such as MVP and Presentation Model, and choosing among them is a design decision. Views that observe a model also add a notification mechanism that the team has to understand.
