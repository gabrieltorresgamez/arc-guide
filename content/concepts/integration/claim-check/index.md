---
title: Claim Check
slug: claim-check
category: integration
kind: pattern
summary: Claim Check keeps large data out of messages. The sender stores the data in an external store
  and sends only a small reference. The receiver uses that reference to fetch the data.
arc42:
- 5
- 6
- 8
- 11
step: s08-integration-data
related:
- content-enricher
- content-filter
- messaging
- message-channel
- shared-database
- message-structure
- integration-pattern
- messaging-pattern-language
checks:
- The document names who owns the payload lifecycle and aligns message expiry with payload retention.
- The claim check is published only after the payload write succeeds.
- Security tokens are not embedded in the claim check; the store enforces its own access control.
- Where integrity matters, messages carry a hash or signature and a mismatch protocol is defined.
- The external store's availability and added latency are acknowledged as risks.
sources:
- url: https://www.enterpriseintegrationpatterns.com/patterns/messaging/StoreInLibrary.html
  title: Claim Check - Enterprise Integration Patterns
  site: enterpriseintegrationpatterns.com
  accessed: '2026-11-09'
- url: https://learn.microsoft.com/en-us/azure/architecture/patterns/claim-check
  title: Claim Check pattern - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-09'
diagrams:
- file: diagram-1.mmd
  caption: The sender stores the payload first, then sends only the claim check.
review:
  status: generated
  flags: []
---

## Explanation

Messaging systems work best with many small messages. They often limit message size. Large messages risk rejection and can slow the system down.

Claim Check avoids this. The sender writes the payload (the large data) to an external store. It then sends a message that holds only a reference to that payload. This reference is the claim check. Receivers use it to fetch the payload directly from the store.

The goal is to shrink the message without losing information. The data is stored persistently, and the claim check travels onward in its place.

**Relation to other patterns.** A Content Filter removes uninteresting data items from a message. Claim Check removes fields only temporarily, because the data stays in the store. Another component can later use a Content Enricher to fetch the stored data with the claim check.

**Design points to settle:**

- **Lifecycle.** Decide who owns the payload's lifecycle. Coordinate message expiry with payload retention. Otherwise a valid claim check may point to deleted data.
- **Write order.** Writing the payload and publishing the claim check happen in separate systems. They are not one atomic (all-or-nothing) transaction. This can leave orphaned payloads or claim checks that resolve to nothing. Publish the claim check only after the write succeeds.
- **Integrity.** If consumers must verify the payload, put a content hash or digital signature in the message. Also define what happens on a mismatch.
- **Security.** Do not embed security tokens in the claim check. The store enforces its own access controls. Keep sensitive data out of the messaging path.

**Cloud use.** Azure samples pair Blob Storage with messaging systems such as Queue Storage, Event Hubs, and Service Bus. Samples 1 to 3 use Event Grid blob URLs as the claim check. Sample 4 uses a custom claim check that the sending application publishes over Kafka.

## Example

A system sends scanned documents between two services. The sending service saves each scan in a shared store. It then publishes a short message with a reference to the scan. The receiving service reads the reference, fetches the scan from the store, and processes it. If it must check the scan, it compares a hash carried in the message.

## Trade-offs

- **Latency.** Receivers make extra network trips compared with inline delivery.
- **Dependency.** The system now relies on the external store's availability and durability.
- **Consistency.** Message and payload live in separate systems, so they can drift apart. Orphaned payloads and unresolvable claim checks are possible.
- **Ownership.** Someone must own payload cleanup and align it with message expiry.
