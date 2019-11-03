.PHONY: create_environment sync_data_to_s3 sync_data_from_s3

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
BUCKET = {{ cookiecutter.s3_bucket }}
PROFILE = {{ cookiecutter.aws_profile }}
PROJECT_NAME = {{ cookiecutter.repo_name }}
PYTHON_INTERPRETER = python3

ifeq (,$(shell which pyenv))
	HAS_PYENV=False
	PYTHON_INTERPRETER_LOCATION=`which $(PYTHON_INTERPRETER)`
else
	HAS_PYENV=True
	PYTHON_INTERPRETER_LOCATION=`pyenv which $(PYTHON_INTERPRETER)`
endif

ifeq (,$(shell which virtualenvwrapper.sh))
	HAS_VIRTUALENVWRAPPER=False
else
	HAS_VIRTUALENVWRAPPER=True
endif

#################################################################################
# COMMANDS                                                                      #
#################################################################################

create_environment: ## Create Python virtual environment and install dependencies.
ifeq (True,$(HAS_VIRTUALENVWRAPPER))
	@echo "Virtualenvwrapper detected..."
ifeq (True,$(HAS_PYENV))
	@source `pyenv which virtualenvwrapper.sh` && mkvirtualenv -a $(PROJECT_DIR) -r $(PROJECT_DIR)/requirements.txt -p $(PYTHON_INTERPRETER_LOCATION) $(PROJECT_NAME)
else
	@source `which virtualenvwrapper.sh` && mkvirtualenv -a $(PROJECT_DIR) -r $(PROJECT_DIR)/requirements.txt -p $(PYTHON_INTERPRETER_LOCATION) $(PROJECT_NAME)
endif
else
	@echo "Creating environment..."
	@$(PYTHON_INTERPRETER_LOCATION) -m venv $(PROJECT_DIR)/venv
	@( \
		. $(PROJECT_DIR)/venv/bin/activate;\
		pip install -U pip setuptools wheel;\
		pip install -r $(PROJECT_DIR)/requirements.txt;\
	)
endif

sync_data_to_s3: ## Sync data and models folders to S3. Will create bucket it doesn't already exist.
	if aws s3 ls "s3://$(BUCKET)" --profile $(PROFILE) 2>&1 | grep -q 'NoSuchBucket'; then aws s3 mb s3://$(BUCKET); fi
	aws s3 sync $(PROJECT_DIR)/data/ s3://$(BUCKET)/data/ --profile $(PROFILE) --exclude "*.DS_Store"
	aws s3 sync $(PROJECT_DIR)/models/ s3://$(BUCKET)/models/ --profile $(PROFILE) --exclude "*.DS_Store"

sync_data_from_s3: ## Sync data and models folders from S3.
	aws s3 sync s3://$(BUCKET)/data/ $(PROJECT_DIR)/data/ --profile $(PROFILE) --exclude "*.DS_Store"
	aws s3 sync s3://$(BUCKET)/models/ $(PROJECT_DIR)/models --profile $(PROFILE) --exclude "*.DS_Store" 

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

.PHONY: help

help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
