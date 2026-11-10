---
title: 'Step 2: Define scope and context'
id: s02-scope-context
review:
  status: generated
  flags:
  - unsupported:Assumes that earlier work already produced a stakeholder list, quality goals and constraints
    (the 'What you need first' list).
  - unsupported:Advice to write a best guess for unclear inside/outside items, mark it as open, and ask
    the decision makers.
  - unsupported:Advice to draft up to five quality goals and continue when none exist yet, and that the
    context may reveal at-risk goals.
  - unsupported:Step order of the numbered procedure is the guide author's own sequencing.
  - unsupported:ClinicBook example partners, the assumed external SMS and e-mail services, the data flows
    and the technical channels are invented for the fictional example.
---

## What you get from this step

You get a clear line between your system and the world around it. You also get a context diagram and a table that list every user and external system your system talks to.

The result goes into arc42 section 3, [Context and Scope](concept:arc42-context-and-scope). It has two parts:

- The **business context** shows which data your system exchanges with each partner.
- The **technical context** shows which channels and protocols carry that data.

Keep the two parts separate. See [Business and Technical Context](concept:business-and-technical-context).

## What you need first

- A short description of what the system must achieve, plus its top quality goals. See [arc42 Introduction and Goals](concept:arc42-introduction-and-goals).
- A list of stakeholders. A stakeholder is a person, team or organization with an interest in the system. See [Stakeholder Identification](concept:stakeholder-identification).
- Any known constraints, such as a fixed launch date or required integrations. See [arc42 Constraints](concept:arc42-constraints).

## If something is missing

- **No stakeholder list:** Make a quick one. Ask who gains or loses from the system, who decides, and who controls resources. Users and neighbor systems often show up this way. See [Stakeholder Identification](concept:stakeholder-identification).
- **Unsure whether something is inside or outside:** Write down your best guess, mark it as open, and ask the people who decide. Do not leave the boundary implicit. See [Architecture Disciplines](concept:architecture-disciplines).
- **No quality goals yet:** Draft up to five and keep going. The context often shows which goals are at risk. See [arc42 Introduction and Goals](concept:arc42-introduction-and-goals).

## How to do it

1. **State the scope.** Write down what is inside the system and what is outside. Make the boundary explicit. See [Architecture Disciplines](concept:architecture-disciplines).
2. **List all communication partners.** Include human users and other IT systems. Leave none out. Questions about external systems and users are answered in the context view. See [Stakeholder Questions Addressed in Views](concept:stakeholder-questions-addressed-in-views).
3. **Draw the business context.** Show your system as one black box. A black box shows no internals. Put the partners around it, outside the boundary. See [Context View](concept:context-view) and [System Context Diagram](concept:c4-level-1-system-context-diagram).
4. **Label each arrow with the data that flows.** Arrows show data flows, not dependencies. If data moves both ways, draw both directions. See [Context View Antipattern: Forgetting Bidirectional Data Flows](concept:context-view-antipattern-forgetting-bidirectional-data-flows).
5. **Group partners if there are many.** Use criteria you state openly. Keep the top diagram a simple overview. See [Refining Complex Context Views](concept:refining-complex-context-views).
6. **Write a context table.** Give each partner one row. Add the domain data exchanged. Keep each row short and describe interface details only once, elsewhere. See [arc42 Context and Scope](concept:arc42-context-and-scope) and [Undetected Duplication Antipattern](concept:undetected-duplication-antipattern).
7. **Add the technical context.** For each domain interface, name the channel or protocol that carries it. Keep this apart from the business context. See [Business and Technical Context](concept:business-and-technical-context).
8. **Mark risks.** Show risky neighbors or interfaces explicitly in the context. See [Context View](concept:context-view).
9. **Check the diagram.** Give it a title that states its type and scope. Add a legend. Use plain names and avoid unexplained acronyms. Leave out technologies and internals in the business view. See [Context View Antipatterns](concept:context-view-antipatterns) and [Architectural Overview Antipattern](concept:architectural-overview-antipatterns).
10. **If you use open data, list it as a partner.** State its license or public-domain status. State that it is machine-readable and how to obtain it. See [Use of external and open data](concept:use-of-external-and-open-data).

## Example: ClinicBook

ClinicBook books appointments for 40 small medical practices. The partners below follow from the system description. Where the description is silent, the text marks an assumption.

**Scope.**

- *Inside:* booking, moving and canceling appointments. Calendar management for practice staff. Triggering reminders.
- *Outside:* the practices' existing practice-management software. The delivery of SMS and e-mail messages (assumed to be done by external services).

**Business context.** The diagram below is a business context diagram of ClinicBook.

```
Title: Business context diagram, ClinicBook (system scope)

 Patient ---- booking, move, cancel requests ---> +-----------+
 Patient <--- slots, confirmations -------------- |           |
 Practice staff -- calendar changes ------------> | ClinicBook|
 Practice staff <- calendars, bookings ---------- |           |
 Practice-mgmt software <- appointments --------- |           |
 Practice-mgmt software -- existing calendars --> |           |
 SMS service <---- reminder text, phone number -- |           |
 E-mail service <- reminder text, address ------- +-----------+

Legend: box = system as black box; labeled arrow = data flow,
arrow head = direction of the data
```

**Context table.**

| Partner | Data exchanged | Technical channel | Note |
|---|---|---|---|
| Patient | Requests in; slots and confirmations out | Web browser and mobile app, over the internet | Health data: mark privacy as a risk |
| Practice staff | Calendar changes in; calendars and bookings out | Web browser | |
| Practice-management software (several vendors) | Appointments out; existing calendars in | Differs by vendor; to be clarified | Risk: legacy systems, no single interface |
| SMS service (assumed) | Reminder text and phone number out | To be chosen | Risk: keep health details out of messages |
| E-mail service (assumed) | Reminder text and address out | To be chosen | Same risk as SMS |

The table points to the main forces. Privacy shows up at every patient-facing and reminder interface. Integration with legacy systems is the biggest unknown, because each vendor may offer a different channel. The team can raise these early because the context makes them visible.

## Done when

- The scope states what is inside and outside the system, and the boundary is explicit. See [Architecture Disciplines](concept:architecture-disciplines).
- Every user and external system appears as a communication partner. See [arc42 Context and Scope](concept:arc42-context-and-scope).
- The business context shows the system as a black box, and each arrow carries a label naming the data. See [Context View Antipatterns](concept:context-view-antipatterns).
- Two-way exchanges show both directions. See [Context View Antipattern: Forgetting Bidirectional Data Flows](concept:context-view-antipattern-forgetting-bidirectional-data-flows).
- A table lists each partner, its data and its technical channel, and the technical context is kept separate. See [Business and Technical Context](concept:business-and-technical-context).
- Risks at interfaces are marked. See [Context View](concept:context-view).
- The diagram has a title and a legend, and readers can understand it without a long explanation. See [Architectural Overview Antipattern](concept:architectural-overview-antipatterns).

## Learn more

- [arc42 Context and Scope](concept:arc42-context-and-scope)
- [Business and Technical Context](concept:business-and-technical-context)
- [Context View](concept:context-view)
- [Context View Antipatterns](concept:context-view-antipatterns)
- [Context View Antipattern: Forgetting Bidirectional Data Flows](concept:context-view-antipattern-forgetting-bidirectional-data-flows)
- [Refining Complex Context Views](concept:refining-complex-context-views)
- [System Context Diagram](concept:c4-level-1-system-context-diagram)
- [Data architecture documentation in arc42](concept:data-architecture-documentation-in-arc42)
- [Use of external and open data](concept:use-of-external-and-open-data)
- [Stakeholder Identification](concept:stakeholder-identification)
- [Rules of Thumb for Modeling](concept:rules-of-thumb-for-modeling)
