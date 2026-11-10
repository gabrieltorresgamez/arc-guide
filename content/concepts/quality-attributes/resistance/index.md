---
title: Resistance
slug: resistance
category: quality-attributes
kind: quality-attribute
summary: Resistance is how well a system keeps operating while a malicious actor attacks it. ISO/IEC 25010
  lists it as a security sub-characteristic. It is about withstanding attacks, not only blocking them.
arc42:
- 10
- 8
- 11
step: s04-quality-requirements
related:
- security
- security-tactics
- security-scenario
- availability
- confidentiality
- authenticity
- integrity
- recoverability
checks:
- The document defines resistance as keeping operations running while under attack, separate from confidentiality
  and authenticity.
- Threat modeling identifies and prioritizes the relevant attack vectors.
- Access is authenticated, authorized, and minimized by privilege, scope, and time.
- Controls prevent attacks and code flaws from exhausting resources, so attacks like DDoS do not cause
  downtime.
- An incident response plan covers detecting, responding to, and recovering from attacks.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=5
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/blog/system-resilience-part-5-commonly-used-system-resilience-techniques/
  title: 'System Resilience Part 5: Commonly-Used System Resilience Techniques | CMU Software Engineering
    Institute'
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/well-architected/security/principles
  title: Security design principles - Microsoft Azure Well-Architected Framework | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

ISO/IEC 25010 is a standard quality model for software products. It defines resistance as a security sub-characteristic: how well a product or system sustains operations while a malicious actor attacks it.

**How it differs from its neighbors**

- Confidentiality means only authorized parties can access data. Resistance is about continuing to operate under attack.
- Authenticity means proving that an identity is the one claimed. It is not about operating under attack.
- Resilience, as the Software Engineering Institute describes it, protects critical capabilities from harm caused by adverse events in general.

**Ways to keep operating under attack**

- Stop attacks and code flaws from exhausting resources. Then a distributed denial-of-service (DDoS) attack, which floods a system with traffic, does not cause downtime.
- Combine redundancy (extra copies of components), diversification (different implementations), and voting, together with containers or virtualization, to limit the ability of a cyberattack to take out all replicates.
- Authenticate and authorize every actor. Minimize access by privilege, scope, and time. This limits exposure and reduces how far corruption can spread.
- Assume breach, a Zero Trust principle. Design compensating controls that limit damage if a primary defense fails.
- Detect attacks, respond to them, and recover. This preserves or restores security assurances during and after an attack. An incident response plan is part of readiness.

**Finding and testing the right attacks**

Threat modeling identifies and prioritizes the attack vectors that matter. Periodic penetration tests then check the defenses by simulating real-world attacks.

## Example

An online ticket shop expects traffic floods when popular events go on sale. The team lists likely attacks in a threat model. They add limits so that no single client can use up all resources. They run several copies of the checkout service. Admin tools require sign-in and grant only the access each role needs. An incident response plan says who reacts and how the shop recovers. A yearly penetration test checks that these measures hold.

## Trade-offs

Security controls should block attackers without blocking legitimate users. Setting that balance between security and availability takes care.

Security can also work against reliability. Security-focused design may add points of failure and operational complexity. Each defense for resistance therefore needs a check on what it adds to the system.
