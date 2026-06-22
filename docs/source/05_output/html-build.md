# HTML ビルド

## 基本コマンド

```bash
# 基本形式
sphinx-build -b html <source_dir> <build_dir>

# このプロジェクト
sphinx-build -b html docs/source docs/build/html
# または
make html
```

## インクリメンタルビルド

Sphinx はデフォルトで変更済みファイルのみビルドします。
完全再ビルドする場合:

```bash
# -E: 環境変数をリセットして全て再ビルド
sphinx-build -E -b html docs/source docs/build/html

# または build/ を削除してからビルド
make clean && make html
```

## ライブリロード開発

```bash
# ファイルを保存するたびにブラウザが自動更新される
sphinx-autobuild docs/source docs/build/html --host 0.0.0.0 --port 8000

# Makefile 経由
make dev
```

## 便利なビルドオプション

```bash
# 警告をエラーとして扱う（CI で役立つ）
sphinx-build -W -b html docs/source docs/build/html

# 詳細出力（デバッグ時）
sphinx-build -v -b html docs/source docs/build/html

# ビルドキャッシュを无視して全ビルド
sphinx-build -a -b html docs/source docs/build/html
```

## HTML 出力のカスタマイズ

### アナリティクススクリプトの追加

```python
# conf.py
html_js_files = [
    ("https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID", {"async": "async"}),
    "analytics.js",
]
```

### コピーライトのカスタマイズ

```python
html_show_copyright = True  # フッターの著作権表示
html_show_sphinx = False    # "Built with Sphinx" を非表示
```

## GitLab/GitHub Pages へのデプロイ

```yaml
# .github/workflows/docs.yml
name: Deploy Docs
on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: pip install -r requirements.txt
      - run: sphinx-build -b html docs/source docs/build/html
      - uses: actions/upload-pages-artifact@v3
        with:
          path: docs/build/html
```

## 演習

:::{exercise} 演習 5-1: HTML ビルドを検証する

1. `sphinx-build -W -b html docs/source docs/build/html` で警告なしビルドを確認する
2. `docs/build/html/` のファイル構成を確認する
3. `make dev` でライブリロードサーバーを起動し、ソースを編集してリアルタイム更新を確認する
:::
