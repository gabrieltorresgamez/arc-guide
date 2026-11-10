---
title: Technology Architecture
slug: technology-architecture
category: enterprise-architecture
kind: concept
summary: Technology architecture describes the infrastructure a system runs on and the standards for choosing
  and operating it. It covers hosting options such as on-premises, cloud and hybrid, and it feeds the
  arc42 deployment view.
arc42:
- 2
- 7
- 8
- 11
step: s05-constraints
related:
- enterprise-architecture-structure-business-and-it-architecture
- distribution-view
- arc42-constraints
- application-architecture
- it-component-catalogue
- deployment-diagram
- relationship-between-enterprise-architecture-and-application-architecture
- operational-constraint
checks:
- The deployment view shows the infrastructure elements relevant to the software.
- Every relevant environment is documented, not just production.
- Technical constraints are listed, with a note on which may be negotiable.
- Hosting choices cite workload requirements and compare total cost of ownership.
- Regulatory and sovereignty requirements appear as concrete architectural requirements, and ownership
  of hardware, platform, network and security is defined.
sources:
- url: https://docs.arc42.org/section-7/
  title: 7 - Deployment view | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-caf-platform-perspective/platform-arch.html
  title: Platform architecture - AWS Prescriptive Guidance
  site: docs.aws.amazon.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/hybrid-considerations
  title: Azure hybrid options - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-2/
  title: 2 - Constraints | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Inputs to hosting decisions and where they lead
review:
  status: generated
  flags: []
---

## Explanation

Technology architecture, as used here, deals with the infrastructure that software runs on.

**Why software teams care.** Infrastructure influences the system and some of its cross-cutting concepts (rules that apply across the whole system). Architects therefore need to know it. The arc42 deployment view records this infrastructure. From a software view, teams only need to capture the infrastructure elements that matter to them. If the system runs in several environments, document every relevant one.

**Constraints.** Technical constraints limit design freedom. A team must always deal with them, though some can be negotiated.

**Standards and guidelines.** Organizations agree on shared standards for technology. AWS guidance calls this platform architecture. It offers blueprints (ready-made patterns) and guardrails for security, networking and logging. Standards should adapt over time as goals and technology change. Standardizing patterns also improves governance and reduces administrative work as the organization grows. Exceptions should be planned and governed.

**Hosting choices.** Some workloads stay on premises, meaning on hardware the organization runs itself. Reasons include latency, processing needs or data residency (rules about where data is kept). Hybrid architecture combines cloud services with datacenters, edge locations and other clouds. Hosting should follow workload requirements, not the current location of hardware.

**Network design.** A hybrid setup needs connectivity to the internet, between cloud environments, and between the on-premises network and the cloud.

**Cost and lifecycle.** Azure guidance advises comparing total cost of ownership for each hosting option. That includes hardware lifecycle, power, cooling, datacenter space and operations, set against cloud consumption costs. Hybrid operations must also account for local hardware lifecycle and update processes.

**Regulation.** Sovereignty controls should be translated into specific architectural requirements. Running a workload locally does not satisfy sovereignty, privacy or regulatory requirements by itself.

**Ownership.** Define who owns the hardware, platform, network and security.

## Example

A small company runs an order system. Its deployment view shows a test and a production environment, each with application servers, a database and a network link to a payment provider. The team lists only the elements that affect the software. A company standard says new services use an approved container platform with set logging and network rules. The team compares the cost of keeping its own servers against cloud hosting, including power, cooling and staff time. A legal requirement says customer data must stay in one country, so the team turns that into a concrete rule for where the database may run.

## Trade-offs

Standards lower administrative effort. Exceptions need a planned, governed process. Keeping workloads on premises can meet latency or residency needs, but it brings hardware lifecycle, update and skills duties for each location. Hybrid setups add network integration work. Cost comparisons must include the full cost of ownership, not only purchase price. Local hosting alone does not guarantee compliance.
