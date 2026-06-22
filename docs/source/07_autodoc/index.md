# 第7章： autodoc — Python から API 文書を自動生成

## 学習目標

- `sphinx.ext.autodoc` で docstring から API 文書を自動生成する
- Napoleon 拡張で Google / NumPy スタイル docstring を書く

```{toctree}
:maxdepth: 2

autodoc-setup
napoleon-docstrings
```

## 実習用サンプルライブラリ

`docs/source/sample_lib/` に実習用の Python ライブラリがあります。

```{automodule} sample_lib.calculator
:members:
:undoc-members: False
:show-inheritance:
```
