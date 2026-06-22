# はじめに

**Sphinx をゼロから体系的に学ぶための実践的な学習教材**へようこそ。
この章では、カリキュラムの全体像・各章の難易度・効率的な学習の進め方を示します。

## カリキュラム

本教材は環境構築から拡張機能の開発まで、8 章で構成されています。

| 章 | テーマ | 概要 |
|---|---|---|
| {doc}`環境構築 <../01_introduction/index>` | 環境構築 | venv / Docker での導入と最初のビルド |
| {doc}`設定 <../02_configuration/index>` | conf.py | プロジェクト設定の全体像 |
| {doc}`構文 <../03_syntax/index>` | RST / MyST | reStructuredText と MyST Markdown |
| {doc}`文書構造 <../04_structure/index>` | toctree | 文書構造の設計・相互参照 |
| {doc}`出力 <../05_output/index>` | HTML / PDF | 複数フォーマットへの出力 |
| {doc}`拡張機能 <../06_extensions/index>` | 拡張開発 | カスタムディレクティブ・ロールの開発 |
| {doc}`autodoc <../07_autodoc/index>` | API 文書 | Python ソースから API 文書を自動生成 |
| {doc}`発展 <../08_advanced/index>` | 応用 | intersphinx・i18n・CI/CD |

## 学習カード

| 章 | テーマ | 難易度 | 想定時間 |
|---|---|---|---|
| {doc}`環境構築 <../01_introduction/index>` | 環境構築 | ★☆☆ | 30分 |
| {doc}`設定 <../02_configuration/index>` | 設定（conf.py） | ★★☆ | 45分 |
| {doc}`構文 <../03_syntax/index>` | 構文（RST / MyST） | ★★☆ | 60分 |
| {doc}`文書構造 <../04_structure/index>` | 文書構造の設計 | ★★☆ | 45分 |
| {doc}`出力 <../05_output/index>` | HTML / PDF 出力 | ★★☆ | 45分 |
| {doc}`拡張機能 <../06_extensions/index>` | 拡張機能の開発 | ★★★ | 90分 |
| {doc}`autodoc <../07_autodoc/index>` | autodoc | ★★★ | 60分 |
| {doc}`発展 <../08_advanced/index>` | 発展トピック | ★★★ | 90分 |

## 学習の進め方

**Sphinx が全く初めての方**は {doc}`環境構築 <../01_introduction/index>` の章から順に進めてください。

**Python での開発経験がある方**は、環境を整えた後、
{doc}`autodoc <../07_autodoc/index>` の章へ飛んで、逆引きに他の章を参照するのが効率的です。

**拡張機能の開発に興味がある方**は {doc}`環境構築 <../01_introduction/index>` と
{doc}`構文 <../03_syntax/index>` を履修後に {doc}`拡張機能の開発 <../06_extensions/index>` へ進んでください。

## この教材で使用するカスタム拡張

{doc}`拡張機能の開発 <../06_extensions/index>` の章で実際に学ぶ拡張機能を、この文書全体で展開しています。

以下はカスタムディレクティブの使用例です。

```{card} カードディレクティブの例
:icon: 📚

このカードは `card_directive` カスタム拡張によって描画されています。
拡張機能の開発の章でその作り方を学びます。
```

バッジロールの例： {badge-new}`New` {badge-tip}`実践的` {badge-warn}`要注意`
