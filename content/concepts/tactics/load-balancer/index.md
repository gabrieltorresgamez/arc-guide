---
title: Load Balancer
slug: load-balancer
category: tactics
kind: pattern
summary: A load balancer spreads incoming requests across several backend servers. It uses resources evenly,
  helps keep response times low, avoids overload, and can hide a failed server from clients.
arc42:
- 5
- 7
- 8
step: s07-solution-strategy
related:
- performance-tactics
- availability
- scalability
- architectural-tactic
- performance-efficiency
- fault-tolerance
- active-redundancy
checks:
- The document states which distribution algorithm the balancer uses, such as round-robin, least connections
  or weighted.
- The document states whether the balancer works at Layer 4 or Layer 7 and why.
- The document says how failed backends are detected and avoided.
- The document says whether clients need session affinity.
- For multi-region backends, the document addresses the regional single point of failure of a single regional
  balancer.
sources:
- url: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/load-balancing-overview
  title: Load Balancing Options - Azure Architecture Center | Microsoft Learn
  site: learn.microsoft.com
  accessed: '2026-11-08'
- url: https://nginx.org/en/docs/http/load_balancing.html
  title: Using nginx as HTTP load balancer
  site: nginx.org
  accessed: '2026-11-08'
diagrams:
- file: diagram-1.mmd
  caption: Clients reach one balancer, which spreads requests over healthy servers and avoids a failed
    one.
review:
  status: generated
  flags: []
---

## Explanation

A load balancer sits between clients and a group of backend servers. It receives each request and decides which server handles it. The goals are to use resources well, raise throughput, shorten response time, and avoid overloading any one server. Because the work is spread over redundant resources, it can also improve availability.

**How it picks a server**

The rule for choosing is called the distribution algorithm. Common choices:

- **Round-robin.** Servers take turns. In nginx this is the default. Azure API Management offers it too.
- **Least connections.** The balancer sends new requests to the less busy server. This helps when requests take very different amounts of time.
- **Weighted.** Some servers get a larger share than others.
- **Priority-based.** Azure API Management offers this as a third method.

**Keeping a client on one server**

Sometimes a client must return to the same server. This is called session affinity or session persistence. The nginx `ip_hash` method does it. It sends a client's requests to the same server unless that server is unavailable.

**Handling failures**

nginx watches the responses it gets. If a server returns an error, nginx marks it as failed and avoids it for a while.

**Where it works**

- **Layer 4** balancers handle TCP/UDP traffic. Azure Load Balancer is one. It is zone redundant and built for high performance and low latency.
- **Layer 7** balancers work with HTTP(S). They offer SSL offload, a web application firewall (WAF), path-based balancing and session affinity. Application Gateway is a proxy balancer of this kind. It provides application delivery controller functionality.

**Passthrough or terminating**

A passthrough balancer connects the client directly to the backend that the algorithm chose. A terminating balancer acts as a proxy. The client connects to the balancer, and the balancer opens a separate connection to the backend.

## Example

An online shop runs three identical copies of its product service behind one load balancer. Clients only know the balancer's address. Each request goes to the next copy in turn. One copy starts returning errors. The balancer marks it as failed and sends traffic to the other two.

## Trade-offs

- A single regional balancer in front of backends in several regions creates a regional single point of failure. It also adds latency, because traffic is forced through one region first.
- Session affinity keeps a client on one server, but it ties that client to the server. If the server becomes unavailable, the client moves.
- Azure positions its Layer 4 service for high performance and low latency.
- Terminating balancers keep a separate backend connection. Passthrough balancers link the client directly to a backend.
