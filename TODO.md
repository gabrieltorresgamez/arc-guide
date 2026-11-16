# TODO

Vision: an **entry point** to the most important architecture topics, for non-architects and for LLMs. Not everything is in full detail; sources and links carry the detail. Rules are in `CLAUDE.md`.

Principles used for every item below:
- All or none. If a set of pages cannot be complete, keep one overview page per topic and link to the best public reference instead of covering some members.
- ISO/IEC 25010:2023 only. Subcharacteristics live inside their characteristic page.
- arc42 (docs.arc42.org) and the arc42 quality model (quality.arc42.org) are link targets, not copy sources.

Status: `[x]` done, `[~]` in progress, `[ ]` open.

## Done (this round)
- [x] Subcharacteristic pages removed; all 40 listed in their characteristic page with short definition and links.
- [x] Tactics regrouped per ISO characteristic (`reliability-`, `maintainability-`, `performance-efficiency-`, `interaction-capability-`, `security-`, `safety-tactics`). Individual tactic pages, energy, integrability/deployability removed.
- [x] `usability` renamed `interaction-capability`; 2011-to-2023 revision page removed; Bass coverage page removed.
- [x] Claim-check tool (`pipeline/claimcheck.py`) restored.

## Research findings (2026-11-16)
- **EIP patterns** (`integration/`): 37 pattern pages vs about 65 patterns on enterpriseintegrationpatterns.com. Partial. Core patterns missing: Aggregator, Resequencer, Message Bus, Channel Adapter, Competing Consumers, Wire Tap, Message Broker, Control Bus.
- **BPMN** (`modeling-bpmn/`): 19 element pages. Partial. Basic elements (start/end event, exclusive and parallel gateway, sub-process) have no page; rare ones do (link event, ad-hoc sub-process, compensation event).
- **UML** (`modeling-uml/`): 30 element pages. Partial. There is no activity, object or communication diagram page.
- **arc42 chapter pages** (`documentation/arc42-*`, 9 pages, 200 to 435 words) map 1:1 to guide steps s01 to s10 and are already short. Keep. Only 1% of `documentation` pages cite quality.arc42.org.
- **arc42 quality model** has about 229 quality pages, 57 approaches, 50 standards, 11 articles and about 151 example quality requirements. Each requirement has Context, Trigger, Acceptance Criteria and an "Implements <qualities>" line. They fit the scenario topic.
- **Licenses:** quality.arc42.org is CC BY-SA 4.0. This repo is CC0. Link to it, never copy or closely adapt its text. docs.arc42.org license not verified.
- **ISO text:** definitions are paraphrased from iso25000.com. Keep them short and in our own words.
- **Characteristic pages** are 319 to 549 words with 6 to 18 sources. Section structure differs between them.
- **Claim check** is noisy. It flags mild "stretched" wording on each run. Treat "unsupported" and "contradicted" as blocking, review "stretched" by hand.

## A. Quality attributes (follow-up of this round)
- [x] A1. Replace the 7 per-attribute scenario pages (`availability-`, `modifiability-`, `performance-`, `security-`, `interoperability-`, `testability-general-`, `usability-scenario`) by `quality-attribute-scenario` plus links to arc42 example requirements per characteristic.
- [x] A2. Fold availability-specific pages into `reliability`: `quantifying-recovery-and-availability-trade-offs`, `forces-decisions/architectural-decisions-for-availability`. Check `fault` (probably keep: tactics use it).
- [x] A3. Merge `standard-quality-attribute-checklist` into `iso-iec-25010-quality-model`.
- [x] A4. The 9 characteristic pages share one tail: Tactics link (where a tactics page exists), Subcharacteristics, In the arc42 quality model, Example quality requirements. The middle sections stay topic-specific on purpose.
- [x] A5. Link each characteristic to its arc42 quality page and tag group (for example `#usable`, `#secure`, `#safe`).

## B. Evaluation (35 pages)
- [x] B1. (18 ATAM-internal pages folded into `architecture-tradeoff-analysis-method-atam`) One ATAM page plus sources instead of about 20 ATAM-internal pages (phases, roles, presentations, results, case study). Keep SAAM, ARID, LASR, risk storming, scenario weighting as short comparison entries. Link arc42 chapter 11.
- [x] B2. Pages under 150 words: `tactics-based-questionnaire`, `atam-phase-0`, `business-drivers-presentation-in-atam` were folded into ATAM or the tactics page. `twin-peaks-model`, `shearing-layers` and `sweeping-it-under-the-rug` are kept: each is a distinct, sourced concept linked from guides or from the Big Ball of Mud pages.

## C. Partial sets (decide all-or-none)
Recommended: overview page per topic plus link to the official reference.
- [x] C1. Integration: `messaging-pattern-language` is now the catalog of all 61 EIP patterns in 7 categories with short definitions and official links. 31 individual pattern pages removed. Claim check on it: the 'not described' findings are tool limits (21 EIP pages over the 300k-character budget; set `CLAIMCHECK_TOTAL_CHARS` higher or check per category). Wording was cut where a finding was clear.
- [x] C2. BPMN: correction to the research note above. The 19 element pages are at element-group level (event, activity, gateway, swimlane, connecting object, data element, artifacts, diagram types), so the set is consistent. 8 tool-specific deep dives (intermediate, boundary, link, compensation events; event-based gateway; ad-hoc sub-process; task markers; data exchange) were folded into the group pages.
- [x] C3. UML (done: element-level and `*-modeling-mistakes` pages folded into 7 diagram pages, 28 pages removed). Original note: `uml-diagram-taxonomy` now lists all 14 diagram types with short definitions and links, so coverage is complete. Open: element-level pages (association, composition vs aggregation, composite state, concurrent region, delegation connector, component port, generalization, instance specification, message types, nested components, package relationships, provided/required interface, state and event, state entry/exit/do, transition syntax, UML interface, use-case goal hierarchy, transfer-object pattern) exist for only some diagram types. Fold them into their diagram page (as short entries) or leave. Also the 7 `*-modeling-mistakes` pages could become one section per diagram page.
- [x] C4. (done: 27 BPM and BPMN background pages folded into 4 host pages: model quality, process analysis and modeling, modeling tips, BPMN overview. `decision-model-and-notation` and `workflow-pattern` kept.) Original note: Check `decision-model-and-notation` and the process-analysis pages (`process-mining`, `process-analysis`, `bpm-life-cycle`, `waves-of-business-process-management`): keep only what stays inside the BPMN overview.

## C5. Other duplicate clusters (folded, same approach)
- [x] `pipe-and-filter-pattern` into `pipes-and-filters`; `layers-pattern` and `layers-and-components-decomposition` into `layered-architecture`; data model pages into `conceptual-data-model` and `conceptual-vs-logical-vs-physical-data-model`; capability map pages into `business-capability-map`; `enterprise-architecture-maturity-stages` into `...-levels`.
- [x] ADR cluster folded: format and quality pages into `architectural-decision-record`, process pages (cycle, issues, dependencies, ready/done) into `architectural-decision-management-practices`.
- [x] D2 view antipattern pages folded into their view pages (component, distribution, runtime, overview, context, good-view). D1 `arc42-quality-chapter` links the arc42 quality model.
- [x] Reviewed and folded: EA artifact pages (7 into the three `*-architecture-artifacts` / technology pages), functional requirements (user story, acceptance criteria, use case, user story vs use case: 12 pages), DDD building blocks (10 pages into `ddd-modeling-elements`), principles (coupling and cohesion, working with principles: 9 pages). Kept on purpose: `story-mapping`, `story-splitting`, `agile-enterprise-backlog-model`, requirement types and elicitation pages.
- [x] Reviewed and folded: fundamentals, vision-stakeholders, evaluation (ATAM terms), enterprise-architecture (TOGAF, frameworks, EA management, business and application architecture). `styles-patterns` kept as is: each page is a distinct style, not a member of a set.

## D. Documentation (57 pages)
- [x] D1. `arc42-quality-chapter`: link quality.arc42.org (Q42, example requirements).
- [x] D2. Review the view-antipattern pages (`component-view-antipattern-...`, `runtime-view-antipattern-...`, `undetected-duplication-antipattern`, ...). Merge into their view page or link docs.arc42.org.
- [ ] D3. Check docs.arc42.org license before quoting or adapting it.

## E. Tooling and quality gates
- [x] E0. Build checks for the content rules (`check_content` in `pipeline/build.py`): minimum words, unknown references, 2011 wording, tactic page naming. Warnings: 132 at the time of writing (see `build/reports/build.md`): single-source pages, orphans, dead "See the article" titles.
- [ ] E4. Work down the build warnings: single-source pages, orphan pages, "See the article X" mismatches.
- [x] E1. Claim-check gate (`pipeline.claimcheck` without slugs checks pages changed since HEAD): only "unsupported" and "contradicted" findings block. Run it on every page touched in A to D.
- [x] E2. Link checker for source URLs: `pipeline/linkcheck.py`. Not run over all pages yet (about 1,500 URLs, about 30 minutes).
- [ ] E3. Update README to match `CLAUDE.md` rules and the claim-check command.

## Notes for the next session
- Section C removes about 100 pages. Commit a checkpoint first, because the work so far is uncommitted and deletions cannot be undone page by page afterwards.
- Page count after all folds: 271 articles (was 552 at the start of this round).
- Claim check has not been run on the pages folded in C3 to C5. Their text is the pages' own sourced summaries, but run `uv run python -m pipeline.claimcheck` before committing if you want the gate.
- Claim-check report of the merged ATAM page: `build/reports/claimcheck-atam.md`.

## Idea (later): structure like a course
Source idea: mirror the chapters of a software architecture course. Assessment: the 16 concept categories already follow those chapters: fundamentals (introduction, basic terms, architect role in agile), forces-decisions (forces, concerns, constraints, decisions), modeling-uml, modeling-bpmn, functional-requirements, quality-attributes (non-functional requirements), documentation (arc42, views, C4, docs as code), enterprise-architecture (frameworks), data-architecture, vision-stakeholders (vision, system idea, stakeholder views), domain-driven-design, principles, styles-patterns, tactics, integration, evaluation (ATAM). Gaps and options:
- [x] C4 now has its own sidebar group, and so does documentation as code (`taxonomy.yaml` subcategories + `content/subgroups.json`). The empty "Documentation antipatterns" group was removed.
- [x] Sidebar order is a learning path: fundamentals, vision, functional requirements, quality attributes, decisions, documentation, UML, BPMN, principles, styles, tactics, integration, DDD, data architecture, enterprise architecture, evaluation (order of `categories:` in `taxonomy.yaml`).
- [x] Certification programs: skipped, no content in this repo.
- [x] Taxonomy change only, no page content touched.

## Tooling notes
- The claim and link checkers read sources with `common.fetch_public`. It falls back to `curl` when Python's OpenSSL rejects an incomplete certificate chain (seen on uml-diagrams.org). Certificate checks stay on. Before this fix such sources were silently skipped as "unreadable", so older claim-check reports may contain false "unsupported" findings for them.
- Pages with many sources (EIP catalog, 65 sources) need `CLAIMCHECK_PAGE_CHARS=7000 CLAIMCHECK_TOTAL_CHARS=520000`, otherwise sources are skipped and definitions look unsupported. With that budget the EIP catalog's 8 system-management definitions were confirmed.
- `CLAIMCHECK_PAGE_CHARS` and `CLAIMCHECK_TOTAL_CHARS` set the per-page and total budget of the claim check.

## Link check (2026-11-16)
- [x] `pipeline.linkcheck` over 1,124 source URLs: 10 bad (2 payment-required, 7 not found, 1 forbidden). Those sources were removed; statements that depended on them were cut after a claim check. `data-architecture-diagram-types` had only a dead source and was deleted.
- [x] Build now fails any page without sources.
- [ ] Run `pipeline.linkcheck` again before each release or every quarter.
- [ ] 14 build warnings remain (single-source pages and false positives of the 'See the article' check).

## Decision
- Claim-check policy: run the gate (`uv run python -m pipeline.claimcheck`, no slugs) on changed pages only. No full-site pass. Pages never touched since the 2026-11 rework keep their original generated text and the earlier claim check of that pipeline.

## Full claim-check pass (2026-11-16)
- All 275 pages were checked with `pipeline.claimcheck`. Rounds on the changed pages: 96 findings (158 never-checked pages), about 50, 21, 14, 12, 12. About 215 sentences were removed or reworded.
- The checker has a noise floor of about 10 findings per run. What is left are invented Example scenarios and findings the checker itself calls "not a problem". Treat the gate as done when only those remain.
- Weak spots (sources the checker cannot read, such as PDFs): `architecture-description-element`, `iso-iec-ieee-42010-architecture-description-model`, `service-oriented-architecture`. Find readable sources for them before adding more text there.

## External review (LLM, 2026-11-16)
Source: a review of the live site by another LLM (shared doc "arc.fuet.ch – Content quality optimization"). It read about 38 pages through a summarizing fetch tool, so its counts are estimates. I checked its main claims against the repo. Its "factual errors" did not hold up (it checked ISO 25010:2023, Fowler's monolith sentence and the Bass tactics itself), which supports the claim check. Its gaps are real.

### Agreed, to do (checked against the repo)
- [x] **Guide link texts after the merges (my side effect).** DONE: 186 links rewritten (the link text that named a merged page is now plain text followed by one link to the host); build warns on 3 or more link texts for one target. 58 link targets in the guides have several different link texts that name pages that were merged away (for example four labels that all go to `architecture-principle`, three that go to `component-view`, three to `stakeholder`). Rewrite each link so its text matches the page it opens. Add a build warning for "same target, different link texts on one page".
- [x] **Source lint** DONE (fails the build now; fixed: 14 empty titles filled from the pages, 3 duplicate sources removed, 3 locale URLs moved to en-us) (build warnings, fail on empty titles): duplicate sources after URL normalization (`reliability-tactics` lists one SEI blog twice), sources with an empty title (`architecture-tradeoff-analysis-method-atam` has 2), non-English Microsoft locale URLs (`bounded-context` uses `sk-sk`).
- [x] **One spelling "trade-off".** DONE (the name "Architecture Tradeoff Analysis Method" keeps its spelling; the build warns on other uses). The text has 258 "trade-off(s)" but 17 "tradeoff(s)". Normalize, and add a check.
- [ ] **Title and slug agree.** 69 pages have a title that differs from the slug. Keep an alias list for intended cases and rename the rest, or add a title that matches (no slug renames while redirects do not exist).
- [x] **Promises in the section scopes** DONE: styles scope now lists only styles that have a page and names the arc42 links; Conway's law has a page (`conways-law`, sourced from Fowler and Wikipedia). Original item: (`taxonomy.yaml` feeds the section `llms.txt`): fundamentals names Conway's law and architectural erosion, styles names event-driven and space-based. Either add a sourced page or cut the promise.
- [~] **Page fixes, each only with sources:** DONE for security-tactics (categories and tactics from the Bass chapter), architectural-decision-record (Nygard structure, status lifecycle, MADR skeleton, Y-statement fixed), quality-attribute-scenario (six elements and a full six-part example), architecture-principle (one parts list), technical-debt (principal, quadrant), reliability-tactics (bulkhead, idempotency), c4-model (diagram now matches the Example, correct C4-PlantUML argument order), software-architecture (Conway's law link, repetition cut), event-sourcing page (renamed Distributed Event Log, links arc42 Event Sourcing). NOT DONE: microservices alternative (the single monolith is already named; modular monolith has no source yet). Original list:
  - `security-tactics`: name the tactic categories (detect, resist, react, recover) and the tactics under them, if a source lists them.
  - `architectural-decision-record`: add a MADR skeleton, a status lifecycle and the origin (Nygard), and make the two Y-statement descriptions agree.
  - `quality-attribute-scenario`: list all six parts, define "source", and use an example that fills every part.
  - `architecture-principle`: one list of a principle's parts. A conflict-resolution method only if a source gives one.
  - `c4-model`: the PlantUML snippet must match the Example text and use the right argument order (check first).
  - `event-sourcing-with-distributed-event-log`: split into a general event sourcing page and the Event Hubs log page, or rename it.
  - `technical-debt`: define principal and explain the quadrant (it is listed as a source but not used).
  - `software-architecture`: add Conway's law (a sentence from the listed source) or drop that source, and cut the repetition that the "More about the definition" fold created.
  - `reliability-tactics`: explain bulkhead and idempotency from sources.
  - `microservices-architecture`: the alternative (modular monolith) from a source.
- [x] **Overlap in Documentation.** DONE: `purpose-of-views` and `architectural-view-types` into `architecture-view`; `4-1-view-model` into `architecture-view-model`; `runtime-view`, `distribution-view` and `component-view` now point to the arc42 chapter pages (the chapter pages stay, so every arc42 chapter has a page). The C4 level pages stay as they are. Original item: Four pages define views (`architecture-view`, `architectural-view-types`, `architecture-view-model`, `4-1-view-model`). Merge them. The arc42 chapter pages I added for 5, 6 and 7 overlap with `component-view`, `runtime-view` and `distribution-view`: decide whether the arc42 pages absorb the view pages or the view pages link them as the arc42 mapping. The C4 level pages overlap with `component-view` and `architectural-overview-diagram`.
- [x] **Odd titles and narrow pages.** DONE: 9 pages folded into their hosts. Original item: Rename or merge "Architect Settles In Method Phase", "Working with Functional Requirements (Method Phase)", "Define Target Data Architecture Method Phase", "Process Automation Magnifies Efficiency". Fold `kroki`, `diagram-metadata-in-png-drawio-png` into `diagrams-as-code`, and `requirements-decision-modeling-for-cyber-physical-systems-of-systems` into a decision page.
- [x] **Missing topics, the cheap way.** DONE: 28 more arc42 approach links on the styles hub and the six tactics pages. Original item: Extend the existing arc42 approach link lists instead of writing pages: styles hub (saga, transactional outbox, API gateway, backends for frontends), security characteristic and tactic page (threat modeling, least privilege, strong authentication, secret management), flexibility and maintainability (blue-green, canary, feature toggles, defer binding). Check that each arc42 URL loads first.
- [x] **SOLID is half there.** DONE: `solid-principles` covers all five (Wikipedia SOLID plus the old ISP and OCP sources); the two single pages were folded. Original item: The site has Interface Segregation and Open-Closed but not Single Responsibility, Liskov Substitution, Dependency Inversion. That breaks "all or none": add one SOLID overview with all five and sources, or fold the two into the principles hub.
- [x] **Tactics for Compatibility and Flexibility.** DECIDED: keep six tactics pages; the rule is "only where a source lists tactics for that ISO characteristic". Stated in the taxonomy scope. Original item: Tactics pages exist for 6 of 9 characteristics (that is stated in the section scope now). Decide: add short hub pages with arc42 approach links, or keep and state the rule ("only where a source has tactics").
- [x] **Review checklists (arc42 sections 1 and 10).** DONE: at most 30 checks per section (primary-section pages first, near-duplicates dropped), a worked example review in the review instructions. Not done: severity per check, one value for every limit. Original item: About 84 and 58 checks. Cap per section, remove near-duplicates, one value per limit (quality goals: "3 to 5" appears in three forms), fix checks that link to unrelated pages, add a worked example review next to the OK / ISSUE / MISSING / N/A template.
- [ ] **Guides.** Step 4: utility-tree priorities (importance, difficulty). Step 7: a method for resolving quality-goal conflicts, from a source. Recovery guide: time boxes and code-based techniques, from sources. One continuous ClinicBook case through all 12 steps.
- [ ] **Examples of quality topics** must show the whole concept (a measurable response measure for the ATAM example, all six scenario parts). Not a site-wide rule.

### Partly agreed
- [ ] **Citations tied to claims.** Inline markers on every claim is too heavy for short entry pages. Do it only where a number, date or attribution appears (ATAM "70 person-days"), and keep the claim check as the safety net.
- [ ] **Concepts named but not linked.** Add a warning, not an auto-linker.

### Not agreed
- A mandatory Trade-offs template (Gains, Costs, Use it when, Avoid it when, Alternatives). It would force text that no source states, against rule 1. Instead remove Trade-offs sections that have no sourced content, and fill the rest only from sources.
- An LLM judge as a build gate for "does the Example show every part". Costly and subjective. The claim check stays the gate. Revisit as an optional report.
- Writing many new pages for AI-based systems, operations, team structure. That reverses the consolidation. Use link hubs first (see above). AI-based systems is a scope decision for later.

### Done during this pass (2026-11-16, later)
- A page was damaged by my automatic sentence removals (`architecture-description-element`: headings with nothing under them, bare "See *X*." lines). All 274 pages were scanned: 14 empty or meaningless headings (mostly empty "Trade-offs" sections) were removed, and the page was deleted because the 42010 standard page already covers it.
- The build now fails any page with an empty section (test included).
- "See the article X" references in concept pages are links now: at build time, exact page titles inside a "See ..." clause are turned into links (about 145 pages). The Markdown files get absolute links.
