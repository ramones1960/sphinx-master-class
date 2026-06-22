# Sphinx マスタークラス — 開発 / ビルド環境
#
# 含まれるもの:
#   - Python 3.12
#   - Sphinx + 全依存ライブラリ（requirements.txt より）
#   - TeX Live（日本語 PDF ビルド用）
#   - latexmk（LaTeX 自動ビルド）
#   - Node.js + Chromium + mermaid-cli（PDF/ePub 用に Mermaid 図を画像化）

FROM python:3.12-slim

LABEL org.opencontainers.image.description="Sphinx マスタークラス学習環境"

# プロキシ設定（環境変数 HTTP_PROXY / HTTPS_PROXY / NO_PROXY から取得）
ARG HTTP_PROXY
ARG HTTPS_PROXY
ARG NO_PROXY
ENV HTTP_PROXY=${HTTP_PROXY} \
    HTTPS_PROXY=${HTTPS_PROXY} \
    NO_PROXY=${NO_PROXY} \
    http_proxy=${HTTP_PROXY} \
    https_proxy=${HTTPS_PROXY} \
    no_proxy=${NO_PROXY}

# システム依存:
#   - make                  : Makefile のビルドターゲット用
#   - TeX Live 一式          : 日本語 PDF ビルド（uplatex + dvipdfmx）
#   - tex-gyre               : Sphinx が標準で読み込む tgtermes / tgheros
#                              （TeX Gyre フォント）の .sty を提供する。
#                              これが無いと PDF ビルドが「tgtermes.sty が
#                              見つからない」というエラーで失敗する。
#   - nodejs / npm / chromium: Mermaid 図を PDF/ePub 用に画像化する
#                              mermaid-cli (mmdc) の実行に必要
#   - fonts-noto-cjk         : Mermaid 図中の日本語を描画するためのフォント
RUN apt-get update && apt-get install -y --no-install-recommends \
    make \
    nodejs \
    npm \
    chromium \
    fonts-noto-cjk \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-recommended \
    tex-gyre \
    texlive-lang-japanese \
    texlive-luatex \
    latexmk \
    && rm -rf /var/lib/apt/lists/*

# mermaid-cli (mmdc) をインストール。Puppeteer には同梱 Chromium を
# ダウンロードさせず、上で apt 導入したシステムの Chromium を使わせる。
ENV PUPPETEER_SKIP_DOWNLOAD=true \
    PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \
    PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium
RUN npm install -g @mermaid-js/mermaid-cli

WORKDIR /workspace

# 依存を先にコピーしてキャッシュを活用
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ライブリロードサーバー用ポート
EXPOSE 8000
