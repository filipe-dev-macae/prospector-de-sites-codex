---
name: deploy-hostgator
description: Publica paginas do Prospector de Sites na HostGator. Use quando o usuario quiser subir site, publicar pagina, fazer deploy, testar FTP/cPanel, verificar URL publica ou configurar publicacao HostGator.
---

# Deploy na HostGator

Publicar cada pagina em `public_html/[pastaBase]/[slug]/index.html`, acessivel por `https://[dominio]/[pastaBase]/[slug]/`.

## Credenciais

Ler de `prospector-config.json`:

- `hostgator.usuario`
- `hostgator.dominio`
- `hostgator.servidor`
- `hostgator.senha`
- `hostgator.pastaBase`

Se usuario, dominio ou servidor faltarem, pedir ao usuario. Se a senha faltar, nunca pedir no chat: orientar o usuario a preencher `"senha"` diretamente no arquivo local. Nunca imprimir senha, comando completo com senha ou logs que possam expor credenciais.

## Metodo 1: FTP programatico

Tentar primeiro com `ftp.[dominio]` e depois com o servidor do config:

```bash
curl -sS --ftp-create-dirs -T index.html \
  "ftp://ftp.DOMINIO/public_html/clientes/SLUG/index.html" \
  --user "USUARIO:SENHA"
```

Ao executar de verdade, montar as credenciais dentro do processo e mascarar saidas. Enviar `sites/[slug]/[slug].html` como `index.html`.

## Metodo 2: cPanel UAPI

Se FTP falhar e o servidor aceitar cPanel:

```bash
curl -sS -u "USUARIO:SENHA" \
  "https://SERVIDOR:2083/execute/Fileman/upload_files" \
  -F "dir=/public_html/clientes/SLUG" -F "file-1=@index.html"
```

Criar a pasta antes se necessario com a API de `mkdir`.

## Metodo 3: navegador assistido

Se a rede local ou sandbox bloquear FTP/HTTPS:

1. Abrir `https://SERVIDOR:2083` no navegador disponivel.
2. Pedir que o usuario faca login se necessario.
3. Abrir Gerenciador de Arquivos.
4. Criar `public_html/[pastaBase]/[slug]/`.
5. Fazer upload do HTML final como `index.html`.

## Verificacao

Sempre abrir ou requisitar `https://[dominio]/[pastaBase]/[slug]/` e confirmar:

- HTTP 200 quando for possivel checar;
- titulo/nome do cliente presente;
- pagina correta, sem indice de diretorio ou 404.

Se falhar, diagnosticar caminho, permissao, host FTP, propagacao DNS e nome do arquivo.

## Atualizacao local

Depois de publicar:

- atualizar `leads.md` com status `publicado`;
- preencher URL nova;
- regenerar `leads.csv`;
- listar as URLs publicas ao usuario.
