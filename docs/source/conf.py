# Sphinx 設定ファイル — Sphinx マスタークラス
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# カスタム拡張 (_ext/) と autodoc 実習用ライブラリ (sample_lib/) のパスを通す
sys.path.insert(0, os.path.abspath("_ext"))
sys.path.insert(0, os.path.abspath("."))

# ─── プロジェクト情報 ──────────────────────────────────────────────────────
project = "Sphinx マスタークラス"
copyright = "2024, Sphinx マスタークラス"
author = "学習者"
release = "1.0"

# ─── 拡張 ──────────────────────────────────────────────────────────
extensions = [
    # ─ 記法サポート ────────────────────────
    "myst_parser",              # Markdown(MyST) を解釈する
    # ─ 表示機能拡張 ──────────────────
    "sphinx_copybutton",        # コードブロックにコピーボタン
    "sphinxcontrib.mermaid",    # Mermaid 図サポート
    # ─ Sphinx 標準拡張 ──────────────────
    "sphinx.ext.todo",          # TODO 管理
    "sphinx.ext.autodoc",       # Python docstring から API 文書を自動生成
    "sphinx.ext.napoleon",      # NumPy/Google スタイル docstring を解釈
    "sphinx.ext.intersphinx",   # 他プロジェクトの文書を相互参照
    "sphinx.ext.viewcode",      # ソースコードへのリンクを追加
    # ─ カスタム拡張（_ext/ 内）─────────────────
    "card_directive",           # カードブロックディレクティブ
    "badge_role",               # インラインバッジロール
    "step_counter",             # 自動番号ステップディレクティブ
    "exercise_directive",       # 演習ディレクティブ
]

# Markdown と reStructuredText の両方を受け付ける
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# MyST の追加機能
myst_enable_extensions = [
    "colon_fence",   # ::: で囲む記法（ディレクティブの別記法）
    "deflist",       # 定義リスト
    "tasklist",      # タスクリスト（- [ ] チェックボックス）
    "fieldlist",     # フィールドリスト
    "attrs_block",   # ブロックに属性を付ける
]

language = "ja"

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# ─── HTML 出力 ───────────────────────────────────────────────────────
html_theme = "furo"
html_title = "Sphinx マスタークラス"
html_static_path = ["_static"]
html_css_files = [
    "custom.css",
    "card-directive.css",
    "badge-role.css",
    "exercise-directive.css",
]

html_theme_options = {
    "navigation_with_keys": True,
    "top_of_page_button": "edit",
}

# ─── intersphinx ──────────────────────────────────────────────────
int ersphinx_mapping = {
    "python": ("https://docs.python.org/ja/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

# ─── todo ──────────────────────────────────────────────────────────
todo_include_todos = True

# ─── autodoc ─────────────────────────────────────────────────────────
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "undoc-members": False,
    "show-inheritance": True,
}
autoclass_content = "both"  # クラスと __init__ の docstring を両方表示

# Napoleon: NumPy / Google スタイル docstring を解釈
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_use_param = True
napoleon_use_rtype = True

# ─── PDF (LaTeX) 出力 ───────────────────────────────────────────────
# 日本語 PDF は uplatex（jsbook）+ dvipdfmx が最も実績のある組み合わせ
latex_engine = "uplatex"

latex_documents = [
    ("index", "sphinx-master-class.tex", "Sphinx マスタークラス",
     "学習者", "manual"),
]

latex_elements = {
    "papersize": "a4paper",
    "pointsize": "11pt",
    "preamble": r"""
\usepackage{lastpage}
\usepackage{fancyhdr}

% 本文ページスタイル
\fancypagestyle{normal}{%
  \fancyhf{}%
  \fancyhead[L]{\small\nouppercase{\leftmark}}%
  \fancyhead[R]{\small Sphinx マスタークラス}%
  \fancyfoot[C]{\small \thepage\ /\ \pageref{LastPage}}%
  \renewcommand{\headrulewidth}{0.4pt}%
  \renewcommand{\footrulewidth}{0.4pt}%
}

% 章の先頭ページ
\fancypagestyle{plain}{%
  \fancyhf{}%
  \fancyhead[R]{\small Sphinx マスタークラス}%
  \fancyfoot[C]{\small \thepage\ /\ \pageref{LastPage}}%
  \renewcommand{\headrulewidth}{0.0pt}%
  \renewcommand{\footrulewidth}{0.4pt}%
}

\pagestyle{normal}
\setcounter{tocdepth}{2}
""",
    "maketitle": r"""
\begin{titlepage}
  \centering
  \vspace*{2cm}
  {\Huge\bfseries Sphinx マスタークラス\par}
  \vspace{0.5cm}
  {\Large 環境構築から拡張機能開発まで\par}
  \vspace{1.5cm}
  \rule{\linewidth}{0.4pt}\par
  \vfill
  {\large \today\par}
\end{titlepage}
""",
    "tableofcontents": r"""
\clearpage
\pagenumbering{roman}
\sphinxtableofcontents
\clearpage
\pagenumbering{arabic}
""",
}

latex_toplevel_sectioning = "chapter"
