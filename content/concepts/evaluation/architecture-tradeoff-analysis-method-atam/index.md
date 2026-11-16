---
title: Architecture Tradeoff Analysis Method (ATAM)
slug: architecture-tradeoff-analysis-method-atam
order: 30
category: evaluation
kind: method
summary: ATAM is a method for checking a software architecture against its quality goals. It shows how
  those goals pull against each other and exposes risks that could block business goals.
long_ok: true
arc42:
- 10
- 11
step: s11-evaluate
related:
- lightweight-atam
- software-architecture-evaluation
- software-architecture-analysis-method-saam
- placing-atam-evaluation-in-arc42
- utility-tree
- scenario-based-questions-from-tactics
checks:
- The architecture documentation records an evaluation of the architecture against its quality attribute
  goals.
- The documented evaluation lists the architectural risks found and states which business goals they could
  threaten.
- Sensitivity points and trade-off points found during the analysis are recorded.
- A utility tree of the driving architectural requirements is included or referenced.
sources:
- url: https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
  title: Architecture Tradeoff Analysis Method® Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method
  title: Architecture tradeoff analysis method - Wikipedia
  site: en.wikipedia.org
  accessed: '2026-11-09'
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8838159/
  title: 'Lightweight Software Architecture Evaluation for Industry: A Comprehensive Review - PMC'
  site: pmc.ncbi.nlm.nih.gov
  accessed: '2026-11-09'
- url: https://c2wiki.gothdyke.mom/ArchitectureTradeoffAnalysisMethod.html
  title: "Architecture Tradeoff Analysis Method"
  site: c2wiki.gothdyke.mom
  accessed: '2026-11-09'
- url: https://llm-coding.github.io/Semantic-Anchors/anchor/atam/
  title: ATAM — Semantic Anchors
  site: llm-coding.github.io
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/documents/629/2000_005_001_13706.pdf
  title: 'ATAM: Method for Architecture Evaluation'
  site: sei.cmu.edu
  accessed: '2026-11-10'
- url: https://cio-wiki.org/wiki/Architecture_Tradeoff_Analysis_Method_(ATAM)
  title: Architecture Tradeoff Analysis Method (ATAM) - CIO Wiki
  site: cio-wiki.org
  accessed: '2026-11-09'
- url: https://www.architectviewmaster.com/blog/architecture-tradeoff-analysis-picking-your-poison-carefully/
  title: 'Architecture Tradeoff Analysis: Picking Your Poison (Carefully) | Architect View Master'
  site: architectviewmaster.com
  accessed: '2026-11-09'
- url: https://concisesoftware.com/blog/architecture-tradeoff-analysis-method-atam/
  title: What is ATAM? Here is the explanation ▷▷ ConciseBlog
  site: concisesoftware.com
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-11/
  title: 11 - Risks and technical debt | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/11-3/
  title: 'Tip 11-3: Identify problems or risks by qualitative evaluation! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://www.heise.de/en/background/Risk-analysis-with-lightweight-architecture-reviews-10355745.html
  title: Risk analysis with lightweight architecture reviews | heise online
  site: heise.de
  accessed: '2026-11-09'
- url: https://www.informit.com/articles/article.aspx?p=24371&seqNum=9
  title: 8 What Are the Benefits and Costs of Performing an Architecture Evaluation? | Evaluating a Software
    Architecture | InformIT
  site: informit.com
  accessed: '2026-11-09'
- url: https://dmccreary.github.io/atam/chapters/10-risk-analysis-atam-reporting/
  title: Sensitivity, Tradeoffs, Risk Analysis, and ATAM Reporting - Architecture Tradeoff Analysis Method
  site: dmccreary.github.io
  accessed: '2026-11-09'
- url: https://docs.arc42.org/section-10/
  title: 10 - Quality | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-08'
- url: https://docs.arc42.org/section-9/
  title: 9 - Architecture decisions | arc42 Documentation
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://docs.arc42.org/tips/10-8/
  title: 'Tip 10-8: Use (quality) scenarios for architecture analysis or evaluation! | arc42 Documentation'
  site: docs.arc42.org
  accessed: '2026-11-09'
- url: https://www.informit.com/store/evaluating-software-architectures-methods-and-case-9780201704822
  title: 'Evaluating Software Architectures: Methods and Case Studies | InformIT'
  site: informit.com
  accessed: '2026-11-09'
- url: https://people.ece.ubc.ca/matei/EECE417/BASS/ch11lev1sec2.html
  title: "Software Architecture in Practice, chapter 11 section 2 (Bass, Clements, Kazman)"
  site: people.ece.ubc.ca
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/library/quality-attribute-workshop-collection/
  title: Quality Attribute Workshop Collection | CMU Software Engineering Institute
  site: sei.cmu.edu
  accessed: '2026-11-09'
- url: https://www.sei.cmu.edu/documents/1288/2020_005_001_650490.pdf
  title: Maintainability
  site: sei.cmu.edu
  accessed: '2026-11-10'
- url: https://www.sei.cmu.edu/documents/1162/1997_005_001_16511.pdf
  title: Recommended Best Industrial Practice for Software Architecture Evaluation
  site: sei.cmu.edu
  accessed: '2026-11-10'
- url: https://arxiv.org/html/2506.00150
  title: Supporting architecture evaluation for ATAM scenarios with LLMs
  site: arxiv.org
  accessed: '2026-11-09'
- url: https://www.informit.com:443/articles/article.aspx?p=24371&seqNum=8
  title: 7 What Are the Outputs of an Architecture Evaluation? | Evaluating a Software Architecture |
    InformIT
  site: informit.com
  accessed: '2026-11-09'
- url: https://dmccreary.github.io/atam/faq/
  title: FAQ - Architecture Tradeoff Analysis Method
  site: dmccreary.github.io
  accessed: '2026-11-09'
diagrams: []
review:
  status: generated
  flags: []
---

## Explanation

The Architecture Tradeoff Analysis Method (ATAM) was developed at the Software Engineering Institute at Carnegie Mellon University. It evaluates a software architecture against its quality attribute goals. These are goals such as performance or security (see the article Quality Attribute). The method also shows how those goals interact.

The aim is to expose architectural risks. These are weaknesses that could keep an organization from reaching its business goals.

**Who takes part.** ATAM brings together a trained evaluation team, the architects and representatives of the stakeholders. The evaluation team is external to the project and has three to five members. Its roles include a leader who runs the evaluation, scribes, a timekeeper and people who ask questions. Project decision-makers have the authority to mandate architectural changes. Broader stakeholders join in the second phase.

**How it runs.** An evaluation typically takes three to four days. ATAM formally has nine steps. In phase 0, the evaluation team and key decision-makers prepare: they arrange logistics and check that the architecture is documented well enough to evaluate. Phase 1 covers steps 1 to 6 and takes about a day. Phase 2 covers steps 7 to 9 and takes about two days.

- **Step 1:** the evaluation leader describes the method to everyone present.
- **Step 2:** a project spokesperson, ideally the project manager or the system customer, presents the business goals.
- **Step 3:** the architect presents the architecture, focused on how it addresses the business drivers.
- **Step 4:** the architect names the architectural approaches. They are only named here, not analyzed.
- **Step 5:** the team builds a utility tree. This is a hierarchic model of the driving requirements, refined down to scenarios and then prioritized (see Utility Tree).
- **Step 6:** the team analyzes the highest-priority scenarios against the approaches and identifies risks, sensitivity points and trade-off points.
- **Step 7:** the larger stakeholder group brainstorms scenarios, and prioritizes them by a vote of the whole group.
- **Step 8:** the analysis is repeated with the top-ranked scenarios.
- **Step 9:** the results are presented to the stakeholders.

**What it produces.**

- **Risks.** An architectural decision that may lead to undesirable consequences given the stated quality attribute requirements. See Architectural Risk.
- **Non-risks.** A decision the team judged well-reasoned for the quality scenarios. A non-risk needs the same evidence as a risk: the quality attribute or scenario, the architectural decision, and the justification that the decision is adequate. An area the team did not examine is not a non-risk.
- **Sensitivity points and trade-off points.** They are described below.
- **Risk themes.** ATAM groups individual risks into themes. Each theme shows how a set of risks threatens a business driver.
- **The utility tree itself.**

The results go into an out-brief presentation, a written report, or both. In arc42, section 11 holds a list of technical risks and debts, ordered by priority (see Placing ATAM Evaluation in arc42).

**Common mistakes.** Findings float free of the architecture when decisions are not linked to quality attributes and scenarios. A vague risk such as "the architecture might have availability problems" names no decision and no scenario, so nobody can act on it. A non-risk or a sensitivity point without a named decision and a named quality cannot be shown.

**When to use it.** ATAM is most valuable early in the life cycle, when the cost of changing the architecture is minimal. It is also suggested when stakeholders have conflicting quality requirements, for example performance versus security. Older systems can be analyzed once their real architecture has been recovered, because their documentation is often missing or inaccurate.

**Comparing alternatives.** arc42 suggests a table with quality goal, scenario, solution approach and risk for qualitative evaluation.

**Benefits.** Risks show up early, quality requirements become clearer, the architecture documentation improves, and stakeholders communicate more.

**Cost.** A full ATAM gathers the evaluation team, the architects and stakeholder representatives for three to four days. One source puts a medium-size evaluation at about 70 person-days across all participants and small projects at about 32. Another source gives a wider range, from two days to several weeks. Reusing recorded scenarios from earlier evaluations can reduce the effort, and lighter methods trade thoroughness for speed (see Lightweight ATAM).

**More about the ATAM terms and steps.**

- **Architectural Approach Identification:** Architectural approach identification is Step 4 of ATAM. The architect names the approaches used in the system. The team only lists them here and analyzes them later.
- **Analysis of Architectural Approaches:** Analysis of architectural approaches is the ATAM step where evaluators examine how design decisions handle important scenarios. It produces risks, non-risks, sensitivity points and trade-off points. A second pass repeats it with stakeholder-ranked scenarios.
- **ATAM Risk:** In ATAM, a risk is an architectural decision that may harm how the system responds to a quality scenario. Teams record risks, and the good decisions (non-risks), so they can review and mitigate them.
- **Sensitivity Point:** A sensitivity point is a property of a system that one quality, such as speed or confidentiality, depends on strongly. Teams flag these points during evaluation so they know which decisions carry the most leverage.
- **Trade-Off Point:** A trade-off point is a property of the architecture that affects several quality attributes at once. Improving one attribute through it costs another. ATAM reports these points so teams can decide on a compromise knowingly.

## Example

A team plans an online ticket shop. Fast checkout and strong data protection are both top goals. During the evaluation, the group finds that encrypting every request slows checkout. That is a trade-off point. The group also finds that checkout depends on one payment service with no fallback. That is a risk. The team records both and links the risk to the business goal of steady sales.

## Trade-offs

ATAM is costly. The method is scenario-based and involves many stakeholders.

Lightweight variants reduce cost by minimizing documentation, formality and the number of stakeholders involved. See Lightweight ATAM.
