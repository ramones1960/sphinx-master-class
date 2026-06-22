# ディレクティブカタログ

ディレクティブは**ブロックレベルの機能**を提供します。
以下ではすべて MyST 記法で示します。

## 注釈ボックス系

````markdown
```{note}
一般的な注意事項。見た目はブルー系。
```

```{tip}
原則やヒント。読者の作業を効率化する情報。
```

```{important}
特に大事な情報。
```

```{warning}
間違えると問題が起きる项目。
```

```{caution}
注意して欲しいリスク。
```

```{danger}
危険な操作や設定。
```

```{error}
エラーや不正な状態を示す。
```
````

## コードブロック

````markdown
```{code-block} python
:caption: example.py
:linenos:
:emphasize-lines: 3

def calculate(a, b):
    """2つの数の和を返す"""
    return a + b  # ここがハイライトされる
```
````

ファイルを直接取り込む場合:

````markdown
```{literalinclude} ../sample_lib/calculator.py
:language: python
:lines: 1-20
:caption: calculator.py
```
````

## toctree — 目次ツリー

````markdown
```{toctree}
:maxdepth: 2
:caption: 目次
:hidden:

page1
page2
subdir/page3
```
````

| オプション | 内容 |
|---|---|
| `maxdepth` | サイドバーに表示する階層の深さ |
| `caption` | セクションタイトル |
| `hidden` | 本文中に目次を表示しない |
| `numbered` | 章番号を付ける |
| `glob` | `guide/*` のように glob パターンで一括登録 |

## figure / image — 画像插入

````markdown
```{figure} _static/architecture.png
:alt: システム構成図
:width: 80%
:align: center

図 1: システム全体の構成
```
````

`figure` はキャプション付き、`image` はキャプションなしです。

## table — 表

````markdown
```{list-table} 項目一覧
:header-rows: 1
:widths: 30 70

* - 項目
  - 説明
* - アイテム A
  - 説明テキスト
```
````

## todo — TODO 管理

````markdown
```{todo}
ここに追加する内容:スクリーンショットを挿入する。
```
````

`todo_include_todos = True` を `conf.py` に設定することで表示されます。

## カスタムディレクティブ（この教材の独自拡張）

````markdown
```{card} カードタイトル
:icon: 📝

カード本文。第6章で作成方法を学びます。
```

```{step} 1
自動番号ステップ。第6章で作成方法を学びます。
```
````
