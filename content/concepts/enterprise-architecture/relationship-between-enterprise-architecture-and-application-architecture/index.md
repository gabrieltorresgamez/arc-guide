---
title: Relationship between Enterprise Architecture and Application Architecture
slug: relationship-between-enterprise-architecture-and-application-architecture
category: enterprise-architecture
kind: concept
summary: 'Enterprise architecture sets organization-wide constraints that limit application architects''
  choices. Influence also runs back: application decisions affect enterprise architecture. Concerns spanning
  several applications need a clear split of responsibility.'
arc42:
- 2
- 4
- 9
step: s05-constraints
related:
- enterprise-architecture-management
- application-architecture
- arc42-constraints
- requirements-versus-constraints
- architecture-principle
- togaf
- architecture-levels
- arc42-architecture-decisions
checks:
- Constraints that originate in enterprise-wide standards, such as mandated technologies, are listed as
  constraints.
- For each organizational constraint, the document states whether it is fixed or negotiable.
- Responsibility for concerns that affect several applications is assigned between EA and the application.
- The document records how compliance with EA specifications is monitored or assessed.
sources:
- url: https://docs.arc42.org/section-2/
  title: 2 - Constraints | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://public.isaqb.org/curriculum-eam/curriculum-eam-en.html
  title: 'Curriculum forCertified Professional forSoftware Architecture (CPSA)®Advanced Level: ModuleEAMEnterprise
    Architecture Management for Software Architects'
  site: public.isaqb.org
  accessed: '2026-11-09'
- url: https://canvas.arc42.org/architecture-inception-canvas
  title: Architecture Inception Canvas - Software Architecture Canvas
  site: canvas.arc42.org
  accessed: '2026-11-09'
- url: https://public.isaqb.org/curriculum-foundation/curriculum-foundation-en.html
  title: 'Curriculum forCertified Professional forSoftware Architecture (CPSA)®: Foundation Level'
  site: public.isaqb.org
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Influence flows in both directions between enterprise and application architecture.
review:
  status: generated
  flags: []
---

## Explanation

Enterprise architecture (EA) looks at the structure of many applications across an organization. The iSAQB Foundation curriculum treats the structure of application landscapes as a related domain outside its own focus on individual systems.

**From EA to the application**

arc42 defines a constraint as a requirement that limits architects' freedom in design and implementation decisions. Some constraints go beyond one system and apply to a whole organization. Teams must always deal with them, although constraints may be negotiable. See the articles on arc42 Constraints and Architectural Constraint.

Technology standards are a common case. In larger enterprises, an architecture committee often sets standards for technology choices. These become technical constraints for the team. A mandated framework for single-page web applications is one example.

Architects must recognize and account for influences from EA specifications, such as EA principles.

**From the application back to EA**

Influence runs both ways. iSAQB teaches that software architecture decisions, and changes to applications, influence the enterprise architecture and the business and IT strategy.

**Governance**

The iSAQB EAM module also covers governance and compliance. It includes methods to monitor and assess whether architectures comply, for example according to TOGAF.

**Sharing responsibility**

Some concerns affect several applications, such as aspects that cut across systems. The iSAQB EAM curriculum expects architects to decide how responsibility for these is divided between EA and the individual applications.

**Freedom of the team**

The arc42 canvas notes that organizational and technical constraints determine how much decision freedom an engineering team has.

## Example

A company's architecture committee decides that all new web front ends use one approved framework. A product team starting a new application records this as a technical constraint. Later the team finds the framework handles offline use poorly. They report this to the committee, which can then revisit the standard.

## Trade-offs

Constraints from EA limit team freedom, as the arc42 canvas notes. Constraints may be negotiable. The iSAQB EAM curriculum expects architects to be able to decide on the division of responsibilities for cross-application concerns between EA and applications.
