.DEFAULT_GOAL := help

.PHONY: install
install: ## Install dependencies
	poetry install --no-root

.PHONY: test
test: ## Run tests
	poetry run pytest

help: ## Show valid commands
	grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
