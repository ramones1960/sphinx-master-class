# Sphinx 標準拡張

`sphinx.ext.*` は Sphinx に同桁されている拡張です。
追加インストール不要で、`conf.py` の `extensions` に追加するだけで利用できます。

## sphinx.ext.autodoc

Python モジュールの docstring から API 文書を自動生成します。

```python
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]
```

文書内での使用例（MyST）:

````markdown
```{automodule} mymodule.calculator
:members:
:undoc-members: False
```
````

詳細は {doc}`../07_autodoc/index` を参照してください。

## sphinx.ext.napoleon

Google / NumPy スタイルの docstring を解釈します。

```python
# Google スタイル
def add(a: int, b: int) -> int:
    """2つの数の和を返す。

    Args:
        a: 左辺の数。
        b: 右辺の数。

    Returns:
        a + b の値。
    """
    return a + b
```

## sphinx.ext.todo

`{todo}` ディレクティブで TODO 項目を管理します。

```python
todo_include_todos = True  # False にすると本番ビルドで TODO を非表示にできる
```

```{todo}
このページにスクリーンショットを追加する。
```

## sphinx.ext.viewcode

autocode で生成された API 文書に「ソースを見る」リンクを追加します。

```python
extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]
```

## sphinx.ext.intersphinx

他の Sphinx プロジェクトのラベルを相互参照します。
詳細は {doc}`../08_advanced/intersphinx` を参照してください。

## sphinx.ext.coverage

docstring のカバレッジをレポートします。

```bash
sphinx-build -b coverage docs/source docs/build/coverage
cat docs/build/coverage/python.txt
```

## sphinx.ext.githubpages

GitHub Pages 用の `.nojekyll` ファイルを自動生成します。

```python
extensions = [..., "sphinx.ext.githubpages"]
```
