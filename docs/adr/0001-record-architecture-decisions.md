**English** | [Português (Brasil)](0001-record-architecture-decisions.pt-BR.md)

# ADR-0001: Record architecture decisions

- **Status:** Accepted
- **Date:** 2026-11-16
- **Deciders:** @pedroisoares

## Context

QuectoERP is built by a very small team (one maintainer working with an AI assistant) and is meant to grow through outside contributors. Decisions made in chats, issues or private notes are lost or hard to find, and newcomers end up reopening them. The [roadmap](../../ROADMAP.md) (milestone 0.1) asks for an ADR process before the first line of kernel code, and the [contributing guide](../../CONTRIBUTING.md) already requires an ADR for new dependencies and architecture changes.

## Decision

We will record every significant decision as an Architecture Decision Record in `docs/adr/`, following the lightweight format described by Michael Nygard ("Documenting Architecture Decisions", 2011): context, decision, consequences and alternatives.

- One decision per file, numbered `NNNN-short-title.md`, with a Brazilian Portuguese twin `NNNN-short-title.pt-BR.md`.
- ADRs are proposed and discussed through pull requests, with status *Proposed* while open and *Accepted* when merged.
- Accepted ADRs are immutable. A change of mind is a new ADR that supersedes the old one.
- The process, statuses and template live in [`docs/adr/README.md`](README.md).
- The first ADRs record decisions that were already taken before this process existed: the license (ADR-0002), the clean-room rule (ADR-0003) and the stack (ADR-0004).

## Consequences

- The reason behind each rule is one link away, in both project languages.
- Proposing a large change costs a short document. That is intended: it is cheaper than reverting code.
- Repository tests check that every ADR has both language files and appears in both indexes, so the index cannot silently fall behind.

## Alternatives considered

- **Wiki or discussion forum:** not versioned with the code and not reviewed through pull requests.
- **Heavier templates (for example MADR with all optional sections):** more structure than a two-person team needs today. We can adopt it later through a new ADR.
