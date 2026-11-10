---
title: SMART Requirements
slug: smart-requirements
category: functional-requirements
kind: principle
summary: SMART is a checklist for judging a requirement. It asks whether the requirement is specific,
  measurable, attainable, realistic and traceable, so teams can verify it, build it and follow it through
  their work.
arc42:
- 1
- 10
step: s03-functional-requirements
related:
- traceability
- acceptance-criteria
- invest-criteria
- user-story
- use-case
- arc42-quality-chapter
- method-phase-working-with-functional-requirements
- architecturally-significant-requirement
checks:
- Each requirement is worded without ambiguity, with consistent terminology and an appropriate level of
  detail.
- For each requirement, the document names the tests or criteria that show it has been met.
- Each requirement has been judged technically feasible, and also realistic given staff, skills, infrastructure
  and time.
- Each requirement is linked from its origin through specification, design, implementation and test.
sources:
- url: https://docs.oracle.com/cd/E13214_01/wli/docs102/bestpract/requirementsappendix.html
  title: 'Appendix: Analyzing Use Cases and Requirements'
  site: docs.oracle.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/SMART_criteria
  title: SMART criteria - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

SMART is a set of questions you ask about each requirement. The letters below follow Oracle's checklist.

**Specific.** Is the requirement unambiguous? Does it use consistent terms? Is it simple and written at the right level of detail?

**Measurable.** Can you verify that the requirement has been met? Ask which tests to run, or which criteria must be satisfied. If nobody can say how to check it, it is not measurable. The article on Acceptance Criterion covers one way to write such checks.

**Attainable.** This is a professional judgment of technical feasibility. Can it be done technically at all?

**Realistic.** In Oracle's checklist, the fourth letter is Realistic. The question is feasibility under your real limits. Do you have enough staff, skills, development infrastructure, runtime infrastructure and time? A requirement can be technically possible and still unrealistic for your team.

**Traceable.** Is the requirement linked from its conception through its specification, design, implementation and test? See the article on Traceability.

**Where the acronym comes from.** George T. Doran proposed SMART in 1981 in Management Review. The paper's title shows it was written for management goals and objectives.

**Variants.** Sources differ on some letters. This article only covers Oracle's version: Specific, Measurable, Attainable, Realistic, Traceable.

## Example

A team writes: "The search must be fast."

- Specific? No. "Fast" is vague.
- Measurable? No. No test can decide it.

They rewrite it with a concrete behavior and a test that can pass or fail. Then they ask the remaining questions. Can it be done technically? Do they have the people, skills, infrastructure and time? Finally, they link the requirement to its design, code and tests so it stays traceable.

## Trade-offs

The checklist cannot answer the questions for you. Attainable is a professional judgment, so two people may disagree. Realistic depends on your staff, skills, infrastructure and time, so the same requirement can pass for one team and fail for another.
