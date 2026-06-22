# ePub ・その他の出力形式

## ePub ビルド

ePub は LaTeX 不要で、追加インストールなしでビルドできます。

```bash
sphinx-build -b epub docs/source docs/build/epub
# または
make epub
```

`conf.py` にメタ情報を追加するとより丁寧な ePub になります。

```python
epub_title = "Sphinx マスタークラス"
epub_author = "著者名"
epub_language = "ja"
epub_show_urls = "footnote"   # URL を脚注として表示
```

## その他のビルダー

| ビルダー | コマンド | 用途 |
|---|---|---|
| `html` | `-b html` | Web サイト |
| `dirhtml` | `-b dirhtml` | `page/index.html` 形式 |
| `singlehtml` | `-b singlehtml` | 1 ファイル HTML |
| `json` | `-b json` | JSON 形式（検索インデックスなど） |
| `text` | `-b text` | プレーンテキスト |
| `man` | `-b man` | Unix man ページ |
| `linkcheck` | `-b linkcheck` | 外部リンクの実在確認 | 

## `linkcheck` ビルダー — リンク切れ検出

外部 URL が正常にアクセスできるか確認します。

```bash
sphinx-build -b linkcheck docs/source docs/build/linkcheck
```

CI で定期実行することでリンク切れを早期発見できます。

```yaml
# .github/workflows/linkcheck.yml
- run: sphinx-build -b linkcheck docs/source docs/build/linkcheck
```

## 演習

:::{exercise} 演習 5-3: linkcheck を実行する

1. `sphinx-build -b linkcheck docs/source docs/build/linkcheck` を実行する
2. `docs/build/linkcheck/output.txt` を確認し、リンクの状態を確認する
:::
