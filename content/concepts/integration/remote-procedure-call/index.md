---
title: Remote Procedure Call
slug: remote-procedure-call
category: integration
kind: style
summary: 'Remote Procedure Call lets one application run a procedure in another application across a network.
  It looks like a local call but behaves differently: it is slower, can fail, and needs careful interface
  design.'
arc42:
- 3
- 5
- 6
- 8
- 9
- 11
step: s08-integration-data
related:
- integration-pattern
- synchronous-vs-asynchronous-communication
- messaging
- file-transfer
- shared-database
- request-reply
- refactoring
- information-hiding
checks:
- The document states how callers handle remote call failures caused by network problems.
- Remote interfaces are coarse-grained rather than a direct copy of in-process method calls.
- Each application's data is reachable only through its exposed procedures.
- The document records that callers block while waiting for the server.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html
  title: Introduction to Integration Styles - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Remote_procedure_call
  title: Remote procedure call - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/EncapsulatedSynchronousIntegration.html
  title: Remote Procedure Invocation - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://martinfowler.com/articles/microservices.html
  title: Microservices
  site: martinfowler.com
  accessed: '2026-11-09'
- url: https://grpc.io/docs/what-is-grpc/introduction/
  title: Introduction to gRPC | gRPC
  site: grpc.io
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: 'A blocking remote procedure call: the caller waits until the server returns.'
review:
  status: generated
  flags: []
---

## Explanation

Remote Procedure Call (RPC) is an integration style. Each application makes some of its procedures available so that other applications can start them over the network. The Enterprise Integration Patterns site calls this style Remote Procedure Invocation. The article Integration Styles compares it with other styles.

**Data stays behind an interface.** Each application is built as a component. Its data sits behind an interface, and other applications reach it only through the procedures on offer. This lets the owning application protect the integrity of its data.

**The call blocks.** By default, the caller waits until the server finishes its work. Only then does the caller continue. The article Synchronous vs. Asynchronous Communication covers this in more depth.

**A remote call is not a local call.** Many RPC tools make a remote call look like a local one. That is deceptive. The two work quite differently, and the difference affects how well the integration works. Remote calls are usually much slower than local calls. They are also less reliable, and network problems can make them fail.

**Granularity matters.** If you simply turn in-process method calls into remote calls, you get chatty communication: many small calls. This performs poorly. Remote interfaces therefore need to be coarser-grained, so each call does more work.

**Change is harder across a boundary.** Refactoring (see the article Refactoring) is much harder when components are remote services than when they are in-process libraries. This makes it harder to evolve interfaces over time.

**Implementations.** CORBA provides RPC through an intermediate layer called the object request broker. Java RMI is another implementation. SOAP succeeds XML-RPC and encodes its HTTP-based calls in XML. gRPC is a modern framework: you define a service and its methods, and clients call them remotely as if they were local.

## Example

An order application needs a customer's credit status. The credit application exposes a procedure called "check credit". The order application calls it and waits for the answer before it accepts the order. If the network is down, the call fails and the order application must decide what to do. If the order application instead made separate calls for the customer's name, limit, and balance, it would be chatty. A single "get credit summary" call would suit a remote interface better.

## Trade-offs

RPC keeps each application's data behind an interface, which protects data integrity. The cost is that remote calls are slower and less reliable than local ones, and they can fail because of the network. The call-like look hides these differences. Interfaces must be coarser-grained to avoid chatty traffic. Changing interfaces later is harder across remote boundaries than inside one program.
