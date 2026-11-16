[English](0003-clean-room-development.md) | **Português (Brasil)**

# ADR-0003: Desenvolvimento clean-room

- **Status:** Aceito
- **Data:** 16/11/2026
- **Decisores:** @pedroisoares

## Contexto

Quem inicia o QuectoERP conhece bem ERPs comerciais existentes, e o mercado brasileiro de ERP tem fornecedores estabelecidos que protegem os seus sistemas. Ideias, processos de negócio e regras legais não são protegidos por direito autoral, mas código-fonte, estruturas de banco, nomes, leiautes de tela e documentação podem ser. Uma disputa sobre material copiado poderia parar o projeto ou expor quem o usa.

## Decisão

O QuectoERP é escrito do zero sob uma regra clean-room. A regra, publicada no [guia de contribuição](../../CONTRIBUTING.pt-BR.md#regra-clean-room-obrigatória), é:

1. Nada de código, estruturas de banco, nomes de tabelas ou campos, leiautes de tela ou documentação copiados ou derivados de outros ERPs, proprietários ou open source com licença incompatível.
2. Quem já trabalhou com o código-fonte ou o dicionário de dados de outro ERP ainda pode ajudar escrevendo *requisitos funcionais com as próprias palavras*, baseados em processos de negócio e na legislação. Essa pessoa nunca cola nem parafraseia material proprietário.
3. O modelo de dados nasce do domínio (DDD), com vocabulário próprio. Nada de prefixos, códigos de rotina ou nomes de parâmetro herdados.
4. **Fontes públicas são a referência** para regras legais e fiscais: leis, manuais oficiais (NF-e, SPED, eSocial), normas de contabilidade pública (MCASP/PCASP), leiautes CNAB da Febraban e similares.
5. **Rastreabilidade.** Toda especificação registra a sua fonte (lei, manual, entrevista, observação de processo). Esse registro é a nossa defesa se a origem de uma regra for questionada.
6. **Material legado nunca entra no repositório**: nem em código, issues, testes, dados de teste ou exemplos.
7. Nenhuma marca de terceiros em nomes de módulos, telas ou documentação.
8. Há revisão jurídica antes da primeira versão pública (0.1.0) e antes de qualquer oferta comercial.

Pull requests que descumprirem a regra são fechados.

## Consequências

- A especificação fica mais lenta: os requisitos são reescritos a partir de fontes públicas, em vez de copiados de um sistema existente.
- Cada módulo precisa de uma lista de fontes junto da especificação, e quem revisa confere essa lista (o modelo de pull request já pede isso).
- Qualquer pessoa pode usar, fazer fork e vender o projeto sem herdar risco jurídico de outro fornecedor.
- Os dados de demonstração (uma empresa fictícia e um órgão público fictício) também precisam ser originais.

## Alternativas consideradas

- **Portar ou traduzir um ERP open source existente:** começo mais rápido, mas prende a arquitetura ao desenho de outra pessoa e pode trazer incompatibilidade de licença.
- **Orientação informal do tipo "só não copie":** difícil de fiscalizar e difícil de defender sem rastreabilidade.
