.PHONY: html pdf epub dev clean docker-html docker-dev docker-pdf

SOURCE = docs/source
BUILD  = docs/build

## ─── ローカルビルド ──────────────────────────────────
html:  ## HTML をビルド（build/html/index.html）
	sphinx-build -b html $(SOURCE) $(BUILD)/html

pdf:   ## PDF をビルド（build/latex/*.pdf、要 LaTeX）
	sphinx-build -M latexpdf $(SOURCE) $(BUILD)

epub:  ## ePub をビルド（build/epub/*.epub）
	sphinx-build -b epub $(SOURCE) $(BUILD)/epub

dev:   ## ライブリロードサーバーを起動（http://localhost:8000）
	sphinx-autobuild $(SOURCE) $(BUILD)/html --host 0.0.0.0 --port 8000

clean: ## ビルド成果物を削除
	rm -rf $(BUILD)/

## ─── Docker ─────────────────────────────────────────
docker-html: ## Docker で HTML ビルド
	docker compose -f docker/docker-compose.yml run --rm html

docker-dev:  ## Docker でライブリロードサーバー起動
	docker compose -f docker/docker-compose.yml up dev

docker-pdf:  ## Docker で PDF ビルド（TeX Live 込み）
	docker compose -f docker/docker-compose.yml run --rm pdf

docker-clean: ## Docker イメージ・コンテナをクリーン
	docker compose -f docker/docker-compose.yml down --rmi local

help: ## このヘルプを表示
	@grep -E '^[a-zA-Z_-]+:.*##' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*##"}{ printf "  %-18s %s\n", $$1, $$2}'
