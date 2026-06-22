# conf.py 基礎

`conf.py` は Sphinx プロジェクトの「設定ファイル」です。
**Python スクリプトとして実行される**ため、変数・検索・ os 模ジュールなどを自由に使えます。

## 最小構成

```python
# docs/source/conf.py

project = "My Project"
copyright = "2024, Your Name"
author = "Your Name"
release = "1.0.0"

extensions = ["myst_parser"]

html_theme = "furo"
```

これだけで HTML ビルドが実行できます。

## 主要設定項目の解説

### プロジェクト情報

```python
project = "Sphinx マスタークラス"  # プロジェクト名（サイトタイトルなどに使用）
copyright = "2024, 棄者"           # 著作権表記
author = "棄者"                   # 著者（PDF の表紙などに使用）
release = "1.0"                      # バージョン
```

### 拡張の有効化

```python
extensions = [
    "myst_parser",           # Markdown サポート
    "sphinx_copybutton",     # コードブロックにコピーボタン
    "sphinx.ext.todo",       # TODO 管理
    "sphinx.ext.autodoc",    # API 文書自動生成
    "sphinx.ext.intersphinx",# 他プロジェクト文書相互参照
]
```

### ウァーニングレベル

```python
suppress_warnings = ["myst.xref_missing"]  # 特定警告を抑制
```

ビルド時に警告が出て完成かない場合、出力内容を読んで原因を特定することが大切です。

### ソースファイルの設定

```python
# .rst と .md の両方を受け付ける
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# 馨図 • OS 生成ファイルを除外
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
```

### MyST の追加機能

```python
myst_enable_extensions = [
    "colon_fence",   # ::: で囲む記法（ディレクティブの別記法）
    "deflist",       # 定義リスト
    "tasklist",      # - [ ] / - [x] チェックボックス
    "fieldlist",     # :key: value フィールドリスト
    "attrs_block",   # {.classname} ブロック属性
]
```

### 言語設定

```python
language = "ja"  # 日本語: "ja"、英語: "en"
```

日本語に設定すると、Sphinx のシステムメッセージ（「前のトピック」など）が日本語化されます。

## パス設定

```python
import os, sys

# カスタム拡張（_ext/ ディレクトリ）のパスを通す
sys.path.insert(0, os.path.abspath("_ext"))

# autodoc 実習用ライブラリのパスを通す
sys.path.insert(0, os.path.abspath("sample_lib"))
```

## todo 拡張の使い方

```python
# conf.py
todo_include_todos = True   # True: 本文内に TODO を表示
                             # False: ビルドから除外（本番ビルド向け）
```

ソース内に `.rst` / `.md` で以下のように書くと TODO ボックスが描画されます。

`````markdown
```{todo}
このセクションは上司のレビューを待ってから書く。
```
`````

## ✓ チェックリスト

- [ ] `project` / `author` / `release` を自分のプロジェクトに合わせて変更して再ビルド
- [ ] `extensions` に不要なものを入れるとエラーになることを確認する
- [ ] `todo_include_todos = True` にして、ソースに `{todo}` を書いて表示を確認する

## 演習

:::{exercise} 演習 2-1: conf.py を編集する

1. `docs/source/conf.py` で `project` を別の名前に変更する
2. `html_title` も同じ名前に変更する
3. `make html` で再ビルドし、ブラウザのタイトルバーが変わったことを確認する
:::
