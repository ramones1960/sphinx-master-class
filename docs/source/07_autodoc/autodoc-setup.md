# autodoc セットアップ

## conf.py の設定

```python
import sys, os

# 対象モジュールのパスを通す
sys.path.insert(0, os.path.abspath("."))  # docs/source/ を起点に

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",  # 「ソースを見る」リンクを追加
]

autodoc_default_options = {
    "members": True,           # public メンバーを自動取込
    "undoc-members": False,    # docstring なしメンバーを除外
    "show-inheritance": True,  # 継承関係を表示
    "member-order": "bysource",# ソース順に並べる
}
autoclass_content = "both"  # クラスの docstring + __init__ の docstring を両方表示
```

## ディレクティブの使い方

### モジュール全体

````markdown
```{automodule} mypackage.mymodule
:members:
```
````

### 特定のクラス

````markdown
```{autoclass} mypackage.mymodule.MyClass
:members:
:special-members: __init__
```
````

### 特定の関数

````markdown
```{autofunction} mypackage.mymodule.my_function
```
````

### 特定メンバーだけ指定

````markdown
```{autoclass} mypackage.MyClass
:members: method_a, method_b
```
````

## 除外したいメンバー

```python
class MyClass:
    def public_method(self):
        """API に公開する"""

    def _internal_method(self):
        """_ 始まりは自動非公開"""

    def exclude_me(self):
        """mydocstring"""
        pass

    exclude_me.__doc__ = None  # ドキュメントを除去して非公開にする
```

## モジュールのディレクトリ構成

```
docs/source/
├── conf.py
└── sample_lib/         # Python パッケージ
    ├── __init__.py
    └── calculator.py   # 実習用モジュール
```

`conf.py` で `sys.path.insert(0, os.path.abspath("."))` とすることで
`sample_lib.calculator` としてインポートできます。

## 演習

:::{exercise} 演習 7-1: autodoc で API 文書を生成する

1. `make html` でビルドし、第7章のトップページを開く
2. `Calculator` クラスの API 文書が自動生成されていることを確認する
3. `sample_lib/calculator.py` に新しいメソッドを追加し、再ビルドで API 文書に反映されることを確認する
:::
