**English** | [Português (Brasil)](ROADMAP.pt-BR.md)

# QuectoERP Roadmap

This is a **living document**. It says where the project is, what comes next and what "done" means for each step. It changes as we learn: phases can be split, merged or reordered, and every change is made through a pull request so the history stays visible.

**Last updated:** 2026-11-16 · **Current phase:** 0 (Kernel), milestone 0.1 (Foundations)

> [!NOTE]
> There are no dates on purpose. QuectoERP is built by a very small team, and each phase starts only when the previous one meets its exit criteria. Dates will be added when there is enough history to estimate honestly.

## How to read this roadmap

| Status | Meaning |
| --- | --- |
| **Done** | Exit criteria met |
| **In progress** | Work has started |
| **Next** | Starts when the current milestone is done |
| **Planned** | Scope is known, order may change |
| **Ideas** | Worth exploring, not committed |

Inside each milestone, `[x]` marks finished items and `[ ]` marks open ones.

## Ground rules

1. **One phase at a time.** A phase starts only when the previous one meets its exit criteria with a real or demonstration user.
2. **No kernel feature without a module that needs it.** The kernel grows because a module asked for it, never "just in case".
3. **Budget as a test.** Every service has size, memory and latency targets measured in CI (see the [README](README.md#initial-resource-budget-per-service)). A milestone is not done if it breaks the budget.
4. **Clean-room.** Every business and legal rule is specified from public sources (laws, official manuals, public standards), never from another ERP. See [CONTRIBUTING](CONTRIBUTING.md).
5. **Demonstration first.** Until there is a pilot customer, a fictional company and a fictional public agency (data published in the repository) play that role and are validated against the official government test environments.

## Overview

| Phase | Goal | Status |
| --- | --- | --- |
| [0. Kernel](#phase-0--kernel) | The base on which every module is written | **In progress** |
| [1. Business core](#phase-1--business-core) | Purchase → sale → finance → accounting → tax, end to end | Planned |
| [2. Commercial and logistics](#phase-2--commercial-and-logistics) | Sell, buy and deliver better | Planned |
| [3. Public sector, manufacturing and quality](#phase-3--public-sector-manufacturing-and-quality) | Open two new markets | Planned |
| [4. Human capital](#phase-4--human-capital) | Payroll and eSocial | Planned |
| [5. Verticals](#phase-5--verticals) | Industry-specific modules | Planned |

---

## Phase 0 · Kernel

The kernel provides identity, multi-company, metadata, parameters, events, auditing, UI shell and the SDK. It knows nothing about inventory or payroll: business rules live in modules.

### Milestone 0.1 · Foundations (In progress)

Everything a contributor needs before the first line of kernel code.

- [x] Public repository and AGPL-3.0 license
- [x] Bilingual contributor files: README, CONTRIBUTING, Code of Conduct, Security policy, issue and PR templates
- [x] Living roadmap (this file)
- [x] Brand identity: logo, favicon and color palette, kept as editable source files
- [ ] Name checks before the public launch: domains, GitHub organization, trademark search (INPI)
- [x] ADR process and template (`docs/adr/`), with the first ADRs recording the decisions already made: stack, license, clean-room rule
- [x] Repository conventions for humans and AI assistants (`CLAUDE.md`)
- [x] Minimal CI on GitHub Actions: build, tests, DCO check

**Exit criteria:** a newcomer can read the docs, understand the project's rules, and open a pull request that CI checks automatically.

### Milestone 0.2 · Proof of concept (Next)

One to two weeks to confirm the minimal stack before committing to it.

- [ ] Sample module compiled with .NET Native AOT
- [ ] SQL generated from metadata, using Npgsql directly
- [ ] Outbox in PostgreSQL with `LISTEN/NOTIFY`
- [ ] Embedded identity with OpenIddict
- [ ] Measure the real numbers against the resource budget
- [ ] **ADR: Resource budget**, with the targets calibrated by the measurements

**Exit criteria:** the budget targets are either met or revised with evidence, and the stack choices are confirmed or replaced through ADRs.

### Milestone 0.3 · Kernel 0.1 (Planned)

| Included in kernel 0.1 | Deferred until a module needs it |
| --- | --- |
| Identity, tenant / company / branch, permissions | Generic approval workflow and long-running sagas |
| Metadata and generator (SQL, API, events, screens) | Analytics and BI |
| Parameters with scope and validity dates | Extension marketplace |
| Events with outbox in PostgreSQL | Micro-frontends |
| Auditing built from events | Job dashboard (0.1 has simple scheduling only) |
| UI shell with generated screens | Languages other than pt-BR in the UI |
| SDK and `quecto` CLI (scaffold, test, package) | S3 storage (0.1 uses local disk behind an interface) |
| Basic OpenTelemetry, generated MCP server | Federation with external identity providers |

**Exit criteria for Phase 0:**

- A sample module built only with the SDK, with generated API, screens, events, permissions, auditing and MCP server, plus one field added by a customer extension.
- The same build runs in the cloud and on-premises, and the minimal install is **one binary + PostgreSQL** within the resource budget.
- First public release (0.1.0) with documentation for contributors.

---

## Phase 1 · Business core

The first "distribution" on top of the kernel, proving it in production with the full business cycle.

**Scope:** master data (products, partners, payment terms, tax tables such as NCM and CFOP), inventory and costing, purchasing, sales and invoicing, tax engine and NF-e (Brazilian electronic invoice), accounts payable and receivable, treasury (CNAB bank files, Pix, reconciliation), accounting, tax books (SPED).

**Exit criteria:** one full month of the demonstration company: NF-e authorized in the SEFAZ test environment, SPED files validated by the official validator (PVA), average cost and trial balance checked. At the end of this phase we look for the first real user.

## Phase 2 · Commercial and logistics

**Scope:** CRM, call center, contracts, service pre-billing, public procurement (buy side, Law 14.133/2021), order management (OMS), warehouse (WMS), transport (TMS), freight, data collection, fixed assets, budgeting.

**Exit criteria:** an order tracked end to end, from sale to delivery.

## Phase 3 · Public sector, manufacturing and quality

**Scope:** public-sector accounting (MCASP/PCASP), budget execution (commitment, settlement, payment), transparency portals; product engineering, production planning (MRP), shop floor; quality (inspection, metrology, documents, non-conformities, audits, SPC, PPAP).

**Exit criteria:** the demonstration agency's budget cycle validated against PCASP; MRP generating production orders.

## Phase 4 · Human capital

**Scope:** personnel management and payroll (eSocial), time tracking, employee portal, positions and salaries, organizational structure, training, recruitment, performance reviews, health plans.

**Exit criteria:** three months of demonstration payroll checked, and eSocial events accepted in the government's restricted production environment.

## Phase 5 · Verticals

**Scope:** retail (offline-first point of sale with NFC-e), field service, projects, legal, copyright management, agribusiness, passenger transport.

**Exit criteria:** one real installation per vertical.

---

## Cross-cutting tracks

These run alongside every phase and are reviewed at the end of each milestone.

| Track | What it covers |
| --- | --- |
| Tax reform | CBS, IBS and the Selective Tax coexist with the current taxes through 2033; the tax engine handles both regimes by validity date |
| Open tax rules | Tax and legal rules as versioned open data, with tests, maintained by the community |
| Resource budget | Size, memory and latency checked on every pull request |
| Security and LGPD | Personal data classification, encryption, retention; responsible disclosure |
| Community | Docs, `good first issue` labels, public RFCs for kernel changes |
| Brand | Identity assets kept as editable sources and updated as the product evolves |

## Ideas (not committed)

- Accounting as an event ledger, enabling continuous close instead of month-end close.
- Native AI assistant over metadata and events, always with human approval.
- Tax engine in Rust compiled to WebAssembly, identical on server, browser and point of sale.
- Extension marketplace with compatibility checked by the kernel.

## How to change this roadmap

- **Mark progress** (`[ ]` → `[x]`) in the same pull request that delivers the item.
- **Add, remove or move scope** through a pull request that explains why. Large changes to a phase or to the kernel go through an RFC or ADR first.
- **Update the date** at the top and keep both language versions in sync. If you can only edit one, mark the translation as pending in the PR.
- When a milestone becomes active, its items are opened as GitHub issues and grouped in a milestone with the same name.

## Change log

| Date | Change |
| --- | --- |
| 2026-11-15 | First version of the roadmap |
| 2026-11-16 | Milestone 0.1: brand identity, ADR process with ADRs 0001 to 0004, `CLAUDE.md` and CI delivered. The resource budget ADR no longer has a fixed number, because 0001 to 0004 are taken |
