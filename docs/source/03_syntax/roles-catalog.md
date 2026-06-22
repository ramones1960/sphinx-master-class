# ロールカタログ

ロールは**インラインレベルの機能**を提供します。MyST 記法: `` {role}`内容` ``

## 相互参照ロール

```markdown
ページ参照:        {doc}`開発ガイド <getting-started>`
見出し参照:      {ref}`環境構築 <setup-label>`
ダウンロードリンク:  {download}`ダウンロード <file.pdf>`
用語集:         {term}`Sphinx`
```

## Python ドメインロール（autodoc と併用）

```markdown
Python クラス:     {py:class}`pathlib.Path`
Python 関数:     {py:func}`os.path.join`
Python メソッド:   {py:meth}`str.format`
Python 属性:     {py:attr}`Path.name`
Python 例外:     {py:exc}`ValueError`
Python モジュール: {py:mod}`pathlib`
```

`intersphinx` と組み合わせると、Python 公式ドキュメントへのリンクになります。

## コードロール

```markdown
インラインコード: {code}`print("hello")`
またはバックティック: `print("hello")`
```

## kbd ・ abbr ロール

```markdown
キーボードショートカット: {kbd}`Ctrl+S`
略語:            {abbr}`HTML (ハイパーテキストマークアップ言語)`
```

## intersphinx ロール

`intersphinx` を有効化すると、他プロジェクトのラベルにリンクできます。

```markdown
# intersphinx_mapping = {"python": ...} の設定が必要
Python 公式: {py:class}`python:pathlib.Path`
Sphinx 公式: {ref}`sphinx:toctree-directive`
```

## カスタムロール（この教材の独自拡張）

```markdown
バッジロール: {badge-new}`New` {badge-tip}`推奨` {badge-warn}`非推奨`
```

表示例: {badge-new}`New` {badge-tip}`推奨` {badge-warn}`非推奨`

作成方法は {doc}`../06_extensions/custom-role` で学びます。

## 演習

:::{exercise} 演習 3-3: 相互参照を使う

1. `docs/source/index.md` に、`{doc}` ロールで第 2 章の `conf-py-basics` へのリンクを追加する
2. 存在しないファイルを指定してビルド警告が出ることを確認する
3. `(label)=` で見出しにラベルを付け、`{ref}` で参照する
:::
