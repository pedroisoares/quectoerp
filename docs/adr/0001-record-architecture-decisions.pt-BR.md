[English](0001-record-architecture-decisions.md) | **Português (Brasil)**

# ADR-0001: Registrar as decisões de arquitetura

- **Status:** Aceito
- **Data:** 16/11/2026
- **Decisores:** @pedroisoares

## Contexto

O QuectoERP é construído por um time muito pequeno (um mantenedor trabalhando com um assistente de IA) e pretende crescer com contribuidores de fora. Decisões tomadas em conversas, issues ou anotações privadas se perdem ou ficam difíceis de achar, e quem chega acaba reabrindo os mesmos debates. O [roadmap](../../ROADMAP.pt-BR.md) (marco 0.1) pede um processo de ADR antes da primeira linha de código do kernel, e o [guia de contribuição](../../CONTRIBUTING.pt-BR.md) já exige ADR para dependências novas e mudanças de arquitetura.

## Decisão

Vamos registrar toda decisão importante como um Registro de Decisão de Arquitetura em `docs/adr/`, no formato leve descrito por Michael Nygard ("Documenting Architecture Decisions", 2011): contexto, decisão, consequências e alternativas.

- Uma decisão por arquivo, numerado `NNNN-titulo-curto.md`, com o par em português do Brasil `NNNN-titulo-curto.pt-BR.md`.
- ADRs são propostos e discutidos em pull requests, com status *Proposto* enquanto abertos e *Aceito* no merge.
- ADRs aceitos não mudam. Mudar de ideia significa escrever um ADR novo que substitui o antigo.
- O processo, os status e o modelo ficam no [`docs/adr/README.pt-BR.md`](README.pt-BR.md).
- Os primeiros ADRs registram decisões tomadas antes de este processo existir: a licença (ADR-0002), a regra clean-room (ADR-0003) e a stack (ADR-0004).

## Consequências

- O motivo de cada regra fica a um link de distância, nos dois idiomas do projeto.
- Propor uma mudança grande custa um documento curto. É de propósito: sai mais barato que reverter código.
- Testes do repositório verificam que todo ADR tem os dois arquivos de idioma e aparece nos dois índices, para que o índice não fique desatualizado sem ninguém perceber.

## Alternativas consideradas

- **Wiki ou fórum de discussão:** não fica versionado com o código nem passa por revisão em pull request.
- **Modelos mais pesados (por exemplo, MADR com todas as seções opcionais):** mais estrutura do que um time de duas pessoas precisa hoje. Pode ser adotado depois, por um novo ADR.
