.PHONY: create_environment

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = {{ cookiecutter.repo_name }}

#################################################################################
# COMMANDS                                                                      #
#################################################################################

create_environment: ## Create Python virtual environment and install dependencies.
	@echo "Creating environment..."
	@python -m venv $(PROJECT_DIR)/venv
	@( \
		. $(PROJECT_DIR)/venv/bin/activate;\
		pip install -U pip setuptools wheel;\
		pip install -r $(PROJECT_DIR)/requirements.txt;\
	)

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

.PHONY: help

help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
