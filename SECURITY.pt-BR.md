[English](SECURITY.md) | **Português (Brasil)**

# Política de Segurança

## Versões suportadas

O QuectoERP está em fase de desenho inicial e ainda não tem versão lançada. Até o primeiro lançamento, correções de segurança são aplicadas só na branch `main`. Esta tabela será atualizada quando os lançamentos começarem.

| Versão | Suportada |
| --- | --- |
| `main` | ✅ |

## Como relatar uma vulnerabilidade

**Não relate vulnerabilidades de segurança por issues, discussões ou pull requests públicos.**

Relate de forma privada pelo GitHub: abra a aba **Security** do repositório e clique em **[Report a vulnerability](https://github.com/pedroisoares/quectoerp/security/advisories/new)**.

Inclua, em português ou inglês:

- O tipo de problema (por exemplo injeção de SQL, desvio de autenticação, vazamento de dados entre tenants).
- O componente, arquivo ou endpoint afetado, e a versão ou o commit.
- O passo a passo para reproduzir e, se possível, um código de prova de conceito.
- O impacto, incluindo como um atacante poderia explorar a falha.

## O que esperar

- Confirmamos o recebimento em até **3 dias úteis**.
- Enviamos uma avaliação inicial em até **10 dias úteis**.
- Mantemos você informado enquanto trabalhamos na correção e combinamos uma data de divulgação, normalmente em até **90 dias**.
- Damos o crédito a você no aviso de segurança, a menos que prefira ficar anônimo.

## Escopo

Pontos de atenção especial para um ERP: isolamento entre tenants e empresas, autenticação e autorização, integridade da trilha de auditoria, assinatura de documentos fiscais e certificados digitais, e exposição de dados pessoais protegidos pela LGPD.

Obrigado por ajudar a manter o QuectoERP e quem o usa em segurança.
