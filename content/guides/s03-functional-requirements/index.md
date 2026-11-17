---
title: 'Step 3: Capture the key functional requirements'
id: s03-functional-requirements
review:
  status: generated
  flags:
  - unsupported:Selecting items that touch main quality needs or outside systems as the ones that matter
    most for architecture is an inference from Responsibility Allocation and the method-phase article,
    not stated directly.
  - unsupported:The statement that the result feeds arc42 section 1 as a brief functional description
    is not explicitly stated in the articles.
  - unsupported:The ClinicBook details (the extra story for health data entry, the table of reasons, the
    use case extensions) are illustrative inventions for the example.
---

## What you get from this step

You get a short list of use cases or user stories that matter most for the architecture. A [use case](concept:use-case) describes how a system responds to requests from outside actors. A [user story](concept:user-story) is a short requirement written from a stakeholder's point of view. It is a reminder to talk, not a full specification.

You do not need a complete requirements document. arc42 asks for a short requirements overview that points to existing documents ([arc42 Introduction and Goals](concept:arc42-introduction-and-goals)). This result feeds arc42 section 1.

## What you need first

- Any existing requirements material, such as a vision document, a backlog or a list of features. Refer to it instead of copying it.
- Customer or user representatives you can talk to. Close, frequent contact with them helps, see [Requirements Difficulty and Customer Engagement](concept:requirements-difficulty-and-customer-engagement).
- A rough idea of the quality requirements, such as security or availability. Quality requirements steer how responsibilities are allocated ([Responsibility Allocation](concept:responsibility-allocation)).

## If something is missing

- **No requirements document exists.** Gather requirements with more than one technique, such as interviews, observation, questionnaires or workshops. See [Requirements Trawling](concept:requirements-trawling). Expect gaps. Some requirements only appear while you build.
- **Nobody is available to answer questions.** Decide who your customer representatives are. Also decide how often you get feedback, for example in reviews. See [Requirements Difficulty and Customer Engagement](concept:requirements-difficulty-and-customer-engagement).
- **The current process is wasteful.** Fix or remove the wasteful steps before you automate them. See Process Automation Magnifies Efficiency ([Continuous Architecture Principles](concept:continuous-architecture-principles)).
- **You only have vague wishes.** Turn them into short stories first, then split them as described below.

## How to do it

1. **Collect what exists.** List the existing requirements sources. Write a brief description of the functions the system must offer. Say which tasks and user objectives they cover. See [Functional suitability](concept:functional-suitability).
2. **Keep functions apart from quality requirements.** Put speed, security and similar needs in their own list. See Working with Functional Requirements (method phase) ([Requirement Types and Documents (Wiegers/Beatty)](concept:requirement-types-and-documents-wiegers-beatty)).
3. **Write each function as a story or a use case.**
   - A story names a specific user role, a goal and a reason. See User Story Role Formulation ([User Story](concept:user-story)).
   - Mark the goal level of each use case. The user-goal level is the most useful one. See Use Case Goal Level ([Use Case](concept:use-case)).
4. **Show the scope in a picture, if it helps.** A [use case diagram](concept:uml-use-case-diagram) draws a system boundary. Actors stay outside it. An actor can be a person, an organization or an external system. Avoid the mistakes in Common Use Case Diagram Errors ([UML Use Case Diagram](concept:uml-use-case-diagram)).
5. **Split items that are too big or too vague.**
   - A story too large for one iteration is an epic ([User Story](concept:user-story)). Split it before you build it.
   - Look hard at any story with the word "manage". Split it by operation. See [Story Splitting](concept:story-splitting).
   - Make the first story a simple end-to-end case. A [story map](concept:story-mapping) calls this a walking skeleton.
6. **Pick the ones that matter for the architecture.** Focus on the architecturally significant ones: those tied to business value, risk or a key stakeholder's concern ([Architecturally Significant Requirement](concept:architecturally-significant-requirement)). Quality requirements steer how responsibilities are allocated. See [Responsibility Allocation](concept:responsibility-allocation). Write the chosen items in more detail, for example with the use case template ([Use Case](concept:use-case)).
7. **Add a check for each chosen item.** Give each story acceptance criteria or examples. Keep them testable. Keep the user's goal visible next to them. See [Acceptance Criterion](concept:acceptance-criterion) and Frequent Mistakes in Defining Acceptance Criteria.
8. **Check the set.** A set of use cases should be neither too small, nor too large, nor off target. See Use Case Completeness Check ([Use Case](concept:use-case)).

## Example: ClinicBook

ClinicBook is an online appointment booking system for 40 small medical practices. Patients use the web and a mobile app. Practice staff manage calendars. The system must integrate with practice-management software from different vendors. It must send reminders by SMS and e-mail and protect health data.

**Step 3 (write stories).** The team writes first stories:

- As a patient, I want to book an appointment online, so that I do not have to call the practice.
- As a patient, I want to move or cancel an appointment, so that I can react when my plans change.
- As a patient, I want a reminder by SMS or e-mail, so that I do not miss my appointment.
- As practice staff, I want to manage the calendar, so that the schedule stays correct.

**Step 5 (split).** "Manage the calendar" is an epic. The team splits it by operation: block a time slot, open a time slot and view the day's appointments. It then checks the pieces against INVEST Criteria ([User Story](concept:user-story)).

**Step 3 (use case).** For the most important story, the team writes a use case. Its name is "Book an appointment". The goal level is user goal. The primary actor is the patient. The practice-management software and the SMS service are supporting actors. The main success scenario is a numbered list. Extensions cover cases such as "the chosen slot was taken meanwhile" and "the practice-management software does not answer".

**Step 6 (pick).** The team picks three items for detailed work. This table shows why:

| Item | Why it matters for the architecture |
|---|---|
| Book an appointment | Morning peaks put load on it. It must talk to several vendors' software. It handles health data. |
| Send a reminder | It uses two outside channels, SMS and e-mail. |
| Move or cancel an appointment | It must stay consistent with the calendar in the practice's own software. |

Calendar management for staff stays a short description for now. The team will detail it later.

**Step 5 (walking skeleton).** The first slice is one patient booking one appointment in one practice. It uses one vendor's software. Other vendors and the mobile app follow later.

**Step 7 (confirm).** One criterion for "Book an appointment": "Given a free slot, when the patient confirms the booking, then the appointment appears in the practice's calendar." A tester can check it.

**Step 8 (check).** The team checks that the set is neither too small, nor too large, nor off target. It finds no use case for the patient's health data entry, so it adds a story.

## Done when

- Each important function is written as a story or a use case, and each one has a role or actor and a goal. ([User Story](concept:user-story), [Use Case](concept:use-case))
- Each use case has a goal level. (Use Case Goal Level ([Use Case](concept:use-case)))
- Stories that were too big are split, and "manage" stories are split by operation. ([Story Splitting](concept:story-splitting))
- The items needed for architectural decisions are chosen and described in detail. Functional requirements are kept apart from quality requirements. (Working with Functional Requirements (method phase) ([Requirement Types and Documents (Wiegers/Beatty)](concept:requirement-types-and-documents-wiegers-beatty)))
- Each chosen story has acceptance criteria that a tester can check. ([Acceptance Criterion](concept:acceptance-criterion))
- The set is neither too small, nor too large, nor off target. (Use Case Completeness Check ([Use Case](concept:use-case)))

## Learn more

- [Use Case](concept:use-case)
- [UML Use Case Diagram](concept:uml-use-case-diagram)
- [User Stories vs. Use Cases](concept:user-stories-vs-use-cases)
- [User Story](concept:user-story)
- [SMART Requirements](concept:smart-requirements)
- [Story Mapping](concept:story-mapping)
- [Agile Enterprise Backlog Model](concept:agile-enterprise-backlog-model)
- [Requirement Types and Documents (Wiegers/Beatty)](concept:requirement-types-and-documents-wiegers-beatty)
- [Requirements Trawling](concept:requirements-trawling)
- [Requirements Difficulty and Customer Engagement](concept:requirements-difficulty-and-customer-engagement)
- [Process Analysis and Modeling](concept:process-analysis-and-modeling)
- [Continuous Architecture Principles](concept:continuous-architecture-principles)
- [Functional suitability](concept:functional-suitability)
- [Responsibility Allocation](concept:responsibility-allocation)
- [Acceptance Criterion](concept:acceptance-criterion)
