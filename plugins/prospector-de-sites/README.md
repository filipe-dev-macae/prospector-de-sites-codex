# Prospector de Sites

Plugin para Codex que apoia prospeccao semi-automatica de clientes com sites ruins.

## Ciclo

1. `setup`: cria `prospector-config.json` com assinatura, nichos, cidade, envio e HostGator.
2. `prospectar`: qualifica negocios do Google Maps e salva `leads.md` + `leads.csv`.
3. `redesenhar`: recria paginas dos melhores leads e gera editor visual + comparador.
4. `editor`: regenera a versao editavel de uma pagina.
5. `publicar`: envia paginas para `public_html/[pastaBase]/[slug]/index.html`.
6. `proposta`: prepara e-mails comerciais em `propostas/` e ajuda a criar rascunhos quando houver navegador/Gmail disponivel.

## Skills

- `$setup-prospector`: configuracao inicial.
- `$prospector-de-sites`: coordenadora do fluxo.
- `$prospeccao-maps`: prospeccao e qualificacao.
- `$redesign-premium`: redesign, editor e comparador.
- `$deploy-hostgator`: publicacao.
- `$proposta-email`: proposta comercial.

## Arquivos gerados

Tudo fica na pasta de trabalho:

- `prospector-config.json`: preferencias e credenciais locais.
- `leads.md`: pipeline principal.
- `leads.csv`: exportacao para planilha.
- `sites/[slug]/`: paginas de cada cliente.
- `comparar.html`: antes/depois.
- `propostas/`: e-mails prontos.

Seguranca: a senha do cPanel/FTP fica apenas em `prospector-config.json` no computador do usuario e nunca deve aparecer no chat ou em logs.

No primeiro uso, `$setup-prospector` deve abrir com um formulario guiado no chat, aplicar defaults seguros e criar os arquivos locais iniciais.
