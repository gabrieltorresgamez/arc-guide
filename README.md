# Software Architecture Guide

A searchable knowledge base about software architecture, written for non-architects: https://arc.fuet.ch

- concept articles, organized by topic, each with its public sources,
- beginner guides: how to start the architecture of a project, what must exist first, what to do if it is missing,
- llms.txt v2 files and a Markdown version of every page, so LLMs can use the site,
- an arc42 review checklist: give an LLM one link and your arc42 document, get a review.

## Vision and principles

The site is an **entry point** to the most important software architecture topics, for readers who are not architects and for LLMs.
It is not a full reference. Pages are short, and the sources and links carry the detail.

1. **Entry point first.** A page says what a topic is, when it matters and where to read more.
2. **Every statement has a public source,** and the text is in our own words.
3. **All or none.** A closed set (for example the ISO 25010 characteristics, the EIP patterns, the arc42 chapters) is covered completely or by one overview page, never partly.
4. **Standards over inventions.** Quality models follow ISO/IEC 25010:2023 only. arc42 and its quality model are the preferred catalogs for tactics and approaches. They are linked, never copied (the quality model is CC BY-SA 4.0).
5. **One entry point per topic,** in a reading order where one exists.

The detailed rules and the automated checks are in `CLAUDE.md`.

**How it was made:** LLM agents researched each topic on the public web and wrote the first version. Since then the
content was edited with an LLM assistant: overlapping pages were merged and statements without a source were removed.
An LLM claim check compares each article with the pages in its source list. The articles are machine-generated and not
reviewed by a person.

## Checks

- `uv run python -m pipeline.build` also runs the content checks: minimum length, unknown references, 2011-model wording, tactic page naming, plus warnings for single-source pages and orphan pages.
- `uv run python -m pipeline.claimcheck [SLUG ...]` checks articles against their sources with Claude (your subscription). Without slugs it checks the pages changed since the last commit and fails on unsupported or contradicted claims.
- `uv run python -m pipeline.linkcheck` checks that every source URL still loads (about 30 minutes for the whole site).
- `uv run pytest` runs the unit tests.

## Build

1. `docker compose up -d` starts a local [Kroki](https://github.com/yuzutech/kroki) for the diagrams.
2. `uv run python -m pipeline.build` builds the site into `site/dist/` and runs the checks.
3. `cd site && npm run dev` for a local preview.

Self-hosting: set `SITE_URL` in `compose.yml`, then `docker compose --profile site up -d --build`; nginx serves the
site on port 8080. Re-run after changing `content/`.
