---
name: prospector-de-sites
description: Coordena o fluxo completo do Prospector de Sites no Codex. Use quando o usuario quiser configurar o prospector, prospectar leads no Google Maps, redesenhar sites ruins, gerar editor visual/comparador, publicar paginas na HostGator, preparar propostas por e-mail, ou mencionar comandos como setup, prospectar, redesenhar, editor, publicar ou proposta.
---

# Prospector de Sites para Codex

Use esta skill como roteador do ciclo comercial:

1. `setup`: configurar assinatura, prospeccao, envio e HostGator em `prospector-config.json`.
2. `prospectar`: buscar negocios bem avaliados com sites ruins e registrar leads.
3. `redesenhar`: criar paginas premium, editor visual e comparador.
4. `editor`: regenerar a versao editavel de uma pagina.
5. `publicar`: subir paginas na HostGator e verificar URLs.
6. `proposta`: preparar e-mails comerciais para leads publicados.

## Arquivos locais

Trabalhe sempre a partir da pasta do projeto ou da pasta de trabalho indicada pelo usuario:

- `prospector-config.json`: assinatura, preferencias, HostGator e modo de envio. Nunca imprimir a senha.
- `leads.md`: fonte de trabalho e historico dos leads avaliados.
- `leads.csv`: exportacao para planilha. Regenerar quando `leads.md` mudar.
- `sites/[slug]/[slug].html`: pagina final autocontida.
- `sites/[slug]/[slug]-editor.html`: pagina com camada de edicao.
- `comparar.html`: comparador antes/depois.
- `propostas/[slug].eml` ou `propostas/[slug].md`: proposta pronta quando nao houver Gmail automatizado.

## Setup

Para configuracao inicial, leia e siga a skill `setup-prospector`. Ela deve abrir com um formulario guiado, coletar os dados em lote e criar `prospector-config.json`, `leads.md` e `leads.csv`.

A senha nunca deve ser pedida no chat; o campo `hostgator.senha` deve ser criado vazio e preenchido manualmente pelo usuario somente quando for publicar.

## Roteamento

- Para prospeccao, leia a skill `prospeccao-maps`.
- Para setup/configuracao inicial, leia `setup-prospector`.
- Para redesenho ou editor, leia `redesign-premium` e use os scripts `inject-editor.py` e `update-comparator.py` quando disponiveis.
- Para publicacao, leia `deploy-hostgator`.
- Para proposta, leia `proposta-email`.

## Regras operacionais

- Preferir automacao local e navegador disponivel no Codex. Se navegador, Gmail ou Google Sheets nao estiverem acessiveis, continuar com arquivos locais e orientar a acao manual.
- Nunca duplicar lead ja existente em `leads.md`, seja qualificado ou descartado.
- Sempre registrar descartados com motivo, porque isso melhora buscas futuras.
- Atualizar status em `leads.md` no fim de cada etapa: `novo`, `redesenhado`, `publicado`, `proposta enviada`.
- Regenerar `leads.csv` quando o status ou novos leads mudarem; usar `scripts/export-leads-csv.py` quando `leads.md` estiver em tabela Markdown.
- Antes de encerrar qualquer fluxo, informar os arquivos criados/alterados e o proximo passo natural.
