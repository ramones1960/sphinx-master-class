# テーマの選択とカスタマイズ

## 主要テーマの比較

| テーマ | 特徴 | 向いている用途 |
|---|---|---|
| **Furo** | モダン・設定レス・ダークモード対応 | 文書サイト全般 |
| **alabaster** | Sphinx 標準同梱（インストール不要） | シンプルなドキュメント |
| **sphinx-rtd-theme** | ReadTheDocs 風 | OSS での採用実績が豊富 |
| **pydata-sphinx-theme** | Pandas/NumPy などのデータ系プロジェクト | データサイエンス |
| **Book theme** | 章・節形式で展開 | 書籍スタイルの大規模な文書 |

## Furo テーマ（この教材で使用）

```bash
pip install furo
```

```python
html_theme = "furo"

html_theme_options = {
    # キーボードナビゲーション（J/K でページ移動）
    "navigation_with_keys": True,
    # 上部の編集ボタン
    "top_of_page_button": "edit",
    # ライト・ダークモードのカラーカスタマイズ
    "light_css_variables": {
        "color-brand-primary": "#0066cc",
    },
    "dark_css_variables": {
        "color-brand-primary": "#4d9fff",
    },
}
```

## CSS でさらにカスタマイズ

`docs/source/_static/custom.css` に CSS を書き、`conf.py` で読み込みます。

```python
html_static_path = ["_static"]
html_css_files = ["custom.css"]
```

日本語フォントを統一する例:

```css
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap");

:root {
  --font-stack: "Noto Sans JP", "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
}
```

## 演習

:::{exercise} 演習 2-2: テーマを切り替える

1. `conf.py` で `html_theme = "alabaster"` に変更する
2. `make html` で再ビルドし、デザインの差異を確認する
3. `furo` に戻し、`html_theme_options` でブランドカラーを変更する
:::
