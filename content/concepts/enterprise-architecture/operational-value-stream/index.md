---
title: Operational Value Stream
slug: operational-value-stream
category: enterprise-architecture
kind: concept
summary: An operational value stream is a high-level, end-to-end set of stages. It starts when a stakeholder
  has a need and ends when that need is met. It shows how an organization delivers a product or service
  to a customer.
arc42:
- 1
- 3
- 12
step: s01-goals-stakeholders
related:
- business-capability
- business-capability-map
- capability-versus-process
- business-architecture
- business-architecture-artifacts
- stakeholder
- enterprise-architecture-management
checks:
- Each operational value stream names the stakeholder who triggers it and the point where that stakeholder's
  need is satisfied.
- Stage names use a verb and a noun, such as "Process Payment".
- Capabilities are mapped to the stages of each value stream.
- Value streams are kept at a high level and decompose into processes instead of replacing them.
sources:
- url: https://www.bpminstitute.org/resources/articles/capabilities-value-streams-business-architectures-essential-alliance
  title: 'Capabilities & Value Streams: Business Architecture’s Essential Alliance | BPMInstitute.org'
  site: bpminstitute.org
  accessed: '2026-11-09'
- url: https://framework.scaledagile.com/Development%20Value%20Streams
  title: Development Value Streams - Scaled Agile Framework
  site: framework.scaledagile.com
  accessed: '2026-11-09'
- url: https://www.bpminstitute.org/resources/articles/capabilities-value-streams-business-architectures-essential-alliance/
  title: 'Capabilities & Value Streams: Business Architecture’s Essential Alliance | BPMInstitute.org'
  site: bpminstitute.org
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Value_stream
  title: Value stream - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'A generic operational value stream: a trigger, ordered stages named verb-noun, and an outcome
    for the stakeholder.'
review:
  status: generated
  flags: []
---

## Explanation

A value stream is an end-to-end collection of activities that creates a result for a customer. An *operational* value stream covers the activities that deliver a product or service to that customer.

**Trigger and end point.** An internal or external stakeholder starts the stream. The stream ends when that stakeholder's need is satisfied. The triggering stakeholder usually takes part in the stream too.

**Stages.** The stream is split into stages. Each stage name uses a verb and a noun, such as "Process Payment".

**Typical examples.**

- Taking an order through to delivery.
- Admitting a patient to a hospital and treating them.
- Granting a loan.

**Link to capabilities.** A business capability is something an organization can do. Capabilities can be mapped to each stage of a value stream, and one value stream enables many capabilities. Value streams are also often cross-mapped to stakeholders and capabilities. See the articles *Business Capability* and *Business Capability Map*.

**Not a business process.** A value stream is high level. Do not confuse it with a business process. A value stream breaks down into processes. See *Capability versus process* for a related comparison.

**Operational versus development.** Development value streams are a different kind. They build and support the products and solutions that operational value streams use.

**Not lean value stream mapping.** Lean value stream mapping aims to improve the flow of materials and information. It is not well suited to broader architectural purposes. The business architecture value stream serves those broader purposes.

## Example

A small lender wants to show how it serves applicants. The trigger is a person who needs a loan. The lender names its stages with a verb and a noun: "Assess Application", "Approve Loan", "Pay Out Funds". The stream ends when the applicant has the loan. The lender then maps the capabilities that support each stage. Each stage can later be broken down into detailed processes.

## Trade-offs

A value stream stays at a high level. It shows what value is delivered and in which stages. It does not show detailed steps, so teams still need business processes for that.
