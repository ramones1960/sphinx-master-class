# Sphinx マスタークラス

**Sphinx をゼロから体系的に学ぶための実践的な学習教材**です。

:::{note}
この文書自体が **Sphinx + MyST Markdown + Furo テーマ** で構築されています。
ソースコード（`docs/source/`）を読みながら、実際の Sphinx プロジェクト構成を体験できます。
:::

## カリキュラム

```{toctree}
:maxdepth: 2
:caption: 第1章：環境構築

01_introduction/index
```

```{toctree}
:maxdepth: 2
:caption: 第2章：設定

02_configuration/index
```

```{toctree}
:maxdepth: 2
:caption: 第3章：構文

03_syntax/index
```

```{toctree}
:maxdepth: 2
:caption: 第4章：文書構造

04_structure/index
```

```{toctree}
:maxdepth: 2
:caption: 第5章：出力

05_output/index
```

```{toctree}
:maxdepth: 2
:caption: 第6章：拡張機能の開発

06_extensions/index
```

```{toctree}
:maxdepth: 2
:caption: 第7章： autodoc

07_autodoc/index
```

```{toctree}
:maxdepth: 2
:caption: 第8章：発展トピック

08_advanced/index
```

## 学習カード

| 章 | テーマ | 難易度 | 想定時間 |
|---|---|---|---|
| {doc}`第1章 <01_introduction/index>` | 環境構築 | ★☆☆ | 30分 |
| {doc}`第2章 <02_configuration/index>` | 設定（conf.py） | ★★☆ | 45分 |
| {doc}`第3章 <03_syntax/index>` | 構文（RST / MyST） | ★★☆ | 60分 |
| {doc}`第4章 <04_structure/index>` | 文書構造の設計 | ★★☆ | 45分 |
| {doc}`第5章 <05_output/index>` | HTML / PDF 出力 | ★★☆ | 45分 |
| {doc}`第6章 <06_extensions/index>` | 拡張機能の開発 | ★★★ | 90分 |
| {doc}`第7章 <07_autodoc/index>` | autodoc | ★★★ | 60分 |
| {doc}`第8章 <08_advanced/index>` | 発展トピック | ★★★ | 90分 |

## 学習の進め方

**Sphinx が全く初めての方**は第1章から順に進めてください。

**Python での開発経験がある方**は、第1章で環境を整えた後、
第7章（autodoc）に飛んで、逆引きに他の章を参照するのが効率的です。

**拡張機能の開発に興味がある方**は第1・第3章を履修後に第6章へ進んでください。

## この教材で使用するカスタム拡張

{doc}`第6章 <06_extensions/index>` で実際に学ぶ拡張機能を、この文書全体で展開しています。

以下はカスタムディレクティブの使用例です。

```{card} カードディレクティブの例
:icon: 📚

このカードは `card_directive` カスタム拡張によって描画されています。
第6章でその作り方を学びます。
```

バッジロールの例： {badge-new}`New` {badge-tip}`実践的` {badge-warn}`要注意`
