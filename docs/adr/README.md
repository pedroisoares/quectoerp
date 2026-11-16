**English** | [Português (Brasil)](README.pt-BR.md)

# Architecture Decision Records

An Architecture Decision Record (ADR) is a short document that captures one significant decision, the context that led to it and its consequences. ADRs are how QuectoERP remembers *why* things are the way they are, so newcomers do not have to guess and old debates do not have to be repeated.

## When to write an ADR

Write an ADR before (or in the same pull request as) a change that:

- adds a runtime dependency: a library, a container or an infrastructure service. The ADR states what it costs in size, memory and operations, and which module needs it;
- changes the public contract between modules (APIs, events, metadata format);
- changes the stack, the license, the contribution rules or the resource budget;
- is hard to reverse, or that someone will probably ask "why did we do this?" about a year from now.

Small, local, easily reversible choices do not need an ADR. If in doubt, open an issue and ask.

## How to propose one

1. Copy [`template.md`](template.md) (and [`template.pt-BR.md`](template.pt-BR.md)) to `NNNN-short-title.md` and `NNNN-short-title.pt-BR.md`, using the next free number. Numbers are never reused.
2. Fill it in with status **Proposed**. Keep it short: one decision per ADR, about one page.
3. Add it to the index below in both languages and open a pull request. Discussion happens in the pull request.
4. When the pull request is approved, change the status to **Accepted** before merging.

Accepted ADRs are not rewritten. To change a decision, write a new ADR that **supersedes** the old one, and update only the old one's status line (`Superseded by ADR-NNNN`). Typos and broken links can be fixed at any time.

As with all user-facing documentation, an ADR has an English file and a Brazilian Portuguese file. If you can only write one language, open the pull request anyway and mark the translation as pending.

## Statuses

| Status | Meaning |
| --- | --- |
| Proposed | Under discussion in an open pull request |
| Accepted | In force |
| Rejected | Discussed and declined; kept for the record |
| Deprecated | No longer relevant, nothing replaces it |
| Superseded by ADR-NNNN | Replaced by a newer decision |

## Index

| ADR | Title | Status |
| --- | --- | --- |
| [0001](0001-record-architecture-decisions.md) | Record architecture decisions | Accepted |
| [0002](0002-license-agpl-and-dco.md) | AGPL-3.0 license and DCO sign-off | Accepted |
| [0003](0003-clean-room-development.md) | Clean-room development | Accepted |
| [0004](0004-technology-stack.md) | Technology stack | Accepted |
