# intersphinx — 他プロジェクト文書を相互参照

`sphinx.ext.intersphinx` を使うと、**別の Sphinx プロジェクトのラベル**に直接リンクできます。

## 設定

```python
extensions = [..., "sphinx.ext.intersphinx"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/ja/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "numpy":  ("https://numpy.org/doc/stable", None),
    "pandas": ("https://pandas.pydata.org/docs", None),
}
```

## 使用例

```markdown
# Python 公式文書のクラスにリンク
Python のパス: {py:class}`pathlib.Path`

# NumPy の関数にリンク
{py:func}`numpy:numpy.array`

# Sphinx のドキュメントのラベルにリンク
{ref}`sphinx:toctree-directive`
```

## objects.inv のダウンロード確認

```bash
# 底数一：対象プロジェクトの objects.inv を参照
python -m sphinx.ext.intersphinx https://docs.python.org/ja/3/objects.inv

# 使用可能なラベルの一覧を確認する
python -m sphinx.ext.intersphinx https://docs.python.org/ja/3/objects.inv | grep pathlib
```

## ローカル / オフライン環境での使用

```python
intersphinx_mapping = {
    # URL の代わりにローカルパスで参照する
    "sister-project": ("/path/to/sister-project/docs/build/html", None),
}
```

## 演習

:::{exercise} 演習 8-1: intersphinx で Python 公式文書を参照する

1. `conf.py` の `intersphinx_mapping` に `"python"` を追加する
2. 任意のページで `{py:class}\`pathlib.Path\`` を書く
3. HTML ビルドでリンクが Python 公式文書へ誘導されることを確認する
:::
