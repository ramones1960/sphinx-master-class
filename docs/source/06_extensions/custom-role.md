# カスタムロールの作成

ロールは **インライン要素**を生成します。ディレクティブよりシンプルなパターンです。

## badge_role.py の実装

`{badge-new}`, `{badge-tip}`, `{badge-warn}` の 3 種類のバッジロールを実装しています。

**使用例**

```markdown
{badge-new}`New feature`  {badge-tip}`Recommended`  {badge-warn}`Deprecated`
```

**実装の概要**

```python
from docutils import nodes
from sphinx.util.docutils import SphinxRole

class BadgeRole(SphinxRole):
    """kind は 'new' / 'tip' / 'warn' などバッジの種類。"""
    def __init__(self, kind: str):
        self.kind = kind
        super().__init__()

    def run(self):
        text = self.text                        # ロールの内容（バッジのラベル）
        node = nodes.inline(
            rawsource=self.rawtext,
            text=text,
            classes=[f"badge", f"badge-{self.kind}"],
        )
        return [node], []

def setup(app):
    for kind in ("new", "tip", "warn", "info"):
        app.add_role(f"badge-{kind}", BadgeRole(kind))
    app.add_css_file("badge-role.css")
    return {"version": "0.1", "parallel_read_safe": True}
```

## ロール開発のパターン

### シンプルロール（関数ベース）

```python
from docutils import nodes

def my_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.emphasis(rawsource=rawtext, text=text)
    return [node], []

def setup(app):
    app.add_role("my-role", my_role)
    return {"version": "0.1", "parallel_read_safe": True}
```

### クラスベース（SphinxRole を継承）

`SphinxRole` を継承すると `self.env`（Sphinx 環境）や `self.config` にアクセスできます。

```python
from sphinx.util.docutils import SphinxRole

class MyRole(SphinxRole):
    def run(self):
        node = nodes.inline(text=self.text)
        return [node], []
```

## CSS でバッジをスタイリングする

```css
/* _static/badge-role.css */
.badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.78em;
    font-weight: 600;
    letter-spacing: 0.02em;
}
.badge-new  { background: #0066cc; color: white; }
.badge-tip  { background: #28a745; color: white; }
.badge-warn { background: #dc3545; color: white; }
.badge-info { background: #6c757d; color: white; }
```

**実際のコード**: `docs/source/_ext/badge_role.py` と `docs/source/_static/badge-role.css`

## 演習

:::{exercise} 演習 6-2: 新しいバッジ種類を追加する

1. `_ext/badge_role.py` を開き、`"danger"` 種類のバッジを追加する
2. `_static/badge-role.css` に `.badge-danger` のスタイルを追加する
3. どこかのページで `{badge-danger}\`Deprecated\`` を書いて動作を確認する
:::
