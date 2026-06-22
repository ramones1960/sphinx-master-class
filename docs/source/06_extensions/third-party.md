# 主なサードパーティ拡張

## myst-parser

Markdown（MyST）形式で文書を書けるようにする拡張です。この教材でも使用しています。

```bash
pip install myst-parser
```

## sphinx-autobuild

ファイル変更をリアルタイムに検知してブラウザを自動更新します。

```bash
pip install sphinx-autobuild
sphinx-autobuild docs/source docs/build/html
```

## furo

モダンなレスポンシブデザインのテーマです。ダークモード対応で設定がシンプルです。

```bash
pip install furo
```

## sphinx-copybutton

コードブロックにコピーボタンを追加します。

```bash
pip install sphinx-copybutton
```

```python
copybutton_prompt_text = r"\$ |>>> |\.\.\.  "
copybutton_prompt_is_regexp = True
```

## sphinxcontrib-mermaid

Mermaid 図（フローチャート・シーケンス図など）を埋め込めます。

```bash
pip install sphinxcontrib-mermaid
```

```{mermaid}
sequenceDiagram
    アリス->>+ボブ: こんにちは
    ボブ-->>-アリス: やあ、こんにちは
```

## sphinx-design

Grig・カード・ドロップダウンなどの UI コンポーネントを提供します。

```bash
pip install sphinx-design
```

## nbsphinx / myst-nb

Jupyter Notebook (.ipynb) を Sphinx 文書に取り込みます。

```bash
pip install myst-nb  # myst-parser と統合済み
```

## sphinx-intl

国際化対応（i18n）をサポートします。詳細は {doc}`../08_advanced/i18n` を参照してください。
