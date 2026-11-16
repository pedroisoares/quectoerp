[English](README.md) | **Português (Brasil)**

# Registros de Decisão de Arquitetura

Um Registro de Decisão de Arquitetura (ADR, do inglês *Architecture Decision Record*) é um documento curto que registra uma decisão importante, o contexto que levou a ela e as suas consequências. Os ADRs são a memória do QuectoERP sobre o *porquê* das coisas, para que quem chega não precise adivinhar e debates antigos não precisem ser repetidos.

## Quando escrever um ADR

Escreva um ADR antes (ou no mesmo pull request) de uma mudança que:

- acrescente uma dependência de execução: biblioteca, contêiner ou serviço de infraestrutura. O ADR informa quanto ela custa em tamanho, memória e operação, e qual módulo precisa dela;
- altere o contrato público entre módulos (APIs, eventos, formato dos metadados);
- altere a stack, a licença, as regras de contribuição ou o orçamento de recursos;
- seja difícil de desfazer, ou sobre a qual alguém provavelmente vai perguntar "por que fizemos isso?" daqui a um ano.

Escolhas pequenas, locais e fáceis de desfazer não precisam de ADR. Na dúvida, abra uma issue e pergunte.

## Como propor um ADR

1. Copie o [`template.pt-BR.md`](template.pt-BR.md) (e o [`template.md`](template.md)) para `NNNN-titulo-curto.pt-BR.md` e `NNNN-titulo-curto.md`, usando o próximo número livre. Números nunca são reaproveitados. O nome do arquivo fica em inglês, igual nos dois idiomas.
2. Preencha com o status **Proposto**. Seja breve: uma decisão por ADR, mais ou menos uma página.
3. Inclua o ADR no índice abaixo, nos dois idiomas, e abra um pull request. A discussão acontece no pull request.
4. Quando o pull request for aprovado, mude o status para **Aceito** antes do merge.

ADRs aceitos não são reescritos. Para mudar uma decisão, escreva um ADR novo que **substitui** o antigo, e no antigo altere apenas a linha de status (`Substituído pelo ADR-NNNN`). Erros de digitação e links quebrados podem ser corrigidos a qualquer momento.

Como toda documentação para usuários, um ADR tem um arquivo em inglês e outro em português do Brasil. Se você só puder escrever em um idioma, abra o pull request mesmo assim e marque a tradução como pendente.

## Status

| Status | Significado |
| --- | --- |
| Proposto | Em discussão num pull request aberto |
| Aceito | Em vigor |
| Rejeitado | Discutido e recusado; mantido como registro |
| Obsoleto | Deixou de valer e nada o substitui |
| Substituído pelo ADR-NNNN | Trocado por uma decisão mais nova |

## Índice

| ADR | Título | Status |
| --- | --- | --- |
| [0001](0001-record-architecture-decisions.pt-BR.md) | Registrar as decisões de arquitetura | Aceito |
| [0002](0002-license-agpl-and-dco.pt-BR.md) | Licença AGPL-3.0 e assinatura DCO | Aceito |
| [0003](0003-clean-room-development.pt-BR.md) | Desenvolvimento clean-room | Aceito |
| [0004](0004-technology-stack.pt-BR.md) | Stack tecnológica | Aceito |
