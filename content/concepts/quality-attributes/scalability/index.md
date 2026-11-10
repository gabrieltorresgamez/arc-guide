---
title: Scalability
slug: scalability
category: quality-attributes
kind: quality-attribute
summary: Scalability is how well a system copes with growing workload by adding resources. A capacity
  limit always exists, and the bottleneck, often a stateful part like a database, decides how far scaling
  can go.
arc42:
- 10
- 4
- 8
- 11
step: s04-quality-requirements
related:
- performance-efficiency
- load-balancer
- modifiability
- quality-attribute-scenario
- performance-tactics
- graceful-degradation
- iso-iec-25010-quality-model
- architectural-tactic
checks:
- The scalability requirement names its workload dimension, such as concurrent requests or data volume.
- Bottlenecks, especially stateful parts like the database, are identified before scale-out is chosen.
- Autoscaling has a maximum instance count and throttling, and dependencies are checked against it.
- Load balancing does not rely on session affinity.
- Scalability tests measure response time, throughput, and error rates at increasing load.
sources:
- url: https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/scale-partition
  title: Architecture strategies for optimizing scaling and partitioning - Microsoft Azure Well-Architected
    Framework | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/scale-out
  title: Design to scale out - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/best-practices/auto-scaling
  title: Autoscaling Guidance - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
- url: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
  title: ISO 25010
  site: iso25000.com
  accessed: '2026-11-08'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Scalability describes how a system handles more work when you give it more resources.

**Measuring it.** You can quantify scalability as the throughput gained per resource added. Throughput is the amount of work finished in a given time. The ideal is linear: double the resources, double the throughput. Bottlenecks and synchronization points typically limit the gain. You can model a system with an approach such as Amdahl's law. Scalability can be quantified by contention (delay from waiting for shared resources) and coherency (delay for data to become consistent).

**Two ways to scale.**
- Horizontal scaling (scale out and in) adds or removes instances. It suits work that splits into independent parts.
- Vertical scaling (scale up and down) changes the capacity of one resource. It often needs downtime. It suits work that is hard to divide, or architectures that cannot scale horizontally.

In the cloud, elastic scaling means you scale out as load grows and scale in when it falls. Supply then follows demand.

**Stateless versus stateful.** Stateless components spread easily across instances, because any instance can handle any request. Session affinity (stickiness) undermines this. It ties a user to one instance, so a high-volume user's traffic is not spread out. Stateful components and dependencies make horizontal scaling harder. Databases need careful design, such as data partitioning.

**Find the bottleneck first.** Adding web servers does not help if the database is the bottleneck. Stateful parts are the likeliest bottlenecks, so identify them before you scale out.

**Limits.** No resource can grow forever. To get past a resource's limit, split the workload into partitions. ISO/IEC 25010 files Capacity under Performance Efficiency: whether the maximum limits of a system parameter meet requirements. Set a maximum instance count to bound resource use, and use throttling to control demand. A configured maximum does not prove that dependencies can carry the load. When demand exceeds safe capacity, throttle incoming work or reduce nonessential functions.

**Patterns.** Azure load balancers don't require client affinity, and eliminating affinity distributes requests across instances. Message queues can absorb extra work and let consumers drain it at their own pace.

**Testing.** A scalability test defines workload dimensions and measures response time, throughput, and error rates at increasing load.

## Example

An online shop expects more visitors during a sale. The team states the dimension: concurrent shoppers. Web servers keep no session data, so a load balancer can add instances freely. Tests show the order database slows first. The team partitions its data before adding more web servers. A queue absorbs spikes of order confirmations. A maximum instance count and throttling protect the database.

## Trade-offs

Vertical scaling often needs downtime, and every resource has an upper scale limit. Horizontal scaling needs work that divides into independent parts, and stateful parts need extra design such as partitioning. Autoscaling can push load onto dependencies that cannot carry it, so it needs limits and throttling.
