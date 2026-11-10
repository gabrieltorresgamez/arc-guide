---
title: Recoverability
slug: recoverability
category: quality-attributes
kind: quality-attribute
summary: Recoverability is how well a system gets its affected data back after an interruption or failure.
  Teams express it with recovery-time and data-loss targets, and improve it by cutting recovery time,
  for example through failover.
arc42:
- 1
- 7
- 8
- 10
step: s04-quality-requirements
related:
- reliability
- availability
- availability-tactics-fault-recovery
- quantifying-recovery-and-availability-trade-offs
- iso-iec-25010-quality-model
- redundant-spare
- fault-tolerance
- graceful-degradation
checks:
- The document states which meaning of MTTR (respond, repair or recovery) it uses.
- Recovery targets are defined per incident (RTO) and for acceptable data loss (RPO).
- Contractual commitments (SLAs) are distinguished from internal targets (SLOs).
- Failover to redundant components is described for the failures the system must recover from.
- Recovery thresholds allow for transient faults and name the automatic action they trigger.
sources:
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=1
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/well-architected/reliability/metrics
  title: Architecture strategies for defining reliability targets - Microsoft Azure Well-Architected Framework
    | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://www2.eecs.berkeley.edu/Pubs/TechRpts/2002/5574.html
  title: 'Recovery Oriented Computing (ROC): Motivation, Definition, Techniques, and Case Studies | EECS
    at UC Berkeley'
  site: www2.eecs.berkeley.edu
  accessed: '2026-11-09'
- url: https://sciencelogic.com/blog/mttr-vs-mttar-vs-mttd-incident-management-metrics
  title: Mean Time to Repair (MTTR) vs MTTA vs MTTD | ScienceLogic
  site: sciencelogic.com
  accessed: '2026-11-09'
- url: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/disaster-recovery-dr-objectives.html
  title: Disaster Recovery (DR) objectives - Reliability Pillar
  site: docs.aws.amazon.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: Phases between a failure and restored service; failover can shorten the path.
review:
  status: generated
  flags: []
---

## Explanation

Recoverability is a part of reliability in the ISO/IEC 25010 quality model (see the article ISO/IEC 25010 Product Quality Model). The standard describes it as the degree to which a product or system can recover the data directly affected when an interruption or failure happens.

**Measuring it: MTTR**

MTTR is one metric related to recovery. The abbreviation is ambiguous. It can stand for four things:

- **Mean Time to Respond:** the time from detecting a problem to the start of active response.
- **Mean Time to Repair:** the time needed to fix the affected component.
- **Mean Time to Resolve:** the time needed to fix, validate, and close the incident.
- **Mean Time to Recovery:** the time needed to restore the service to normal operation.

Teams should document which meaning they use. Azure defines MTTR as the time to restore a component after a failure is detected. It groups MTTR with RTO, RPO and MTBF as recovery targets.

**Related targets**

RTO is the maximum downtime allowed for a single incident. MTTR is an average over several incidents. RPO is the maximum acceptable time since the last data recovery point, so it limits data loss.

**Agreements**

An SLA is a formal contract. It has financial and legal consequences if the organization fails to deliver. An SLO is a different thing: it is used to evaluate whether potential downtime is within tolerable limits.

**Ways to recover faster**

- **Failover:** switch to a redundant copy of a component. With several deployment units ("stamps") in multiple regions, a failure in one can be recovered by failing over to another. In that case, the overall workload SLO is higher.
- **Automatic triggers:** set recovery thresholds that allow for short-lived (transient) faults. For example, if a web node is unavailable for more than five minutes, add a new node to the pool automatically.
- **Recovery-oriented design:** recovery-oriented computing improves availability by shortening recovery time, not by trying to prevent every failure.

## Example

An online shop runs in two regions. The database in region A fails. Monitoring detects it, and traffic fails over to region B while engineers repair region A. The team had set a maximum downtime for one incident (RTO) and a maximum age of the last data copy (RPO). It then checks the incident against both targets and adds the duration to its average recovery time.

## Trade-offs

Azure advises stakeholders that flows or workloads not thoroughly tested for recovery metrics shouldn't have guaranteed SLAs. Meeting high SLOs raises the question of how much redundancy is needed. Thresholds that react too fast may trigger recovery for faults that would have cleared by themselves, so they should allow for transient faults. See the article Quantifying Recovery and Availability Trade-offs.
