---
title: Battlefield Control System ATAM Case Study
slug: battlefield-control-system-atam-case-study
category: evaluation
kind: artifact
summary: The Battlefield Control System is the first worked case study of the ATAM, an architecture evaluation
  method, in the book Evaluating Software Architectures. It shows how risks, sensitivity points and trade-off
  points are found.
arc42:
- 11
- 10
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- atam-findings-risks-non-risks-sensitivity-points-and-trade-offs
- sensitivity-point
- trade-off-point
- atam-results
- atam-application-phases
- quality-attribute
- software-architecture-evaluation
checks:
- Each risk in the evaluation is stated as an architectural decision that may lead to undesirable consequences.
- Each sensitivity point names a decision that has a marked effect on one or more quality attributes.
- Each trade-off point names the quality attributes in tension, such as reliability and performance.
sources:
- url: https://www.informit.com/store/evaluating-software-architectures-methods-and-case-9780201704822
  title: 'Evaluating Software Architectures: Methods and Case Studies | InformIT'
  site: informit.com
  accessed: '2026-11-09'
- url: https://people.ece.ubc.ca/matei/EECE417/BASS/ch11lev1sec2.html
  title: ''
  site: people.ece.ubc.ca
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

The Battlefield Control System is the first case study that applies the ATAM. It appears in chapter 4 of *Evaluating Software Architectures*. A case study shows the method on a concrete system instead of describing it in the abstract.

The method itself is covered in the article Architecture Tradeoff Analysis Method (ATAM). Three kinds of findings matter when you read a case study like this one.

**Risk.** A risk is an architectural decision that may lead to undesirable consequences in light of stated quality attribute requirements. Identified risks can form the basis for a risk mitigation plan.

**Sensitivity point.** A sensitivity point is an architectural decision with a marked effect on one or more quality attributes. A quality attribute is a property such as speed or reliability. See Sensitivity Point and Quality Attribute.

**Trade-off point.** A backup database is an example of a trade-off point. It helps reliability but keeps costing system resources, which hurts performance, so it is a trade-off point between reliability and performance. See Trade-off Point.

When you read the case study, check how each finding ties back to one specific architectural decision.

## Example

A team reviews an invented order system. It writes every order to a second database as a backup. Reviewers note that this one decision affects both reliability and performance. They record it as a trade-off point. Whether it is also a risk depends on whether its performance cost is excessive given the system's quality attribute requirements.

## Trade-offs

A single case study covers one system only. Use it to learn how findings are named and linked to decisions.
