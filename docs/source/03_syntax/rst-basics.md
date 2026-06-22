# reStructuredText 基礎

reStructuredText（RST）は Sphinx 標準のフォーマットです。
MyST Markdown より学習コストは高いですが、**標準 Sphinx ドキュメントや OSS プロジェクトのソースを読む**際に必要です。

## 見出し

RST の見出しは**文字の下に線を引く**記法です。

```rst
第1章のタイトル
================

第2章のタイトル
----------------

サブセクション
~~~~~~~~~~~
```

線の種類はプロジェクト内で統一されていればよく、一般的に `=` `-` `~` `^` の順で使います。

## リスト

```rst
* 箇条書きリスト
* 2番目の項目

  * ネスト（インデントは 2 スペース以上）

1. 番号付きリスト
2. 2番目
```

## テーブル

```rst
+----------+----------+
| 列 1     | 列 2     |
+==========+==========+
| データ 1  | データ 2  |
+----------+----------+

.. シンプルテーブル
.. list-table:: タイトル
   :header-rows: 1

   * - 列 1
     - 列 2
   * - データ 1
     - データ 2
```

## ディレクティブ（RST）

```rst
.. note::

   注意事項。**内容はインデント**して書く。

.. warning::

   警告メッセージ。

.. code-block:: python

   def hello():
       print("Hello, Sphinx!")

.. image:: _static/logo.png
   :alt: ロゴ
   :width: 200px
```

## インラインマークアップ

```rst
**太字**、*イタリック*、``インラインコード``

`外部リンク <https://example.com>`_

:doc:`内部リンク <getting-started>`
```

## RST と MyST の対応表

| 要素 | reStructuredText | MyST Markdown |
|---|---|---|
| 見出し | `== -- ~~`  | `# ## ###` |
| 箇条書きリスト | `* item` | `- item` |
| コードブロック | `.. code-block:: python` | ` ```python ` |
| 警告ボックス | `.. warning::` | ` ```{warning} ` |
| 相互参照 | `:doc:\`page\`` | `{doc}\`page\`` |

## 演習

:::{exercise} 演習 3-1: RST ファイルを作成する

1. `docs/source/hello.rst` を新規作成する
2. RST 記法で見出し・リスト・警告ボックスを含むページを書く
3. `index.md` の `toctree` に追加して HTML をビルドする
4. MyST 版と見比べて、記法の違いを確認する
:::
