---
title: 'Step 4: Make quality requirements concrete'
id: s04-quality-requirements
review:
  status: generated
  flags:
  - unsupported:All ClinicBook numbers (500 requests per minute, 3 seconds, 60 seconds, 10 person-days,
    99%) are invented illustration values, not taken from the articles.
---

## What you get from this step

You end this step with three things:

- A short, ranked list of your top quality goals. These are the qualities that matter most, such as security or speed. Pick three, and no more than five. See [Quality Attribute Prioritization](concept:quality-attribute-prioritization).
- One measurable scenario for each goal. A scenario is a short, concrete story of something that happens to the system and how the system should react. See [Quality Attribute Scenario](concept:quality-attribute-scenario).
- A quality tree. It gives the overview and shows where scenarios are missing. See [Utility Tree](concept:utility-tree).

In arc42, the top goals go into section 1.2. The scenarios and the tree go into chapter 10. Chapter 10 only references the top goals, because section 1.2 already describes them. See [arc42 Quality Requirements Chapter](concept:arc42-quality-chapter).

## What you need first

- A list of the main things the system must do (use cases), even a rough one.
- The key stakeholders and what each of them worries about.
- A sense of the business value and the risks. A quality goal is architecturally significant when it is hard to meet, costly to change later, or risky. See [Architecturally Significant Requirement](concept:architecturally-significant-requirement).

## If something is missing

- **No use case list yet.** Start from stakeholder concerns and the standard quality list. Most quality requirements belong to one use case, so write them down once the use case exists. See [Quality attributes in use case descriptions](concept:quality-attributes-in-use-case-descriptions).
- **Stakeholders disagree on priority.** You cannot maximize every quality at once, and improving one usually costs another. Rank the goals by stakeholder importance and make the conflicts visible. See [Quality Attribute Trade-off](concept:architectural-trade-off-thinking).
- **Nobody knows which number to use.** Write the scenario anyway and mark the number as open. Then agree on it with the business stakeholders. See [Performance Efficiency](concept:performance-efficiency).
- **You are unsure which qualities exist.** Use a ready-made list as a checklist. See [Standard Quality Attribute List](concept:standard-quality-attribute-checklist).

## How to do it

1. **Collect candidate qualities.** Go through the nine characteristics of the 2023 edition of [ISO/IEC 25010 Product Quality Model](concept:iso-iec-25010-quality-model). Note that the 2023 edition calls usability "Interaction Capability". See [ISO/IEC 25010:2023 Product Quality Model Revision](concept:iso-25010-2023-revision). No list is complete. Also check a second, shorter list for topics such as deployability. See [Quality Attribute Coverage in Bass et al.](concept:quality-attribute-coverage-in-bass-et-al).
2. **Pick the top three, at most five.** Rank them in a table. Link each goal to business value, a risk, or a key stakeholder's concern. Keep the other qualities for chapter 10.
3. **Write each goal as a scenario.** Use six parts:
   - *Source:* who or what starts it.
   - *Stimulus:* the event.
   - *Artifact:* the part of the system that is hit.
   - *Environment:* the condition at that moment, such as normal operation or peak load.
   - *Response:* what the system does.
   - *Response measure:* a number or criterion that tells you if the response was good enough.

   See [Availability Scenario](concept:availability-scenario), [Security Scenario](concept:security-scenario), [Performance Efficiency Scenario](concept:performance-scenario) and [Interoperability Scenario](concept:interoperability-scenario) for the same idea per quality.
4. **Check that you can decide.** A reader must be able to say "met" or "not met". Avoid buzzwords like "fast" or "secure". Give a time period for availability percentages. See [Insufficient Quality as Driver of Change](concept:insufficient-quality-as-driver-of-change).
5. **Cover both kinds of scenario.** Usage scenarios describe the runtime reaction to a stimulus. Change scenarios describe the effect of modifying or extending the system. See [Modifiability Scenario](concept:modifiability-scenario).
6. **Add lesser scenarios, but keep the total small.** Around ten scenarios is manageable for most systems.
7. **Build the quality tree.** Put "quality" at the root. Refine it into categories and topics. Put one scenario at each leaf. Look for empty branches and either add a scenario or note why the branch is empty.
8. **Place everything in arc42.** Top goals go into section 1.2 as a table ordered by priority. Chapter 10 holds the tree and all scenarios and points back to section 1.2.

## Example: ClinicBook

ClinicBook is an online booking system for 40 small medical practices. The forces are privacy and security, availability during morning peaks, integration with legacy systems, a small team and a fixed launch date. The numbers below are invented for illustration. A real team would agree on them with its stakeholders.

**Section 1.2: top quality goals**

| Priority | Quality goal | Why it matters |
|---|---|---|
| 1 | Security (confidentiality of health data) | Patients trust practices with health data. A leak is a serious risk. |
| 2 | Reliability (availability at morning peaks) | Patients book when practices open. |
| 3 | Compatibility (interoperability with practice software) | Each practice already runs software from a different vendor. |

**Chapter 10: scenarios**

- **S1, confidentiality.**
  - Source: a staff member of practice A.
  - Stimulus: tries to open a patient record of practice B.
  - Artifact: the patient data interface.
  - Environment: normal operation.
  - Response: access is denied and the attempt goes into an audit trail.
  - Measure: 100% of such attempts are denied in the test. Each attempt appears in the audit trail within one minute.

  See [Confidentiality](concept:confidentiality).
- **A1, availability.**
  - Source: patients.
  - Stimulus: 500 booking requests arrive in one minute while one server instance fails.
  - Artifact: the booking service.
  - Environment: weekday morning peak.
  - Response: bookings continue and none is lost.
  - Measure: 95% of requests finish within 3 seconds.

  See [Availability](concept:availability).
- **I1, interoperability.**
  - Source: the ClinicBook booking service.
  - Stimulus: a patient books a slot at a practice whose software comes from vendor X. This vendor is known before runtime.
  - Artifact: the interface to the practice-management software.
  - Environment: normal operation.
  - Response: the appointment is sent in the vendor's format. If the vendor system accepts it, the patient gets a confirmation. If it rejects it, practice staff are notified and the patient sees the slot as not booked.
  - Measure: 99% of accepted appointments appear in the practice system within 60 seconds.

  See [Interoperability](concept:interoperability).
- **M1, change scenario (lesser goal).**
  - Source: a developer.
  - Stimulus: adds support for a new vendor's practice software.
  - Artifact: the integration layer.
  - Environment: development.
  - Response: the change is made without touching the booking logic.
  - Measure: at most 10 person-days of effort.

  This fits the small team. See [Modifiability](concept:modifiability).
- **U1, usability (lesser goal).**
  - Source: a first-time patient.
  - Stimulus: moves an appointment in the mobile app.
  - Artifact: the app's booking screens.
  - Environment: first use, without a tutorial.
  - Response: the move succeeds.
  - Measure: within 60 seconds.

  See [Usability Quality Attribute Scenario](concept:usability-scenario).

**Quality tree**

```
Quality
├── Security
│   └── Confidentiality ......... S1
├── Reliability
│   └── Availability ............ A1
├── Compatibility
│   └── Interoperability ........ I1
├── Maintainability
│   └── Modifiability ........... M1
├── Interaction Capability
│   └── Learnability ............ U1
└── Performance efficiency ...... (no leaf yet: A1 sets the peak response time;
                                   add a scenario if this proves too thin)
```

The tree shows one empty branch. The team writes down why it is empty.

## Done when

- You have three to five quality goals, ranked in a table in section 1.2. See [Quality Attribute Prioritization](concept:quality-attribute-prioritization).
- Each top goal links to business value, a risk, or a stakeholder concern. See [Architecturally Significant Requirement](concept:architecturally-significant-requirement).
- Each top goal has at least one scenario with source, stimulus, artifact, environment, response and response measure. See [Quality Attribute Scenario](concept:quality-attribute-scenario).
- Each response measure can be checked, so a reader can decide whether the requirement is met. See [Insufficient Quality as Driver of Change](concept:insufficient-quality-as-driver-of-change).
- The scenarios include both usage and change scenarios, and the total stays around ten. See [Standard Quality Attribute List](concept:standard-quality-attribute-checklist).
- The quality tree has "quality" at its root and a scenario at every leaf. Empty branches are filled or explained. See [Utility Tree](concept:utility-tree).
- Chapter 10 holds the tree and the scenarios and references the top goals in section 1.2. See [arc42 Quality Requirements Chapter](concept:arc42-quality-chapter).

## Learn more

- [arc42 Quality Requirements Chapter](concept:arc42-quality-chapter)
- [Quality Attribute](concept:quality-attribute)
- [Quality Attribute Scenario](concept:quality-attribute-scenario)
- [Quality Attribute Prioritization](concept:quality-attribute-prioritization)
- [Utility Tree](concept:utility-tree)
- [Architecturally Significant Requirement](concept:architecturally-significant-requirement)
- [Quality Attribute Trade-off](concept:architectural-trade-off-thinking)
- [ISO/IEC 25010 Product Quality Model](concept:iso-iec-25010-quality-model)
- [ISO/IEC 25010:2023 Product Quality Model Revision](concept:iso-25010-2023-revision)
- [Standard Quality Attribute List](concept:standard-quality-attribute-checklist)
- [Quality Attribute Coverage in Bass et al.](concept:quality-attribute-coverage-in-bass-et-al)
- [Quality attributes in use case descriptions](concept:quality-attributes-in-use-case-descriptions)
- [Availability Scenario](concept:availability-scenario)
- [Security Scenario](concept:security-scenario)
- [Interoperability Scenario](concept:interoperability-scenario)
- [Modifiability Scenario](concept:modifiability-scenario)
- [Performance Efficiency Scenario](concept:performance-scenario)
- [Usability Quality Attribute Scenario](concept:usability-scenario)
