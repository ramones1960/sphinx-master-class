# PDF ビルド（LaTeX 経由）

Sphinx の PDF 出力は **LaTeX を経由**します。フローは:

```{mermaid}
flowchart LR
    A[".rst/.md"] --> B{{sphinx-build}}
    B --> C[".tex ファイル"]
    C --> D{{uplatex/xelatex}}
    D --> E[".dvi/.pdf"]
    E --> F{{dvipdfmx}} --> G["PDF"]
```

## TeX Live のインストール

**Docker を使う場合はコンテナ内に含まれているため不要**です。

```bash
# Debian/Ubuntu
sudo apt-get install -y \
  texlive-latex-recommended texlive-latex-extra \
  texlive-fonts-recommended texlive-lang-japanese latexmk

# macOS (Homebrew)
brew install --cask mactex
```

## ビルドコマンド

```bash
# latexmk に任せる（推奨）: .tex 生成 → uplatex ・ dvipdfmx を自動実行
sphinx-build -M latexpdf docs/source docs/build
# PDF: docs/build/latex/sphinx-master-class.pdf

# Makefile 経由
make pdf
# または Docker 経由
make docker-pdf
```

## conf.py の日本語 PDF 設定

```python
latex_engine = "uplatex"   # 日本語の定番

latex_documents = [
    ("index", "my-docs.tex", "文書タイトル", "著者名", "manual"),
]

latex_elements = {
    "papersize": "a4paper",
    "pointsize": "11pt",
    # プリアンブルでフォント・ヘッダー/フッターをカスタマイズ
    "preamble": r"""
\usepackage{fancyhdr}
\usepackage{lastpage}
""",
}
```

## 表紙・目次・ヘッダーのカスタマイズ

`conf.py` の `latex_elements` で LaTeX マクロを直接指定します。
実例はこのプロジェクトの `docs/source/conf.py` を参照してください。

```python
latex_elements = {
    # 表紙（maketitle を完全制御）
    "maketitle": r"""
\begin{titlepage}
  \centering
  {\Huge\bfseries タイトル\par}
  \vfill
  {\large \today\par}
\end{titlepage}
""",
    # 目次（ページ番号をローマ数字に）
    "tableofcontents": r"""
\clearpage
\pagenumbering{roman}
\sphinxtableofcontents
\clearpage
\pagenumbering{arabic}
""",
}
```

## トラブルシューティング

```bash
# .tex のみ生成（デバッグ用）
sphinx-build -b latex docs/source docs/build/latex

# 手動ビルド
cd docs/build/latex
uplatex sphinx-master-class.tex
dvipdfmx sphinx-master-class.dvi
```

## 演習

:::{exercise} 演習 5-2: PDF をビルドする

1. Docker またはローカル TeX Live で `make pdf` / `make docker-pdf` を実行する
2. `docs/build/latex/sphinx-master-class.pdf` を開き、表紙・目次・本文を確認する
3. `conf.py` の `latex_elements["maketitle"]` を編集して表紙をカスタマイズする
:::
