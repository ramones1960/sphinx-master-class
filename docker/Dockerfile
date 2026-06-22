# Sphinx マスタークラス — 開発 / ビルド環境
#
# 含まれるもの:
#   - Python 3.12
#   - Sphinx + 全依存ライブラリ（requirements.txt より）
#   - TeX Live（日本語 PDF ビルド用）
#   - latexmk（LaTeX 自動ビルド）

FROM python:3.12-slim

LABEL org.opencontainers.image.description="Sphinx マスタークラス学習環境"

# TeX Live（日本語 PDF に必要）+ make
RUN apt-get update && apt-get install -y --no-install-recommends \
    make \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-lang-japanese \
    texlive-luatex \
    latexmk \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# 依存を先にコピーしてキャッシュを活用
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ライブリロードサーバー用ポート
EXPOSE 8000
