"""Sphinx 拡張: card ディレクティブ。

タイトル・アイコン・本文を持つ視覚的なカードブロックを描画する。

RST 記法::

    .. card:: カードタイトル
       :icon: 📊

       カード本文。

MyST Markdown 記法::

    ```{card} カードタイトル
    :icon: 📊

    カード本文。
    ```
"""

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class card_node(nodes.General, nodes.Element):
    pass


class CardDirective(SphinxDirective):
    required_arguments = 1            # タイトルは必須
    optional_arguments = 0
    final_argument_whitespace = True  # タイトルにスペースを含められる
    has_content = True
    option_spec = {
        "icon": directives.unchanged,  # :icon: Unicode 絵文字またはテキスト
    }

    def run(self):
        title = self.arguments[0]
        icon  = self.options.get("icon", "")

        node = card_node()
        node["title"] = title
        node["icon"]  = icon

        # コンテンツを docutils のノードツリーに変換して card_node に追加
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


# ── HTML ビジター ─────────────────────────────────────────

def visit_card_html(self, node):
    icon  = node.get("icon", "")
    title = node.get("title", "")
    icon_html = f'<span class="card-icon">{icon}</span> ' if icon else ""
    self.body.append(
        f'<div class="sphinx-card">'
        f'<div class="sphinx-card-header">{icon_html}'
        f'<span class="sphinx-card-title">{self.encode(title)}</span></div>'
        f'<div class="sphinx-card-body">'
    )


def depart_card_html(self, node):
    self.body.append("</div></div>\n")


# ── LaTeX ビジター ────────────────────────────────────────

def visit_card_latex(self, node):
    title = node.get("title", "")
    icon  = node.get("icon", "")
    label = f"{icon} {title}" if icon else title
    self.body.append(
        "\\begin{mdframed}[backgroundcolor=gray!10,"
        "topline=false,bottomline=false,leftline=true,"
        "linewidth=2pt,linecolor=black!50]\n"
        f"{{\\bfseries {label}}}\\par\\smallskip\n"
    )


def depart_card_latex(self, node):
    self.body.append("\\end{mdframed}\n")


# ── テキストビジター（最小限のフォールバック） ───────────────────

def visit_card_text(self, node):
    title = node.get("title", "")
    self.add_text(f"[{title}] ")


def depart_card_text(self, node):
    pass


# ── setup ──────────────────────────────────────────────────────

def setup(app):
    app.add_node(
        card_node,
        html=(visit_card_html, depart_card_html),
        latex=(visit_card_latex, depart_card_latex),
        text=(visit_card_text, depart_card_text),
    )
    app.add_directive("card", CardDirective)
    app.add_css_file("card-directive.css")
    # LaTeX ビジターが \begin{mdframed} を使うため、PDF ビルド時に
    # mdframed パッケージをプリアンブルへ読み込ませる。
    app.add_latex_package("mdframed")
    return {"version": "0.1", "parallel_read_safe": True}
