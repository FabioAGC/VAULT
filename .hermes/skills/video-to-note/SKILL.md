---
name: video-to-note
description: Cria nota no vault a partir de link de YouTube ou Reels
version: 1.0.0
metadata:
  hermes:
    tags: [obsidian, video, ingestao]
    category: obsidian
    requires_toolsets: [terminal]
---
# Video → Nota

## When to Use
O usuário envia uma URL de youtube.com, youtu.be, instagram.com/reel ou instagram.com/p.

## Procedure
1. Na raiz do vault, rodar:
   `python .hermes/skills/video-to-note/scripts/transcribe.py "<url>"`
   A saída é JSON: title, author, source, url, duration_s, upload_date, language, method, description, transcript.
   Se o JSON tiver "error", mostrar ao usuário e parar.
2. Ler a transcrição inteira antes de escrever.
3. Buscar no vault 3–5 notas relacionadas (search_files com 3–5 termos-chave da transcrição) e o MOC mais próximo em 99 - META/MOCs/.
4. Preencher templates/nota-video.md seguindo as regras de Escrita do .hermes.md. Idioma da nota = campo language.
5. Escolher a pasta do tema (ver "Onde salvar notas novas" no .hermes.md). Criar pasta ou subpasta se não existir, sem perguntar. Salvar em `<pasta>/<título curto>.md` (título ≤ 60 caracteres).
6. Adicionar um link para a nota nova no MOC escolhido, no MOC (criar o MOC se não existir).
7. Responder com: caminho da nota (e se criou pasta nova), 1 frase de resumo, notas linkadas.

## Pitfalls
- Nome de arquivo no Windows: remover os caracteres \ / : * ? " < > | do título.
- Reels sem legenda: o script cai para o Whisper; demora mais (1–3 min). Isso é esperado.
- Instagram pedindo login: rodar de novo com `--cookies-from-browser chrome` (ou edge/firefox).
- Erro de extração do yt-dlp: rodar `pip install -U yt-dlp` e tentar de novo.
- Não inventar conteúdo que não está na transcrição. Se a transcrição for ruim, dizer isso na nota.

## Verification
- Frontmatter YAML válido, com tags apenas de 99 - META/tags.md.
- Pelo menos 1 link [[ ]] para MOC e 1 para nota relacionada (se existir alguma).
- Frases dentro dos limites do STE (≤ 30 palavras).
- Nota com a profundidade pedida em "Tamanho e profundidade" do .hermes.md.
- Frontmatter só com `url` e `tags`.
