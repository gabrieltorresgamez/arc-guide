---
title: Business Architecture
slug: business-architecture
category: enterprise-architecture
kind: concept
summary: Business architecture is a blueprint of an organization that gives everyone a common understanding
  of it. It is one of four enterprise architecture domains and centers on capabilities, value streams,
  information and organizational structure.
arc42:
- 1
- 3
- 8
step: s06-domain
related:
- business-capability
- business-capability-map
- operational-value-stream
- enterprise-architecture-structure-business-and-it-architecture
- togaf
- data-architecture
- application-architecture
- technology-architecture
checks:
- Business capabilities are described as what the business can achieve, without people, processes, data
  or technology.
- Capability maps and value stream diagrams are kept as separate artifacts.
- Business or domain models are documented in arc42 section 8.
- The context description lets all stakeholders see which data is exchanged with the system environment.
sources:
- url: https://en.wikipedia.org/wiki/Business_architecture
  title: Business architecture - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.bmc.com/resources/topics/bizbok-introduction.html
  title: Introduction to BIZBOK - BMC Software
  site: bmc.com
  accessed: '2026-11-09'
- url: https://www.grahamberrisford.com/00EAframeworks/03TOGAF/AMTOGpapers/Business%20architecture%20(inc%20capabilities%20and%20value%20streams)%20in%20TOGAF.htm
  title: ''
  site: grahamberrisford.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/8-5/
  title: 'Tip 8-5: Document business or domain models! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-3/
  title: 3 - Context and scope | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Business architecture with BIZBOK core and outer elements, next to the other three enterprise
    architecture domains.
review:
  status: generated
  flags: []
---

## Explanation

Business architecture is a blueprint of the enterprise. It gives people a shared understanding of the organization. One definition describes it as holistic, multidimensional views of capabilities, end-to-end value delivery, information and organizational structure.

**Place among the domains.** TOGAF treats it as one of four domains of enterprise architecture. The other three are application, data and technology. See the article on TOGAF for the framework.

**What it answers.** The description works like a wireframe. It ties business objectives to demand. It commonly answers who, what, where, when, why and how of daily operations.

**BIZBOK elements.** BIZBOK is a body of knowledge for business architecture. Its stakeholders derive four insights from every domain: organization, capabilities, value streams and information. Domains also represent concepts such as strategy and metrics.

**Capabilities.** A business capability states what a business can achieve, not how. It ignores people, processes, data and technology. Capability mapping is one of the BIZBOK modeling techniques and covers defining and developing capabilities. See Business Capability and Business Capability Map.

**Value streams.** A value stream covers the end-to-end activities that deliver value to external and internal stakeholders. A value stream diagram and a capability map are listed as separate artifacts.

**In arc42.** arc42 advises documenting business or domain models in section 8, because many building blocks refer to them. The context section expects all stakeholders to understand which data the system exchanges with its environment.

## Example

A parcel company describes a capability called "Deliver parcels". The name says what the company can do. It says nothing about drivers, software or routes. A separate value stream diagram then shows the end-to-end steps from a customer's order to the delivered parcel. The two artifacts show the same business from different angles.

## Trade-offs

One point to note: capability maps and value stream diagrams are listed as separate artifacts.
