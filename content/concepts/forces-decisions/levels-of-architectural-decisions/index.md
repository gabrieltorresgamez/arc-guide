---
title: Levels of Architectural Decisions
slug: levels-of-architectural-decisions
category: forces-decisions
kind: concept
summary: Architectural decisions are made at several organizational levels. Higher levels decide less
  and mainly set guidelines. Development teams make most decisions, so sharing them openly keeps the architecture
  sound.
arc42:
- 9
- 4
step: s09-decisions
related:
- architectural-decision
- architectural-decision-record
- architecture-principle
- architectural-decision-management-practices
- architecturally-significant-decision
- architecture-decay
- arc42-architecture-decisions
checks:
- Architectural decisions made by teams are recorded, for example in ADRs, after seeking advice from affected
  parties.
- Decisions are visible to all organizational levels, not only to the team that made them.
- Higher-level bodies provide guidelines or principles rather than deciding everything themselves.
sources:
- url: https://www.informit.com/articles/article.aspx?p=3128836&seqNum=2
  title: Architectural Decisions | Why Software Architecture is Important and Essential Activities | InformIT
  site: informit.com
  accessed: '2026-11-09'
- url: https://www.infoq.com/articles/empowering-decentralizing-architectural-decision-making/
  title: 'Empowering Teams: Decentralizing Architectural Decision-Making - InfoQ'
  site: infoq.com
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

Organizations make architectural decisions at different levels, such as enterprise boards, product-level boards, and development teams.

**Fewer decisions higher up.** The higher you go, the fewer decisions get made and the fewer reviews take place. An enterprise architecture board, for example, decides far less than a product-level governance board.

**Teams decide most.** Most decisions that can affect an architecture are made on the ground by development teams.

**Guidelines, not decisions.** The main job of higher governance bodies is to define guidelines, not to make decisions. Architecture principles can also guide teams. They help align teams with business strategy without becoming centralized decisions. (See Architecture Principle.)

**Decentralized decisions.** In a decentralized approach, any team may decide. It first asks the people affected for advice. It then records the decision in an Architectural Decision Record (ADR). Architects facilitate this process. They do not make the decisions themselves.

**Visibility holds it together.** Because teams decide so much, decisions must be visible at all organizational levels. This helps avoid architectural compromise. Transparency in sharing decisions and seeking advice is fundamental to decentralized decision making.

## Example

Two teams work on one product. Each has a deadline. One team adds a few stored procedures (logic that runs inside the database) here and there to finish its work. Nobody outside the team hears about it. Each choice looks small. Together they can quietly erode the architecture. If the team had recorded each choice and asked affected parties for advice, others could have seen the pattern early and responded.

## Trade-offs

Letting teams decide puts most decisions close to the work. But it depends on transparency. If teams do not share their decisions, the architecture can be compromised without anyone noticing.
