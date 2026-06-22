# ローカルインストール（venv）

## 前提条件

- Python 3.9 以上（`python --version` で確認）
- pip（Python に同梱）

:::{tip}
**なぜ venv を使うのか?** 他の Python プロジェクトと依存バージョンが衝突するのを防ぐためです。
Sphinx のバージョンアップで別プロジェクトが壊れることもあるため、プロジェクトごとに環境を分離するのがベストプラクティスです。
:::

(local-step1)=
## STEP 1: リポジトリをクローンする

```bash
git clone https://github.com/ramones1960/sphinx-master-class.git
cd sphinx-master-class
```

(local-step2)=
## STEP 2: venv 仮想環境を作成・有効化する

```bash
# リポジトリルート直下に .venv を作成
python -m venv .venv

# 有効化
macOS / Linux: source .venv/bin/activate
Windows CMD:   .venv\Scripts\activate.bat
Windows PS:    .venv\Scripts\Activate.ps1
```

有効化するとプロンプトに `(.venv)` が表示されます。

(local-step3)=
## STEP 3: 依存ライブラリをインストールする

```bash
pip install -r requirements.txt
```

インストールされる主なライブラリ:

| ライブラリ | 役割 |
|---|---|
| `sphinx` | Sphinx 本体 |
| `furo` | モダンな HTML テーマ |
| `myst-parser` | Markdown サポート |
| `sphinx-copybutton` | コードブロックのコピーボタン |
| `sphinxcontrib-mermaid` | Mermaid 図 |
| `sphinx-autobuild` | ライブリロード |

(local-step4)=
## STEP 4: HTML をビルドする

```bash
# Makefile を使う場合
make html

# 直接コマンドの場合
sphinx-build -b html docs/source docs/build/html
```

`docs/build/html/index.html` をブラウザで開くとこの文書が表示されます。

(local-step5)=
## STEP 5: ライブリロードサーバーで開発する

保存するたびにブラウザが自動更新される開発サーバーです。

```bash
# Makefile を使う場合
make dev

# 直接コマンド
sphinx-autobuild docs/source docs/build/html --host 0.0.0.0 --port 8000
```

http://localhost:8000 で確認できます。

## よくあるビルドエラー・警告への対処

Sphinx はビルド時にさまざまな情報を出力します。

```
# 警告の例（対応が必要）
WARNING: document isn't included in any toctree
  -> toctree に登録していないページがある

WARNING: undefined label: 'some-label'
  -> {ref} で指定したラベルが存在しない

# エラーの例（ビルドが失敗）
ERROR: Unknown directive type "hogehoge".
  -> 存在しないディレクティブを使用している
```

## venv の終了・再開

```bash
# 終了
deactivate

# 再開（リポジトリのルートにいることを前提）
source .venv/bin/activate
```

## ✓ チェックリスト

- [ ] `python --version` で 3.9 以上を確認
- [ ] `pip install -r requirements.txt` がエラーなしに完了
- [ ] `make html` で `docs/build/html/index.html` が生成される
- [ ] `make dev` で http://localhost:8000 で文書が表示される

## 演習

:::{exercise} 演習 1-1: 最初の HTML ビルド

1. `docs/source/index.md` を開き、トップの見出し文字を変更する
2. `make html` で再ビルドする
3. `docs/build/html/index.html` で変更が反映されていることを確認する
:::

:::{exercise} 演習 1-2: 新規ページを追加する

1. `docs/source/hello.md` を新規作成し、内容を書く
2. `docs/source/index.md` の `toctree` に `hello` を追加する
3. 再ビルドしてサイドバーに新ページが表示されることを確認する
:::
