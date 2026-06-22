"""Exercise directive for Sphinx learning materials."""
from __future__ import annotations

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

_LEVELS = ("beginner", "intermediate", "advanced")


def _level_choice(argument: str) -> str:
    return directives.choice(argument, _LEVELS)


class exercise_node(nodes.General, nodes.Element):
    pass


class ExerciseDirective(SphinxDirective):
    """Renders a numbered exercise box with optional difficulty level."""

    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        "level": _level_choice,
    }

    def run(self) -> list[nodes.Node]:
        env = self.env
        if not hasattr(env, "exercise_count"):
            env.exercise_count = 0
        env.exercise_count += 1

        title_text = self.arguments[0] if self.arguments else f"演習 {env.exercise_count}"
        level = self.options.get("level", "beginner")

        node = exercise_node()
        node["title"] = title_text
        node["number"] = env.exercise_count
        node["level"] = level
        node.document = self.state.document

        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def visit_exercise_html(self, node: exercise_node) -> None:
    level = node.get("level", "beginner")
    self.body.append(
        f'<div class="exercise exercise-{level}">'
        f'<div class="exercise-header">'
        f'<span class="exercise-icon">&#9998;</span> '
        f'<span class="exercise-title">{node["title"]}</span>'
        f'</div>'
        f'<div class="exercise-body">'
    )


def depart_exercise_html(self, node: exercise_node) -> None:
    self.body.append("</div></div>")


def visit_exercise_latex(self, node: exercise_node) -> None:
    title = node["title"].replace("_", r"\_").replace("#", r"\#")
    self.body.append(
        f"\\begin{{quote}}\n\\textbf{{{title}}}\n\n"
    )


def depart_exercise_latex(self, node: exercise_node) -> None:
    self.body.append("\\end{quote}\n")


def visit_exercise_text(self, node: exercise_node) -> None:
    self.new_state(0)
    self.add_text(f"[演習] {node['title']}\n" + "-" * 40 + "\n")


def depart_exercise_text(self, node: exercise_node) -> None:
    self.end_state()


def setup(app):
    app.add_node(
        exercise_node,
        html=(visit_exercise_html, depart_exercise_html),
        latex=(visit_exercise_latex, depart_exercise_latex),
        text=(visit_exercise_text, depart_exercise_text),
    )
    app.add_directive("exercise", ExerciseDirective)
    app.add_css_file("exercise-directive.css")
    return {"version": "0.2", "parallel_read_safe": True}
