.DEFAULT_GOAL := help

.PHONY: install
install: ## Install dependencies
	poetry install

.PHONY: test
test: ## Run tests
	poetry run pytest

.PHONY: isort
isort: ## Run isort formatting
	poetry run isort .

.PHONY: black
black: ## Run Black formatting
	poetry run black .

.PHONY: format
format: isort black ## Run formatting

.PHONY: quality
quality: ## Check code quality
	poetry run flake8 .

help: ## Show valid commands
	grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
