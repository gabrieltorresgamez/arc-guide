---
title: 'Step 11: Evaluate the architecture'
id: s11-evaluate
review:
  status: generated
  flags:
  - unsupported:That arc42 section 10 holds the quality scenarios used in the evaluation (taken from the
    guide metadata, not from a linked article).
  - unsupported:The ClinicBook scenarios, numbers (3 seconds, Monday 8:00), decisions and findings are
    invented illustrations, not taken from the articles.
  - unsupported:The definition of a utility tree as a tree that breaks quality goals down into scenarios
    is a paraphrase beyond the exact article wording.
---

## What you get from this step

You get a written evaluation of your architecture. It checks the design against your quality scenarios. A quality scenario is a short, concrete description of how the system should respond to a specific event.

The evaluation records four kinds of findings. See [Analysis of Architectural Approaches](concept:analysis-of-architectural-approaches).

- **Risk:** a decision that may harm the response to a scenario. See [ATAM Risk](concept:architectural-risk).
- **Non-risk:** a decision the team analyzed and found sound for a quality goal. See [ATAM Non-Risk](concept:atam-non-risk).
- **Sensitivity point:** a property that one quality depends on strongly. See [Sensitivity Point](concept:sensitivity-point).
- **Trade-off point:** a property that affects several qualities at once, so improving one costs another. See [Trade-off Point](concept:trade-off-point).

You also get risk themes. A theme groups related risks and names the business driver they threaten. A business driver is a business goal behind the system. See [ATAM Results](concept:atam-results).

The findings go into arc42 section 11. See [Placing ATAM Evaluation in arc42](concept:placing-atam-evaluation-in-arc42). The scenarios you checked against belong in section 10.

## What you need first

- **Specific, measurable quality scenarios.** Vague requirements produce vague findings. See [Insufficient ATAM Application](concept:insufficient-atam-application).
- **Prioritized scenarios.** The stakeholder group ranks them by vote. See [Scenario Weight Assignment and Prioritization](concept:scenario-weight-assignment).
- **Business drivers, written down.** See [Business Drivers Presentation in ATAM](concept:business-drivers-presentation-in-atam).
- **Architecture documentation that is good enough to evaluate.** It should show a dynamic view, run-time interactions and how software maps to hardware. See [Architecture Presentation in ATAM](concept:architecture-presentation-in-atam).
- **Key decisions with reasons.** See [Architectural Decision Records as Evaluation Prerequisite](concept:architectural-decision-records-as-evaluation-prerequisite).
- **Good timing.** Evaluate before you spend heavily on implementation. See [ATAM Application Phases](concept:atam-application-phases).

## If something is missing

- **No ranked scenarios.** Brainstorm them with all stakeholders, then vote. Make sure each architectural driver has at least one scenario. See [Scenario Weight Assignment and Prioritization](concept:scenario-weight-assignment).
- **Thin documentation.** Write your gaps as targeted questions, for example about dependencies, the database and data volume. See [ATAM Phase 0 (Setup and Documentation Improvement)](concept:atam-phase-0).
- **No decision records.** Record the important, expensive, large-scale or risky decisions first. For each one, write the alternative you chose, the criteria, and all consequences, including the negative ones. See [Architectural Decision Records as Evaluation Prerequisite](concept:architectural-decision-records-as-evaluation-prerequisite).
- **No time or people for a full evaluation.** A full evaluation takes days and many people. Estimate the effort first. Then consider a lighter method. See [Advantages and Drawbacks of ATAM](concept:advantages-and-drawbacks-of-atam), [Lightweight ATAM](concept:lightweight-atam), [Lightweight Approach for Software Reviews (LASR)](concept:lightweight-approach-for-software-reviews-lasr) and [Risk Storming](concept:risk-storming).
- **An existing system.** Recover its real architecture before you analyze it. Do not simply trust the old documents. See [ATAM Application Phases](concept:atam-application-phases).

## How to do it

1. **Choose the form of the review.** Pick a full ATAM or a lighter variant. Estimate the duration and the number of participants. Write down which form you used. See [Advantages and Drawbacks of ATAM](concept:advantages-and-drawbacks-of-atam) and [Lightweight ATAM](concept:lightweight-atam).
2. **Pick the people.** A full ATAM uses an external evaluation team of about three to five people. It also uses decision-makers who can mandate changes, and broader stakeholders who join in the second phase. See [ATAM Roles](concept:atam-roles) and [ATAM Evaluation Team and Stakeholder Selection](concept:atam-evaluation-team-and-stakeholder-selection).
3. **Prepare the documentation.** Close the gaps from your questions. Give the architect a presentation template well ahead of time. See [ATAM Phase 0 (Setup and Documentation Improvement)](concept:atam-phase-0) and [Steering Stakeholder Communication in ATAM Evaluation](concept:steering-stakeholder-communication-in-atam-evaluation).
4. **Explain the method.** The evaluation leader describes it to all participants at the start. Plan for about three to four days in total. See [ATAM Phase 1: Architecture-centric Analysis](concept:atam-phase-1-architecture-centric-analysis).
5. **Present the business drivers.** The project manager or the customer presents them. The architect then presents the architecture and shows how it addresses those drivers. See [Business Drivers Presentation in ATAM](concept:business-drivers-presentation-in-atam).
6. **List the architectural approaches.** Only list them here. Add no findings yet. See [Architectural Approach Identification](concept:architectural-approach-identification).
7. **Build the utility tree.** It breaks the quality goals down until it reaches scenarios. Each scenario has a stimulus, a response and a priority. See [ATAM Phase 1 and 2 Activities](concept:atam-phase-1-and-2-activities).
8. **Analyze the approaches against the top scenarios.** For each scenario, ask how the decisions handle it. Record each finding with the decision and the scenario it concerns. See [Analysis of Architectural Approaches](concept:analysis-of-architectural-approaches). A tactics questionnaire can add questions, but use it together with scenarios. See [Tactics-based Questionnaire](concept:tactics-based-questionnaire).
9. **Repeat with the wider stakeholder group.** Brainstorm more scenarios and vote on them. Use the top-ranked ones as test cases for your earlier analysis. See [Analysis of Architectural Approaches](concept:analysis-of-architectural-approaches).
10. **Group and rank the risks.** Order risks by priority and suggest a mitigation for each. Group them into themes. Name the business driver each theme threatens. Keep the non-risks in the report. See [ATAM Findings: Risks, Non-Risks, Sensitivity Points and Trade-off Points](concept:atam-findings-risks-non-risks-sensitivity-points-and-trade-offs).
11. **Write up the results.** Deliver an out-brief, a written report, or both. Put the findings into section 11. Record each trade-off decision with its reasons in section 9. Track accepted trade-off consequences in the prioritized risk list. State where technical debt is recorded if section 11 no longer holds it. See [Placing ATAM Evaluation in arc42](concept:placing-atam-evaluation-in-arc42) and [Trade-off Point](concept:trade-off-point).

## Example: ClinicBook

ClinicBook has a small team and a fixed launch date. The team cannot afford a full evaluation. It runs a lightweight ATAM and writes that down. It also notes that a lightweight review may miss some risks. See [Lightweight ATAM](concept:lightweight-atam).

The conflicting forces are privacy and security, and availability during morning peaks. That conflict is a good reason for an evaluation. See [ATAM Application Phases](concept:atam-application-phases).

**Business drivers.** The project manager presents them: patients can book reliably in the morning, health data stays protected, and the launch date holds.

**Top scenarios** (example values for illustration):

- *Peak availability:* On a Monday at 8:00, patients book appointments at peak load. Bookings succeed within 3 seconds.
- *Integration:* A practice's management software is unreachable. Patients can still book, and the practice sees the booking later.
- *Privacy:* A staff member of practice A tries to open a patient record from practice B. The system refuses and logs the attempt.

**Decisions under review** (from the architect's presentation):

- Booking calls the practice's own software directly.
- Reminders go through a queue.
- ClinicBook keeps a copy of each practice's calendar.

**Findings:**

- **Risk.** Booking calls the practice software directly and waits for the answer. Some vendors' systems are slow in the morning. Scenario: the integration scenario. Consequence: bookings fail at peak. Suggested mitigation: save the booking in ClinicBook first and pass it on afterward.
- **Non-risk.** ClinicBook stores the booking before it queues the reminder. Scenario: peak availability. Reason: an SMS or e-mail outage cannot block a booking.
- **Sensitivity point.** The timeout for calls to the practice software. A small change strongly affects the response time at peak.
- **Trade-off point.** How often the calendar copy refreshes. Frequent refreshes keep slots accurate but add load at peak. Rare refreshes ease load but risk double bookings. The team records its choice and reasons in section 9.

**Risk theme.** "Dependence on practice software" threatens the driver "reliable booking in the morning" and, through extra work, the launch date.

The team puts these findings into section 11, ordered by priority. It then notes where technical debt is listed.

## Done when

- You evaluated the architecture early, before major implementation spending, and recorded which form of review you used. See [ATAM Application Phases](concept:atam-application-phases) and [Lightweight ATAM](concept:lightweight-atam).
- The scenarios behind the evaluation are specific and ranked by the stakeholder group. See [Scenario Weight Assignment and Prioritization](concept:scenario-weight-assignment).
- Each risk names a decision and a scenario, and has a suggested mitigation. See [ATAM Risk](concept:architectural-risk).
- Each non-risk names a scenario, a decision and a justification. See [ATAM Non-Risk](concept:atam-non-risk).
- Sensitivity points and trade-off points are listed and name the qualities they affect. See [Sensitivity Point](concept:sensitivity-point) and [Trade-off Point](concept:trade-off-point).
- Risks are grouped into themes, and each theme names a business driver. See [ATAM Results](concept:atam-results).
- The results sit in section 11, and you stated where technical debt is recorded. See [Placing ATAM Evaluation in arc42](concept:placing-atam-evaluation-in-arc42).

## Learn more

- [Architecture Tradeoff Analysis Method (ATAM)](concept:architecture-tradeoff-analysis-method-atam)
- [Software Architecture Evaluation](concept:software-architecture-evaluation)
- [ATAM Phase 1 and 2 Activities](concept:atam-phase-1-and-2-activities)
- [Comparing Architectural Alternatives with ATAM](concept:comparing-architectural-alternatives-with-atam)
- [Fitness for Purpose](concept:fitness-for-purpose)
- [Technical Debt](concept:technical-debt)
- [Risk Storming](concept:risk-storming)
- [Lightweight Approach for Software Reviews (LASR)](concept:lightweight-approach-for-software-reviews-lasr)
- [Software Architecture Analysis Method (SAAM)](concept:software-architecture-analysis-method-saam)
- [Active Reviews for Intermediate Designs (ARID)](concept:active-reviews-for-intermediate-designs-arid)
- [Scenario-based Questions from Tactics](concept:scenario-based-questions-from-tactics)
- [Battlefield Control System ATAM Case Study](concept:battlefield-control-system-atam-case-study)
