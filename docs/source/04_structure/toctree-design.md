# toctree の設計

`toctree` は Sphinx 文書の**目次構造の起点**です。
サイドバー・目次ページ・ PDF の章立てがすべて `toctree` の定義から生成されます。

## 基本構文

````markdown
```{toctree}
:maxdepth: 2
:caption: セクション名

page1
page2
subdir/page3
```
````

注意点:
- **拡張子は不要**。`.md` / `.rst` のどちらでも拡張子を除いた同じファイル名で登録する
- **サブディレクトリはスラッシュ区切り**: `subdir/page3`
- **`toctree` に載せないページ**はビルド時に "orphan" 警告が出る

## `maxdepth` の選び方

| `maxdepth` | サイドバーに表示される階層 |
|---|---|
| `1` | ページのトップレベルの見出しのみ |
| `2` | 2 階層まで（推奨） |
| `3` | 3 階層まで（サイドバーが長くなる） |

## 複数の toctree でセクション分割

1 つのページ内に複数の `toctree` を置けます。

````markdown
```{toctree}
:caption: ガイド

install
configuration
```

```{toctree}
:caption: API リファレンス

api/module-a
api/module-b
```
````

## `numbered` — 章番号を付ける

````markdown
```{toctree}
:numbered:

chapter1
chapter2
```
````

章番号が必要な、パート構成の文書に向いています。

## `glob` — パターンで一括登録

````markdown
```{toctree}
:glob:

guide/*
api/*.rst
```
````

`glob` を使うとファイルをアルファベット順で自動登録します。
追加したファイルが自動でインデックスに含まれるため、読者ノートなどの日付順コンテンツに向いています。

## `hidden` — サイドバーには表示するが本文には出さない

````markdown
```{toctree}
:hidden:

hidden-page
```
````

## ページ追加の基本手順

```{step} 1
`docs/source/` 配下に `.md` または `.rst` ファイルを作成する
```

```{step} 2
所属させたい `toctree` にファイル名を追加する（拡張子は不要）
```

```{step} 3
`make html` または `make dev` でビルドし、サイドバーに新ページが表示されることを確認する
```

## 演習

:::{exercise} 演習 4-1: toctree にサブディレクトリを使う

1. `docs/source/notes/` ディレクトリを作成する
2. `docs/source/notes/2024-01.md` を新規作成する
3. `index.md` の `toctree` に `notes/2024-01` を追加する
4. HTML ビルドでサイドバーに表示されることを確認する
:::
