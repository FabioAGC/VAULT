#!/usr/bin/env python3
"""Extrai a transcrição de um vídeo (YouTube, Instagram Reels e outros sites do yt-dlp).

1. Tenta a legenda (manual > automática no idioma original).
2. Se não houver, baixa o áudio e transcreve com faster-whisper.
Saída: JSON em stdout. Em caso de erro: {"error": "..."} e exit code 1.

Uso:
  python transcribe.py <url> [--cookies-from-browser chrome] [--whisper-model small] [--force-whisper]
"""
import argparse
import glob
import json
import os
import re
import sys
import tempfile
from collections import deque

import yt_dlp

LANG_PREFS = ["pt", "en"]


def pick_track(tracks, candidates):
    """Escolhe a faixa de legenda pelo idioma (código exato ou variante: pt, pt-BR...)."""
    if not tracks:
        return None
    for cand in candidates:
        for key in tracks:
            if key == cand or key.lower().startswith(cand.lower() + "-"):
                return key
    return None


def pick_auto(tracks, candidates):
    """Legenda automática: prefere a faixa original (-orig) para evitar tradução automática."""
    if not tracks:
        return None
    originals = [k for k in tracks if k.endswith("-orig")]
    if originals:
        return originals[0]
    return pick_track(tracks, candidates)


def vtt_to_text(path):
    """Converte VTT em texto corrido, removendo tempos, tags e linhas repetidas."""
    recent = deque(maxlen=6)
    parts = []
    with open(path, encoding="utf-8", errors="ignore") as f:
        for raw in f:
            line = raw.strip()
            if (
                not line
                or line == "WEBVTT"
                or "-->" in line
                or line.startswith(("Kind:", "Language:", "NOTE", "STYLE"))
                or line.isdigit()
            ):
                continue
            line = re.sub(r"<[^>]+>", "", line).strip()
            if line and line not in recent:
                parts.append(line)
                recent.append(line)
    return " ".join(parts)


def fetch_subtitles(url, lang, automatic, tmp, base_opts):
    opts = dict(
        base_opts,
        skip_download=True,
        writesubtitles=not automatic,
        writeautomaticsub=automatic,
        subtitleslangs=[lang],
        subtitlesformat="vtt",
        outtmpl=os.path.join(tmp, "%(id)s.%(ext)s"),
    )
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])
    files = glob.glob(os.path.join(tmp, "*.vtt"))
    return vtt_to_text(files[0]) if files else None


def transcribe_audio(url, tmp, base_opts, model_size):
    opts = dict(
        base_opts,
        format="bestaudio/best",
        outtmpl=os.path.join(tmp, "%(id)s.%(ext)s"),
        postprocessors=[{"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}],
    )
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])
    files = glob.glob(os.path.join(tmp, "*.mp3"))
    if not files:
        raise RuntimeError("Áudio não encontrado após o download. O FFmpeg está instalado e no PATH?")

    from faster_whisper import WhisperModel  # import tardio: só carrega se precisar

    model = WhisperModel(model_size, device="auto", compute_type="int8")
    segments, info = model.transcribe(files[0], vad_filter=True)
    text = " ".join(s.text.strip() for s in segments)
    return text, info.language


def fmt_date(yyyymmdd):
    if yyyymmdd and len(yyyymmdd) == 8:
        return f"{yyyymmdd[:4]}-{yyyymmdd[4:6]}-{yyyymmdd[6:]}"
    return None


def detect_source(info):
    key = (info.get("extractor_key") or "").lower()
    if "youtube" in key:
        return "youtube"
    if "instagram" in key:
        return "instagram"
    return key or "outro"


def run(args):
    base_opts = {"quiet": True, "no_warnings": True, "noprogress": True}
    if args.cookies_from_browser:
        base_opts["cookiesfrombrowser"] = (args.cookies_from_browser,)

    with yt_dlp.YoutubeDL(base_opts) as ydl:
        info = ydl.extract_info(args.url, download=False)

    # Posts com vários itens (carrossel) chegam como playlist: usa o primeiro vídeo.
    if info.get("_type") == "playlist" and info.get("entries"):
        info = next(e for e in info["entries"] if e)

    url = info.get("webpage_url") or args.url
    language = info.get("language")
    candidates = [c for c in [language] + LANG_PREFS if c]

    transcript, method = None, None
    with tempfile.TemporaryDirectory() as tmp:
        if not args.force_whisper:
            manual = pick_track(info.get("subtitles") or {}, candidates)
            auto = None if manual else pick_auto(info.get("automatic_captions") or {}, candidates)
            track = manual or auto
            if track:
                try:
                    transcript = fetch_subtitles(url, track, bool(auto), tmp, base_opts)
                except Exception as exc:  # cai para o Whisper
                    print(f"aviso: falha ao baixar legenda ({exc})", file=sys.stderr)
                if transcript:
                    method = "subtitles-manual" if manual else "subtitles-auto"
                    language = language or track.split("-")[0]

        if not transcript:
            transcript, whisper_lang = transcribe_audio(url, tmp, base_opts, args.whisper_model)
            method = "whisper"
            language = language or whisper_lang

    return {
        "url": url,
        "id": info.get("id"),
        "source": detect_source(info),
        "title": info.get("title"),
        "author": info.get("uploader") or info.get("channel"),
        "duration_s": info.get("duration"),
        "upload_date": fmt_date(info.get("upload_date")),
        "language": language,
        "method": method,
        "description": (info.get("description") or "")[:1500],
        "transcript": transcript,
    }


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("url")
    ap.add_argument("--cookies-from-browser", help="chrome, edge, firefox...")
    ap.add_argument("--whisper-model", default=os.environ.get("WHISPER_MODEL", "small"))
    ap.add_argument("--force-whisper", action="store_true", help="ignora legendas")
    args = ap.parse_args()

    try:
        result = run(args)
    except Exception as exc:
        print(json.dumps({"error": str(exc), "url": args.url}, ensure_ascii=False))
        sys.exit(1)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
