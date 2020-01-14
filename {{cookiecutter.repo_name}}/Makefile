.PHONY: create-environment clean lint

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = {{ cookiecutter.repo_name }}

#################################################################################
# COMMANDS                                                                      #
#################################################################################

create-environment: ## Create Python virtual environment and install dependencies.
	@echo "Creating environment..."
	@python -m venv $(PROJECT_DIR)/venv
	@( \
		. $(PROJECT_DIR)/venv/bin/activate;\
		pip install -U pip setuptools wheel;\
		pip install -r $(PROJECT_DIR)/requirements.txt;\
	)

clean: ## Clean environment.
	rm -rf $(PROJECT_DIR)/venv

lint: ## Lint source code.
	flake8 $(PROJECT_DIR)/src/{{ cookiecutter.package_name }}

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

.PHONY: help

help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
