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
  texlive-fonts-recommended tex-gyre \
  texlive-lang-japanese latexmk

# macOS (Homebrew)
brew install --cask mactex
```

:::{important}
`tex-gyre` パッケージを忘れないでください。Sphinx の LaTeX 出力は標準で
`tgtermes` / `tgheros`（TeX Gyre フォント）を読み込みます。これが無いと
**`tgtermes.sty が見つからない`** というエラーで PDF ビルドが失敗します。
:::

:::{note}
**Mermaid 図を PDF に含める場合**は、図を画像化する
[mermaid-cli](https://github.com/mermaid-js/mermaid-cli)（`mmdc` コマンド）が
別途必要です（Node.js + Chromium を使用）。
未インストールの場合、ビルドは成功しますが図は省略され、
`command 'mmdc' cannot be run` という警告が出ます。
**Docker 環境にはこれらがすべて同梱されている**ため、`make docker-pdf` なら
追加設定なしで図入りの PDF が生成できます。
:::

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

## conf.py の基本設定

### エンジンと文書定義

```python
# 日本語 PDF には uplatex（jsbook クラス）が最も実績のある組み合わせ
latex_engine = "uplatex"

latex_documents = [
    # (スタート文書, 出力ファイル名, タイトル, 著者, ドキュメントクラス)
    ("index", "my-docs.tex", "文書タイトル", "著者名", "manual"),
]
```

`"manual"` は書籍スタイル（章・節構成）、`"howto"` は短い技術文書向けです。

### `latex_elements` の主要キー

`latex_elements` 辞書で LaTeX コードを直接注入します。

| キー | 役割 | 典型的な値 |
|---|---|---|
| `papersize` | 用紙サイズ | `"a4paper"`, `"letterpaper"` |
| `pointsize` | 基本フォントサイズ | `"10pt"`, `"11pt"`, `"12pt"` |
| `preamble` | LaTeX プリアンブルへの追加コード | `\usepackage{...}` など |
| `maketitle` | 表紙の LaTeX コード | `\begin{titlepage}...\end{titlepage}` |
| `tableofcontents` | 目次の LaTeX コード | `\sphinxtableofcontents` を含む |
| `atendofbody` | 本文末尾への追加コード | 付録コマンドなど |

```python
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

## 表紙のカスタマイズ

`maketitle` キーで表紙全体を LaTeX で制御します。

```python
latex_elements = {
    "maketitle": r"""
\begin{titlepage}
  \centering
  \vspace*{2cm}
  {\Huge\bfseries タイトル\par}
  \vspace{0.5cm}
  {\Large サブタイトル\par}
  \vspace{1.5cm}
  \rule{\linewidth}{0.4pt}\par
  \vfill
  {\large \today\par}
\end{titlepage}
""",
}
```

## 目次と前付け・本文のページ番号

技術文書では「前付け（目次まで）はローマ数字、本文はアラビア数字」が一般的です。
`jsbook` クラスの `\frontmatter` / `\mainmatter` を使うと、ルートドキュメント（序文・
はじめに）を **番号なし章** として扱い、以降の章を 1 から正しく番号付けできます。

```python
latex_elements = {
    # 目次を \frontmatter（ローマ数字・章番号なし）の中に収める
    "tableofcontents": r"""
\frontmatter
\pagestyle{normal}
\clearpage
\sphinxtableofcontents
\clearpage
""",
}
```

そしてルートドキュメント（`index.md` や `index.rst`）の末尾に
`\mainmatter` を挿入して本文（番号付き章）へ切り替えます。

````markdown
```{raw} latex
\mainmatter
\pagestyle{normal}
```
````

こうすることで、序章（ルート文書）は章番号が付かず、
第1章から正しく番号付けが始まります。

:::{tip}
このプロジェクト自体がこのパターンを採用しています。
`docs/source/conf.py` と `docs/source/index.md` の末尾を参照してください。
:::

## ヘッダー・フッターのカスタマイズ

`fancyhdr` パッケージを使うとヘッダー・フッターを自由に制御できます。

```python
latex_elements = {
    "preamble": r"""
\usepackage{lastpage}
\usepackage{fancyhdr}

% 本文ページスタイル
\fancypagestyle{normal}{%
  \fancyhf{}%
  \fancyhead[L]{\small\nouppercase{\leftmark}}%   左ヘッダー: 章タイトル
  \fancyhead[R]{\small 文書タイトル}%              右ヘッダー: 固定テキスト
  \fancyfoot[C]{\small \thepage\ /\ \pageref{LastPage}}%  中央フッター: ページ番号
  \renewcommand{\headrulewidth}{0.4pt}%
  \renewcommand{\footrulewidth}{0.4pt}%
}

% 章の先頭ページ（plain スタイル）
\fancypagestyle{plain}{%
  \fancyhf{}%
  \fancyhead[R]{\small 文書タイトル}%
  \fancyfoot[C]{\small \thepage\ /\ \pageref{LastPage}}%
  \renewcommand{\headrulewidth}{0.0pt}%
  \renewcommand{\footrulewidth}{0.4pt}%
}

\pagestyle{normal}
""",
}
```

| 位置指定 | 意味 |
|---|---|
| `[L]` | 左 |
| `[C]` | 中央 |
| `[R]` | 右 |
| `[LE]` / `[RO]` | 左ページの左 / 右ページの右（両面印刷用） |

## 目次の深さの設定

`\setcounter{tocdepth}{N}` で目次に表示するレベルを制御します。

```python
latex_elements = {
    "preamble": r"""
\setcounter{tocdepth}{2}   % 章・節・小節まで表示（subsection まで）
""",
}
```

| 値 | 表示するレベル |
|---|---|
| `0` | 章（chapter）のみ |
| `1` | 章 + 節（section） |
| `2` | 章 + 節 + 小節（subsection） |
| `3` | 章 + 節 + 小節 + 小小節（subsubsection） |

## フォントのカスタマイズ

### 欧文フォント

Sphinx のデフォルトは TeX Gyre Termes（Times 系）です。変更するには:

```python
latex_elements = {
    "preamble": r"""
% TeX Gyre Pagella（Palatino 系）に変更する例
\usepackage{tgpagella}
""",
}
```

### 日本語フォント（uplatex）

```python
latex_elements = {
    "preamble": r"""
% IPAex フォントを使用する例
\usepackage[ipaex]{pxchfon}
""",
}
```

## `latex_toplevel_sectioning` の設定

```python
# 最上位の見出しレベルを LaTeX のどのコマンドにマップするか
latex_toplevel_sectioning = "chapter"   # デフォルト（manual クラス）
# latex_toplevel_sectioning = "section"   # howto クラスで使う場合
# latex_toplevel_sectioning = "part"      # 最上位を \part{} にする場合
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

| エラーメッセージ | 原因と対処 |
|---|---|
| `tgtermes.sty not found` | `tex-gyre` パッケージ未インストール |
| `! LaTeX Error: File 'pxchfon.sty' not found` | 日本語フォントパッケージ未インストール |
| `command 'mmdc' cannot be run` | mermaid-cli 未インストール（図は省略される） |
| `uplatex: command not found` | TeX Live の日本語パッケージ未インストール |

## 演習

:::{exercise} 演習 5-2: PDF をビルドする

1. Docker またはローカル TeX Live で `make pdf` / `make docker-pdf` を実行する
2. `docs/build/latex/sphinx-master-class.pdf` を開き、表紙・目次・本文を確認する
3. `conf.py` の `latex_elements["maketitle"]` を編集して表紙をカスタマイズする
4. `latex_elements["preamble"]` のフッター文字を変更して再ビルドし、変更を確認する
:::

