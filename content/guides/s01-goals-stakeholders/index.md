---
title: 'Step 1: Understand the goals and the stakeholders'
id: s01-goals-stakeholders
review:
  status: generated
  flags:
  - unsupported:The three questions to ask a sponsor when no business description exists are the author's
    suggestion, not from the articles.
  - unsupported:The ClinicBook vision, business goals, stakeholder list, quality scenarios and the launch-date
    trade-off are invented illustrations, not from the articles.
  - unsupported:Rating by power and interest in step 5 is applied to the stakeholder list as a suggested
    practice; the power grid article supports it, but placing it in this step is a judgment.
---

## What you get from this step

You get a short written base for all later architecture work. It holds four things:

- a vision for the system,
- the business goals behind it,
- a list of stakeholders,
- the concerns of each stakeholder.

A *stakeholder* is a person, team or organization with an interest in the system. Their interests are called *concerns*. Read [Stakeholder Perspective and Concern](concept:stakeholder-perspective-and-concern) for the details.

You write the result into section 1 of arc42, "Introduction and Goals". See [arc42 Introduction and Goals](concept:arc42-introduction-and-goals). That section stays short. It holds a requirements overview, the top quality goals and a stakeholder table.

## What you need first

- A rough idea of what the system should do and for whom.
- Any existing requirements documents. You will link to them, not copy them. See [Architect Settles In Method Phase](concept:architect-settles-in-method-phase).
- Access to the people who sponsor, build or use the system, or to someone who knows them.
- If one exists, a description of the business behind the system, such as a [Business Model Canvas](concept:business-model-canvas). It shows the customers and partners you must not forget.

## If something is missing

- **No requirements document.** Write a short overview yourself. Mark it as a first version. Early results get refined over time.
- **No business description.** Ask the sponsor three questions. Who are the customers? What value do they get? Why does the business pay for this system?
- **Unclear scope or security needs.** Write your assumptions down and challenge them. An assumption like "we only need a simple login" is risky when nobody has questioned it. See [Common Architect Mistakes](concept:common-architect-mistakes).
- **Stakeholders you cannot reach.** List them anyway. Ask someone to speak for each group, so that no class is ignored. See [Stakeholder](concept:stakeholder).

## How to do it

1. **Write a vision statement.** Keep it short. Name the target customers. Say what value they get. Name the few features that make the system stand out. Do not list every feature. See [Vision Statement](concept:vision-statement).
2. **Connect the vision to business goals.** The value in the vision should link to a business goal and to the business case. See [System Idea and Vision Elements](concept:system-idea-and-vision-elements).
3. **Find the stakeholders.** Ask guiding questions. Who gains or loses? Who decides? Who controls resources? Check every class of stakeholder, for example the people who acquire the system and the people who assess it. See [Stakeholder Identification](concept:stakeholder-identification).
4. **Record their concerns.** Build a table with the role, the name or contact, and what each stakeholder expects from the architecture and its documentation. See [Stakeholder Concern](concept:stakeholder-concern).
5. **Decide how closely to engage each group.** Rate each stakeholder by power and interest. Engage high-power, high-interest stakeholders closely. Keep high-power, low-interest stakeholders satisfied. See [Stakeholder Power Grid](concept:stakeholder-power-grid).
6. **Choose the top three to five quality goals.** Pick the ones most important to the major stakeholders. Give each goal a short scenario, not only a keyword. Leave detailed quality requirements for section 10 of arc42. See [arc42 Introduction and Goals](concept:arc42-introduction-and-goals).
7. **Name concerns that conflict.** Write down which trade-off you choose and why. Record the reasoning in an Architecture Decision Record (ADR). See [Concern](concept:concern).
8. **Keep the requirements overview short.** Link to the existing requirements documents.
9. **Review the result with the stakeholders.** Update it later when you learn more.

## Example: ClinicBook

ClinicBook is an online appointment booking system for a network of 40 small medical practices. Patients book, move and cancel appointments on the web and in a mobile app. Practice staff manage calendars. ClinicBook connects to the practices' existing practice-management software, sends reminders by SMS and e-mail, and protects health data.

**Vision statement (example).** "Patients of our 40 practices book, move and cancel appointments in a minute, on the web or on their phone. Practice staff keep full control of their calendars."

**Business goals (example).**
- Patients use the online service instead of the phone.
- The system launches on the fixed launch date.
- The practices keep their existing software.

**Stakeholders and concerns (example).** The names and contacts are placeholders. Fill in real ones.

| Role | Name / contact | Expectations |
|---|---|---|
| Patient | (representative to be named) | Booking works at any time, also on a phone. Health data stays private. |
| Practice staff | (representative to be named) | The calendar matches the practice-management software. Few double bookings. |
| Practice owner | (name to be filled in) | Fewer missed appointments. No extra work for the staff. |
| Vendor of practice-management software | (name to be filled in) | A clear, stable interface to their product. |
| Data protection officer | (name to be filled in) | The architecture shows how health data is protected. |
| Development team | (name to be filled in) | A structure the small team can build and maintain. |
| Project sponsor | (name to be filled in) | The system launches on the fixed date. |

**Top quality goals (example).** The goals come from the forces of the system. Each has a short scenario.

| Goal | Scenario |
|---|---|
| Privacy and security | A person without rights tries to read another patient's appointment. The system refuses and logs the attempt. |
| Availability in morning peaks | Many patients book between 7:00 and 9:00. Booking still works. |
| Integrability | A practice uses a different vendor's software. ClinicBook still reads and writes its calendar. |
| Maintainability | A small team adds a new reminder channel without changing the booking logic. |

The details, such as exact numbers, move to section 10.

**Conflicts (example).** The fixed launch date conflicts with integration with many legacy systems. The team may support only some vendors at launch. It records this choice and its reasons in an ADR. The small team and the high security needs also pull against each other. The team notes the trade-off and the reasoning in the same way.

## Done when

- You wrote a short vision statement that names the target customers, their value and a few standout features. See [Vision Statement](concept:vision-statement).
- Your stakeholder table lists roles, names or contacts and expectations, and covers every stakeholder class. See [Stakeholder Identification](concept:stakeholder-identification).
- Each stakeholder concern appears in the table and is addressed in the architecture description. See [Stakeholder Concern](concept:stakeholder-concern).
- Section 1 lists at most five quality goals, each with a short scenario. See [arc42 Introduction and Goals](concept:arc42-introduction-and-goals).
- The quality goals are the ones most important to the major stakeholders. See [Stakeholder Perspective and Concern](concept:stakeholder-perspective-and-concern).
- Conflicting concerns are named, with the chosen trade-off and its reasoning. See [Concern](concept:concern).
- The requirements overview is short and links to existing documents. See [Architect Settles In Method Phase](concept:architect-settles-in-method-phase).

## Learn more

- [Stakeholder](concept:stakeholder)
- [Stakeholder Perspective and Concern](concept:stakeholder-perspective-and-concern)
- [Stakeholder Concern](concept:stakeholder-concern)
- [Stakeholder Identification](concept:stakeholder-identification)
- [Stakeholder Power Grid](concept:stakeholder-power-grid)
- [Stakeholder Readiness for Change Assessment](concept:stakeholder-readiness-for-change-assessment)
- [Concern](concept:concern)
- [Vision Statement](concept:vision-statement)
- [System Idea and Vision Elements](concept:system-idea-and-vision-elements)
- [arc42 Introduction and Goals](concept:arc42-introduction-and-goals)
- [Business Model Canvas](concept:business-model-canvas)
- [Software Architecture Basic Concepts](concept:software-architecture-basic-concepts)
- [Software Architect](concept:software-architect-role)
- [Common Architect Mistakes](concept:common-architect-mistakes)
