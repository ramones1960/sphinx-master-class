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

## 章番号を正しく付ける — ルート文書の構造が鍵

PDF（`manual` クラス）では、**ルート文書（`index.md`）の見出しがそのまま章立てに反映**されます。
ここを誤ると章番号がズレるため、構造で解決するのが定石です。

:::{warning}
**やりがちな失敗**: ルート `index.md` に `## カリキュラム` `## 学習カード` などの
見出しと本文を直接書くと、それぞれが `\chapter`（＝独立した章）に化け、
`toctree` で並べた本来の各章はその配下の `\section` に押し込まれます。
結果、概要が「第1章」になり、本来の章番号が 1 つずつズレます。
`\frontmatter` / `\mainmatter` で番号を打ち消すのは対症療法に過ぎません。
:::

**根本対応**は、ルート `index.md` を「タイトル＋`toctree` だけ」の薄い表紙にし、
概要（カリキュラム・学習カードなど）は独立した「はじめに」章へ分離することです。
このプロジェクトはこの構成を採用しています。

````markdown
# ドキュメントタイトル

```{toctree}
:maxdepth: 2
:numbered:

00_introduction/index   ← 「はじめに」（概要をここへ）
01_introduction/index
02_configuration/index
...
```
````

- `toctree` をルートの見出し直下に置く（`##` 見出しで包まない）ことで、各ドキュメントが**トップレベルの章**になります。
- 各章タイトルには「第N章：」と手書きせず、`:numbered:` に採番を委ねます。`jsbook` は `\chapter` に自動で「第N章」を付けるため、手書きすると **二重番号**（例: 「第2章 第1章：…」）になります。
- `:numbered:` により **HTML（`1. はじめに`）と PDF（`第1章 はじめに`）の番号が一致**します。

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

## ページ番号をフッターに統一する

技術文書では「前付け（目次まで）はローマ数字、本文はアラビア数字」が一般的です。
本プロジェクトでは `tableofcontents` で目次を前付けに、本文をアラビア数字に切り替えています。

```python
latex_elements = {
    "tableofcontents": r"""
\clearpage
\pagenumbering{roman}
\sphinxtableofcontents
\clearpage
\pagenumbering{arabic}
""",
}
```

ページ番号の**位置**は `fancyhdr` で制御します。番号を必ず**下中央のフッター**へ集約し、
ヘッダーには出さないのがポイントです。

```python
latex_elements = {
    "preamble": r"""
\usepackage{lastpage}
\usepackage{fancyhdr}

% 本文ページスタイル（番号はフッター中央のみ）
\fancypagestyle{normal}{%
  \fancyhf{}%
  \fancyhead[L]{\small\nouppercase{\leftmark}}%   左ヘッダー: 章タイトル
  \fancyhead[R]{\small 文書タイトル}%              右ヘッダー: 固定テキスト
  \fancyfoot[C]{\small \thepage\ /\ \pageref{LastPage}}%  フッター: ページ番号
  \renewcommand{\headrulewidth}{0.4pt}%
  \renewcommand{\footrulewidth}{0.4pt}%
}
% 章の先頭ページ（plain）と、jsbook 既定の headings も同じ定義にして
% 「右上にページ番号が出る」混在を構造的に防ぐ
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\small \thepage}}
\fancypagestyle{headings}{\fancyhf{}%
  \fancyhead[L]{\small\nouppercase{\leftmark}}\fancyfoot[C]{\small \thepage}}

\pagestyle{normal}
"""
}
```

:::{tip}
`\mainmatter` / `\frontmatter`（jsbook）は便利ですが、`\mainmatter` は
`\pagestyle{headings}` を呼び直すため、**ヘッダー右上にページ番号が再出現**します。
番号をフッターに固定したい場合は使わないか、上記のように `headings` 自体を
フッター番号へ上書きしてください。
:::

| 位置指定 | 意味 |
|---|---|
| `[L]` | 左 |
| `[C]` | 中央 |
| `[R]` | 右 |
| `[LE]` / `[RO]` | 左ページの左 / 右ページの右（両面印刷用） |

## 目次の深さの設定

`\setcounter{tocdepth}{N}` で目次に表示するレベルを制御します。

| 値 | 表示するレベル |
|---|---|
| `0` | 章（chapter）のみ |
| `1` | 章 + 節（section） |
| `2` | 章 + 節 + 小節（subsection） |
| `3` | 章 + 節 + 小節 + 小小節（subsubsection） |

## フォントのカスタマイズ

```python
latex_elements = {
    "preamble": r"""
% 欧文: TeX Gyre Pagella（Palatino 系）に変更する例
\usepackage{tgpagella}
% 日本語（uplatex）: IPAex フォントを使用する例
\usepackage[ipaex]{pxchfon}
""",
}
```

## トラブルシューティング

```bash
# .tex のみ生成（デバッグ用。章立てが正しいか \chapter{} を grep で確認できる）
sphinx-build -b latex docs/source docs/build/latex

# 手動ビルド
cd docs/build/latex
uplatex sphinx-master-class.tex
dvipdfmx sphinx-master-class.dvi
```

| エラーメッセージ | 原因と対処 |
|---|---|
| `tgtermes.sty not found` | `tex-gyre` パッケージ未インストール |
| `File 'pxchfon.sty' not found` | 日本語フォントパッケージ未インストール |
| `command 'mmdc' cannot be run` | mermaid-cli 未インストール（図は省略される） |
| `uplatex: command not found` | TeX Live の日本語パッケージ未インストール |
| 章番号が 1 つずれる | ルート `index.md` に見出し＋本文を直書きしている（上記「章番号を正しく付ける」参照） |

## 演習

:::{exercise} 演習 5-2: PDF をビルドする

1. Docker またはローカル TeX Live で `make pdf` / `make docker-pdf` を実行する
2. `docs/build/latex/sphinx-master-class.pdf` を開き、表紙・目次・本文を確認する
3. `conf.py` の `latex_elements["maketitle"]` を編集して表紙をカスタマイズする
4. `latex_elements["preamble"]` のフッター文字を変更して再ビルドし、ページ番号がフッターに統一されていることを確認する
:::
