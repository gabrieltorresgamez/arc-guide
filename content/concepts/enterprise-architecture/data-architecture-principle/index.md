---
title: Data Architecture Principle
slug: data-architecture-principle
category: enterprise-architecture
kind: principle
summary: 'A data architecture principle is a short, high-level rule for how an organization treats its
  data. Typical examples: data is shared, accessible, and secure, and each data element has an accountable
  trustee.'
arc42:
- 8
- 4
- 2
step: s08-integration-data
related:
- architecture-principle
- data-architecture
- arc42-crosscutting-concepts
- togaf
- structure-of-an-architecture-principle
- working-with-principles
- data-architecture-documentation-in-arc42
- accountability
checks:
- Each important data element has a named trustee accountable for its quality.
- Quality control measures exist to keep data accurate and current.
- Data administration responsibilities are clearly assigned.
- A principle states that data is protected from unauthorized use and disclosure.
- The business or domain data model is documented as a concept.
sources:
- url: https://togaf.visual-paradigm.com/2025/03/04/expanding-the-framework-additional-togaf-principles-for-effective-data-management/
  title: 'Expanding the Framework: Additional TOGAF Principles for Effective Data Management - Visual
    Paradigm'
  site: togaf.visual-paradigm.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-8/
  title: 8 - Concepts | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A data architecture principle is a basic rule for handling data. It guides design choices about data. The examples below follow TOGAF-style data principles (see the article "TOGAF").

**Typical principles**

- **Data is shared.** Data is shared across enterprise functions and organizations. The rationale: efficient sharing can improve decisions, because people rely on a single accurate source of information.
- **Data is accessible.** Users can reach the data they need to do their jobs.
- **Data has a trustee.** Each data element has a trustee who is accountable for its quality. One implication is quality control measures that keep data accurate and current.
- **Data is secure.** Data is protected from unauthorized use and disclosure.

**Implications and governance**

A principle also lists what follows from it. One implication ties to governance: functional data administration responsibilities should be clearly assigned.

**Principles in arc42**

arc42 is a documentation template. It lists principles among its cross-cutting concepts. Others include approaches, rules, tactics, and strategies (see "Crosscutting Concept"). arc42 says concepts form the basis for conceptual integrity, meaning the architecture stays consistent and homogeneous. It also advises documenting at least the business or domain data model as a concept.

For principles in general, see "Architecture Principle".

## Example

A retail company writes down three data principles. First: customer data is shared across sales and support. Second: each data element, such as the customer address, has a named trustee who answers for its quality. Third: customer data is protected from unauthorized use and disclosure. Each principle gets a short statement, a reason, and a list of consequences. One consequence is that someone must be assigned to administer the customer data.

## Trade-offs

Sharing and accessibility make data easier to reach. Security protects data from unauthorized use, so open sharing has to be balanced with protection. Principles also create work: quality control measures must be put in place, and administration duties must be assigned.
