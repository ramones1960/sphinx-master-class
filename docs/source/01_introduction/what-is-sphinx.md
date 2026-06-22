# Sphinx とは

## ひとことで言うと

Sphinx は **「1 つのソースから、HTML・PDF・ePub など複数の形式の文書を生成する」**ドキュメントビルダーです。
もともと **Python 公式ドキュメント**のために作られ、
今では多くの OSS ・社内文書で使われています。

```{mermaid}
flowchart LR
    subgraph src["ソース（あなたが書くもの）"]
        A[".rst / .md \nファイル"]
        B["conf.py\n（設定）"]
    end
    A --> S{{Sphinx}}
    B --> S
    S --> H["HTML\n（Web サイト）"]
    S --> P["PDF\n（LaTeX 経由）"]
    S --> E["ePub\n（電子書籍）"]
```

**書くのはプレーンテキスト 1 種類だけ**で、出力形式はビルド時に選べます。
「Web 用」「印刷・納品用 PDF」を別々に作る必要がありません（**Single Source, Multiple Output**）。

## なぜ Sphinx が選ばれるのか — 4 つの設計思想

### 1. ドキュメントを「ソースコード」として扱う（Docs as Code）

文書を `.rst` / `.md` というテキストで書くため、**Git で差分管理・レビュー・履歴追跡**ができます。
Word のバイナリファイルと違い、`git diff` で「誰が・いつ・どこを変えたか」がわかります。

### 2. 「壊れない参照」を仕組みで保証する

Sphinx 最大の特徴が **相互参照（cross-reference）** です。
ページや見出しを **ID（ラベル）** で参照するため、リンク先を移動・改名しても壊れにくく、
**存在しない参照はビルド時に警告**として検出されます。

```markdown
ページ参照: {doc}`開発ガイド <getting-started>`
見出し参照: {ref}`環境構築 <setup-label>`
```

### 3. 1 ソースから複数フォーマットへ出力する

同じソースから **HTML / PDF（LaTeX）/ ePub / man ページ** を生成できます。
「Web で公開しつつ、PDF で納品する」といった要件に、ソースを二重管理せず対応できます。

### 4. 拡張（extension）で機能を足せる

Sphinx 本体は最小限で、機能は**拡張**として `conf.py` の `extensions` に足していきます。

| 拡張 | 役割 |
|---|---|
| `myst_parser` | Markdown(MyST) を書けるようにする |
| `sphinx.ext.autodoc` | Python の docstring から API 文書を自動生成 |
| `sphinx.ext.intersphinx` | 他プロジェクトの文書（Python 公式など）を相互参照 |
| `sphinxcontrib.mermaid` | Mermaid 図を埋め込む |

**自作の拡張**でディレクティブを追加することもできます。第6章で実装を学びます。

## reStructuredText と MyST Markdown の関係

Sphinx の**本来のフォーマットは reStructuredText（`.rst`）**ですが、
`myst-parser` という拡張で **Markdown（`.md`）も書ける**ようになっています。

| | reStructuredText `.rst` | MyST Markdown `.md` |
|---|---|---|
| 位置づけ | Sphinx 標準・最も機能が豊富 | Markdown ベースで対応機能を加える |
| 学習コスト | 高め（独自記法） | 低め（Markdown ベース） |
| ディレクティブ | `.. note::` | ` ```{note}` または `:::note` |
| 混在 | 可能（1 プロジェクト内で両方使える） | 可能 |

:::{note}
この教材は **MyST Markdown** を主張として使用し、
第3章で RST の基礎も学びます。
:::

## Sphinx が向いている用途

- **Python ライブラリの API ドキュメント**（autodoc で docstring から自動生成）
- **厳密な相互参照・用語集が必要な大規模仕様書**
- **PDF 納品が必要な文書**（表紙・目次・ヘッダー/フッター付き）
- **プロジェクト仕様書・技術ドキュメント**

## 次に読む

- {doc}`install-local` — venv でローカルにインストールする
- {doc}`install-docker` — Docker で汚染なしの環境を作る
