---
title: Software Architecture Analysis Method (SAAM)
slug: software-architecture-analysis-method-saam
category: evaluation
kind: method
summary: SAAM is the first documented method for analyzing a software architecture. It uses scenarios
  to test how well a design handles change, and it came before ATAM.
arc42:
- 10
- 11
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- software-architecture-evaluation
- modifiability
- modifiability-scenario
- quality-attribute-scenario
- scenario-weight-assignment
- advantages-and-drawbacks-of-atam
- quality-attribute
checks:
- The architecture document lists the change scenarios used to evaluate the design.
- Scenarios are prioritized, for example by likelihood and criticality.
- The document notes that the assessment depends on the evaluators' experience and possible bias.
sources:
- url: https://en.wikipedia.org/wiki/Software_Architecture_Analysis_Method
  title: Software architecture analysis method - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://cio-wiki.org/wiki/Software_Architecture_Analysis_Method_(SAAM)
  title: Software Architecture Analysis Method (SAAM) - CIO Wiki
  site: cio-wiki.org
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/library/scenario-based-analysis-of-software-architecture/
  title: Scenario-Based Analysis of Software Architecture | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

SAAM stands for Software Architecture Analysis Method. It was the first documented method for analyzing software architecture. It was developed in the mid-1990s. Its goal was to analyze modifiability, meaning how easily a system can be changed (see the article Modifiability).

The method works with scenarios. The scenarios represent possible changes or enhancements that might be needed in the future. SAAM uses scenarios to check how well an architecture supports change and modification. The original paper presents a structured, scenario-based method for analyzing architectures against quality attributes (see Quality Attribute).

Scenarios are prioritized. One secondary source says this is done by likelihood and criticality: how probable a change is and how much it matters. This focuses the analysis on the most significant scenarios.

SAAM is described as a precursor to the Architecture Tradeoff Analysis Method (ATAM). So ATAM can be seen as the later method, and SAAM as its earlier ancestor.

One benefit is insight into how architectural choices affect the system's ability to change.

## Example

A team runs a web shop. They list likely changes: add a new payment provider, change the tax rules, and support a second language. They rank these by how likely and how important each one is. Then they walk through the architecture and ask how well it handles each change. The result shows which design choices make change easy and which make it hard.

## Trade-offs

- Results can be subjective. They depend on the experience and bias of the evaluators.
- Building a comprehensive scenario set and evaluating it takes time and resources.
- The gain is a clearer view of how design choices affect the ability to change.
