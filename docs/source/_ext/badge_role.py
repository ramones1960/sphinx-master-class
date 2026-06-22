"""Sphinx 拡張: インラインバッジロール。

テキスト内に色付きバッジラベルを挿入するインラインロール。

提供するロール:
    ``{badge-new}`ラベルテキスト```    → 青バッジ（新機能）
    ``{badge-tip}`ラベルテキスト```    → 緑バッジ（推奨）
    ``{badge-warn}`ラベルテキスト```   → 赤バッジ（警告）
    ``{badge-info}`ラベルテキスト```   → グレーバッジ（中立）
"""

from docutils import nodes
from sphinx.util.docutils import SphinxRole


class BadgeRole(SphinxRole):
    """kind の値に応じた CSS クラスが付くインラインノードを生成する。"""

    def __init__(self, kind: str):
        self.kind = kind
        super().__init__()

    def run(self):
        node = nodes.inline(
            rawsource=self.rawtext,
            text=self.text,
            classes=["badge", f"badge-{self.kind}"],
        )
        return [node], []


def setup(app):
    for kind in ("new", "tip", "warn", "info"):
        app.add_role(f"badge-{kind}", BadgeRole(kind))
    app.add_css_file("badge-role.css")
    return {"version": "0.1", "parallel_read_safe": True}
