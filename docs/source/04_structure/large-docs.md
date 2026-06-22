# 大規模文書の構成

## 推奨ディレクトリ構成

親ページが子の `toctree` を持つ階層構成が大規模文書では厹主です。

```
docs/source/
├── index.md          # トップ toctree（各章の index.md を登録）
├── guide/
│   ├── index.md      # ガイド章の toctree（各ページを登録）
│   ├── install.md
│   └── configuration.md
├── api/
│   ├── index.md
│   ├── module-a.md
│   └── module-b.md
└── changelog/
    ├── index.md
    └── v1.0.md
```

トップの `index.md` には各ディレクトリの `index` だけを登録し、各章の `index.md` がその章内のページを管理する構造にします。

## ラベルの命名規则

大規模文書でラベル重複を防ぐため、**プレフィック割り当ての命名規則**を決めます。

```
# この教材の命名規則
(chXX-<ファイル名>-<見出し説明>)=

# 例
(ch01-install-venv-step2)=
(ch06-ext-card-directive-api)=
```

## 用語集を作る

`glossary` ディレクティブで用語集を定義し、`{term}` ロールで本文から参照できます。

````markdown
```{glossary}
Sphinx
  Python 製のドキュメントビルダー。
  HTML / PDF / ePub など複数の形式に出力できる。

MyST
  Markedly Structured Text。
  Markdown に Sphinx 機能を追加した履定仕様。
```
本文内での表示: {term}`Sphinx` や {term}`MyST` はクリック可能なリンクになります。
````

## orphan ページを許容する

```markdown
---
orphan: true
---

# toctree に登録しないページ

ダイレクト URL でアクセスするページなどに使います。
```

## 演習

:::{exercise} 演習 4-3: 階層的な toctree を設計する

1. `docs/source/api/` ディレクトリと `docs/source/api/index.md` を作成する
2. `api/index.md` に `toctree` を設定し、ダミーページ 2 つを登録する
3. `docs/source/index.md` のトップ toctree に `api/index` を追加する
4. サイドバーの階層構造を確認する
:::
