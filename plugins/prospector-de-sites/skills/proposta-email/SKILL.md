---
name: proposta-email
description: Escreve propostas comerciais por e-mail para leads do Prospector de Sites. Use quando o usuario quiser preparar, revisar, criar rascunho ou enviar proposta para um lead publicado, com rapport real, link da pagina nova e sem preco no primeiro contato.
---

# Proposta por e-mail

Objetivo: fazer o cliente abrir o link da pagina nova. A venda acontece na resposta, nao no primeiro e-mail.

## Regras

1. Sem preco no primeiro e-mail.
2. Abrir com rapport real: nota no Google, quantidade de avaliacoes, credencial ou detalhe publico verificavel.
3. Citar o problema do site atual com delicadeza e de forma objetiva.
4. Apresentar a nova versao ja publicada como demonstracao concreta.
5. Pedir apenas que a pessoa abra no celular e responda com a impressao.
6. Manter entre 120 e 180 palavras.

## Entrada

Ler `prospector-config.json` e `leads.md`. Selecionar leads com:

- status `publicado`;
- e-mail confirmado;
- URL nova preenchida;
- proposta ainda nao enviada.

Para leads sem e-mail, preparar uma versao curta para WhatsApp.

## Estrutura

- Assunto especifico, sem cara de disparo em massa.
- Paragrafo 1: apresentacao breve + elogio verificavel.
- Paragrafo 2: oportunidade percebida no site atual.
- Paragrafo 3: link da nova pagina publicada e, se util, link antigo para comparacao.
- Paragrafo 4: CTA leve para abrir e responder.
- Assinatura com nome, apresentacao e WhatsApp do config.

## Saida Codex-first

- Criar `propostas/[slug].md` com assunto, destinatario e corpo.
- Quando fizer sentido, criar tambem `propostas/[slug].eml` para abrir em cliente de e-mail.
- Se navegador/Gmail estiver disponivel e o usuario pedir, ajudar a criar rascunho no Gmail web.
- Se nao houver Gmail automatizado, entregar o arquivo local pronto para copiar.
- Salvar screenshot da dobra inicial em `sites/[slug]/preview.png` quando houver navegador ou ferramenta de captura disponivel. Se nao houver, orientar anexar manualmente depois.
- Atualizar `leads.md` para `proposta enviada` somente quando o rascunho/envio for confirmado pelo usuario ou executado pelo Codex.

## Follow-up

Sugerir um unico follow-up educado apos 3 ou 4 dias uteis sem resposta: perguntar se conseguiu ver a pagina e reforcar que a nova versao e apenas uma proposta visual.
