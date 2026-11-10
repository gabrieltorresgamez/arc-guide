---
title: IT Component Catalogue
slug: it-component-catalogue
category: enterprise-architecture
kind: artifact
summary: An IT component catalogue lists the technology components a company uses and gives each a status.
  Linking components to applications shows which to keep, approve, or retire.
arc42:
- 2
- 7
- 11
step: s05-constraints
related:
- technology-architecture
- technical-debt
- traceability
- enterprise-architecture-management
- togaf
- arc42-constraints
- distribution-view
- application-lifecycle-diagram
checks:
- Each catalogued component shows a standardization status (standard, approval needed, or not permitted).
- Each technology has a lifecycle status such as adopt, tolerate, invest, or retire.
- Component end dates are compared with the end dates of the applications that rely on them.
- Exceptions to standards are tracked and linked to the applications that depend on them.
- Unsupported technologies have a retirement plan tied to their lifecycle status.
sources:
- url: https://documentation.alfabet.com/11-7/en/PortMan_SAG_Governance_StandardsCatalog_Analyze.html
  title: What is our standards catalog?
  site: documentation.alfabet.com
  accessed: '2026-11-09'
- url: https://www.orbussoftware.com/solutions/use-case/technology-standards-management
  title: Technology Standards Management | OrbusInfinity
  site: orbussoftware.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

An IT component catalogue is a list of technology components. Each entry gets a status that says how the organization treats that component. The labels here come from two tools, Alfabet and Orbus, and vary by tool.

**Standardization status.** In Alfabet's standards catalogue, color shows the status:

- Green: the component is standard. Teams may use it without approval.
- Yellow: teams must get approval before they use it.
- Orange: the component is not permitted.

**Lifecycle status.** Orbus applies one of four statuses to every technology: adopt, tolerate, invest, or retire. The status supports build, buy, and migration decisions.

**Links to applications.** A component is more useful in the catalogue when it links to the applications that depend on it. That link allows a lifecycle check. Compare the component's end date with the end dates of the applications that rely on it. If the component ends first, you have a conflict to resolve.

**Governance.** Standards governance means enforcing the standards. It also means tracking exceptions. Strong governance prevents non-approved technologies from entering the portfolio unchecked.

**Technical debt.** Without a retirement plan tied to lifecycle status, unsupported technologies pile up. Risk grows and portfolio costs rise. Governance that tracks legacy technology retirement plans helps reduce technical debt (see the article Technical Debt).

## Example

A company lists three database products. Product A is green and marked "adopt". Product B is yellow, so a new project needs approval to use it. Product C is orange and marked "retire".

The catalogue links Product C to a billing application that runs until 2031. Product C's vendor support ends in 2028. The end-date check shows the conflict, so the team plans a migration before 2028.

## Trade-offs

Governance aims for fewer non-approved technologies entering the portfolio unchecked and less unsupported technology piling up.
