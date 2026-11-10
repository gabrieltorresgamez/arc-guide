---
title: Security Tactic
slug: security-tactics
category: tactics
kind: tactic
summary: Security tactics are design decisions for protecting a system. They borrow ideas from physical
  security and fall into four categories. Patterns can realize them, and stakeholders can choose them
  together.
arc42:
- 4
- 8
- 9
step: s07-solution-strategy
related:
- architectural-tactic
- security
- tactics-vs-architectural-styles-and-patterns
- choosing-and-applying-tactics
- encrypt-data
- nonrepudiation
- security-scenario
- architectural-pattern
checks:
- The document states which security tactics were chosen, rather than only naming security patterns.
- Where a pattern is used, the document says which tactic it realizes.
- The document records that stakeholders took part in selecting the security tactics.
sources:
- url: https://www.informit.com/articles/article.aspx?p=3197432&seqNum=6
  title: 3.6 Design Concepts to Support Security | Making Design Decisions | InformIT
  site: informit.com
  accessed: '2026-11-09'
- url: https://laccei.org/LACCEI2014-Guayaquil/RP202.html
  title: Latin American and Caribbean Consortium of Engineering Institutions
  site: laccei.org
  accessed: '2026-11-09'
- url: https://vufind.katalog.k.utb.cz/SummonRecord/FETCH-LOGICAL-i105t-58c88a68c2967a0821f4e19830480975799017cbcc59fa89dc7112f7dfc9e6833
  title: 'More Information: Towards the selection of security tactics based on non-functional requirements:
    Security tactic planning poker :: K.UTB vyhledávací portál | TBU Library Retrieval Portal'
  site: vufind.katalog.k.utb.cz
  accessed: '2026-11-09'
- url: https://pure.psu.edu/en/publications/revising-a-security-tactics-hierarchy-through-decomposition-recla/
  title: Revising a security tactics hierarchy through decomposition, reclassification, and derivation
    - Penn State
  site: pure.psu.edu
  accessed: '2026-11-09'
- url: https://pure.psu.edu/en/publications/a-methodology-for-mining-security-tactics-from-security-patterns/
  title: A methodology for mining security tactics from security patterns - Penn State
  site: pure.psu.edu
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Security tactics are a way to think about protecting software. The idea comes from physical security. In the physical world, a secure facility lets people reach only certain resources. The same kinds of strategies also make sense for computer-based systems. They lead to four categories of security tactics.

**Tactics and patterns work together.** Researchers who revisited the tactics argue that patterns and tactics complement each other. They are not alternatives. You can use them together, and a pattern can realize a tactic.

**The tactic set has been revised.** A 2014 paper noted that the initial set of security tactics had been refined only once up to that point. Its authors proposed a refined set and a new classification.

**New tactics can come from patterns.** Two ideas appear in the research:

- Split an existing architectural pattern into the tactics it is made of.
- Mine tactics from well-known security patterns instead of inventing them from scratch.

**Stakeholders can choose tactics together.** Security Tactic Planning Poker (SToPPER) is a technique for this. Stakeholders interact with each other and jointly select security tactics. In a study with 9 subjects, the technique helped establish a common basis for using security tactics.

## Example

A team builds an online shop and wants to protect customer accounts. Instead of jumping to a product, they first agree on the kinds of protection they need. They hold a SToPPER-style session with the business owner, the operations lead, and the developers. Together they pick the tactics that matter most. Later, the architects look for patterns that realize those tactics.

## Trade-offs

A 2014 paper noted that the initial tactic set had been refined only once. Its authors found that some tactics would be better described as principles or policies, that some were not needed, and that others did not cover the functions needed to secure systems. They proposed a new set and classification.
