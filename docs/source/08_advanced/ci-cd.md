# CI/CD インテグレーション

## GitHub Actions で HTML をビルド・デプロイ

```yaml
# .github/workflows/docs.yml
name: Build and Deploy Docs

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          cache: 'pip'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Build HTML (warnings as errors)
        run: sphinx-build -W -b html docs/source docs/build/html

      - name: Upload Pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: docs/build/html

  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/deploy-pages@v4
        id: deployment
```

## PDF ビルドを CI に追加する

```yaml
      - name: Install TeX Live
        run: |
          sudo apt-get update
          sudo apt-get install -y --no-install-recommends \
            texlive-latex-recommended texlive-latex-extra \
            texlive-fonts-recommended texlive-lang-japanese latexmk

      - name: Build PDF
        run: sphinx-build -M latexpdf docs/source docs/build

      - name: Upload PDF artifact
        uses: actions/upload-artifact@v4
        with:
          name: documentation-pdf
          path: docs/build/latex/*.pdf
```

## リンクチェックを定期実行する

```yaml
# .github/workflows/linkcheck.yml
name: Link Check

on:
  schedule:
    - cron: '0 9 * * 1'  # 毎週月曜日午前 9 時
  workflow_dispatch:      # 手動実行も有効化

jobs:
  linkcheck:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: pip install -r requirements.txt
      - run: sphinx-build -b linkcheck docs/source docs/build/linkcheck
      - name: Upload linkcheck result
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: linkcheck-results
          path: docs/build/linkcheck/
```

## プルリクエストでビルド検証を実行する

```yaml
# PR 時は -W フラグで警告をエラー扱いにする
- name: Build HTML (strict)
  run: sphinx-build -W --keep-going -b html docs/source docs/build/html
```

`--keep-going` を併用すると、最初のエラーで止まらず全ての警告・エラーを出力してから失敗します。

## 演習

:::{exercise} 演習 8-3: GitHub Actions を設定する

1. `.github/workflows/docs.yml` を作成する
2. main ブランチにプッシュして Actions が実行されることを確認する
3. GitHub Pages の設定で Actions をソースに指定してデプロイする
:::
