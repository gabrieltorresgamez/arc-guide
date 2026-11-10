---
title: Security Scenario
slug: security-scenario
category: quality-attributes
kind: concept
summary: A security scenario describes one concrete attack on a system and how the system should respond.
  It has six parts, and a measurable result shows whether the response is good enough.
arc42:
- 10
step: s04-quality-requirements
related:
- quality-attribute-scenario
- security
- security-tactics
- confidentiality
- integrity
- nonrepudiation
- arc42-quality-chapter
- availability-scenario
checks:
- Each security scenario names a source, stimulus, artifact, environment, response and response measure.
- Each response measure is quantitative, so a reviewer can decide whether the response is good enough.
- Security scenarios cover at least integrity, availability and non-repudiation.
- Scenarios that need traceability of attackers include recording of user and system actions.
sources:
- url: https://dmccreary.github.io/atam/chapters/06-quality-attribute-scenarios/
  title: Quality Attribute Scenarios - Architecture Tradeoff Analysis Method
  site: dmccreary.github.io
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=3197432&seqNum=6
  title: 3.6 Design Concepts to Support Security | Making Design Decisions | InformIT
  site: informit.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
- url: https://quality.arc42.org/qualities/security
  title: Security | arc42 Quality Model
  site: quality.arc42.org
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

A security scenario is a short, concrete story about a security problem. It is one kind of quality attribute scenario (see Quality Attribute Scenario). Security scenarios state how the system reacts when someone tries to breach its security properties.

**The six parts**

- **Source:** who or what starts the scenario.
- **Stimulus:** the event the source generates. In a security scenario, this is the attack attempt.
- **Artifact:** the part of the system that must respond to the stimulus.
- **Environment:** the conditions under which the scenario plays out, such as normal operation.
- **Response:** what the system does about the event.
- **Response measure:** a quantitative criterion that decides whether the response is good enough.

**What the response covers**

Security is commonly analyzed through three characteristics:

- Confidentiality: protection from unauthorized access.
- Integrity: no unauthorized manipulation of data or services.
- Availability: the system is there for legitimate use.

Non-repudiation also belongs to security. It means a sender cannot later deny sending a message. The arc42 quality model says security requires at least integrity, availability and non-repudiation.

A response can also include keeping a record of user and system actions. Such an audit record helps trace and identify attackers.

**Link to tactics**

Security tactics (see Security Tactic) fall into four groups: detect, resist, react and recover. The scenario states the outcome you need. Tactics are the design means to reach it.

**Where scenarios are used**

arc42 section 10 uses quality scenarios to make quality requirements concrete and measurable. It asks that scenarios be specific and measurable.

## Example

The arc42 quality catalog contains a pay-rate scenario:

- **Source:** a disgruntled employee working remotely.
- **Stimulus:** the employee attempts to improperly modify pay rate data during normal operation.
- **Response:** the system blocks the attempt and logs all access attempts in an audit trail. The data is restored if needed.
- **Response measure:** the data is restored within one business day.

## Trade-offs

Each scenario is only useful if its response measure is specific and measurable. A vague measure cannot show whether the response was good enough.
