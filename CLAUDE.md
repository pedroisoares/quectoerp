# CLAUDE.md

Conventions for anyone, human or AI assistant, who changes this repository. Read it before the first change in a session. The human-facing versions of these rules live in [CONTRIBUTING.md](CONTRIBUTING.md), and the reasons behind them in [docs/adr/](docs/adr/README.md). If this file and those disagree, they win; fix this file in the same pull request.

## What this project is

QuectoERP is an open source ERP built as a small kernel (identity, multi-company, metadata, parameters, events, audit, UI shell, SDK) plus pluggable business modules. Every service has a measured resource budget, and the minimal install is one binary plus PostgreSQL. See [README.md](README.md) and [ROADMAP.md](ROADMAP.md) for where the project stands.

Current phase: **0 (Kernel)**. There is no kernel code yet; check the roadmap for the active milestone before proposing work.

## Rules that are never bent

1. **Clean-room** ([ADR-0003](docs/adr/0003-clean-room-development.md)). Never write code, schemas, table or field names, screen layouts or text copied or derived from another ERP. Legal and tax rules come only from public sources (laws, official manuals, public standards), and every specification records its source. Never add legacy material to the repository, issues, tests or fixtures. If a request would need proprietary material, stop and say so.
2. **No runtime reflection in services** ([ADR-0004](docs/adr/0004-technology-stack.md)). Everything must work under .NET Native AOT: use source generators, `System.Text.Json` source generation and generated SQL with Npgsql. No EF Core at runtime.
3. **Every new runtime dependency needs an ADR** that states its cost in size, memory and operations, and which module needs it. Test-only packages do not. NuGet versions live only in `Directory.Packages.props`.
4. **No kernel feature without a module that needs it** (roadmap, ground rule 2).
5. **Resource budget is a test.** A regression above 10% against `main` in binary size, memory, startup or latency needs a justification in the pull request.
6. **Each module owns its PostgreSQL schema.** Modules talk through APIs and events, never through each other's tables.

## Languages

- Code, identifiers, code comments and commit messages: **English**.
- Brazilian legal terms keep their original name (NF-e, SPED, eSocial, CFOP) with a short English explanation the first time they appear.
- User-facing documentation is bilingual: `NAME.md` (English) and `NAME.pt-BR.md` (Brazilian Portuguese), each linking to the other on the first line, exactly as the existing files do. Change both in the same pull request, or mark the translation as pending. The repository tests enforce the pairing and the first line.
- This file and everything under `.github/` are single-language.
- The maintainer prefers to be addressed in **Brazilian Portuguese** in conversations, issues and pull request descriptions.

## Repository layout

| Path | Contents |
| --- | --- |
| `docs/adr/` | Architecture Decision Records, index and template |
| `brand/` | Logo, favicon and color tokens, all generated from `brand/brand.json` |
| `tests/QuectoERP.Repository.Tests/` | Tests for repository conventions (bilingual docs, links, ADRs, roadmap) |
| `.github/` | Issue and PR templates, CODEOWNERS, CI workflow and scripts |
| `QuectoERP.slnx` | The solution; add every new project to it |
| `global.json`, `Directory.Build.props`, `Directory.Packages.props`, `.editorconfig` | SDK pin and shared build, package and style settings |

Expected later: `src/` for the kernel, SDK and modules, and `tests/` next to them.

## Commands

```bash
dotnet restore
dotnet format --verify-no-changes   # style check, as in CI; drop the flag to fix
dotnet build --configuration Release
dotnet test --configuration Release
python3 brand/scripts/build.py      # after any change to brand/brand.json
.github/scripts/check-dco.sh origin/main HEAD
```

Warnings are errors. The SDK is .NET 10, pinned in `global.json`, and tests run on Microsoft.Testing.Platform with xUnit v3.

## Workflow

- Branch from `main`: `feat/…`, `fix/…`, `docs/…`.
- Small, focused commits in [Conventional Commits](https://www.conventionalcommits.org/) format, for example `feat(kernel): add tenant resolver`, `docs(adr): add ADR-0005`.
- **Sign off every commit** with `git commit -s`. The sign-off must match the commit author; CI checks it.
- Pull requests follow `.github/PULL_REQUEST_TEMPLATE.md`, are squash-merged with the PR title, and need CI green plus a maintainer's approval.
- When a pull request delivers a roadmap item, tick it (`[ ]` to `[x]`) in both `ROADMAP.md` and `ROADMAP.pt-BR.md`, update the "last updated" date in both, and add a line to the change history.
- New ADR: copy `docs/adr/template.md` and `template.pt-BR.md`, take the next number, add it to both indexes. Accepted ADRs are never rewritten; supersede them.

## Before you say a change is done

- `dotnet format --verify-no-changes`, `dotnet build` and `dotnet test` pass locally.
- Both language versions of every changed document are updated.
- No proprietary or legacy material entered the diff.
