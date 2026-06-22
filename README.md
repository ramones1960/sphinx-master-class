# Sphinx マスタークラス

環境構築から拡張機能の開発まで、Sphinx を体系的に習得するための学習教材です。
この文書自体が Sphinx で構築されており、**読みながら実際のプロジェクト構成を体験**できます。

## カリキュラム

| 章 | テーマ | 難易度 |
|---|---|---|
| 第1章 | 環境構築 — venv / Docker | ★☆☆ |
| 第2章 | 設定（conf.py） | ★★☆ |
| 第3章 | 構文 — reStructuredText / MyST Markdown | ★★☆ |
| 第4章 | 文書構造の設計 — toctree・相互参照 | ★★☆ |
| 第5章 | HTML・PDF・ePub 出力 | ★★☆ |
| 第6章 | 拡張機能の開発 — カスタムディレクティブ・ロール | ★★★ |
| 第7章 | autodoc — Python ソースから API 文書を自動生成 | ★★★ |
| 第8章 | 発展 — intersphinx・i18n・CI/CD | ★★★ |

## クイックスタート（Docker）

```bash
git clone https://github.com/ramones1960/sphinx-master-class.git
cd sphinx-master-class

# ライブリロード開発サーバー（http://localhost:8000）
docker compose -f docker/docker-compose.yml up dev

# HTML をビルドして build/html/ に出力
docker compose -f docker/docker-compose.yml run --rm html

# PDF をビルド（TeX Live 込み）
docker compose -f docker/docker-compose.yml run --rm pdf
```

## クイックスタート（ローカル venv）

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# HTML ビルド
make html
# または: sphinx-build -b html docs/source docs/build/html

# ライブリロード
make dev
```

## リポジトリ構成

```
sphinx-master-class/
├── README.md
├── requirements.txt        # Python 依存
├── Makefile                # 便利コマンド集
├── docker/
│   ├── Dockerfile          # Sphinx + TeX Live 環境
│   └── docker-compose.yml
└── docs/
    └── source/             # Sphinx プロジェクト（教材本体）
        ├── conf.py
        ├── index.md
        ├── 01_introduction/
        ├── 02_configuration/
        ├── 03_syntax/
        ├── 04_structure/
        ├── 05_output/
        ├── 06_extensions/
        ├── 07_autodoc/
        ├── 08_advanced/
        ├── _ext/            # 学習用カスタム拡張（3つ）
        ├── _static/         # CSS
        └── sample_lib/      # autodoc 実習用サンプルライブラリ
```

## ビルド確認済み環境

- Python 3.12
- Sphinx 7.4+
- Docker 24+（PDF ビルドには TeX Live を含む Docker イメージを使用）

## 参考リポジトリ

この教材は [doc-by-ssg-sample](https://github.com/ramones1960/doc-by-ssg-sample) の
Sphinx サンプルを参考に、より体系的な学習コースとして構築されています。
