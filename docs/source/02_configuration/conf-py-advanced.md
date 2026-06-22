# conf.py 発展設定

## intersphinx — 他プロジェクトの文書を相互参照

```python
extensions = [..., "sphinx.ext.intersphinx"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/ja/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "numpy":  ("https://numpy.org/doc/stable", None),
}
```

設定後は他プロジェクトのラベルに対して `{py:class}` や `{ref}` を使えます。
詳細は {doc}`../08_advanced/intersphinx` を参照してください。

## copybutton — コードブロックのコピーボタン

```python
extensions = [..., "sphinx_copybutton"]

# プロンプト（$ や >>> など）をコピー対象から除外
copybutton_prompt_text = r"\$ |>>> |\.\.\.  "
copybutton_prompt_is_regexp = True
```

## autodoc — docstring から API 文書を自動生成

```python
extensions = [..., "sphinx.ext.autodoc", "sphinx.ext.napoleon"]

autodoc_default_options = {
    "members": True,           # パブリックメンバーを自動取込
    "undoc-members": False,    # docstring なしのメンバーを除外
    "show-inheritance": True,  # 継承関係を表示
}
autoclass_content = "both"     # クラスの docstring + __init__ の docstring を両方表示
```

## LaTeX / PDF 設定

### エンジンの選択

```python
# 日本語に最適化されたエンジン
latex_engine = "uplatex"   # uplatex + dvipdfmx（日本語 PDF の定番）
# latex_engine = "xelatex" # XeTeX（多言語対応が容易）
# latex_engine = "lualatex" # LuaLaTeX（最新だが遅い）
```

### 出力ファイル名の設定

```python
latex_documents = [
    # (startdocname, targetname, title, author, theme, toctree_only)
    ("index", "my-docs.tex", "My Documentation", "Author", "manual"),
]
```

### ページスタイル・フォント・プリアンブル

```python
latex_elements = {
    "papersize": "a4paper",
    "pointsize": "11pt",
    "preamble": r"""
\usepackage{fancyhdr}
\usepackage{lastpage}
\fancypagestyle{normal}{%
  \fancyhf{}%
  \fancyfoot[C]{\thepage\ /\ \pageref{LastPage}}%
  \renewcommand{\headrulewidth}{0.4pt}%
}
""",
}
```

## HTML 記事メタデータ

```python
# 表紙画像（Furo・sphinx_rtd_themeなどが対応）
html_logo = "_static/logo.png"
html_favicon = "_static/favicon.ico"

# トップレベルタイトル
html_title = "My Documentation"

# 追加 CSS
html_css_files = ["custom.css"]

# 自巻きで】「小型」表示を無効化
html_compact_lists = True
```

## ✓ チェックリスト

- [ ] `intersphinx_mapping` に Python 公式文書を追加して和参照を試す
- [ ] `copybutton_prompt_text` で `$` プロンプトを除外してテストする
- [ ] `latex_elements["preamble"]` でページフッターを追加し、PDF ビルドで確認する
