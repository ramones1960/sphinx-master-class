"""Sphinx 拡張: step ディレクティブ。

ステップ番号付きの手順ブロックを描画する。

使用例::

    ```{step} 1
    増主テキスト
    ```

    ```{step} 2
    次のステップ
    ```

マークダウン文中で相互参照ディレクティブやコードブロックを含めることもできる。
"""

from docutils import nodes
from sphinx.util.docutils import SphinxDirective


class step_node(nodes.General, nodes.Element):
    pass


class StepDirective(SphinxDirective):
    required_arguments = 1           # ステップ番号またはラベル
    optional_arguments = 0
    final_argument_whitespace = True # スペースを含むラベルも許容
    has_content = True

    def run(self):
        step_num = self.arguments[0]
        node = step_node()
        node["step"] = step_num
        node.line = self.lineno
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


# ── HTML ビジター ─────────────────────────────────────────

def visit_step_html(self, node):
    step = node.get("step", "?")
    self.body.append(
        f'<div class="sphinx-step">'
        f'<span class="sphinx-step-number">{self.encode(step)}</span>'
        f'<div class="sphinx-step-content">'
    )


def depart_step_html(self, node):
    self.body.append("</div></div>\n")


# ── LaTeX ビジター ────────────────────────────────────────

def visit_step_latex(self, node):
    step = node.get("step", "?")
    self.body.append(
        f"\\begin{{description}}\n\\item[STEP {step}] "
    )


def depart_step_latex(self, node):
    self.body.append("\\end{description}\n")


# ── テキストビジター ───────────────────────────────────────

def visit_step_text(self, node):
    step = node.get("step", "?")
    self.add_text(f"STEP {step}: ")


def depart_step_text(self, node):
    pass


# ── setup ─────────────────────────────────────────────────────

def setup(app):
    app.add_node(
        step_node,
        html=(visit_step_html, depart_step_html),
        latex=(visit_step_latex, depart_step_latex),
        text=(visit_step_text, depart_step_text),
    )
    app.add_directive("step", StepDirective)
    return {"version": "0.1", "parallel_read_safe": True}
