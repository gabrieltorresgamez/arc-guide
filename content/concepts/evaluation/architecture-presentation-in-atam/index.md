---
title: Architecture Presentation in ATAM
slug: architecture-presentation-in-atam
category: evaluation
kind: practice
summary: In an ATAM evaluation, the architect presents the architecture to the evaluation team as step
  3 of nine. The detail shown limits how deep and how good the later risk analysis can be.
arc42:
- 5
- 6
- 7
- 11
step: s11-evaluate
related:
- architecture-tradeoff-analysis-method-atam
- business-drivers-presentation-in-atam
- battlefield-control-system-atam-case-study
- atam-phase-0
- analysis-of-architectural-approaches
- utility-tree
- atam-phase-1-and-2-activities
- software-architecture-evaluation
checks:
- The architecture presentation states technical constraints, interacting systems, and the approaches
  used for quality attributes.
- The presentation explains how the architecture addresses the business drivers.
- Documentation includes a dynamic view, run-time interaction charts, and a view allocating software to
  hardware.
- Client loading, process priorities, and process-to-hardware allocation can be answered from the documentation.
- The architect received a presentation template well before the evaluation.
sources:
- url: https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method
  title: Architecture tradeoff analysis method - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/documents/629/2000_005_001_13706.pdf
  title: 'ATAM: Method for Architecture Evaluation'
  site: sei.cmu.edu
  accessed: '2026-11-10'
- url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  title: Architecture Tradeoff Analysis Method® Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Presenting the architecture is step 3 of the nine ATAM steps.
review:
  status: generated
  flags: []
---

## Explanation

ATAM is a nine-step method for evaluating an architecture. It exposes risks that could keep an organization from reaching its business goals. See Architecture Tradeoff Analysis Method (ATAM) for the full method.

**Where it sits.** Presenting the architecture is step 3. It follows two steps: presenting ATAM itself, then presenting the business drivers (see Business Drivers Presentation in ATAM). Later steps build on it. They include building a utility tree, analyzing architectural approaches, and prioritizing scenarios.

**What the architect does.** The architect describes the proposed architecture to the evaluation team. The architect pitches it at an appropriate level of detail. The focus is on how the architecture addresses the business drivers.

**Why depth matters.** The analysis ATAM produces matches the level of detail of the architectural specification.

## Example

An architect prepares a presentation for a hypothetical order system. Using the template, the architect lists the prescribed database, the payment service the system must talk to, and the approaches chosen for fast response. The architect then shows a runtime interaction chart and a diagram that places each piece of software on a server. An evaluator asks how many clients use the system at once and which processes get priority. The architect cannot answer. The team notes that performance analysis must wait until this is documented.

## Trade-offs

A thin presentation limits the analysis. Performance questions cover how heavily clients load the system, how priorities are given to processes, and how processes map to hardware.
