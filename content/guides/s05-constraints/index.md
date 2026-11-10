---
title: 'Step 5: Collect constraints and forces'
id: s05-constraints
review:
  status: generated
  flags:
  - unsupported:Example constraint sources and reasons (announced launch date, practices keep current
    tools, code style rule) are invented for the fictional ClinicBook example, not from the articles.
  - unsupported:Treating the launch date as a fixed constraint while also naming it as a force in 'legacy
    integration versus the launch date' is the guide's own framing.
---

## What you get from this step

You get two lists.

The first list holds your constraints. A constraint is a requirement that limits how you may design and build the system. You must deal with it, though some constraints can be negotiated. The [arc42 Constraints](concept:arc42-constraints) chapter (section 2) keeps all of them in one place. Readers then see where the team is free and where it must comply.

The second list holds your forces. A force is a pressure that pulls a decision in different directions, such as deadlines, cost, skill or change. You do not simply obey a force. You weigh it against the others. See [Architectural Force](concept:architectural-forces).

## What you need first

- A short list of who is involved in or affected by the system, and what they expect. See [Architect Settles In Method Phase](concept:architect-settles-in-method-phase) and [Stakeholder Concern](concept:stakeholder-concern).
- The quality goals of the most important stakeholders. See [Software Architecture in Its Context](concept:software-architecture-in-its-context).
- Links to existing requirements documents. Link to them. Do not copy them.
- Any organization-wide standards, such as mandated technologies. See [Relationship between Enterprise Architecture and Application Architecture](concept:relationship-between-enterprise-architecture-and-application-architecture).

## If something is missing

- **No stakeholder list yet:** Write a first, rough list of who is involved. Early results get refined over time, as [Architect Settles In Method Phase](concept:architect-settles-in-method-phase) describes.
- **No quality goals yet:** Ask the key stakeholders what they care about most. Write down what you hear and mark it as a first version.
- **No known organization-wide standards:** Ask whether the organization keeps an [IT Component Catalogue](concept:it-component-catalogue). It shows which technologies are standard, need approval, or are not permitted. If no such list exists, record the open question.
- **You cannot tell whether a constraint is fixed:** Record it as a constraint and mark it as unclear. Then ask the person who wants it. See [Architectural Constraint](concept:requirements-versus-constraints).

## How to do it

1. **Open one place for constraints.** Use arc42 section 2. Do not scatter constraints across documents. See [arc42 Constraints](concept:arc42-constraints).
2. **Collect candidates from several sources.** Look at stakeholder wishes, organization-wide standards, the technologies the organization already approves, and hosting and infrastructure rules. Regulatory and data-location rules also count. See [Enterprise Architecture](concept:enterprise-architecture-management) and [Technology Architecture](concept:technology-architecture).
3. **Write who wants each constraint and why.** A constraint without a reason is hard to defend or to negotiate. See [Architectural Constraint](concept:requirements-versus-constraints).
4. **Mark each constraint as fixed or negotiable.** Do this for organizational constraints too. See [Requirements and Means Influence Architecture](concept:requirements-and-means-influence-architecture).
5. **Describe the consequences.** Note extra cost, extra effort or lost options that follow from the constraint.
6. **Group the list when it gets long.** Use technical, organizational/political, and conventions. Budget, time and processes are organizational. Programming style and naming rules are conventions. Keep constraints from the wider organization apart from those of this system. See [Software Architecture in Its Context](concept:software-architecture-in-its-context).
7. **List the forces separately.** Name the pressures that pull in different directions. Write each as a pair, for example "launch date versus maintainability". See [Concern](concept:concern).
8. **State where you are free.** Whatever the constraints leave open is your design space. Say so in the document.
9. **Expect to revise.** Constraints and forces change as you learn more. Early choices may need correcting, as [Architecture Challenges at Project Start](concept:architecture-challenges-at-project-start) points out. Later, name the forces that drove each important decision in its decision record. See [Architectural Decision Record](concept:architectural-decision-record).

## Example: ClinicBook

ClinicBook is an online appointment booking system for 40 small medical practices. Patients book, move and cancel appointments on the web and in a mobile app. Practice staff manage calendars. The team collected the following.

**Constraints (section 2)**

| Constraint | Group | Who wants it and why | Fixed or negotiable | Consequence |
|---|---|---|---|---|
| Launch on the agreed date | Organizational | Business owner; the date is already announced | Fixed | The scope must fit the time |
| Connect to each practice's existing practice-management software, from several vendors | Technical | Practices keep their current tools | Fixed | Several interfaces; more integration effort |
| Protect health data | Technical | Patients and practices; the data is sensitive | Fixed | Extra effort for security and for the hosting choice |
| Follow the team's agreed code style and naming rules | Conventions | Team; keeps the code readable | Negotiable | Small effort; can change if the team agrees |

The rows on the date, integration and health data are fixed. The team cannot trade them away. The style rule is negotiable, so the team marked it that way.

**Forces (weighed, not obeyed)**

- **Privacy and security versus easy booking.** Strong protection can make booking slower for patients.
- **Availability in morning peaks versus effort and cost.** Redundancy helps keep booking up when parts fail. It also adds cost and complexity. See [Architectural Decisions for Availability](concept:architectural-decisions-for-availability).
- **Legacy integration versus the launch date.** Each vendor's software adds work, and the date does not move.
- **A small team versus everything above.** Every choice costs the team time.

**Where the team is free:** how ClinicBook is built inside, as long as the four constraints hold. Later, each important choice will name the forces it balanced. The team keeps those choices in a short, selective list. See [Architecturally Significant Decision](concept:architecturally-significant-decision).

## Done when

- All constraints sit in one list, each with a reason and a named source. See [arc42 Constraints](concept:arc42-constraints).
- Each constraint is marked fixed or negotiable, and its consequences are written down. See [Architectural Constraint](concept:requirements-versus-constraints).
- Long lists are grouped, and organization-wide constraints are separate from system-specific ones. See [Software Architecture in Its Context](concept:software-architecture-in-its-context).
- Constraints from enterprise-wide standards, such as mandated technologies, are included. See [Relationship between Enterprise Architecture and Application Architecture](concept:relationship-between-enterprise-architecture-and-application-architecture).
- Forces are listed apart from constraints, and conflicting pairs are named. See [Architectural Force](concept:architectural-forces).
- The document says where the team is free and where it is bound. See [Requirements and Means Influence Architecture](concept:requirements-and-means-influence-architecture).

## Learn more

- [arc42 Constraints](concept:arc42-constraints)
- [Architectural Constraint](concept:requirements-versus-constraints)
- [Architectural Force](concept:architectural-forces)
- [Concern](concept:concern)
- [Architect Settles In Method Phase](concept:architect-settles-in-method-phase)
- [Software Architecture in Its Context](concept:software-architecture-in-its-context)
- [Requirements and Means Influence Architecture](concept:requirements-and-means-influence-architecture)
- [Relationship between Enterprise Architecture and Application Architecture](concept:relationship-between-enterprise-architecture-and-application-architecture)
- [Enterprise Architecture](concept:enterprise-architecture-management)
- [IT Component Catalogue](concept:it-component-catalogue)
- [Technology Architecture](concept:technology-architecture)
- [Architecture Challenges at Project Start](concept:architecture-challenges-at-project-start)
- [Architectural Decisions for Availability](concept:architectural-decisions-for-availability)
- [Architectural Decision Record](concept:architectural-decision-record)
