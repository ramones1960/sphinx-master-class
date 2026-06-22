# カスタムディレクティブの作成

この章では、`_ext/card_directive.py` と `_ext/step_counter.py` の実装を順に解説します。

## 拡張の基本構造

Sphinx 拡張は **Python モジュール**です。`setup(app)` 関数がエントリポイントです。

```python
# _ext/my_extension.py

from docutils import nodes
from sphinx.util.docutils import SphinxDirective

class MyNode(nodes.General, nodes.Element):
    pass

class MyDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    optional_arguments = 1

    def run(self):
        node = MyNode()
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]

def visit_mynode_html(self, node): self.body.append('<div class="myclass">')
def depart_mynode_html(self, node): self.body.append('</div>')
def visit_mynode_text(self, node): pass
def depart_mynode_text(self, node): pass

def setup(app):
    app.add_node(
        MyNode,
        html=(visit_mynode_html, depart_mynode_html),
        latex=(visit_mynode_text, depart_mynode_text),
        text=(visit_mynode_text, depart_mynode_text),
    )
    app.add_directive("mydir", MyDirective)
    return {"version": "0.1", "parallel_read_safe": True}
```

## `card_directive.py` の実装

`{card}` ディレクティブはタイトル・アイコン・本文を持つ視覚的なカードブロックを生成します。

**使用例**

````markdown
```{card} カードタイトル
:icon: 💡

カードの本文コンテンツ。**Markdown も使えます**。
```
````

**実装のポイント**

```python
class CardDirective(SphinxDirective):
    required_arguments = 1    # タイトルは必須
    optional_arguments = 0
    final_argument_whitespace = True  # タイトルにスペースを允許
    has_content = True
    option_spec = {
        "icon": directives.unchanged,  # :icon: オプション
    }

    def run(self):
        title = self.arguments[0]
        icon  = self.options.get("icon", "")
        
        card = card_node()
        card["title"] = title
        card["icon"]  = icon
        
        # 内容を docutils のノードツリーに変換
        self.state.nested_parse(self.content, self.content_offset, card)
        return [card]
```

**実際のコード**: `docs/source/_ext/card_directive.py`

## `step_counter.py` の実装

`{step}` ディレクティブはページ内で自動番号が付くステップのリストを生成します。

**使用例**

````markdown
```{step} 1
最初のステップ
```

```{step} 2
次のステップ
```
````

**実装のポイント**

```python
class StepDirective(SphinxDirective):
    required_arguments = 1   # ステップ番号またはタイトル
    has_content = True

    def run(self):
        step_num = self.arguments[0]
        node = step_node()
        node["step"] = step_num
        # ソースの行番号情報を保存（エラーメッセージに使う）
        node.line = self.lineno
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]
```

**実際のコード**: `docs/source/_ext/step_counter.py`

## conf.py に拡張を登録する

```python
import sys, os
sys.path.insert(0, os.path.abspath("_ext"))

extensions = [
    ...,
    "card_directive",   # _ext/card_directive.py
    "badge_role",       # _ext/badge_role.py
    "step_counter",     # _ext/step_counter.py
]
```

## ディレクティブ開発のチェックリスト

```{step} 1
`nodes.General` + `nodes.Element` を継承したノードクラスを定義する
```

```{step} 2
`SphinxDirective` を継承したディレクティブクラスを定義する
```

```{step} 3
`visit_*` / `depart_*` 関数で HTML・LaTeX の実際の出力を定義する
```

```{step} 4
`setup(app)` で `app.add_node()` と `app.add_directive()` を呼び出す
```

```{step} 5
`conf.py` の `extensions` に拡張名を追加して HTML で動作を確認する
```

## 演習

:::{exercise} 演習 6-1: カスタムディレクティブを拡張する

1. `_ext/card_directive.py` を開き、`:link:` オプションを追加してカードにリンクを追加する
2. HTML の `visit_card_html` 関数で `<a href="...">` でカード全体をラップする
3. どこかのページで `:link:` オプション付きの `{card}` を書いて動作を確認する
:::
