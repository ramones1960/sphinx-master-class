# Docker 環境セットアップ

Docker を使うと、Python / TeX Live をホストにインストールすることなく、**クリーンで再現性の高い環境**で Sphinx（HTML + PDF）を利用できます。

## 前提条件

- Docker Desktop（Mac / Windows）または Docker Engine（Linux）
- Docker Compose V2（`docker compose` コマンド利用）

## 構成

`docker/` 配下に 2 ファイルあります。

```
docker/
├── Dockerfile           # Python 3.12 + TeX Live + Sphinx
└── docker-compose.yml   # 三種類のサービス定義
```

### Dockerfile の構成

```{literalinclude} ../../../docker/Dockerfile
:language: dockerfile
:caption: docker/Dockerfile
```

## サービス一覧

| サービス | 用途 | コマンド |
|---|---|---|
| `dev` | ライブリロード開発 | `docker compose up dev` |
| `html` | HTML ビルド | `docker compose run --rm html` |
| `pdf` | PDF ビルド | `docker compose run --rm pdf` |
| `epub` | ePub ビルド | `docker compose run --rm epub` |

## クイックスタート

### 1. ライブリロード開発サーバーを起動する

```bash
# 初回はイメージのビルドが入る（数分かかる場合あり）
docker compose -f docker/docker-compose.yml up dev

# または Makefile を経由して
make docker-dev
```

http://localhost:8000 で開発サーバーが起動します。
ソースを編集・保存するとブラウザが自動更新されます。

### 2. HTML ビルドのみ実行する

```bash
docker compose -f docker/docker-compose.yml run --rm html
# または
make docker-html
```

`docs/build/html/index.html` が生成されます。

### 3. PDF をビルドする

```bash
docker compose -f docker/docker-compose.yml run --rm pdf
# または
make docker-pdf
```

TeX Live がコンテナに包まれているため、**ホストに LaTeX がなくても PDF を生成**できます。

## Docker vs ローカル venv の選び方

| 観点 | Docker | ローカル venv |
|---|---|---|
| セットアップ | Docker のみ必要 | Python + pipだけ |
| PDF ビルド | コンテナ内の TeX Live を使用✅ | 別途 LaTeX のインストールが必要 |
| 再現性 | 最高（環境を完全隔離） | 良好（venv で隔離） |
| 起動速度 | 初回ビルド時は遅い | 高速 |
| ディスク占有 | 大（~2GB） | 小 |

## ✓ チェックリスト

- [ ] `docker --version` で Docker がインストールされていることを確認
- [ ] `docker compose -f docker/docker-compose.yml run --rm html` でエラーなし完了
- [ ] `docs/build/html/index.html` が生成される
- [ ] `make docker-dev` で http://localhost:8000 にアクセスできる

## 演習

:::{exercise} 演習 1-3: Docker で PDF をビルドする

1. `make docker-pdf` を実行する
2. `docs/build/latex/` ディレクトリに `.pdf` ファイルが生成されることを確認する
3. PDF を開き、HTML トップページと同じ内容が表示されることを確認する
:::
