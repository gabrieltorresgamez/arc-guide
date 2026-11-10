---
title: Microkernel Pattern
slug: microkernel-pattern
category: styles-patterns
kind: pattern
summary: A microkernel keeps only the most basic mechanisms in a small core. Everything else runs outside
  it as ordinary programs. This can help stability, but it costs performance.
arc42:
- 4
- 5
- 9
step: s07-solution-strategy
related:
- layered-architecture
- architectural-pattern
- microservices-architecture
- modifiability
- performance-efficiency
checks:
- The document states which basic mechanisms the core provides and which services run outside it.
- The document accounts for the performance cost of message exchange between clients and service providers.
sources:
- url: https://en.wikipedia.org/wiki/Microkernel
  title: Microkernel - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: Services run outside a small core and communicate by messages.
review:
  status: generated
  flags:
  - weak-sources
  - single-domain
---

## Explanation

A microkernel is a very small core of software. It offers only the basic mechanisms that an operating system needs. Examples are address spaces, threads, and message passing. The rest of the operating system is built on top of these mechanisms.

Services such as device drivers do not live inside the core. They run outside it as ordinary programs. A driver is the software that lets the system talk to a piece of hardware.

This split helps when a driver has bugs. A faulty driver sits outside the core, so the system as a whole stays more stable. The benefit applies mainly to accidental bugs, since running a driver in user space does not necessarily reduce the damage a misbehaving driver can cause.

When a program needs a service, it cannot just make one call into the core. It exchanges messages with a server that provides the service. That is the price of the small core.

## Example

Imagine a small system core that only schedules work and passes messages. A printer driver runs next to it as a normal program. An application asks the printer driver for help by sending it a message. If the printer driver has a bug, the fault stays outside the core.

## Trade-offs

**Performance.** On most mainstream processors, getting a service costs more than in a design where services sit inside one big kernel. Each request needs a message exchange with a server instead of a single system call.

**Stability versus security.** Running drivers outside the core helps against buggy drivers. It does not necessarily reduce the damage a misbehaving driver can cause, though IOMMUs can allow user-mode drivers to be untrusted.
