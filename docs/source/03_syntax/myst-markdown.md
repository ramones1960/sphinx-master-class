# MyST Markdown

MyST（Markedly Structured Text）は、Markdown に Sphinx の機能（ディレクティブ・ロール）を追加した拡張仕様です。
**普通の Markdown の写き方はそのまま使える**ため、既存の Markdown ライターにとって導入コストが低いです。

## ディレクティブの書き方

MyST のディレクティブは 2 種類の記法で書けます。

### バックティックフェンス（標準）

````markdown
```{note}
これは注釈ボックスです。
```
````

### コロンフェンス（`myst_enable_extensions = ["colon_fence"]`が必要）

```markdown
:::{note}
コロンフェンスでも同じことができます。
Markdown のコードブロックと区別するため、
ネストするときに便利です。
:::
```

## ディレクティブのオプション指定

````markdown
```{code-block} python
:caption: hello.py
:linenos:
:emphasize-lines: 2

def hello():
    print("Hello, Sphinx!")  # この行がハイライトされる
```
````

バックティックフェンスでは `:option:` 形式でオプションを指定し、コロンフェンスでは引数として指定します。

## ロール（インライン要素）

```markdown
ページ参照:  {doc}`開発ガイド <getting-started>`
ラベル参照:  {ref}`セクション名 <label-name>`
外部リンク:   [Sphinx](https://www.sphinx-doc.org/)
Python 型:  {py:class}`str`
```

## ラベルの付け方

```markdown
(my-label)=
## この見出しにラベルが付く

{ref}`この見出しを参照 <my-label>`
```

`(label)=` は **見出しの直前**に置くことで、その見出しに ID を付けます。

## タスクリスト（`tasklist` 機能が必要）

```markdown
- [x] 完了済みのタスク
- [ ] 未完了のタスク
- [ ] 別のタスク
```

## 定義リスト（`deflist` 機能が必要）

```markdown
Sphinx
: Python 製のドキュメントビルダー

MyST
: Markdown に Sphinx 機能を加えた履定仕様
```

## Mermaid 図

````markdown
```{mermaid}
flowchart TD
    A[インプット] --> B[処理]
    B --> C[アウトプット]
```
````

## 演習

:::{exercise} 演習 3-2: MyST の様々な記法を試す

1. `docs/source/sandbox.md` を新規作成する
2. `note` / `warning` / `tip` / `important` の 4 種類のディレクティブを書く
3. Mermaid 図（フローチャート）を挿入する
4. `toctree` に追加して HTML で表示を確認する
:::
