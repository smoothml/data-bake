.PHONY: create_environment sync_data_to_s3 sync_data_from_s3

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
BUCKET = {{ cookiecutter.s3_bucket }}
PROFILE = {{ cookiecutter.aws_profile }}
PROJECT_NAME = {{ cookiecutter.repo_name }}
PYTHON_INTERPRETER = {{ cookiecutter.python_interpreter }}

ifeq (,$(shell which pyenv))
	PYTHON_INTERPRETER_LOCATION=`which $(PYTHON_INTERPRETER)`
else
	PYTHON_INTERPRETER_LOCATION=`pyenv which $(PYTHON_INTERPRETER)`
endif

#################################################################################
# COMMANDS                                                                      #
#################################################################################

create_environment:
	@echo "Installing virtualenv if not already installed..."
	@pip install --user -q virtualenv
	@echo "Creating environment..."
	@virtualenv -p $(PYTHON_INTERPRETER_LOCATION) $(PROJECT_DIR)/venv
	@( \
		. $(PROJECT_DIR)/venv/bin/activate;\
		pip install -U pip setuptools wheel;\
		pip install -r $(PROJECT_DIR)/requirements.txt;\
	)

sync_data_to_s3:
	aws s3 sync $(PROJECT_DIR)/data/ s3://$(BUCKET)/data/ --exclude "*.DS_Store"
	aws s3 sync $(PROJECT_DIR)/models/ s3://$(BUCKET)/models/ --exclude "*.DS_Store"

sync_data_from_s3:
	aws s3 sync s3://$(BUCKET)/data/ $(PROJECT_DIR)/data/ --exclude "*.DS_Store"
	aws s3 sync s3://$(BUCKET)/models/ $(PROJECT_DIR)/models --exclude "*.DS_Store" 

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := show-help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: show-help
show-help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
