[English](ROADMAP.md) | **Português (Brasil)**

# Roadmap do QuectoERP

Este é um **documento vivo**. Ele mostra onde o projeto está, o que vem a seguir e o que significa "pronto" em cada etapa. Ele muda conforme aprendemos: fases podem ser divididas, juntadas ou reordenadas, e toda mudança passa por um pull request para que o histórico fique visível.

**Última atualização:** 15/11/2026 · **Fase atual:** 0 (Kernel), marco 0.1 (Fundações)

> [!NOTE]
> Não há datas, de propósito. O QuectoERP é construído por um time muito pequeno, e cada fase só começa quando a anterior cumpre seus critérios de saída. As datas entram quando houver histórico suficiente para estimar com honestidade.

## Como ler este roadmap

| Status | Significado |
| --- | --- |
| **Concluído** | Critérios de saída cumpridos |
| **Em andamento** | O trabalho começou |
| **Próximo** | Começa quando o marco atual terminar |
| **Planejado** | Escopo conhecido, a ordem pode mudar |
| **Ideias** | Vale explorar, sem compromisso |

Dentro de cada marco, `[x]` indica item concluído e `[ ]` item em aberto.

## Regras básicas

1. **Uma fase de cada vez.** Uma fase só começa quando a anterior cumpre os critérios de saída com um usuário real ou de demonstração.
2. **Nenhum recurso do kernel sem um módulo que precise dele.** O kernel cresce porque um módulo pediu, nunca "por via das dúvidas".
3. **Orçamento como teste.** Cada serviço tem metas de tamanho, memória e latência medidas no CI (veja o [README](README.pt-BR.md)). Um marco não está pronto se estourar o orçamento.
4. **Clean-room.** Toda regra de negócio e legal é especificada a partir de fontes públicas (leis, manuais oficiais, padrões públicos), nunca a partir de outro ERP. Veja o [CONTRIBUTING](CONTRIBUTING.pt-BR.md).
5. **Demonstração primeiro.** Enquanto não houver cliente piloto, uma empresa fictícia e um órgão público fictício (dados publicados no repositório) cumprem esse papel e são validados nos ambientes oficiais de teste do governo.

## Visão geral

| Fase | Objetivo | Status |
| --- | --- | --- |
| [0. Kernel](#fase-0--kernel) | A base sobre a qual todo módulo é escrito | **Em andamento** |
| [1. Núcleo empresarial](#fase-1--núcleo-empresarial) | Compra → venda → financeiro → contábil → fiscal, de ponta a ponta | Planejado |
| [2. Comercial e logística](#fase-2--comercial-e-logística) | Vender, comprar e entregar melhor | Planejado |
| [3. Setor público, manufatura e qualidade](#fase-3--setor-público-manufatura-e-qualidade) | Abrir dois mercados novos | Planejado |
| [4. Capital humano](#fase-4--capital-humano) | Folha e eSocial | Planejado |
| [5. Verticais](#fase-5--verticais) | Módulos por segmento | Planejado |

---

## Fase 0 · Kernel

O kernel oferece identidade, multiempresa, metadados, parâmetros, eventos, auditoria, UI shell e o SDK. Ele não sabe nada de estoque ou de folha: regra de negócio fica nos módulos.

### Marco 0.1 · Fundações (Em andamento)

Tudo o que um contribuidor precisa antes da primeira linha de código do kernel.

- [x] Repositório público e licença AGPL-3.0
- [x] Arquivos bilíngues para contribuidores: README, CONTRIBUTING, Código de Conduta, Política de Segurança, modelos de issue e PR
- [x] Roadmap vivo (este arquivo)
- [ ] Identidade visual: logotipo, favicon e paleta de cores, mantidos como arquivos-fonte editáveis
- [ ] Verificação do nome antes do lançamento público: domínios, organização no GitHub, busca de marca (INPI)
- [ ] Processo e modelo de ADR (`docs/adr/`), com os primeiros ADRs registrando as decisões já tomadas: stack, licença, regra clean-room
- [ ] Convenções do repositório para pessoas e assistentes de IA (`CLAUDE.md`)
- [ ] CI mínimo no GitHub Actions: build, testes, checagem de DCO

**Critério de saída:** quem chega consegue ler a documentação, entender as regras do projeto e abrir um pull request que o CI verifica automaticamente.

### Marco 0.2 · Prova de conceito (Próximo)

Uma a duas semanas para confirmar a stack mínima antes de assumir o compromisso.

- [ ] Módulo de exemplo compilado com .NET Native AOT
- [ ] SQL gerado a partir dos metadados, usando Npgsql direto
- [ ] Outbox no PostgreSQL com `LISTEN/NOTIFY`
- [ ] Identidade embutida com OpenIddict
- [ ] Medir os números reais contra o orçamento de recursos
- [ ] **ADR-0001: Orçamento de recursos**, com as metas calibradas pelas medições

**Critério de saída:** as metas do orçamento foram cumpridas ou revisadas com evidência, e as escolhas de stack foram confirmadas ou substituídas por ADRs.

### Marco 0.3 · Kernel 0.1 (Planejado)

| Entra no kernel 0.1 | Fica para quando um módulo precisar |
| --- | --- |
| Identidade, tenant / empresa / filial, permissões | Workflow genérico de aprovação e sagas longas |
| Metadados e gerador (SQL, API, eventos, telas) | BI e base analítica |
| Parâmetros com escopo e vigência | Marketplace de extensões |
| Eventos com outbox no PostgreSQL | Micro-frontends |
| Auditoria a partir dos eventos | Painel de jobs (o 0.1 tem só agendamento simples) |
| UI shell com telas geradas | Idiomas além de pt-BR na interface |
| SDK e CLI `quecto` (scaffold, teste, empacotamento) | Armazenamento S3 (o 0.1 usa disco local atrás de uma interface) |
| OpenTelemetry básico, servidor MCP gerado | Federação com provedores de identidade externos |

**Critérios de saída da Fase 0:**

- Um módulo de exemplo construído só com o SDK, com API, telas, eventos, permissões, auditoria e servidor MCP gerados, e um campo adicionado por extensão de cliente.
- O mesmo build roda em nuvem e on-prem, e a instalação mínima é **um binário + PostgreSQL** dentro do orçamento de recursos.
- Primeira versão pública (0.1.0) com documentação para contribuidores.

---

## Fase 1 · Núcleo empresarial

A primeira "distribuição" sobre o kernel, que o prova em produção com o ciclo de negócio completo.

**Escopo:** cadastros (produtos, parceiros, condições de pagamento, tabelas fiscais como NCM e CFOP), estoque e custos, compras, vendas e faturamento, motor tributário e NF-e, contas a pagar e a receber, tesouraria (CNAB, Pix, conciliação), contabilidade, livros fiscais (SPED).

**Critério de saída:** um mês completo da empresa de demonstração: NF-e autorizada em homologação da SEFAZ, arquivos do SPED validados no PVA, custo médio e balancete conferidos. Ao fim desta fase buscamos o primeiro usuário real.

## Fase 2 · Comercial e logística

**Escopo:** CRM, call center, contratos, pré-faturamento de serviços, licitações (lado da compra, Lei 14.133/2021), gestão de pedidos (OMS), armazém (WMS), transporte (TMS), frete, coleta de dados, ativo fixo, orçamento.

**Critério de saída:** um pedido rastreado de ponta a ponta, da venda à entrega.

## Fase 3 · Setor público, manufatura e qualidade

**Escopo:** contabilidade pública (MCASP/PCASP), execução orçamentária (empenho, liquidação, pagamento), portais de transparência; engenharia de produto, planejamento da produção (MRP), chão de fábrica; qualidade (inspeção, metrologia, documentos, não-conformidades, auditorias, CEP, PPAP).

**Critério de saída:** ciclo orçamentário do órgão de demonstração validado contra o PCASP; MRP gerando ordens de produção.

## Fase 4 · Capital humano

**Escopo:** gestão de pessoal e folha (eSocial), ponto eletrônico, portal do colaborador, cargos e salários, estrutura organizacional, treinamento, recrutamento, avaliação de desempenho, planos de saúde.

**Critério de saída:** três meses de folha de demonstração conferidos e eventos do eSocial aceitos no ambiente de produção restrita.

## Fase 5 · Verticais

**Escopo:** varejo (PDV offline-first com NFC-e), field service, projetos, jurídico, direitos autorais, agronegócio, transporte de passageiros.

**Critério de saída:** uma instalação real por vertical.

---

## Trilhas transversais

Correm em paralelo a todas as fases e são revisadas ao fim de cada marco.

| Trilha | O que cobre |
| --- | --- |
| Reforma Tributária | CBS, IBS e Imposto Seletivo convivem com os tributos atuais até 2033; o motor tributário trata os dois regimes por vigência |
| Regras fiscais abertas | Regras fiscais e legais como dado aberto versionado, com testes, mantidas pela comunidade |
| Orçamento de recursos | Tamanho, memória e latência verificados em todo pull request |
| Segurança e LGPD | Classificação de dados pessoais, criptografia, retenção; divulgação responsável |
| Comunidade | Documentação, rótulos `good first issue`, RFCs públicos para mudanças no kernel |
| Marca | Arquivos da identidade mantidos como fontes editáveis e atualizados conforme o produto evolui |

## Ideias (sem compromisso)

- Contabilidade como livro-razão de eventos, permitindo fechamento contínuo em vez de fechamento mensal.
- Assistente de IA nativo sobre metadados e eventos, sempre com aprovação humana.
- Motor tributário em Rust compilado para WebAssembly, idêntico no servidor, no navegador e no PDV.
- Marketplace de extensões com compatibilidade verificada pelo kernel.

## Como alterar este roadmap

- **Marque o progresso** (`[ ]` → `[x]`) no mesmo pull request que entrega o item.
- **Inclua, remova ou mova escopo** por um pull request que explique o motivo. Mudanças grandes numa fase ou no kernel passam antes por um RFC ou ADR.
- **Atualize a data** no topo e mantenha as duas versões de idioma iguais. Se só puder editar uma, marque a tradução como pendente no PR.
- Quando um marco fica ativo, seus itens viram issues no GitHub, agrupadas num milestone com o mesmo nome.

## Histórico de mudanças

| Data | Mudança |
| --- | --- |
| 15/11/2026 | Primeira versão do roadmap |
