---
title: Web as a Software Connector
slug: web-as-integration-pattern
category: integration
kind: style
summary: The Web can connect software components. Resources have global URIs, and components read or change
  them through HTTP. Links inside the returned data let clients discover further resources.
arc42:
- 3
- 4
- 8
step: s08-integration-data
related:
- software-connector
- integration-pattern
- shared-database
- messaging
- remote-procedure-call
- file-transfer
- idempotent-receiver
- retry
checks:
- Shared state is exposed as resources, each identified by a URI that other representations can reference.
- Operations that clients may retry after a failure use idempotent HTTP methods (GET, PUT, DELETE).
- Reads use GET only, so caches and intermediaries can take part.
- Representations contain links that tell clients what they can do next.
sources:
- url: https://www.rfc-editor.org/rfc/rfc9110.html
  title: 'RFC 9110: HTTP Semantics'
  site: rfc-editor.org
  accessed: '2026-11-10'
- url: https://martinfowler.com/articles/richardsonMaturityModel.html
  title: Richardson Maturity Model
  site: martinfowler.com
  accessed: '2026-11-10'
- url: https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
  title: 'Fielding Dissertation: CHAPTER 5: Representational State Transfer (REST)'
  site: ics.uci.edu
  accessed: '2026-11-10'
diagrams:
- file: diagram-1.mmd
  caption: Components exchange state through resources; a link in one representation leads to another
    resource.
review:
  status: generated
  flags: []
---

## Explanation

**Resources and URIs.** The Web is built on the REST style. In REST, the resource is the central abstraction of information. Most resources are identified by a URI.

**Safe reads.** HTTP defines GET as a safe operation. It does not significantly change server state. Because of this, any participant in the routing of requests can use caching.

**Discovery through links.** Representations can contain hyperlinks, also called hypermedia controls. These links tell a client what it can do next and give it a starting point for exploring the protocol. This also makes the protocol more self-documenting.

**Scalability.** REST gains the client-server separation of concerns while avoiding the server scalability problems of the traditional client-server style.

## Example

An order system publishes each order as a resource at its own URI. A billing component reads the order with GET. The order representation also contains a link to the customer resource. Billing follows that link instead of knowing the customer address in advance.
