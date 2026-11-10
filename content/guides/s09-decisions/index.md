---
title: 'Step 9: Make and record decisions'
id: s09-decisions
review:
  status: generated
  flags:
  - unsupported:ClinicBook example options, criteria and decision details (adapters, nightly file exchange,
    vendor switch) are invented for illustration and not from the articles
  - unsupported:Claim that a log you cannot maintain helps nobody is a paraphrase of the 'small enough
    to maintain' idea, not stated verbatim
  - unsupported:Claim that practices would likely refuse the cost of switching vendors is an example assumption
---

## What you get from this step

You get a short list of the decisions that shape your system. Each one has a record that says what you decided, why, which options you rejected, and what the choice costs. This list becomes section 9 of your arc42 document. See [arc42 Architecture Decisions](concept:arc42-architecture-decisions).

An [Architectural Decision](concept:architectural-decision) is a choice of one option from several, made against stated criteria. Writing it down lets others retrace the choice later. It also helps the team avoid reopening settled questions.

## What you need first

- **Constraints and forces.** A constraint must be handled, though some can be negotiated. A force is a pressure you weigh, such as a deadline or a skill gap. See [Architectural Constraint](concept:requirements-versus-constraints) and [Architectural Force](concept:architectural-forces).
- **A short list of significant quality requirements.** These are the few requirements that are hard to meet or costly to change later. See [Architecturally Significant Requirement](concept:architecturally-significant-requirement).
- **Stakeholders and their concerns.** A concern is something a stakeholder cares about, such as security or performance. See [Stakeholder Concern](concept:stakeholder-concern).
- **Your fundamental decisions from section 4.** Section 9 points back to them instead of repeating them. See [arc42 Architecture Decisions](concept:arc42-architecture-decisions).

## If something is missing

- **No clear quality requirements yet.** Draft a rough version from the stakeholder concerns. Refine it as the architecture work shows limits and conflicts. See [Twin Peaks Model](concept:twin-peaks-model).
- **Constraints are unknown or mixed up with wishes.** List them in one place. For each, write who wants it, why, and whether it is negotiable. See [Architect Settles In Method Phase](concept:architect-settles-in-method-phase).
- **Nobody knows who decides.** Name who is responsible, accountable, consulted and informed. A role is enough. See [RACI Matrix](concept:raci-matrix).
- **You cannot decide yet.** Check whether the last responsible moment has come. That is the point where waiting would remove an important option. Write down which decisions you deferred and why. See [Last Responsible Moment](concept:last-responsible-moment) and [Solution as Moving Target](concept:solution-as-moving-target).
- **No template.** Pick one lean template before you write. [Markdown Architectural Decision Records](concept:markdown-architectural-decision-records-madr) and the one-sentence [Y-Statement](concept:y-statement) are two options.

## How to do it

1. **Pick the decisions worth recording.** Choose those that are hard or costly to change, or that carry high risk or cost. The integration style is a typical case. Skip small, local choices. See [Architecturally Significant Decision](concept:architecturally-significant-decision).
2. **Keep the list small.** A log you cannot maintain helps nobody. Tie each entry to a significant requirement, and state why you judged it significant. See [Architectural Decision Management](concept:architectural-decision-management-practices).
3. **Phrase each decision as a short question.** One question covers one concern. See [Architectural Design Issue](concept:formulation-of-decision-issues).
4. **Check that you are ready to decide.** Ask five things. Who are the stakeholders? Is there time? Are there alternatives? Are the requirements known? Is there a template? See [Architectural Decision Definition of Ready](concept:definition-of-ready-for-architectural-decisions).
5. **List criteria and real options.** Take the criteria from the context and the requirements, not from the strengths of the option you prefer. List at least two real options, not filler. See [ADR Common Mistakes and Review Checklist](concept:adr-common-mistakes-and-remediations).
6. **Decide with the right people.** Name the decision makers. Plan stakeholder involvement ahead of time. See [Architectural Decision Management Cycle](concept:architectural-decision-management-cycle).
7. **Write one record per decision.** Include the context, the criteria, the options, the outcome and the reasons. Explain why you chose the option; do not repeat the title. See [Architectural Decision Record](concept:architectural-decision-record) (ADR) and [Architecture Decision Rationale](concept:architecture-decision-rationale).
8. **List all consequences, good and bad.** Name a concrete price. "More effort later" is weak. Say where the effort goes. See [Architecture Decision Documentation and Requirements Management](concept:decision-documentation-and-requirements-management).
9. **Note follow-up decisions.** One decision often triggers others. Mark the ones with many follow-ons as early or big decisions. See [Decision Dependencies](concept:decision-dependencies).
10. **Say when you will review it.** Name the change that would make you look again. When a decision is replaced, mark the old one as superseded and point to the new one. See [Architectural Decision-Making Process](concept:architectural-decision-making-in-project-development).
11. **Check any AI-drafted text.** People must review it, verify every reference and make the final choice. See [GenAI Support for Architectural Decision Records](concept:genai-support-for-architectural-decision-records).

## Example: ClinicBook

ClinicBook is an online booking system for 40 small medical practices. Its forces are privacy and security, availability during morning peaks, legacy integration, a small team and a fixed launch date.

**Candidates.** The team lists the decisions that are costly to change:

| Question | Why it is significant |
|---|---|
| How does ClinicBook exchange appointments with the practices' software? | Integration style is hard to reverse. Practices use different vendors. |
| How does the system cope with morning peaks? | Availability is a key quality goal. See [Architectural Decisions for Availability](concept:architectural-decisions-for-availability). |
| Where and how is health data protected? | Privacy is a key concern and affects the whole system. |

The team does not record small local choices, such as the date-format library. These would bury the important decisions.

**One record.** The team writes the integration decision in a short template. The options, criteria and numbers below are invented for this example.

> **Title:** Use one adapter per vendor behind a common interface to synchronize appointments with practice software
>
> **Question:** How does ClinicBook keep its calendars in step with the practices' existing software?
>
> **Decision makers:** Architect (accountable), development team (responsible). Practice staff representatives are consulted. Practice managers are informed.
>
> **Context and drivers:**
> - Practices use different vendors. This is a constraint.
> - Patients must not book a slot that is already taken.
> - The team is small, and the launch date is fixed.
> - Health data must stay protected when it leaves ClinicBook.
>
> **Options:**
> 1. One adapter per vendor behind a common internal interface.
> 2. A nightly file exchange with each practice.
> 3. Ask all practices to switch to one vendor's software.
>
> **Outcome:** Option 1.
>
> **Why:**
> - Option 2 leaves calendars out of date for hours. That risks double bookings.
> - Option 3 is outside the project's control. Practices would likely refuse the cost of switching.
> - Option 1 keeps calendars current and keeps vendor details in one place.
>
> **Consequences:**
> - Good: Calendars stay current. A new vendor touches only one adapter.
> - Bad: The team must build and maintain several adapters before launch. This takes effort from other work.
> - Bad: Each adapter is a new place where health data crosses a boundary and must be protected.
> - Bad: A vendor interface change can break one adapter.
>
> **Follow-up decisions:** How to secure the data in transit. What happens when a practice system is down.
>
> **Review:** Revisit if the launch date is at risk or a vendor changes its interface.

**In section 9.** The architect adds this record to section 9. The two other candidates get their own records. Section 9 links to the matching entries in section 4 instead of repeating them.

## Done when

- Section 9 lists only important, expensive, large-scale or risky decisions, not every choice. See [Architecturally Significant Decision](concept:architecturally-significant-decision).
- Each record covers one decision and compares at least two real options against criteria that come from the requirements. See [Architectural Decision Record](concept:architectural-decision-record).
- Each record gives the reason for the choice and lists negative consequences too. See [Architecture Decision Rationale](concept:architecture-decision-rationale).
- Each record names its decision makers. See [RACI Matrix](concept:raci-matrix).
- Each record says when it will be reviewed, and follow-up decisions are noted. See [Decision Dependencies](concept:decision-dependencies).
- Section 9 refers to section 4 instead of repeating fundamental decisions. See [arc42 Architecture Decisions](concept:arc42-architecture-decisions).

## Learn more

- [ADR Common Mistakes and Review Checklist](concept:adr-common-mistakes-and-remediations)
- [Architectural Decision Record Example](concept:middleware-architectural-decision-example)
- [Architectural Decision Making Fallacies](concept:architectural-decision-making-fallacies)
- [Definition of Done for Architectural Decisions](concept:definition-of-done-for-architectural-decisions)
- [Architectural Decision Management Cycle](concept:architectural-decision-management-cycle)
- [Levels of Architectural Decisions](concept:levels-of-architectural-decisions)
- [Seven Types of Architectural Decisions](concept:seven-types-of-architectural-decisions)
- [Architecture as Set of Design Decisions](concept:architecture-as-set-of-design-decisions)
- [Architecture Challenges at Project Start](concept:architecture-challenges-at-project-start)
- [Conflicting Architecture Principles](concept:conflicting-architecture-principles)
